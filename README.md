# Renewable Fuels Assessment – WCO Biodiesel and PtL Fuels  
### Repository for LCA and TEA Models Supporting TRD Journal Submission

This repository contains supporting materials for the research article:

> **"Prioritizing Renewable Fuels in Transport: An Integrated LCA and Techno-Economic Study of Biodiesel and PtL Pathways"**  
> *Submitted to Transportation Research Part D: Transport and Environment*  
> **Author:** Kenechukwu Kingsley Okafor  
> **Affiliation:** Nottingham Trent University  
> **Status:** Under peer review

---

## 🔍 Contents

### `/LCA_Model/`
- OpenLCA Excel project files for Waste Cooking Oil (WCO) biodiesel and Power-to-Liquid (PtL) synthetic fuel pathways.
- System boundaries based on cradle-to-gate scope.
- Functional unit: 1 MJ of delivered fuel energy.
- Data sources: Ecoinvent 3.7, Agribilayse.

### `/TEA_Model/`
- Excel-based techno-economic model for fuel cost evaluation.
- Includes LCOF, NPV, and MIRR calculators.
- Key assumptions based on published sources, with scenario variables.

### `/Sensitivity_Analysis/`
- Python scripts (.ipynb and .py) used to generate GWP and LCOF sensitivity charts.
- Parameters include DAC energy input, electricity cost, feedstock price, etc.

---

## 📁 Usage

These materials are provided to ensure transparency and reproducibility.  
To run the sensitivity scripts:
1. Install dependencies listed in `requirements.txt`
2. Launch the Jupyter notebook or run `sensitivity_model.py`

*Note: OpenLCA files require OpenLCA software (version ≥1.10).*

---

## 📄 Citation

Please cite the corresponding article once published.  
Citation information and DOI will be updated upon acceptance.

---

## 📬 Contact

For questions, clarification, or collaboration:
**Email:** [ken.k.okafor@gmail.com]  
**Corresponding author:** Kenechukwu Kingsley Okafor

---

## 🔒 Access

This repository is currently private during peer review.  
Access may be granted upon request or will be made public upon article acceptance.
