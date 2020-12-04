
# SpikeInterface:<br> graphical pipeline designer

## Context

[SpikeInterface](https://github.com/SpikeInterface/spikeinterface) is a Python framework designed to unify preexisting spike sorting technologies into a single code base. It is a piece of software mostly used among academic neuroscience labs.

There also exists [spikely](https://github.com/SpikeInterface/spikely), which is a graphic UI built with [PyQT](https://en.wikipedia.org/wiki/PyQt) and it wraps around SpikeInterface so SpikeInterface library can be used without writing a single line of code.

![](https://docs.monadical.com/uploads/upload_c8439e9b37ddb18452709c8cf457ed34.png)

This window provides a way to design a pipeline of SpikeInterface elements that needs to be run as jobs.

## Issue

spikely interface works good but looks tough and doesn't represent a clear workflow/pipeline, so creating a better graphical interface is required.

Suggestion is to use [React](https://reactjs.org/)  and [react-digraph](https://github.com/uber/react-digraph) (or similar) along with [Django](https://www.djangoproject.com/) and [airflow](https://airflow.apache.org/) (or similar python job scheduler) to build a webapp that offers a better graphical interface to design workflows, run and manage jobs.

Like this one:
![](https://docs.monadical.com/uploads/upload_41be742479a2397ac3ae5cd6b7697552.gif)


or this one:
![](https://docs.monadical.com/uploads/upload_37c2cacf1d3faaa2a0f49a2c3b57b5ca.png)

## Proposal

Goal is to improve the user experience on pipeline designing, steps to accomplish that can be summarized like:

1. Abstract/couple SpikeInterface [elements](https://spikeinterface.readthedocs.io/en/latest/api.html) with a DAG (directional acyclic graph) pipeline framework and be able to run sample pipelines. *Note: providing an example is helpful* **~3-4 weeks**
    * Create script for running pipelines using preferred structure to save it
3. Create Django project, react page and pipeline designing view, including: list of nodes, way to draw and connect them, parameter setting panel **~3-4 weeks**
4. Connect point 1 and 2 to programmatically construct pipelines with webapp and execute them with DAG+SpikeInterface **~7 weeks**
    * Connect ui to previous Abstraction (not running yet) (2 weeks)
    * Add react-graph, constructing pipelines, saving params and saving fine pipeline data file (3 weeks)
    * Connect Ui to backend pipeline processing to complete tasks (2 weeks)

ETA: ~7-10 weeks

*For further work:*
* a job viewer/manager can be developed to gain more control over running pipeline
* ability to save/load pipelines
* Use docker to containerize project 

### Concerns and time delayers
* Understanding SpikeInterface elements, associated parameters (do they all have defaults?) and time/resource consuming tasks


---
---
---

## Research

A python pipeline/workflow library allows the user to run tasks in different ways which includes single sequential lines, trees, diamonds and decision forks.
Python pipeline libraries/frameworks:

* [Apache Airflow](https://github.com/apache/airflow): Robust enough, GUI included, complex structure.
* [Couler](https://github.com/couler-proj/couler): Made to be simpler than airflow, requires Argo
* [Mara pipelines](https://github.com/mara/mara-pipelines): Looks understandable, requires Postgres
* [Bonobo](https://github.com/python-bonobo/bonobo): ETL python framework, easy syntax, Django commands compatible
* [Jug](https://github.com/luispedro/jug): Simple, maybe not enough, still worth the review
* [Metaflow](https://github.com/Netflix/metaflow): Powered by Netflix, looks powerful
* [pypyr](https://pypyr.io/): Uses .yaml files to define the pipeline
* [dagster](https://dagster.io/): Pipelines written in python, complex and robust
* [ploomber](https://github.com/ploomber/ploomber): Based on modular scripts, looks useful

