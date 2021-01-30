import praw
import datetime
from praw.models import MoreComments
import csv

reddit = praw.Reddit(client_id = '1epYXaQUEU0ayA',
                    client_secret = 'T7-VTUva1G-E_kGa8yHKZBOKJNvlpg',
                    username = 'Saurabh_Joshi_24',
                    password = 'your_password',
                    user_agent = 'scrapper'
                    )

# print(reddit.user.me())

subreddit = reddit.subreddit('wallstreetbets')

hot_wallstreetbets = subreddit.hot(limit=15)

data_lists = []


for posts in hot_wallstreetbets:

    if not posts.stickied:    
    
        time = str(datetime.datetime.fromtimestamp(posts.created))
        Author = str(posts.author)
        Title = str(posts.title)
        message = str(posts.media)
        replies = str(message)
        upvotes = str(posts.ups)
        downvotes = str(posts.downs)
       
        data = [time, Author, Title, message, upvotes, downvotes]
        data_lists.append(data)
        print('Inserting POST Records....')

        for comment in subreddit.comments(limit=None):

            time = str(datetime.datetime.fromtimestamp(comment.created_utc))
            Author = str(comment.author)
            message = str(comment.body)
            replies = str(message)
            upvotes = str(comment.score)
            downvotes = str(comment.downs)

            data = [time, Author, Title, message, upvotes, downvotes]
            data_lists.append(data)

            print('|---------------------------------------------------------|')
            print('Inserting all the individual replies....')
    
    print('|---------------------------------------------------------|')
    

with open('./Dataset/raw_dataset.csv', 'w', encoding='utf-8') as file:

    writer = csv.writer(file)
    writer.writerow(['Time', 'Author', 'Title', 'Replies', 'upvotes', 'downvotes']) #header

    for row in data_lists:
        writer.writerow(row)

# with open('./Dataset/raw_dataset.txt', 'w', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerow(['Time', 'Author', 'Title', 'Replies\n', 'upvotes', 'downvotes']) #header
#     for row in data_lists:
#         f.write(" ".join(row))
