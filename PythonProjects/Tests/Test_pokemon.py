import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = 'fc8db1cafc433d281111a5324fe627b0'

def test_status_code():
    answer = requests.get(f'{host}/trainers')

    assert  answer.status_code == 200


def test_response():
    answer_body = requests.get(f'{host}/trainers' , params = {'trainer_id' : 1524 })
    assert answer_body.json()['trainer_name'] == 'ruslan'
