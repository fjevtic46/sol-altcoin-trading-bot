import base64
import json
import requests
from solana.rpc.api import Client
from solana.rpc.api import Pubkey
from solana.rpc.api import VersionedTransaction
from solders import keypair
from solders import message
from solana.rpc.types import TxOpts
from solana.rpc.types import TokenAccountOpts
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Processed
from firstIteration import tokenSwap as tp


from solana.rpc.api import Client
from solders.pubkey import Pubkey
from spl.token.client import Token #Import the standalone function
# from spl.token.client import G
from spl.token.constants import TOKEN_PROGRAM_ID
from solders.keypair import Keypair
# from base58 import b58decode
import requests
import json
import time

# Configuration
SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"  # Replace with your Solana RPC URL
PRIVATE_KEY_BASE58 = "" # Replace with your private key in base58
FROM_TOKEN_MINT = Pubkey.from_string("So11111111111111111111111111111111111111112")  # SOL
TO_TOKEN_MINT = Pubkey.from_string("4ufd8JtAY1vMGPeAHAbNhztJoVgqSMiiK3EFpsmopump")  # Replace with the altcoin's mint address
AMOUNT_IN_SOL = 0.02  # Amount of SOL to swap

# Replace with your actual values
RPC_URL = "https://api.mainnet-beta.solana.com"  # Or your preferred RPC endpoint
# PRIVATE_KEY_BASE58 = "YOUR_PRIVATE_KEY_BASE58"
ALTCOIN_ADDRESS = "YOUR_ALTCOIN_MINT_ADDRESS" #The mint address of the altcoin, not your wallet address.
EXCHANGE_API_KEY = "YOUR_EXCHANGE_API_KEY"
EXCHANGE_API_SECRET = "YOUR_EXCHANGE_API_SECRET"
EXCHANGE_BASE_URL = "YOUR_EXCHANGE_API_URL" #example: "https://api.exampleexchange.com"
EXCHANGE_ALTCOIN_DEPOSIT_ADDRESS = "EXCHANGE_ALTCOIN_DEPOSIT_ADDRESS" #the exchange's deposit address for the altcoin
ALTCOIN_SYMBOL = "ALT" #example: "ABC"
SOL_SYMBOL = "SOL"

def get_altcoin_balance(client, owner_pubkey, altcoin_mint_address):
    """Gets the balance of an SPL token in a wallet."""
    token_mint_pubkey = Pubkey.from_string(altcoin_mint_address)
    token_account = Token.get_associated_token_address(owner_pubkey, token_mint_pubkey)

    try:
        response = client.get_token_account_balance(token_account)
        return float(response.value.amount) / (10 ** response.value.decimals) #important division here
    except Exception as e:
        print(f"Error getting altcoin balance: {e}")
        return 0
client = Client(SOLANA_RPC_URL)
private_key = keypair.Keypair.from_base58_string(PRIVATE_KEY_BASE58)
public_key = private_key.pubkey()
mint_key = Pubkey.from_string("fiYsJnMggjZ4zSyHLcFk4LdJB6xaWcQrTYxQ1btpump")
# balance = get_altcoin_balance(client,owner_pubkey=public_key,altcoin_mint_address="6V4TgjgAmDHPSW4kgFjegnhHaSk4eBeydZdRxjNhpump")
# print(balance)
token_account = client.get_token_accounts_by_owner(public_key, TokenAccountOpts(mint=mint_key))
token_account_pubkey = token_account.value[0].pubkey

balance = client.get_token_account_balance(token_account_pubkey)
print(f"Token Account: {token_account}, Balance: {balance.value.ui_amount}") # balance.value.amount
print(balance)
def get_jupiter_swap_quote(from_token_mint, to_token_mint, amount, slippage_bps=50):
    """Gets a swap quote from Jupiter."""
    url = f"https://api.jup.ag/swap/v1/quote?inputMint={from_token_mint}&outputMint={to_token_mint}&amount={amount}&slippageBps={slippage_bps}"
    response = requests.get(url)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    return response.json()
# quote = get_jupiter_swap_quote(mint_key,FROM_TOKEN_MINT,17628033230)
# print(quote)
# tp.execute_jupiter_swap(PRIVATE_KEY_BASE58,quote)
print(balance.value.amount)

