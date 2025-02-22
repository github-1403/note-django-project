from django.test import TestCase
from django.shortcuts import reverse
from .models import Note


class NoteListViewTest(TestCase):

    def setUp(self):
        self.note1 = Note.objects.create(author='sample_author_1', text='sample_text_1')

    def test_notes_list_view_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_notes_list_view_url_by_name(self):
        response = self.client.get(reverse('notes_list'))
        self.assertEqual(response.status_code, 200)

    def test_notes_list_page(self):
        response = self.client.get(reverse('notes_list'))
        self.assertContains(response, self.note1.author)
        self.assertContains(response, self.note1.text)
