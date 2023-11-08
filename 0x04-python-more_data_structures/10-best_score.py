#!/usr/bin/python3
#10-best_score.py

def best_score(my_dict):
    return max(my_dict, key=my_dict.get) if my_dict else None

