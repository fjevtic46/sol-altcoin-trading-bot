import firstIteration.dataRetrieval as dr
import firstIteration.dataFilter as df
import firstIteration.tokenSwap as ts
import firstIteration.tokenSell as tsell
import time
token_list = dr.get_latest_boosted_tokens_dexscreener()
valid_tokens = df.filter_dexscreener_data(token_list)
valid_token_dict = dict()
print("Num Valid Tokens:",len(valid_tokens))
print("Valid Tokens:",valid_tokens)
for token in valid_tokens:
    if token[0]['tokenAddress'] not in valid_token_dict:
        valid_token_dict[token[0]['tokenAddress']] = dict()
        tokenData = df.get_pricehistory_dexscreener(token[0]['tokenAddress'])[0]
        valid_token_dict[token[0]['tokenAddress']]['priceNative'] = float(tokenData['priceNative'])
        valid_token_dict[token[0]['tokenAddress']]['m5_buys'] = tokenData['txns']['m5']['buys']
        valid_token_dict[token[0]['tokenAddress']]['m5_buysell_ratio'] = tokenData['txns']['m5']['buys'] / tokenData['txns']['m5']['sells']
        valid_token_dict[token[0]['tokenAddress']]['m5_volume'] = tokenData['volume']['m5']
        valid_token_dict[token[0]['tokenAddress']]['m5_priceChange'] = tokenData['priceChange']

        ts.purchase_token(token[0]['tokenAddress'])
print(valid_token_dict.keys())
while(len(valid_token_dict) > 0):
    sold_tokens = []
    for tokenAddress,tokenMetadata in valid_token_dict.items():
        tokenLiveData = df.get_pricehistory_dexscreener(tokenAddress)[0]
        condition_count = 0
        if (tokenMetadata['priceNative'] * 0.92) <= float(tokenLiveData['priceNative']):
            condition_count += 1
            # valid_token_dict[tokenAddress]['priceNative'] = float(tokenLiveData['priceNative'])
        if tokenMetadata['m5_buys'] <= tokenLiveData['txns']['m5']['buys']:
            condition_count += 1
            # valid_token_dict[tokenAddress]['m5_buys'] = tokenLiveData['txns']['m5']['buys']
        if tokenMetadata['m5_buysell_ratio'] <= tokenLiveData['txns']['m5']['buys'] / tokenLiveData['txns']['m5']['sells']:
            condition_count += 1
        if tokenMetadata['m5_volume'] <= tokenLiveData['volume']['m5']:
            condition_count += 1
            # valid_token_dict[tokenAddress]['m5_volume'] = tokenLiveData['2volume']['m5']
        if condition_count == 0:
            tsell.sell_token(tokenAddress)
            sold_tokens.append(tokenAddress)
        time.sleep(1)
    for token in sold_tokens:
        del valid_token_dict[token]
    print(valid_token_dict.keys())
print("Complete")
    # save price native
    # purchase
    # print(tokenData)
    # print(token[0]['tokenAddress'],token[1])
# print("Total number of valid tokens:",len(valid_tokens))
# print("Total number of tokens: ",len(token_list))
# # 'priceNative': '0.0000002281'

#monitor
