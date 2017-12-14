# Eredar

A Program To Read and Store epub books.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for
development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

pycharm or other python interpreter ide


### Installing

if using pycharm follow the following instructions

```
start up pycharm and go to check out from version control
select github.
create api token
enter github details.
```

when logged in:

```
Open the context menu and go to option:https://github.com/gitreadyforthis/eredar.git
chose the directory to insert it into or just leave it with default and hit clone
```
when project is cloned succsessfully:
```
go to the file requirements.txt and allow pycharm to install dependancies by clicking the package requirements bar.
```
when dependancies are installed:
```
go to the toolbar click tools → manage.py task
when console comes up type makemigrations
hit enter
migrate hit enter
```
when migrations have finished:
```
hit the run button at the top where it says eredar with the django symbol
it should start a console 
click the localhost ip to open the website in your default browser
```
use site as normal.
register login read and upload.

## Built With

* [Pycharm](https://www.jetbrains.com/pycharm/)- Primary Development environment
* [Github](github.com) - project management
* [NodeJs](https://nodejs.org/en/)
* [Django](https://www.djangoproject.com/)
* [Epubjs](http://futurepress.org/)

## Authors

* **Brian Reiskin**


## Acknowledgments

* Thanks to Epubjs for making their code open source
* Was inspired by a lackluster reading app i had for my phone to see if i could do better
