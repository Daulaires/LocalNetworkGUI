import requests
from tkinter import simpledialog

class CustomRequester:
    """HTTPAPI Requester"""
    def __init__(self, url):
        self.url = url
        

    def get():
        """Website Getter"""
        # ask what website to get
        url = simpledialog.askstring("Website", "Enter Website")
        amount = simpledialog.askinteger("Amount", "Enter Amount")
        r = [requests.get(url).headers]
        for i in range(amount):
            r.append(requests.get(url).headers)
            print(i)
        return 0
    def Post():
        """Website Poster"""
        # ask what website to post to
        url = simpledialog.askstring("Website", "Enter Website")
        # ask what to post
        data = simpledialog.askstring("Data", "Enter Data")
        # post to website
        r = requests.post(url, data)
        # print the website
        print(r)
        return 0
    