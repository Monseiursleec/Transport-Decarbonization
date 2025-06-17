#!/usr/bin/env python
# coding: utf-8

# In[9]:


#SHEET 2 LCOF BREAKDOWN AND COST COMPARISONS
# Re-import necessary libraries after execution reset
import numpy as np
import matplotlib.pyplot as plt

# Step 15: Generate LCOF Visuals for Sheet 2

# Define categories for comparison
categories_lcof = ["Annualized CAPEX (€/MJ)", "OPEX (€/MJ)", "Total LCOF (€/MJ)"]

# Values for WCO and PtL (€/MJ)
wco_lcof_values = [0.0003, 0.023, 0.023]  # CAPEX component, OPEX component, Total LCOF
ptl_lcof_values = [0.0424, 0.103, 0.145]  # CAPEX component, OPEX component, Total LCOF

# Create a bar chart for WCO vs. PtL LCOF comparison
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35  # Width of the bars
x = np.arange(len(categories_lcof))  # X-axis positions

# Plot bars
bars1 = ax.bar(x - bar_width/2, wco_lcof_values, bar_width, label="WCO Biodiesel", color='green')
bars2 = ax.bar(x + bar_width/2, ptl_lcof_values, bar_width, label="PtL Fuel", color='blue')

# Labels and Formatting
ax.set_xlabel("Cost Components of LCOF")
ax.set_ylabel("€/MJ")
ax.set_title("LCOF Breakdown: WCO Biodiesel vs. PtL Fuel")
ax.set_xticks(x)
ax.set_xticklabels(categories_lcof, rotation=15)
ax.legend()

# Display the chart
plt.show()


# In[10]:


# Re-attempt: Generate Cash Flow Over 20 Years Chart for WCO & PtL

# Define years (1 to 20)
years = np.arange(1, 21)

# Yearly cash flows for WCO & PtL (based on previous calculations)
cash_flow_wco = [54.55] * 20  # Constant cash flow for WCO
cash_flow_ptl = [4.93, 7.16, 9.50, 11.96, 14.55, 17.26, 20.11, 23.10, 26.24, 29.54,
                 33.00, 36.64, 40.46, 44.47, 48.68, 53.10, 57.74, 62.61, 67.73, 73.10]  # Increasing cash flow for PtL

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot WCO Cash Flow
ax.plot(years, cash_flow_wco, marker='o', linestyle='-', color='green', label="WCO Biodiesel")

# Plot PtL Cash Flow
ax.plot(years, cash_flow_ptl, marker='s', linestyle='--', color='blue', label="PtL Fuel")

# Labels and Formatting
ax.set_xlabel("Years")
ax.set_ylabel("Yearly Cash Flow (€M)")
ax.set_title("Projected Cash Flow Over 20 Years (WCO vs. PtL)")
ax.legend()
ax.grid(True)

# Display the chart
plt.show()


# In[11]:


# Re-import necessary libraries after execution reset
import numpy as np
import matplotlib.pyplot as plt

# Step 17: Generate MIRR vs. Discount Rate Bar Chart for WCO & PtL (Sheet 3)

# Define discount rates and corresponding MIRR values for WCO & PtL
discount_rates = ["5%", "6%", "7%", "8% (Base)", "9%", "10%", "11%"]
mirr_wco = [42.8, 41.2, 39.8, 38.2, 36.9, 35.5, 34.2]  # MIRR (%) for WCO at different discount rates
mirr_ptl = [9.2, 8.5, 7.6, 6.1, 5.4, 4.2, 3.7]  # MIRR (%) for PtL at different discount rates

# Create the bar chart for MIRR vs. Discount Rate
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35  # Width of bars
x = np.arange(len(discount_rates))  # X-axis positions

# Plot bars
bars1 = ax.bar(x - bar_width/2, mirr_wco, bar_width, label="WCO Biodiesel", color='green')
bars2 = ax.bar(x + bar_width/2, mirr_ptl, bar_width, label="PtL Fuel", color='blue')

# Labels and Formatting
ax.set_xlabel("Discount Rate (%)")
ax.set_ylabel("MIRR (%)")
ax.set_title("MIRR Sensitivity to Discount Rate (WCO vs. PtL)")
ax.set_xticks(x)
ax.set_xticklabels(discount_rates)
ax.legend()

