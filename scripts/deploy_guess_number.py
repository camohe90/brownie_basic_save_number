
from brownie import Wei, accounts, Guess_number,config


def main():
    account = accounts.add(config["wallets"]["from_key"])
    deploy_details = {
        'from' : account,
        'value': Wei('0.1 ether')
    }
    guess_number_tx = Guess_number.deploy(9, deploy_details)
    return guess_number_tx

