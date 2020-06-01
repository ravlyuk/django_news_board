**very simple fronted:**  http://news-board2020.herokuapp.com


# BASE API FUNCTIONAL

**create news:**
 
 http://news-board2020.herokuapp.com/api/v1/news/create/


Allow: POST, OPTIONS

{
    "title": "",
    "content": "",
    "name_author": "",
    "rubric": ""
}

-------------

**show all news:** 

http://news-board2020.herokuapp.com/api/v1/news/all/

Allow: GET, HEAD, OPTIONS

{
        "title": '',
        "content": '',
        "name_author": '',
        "rubric": '',
        "published": '',
        "likes": ''
}

-------------

**get, update, delete single news:** 

http://news-board2020.herokuapp.com/api/v1/news/detail/<id_post>/

Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS

{
        "title": '',
        "content": '',
        "name_author": '',
        "rubric": '',
        "published": ''
}

-------------

**post voice:** 

http://news-board2020.herokuapp.com/api/v1/news/voice/

Allow: POST, OPTIONS

{
        "id_news": ''
}

-------------

**add comment:** 

http://news-board2020.herokuapp.com/api/v1/news/comments/create/<int:pk>

Allow: POST, OPTIONS

{
    "name": "",
    "content": "",
    "post": ""
}

-------------

**all comments:** 

http://news-board2020.herokuapp.com/api/v1/news/comments/all/

Allow: GET

{
    "name": "",
    "content": "",
    "post": "",
    "published": ""
}

-------------

**get, update, delete single comment:** 

http://news-board2020.herokuapp.com/api/v1/news/comments/detail/<int:pk>/

Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS

{
    "name": "",
    "content": "",
    "post": ""
}
