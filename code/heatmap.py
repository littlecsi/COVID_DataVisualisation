import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from folium import plugins
import json
from datetime import datetime

# Read csv
patientInfo = pd.read_csv('PatientInfo.csv')
# patientRoute = pd.read_csv('../resources/PatientRoute.csv')
# region = pd.read_csv('../resources/Region.csv')
# timeAge = pd.read_csv('../resources/TimeAge.csv')
# weather = pd.read_csv('../resources/Weather.csv')

print(patientInfo.head())
