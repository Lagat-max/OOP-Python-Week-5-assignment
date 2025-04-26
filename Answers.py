# Activity 1: Design Your Own Class! 

class Movie:
    def __init__(self, title, director, year, genre, cast, summary):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
        self.cast = cast
        self.summary = summary

    def get_details(self):
        print(f"Title: {self.title}, Director: {self.director}, Year: {self.year}, Genre: {self.genre}, Cast: {self.cast}, Summary: {self.summary}")

    def rate_movie(self, rating):
        print(f"The movie {self.title} has been rated {rating} stars!")

    def recommend(self):
        print(f"We recommend you watch {self.title} because of its {self.genre} theme!")

# Creating a Movie object
movie_object = Movie("Inception", "Christopher Nolan", 2010, "Science Fiction", "Leonardo DiCaprio, Joseph Gordon-Levitt", "A mind-bending journey into the world of dreams.")
movie_object.get_details()
movie_object.rate_movie(4.5)
movie_object.recommend()

# Inheritance layer
class Comedy(Movie):
    def __init__(self, title, director, year, cast, summary, funniest_moment):
        super().__init__(title, director, year, "Comedy", cast, summary)
        self.funniest_moment = funniest_moment

    def describe_funniest_moment(self):
        print(f"The funniest moment in {self.title} is when: {self.funniest_moment}")

# Creating a Comedy object
comedy_object = Comedy("The Hangover", "Todd Phillips", 2009, "Bradley Cooper, Zach Galifianakis", "A bachelor party in Las Vegas turns into an unforgettable misadventure.", "Waking up in a trashed hotel suite with a tiger")
comedy_object.get_details()  # Inherits from Movie class
comedy_object.describe_funniest_moment()  # Specific to Comedy class



# Activity 2: Polymorphism Challenge! 

class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement move() method")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Dog(Animal):
    def move(self):
        print("Running 🐶")

class Bird(Animal):
    def move(self):
        print("Flying 🕊️")

car = Car()
plane = Plane()
dog = Dog()
bird = Bird()

car.move()
plane.move()
dog.move()
bird.move()

# Demonstrating polymorphism
for object in [car, plane, dog, bird]:
    object.move()

