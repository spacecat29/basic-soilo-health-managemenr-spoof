# ✅ Step 1: Import Required Libraries
import pdfplumber  # 📄 PDF se table extract karne ke liye  
import pandas as pd  # 📊 Data ko table format me store aur process karne ke liye  
import numpy as np  # 🔢 Numerical calculations ke liye  
import matplotlib.pyplot as plt  # 📈 Graphs banane ke liye  

# ✅ Step 2: Load the PDF File  
var_soil_pdf = "soil_data.pdf"  # 📄 Apni PDF ka naam yaha likho  

# 📄 PDF open kar rahe hai aur pehle page se table extract karenge  
with pdfplumber.open(var_soil_pdf) as pdf:  
    rpages = pdf.pages[0]  # 🔹 Pehla page select kar rahe hai  
    table = rpages.extract_table()  # 🔹 Table extract kar rahe hai  

# ✅ Step 3: Convert Extracted Table into Pandas DataFrame  
if table:  
    df = pd.DataFrame(table)  # 🔹 Extracted data ko DataFrame me convert kar rahe hai  
    df.columns = ["Soil Type", "Sand", "Silt", "Clay", "Moisture", "Bulk Density", "Porosity", "Bearing Capacity"]  
    df = df[1:]  # 🔹 Pehli row headers hoti hai, isliye actual data second row se start hoga  
else:  
    print("❌ No Table Found in PDF. Please Insert a Table.")  # ⚠️ Agar table nahi mila to error message  
    exit()  # ❌ Program ko yahi stop karenge  

# ✅ Step 4: Convert Numeric Columns to Proper Format  
prop_columns = ["Sand", "Silt", "Clay", "Moisture", "Bulk Density", "Porosity", "Bearing Capacity"]  

# 🔹 Check actual column names jo extract hue hai  
print("\n📌 Extracted Column Names:", df.columns)  

# 🔹 Sirf unhi columns ko number me convert karenge jo dataframe me present hai  
valid_columns = [col for col in prop_columns if col in df.columns]  
df[valid_columns] = df[valid_columns].apply(pd.to_numeric, errors='coerce')  # 🔹 Agar number convert nahi ho raha to 'NaN' mark karega  

# ✅ Step 5: Display Extracted Data  
print("\n📊 Extracted Soil Data from PDF:")  
print(df)  # 📋 Extracted data ko terminal me print karenge  

# ✅ Step 6: Define **Ideal Soil Conditions** for Farming & Construction  
ideal_farming = {
    "Moisture": 20,  
    "Porosity": 40,  
    "Bearing Capacity": 50  
}

ideal_construction = {
    "Moisture": 10,  
    "Porosity": 30,  
    "Bearing Capacity": 150  
}

# ✅ Step 7: Generate Graphs  
soil_col = "Soil Type" if "Soil Type" in df.columns else df.columns[0]  # Agar "Soil Type" nahi mila to pehla column lo  

# 🔹 **1️⃣ Graph: Extracted Soil Properties vs. Ideal Farming Soil**
plt.figure(figsize=(8,5))
plt.bar(df[soil_col], df["Moisture"], color='blue', label="Extracted Soil")
plt.axhline(y=ideal_farming["Moisture"], color='black', linestyle="--", label="Farming Moisture")  
plt.xlabel("Type Of Soil")
plt.ylabel("Moisture (%)")
plt.title("Extracted vs. Ideal Farming Moisture")
plt.legend()
plt.show()

# 🔹 **2️⃣ Graph: Extracted Soil Properties vs. Ideal Construction Soil**
plt.figure(figsize=(8,5))
plt.bar(df[soil_col], df["Bearing Capacity"], color='red', label="Extracted Soil")
plt.axhline(y=ideal_construction["Bearing Capacity"], color='black', linestyle="--", label="Construction Bearing Capacity")  
plt.xlabel("Type Of Soil")
plt.ylabel("Bearing Capacity (n/mm²)")
plt.title("Extracted vs. Ideal Construction Bearing Capacity")
plt.legend()
plt.show()

for index, row in df.iterrows():
    soil_type = row["Soil Type"]
    moisture = row["Moisture"]
    bearing_capacity = row["Bearing Capacity"]
    
    # ✅ Suitability Checks
    is_farming_suitable = moisture >= 15 and moisture <= 30  # Farming needs moderate moisture
    is_construction_suitable = bearing_capacity >= 100  # High bearing capacity required
    
    if is_farming_suitable and is_construction_suitable:
        print(f"✅ {soil_type} is **suitable for both Farming & Construction**")
    elif is_farming_suitable:
        print(f"🌱 {soil_type} is **more suitable for Farming**")
    elif is_construction_suitable:
        print(f"🏗️ {soil_type} is **more suitable for Construction**")
    else:
        print(f"❌ {soil_type} is **not ideal for either Farming or Construction**")
