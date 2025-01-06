
# Prisoner Transfer Eligibility Calculator

A Python-based program that estimates when a prisoner becomes eligible for transfer to an open prison under Turkish Crime Law. This tool simplifies the complexities of legal calculations, making legal timelines more accessible and understandable.

---

## 📜 Project Overview

The Prisoner Transfer Eligibility Calculator simulates a sentencing calculator that estimates when a prisoner becomes eligible for transfer to an open prison based on their crime under Turkish Crime Law. This program is a simplified prototype designed for first-time offenders, focusing on accessibility and public understanding of sentencing and transfer timelines.

By providing a clear and user-friendly interface, the program helps users estimate eligibility timelines while educating them about sentencing factors.

### Key Features:
- **Eligibility Timeline Calculation:** Determines how long a prisoner must stay in a closed facility before transfer to an open prison.
- **Crime Categories:** Supports **first-degree crimes** (e.g., murder, terrorism) and **second-degree crimes** (e.g., petty theft, vandalism).
- **Behavioral Input:** Adjusts eligibility based on the number of warnings received during incarceration.
- **Dynamic Input Validation:** Ensures user-provided data is valid and provides helpful feedback.

---

## 💻 How to Run the Program

### Prerequisites:
- **Python 3.7 or higher**: Download and install it from the [official Python website](https://www.python.org/).

### Steps to Run:
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/YourUsername/PrisonerTransferEligibility.git
   cd PrisonerTransferEligibility
2. **Run the Script:**
Execute the program:
python prisoner_transfer_calculator.py
Provide Inputs:
Enter the required details when prompted:
Age: A number between 18-90.
Years Sentenced: Total sentence length in years (positive number).
Crime Name: Name of the crime from provided categories.
Warnings: Number of behavioral warnings during incarceration.
---
**📝 Example Usage**

This program determines when a prisoner becomes eligible for transfer to an open prison or lower-security facility.

Types of Crimes:
  First Degree Crimes: ['murder', 'terrorism', 'rape', 'kidnapping', ...]
  Second Degree Crimes: ['petty theft', 'vandalism', 'fraud', ...]

Please enter age between 18-90: 35
How many years was the sentence decided by the judge? 10
What is the name of the crime? murder

For murder, the prisoner must stay in the closed prison facility for 8.0 years.
Then, they can be transferred to the open prison facility for 2.0 years, assuming all other factors remain constant.

---
### 🌟 Future Development

This project is a foundational prototype with significant potential for further enhancements. Future improvements could include:

1. **Collaboration with Legal Experts:**
   - Incorporate real-world legal complexity.
   - Extend support for recurring offenders and detailed scenarios.

2. **Advanced Crime Categorization:**
   - Allow dynamic updates to crime categories and eligibility rules.

3. **Behavioral Insights:**
   - Include more granular behavioral tracking and impact analysis.

4. **Reporting Features:**
   - Generate detailed sentencing and eligibility reports.

5. **Accessibility:**
   - Develop a **Graphical User Interface (GUI)** for easier navigation.
   - Translate into multiple languages for wider reach.


### 🛠️ Technical Details

The program includes the following logic:

1. **Crime Categorization:**
   - Two main crime categories:
     - **First Degree Crimes:** Higher severity, longer closed prison time (80% of sentence).
     - **Second Degree Crimes:** Lesser severity, shorter closed prison time (60% of sentence).

2. **Behavioral Warnings:**
   - Prisoners with ≤3 warnings remain eligible.
   - Excessive warnings (>3) disqualify transfer eligibility.

3. **Simplified Calculations:**
   - Focused on first-time offenders.
   - Operates based on general Turkish Crime Law assumptions.

