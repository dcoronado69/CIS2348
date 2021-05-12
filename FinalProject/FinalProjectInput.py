#------------------------------------------------------------------------------------------------------
#Part - 1
#------------------------------------------------------------------------------------------------------

import pandas as pd
from datetime import date

#Labels for the input files
manufacturer_List_Label = ["item ID","manufacturer","item type","damaged"]
price_List_Label = ["item ID","price"]
serviceDates_List_Label = ["item ID","service date"]

#Labels for the output files
full_Inventory_Label = ["item ID","manufacturer","item type","price","service date","damaged"]
itemType_Inventory_Label = ["item ID","manufacturer","price","service date","damaged"]
pastServiceDate_Inventory_Label = ["item ID","manufacturer","item type","price","service date","damaged"]
damaged_Inventory_Label = ["item ID","manufacturer","item type","price","service date"]

#Reading the csv files
manufacturerList = pd.read_csv('ManufacturerList1.csv', header=None)
priceList = pd.read_csv('PriceList1.csv', header=None)
serviceDatesList = pd.read_csv('ServiceDatesList1.csv', header=None)

#Assigning the column names
manufacturerList.columns = manufacturer_List_Label
priceList.columns = price_List_Label
serviceDatesList.columns = serviceDates_List_Label

#Joining the manufacturereList with the priceList when manufacturerList[item ID] == priceList[item ID]
mp = manufacturerList.merge(priceList, how='left')

#Joining the manufacturereList with the priceList when mp[item ID] == serviceDatesList[item ID]
mps = mp.merge(serviceDatesList ,how='left')

#today stores the present date for filtering out the items those past their service date
today = (date.today()).strftime("%m/%d/%Y")

#Creating 'full item Inventory' sorted according to 'manufacturer name' in the Ascending order
full_Inv = mps.sort_values(by=["manufacturer"])

#Creating 'item Inventory' sorted according to 'item ID' in the Ascending order
item_Inv = mps.sort_values(by=["item ID"])

#Creating 'past service date item Inventory' sorted according to 'service date' in the Ascending order
past_Inv = mps.sort_values(by=["service date"])

#Filtering the 'past service date item Inventory' by removing the the items whose service date is not passed
past_Inv['service date'] = pd.to_datetime(past_Inv['service date'])
past_Inv = past_Inv.set_index(["service date"])
past_Inv = past_Inv.sort_values(by=["service date"])
past_Inv = past_Inv.loc[:today]
past_Inv = past_Inv.merge(serviceDatesList, how='left')

#Creating an Inventory of the damaged Items 
damage_Inv = mps.loc[mps['damaged'] == 'damaged']

#Sorting 'Damaged Item Inventory' according to most expensive to least expensive
damage_Inv = damage_Inv.sort_values(by="price",ascending = False)

#Grouping the data of 'item Inventory' by 'item type'
item_Inv_group = item_Inv.groupby( item_Inv['item type']) 

#Saving the separate CSV files for each 'item type'
for ele in item_Inv_group.groups : 
	temp_df = item_Inv_group.get_group(ele)
	temp_df.to_csv(ele.capitalize()+"Inventory.csv",columns=itemType_Inventory_Label, header=False, index=False)

#Saving the CSV files for 'FullInventory','PastServiceDateInventory' and 'DamagedInventory'
full_Inv.to_csv("FullInventory.csv",columns=full_Inventory_Label, header=False, index=False)
past_Inv.to_csv("PastServiceDateInventory.csv",columns=pastServiceDate_Inventory_Label, header=False, index=False)
damage_Inv.to_csv("DamagedInventory.csv",columns=damaged_Inventory_Label, header=False, index=False)


#---------------------------------------------------------------------------------------------------------
#Part - 2
#---------------------------------------------------------------------------------------------------------

query = ""

#Filtering out the items whose service Date and are damaged is past
filtered_Inv = pd.concat([mps, past_Inv, past_Inv]).drop_duplicates(keep=False)
filtered_Inv = filtered_Inv[filtered_Inv['damaged'] != "damaged"]

query = input("Enter manufacturer name and Item Type (Press 'q' to quit )  :  ")	
while query.strip() != "q" :
	found = -1
	query_arr = query.split()
	temp = filtered_Inv.copy()
	col_name = 'manufacturer'
	for ele in query_arr:
		t = temp[temp[col_name].str.strip() == ele]
		if ((len(t) > 0) and (col_name == 'manufacturer')) :
			temp = t.copy()
			col_name = 'item type'
		elif ((len(t) > 0) and (col_name == 'item type')) :
			temp = t.copy()
			temp = temp[temp['price'] == temp['price'].max()]
			found = 1
			break

	if found == 1 :
                #Desired Item found 
		temp = temp.iloc[0]
		print("Your item is: %s, %s, %s, %s"%(temp['item ID'], temp['manufacturer'], temp['item type'], temp['price']))			

		suggest = filtered_Inv[(filtered_Inv['item type'].str.strip() == temp['item type'].strip()) & (filtered_Inv['manufacturer'].str.strip()!=temp['manufacturer'].strip())]
		suggest = suggest[suggest['price'] == suggest['price'].max()]

		if len(suggest) > 0 :
                        #Suggestion for the item found
			suggest = suggest.iloc[0]
			print("You may, also, consider: %s, %s, %s, %s, %s . "%(suggest['item ID'], suggest['manufacturer'], suggest['item type'], suggest['price'], suggest['service date'] ))
			
		else:
			pass

	else:
		print("No such item in inventory")

	query = input("Enter manufacturer name and Item Type (Press 'q' to quit ) :  ")
	









