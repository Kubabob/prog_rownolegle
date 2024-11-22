import matplotlib.pyplot as plt
import pandas as pd

timings = pd.read_csv(
    "pi_results.csv", names=["processes", "n_points", "pi", "time"]
)
plt.scatter(timings.loc[:, "processes"], timings.loc[:, "time"])
plt.show()
