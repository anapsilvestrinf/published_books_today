# Get all the books from your 'to-read' booklist released today delivered to your inbox.

---------------------------

## Description

This project checks a booklist from a user on GoodReads. Moreover, if the publication date of at least one of the books is today, it sends an e-mail that contains information about this book.

Additionally, you can schedule the script to run daily and receive notifications about your booklist every day without effort.

<div align="center">
    <img src="https://github.com/anapsilvestrinf/published_books_today/blob/main/email_example.png?raw=true"alt="Email example" />
</div>

## Inspiration

I enjoy reading books from indie/independent and small publishers. Moreover, many books come out every week and, consequently, I usually don't keep track of the new releases of my interest. 

Also, I have a kindle unlimited membership, and that's why I don't see any advantage in pre-ordering a book and paying more only to have it automatically on my kindle. 

So, the purpose of this project is to keep up with new book releases from a booklist without paying more and without effort.

## Prerequisites

Before running the python script, you will need to install some packages:

* Requests

* BeautifulSoup

You also need to modify the following variables at the beginning of the main.py file and add as value your personal data:

```python
####################
# Adapt for your use 
#'to-read' booklist link from the user we want, example: "https://www.goodreads.com/review/list/24011233?shelf=to-read"
user_bookshelf = "your_bookshelf_link"
# Change your email below. In this project, we will use the same email to send and receive the message, but you can modify this.
EMAIL_SENDER = "your_email"
EMAIL_RECEIVER = "your_email"
# Add the password of the sender email generated for this python script. 
# Here you can find the step-by-step of how to obtain this password: https://towardsdatascience.com/how-to-send-beautiful-emails-with-python-the-essential-guide-a01d00c80cd0
EMAIL_PASSWORD = "your_password_generated"
####################
```

As mentioned in the code, you can find how to obtain the password in [this guide.](https://towardsdatascience.com/how-to-send-beautiful-emails-with-python-the-essential-guide-a01d00c80cd0)

Lastly, you can run the `main.py` code and receive the email in your inbox.

## Support

Contributions, issues and feature requests are welcome. 

Please, ⭐️ this repository if you liked this project!

## Credits and references

* [How to generate a password that the Python script will use to log into the account and send emails](https://towardsdatascience.com/how-to-send-beautiful-emails-with-python-the-essential-guide-a01d00c80cd0)
* [How to schedule the Python Script with Windows Task Scheduler](https://www.youtube.com/watch?v=n2Cr_YRQk7o)

* [HTML email template](https://app.postdrop.io/)

-------------------------------------------------

<div align="center">
    <a href="https://github.com/anapsilvestrinf" target="_blank"> 
      <img src="https://img.shields.io/badge/made%20with%20%E2%9D%A4%EF%B8%8F%20by-anapsilvestrinf-red" alt="Made with love by anapsilvestrinf" />
	</a>
</div>



