import subprocess


# TODO: logging

def check_dependencies():
    # Check if git and conda are installed
    # Is git a requirement?
    print("Checking for dependencies...")
    conda_version = str(subprocess.check_output([f"conda", "--version"])).split(" ")[1].split("\\n")[0]
    if int(conda_version.split(".")[0]) < 4:
        print("conda version is less than v4, update is required...")
        # conda update -q -y -n base -c defaults conda
        exit(1)
    git_version = str(subprocess.check_output([f"git", "--version"])).split(" ")[2].split("\\n")[0]
    if int(git_version.split(".")[0]) < 2:
        print("git version is less than v2, update is required...")
        # conda install -q -y git
        exit(1)
    print("All dependencies OK.")


def check_or_create_iblenv():
    """Creates the Anaconda environment for iblenv"""
    print("Check if Anaconda iblenv exists")
    if "iblenv" in str(subprocess.run(["conda", "env", "list"], capture_output=True).stdout):
        print("iblenv already installed")  # remove environment, install fresh, or call an update?
    else:
        print("iblenv does not currently exist, creating it now...")
        try:
            subprocess.check_call(["conda", "create", "-q", "-y", "--name", "iblenv", "python=3.8"])
            print("Environment created")
        except subprocess.CalledProcessError:
            print("Anaconda creation of the iblenv environment failed.")
            raise


if __name__ == "__main__":
    print("------ install.py script called ------")
    check_dependencies()
    check_or_create_iblenv()

    # clone additional repositories (functionalize)
    # TODO: do not clone; create pypi packages in those repos instead
    # subprocess.check_call(["git", "clone", "https://github.com/int-brain-lab/ibllib.git"])
    # subprocess.check_call(["git", "clone", "https://github.com/int-brain-lab/iblapps.git"])
    # Include other repos?
    # git clone https://github.com/int-brain-lab/analysis.git
    # git clone https://github.com/int-brain-lab/IBL-pipeline.git
    # git clone https://github.com/int-brain-lab/iblenv.git
    # git clone https://github.com/cortex-lab/phylib
    # git clone https://github.com/cortex-lab/phy
