import firstIteration.tokenSwap as ts
from solana.rpc.api import Client
from solana.rpc.api import Pubkey
from solana.rpc.types import TxOpts
from solana.rpc.types import TokenAccountOpts
from solders import keypair
def sell_token(tokenAddress):
    SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"  # Replace with your Solana RPC URL
    PRIVATE_KEY_BASE58 = "" # Replace with your private key
    FROM_TOKEN_MINT = Pubkey.from_string("So11111111111111111111111111111111111111112")  # SOL
    client = Client(SOLANA_RPC_URL)
    private_key = keypair.Keypair.from_base58_string(PRIVATE_KEY_BASE58)
    public_key = private_key.pubkey()
    mint_key = Pubkey.from_string(tokenAddress)
    # balance = get_altcoin_balance(client,owner_pubkey=public_key,altcoin_mint_address="6V4TgjgAmDHPSW4kgFjegnhHaSk4eBeydZdRxjNhpump")
    # print(balance)
    token_account = client.get_token_accounts_by_owner(public_key, TokenAccountOpts(mint=mint_key))
    token_account_pubkey = token_account.value[0].pubkey

    balance = client.get_token_account_balance(token_account_pubkey)
    # print(f"Token Account: {token_account}, Balance: {balance.value.ui_amount}")  # balance.value.amount
    # print(balance)
    quote = ts.get_jupiter_swap_quote(mint_key, FROM_TOKEN_MINT, balance.value.amount)
    ts.execute_jupiter_swap(PRIVATE_KEY_BASE58, quote)
    print("Swap complete for: ",tokenAddress)