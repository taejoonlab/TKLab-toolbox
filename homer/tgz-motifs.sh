#!/bin/bash
for DIR in $(ls -d motifs.*)
do
  TGZ=$DIR".tgz"

  if [ -e $TGZ ]; then
    echo "Skip $DIR"
  else
    echo "Make $TGZ"
    tar cvzpf $TGZ $DIR
  fi
done
