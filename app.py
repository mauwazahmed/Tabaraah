import streamlit as st
import pandas as pd

def calculate_total_cost(dates, tasbeeh, miswak, topi, zamzam, mat, itar):
    prices = {
        "Dates": {"Ajwa": 6, "Kalmi": 6, "Sukri": 6, "Mabroom": 4},
        "Tasbih" : {"Type 1": 10, "Type 2": 15, "Type 3": 17, "Type 4": 20},
        "Miswak" : {"Type 1": 10, "Type 2": 15},
        "Topi" : {"Type 1": 15, "Type 2": 17, "Type 3": 20, "Type 4": 25},
        "ZamZam" : {"Pink 100ml":6, "Pink 60ml" : 5, "Green 60ml" : 2.5},
        "Mat" : {"Type 1": 120, "Type 2": 150, "Type 3": 195, "Type 4": 250},
        "Itar" : {"Type 1": 10, "Type 2": 15, "Type 3": 20}
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
    for item, detail in itar.items():
        total_cost += prices["Itar"][item] * detail[0] * detail[1]
    
    packaging = 10
    labor = 5
    margin = 20

    total_cost  = (total_cost+packaging+labor+misc+margin)

    return total_cost

st.title("Hajj/Umrah Gift Cost Calculator")
st.divider()

data = {
    "ZamZam" : {
        "Type": ["Pink 100ml", "Pink 60ml", "Green 60ml"],
        "Price per Unit (Rs)": [6, 5, 2.5]
    },
    "Dates" : {
        "Type": [ "Ajwa", "Kalmi", "Sukri", "Mabroom"],
        "Price per Unit (Rs)": [6, 6, 6, 4]
    },
    "Tasbih" : {
        "Type":  ["Type 1", "Type 2", "Type 3", "Type 4"],
        "Price per Unit (Rs)": [10, 15, 17, 20]
    },
    "Miswak" : {
        "Type": ["Type 1", "Type 2"],
        "Price per Unit (Rs)": [10, 15]
    },
    "Topi" : {
        "Type": ["Type 1", "Type 2", "Type 3", "Type 4"],
        "Price per Unit (Rs)": [15, 17, 20, 25]
    },
    "Mat" : {
        "Type": ["Type 1", "Type 2", "Type 3", "Type 4"],
        "Price per Unit (Rs)": [120, 150, 200, 250]
    },
    "Itar" : {
        "Type": ["Type 1", "Type 2", "Type 3"],
        "Price per Unit (Rs)": [10, 15, 20]
    }
}
    
items = ["ZamZam","Dates","Tasbih","Miswak","Topi","Mat"]

num_packets = st.number_input("Number of Gift Packets", min_value=0, step=1, key=1)
st.divider()    


df = pd.DataFrame(data["ZamZam"])
st.subheader("ZamZam")
st.dataframe(df,hide_index=True)
zamzam = {st.selectbox("Select Zamzam Bottle Quantity", data["ZamZam"]["Type"]): [st.number_input("Number of Units in One Packet", min_value=0, step=1, key=2),st.number_input("Number of Packets Required", min_value=0, step=1, value=num_packets, key = 3)]}
st.divider()    


df = pd.DataFrame(data["Dates"])
st.subheader("Dates")
st.dataframe(df,hide_index=True)
dates = {st.selectbox("Select Date Type", data["Dates"]["Type"]): [st.number_input("Number of Units in One Packet", min_value=0, step=1, key=4),st.number_input("Number of Packets Required", min_value=0, step=1, value=num_packets,key=5)]}
st.divider()    

df = pd.DataFrame(data["Tasbih"])
st.subheader("Tasbih")
st.dataframe(df,hide_index=True)
tasbih = {st.selectbox("Select Tasbeeh Type", data["Tasbih"]["Type"]): [st.number_input("Number of Units in One Packet", min_value=0, step=1, key=6),st.number_input("Number of Packets Required", min_value=0, step=1, value=num_packets, key=7)]}
st.divider()    

df = pd.DataFrame(data["Miswak"])
st.subheader("Miswak")
st.dataframe(df,hide_index=True)
miswak = {st.selectbox("Select Miswak Type", data["Miswak"]["Type"]): [st.number_input("Number of Units in One Packet", min_value=0, step=1, key=8),st.number_input("Number of Packets Required", min_value=0, step=1, value=num_packets, key=9)]}
st.divider()    

df = pd.DataFrame(data["Topi"])
st.subheader("Topi")
st.dataframe(df,hide_index=True)
topi = {st.selectbox("Select Topi Type", data["Topi"]["Type"]): [st.number_input("Number of Units in One Packet", min_value=0, step=1, key=10),st.number_input("Number of Packets Required", min_value=0, step=1, value=num_packets, key=11)]}
st.divider()    

df = pd.DataFrame(data["Mat"])
st.subheader("Prayer Mat")
st.dataframe(df,hide_index=True)
mat = {st.selectbox("Select Prayer Mat Type", data["Mat"]["Type"]): [st.number_input("Number of Units in One Packet", min_value=0, step=1, key=12),st.number_input("Number of Packets Required", min_value=0, step=1, value=num_packets, key=13)]}

df = pd.DataFrame(data["Itar"])
st.subheader("Prayer Mat")
st.dataframe(df,hide_index=True)
itar = {st.selectbox("Select Prayer Mat Type", data["Itar"]["Type"]): [st.number_input("Number of Units in One Packet", min_value=0, step=1, key=14),st.number_input("Number of Packets Required", min_value=0, step=1, value=num_packets, key=15)]}

  

st.divider()    

if st.button("Calculate Total Cost"):
    total_cost = calculate_total_cost(dates, tasbih, miswak, topi, zamzam, mat, itar)
    st.success(f"Total Cost: Rs {total_cost} + Delivery Charges (as applicable). With GST: Rs. {total_cost*1.18}")
