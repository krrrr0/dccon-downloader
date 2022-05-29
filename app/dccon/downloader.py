from app.dccon.model import DCConModel
from pathlib import Path
import aiohttp
import asyncio
import json
import aiofiles
import re

filename_safe = '[\/:*?"<>|]'


class DCConClient:
    def __init__(self) -> None:
        headers = {
            "Origin": "https://dccon.dcinside.com",
            "Referer": "https://dccon.dcinside.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
            "X-Requested-With": "XMLHttpRequest",
        }

        self.session = aiohttp.ClientSession(headers=headers)

        return

    @staticmethod
    async def fetch_and_save(session: aiohttp.ClientSession, url: str, dest: str) -> str:
        # print("fetch", url, "to", dest)
        async with session.get(url) as response:
            assert response.status == 200

            f = await aiofiles.open(dest, mode='wb')
            await f.write(await response.read())
            await f.close()

        return url
            

    def create_folder(self, dest) -> None:
        Path(dest).mkdir(parents=True, exist_ok=True)
        return


    async def download_data(self, dccon: DCConModel, dest: str) -> None:
        if self.session.closed:
            self.session = aiohttp.ClientSession()

        safe_title = re.sub(filename_safe,'',dccon.title).strip()

        self.create_folder(f"{dest}/{dccon.index} - {safe_title}/")

        main_image_url = f"https://dcimg5.dcinside.com/dccon.php?no={dccon.raw['info']['main_img_path']}"
        dccon.images.make_urls_from_path()

        download_futures = [self.fetch_and_save(self.session, main_image_url, f"{dest}/{safe_title}/main.jpg")]
        download_futures += [
            self.fetch_and_save(
                self.session, 
                image.url, 
                f"{dest}/{safe_title}/{str(seq).zfill(2)}_{re.sub(filename_safe, '', image.title)}.{image.ext}"
            ) for seq, image in enumerate(dccon.images.images)
        ]

        for download_future in asyncio.as_completed(download_futures):
            result = await asyncio.shield(download_future)
            # print('finished:', result)

        async with aiofiles.open(f"{dest}/ {safe_title}/package_info.json", mode='w', encoding="utf-8") as fp:
            await fp.write(json.dumps(dccon.raw, ensure_ascii=False))
        
        return

    async def download_info(self, package_index: int) -> DCConModel:
        if self.session.closed:
            self.session = aiohttp.ClientSession()

        payload = {
            "ci_t": "",
            "package_idx": str(package_index),
            "code": ""
        }

        async with self.session.post("https://dccon.dcinside.com/index/package_detail", data=payload) as resp:
            assert resp.status == 200
            result = await resp.text()

        return DCConModel(json.loads(result))


    async def close(self) -> None:
        await self.session.close()
        return

    