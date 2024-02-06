import pandas as pd
import keyboard

data_set = pd.read_csv("Abbreviations_data.csv")

try:
    for data in data_set.values.tolist():
        keyboard.add_abbreviation(data[0], data[1]+" ")
    print("Smart Keyboard Started!")
    keyboard.record()
except:
    print("Stopped!")


