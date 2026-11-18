from pyscript import document, when, window
from pyscript.ffi import create_proxy, is_none

import math
import time
import json

from data import BUILDINGS, UPGRADES, ACHIEVEMENTS


shop = document.querySelector("#shop")
shop_buttons = {}
upgrader = document.querySelector("#upgrades")
upgrader_buttons = {}
bought = document.querySelector("#bought")
bought_ups = {}
achievements = document.querySelector("#achievements")
achieved = {}

groups_ups = {}
ups_rows = {}

toasts = document.querySelector("#toasts")

status = document.querySelector("#shave-status")
pips_box = document.querySelector("#shave-pips")
pips = pips_box.querySelectorAll(".pip")
cookie_btn = document.querySelector("#cookie")

KIND_ORDER = ["clicks", "building", "cps", "earned"]

minute = 60 * 1000

COOLDOWN_MIN = 10 * minute
COOLDOWN_MAX = 20 * minute

BOOST_MIN = 1 * minute
BOOST_MAX = 2 * minute

SHAVE_STAGES = 7

last_shave = 0

SAVE_KEY = 'potato_save'


def fmt_time(ms):
    secs = int(ms / 1000)
    
    minutes = secs // 60
    left_secs = secs % 60
    
    return f"{minutes}:{left_secs:02d}"

    
def now_ms():
    return time.time() * 1000


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
    'achievements': [],
    'earned': 0.0,
    'click_earned': 0.0,
    'shave_stage': 0,
    'shave_ready_at': 0,
    'boost_until': 0,
    'boosts': 0,
    "last_save": now_ms(),
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
    
    STATE['last_save'] = data.get('last_save', now_ms())
    
    saved_buildings = data.get('buildings', {})
    
    for building in BUILDINGS:
        STATE['buildings'][building['id']] = saved_buildings.get(building['id'], 0)
        
    STATE['upgrades'] = data.get('upgrades', [])
    
    STATE['achievements'] = data.get('achievements', [])
    STATE['earned'] = data.get('earned', 0.0)
    STATE['click_earned'] = data.get('click_earned', 0.0)
    
    STATE['shave_stage'] = data.get('shave_stage', 0)
    STATE['shave_ready_at'] = data.get('shave_ready_at', 0)
    STATE['boost_until'] = data.get('boost_until', 0)
    
    STATE['boosts'] = data.get('boosts', 0)


def upgrade_multi(upgrade):
    if 'per' in upgrade:
        return 1 + upgrade['bonus'] * STATE['buildings'][upgrade["per"]]
    
    return upgrade['multi']


def random_between(a, b):
    return a + (b - a) * window.Math.random()
    
    
def boost_active():
    return now_ms() < STATE['boost_until']
    
    
def shave_ready():
    return now_ms() >= STATE['shave_ready_at'] and not boost_active()
    
    
def boost_mult():
    if boost_active():
        return 2
    return 1


def click_power():
    power = 1
    for upgrade in UPGRADES:
        if upgrade["kind"] == "click" and upgrade['id'] in STATE["upgrades"]:
            power *= upgrade_multi(upgrade)
            
    return power


def building_power(building):
    power = 1
    for upgrade in UPGRADES:
        if upgrade["kind"] == 'building' and upgrade['id'] in STATE['upgrades'] and upgrade['target'] == building["id"]:
            power *= upgrade_multi(upgrade)
            
    return power


