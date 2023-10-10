# Tests for your routes go here

import pytest
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
@pytest.mark.skip
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
@pytest.mark.skip
def test_get_albums_returns_all_albums(web_client, db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album(1, test_album1, 2021, 1)\n"\
                                            "Album(2, test_album2, 2022, 2)\n"\
                                            "Album(3, test_album3, 2023, 3)"



# Request:
#         GET /artists
# Parameters: 
#         None
# Expected Response:
#         (202 OK)
#         Pixies, ABBA, Taylor Swift, Nina Simone
"""
Test that the request GET method with path /artists returns list of artist names
"""
def test_get_artists_returns_all_artist_names(web_client, db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone'


# Request:
#         POST /artists
# Parameters (body): 
#         name=Wild nothing
#         genre=Indie 
# Expected Response:
#         (202 OK)
#         No content / ''
# 
# Then a subsequent request for:
#          GET /artists
# Expected response:
#         (202 OK)
#         Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing
"""
First Test the POST /artists route returns a status code 200, with body params with new artist
Then check that the request GET /artists returns list of artist names including the new artist
"""
def test_post_artists_adds_artist(web_client, db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    response = web_client.post('/artists', data={
                                                'name': 'Wild nothing',
                                                'genre': 'Indie'
                                                })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ''

    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing'



# Request:
#         POST /artists
# Parameters (body): 
#         None
# Expected Response:
#         (400 Invalid Request)
#         'You must provide an artist name and genre parameter'
"""
Test POST /artists with no body parameters returns 400 error status code, and message
"""
def test_post_artists_with_no_parameters(web_client, db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    response = web_client.post('/artists')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'You must provide an artist name and genre parameter'