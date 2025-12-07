# 💰 Tip Calculator Project

We're going to build a tip calculator.

If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay:

(150.00 / 5) * 1.12 = 33.6

After formatting the result to 2 decimal places = 33.60

---

## 🚀 How It Works
1. 📝 Asks for the total bill amount
2. 🧾 Asks for the tip percentage
3. 👥 Asks for the number of people
4. 💵 Calculates total tip: `total_tip = bill * tip / 100`
5. 💵 Calculates total bill: `total_bill = bill + total_tip`
6. 🔢 Divides total bill among people: `bill_per_person = total_bill / people`
7. 🔢 Rounds the result to 2 decimal places: `final_amount = round(bill_per_person, 2)`
8. 🖨️ Prints the result using f-strings: `print(f"Each person should pay: {final_amount}")`

---