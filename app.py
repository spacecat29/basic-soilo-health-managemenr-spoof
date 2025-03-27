from flask import Flask, render_template, request
import pdfplumber
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# ✅ Function to process the PDF and extract soil data
def process_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        rpages = pdf.pages[0]  # 🔹 Read first page
        table = rpages.extract_table()  # 🔹 Extract table

    if table:
        df = pd.DataFrame(table)
        df.columns = ["Soil Type", "Sand", "Silt", "Clay", "Moisture", "Bulk Density", "Porosity", "Bearing Capacity"]
        df = df[1:]  # 🔹 Remove extra header row
        prop_columns = ["Sand", "Silt", "Clay", "Moisture", "Bulk Density", "Porosity", "Bearing Capacity"]
        df[prop_columns] = df[prop_columns].apply(pd.to_numeric, errors='coerce')  # 🔹 Convert to numbers
        return df
    else:
        return None

# ✅ Define Ideal Soil Conditions
ideal_farming = {"Moisture": 20, "Porosity": 40, "Bearing Capacity": 50}
ideal_construction = {"Moisture": 10, "Porosity": 30, "Bearing Capacity": 150}

# ✅ Flask Route for Homepage
@app.route('/')
def home():
    return render_template('index.html')

# ✅ Flask Route for Uploading PDF & Processing Data
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "❌ No file uploaded. Please select a file."

    file = request.files['file']
    
    if file.filename == '':
        return "❌ No file selected."
    
    # ✅ Ensure Uploads Folder Exists
    upload_folder = "uploads"
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)  # ✅ Save uploaded file

    # ✅ Process the uploaded PDF
    df = process_pdf(file_path)
    
    if df is None:
        return "❌ No valid table found in the PDF."

    # ✅ Convert DataFrame to HTML Table for Web Display
    table_html = df.to_html(classes='table table-striped')

    # ✅ Ensure Static Folder Exists for Graphs
    static_folder = "static"
    if not os.path.exists(static_folder):
        os.makedirs(static_folder)

    # ✅ Generate Graph: Extracted vs. Ideal Farming Moisture
    plt.figure(figsize=(8, 5))
    plt.bar(df["Soil Type"], df["Moisture"], color='blue', label="Extracted Soil")
    plt.axhline(y=ideal_farming["Moisture"], color='black', linestyle="--", label="Ideal Farming Moisture")
    plt.xlabel("Soil Type")
    plt.ylabel("Moisture (%)")
    plt.title("Extracted vs. Ideal Farming Moisture")
    plt.legend()
    graph1_path = os.path.join(static_folder, "moisture_graph.png")
    plt.savefig(graph1_path)
    plt.close()

    # ✅ Generate Graph: Extracted vs. Ideal Construction Bearing Capacity
    plt.figure(figsize=(8, 5))
    plt.bar(df["Soil Type"], df["Bearing Capacity"], color='red', label="Extracted Soil")
    plt.axhline(y=ideal_construction["Bearing Capacity"], color='black', linestyle="--", label="Ideal Construction Bearing Capacity")
    plt.xlabel("Soil Type")
    plt.ylabel("Bearing Capacity (n/mm²)")
    plt.title("Extracted vs. Ideal Construction Bearing Capacity")
    plt.legend()
    graph2_path = os.path.join(static_folder, "bearing_graph.png")
    plt.savefig(graph2_path)
    plt.close()

    # ✅ Suitability Analysis
    suitability_results = []
    for index, row in df.iterrows():
        soil_type = row["Soil Type"]
        moisture = row["Moisture"]
        bearing_capacity = row["Bearing Capacity"]

        is_farming_suitable = 15 <= moisture <= 30
        is_construction_suitable = bearing_capacity >= 100

        if is_farming_suitable and is_construction_suitable:
            result = f"✅ {soil_type} is suitable for both Farming & Construction"
        elif is_farming_suitable:
            result = f"🌱 {soil_type} is more suitable for Farming"
        elif is_construction_suitable:
            result = f"🏗️ {soil_type} is more suitable for Construction"
        else:
            result = f"❌ {soil_type} is not ideal for Farming or Construction"
        
        suitability_results.append(result)

    return render_template('result.html', table=table_html, graph1=graph1_path, graph2=graph2_path, results=suitability_results)

# ✅ Run Flask App
if __name__ == '__main__':
    app.run(debug=True)
