#%%
# %load_ext autoreload
# %autoreload 2

import sys
sys.path.append('src/')

import driftpy
print(driftpy.__path__)

from driftpy.constants.config import configs
from anchorpy import Provider
import json 
from anchorpy import Wallet
from solana.rpc.async_api import AsyncClient
from driftpy.drift_client import DriftClient
from driftpy.accounts import get_user_account,get_perp_market_account
from solana.publickey import PublicKey
from dataclasses import asdict
from solana.keypair import Keypair
import asyncio

async def main():
    global summary_data

    with open('tmp.json', 'r') as f: 
        secret = json.load(f) 
    kp = Keypair.from_secret_key(bytes(secret))
    print('pk:', kp.public_key)

    config = configs['devnet']
    url = 'https://api.devnet.solana.com'
    wallet = Wallet(kp)
    connection = AsyncClient(url)
    provider = Provider(connection, wallet)
    dc = DriftClient.from_config(config, provider)

    settle_pk = PublicKey("CkZLqWuzgE985Y9RC6pt7LYvCUjN4HVXuJESt8yG7wW4")

    while True: 
        print('settling...')
        await dc.settle_lp(
            settle_pk, 
            0
        )
        user = await get_user_account(
            dc.program, 
            settle_pk,
        )
        market = await get_perp_market_account(
            dc.program, 0 
        )
        position = user.positions[0]
        print('position:', position)
        print('lp position:', market.amm.market_position_per_lp)

        summary_data.append(
            asdict(position)
        )

        await asyncio.sleep(10)
        print()

summary_data = []
try:
    asyncio.run(main())
finally:
    import pandas as pd 
    df = pd.DataFrame(summary_data)
    df.to_csv("examples/lp_summary_bot.csv", index=False)

#%%
#%%
#%%
# from driftpy.constants.numeric_constants import AMM_RESERVE_PRECISION
# n_tokens = 1_000 * AMM_RESERVE_PRECISION
# sig = await dc.add_liquidity(
#     n_tokens, 0
# )
# sig

# #%%
# import time 

#%%
#%%
# # %%
# pk = PublicKey("2zJhfetddV3J89zRrQ6o9W4KW2JbD6QYHjB7uT2VsgnG")
# drift_user = User(
#     dc, 
#     pk
# )

# %%
# %%
