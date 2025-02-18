import json
import pandas as pd
import matplotlib.pyplot as plt

# Načtení JSON dat
file_path = "data.json"  # Uprav cestu k souboru dle potřeby
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Transformace do DataFrame
years = list(data["dimension"]["as1001rs_rok"]["category"]["index"].keys())[::-1]
indicators = data["dimension"]["as1001rs_ukaz"]["category"]["label"]
gender_labels = data["dimension"]["as1001rs_poh"]["category"]["label"]

values = data["value"]

# Převod dat na tabulku
columns = ["Year", "Indicator", "Gender", "Value"]
df = pd.DataFrame(columns=columns)

index = 0
for year in years:
    for indicator_key, indicator_name in indicators.items():
        for gender_key, gender_name in gender_labels.items():
            df = pd.concat([
                df,
                pd.DataFrame([[int(year), indicator_name, gender_name, values[index]]], columns=columns)
            ], ignore_index=True)
            index += 1

# Převod sloupce Year na integer a hodnoty na float
df["Year"] = df["Year"].astype(int)
df["Value"] = df["Value"].astype(float)

# ---------------- 1. Vývoj populace podle pohlaví ----------------
plt.figure(figsize=(10, 5))

df_population = df[df["Indicator"] == "Počet obyvateľov k 31. 12."]
df_total = df_population[df_population["Gender"] == "spolu"]
df_men = df_population[df_population["Gender"] == "muži"]
df_women = df_population[df_population["Gender"] == "ženy"]

plt.plot(df_total["Year"], df_total["Value"], marker="o", label="Celkem")
plt.plot(df_men["Year"], df_men["Value"], marker="s", linestyle="dashed", label="Muži")
plt.plot(df_women["Year"], df_women["Value"], marker="^", linestyle="dotted", label="Ženy")

plt.xlabel("Rok")
plt.ylabel("Počet obyvatel")
plt.title("Vývoj populace Slovenska podle pohlaví (2018-2023)")
plt.legend()
plt.grid(True)
plt.show()

# ---------------- 2. Podíl obyvatel v produktivním věku ----------------
plt.figure(figsize=(10, 5))

df_productive_age = df[df["Indicator"] == "Podiel obyvateľov vo veku produktívnom (15 - 64 rokov), %"]
for gender in ["spolu", "muži", "ženy"]:
    df_subset = df_productive_age[df_productive_age["Gender"] == gender]
    plt.plot(df_subset["Year"], df_subset["Value"], marker="o", label=gender)

plt.xlabel("Rok")
plt.ylabel("Podíl (%)")
plt.title("Podíl obyvatel v produktivním věku (15-64 let) na Slovensku")
plt.legend()
plt.grid(True)
plt.show()

# ---------------- 3. Průměrný a mediánový věk obyvatel ----------------
plt.figure(figsize=(10, 5))

df_avg_age = df[df["Indicator"] == "Priemerný vek obyvateľov, roky"]
df_median_age = df[df["Indicator"] == "Mediánový vek obyvateľov, roky"]

plt.plot(df_avg_age[df_avg_age["Gender"] == "spolu"]["Year"], 
         df_avg_age[df_avg_age["Gender"] == "spolu"]["Value"], marker="o", label="Průměrný věk")
plt.plot(df_median_age[df_median_age["Gender"] == "spolu"]["Year"], 
         df_median_age[df_median_age["Gender"] == "spolu"]["Value"], marker="s", linestyle="dashed", label="Mediánový věk")

plt.xlabel("Rok")
plt.ylabel("Věk (roky)")
plt.title("Vývoj průměrného a mediánového věku obyvatelstva")
plt.legend()
plt.grid(True)
plt.show()

# ---------------- 4. Index ekonomické závislosti starších osob ----------------
plt.figure(figsize=(10, 5))

df_dependency_index = df[df["Indicator"] == "Index ekonomickej závislosti starých ľudí, %"]
for gender in ["spolu", "muži", "ženy"]:
    df_subset = df_dependency_index[df_dependency_index["Gender"] == gender]
    plt.plot(df_subset["Year"], df_subset["Value"], marker="o", label=gender)

plt.xlabel("Rok")
plt.ylabel("Index (%)")
plt.title("Index ekonomické závislosti starších osob")
plt.legend()
plt.grid(True)
plt.show()
