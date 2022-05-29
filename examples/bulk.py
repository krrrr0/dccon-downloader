from app.dccon import downloader
import asyncio


async def fetch(client, i, dest):
    try:
        await client.download_data(await client.download_info(i), dest)
    except Exception:
        # 잘못된 번호, 판매 기간 중지 등 다운로드 불가시
        print(f"{i}: 실패")
    else:
        print(f"{i}: 성공")
    return


async def bound_fetch(sem, client, i, dest):
    # Getter function with semaphore.
    async with sem:
        await fetch(client, i, dest)



async def run(dest):
    client = downloader.DCConClient()
    tasks = []

    sem = asyncio.Semaphore(1000)

    for i in range(107320):
        # pass Semaphore and client to every GET request
        task = asyncio.ensure_future(bound_fetch(sem, client, i, dest))
        tasks.append(task)
    responses = asyncio.gather(*tasks)
    await responses
    
    
    await client.close()
    return


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run("E:/dccon"))
    loop.run_until_complete(future)