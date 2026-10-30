from pyscript import document, when, window
from pyscript.ffi import create_proxy, is_none
import math
import json


shop = document.querySelector("#shop")
shop_buttons = {}

SAVE_KEY = 'potato_save'


BUILDINGS = [
    {
        "id": "click",
        "name": "Cursor",
        "base_cost": 10,
        "growth": 1.15,
        "cps": 0.1
    },
    {
        "id": 'minesweeper',
        "name": "Minesweeper",
        "base_cost": 100,
        "growth": 1.15,
        "cps": 1
    },
    {
        "id": 'tetris',
        "name": "Tetris",
        "base_cost": 1200,
        "growth": 1.15,
        "cps": 10
    },
    {
        "id": 'faceit',
        "name": "Faceit",
        "base_cost": 14500,
        "growth": 1.15,
        "cps": 100
    },
    {
        "id": 'basket',
        "name": "Basketball",
        "base_cost": 180000,
        "growth": 1.15,
        "cps": 1000
    },
    {
        "id": 'maksym',
        "name": "Maksym Parkhomenko",
        "base_cost": 2200000,
        "growth": 1.15,
        "cps": 10000
    }
]

STATE = {
    "cookies": 0.0,
    "buildings": {
        "click": 0,
        "minesweeper": 0,
        "tetris": 0,
        "faceit": 0,
        "basket": 0,
        "maksym": 0,
    },
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
    
    STATE['last_save'] = data.get('last_save', window.Date.now())
    
    saved_buildings = data.get('buildings', {})
    
    for building in BUILDINGS:
        STATE['buildings'][building['id']] = saved_buildings.get(building['id'], 0)
    


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
        button.querySelector(".b-rate").innerText = f"{building['cps']} per second"
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

def plus_cookie():
    STATE['cookies'] += 1
    render()
    
    
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


def cps():
    total = 0
    for i in BUILDINGS:
        owned = STATE['buildings'][i["id"]]
        total += i["cps"] * owned
    return total
    

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
render()
window.setInterval(create_proxy(tick), 10)
window.setInterval(create_proxy(save), 5000)
