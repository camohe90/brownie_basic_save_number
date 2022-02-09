
from brownie import Contract

def main():
    guess_number_contract = Contract('0x744359d5D5e43e4d7975da6394C30AACb963fb45')
    guess_number_tx = guess_number_contract.getBalance()
    print(guess_number_tx)

