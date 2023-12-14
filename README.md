# LFGPy

<div align="center">
    <img src="https://i.ibb.co/grmRzsk/1-removebg-preview.png" width="30%" height="30%">
</div>

LFGPy is the Python client for the [LFG](https://lfg.exchange//) protocol. It allows you to trade and fetch data from Drift using Python.

**[Read the full SDK documentation here!](https://github.com/LFGexchangedex/app)**

## Installation

```
pip install lfgpy
```

Note: requires Python >= 3.10.

## ⚠️ IMPORTANT ⚠️

**PLEASE**, do not use QuickNode free RPCs to subscribe to the LFG Client.

If you are using QuickNode, you *must* use `AccountSubscriptionConfig("demo")`, and you can only subscribe to 1 perp market and 1 spot market at a time.

Non-QuickNode free RPCs (including the public mainnet-beta url) can use `cached` as well.

Example setup for `AccountSubscriptionConfig("demo")`: 

```
    # This example will listen to perp markets 0 & 1 and spot market 0
    # If you are listening to any perp markets, you must listen to spot market 0 or the SDK will break

    perp_markets = [0, 1]
    spot_market_oracle_infos, perp_market_oracle_infos, spot_market_indexes = get_markets_and_oracles(perp_markets = perp_markets)

    oracle_infos = spot_market_oracle_infos + perp_market_oracle_infos

    LFG_client = LFGClient(
        connection,
        wallet, 
        "mainnet",             
        perp_market_indexes = perp_markets,
        spot_market_indexes = spot_market_indexes,
        oracle_infos = oracle_infos,
        account_subscription = AccountSubscriptionConfig("demo"),
    )
    await LFG_client.subscribe()
```
If you intend to use `AccountSubscriptionConfig("demo)`, you *must* call `get_markets_and_oracles` to get the information you need.

`get_markets_and_oracles` will return all the necessary `OracleInfo`s and `market_indexes` in order to use the SDK.

## SDK Examples

- `examples/` folder includes more examples of how to use the SDK including how to provide liquidity/become an lp, stake in the insurance fund, etc.

## Setting Up Dev Env

`bash setup.sh`


## Building the docs

Local Docs: `mkdocs serve`

Updating public docs: `poetry run mkdocs gh-deploy --force`

## Releasing a new version of the package

- `python new_release.py`
- Create a new release at https://github.com/LFGexchangedex/app.
  - (The CI process will upload a new version of the package to PyPI.)

# Development

Ensure correct python version (using pyenv is recommended):
```
pyenv install 3.10.11
pyenv global 3.10.11
poetry env use $(pyenv which python)
```

Install dependencies:
```
poetry install
```

Run tests:
```
poetry run bash test.sh
```

Run Acceptance Tests
```
poetry run bash acceptance_test.sh
```