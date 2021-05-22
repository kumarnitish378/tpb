print("Loading...")


import tweepy
from time import sleep, time
from pandas import read_csv
from random import randint
import os
# Now run this File

os.system("mkdir imageFile")
dirname = os.getcwd()
read = open("TweetMessage.txt", 'a')
read.close()

class twit():
    def go(self, name):
        print("in the class", name)

    def bot(self, consumer_key, consumer_secret, key,secret, message, numbere_of_msg):
        consumer_key = consumer_key
        consumer_secret = consumer_secret
        key = key
        secret = secret
        from tweepy import OAuthHandler, API
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(key, secret)
        auth.get_username()
        API(auth)
        tweet = message
        n = int(numbere_of_msg)
        c = 0
        for i in range(n):
            api = API(auth)
            try:
                api.update_status(tweet + " " + str(time()))
                print("send {}".format(i + 1))
                sleep(0.2)
                c += 1
            except Exception as eroor:
                print(eroor)
                pass
        print("succesfull send = {}".format(c))


    def findTag(self, consumer_key, consumer_secret, key,secret, Tag, date_since="12-03-2019", items=10):
        consumer_key = consumer_key
        consumer_secret = consumer_secret
        key = key
        secret = secret

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(key, secret)
        b = auth.get_username()
        api = tweepy.API(auth)
        search_words = Tag
        n = int(items)
        tweets = tweepy.Cursor(api.search,
                           q=search_words,
                           lang="en",
                           since=date_since).items(n)

        for tw in tweets:
            print(tw.text)


    def postWithImage(self, consumer_key, consumer_secret, key,secret, message, numbere_of_msg, file_name):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(key, secret)
        auth.get_username()
        api = tweepy.API(auth)
        media = api.media_upload(file_name)
        tweet = message
        for tw in range(int(numbere_of_msg)):
            api.update_status(status=tweet, media_ids=[media.media_id])
            print("Send Done!")
            sleep(0.2)


if __name__ == "__main__":

    consumer_key = ["consumer_key"]
    consumer_secret = ["consumer_secret"]
    key = ["key"]
    secret = ["secret"]
    data = ""
    try:
        print("Loading credential File...")
        data = read_csv(dirname+'\credential.csv')
        print("reading Done!")
    except Exception as xyz:
        print(xyz)
        exit("credential.csv Not Found ")
    obj = []
    number_of_Bot = len(data)
    print("Number Of Bot: {}".format(number_of_Bot))
    # Creating Bot Object
    if number_of_Bot > 0:
        for i in range(number_of_Bot):
            obj.append(twit())

        # Storing All Credentials
        consumer_key = list(data["consumer_key"])
        consumer_secret = list(data["consumer_secret"])
        key = list(data["key"])
        secret = list(data["secret"])
    else:
        print("First You Need to Add API Credentials in 'credential.csv' file")
        c = input("press q for Exit :> ")
        while c != 'q':
            pass
        exit("Thanks! ")
    # ----------------Banner----------------------

    print("""
    ++--------------+-----------------+-------------------++
    ++--------------+-----------------+-------------------++
    ||   |||||||||*     |||||||||||||      ||||||||||*    ||
    ||   ||       ||         ||            ||        ||   ||
    ||   ||       ||         ||            ||        ||   ||
    ||   |||||||||*          ||            ||||||||||*    ||
    ||   ||                  ||            ||        ||   || 
    ||   ||                  ||            ||        ||   ||
    ||   ||          *       ||         *  ||||||||||*    ||
    ++--------------+-----@pycat378---+-------------------++
      >>>>>>>>>>>>  hacktheworld378@gmail.com  <<<<<<<<<<<<
    ++---Python-----+----Twitter------+-----Bot-----------++
        """)
    while True:
        print("""
        [1]. For Text only Post
        [2]. For Text with Image
        [3]. Help 
        [0]. For Quit
        """)

        choice = ""
        while True:
            choice = int(input("PTB :> "))
            if choice == 1:
                break
            elif choice == 2:
                break
            elif choice == 0:
                exit("Thanks for Using! ")
            elif choice == 3:
                print("""
                    help :> Fist You Need to Add All API Credential in "credential.csv" file
                    help :> Then You can Add You message with #tag or without #tag in "TweetMessage.txt" file Line Wise
                            You Can Add Multiple Message in This File.
                    help :> You can Use Multiple Bot at the Same Time by adding Multiple
                            API Credential in "credential.csv" File 
                        """)
            else:
                print("Select Valid Option :( ")
        if choice == 1:
            # --------------------------------------
            number_of_msg = input("Enter No of message :> ")
            # --------------------------------------
            # Creating objects for multiple tweets only Text message
            text_choice = input("Do you want to use TweetMessage.txt file for Tweet Message? (y/n) :> ")
            if text_choice == 'n':
                mess = input("Enter Text for Post :> ")
                message = [mess]
            else:
                read = open("TweetMessage.txt", 'r')
                message = read.readlines()
                read.close()
            while message is None:
                mess = input("Enter Text for Post :> ")
                message = [mess]
            print("Numer of message = {}".format(len(message)))
            if 2 == 2:
                for j in range(number_of_Bot):
                    obj[j].bot(consumer_key[j], consumer_secret[j], key[j], secret[j], message[randint(0, len(message)-1)], number_of_msg)
                # Creating Multiple Process Parallel
                # ----------------------------------------------------- #
                # process = []
                # for i in range(number_of_Bot):
                #     process.append(mlt.Process(target=obj[i].bot, args=(consumer_key[i], consumer_secret[i], key[i], secret[i], message[randint(0, len(message))], number_of_msg),))
                #
                # # start process
                # for j in process:
                #     j.start()
                #     # j.join()
                # for j in process:
                #     j.join()
                # ----------------------------------------------------- #
                print("Completed! ")

        if choice == 2:
            pcaption = ""
            caption_text = ""
            list_of_img = os.listdir(dirname+"\imageFile")
            number_of_img = len(list_of_img)
            print("We found {} Images: ".format(number_of_img))
            if number_of_img > 0:
                caption_text = input("Enter Message for post: ")
                pcaption = caption_text
            count = 0
            if number_of_img > 0:
                for text in range(number_of_img):
                    if count != 0:
                        yesno = input("Do you want to Go with Same Caption? (y/n): ")
                        if yesno == 'n' or yesno == 'N':
                            caption_text = input("Enter Message for post: ")
                            count = 1
                        else:
                            caption_text = pcaption
                    count = 1
                    caption_text = caption_text+" "+ str(time())
                    file_path = dirname+"\imageFile"+"\\"+list_of_img[text]
                    post_object = []
                    for post in range(number_of_Bot):
                        post_object.append(twit())

                    for jj in range(number_of_Bot):
                        post_object[jj].postWithImage(consumer_key[jj], consumer_secret[jj], key[jj], secret[jj],
                                                      caption_text, "1", file_path)
                    try:
                        print(file_path)
                        os.remove(file_path)
                    except:
                        pass
                print("All process Done!")
            else:
                print("There is No any image file. First you need to Add images")

        while True:
            abc = input("Do You want Continue (y/n)")
            if abc == 'y':
                break
            if abc == 'n':
                exit("Thanks! ")