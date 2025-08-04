import jmcomic


def get_benzi(id):
    option  = jmcomic.create_option_by_file("D:/Study/PythonAutomation/JMComic/option.yml")
    file = jmcomic.download_album(id,option) #获取本子

    #获取文件路径 并返回
    return 'D:/Study/PythonAutomation/JMComic/'+id+'.pdf' 
    
if __name__ == "__main__":
    option  = jmcomic.create_option_by_file("D:/Study/PythonAutomation/JMComic/option.yml")
    jmcomic.download_album(422866,option) #获取本子
