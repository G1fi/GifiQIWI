import json
from classes import *

wallets = 123

def load_wallets():
    with open('wallets_data.json', 'r', encoding='utf-8') as file:
        wallets_data = json.load(file)

    wallets = dict.fromkeys(wallets_data.keys())

    for wallet_name in wallets:
        Wallet(wallets_data[wallet_name])


def write_wallet(name: str, token: str):
    with open('wallets_data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        data[name] = token

    with open('wallets_data.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(data, indent=4))

