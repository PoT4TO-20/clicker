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
    }
]

ACHIEVEMENTS = [
    {
        "id": 'clicks1',
        "name": 'First step on the potato field',
        "desc": 'Click once on the potato in this save',
        "icon": None,
        "kind": 'clicks',
        'target': None,
        'amount': 1 
    },
    {
        "id": 'cps1',
        "name": 'One extra every second',
        "desc": 'Gain 1 potato per second',
        "icon": None,
        "kind": 'cps',
        'target': None,
        'amount': 1 
    },
    {
        "id": 'potato1',
        "name": 'A small potato drawer',
        "desc": 'Get a total of 10 potatoes earned',
        "icon": None,
        "kind": 'earned',
        'target': None,
        'amount': 10
    },
    {
        "id": 'cursors1',
        "name": 'Another cursor??',
        "desc": 'Buy 1 Cursor building from the Shop',
        "icon": None,
        "kind": 'building',
        'target': 'click',
        'amount': 1 
    },
    {
        "id": 'sweeper1',
        "name": 'Explosive potatoes',
        "desc": 'Buy 1 Minesweeper building from the Shop',
        "icon": None,
        "kind": 'building',
        'target': 'minesweeper',
        'amount': 1 
    },
    {
        "id": 'tetris1',
        "name": 'Fit that potato',
        "desc": 'Buy 1 Tetris building from the Shop',
        "icon": None,
        "kind": 'building',
        'target': 'tetris',
        'amount': 1 
    },
    {
        "id": 'faceit1',
        "name": 'You better not miss a shot.',
        "desc": 'Buy 1 Faceit building from the Shop',
        "icon": None,
        "kind": 'building',
        'target': 'faceit',
        'amount': 1 
    },
    {
        "id": 'basket1',
        "name": 'Lay-up',
        "desc": 'Buy 1 Basketball building from the Shop',
        "icon": None,
        "kind": 'building',
        'target': 'basket',
        'amount': 1 
    },
    {
        "id": 'clicks2',
        "name": 'Getting a hang of it',
        "desc": 'Click 100 times on the potato in this save',
        "icon": None,
        "kind": 'clicks',
        'target': None,
        'amount': 100 
    },
    {
        "id": 'cps2',
        "name": 'A hundred per second?!',
        "desc": 'Gain 100 potato per second',
        "icon": None,
        "kind": 'cps',
        'target': None,
        'amount': 100
    },
    {
        "id": 'potato2',
        "name": 'A small potato shop',
        "desc": 'Get a total of 1000 potatoes earned',
        "icon": None,
        "kind": 'earned',
        'target': None,
        'amount': 1000
    },
    {
        "id": 'cursors2',
        "name": 'A whole band of cursors, nice',
        "desc": 'Buy 10 Cursor building from the Shop',
        "icon": None,
        "kind": 'building',
        'target': 'click',
        'amount': 10
    },
    {
        "id": 'sweeper2',
        "name": 'Are there this many?',
        "desc": 'Buy 10 Minesweeper building from the Shop',
        "icon": None,
        "kind": 'building',
        'target': 'minesweeper',
        'amount': 10 
    },
    {
        "id": 'tetris2',
        "name": 'Complete that line of potatoes',
        "desc": 'Buy 10 Tetris building from the Shop',
        "icon": None,
        "kind": 'building',
        'target': 'tetris',
        'amount': 10
    },
    {
        "id": 'faceit2',
        "name": 'Insta smoke is good',
        "desc": 'Buy 10 Faceit building from the Shop',
        "icon": None,
        "kind": 'building',
        'target': 'faceit',
        'amount': 10 
    },
    {
        "id": 'basket2',
        "name": 'A 2-pointer',
        "desc": 'Buy 10 Basketball building from the Shop',
        "icon": None,
        "kind": 'building',
        'target': 'basket',
        'amount': 10
    },
]

