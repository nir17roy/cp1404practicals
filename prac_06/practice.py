class Song:
    def __init__(self,title = "", artist="", duration=0.0, is_favorite= False):
        self.title = title
        self.artist=artist
        self.duration = duration
        self.is_favorite = is_favorite
    def mark_favourite(self):
        self.is_favorite = True
    def __str__(self):

        favorite = self.is_favorite
        if favorite :
            marking = "favorite"
        else:
            marking = "not that much fav"
        return f"{self.title} by {self.artist} - {self.duration} mins [{marking}]"
gaan = Song("radha" , "shyam", 0.0, True)
print(gaan)