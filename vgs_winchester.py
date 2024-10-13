# This script scrapes house transactions for Winchester, VA

# Importing required modules

import urllib
from bs4 import BeautifulSoup as bs
import pandas as pd
import ssl

# Prep for scraping

ssl._create_default_https_context = ssl._create_stdlib_context

# Main loop

pids = []
address = []
typ = []
buyer = []
seller = []
price = []
date = []

year = []
feet = []
model = []
style = []
grade = []
grade_adj = []
stories = []
num_units = []
roof = []
cover = []
exwall1 = []
exwall2 = []
heat = []
fuel = []
ac = []
inwall1 = []
inwall2 = []
infloor1 = []
infloor2 = []
rooms = []
beds = []
full = []
half = []
extra_fix = []
fireplace = []
foundation = []
bsmt = []
gar = []

use_code = []
descr = []
neighborhood = []
acres = []

for PID in range(1,10000):
    
    print(PID)
    
    try:
        
        VGSURL = 'https://gis.vgsi.com/winchesterVA/Parcel.aspx?pid=' + str(PID)
        page = urllib.request.Request(VGSURL, headers = {'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(page)
        soup = bs(response, 'html.parser')
        results_add = soup.find(id = 'MainContent_rowLocation')
        
        if results_add == None:
            
            continue
            
        else:
            
            x = results_add.findAll('span')[0].text
            print(x)
            results = soup.find(id = 'MainContent_panSlh')
            sales = results.findAll('tr')
            science = soup.find(id = 'tabs-4')
            ugh = science.findAll('td')
            dental = soup.find(id = 'MainContent_panLandUse').findAll('td')
            floss = soup.find(id = 'MainContent_panLandLine').findAll('td')
            hood = soup.find(id = 'MainContent_lblAssngDist').text
            
            for i in range(1,len(sales)):
                
                entry = sales[i].findAll('td')
                
                try:
                    
                    buyer.append(entry[0].text)
                
                except:
                    
                    buyer.append(None)
                
                try:
                    
                    price.append(entry[1].text)
                    
                except:
                    
                    price.append(None)
                
                try:
                    
                    date.append(entry[3].text)
                    
                except:
                    
                    date.append(None)
                
                try:
                    
                    year.append(float(ugh[1].text))
                    
                except:
                    
                    year.append(None)
                    
                try:
                    
                    feet.append(float(ugh[3].text.replace(',', '')))
                    
                except:
                    
                    feet.append(None)
                    
                try:
                    
                    style.append(ugh[17].text)
                    
                except:
                    
                    style.append(None)
                
                try:
                    
                    model.append(ugh[15].text)
                    
                except:
                    
                    model.append(None)
                    
                try:
                    
                    grade.append(ugh[19].text)
                    
                except:
                    
                    grade.append(None)
                    
                try:
                    
                    stories.append(float(ugh[23].text))
                    
                except:
                    
                    stories.append(None)
                    
                try:
                    
                    grade_adj.append(float(ugh[21].text))
                    
                except:
                    
                    grade_adj.append(None)
                    
                try:
                    
                    num_units.append(float(ugh[25].text))
                    
                except:
                    
                    num_units.append(None)
                    
                try:
                    
                    exwall1.append(float(ugh[31].text))
                    
                except:
                    
                    exwall1.append(None)
                    
                try:
                    
                    exwall2.append(float(ugh[33].text))
                    
                except:
                    
                    exwall2.append(None)
                    
                try:
                    
                    roof.append(ugh[27].text)
                    
                except:
                    
                    roof.append(None)
                    
                try:
                    
                    cover.append(ugh[29].text)
                    
                except:
                    
                    cover.append(None)
                    
                try:
                    
                    inwall1.append(ugh[41].text)
                    
                except:
                    
                    inwall1.append(None)
                    
                try:
                    
                    inwall2.append(ugh[43].text)
                    
                except:
                    
                    inwall2.append(None)
                    
                try:
                    
                    infloor1.append(ugh[47].text)
                    
                except:
                    
                    infloor1.append(None)
                    
                try:
                    
                    infloor2.append(ugh[49].text)
                    
                except:
                    
                    infloor2.append(None)
                
                try:
                    
                    fuel.append(ugh[37].text)
                    
                except:
                    
                    fuel.append(None)
                    
                try:
                    
                    heat.append(ugh[35].text)
                    
                except:
                    
                    heat.append(None)
                    
                try:
                    
                    ac.append(ugh[39].text)
                    
                except:
                    
                    ac.append(None)
                                        
                try:
                    
                    beds.append(float(ugh[55].text))
                    
                except:
                    
                    beds.append(None)
                    
                try:
                    
                    full.append(float(ugh[57].text))
                    
                except:
                    
                    full.append(None)
                    
                try:
                    
                    half.append(float(ugh[59].text))
                    
                except:
                    
                    half.append(None)
                    
                try:
                    
                    extra_fix.append(float(ugh[61].text))
                    
                except:
                    
                    extra_fix.append(None)
                    
                try:
                    
                    rooms.append(float(ugh[53].text))
                    
                except:
                    
                    rooms.append(None)
                    
                try:
                    
                    foundation.append(ugh[79].text)
                    
                except:
                    
                    foundation.append(None)
                    
                try:
                    
                    fireplace.append(float(ugh[65].text))
                    
                except:
                    
                    fireplace.append(None)
                    
                try:
                    
                    gar.append(ugh[89].text)
                    
                except:
                    
                    gar.append(None)
                    
                try:
                    
                    bsmt.append(ugh[81].text)
                    
                except:
                    
                    bsmt.append(None)
                                        
                try:
                    
                    use_code.append(dental[1].text)
                    
                except:
                    
                    use_code.append(None)
                    
                try:
                    
                    descr.append(dental[3].text.replace('  ', '').replace('\n', '').replace('\r', '').replace('\xa0', ''))
                    
                except:
                    
                    descr.append(None)
                    
                try:
                    
                    neighborhood.append(hood)
                    
                except:
                    
                    neighborhood.append(None)
                    
                try:
                    
                    acres.append(float(floss[1].text))
                    
                except:
                    
                    acres.append(None)
                    
                try:
                    
                    pids.append(PID)
                    
                except:
                    
                    pids.append(None)
                    
                try:
                    
                    address.append(x)
                    
                except:
                    
                    address.append(None)
                    
                try:
                    
                    typ.append(results_add.findAll('td')[2].text)
                    
                except:
                    
                    typ.append(None)
                
                if i == len(sales)-1:
                    
                    seller.append(None)
                    
                else:
                    
                    stuff = sales[i+1].findAll('td')
                    seller.append(stuff[0].text)
                
    except:
        
        continue

pids = pd.Series(pids, name = 'PID')
address = pd.Series(address, name = 'Address')
typ = pd.Series(typ, name = 'Type')
buyer = pd.Series(buyer, name = 'Buyer')
seller = pd.Series(seller, name = 'Seller')
price = pd.Series(price, name = 'Price')
date = pd.Series(date, name = 'Date')
year = pd.Series(year, name = 'Built')
feet = pd.Series(feet, name = 'SqFt')
style = pd.Series(style, name = 'Style')
model = pd.Series(model, name = 'Model')
grade = pd.Series(grade, name = 'Grade')
grade_adj = pd.Series(grade_adj, name = 'Grade_Adj')
stories = pd.Series(stories, name = 'Stories')
num_units = pd.Series(num_units, name = 'Number_of_Units')
roof = pd.Series(roof, name = 'Roof_Type')
cover = pd.Series(cover, name = 'Roof_Cover')
exwall1 = pd.Series(exwall1, name = 'Exterior_Wall1')
exwall2 = pd.Series(exwall2, name = 'Exterior_Wall2')
heat = pd.Series(heat, name = 'Heat_System')
fuel = pd.Series(fuel, name = 'Heat_Fuel')
ac = pd.Series(ac, name = 'AC_Type')
inwall1 = pd.Series(inwall1, name = 'Interior_Wall1')
inwall2 = pd.Series(inwall2, name = 'Interior_Wall2')
infloor1 = pd.Series(infloor1, name = 'Interior_Floor1')
infloor2 = pd.Series(infloor2, name = 'Interior_Floor2')
rooms = pd.Series(rooms, name = 'Rooms')
beds = pd.Series(beds, name = 'Bedrooms')
full = pd.Series(full, name = 'Full_Baths')
half = pd.Series(half, name = 'Half_Baths')
extra_fix = pd.Series(extra_fix, name = 'Extra_Fixtures')
fireplace = pd.Series(fireplace, name = 'Fireplaces')
foundation = pd.Series(foundation, name = 'Foundation')
gar = pd.Series(gar, name = 'Garage')
bsmt = pd.Series(bsmt, name = 'Basement')
use_code = pd.Series(use_code, name = 'Use_Code')
descr = pd.Series(descr, name = 'Use_Code_Description')
neighborhood = pd.Series(neighborhood, name = 'Neighborhood')
acres = pd.Series(acres, name = 'Acres')

Sales_df = pd.concat([pids, address, typ, buyer, seller, price, date, year, feet, style,
                      model, grade, grade_adj, stories, num_units, exwall1, exwall2, roof, cover, inwall1,
                      inwall2, infloor1, infloor2, heat, fuel, ac, beds, full, half, extra_fix, rooms,
                      foundation, fireplace, gar, bsmt, use_code, descr, neighborhood, acres], axis = 1)

Sales_df = Sales_df.replace('\xa0', None)

Sales_df.to_csv('D:/accidental_effect/data/winchester.csv', encoding = 'utf8', index = False)