UPGRADES = [
    {
        "id": "tapper1",
        "name": "Tapper",
        "icon": None,
        "desc": "+100% to the amount of potatoes per click",
        "cost": 100,
        "kind": 'click',
        "target": None,
        "multi": 2,
        "requires": 10
    },
    {
        "id": "cursorer1",
        "name": "Better Aim",
        "icon": None,
        "desc": "+100% to the amount of potatoes per click by the 'Click' building",
        "cost": 100,
        "kind": 'building',
        "target": "click",
        "multi": 2,
        "requires": 1
    },
    {
        "id": "mine1",
        "name": "The '1' Block",
        "icon": None,
        "desc": "+100% to the amount of potatoes per click by the 'Minesweeper' building",
        "cost": 500,
        "kind": 'building',
        "target": "minesweeper",
        "multi": 2,
        "requires": 1
    },
    {
        "id": "tetris1",
        "name": "The T Shape",
        "icon": None,
        "desc": "+100% to the amount of potatoes per click by the 'Tetris' building",
        "cost": 6000,
        "kind": 'building',
        "target": "tetris",
        "multi": 2,
        "requires": 1
    },
    {
        "id": "tapper2",
        "name": "Fast Tapper",
        "icon": None,
        "desc": "+100% to the amount of potatoes per click",
        "cost": 500,
        "kind": 'click',
        "target": None,
        "multi": 2,
        "requires": 120
    },
    {
        "id": "cursorer2",
        "name": "Matvey's Aim",
        "icon": None,
        "desc": "+100% to the amount of potatoes per click by the 'Click' building",
        "cost": 500,
        "kind": 'building',
        "target": "click",
        "multi": 2,
        "requires": 13
    },
    {
        "id": "mine2",
        "name": "The '2' Block",
        "icon": None,
        "desc": "+100% to the amount of potatoes per click by the 'Minesweeper' building",
        "cost": 2000,
        "kind": 'building',
        "target": "minesweeper",
        "multi": 2,
        "requires": 20
    },
    {
        "id": "tetris2",
        "name": "The L Shape",
        "icon": None,
        "desc": "+100% to the amount of potatoes per click by the 'Tetris' building",
        "cost": 25000,
        "kind": 'building',
        "target": "tetris",
        "multi": 2,
        "requires": 10
    },
    {
        "id": "tapper3",
        "name": "Really Fast Tapper",
        "icon": None,
        "desc": "+100% to the amount of potatoes per click",
        "cost": 5000,
        "kind": 'click',
        "target": None,
        "multi": 2,
        "requires": 2000
    },
    {
        "id": "cursorer3",
        "name": "Anton's Aim",
        "icon": None,
        "desc": "+100% to the amount of potatoes per click",
        "cost": 2000,
        "kind": 'building',
        "target": "click",
        "multi": 2,
        "requires": 50
    },
    {
        "id": "mine3",
        "name": "The '3' Block",
        "icon": None,
        "desc": "+100% to the amount of potatoes per click by the 'Minesweeper' building",
        "cost": 7000,
        "kind": 'building',
        "target": "minesweeper",
        "multi": 2,
        "requires": 50
    },
    {
        "id": "tetris3",
        "name": "The J Shape",
        "icon": None,
        "desc": "+100% to the amount of potatoes per click by the 'Tetris' building",
        "cost": 86000,
        "kind": 'building',
        "target": "tetris",
        "multi": 2,
        "requires": 36
    },
    {
        "id": "tapper4",
        "name": "Brutal Tapper",
        "icon": None,
        "desc": "+200% to the amount of potatoes per click",
        "cost": 199999,
        "kind": 'click',
        "target": None,
        "multi": 4,
        "requires": 5600
    },
    {
        "id": "cursorer4",
        "name": "Maxim's Aim",
        "icon": None,
        "desc": "+200% to the amount of potatoes per click",
        "cost": 7000,
        "kind": 'building',
        "target": "click",
        "multi": 4,
        "requires": 100
    },
    {
        "id": "mine4",
        "name": "The '4' Block",
        "icon": None,
        "desc": "+200% to the amount of potatoes per click by the 'Minesweeper' building",
        "cost": 23000,
        "kind": 'building',
        "target": "minesweeper",
        "multi": 4,
        "requires": 100
    },
    {
        "id": "tetris4",
        "name": "The Z Shape",
        "icon": None,
        "desc": "+200% to the amount of potatoes per click by the 'Tetris' building",
        "cost": 250000,
        "kind": 'building',
        "target": "tetris",
        "multi": 4,
        "requires": 100
    },
    {
        "id": "tapper5",
        "name": "True Tapper",
        "icon": None,
        "desc": "+200% to the amount of potatoes per click",
        "cost": 500000,
        "kind": 'click',
        "target": None,
        "multi": 4,
        "requires": 9999
    },
    {
        "id": "cursorer5",
        "name": "Dima's Aim",
        "icon": None,
        "desc": "+200% to the amount of potatoes per click",
        "cost": 20000,
        "kind": 'building',
        "target": "click",
        "multi": 4,
        "requires": 333
    },
    {
        "id": "mine5",
        "name": "The '5' Block",
        "icon": None,
        "desc": "+200% to the amount of potatoes per click by the 'Minesweeper' building",
        "cost": 57000,
        "kind": 'building',
        "target": "minesweeper",
        "multi": 4,
        "requires": 250
    },
    {
        "id": "tetris5",
        "name": "The S Shape",
        "icon": None,
        "desc": "+200% to the amount of potatoes per click by the 'Tetris' building",
        "cost": 777777,
        "kind": 'building',
        "target": "tetris",
        "multi": 4,
        "requires": 223
    },
    {
        "id": "tapper6",
        "name": "Larp Tapper",
        "icon": None,
        "desc": "+400% to the amount of potatoes per click",
        "cost": 3000000,
        "kind": 'click',
        "target": None,
        "multi": 8,
        "requires": 25000
    },
    {
        "id": "cursorer6",
        "name": "David's Aim",
        "icon": None,
        "desc": "+400% to the amount of potatoes per click",
        "cost": 500000,
        "kind": 'building',
        "target": "click",
        "multi": 8,
        "requires": 500
    },
    {
        "id": "mine6",
        "name": "The '6' Block",
        "icon": None,
        "desc": "+400% to the amount of potatoes per click by the 'Minesweeper' building",
        "cost": 57000,
        "kind": 'building',
        "target": "minesweeper",
        "multi": 8,
        "requires": 666
    },
    {
        "id": "tetris6",
        "name": "The O Shape",
        "icon": None,
        "desc": "+400% to the amount of potatoes per click by the 'Tetris' building",
        "cost": 777777,
        "kind": 'building',
        "target": "tetris",
        "multi": 8,
        "requires": 443
    },
]