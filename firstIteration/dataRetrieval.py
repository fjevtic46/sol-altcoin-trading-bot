import requests
import time

def get_latest_tokens_dexscreener():
    """Fetches real-time latest tokens from Dex Screener"""
    url = "https://api.dexscreener.com/token-profiles/latest/v1"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
def get_latest_boosted_tokens_dexscreener():
    """Fetches real time boosted tokens from DexScreener"""
    url = "https://api.dexscreener.com/token-boosts/latest/v1"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
def get_latest_boosted_tokens_dexscreener():
    """Fetches real time boosted tokens from DexScreener"""
    url = "https://api.dexscreener.com/token-boosts/top/v1"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
def get_data_jupiter():
    pass
def get_data_raydium():
    pass