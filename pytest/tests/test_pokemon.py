import requests
import pytest

host = 'https://pokemonbattle.me:9104'

def test_status_code():
    answer = requests.get(f'{host}/trainers', params= {'trainer_id' : 4605})
    answer.status_code == 200


def test_name_trainer():
    answer_name = requests.get(f'{host}/trainers', params= {'trainer_id' : '4605'})
    assert answer_name.json()['trainer_name'] == 'tata'