# This script will eventually be used to create the Loyalty Token
from algosdk import account, mnemonic
from algosdk.v2client import algod

# Basic setup for Algorand Node
algod_address = "https://algonode.cloud"
algod_token = ""
algod_client = algod.AlgodClient(algod_token, algod_address)

print("Algorand Loyalty Token Script Initialized...")
