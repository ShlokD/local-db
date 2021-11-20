import unittest

from localdb import LocalDB


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.db = LocalDB('test')

        self.db.create_table("music")
        self.db.table("music").push({"id": 1, "song": "99 Problems", "artist": "Jay Z"});
        self.db.table("music").push({"id": 2, "song": "Roc Boys", "artist": "Jay Z"});

        self.db.create_table("movies");
        self.db.table("movies").push({"id": 1, "title": "The Lion King", "releaseYear": "1993"})
        self.db.table("movies").push({"id": 2, "title": "Rush Hour", "releaseYear": "2001"})

        self.db.write()

    def test_empty_query(self):
        results = self.db.table("music").query()
        self.assertEqual(results, [{"id": 1, "song": "99 Problems", "artist": "Jay Z"},
                                   {"id": 2, "song": "Roc Boys", "artist": "Jay Z"}])

    def test_query(self):
        results = self.db.table("music").query({ "id": 2})
        self.assertEqual(results, [{"id": 2, "song": "Roc Boys", "artist": "Jay Z"}])

    def test_delete(self):
        self.db.table("music").delete({ "id": 2})
        self.db.write()
        results = self.db.table("music").query()
        self.assertEqual(results, [{ "id": 1, "song": "99 Problems", "artist": "Jay Z"}])

    def test_update(self):
        self.db.table("movies").update({"id": 1}, { "releaseYear": "1994", "genre": "Animation"})
        self.db.write();
        results = self.db.table("movies").query({ "id": 1 })
        self.assertEqual(results, [{ "id": 1, "title": "The Lion King", "releaseYear": "1994", "genre": "Animation"}])


if __name__ == '__main__':
    unittest.main()
