# 🏋️‍♂️ Simple BMI Calculator in Python

A sleek and simple Python script that accepts height and weight inputs, calculates Body Mass Index (BMI), and provides user recommendations based on international health standards (WHO).

---

## 🚀 Features

* **⚡ Fast & Lightweight:** Runs instantly in your terminal.
* **🌍 Standardized:** Uses official World Health Organization (WHO) BMI categories.
* **📊 User-Centric:** Gives clear, actionable feedback based on your results.
* **🛠️ Error Handling:** Validates inputs so it won't crash on typos.

---

## 📈 BMI Categories & Standards

The script evaluates your BMI based on the following international standards:

| BMI Range | Category | Recommendation |
| :--- | :--- | :--- |
| **< 18.5** | Underweight | Consider a nutritional plan to gain healthy weight. |
| **18.5 – 24.9** | Normal weight | Great job! Maintain your current lifestyle. |
| **25.0 – 29.9** | Overweight | Regular exercise and diet adjustments are advised. |
| **≥ 30.0** | Obese | Health consultation recommended for a structured plan. |

---

## 💻 How It Works

Here is a quick look at how the formula is implemented:

$$\text{BMI} = \frac{\text{weight (kg)}}{\text{height (m)}^2}$$

### 🛠️ Usage Example

```python
# Sample snippet of the recommendation logic
if bmi < 18.5:
    print("Category: Underweight 🦴")
elif 18.5 <= bmi < 25:
    print("Category: Normal weight ✅")
# ... and so on
