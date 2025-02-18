import matplotlib.pyplot as plt
import numpy as np

# 1. Počet slovenských žen ve věku 20–30 let
total_women_sk = 2770000  # Celkový počet žen na Slovensku
women_20_30_ratio = 0.15  # Podíl žen ve věku 20–30 let

women_20_30_sk = total_women_sk * women_20_30_ratio
error_20_30_sk = women_20_30_sk * 0.10  # Odchylka ±10 %

# 2. Počet slovenských žen v ČR ve věku 20–30 let
total_women_cz_20_30 = 500000  
foreign_women_ratio = 0.036  
slovak_ratio_in_foreign = 0.5  

women_20_30_cz = total_women_cz_20_30 * foreign_women_ratio * slovak_ratio_in_foreign
error_20_30_cz = women_20_30_cz * 0.10  

# 3. Počet žen s gymnaziálním vzděláním
gymnasium_ratio = 0.10  

women_20_30_gym_sk = women_20_30_sk * gymnasium_ratio
women_20_30_gym_cz = women_20_30_cz * gymnasium_ratio
error_gym_sk = women_20_30_gym_sk * 0.10  
error_gym_cz = women_20_30_gym_cz * 0.10  

# 4. Počet žen, které jsou "průměrně pěkné"
attractive_ratio = 0.50  

women_20_30_gym_attractive_sk = women_20_30_gym_sk * attractive_ratio
women_20_30_gym_attractive_cz = women_20_30_gym_cz * attractive_ratio
error_attractive_sk = women_20_30_gym_attractive_sk * 0.10  
error_attractive_cz = women_20_30_gym_attractive_cz * 0.10  

# 5. Grafické znázornění s chybovými úsečkami
categories = ["Věk 20-30", "Gymnázium", "Atraktivní"]
values_sk = [women_20_30_sk, women_20_30_gym_sk, women_20_30_gym_attractive_sk]
values_cz = [women_20_30_cz, women_20_30_gym_cz, women_20_30_gym_attractive_cz]
errors_sk = [error_20_30_sk, error_gym_sk, error_attractive_sk]
errors_cz = [error_20_30_cz, error_gym_cz, error_attractive_cz]

# Nastavení šířky sloupců a pozic
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.4
x = np.arange(len(categories))

# Vykreslení sloupců pro SK a CZ vedle sebe
bars_sk = ax.bar(x - bar_width/2, values_sk, bar_width, yerr=errors_sk, label="Slovensko", alpha=0.8, color="blue", capsize=5)
bars_cz = ax.bar(x + bar_width/2, values_cz, bar_width, yerr=errors_cz, label="Česká republika", alpha=0.8, color="red", capsize=5)

# Přidání hodnot přímo do grafu
for bars, values in zip([bars_sk, bars_cz], [values_sk, values_cz]):
    for bar, value in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f"{int(value):,}", ha='center', va='bottom', fontsize=10, color="black")

# Nastavení popisků a vzhledu grafu
ax.set_xlabel("Kategorie")
ax.set_ylabel("Počet žen")
ax.set_title("Odhadovaný počet slovenských žen (věk 20-30 let, gymnázium, atraktivita)")
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
ax.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()




# Přesné hodnoty podle požadavku
women_20_30_sk = 415500
women_20_30_cz = 9000

women_20_30_gym_sk = 41550
women_20_30_gym_cz = 900

women_20_30_gym_attractive_sk = 20775
women_20_30_gym_attractive_cz = 450

# Nastavení odchylky (10 %)
error_20_30_sk = women_20_30_sk * 0.10
error_20_30_cz = women_20_30_cz * 0.10

error_gym_sk = women_20_30_gym_sk * 0.10
error_gym_cz = women_20_30_gym_cz * 0.10

error_attractive_sk = women_20_30_gym_attractive_sk * 0.10
error_attractive_cz = women_20_30_gym_attractive_cz * 0.10

# Kategorie a hodnoty
categories = ["Věk 20-30", "Gymnázium", "Atraktivní"]
values_sk = [women_20_30_sk, women_20_30_gym_sk, women_20_30_gym_attractive_sk]
values_cz = [women_20_30_cz, women_20_30_gym_cz, women_20_30_gym_attractive_cz]
errors_sk = [error_20_30_sk, error_gym_sk, error_attractive_sk]
errors_cz = [error_20_30_cz, error_gym_cz, error_attractive_cz]

# Vykreslení grafu
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.4
x = np.arange(len(categories))

bars_sk = ax.bar(x - bar_width/2, values_sk, bar_width, yerr=errors_sk, label="Slovensko", alpha=0.8, color="blue", capsize=5)
bars_cz = ax.bar(x + bar_width/2, values_cz, bar_width, yerr=errors_cz, label="Česká republika", alpha=0.8, color="red", capsize=5)

# Přidání přesných hodnot do grafu
for bars, values in zip([bars_sk, bars_cz], [values_sk, values_cz]):
    for bar, value in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f"{int(value):,}", ha='center', va='bottom', fontsize=10, color="black")

# Nastavení grafu
ax.set_xlabel("Kategorie")
ax.set_ylabel("Počet žen")
ax.set_title("Odhadovaný počet slovenských žen (věk 20-30 let, gymnázium, atraktivita)")
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
ax.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()
