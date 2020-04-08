# iblenv
Unified environment and Issue tracker for all IBL

## Unified environment instructions
Make sure you close
Create or cd to a directory where you want to store all the source code:

```
mkdir iblcode
cd iblcode
```


``` 
git clone https://github.com/int-brain-lab/ibllib.git --branch develop
git clone https://github.com/int-brain-lab/iblapps.git --branch develop
git clone https://github.com/int-brain-lab/IBL-pipeline.git
git clone https://github.com/int-brain-lab/iblenv.git

conda env create --file ./iblenv/iblenv.yaml python=3.8
conda activate iblcode

conda develop ./ibllib/
conda develop ./IBL-pipeline
conda develop ./iblapps

```

Make sure you don't attempt to run code from this directory containing your sources !
```
cd ..
conda activate iblcode
ipython
%gui qt
```


Make sure you're comfortable switching branches if you want to follow closely features development.

```
git checkout develop
```
