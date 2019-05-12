# uniform
from scipy.stats import uniform
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# binomial
from scipy.stats import binom
fig, ax = plt.subplots(1, 1)
# Calculate a few first moments:
n, p = 5, 0.4
mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')

# bournoulli
from scipy.stats import bernoulli
fig, ax = plt.subplots(1, 1)
# Calculate a few first moments:
p = 0.3
mean, var, skew, kurt = bernoulli.stats(p, moments='mvsk')

# poisson
from scipy.stats import poisson
fig, ax = plt.subplots(1, 1)

mu = 0.6
mean, var, skew, kurt = poisson.stats(mu, moments='mvsk')

# vonmises
from scipy.stats import vonmises
fig, ax = plt.subplots(1, 1)
# Calculate a few first moments:
kappa = 3.99
mean, var, skew, kurt = vonmises.stats(kappa, moments='mvsk')
