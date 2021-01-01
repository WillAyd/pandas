import numpy as np
import pandas as pd

np.random.seed(123)


df = pd.DataFrame(
        {
            "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
            "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
            "C": np.random.randn(8),
            "D": np.arange(8),
        }
    )
rng = pd.date_range("2014", periods=len(df))
#df.index = rng
g = df.groupby(["A"])[["C"]]
g_exp = df[["C"]].groupby(df["A"])

res = g.describe()
exp = g_exp.describe()

