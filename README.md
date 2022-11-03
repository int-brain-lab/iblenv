# IBLENV installation guide
Unified environment and issue tracker for IBL github repositories.

## Update environment

In a terminal, navigate to your working directory, the one in you cloned the `iblenv` and `iblapps` repositories previously
(typically something like `int-brain-lab`). Run the following commands in your terminal: 

```bash
conda activate iblenv
cd iblapps
git pull
cd ..
cd iblenv
pip install --requirement requirements.txt --upgrade
```

If any errors are encountered, it is recommended to follow the "Removing an old installation" instructions and then the "Install 
from scratch" instructions. 

## Install from scratch
In order to create the unified environment for using IBL repositories, first download and install 
[Anaconda](https://www.anaconda.com/distribution/#download-section) and [git](https://git-scm.com/downloads), and follow their 
installer instructions to add each to the system path. Also, please ensure Anaconda is installed to your home directory. The 
below instructions will tell you how to set up and activate the unified conda environment (`iblenv`) and properly install 
multiple repositories within this environment.

In your git terminal, navigate to the directory in which you want to install the IBL repositories (e.g. create a folder named 
something like `int-brain-lab` and work from within it). Then run the following commands:

```bash
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
[Additional documentation here for working with iblenv](https://int-brain-lab.github.io/iblenv/)

## Troubleshooting:

### Spyder
If using Anaconda's Spyder IDE, please take note. When installing Spyder in a virtual environment, like iblenv, conda 
will add many packages to that virtual environment. In the case of iblenv, some packages installed by spyder are in direct 
conflict with the pip installed packages. This will create an inconsistent and unstable environment, especially when attempting 
to perform any sort of update on those packages. For more information about how to work with pip within conda, please read the 
following [article](https://www.anaconda.com/blog/using-pip-in-a-conda-environment).

It is not recommended to use the Spyder IDE in conjunction with iblenv. Please seek alternatives, like 
[PyCharm](https://www.jetbrains.com/pycharm/) or [Visual Studio Code](https://code.visualstudio.com/).