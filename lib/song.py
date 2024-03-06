class Song:
    count=0
    genres=[]
    artists=[]
    def __init__(self,name,artist,genre):
         self.name=name
         self.artist=artist
         self.genre=genre
         Song.add_song_to_count()
         Song.add_to_genre(genre)
         Song.add_to_artists_count(artist)
               
    @classmethod
    def add_song_to_count(cls):
        cls.count+=1
    
    @classmethod
    def add_to_genre(cls,genre):
        cls.genres.append(genre)
    @classmethod
    def add_to_artists_count(cls, artist):
        cls.artists.append(artist)
    
    @classmethod
    def genre_count(cls):
        genre_count = {}
        for genre in cls.genres:
            if genre in genre_count:
                genre_count[genre] += 1
            else:
                genre_count[genre] = 1
        return genre_count
    @classmethod
    def artist_count(self):
        artist_count = {}
        for artist in self.artists:
            if artist in artist_count:
                artist_count[artist] += 1
            else:
                artist_count[artist] = 1
        return artist_count

            
        
            
      
        
# Tests
        
wholeheart=Song("whole heart", "Hill song", "worship") 
findMe=Song("As you find me", "Hill song", "worship") 
you_say=Song("You say", "Hill sondg", "Jazz") 

print(Song.count)
print(Song.genres)
print(Song.artists)
print(Song.genre_count())
print(Song.artist_count())

    
