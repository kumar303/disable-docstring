import os

from nose.plugins import Plugin


class DisableDocstring(Plugin):
    """Tells unittest not to use docstrings as test names."""

    name = 'disable-docstring'

    def options(self, parser, env=os.environ):
        super(DisableDocstring, self).options(parser, env=env)
        parser.add_option('--disable-docstring', action="store_true",
                          help=DisableDocstring.__doc__)

    def configure(self, options, conf):
        super(DisableDocstring, self).configure(options, conf)
        if options.disable_docstring:
            self.enabled = True
        if not self.enabled:
            return

    def describeTest(self, test):
        return '(%s) %s' % (test, test.test._testMethodName)
