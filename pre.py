
from mortality import *

di = {'Age': 81, 'Sex': 0, 'SARS-CoV-2 nucleic acids:': '2', 'Computed tomography (CT):': '1', 'MCH': '31.20', 'HCT': '35.80', 'RBC': '3.94', 'PLT': '304', 'MO': '0.21', 'NE': '1.13', 'EOP ': '3.10', 'LYP': '41.20', 'WBC': '2.42', 'MCHC': '344.0', 'MCV': '90.70', 'HGB': '123.0', 'MPV': '8.50', 'EO': '0.07', 'LY': '1.0', 'BAP': '0.30', 'MOP': '8.70', 'NEP': '46.70'}
print(ClinicalPredict(di))