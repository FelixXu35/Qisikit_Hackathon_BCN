# Qisikit_Hackathon_BCN

### Black-Scholes mode

The Black-Scholes model is a mathematical model used to calculate the theoretical price of European-style options, which are financial derivatives that give the holder the right (but not the obligation) to buy or sell an underlying asset at a predetermined price and time[^1]. The model was developed by Fischer Black and Myron Scholes in the early 1970s[^2] and is widely used in finance to estimate the fair price of options.

The Black-Scholes differential equation is given by:
$$
\frac{∂C}{∂t} + \frac{1}{2} σ^2 S^2 \frac{∂^2C}{∂S^2} + rS \frac{∂C}{∂S} - rC = 0
$$
Where:

- $C$ is the price of the call option as a function of the underlying asset price $S$ and time $t$.
- $σ$ is the volatility of the underlying asset.
- $r$ is the risk-free interest rate.

The Black-Scholes model is based on several assumptions, including 

1. The underlying asset follows a log-normal distribution.
2. No dividends are paid during the life of the option.
3. No transaction costs or taxes.
4. The risk-free rate and volatility of the underlying asset are constant over the life of the option.
5. The option is European-style.

The formula for the Black-Scholes model takes into account several factors, including the current price of the underlying asset, the exercise price of the option, the time to expiration of the option, the risk-free rate of interest, and the volatility of the underlying asset. By inputting these factors into the formula, the model calculates the theoretical price of the option.

The Black-Scholes model has had a significant impact on the field of finance, and it is widely used by traders, investors, and academics. However, it has also been subject to criticism and limitations, including its assumptions and the fact that it may not accurately predict actual market prices.

### Methodology

###  Reference 

[^1]: Hull, J. C. (2018). Options, futures, and other derivatives. Pearson.
[^2]: Black, F., & Scholes, M. (1973). The pricing of options and corporate liabilities. Journal of Political Economy, 81(3), 637-654.

