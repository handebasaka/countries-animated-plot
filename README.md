## Creating an Animated Scatterplot Showing the Correlation Between Life Expectancy and Fertility in 1960 - 2023

A scatterplot effectively displays the correlation between life expectancy and fertility rates across different countries over the years. In the notebook below, by animating the scatterplot, we will dynamically show how these key indicators of development and population have evolved between 1960 to 2023, revealing trends that static visualizations might miss.

**Dataset:** Gapminder is an independent foundation and provides the data publicly. We will download the data from here and take the datasets: "Population", "Life expectancy", and "Babies per woman" (fertility rate). We can also add continent information into our final dataset. Since the data contains too many gaps before 1950, we will focus on data after that.

To get started making a word cloud in Python, we will need some packages below:
- `pandas`: It is a data analysis and manipulation library that provides data structures and tools.
- `matplotlib.pyplot`: It is a plotting library for creating visualizations in Python.
- `seaborn`: It provides a high-level interface for drawing attractive and informative statistical graphics.
- `imageio`: It provides an easy interface to read and write a wide range of image data, including animated images, volumetric data, and scientific formats.

After the data cleaning and manipulation process, the final dataset will look like below:

| # | Column | Dtype | Description |
| ---- | ---- | ---- | ---- |
| 0 | `country` | object | country |
| 1 | `year` | int64 | year |
| 2 | `population` | float64 | total population  |
| 3 | `life_exp` | float64 | life expectancy at birth (year) |
| 4 | `fer_rate` | float64 | fertility rate - number of babies per woman |
| 5 | `continent` | object | continent  |


## Goals
- The goal of this project is to create a visualization to understand the trend between life expectancy, fertility rates and population. We will make it an animation version.


## Tools and Technologies Used
`Python`

`Pandas` for data manipulation 

`Matplotlib`, `Seaborn` and `Imageio` for data visualization

## How to Run
clone:
```sh
git clone https://github.com/handebasaka/countries-animated-plot
```
open the solution file:
```bash
cd countries-animated-plot
```
run python script:
```bash
python3 countries-animated-plot.py
```
