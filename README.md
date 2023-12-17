# Harry Manton T2A2 

## Apps Purpose
My app is for logging dough recipes. Users can sign up and store their own recipes. gain access to any public recipe, comment on them and clone them for their own record.

## Reason for Creating
Everytime I bake bread I log my process in a table, Ive written inside an exersice book. I am currently on my 3rd book and will continue to log my methods every time I make a new batch(now digally though).

This method has worked very well, but has a major flaw, it is very inefficient when you need to look back on a specific record or field.

My app will utilise the best aspects of the phsyical entries, but provide quick and easy navigation to desired records.
In addition, opening the database to additional users can create expotential dough logs resulting in diverse recipes, different methods/techniques, boarder search capabilites and socialisation for Doughnuts.

Below is a picture of one of my phyical entries.

## Why Postgres
I have chosen Postgres because I have the most experienced with it and I prioritise developing my app above learning a different Database Management System (DBMS).

## Why Consider Alternative Database Systems
 What are the drawbacks compared to others?

## ORM - Functionalities and Benefits
Object Relation Mapping(ORM) provides interaction between applications and databases. I will be using SQLAlchemy as my ORM and it will allows me to code my app in python and utilise a flask architype.

### Language Flexibility
- ORM's allow developers to interact with the database using their preferrend programming language. This flexibility lets developers leverage their abilities while abstracting away direct SQL queries.

### Code Readability
- Using an ORM will typically result in consistent and readable code. This benefits collaboration and development, as one or multiple developers can more easily identify and build on features within the app.

### Development Speed
- ORM's reduce the boilerplate code needed, enabling developers to accomplish tasks more efficiently. The removal of repeated code  results in quick and efficient production.

## End-Points
### End-Point Checklist from ```print(app.url_map) ```
1. [x] <Rule '/' (OPTIONS, POST) -> /.login>
1. [x] <Rule '/signup' (OPTIONS, POST) -> /.signup>
1. [x] <Rule '/<id>' (GET, HEAD, OPTIONS) -> /.single_user>
1. [x] <Rule '/logs/' (GET, HEAD, OPTIONS) -> /./.log_view>
1. [x] <Rule '/logs/<user_id>' (GET, HEAD, OPTIONS) -> /./.single_user>
1. [x] <Rule '/logs/target/<id>' (GET, HEAD, OPTIONS) -> /./.target_log>
1. [x] <Rule '/logs/' (OPTIONS, POST) -> /./.create_log>
1. [x] <Rule '/logs/edit/<id>' (PUT, OPTIONS, PATCH) -> /./.update_log>
1. [x] <Rule '/logs/delete/<id>' (OPTIONS, DELETE) -> /./.delete_log>
1. [x] <Rule '/logs/comments/' (GET, HEAD, OPTIONS) -> /././.my_comments>
1. [x] <Rule '/logs/comments/<log_id>' (GET, HEAD, OPTIONS) -> /././.log_comments>
1. [x] <Rule '/logs/comments/user<user_id>' (GET, HEAD, OPTIONS) -> /././.user_comments>
1. [x] <Rule '/logs/comments/<log_id>' (OPTIONS, POST) -> /././.create_comment>
1. [x] <Rule '/logs/comments/edit/<id>' (PUT, OPTIONS, PATCH) -> /././.update_comment>
1. [x] <Rule '/logs/comments/delete/<id>' (OPTIONS, DELETE) -> /././.delete_comment>
1. [x] <Rule '/logs/clone/<id>' (GET, HEAD, OPTIONS) -> /././clone.create_clone>

### Checklist Review
1. Logging should just give you the key, id and your username
1. View single User should show their comments.
1. Creating a user isnt hashing password and return all but password
1. __No Edit__ Returns your Logs from your JWT identity
1. __No Edit__ Returns specified Users Logs 
1. __No Edit__ Returns specified Log with nested User
1. Needed to provide recipe in create as no recipe routes exist, will need to do the same for edit
1. Copy and pasted above into log edit for recipe manipulation. Needed to delete existing recipe before commit to avoid Integrity error from PK
1. As above needed to delete nested fields when deleting Log. Also, noticed that when deleting Log as Admin the return is just the Admins Logs, where maybe should return all
1. __No Edit__ Returns your Comments from your JWT identity
1. __No Edit__ Returns Comments from a Log and provides a few key user details
1. __No Edit__ Returns just the specificed Users Comments that contains log_id, the comment_id and the messages from the User
1. __No Edit__ Creating a comment just returns the comment you created and its id
1. Changed to Only return the Message that was edited
1. __No Edit__ However, similar to above Admin can delete any comment, but only get their comments returned.
1. __No Edit__  Return the log cloned with new PK's

