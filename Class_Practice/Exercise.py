name = "Richard"
major = "Computer Science"
hobbies = ["video games, ", "music, ", "movies, ", "working out"]
favMovie = "Star Wars, all of em"
career = "Advice for changing careers, as and older candidate, applying for entry level jobs with not much relevent experience?"
print(f"Hello, my name is {name} and I am a {major} here at UWM. Some hobbies I enjoy are: ", end = "")
for hobby in hobbies:
  print(hobby, end = "")
print(f". My favorite movie is {favMovie}.")
