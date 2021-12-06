# Introduction to DataJoint

DataJoint is a workflow management system that integrates a relational database with computational data pipelines that are programmed and accessed directly using Matlab or Python. To find out more about DataJoint please visit their website [https://datajoint.org/](https://datajoint.org/). The IBL has collaborated with DataJoint to develop the IBL-pipeline, a set of tables organised in a structured manner that contain most experimental data and metadata collected within the IBL. Any new data generated in the collaboration is ingested into the IBL-pipeline on a daily basis, and so this framework can be used to access the latest data collected within the IBL.

There are several ways in which *internal* IBL users can use DataJoint to interact with the data stored in the IBL-pipeline.

1.  **IBL Navigator website [https://djcompute.internationalbrainlab.org/](https://djcompute.internationalbrainlab.org/)**

    DataJoint provides a website that displays behavioural and electrophysiological plots generated from data contained within the [IBL-pipeline](https://github.com/int-brain-lab/IBL-pipeline). New plots are generated on a daily basis so that users can view the website to get an overview of the latest behavioural and ephys data available.

2.  **Jupyter Notebooks website [https://jupyter.internationalbrainlab.org/](https://jupyter.internationalbrainlab.org/)**

    DataJoint hosts a JupyterHub server with access to the IBL-pipeline. This platform can be used to programatically explore and perform analysis on data stored within the IBL-pipeline without requiring a local install of dependant packages. To use the platform you will need to register your github account as well as have access to your [DataJoint login credentials](dj_credentials). To get started using the IBL-pipeline please proceed to the [DataJoint basics tutorial](../notebooks/dj_basics/dj_basics.ipynb).

3.  **Accessing the DataJoint database on your local machine**

    The most flexible way to use DataJoint with IBL data is to install the [IBL-pipeline](https://github.com/int-brain-lab/IBL-pipeline) package onto your local computer. This package is automatically installed as part of the [IBL unified environment](https://github.com/int-brain-lab/iblenv), and if you've followed the installation instructions you are ready to start using DataJoint in this way. The only thing you will need to do is to set up some local credentials. The [instructions on the next page](dj_credentials) will guide you through how to set these up.

For *external* users looking to use DataJoint to access the public IBL dataset please proceed directly to: [Accessing public IBL data with DataJoint](dj_public).

## Contact info

- Need credentials to access the data? Email: <info@internationalbrainlab.org>
- Issues with the data? Post an issue here: <https://github.com/int-brain-lab/iblenv/issues>
- General questions about the paper _The International Brain Laboratory et al. 2020_? Email: <info+behavior@internationalbrainlab.org>
