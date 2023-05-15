import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk

def diagnose():
    body_part = body_part_var.get()
    symptom = symptom_var.get()
    query = body_part + " " + symptom
    url = "https://www.mayoclinic.org/" + query
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    conditions = []
    for item in soup.select('.result-container .result-title a'):
        conditions.append(item.text.strip())
    total_conditions = len(conditions)
    condition_counts = {}
    for condition in conditions:
        if condition in condition_counts:
            condition_counts[condition] += 1
        else:
            condition_counts[condition] = 1
    likelihoods = {}
    for condition in condition_counts:
        likelihoods[condition] = round(condition_counts[condition] / total_conditions * 100, 2)
    sorted_likelihoods = {k: v for k, v in sorted(likelihoods.items(), key=lambda item: item[1], reverse=True)}
    result_text = "Possible conditions and their likelihoods:\n"
    for condition in sorted_likelihoods:
        result_text += condition + ": " + str(sorted_likelihoods[condition]) + "%\n\n"
        if "treatment" in condition.lower():
            condition_url = "https://www.mayoclinic.org/diseases-conditions/" + condition.lower().replace(" ", "-") + "/treatment"
            condition_response = requests.get(condition_url)
            condition_soup = BeautifulSoup(condition_response.content, 'html.parser')
            treatment_list = condition_soup.select(".treatments-and-drugs__list ol li")
            treatment_text = "Recommended treatments:\n"
            for treatment in treatment_list:
                treatment_text += "- " + treatment.text.strip() + "\n"
            result_text += treatment_text + "\n"
    result_label.configure(text=result_text)

# create GUI
root = tk.Tk()
root.title("Symptom Checker")

# create body part dropdown
body_part_label = ttk.Label(root, text="Select the affected body part:")
body_part_label.pack()
body_part_var = tk.StringVar()
body_part_dropdown = ttk.Combobox(root, textvariable=body_part_var, values=[
    "Head",
    "Neck",
    "Chest",
    "Abdomen",
    "Pelvis",
    "Back",
    "Arms",
    "Legs"
])
body_part_dropdown.pack()

# create symptom dropdown
symptom_label = ttk.Label(root, text="Select the symptom:")
symptom_label.pack()
symptom_var = tk.StringVar()
symptom_dropdown = ttk.Combobox(root, textvariable=symptom_var, values=[
    "Pain",
    "Swelling",
    "Fever",
    "Cough",
    "Shortness of breath",
    "Nausea",
    "Vomiting",
    "Diarrhea",
    "Constipation",
    "Fatigue",
    "Weakness",
    "Numbness",
    "Tingling"
])
symptom_dropdown.pack()

# create diagnose button
diagnose_button = ttk.Button(root, text="Diagnose", command=diagnose)
diagnose_button.pack()

# create result label
result_label = ttk.Label(root, text="")
result_label.pack()

root.mainloop()