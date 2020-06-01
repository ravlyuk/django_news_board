**very simple fronted:**  http://news-board2020.herokuapp.com


# BASE API FUNCTIONAL



**show all news:** 

http://news-board2020.herokuapp.com/api/v1/news/all/

**Method**: GET

-------------

**create news:**
 
 http://news-board2020.herokuapp.com/api/v1/news/create/


**Method**: POST, OPTIONS

**Values**: title, content, name_author, rubric

-------------

**get, update, delete the single news:** 

http://news-board2020.herokuapp.com/api/v1/news/detail/<post_id>/

**Method**: GET, PUT, PATCH, DELETE, HEAD, OPTIONS

**Values**: title, content, name_author, rubric, published

-------------

**post voice:** 

http://news-board2020.herokuapp.com/api/v1/news/voice/

**Method**: POST

**Values**: id_news

-------------

**add comment:** 

http://news-board2020.herokuapp.com/api/v1/news/comments/create/<post_id>/

**Method**: POST

**Values**: name, content, post

-------------

**all comments:** 

http://news-board2020.herokuapp.com/api/v1/news/comments/all/

**Method**: GET

**Values**: name, content, post, published

-------------

**get, update, delete single comment:** 

http://news-board2020.herokuapp.com/api/v1/news/comments/detail/<post_id>/

**Method**: GET, PUT, PATCH, DELETE, OPTIONS

**Values**: name, content, post
