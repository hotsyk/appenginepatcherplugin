"""
Plugin to patch GAE and Django to run nose tests

appenginepatch library should be in system path
"""
import traceback
import os
from nose.plugins import Plugin

class AppenginePatcher(Plugin):

    name = 'appenginepatcherplugin'
    score = 20
    enabled = False
    env_opt = 'NOSE_APPENGINEPATCHERPLUGIN'

    def __init__(self, enabled=False):
        super(AppenginePatcher, self).__init__()
        self.enabled = enabled

        if not self.enabled:
            return
        from appenginepatch.aecmd import setup_env
        setup_env(manage_py_env=True)

    def options(self, parser, env=os.environ):
        parser.add_option(
            "--appenginepatcherplugin", action='store_true',
            dest='AppenginePatcher', default=env.get(self.env_opt, False),
            help="Make nose run with gae and appenginepatcher")

    def configure(self, options, conf):
        self.conf = conf
        enable = getattr(options, 'AppenginePatcher', False)
        self.enabled = enable
        if enable:
            from appenginepatch.aecmd import setup_env
            setup_env(manage_py_env=True)

