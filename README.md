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
## End-Point Checklist from ```print(app.url_map) ```
- [ ] Contact the media 
- [ ] <Rule '/' (OPTIONS, POST) -> /.login>,
- [ ] <Rule '/signup' (OPTIONS, POST) -> /.signup>,
- [ ] <Rule '/<id>' (GET, HEAD, OPTIONS) -> /.single_user>,
- [ ] <Rule '/logs/' (GET, HEAD, OPTIONS) -> /./.log_view>,
- [ ] <Rule '/logs/<user_id>' (GET, HEAD, OPTIONS) -> /./.single_user>,
- [ ] <Rule '/logs/target/<id>' (GET, HEAD, OPTIONS) -> /./.target_log>,
- [ ] <Rule '/logs/' (OPTIONS, POST) -> /./.create_log>,
- [ ] <Rule '/logs/edit/<id>' (PUT, OPTIONS, PATCH) -> /./.update_log>,
- [ ] <Rule '/logs/delete/<id>' (OPTIONS, DELETE) -> /./.delete_log>,
- [ ] <Rule '/logs/comments/' (GET, HEAD, OPTIONS) -> /././.my_comments>,
- [ ] <Rule '/logs/comments/<log_id>' (GET, HEAD, OPTIONS) -> /././.log_comments>,
- [ ] <Rule '/logs/comments/user<user_id>' (GET, HEAD, OPTIONS) -> /././.user_comments>,
- [ ] <Rule '/logs/comments/<log_id>' (OPTIONS, POST) -> /././.create_comment>,
- [ ] <Rule '/logs/comments/edit/<id>' (PUT, OPTIONS, PATCH) -> /././.update_comment>,
- [ ] <Rule '/logs/comments/delete/<id>' (OPTIONS, DELETE) -> /././.delete_comment>,
- [ ] <Rule '/logs/clone/<id>' (GET, HEAD, OPTIONS) -> /././clone.create_clone>])