
class TrackList():
    def __init__(self):
        self.listened_tracks = []

    def add_track_to_list(self, string):
        self.listened_tracks.append(string)
        # return self.listened_tracks
        
    def view_listened_to_tracks(self):
        return self.listened_tracks

# test = TrackList()

# print(test.listened_tracks)

# test.add_track_to_list("whatever")
# test.add_track_to_list("hello")

# print(test.view_listened_to_tracks())


# As a user
# So that I can keep track of my music listening
# I want to add tracks I've listened to and see a list of them.

