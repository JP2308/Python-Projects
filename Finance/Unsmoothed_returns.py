# test of unsmoothed returns

import numpy as np
import matplotlib.pyplot as plt

def estimate_autocorrelation(returns):
    """Estimates the first-order autocorrelation coefficient (ρ)."""
    return np.corrcoef(returns[:-1], returns[1:])[0, 1]

def unsmooth_returns(appraisal_returns):
    """Applies Geltner's unsmoothing formula to appraisal-based returns."""
    # Step 1: Estimate the autocorrelation (ρ)
    rho = estimate_autocorrelation(appraisal_returns)
    print(f"Estimated autocorrelation (ρ): {rho:.4f}")

    # Step 2: Apply Geltner's unsmoothing formula
    unsmoothed = []
    for t in range(1, len(appraisal_returns)):
        unsmoothed_return = (appraisal_returns[t] - rho * appraisal_returns[t - 1]) / (1 - rho)
        unsmoothed.append(unsmoothed_return)

    return np.array(unsmoothed)

# Example: Quarterly appraisal-based returns (in %)
appraisal_returns = np.array([17.33, 7.33, 4.24, 14.59, 13.05])

# Step 3: Calculate unsmoothed returns
unsmoothed_returns = unsmooth_returns(appraisal_returns)

print("Appraisal-based returns:", appraisal_returns)
print("Unsmoothed returns:", unsmoothed_returns)

# Step 4: Visualize the results
plt.figure(figsize=(8, 5))
plt.plot(appraisal_returns, label='Appraisal-Based Returns', marker='o')
plt.plot(np.arange(1, len(appraisal_returns)), unsmoothed_returns, label='Unsmoothed Returns', marker='x')
plt.title('Appraisal-Based vs. Unsmoothed Returns')
plt.xlabel('Time Periods')
plt.ylabel('Returns (%)')
plt.legend()
plt.grid(True)
plt.show()
