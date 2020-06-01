**very simple fronted:**  http://news-board2020.herokuapp.com


# BASE API FUNCTIONAL



**show all news:** 

http://news-board2020.herokuapp.com/api/v1/news/all/

Allow: GET

-------------

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

**get, update, delete the single news:** 

http://news-board2020.herokuapp.com/api/v1/news/detail/<post_id>/

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

Allow: POST

{
        "id_news": ''
}

-------------

**add comment:** 

http://news-board2020.herokuapp.com/api/v1/news/comments/create/<post_id>/

Allow: POST

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

http://news-board2020.herokuapp.com/api/v1/news/comments/detail/<post_id>/

Allow: GET, PUT, PATCH, DELETE, OPTIONS

{
    "name": "",
    "content": "",
    "post": ""
}
