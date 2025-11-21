# Configuration des projets PyCharm

# Test des DL GitHub



# Import pandas so we can manipulate data
import pandas as pd

# Import os to manipulate our environment
import os
cwd = os.getcwd()
print(cwd)

# (Look at how big a Python list is)


# Import an Excel file in Python
# If it doesn't work, do what the error says. Maybe it says to import openpyxl?
# openpyxl is another library that pandas needs to use to read Excel files
# Run python3 -m pip install openpyxl
df = pd.read_excel("../data/store_results/annual_sales_eu.xlsx")

# Check if it worked
print(df.head())

# Try again without considering the first line as a header
df = pd.read_excel("../data/store_results/annual_sales_eu.xlsx", header=None)

# Check if it worked
print(df.head())

# Transpose the table
df = df.transpose()
print(df.head())

# Try replacing missing values by the last valid value
df[0] = df[0].ffill()
print(df.head())

# Since it works let's do it on all 3 first columns
df.iloc[:, 0:3] = df.iloc[:, 0:3].ffill()




# Set column names equal to values in row index position 0
df.columns = df.iloc[0]

# Remove first row from DataFrame
df = df[1:]

# View updated DataFrame
print(df.head())

# Check what the columns are now
print(df.columns)

# Unpivot columns properly
# 1. Reset the index (ton transpose crée des index chelous)
df = df.reset_index(drop=True)

# 2. Nettoyer les colonnes : remplacer les nan par un nom propre
df.columns = [f"col_{i}" if pd.isna(c) else c for i, c in enumerate(df.columns)]

# 3. Identifier les colonnes à unpivot (ici les années)
year_columns = [c for c in df.columns if isinstance(c, (int, float))]

# 4. On garde toutes les colonnes non-numériques comme id_vars
id_vars = [c for c in df.columns if c not in year_columns]

# 5. Melt
df_long = df.melt(
    id_vars=id_vars,
    value_vars=year_columns,
    var_name="Year",
    value_name="Value"
)

print(df_long.head())

new_cols = {
    "col_0": "City",
    "col_1": "Street",
    "col_2": "Zip code",
    "col_3": "Product",
}

df_long = df_long.rename(columns=new_cols)
print(df_long)

# package into a function
import pandas as pd
import os
from pathlib import Path


def transform_sales_file(path: str) -> pd.DataFrame:
    """
    Read one 'annual_sales' Excel file, clean it and return it in long format:
    City, Street, Zip code, Product, Year, Value (+ SourceFile)
    """
    # 1. Lecture sans header
    df = pd.read_excel(path, header=None)

    # 2. Transpose
    df = df.transpose()

    # 3. Forward-fill des 3 premières colonnes (City, Street, Zip)
    df.iloc[:, 0:3] = df.iloc[:, 0:3].ffill()

    # 4. La première ligne devient l'en-tête
    df.columns = df.iloc[0]
    df = df[1:]  # on enlève la ligne d'en-tête

    # 5. Drop des colonnes complètement vides (au cas où)
    df = df.dropna(axis=1, how="all")

    # 6. Reset index
    df = df.reset_index(drop=True)

    # 7. Remplacement des noms de colonnes NaN par col_i
    df.columns = [f"col_{i}" if pd.isna(c) else c for i, c in enumerate(df.columns)]

    # 8. Colonnes d'années = colonnes dont le nom est numérique
    year_columns = [c for c in df.columns if isinstance(c, (int, float))]

    # 🔴 IMPORTANT : on force les id_vars, on ne prend pas toutes les non-numériques
    id_vars = ["col_0", "col_1", "col_2", "col_3"]

    # 9. Melt
    df_long = df.melt(
        id_vars=id_vars,
        value_vars=year_columns,
        var_name="Year",
        value_name="Value",
    )

    # 10. Year en int
    df_long["Year"] = df_long["Year"].astype(int)

    # 11. Rename des colonnes d’ID
    new_cols = {
        "col_0": "City",
        "col_1": "Street",
        "col_2": "Zip code",
        "col_3": "Product",
    }
    df_long = df_long.rename(columns=new_cols)

    # 12. Source du fichier (si tu veux la garder)
    df_long["SourceFile"] = os.path.basename(path)

    # 13. On ne garde que ce qui nous intéresse => plus de col_4 possible
    df_long = df_long[["City", "Street", "Zip code", "Product", "Year", "Value", "SourceFile"]]
    print(df_long["Value"].sum())
    print()

    return df_long

folder = Path("../data/store_results")
excel_files = list(folder.glob("*.xlsx"))

df_list = [transform_sales_file(f) for f in excel_files]
df_all = pd.concat(df_list, ignore_index=True)

print(df_all.head())
print(df_all.shape)
print(df_all["Value"].sum())
