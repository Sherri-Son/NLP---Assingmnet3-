import json
import collections
import argparse
import random
import numpy as np
import requests
import re

def your_netid():
    YOUR_NET_ID = 'cs8607'      # <-- put your NetID here
    return YOUR_NET_ID

def your_hf_token():
    YOUR_HF_TOKEN = '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'  # <-- put your Hugging Face token here (hf_...)
    return YOUR_HF_TOKEN


# for adding small numbers (1-6 digits) and large numbers (7 digits), write prompt prefix and prompt suffix separately.
def your_prompt():
    """Returns a prompt to add to "[PREFIX]a+b[SUFFIX]", where a,b are integers
    Returns:
        A string.
    Example: a=1111, b=2222, prefix='Input: ', suffix='\nOutput: '
    """
    prefix = (
        "Add the two 7-digit numbers. Give only the exact sum.\n"
        "4827361+5938274=10765635\n"
        "1092837+4655190=5748027\n"
        "9876543+1234567=11111110\n"
        "4186027+4098086=8284113\n"
        "8589669+8812311=17401980\n"
        "2468013+3579246=6047259\n"
        "8580488+9520162=18100650\n"
        "3051729+6948271=10000000\n"
    )
    suffix = '='

    return prefix, suffix


def your_config():
    """Returns a config for prompting api
    Returns:
        For both short/medium, long: a dictionary with fixed string keys.
    Note:
        do not add additional keys.
        The autograder will check whether additional keys are present.
        Adding additional keys will result in error.
    """
    config = {
        'max_tokens': 50,          
        'temperature': 0.1,        
        'top_k': 1,               
        'top_p': 0.9,              
        'repetition_penalty': 1,  
        'stop': ['\n']}            

    return config


def your_pre_processing(s):
    return s


def your_post_processing(output_string):
    """Returns the post processing function to extract the answer for addition
    Returns:
        For: the function returns extracted result
    Note:
        do not attempt to "hack" the post processing function
        by extracting the two given numbers and adding them.
        the autograder will check whether the post processing function contains arithmetic additiona and the graders might also manually check.
    """

    cleaned = output_string.replace(",", "")
    match = re.search(r"\d{1,}", cleaned)
    if match is None:
        return 0
    return int(match.group(0))