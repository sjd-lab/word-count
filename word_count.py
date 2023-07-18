import os
import argparse
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor


def word_count_counter(textfile):
    """Using collectons Counter 

    Args:
        textfile (str): text file 

    Returns:
        dict: dictionary of word count
    """
    print('using counter')
    with open(textfile) as file:
        filetext = file.read().lower()
        filetext = filetext.split()
        return dict(Counter(filetext))


def word_count(textfile):
    """Using counter logic"""
    print('using counter logic')
    words_count = defaultdict(int)
    with open(textfile) as file:
        filetext = file.read().lower()
        words = filetext.split()
        for word in words:
            words_count[word] += 1
    return dict(words_count)


def word_count_text(textdata):
    """Using collectons Counter and text input"""
    print('using counter text')
    filetext = textdata.lower().split()
    return Counter(filetext)


def read_chunk(textfile, chunk_size):
    with open(textfile) as file:
        while True:
            filetext = file.read(chunk_size)
            if not filetext:
                break
            yield filetext


def word_count_multithread(textfile, threads):
    "Using multithread"
    print('using multi thread')
    file_size = os.path.getsize(textfile)
    chunk_size = int(file_size / threads)
    with ThreadPoolExecutor() as executor:
        results = executor.map(
            word_count_text, read_chunk(textfile, chunk_size))

    merged_count = Counter()
    for result in results:
        merged_count += result
    return dict(merged_count)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="word count")
    parser.add_argument("-f", "--file", type=str)
    parser.add_argument("-c", "--counter",
                        help="Use collections.counter", type=int, default=0)
    parser.add_argument("-t", "--threads", type=int,
                        help="Enable multithreading by giving number of threads", default=0)

    args = parser.parse_args()
    if args.counter:
        print(word_count_counter(textfile=args.file))
    elif args.threads:
        print(word_count_multithread(textfile=args.file, threads=args.threads))
    else:
        print(word_count(textfile=args.file))
