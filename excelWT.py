import xlwt
from datetime import datetime


#设置表格样式
def set_style(name,height,bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style

#写Excel
def write_excel(dat1,dat2,pageIndex):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('微博数据',cell_overwrite_ok=True)
    # row0 = ["姓名","年龄","出生日期","爱好"]
    # colum0 = ["张三","李四","恋习Python","小明","小红","无名"]

    # 从0开始算 所以3是第4行
    # 从0开始算 所以5是第6列
    # dat为数组
    i=0
    while i< len(dat1):
        sheet1.write(i,0,dat1[i])
        sheet1.write(i,1,dat2[i])
        
        i=i+1



    # #写第一行
    # for i in range(0,len(row0)):
    #     sheet1.write(0,i,row0[i],set_style('Times New Roman',220,True))
    # #写第一列
    # for i in range(0,len(colum0)):
    #     sheet1.write(i+1,0,colum0[i],set_style('Times New Roman',220,True))

    # sheet1.write(1,3,'2006/12/12')
    # sheet1.write_merge(4,5,3,3,'打篮球')

    f.save('微博数据%s-P%d.xls' % (datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),pageIndex))
    
    

if __name__ == '__main__':
    dat1=["da1"]

    dat2=["da1"]
    write_excel(dat1,dat2,0)
    print('success')
    

    