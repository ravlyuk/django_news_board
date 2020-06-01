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
    "title": <value>,
    "content": <value>,
    "name_author": <value>,
    "rubric": <value>
}


-------------

**get, update, delete the single news:** 

http://news-board2020.herokuapp.com/api/v1/news/detail/<post_id>/

Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS

{
        "title": <value>,
        "content": <value>,
        "name_author": <value>,
        "rubric": <value>,
        "published": <value>
}

-------------

**post voice:** 

http://news-board2020.herokuapp.com/api/v1/news/voice/

Allow: POST

{
        "id_news": <value>
}

-------------

**add comment:** 

http://news-board2020.herokuapp.com/api/v1/news/comments/create/<post_id>/

Allow: POST

{
    "name": <value>,
    "content": <value>,
    "post": <value>
}

-------------

**all comments:** 

http://news-board2020.herokuapp.com/api/v1/news/comments/all/

Allow: GET

{
    "name": <value>,
    "content": <value>,
    "post": <value>,
    "published": <value>
}

-------------

**get, update, delete single comment:** 

http://news-board2020.herokuapp.com/api/v1/news/comments/detail/<post_id>/

Allow: GET, PUT, PATCH, DELETE, OPTIONS

{
    "name": <value>,
    "content": <value>,
    "post": <value>
}