def render():
    cookies = int(STATE['cookies'])
    document.querySelector("#count").innerText = f"{cookies} potatoes"
    
    rate = cps() * boost_mult()
    document.querySelector("#cps").innerText = f"potatoes per second: {rate:.1f}"
    
    for building in BUILDINGS:
        button = shop_buttons[building["id"]]
        owned = STATE['buildings'][building['id']]
        costs = cost(building)
        
        button.querySelector(".b-owned").innerText = f"Owned: {owned}"
        button.querySelector(".b-cost").innerText = f"{costs} potatoes"
        button.querySelector(".b-rate").innerText = f"{building['cps'] * building_power(building)} per second"
        button.disabled = STATE["cookies"] < costs
    
    for group in groups_ups.values():
        group.hidden = True
    
    for upgrade in UPGRADES:
        button = upgrader_buttons[upgrade["id"]]
        tile = bought_ups[upgrade['id']]
        costs = upgrade['cost']
        
        button.hidden = not is_unlocked(upgrade) or upgrade['id'] in STATE['upgrades']
        button.disabled = STATE["cookies"] < costs
        
        tile.hidden = not upgrade['id'] in STATE['upgrades']
        
        if upgrade['id'] in STATE['upgrades']:
            groups_ups[group_of(upgrade)].hidden = False
        
    document.querySelector("#bought-count").innerText = f"{len(STATE['upgrades'])} / {len(UPGRADES)}"
        
    document.querySelector("#stat-earned").innerText = f"{int(STATE['earned'])}"
    document.querySelector("#stat-clicks").innerText = f"{STATE['clicks']}"
    document.querySelector("#stat-click-earned").innerText = f"{int(STATE['click_earned'])}"
    document.querySelector("#stat-building-earned").innerText = f"{int(STATE['earned']) - int(STATE['click_earned'])}"
    document.querySelector('#stat-boosts').innerText = f"{STATE['boosts']}"
    document.querySelector('#stat-boosts-row').hidden = STATE['boosts'] == 0
    
    for achievement in ACHIEVEMENTS:
        tile = achieved[achievement['id']]
        icon = achievement.get('icon')
        name = achievement['name']
        desc = achievement['desc']
        
        if icon is None:
            icon = achievement['name'][0]
        
        if achievement['id'] in STATE['achievements']:
            tile.className = 'achievement'
            tile.querySelector(".a-icon").innerText = icon
            tile.querySelector(".a-name").innerText = name
            tile.querySelector(".a-desc").innerText = desc
        else:
            tile.className = 'achievement locked'
            tile.querySelector(".a-icon").innerText = '?'
            tile.querySelector(".a-name").innerText = '???'
            tile.querySelector(".a-desc").innerText = "???"
            
    document.querySelector("#ach-count").innerText = f"{len(STATE['achievements'])} / {len(ACHIEVEMENTS)}"
    
    now = now_ms()
    
    if boost_active():
        status.className = 'boost'
        status.innerText = f"2X Income Boost\n {fmt_time(STATE['boost_until'] - now)} left"
    else:
        status.className = ''
        status.innerText = ""
        
    pips_box.hidden = STATE['shave_stage'] == 0 or now_ms() - last_shave > 5000

    for i, pip in enumerate(pips):
        if i < STATE['shave_stage']:
            pip.className = 'pip done'
        else:
            pip.className = 'pip'
            
    document.body.classList.toggle("boosted", boost_active())
        
        
def tick():
    current = now_ms()
    seconds = (current - STATE['last_save']) / 1000
    STATE['last_save'] = current
    
    gained = cps() * seconds * boost_mult()
    
    STATE['cookies'] += gained
    STATE['earned'] += gained
    
    check_achievements()
    render()
    

def plus_cookie(event):
    gained = click_power() * boost_mult()
    STATE['cookies'] += gained 
    STATE['clicks'] += 1
    STATE['earned'] += gained 
    STATE['click_earned'] += gained 
    render()
    show_float(event.clientX, event.clientY, gained)
    
    
def cps():
    total = 0
    for i in BUILDINGS:
        owned = STATE['buildings'][i["id"]]
        total += i["cps"] * owned * building_power(i)
    return total
    

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
    for upgrade in sorted(UPGRADES, key=lambda u: u['cost']):
        button = document.createElement("button")
        button.className = 'upgrade'
        name = upgrade["name"]
        desc = upgrade['desc']
        icon = upgrade.get('icon')
        if icon is None:
            icon = name[0]
        
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


def build_bought():
    click = document.createElement("div")
    click.className = 'bought-group'
    
    click.innerHTML = """
        <h3>Clicks</h3>
        <div class="bought-row"></div>
    """
    
    bought.appendChild(click)
    groups_ups['clicks'] = click
    ups_rows['clicks'] = click.querySelector(".bought-row")
    
    for b in BUILDINGS:
        building = document.createElement("div")
        building.className = 'bought-group'
        
        building.innerHTML = f"""
            <h3>{b['name']}</h3>
            <div class="bought-row"></div>
        """
        
        bought.appendChild(building)
        groups_ups[b['id']] = building
        ups_rows[b['id']] = building.querySelector(".bought-row")
    
    for upgrade in UPGRADES:
        tile = document.createElement("div")
        tile.className = 'owned-up'
        icon = upgrade.get('icon')
        name = upgrade['name']
        desc = upgrade['desc']
        
        if icon is None:
            icon = name[0]
        
        tile.innerHTML = f"""
            <span class="a-icon">{icon}</span>
            <span class="a-info">
                <span class="a-name">{name}</span>
                <span class="a-desc">{desc}</span>
            </span>
        """
        
        ups_rows[group_of(upgrade)].appendChild(tile)
        bought_ups[upgrade['id']] = tile
        
        
