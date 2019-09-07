# install xvfb for running ete3 without X windows
sudo apt update
sudo apt install xvfb

# install libopenblas for Slr
sudo apt install libopenblas-dev

# Install ete3 via conda
conda install -c etetoolkit ete3 ete_toolchain

# Check ete3 build
ete3 build check

# If any program is failed, check ~/miniconda3/bin/ete3_apps/bin/
# i.e. 
# $ ~/miniconda3/bin/ete3_apps/bin/Slr
# ~/miniconda3/bin/ete3_apps/bin/Slr: error while loading shared libraries: libopenblas.so.0: cannot open shared object file: No such file or directory


