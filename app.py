import streamlit as st
import pandas as pd

def calculate_total_cost(dates, tasbeeh, miswak, topi, zamzam, mat):
    prices = {
        "Dates": {"Ajwa": 2, "Kalmi": 2, "Sukri": 1, "Medjool": 3},
        "Tasbih" : {"Type 1": 8, "Type 2": 10, "Type 3": 12, "Type 4": 14},
        "Miswak" : {"Type 1": 8, "Type 2": 10, "Type 3": 12, "Type 4": 14},
        "Topi" : {"Type 1": 10, "Type 2": 15, "Type 3": 20, "Type 4": 25},
        "ZamZam" : {"100 ml":15, "50 ml" : 10},
        "Mat" : {"Type 1": 120, "Type 2": 150, "Type 3": 200, "Type 4": 250}
    }
    
    total_cost = 0
    for item, detail in dates.items():
        total_cost += prices["Dates"][item] * detail[0] * detail[1]
    for item, detail in tasbeeh.items():
        total_cost += prices["Tasbih"][item] * detail[0] * detail[1]
    for item, detail in miswak.items():
        total_cost += prices["Miswak"][item] * detail[0] * detail[1]
    for item, detail in topi.items():
        total_cost += prices["Topi"][item] * detail[0] * detail[1]
    for item, detail in zamzam.items():
        total_cost += prices["ZamZam"][item] * detail[0] * detail[1]
    for item, detail in mat.items():
        total_cost += prices["Mat"][item] * detail[0] * detail[1]
    
    packaging = 10
    labor = 5
    margin = 20
    misc = 5

    total_cost  = (total_cost+packaging+labor+misc+margin)*1.18

    return total_cost

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

num_packets = st.number_input("Number of Gift Packets", min_value=0, step=1, key=1)
st.divider()    


df = pd.DataFrame(data["ZamZam"])
st.subheader("ZamZam")
st.dataframe(df,hide_index=True)
zamzam = {st.selectbox("Select Zamzam Bottle Quantity", ["50 ml", "100 ml"]): [st.number_input("Number of Units in One Packet", min_value=0, step=1, key=2),st.number_input("Number of Packets Required", min_value=0, step=1, value=num_packets, key = 3)]}
st.divider()    


df = pd.DataFrame(data["Dates"])
st.subheader("Dates")
st.dataframe(df,hide_index=True)
dates = {st.selectbox("Select Date Type", ["Ajwa", "Kalmi", "Sukri", "Medjool"]): [st.number_input("Number of Units in One Packet", min_value=0, step=1, key=4),st.number_input("Number of Packets Required", min_value=0, step=1, value=num_packets,key=5)]}
st.divider()    

df = pd.DataFrame(data["Tasbih"])
st.subheader("Tasbih")
st.dataframe(df,hide_index=True)
tasbih = {st.selectbox("Select Tasbeeh Type", ["Type 1", "Type 2", "Type 3", "Type 4"]): [st.number_input("Number of Units in One Packet", min_value=0, step=1, key=6),st.number_input("Number of Packets Required", min_value=0, step=1, value=num_packets, key=7)]}
st.divider()    

df = pd.DataFrame(data["Miswak"])
st.subheader("Miswak")
st.dataframe(df,hide_index=True)
miswak = {st.selectbox("Select Miswak Type", ["Type 1", "Type 2", "Type 3", "Type 4"]): [st.number_input("Number of Units in One Packet", min_value=0, step=1, key=8),st.number_input("Number of Packets Required", min_value=0, step=1, value=num_packets, key=9)]}
st.divider()    

df = pd.DataFrame(data["Topi"])
st.subheader("Topi")
st.dataframe(df,hide_index=True)
topi = {st.selectbox("Select Topi Type", ["Type 1", "Type 2", "Type 3", "Type 4"]): [st.number_input("Number of Units in One Packet", min_value=0, step=1, key=10),st.number_input("Number of Packets Required", min_value=0, step=1, value=num_packets, key=11)]}
st.divider()    

df = pd.DataFrame(data["Mat"])
st.subheader("Prayer Mat")
st.dataframe(df,hide_index=True)
mat = {st.selectbox("Select Prayer Mat Type", ["Type 1", "Type 2", "Type 3", "Type 4"]): [st.number_input("Number of Units in One Packet", min_value=0, step=1, key=12),st.number_input("Number of Packets Required", min_value=0, step=1, value=num_packets, key=13)]}

  

st.divider()    

if st.button("Calculate Total Cost"):
    total_cost = calculate_total_cost(dates, tasbih, miswak, topi, zamzam, mat)
    st.success(f"Total Cost: Rs {total_cost} + Delivery Charges (as applicable)")
