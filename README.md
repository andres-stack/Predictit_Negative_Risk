# Predictit_Negative_Risk
Calculate negative risk and buy contracts if negative risk exists.

Negative Risk is describes as a situation where your worst possible outcome in a market, when the market resolves, is a gain.
Predictit is a betting website that offers markets in which users buy up "yes" or "no" contracts. Once the market resolves only one yes contract in the market returns money while the rest of the no contracts return money.

In certain markets, if a user buys every single no contract in the market, the money gained from the all of the "no" contracts minus the money lost from "yes" contract is greater than the initial investment.

This program gathers market data every 25 seconds and calculates if any negative risk exists. Once negative risk exists, the "no" contracts of the market are purchased.



