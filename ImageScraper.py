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
    
    oldSubmissions = []
    checkData = []
    if fileExistence(filename):
        with open(filename, "r") as f:
            oldSubmissions = f.readlines()[1:]
        f.close()
        checkData = []
        for i in range(len(oldSubmissions)):
            oldSubmissions[i] = oldSubmissions[i].strip("\n").split(",")
            oldSubmissions[i][1] = float(oldSubmissions[i][1])
            checkData.append([oldSubmissions[i][0], float(oldSubmissions[i][1])])


    submissionData = getSubmissions(redditIn, nImages, checkData)

    if fileExistence(filename):
        submissionData.extend(oldSubmissions)
    submissionSortedData = sorted(submissionData, key = lambda x: x[1])
    with open(filename, "w") as f:
        f.write("submissionID,timeCreatedUnix,url,rating")
        for submission in submissionSortedData:
            f.write("\n{},{},{},None".format(submission[0], submission[1], submission[2]))
        f.close()

#===========================================================================================
# File functions #

def checkKey(filename):
    '''Finds the last used key value plus 1 in the cat picture url file'''
    with open(filename, 'rb') as f:
        f.seek(-2, os.SEEK_END)
        while f.read(1) != b'\n':
            f.seek(-2, os.SEEK_CUR)
        last_line = f.readline().decode()
    f.close()
    key = last_line.split(",")[0]
    return int(key) + 1

def deleteFile(filename):
    '''Deletes specified file'''
    os.remove(filename)
    print("File Removed!")

def fileExistence(filename):
    '''Checks if the given file exists.'''
    return os.path.isfile(filename)
    

def checkInFile(id, timeCreated, checkData):
    for submission in checkData:
        if id == submission[0] and timeCreated == checkData[1]:
            return True
    return False

#===========================================================================================

def getSubmissions(redditIn, nImages, checkData):
    '''Gets reddit submission instances from the cats subreddit top week page.'''
    submissionData = []
    count = 0
    for submission in redditIn.reddit.subreddit('cats').top("week", limit=None):
        url = submission.url
        id = submission.id
        timeCreated = submission.created
        if count >= nImages:
            break
        elif url.endswith(('.jpg', '.png', '.gif', '.jpeg')) and not checkInFile(id, timeCreated, checkData):
            submissionData.append([id, timeCreated, url])
            count += 1
    return submissionData

#===========================================================================================
filename='CatPicURLs.csv'
catsInstance = redditIn()
catImageS(catsInstance, 2000, filename)
#deleteFile(filename)