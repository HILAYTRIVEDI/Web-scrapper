from urllib.request import urlopen
from Link_file import Linkfinder
from Web_crawler import *


class Spider:
    # class variables which are shared among spiders
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        # noinspection PyArgumentList
        self.boot()
        self.crawl_page('First spider ',Spider.base_url)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' now_crawling ' + page_url)
            print('links in queue ' + str(len(Spider.queue)) + "|||" + "Total files crawled " + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gathered_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_file()

    @staticmethod
    def gathered_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':
                html_byte = response.read()
                html_string = html_byte.decode("utf-8")

            finder = Linkfinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except:
            print("Error : cannot crawl page")
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:  # check that url is already in queue or not
                continue
            if url in Spider.crawled:  # check that url is already in crawled or not
                continue
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_file():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)

    @staticmethod
    def boot():
        create_project_directory(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)
