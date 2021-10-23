from tkinter import *


def main():
    root = Tk()

    # 配置一个按钮并放置
    menubutton = Menubutton(root,
    text='单击出现下拉菜单',
    relief=RAISED)
    menubutton.pack()

    user_choice = IntVar()
    # 默认选中 - 木部
    user_choice.set(1)

    file_menu = Menu(menubutton, tearoff=False)
    file_menu.add_radiobutton(label='木部', variable=user_choice, value=1)
    file_menu.add_radiobutton(label='谷部', variable=user_choice, value=2)

    # 这里不是root
    menubutton.config(menu=file_menu)

    mainloop()


if __name__ == '__main__':
    main()
