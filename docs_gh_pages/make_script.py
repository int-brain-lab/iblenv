import os
os.environ["TQDM_DISABLE"] = "1"  # noqa

import sys
import shutil
import argparse
import subprocess
from pathlib import Path

from iblutil.util import setup_logger
from scripts.execute_notebooks import process_notebooks

_logger = setup_logger(name='íbllib', level=20)

root = Path.cwd()
scripts_path = root.joinpath('scripts')

nb_path = root.joinpath('notebooks')
nb_path_external = [# Path(root.parent.parent).joinpath('ibllib-repo', 'examples'),
                    Path(root.parent.parent).joinpath('ibllib-repo', 'examples', 'loading_data'),
                    Path(root.parent.parent).joinpath('iblatlas', 'examples'),
                    Path(root.parent.parent).joinpath('ibllib-repo', 'examples', 'data_release'),
                    Path(root.parent.parent).joinpath('ibllib-repo', 'examples', 'exploring_data'),
                    Path(root.parent.parent).joinpath('ibllib-repo', 'brainbox', 'examples'),
                    Path(root.parent.parent).joinpath('ONE', 'docs', 'notebooks')]
# external_file_patterns = ['docs', 'loading', 'atlas', 'docs', 'quickstart']
external_file_patterns = ['loading', 'atlas', 'data', 'data', 'docs_wheel', 'quickstart']


def make_documentation(execute, force, documentation, clean, specific, github, message, pre_clean, serve=False):

    # Clean up any nblink files
    nb_external_files = root.joinpath('notebooks_external').glob('*')
    for file in nb_external_files:
        os.remove(file)

    assert len(external_file_patterns) == len(nb_path_external)
    status = 0
    # Case where we want to rebuild all examples
    if execute and not specific:
        # Execute notebooks in docs folder
        #### remove the running of datajoint docs
        # status += process_notebooks(nb_path, execute=True, force=force)
        # Execute notebooks in external folders
        for nb_path_ext, pattern in zip(nb_path_external, external_file_patterns):
            status += process_notebooks(nb_path_ext, execute=True, force=force,
                                        link=True, filename_pattern=pattern)
        _logger.info("Finished processing notebooks")

        if status != 0:
            # One or more examples returned an error
            sys.exit(1)
        else:
            # If no errors make the documentation
            _logger.info("Cleaning up previous documentation")
            os.system("make clean")
            _logger.info("Making documentation")
            os.system("make html")
            sys.exit(0)

    # Case where we only want to build specific examples
    if execute and specific:
        for nb in specific:
            if str(nb).startswith(str(root)):
                status += process_notebooks(nb, execute=True, force=force)
            else:
                status += process_notebooks(nb, execute=True, force=force, link=True)
            _logger.info("Finished processing notebooks")

        # Create the link files for the other notebooks in external paths that we haven't
        # executed. N.B this must be run after the above commands
        for nb_path_ext, pattern in zip(nb_path_external, external_file_patterns):
            process_notebooks(nb_path_ext, execute=False, link=True, filename_pattern=pattern)

        if status != 0:
            # One or more examples returned an error
            sys.exit(1)
        else:
            # If no errors make the documentation
            _logger.info("Cleaning up previous documentation")
            os.system("make clean")
            _logger.info("Making documentation")
            os.system("make html")
            sys.exit(0)

    if documentation:
        for nb_path_ext, pattern in zip(nb_path_external, external_file_patterns):
            process_notebooks(nb_path_ext, execute=False, link=True, filename_pattern=pattern)

        _logger.info("Cleaning up previous documentation")
        os.system("make clean")
        _logger.info("Making documentation")
        os.system("make html")
        print("Documentation built successfully, to serve the site locally, run the following command:")
        print("python -m http.server -d ./_build/html")
        sys.exit(0)

    if pre_clean:
        # clean up for github but don't commit. In the examples only notebooks with an execute flag=True are kept,
        # the rest are deleted.
        # Clean up the build path regardless
        build_nb_path = root.joinpath('_build', 'html', 'notebooks')
        build_nb_external_path = root.joinpath('_build', 'html', 'notebooks_external')
        process_notebooks(build_nb_path, execute=False, cleanup=True, remove_gh=True)
        process_notebooks(build_nb_external_path, execute=False, cleanup=True, remove_gh=True)

        # remove the _sources folder as we don't need this
        build_nb_source_path = root.joinpath('_build', 'html', '_sources')
        if build_nb_source_path.exists():
            shutil.rmtree(build_nb_source_path)


    if github:
        # clean up for github. In the examples only notebooks with an execute flag=True are kept,
        # the rest are deleted.
        # Clean up the build path regardless
        build_nb_path = root.joinpath('_build', 'html', 'notebooks')
        build_nb_external_path = root.joinpath('_build', 'html', 'notebooks_external')
        process_notebooks(build_nb_path, execute=False, cleanup=True, remove_gh=True)
        process_notebooks(build_nb_external_path, execute=False, cleanup=True, remove_gh=True)

        # remove the _sources folder as we don't need this
        build_nb_source_path = root.joinpath('_build', 'html', '_sources')
        if build_nb_source_path.exists():
            shutil.rmtree(build_nb_source_path)

        # Need to figure out how to do this
        if not message:
            message = "commit latest documentation"

        exec = Path('scripts').joinpath('gh_push.sh')
        command = f'{exec} "{message}"'
        print(command)
        subprocess.call(command, shell=True)  # noqa: E605

    # Clean up notebooks in directory if also specified
    if clean:
        _logger.info("Cleaning up notebooks")
        process_notebooks(nb_path, execute=False, cleanup=True)
        for nb_path_ext, pattern in zip(nb_path_external, external_file_patterns):
            process_notebooks(nb_path_ext, execute=False, cleanup=True,
                              filename_pattern=pattern)

        try:
            build_path = root.joinpath('_build')
            if build_path.exists():
                shutil.rmtree(build_path)
        except Exception as err:
            print(err)
            _logger.error('Could not remove _build directory in iblenv/docs_gh_pages, please '
                          'delete manually')
        try:
            autosummary_path = root.joinpath('_autosummary')
            if autosummary_path.exists():
                shutil.rmtree(autosummary_path)
        except Exception as err:
            print(err)
            _logger.error('Could not remove _autosummary directory in iblenv/docs_gh_pages, please'
                          ' delete manually')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Make IBL documentation')

    parser.add_argument('-e', '--execute', default=False, action='store_true',
                        help='Execute notebooks')
    parser.add_argument('-f', '--force', default=False, action='store_true',
                        help='Force notebook execution even if already run')
    parser.add_argument('-d', '--documentation', default=False, action='store_true',
                        help='Make documentation')
    parser.add_argument('-s', '--specific', nargs='+', required=False,
                        help='List of specific files to execute')
    parser.add_argument('-c', '--cleanup', default=False, action='store_true',
                        help='Cleanup notebooks once documentation made')
    parser.add_argument('-gh', '--github', default=False, action='store_true',
                        help='Push documentation to gh-pages')
    parser.add_argument('-pc', '--preclean', default=False, action='store_true',
                        help='Clean up documentation for gh-pages')
    parser.add_argument('-m', '--message', default=None, required=False, type=str,
                        help='Commit message')
    args = parser.parse_args()
    make_documentation(execute=args.execute, force=args.force, documentation=args.documentation,
                       clean=args.cleanup, specific=args.specific, github=args.github,
                       message=args.message, pre_clean=args.preclean)
