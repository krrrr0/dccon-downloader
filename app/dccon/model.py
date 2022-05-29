import datetime
from typing import List


class Image:
    def __init__(self, idx: int, title: str, ext: str, path: str) -> None:
        self.index = idx
        self.title = title
        self.ext = ext
        self.path = path
        self.url = ""
        return

    def make_url_from_path(self) -> str:
        self.url = f"https://dcimg5.dcinside.com/dccon.php?no={self.path}"
        return self.url


class Images:
    def __init__(self, image_info_dict) -> None:
        image_list = []

        for image in image_info_dict:
            image_list.append(
                Image(int(image['idx']), image['title'], image['ext'], image['path'])
            )

        self.images = image_list
        return

    def make_urls_from_path(self) -> List[str]:
        return [i.make_url_from_path() for i in self.images]

    def __len__(self) -> int:
        return len(self.images)



class Author:
    def __init__(self, seller_no: int, seller_id: str, seller_name: str) -> None:
        self.index = seller_no
        self.username = seller_id
        self.name = seller_name

        return


class DCConModel:
    def __init__(self, package_json: dict) -> None:
        assert package_json["info"]["open"] == "Y"

        info_dict = package_json["info"]

        self.index = int(info_dict["package_idx"])
        self.title = info_dict["title"]
        self.description = info_dict["description"]
        self.reg_date = datetime.datetime.strptime(info_dict["reg_date"], "%Y-%m-%d %H:%M:%S")

        self.author = Author(info_dict["seller_no"], info_dict["seller_id"], info_dict["seller_name"])
        self.images = Images(package_json["detail"])

        self.tags = [t["tag"] for t in package_json["tags"]]

        self.sale_count = int(info_dict["sale_count"])

        self.raw = package_json
        
        return

    def __str__(self) -> str:
        return f"디시콘 #{self.index} - {self.title} ({self.description}) by {self.author.name} : {len(self.images)}개 이미지"