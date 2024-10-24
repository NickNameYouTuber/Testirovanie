import pytest
from main import get_json_from_file, add_json_to_file, save_json_to_file, sort_json

@pytest.fixture
def superhero_data():
    return get_json_from_file('SuperHero.json')

@pytest.fixture
def new_superheroes():
    return [
        {
            "name": "Superchel",
            "age": 32,
            "secretIdentity": "Cool chel",
            "powers": ["Super speed", "Super power"]
        },
        {
            "name": "XZ Kto",
            "age": 19,
            "secretIdentity": "Azizov Aziz",
            "powers": ["Super lazy"]
        }
    ]

@pytest.fixture
def initial_data():
    return {
        "squadName": "Super hero squad",
        "homeTown": "Metro City",
        "formed": 2016,
        "secretBase": "Super tower",
        "active": True,
        "members": [
            {
                "name": "Molecule Man",
                "age": 29,
                "secretIdentity": "Dan Jukes",
                "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]
            },
            {
                "name": "Madame Uppercut",
                "age": 39,
                "secretIdentity": "Jane Wilson",
                "powers": ["Million tonne punch", "Damage resistance", "Superhuman reflexes"]
            },
            {
                "name": "Eternal Flame",
                "age": 1000000,
                "secretIdentity": "Unknown",
                "powers": ["Immortality", "Heat Immunity", "Inferno", "Teleportation", "Interdimensional travel"]
            }
        ]
    }

def test_get_json(superhero_data):
    expected = {
        'squadName': 'Super hero squad',
        'homeTown': 'Metro City',
        'formed': 2016,
        'secretBase': 'Super tower',
        'active': True,
        'members': [
            {
                'name': 'Molecule Man',
                'age': 29,
                'secretIdentity': 'Dan Jukes',
                'powers': ['Radiation resistance', 'Turning tiny', 'Radiation blast']
            },
            {
                'name': 'Madame Uppercut',
                'age': 39,
                'secretIdentity': 'Jane Wilson',
                'powers': ['Million tonne punch', 'Damage resistance', 'Superhuman reflexes']
            },
            {
                'name': 'Eternal Flame',
                'age': 1000000,
                'secretIdentity': 'Unknown',
                'powers': ['Immortality', 'Heat Immunity', 'Inferno', 'Teleportation', 'Interdimensional travel']
            }
        ]
    }

    assert superhero_data == expected

def test_add_json(initial_data, new_superheroes):
    save_json_to_file(initial_data, "superhero_new.json")
    add_json_to_file("superhero_new.json", new_superheroes)
    actual = get_json_from_file("superhero_new.json")

    expected = {
        "squadName": "Super hero squad",
        "homeTown": "Metro City",
        "formed": 2016,
        "secretBase": "Super tower",
        "active": True,
        "members": [
            {
                "name": "Molecule Man",
                "age": 29,
                "secretIdentity": "Dan Jukes",
                "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]
            },
            {
                "name": "Madame Uppercut",
                "age": 39,
                "secretIdentity": "Jane Wilson",
                "powers": ["Million tonne punch", "Damage resistance", "Superhuman reflexes"]
            },
            {
                "name": "Eternal Flame",
                "age": 1000000,
                "secretIdentity": "Unknown",
                "powers": ["Immortality", "Heat Immunity", "Inferno", "Teleportation", "Interdimensional travel"]
            },
            {
                "name": "Superchel",
                "age": 32,
                "secretIdentity": "Cool chel",
                "powers": ["Super speed", "Super power"]
            },
            {
                "name": "XZ Kto",
                "age": 19,
                "secretIdentity": "Azizov Aziz",
                "powers": ["Super lazy"]
            }
        ]
    }

    assert actual == expected

def test_sort_json(initial_data, new_superheroes):
    save_json_to_file(initial_data, "superhero_new.json")
    add_json_to_file("superhero_new.json", new_superheroes)
    sort_json("superhero_new.json")
    actual = get_json_from_file("superhero_new.json")

    assert actual['members'][0]['age'] < actual['members'][1]['age']
    assert actual['members'][1]['age'] < actual['members'][2]['age']
    assert actual['members'][2]['age'] < actual['members'][3]['age']
    assert actual['members'][3]['age'] < actual['members'][5]['age'] # негативынй тест