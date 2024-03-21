# Hayashi-Yoshida correlation estimators

## The Hayashi-Yoshida estimator is a tool to approximate the correlation between two random variables which are measured at discrete times in a non-synchronous manner.

This repository translates the Hayashi-Yoshida estimator from a pure mathematical notation to Python code. It was first introduced in the paper:

Hayashi, Takaki, and Nakahiro Yoshida. "On covariance estimation of non-synchronously observed diffusion processes." Bernoulli 11.2 (2005): 359-379.

During their research, they wanted to find a way of comparing two diffusion processes when they are observed only at discrete times in a non-synchronous manner.
This can be extended to the analysis of highly resolved time series of random variables where there are instances of measurements without any values. 
An example can be financial time series. In Chapter 3.2 of the aforementioned paper, the exact mathematical derivation with the proof can be found.

## A case difference is made for known and unknown standard deviations of the two random variables.

This can be used when the supposed limits of the standard deviations are known and not diverging.


## Diffusive processes

In the original paper diffusive processes where used. Those can have have different realisations which is why I^i and J^j are not the same process. Thus when using the 
estimator with fixed data (like as stock time series) which only has one realization (the past performace) the random interval I^i = J^j.
