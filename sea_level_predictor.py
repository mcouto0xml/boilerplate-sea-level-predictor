import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Ler os dados do arquivo
    df = pd.read_csv('epa-sea-level.csv')

    # Criar o gráfico de dispersão
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Criar a primeira linha de tendência (usando todos os dados)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    plt.plot(years_extended, intercept + slope * years_extended, color='red')

    # Criar a segunda linha de tendência (usando dados a partir de 2000)
    recent_df = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    
    # Plotar a segunda linha de tendência no mesmo intervalo de anos (2000-2050)
    years_recent = pd.Series(range(2000, 2051))
    plt.plot(years_recent, intercept_recent + slope_recent * years_recent, color='green')

    # Adicionar os rótulos e o título
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Salvar o gráfico e retornar
    plt.savefig('sea_level_plot.png')
    return plt.gca()
