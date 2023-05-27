from app import db
from models import Playlist, Song, PlaylistSong


db.drop_all()
db.create_all()

s1 = Song(title = "Super Freak", artist = "Rick James")
db.session.add(s1)
db.session.commit()

s2 = Song(title = "Stairway", artist = "Zepplin")
db.session.add(s2)
db.session.commit()

s3 = Song(title = "Big Wheel", artist = "Tina Turner")
db.session.add(s3)
db.session.commit()

s4 = Song(title = "Jack Straw", artist = "The Dead")
db.session.add(s4)
db.session.commit()

s5 = Song(title = "Pictures of You ", artist = "The Cure ")
db.session.add(s5)
db.session.commit()

p1 = Playlist(name="Freak Mix", description="Ricky and Friends")
db.session.add(p1)
db.session.commit()

p2 = Playlist(name="FOREVER GRATFUL", description="Gratful Dead 70s mix")
db.session.add(p2)
db.session.commit()

p3 = Playlist(name="RIP the Great", description="Tina Turner")
db.session.add(p3)
db.session.commit()

p4 = Playlist(name="Mega Mix", description="All the Hits")
db.session.add(p4)
db.session.commit()

p5 = Playlist(name="Chill Tunes", description="Something to relax to")
db.session.add(p5)
db.session.commit()

