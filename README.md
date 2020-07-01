# iblenv
Unified environment and Issue tracker for all IBL github repositories.

## Unified environment instructions
*Note*: if you already have a conda environment named 'iblenv' (you can check with the command `conda env list`), then remove this environment with the command `conda env remove -n iblenv`.

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

```
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
