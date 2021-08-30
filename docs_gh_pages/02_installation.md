# Installation

## To access the public datasets
If you are solely interested in accessing the publicly available datasets,
please visit this [section](../../08_public.html) for instructions.

You do not have to install all the libraries mentioned below.

# To access the private datasets and/or use IBL visualisation tools
### Recap on the main IBL librairies
There are currently a number of useful libraries being developed within the IBL 
[(https://github.com/int-brain-lab)](https://github.com/int-brain-lab). Those integral to the IBL data architecture 
include,

1. [**ibllib**](https://github.com/int-brain-lab/ibllib)

    The library used to implement the IBL data architecture pipeline. It currently contains two main modules
    * ibllib - general purpose library containing I/O, signal processing and IBL data pipelines utilities.
    * brainbox - neuroscience analysis oriented library
    
2. [**ONE**](https://github.com/int-brain-lab/ONE)

   The library used to search for and load IBL data

3.  [**IBL-pipeline**](https://github.com/int-brain-lab/IBL-pipeline)

    The library used to implement the IBL Datajoint pipeline

### Unified Environment
To facilitate the use of `ibllib` and `IBL-pipeline`, we have compiled all the dependencies into a unified python 
environment `iblenv`. In addition to these two libraries, this environment is also compatible with other visualisation 
tools and analysis pipelines being developed as part of the IBL. 

Internal users are kindly requested to install this unified environment.
External users are encouraged to do so if wanting to use visualisation tools alongside datasets.

To install this python environment, please follow 
[these](https://github.com/int-brain-lab/iblenv) installation instructions.

