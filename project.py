import pandas as pd
import matplotlib.pyplot as plt     

df = pd.read_csv('gurgaon_real_estate.csv')
print(df.head())

#data cleaning

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)
    



print(df.columns)


#Numercal column cleaning (Price, rate_per_sqft,)


df["price"] = df["price"].str.replace(",", "", regex=False)
df["price"] = df["price"].astype(float)
df["price"] = df["price"].astype(int)
print(df["price"].dtype)
print(df["price"].head())

df["rate_per_sqft"] = df["rate_per_sqft"].str.replace(",", "", regex=False)
df["rate_per_sqft"] = df["rate_per_sqft"].astype(float)
df["rate_per_sqft"] = df["rate_per_sqft"].astype(int)
print(df["rate_per_sqft"].dtype)
print(df["rate_per_sqft"].head())


df["bhk_count"] = df["bhk_count"].astype(int)

print(df["bhk_count"].dtype)
print(df["bhk_count"].head())

#categorical column cleaning (Status)


df["status"] = (
df["status"]
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")  
)

print(df["status"].value_counts())

#rera approval cleaning

df["rera_approval"] = (
    df["rera_approval"]
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print(df["rera_approval"].value_counts())

#flat_type cleaning
df["flat_type"] = (
    df["flat_type"]
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)
print(df["flat_type"].value_counts())

#cheching for null values

print(df.isnull().sum())

#check duplicates



df = df.drop_duplicates()

print(df.duplicated().sum())
print(df.shape)


# Business Questions to Answer


#Q1. Which is the costliest flat in the dataset?

highest_price_index = df["price"].idxmax()
costliest_flat = df.loc[highest_price_index]
print(costliest_flat)

#Q2 Which locality has the highest average price?

locality_avg_price = df.groupby("locality")["price"].mean()
print(locality_avg_price.idxmax())


#Q3 Which locality has the highest rate per sqfr price?


locality_avg_rate = df.groupby("locality")["rate_per_sqft"].mean()
Highest_locality = locality_avg_rate.idxmax()
Highest_rate = locality_avg_rate.max()

print(f"Highest_locality: {Highest_locality}")
print(f"Highest_avg rate per sqft: {Highest_rate}")



#Q4 Do ready-to-move properties cost more than under-construction properties?

status_avg_price = df.groupby("status")["price"].mean()
print(status_avg_price)

if status_avg_price["ready_to_move"] > status_avg_price["under_construction"]:
    print("Ready to move properties cost more")

else:
    print("Under constructio cost more")


print("========== Q5 START ==========")
    #Q5. Do RERA-approved properties command a price premium?
   

rera_avg_price = df.groupby("rera_approval")["price"].mean()
print(rera_avg_price)

if rera_avg_price["approved_by_rera"] > rera_avg_price["not_approved_by_rera"]:
        print("Rera approved prices is higher")


else:
        print("not rera approved price is higher")



    #Q6 How does area (sqft) impact property price?

#plt.scatter(df["area"], df["price"])
#plt.title("Area vs Price")
#plt.xlabel("Area (Sqft)")
#plt.ylabel("Price")
#plt.show()
 

   #Q7 Which BHK configuration is the most expensive on average?


bhk_avg_price = df.groupby("bhk_count")["price"].mean()
print(bhk_avg_price)

print("Most Expensive BHK Configuration")
print(bhk_avg_price.idxmax())



     #Q8:Which property type (Apartment, Floor, Plot) is the costliest?

property_type_avg_price = df.groupby("property_type")["price"].mean()
print(property_type_avg_price)

print("Most Expensive Property")
print(property_type_avg_price.idxmax())


     #Q9: Do certain builders price higher?

builder_avg_price = df.groupby("builder_name")["price"].mean()
print(builder_avg_price)

print(builder_avg_price.idxmax())

#Answer9 : Yes, certain builders do command higher average prices. In this dataset, Harish has the highest average property price among the builders.


#Q10: Are larger homes always more expensive per square foot?
plt.scatter(df["area"], df["rate_per_sqft"])

plt.xlabel("Area (sqft) ")
plt.ylabel("Rate per square foot")
plt.title("Area Vs Rate per square foot")

plt.show()

#Q10 Answer: Larger homes are not necessarily more expensive per square foot. The scatter plot suggests that price per square foot tends to be higher for smaller properties, while larger properties generally show lower or more varied rates per square foot.