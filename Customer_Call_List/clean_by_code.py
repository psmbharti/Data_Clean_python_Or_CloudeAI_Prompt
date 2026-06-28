import pandas as pd

df = pd.read_excel(r"C:\Users\madhu\OneDrive\Desktop\GITHUB_Resume_Projects\Data_Cleaning_Python\Customer_Call_List\Customer Call List.xlsx")
#print(df)

df = df.drop_duplicates()
#print (df)

df= df.drop(columns = "Not_Useful_Column")
#print(df)

# df["Last_Name"] = df["Last_Name"].str.lstrip("...")
# df["Last_Name"] = df["Last_Name"].str.lstrip("/")
# df["Last_Name"] = df["Last_Name"].str.rstrip("_")
#or at once
df["Last_Name"] = df["Last_Name"].str.strip("._/")
#print(df["Last_Name"])

# Step 1: convert to string
df["Phone_Number"] = df["Phone_Number"].astype(str)

# Step 2: remove ALL non-digit characters
df["Phone_Number"] = df["Phone_Number"].str.replace(r"\D", "", regex=True)

# Step 3: format only valid 10-digit numbers as XXX-XXX-XXXX
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + "-" + x[3:6] + "-" + x[6:10])
df["Phone_Number"] = df["Phone_Number"].replace("--", "")
#print(df['Phone_Number'])

df[['Street_Address', 'State', 'Zip_code']] = df['Address'].str.split(',', n=2, expand=True)

#print(df[['Street_Address', 'State', 'Zip_code']])

df['Paying Customer'] = df['Paying Customer'].str.replace('Yes','Y')
df['Paying Customer'] = df['Paying Customer'].str.replace('No','N')
#print(df['Paying Customer'])

df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Yes','Y')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('No','N')
#print(df['Do_Not_Contact'])

df = df.fillna('')
#print(df)

df = df[df["Do_Not_Contact"] != "Y"]
#print(df["Do_Not_Contact"])

df = df[df["Phone_Number"] != ""]

df= df.drop(columns = "Address")

df = df.reset_index(drop=True)

#print(df)


df.to_excel(r"C:\Users\madhu\OneDrive\Desktop\GITHUB_Resume_Projects\Data_Cleaning_Python\Customer_Call_List\clean_by_code.xlsx",index=False)
print("Successfully created clean_by_code.xlsx")


