import pandas as pd

def show_size(csv):
    row,col=csv.shape
    print("\nNo of Rows and Cols are :")
    print(f"Rows --> {row}")
    print(f"Columns --> {col}")

def show_datatype(csv):
    print("\nColumns --> DataType")
    for cur in csv.columns:
        print(f"{cur} --> {csv[cur].dtype}")

def show_missing_values(csv):
    print("\nNo of null Values in each column are :\n",csv.isnull().sum())

def show_statistics(csv):
    #If Sales present 
    sf=True
    for col in csv.columns:
        if col.lower()=='sales':
            print(f"\nHighest Sales {csv['Sales'].max()}")
            print(f"Lowest Sales {csv['Sales'].min()}")
            print(f"Sales Sum {csv['Sales'].sum()}")
            print(f"Sales Mean {csv['Sales'].mean()}")
            print(f"Sales Median {csv['Sales'].median()}\n")
            sf=False

    #Else for any other Columns
    if sf:
        ch=input("\nDo you want to perform numberical operation on any col ? (Yes or No): ")
        if ch.lower()=="yes":
            ucol=input("Enter a valid column with numerical's")
            if ucol not in csv.columns :
                print("Sorry its invalid\n")
            elif not pd.api.types.is_numeric_dtype(csv[ucol]):
                print("Sorry its not numeric\n")
            else:
                print(f"Lowest {ucol} {csv[ucol].min()}")
                print(f"Highest {ucol} {csv[ucol].max()}")
                print(f"{ucol} Sum {csv[ucol].sum()}")
                print(f"{ucol} Mean {csv[ucol].mean()}")
                print(f"{ucol} Median {csv[ucol].median()}\n")                

def data_cleaning(csv):
    ch=input("Do you want to replace the missing values ? --> Yes or No :")
    if ch.lower()=="yes":
        for col in csv.columns:
            if pd.api.types.is_numeric_dtype(csv[col]):
                #Replacing NAN values with meadian
                csv[col]=csv[col].fillna(csv[col].median())
            else:
                #Replacing NAN text with Unknown
                csv[col] = csv[col].fillna("Unknown")

def save_file(csv):
    ch=input("Do you want to save the cleaned data (Yes or No) :")
    if ch.lower()=="yes":
        fname=input("Enter file name(With .csv at the end) :")
        csv.to_csv(fname,index=False)
        print("\nCSV is Saved as cleaned_data")

def main():
    #File path as input from user
    csv_file_path = input("Enter the path of the CSV file :")

    #Reading csv file from path
    try:
        csv_file=pd.read_csv(csv_file_path)
    except FileNotFoundError:
        print("file not found.")
    except Exception as e:
        print(e)
        return

    #Size of the CSV file
    show_size(csv_file)

    #Shows Columns and Datatype
    show_datatype(csv_file)

    #Finds Missing values
    show_missing_values(csv_file)

    #Calculating The max,min,sum,mean,medain
    show_statistics(csv_file)

    #Data Cleaning
    data_cleaning(csv_file)

    #Saving the Creared file
    save_file(csv_file)

    # print(csv_file.describe().head())
    # print(csv_file.head())

main()