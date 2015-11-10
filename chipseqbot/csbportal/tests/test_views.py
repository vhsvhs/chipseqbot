from django.test import TestCase

def add_middleware_to_request(request, middleware_class):
    middleware = middleware_class()
    middleware.process_request(request)
    return request

def add_middleware_to_response(request, middleware_class):
    middleware = middleware_class()
    middleware.process_request(request)
    return request

class UserProfileTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        
    def tearDown(self):
        del self.factory