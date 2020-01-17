#!/bin/bash

# https://community.nanoporetech.com/protocols/Guppy-protocol/v/gpb_2003_v1_revo_14dec2018/linux-guppy

sudo apt-get update
sudo apt-get install wget lsb-release
export PLATFORM=$(lsb_release -cs)
wget -O- https://mirror.oxfordnanoportal.com/apt/ont-repo.pub | sudo apt-key add -
echo "deb http://mirror.oxfordnanoportal.com/apt ${PLATFORM}-stable non-free" | sudo tee /etc/apt/sources.list.d/nanoporetech.sources.list
sudo apt-get update

sudo apt-get install ont-guppy
