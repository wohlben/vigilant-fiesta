from .ScrapeManagerBase import ScrapeManagerBase as _ScrapeManagerBase
from .rrl import RRLLatestScraper, RRLNovelScraper, RRLChapterScraper

__all__ = [
    "Managers",
    "RRLNovelScraper",
    "RRLLatestScraper",
    "RRLChapterScraper",
    "ScrapeManager",
]


class ScrapeManager(_ScrapeManagerBase):
    parser_name = "generic"

    def parse(self):
        pass


class Managers(object):
    def __init__(self, *args, **kwargs):
        self.manager = ScrapeManager()
        self.rrl_latest = RRLLatestScraper()
        self.rrl_novel = RRLNovelScraper()
        self.rrl_chapter = RRLChapterScraper()
