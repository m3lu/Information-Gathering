import geocoder
import folium

n = input("What is the ip: ")
print("The ip is:", n)

g = geocoder.ip(n)

myAddress = g.latlng
print(myAddress)