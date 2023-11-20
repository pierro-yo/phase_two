
from lib.track_list import *

def test_add_track_to_list():
    test = TrackList()
    result = test.add_track_to_list("test song")
    assert result == ["test song"]

def test_view_listened_to_tracks():
    test = TrackList()
    result = test.add_track_to_list("test song")
    result = test.add_track_to_list("test song 2")
    assert result == ["test song","test song 2" ]

