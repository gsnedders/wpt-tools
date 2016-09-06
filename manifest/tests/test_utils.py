import os

from hypothesis import given, example
from hypothesis.strategies import text

from ..utils import rel_path_to_url, url_to_rel_path

@given(text("a" + os.sep, min_size=1).filter(lambda x: not os.path.isabs(x)),
       text("a/", min_size=1))
def test_rel_path_to_url_roundtrip(rel_path, url_base):
    assert rel_path == url_to_rel_path(rel_path_to_url(rel_path, url_base), url_base)
