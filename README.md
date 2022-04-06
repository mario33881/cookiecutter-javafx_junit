# COOKIECUTTER - JAVAFX AND JUNIT

This cookiecutter defines a simple Hello world Java application
that uses JavaFX as the GUI library and JUnit as the unit testing library.

## Prerequisites

Before using this template you need to install:
* ```git```: it is used to download this template from GitHub
* ```python 3```: the template engine is written and executed in python
* ```cookiecutter``` library for python: template engine, creates the project folder from this template
* ```Java JDK```: needed to program Java applications
* ```Maven```: project management and comprehension tool for Java projects. Installs dependencies and runs builds/tests from the terminal (and from IDEs).

Steps to install the prerequisites:
> NOTE: if you install something and you can't run it using the command line, try closing the terminal and then open it again.

1. Install git.

    For debian based distros (like Ubuntu) use:
    ```
    sudo apt install git
    ```

    For Windows you can download the setup file from the [official website here](https://git-scm.com/downloads).

2. Install [python 3](https://www.python.org/). Make sure it is available in PATH:

    ```
    python3 --version
    ```
    > Also try ```python --version``` or ```py --version``` if that doesn't work.

3. Install cookiecutter using PIP:

    ```
    python3 -m pip install --user cookiecutter
    ```
    > If ```python3``` didn't work in the command above, use the working alternative.

    > If the command fails, try without the ```--user``` flag.

    Try running this command to check if cookiecutter was installed correctly:
    ```
    cookiecutter --version
    ```

4. Install [Java JDK (Java Development Kit)](https://www.oracle.com/java/technologies/downloads/).

5. Install Maven.

    For debian based distros (like Ubuntu) use:
    ```
    sudo apt install maven
    ```

    For Windows the easiest way of installing Maven is to use [chocolatey](https://chocolatey.org/).

    [Install chocolatey](https://chocolatey.org/install) and then run the following command inside powershell:
    ```
    choco install maven
    ```

    You can also use a Graphical User Interface for chocolatey. But first you need to install it using this command:
    ```
    choco install chocolateygui
    ```
    After that you can install Maven from the chocolatey tab, search for "Maven" and install it.

    Try running this command to check if Maven was installed correctly:
    ```
    mvn --version
    ```

## Use the cookiecutter template

1. Run cookiecutter and answer the prompted questions.

    Cookiecutter will ask you to enter values for these parameters:
    * ```projectName```: project name
    * ```artifactId```: it is the name of the main executable. For example, you can use the project name or something like "MainApp".
    * ```groupId```: Group identifier, "inverse" URL format (the same format as the java ```package name``` convention). You can choose something like "org.example.myapp".
    * ```java_package_dir```: use the value suggested to you by pressing enter
    * ```version```: application version
    * ```os```: are you developing on a "linux/other" OS machine or on a "windows" machine?
    * ```indent_style```: do you prefer "space"(s) or "tab"(s) as your identation style?
    * ```indent_size```: indentation size
    > You can always accept default/suggested values by pressing enter

    Here is the command that will prompt you these questions:
    ```
    cookiecutter https://github.com/mario33881/cookiecutter-javafx_junit.git
    ```

2. Read the ```README.md``` file inside the project template to get started.

Change the files as you like with your favourite IDE or text editor.

You can run the application and tests by using an IDE or by running Maven from the command line.
> More instructions inside the project's ```README.md``` file

Next time you can simply run the following command to create a new project:
```
cookiecutter cookiecutter-javafx_junit
```
> Cookiecutter saves the template locally in the ```.cookiecutter``` folder (located inside the home folder)

## Changelog

**2022-04-05 Version 1.0.0**:

first version

## Author
[Zenaro Stefano (mario33881)](https://github.com/mario33881)
