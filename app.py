import streamlit as st

def calculate_total_cost(dates, tasbeeh, miswak, topi, num_packets):
    prices = {
        "Ajwa": 2, "Kalmi": 2, "Sukri": 1, "Medjool": 3,
        "Tasbeeh Type 1": 10, "Tasbeeh Type 2": 12, "Tasbeeh Type 3": 8, "Tasbeeh Type 4": 14,
        "Miswak Type 1": 10, "Miswak Type 2": 12, "Miswak Type 3": 8, "Miswak Type 4": 14,
        "Topi Type 1": 10, "Topi Type 2": 15, "Topi Type 3": 20, "Topi Type 4": 25,
    }
    
    total_cost = 0
    for item, quantity in dates.items():
        total_cost += prices[item] * quantity
    for item, quantity in tasbeeh.items():
        total_cost += prices[item] * quantity
    for item, quantity in miswak.items():
        total_cost += prices[item] * quantity
    for item, quantity in topi.items():
        total_cost += prices[item] * quantity
    
    return total_cost * num_packets

st.title("Hajj/Umrah Gift Cost Calculator")

data = {
    "Item": ["Dates", "Dates", "Dates", "Dates", "Tasbeeh", "Tasbeeh", "Tasbeeh", "Tasbeeh",
             "Miswak", "Miswak", "Miswak", "Miswak", "Topi", "Topi", "Topi", "Topi"],
    "Type": ["Ajwa", "Kalmi", "Sukri", "Medjool", "Type 1", "Type 2", "Type 3", "Type 4",
             "Type 1", "Type 2", "Type 3", "Type 4", "Type 1", "Type 2", "Type 3", "Type 4"],
    "Price per Unit (Rs)": [2, 2, 1, 3, 10, 12, 8, 14, 10, 12, 8, 14, 10, 15, 20, 25]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Display in Streamlit
st.title("Price List of Items")
st.table(df)

st.header("Select Items for Each Packet")
dates = {st.selectbox("Select Date Type", ["Ajwa", "Kalmi", "Sukri", "Medjool"]): st.number_input("Number of Dates", min_value=0, step=1)}
tasbeeh = {st.selectbox("Select Tasbeeh Type", ["Tasbeeh Type 1", "Tasbeeh Type 2", "Tasbeeh Type 3", "Tasbeeh Type 4"]): st.number_input("Number of Tasbeeh", min_value=0, step=1)}
miswak = {st.selectbox("Select Miswak Type", ["Miswak Type 1", "Miswak Type 2", "Miswak Type 3", "Miswak Type 4"]): st.number_input("Number of Miswak", min_value=0, step=1)}
topi = {st.selectbox("Select Topi Type", ["Topi Type 1", "Topi Type 2", "Topi Type 3", "Topi Type 4"]): st.number_input("Number of Topi", min_value=0, step=1)}

num_packets = st.number_input("Number of Gift Packets", min_value=1, step=1)

if st.button("Calculate Total Cost"):
    total_cost = calculate_total_cost(dates, tasbeeh, miswak, topi, num_packets)
    st.success(f"Total Cost: Rs {total_cost}")
