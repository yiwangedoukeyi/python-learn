# 2.1.0版本后，xlrd只支持.xls, 在此之前，可以支持.xlsx
import xlrd 

data = xlrd.open_workbook(filename) # 文件名以及路径，如果路径或者文件名有中文给前面加一个 r

#获取excel文件的一个工作表
table = data.sheets()[0]                    #通过索引顺序获取
table = data.sheet_by_index(sheet_indx)     #通过索引顺序获取
table = data.sheet_by_name(sheet_name)      #通过名称获取

# 以上三个函数都会返回一个xlrd.sheet.Sheet()对象

names = data.sheet_names()                  #返回book中所有工作表的名字
data.sheet_loaded(sheet_name or indx)       # 检查某个sheet是否导入完毕

# 行操作
nrows = table.nrows
    # 获取该sheet中的行数，注，这里table.nrows后面不带().

table.row(rowx)
    # 返回由该行中所有的单元格对象组成的列表,这与tabel.raw()方法并没有区别。

table.row_slice(rowx)
    # 返回由该行中所有的单元格对象组成的列表

table.row_types(rowx, start_colx=0, end_colx=None)
    # 返回由该行中所有单元格的数据类型组成的列表；　　　　
    # 返回值为逻辑值列表，若类型为empy则为0，否则为1

table.row_values(rowx, start_colx=0, end_colx=None)
    # 返回由该行中所有单元格的数据组成的列表

table.row_len(rowx)
    # 返回该行的有效单元格长度，即这一行有多少个数据

# 列操作
ncols = table.ncols
    # 获取列表的有效列数

table.col(colx, start_rowx=0, end_rowx=None)
    # 返回由该列中所有的单元格对象组成的列表

table.col_slice(colx, start_rowx=0, end_rowx=None)
    # 返回由该列中所有的单元格对象组成的列表

table.col_types(colx, start_rowx=0, end_rowx=None)
    # 返回由该列中所有单元格的数据类型组成的列表

table.col_values(colx, start_rowx=0, end_rowx=None)
    # 返回由该列中所有单元格的数据组成的列表

# 单元格操作
table.cell(rowx,colx)
    # 返回单元格对象

table.cell_type(rowx,colx)
    # 返回对应位置单元格中的数据类型

table.cell_value(rowx,colx)
    # 返回对应位置单元格中的数据