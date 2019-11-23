#!/bin/bash

# https://github.com/etal/cnvkit
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge

conda install cnvkit
