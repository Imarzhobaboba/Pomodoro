import asyncio

async def main():
    print('hello world 1')
    await asyncio.sleep(3)
    print('hello world 3')



async def main_1():
    print('hello world 2')



event_loop = asyncio.get_event_loop()
tasks = [event_loop.create_task(main()),
         event_loop.create_task(main_1())]

wait_tasks = asyncio.wait(tasks)

event_loop.run_until_complete(wait_tasks)
event_loop.close()