import pandas as pd

#File path as input from user
csv_file_path = input("Enter the path of the CSV file :")

#Reading csv file from path
csv_file=pd.read_csv(csv_file_path)

#Size of the CSV file
row,col=csv_file.shape
print(f"\nRows: {row}")
print(f"Columns: {col}")

#Shows Columns
print(f"\nColumns={csv_file.columns}")

#============================================================

#Finds Missing values
print("\nNo of null Values in each column are :\n",csv_file.isnull().sum())

#============================================================

#Calculating The max,min,sum,mean,medain

#For Sales if present 
sf=True
for col in csv_file.columns:
    if col=="Sales":
        print(f"\nHighest Sales {csv_file["Sales"].max()}")
        print(f"Lowest Sales {csv_file["Sales"].min()}")
        print(f"Sales Sum {csv_file["Sales"].sum()}")
        print(f"Sales Mean {csv_file["Sales"].mean()}")
        print(f"Sales Median {csv_file["Sales"].median()}\n")
        sf=False

#Else for any other Columns
if sf:
    ch=input("Do you want to perform numberical operation on any col ? (Yes or No): ")
    if ch.lower()=="yes":
        ucol=input("Enter a valid column with numerical's")
        if ucol in csv_file:
            print(f"Lowest {ucol} {csv_file[ucol].min()}")
            print(f"Highest {ucol} {csv_file[ucol].max()}")
            print(f"{ucol} Sum {csv_file[ucol].sum()}")
            print(f"{ucol} Mean {csv_file[ucol].mean()}")
            print(f"{ucol} Median {csv_file[ucol].median()}\n")
        else:
            print("Sorry its invalid\n")

#============================================================

#Data Cleaning
ch=input("Do you want to replace the missing values ? --> Yes or No :")
if ch.lower()=="yes":
    for col in csv_file.columns:
        if pd.api.types.is_numeric_dtype(csv_file[col]):
            #Replacing NAN values with meadian
            csv_file[col]=csv_file[col].fillna(csv_file[col].median())
        else:
            #Replacing NAN text with Unknown
            csv_file[col] = csv_file[col].fillna("Unknown")

#============================================================

#Saving the Creared file
csv_file.to_csv("cleaned_data.csv",index=False)
print("\nCSV is Saved as cleaned_data")

#============================================================

# print(csv_file.describe().head())
# print(csv_file.head())