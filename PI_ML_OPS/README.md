# Machine Learning Integrator Project

In this project we will follow the guidelines presented in the following repository: <https://github.com/soyHenry/PI_ML_OPS/tree/PT>.

## Step 1. Decompress Raw Data into .csv Files

The three raw data files given:

- steam_games.json.gz
- user_reviews.json.gz
- users_items.json.gz

were decompressed and converted into .csv files using the `openRawData.ipynb` notebook. Procedure, difficulties and solutions are detailed there.

The results:

- Data/df_items.csv
- Data/df_steam_games.csv
- Data/df_reviews.csv
- Data/df_user_items.csv

are saved in the `Data` folder and can be opened using Pandas.

Note that `df_items.csv` and `df_user_items.csv` contains almost the same data, however, the first one was obtained from `steam_games.json.gz` and the later was obtained from `users_items.json.gz`. This will be analyzed further on.

## Step 2. Transformations

In this step we clean, separate and imputate data. The three data files given:

- Data/df_items.csv
- Data/df_steam_games.csv
- Data/df_reviews.csv
- Data/df_user_items.csv

were analyzed and manipulated using the `transformationsData.ipynb` notebook. Procedure, difficulties and solutions are detailed there.

The results:

- TransformedData/df_userItems.csv
- TransformedData/ItemsData/itemsData_<steam_id>.csv
- TransformedData/df_userItems_R.csv
- TransformedData/df_reviews.csv
- TransformedData/ReviewsData/revData_<steam_id>.csv
- TransformedData/df_steamGames.csv

are saved in `TransformedData` folder and can be opened using Pandas.

## Step 3. Feature Engineering

In this step we assign a sentiment value to the reviews of the users. The data files given:

- TransformedData/df_reviews.csv
- TransformedData/ReviewsData/revData_<steam_id>.csv

were used in the `featureEng.ipynb` notebook. Procedure, difficulties and solutions are detailed there.

The results:

- FeatEngData/ReviewsData/revData_<steam_id>.csv

are saved in `FeatEngData` folder and can be opened using Pandas.

## Step 4. Data Creation

In this step we create important datasets that will later be used by the API Functions. The data files given:

- TransformedData/df_userItems.csv
- TransformedData/ItemsData/itemsData_<steam_id>.csv
- TransformedData/df_userItems_R.csv
- TransformedData/df_reviews.csv
- TransformedData/ReviewsData/revData_<steam_id>.csv
- TransformedData/df_steamGames.csv

were used in the `dataCreation.ipynb` notebook. Procedure, difficulties and solutions are detailed there.

The results:

- APIData/df_userItems.csv
- APIData/ItemsData/itemsData_<steam_id>.csv
- APIData/genresRank.csv
- APIData/GenresData/genreData_<genre>.csv
- APIData/df_steamGames.csv
- APIData/df_reviews.csv
- APIData/ReviewsData/revData_<steam_id>.csv
- APIData/df_reviews_r.csv
- APIData/df_inputs.csv

are saved in `APIData` folder and can be opened using Pandas.

## Step 5. Exploratory Data Analysis

In this step we use several techniques to explore the steam games data. The data files given:

- APIData/df_steamGames.csv

were used in the `eda.ipynb` notebook. Procedure, difficulties and solutions are detailed there.

## Step 6. Machine Learning Model

In this step we create the machine learning model to comply with desired functions. Datasets are also created to consume less memory in the API. The data files given:

- APIData/df_steamGames.csv
- APIData/df_userItems.csv
- APIData/ItemsData/itemsData_<steam_id>.csv

were used in the `mlModels.ipynb`. Procedure, difficulties and solutions are detailed there.

The results:

- APIData/MLData/df_cosineSim_gR.csv
- APIData/MLData/df_top5.csv

are saved in `APIData/MLData` folder and can be opened using Pandas.

## Step 7. Functions Creation
