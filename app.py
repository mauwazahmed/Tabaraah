import streamlit as st
import pandas as pd

def calculate_total_cost(num_packets, dates, tasbeeh, miswak, topi, zamzam, f_b, mat, itar, pkt):
    prices = {
        "Dates": {"Ajwa": 9, "Kalmi": 7, "Sukri": 5, "Rushdi": 3},
        "Tasbih" : {"Type 1": 10, "Type 2": 20, "Type 3": 25, "Type 4": 35,"Type 5": 50},
        "Miswak" : {"Type 1": 15, "Type 2": 20},
        "Topi" : {"Type 1": 20, "Type 2": 25, "Type 3": 30, "Type 4": 80},
        "ZamZam Empty" : {"Pink 100ml":6, "Pink 60ml" : 5, "Green 60ml" : 2.5},
        "ZamZam Filled" : {"Pink 100ml":40, "Pink 60ml" : 30, "Green 60ml" : 27},
        "Mat" : {"Type 1": 100, "Type 2": 150, "Type 3": 200},
        "Itar" : {"Type 1": 15, "Type 2": 20, "Type 3": 25},
        "Packaging" : {"Type 1": 1, "Type 2": 30, "Type 3": 50}
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
        total_cost += prices[f"ZamZam {f_b}"][item] * detail[0] * detail[1]
    for item, detail in mat.items():
        total_cost += prices["Mat"][item] * detail[0] * detail[1]
    for item, detail in itar.items():
        total_cost += prices["Itar"][item] * detail[0] * detail[1]
    for item, detail in pkt.items():
        total_cost += prices["Packaging"][item] * detail[0] * detail[1]
    
    return total_cost

st.title("Hajj/Umrah Gift Cost Calculator")
st.divider()

data = {
    "ZamZam" : {
        "Type": ["Pink 100ml", "Pink 60ml", "Green 60ml"],
        "Empty Bottle (price per unit)": [6, 5, 2.5],
        "Filled Bottle (price per unit)": [40, 30, 27]
    },
    "Dates" : {
        "Type": [ "Ajwa", "Kalmi", "Sukri", "Rushdi"],
        "Price per Unit (Rs)": [9, 7, 5, 3]
    },
    "Tasbih" : {
        "Type":  ["Type 1", "Type 2", "Type 3", "Type 4", "Type 5"],
        "Price per Unit (Rs)": [10, 20, 25, 35, 50]
    },
    "Miswak" : {
        "Type": ["Type 1", "Type 2"],
        "Price per Unit (Rs)": [15, 20]
    },
    "Topi" : {
        "Type": ["Type 1", "Type 2", "Type 3", "Type 4"],
        "Price per Unit (Rs)": [20, 25, 30, 80]
    },
    "Mat" : {
        "Type": ["Type 1", "Type 2", "Type 3"],
        "Price per Unit (Rs)": [100, 150, 200]
    },
    "Itar" : {
        "Type": ["Type 1", "Type 2", "Type 3"],
        "Price per Unit (Rs)": [15, 20, 25]
    },
    "Packaging" : {
        "Type": ["Type 1", "Type 2", "Type 3"],
        "Price per Unit (Rs)": [1, 30, 50]
    }
}
    
items = ["ZamZam","Dates","Tasbih","Miswak","Topi","Mat"]

num_packets = st.number_input("Number of Gift Packets", min_value=0, step=1, key=1)
st.divider()    


df = pd.DataFrame(data["ZamZam"])
st.subheader("ZamZam")
st.dataframe(df,hide_index=True)
f_b = st.selectbox("Do you want empty or filled bottles?", ['Empty','Filled'], key = 25)
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
st.subheader("Itar")
st.dataframe(df,hide_index=True)
itar = {st.selectbox("Select Itar Type", data["Itar"]["Type"]): [st.number_input("Number of Units in One Packet", min_value=0, step=1, key=14),st.number_input("Number of Packets Required", min_value=0, step=1, value=num_packets, key=15)]}

df = pd.DataFrame(data["Packaging"])
st.subheader("Packaging")
st.dataframe(df,hide_index=True)
pkt = {st.selectbox("Select Packaging Type", data["Packaging"]["Type"]): [st.number_input("Number of Units in One Packet", min_value=1, step=1, value=1, key=16),st.number_input("Number of Packets Required", min_value=0, step=1, value=num_packets, key=17)]}



st.divider()    

if st.button("Calculate Total Cost"):
    total_cost = calculate_total_cost(num_packets, dates, tasbih, miswak, topi, zamzam, f_b, mat, itar, pkt)
    st.success(f"Total Cost (excl GST): Rs {total_cost} \n Total Cost (GST incl): Rs {total_cost*1.18} \n + Delivery Charges (as applicable)")
