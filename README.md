# JMComic-QQBot
利用Python API for JMComic + NapCat+NcatBot完成qq对话中自动获取本子资源机器人

实现效果，根据特定询问，机器人账号QQ将会返回给你id对应的本子文件（可以设定为群机器人），文件类型为PDF

---
## 文件介绍
1、bot为主程序

3、option.yml 为本子获取配置文件

## 环境搭建
1、推荐使用 python>3.9

2、下载所需三方库 

  ```shell
  pip install jmcomic -i https://pypi.org/project -U
  ```
   ```shell
  pip install img2pdf
  ```

  ```shell
  pip install ncatbot -U -i https://mirrors.aliyun.com/pypi/simple
  ```
3、运行bot 即可 （bot号为机器人的qq号）

4、同意安装NapCat 

5、其它账号询问此用户即可，默认为 /jm id 的形式 

6、机器人qq返回给你本子文件（只能返回一章节，可以根据需求修改）


## 项目来源参考文档
### JMComic 爬取脚本文档
https://github.com/hect0x7/JMComic-Crawler-Python/blob/master/README.md
### 机器人脚本文档
https://docs.ncatbot.xyz/
