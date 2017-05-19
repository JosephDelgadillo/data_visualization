import matplotlib.pyplot as plt

years = [1950,
         1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000,
         2005, 2010, 2015]

pops = [2.5, 2.7, 3, 3.3, 3.6,
        4.0, 4.4, 4.8, 5.3, 5.7, 6.1, 6.5, 6.9, 7.3]

deaths = [1.2, 1.7, 1.8, 2.2, 2.5,
          2.7, 2.9, 3, 3.1, 3.3, 3.5, 3.8, 4, 4.3]

lines = plt.plot(years, pops, years, deaths)
plt.grid(True)

plt.setp(lines, color=(1, .4, .4), marker="o")

plt.show()
