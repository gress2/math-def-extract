#!/bin/bash

find . -name "enwiki*.xml*" -exec python cull.py {} ";" 
