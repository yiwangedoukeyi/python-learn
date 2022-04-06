from selenium import webdriver

option = webdriver.ChromeOptions()

# 添加启动参数
option.add_argument()

# 添加扩展应用 
option.add_extension()
option.add_encoded_extension()

# 添加实验性质的设置参数 
option.add_experimental_option()

# 设置调试器地址
option.debugger_address()

# 添加UA
options.add_argument('user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"')

# 指定浏览器分辨率
options.add_argument('window-size=1920x3000') 

# 谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('--disable-gpu') 

 # 隐藏滚动条, 应对一些特殊页面
options.add_argument('--hide-scrollbars')

# 不加载图片, 提升速度
options.add_argument('blink-settings=imagesEnabled=false') 

# 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
options.add_argument('--headless') 

# 以最高权限运行
options.add_argument('--no-sandbox')

# 手动指定使用的浏览器位置
options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" 

#添加crx插件
option.add_extension('d:\crx\AdBlock_v2.17.crx') 

# 禁用JavaScript
option.add_argument("--disable-javascript") 

# 设置开发者模式启动，该模式下webdriver属性为正常值
options.add_experimental_option('excludeSwitches', ['enable-automation']) 

# 禁用浏览器弹窗
prefs = {  
    'profile.default_content_setting_values' :  {  
        'notifications' : 2  
     }  
}  
options.add_experimental_option('prefs',prefs)


driver=webdriver.Chrome(chrome_options=chrome_options)

–user-data-dir=”[PATH]” 
# 指定用户文件夹User Data路径，可以把书签这样的用户数据保存在系统分区以外的分区

　　–disk-cache-dir=”[PATH]“ 
# 指定缓存Cache路径

　　–disk-cache-size= 
# 指定Cache大小，单位Byte

　　–first run 
# 重置到初始状态，第一次运行

　　–incognito 
# 隐身模式启动

　　–disable-javascript 
# 禁用Javascript

　　--omnibox-popup-count="num" 
# 将地址栏弹出的提示菜单数量改为num个

　　--user-agent="xxxxxxxx" 
# 修改HTTP请求头部的Agent字符串，可以通过about:version页面查看修改效果

　　--disable-plugins 
# 禁止加载所有插件，可以增加速度。可以通过about:plugins页面查看效果

　　--disable-javascript 
# 禁用JavaScript，如果觉得速度慢在加上这个

　　--disable-java 
# 禁用java

　　--start-maximized 
# 启动就最大化

　　--no-sandbox 
# 取消沙盒模式

　　--single-process 
# 单进程运行

　　--process-per-tab 
# 每个标签使用单独进程

　　--process-per-site 
# 每个站点使用单独进程

　　--in-process-plugins 
# 插件不启用单独进程

　　--disable-popup-blocking 
# 禁用弹出拦截

　　--disable-plugins 
# 禁用插件

　　--disable-images 
# 禁用图像

　　--incognito 
# 启动进入隐身模式

　　--enable-udd-profiles 
# 启用账户切换菜单

　　--proxy-pac-url 
# 使用pac代理 [via 1/2]

　　--lang=zh-CN 
# 设置语言为简体中文

　　--disk-cache-dir 
# 自定义缓存目录

　　--disk-cache-size 
# 自定义缓存最大值（单位byte）

　　--media-cache-size 
# 自定义多媒体缓存最大值（单位byte）

　　--bookmark-menu 
# 在工具 栏增加一个书签按钮

　　--enable-sync 
# 启用书签同步