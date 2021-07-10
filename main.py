import os
import functions
import utilities

try:
    import pandas
    import openpyxl
    from tkinter import Tk  # from tkinter import Tk for Python 3.x
    from tkinter.filedialog import askopenfilename
except ImportError:
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    import pandas
    import openpyxl
    from tkinter import Tk  # from tkinter import Tk for Python 3.x
    from tkinter.filedialog import askopenfilename


def read_file_to_df(filename):
    try:
        excel_df = pandas.read_excel(filename)
    except FileNotFoundError:
        raise FileNotFoundError("Bad file name. Try Again.")
    except ValueError:
        raise ValueError("Probably picked a file that isn't an excel file.")
    except Exception as e:
        print("Something really bad happened: " + e)
        exit(1)
    return excel_df

def get_filename():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    return filename

def get_functions(module):
    ret = []
    for i in dir(module):
        f = getattr(module, i)
        if callable(f):
            ret.append(f)
    return ret

def get_start_row(df):
    df_shape = df.shape
    print(df)
    max_start_row = df_shape[0]-1
    while True:
        start = input("Enter start row (0 to "+str(max_start_row)+"). 0 for all rows in dataframe, "+str(max_start_row)+" for the last row only.:\n")
        try:
            start = int(start)
            if 0 <= start <= max_start_row:
                return [start, max_start_row]
            else:
                print("Number not in range. Try again.")
        except:
            print("Try again.")

if __name__ == '__main__':

    funcs = get_functions(functions)
    filename = get_filename()
    df = read_file_to_df(filename)
    start_row, end_row = get_start_row(df)
    if start_row>0:
        df = df.iloc[start_row:end_row+1]
    for func in funcs:
        func_name = func.__name__
        _, column_name = func_name.split("_",1)
        df[column_name] = df.apply(func, start_row=start_row, axis=1)

    print(df)

