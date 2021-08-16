# Accessing public data with ONE

The public data includes both compressed raw ephys data and preprocessed data, as well as behaviour
and video data.  A full list of dataset types and their details can be found 
[here](https://docs.google.com/document/d/1OqIqqakPakHXRAwceYLwFY9gOrm8_P62XIfCTnHwstg/edit).

To get started you will first need to install python. We recommend installing through 
[Anaconda](https://www.anaconda.com/products/individual#download-section). Once python is installed
open a conda terminal and type the following to create a new conda environment. 
When prompted enter yes.
```python
conda create --name ibllib python=3.8 
```

We will then activate this new environment and install ibllib
```python
conda activate ibllib
pip install ibllib
```

Once installed open a python or ipython terminal by typing
```
ipython
```

In the python terminal type:

```python
from oneibl.one import ONE
one = ONE(silent=True)
```

If everything has been installed correctly you should see a message in the terminal saying,
```python
Connected to https://openalyx.internationalbrainlab.org as intbrainlab
```

To start exploring the publically available available please proceed to 
[Getting started with ONE](../notebooks/public_one/public_one.ipynb)
