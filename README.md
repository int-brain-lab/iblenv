[Additional documentation can be found here.](https://int-brain-lab.github.io/iblenv/)

# IBLENV
The unified environment and issue tracker for all IBL github repositories.

## Installing iblenv conda environment from scratch
In order to create the unified Anaconda environment for using IBL repositories you will need to have Anaconda and git installed. 
To check that these applications are installed, please open a terminal (command prompt) and perform the following commands:
* `git --version` # output should be something like "git version 2.34.1"
* `conda --version` # output should be something like "conda 4.12.0"


If the commands are unrecognized or the version is far below the ones listed above, please download and install/update:
* [git](https://git-scm.com/downloads)
* [Anaconda](https://www.anaconda.com/distribution/#download-section) - ensure Anaconda is installed to your home directory (not 
  system-wide)

After installation or updates complete, open a new terminal and rerun the version commands listed above to verify they have 
been installed properly. Once complete, perform the following steps:
* create and change to the directory that you will want to house the IBL repositories, something like 
`/home/username/Documents/int-brain-lab` or `C:\Users\username\Documents\int-brain-lab` works well
* run the commands:
  * `git clone https://github.com/int-brain-lab/iblenv.git`
  * `cd iblenv`
  * `python install.py`

The installation script simply
* verifies all the dependencies have been installed
* creates the iblenv anaconda environment if it does not exist already
* uses pip to install of the packages found in the requirements.txt file

You should now be able to start writing and running python scripts to analyze and visualize data. 

**TODO: Include a few example scripts utilizing iblapps and iblutil**

### Notes for most users:
* Whenever you run IBL code in Python you should activate the `iblenv` environment
* If you want to launch GUIs that rely on pyqt (e.g. the IBL data exploration gui or phy) from IPython, you should first run the 
IPython magic command `%gui qt` **TODO: verify this step is still required**

## Updating iblenv conda environment
To get the latest bug fixes and features, run the following commands:
* `conda activate iblenv` (if it is not already active)
* `pip freeze > my_requirements.txt`
* `pip install -r my_requirements.txt --upgrade`

This series of commands simply activates the iblenv anaconda environment, creates a 'snapshot' of the package environment, and 
finally instructs pip to upgrade all the packages from that snapshot. This has the added benefit of quickly being able to revert
to a previous state.

## Advanced usage
More advanced users may always look to `git clone` additional repositories instead of retrieving packages from 
pip/requirements.txt. If the repo of interest is in the `requirements.txt` file, you must first remove it prior to running the 
install script or remove the package from the environment manually. Other repositories of interest:
* iblapps - https://github.com/int-brain-lab/iblapps
* iblutil - https://github.com/int-brain-lab/iblutil
* analysis - https://github.com/int-brain-lab/analysis
* IBL-pipeline - https://github.com/int-brain-lab/IBL-pipeline
* phylib - https://github.com/cortex-lab/phylib
* phy - https://github.com/cortex-lab/phy

If you plan on making modifications to the repos, you may choose to install the repositories in develop mode. From the parent 
directory 'int-brain-lab', you can run the following commands `conda develop ./repo-name`

### Information on the `conda develop` command:
**What does `conda develop` really do?** Running conda develop creates a `.pth` file in your conda environment, with the 
repository you give as input arg when calling conda-develop. When you run a python script (with iblenv activated) and import 
ibllib), conda will first see if you installed this as a package (e.g. through `pip install ibllib`). If conda can't find the 
package, it will look in the `.pth` file that was created by conda develop. It will then use these files on your disk (that you 
can keep up-to-date by fetching/pulling) to import the latest version of the code.

### Notes for advanced users:
* These IBL repositories are under active development, remember to `git fetch`/`git pull` regularly to avoid insurmountable merge 
conflicts
* If you want to closely follow feature development across different repositories, you can checkout and pull the relevant
branch(es) within those repositories
