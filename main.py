from app.dccon import downloader
import asyncio
import argparse
import os


async def run(i, dest):
    print(f"다운로드: {i}...", end=" ")

    client = downloader.DCConClient()
        
    try:
        await client.download_data(await client.download_info(i), dest)
    except Exception:
        # 잘못된 번호, 판매 기간 중지 등 다운로드 불가시
        print("실패: 올바르지 않은 번호 또는 판매 기한 만료")
    else:
        print("완료!")
    
    await client.close()
    return
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser("python main.py")
    parser.add_argument("id", help="다운로드할 디시콘 번호입니다.", type=int)
    parser.add_argument("destination", help="다운로드할 위치입니다. 생략시 현재 폴더로 다운로드됩니다. 예시) ./dccon 기본: 현재 디렉토리", type=str, nargs="?", default=".")

    args = parser.parse_args()

    if os == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(run(args.id, args.destination))
