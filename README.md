# iblenv
Unified environment and Issue tracker for all IBL github repositories.

## Unified environment instructions
In order to create the unified environment for using IBL repositories, first download and install [Anaconda]https://www.anaconda.com/distribution/#download-section) and [git](https://git-scm.com/downloads), and follow their installer instructions to add each to the system path. Also, ensure Anaconda is installed to your home directory. The below instructions will tell you how to set up and activate the unified conda environment (`iblenv`) and properly install the 'ibllib', 'iblapps', 'analysis', and 'IBL-pipeline' repositories within this environment.

There are two options for setting up the environment:

### Option 1: Run installation setup files with a single command

First, download the [setup files](https://drive.google.com/open?id=1YtD6v9lO07fzq-xnJTwiKKIZIFt4BMLX), and extract and copy these three files to the directory in which you want to install the IBL repositories (e.g. create a folder named `int-brain-lab` and copy these files there).

Next, ensure that Anaconda has been installed to your home directory and `git` and `conda` are on your system path (to check, try running `git --version` and `conda --version` in your system terminal). If either `git` or `conda` are not on your system path and you want to add them, click [add conda to system path](https://www.google.com/search?q=how+to+add+conda+to+system+path) or [add git to system path](https://www.google.com/search?q=how+to+add+git+to+system+path) for instructions on how to do so. If either `git` or `conda` are not on your system path and you *don't* want to add them, proceed with [Option 2](#option-2-run-all-the-setup-commands-manually).

Then, ensure that the only active applications on your computer are your system terminal and optionally a text editor. Close *all* other applications (this includes the web browser you may be reading this on) before continuing. If you leave other applications open, then worse than failing and aborting the install process, `conda` may create and install some packages in the environment but fail silently, which can cause future issues. Feel free to copy and paste these instructions to your text editor before closing all other applications.

If you have adhered to the above directions, then all you have to do is, within your system terminal, navigate to the directory in which you copied over the setup files and run the command `sudo sh iblrepos_setup.sh` if you are using Mac/Linux, or `.\iblrepos_setup.cmd` if you are using Windows (you may need to launch the Windows terminal as an administrator). That's it, you're done!

### Option 2: Run all the setup commands manually

Ensure that the only active applications on your computer are your system terminal and optionally a text editor. Close *all* other applications (this includes the web browser you may be reading this on) before continuing. If you leave other applications open, then worse than failing and aborting the install process, `conda` may create and install some packages in the environment but fail silently, which can cause future issues. Feel free to copy and paste these instructions to your text editor before closing all other applications.

In your git terminal, navigate to the directory in which you want to install the IBL repositories (e.g. create a folder named `int-brain-lab`), and run the following `git` commands:

```
git clone https://github.com/int-brain-lab/ibllib.git --branch develop
git clone https://github.com/int-brain-lab/iblapps.git --branch develop
git clone https://github.com/int-brain-lab/analysis.git
git clone https://github.com/int-brain-lab/IBL-pipeline.git
git clone https://github.com/int-brain-lab/iblenv.git
```

Then in your conda terminal, navigate to this same directory, and run the following `conda` commands:

```
conda env create -f ./iblenv/iblenv.yaml python==3.8
conda activate iblenv
conda-develop ./ibllib
conda-develop ./iblapps
conda-develop ./analysis
conda-develop ./IBL-pipeline
```

Notes:
- Whenever you run IBL code in Python you should activate the `iblenv` environment, and ensure the IBL repository paths are *not* added directly to your python path (e.g. don't start a python console from within any of the directories that contain an IBL repository).
- While these IBL repositories are under active development, remember to git pull regularly.
- If you want to closely follow feature development across different repositories, you can simply checkout and pull the relevant branches within those repositories.
- If you want to launch GUIs that rely on pyqt (e.g. the IBL data exploration gui or phy) from IPython, you should first run the IPython magic command `%gui qt`.
