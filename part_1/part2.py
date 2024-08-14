#!/usr/bin/env python
# coding: utf-8

# #### Fill the gaps in the code.
# 
# ---
# 
# ### Cheap Crowdfunding Problem
# 
# There is a crowdfunding project that you want to support. This project gives the same reward to every supporter, with one peculiar condition: the amount you pledge must not be equal to any earlier pledge amount.
# 
# You would like to get the reward, while spending the least amount > 0.
# 
# You are given a list of amounts pledged so far in an array of integers. You know that there is less than 100,000 of pledges and the maximum amount pledged is less than $1,000,000.
# 
# Implement a function `find_min_pledge(pledge_list)` that will return the amount you should pledge.
# 
# ---
# 

# In[6]:


def find_min_pledge(pledge_list):
    existing_pledges = set(pledge_list)
    min_pledge = 1
    
    while min_pledge in existing_pledges:
        min_pledge += 1
    
    return min_pledge


# ### Extract Titles from RSS feed
# 
# Implement `get_headlines()` function. It should take a URL of an RSS feed and return a list of strings representing article titles.
# 

# In[7]:


import xml.etree.ElementTree as ET
import requests

def get_headlines(rss_url):
    """
    Fetches and parses the RSS feed from the given URL to extract article titles.
    Uses xml.etree.ElementTree for XML parsing.
    """

    response = requests.get(rss_url)
    response.raise_for_status()  
    root = ET.fromstring(response.content)
    titles = [item.find('title').text for item in root.findall('.//item')]
    return titles


google_news_url = "https://news.google.com/news/rss"
print(get_headlines(google_news_url))


# ### Streaming Payments Processor
# 
# The function `process_payments()` processes a large, but finite amount of payments in a streaming fashion. It relies on two library functions: `stream_payments_to_storage(storage)` reads payments from a processor and writes them to storage by calling `storage.write(buffer)` on its `storage` argument, which is supplied by the `get_payments_storage()` function.
# 
# **TODO:** Modify `process_payments()` to print a checksum of bytes written by `stream_payments_to_storage()`. The checksum is a simple arithmetic sum of bytes. For example, if `bytes([1, 2, 3])` were written, it should print `6`.
# 
# **Restrictions:**
# - Only one call each to `get_payments_storage()` and `stream_payments_to_storage()`
# - No reading from storage
# - No disk use for temporary storage
# - System memory cannot hold all payments
# 
# 

# In[8]:


import io

def get_payments_storage():
    """
    Returns an instance of io.BufferedWriter for Windows, using 'NUL' to discard output.
    """
    return open('NUL', 'wb')

def stream_payments_to_storage(storage):
    """
    Loads payments and writes them to the `storage`.
    Returns when all payments have been written.
    """
    for i in range(10):
        storage.write(bytes([1, 2, 3, 4, 5]))

def process_payments():
    
    class ChecksumStorage(io.BufferedWriter):
        def __init__(self, raw):
            super().__init__(raw)
            self.checksum = 0  

        def write(self, b):
            self.checksum += sum(b)
            return super().write(b)

    with get_payments_storage() as raw_storage:
        checksum_storage = ChecksumStorage(raw_storage)
        
        stream_payments_to_storage(checksum_storage)

        print("Checksum of bytes written:", checksum_storage.checksum)

process_payments()


# ### Streaming Payments Processor, Two Vendors Edition
# 
# We've enhanced our payment processor system by contracting two vendors to implement `stream_payments()` and `store_payments()` functions. The new function, `process_payments_2()`, processes payments in a streaming manner. However, the vendors provided functions with incompatible APIs.
# 
# **TODO:** Analyze the APIs of `stream_payments()` and `store_payments()` and write glue code in `process_payments_2()` to integrate these functions effectively.
# 
# **Restrictions:**
# - Only one call each to `stream_payments()` and `store_payments()`
# - No reading from storage
# - No disk use for temporary storage
# - System memory cannot hold all payments
# 

# In[9]:


import io

def stream_payments(callback_fn):
    """
    Reads payments from a payment processor and calls `callback_fn(amount)` for each payment.
    Returns when there is no more payments.
    """
    for amount in range(1, 11):
        callback_fn(amount)

def store_payments(amount_iterator):
    """
    Iterates over the payment amounts from amount_iterator and stores them to a remote system.
    """

    for amount in amount_iterator:
        print(f"Stored payment amount: {amount}")

def process_payments_2():
    """
    Glue code to connect stream_payments and store_payments using a generator.
    """
    def payment_generator():
        """
        Generator function to adapt streamed payments for storing.
        """
        payments = []
        def callback(amount):
            payments.append(amount)
            return True
        
        stream_payments(callback)
        

        for payment in payments:
            yield payment
    

    store_payments(payment_generator())


process_payments_2()


# ### Code Review
# 
# Please do a code review for the following snippet. Add your review suggestions inline as Python comments.
# 

# In[10]:


def get_value(data, key, default, lookup=None, mapper=None):
    """
    Finds the value from data associated with key, or default if the key isn't present.
    If a lookup enum is provided, this value is then transformed to its enum value.
    If a mapper function is provided, this value is then transformed by applying mapper to it.
    """
    return_value = data[key]  # This will raise KeyError if key is not in data.
    if return_value is None or return_value == "":
        return_value = default
    if lookup:
        return_value = lookup[return_value]  # This may raise KeyError if return_value is not in lookup.
    if mapper:
        return_value = mapper(return_value)
    return return_value

