# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

# Request:
#         GET /artists
# Parameters: 
#         None
# Expected Response:
#         (202 OK)
#         Pixies, ABBA, Taylor Swift, Nina Simone

AND


# Request:
#         POST /artists
# Parameters (body): 
#         name=Wild nothing
#         genre=Indie 
# Expected Response:
#         (202 OK)
#         No content / ''


```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python

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


```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
```


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
