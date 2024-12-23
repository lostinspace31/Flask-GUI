from flask import Flask, render_template, request
import os
import docx
from docx import Document
import pandas as pd
from pyvis.network import Network

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/code1", methods=["GET", "POST"])
def code1():
    table_data = None
    observations = []

    if request.method == "POST":
        # Retrieve form parameters
        param1 = request.form.get("param1")
        param2 = request.form.get("param2")
        param3 = request.form.get("param3")
        param4 = request.form.get("param4")

        # Set param3 based on dropdown value
        if param3 == "Yes":
            param3 = "y"
        else:
            param3 = "n"

        # Print parameters to the server log
        print(f"Parameter 1: {param1}")
        print(f"Parameter 2: {param2}")
        print(f"Parameter 3: {param3}")
        print(f"Parameter 4: {param4}")

        # Write parameters to a file
        directory = 'your_directory'  # Replace with your desired directory
        file_path = os.path.join(directory, 'content.txt')
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(file_path, 'w') as file:
            file.write(f"{param1}\n{param2}\n{param3}\n{param4}")
        print(f"Parameters written to {file_path}")

        # Read the Excel file and get data from table 'Table1'
        try:
            excel_file = "output.xlsx"
            df = pd.read_excel(excel_file, engine="openpyxl")
            table_data = {
                "headers": df.columns.tolist(),
                "rows": df.values.tolist()
            }
        except Exception as e:
            print(f"Error reading Excel file: {e}")
        
        # Read observations from Word document
        try:
            docx_file = "output.docx"
            doc = Document(docx_file)
            for table in doc.tables:
                for row in table.rows[1:]:  # Skipping the first row (header)
                    row_text = [cell.text.strip() for cell in row.cells]
                    observations.append(" | ".join(row_text))
                break
        except Exception as e:
            print(f"Error reading Word file: {e}")

    return render_template("form.html", table_data=table_data, observations=observations)

@app.route("/code2", methods=["GET", "POST"])
def code2():
    if request.method == "POST":
        # Simply process the form data if needed
        param = request.form.get("param")
        print(f"Received parameter: {param}")

    # Always serve the existing `output.html` in the background
    return render_template("form2.html")

@app.route("/code3", methods=["GET", "POST"])
def code3():
    return render_template("form3.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Change port to 5001 to avoid conflict
