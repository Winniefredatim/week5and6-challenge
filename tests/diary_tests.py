from unittest import TestCase
import json

from diaryStore import store
from application import create_api as create_app_base


class DiaryTest(TestCase):

    def create_api(self):
        return create_app_base()

    def setUp(self):
        self.app_factory = self.create_api()
        self.app = self.app_factory.test_client()

    def tearDown(self):
        store.diary.clear()

    def test_empty_list(self):
        result = self.app.get('/diary/api/v1/mydiary', content_type='application/json')
        self.assertIn('No diary_items found', str(result.data))
        self.assertEqual(result.status_code, 200)
        self.assertEqual(len(store.diary), 0)

    def test_pet_not_found(self):
        result = self.app.get('/diary/api/v1/Mydiary/1', content_type='application/json')
        self.assertEqual(result.status_code, 404)

    def test_post_pet(self):
        data = json.dumps({'name': 'Winnie'})
        result = self.app.post('/diary/api/v1/Mydiary/', data=data, content_type='application/json')
        self.assertEqual(result.status_code, 201)
        self.assertEqual(len(store.diary), 1)

    def test_get_all_pets(self):
        data = json.dumps({'page': 'one'})
        self.app.post('/diary/api/v1/Mydiary/', data=data, content_type='application/json')
        data = json.dumps({'page': 'Two'})
        self.app.post('/diary/api/v1/Mydiary/', data=data, content_type='application/json')
        result = self.app.get('/diary/api/v1/Mydiary/', content_type='application/json')
        self.assertEqual(result.status_code, 200)
        self.assertIn('one', str(result.data))
        self.assertIn('Two', str(result.data))
        self.assertEqual(len(store.diary), 2)