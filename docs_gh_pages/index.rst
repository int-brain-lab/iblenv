.. one_ibl documentation master file, created by
   sphinx-quickstart on Fri Jul 20 17:20:00 2018.

Welcome to IBL code library documentation!
##########################################

IBL data structure
*************************
.. image:: ./_static/IBL_data.png
   :alt: Alyx data structure

In the IBL, data acquired in laboratories spread across countries needs to be centralized into a
common store, accessible from anywhere in the world, at all times.
This challenge is met by the IBL data architecture, documented briefly below; a thorough description
can be found in our `preprint <https://www.biorxiv.org/content/10.1101/827873v3>`_.

The central store has two components:

* A **Bulk Data Store** that stores **large raw data files** (e.g. raw electrophysiology and video data) as well as **pre-processed data** (e.g. results of spike sorting or video segmentation). This database is accessible through HTTP, FTP and Globus. This is known informally as the "Flatiron server" as our original data server was generously hosted by the `Flatiron Institute <https://www.simonsfoundation.org/flatiron/>`_.
* A **Relational Database** that stores **metadata** (e.g. information on each experiment and experimental subject) in a structured manner, together with links to the bulk data files. This database is known as `Alyx <https://github.com/cortex-lab/alyx>`_, for reasons no-one can remember. Alyx contains a web-based front-end to allow users to perform colony management and enter metadata during experiments; documentation on this front end is `here <https://docs.google.com/document/d/1cx3XLZiZRh3lUzhhR_p65BggEqTKpXHUDkUDagvf9Kc/edit?usp=sharing>`_. Information on how to connect to Alyx programmatically is `here <https://alyx.readthedocs.io/en/latest/>`_.

Tools to access the data
*************************
There are two main ways to access the data:

* `ONE <https://int-brain-lab.github.io/ONE/>`_: an API that connects to the central store, allowing users to search and load data of interest from specific experiments.
* `Datajoint <https://datajoint.io>`_: a framework to perform automated pipelined analyses on a subset of lightweight data such as behavioral choices and spike times, that allows rapid integration of data from multiple experiments and users.

The full IBL data will be publically released when we have completed collection, preprocessing, curation, and quality control. In the meantime, a subset of curated data are publically available.

Software to analyze IBL data
****************************
IBL has released a suite of tools to process and visualize our data.

* `Brainbox <https://github.com/int-brain-lab/ibllib>`_: A library of analysis functions that can be used on IBL data or other neurophysiology recordings.
* `IBL Viewer <https://github.com/int-brain-lab/iblviewer/blob/main/README.md>`_: A simple and fast interactive visualization tool based on VTK that uses GPU accelerated volume and surface rendering. From electrophysiological data to neuronal connectivity, this tool allows simple and effective 3D visualization for many use-cases like multi-slicing and time series (even on volumes), and can be embedded within Jupyter Lab/Notebook and Qt user interfaces.

.. attention::
   To get all the software, including ONE, brainbox and visualization tools, install the
   `Unified Environment <./02_installation.html>`_. This is recommended for IBL members.

.. toctree::
   :hidden:
   :caption: The Open Neurophysiology Environment
   :maxdepth: 1

   notebooks_external/one_quickstart
   Full documentation Website for ONE <https://int-brain-lab.github.io/ONE/>

.. toctree::
   :hidden:
   :caption: DataJoint
   :maxdepth: 1

   dj_docs/dj_introduction
   dj_docs/dj_public
   dj_docs/dj_credentials

.. toctree::
   :hidden:
   :caption: Public
   :maxdepth: 1

   public_docs/public_introduction

.. toctree::
   :hidden:
   :caption: Exploring IBL Data
   :maxdepth: 1

   loading_examples


.. toctree::
   :hidden:
   :caption: Miscellaneous
   :maxdepth: 1

   02_installation
   09_contribution

.. toctree::
   :hidden:
   :caption: Examples & Tutorials
   :maxdepth: 1

   06_examples
   notebooks/dj_intro/dj_intro
   notebooks/dj_basics/dj_basics
   notebooks_external/docs_wheel_moves

.. toctree::
   :hidden:
   :caption: API Reference
   :maxdepth: 1

   010_api_reference.rst
   genindex