def build_achievements():
    for a in sorted(ACHIEVEMENTS, key=lambda x: (KIND_ORDER.index(x['kind']), x['amount'])):
        achievement = document.createElement("div")
        achievement.className = 'achievement locked'
        
        achievement.innerHTML = f"""
            <span class="a-icon">?</span>
            <span class="a-info">
                <span class="a-name">???</span>
                <span class="a-desc">???</span>
            </span>
        """
        
        achievements.appendChild(achievement)
        achieved[a['id']] = achievement
        
        
def group_of(upgrade):
    if upgrade['kind'] == 'click':
        return 'clicks'
    else:
        return upgrade['target']
    
    
def is_achieved(achievement):
    if achievement['kind'] == 'clicks':
        if STATE['clicks'] >= achievement['amount']:
            return True
        
    if achievement['kind'] == 'cps':
        if cps() >= achievement['amount']:
            return True
        
    if achievement['kind'] == 'earned':
        if STATE['earned'] >= achievement['amount']:
            return True
        
    if achievement['kind'] == 'building':
        target = achievement['target']
        if STATE['buildings'][target] >= achievement['amount']:
            return True
        
    return False
    
    
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


def show_toast(achievement):
    toast = document.createElement("div")
    toast.className = 'toast'
    icon = achievement.get('icon')
    name = achievement['name']
    
    if icon is None:
        icon = name[0]
    
    toast.innerHTML = f"""
        <span class="t-icon">{icon}</span>
        <span class="t-text">
            <span class="t-title">Achievement unlocked</span>
            <span class="t-name">{name}</span>
        </span>
    """
    
    toasts.appendChild(toast)
    window.setTimeout(create_proxy(toast.remove), 4000)
    

def check_achievements():
    for achievement in ACHIEVEMENTS:
        if achievement['id'] in STATE['achievements']:
            continue
        
        if is_achieved(achievement):
            STATE['achievements'].append(achievement['id'])
            show_toast(achievement)


def show_float(x, y, amount):
    potato = document.createElement("span")
    potato.className = 'float-text'
    
    potato.innerText = f"+{amount:.1f}"
    potato.style.left = f"{x}px"
    potato.style.top = f"{y}px"
    
    document.body.appendChild(potato)
    window.setTimeout(create_proxy(potato.remove), 1000)
    
    
def drop_peels(x, y):
    for n in range(3):
        piece = document.createElement("span")
        piece.className = 'peel blob'

        piece.style.left = f"{x}px"
        piece.style.top = f"{y}px"

        piece.style.setProperty("--dx", f"{random_between(-60, 60)}px")
        piece.style.setProperty("--rot", f"{random_between(-270, 270)}deg")

        document.body.appendChild(piece)
        window.setTimeout(create_proxy(piece.remove), 1000)


@when("click", "#cookie")
def click_cookie(event):
    plus_cookie(event)
    
    
@when("contextmenu", "#cookie")
def right_click_cookie(event):
    global last_shave
    event.preventDefault()
    
    cookie_btn.classList.remove("shake")
    cookie_btn.offsetWidth
    cookie_btn.classList.add("shake")
    window.setTimeout(create_proxy(lambda: cookie_btn.classList.remove("shake")), 400)
    
    if not shave_ready():
        return
    
    if now_ms() - last_shave < 1000:
        return
    else:
        last_shave = now_ms()
    
    STATE['shave_stage'] += 1
    drop_peels(event.clientX, event.clientY)
    
    if STATE['shave_stage'] >= SHAVE_STAGES:
        now = now_ms()
        STATE['boost_until'] = now + random_between(BOOST_MIN, BOOST_MAX)
        STATE['shave_stage'] = 0
        STATE['shave_ready_at'] = STATE['boost_until'] + random_between(COOLDOWN_MIN, COOLDOWN_MAX)
        
        STATE['boosts'] += 1
        
    
    render()
    

@when("click", "#reset-yes")
def on_reset(event):
    window.localStorage.removeItem(SAVE_KEY)
    window.location.reload()
    

load()
build_shop()
build_upgrader()
build_bought()
build_achievements()
render()
window.setInterval(create_proxy(tick), 10)
window.setInterval(create_proxy(save), 5000)



#CHECKS

