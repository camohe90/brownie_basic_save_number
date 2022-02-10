
from brownie import Contract, config, accounts, network, Wei

def main():
    account = accounts.add(config["wallets"]["from_key"])
    basic_storage = Contract('0x104ea61A2642d0667c607E76eC4faE7F8E5D016B')
    signer_details = {
        'from' : account
    }
    guess_number_tx = basic_storage.saveNumber(2, signer_details)
    return guess_number_tx

