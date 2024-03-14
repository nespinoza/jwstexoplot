import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
sns.set_style('ticks')

import requests

URL = "https://www.stsci.edu/~nnikolov/TrExoLiSTS/JWST/trexolists.csv"
response = requests.get(URL)
open("trexolists_jwst.csv", "wb").write(response.content)
