[Additional documentation can be found here.](https://int-brain-lab.github.io/iblenv/)

# IBLENV
The unified environment and issue tracker for all IBL github repositories.


## Installing iblenv conda environment from scratch
In order to create the unified Anaconda environment for using IBL repositories you will need to have Anaconda and git installed. 
To check that these applications are installed, please open a terminal (command prompt) and perform the following commands:

```
git --version    # output should be something like "git version 2.34.1"
conda --version  # output should be something like "conda 4.12.0"
```

If the commands are unrecognized or the version is far below the ones listed above, please download and install/update:
* [git](https://git-scm.com/downloads)
* [Anaconda](https://www.anaconda.com/distribution/#download-section) - ensure Anaconda is installed to your home directory (not 
  system-wide)

After updates or installation completes, open a new terminal and rerun the version commands listed above to verify they have 
been installed properly. Once verification has been completed, perform the following steps:
* create and change to the directory that you will want to house the IBL repositories, something like 
`/home/username/Documents/int-brain-lab` or `C:\Users\username\Documents\int-brain-lab` works well
* run the commands:
  * `git clone https://github.com/int-brain-lab/iblenv.git`
  * `cd iblenv`
  * `python install.py`

This will clone the requisite repositories...
TODO: Complete installation instructions


## Updating iblenv conda environment
run the commands:
* `python update.py`

TODO: Complete update instructions



## Advanced usage



---
Update documentation below
---

In your git terminal, navigate to the directory in which you want to install the IBL repositories (e.g. create a folder named `int-brain-lab`), and run the following `git` commands:

```
git clone https://github.com/int-brain-lab/ibllib.git --branch develop ibllib-repo
git clone https://github.com/int-brain-lab/iblapps.git  --branch develop
git clone https://github.com/int-brain-lab/analysis.git
git clone https://github.com/int-brain-lab/IBL-pipeline.git
git clone https://github.com/int-brain-lab/iblenv.git
git clone https://github.com/cortex-lab/phylib
git clone https://github.com/cortex-lab/phy
```

Then in your conda terminal, navigate to this same directory, and run the following `conda` commands:


Make sure that if iblenv was previously installed, it is cleaned up:
```
conda env list
conda env remove -n iblenv
```

Install all the repositories in develop mode (the first command can take some time to complete):
```
conda config --set channel_priority false
conda env create -f ./iblenv/iblenv.yaml
conda activate iblenv
conda develop ./ibllib-repo
conda develop ./iblapps
conda develop ./analysis
conda develop ./IBL-pipeline
conda develop ./phy
conda develop ./phylib
```

NB: On Mac OS, the git and conda terminals are one and the same, the terminal.

## Notes:
- Whenever you run IBL code in Python you should activate the `iblenv` environment
- While these IBL repositories are under active development, remember to git pull regularly.
- If you want to closely follow feature development across different repositories, you can simply checkout and pull the relevant branches within those repositories.
- If you want to launch GUIs that rely on pyqt (e.g. the IBL data exploration gui or phy) from IPython, you should first run the IPython magic command `%gui qt`.

## More:
- **What does `conda develop` really do?** Running conda develop creates a `.pth` file in your conda environment, with the repository you give as input arg when calling conda-develop. When you run a python script (with iblenv activated) and import ibllib), conda will first see if you installed this as a package (e.g. through pip install ibllib). Warning: do not use pip install or conda install for any of the repos above; this will make conda use those, instead of the local ones that you've cloned.

If conda can't find the package, it will look in the .pth file that was created by conda develop. It will then use these files on your disk (that you can keep up-to-date by simply pulling) to import the latest version of the code.

## Update environment

In a terminal, navigate to the directory in which you cloned iblenv (typically `int-brain-lab/iblenv`) and type: 

` conda env update --file iblenv.yaml --prune`

Note: It can take longer to update than to install from scratch -- do not hesitate to follow the steps below if taking too much time!

If you start from scratch, do:

` conda clean --all`

Then repeat all steps of the install from scratch section, but starting **after** git clone.

If still slow, use the mamba installation approach.

