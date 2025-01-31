def rating_sort(books):
    for book in books:
        if book['rating'] > 8.0:
            print(book)
books = [
{
"title": "1984", 
"rating": 9.5,
"genre": "Dystopian"
},
{
"title": "The Catcher in the Rye",
"rating": 7.8,
"genre": "Classic"
},
{
"title": "To Kill a Mockingbird",
"rating": 9.1,
"genre": "Classic"
},
{
"title": "The Great Gatsby",
"rating": 8.5,
"genre": "Classic"
},
{
"title": "Moby Dick",
"rating": 7.0,
"genre": "Adventure"
},
{
"title": "Pride and Prejudice",
"rating": 8.9,
"genre": "Romance"
},
{
"title": "The Hobbit",
"rating": 9.0,
"genre": "Fantasy"
},
{
"title": "The Road",
"rating": 8.0,
"genre": "Dystopian"
},
{
"title": "The Shining",
"rating": 9.2,
"genre": "Horror"
},
{
"title": "Dracula",
"rating": 8.4,
"genre": "Horror"
},
{
"title": "Frankenstein",
"rating": 8.1,
"genre": "Horror"
},
{
"title": "Dune",
"rating": 9.3,
"genre": "Sci-Fi"
},
{
"title": "Neuromancer",
"rating": 8.5,
"genre": "Sci-Fi"
},
{
"title": "Brave New World",
"rating": 9.0,
"genre": "Dystopian"
},
{
"title": "Fahrenheit 451",
"rating": 8.7,
"genre": "Dystopian"
}
]
rating_sort(books)