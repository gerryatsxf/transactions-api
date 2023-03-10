
from kink import inject


@inject # for dependency injection magic!
class HelloWorldService(object):
    '''Lets you get interact with hello_world script scripts, and get related information about them'''
    def __init__(self, hello_world_script=None):
        self.hello_world_script = hello_world_script # this dependency should always be injected from di.bootstrap

    def run_script(self, params):

        if type(params) is not dict:
            raise TypeError('PARAMETERS SUBMITTED ARE NOT OF VALID TYPE')

        if 'message' not in params.keys() :
            raise AttributeError('PARAMETERS SUBMITTED MUST HAVE message PROPERTY')

        if type(params['message']) is not str:
            raise TypeError('MESSAGE SUBMITTED IS NOT STRING')

        return self.hello_world_script(params)

    def get_script_index(self):
        return {'scripts':['hello_world.py']}