# PeopleSoftID:1971072
import pandas as pd
from datetime import date

manufacturer_List_Label = ["item ID", "manufacturer", "item type", "damaged"]
price_List_Label = ["item ID", "price"]
serviceDates_List_Label = ["item ID", "service date"]

full_Inventory_Label = ["item ID", "manufacturer", "item type", "price", "service date", "damaged"]
itemType_Inventory_Label = ["item ID", "manufacturer", "price", "service date", "damaged"]
pastServiceDate_Inventory_Label = ["item ID", "manufacturer", "item type", "price", "service date", "damaged"]
damaged_Inventory_Label = ["item ID", "manufacturer", "item type", "price", "service date"]

manufacturerList = pd.read_csv('ManufacturerList1.csv', header=None)
priceList = pd.read_csv('PriceList1.csv', header=None)
serviceDatesList = pd.read_csv('ServiceDatesList1.csv', header=None)

# manufacturerList.fillna(0,inplace=True)

manufacturerList.columns = manufacturer_List_Label
priceList.columns = price_List_Label
serviceDatesList.columns = serviceDates_List_Label

mp = manufacturerList.merge(priceList, how='left')
mps = mp.merge(serviceDatesList, how='left')
today = (date.today()).strftime("%m/%d/%Y")

full_Inv = mps.sort_values(by=["manufacturer"])
item_Inv = mps.sort_values(by=["item ID"])
item_Inv = item_Inv.loc[item_Inv['item type'] == 'laptop']

past_Inv = mps.sort_values(by=["service date"])
past_Inv['service date'] = pd.to_datetime(past_Inv['service date'])
past_Inv = past_Inv.set_index(["service date"])
past_Inv = past_Inv.loc[:today]

past_Inv = past_Inv.merge(serviceDatesList, how='left')

damage_Inv = mps.loc[mps['damaged'] == 'damaged']



full_Inv.to_csv("FullInventory.csv", columns=full_Inventory_Label, header=False, index=False)
item_Inv.to_csv(" LaptopInventory.csv", columns=itemType_Inventory_Label, header=False, index=False)
past_Inv.to_csv("PastServiceDateInventory.csv", columns=pastServiceDate_Inventory_Label, header=False, index=False)
damage_Inv.to_csv("DamagedInventory.csv", columns=damaged_Inventory_Label, header=False, index=False)
