from discord.ext import tasks
import asyncio
import psutil 
import aiohttp 

env = {"minutes": 0.5, "server": "http://localhost:5555/add"}


async def loop_task():
    """
    Default app list:
    Visual Studio Code -> code
    Discord (all desktop clients) -> discord
    Paint for windows -> paint
    """
    
    exists_discord=str("DiscordCanary.exe" in (p.name() for p in psutil.process_iter()) or "DiscordDevelopment.exe" in (p.name() for p in psutil.process_iter()) or "Discord.exe" in (p.name() for p in psutil.process_iter()) or "DiscordPTB.exe" in (p.name() for p in psutil.process_iter()))
    exists_paint = str("mspaint.exe" in (p.name() for p in psutil.process_iter()))
    exists ={"code":  str("Code.exe" in (p.name() for p in psutil.process_iter())), "discord":exists_discord, "paint": exists_paint}
    print(exists)
    async with aiohttp.ClientSession() as session:
        await session.post(env["server"], data=str(exists))
        await session.close()
    await asyncio.sleep(60*env["minutes"])

    
async def run_task_forever(task, *args):
    while True:
        await task(*args)




# Python 3.7+
asyncio.run(run_task_forever(loop_task))

