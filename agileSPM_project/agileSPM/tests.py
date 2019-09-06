from django.test import TestCase, Client
import unittest
from .views import scrumForm, scrumbanForm, kanbanForm
from django.urls import reverse
from django.shortcuts import redirect
from .models import SOWKanban, SOWScrum, SOWScrumban
import json

class FormTest(unittest.TestCase):
    client = Client() # uses a client to visit all the pages
 
    def setUpTop(cls):
        print('run once to set up test data')
        pass
    
    def setUp(self):
        print('every time it runs a test:')

        # self.scrum1 = SOWScrum.objects.create(id=100, title='S100')
        # self.kanban1 = SOWKanban.objects.create(id=100, title='K100')
        # self.scrumban1 = SOWScrumban.objects.create(id=100, title='SB100')

    # test if access granted without authentication.
    def test_client_form_GET(self):
      
        response = self.client.get(reverse('scrum_form'))
        self.assertTrue(response.status_code, 302) # asserts whether the page was accessed or not.

        response = self.client.get(reverse('kanban_form'))
        self.assertTrue(response.status_code, 302) # asserts whether the page was accessed or not.

        response = self.client.get(reverse('scrumban_form'))
        self.assertTrue(response.status_code, 302) # asserts whether the page was accessed or not.

        response = self.client.get(reverse('my_docs'))
        self.assertTrue(response.status_code, 200) # asserts whether the page was accessed or not.

        response = self.client.get(reverse('scrumban_doc', args=['100']))
        self.assertTrue(response.status_code, 200) # asserts whether the page was accessed or not.

        response = self.client.get(reverse('kanban_doc', args=['100']))
        self.assertTrue(response.status_code, 200) # asserts whether the page was accessed or not.

        response = self.client.get(reverse('scrum_doc', args=['100']))
        self.assertTrue(response.status_code, 200) # asserts whether the page was accessed or not.


    # test teseting input through post

    # def test_client_POST(self):
    #     kanban_post = SOWKanban.objects.create(id=208, title='K288')
    #     url = redirect('success_kanban', id=208)

    #     response = self.client.post(self.url, {
    #         'backlog': 'backlog item1',
    #         'inScope': 'scope4',
    #         'outScope': 'notscope5'
    #     })

    #     self.assertEquals(response.status_code, 200)
    #     self.assertEquals(response.scrum_post.backlog, 'backlog item1')

if __name__ == '__main__': 
    unittest.main() 
