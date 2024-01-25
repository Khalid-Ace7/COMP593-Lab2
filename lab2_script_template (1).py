def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {"full_name": "KHALID UDDIN",
                "student_id": 10313140,
                "pizza_toppings": ["Mushrooms","Sausage","Onion"],
                'movies': [
                    {"title": "Milkha Singh","genere": "Documentary"},
                    {"title": "Crazy jatta","genere": "Comedy"}]
                }

    # TODO: Step 3 - Add another movie to the data structure
    about_me["movies"].append({"title": "Anohana", "genere": "Romantic"})
    
    print_student_name_and_id(about_me)
    
    
    # TODO: Step 6 - Call the function to print a bullet list of pizza toppings before adding toppings
    print_pizza_toppings(about_me)

    # TODO: Step 5 - Call the function to add more pizza toppings
    add_pizza_toppings(about_me, ("Ham", "Pineapple"))

    # TODO: Step 6 - Call the function to print a bullet list of pizza toppings after adding toppings
    print_pizza_toppings(about_me)

    # TODO: Step 7 - Call the function to print a comma-separated list of movie genres
    print_movie_genres(about_me)

    # TODO: Step 8 - Call the function to print a comma-separated list of movie titles
    print_movie_titles(about_me['movies'])


# TODO: Step 4 - Function that prints student name and ID
def print_student_name_and_id(about_me):
    full_name = about_me["full_name"]
    first_name = (full_name.split(" "))[0]
    student_id = about_me['student_id']
    print(f"My name is {full_name}, but you can call me Mr.{first_name}.")
    print(f"My student ID is {student_id}.")


# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'].extend(toppings)
    about_me['pizza_toppings'] = sorted([topping.lower() for topping in about_me['pizza_toppings']])


# TODO: Step 6 - Function that prints a bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print("My favourite pizza toppings are:")
    for topping in about_me['pizza_toppings']:
        print(f"- {topping.capitalize()}")
    print()


# TODO: Step 7 - Function that prints a comma-separated list of movie genres
def print_movie_genres(about_me):
    genres = [movie['genere'] for movie in about_me['movies']]
    print(f"I like to watch {', '.join(genres)} movies.\n")


# TODO: Step 8 - Function that prints a comma-separated list of movie titles
def print_movie_titles(movie_list):
    titles = [movie['title'] for movie in movie_list]
    formatted_titles = ', '.join([title.capitalize() for title in titles])
    print(f"Some of my favourite movies are {formatted_titles}!\n")


if __name__ == '__main__':
    main()