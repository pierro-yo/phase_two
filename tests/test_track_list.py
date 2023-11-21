
from lib.track_list import *

def test_add_track_to_list():
    test = TrackList()
    test.add_track_to_list("hello")
    # result = test.add_track_to_list("test song")
    result = test.listened_tracks
    assert result == ["hello"]

def test_view_listened_to_tracks():
    test = TrackList()
    # result = test.add_track_to_list("test song")
    # result = test.add_track_to_list("test song 2")
    test.add_track_to_list("hello")
    test.add_track_to_list("hello2")
    result = test.listened_tracks
    assert result == ["hello","hello2"]

