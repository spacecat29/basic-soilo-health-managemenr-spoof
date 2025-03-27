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
else:
    print("no Table In It Please Insert A Table")
    exit() 


prop_columns = ["Sand", "Silt", "Clay", "Moisture", "Bulk Density", "Porosity", "Bearing Capacity"]

print("Extracted Columns Name: ",df.columns)
valid_columns = [col for col in prop_columns if col in df.columns] 
df[valid_columns] = df[valid_columns].apply(pd.to_numeric,errors = 'coerce')

print("Content from PDF (Extracted)")
print(df)

#part-2-graph
plt.figure(figsize=(8,5))
plt.bar(df["Soil Type"], df["Moisture"],color='blue')
plt.xlabel("Type Of Soil")
plt.ylabel("Moisture Content in %")
plt.title("soil Moisture By Type")
plt.show()

plt.figure(figsize=(8,5))
plt.bar(df["Soil Type"], df["Porosity"],color='red')
plt.xlabel("Type Of Soil")
plt.ylabel("Porosity Content in %")
plt.title("soil Porosity By Type")
plt.show()

plt.figure(figsize=(8,5))
plt.bar(df["Soil Type"], df["Bearing Capacity"],color='green')
plt.xlabel("Type Of Soil")
plt.ylabel("Bearing Capacity in n/mm^2")
plt.title("Soil Bearing By Type")
plt.show()
