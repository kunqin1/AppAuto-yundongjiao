import time

from Tool import ComeHome, driver, moreButton, GoMainView
from Login import denglu

# 数据首页
# 详情数据按钮
DataDetails = "com.yundongjiao.lepao:id/rec_exercise_data"
# 总消耗卡路里
TotalC1 = "com.yundongjiao.lepao:id/exe_main_xh"
# 总运动时长
TotalTime1 = "com.yundongjiao.lepao:id/exe_main_sc"
# 总运动天数
TotalDay1 = "com.yundongjiao.lepao:id/exe_main_lj"

# 详情页
# 总运动时长
TotalTime = "com.yundongjiao.lepao:id/total"
# 总消耗卡路里
TotalC = "com.yundongjiao.lepao:id/total_xh"
# 总运动天数
TotalDay2 = "com.yundongjiao.lepao:id/total_lj"
# 标题
title = "com.yundongjiao.lepao:id/title"
# 分享按钮
share = "com.yundongjiao.lepao:id/fx"
# 总、日、周、月栏


className = "android.support.v7.app.ActionBar$Tab"
xpath = "//android.support.v7.app.ActionBar.Tab"
# 分享页面微信、朋友圈按钮
button = "com.yundongjiao.lepao:id/socialize_image_view"
# 当前维度消耗的卡路里
calorie = "com.yundongjiao.lepao:id/energy"


# 进入数据详情页
def GoDataDetails():
    # 定位五个主按钮的父级元i
    GoMainView.GoMainView(3)
    driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/rec_exercise_data").click()


# 验证数据首页和详情页总的运动数据显示一致
def DataSame():
    time.sleep(2)
    GoMainView.GoMainView(3)
    TotalC1 = driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/exe_main_xh").text
    TotalTime1 = driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/exe_main_sc").text
    TotalDay1 = driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/exe_main_lj").text
    time.sleep(1)
    driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/rec_exercise_data").click()
    TotalTime = driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/total").text
    # TotalTime = 56
    TotalC = driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/total_xh").text
    TotalDay2 = driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/total_lj").text
    if TotalC1 == TotalC and TotalTime1 == TotalTime and TotalDay1 == TotalDay2:
        print("1")
        # return True
    else:
        print("2")
        # return False


# 验证各数据页面可以竖向滑动查看
def SwipeDataUp():
    global result
    GoDataDetails()
    driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/title").click()
    A = driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/tabLayouts")
    B = A.find_element_by_class_name("android.widget.LinearLayout")
    # 定位数据类型
    DataTypes = B.find_elements_by_class_name("android.support.v7.app.ActionBar$Tab")
    for i in range(len(DataTypes))[::-1]:
        try:
            DataTypes[i].click()
            # 定位时间类型
            TimeTypes = driver.open.get_driver().find_elements_by_class_name("android.support.v7.app.ActionBar$Tab")
            for j in range(len(TimeTypes)):
                TimeTypes[j].click()
                time.sleep(1)
                denglu.up_Swipe()
                result = True
            driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/title").click()
            time.sleep(2)
        except:
            result = False
    return result


# 验证日、周、月的横向滑动
def SwipeDataRight():
    GoDataDetails()
    driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/title").click()
    A = driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/tabLayouts")
    B = A.find_element_by_class_name("android.widget.LinearLayout")
    DataTypes = B.find_elements_by_class_name("android.support.v7.app.ActionBar$Tab")
    for i in range(len(DataTypes))[::-1]:
        try:
            DataTypes[i].click()
            TimeTypes = driver.open.get_driver().find_elements_by_class_name("android.support.v7.app.ActionBar$Tab")
            for j in range(len(TimeTypes)):
                TimeTypes[j].click()
                denglu.left_Swipe()
                print("t")
            driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/title").click()
        except:
            print("F")


# 验证总模块分享功能
def TotalShare():
    GoDataDetails()
    driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/title").click()
    DataTypes = driver.open.get_driver().find_elements_by_class_name("android.support.v7.app.ActionBar$Tab")
    for i in range(len(DataTypes)):
        try:
            DataTypes[i + 1].click()
            TimeTypes = driver.open.get_driver().find_elements_by_class_name("android.support.v7.app.ActionBar$Tab")
            for j in range(len(TimeTypes)):
                TimeTypes[0].click()
                TotalTime = driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/total").text
                TotalC = driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/total_xh").text
                TotalDay2 = driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/total_lj").text
                driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/title").click()
                if (TotalC != 0) and (TotalC1 != 0) and (TotalDay2 != 0):
                    buttons = driver.open.get_driver().find_elements_by_id(
                        "com.yundongjiao.lepao:id/socialize_image_view")
                    for n in range(len(buttons)):
                        buttons[n].click()
                        driver.open.get_driver().keyevent(4)
                        try:
                            driver.open.get_driver().find_element_by_id("com.tencent.mm:id/br")
                            print("t")
                        except:
                            print("f")
        except:
            print("F")


# def DataType():
#     GoDataDetails()
#     driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/title").click()
#     A = driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/tabLayouts")
#     B = A.find_element_by_class_name("android.widget.LinearLayout")
#     DataTypes = B.find_elements_by_class_name("android.support.v7.app.ActionBar$Tab")
#     return DataTypes


if __name__ == '__main__':
    # GoDataDetails()
    # DataSame()
    # SwipeDataUp()
    SwipeDataRight()
    # TotalShare()
