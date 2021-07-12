# books/tests.py
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


from .models import Book, Review


class BookTests(TestCase):
    

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='reviewuser',
            email='reviewuser@email.com',
            password='testpass123'
        )

        cls.book = Book.objects.create(
            title='Neuromancer',
            author='Bill Gibson',
            price='25.00',
        )

        cls.review = Review.objects.create(
            book = cls.book,
            author = cls.user,
            review = 'Stunning start to finish',
        )
    

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Neuromancer')
        self.assertEqual(f'{self.book.author}', 'Bill Gibson')
        self.assertEqual(f'{self.book.price}', '25.00')

    
    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Neuromancer')
        self.assertTemplateUsed(response, 'books/book_list.html')
        self.assertNotContains(response, 'New romancer')


    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Neuromancer')
        self.assertTemplateUsed(response, 'books/book_detail.html')
        self.assertNotContains(response, 'New romancer')