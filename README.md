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

After installation or updates complete, open a new terminal and rerun the version commands listed above to verify they have 
been installed properly. Once verification has been completed, perform the following steps:
* create and change to the directory that you will want to house the IBL repositories, something like 
`/home/username/Documents/int-brain-lab` or `C:\Users\username\Documents\int-brain-lab` works well
* run the commands:
  * `git clone https://github.com/int-brain-lab/iblenv.git`
  * `cd iblenv`
  * `python install.py`

The installation script simply
* verifies all the dependencies have been installed
* creates the iblenv anaconda environment
* uses pip to install of the packages found in the requirements.txt file

You should now be able to start writing and running python scripts to analyze and visualize data. 

TODO: Include a few example scripts utilizing iblapps and iblutil

## Updating iblenv conda environment
Run the commands:
* `conda activate iblenv` (if you are not already in the iblenv environment)
* `pip freeze > my_requirements.txt`
* `pip install -r my_requirements.txt --upgrade`

This series of commands simply activates the iblenv anaconda environment, creates a snapshot of the package environment, and 
finally instructs pip to upgrade all the packages.  

TODO: Update documentation below

## Advanced usage
More advanced users may always look to clone additional repositories. Other repositories of interest:
* analysis https://github.com/int-brain-lab/analysis
* IBL-pipeline https://github.com/int-brain-lab/IBL-pipeline
* phylib https://github.com/cortex-lab/phylib
* phy https://github.com/cortex-lab/phy

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

## Notes:
- Whenever you run IBL code in Python you should activate the `iblenv` environment
- While these IBL repositories are under active development, remember to git pull regularly.
- If you want to closely follow feature development across different repositories, you can simply checkout and pull the relevant branches within those repositories.
- If you want to launch GUIs that rely on pyqt (e.g. the IBL data exploration gui or phy) from IPython, you should first run the IPython magic command `%gui qt`.

## More:
- **What does `conda develop` really do?** Running conda develop creates a `.pth` file in your conda environment, with the 
repository you give as input arg when calling conda-develop. When you run a python script (with iblenv activated) and import 
ibllib), conda will first see if you installed this as a package (e.g. through pip install ibllib). Warning: do not use pip 
install or conda install for any of the repos above; this will make conda use those, instead of the local ones that you've cloned.

If conda can't find the package, it will look in the .pth file that was created by conda develop. It will then use these files 
on your disk (that you can keep up-to-date by simply pulling) to import the latest version of the code.
