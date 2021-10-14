import time

from Tool import driver


# 根据传入i的值点击几个主页面
def GoMainView(i):
    time.sleep(2)
    # 定位五个主按钮的父级元素
    root_element = driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/main_bottom")
    # 利用相对定位方法找到子集元素
    MainButtons = root_element.find_elements_by_class_name("android.widget.RelativeLayout")
    MainButtons[i].click()