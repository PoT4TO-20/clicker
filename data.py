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
        "cost": 1000,
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
        "cost": 5000,
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
        "cost": 12000,
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
        "cost": 300000,
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