import pandas as pd
import math
import matplotlib.pyplot as plt
# Define range of n values
n_values = list(range(1, 50))  # Up to 20 to keep computations reasonable

# Assume each operation takes 0.25 nanosecond (2.5e-10 seconds), 4GHz processor
# Further assume that coefficient are 1 and constants are negligible
time_divisor = 2.5e-10  # 0.25 nanoseconds


# Define significant time markers in seconds
time_markers = {
    "Hummingbird wing flap": 0.015,  # 15 milliseconds
    "1 Second": 1,
    "1 Day": 86400,
    "1 Month": 30 * 86400,
    "1 Year": 365 * 86400,
    "1 Decade": 10 * 365 * 86400,
    "1 Century": 100 * 365 * 86400,
    "Death of the Sun": 4.5e9 * 365 * 86400,  # 4.5 billion years
    "Death of Milky Way": 10e26 * 365 * 86400,  # 2.5 trillion years
}

# Compute log, factorial, 2^n, and n^n for each n
logn_steps = [math.log(n) for n in n_values]
logn_times = [n * time_divisor for n in logn_steps]


factorials_steps = [math.factorial(n) for n in n_values]
factorial_times = [n * time_divisor for n in factorials_steps]

exponential_steps = [2**n for n in n_values]
exponential_times = [n * time_divisor for n in exponential_steps]

n_powers = [n**n for n in n_values]
n_power_times = [n * time_divisor for n in n_powers]

data = {
    "n": n_values,
    "log(n)": logn_steps,
    "log(n) Time (s)": logn_times,
    "n Time (s)": [n * time_divisor for n in n_values],
    "2^n": exponential_steps,
    "2^n Time (s)": exponential_times,
    "n! (factorial)": factorials_steps,
    "n! Time (s)":  factorial_times,
    "n^n": n_powers,
    "n^n Time (s)": n_power_times
}

# Create DataFrame
df = pd.DataFrame(data)

print(df)

# Plot different time complexities
plt.figure(figsize=(12, 6))

plt.plot(df["n"], df["log(n) Time (s)"], label="log(n) Time (s)", marker="o")
plt.plot(df["n"], df["n Time (s)"], label="n Time (s)", marker="s")
plt.plot(df["n"], df["2^n Time (s)"], label="2^n Time (s)", marker="^")
plt.plot(df["n"], df["n! Time (s)"], label="n! Time (s)", marker="x")
plt.plot(df["n"], df["n^n Time (s)"], label="n^n Time (s)", marker="d")


# Add horizontal lines for significant time markers
for label, value in time_markers.items():
    plt.axhline(y=value, color="grey", linestyle="--", linewidth=0.8)
    plt.text(df["n"].max(), value, label, verticalalignment="bottom", fontsize=10, color="black")

# Log scale for better visualization
plt.yscale("log")

# Labels and title
plt.xlabel("n")
plt.ylabel("Time (s)")
plt.title("Growth of Computational Complexity Over n")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

plt.show()
