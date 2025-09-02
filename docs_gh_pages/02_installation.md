# Installation of IBL Unified Environment
To facilitate the use of `ibllib` and `IBL-pipeline`, we have compiled all the dependencies into a unified python 
environment `iblenv`. In addition to these two libraries, this environment is also compatible with other visualisation 
tools and analysis pipelines being developed as part of the IBL. 

To use IBL data you will need a python environment with python >= 3.10, although Python 3.13 is recommended. 
To create a new environment from scratch you can install either [uv/pip](https://docs.astral.sh/uv/) or [anaconda](https://www.anaconda.com/products/distribution#download-section) and follow the instructions below to create a new python environment (more information can also be found [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html))

Please follow the installation instructions below for your favourite package manager.

## UV / pip instructions

Run the following commands in your terminal: 

```bash
uv venv --python 3.13
```
Make sure to always activate this environment before installing or working with the IBL data
```bash
source .venv/bin/activate
```

Install required packages to access the data
```shell
uv pip install ONE-api
uv pip install ibllib
```

## Conda instructions

### Install

In your git terminal, navigate to the directory in which you want to install the IBL repositories (e.g. create a folder named 
something like `int-brain-lab` and work from within it). Then run the following commands:

```bash
conda update -n base -c defaults conda
conda create --name ibl python=3.13 --yes
conda activate ibl

pip install ONE-api
pip install ibllib
```

### Removing an old installation
The following command will completely remove an anaconda environment and all of its packages: `conda remove --name ibl --all`
