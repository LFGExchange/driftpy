# PRECISIONS
AMM_RESERVE_PRECISION = 1_000_000_000
BASE_PRECISION = AMM_RESERVE_PRECISION
PRICE_PRECISION = 1_000_000
PEG_PRECISION = 1_000_000
QUOTE_PRECISION = 1_000_000
FUNDING_RATE_BUFFER = 1_000
MARGIN_PRECISION = 10_000
BID_ASK_SPREAD_PRECISION = 1_000_000
TEN_BPS = BID_ASK_SPREAD_PRECISION
PERP_DECIMALS = 9
CONCENTRATION_PRECISION = 1_000_000
IF_FACTOR_PRECISION = 1_000_000

SPOT_BALANCE_PRECISION = 1_000_000_000
SPOT_CUMULATIVE_INTEREST_PRECISION = 10_000_000_000
SPOT_UTILIZATION_PRECISION = 1_000_000
SPOT_RATE_PRECISION = 1_000_000
LIQUIDATION_FEE_PRECISION = 1_000_000
SPOT_WEIGHT_PRECISION = MARGIN_PRECISION
SPOT_IMF_PRECISION = 1_000_000
FUNDING_RATE_PRECISION = PRICE_PRECISION * FUNDING_RATE_BUFFER

# PRECISION CONVERSIONS
PRICE_TO_PEG_PRECISION_RATIO = PRICE_PRECISION / PEG_PRECISION
AMM_TO_QUOTE_PRECISION_RATIO = AMM_RESERVE_PRECISION / QUOTE_PRECISION
AMM_TIMES_PEG_TO_QUOTE_PRECISION_RATIO = (
    AMM_RESERVE_PRECISION * PEG_PRECISION / QUOTE_PRECISION
)
QUOTE_TO_BASE_AMT_FUNDING_PRECISION = (
    AMM_RESERVE_PRECISION * FUNDING_RATE_PRECISION / QUOTE_PRECISION
)
PRICE_TO_QUOTE_PRECISION_RATIO = PRICE_PRECISION / QUOTE_PRECISION
PRICE_TIMES_AMM_TO_QUOTE_PRECISION_RATIO = (
    PRICE_PRECISION * AMM_TO_QUOTE_PRECISION_RATIO
)
LIQUIDATION_FEE_TO_MARGIN_PRECISION_RATIO = LIQUIDATION_FEE_PRECISION / MARGIN_PRECISION
FUNDING_RATE_TO_QUOTE_PRECISION_PRECISION_RATIO = (
    FUNDING_RATE_PRECISION / QUOTE_PRECISION
)
FUNDING_RATE_PRECISION = PRICE_PRECISION * FUNDING_RATE_BUFFER
PRICE_DIV_PEG = PRICE_PRECISION / PEG_PRECISION

# FEE REBATES
SHARE_OF_FEES_ALLOCATED_TO_CLEARING_HOUSE_NUMERATOR = 1
SHARE_OF_FEES_ALLOCATED_TO_CLEARING_HOUSE_DENOMINATOR = 2

SHARE_OF_IF_ESCROW_ALLOCATED_TO_PROTOCOL_NUMERATOR = 1
SHARE_OF_IF_ESCROW_ALLOCATED_TO_PROTOCOL_DENOMINATOR = 2

SHARE_OF_REVENUE_ALLOCATED_TO_INSURANCE_FUND_VAULT_NUMERATOR = 1
SHARE_OF_REVENUE_ALLOCATED_TO_INSURANCE_FUND_VAULT_DENOMINATOR = 1

MAX_APR_PER_REVENUE_SETTLE_TO_INSURANCE_FUND_VAULT = 1000
MAX_APR_PER_REVENUE_SETTLE_PRECISION = 10
UPDATE_K_ALLOWED_PRICE_CHANGE = PRICE_PRECISION / 10_000

# TIME PERIODS
ONE_HOUR = 3600
ONE_HOUR_I128 = ONE_HOUR
TWENTY_FOUR_HOUR = 3600 * 24
ONE_YEAR = 31536000
EPOCH_DURATION = TWENTY_FOUR_HOUR * 28

# FEES
ONE_BPS_DENOMINATOR = 10000
ONE_HUNDRED_MILLION_QUOTE = 100_000_000 * QUOTE_PRECISION
FIFTY_MILLION_QUOTE = 50_000_000 * QUOTE_PRECISION
TEN_MILLION_QUOTE = 10_000_000 * QUOTE_PRECISION
FIVE_MILLION_QUOTE = 10_000_000 * QUOTE_PRECISION
ONE_MILLION_QUOTE = 1_000_000 * QUOTE_PRECISION
TWO_HUNDRED_FIFTY_THOUSAND_QUOTE = 250_000 * QUOTE_PRECISION
ONE_HUNDRED_THOUSAND_QUOTE = 100_000 * QUOTE_PRECISION
TWENTY_FIVE_THOUSAND_QUOTE = 25_000 * QUOTE_PRECISION
TEN_THOUSAND_QUOTE = 10_000 * QUOTE_PRECISION
ONE_THOUSAND_QUOTE = 1_000 * QUOTE_PRECISION
MAX_REFERRER_REWARD_EPOCH_UPPER_BOUND = 4000 * QUOTE_PRECISION
LP_FEE_SLICE_NUMERATOR = 8
LP_FEE_SLICE_DENOMINATOR = 10
FEE_DENOMINATOR = 10 * ONE_BPS_DENOMINATOR
FEE_PERCENTAGE_DENOMINATOR = 100

# CONSTRAINTS
MAX_CONCENTRATION_COEFFICIENT = 1_414_200
MAX_LIQUIDATION_SLIPPAGE = 10_000
MAX_LIQUIDATION_SLIPPAGE_U128 = 10_000
MAX_MARK_TWAP_DIVERGENCE = 500_000
MAXIMUM_MARGIN_RATIO = MARGIN_PRECISION
MINIMUM_MARGIN_RATIO = MARGIN_PRECISION / 50
DEFAULT_LARGE_BID_ASK_FACTOR = 10 * BID_ASK_SPREAD_PRECISION
MAX_BID_ASK_INVENTORY_SKEW_FACTOR = 10 * BID_ASK_SPREAD_PRECISION

# FORMULAIC REPEG / K
K_BPS_UPDATE_SCALE = 1_000_000
K_BPS_DECREASE_MAX = 22000
K_BPS_INCREASE_MAX = 1000

PEG_BPS_UPDATE_SCALE = 1_000_000
PEG_BPS_DECREASE_MAX = 1000
PEG_BPS_INCREASE_MAX = 1000

QUOTE_SPOT_MARKET_INDEX = 0