
from brownie import Contract

def main():
    basic_storage = Contract('0x104ea61A2642d0667c607E76eC4faE7F8E5D016B')
    basic_storage_tx = basic_storage.readNumber()
    print(basic_storage_tx)

