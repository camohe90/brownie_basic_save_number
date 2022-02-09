
from brownie import Contract, config, accounts, network, Wei

def main():
    account = accounts.add(config["wallets"]["from_key"])
    guess_number_contract = Contract('0x744359d5D5e43e4d7975da6394C30AACb963fb45')
    # guess_number_contract = Guess_number[-1]
    deploy_details = {
        'from' : account,
        'value': Wei('0.1 ether')
    }
    guess_number_tx = guess_number_contract.play(2, account.address, deploy_details)
    return guess_number_tx

