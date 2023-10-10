import os
from flask import Flask, request

from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/albums', methods=['POST', 'GET'])
def albums_post():

    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    if request.method == 'POST':
        title = request.form.get('title')
        release_year = request.form.get('release_year')
        artist_id = request.form.get('artist_id')

        new_album = Album(None, title, release_year, artist_id)
        repository.create(new_album)
        return ''
    
    if request.method == 'GET':
        albums = repository.all()
        return '\n'.join(str(album) for album in albums)


# @app.route('/albums', methods=['GET'])
# def albums_get():
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     albums = repository.all()
#     return '\n'.join(str(album) for album in albums)



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