# Display the chart
plt.show()


# In[7]:


#SHEET 4 VISUALIZATION
# Step 11: Generate Tornado Chart for NPV Sensitivity (WCO & PtL)

# Define sensitivity parameters for WCO & PtL
parameters_wco = ["Feedstock Cost -20%", "Feedstock Cost +20%", "Glycerol Credit -20%", "Glycerol Credit +20%", "Electricity Cost ±10%"]
parameters_ptl = ["CAPEX -30%", "CAPEX -50%", "OPEX -20%", "Carbon Credit (€50/tCO₂)", "Fuel Price +30% (€6.50/L)"]

# NPV changes from base case for WCO (values from Sheet 4 calculations)
npv_wco_base = 531.64
npv_wco_changes = [
    699.47 - npv_wco_base,  # Feedstock Cost -20%
    412.52 - npv_wco_base,  # Feedstock Cost +20%
    550.76 - npv_wco_base,  # Glycerol Credit -20%
    515.39 - npv_wco_base,  # Glycerol Credit +20%
    499.32 - npv_wco_base   # Electricity Cost ±10%
]

# NPV changes from base case for PtL (values from Sheet 4 calculations)
npv_ptl_base = -138.95
npv_ptl_changes = [
    50.76 - npv_ptl_base,  # CAPEX -30%
    105.32 - npv_ptl_base,  # CAPEX -50%
    42.67 - npv_ptl_base,  # OPEX -20%
    18.52 - npv_ptl_base,  # Carbon Credit (€50/tCO₂)
    98.84 - npv_ptl_base   # Fuel Price +30%
]

# Sort WCO values by magnitude for better visualization
sorted_indices_wco = sorted(range(len(npv_wco_changes)), key=lambda k: abs(npv_wco_changes[k]), reverse=True)
sorted_parameters_wco = [parameters_wco[i] for i in sorted_indices_wco]
sorted_npv_wco_changes = [npv_wco_changes[i] for i in sorted_indices_wco]

# Sort PtL values by magnitude
sorted_indices_ptl = sorted(range(len(npv_ptl_changes)), key=lambda k: abs(npv_ptl_changes[k]), reverse=True)
sorted_parameters_ptl = [parameters_ptl[i] for i in sorted_indices_ptl]
sorted_npv_ptl_changes = [npv_ptl_changes[i] for i in sorted_indices_ptl]

# Create Tornado Chart for NPV Sensitivity (WCO & PtL)
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# WCO Tornado Chart
axes[0].barh(sorted_parameters_wco, sorted_npv_wco_changes, color=['blue' if v < 0 else 'green' for v in sorted_npv_wco_changes])
axes[0].axvline(0, color='black', linewidth=1)
axes[0].set_xlabel("NPV Change (€M)")
axes[0].set_title("Tornado Chart: NPV Sensitivity for WCO Biodiesel")
axes[0].invert_yaxis()

# PtL Tornado Chart
axes[1].barh(sorted_parameters_ptl, sorted_npv_ptl_changes, color=['blue' if v < 0 else 'green' for v in sorted_npv_ptl_changes])
axes[1].axvline(0, color='black', linewidth=1)
axes[1].set_xlabel("NPV Change (€M)")
axes[1].set_title("Tornado Chart: NPV Sensitivity for PtL Fuel")
axes[1].invert_yaxis()

# Adjust layout and display
plt.tight_layout()
plt.show()


# In[8]:


# Step 12: Generate Tornado Chart for LCOF Sensitivity (€/MJ for WCO & PtL)

# Define sensitivity parameters for WCO & PtL affecting LCOF
parameters_wco_lcof = ["Feedstock Cost -20%", "Feedstock Cost +20%", "Glycerol Credit -20%", "Glycerol Credit +20%", "Electricity Cost ±10%"]
parameters_ptl_lcof = ["CAPEX -30%", "CAPEX -50%", "OPEX -20%", "Carbon Credit (€50/tCO₂)", "Fuel Price +30% (€6.50/L)"]

