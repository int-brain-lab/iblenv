# Publicly available IBL data

## Introduction to the IBL experiments
The aim of the International Brain Laboratory (IBL) is to understand the brain functions 
underlying decision making. Understanding these processes is a problem with a scale and complexity 
that far exceed what can be tackled by any single laboratory and that demands computational theory 
to be interwoven with experimental design and analysis in a manner not yet achieved. To overcome these 
challenges, we have created a virtual laboratory, unifying a group of 22 highly experienced neuroscience 
groups distributed across the world. 

Datasets are acquired in a dozen of laboratories performing experimental work (e.g. Churchland lab, Mainen lab, Zador lab).
In each of these laboratories, mice are first trained in the IBL decision-making task 
[following a standardized training pipeline](https://elifesciences.org/articles/63711). Briefly, the mice are fixed
in front of a screen, and have to turn a Lego wheel in order to position a visual stimulus appearing on one of the 
side of the screen towards its center. The complexity of the task increases as the contrast of the visual stimulus is lowered,
and the probability of the stimulus appearing on a given side varies.

Various sensors are used to monitor the animal's performance and condition (e.g. a rotary encoder attached to the Lego wheel,
camera(s) to view the mouse posture). Behavior data is acquired throughout the learning phase on "Training rigs" (see our
[article on behavioral training](https://elifesciences.org/articles/63711) for details).
Once a mouse has reached proficiency in the IBL task, it is moved to an "Ephys rig" where its brain activity is recorded from.
 
We aim to use different brain recording modalities, so as to have complimentary views on the brain activity. For example:
Neuropixels, Mesoscope, Fiberfluorophotometry, Widefield Imaging techniques all have their unique advantages over one another. 
Our most advanced project as of now is the one involving Neuropixels recordings.

### Neuropixels datasets
The data consists of neurophysiological and behavior measurements acquired in mice, using Neuropixels probes.
In a single recording session, up to two Neuropixels probes (labelled typically `probe00` or `probe01`)
are inserted in the mouse's brain. The location of these probes in the brain will vary from mouse to mouse, as the
aim of this IBL project is to tile the whole mouse brain using these probes.

The data is acquired on three computers (one decidated to acquiring the raw ephys, raw video and raw behavioral data
respectively), and saved into their corresponding folder (see sections below for details).
At the end of a Neuropixels recording session, some stimuli are replayed whilst the mouse is passive 
(i.e. not engaged in the IBL task). The behavioral data acquired during this replay of stimuli is also saved in a dedicated folder.

Once acquired, the data are centralised onto a single computer, and processed (using heavy algorithms, such as
Deep Lab Cut for tracking points on video data, or pyKilosort for detecting and sorting the spikes of cells on the ephys traces),
before being sent and stored onto our centralised database (see our [article on data architecture ](https://www.biorxiv.org/content/10.1101/827873v3) for details).



## What is available for download

### Behavioral data associated to our 2020's publication
The IBL has released all of the behavior sessions associated with the publication 
[International Brain Laboratory et al., 2021](https://elifesciences.org/articles/63711)
via [Datajoint](public_datajoint).

### Neuropixels datasets (pilot release)
The IBL has released a handful of pilot datasets that are available for download through both ONE and Datajoint (see sections below). 


## How to browse the datasets
If you first want to quickly view and browse what datasets are in a recording session, you can easily do so in a web browser via this [Flatiron web page](https://ibl.flatironinstitute.org/public/).

Generally speaking, a single recording session fits into a folder, which name is characterised by:
it's lab name / a folder Subjects / the name of the subject (i.e. the mouse nickname) / the date / the session number.

For example: `mainenlab/Subjects/ZM_2240/2020-01-21/001`

Notes:
- A lab can host multiple subjects, e.g. the 
[Churchland lab](https://ibl.flatironinstitute.org/public/churchlandlab/Subjects) hosts `CSHL047` and `CSHL049`.
- There can be multiple sessions done in one day per subject, in such case the number of session `001` would increase
to `002`, `003` etc.
- Sometimes, the valuable data is found only in a later session in the day (in the case of a restart for example),
so it is not uncommon to see sessions for which only the `003` folder is saved for example.

## Neuropixels pilot datasets
Specifically, the Neuropixels pilot datasets are in the folders:

- [churchlandlab/Subjects/CSHL047/2020-01-20/001](https://ibl.flatironinstitute.org/public/churchlandlab/Subjects/CSHL047/2020-01-20/001/)
- [churchlandlab/Subjects/CSHL049/2020-01-08/001](https://ibl.flatironinstitute.org/public/churchlandlab/Subjects/CSHL049/2020-01-08/001/)
- [cortexlab/Subjects/KS023/2019-12-10/001](https://ibl.flatironinstitute.org/public/cortexlab/Subjects/KS023/2019-12-10/001/)
- [hoferlab/Subjects/SWC_043/2020-09-21/001](https://ibl.flatironinstitute.org/public/hoferlab/Subjects/SWC_043/2020-09-21/001/)
- [zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001](https://ibl.flatironinstitute.org/public/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/)
- [mainenlab/Subjects/ZM_2240/2020-01-21/001/](https://ibl.flatironinstitute.org/public/mainenlab/Subjects/ZM_2240/2020-01-21/001/)

Taking the session from [mainenlab/Subjects/ZM_2240/2020-01-21/001/](https://ibl.flatironinstitute.org/public/mainenlab/Subjects/ZM_2240/2020-01-21/001/)
 as example, the following subfolders will contain:
- `alf/` : The extracted data, to be used in analysis.
- `logs/` : logged information
- `raw_behavior_data/` : The raw behavior data (events that occur during a trials)
- `raw_ephys_data/` : The raw ephys data (in this case, Neuropixels data)
- `raw_passive_data/`: The raw passive data (events that occur during the replay of task stimuli)
- `raw_video_data/`: The raw video data
- `spike_sorters/` : The raw processing output data for each spike sorter used

The `alf/` folder notably contains:
- the probe folder (`probe00/` or `probe01/`), in which are the extracted output of the spike sorting to be used for analysis
- the extracted behavior trials data
- the extracted DLC data (for each camera used, here `body`, `left` and `right`)
- the extracted wheel data
- the extracted passive protocol data

One probe folder, e.g. [`probe00/`](https://ibl.flatironinstitute.org/public/mainenlab/Subjects/ZM_2240/2020-01-21/001/alf/probe00/)
can contain the output of multiple spike sorters. In this case, it contains a first spike sorter output directly into the
folder itself (see e.g. the `cluster` datasets), and a secondary version under a subfolder
(here the subfolder named `pykilosort`).

The size of each dataset can be easily viewed under the `Size` column in the web browser. For example,
the [raw vide data](https://ibl.flatironinstitute.org/public/mainenlab/Subjects/ZM_2240/2020-01-21/001/raw_video_data/)
is particularly heavy (several GB). In this specific case, you can view the raw video data in the browser by clicking on it,
e.g. [_iblrig_leftCamera.raw](https://ibl.flatironinstitute.org/public/mainenlab/Subjects/ZM_2240/2020-01-21/001/raw_video_data/_iblrig_leftCamera.raw.edcfa043-6314-4f80-ba6f-bf6d08922eda.mp4).

A detailed explanation of datasets definition and format are described
in this [sheet](https://docs.google.com/spreadsheets/u/1/d/1ieLXRPLLSgUKcLvFkrqizfZl5HjdfE6bQ2KLBCRmjQo/edit?usp=drive_web&ouid=107692576857324699678)
and [document](https://docs.google.com/document/d/1OqIqqakPakHXRAwceYLwFY9gOrm8_P62XIfCTnHwstg/edit#).

## Download the public datasets

To start downloading and performing analysis on the datasets, please follow the links below.

1)  [Accessing public data with ONE](https://int-brain-lab.github.io/ONE/notebooks/one_quickstart.html)

2)  [Accessing public data with Datajoint](public_datajoint)

Note: Please use the ONE option for downloading Neuropixels datasets for now.