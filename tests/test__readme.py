from .ut_utils import TestCase
import os
import doctest

class ReadmeTest(TestCase):
    def test__readme_file(self):
        readme_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "README.rst"))
        self.assertTrue(os.path.exists(readme_path))
        result = doctest.testfile(readme_path, module_relative=False)
        self.assertEqual(result.failed, 0, "%s tests failed!" % result.failed)