# LCOF changes from base case for WCO (€/MJ)
lcof_wco_base = 0.021
lcof_wco_changes = [
    0.018 - lcof_wco_base,  # Feedstock Cost -20%
    0.027 - lcof_wco_base,  # Feedstock Cost +20%
    0.020 - lcof_wco_base,  # Glycerol Credit -20%
    0.022 - lcof_wco_base,  # Glycerol Credit +20%
    0.022 - lcof_wco_base   # Electricity Cost ±10%
]

# LCOF changes from base case for PtL (€/MJ)
lcof_ptl_base = 0.145
lcof_ptl_changes = [
    0.097 - lcof_ptl_base,  # CAPEX -30%
    0.085 - lcof_ptl_base,  # CAPEX -50%
    0.123 - lcof_ptl_base,  # OPEX -20%
    0.132 - lcof_ptl_base,  # Carbon Credit (€50/tCO₂)
    0.111 - lcof_ptl_base   # Fuel Price +30%
]

# Sort WCO values by magnitude for better visualization
sorted_indices_wco_lcof = sorted(range(len(lcof_wco_changes)), key=lambda k: abs(lcof_wco_changes[k]), reverse=True)
sorted_parameters_wco_lcof = [parameters_wco_lcof[i] for i in sorted_indices_wco_lcof]
sorted_lcof_wco_changes = [lcof_wco_changes[i] for i in sorted_indices_wco_lcof]

# Sort PtL values by magnitude
sorted_indices_ptl_lcof = sorted(range(len(lcof_ptl_changes)), key=lambda k: abs(lcof_ptl_changes[k]), reverse=True)
sorted_parameters_ptl_lcof = [parameters_ptl_lcof[i] for i in sorted_indices_ptl_lcof]
sorted_lcof_ptl_changes = [lcof_ptl_changes[i] for i in sorted_indices_ptl_lcof]

# Create Tornado Chart for LCOF Sensitivity (€/MJ for WCO & PtL)
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# WCO Tornado Chart
axes[0].barh(sorted_parameters_wco_lcof, sorted_lcof_wco_changes, color=['blue' if v < 0 else 'green' for v in sorted_lcof_wco_changes])
axes[0].axvline(0, color='black', linewidth=1)
axes[0].set_xlabel("LCOF Change (€/MJ)")
axes[0].set_title("Tornado Chart: LCOF Sensitivity for WCO Biodiesel")
axes[0].invert_yaxis()

# PtL Tornado Chart
axes[1].barh(sorted_parameters_ptl_lcof, sorted_lcof_ptl_changes, color=['blue' if v < 0 else 'green' for v in sorted_lcof_ptl_changes])
axes[1].axvline(0, color='black', linewidth=1)
axes[1].set_xlabel("LCOF Change (€/MJ)")
axes[1].set_title("Tornado Chart: LCOF Sensitivity for PtL Fuel")
axes[1].invert_yaxis()

# Adjust layout and display
plt.tight_layout()
plt.show()


# In[5]:


#SHEET 5 
# Re-import necessary libraries after execution reset
import numpy as np
import matplotlib.pyplot as plt

# Step 14: Re-generate the Final TEA Comparison Chart for WCO vs. PtL

# Define categories for comparison
categories = ["NPV (€M)", "MIRR (%)", "LCOF (€/MJ)", "CAPEX (€M)", "OPEX (€M/year)"]

# Values for WCO and PtL
wco_values = [531.64, 38.2, 0.021, 3.97, 28.00]
ptl_values = [-138.95, 6.1, 0.145, 390, 96.64]

# Create a bar chart for WCO vs. PtL comparison
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35  # Width of the bars
x = np.arange(len(categories))  # X-axis positions

# Plot bars
bars1 = ax.bar(x - bar_width/2, wco_values, bar_width, label="WCO Biodiesel", color='green')
bars2 = ax.bar(x + bar_width/2, ptl_values, bar_width, label="PtL Fuel", color='blue')

# Labels and Formatting
ax.set_xlabel("Financial & Cost Metrics")
ax.set_ylabel("Values")
ax.set_title("Final TEA Comparison: WCO Biodiesel vs. PtL Fuel")
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=15)
ax.legend()

# Display the chart
plt.show()


# In[ ]:




