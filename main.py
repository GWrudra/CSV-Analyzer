import pandas as pd

def show_size(csv):
    partition()
    row,col=csv.shape
    print("No of Rows and Cols are :")
    print(f"Rows --> {row}")
    print(f"Columns --> {col}")
    partition()

def show_datatype(csv):
    partition()
    print("Columns --> DataType")
    for cur in csv.columns:
        print(f"{cur} --> {csv[cur].dtype}")
    partition()

def show_missing_values(csv):
    partition()
    print("No of null Values in each column are :\n",csv.isnull().sum())
    partition()

def show_statistics(csv):
    partition()
    #If Sales present 
    sf=True
    for col in csv.columns:
        if col.lower()=='sales':
            print(f"Highest Sales {csv['Sales'].max()}")
            print(f"Lowest Sales {csv['Sales'].min()}")
            print(f"Sales Sum {csv['Sales'].sum()}")
            print(f"Sales Mean {csv['Sales'].mean()}")
            print(f"Sales Median {csv['Sales'].median()}")
            sf=False

    #Else for any other Columns
    if sf:
        ch=input("Do you want to perform numberical operation on any col ? (Yes or No): ")
        if ch.lower()=="yes":
            ucol=input("Enter a valid column with numerical's")
            if ucol not in csv.columns :
                print("Sorry its invalid")
            elif not pd.api.types.is_numeric_dtype(csv[ucol]):
                print("Sorry its not numeric\n")
            else:
                print(f"Lowest {ucol} {csv[ucol].min()}")
                print(f"Highest {ucol} {csv[ucol].max()}")
                print(f"{ucol} Sum {csv[ucol].sum()}")
                print(f"{ucol} Mean {csv[ucol].mean()}")
                print(f"{ucol} Median {csv[ucol].median()}")
    partition()

def data_cleaning(csv):
    partition()
    #Replacing NAN values with mean/meadian(User choise)
    ch=input("Replace missing value's with mean or meadian : ")
    for col in csv.columns:
        if pd.api.types.is_numeric_dtype(csv[col]):
            if ch.lower()=="mean":
                csv[col]=csv[col].fillna(csv[col].mean())
            elif ch.lower()=="meadian":
                csv[col]=csv[col].fillna(csv[col].median())
            else:
                print("Wrong spelling")
        else:
            #Replacing NAN text with Unknown
            csv[col] = csv[col].fillna("Unknown")
        print("Cleaned")

    partition()

def save_file(csv):
    partition()
    fname=input("Enter file name(With .csv at the end) :")
    csv.to_csv(fname,index=False)
    print(f"\nCSV is Saved as {fname}")
    partition()

def show_disc(csv):
    partition()
    print(csv.describe().head())
    partition()

def show_corelation_matrix(csv):
    partition()
    print(csv.corr(numeric_only=True))
    partition()

def partition():
    print("\n=======X=======X=======X=======\n")
        

def main():
    #File path as input from user
    csv_file_path = input("Enter the path of the CSV file :")

    #Reading csv file from path
    try:
        csv_file=pd.read_csv(csv_file_path)
    except FileNotFoundError:
        print("file not found.")
        return
    except Exception as e:
        print(e)
        return

    while(True):
        print('''1.Size of the file
2.Columns and Datatype
3.Missing values
4.Statistics
5.Description of table
6.Data Cleaning
7.show_corealation_matrix
8.Save file
9.Exit
''')

        ch=int(input("Enter the option only(Number):"))
        if ch==1:
            show_size(csv_file)
        elif ch==2:
            show_datatype(csv_file)
        elif ch==3:
            show_missing_values(csv_file)
        elif ch==4:
            show_statistics(csv_file)
        elif ch==5:
            show_disc(csv_file)
        elif ch==6:
            data_cleaning(csv_file)
        elif ch==7:
            show_corelation_matrix(csv_file)
        elif ch==8:
            save_file(csv_file)
        else :
            break

main()