import subprocess

# Perform some sort of logging
# Error checking on git and Anaconda
# Include other repos?
# git clone https://github.com/int-brain-lab/analysis.git
# git clone https://github.com/int-brain-lab/IBL-pipeline.git
# git clone https://github.com/int-brain-lab/iblenv.git
# git clone https://github.com/cortex-lab/phylib
# git clone https://github.com/cortex-lab/phy
if __name__ == "__main__":
    subprocess.check_call(["git", "clone", "https://github.com/int-brain-lab/ibllib.git"])
    subprocess.check_call(["git", "clone", "https://github.com/int-brain-lab/iblapps.git"])
