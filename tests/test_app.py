# import unittest
# from app import create_app

# class TestApp(unittest.TestCase):

#     def setUp(self):
#         self.app = create_app()
#         self.client = self.app.test_client()
#         self.app_context = self.app.app_context()
#         self.app_context.push()

#     def tearDown(self):
#         self.app_context.pop()

#     def test_home(self):
#         response = self.client.get('/')
#         print(response.data)  # Debug output
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response.headers['Location'], 'http://localhost/documentation')

# if __name__ == '__main__':
#     unittest.main()
