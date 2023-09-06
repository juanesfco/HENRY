# Machine Learning Integrator Project

In this project we will follow the guidelines presented in the following repository: <https://github.com/soyHenry/PI_ML_OPS/tree/PT>.

## Step 1. Decompress Raw Data into .csv Files

The three raw data files given:

- steam_games.json.gz
- user_reviews.json.gz
- users_items.json.gz

were decompressed and converted into .csv files using the `openRawData.ipynb` notebook. Procedure, difficulties and solutions are detailed there.

The results:

- df_items.csv
- df_steam_games.csv
- df_reviews.csv
- df_user_items.csv

can be opened using Pandas.

Note that `df_items.csv` and `df_user_items.csv` contains almost the same data, however, the first one was obtained from `steam_games.json.gz` and the later was obtained from `users_items.json.gz`. This will be analyzed further on.

## Step 2. Transformations

In this step we eliminate unnecesary data.
