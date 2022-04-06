import xlwings as xw

# 打开Excel程序，默认设置：程序可见，只打开不新建工作薄
app = xw.App(visible=True,add_book=False)
app.display_alerts=False
app.screen_updating=False
#新建工作簿 (如果不接下一条代码的话，Excel只会一闪而过，卖个萌就走了）
wb = app.books.add()
# 打开已有工作簿（支持绝对路径和相对路径）
wb = app.books.open('example.xlsx')
#练习的时候建议直接用下面这条
#wb = xw.Book('example.xlsx')
#这样的话就不会频繁打开新的Excel

#保存工作簿
wb.save('example.xlsx')

# 退出工作簿（可省略）
wb.close()
# 退出Excel
app.quit()

# wb就是新建的工作簿(workbook)，下面则对wb的sheet1的A1单元格赋值
wb.sheets['sheet1'].range('A1').value='人生'

# 按名字引用工作簿，注意工作簿应该首先被打开
wb=xw.books['工作簿的名字']

# 引用活动的工作薄
wb=xw.books.active

# 引用工作簿中的sheet
sht=xw.books['工作簿的名字'].sheets['sheet的名字']
# 或者
wb=xw.books['工作簿的名字']
sht=wb.sheets['sheet的名字']

# 读取写入数据
sht.range('a1').value = 'Hello'

# 行存储：将列表[1,2,3]储存在A1：C1中
sht.range('A1').value=[1,2,3]
# 列存储：将列表[1,2,3]储存在A1:A3中
sht.range('A1').options(transpose=True).value=[1,2,3]
# 将2x2表格，即二维数组，储存在A1:B2中，如第一行1，2，第二行3，4
sht.range('A1').options(expand='table')=[[1,2],[3,4]]

#按行插入
sht.range('a1').value = [1,2,3,4]
#等同于
sht.range('a1:d1').value = [1,2,3,4]

# 按列插入
sht.range('a2').options(transpose=True).value = [5,6,7,8]
# 多行输入
sht.range('a6').expand('table').value = [['a','b','c'],['d','e','f'],['g','h','i']]

# 将A1的值，读取到a变量中
a=sht.range('A1').value

#将A1到A2的值，读取到a列表中
a=sht.range('A1:A2').value
# 将第一行和第二行的数据按二维数组的方式读取
a=sht.range('A1:B2').value

# 选取一列的数据
# 先计算单元格的行数(前提是连续的单元格)
rng = sht.range('a1').expand('table')
nrows = rng.rows.count

# 接着就可以按准确范围读取了
a = sht.range(f'a1:a{nrows}').value

# 选取一行的数据
ncols = rng.columns.count

#用切片
fst_col = sht[0,:ncols].value

