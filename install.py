import os
import subprocess

# TODO: logging
ON_WINDOWS = True if os.name == "nt" else False


def check_dependencies():
    """Check required dependencies are installed"""
    print("Checking for dependencies...")
    environment_vars = str(subprocess.check_output([os.environ["CONDA_EXE"], "list", "-n", "base", "--json"]))
    if "conda" not in environment_vars:
        print("--- Anaconda not found in environment, please follow the README instructions for repo dependencies ---")
        print(environment_vars)
        exit(0)
    try:
        conda_version = str(subprocess.check_output(["conda", "--version"], shell=True)).split(" ")[1].split(".") if ON_WINDOWS \
            else conda_version = str(subprocess.check_output(["conda", "--version"])).split(" ")[1].split(".")
    except subprocess.CalledProcessError or FileNotFoundError:
        print("Anaconda call failed, check if Anaconda is installed.")
        raise
    conda_major_version = int(conda_version[0])
    conda_minor_version = int(conda_version[1])
    if conda_major_version < 4:
        print("conda version is less than v4, manual removal and re-installation is required...")
        exit(0)
    elif conda_major_version == 4 and conda_minor_version < 10:
        print("Attempting to update Anaconda...")
        try:
            subprocess_cmd = ["conda", "update", "--quiet", "--yes", "--name", "base", "--channel", "defaults", "conda"]
            subprocess.check_output(subprocess_cmd, shell=True) if ON_WINDOWS else subprocess.check_output(subprocess_cmd)
        except subprocess.CalledProcessError:
            print("Anaconda update failed, check if Anaconda is installed.")
            raise
    else:
        print("All dependencies OK.")


def check_or_create_iblenv():
    """Creates the Anaconda environment for iblenv"""
    print("Check if Anaconda iblenv exists")
    if "iblenv" in str(subprocess.run(["conda", "env", "list"], capture_output=True).stdout):
        print("iblenv already installed")  # remove environment, install fresh, or call an update?
    else:
        print("iblenv does not currently exist, creating it now...")
        try:
            subprocess_cmd = ["conda", "create", "-q", "-y", "--name", "iblenv", "python=3.8"]
            subprocess.check_call(subprocess_cmd, shell=True) if ON_WINDOWS else subprocess.check_call(subprocess_cmd)
            print("Environment created")
        except subprocess.CalledProcessError:
            print("Anaconda creation of the iblenv environment failed.")
            raise


def pip_install_packages():
    """Use pip to install packages listed in requirements.txt"""
    print("Ensuring pip is up to date and using it to install packages in the requirements.txt file...")
    try:
        sp_upgrade_cmd = ["conda", "run", "--name", "iblenv", "python", "-m", "pip", "install", "--upgrade", "pip"]
        sp_run_cmd = ["conda", "run", "--name", "iblenv", "python", "-m", "pip", "install", "--requirement", "requirements.txt"]

        subprocess.check_call(sp_upgrade_cmd, shell=True) if ON_WINDOWS else subprocess.check_call(sp_upgrade_cmd)
        subprocess.check_call(sp_run_cmd, shell=True) if ON_WINDOWS else subprocess.check_call(sp_run_cmd)
    except subprocess.CalledProcessError:
        print("pip installation could not be completed")
        raise


if __name__ == "__main__":
    print("------ install.py script called ------")
    check_dependencies()
    check_or_create_iblenv()
    pip_install_packages()
