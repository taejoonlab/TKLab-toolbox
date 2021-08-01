#!/bin/bash
for DIR in $(ls -d tags.*)
do
  TGZ=$DIR".tgz"

  if [ -e $TGZ ]; then
    echo "Skip $DIR"
  else
    echo "Make $TGZ"
    tar cvzpf $TGZ $DIR
  fi
done
