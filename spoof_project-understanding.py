# ✅ Step 1: Import required libraries
import pdfplumber  # PDF se tables extract karne ke liye
import pandas as pd  # Data ko table format me store aur process karne ke liye
import numpy as np  # Numerical calculations ke liye
import matplotlib.pyplot as plt  # Graphs banane ke liye

# ✅ Step 2: Load the PDF File
pdf_file = "soil_data.pdf"  # 📄 Apni PDF ka naam yaha likho

# PDF ko open kar rahe hai aur pehle page se table extract karenge
with pdfplumber.open(pdf_file) as pdf:  ithe ky pdf cha data kaa read hoto ahe? ani hi kay method ahe ka ?extract_table()

    page = pdf.pages[0]  # 🔹 Pehla page select kar rahe hai
    table = page.extract_table()  # 🔹 Table extract kar rahe hai 
# ✅ Step 3: Convert Extracted Table into Pandas DataFrame
df = pd.DataFrame(table[1:], columns=table[0])  # 🔹 Pehli row headers hoti hai, isliye second row se start kar rahe hai

# ✅ Step 4: Convert Numeric Columns to Proper Format
# PDF se aane wale data text format me hote hai, isliye numeric values ko number me convert karna zaroori hai
numeric_columns = ["Sand (%)", "Silt (%)", "Clay (%)", "Moisture (%)", "Bulk Density (g/cm³)", "Porosity (%)", "Bearing Capacity (kN/m²)"]
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric) yhacha magchi logic kay ahe? # 🔹 Sare numeric columns ko float/int me convert kar rahe hai

# ✅ Step 5: Display the Extracted Soil Data
print("\n📊 Extracted Soil Properties from PDF:")
print(df)  # 🔹 Terminal me table print karega

# ✅ Step 6: Calculate Extra Property - Compaction Factor
# Formula: Bulk Density ÷ Porosity (Important for Construction)
df["Compaction Factor"] = np.round(df["Bulk Density (g/cm³)"] / df["Porosity (%)"], 2)

# ✅ Step 7: Print Table with New Calculated Column
print("\n📌 Soil Data with Calculated Compaction Factor:")
print(df[["Soil Type", "Bulk Density (g/cm³)", "Porosity (%)", "Compaction Factor"]])

# ✅ Step 8: Generate Graphs for Data Analysis

# 🔹 1️⃣ Soil Moisture Graph
plt.figure(figsize=(8, 5)) syntax kay ahe?  # 🔹 Graph ka size set kar rahe hai
plt.bar(df["Soil Type"], df["Moisture (%)"], color='blue')  # 🔹 Bar graph banayenge jo Soil Type aur Moisture (%) dikhayega
plt.xlabel("Soil Type")  # 🔹 X-axis label
plt.ylabel("Moisture Content (%)")  # 🔹 Y-axis label
plt.title("Soil Moisture by Type")  # 🔹 Graph ka title
plt.show()  # 🔹 Graph display karega

# 🔹 2️⃣ Soil Porosity Graph
plt.figure(figsize=(8, 5))
plt.bar(df["Soil Type"], df["Porosity (%)"], color='green')
plt.xlabel("Soil Type")
plt.ylabel("Porosity (%)")
plt.title("Soil Porosity by Type")
plt.show()

# 🔹 3️⃣ Soil Bearing Capacity Graph
plt.figure(figsize=(8, 5))
plt.bar(df["Soil Type"], df["Bearing Capacity (kN/m²)"], color='red')
plt.xlabel("Soil Type")
plt.ylabel("Bearing Capacity (kN/m²)")
plt.title("Soil Bearing Capacity by Type")
plt.show()

print('----------NO-Errors-Code------------------------------------------------------------------------------')
# ✅ Step 1: Required Libraries Import  
import pdfplumber  # 📄 PDF se table extract karne ke liye  
import pandas as pd  # 📊 Data ko table format me store aur process karne ke liye  
import numpy as np  # 🔢 Numerical calculations ke liye  
import matplotlib.pyplot as plt  # 📈 Graphs banane ke liye  

