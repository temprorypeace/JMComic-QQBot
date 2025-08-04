# ========= 导入必要模块 ==========
from ncatbot.core import BotClient, GroupMessage, PrivateMessage
from ncatbot.utils import get_log
from tools import get_benzi
# ========== 创建 BotClient ==========
bot = BotClient()
_log = get_log()

# ========= 注册回调函数 ==========
@bot.group_event()
async def on_group_message(msg: GroupMessage):
    _log.info(msg)
    info = msg.raw_message.split()
    if info[0] == "/jm":
        benzi_path = get_benzi(info[1]) 
        await bot.api.post_group_file(group_id=msg.group_id, file = benzi_path) # 这里写接收者的 QQ 号和文件的路径

@bot.private_event()
async def on_private_message(msg: PrivateMessage):
    _log.info(msg)

    ## 处理对话命令形式
    info = msg.raw_message.split()

    if info[0] == "/jm":
        benzi_path = get_benzi(info[1]) 
        await bot.api.post_private_file(user_id=msg.user_id, file = benzi_path) # 这里写接收者的 QQ 号和文件的路径


# ========== 启动 BotClient==========
if __name__ == "__main__":
    bot.run(bt_uin="749064196") # 这里写 Bot 的 QQ 号
    
