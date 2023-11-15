from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
from random import randint


# ZADANIE 1
# obraz: diff_jpg

diff = Image.open('diff_jpg.jpg')
