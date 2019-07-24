import xlrd
import os
import xlwt
from excelWT import write_excel


# 读取文件
def file_name(file_dir):   
    for root,dirs,files in os.walk(file_dir):  
        # print(root) #当前目录路径  
        # print(dirs) #当前路径下所有子目录  
        # print(files[0]) #当前路径下所有非目录子文件  
        return files

location="C://Users/SANG-ASUS/Desktop/weiboData"

dataCol1=[]
dataCol2=[]
if __name__ == '__main__':
    xls=file_name(location)
    for index in xls:
        print(index)
        workbook = xlrd.open_workbook(location+'/'+str(index))
        details1=workbook.sheet_by_index(0).col_values(0)
        details2=workbook.sheet_by_index(0).col_values(1)
        for d in details1:
                print(d)
                dataCol1.append(d)
        for d2 in details2:
                dataCol2.append(d2)

        

    print("正在写入")
    write_excel(dataCol1,dataCol2,520)
    print('success')
    

