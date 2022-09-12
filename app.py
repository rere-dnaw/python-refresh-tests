from post import Post
from blog import Blog
from datetime import datetime

# b = Blog('Dogs', 'Tom Dans')
# b.create_post('Husky', 'Drama queen')

# #b.posts.append(Post('Fiat New', 'New content info.'))
# b2 = Blog("Cars", "Tom Don",[Post('See me', 'Testing posts')])
# date = datetime.now()
# b2.create_post('Fiat', "It's a average car", date)

# print(b2.json())
def list_blogs(blogs):
    if len(blogs) != 0: 
        for blog in blogs:
            print(blog)
    else:
        print('Blog list empty!\n')

def add_blog(blogs):
    title = input('Enter blog title: ')
    author = input('Enter blog author: ')
    blogs.append(Blog(title, author))

def add_post(blogs):
    for idx, blog in enumerate(blogs):
        print(f"{idx + 1}){blog.title}")

    while True:
        blog_select = ord(input('Select block number: '))
        if blog_select in range(1, len(blogs) + 1, 1):
            title = input('Enter post title: ')
            content = input('Enter post content: ')
            blogs[blog_select - 1].posts.append(Post(title, content))
        #elif 
        else:
            print("Selected blog doen't exist! Please select agian.")

def menu():
    print(f'What do you want to do?\n1)List blogs.\n2)Add blog\n3)Add Post.\n4)Exit.')
    option = 0
    blogs = []
    while True:
        option = ord(input('Selet option: '))
        if option == 49:
            list_blogs(blogs)
        elif option == 50:
            add_blog(blogs)
        elif option == 51:
            add_post(blogs)
        elif option == 52:
            break
        else:
            continue

test = ord('1')
print(test)

menu()