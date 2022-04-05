# COOKIECUTTER - JAVAFX AND JUNIT

This cookiecutter defines a simple Hello world Java application
that uses JavaFX as the GUI library and JUnit as the unit testing library.

## Prerequisites

1. Install [python 3](https://www.python.org/). Make sure it is available in PATH:

    ```
    python3 --version
    ```
    > Also try ```python --version``` or ```py --version``` if that doesn't work.

2. Install cookiecutter using PIP:

    ```
    python3 -m pip install --user cookiecutter
    ```
    > If ```python3``` didn't work in the command above, use the working alternative.

    > If the command fails, try without the ```--user``` flag.

3. Install Java JDK (Java Development Kit).

4. Install maven.

    For debian based distros (like Ubuntu) use:
    ```
    sudo apt install maven
    ```

    For Windows the easiest way of installing maven is to use [chocolatey](https://chocolatey.org/).

    [Install chocolatey](https://chocolatey.org/install) and then run the following command inside powershell:
    ```
    choco install maven
    ```

    You can also use a Graphical User Interface for chocolatey. But first you need to install it using this command:
    ```
    choco install chocolateygui
    ```
    After that you can install Maven from the chocolatey tab, search for "Maven" and install it.

## Use the cookiecutter template

1. Run the following command and answer the prompted questions:

    ```
    cookiecutter https://github.com/mario33881/cookiecutter-javafx_junit.git
    ```

2. Read the ```README.md``` file inside the project template to get started.

Change the files as you like with your favourite IDE or text editor.

You can run the application and tests by using an IDE or by running Maven from the command line.
> More instructions inside the project's ```README.md``` file

## Changelog

**2022-04-05 Version 1.0.0**:

first version

## Author
[Zenaro Stefano (mario33881)](https://github.com/mario33881)
