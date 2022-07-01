
movies, likes, dislikes = [], [], []
choice = None
mov_sel = None
print("Welcome to the Programming Course Movie Database (PCMDB) In")
while choice != 0:
    print("1: Enter a new film\n"
          "2: Like / dislike a film")
    choice = int(input("Enter your option (0 exit): "))
    # if choice != 0:
    if choice != 1 and choice != 2:
        print("Wrong option")
    else:
        if choice == 1:
            movies.append(input("Enter the film name: "))
            likes.append(0)
            dislikes.append(0)
            print(movies[-1])
        if choice == 2:
            print("'This is the list of movies!")
            for i in range(len(movies)):
                print(i+1, movies[i], "\n\t"
                      "likes: ", likes[i], "dislikes: ", dislikes[i])
                mov_sel = int(input("Enter the number of the movie you want to vote."))
                if mov_sel > int(len(movies)):
                    print('Wrong fil number')
                else:
                    valoration = input(" Did you like it (yes/no) ?")
                    if valoration == "no":
                        dislikes[mov_sel-1] += 1
                    elif valoration >= "yes":
                        likes[mov_sel-1] += 1
                    print("Thanks, now the film has:\n "
                          "Likes", likes[mov_sel-1], "Dislikes", dislikes[mov_sel-1])
print("Thanks for using the program!.")
