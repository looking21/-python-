import pyautogui
import time


def perform_automation():
    try:
        # 按下 Windows 键打开开始菜单
        pyautogui.hotkey('win')
        time.sleep(2)  # 等待开始菜单完全显示

        # 输入网址并访问
        pyautogui.typewrite('http://www.baidu.com', interval=0.1)  # interval 设置为 0.1 秒
        time.sleep(4)  # 等待网页加载

        # 按下回车键
        pyautogui.press('enter')
        pyautogui.press('enter')
    except Exception as e:
        print(f"An error occurred: {e}")


# 调用函数执行自动化
perform_automation()
