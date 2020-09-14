import threading
from queue import Queue
from Spider import Spider
from domain import *
from Web_crawler import *

PROJECT_NAME = 'Hilay 2'
HOME_PAGE = 'https://www.youtube.com/'
DOMAIN_NAME = get_domain_name(HOME_PAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 10
queue = Queue()
Spider(PROJECT_NAME,HOME_PAGE,DOMAIN_NAME)

# create threads / spiders
def create_spiders():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

#do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name,url)
        queue.task_done()


def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
        queue.join()
    crawl()



# to define how many queues are remaining
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links))+ 'links in th queue')
        create_jobs()


create_spiders()
crawl()