### End-Point Sample

1. *'/' (OPTIONS, POST) -> /.login>* A user will POST with an email and the associated password. The API will validate and return a JWT token. 
<img src="/docs/Route _Screenshot_1.png" alt="End-point 1">

1. *'/signup' (OPTIONS, POST) -> /.signup>* A user can sign up by entering a email and username and password. The username and password my be unique in the DB.
<img src="/docs/Route_Screenshot_2.png" alt="End-point 2">

1. *'/<id>' (GET, HEAD, OPTIONS) -> /.single_user>* A signed in user search for a single user. returns a list of users logs with nested recipes and comments.
<img src="/docs/Route_Screenshot_3.png" alt="End-point 3">

1. *'/logs/' (GET, HEAD, OPTIONS) -> /./.log_view>* Uses your JWT token to return your logs.
<img src="/docs/Route_Screenshot_4.png" alt="End-point 4">

1. *'/logs/<user_id>' (GET, HEAD, OPTIONS) -> /./.single_user>* Targets a single users logs.
<img src="/docs/Route_Screenshot_5.png" alt="End-point 5">

1. *'/logs/target/<id>' (GET, HEAD, OPTIONS) -> /./.target_log>* Targets a single log.
<img src="/docs/Route_Screenshot_6.png" alt="End-point 6">

1. *'/logs/' (OPTIONS, POST) -> /./.create_log>* A logged in users makes a new log. POST requires a Title, users can also input the recipe here, or later while editing (if no recipe entered defualts are provided).
<img src="/docs/Route_Screenshot_7.png" alt="End-point 7">

1. *'/logs/edit/<id>' (PUT, OPTIONS, PATCH) -> /./.update_log>* A user can edit their logs (or admin any log). <img src="/docs/Route_Screenshot_8.png" alt="End-point 8">

1. *'/logs/delete/<id>' (OPTIONS, DELETE) -> /./.delete_log>* A user can delete their log, it will return remaining logs. <img src="/docs/Route_Screenshot_9.png" alt="End-point 9">

1. *'/logs/comments/' (GET, HEAD, OPTIONS) -> /././.my_comments>* Uses the JWT token to give a user their comments. <img src="/docs/Route_Screenshot_10.png" alt="End-point 10">

1. *'/logs/comments/<log_id>' (GET, HEAD, OPTIONS) -> /././.log_comments>* Targets a specific log and returns comment on it. <img src="/docs/Route_Screenshot_11.png" alt="End-point 11">

1. *'/logs/comments/user<user_id>' (GET, HEAD, OPTIONS) -> /././.user_comments>* Returns target users comments. <img src="//docs/Route_Screenshot_12.png" alt="End-point 12">

1. *'/logs/comments/<log_id>' (OPTIONS, POST) -> /././.create_comment>* Creates a comment, only requires the message to be input as route directs which log. <img src="/docs/Route_Screenshot_13.png" alt="End-point 13">

1. *'/logs/comments/edit/<id>' (PUT, OPTIONS, PATCH) -> /././.update_comment>* Edits the message on a comment. <img src="/docs/Route_Screenshot_14.png" alt="End-point 14">

1. *'/logs/comments/delete/<id>' (OPTIONS, DELETE) -> /././.delete_comment>* Delete target comment. <img src="/docs/Route_Screenshot_15.png" alt="End-point 15">

1. *'/logs/clone/<id>' (GET, HEAD, OPTIONS) -> /././clone.create_clone>* Clones Target Log and nested recipe. not comments. <img src="/docs/Route_Screenshot_16.png" alt="End-point 16">

