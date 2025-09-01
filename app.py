import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Pinnacle - Investment Planner", layout="centered")

# --- HOME UI ---
st.title("📈 Pinnacle Investment Planner")
st.write("Welcome to **Pinnacle**, your smart investment companion.")
st.markdown("---")

# --- USER INPUT ---
risk = st.selectbox("Choose your risk appetite:", ["Low", "Medium", "High"])
amount = st.number_input("Enter the amount you want to invest (₹):", min_value=1000, step=1000)

# --- ALLOCATION LOGIC ---
def calculate_allocation(risk, amount):
    if risk == "Low":
        return {
            "Fixed Deposits": 0.35 * amount,
            "Bonds": 0.25 * amount,
            "Debt Mutual Funds": 0.20 * amount,
            "Gold": 0.20 * amount
        }
    elif risk == "Medium":
        return {
            "Large Cap Stocks": 0.30 * amount,
            "Balanced Mutual Funds": 0.30 * amount,
            "REITs": 0.20 * amount,
            "Gold": 0.20 * amount
        }
    else:  # High risk
        return {
            "Equity (Mid/Small Cap)": 0.40 * amount,
            "Crypto": 0.20 * amount,
            "Startups/VC Funds": 0.20 * amount,
            "REITs": 0.10 * amount,
            "Gold": 0.10 * amount
        }

# --- SHOW RESULT ---
if amount > 0:
    st.subheader("💡 Suggested Allocation")
    allocation = calculate_allocation(risk, amount)

    for inv, val in allocation.items():
        st.write(f"**{inv}:** ₹{val:,.0f}")

    # --- PIE CHART ---
    fig, ax = plt.subplots()
    ax.pie(allocation.values(), labels=allocation.keys(), autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

st.markdown("---")
st.markdown("🔎 Learn more in our [Research Section](research.html)")