# Review suggestions:
# - Use data.get(key) instead of data[key] to prevent KeyError if the key is missing.
# - Add error handling or checks before accessing lookup to prevent potential KeyError.
# - Ensure that default values are handled properly, especially if None is a valid data value.


# In[11]:


def get_value(data, key, default, lookup=None, mapper=None):
    """
    Finds the value from data associated with key, or default if the key isn't present.
    If a lookup enum is provided, this value is then transformed to its enum value.
    If a mapper function is provided, this value is then transformed by applying mapper to it.
    """
    return_value = data.get(key, default)  # Safer access with default fallback
    if return_value in [None, ""]:
        return_value = default
    if lookup and return_value in lookup:
        return_value = lookup[return_value]  # Safely access lookup
    if mapper:
        return_value = mapper(return_value)
    return return_value


# ---

# In[12]:


def ftp_file_prefix(namespace):
    """
    Given a namespace string with dot-separated tokens, returns the
    string with the final token replaced by 'ftp'.
    Example: a.b.c => a.b.ftp
    """
    return ".".join(namespace.split(".")[:-1]) + '.ftp'

# Review suggestions:
# - Check if namespace is empty or doesn't contain dots to handle potential errors.
# - Add a check to return an unchanged namespace if no dots are present.


# In[13]:


def ftp_file_prefix(namespace):
    """
    Given a namespace string with dot-separated tokens, returns the
    string with the final token replaced by 'ftp'.
    Example: a.b.c => a.b.ftp
    """
    if not namespace:
        return namespace  # Return unchanged if empty
    parts = namespace.split(".")
    if len(parts) == 1:
        return namespace  # Return unchanged if no dots
    return ".".join(parts[:-1]) + '.ftp'


# ---

# In[14]:


def string_to_bool(string):
    """
    Returns True if the given string is 'true' case-insensitive,
    False if it is 'false' case-insensitive.
    Raises ValueError for any other input.
    """
    if string.lower() == 'true':
        return True
    if string.lower() == 'false':
        return False
    raise ValueError(f'String {string} is neither true nor false')

# Review suggestions:
# - Good error handling with ValueError for unexpected strings.
# - Ensure input validation is done where this function is called to handle non-string inputs.


# In[15]:


def string_to_bool(string):
    """
    Returns True if the given string is 'true' case-insensitive,
    False if it is 'false' case-insensitive.
    Raises ValueError for any other input.
    """
    if isinstance(string, str):
        lower_string = string.lower()
        if lower_string == 'true':
            return True
        if lower_string == 'false':
            return False
    raise ValueError(f'String {string} is neither true nor false')


# ---

# In[16]:


def config_from_dict(dict):
    """
    Given a dict representing a row from a namespaces csv file,
    returns a DAG configuration as a pair whose first element is the
    DAG name and whose second element is a dict describing the DAG's properties.
    """
    namespace = dict['Namespace']
    return (dict['Airflow DAG'], {
        "earliest_available_delta_days": 0,
        "lif_encoding": 'json',
        "earliest_available_time": get_value(dict, 'Available Start Time', '07:00'),
        "latest_available_time": get_value(dict, 'Available End Time', '08:00'),
        "require_schema_match": get_value(dict, 'Requires Schema Match', 'True', mapper=string_to_bool),
        "schedule_interval": get_value(dict, 'Schedule', '1 7 * * * '),
        "delta_days": get_value(dict, 'Delta Days', 'DAY_BEFORE', lookup=DeltaDays),
        "ftp_file_wildcard": get_value(dict, 'File Naming Pattern', None),
        "ftp_file_prefix": get_value(dict, 'FTP File Prefix', ftp_file_prefix(namespace)),
        "namespace": namespace
    })

# Review suggestions:
# - Use dict.get() for safer default handling when keys are missing.
# - Consider separating the construction of the config dictionary from the return statement for clarity.
# - Validate that the 'Namespace' and 'Airflow DAG' keys exist before accessing them to avoid KeyError.


# In[17]:


def config_from_dict(dictionary):
    """
    Given a dict representing a row from a namespaces csv file,
    returns a DAG configuration as a pair whose first element is the
    DAG name and whose second element is a dict describing the DAG's properties.
    """
    namespace = dictionary.get('Namespace')
    if not namespace:  # Check for missing namespace
        raise KeyError('Namespace is required')

    return (dictionary.get('Airflow DAG', 'Default DAG'), {
        "earliest_available_delta_days": 0,
        "lif_encoding": 'json',
        "earliest_available_time": get_value(dictionary, 'Available Start Time', '07:00'),
        "latest_available_time": get_value(dictionary, 'Available End Time', '08:00'),
        "require_schema_match": get_value(dictionary, 'Requires Schema Match', 'True', mapper=string_to_bool),
        "schedule_interval": get_value(dictionary, 'Schedule', '1 7 * * * '),
        "delta_days": get_value(dictionary, 'Delta Days', 'DAY_BEFORE'),
        "ftp_file_wildcard": get_value(dictionary, 'File Naming Pattern', None),
        "ftp_file_prefix": ftp_file_prefix(namespace),
        "namespace": namespace
    })


# ---
