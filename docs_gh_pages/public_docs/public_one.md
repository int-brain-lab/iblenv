# Accessing public data with ONE

To get started you will first need to install python. We recommend installing through 
[Anaconda](https://www.anaconda.com/products/individual#download-section). Once python is installed
open a conda terminal and type the following to 1) Create a new conda environment 2) Install ibllib

```python
conda create --name ibllib python=3.8 
conda activate ibllib
pip install ibllib
```

Once installed activate your conda environment and open a python or ipython terminal by typing
```
conda activate ibllib
ipython
```

In the python terminal type:

```python
from oneibl.one import OneAlyx
OneAlyx.setup()
```

You will be prompted to enter information in the following order. 
 
  
```python
ALYX_LOGIN:             # Input 'iblpublic'
ALYX_URL:               # Input 'https://public.alyx.internationalbrainlab.org'
CACHE_DIR:              # Optionally change or keep default
HTTP_DATA_SERVER:       # Keep default by pressing enter
HTTP_DATA_SERVER_LOGIN: # Keep default by pressing enter
Alyx password:          # 'NeuroPhysTest'
FlatIron HTTP password:	# Keep default by pressing enter
```

To check that everything has been set up properly type the following
```python
from oneibl.one import ONE
one = ONE()
```

If you successfully entered the credentials above you should see a message in the terminal saying,
```python
Connected to https://public.alyx.internationalbrainlab.org as iblpublic
```

To start exploring the publically available available please proceed to 
[Getting started with ONE](../notebooks/public_one/public_one.ipynb)