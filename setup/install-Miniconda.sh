#!/bin/bash

if [ -x "$(command -v conda)" ]; then
  echo "conda is avilalbe. Skip installation."
else
  echo "Install the latest Miniconda3"
  MINICONDA_INSTALLER="Miniconda3-latest-Linux-x86_64.sh"
  wget https://repo.continuum.io/miniconda/$MINICONDA_INSTALLER
  chmod 755 $MINICONDA_INSTALLER
  ./$MINICONDA_INSTALLER
  rm $MINICONDA_INSTALLER
fi
