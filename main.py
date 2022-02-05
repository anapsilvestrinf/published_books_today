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
import most_email_template as template
import requests
from bs4 import BeautifulSoup
import datetime as dt
import smtplib
from email.message import EmailMessage
####################
# First step: Get the expected publications:
def html_page(link):
    response = requests.get(link)
    return response.content

def find_all_pages(link_first_page):
    pages_bookshelf = []
    parser = BeautifulSoup(html_page(link_first_page), 'html.parser')

    obj_pagination = parser.find(id="reviewPagination")
    for href in obj_pagination.find_all("a"):
        if href is not None:
            link = href.get("href")
            link = "https://www.goodreads.com" + link
            if link not in pages_bookshelf and link != link_first_page:
                pages_bookshelf.append(link)
        
    return pages_bookshelf

def find_expected_books(page):
    parser = BeautifulSoup(page, 'html.parser')
    books = parser.find(id="booksBody")
    pub_dates = {}
    # Test a random publishing date from your booklist: today = dt.datetime.strptime("Oct 30, 2021", "%b %d, %Y").date() 
    today = dt.date.today()

    for book in books.find_all("tr"):
        field_title = book.find(class_="field title")
        title = field_title.find("a").get("title")
        link_book = "https://www.goodreads.com" + field_title.find("a").get("href")

        field_author = book.find(class_="field author")
        author = field_author.find("a").text
        field_date_pub_edition = book.find(class_="field date_pub_edition")
        expected_date = field_date_pub_edition.find(class_="value").text.strip("\n").strip()

        #expected_date must be greater than or equal to "(3 char) (2 numbers), (4 numbers)"
        if expected_date is not None and expected_date != 'unknown' and len(expected_date) >= 12:
            expected_date = dt.datetime.strptime(expected_date, "%b %d, %Y")
            if expected_date.date() == today:
                pub_dates[title] = [author, link_book]

    return pub_dates

def find_amazon_link(html_book):
    parser = BeautifulSoup(html_book, 'html.parser')
    link = parser.find("a", id = "buyButton").get("href")
    return "https://www.goodreads.com" + link

html = html_page(user_bookshelf)

pages = find_all_pages(user_bookshelf)

books_all_pages = find_expected_books(html)

for page_link in pages:
    html = html_page(page_link)
    books_all_pages.update(find_expected_books(html))

if books_all_pages is not None:
    for key in books_all_pages:
        link_book = books_all_pages[key][1]
        html_book = html_page(link_book)
        amazon_link = find_amazon_link(html_book)
        books_all_pages[key].append(amazon_link)

    #print(books_all_pages)
    ####################
    # Second step: Send the e-mail if there's any book being published in the day
    
    message = EmailMessage()
    message['From'] = EMAIL_SENDER
    message['To'] = EMAIL_RECEIVER
    message['Subject'] = f'Books being released: {dt.date.today().strftime("%b %d, %Y")}'

    #Email template

    html_beginning = template.html_beginning_template
    html_ending = template.html_ending_template
    html_middle_template = template.html_middle_template

    html_template = [html_beginning]
    for key in books_all_pages:
        html_template.append(html_middle_template.format(books_all_pages[key][1], key, books_all_pages[key][0], books_all_pages[key][2]))

    html_template.append(html_ending)
    html_template = ' '.join(html_template)
    message.set_content(html_template, subtype='html')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.send_message(message)

####################
# Third step: Schedule this script. 
# For instance, you can schedule this script using Windows Task Scheduler.