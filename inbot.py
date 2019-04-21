import praw
import os
import urllib.request
import time
from PIL import Image
from Naked.toolshed.shell import execute_js


subreddits = "memes"
hashtags = "#reddit #memes #meme #memes #bestmemes #instamemes #funny #funnymemes #dankmemes #offensivememes #edgymemes #spicymemes #nichememes #memepage #funniestmemes #dank #memesdaily #jokes #memesrlife #memestar #memesquad #humor #lmao #igmemes #lol #memeaccount #memer #relatablememes #funnyposts #sillymemes #nichememe #memetime"
posts_per_day = 5000


def bot_login():
    print('Logging in...')
    r = praw.Reddit(username='YOUR USERNAME HERE',
                    password='YOUR PASSWORD HERE',
                    client_id='YOUR CLIENT ID HERE',
                    client_secret='YOUR CLIENT SECRET HERE',
                    user_agent='A Bot that reposts Reddit Posts onto Instagram')
    print('Logged in as user: "'+str(r.user.me())+'"')
    print("------------------------------------------------------------------")
    return r


def run_bot(r, posts_found):
    # goes though hot posts of the day
    for i in range(int(posts_per_day*1.25+5)):
        print("Serching for top post in r/"+subreddits)
        try:
            submission = list(r.subreddit(subreddits).hot(limit=(int(posts_per_day*1.25+5))))[i]
            # checks it hasn't already posted it
            if submission not in posts_found:
                print(f"Current hot post in r/"+subreddits+" rank({str(i+1)}) is post titled: " +
                      str(submission.title)+", id number: "+str(submission))
                print("--------------------------------------------------")
                # saves image to folder
                image_url = submission.url.replace("https", "http")
                print(f"url: {image_url}")
                urllib.request.urlretrieve(image_url,
                                           str(submission.title)+".jpg")
                print("Saved Image: "+submission.id+" to folder")
                posts_found.append(submission.id)
                # changes it to fit Instagrams aspect ratio
                print("Changing aspect ratio")
                im = Image.open(submission.title+".jpg")
                x, y = im.size
                if x >= y:
                    desired_width = x
                    desired_height = x
                else:
                    desired_height = y
                    desired_width = y
                w = max(desired_width, x)
                h = max(desired_height, y)
                new_im = Image.new("RGB", (w, h), (255, 255, 255))
                new_im.paste(im, ((w - x) // 2, (h - y) // 2))
                new_im.save(submission.title+".jpg", "JPEG")
                hi = (submission.id + "\n")
                # Adds to the list of posts found
                with open("Memory/posts_found.txt", "a") as f:
                    f.write(hi)
                with open("Memory/Caption.txt", "a") as f:
                    f.write(submission.title)
                with open("Memory/Caption2.txt", "a") as f:
                    f.write("\n-\nmirrored from a post on r/"+subreddits+" by u/"+str(submission.author)+":https://reddit.com/"+hi + "\n using a bot made by @nateweav_ :)\n"
                            " \n\n•\n•\n•\n•\n•\n•\n•\n•\n\n" + hashtags)
                print("Saved post id")
                print("---------------------------------------------------")
                print("Posting to Instagram")
                # runs Instagram script
                success = execute_js('Instagram.js')
                if success:
                    print("Done")
                    os.remove(submission.title+".jpg")
                else:
                    print("Failed to upload")
                break
            else:
                print("No new post")
        except Exception:
            print("post "+str(i)+" is not compatable")
            print("------------------------------------------------------")
            pass

# function to chech what posts have been posted


def get_saved_posts():

    with open("Memory/posts_found.txt", "r+") as f:
        posts_found = f.read()
        posts_found = posts_found.split("\n")
        # print(posts_found)

    return posts_found


# login to reddit
r = bot_login()
run_number = 1
while True:
    # clears captions
    open("Memory/Caption.txt", 'w').close()
    open("Memory/Caption2.txt", 'w').close()
    posts_found = get_saved_posts()
    run_bot(r, posts_found)
    print("Run number: "+str(run_number))
    run_number += 1
    print(f"Waiting {str(24/posts_per_day)} hours before posting again")
    time.sleep(24/posts_per_day*3600)
