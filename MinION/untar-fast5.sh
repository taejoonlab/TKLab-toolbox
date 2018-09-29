#!/bin/bash
for TGZ in $(ls *tgz)
do
  tar xvzf $TGZ
done
