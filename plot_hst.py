import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
sns.set_style('ticks')

import requests

URL = "https://www.stsci.edu/~WFC3/trexolists/Trexolists20211026.txt"
response = requests.get(URL)
open("Trexolists20211026.txt", "wb").write(response.content)
