# Tests for your routes go here
from lib.album import Album

# EXAMPLE

# Request:
#         POST /albums
# Parameters (body):
#         title=Voyage
#         release_year=2022
#         artist_id=2
# Expected:
#         200 OK
#         (No content)
# Test it is added
def test_post_albums_with_new_album(web_client, db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    response = web_client.post('/albums', data={'title': 'Voyage',
                                                'release_year': 2022,
                                                'artist_id':2})
    assert response.status_code == 200
    
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album(1, test_album1, 2021, 1)\n"\
                                            "Album(2, test_album2, 2022, 2)\n"\
                                            "Album(3, test_album3, 2023, 3)\n"\
                                            "Album(4, Voyage, 2022, 2)"



# Request:
#           GET /albums
# Parameters: 
#           None
# Response: 
#           List of albums & 202 OK status
# Test it returns all albums
def test_get_albums_returns_all_albums(web_client, db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album(1, test_album1, 2021, 1)\n"\
                                            "Album(2, test_album2, 2022, 2)\n"\
                                            "Album(3, test_album3, 2023, 3)"
