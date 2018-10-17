from django.test import TestCase
from scrapes.models import Parser
from novels.models import Fiction, Chapter
from scrapes.fetch_generators import rrl_chapter_generator
import logging


class GenerateChapterTestCase(TestCase):
    parser_id = int

    @classmethod
    def setUpTestData(cls):
        logging.disable(logging.CRITICAL)
        cls.parser_id = Parser.objects.get(name="rrl chapter").id

    def setUp(self):
        fictions = [
            {
                "title": "monitored",
                "monitored": True,
                "url": "someurl/fiction/1/novelname",
            },
            {
                "title": "unmonitored",
                "monitored": False,
                "url": "another-url/fiction/22/novel-name2",
            },
        ]
        fics = [Fiction.objects.create(**fic) for fic in fictions]
        chapters = [
            {"fiction": fics[0], "url": "someurl/chapter/333/chapter"},
            {
                "fiction": fics[0],
                "url": "someurl/chapter/334/chapter",
                "content": "blub",
            },
            {"fiction": fics[1], "url": "someurl/chapter/3/chapter"},
            {"fiction": fics[1], "url": "someurl/chapter/4/chapter"},
        ]
        [Chapter.objects.create(**chap) for chap in chapters]

    def add_queue_events(self):
        return rrl_chapter_generator.add_queue_events(self.parser_id)

    def monitored_novels(self):
        return len(rrl_chapter_generator.monitored_novels(self.parser_id))

    def missing_chapters(self):
        return rrl_chapter_generator.missing_chapters(self.parser_id).count()

    def pending_fetches(self):
        return rrl_chapter_generator.pending_fetches(self.parser_id).count()

    def test_starting_data(self):
        self.assertGreater(
            self.monitored_novels(), 0, "test data doesn't include any monitored novels"
        )
        self.assertGreater(
            self.missing_chapters(),
            0,
            "test data isn't providing anything to add to the pending queue",
        )

    def test_adding_fetch_events(self):
        self.add_queue_events()
        self.assertEquals(
            self.missing_chapters(), 0, "we're still finding chapters to queue..."
        )

    def test_correct_amount_added(self):
        pending = self.pending_fetches()
        self.add_queue_events()
        self.assertEquals(pending + 1, self.pending_fetches())