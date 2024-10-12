# This script converts addresses to coordinates

# Importing required modules

from geopy.geocoders import Photon
import pandas as pd

# Project directory

direc = 'D:/accidental_effect/'
direc = 'C:/Users/macary/Documents/accidental_effect/'

# Reading in the house data

h = pd.read_csv(direc + 'data/harrisonburg.csv')
s = pd.read_csv(direc + 'data/staunton.csv')
w = pd.read_csv(direc + 'data/winchester.csv')

# Initializing Nominatim

geolocator = Photon(user_agent = 'measurements')

# Subsetting the data for residential/dwelling

h = h[h.Use_Code_Description == 'Dwelling'].reset_index(drop = True)
s = s[s.Use_Code_Description.isin(['Dwelling - 1 Fam', 'Dwelling - 1 Fam Comm', 'Dwelling - 1 Fam Vac', 'Dwelling - 2 Fam', 'Dwelling - Townhouse'])].reset_index(drop = True)
w = w[w.Use_Code_Description.isin(['Dwelling - Multi Fam', 'Dwelling - Multi Vac', 'Dwelling- Multi Comm', 'SFD - Urban Res', 'SFD - Urban Vacant'])].reset_index(drop = True)

# Getting unique addresses

h_addresses = list(h.Address.unique())
s_addresses = list(s.Address.unique())
w_addresses = list(w.Address.unique())

# Getting the coordinates with geopy

h_lats = []
s_lats = []
w_lats = []

h_lons = []
s_lons = []
w_lons = []

for i in range(len(h_addresses)):
    
    print('Harrisonburg address ' + str(1+i) + ' of 5,613.......')
    
    try:
        
        location = geolocator.geocode(h_addresses[i] + ', Harrisonburg, Virginia, USA')
        h_lats.append(location.latitude)
        h_lons.append(location.longitude)
        print(location.address)
        print((location.latitude, location.longitude))
            
    except:
        
        h_lats.append(None)
        h_lons.append(None)

for i in range(len(s_addresses)):
    
    print('Staunton address ' + str(1+i) + ' of 8,526.......')
    
    try:
        
        location = geolocator.geocode(s_addresses[i] + 'Staunton, Virginia, USA')
        s_lats.append(location.latitude)
        s_lons.append(location.longitude)
        print(location.address)
        print((location.latitude, location.longitude))
            
    except:
        
        s_lats.append(None)
        s_lons.append(None)

for i in range(len(w_addresses)):
    
    print('Winchester address ' + str(1+i) + ' of 8,557.......')
    
    try:
        
        location = geolocator.geocode(w_addresses[i] + 'Winchester, Virginia, USA')
        w_lats.append(location.latitude)
        w_lons.append(location.longitude)
        print(location.address)
        print((location.latitude, location.longitude))
            
    except:
        
        w_lats.append(None)
        w_lons.append(None)

# Creating a full list of house transaction coordinates

hlat = []
slat = []
wlat = []

hlon = []
slon = []
wlon = []

for i in range(len(h)):
    
    print('Transaction ' + str(1+i) + ' of 15,507.......')
    hlat.append(h_lats[h_addresses.index(h.Address[i])])
    hlon.append(h_lons[h_addresses.index(h.Address[i])])

for i in range(len(s)):
    
    print('Transaction ' + str(1+i) + ' of 32,926.......')
    slat.append(s_lats[s_addresses.index(s.Address[i])])
    slon.append(s_lons[s_addresses.index(s.Address[i])])

for i in range(len(w)):
    
    print('Transaction ' + str(1+i) + ' of 31,363.......')
    wlat.append(w_lats[w_addresses.index(w.Address[i])])
    wlon.append(w_lons[w_addresses.index(w.Address[i])])

# Adding coordinates to datafamrs

h = pd.concat([h, pd.Series(hlat, name = 'latitude'), pd.Series(hlon, name = 'longitude')], axis = 1)
s = pd.concat([s, pd.Series(slat, name = 'latitude'), pd.Series(slon, name = 'longitude')], axis = 1)
w = pd.concat([w, pd.Series(wlat, name = 'latitude'), pd.Series(wlon, name = 'longitude')], axis = 1)

# Removing misidentified observations

h = h[h.latitude > 38.35]
h = h[h.latitude < 38.50]

h = h[h.longitude > -78.96]
h = h[h.longitude < -78.78].reset_index(drop = True)

s = s[s.latitude > 38.08]
s = s[s.latitude < 38.25]

s = s[s.longitude > -79.14]
s = s[s.longitude < -78.95].reset_index(drop = True)

w = w[w.latitude > 39.06]
w = w[w.latitude < 39.27]

w = w[w.longitude > -78.23]
w = w[w.longitude < -78.07].reset_index(drop = True)

# Saving dataframes

h.to_csv(direc + 'data/harrisonburg_clean.csv', index = False)
s.to_csv(direc + 'data/staunton_clean.csv', index = False)
w.to_csv(direc + 'data/winchester_clean.csv', index = False)

