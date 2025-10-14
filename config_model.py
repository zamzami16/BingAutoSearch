from dataclasses import dataclass, asdict
from typing import List
import json as json_package


@dataclass
class Delay:
    min: int
    max: int

    @staticmethod
    def from_dict(d: dict) -> "Delay":
        return Delay(min=int(d.get("min")), max=int(d.get("max")))


@dataclass
class Scroll:
    min: int
    max: int

    @staticmethod
    def from_dict(d: dict) -> "Scroll":
        return Scroll(min=int(d.get("min", 0)), max=int(d.get("max", 0)))


@dataclass
class TotalScroll:
    min: int
    max: int

    @staticmethod
    def from_dict(d: dict) -> "TotalScroll":
        return TotalScroll(min=int(d.get("min", 2)), max=int(d.get("max", 5)))


@dataclass
class GlobalSetting:
    delay: Delay
    total_search: int
    scroll: Scroll
    total_scroll: TotalScroll

    @staticmethod
    def from_dict(d: dict) -> "GlobalSetting":
        return GlobalSetting(
            delay=Delay.from_dict(d.get("delay", {})),
            total_search=int(d.get("total_search", 0)),
            scroll=Scroll.from_dict(d.get("scroll", {"min": 500, "max": 1000})),
            total_scroll=TotalScroll.from_dict(
                d.get("total_scroll", {"min": 2, "max": 5})
            ),
        )


@dataclass
class ItemConfig:
    pos_x: int
    pos_y: int
    d_x: int
    d_y: int

    @staticmethod
    def from_dict(d: dict) -> "ItemConfig":
        return ItemConfig(
            pos_x=int(d.get("pos_x", 0)),
            pos_y=int(d.get("pos_y", 0)),
            d_x=int(d.get("d_x", 0)),
            d_y=int(d.get("d_y", 0)),
        )


@dataclass
class DataItem:
    name: str
    config: ItemConfig

    @staticmethod
    def from_dict(d: dict) -> "DataItem":
        return DataItem(
            name=str(d.get("name", "")),
            config=ItemConfig.from_dict(d.get("config", {})),
        )


@dataclass
class Config:
    global_setting: GlobalSetting
    data: List[DataItem]

    @staticmethod
    def from_dict(d: dict) -> "Config":
        gs = GlobalSetting.from_dict(d.get("global_setting", {}))
        data_list = [DataItem.from_dict(item) for item in d.get("data", [])]
        return Config(global_setting=gs, data=data_list)

    @staticmethod
    def from_file(path: str) -> "Config":
        """
        Static method membaca JSON dari file dan mengembalikan instance Config.
        Contoh pemakaian:
            cfg = Config.from_file(r"d:\KERJA\python\auto-bing-search\config.json")
        """
        with open(path, "r", encoding="utf-8") as f:
            raw = json_package.load(f)
        return Config.from_dict(raw)

    @staticmethod
    def from_file_or_default(path: str) -> "Config":
        """
        Jika file config tidak ada, gunakan default seperti file config.json.
        """
        import os

        if os.path.exists(path):
            return Config.from_file(path)
        # Default config sesuai file config.json
        default_dict = {
            "global_setting": {
                "delay": {"min": 3, "max": 7},
                "total_search": 32,
                "scroll": {"min": 500, "max": 1000},
                "total_scroll": {"min": 2, "max": 5},
            },
            "data": [
                {
                    "name": "screean-left",
                    "config": {"pos_x": 400, "pos_y": 50, "d_x": 150, "d_y": 5},
                }
            ],
        }
        return Config.from_dict(default_dict)

    def to_dict(self) -> dict:
        return asdict(self)
