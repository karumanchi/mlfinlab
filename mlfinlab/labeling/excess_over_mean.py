"""
Return in excess of mean method.

Chapter 5.5, Machine Learning for Factor Investing, by Coqueret and Guida, (2020).
"""
import numpy as np


def excess_over_mean(prices, binary=False):
    """
    Return in excess of mean labelling method. Sourced from "The benefits of tree-based models for stock selection"
    Zhu et al. (2012).

    Returns a DataFrame containing returns of stocks over the mean of all stocks in the portfolio. Or in the case of
    binary classification, it returns a DataFrame of the signs of the returns. In this case, an observation may be
    labelled as 0 if it itself is the mean.

    :param prices: (pd.DataFrame) Close prices of all stocks in the market that are used to establish the mean.
                   Returns on each stock are then compared to the mean for the given timestamp.
    :param binary: (bool) If False, the numerical value of excess returns over mean will be given. If True, then only
                    the sign of the excess return over mean will be given (-1 or 1). A label of 0 will be given if
                    the observation itself equal to the mean.  Note: if there are any 0 labels (as a result of an
                    observation being exactly equal to the mean for a given time index).
    :return: (pd.DataFrame) Numerical returns in excess of the market mean return, or sign of return depending on
                whether binary is False or True respectively.
    """
    # Get return per period
    returns = prices.pct_change(periods=1).shift(-1)

    # Calculate mean returns for each period as market return
    market_return = returns.mean(axis=1)

    # Calculate excess over market (mean) return
    returns_over_mean = returns.sub(market_return, axis=0)

    # If binary is true, returns sign of the return over meam instead of the value
    if binary:
        return np.sign(returns_over_mean)

    return returns_over_mean
