import streamlit as st
import pandas as pd

def calculate_total_cost(dates, tasbeeh, miswak, topi, zamzam, mat, num_packets):
    prices = {
        "Dates": {"Ajwa": 2, "Kalmi": 2, "Sukri": 1, "Medjool": 3},
        "Tasbih" : {"Type 1": 8, "Type 2": 10, "Type 3": 12, "Type 4": 14},
        "Miswak" : {"Type 1": 8, "Type 2": 10, "Type 3": 12, "Type 4": 14},
        "Topi" : {"Type 1": 10, "Type 2": 15, "Type 3": 20, "Type 4": 25},
        "ZamZam" : {"100 ml":15, "50 ml" : 10},
        "Mat" : {"Type 1": 120, "Type 2": 150, "Type 3": 200, "Type 4": 250}
    }
    
    total_cost = 0
    for item, quantity in dates.items():
        total_cost += prices["Dates"][item] * quantity
    for item, quantity in tasbeeh.items():
        total_cost += prices["Tasbih"][item] * quantity
    for item, quantity in miswak.items():
        total_cost += prices["Miswak"][item] * quantity
    for item, quantity in topi.items():
        total_cost += prices["Topi"][item] * quantity
    for item, quantity in zamzam.items():
        total_cost += prices["ZamZam"][item] * quantity
    for item, quantity in mat.items():
        total_cost += prices["Mat"][item] * quantity
    total_cost += 50
    return total_cost * num_packets

st.title("Hajj/Umrah Gift Cost Calculator")

data = {
    "ZamZam" : {
        "Type": ["50 ml", "100 ml"],
        "Price per Unit (Rs)": [10, 15]
    },
    "Dates" : {
        "Type": [ "Ajwa", "Kalmi", "Sukri", "Medjool"],
        "Price per Unit (Rs)": [2, 2, 1, 3]
    },
    "Tasbih" : {
        "Type":  ["Type 1", "Type 2", "Type 3", "Type 4"],
        "Price per Unit (Rs)": [8, 10, 12, 14]
    },
    "Miswak" : {
        "Type": ["Type 1", "Type 2", "Type 3", "Type 4"],
        "Price per Unit (Rs)": [8, 10, 12, 14]
    },
    "Topi" : {
        "Type": ["Type 1", "Type 2", "Type 3", "Type 4"],
        "Price per Unit (Rs)": [10, 15, 20, 25]
    },
    "Mat" : {
        "Type": ["Type 1", "Type 2", "Type 3", "Type 4"],
        "Price per Unit (Rs)": [120, 150, 200, 250]
    }
}
    
items = ["ZamZam","Dates","Tasbih","Miswak","Topi","Mat"]

col1, col2 = st.columns([1,2],gap="medium",border=True)

with col1:
    st.header("Price List of Items")
    for i in range(len(items)):
        d = data[items[i]]
        df = pd.DataFrame(d)
        # Convert to DataFrame
        st.subheader(items[i])
        # st.table(df)
        st.dataframe(df,hide_index=True)

with col2:
    st.header("Select Items for Each Packet")
    dates = {st.selectbox("Select Date Type", ["Ajwa", "Kalmi", "Sukri", "Medjool"]): st.number_input("Number of Dates", min_value=0, step=1)}
    zamzam = {st.selectbox("Select Zamzam Bottle Quantity", ["50 ml", "100 ml"]): st.number_input("Number of Bottles", min_value=0, step=1)}
    tasbeeh = {st.selectbox("Select Tasbeeh Type", ["Type 1", "Type 2", "Type 3", "Type 4"]): st.number_input("Number of Tasbeeh", min_value=0, step=1)}
    miswak = {st.selectbox("Select Miswak Type", ["Type 1", "Type 2", "Type 3", "Type 4"]): st.number_input("Number of Miswak", min_value=0, step=1)}
    topi = {st.selectbox("Select Topi Type", ["Type 1", "Type 2", "Type 3", "Type 4"]): st.number_input("Number of Topi", min_value=0, step=1)}
    mat = {st.selectbox("Select Prayer Mat Type", ["Type 1", "Type 2", "Type 3", "Type 4"]): st.number_input("Number of Mats", min_value=0, step=1)}

    num_packets = st.number_input("Number of Gift Packets", min_value=1, step=1)

    if st.button("Calculate Total Cost"):
        total_cost = calculate_total_cost(dates, tasbeeh, miswak, topi, zamzam, mat, num_packets)
        st.success(f"Total Cost: Rs {total_cost} + Delivery Charges (as applicable)")
