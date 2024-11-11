# https://data-puzzles.com/challenges/espresso-test/
# https://colab.research.google.com/drive/13r-UPXbMzSSvIsyUZCZ6fzqah7fbuWCr?usp=sharing


from scipy.stats import norm  # t-student?
import math

# Parameters
alpha = 0.10  # Significance level
beta = 0.20   # Type II error rate (1 - power)
p0 = 0.50     # Baseline success rate
mde = 0.25    # Minimum Detectable Effect (percentage points)

# Calculate z-scores for alpha and beta
z_alpha = norm.ppf(1 - alpha / 2)
z_beta = norm.ppf(1 - beta)

# Calculate p1 (success rate under the alternative hypothesis)
p1 = p0 + mde

# Compute the pooled standard deviation
pooled_sd = math.sqrt(2 * p0 * (1 - p0))

# Calculate the sample size per group
sample_size = ((z_alpha + z_beta) ** 2 * pooled_sd ** 2) / (mde ** 2)

# Total number of trials needed
total_trials = math.ceil(2 * sample_size)  # Multiply by 2 for both groups

print("Required number of trials:", total_trials)
