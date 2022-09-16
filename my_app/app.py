from post import Post
from blog import Blog

from statics import lang_eng as lang_str


def list_blogs():
    if len(blogs) != 0:
        while True:
            for idx, blog in enumerate(blogs):
                print(f"{idx + 1}) {blog}")
            select = input("Type blog number to select "
                           "(Press 'b' to go back.): ")
            if ord(select) == 98:
                break
            elif ord(select) in range(49, 49 + len(blogs) + 1, 1):
                open_blog(blogs[int(select) - 1])
            else:
                print("Selected blog doen't exist! Please try again.")
    else:
        print('Blog list empty!\n')


def open_blog(blog):
    option = 0
    while True:
        print('\nWhat do you want to do?\n1)List Posts.\n2)Add Post\n3)Back.')
        option = ord(input('Selet option: '))
        print('\n')
        if option == 49:
            for post in blog.posts:
                print(post)
        elif option == 50:
            title = input('Enter post title: ')
            content = input('Enter post content: ')
            blog.create_post(title, content)
        elif option == 51:
            break
        else:
            continue


def add_blog():
    title = input('Enter blog title: ')
    author = input('Enter blog author: ')
    blogs.append(Blog(title, author))


def add_post():
    while True:
        for idx, blog in enumerate(blogs):
            print(f"{idx + 1}){blog.title}")
        print("Press 'b' to go back.")
        blog_select = input('Select block number: ')
        if blog_select.isdigit():
            if ord(blog_select) in range(49, 49 + len(blogs), 1):
                title = input('Enter post title: ')
                content = input('Enter post content: ')
                blogs[int(blog_select) - 1].posts.append(Post(title, content))
            else:
                print("Selected blog doen't exist! Please select agian.")
        elif ord(blog_select) == 98:
            break
        else:
            print("Please use numbers to select blog!")


def menu():
    option = ord(input(lang_str.MAIN_MENU_OPT))

    while option != 52:
        if option == 49:
            list_blogs()
        elif option == 50:
            add_blog()
        elif option == 51:
            add_post()
        else:
            continue
        option = ord(input(lang_str.MAIN_MENU_OPT))


blogs = []
# menu()
