# Using napari with cryo-electron tomography data

This repo contains a quick demonstration of how to use napari to visualise cryo-electron tomography data. 

This demo was given after a presentation at the MRC Laboratory of Molecular Biology tomography meeting on 29/04/22. Slides can be downloaded from [zenodo](https://zenodo.org/record/6505039).

# Installation
Install into a fresh virtual environment, I personally use [miniconda](https://docs.conda.io/en/latest/miniconda.html) for environment management.

```commandline
git clone https://github.com/alisterburt/napari-cryo-et-demo.git
cd napari-cryo-et-demo
pip install -r requirements.txt
```

# Downloading example data

We will download [example data from zenodo](https://zenodo.org/record/6504891) using `zenodo_get` which was installed in the previous step.

```commandline
zenodo_get --output-dir hiv 6504891
```

# Running
Run the demo script with 

```commandline
python visualise_particles_on_tomogram.py
```