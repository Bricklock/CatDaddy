import praw

reddit = praw.Reddit(
    client_id='kyuTgV9ra6nCzDUnp3Dg9A',
    client_secret='ht0lNwisfQVN7CgZ6npe3i0Sy1hY5A',
    user_agent='my user agent' )

file = open('CatPicURLs.csv', 'a')
key = 1

for submission in reddit.subreddit('cats').new(limit=10):
    url = submission.url
    if url.endswith(('.jpg', '.png', '.gif', '.jpeg')):
        file.write('\n{},{},None'.format(key, url))
        key += 1

file.close()