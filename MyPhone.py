import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import tkinter as tk
from tkinter import messagebox
import folium
import webbrowser

# Function to retrieve location and carrier information for a phone number
def get_phone_info(number):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(number, None)
        
        # Get location information
        location = geocoder.description_for_number(parsed_number, 'en')
        
        # Get carrier information
        service_provider = carrier.name_for_number(parsed_number, "en")
        
        return location, service_provider
    except phonenumbers.NumberParseException as e:
        return None, None

# Function to get latitude and longitude of a location
def get_lat_long(location):
    key = 'b8d1870ffad84d4998880b20ff7356dd'  # Replace with your OpenCage API key
    geocoder = OpenCageGeocode(key)
    results = geocoder.geocode(location)
    if results and len(results):
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        return lat, lng
    return None, None

# Function to display the map in a new window
def show_map(location):
    lat, lng = get_lat_long(location)
    if lat is not None and lng is not None:
        map = folium.Map(location=[lat, lng], zoom_start=10)
        folium.Marker([lat, lng], popup=location).add_to(map)
        map.save('map.html')
        webbrowser.open('map.html')
    else:
        messagebox.showerror("Error", "Failed to retrieve accurate location coordinates.")

# Function to handle button click event
def on_click():
    phone_number = entry.get()
    location, service_provider = get_phone_info(phone_number)
    
    if location and service_provider:
        messagebox.showinfo("Phone Number Information", f"Location: {location}\nService Provider: {service_provider}")
        show_map(location)
    else:
        messagebox.showerror("Error", "Invalid phone number or unable to retrieve information.")

# Create main window
root = tk.Tk()
root.title("Phone Number Tracker")
root.geometry("1080x720")  # Set window size

# Create input label and entry field
label = tk.Label(root, text="Enter your phone number:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Create track button
button = tk.Button(root, text="Track Now !", command=on_click)
button.pack()

# Run the application
root.mainloop()