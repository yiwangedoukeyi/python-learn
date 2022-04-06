from selenium import webdriver

# 如果没有设置路径，将从PATH中查找
driver = webdriver.Chrome('F:\\python_learn\\chromedriver_win32\\chromedriver')
driver.get('http://www.baidu.com/')

#元素定位
driver.find_element_by_id(1)
driver.find_element_by_name()
driver.find_element_by_class_name()
driver.find_element_by_tag_name()
driver.find_element_by_link_text()
driver.find_element_by_partial_link_text()
driver.find_element_by_xpath()
driver.find_element_by_css_selector()

# 新版本用这种方式
from selenium.webdriver.common.by import By
driver.find_element(By.XPATH,'//*[@id="pvExplorationHost"]/div')


# 控制浏览器大小
driver.set_window_size(480, 800)

# 后退 
driver.back()

# 前进 
driver.forward()

# 刷新
driver.refresh()

# 点击和输入
driver.find_element_by_id("kw").clear() # 清除文本 
driver.find_element_by_id("kw").send_keys("selenium") # 模拟按键输入 
driver.find_element_by_id("su").click() # 点击元素

# 提交
search_text = driver.find_element_by_id('kw') 
search_text.send_keys('selenium') 
search_text.submit()

#属性
search_text.size() # 尺寸
search_text.text() # 文本
search_text.get_attribute(name) # 属性值
search_text.is_displayed() # 设置该元素是否用户可见

# 鼠标操作
from selenium.webdriver.common.action_chains import ActionChains
perform() #执行所有 ActionChains 中存储的行为；
context_click() #右击；
double_click() # 双击；
drag_and_drop() # 拖动；
move_to_element() #鼠标悬停。

# 定位到要悬停的元素
above = driver.find_element_by_link_text("设置")
# 对定位到的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(above).perform()

# 键盘事件
send_keys(Keys.BACK_SPACE) # 删除键（BackSpace）
send_keys(Keys.SPACE) # 空格键(Space)
send_keys(Keys.TAB) # 制表键(Tab)
send_keys(Keys.ESCAPE) # 回退键（Esc）
send_keys(Keys.ENTER) # 回车键（Enter）
send_keys(Keys.CONTROL,'a') # 全选（Ctrl+A）
send_keys(Keys.CONTROL,'c') # 复制（Ctrl+C）
send_keys(Keys.CONTROL,'x') # 剪切（Ctrl+X）
send_keys(Keys.CONTROL,'v') # 粘贴（Ctrl+V）
send_keys(Keys.F1) # 键盘 F1
# 输入框输入内容
driver.find_element_by_id("kw").send_keys("seleniumm")

# 删除多输入的一个
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

# 获取断言信息
title = driver.title # 打印当前页面title
now_url = driver.current_url # 打印当前页面URL
user = driver.find_element_by_class_name('nums').text # # 获取结果数目

# 等待页面加载完成
#显示等待
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

element = WebDriverWait(driver, 5, 0.5).until(
                      EC.presence_of_element_located((By.ID, "kw"))
                      )
element.send_keys('selenium')
driver.quit()
WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)

# driver ：浏览器驱动。
# timeout ：最长超时时间，默认以秒为单位。
# poll_frequency ：检测的间隔（步长）时间，默认为0.5S。
# ignored_exceptions ：超时后的异常信息，默认情况下抛NoSuchElementException异常。
# WebDriverWait()一般由until()或until_not()方法配合使用，下面是until()和until_not()方法的说明。
# until(method, message=‘’) 调用该方法提供的驱动程序作为一个参数，直到返回值为True。
# until_not(method, message=‘’) 调用该方法提供的驱动程序作为一个参数，直到返回值为False。

# 隐式等待
# 如果某些元素不是立即可用的，隐式等待是告诉WebDriver去等待一定的时间后去查找元素。 默认等待时间是0秒，一旦设置该值，隐式等待是设置该WebDriver的实例的生命周期。

from selenium import webdriver
driver = webdriver.Firefox()    
driver.implicitly_wait(10) # seconds    
driver.get("http://somedomain/url_that_delays_loading")    
myDynamicElement = driver.find_element_by_id("myDynamicElement") 

# 在不同的窗口和框架之间移动
driver.switch_to_window("windowName")
driver.switch_to_frame("frameName")
# 以直接取表单的id 或name属性。如果iframe没有可用的id和name属性，则可以通过下面的方式进行定位。

#先通过xpth定位到iframe
xf = driver.find_element_by_xpath('//*[@id="x-URS-iframe"]')

#再将定位对象传给switch_to_frame()方法
driver.switch_to_frame(xf)
# 一旦我们完成了frame中的工作，我们可以这样返回父frame:

driver.switch_to_default_content()
# 警告框处理
alert = driver.switch_to_alert()
alert.text() # 返回 alert/confirm/prompt 中的文字信息。
alert.accept() # 接受现有警告框。
alert.dismiss() # 解散现有警告框。
alert.send_keys(keysToSend) # 发送文本至警告框。keysToSend：将文本发送至警告框。

# 下拉框选择
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')
sel = driver.find_element_by_xpath("//select[@id='nr']")
select = Select(sel)
select.select_by_value('50')  # 显示50条
select.select_by_index(index)
select.select_by_visible_text("text")
select.deselect_all() # 全部取消选择

# 文件上传
driver.find_element_by_name("file").send_keys('D:\\upload_file.txt')  # # 定位上传按钮，添加本地文件

# cookie操作
# WebDriver操作cookie的方法：

driver.get_cookies() # 获得所有cookie信息。
driver.get_cookie(name) # 返回字典的key为“name”的cookie信息。
driver.add_cookie(cookie_dict) # 添加cookie。“cookie_dict”指字典对象，必须有name 和value 值。
driver.delete_cookie(name,optionsString) # 删除cookie信息。“name”是要删除的cookie的名称，“optionsString”是该cookie的选项，目前支持的选项包括“路径”，“域”。
driver.delete_all_cookies() # 删除所有cookie信息

# 调用JavaScript代码
js="window.scrollTo(100,450);"
driver.execute_script(js) # 通过javascript设置浏览器窗口的滚动条位置
# 通过execute_script()方法执行JavaScripts代码来移动滚动条的位置。

# 窗口截图
driver.get_screenshot_as_file("D:\\baidu_img.jpg") # 截取当前窗口，并指定截图图片的保存位置

# 关闭浏览器
close() 关闭单个窗口
quit() 关闭所有窗口

# 手动获取网页的cookie，将其序列化并存储在本地，此方法需要将cookie的各个格式一起添加
# 可以使用https://www.editthiscookie.com/ 这上面的chrome插件将cookie存为列表
# 写入代码
for item in cookies:
    driver.add_cookie(item)
