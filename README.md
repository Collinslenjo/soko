# Soko Book Rental Store Api
> Note: Each story is in its own branch

## Requirements
- [Python 3](https://www.python.org)
- [Django](https://www.djangoproject.com)

## Running the application
To run this application, clone the repository on your local machine and run the following commands.
```sh
    $ git clone https://github.com/Collinslenjo/soko.git
    $ cd soko
    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    $ ./manage.py makemigrations
    $ ./manage.py migrate
    $ ./manage.py test
    $ ./manage.py runserver
```
Your server is running on ```http://localhost:8000/api/```

#### API Endpoints
|End point | Public Access|Action
|----------|--------------|------
api/ | False | Calculate and view your rental cost
api/books/ | False | Create and Retrieve Books
api/books/<int:book_id> | False | Retrieve, Update & Delete Book 
api/categories/ | False | View and create book categories
api/categories/<int:category_id>/ | False | Retrieve Update and Delete a category
api/rentbooks/ | False | View and create rent records
api/rentbooks/<int:rent_id>/ | False | Retrieve Update and Delete rent records


#### STORY 3
* create a user i.e for testing use (```./manage.py createsuperuser```)
* create 3 categories (regular, fiction, and novel) in the database with their charges i.e  ``` {"name":"regular", "charge":1.5, "minimumcharge": 4.5,"minimumdays":3} ```

```
POST http://localhost:8000/api/books/

{
    "id": 1,
    "name": "novel",
    "charge": 1.5,
    "minimumcharge": 4.5,
    "minimumdays": 3,
    "createdAt": "2019-03-15T10:05:51.343411Z",
    "updatedAt": "2019-03-15T10:05:51.343445Z"
}
```

 * create different books with the category id's i.e ```{"bookname":"A Dance of Dragons", "category":1,"user":1}```

```
POST http://localhost:8000/api/categories/

{
    "id": 1,
    "bookname": "A Dance of Dragons",
    "category": 1,
    "user": 1,
    "createdAt": "2019-03-15T13:15:09.649537Z",
    "updatedAt": "2019-03-15T13:15:09.649571Z"
}
```
* create a rent record like ```{"book":1,"user":1}```
* your response should look like below:

```
POST http://localhost:8000/api/rentbooks/

{
    "id": 1,
    "book": 1,
    "user": 1,
    "returned": false,
    "dateBorrowed": "2019-03-15T13:15:44.149304Z",
    "dateReturned": null
}
```

* now visit ```http://localhost:8000/api/``` to see your cost calculation. (if less than a day you should see 0)