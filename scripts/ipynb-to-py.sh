#!/bin/bash
IPYNB=$1
jupyter nbconvert --to script $1
