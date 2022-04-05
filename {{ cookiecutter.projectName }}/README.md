# {{ cookiecutter.artifactId }}

This is a template for JavaFX applications.

Creates a 640x480 window that shows which versions of Java and JavaFX the app is using.

> This template also defines a simple unit tests template using JUnit 5.

## Repository files

This repository contains the following files:
* ```.editorconfig```: tells your text editor to trim trailing whitespace, set the correct end of line, ...
* ```.gitignore```: tells git which files to ignore (build output)
* ```pom.xml```: Maven configuration file (Defines JavaFX and JUnit as dependencies)
* ```README.md```: this file. Describes what the application does, its structure, how to run it, how to run the tests, who are the authors, ...

This repository contains the following folders:
* ```src```: contains source files and resources used by the project.
    * ```main/java```: contains application's source code
    * ```main/resources```: contains application's resources
    * ```test/java```: contains tests' source code
    * ```test/resources```: contains tests' resources

## How to run the application

To run the application, execute the following command in the command line:
```
mvn javafx:run
```

## How to run the tests

To run the application's tests, execute the following command:
```
mvn test
```

## Authors

The authors are x, y, z.