# 常用函数和方法
# 1.Book工作薄常用的api
wb=xw.books[‘工作簿名称']
wb.activate() # 激活为当前工作簿
wb.fullname # 返回工作簿的绝对路径
wb.name # 返回工作簿的名称
wb.save(path=None) # 保存工作簿，默认路径为工作簿原路径，若未保存则为脚本所在的路径
wb.close() # 关闭工作簿

# 引用Excel程序中，当前的工作簿
wb=xw.books.acitve
# 返回工作簿的绝对路径
x=wb.fullname
# 返回工作簿的名称
x=wb.name
# 保存工作簿，默认路径为工作簿原路径，若未保存则为脚本所在的路径
x=wb.save(path=None)
# 关闭工作簿
x=wb.close()

# sheet常用的api
# 引用某指定sheet
sht=xw.books['工作簿名称'].sheets['sheet的名称']
# 激活sheet为活动工作表
sht.activate()
# 清除sheet的内容和格式
sht.clear()
# 清除sheet的内容
sht.contents()
# 获取sheet的名称
sht.name
# 删除sheet
sht.delete

range常用的api
# 引用当前活动工作表的单元格
rng=xw.Range('A1')
# 加入超链接
# rng.add_hyperlink(r'www.baidu.com','百度',‘提示：点击即链接到百度')
# 取得当前range的地址
rng.address
rng.get_address()
# 清除range的内容
rng.clear_contents()
# 清除格式和内容
rng.clear()
# 取得range的背景色,以元组形式返回RGB值
rng.color
# 设置range的颜色
rng.color=(255,255,255)
# 清除range的背景色
rng.color=None
# 获得range的第一列列标
rng.column
# 返回range中单元格的数据
rng.count
# 返回current_region
rng.current_region
# 返回ctrl + 方向
rng.end('down')
# 获取公式或者输入公式
rng.formula='=SUM(B1:B5)'
# 数组公式
rng.formula_array
# 获得单元格的绝对地址
rng.get_address(row_absolute=True, column_absolute=True,include_sheetname=False, external=False)
# 获得列宽
rng.column_width
# 返回range的总宽度
rng.width
# 获得range的超链接
rng.hyperlink
# 获得range中右下角最后一个单元格
rng.last_cell
# range平移
rng.offset(row_offset=0,column_offset=0)
#range进行resize改变range的大小
rng.resize(row_size=None,column_size=None)
# range的第一行行标
rng.row
# 行的高度，所有行一样高返回行高，不一样返回None
rng.row_height
# 返回range的总高度
rng.height
# 返回range的行数和列数
rng.shape
# 返回range所在的sheet
rng.sheet
#返回range的所有行
rng.rows
# range的第一行
rng.rows[0]
# range的总行数
rng.rows.count
# 返回range的所有列
rng.columns
# 返回range的第一列
rng.columns[0]
# 返回range的列数
rng.columns.count
# 所有range的大小自适应
rng.autofit()
# 所有列宽度自适应
rng.columns.autofit()
# 所有行宽度自适应
rng.rows.autofit()

books 工作簿集合的api
# 新建工作簿
xw.books.add()
# 引用当前活动工作簿
xw.books.active
4.sheets 工作表的集合

# 新建工作表
xw.sheets.add(name=None,before=None,after=None)
# 引用当前活动sheet
xw.sheets.active

# 数据结构
# 1.一维数据

# python的列表，可以和Excel中的行列进行数据交换，python中的一维列表，在Excel中默认为一行数据。
sht=xw.sheets.active
# 将1，2，3分别写入了A1，B1，C1单元格中
sht.range('A1').value=[1,2,3]
# 将A1，B1，C1单元格的值存入list1列表中
list1=sht.range('A1:C1').value
# 将1，2，3分别写入了A1，A2，A3单元格中
sht.range('A1').options(transpose=True).value=[1,2,3]
# 将A1，A2，A3单元格中值存入list1列表中
list1=sht.range('A1:A3').value

# 2.二维数据
# python的二维列表，可以转换为Excel中的行列。二维列表，即列表中的元素还是列表。在Excel中，二维列表中的列表元素，代表Excel表格中的一列。例如：

# 将a1,a2,a3输入第一列，b1,b2,b3输入第二列
list1=[[‘a1’,'a2','a3'],['b1','b2','b3']]
sht.range('A1').value=list1
# 将A1：B3的值赋给二维列表list1
list1=sht.range('A1:B3').value
3.Excel中区域的选取表格

# 选取第一列
rng=sht. range('A1').expand('down')
rng.value=['a1','a2','a3']

# 选取第一行
rng=sht.range('A1').expand('right')
rng=['a1','b1']

# 选取表格
rng.sht.range('A1').expand('table')
rng.value=[[‘a1’,'a2','a3'],['b1','b2','b3']]

# 生成图表的方法
app = xw.App()
wb = app.books.active
sht = wb.sheets.active

chart = sht.charts.add(100, 10)  # 100, 10 为图表放置的位置坐标。以像素为单位。
chart.set_source_data(sht.range('A1').expand())  # 参数为表格中的数据区域。
# chart.chart_type = i               # 用来设置图表类型，具体参数件下面详细说明。
chart.api[1].ChartTitle.Text = i          # 用来设置图表的标题。

import xlwings as xw
app = xw.App()
wb = app.books.active
sht = wb.sheets.active
# 生成图表的数据
sht.range('A1').value = [['时间', '数量'], ['1日', 2], ['2日', 1], ['3日', 3]
             , ['4日', 4], ['5日', 5], ['6日', 6]]
"""图表类型参数，被注释的那几个，无法生成对应的图表"""
dic = {
  '3d_area': -4098,
  '3d_area_stacked': 78,
  '3d_area_stacked_100': 79,
  '3d_bar_clustered': 60,
  '3d_bar_stacked': 61,
  '3d_bar_stacked_100': 62,
  '3d_column': -4100,
  '3d_column_clustered': 54,
  '3d_column_stacked': 55,
  '3d_column_stacked_100': 56,
  '3d_line': -4101,
  '3d_pie': -4102,
  '3d_pie_exploded': 70,
  'area': 1,
  'area_stacked': 76,
  'area_stacked_100': 77,
  'bar_clustered': 57,
  'bar_of_pie': 71,
  'bar_stacked': 58,
  'bar_stacked_100': 59,
  'bubble': 15,
  'bubble_3d_effect': 87,
  'column_clustered': 51,
  'column_stacked': 52,
  'column_stacked_100': 53,
  'cone_bar_clustered': 102,
  'cone_bar_stacked': 103,
  'cone_bar_stacked_100': 104,
  'cone_col': 105,
  'cone_col_clustered': 99,
  'cone_col_stacked': 100,
  'cone_col_stacked_100': 101,
  'cylinder_bar_clustered': 95,
  'cylinder_bar_stacked': 96,
  'cylinder_bar_stacked_100': 97,
  'cylinder_col': 98,
  'cylinder_col_clustered': 92,
  'cylinder_col_stacked': 93,
  'cylinder_col_stacked_100': 94,
  'doughnut': -4120,
  'doughnut_exploded': 80,
  'line': 4,
  'line_markers': 65,
  'line_markers_stacked': 66,
  'line_markers_stacked_100': 67,
  'line_stacked': 63,
  'line_stacked_100': 64,
  'pie': 5,
  'pie_exploded': 69,
  'pie_of_pie': 68,
  'pyramid_bar_clustered': 109,
  'pyramid_bar_stacked': 110,
  'pyramid_bar_stacked_100': 111,
  'pyramid_col': 112,
  'pyramid_col_clustered': 106,
  'pyramid_col_stacked': 107,
  'pyramid_col_stacked_100': 108,
  'radar': -4151,
  'radar_filled': 82,
  'radar_markers': 81,
  # 'stock_hlc': 88,
  # 'stock_ohlc': 89,
  # 'stock_vhlc': 90,
  # 'stock_vohlc': 91,
  # 'surface': 83,
  # 'surface_top_view': 85,
  # 'surface_top_view_wireframe': 86,
  # 'surface_wireframe': 84,
  'xy_scatter': -4169,
  'xy_scatter_lines': 74,
  'xy_scatter_lines_no_markers': 75,
  'xy_scatter_smooth': 72,
  'xy_scatter_smooth_no_markers': 73
}
w = 385
h = 241
n = 0
x = 100
y = 10
for i in dic.keys():
    xx = x + n % 3*w  # 用来生成图表放置的x坐标。
    yy = y + n//3*h   # 用来生成图表放置的y坐标。
    chart = sht.charts.add(xx, yy)
    chart.set_source_data(sht.range('A1').expand())
    chart.chart_type = i
    chart.api[1].ChartTitle.Text = i
    n += 1
wb.save('chart_图表')
wb.close()
app.quit()