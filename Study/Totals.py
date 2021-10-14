from Tool import ComeHome, handjson
from Tool import element, elements
from config import handyml
from Tool.element import Element


def click():
    # ComeHome.GoHome()
    # moreButton.GoHomeTop()
    element.element.click(handyml.read_yaml("rank.yml", "首页健身目的"))
    e = elements.elements.find_elements(handyml.read_yaml("rank.yam", "健身目的选择元素list"))
    print(e)


if __name__ == '__main__':
    click()
