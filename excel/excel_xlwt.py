import xlwt # 只支持.xls

# 创建新的workbook（其实就是创建新的excel）
workbook = xlwt.Workbook(encoding= 'ascii')

# 创建新的sheet表
worksheet = workbook.add_sheet("My new Sheet")

# 往表格写入内容
worksheet.write(0,0, "内容1")
worksheet.write(2,1, "内容2")

# 保存
workbook.save("新创建的表格.xls")

# 设置字体格式

# 初始化样式
style = xlwt.XFStyle()

# 为样式创建字体
font = xlwt.Font()
font.name = 'Times New Roman'   #字体
font.bold = True                #加粗
font.underline = True           #下划线
font.italic = True              #斜体

# 设置样式
style.font = font

# 往表格写入内容
worksheet.write(0,0, "内容1")
worksheet.write(2,1, "内容2",style)

# 设置列宽
# xlwt中列宽的值表示方法：默认字体0的1/256为衡量单位。
# xlwt创建时使用的默认宽度为2960，既11个字符0的宽度
# 所以我们在设置列宽时可以用如下方法：
# width = 256 * 20 256为衡量单位，20表示20个字符宽度
worksheet.col(0).width = 256*20

# 设置行高
style = xlwt.easyxf('font:height 360;')  # 18pt,类型小初的字号
row = worksheet.row(0)
row.set_style(style)

# 合并行和列
# 合并 第1行到第2行 的 第0列到第3列，最后一个是合并后的单元格中填什么
worksheet.write_merge(1, 2, 0, 3, 'Merge Test')

# 添加边框
# 设置边框样式
borders = xlwt.Borders()  # Create Borders

# May be:   NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR,
#           MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED,
#           MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
# DASHED虚线
# NO_LINE没有
# THIN实线

borders.left = xlwt.Borders.DASHED
borders.right = xlwt.Borders.DASHED
borders.top = xlwt.Borders.DASHED
borders.bottom = xlwt.Borders.DASHED
borders.left_colour = 0x40
borders.right_colour = 0x40
borders.top_colour = 0x40
borders.bottom_colour = 0x40

style = xlwt.XFStyle()  # Create Style
style.borders = borders  # Add Borders to Style

# 设置单元格背景色
# 创建样式
pattern = xlwt.Pattern()

# May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
pattern.pattern = xlwt.Pattern.SOLID_PATTERN

# May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow,
# 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow ,
# almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
pattern.pattern_fore_colour = 5
style = xlwt.XFStyle()

# 设置单元格对齐,其中horz代表水平对齐方式，vert代表垂直对齐方式。
# VERT_TOP = 0x00 上端对齐
# VERT_CENTER = 0x01 居中对齐（垂直方向上）
# VERT_BOTTOM = 0x02 低端对齐
# HORZ_LEFT = 0x01 左端对齐
# HORZ_CENTER = 0x02 居中对齐（水平方向上）
# HORZ_RIGHT = 0x03 右端对齐
# 设置样式
style = xlwt.XFStyle()
al = xlwt.Alignment()
al.horz = 0x02  # 设置水平居中
al.vert = 0x01  # 设置垂直居中
style.alignment = al