from removebg import RemoveBg
rmbg = RemoveBg("R6BKfwJzxyZot8koPDZKfNBF", "error.log") # 引号内是你获取的API

def remove_bg(img_path):
    '''去除图片背景'''
    rmbg.remove_background_from_img_file(img_path) #图片地址