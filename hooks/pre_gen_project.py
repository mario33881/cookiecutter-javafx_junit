"""
Be sure the user won't change the 'java_package_dir' value.

In theory using '_java_package_dir' (with the underscore "_") instead of '_java_package_dir' would not prompt the user from input, preventing the user from entering the wrong value.

Strangely enough, '_java_package_dir' value is not calculated correctly by cookiecutter but with 'java_package_dir' it works... (Problem found on Windows)
"""

import sys

groupId = "{{ cookiecutter.groupId }}"
java_package_dir = "{{ cookiecutter.java_package_dir }}"

expected_java_package_dir = groupId.replace(".", "/")

if expected_java_package_dir != java_package_dir:
    print("ERROR: please do not set a custom 'java_package_dir' value! Please, execute cookiecutter again and press enter when asked for this value")
    print("The correct value will be generated automatically from the 'groupId' value")
    sys.exit(1)
