[Documentation here ! ](https://int-brain-lab.github.io/iblenv/)

# IBLENV installation guide
Unified environment and Issue tracker for all IBL github repositories.

## Update environment

In a terminal, navigate to the directory in which you cloned iblenv (typically `int-brain-lab/iblenv`) and type: 

` conda env update --file iblenv.yaml --prune`

Note: It can take longer to update than to install from scratch -- do not hesitate to follow the steps below if taking too much time!
I you start from scratch, do:
` conda clean --all`
Then repeat all steps of the install from scratch section, but starting **after** git clone.
If still slow, use the mamba installation approach.

## Install from scratch
In order to create the unified environment for using IBL repositories, first download and install [Anaconda](https://www.anaconda.com/distribution/#download-section) and [git](https://git-scm.com/downloads), and follow their installer instructions to add each to the system path. Also, ensure Anaconda is installed to your home directory. The below instructions will tell you how to set up and activate the unified conda environment (`iblenv`) and properly install the 'ibllib', 'iblapps', 'analysis', and 'IBL-pipeline' repositories within this environment.

Ensure that the only active applications on your computer are your system terminal and optionally a text editor. Close *all* other applications (this includes the web browser you may be reading this on) before continuing. If you leave other applications open, then worse than failing and aborting the install process, `conda` may create and install some packages in the environment but fail silently, which can cause future issues. Feel free to copy and paste these instructions to your text editor before closing all other applications.

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

# Mambaforge IBLENV installation

[Mamba](https://github.com/mamba-org/mamba) is a drop-in conda alternative which provides much faster solving of environments thanks to a backend written mostly in C++ which relies on `libsolv`, a faster dependency solver. It can be installed via conda, and must be 

[Mambaforge](https://github.com/conda-forge/miniforge#miniforge) is a complete conda replacement which couples mamba with complete reliance on the open-source and community-run conda-forge channel. The "defaults" channel which is run by Continuum analytics is not enabled in this distribution.

This option has the advantages of being both:
1. Faster than conda
2. Supporting more hardware architectures (OSX Users with apple silicon can rejoice! Apple ARM M1 is supported for many packages)

It also means the IBL environment doesn't fall into dependency resolution hell when trying to install pytorch on top of the normal iblenv spec.

## Update environment

As in the conda example, change to the iblenv repo directory on your machine (make sure it's up to date). Then run:

` mamba env update --file iblenv.yaml --prune`

The only change from above is the substition of mamba for conda

## Installing from scratch

First ensure that you have git installed. Then, follow the instructions for [downloading and installing mambaforge](https://github.com/conda-forge/miniforge#mambaforge) on your platform.

Once mambaforge is installed, run the following commands to download all IBL repositories:

```
git clone https://github.com/int-brain-lab/ibllib.git --branch develop ibllib-repo
git clone https://github.com/int-brain-lab/iblapps.git  --branch develop
git clone https://github.com/int-brain-lab/analysis.git
git clone https://github.com/int-brain-lab/IBL-pipeline.git
git clone https://github.com/int-brain-lab/iblenv.git
git clone https://github.com/cortex-lab/phylib
git clone https://github.com/cortex-lab/phy
mamba install conda-build
```

This ensures you have the necessary repos, and the conda-build package.

Now that you have a complete copy of all IBL environment repos, change directory into the iblenv directiory and run the following:

` mamba env create -f iblenv_mamba.yaml `

Then run the usual suite of conda-develop commands to link your python to the cloned version of the repos:

```
conda activate iblenv
conda develop ./ibllib-repo
conda develop ./iblapps
conda develop ./analysis
conda develop ./IBL-pipeline
conda develop ./phy
conda develop ./phylib
```

All done! See notes from above on how exactly conda develop works, and how to make sure you're up to date on the latest IBL code versions.
