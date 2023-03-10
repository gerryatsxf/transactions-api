import unittest
from unittest import mock
from kink import di
from app.hello_world.service.hello_world import HelloWorldService

class HelloWorldServiceTest(unittest.TestCase):
    
    @mock.patch("app.hello_world.script.hello_world")
    def setUp(self, hello_world_script_mock):
        di['hello_world_script'] = hello_world_script_mock
        self.hello_world_script_mock = hello_world_script_mock
        self.hello_world_service = HelloWorldService()

    def test_hello_world_script_called_when_running_script(self):
        params = {'message':'Hey there!'}
        self.hello_world_script_mock.return_value = {'message':'HEY THERE!'}
        result = self.hello_world_service.run_script(params)
        self.hello_world_script_mock.assert_called_with(params)
        self.assertTrue('message' in result.keys())

    def test_hello_world_script_called_with_bad_params(self):
        params = '{"message":"Hey there!"}'
        self.assertRaises(TypeError, self.hello_world_service.run_script, params)
        params = {"not_my_message":"Hey there!"}
        self.assertRaises(AttributeError, self.hello_world_service.run_script, params)
        params = {"message":500}
        self.assertRaises(TypeError, self.hello_world_service.run_script, params)

    def test_script_index_is_non_empty_list(self):
        result = self.hello_world_service.get_script_index()
        self.assertTrue('scripts' in result.keys())
        self.assertTrue(type(result['scripts']) is list)
        self.assertTrue(len(result['scripts']) > 0)


