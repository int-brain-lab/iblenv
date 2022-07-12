[Documentation here ! ](https://int-brain-lab.github.io/iblenv/)

# IBLENV installation guide
Unified environment and issue tracker for IBL github repositories.

## Update environment

In a terminal, navigate to your working directory, the one in you cloned the `iblenv` and `iblapps` repositories previously
(typically something like `int-brain-lab`) and type: 

```commandline
conda activate iblenv
cd iblapps
git pull
cd ..
cd iblenv
pip install --requirement requirements.txt --upgrade
```

## Install from scratch
In order to create the unified environment for using IBL repositories, first download and install 
[Anaconda](https://www.anaconda.com/distribution/#download-section) and [git](https://git-scm.com/downloads), and follow their 
installer instructions to add each to the system path. Also, please ensure Anaconda is installed to your home directory. The 
below instructions will tell you how to set up and activate the unified conda environment (`iblenv`) and properly install 
multiple repositories within this environment.

Ensure that the only active applications on your computer are your system terminal and optionally a text editor. Close *all* 
other applications (this includes the web browser you may be reading this on) before continuing. If you leave other applications 
open, then worse than failing and aborting the installation process, `conda` may create and install some packages in the 
environment but fail silently, which can cause future issues. Feel free to copy and paste these instructions to your text editor 
before closing all other applications.

In your git terminal, navigate to the directory in which you want to install the IBL repositories (e.g. create a folder named 
something like `int-brain-lab`), and run the following commands:

```commandline
conda create --name iblenv python=3.9 --yes
conda activate iblenv
git clone https://github.com/int-brain-lab/iblapps
pip install --editable iblapps
git clone https://github.com/int-brain-lab/iblenv
cd iblenv
pip install --requirement requirements.txt
```

## Removing an old installation
The following command will completely remove an anaconda environment and all of its packages: `conda remove --name iblenv --all`

## Notes:
- Whenever you run IBL code in Python you should activate the `iblenv` environment, i.e. `conda activate iblenv`
- If you want to launch GUIs that rely on pyqt (e.g. the IBL data exploration gui or phy) from IPython, you should first run the 
IPython magic command `%gui qt`.

All done! See notes from above on how exactly conda develop works, and how to make sure you're up to date on the latest IBL code versions.