# ✅ Step 2: Load the PDF File  
var_soil_pdf = "soil_data.pdf"  # 📄 PDF ka naam (ye file aapke script folder me honi chahiye)  

# 📄 PDF open kar rahe hai aur pehle page se table extract karenge  
with pdfplumber.open(var_soil_pdf) as pdf:  
    rpages = pdf.pages[0]  # 🔹 Pehla page select kar rahe hai  
    table = rpages.extract_table()  # 🔹 Table extract kar rahe hai  

# ✅ Step 3: Convert Extracted Table into Pandas DataFrame  
if table:  
    df = pd.DataFrame(table)  # 🔹 Extracted data ko DataFrame me convert kar rahe hai  
    df.columns = ["Soil Type", "Sand", "Silt", "Clay", "Moisture", "Bulk Density", "Porosity", "Bearing Capacity"]  
    # 🔹 Column headers manually set kar rahe hai, kyunki PDF se kabhi kabhi galat extract hota hai  
    
    df = df[1:] df.columns kay ahe?inbuiltfunction ahe ka?, df = df[1:] 0 ne kabara start nahi kela # 🔹 Pehli row headers hoti hai, isliye actual data second row se start hoga  
else:  
    print("❌ No Table Found in PDF. Please Insert a Table.")  # ⚠️ Agar table nahi mila to error message  
    exit() new item # ❌ Program ko yahi stop karenge  

# ✅ Step 4: Convert Numeric Columns to Proper Format  
prop_columns = ["Sand", "Silt", "Clay", "Moisture", "Bulk Density", "Porosity", "Bearing Capacity"]   hi step kay ahe?

# 🔹 Check actual column names jo extract hue hai  
print("\n📌 Extracted Column Names:", df.columns)  same hi pan step cha purpose kay ahe?

# 🔹 Sirf unhi columns ko number me convert karenge jo dataframe me present hai  
valid_columns = [col for col in prop_columns if col in df.columns]  logic samjun ghe col var ahe ki kahi new 
df[valid_columns] = df[valid_columns].apply(pd.to_numeric, errors='coerce') hyacha purpose kay ahe? # 🔹 Agar number convert nahi ho raha to 'NaN' mark karega  

# ✅ Step 5: Display Extracted Data  
print("\n📊 Extracted Soil Data from PDF:")  
print(df)  # 📋 Extracted data ko terminal me print karenge  

# ✅ Step 6: Generate Graphs  
# 🔹 "Soil Type" column agar missing hai to first column ka use karenge  
soil_col = "Soil Type" if "Soil Type" in df.columns else df.columns[0]  

# 🔹 1️⃣ Soil Moisture Graph  
plt.figure(figsize=(8,5))  # 📏 Graph ka size set kar rahe hai  
plt.bar(df[soil_col], df["Moisture"], color='blue')  # 📊 Moisture ke values bar graph me show karenge  
plt.xlabel("Type Of Soil")  # 📌 X-axis ka naam  
plt.ylabel("Moisture Content (%)")  # 📌 Y-axis ka naam  
plt.title("Soil Moisture By Type")  # 📌 Graph ka title  
plt.show()  # 📊 Graph ko show karne ka command  

# 🔹 2️⃣ Soil Porosity Graph  
plt.figure(figsize=(8,5))  
plt.bar(df[soil_col], df["Porosity"], color='red')  
plt.xlabel("Type Of Soil")  
plt.ylabel("Porosity (%)")  
plt.title("Soil Porosity By Type")  
plt.show()  

# 🔹 3️⃣ Soil Bearing Capacity Graph  
plt.figure(figsize=(8,5))  
plt.bar(df[soil_col], df["Bearing Capacity"], color='green')  
plt.xlabel("Type Of Soil")  
plt.ylabel("Bearing Capacity (n/mm²)")  
plt.title("Soil Bearing By Type")  
plt.show()  
