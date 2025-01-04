import pandas as pd

def test_pandas():
  df = pd.DataFrame(
    [
      [1, "Alice", 14],
      [2, "Bob", 23],
      [3, "Cypher", 45],
      [4, "David", 39],
    ],
    columns=["id", "name", "age"]
  )
  df = df.set_index("id")

  assert df.loc[1]["age"] == 14
  assert df.loc[2]["name"] == "Bob"

