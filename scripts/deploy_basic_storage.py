
from brownie import  accounts, Basic_storage, config

# Basic_storage es el nombre del contrato inteligente y no del archivo .sol

def main():
    account = accounts.add(config["wallets"]["from_key"])
    deploy_details = {
        'from' : account
    }
    basic_storage_tx = Basic_storage.deploy(deploy_details)
    return basic_storage_tx

