import subprocess


# TODO: logging
# TODO: "from packaging.version import parse" to more easily parse version numbers


def check_dependencies():
    """Check required dependencies are installed"""
    print("Checking for dependencies...")
    conda_version = str(subprocess.check_output([f"conda", "--version"])).split(" ")[1].split("\\n")[0]
    if int(conda_version.split(".")[0]) < 4:
        print("conda version is less than v4, update is required...")
        # conda update -q -y -n base -c defaults conda
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


def pip_install_packages():
    """Use pip to install packages listed in requirements.txt"""
    print("Ensuring pip is up to date and using it to install packages in the requirements.txt file...")
    try:
        subprocess.check_call(["conda", "run", "--name", "iblenv", "python", "-m", "pip", "install", "--upgrade", "pip"])
        subprocess.check_call(
            ["conda", "run", "--name", "iblenv", "python", "-m", "pip", "install", "--requirement", "requirements.txt"])
    except subprocess.CalledProcessError:
        print("pip installation could not be completed")
        raise


if __name__ == "__main__":
    print("------ install.py script called ------")
    check_dependencies()
    check_or_create_iblenv()
    pip_install_packages()
