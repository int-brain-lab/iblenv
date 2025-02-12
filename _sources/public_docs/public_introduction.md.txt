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

### Behavioral data associated to our 2020 publication
The IBL has released all of the behavior sessions associated with the publication 
[Standardized and reproducible measurement of decision-making in mice](https://elifesciences.org/articles/63711)
via ONE and Datajoint. 
* Please follow this [link](../notebooks_external/data_release_behavior) for instructions on how to access this data

### Pilot neuropixels datasets
The IBL has released a handful of pilot datasets that are available for download through ONE. 
* Please follow this [link](data_release_pilot) to explore these datasets 

### Reproducible ephys data associated with our 2022 preprint
The IBL has released all data associated with the preprint [Reproducibility of in vivo electrophysiological measurements in mice](https://www.biorxiv.org/content/10.1101/2022.05.09.491042v3). 
* Please follow this [link](../notebooks_external/data_release_repro_ephys) to access this data


### Brain wide map data release - Q4 2022
The IBL has released all data described in our [technical paper](https://doi.org/10.6084/m9.figshare.21400815). 
* Please follow this [link](../notebooks_external/data_release_brainwidemap) to access this data

### Coming soon: benchmark dataset for spike sorting
A list of insertion for which we will provide benchmarks is available [here](../notebooks_external/data_release_spikesorting_benchmarks).