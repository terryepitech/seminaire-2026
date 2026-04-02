import os
import sys
import unittest

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import importlib


class TestAppModule(unittest.TestCase):

    def test_app_module_imports(self):
        app = importlib.import_module("app")
        self.assertIsNotNone(app)


if __name__ == "__main__":
    unittest.main()
