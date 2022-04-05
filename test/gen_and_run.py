"""
GEN_AND_RUN: Generates projects using the template and runs them.

Currently this script needs someone that manually
closes the windows that are opened by maven.
"""

import json
import subprocess
import os
import shutil

from cookiecutter.main import cookiecutter
from cookiecutter.exceptions import FailedHookException

current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, "testconfig.json")
default_config_path = os.path.join(current_dir, "..", "cookiecutter.json")

test_cases_conf = [
    {
        "artifactId": "AnotherName",
        "groupId": "com.rand.example.company",
        "indent_size": "3",
        "indent_style": "tab",
        "java_package_dir": "com/rand/example/company",
        "os": "windows",
        "projectName": "AnotherName",
        "version": "3.2.1"
    },
]

test_cases_fails_conf = [
    {
        "artifactId": "A",
        "groupId": "com.rand.example.second.company",
        "indent_size": "5",
        "indent_style": "spaces",
        "java_package_dir": "com/custom/strange/package/dir/example/company",
        "os": "linux/other",
        "projectName": "DifferentNameFromArtifactId",
        "version": "0.0.0"
    }
]


def test_default_config():
    """
    Tests the default configuration.
    """
    test_custom_config(t_config=None)


def test_custom_config(t_config):
    test_generic_config(t_config, will_fail=False)

def test_failing_config(t_config):
    test_generic_config(t_config, will_fail=True)


def test_generic_config(t_config, will_fail):
    """
    Tests a generic configuration given by the user.

    :param dict t_config: custom configuration
    :param bool will_fail: True means that this config is meant to fail
    """
    os.chdir(current_dir)

    try:
        cookiecutter(
            os.path.realpath(os.path.join(current_dir, "..")),
            no_input=True,
            extra_context=t_config,
            overwrite_if_exists=True
        )
    except FailedHookException as e:
        if not will_fail:
            raise e

    if will_fail:
        os.chdir(current_dir)
        return None

    if t_config is None:
        os.chdir("MyAmazingApp")
    else:
        os.chdir(t_config["projectName"])

    exit_code = subprocess.call("mvn test", shell=True)
    if will_fail:
        assert exit_code != 0, "Tests exit code should NOT be 0, or fail"
    else:
        assert exit_code == 0, "Tests exit code should be 0, or success"

    exit_code = subprocess.call("mvn javafx:run", shell=True)
    if will_fail:
        assert exit_code != 0, "Running the application should result in having exit code NOT 0, or fail"
    else:
        assert exit_code == 0, "Running the application should result in having exit code 0, or success"

    os.chdir(current_dir)


def verify_config_input(t_config):
    """
    Verifies that the custom config has
    all the correct properties.

    :param dict t_config: custom configuration
    :raises ValueError: the custom config dictionary has wrong or missing keys
    """
    def_conf = get_default_config(default_config_path)

    if sorted(def_conf.keys()) != sorted(t_config.keys()):
        raise ValueError("Some keys are wrong/missing inside the '{}' config file".format(t_config))


def get_default_config(t_path):
    """
    Read default configuration from ``t_path`` file

    :param str t_path: default configuration path
    :return dict: dictionary with the configuration
    """
    with open(t_path, 'r') as infile:
        context = json.load(infile)

    return context


def remove(t_path):
    """
    Removes ``filepath`` with the correct function:
    uses os.remove() on files and shutil.rmtree on folders.

    :param str t_path: path of file/folder to remove
    """
    if os.path.isfile(t_path):
        os.remove(t_path)
    elif os.path.isdir(t_path):
        shutil.rmtree(t_path)


if __name__ == "__main__":

    print("testing default:")
    test_default_config()
    remove(os.path.join(current_dir, "MyAmazingApp"))

    print("=" * 20)
    for test_case_conf in test_cases_conf:
        print("testing custom conf:", test_case_conf)
        verify_config_input(test_case_conf)
        test_custom_config(test_case_conf)
        remove(os.path.join(current_dir, test_case_conf["projectName"]))
        print("=" * 20)

    for test_case_conf in test_cases_fails_conf:
        print("testing custom failing conf:", test_case_conf)
        verify_config_input(test_case_conf)
        test_failing_config(test_case_conf)
        project_path = os.path.join(current_dir, test_case_conf["projectName"])
        if os.path.exists(project_path):
            remove(project_path)
        print("=" * 20)

    print("Done!")
