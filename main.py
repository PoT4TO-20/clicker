from pyscript import document, when, window
from pyscript.ffi import create_proxy, is_none

import math
import json

from data import BUILDINGS, UPGRADES


shop = document.querySelector("#shop")
shop_buttons = {}
upgrader = document.querySelector("#upgrades")
upgrader_buttons = {}

SAVE_KEY = 'potato_save'

STATE = {
    "cookies": 0.0,
    "clicks": 0,
    "buildings": {
        "click": 0,
        "minesweeper": 0,
        "tetris": 0,
        "faceit": 0,
        "basket": 0,
        "maksym": 0,
    },
    "upgrades": [],
    "last_save": window.Date.now(),
}


def save():
    text = json.dumps(STATE)
    window.localStorage.setItem(SAVE_KEY, text)
    
    
def load():
    text = window.localStorage.getItem(SAVE_KEY)
    if is_none(text):
        return
    
    data = json.loads(text)
    STATE['cookies'] = data.get('cookies', 0.0)
    STATE['clicks'] = data.get('clicks', 0)
    
    STATE['last_save'] = data.get('last_save', window.Date.now())
    
    saved_buildings = data.get('buildings', {})
    
    for building in BUILDINGS:
        STATE['buildings'][building['id']] = saved_buildings.get(building['id'], 0)
        
    STATE['upgrades'] = data.get('upgrades', [])
    
    

def click_power():
    power = 1
    for upgrade in UPGRADES:
        if upgrade["kind"] == "click" and upgrade['id'] in STATE["upgrades"]:
            power *= upgrade["multi"]
            
    return power


def building_power(building):
    power = 1
    for upgrade in UPGRADES:
        if upgrade["kind"] == 'building' and upgrade['id'] in STATE['upgrades'] and upgrade['target'] == building["id"]:
            power *= upgrade["multi"]
            
    return power


def render():
    cookies = int(STATE['cookies'])
    document.querySelector("#count").innerText = f"{cookies} potatoes"
    
    rate = cps()
    document.querySelector("#cps").innerText = f"potatoes per second: {rate:.1f}"
    
    for building in BUILDINGS:
        button = shop_buttons[building["id"]]
        owned = STATE['buildings'][building['id']]
        costs = cost(building)
        
        button.querySelector(".b-owned").innerText = f"Owned: {owned}"
        button.querySelector(".b-cost").innerText = f"{costs} potatoes"
        button.querySelector(".b-rate").innerText = f"{building['cps'] * building_power(building)} per second"
        button.disabled = STATE["cookies"] < costs
        
    for upgrade in UPGRADES:
        button = upgrader_buttons[upgrade["id"]]
        costs = upgrade['cost']
        
        button.hidden = not is_unlocked(upgrade) or upgrade['id'] in STATE['upgrades']
        button.disabled = STATE["cookies"] < costs
        
        
def tick():
    current = window.Date.now()
    seconds = (current - STATE['last_save']) / 1000
    STATE['last_save'] = current
    
    STATE['cookies'] += cps() * seconds
    render()
    

def build_shop():
    for building in BUILDINGS:
        button = document.createElement("button")
        button.className = 'building'
        name = building["name"]
        owned = STATE['buildings'][building["id"]]
        
        button.innerHTML = f"""
            <span class="b-name">{name}</span>
            <span class="b-owned">{owned}</span>
            <span class="b-cost">{cost(building)}</span>
            <span class="b-rate"></span>
        """
        
        button.onclick = create_proxy(lambda event, i = building: buy(i))
        
        shop.appendChild(button)
        shop_buttons[building["id"]] = button
        
        
def build_upgrader():
    for upgrade in UPGRADES:
        button = document.createElement("button")
        button.className = 'upgrade'
        name = upgrade["name"]
        desc = upgrade['desc']
        icon = upgrade.get('icon')
        if icon is None:
            icon = upgrade['name']
        
        button.innerHTML = f"""
            <span class="u-icon">{icon}</span>
            <span class="u-info">
                <span class="u-name">{name}</span>
                <span class="u-desc">{desc}</span>
                <span class="u-cost">{upgrade['cost']}</span>
            </span>
        """
        
        button.onclick = create_proxy(lambda event, i = upgrade: buy_upgrade(i))
        
        upgrader.appendChild(button)
        upgrader_buttons[upgrade["id"]] = button


def plus_cookie():
    STATE['cookies'] += click_power()
    STATE['clicks'] += 1
    render()
    
    
def cps():
    total = 0
    for i in BUILDINGS:
        owned = STATE['buildings'][i["id"]]
        total += i["cps"] * owned * building_power(i)
    return total
    
    
def cost(building):
    owned = STATE['buildings'][building["id"]]
    price = building["base_cost"] * building["growth"] ** owned
    return math.ceil(round(price, 6))


def buy(building):
    costs = cost(building)
    if STATE['cookies'] >= costs:
        STATE['cookies'] -= costs
        STATE['buildings'][building["id"]] += 1
        render()
    return    


def is_unlocked(upgrade):
    if upgrade['kind'] == 'click':
        if STATE['clicks'] >= upgrade['requires']:
            return True
        
    if upgrade['kind'] == 'building':
        target = upgrade['target']
        if STATE['buildings'][target] >= upgrade['requires']:
            return True
        
    return False


def buy_upgrade(upgrade):
    if upgrade['id'] in STATE['upgrades']:
        return
    
    if STATE['cookies'] >= upgrade['cost']:
        STATE['cookies'] -= upgrade['cost']
        STATE['upgrades'].append(upgrade['id'])
        render()



@when("click", "#cookie")
def click_cookie(event):
    plus_cookie()
    
    
@when("contextmenu", "#cookie")
def right_click_cookie(event):
    event.preventDefault()
    

@when("click", "#reset")
def on_reset(event):
    answer = window.confirm("Reset everything?")
    if not answer:
        return
    
    window.localStorage.removeItem(SAVE_KEY)
    window.location.reload()
    

load()
build_shop()
build_upgrader()
render()
window.setInterval(create_proxy(tick), 10)
window.setInterval(create_proxy(save), 5000)



#CHECKS
