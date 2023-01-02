import pandas as pd
import numpy as np
class Asset:
      def __init__(self, name, age):
          self.name = name
          self.age = age
          self.owner = "bfsu"
      def makemoney(self):
          print(self.owner,"is making big money")
          return np.array([6, 7, 8])