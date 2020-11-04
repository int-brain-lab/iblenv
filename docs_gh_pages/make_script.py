import os
import argparse
import subprocess
from pathlib import Path
import logging
from scripts.execute_notebooks import process_notebooks
from ibllib.misc import logger_config  # noqa

_logger = logging.getLogger('ibllib')
root = Path.cwd()
scripts_path = root.joinpath('scripts')

nb_path = root.joinpath('notebooks')
nb_path_external = [Path(root.parent.parent).joinpath('ibllib-repo', 'examples'),
                    Path(root.parent.parent).joinpath('ibllib-repo', 'brainbox', 'examples')]


def make_documentation(execute, force, documentation, clean, github, message):

    # Clean up any nblink files
    nb_external_files = root.joinpath('notebooks_external').glob('*')
    for file in nb_external_files:
        os.remove(file)

    if execute:
        process_notebooks(nb_path, execute=True, force=force)
        for nb_path_ext in nb_path_external:
            process_notebooks(nb_path_ext, execute=True, force=force,
                              link=True, filename_pattern='docs')
        _logger.info("Finished processing notebooks")

    if documentation:
        # Need to make sure you have the documentation python files
        if not execute:
            for nb_path_ext in nb_path_external:
                process_notebooks(nb_path_ext, execute=False, link=True, filename_pattern='docs')

        _logger.info("Cleaning up previous documentation")
        os.system("make clean")
        _logger.info("Making documentation")
        os.system("make html")

        # Clean up the build path regardless
        build_nb_path = root.joinpath('_build', 'html', 'notebooks')
        build_nb_source_path = root.joinpath('_build', 'html', '_sources', 'notebooks')
        build_nb_external_path = root.joinpath('_build', 'html', 'notebooks_external')
        process_notebooks(build_nb_path, execute=False, cleanup=True)
        process_notebooks(build_nb_source_path, execute=False, cleanup=True)
        process_notebooks(build_nb_external_path, execute=False, cleanup=True)

    # Clean up notebooks in directory if also specified
    if clean:
        _logger.info("Cleaning up notebooks")
        process_notebooks(nb_path, execute=False, cleanup=True)
        for nb_path_ext in nb_path_external:
            process_notebooks(nb_path_ext, execute=False, cleanup=True,
                              filename_pattern='docs')

    # If github is True push the latest documentation to gh-pages
    if github:
        # Need to figure out how to do this
        if not message:
            message = "commit latest documentation"

        subprocess.call(['scripts\gh_push.sh', message], shell=True)  # noqa: E605


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Make IBL documentation')

    parser.add_argument('-e', '--execute', default=False, action='store_true',
                        help='Execute notebooks')
    parser.add_argument('-f', '--force', default=False, action='store_true',
                        help='Force notebook execution even if already run')
    parser.add_argument('-d', '--documentation', default=False, action='store_true',
                        help='Make documentation')
    parser.add_argument('-c', '--cleanup', default=False, action='store_true',
                        help='Cleanup notebooks once documentation made')
    parser.add_argument('-gh', '--github', default=False, action='store_true',
                        help='Push documentation to gh-pages')
    parser.add_argument('-m', '--message', default=None, required=False, type=str,
                        help='Commit message')
    args = parser.parse_args()
    make_documentation(execute=args.execute, force=args.force, documentation=args.documentation,
                       clean=args.cleanup, github=args.github, message=args.message)
