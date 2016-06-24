import unittest
from pyramid import testing


class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from tutorial import main
        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=302)

    def test_plain_without_name(self):
        res = self.testapp.get('/plain', status=200)
        self.assertIn(b'No name provided', res.body)

    def test_plain_with_name(self):
        res = self.testapp.get('/plain?name=John Doe', status=200)
        self.assertIn(b'John Doe', res.body)


if __name__ == "__main__":
    unittest.main()
