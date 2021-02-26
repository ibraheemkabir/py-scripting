from geopy.geocoders import Nominatim
import pandas

df=pandas.read_csv("supermarkets.csv")
nom=Nominatim()
n= nom.geocde("")
df["Coordinates"] = df["Address"].apply(nom.geocode)
df["Latitude"] =df["Coordinates"].apply(lambda x: x.latitude if x!= None else None)
print(nom.geocode("Osho st, Lagos iSLAND, LA"))