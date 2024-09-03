# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import imageio

# Read the whole datasets (you need to provide the related file path where your files saved)
pop = pd.read_csv('data/pop.csv')
lex = pd.read_csv('data/lex.csv')
fer = pd.read_csv('data/total_fertility.csv')
continent = pd.read_csv('data/continents.csv', sep= ';')

# Determine the start and end year based on the year range you want to investigate
start_year = 1960
end_year = 2024

# Data manipulation for population dataset
# Transpose the dataset to show countries' yearly population in each row
pop = pop.melt(id_vars= 'country', var_name= 'year', value_name= 'population')
# Change the data type for year column
pop['year'] = pop['year'].astype(int)
# Filter the dataset based on the year range you want to investigate
pop = pop[(pop['year'] >= start_year) & (pop['year'] < end_year)]

# Function to convert population values
def convert_population(pop):
    pop = str(pop)
    if 'B' in pop:
        return float(pop.replace('B', '')) * 1e9
    elif 'M' in pop:
        return float(pop.replace('M', '')) * 1e6
    elif 'k' in pop:
        return float(pop.replace('k', '')) * 1e3
    else:
        return float(pop)

# Apply the function to the population column
pop['population'] = pop['population'].apply(convert_population)

# Data manipulation for life expectancy dataset
# Transpose the dataset to show countries' yearly life expectancy in each row
lex = lex.melt(id_vars= 'country', var_name= 'year', value_name= 'life_exp')
# Change the data type for year column
lex['year'] = lex['year'].astype(int)
# Filter the dataset based on the year range you want to investigate
lex = lex[(lex['year'] >= start_year) & (lex['year'] < end_year)]

# Data manipulation for fertility rate dataset
# Transpose the dataset to show countries' yearly fertility rate in each row
fer = fer.melt(id_vars= 'country', var_name= 'year', value_name= 'fer_rate')
# Change the data type for year column
fer['year'] = fer['year'].astype(int)
# Filter the dataset based on the year range you want to investigate
fer = fer[(fer['year'] >= start_year) & (fer['year'] < end_year)]

# Merge population, life expectancy, fertility rate and continent datasets in one dataset 
countries = pop.merge(lex, how= 'inner', on= ['country', 'year'])
countries = countries.merge(fer, how= 'inner', on= ['country', 'year'])
countries = countries.merge(continent, how= 'inner', on= 'country')

# Create a for loop to create one graph for each year and then save them
for year in range(start_year, end_year):
    countries_temp = countries[countries['year'] == year]
    plt.figure(figsize=(40,32))
    sns.set_theme(style= 'darkgrid', palette= 'turbo')
    sns.scatterplot(data= countries_temp, x= 'life_exp', y= 'fer_rate', size= 'population', sizes=(400, 4000), hue= 'continent', alpha= 0.8)
    plt.legend(labelspacing= 2.7, fontsize= 24, loc= 'upper left', markerscale= 2)
    plt.title(f'Life Expectancy vs Fertility Rate in {year}', fontsize= 50)
    plt.xlabel('Life Expectancy (year)', fontsize= 30)
    plt.xticks(fontsize= 30, rotation= 45)
    plt.ylabel('Fertility Rate (# of babies per woman)', fontsize= 30)
    plt.yticks(fontsize= 30)
    plt.axis([0, 90, 0, 9.5])

    # Show country names in the annotation (for countries which have max and min population each year)
    max_min = [countries_temp['population'].max(), countries_temp['population'].min()]
    for i in max_min:    
        x_cor = (countries_temp.loc[countries_temp['population'] == i, ['life_exp']].values[0])
        y_cor = (countries_temp.loc[countries_temp['population'] == i, ['fer_rate']].values[0])
        text = countries_temp.loc[countries_temp['population'] == i, ['country']].values[0][0]
        plt.text(s= text, x= x_cor, y= y_cor, fontsize= 32, weight= 'bold')

    plt.savefig(f'images/plot_{year}.png')
    plt.close()

# Combine all years' graphs in a gif and save it
images = []

for year in range(start_year, end_year):
    filename = f'plot_{year}'
    images.append(imageio.v3.imread(f'./images/plot_{year}.png'))

# Save the gif, set the pace of gif with 'fps' parameter
imageio.mimsave(f'./images/animated_plot.png', images, fps= 5)