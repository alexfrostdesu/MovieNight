import os
import random
# from colorama import init, Fore, Back, Style

# print(Fore.RED + 'some red text' + Fore.GREEN + 'some more text')
# print(Back.GREEN + 'and with a green background')
# print(Style.BRIGHT + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')


def check_file(file):
    if os.path.isfile(file):
        mode = 'a+'
    else:
        mode = 'w+'
    return mode


# init()
PATH = os.getcwd()
watchlist = './wanttowatchlist'
os.chdir(PATH)
mode = check_file(watchlist)
movies_to_show = 10
files_extensions = ['.mkv', '.avi', '.m4v', '.wmv', '.mov']


def print_movies(movie_list, amount=None):
    if amount <= len(movie_list):
        for movie in movie_list:
            print(movie)
            if movie_list.index(movie) >= amount:
                print('.\n.\nand more...')
                print('Show all movies? (Y/N)')
                break
        if input().lower() == 'y':
            for movie in movie_list:
                print(movie)
    else:
        for movie in movie_list:
            print(movie)


def get_movie_files():
    all_directory_files = os.listdir(PATH)
    movie_files = dict([(file, os.path.getctime(PATH + '/' + file)) for file in all_directory_files if
                        any(file.endswith(ext) for ext in files_extensions)])
    sorted_movie_files = sorted(movie_files, key=movie_files.get, reverse=True)
    return sorted_movie_files


def show_watchlist():
    print('Show your want to watch list? (Y/N)')
    if input().lower() == 'y':
        with open(watchlist, 'r', encoding='utf-8') as file:
            watch_list = [movie[:-1] for movie in file if movie != '']
        print(f'{len(watch_list)} movies in your want to watch list:')
        print_movies(watch_list, movies_to_show)


def add_movies_to_watchlist():
    movie_files = get_movie_files()
    print('Add movies from directory one by one? (Y/N)')
    if input().lower() == 'y':
        file = open(watchlist, mode, encoding='utf-8')
        for movie in movie_files:
            print(movie)
            print('Add the movie? (Y/N/Q)')
            answer = input().lower()
            if answer == 'y':
                file.write(movie + '\n')
            elif answer == 'q':
                break
        file.close()


def create_watchlist():
    print('Create new movie list? (Y/N)')
    if input().lower() == 'y':
        movie_files = get_movie_files()
        if movie_files:
            print(f'Found {len(movie_files)} movies:')
            print_movies(movie_files, movies_to_show)
            print('Add them all to want to watch list? (Y/N)')
            if input().lower() == 'y':
                with open(watchlist, mode, encoding='utf-8') as file:
                    for movie in movie_files:
                        file.write(movie + '\n')
            else:
                add_movies_to_watchlist()
        else:
            print('No movie files found, please check directory or files extensions')
            exit()
    else:
        print('You need to create want to watch list first')


def select_movie():
    with open(watchlist, 'r', encoding='utf-8') as file:
        watch_list = [movie[:-1] for movie in file if movie != '']
    print('Selecting movie from watchlist')
    movie = random.choice(watch_list)
    print('Start Movie? (Y/N) \n' + movie)
    print(PATH + '/' + movie)
    if input().lower() == 'y':
        os.startfile(PATH + '/' + movie)


def main():
    if os.path.isfile(watchlist):
        show_watchlist()
        print('Add new movies to the want to watch list? (Y/N)')
        if input().lower() == 'y':
            add_movies_to_watchlist()
            show_watchlist()
        select_movie()

    else:
        create_watchlist()
        main()


if __name__ == '__main__':
    main()
