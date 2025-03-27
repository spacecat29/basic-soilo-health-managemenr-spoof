import pdfplumber
import pandas as pd 
import numpy as np  
import matplotlib.pyplot as plt

# pdf_file = var_soil_pdf in this code
var_soil_pdf = "soil_data.pdf"

with pdfplumber.open(var_soil_pdf) as pdf:
    rpages = pdf.pages[0]
    table = rpages.extract_table()

if table:
    df = pd.DataFrame(table) 
    df.columns = ["Soil Type", "Sand", "Silt", "Clay", "Moisture", "Bulk Density", "Porosity", "Bearing Capacity"]  
    df = df[1:]
else:
    print("no Table In It Please Insert A Table")
    exit() 


prop_columns = ["Sand", "Silt", "Clay", "Moisture", "Bulk Density", "Porosity", "Bearing Capacity"]
print("Names Of Col From PDF:",df.columns)

valid_columns = [col for col in prop_columns if col in df.columns]
df[prop_columns] = df[prop_columns].apply(pd.to_numeric,errors = 'coerce')


print("Content from PDF (Extracted)")
print(df)

soil_col = "Soil Type" if "Soil Type"in df.columns else df.columns[0]

#part-2-graph
plt.figure(figsize=(8,5))
plt.bar(df[soil_col], df["Moisture"],color='blue')
plt.xlabel("Type Of Soil")
plt.ylabel("Moisture Content in %")
plt.title("Soil Moisture By Type")
plt.show()

plt.figure(figsize=(8,5))
plt.bar(df[soil_col], df["Porosity"],color='red')
plt.xlabel("Type Of Soil")
plt.ylabel("Porosity Content in %")
plt.title("Soil Porosity By Type")
plt.show()

plt.figure(figsize=(8,5))
plt.bar(df[soil_col], df["Bearing Capacity"],color='brown')
plt.xlabel("Type Of Soil")
plt.ylabel("Bearing Capacity in n/mm^2")
plt.title("Soil Bearing By Type")
plt.show()
