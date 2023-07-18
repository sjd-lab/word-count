# word-count
Word count from a given file using different methods

usage: word_count.py [-h] [-f FILE] [-c COUNTER] [-t THREADS]

Get word count using different approches (dictionary, collections.Counter, multithreading using concurrent.futures).

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE
  -c COUNTER, --counter COUNTER
                        Use collections.counter
  -t THREADS, --threads THREADS
                        Enable multithreading by giving number of threads

eg :
python .\word_count.py -f "gnu.org_licenses_gpl-3.0.txt"