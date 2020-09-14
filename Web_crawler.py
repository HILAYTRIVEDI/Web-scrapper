import os


# Every website u crawl is the seperate folder


def create_project_directory(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)


# Create queue and crawled files

def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Create a new file


def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# Add data on to existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Delete the context of file
def delete_file_context(path):
    with open(path, 'w'):
        pass


# read file and store in the perticular set
def file_to_set(file_name):
    result = set()
    with open(file_name, 'rt') as f:
        for line in f:
            result.add(line.replace('\n', ''))
    return result


# iterate through the set and each line in the set is a new file
def set_to_file(links, file):
    delete_file_context(file)
    for link in sorted(links):
        append_to_file(file, link)
