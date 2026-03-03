import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

gdp = pd.read_csv(r'applied_data_science\Visualization\Project\GDP.csv', skiprows=3, index_col=0)

life = pd.read_csv(r'applied_data_science\Visualization\Project\Life_Expectancy.csv', skiprows=3, index_col=0)

US_gdp = gdp.loc["United States", "1960":"2023"].astype(float)
US_life = life.loc["United States", "1960":"2023"].astype(float)

df = pd.DataFrame({
    'GDP': US_gdp,
    'Life Expectancy': US_life
})

ax = df.plot(y='GDP', figsize=(10, 6), label='GDP', color='tab:blue')
df.plot(y='Life Expectancy', ax=ax, secondary_y=True, label='Life Expectancy', color='tab:red')

ax.set_xlabel('Year')
ax.set_ylabel('GDP (current US$)')
ax.right_ax.set_ylabel('Life Expectancy (years)')
plt.title('United States GDP and Life Expectancy (1960-2023)')
plt.show()
