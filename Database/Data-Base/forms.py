"""Forms for playlist app."""

from wtforms import SelectField, StringField, TextAreaField
from wtforms.validators import InputRequired, Optional,Length
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField(
    "Playlist Title", validators=[InputRequired(), Length(min=3, max=20)])

    description = TextAreaField(
    "Description", validators=[Optional()] )


class SongForm(FlaskForm):
    """Form for adding songs."""
    title = StringField(
    "Song Title", validators=[InputRequired(), Length(min=1, max=30)])

    artist = StringField(
    "Artist", validators=[InputRequired(),Length(min=1, max=30)])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
