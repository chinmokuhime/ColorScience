# tkinter - 使用者介面, 負責索引檔案路徑
# csv - CSV資料格式讀取
# numpy - 數值格式的轉換 (string, tuple, float, array), CSV檔案新建與資料寫入
# colour - 色差計算Function引用 (colour.delta_E(DATA 1, DATA 2, method='CIE 1976'))

from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
import csv
import numpy as np
import colour


# tkinter module - open file with browser GUI
root = Tk()
root.withdraw()
path = askopenfilename()
path2 = askopenfilename()
save_path = askdirectory()

# import the csv1's CIELab values as float type - lab_list
with open (path) as csvfile:
    readCSV = csv.DictReader(csvfile, delimiter=',')
    lab_list = []
    l = []
    a = []
    b = []
    for row in readCSV:
        l = row['LAB_L']
        a = row['LAB_A']
        b = row['LAB_B']
        if l or a or b.isdigit():
            l_n = float(l)
            a_n = float(a)
            b_n = float(b)
            lab_data = np.array([l_n, a_n, b_n])
            lab_list.append(lab_data)
            row_count = sum(1 for row in lab_list)+1 # 計算總行數
        
# import the csv2's CIELab values as float type - lab2_list
with open (path2) as csvfile:
    readCSVs = csv.DictReader(csvfile, delimiter=',')
    lab2_list = []
    l2 = []
    a2 = []
    b2 = []
    for row in readCSVs:
        l2 = row['LAB_L']
        a2 = row['LAB_A']
        b2 = row['LAB_B']
        if l2 or a2 or b2.isdigit():
            l2_n = float(l2);
            a2_n = float(a2);
            b2_n = float(b2);
            lab2_data = np.array([l2_n, a2_n, b2_n])
            lab2_list.append(lab2_data)

# Calculate delta_E
CIE_1976 = colour.delta_E(lab_list, lab2_list, method = 'CIE 1976')
CIE_1994 = colour.delta_E(lab_list, lab2_list, method = 'CIE 1994')
CIE_2000 = colour.delta_E(lab_list, lab2_list, method = 'CIE 2000')


# Create & write CSV file
serial_num = range(1,row_count)
np.savetxt(save_path +'/'+ 'delta_E.csv', np.column_stack((serial_num, CIE_1976,CIE_1994,CIE_2000)), delimiter=',', fmt = '%s', header ='Sample_ID, CIE_1976, CIE1994, CIE2000')

root.destroy()

