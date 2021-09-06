#===========================================================================================
# Setup 
import praw
import os

#===========================================================================================
# Classes for Image Scraper #

class redditIn:
    '''Class for a reddit user instance.'''

    def __init__(self, client_id='kyuTgV9ra6nCzDUnp3Dg9A', client_secret='ht0lNwisfQVN7CgZ6npe3i0Sy1hY5A', user_agent='my user agent'):
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent
        self.reddit = praw.Reddit(
            client_id = self.client_id,
            client_secret = self.client_secret,
            user_agent = self.user_agent
            )

#===========================================================================================
# Main cat image scrapper function # 

def catImageS(redditIn, nImages, filename='CatPicURLs.csv'):
    '''Adds a specified amount of cat picture URLs from Reddit
    to a named file; which would be created if it does not already exist.'''

    # Finds the current key value for our file (check the function checkKey for more details)
    key = checkKey(filename)
    
    count = 0
    f = open(filename, 'a')

    # Finds submissions in the 'hot' section of the 'cats' sub-reddit 
    # and appends their URLs with an index key. 
    for submission in redditIn.reddit.subreddit('cats').hot(limit=None):
        url = submission.url
        if count >= nImages:
            break
        elif url.endswith(('.jpg', '.png', '.gif', '.jpeg')):
            f.write('\n{},{},None'.format(key, url))
            count += 1
            key += 1

    f.close()

#===========================================================================================
# File functions #

def checkKey(filename):
    '''Finds the last used key value plus 1 in the cat picture url file; 
    returns 1 if the file does not exist'''

    if os.path.isfile(filename):
        with open(filename, 'rb') as f:
            f.seek(-2, os.SEEK_END)
            while f.read(1) != b'\n':
                f.seek(-2, os.SEEK_CUR)
            last_line = f.readline().decode()
        f.close()
        key = last_line.split(",")[0]
        print("File exists")
        return int(key) + 1
    else:
        print('File does not exist')
        return 1

def deleteFile(filename):
    '''Deletes specified file'''

    os.remove(filename)
    print("File Removed!")

#===========================================================================================



catsInstance = redditIn()
catImageS(catsInstance, 10, filename='CatPicURLs.csv')

