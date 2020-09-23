#this a map application made with python
#you can access any location available on google maps, and this map application has been made using only 3 lines of code
#install the "folium" module with pip install folium 
#then continue
import folium 
map = folium.Map(location=[22.5726, 88.3639]) #you can enter any location inside of the list, i have entered my home towns location
map.save("map.html") //saving the file to an html file, and if you open this html file anywhere, you will be able 
