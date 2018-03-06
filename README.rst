====================
OpenFermion-ProjectQ
====================

.. image:: https://travis-ci.org/quantumlib/OpenFermion-ProjectQ.svg?branch=master
    :target: https://travis-ci.org/quantumlib/OpenFermion-ProjectQ

.. image:: https://coveralls.io/repos/github/quantumlib/OpenFermion-ProjectQ/badge.svg?branch=master
    :target: https://coveralls.io/github/quantumlib/OpenFermion-ProjectQ?branch=develop

.. image:: https://readthedocs.org/projects/openfermion-projectq/badge/?version=latest
    :target: http://openfermion-projectq.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://badge.fury.io/py/openfermionprojectq.svg
    :target: https://badge.fury.io/py/openfermionprojectq

.. image:: https://img.shields.io/badge/python-2.7%2C%203.4%2C%203.5%2C%203.6-brightgreen.svg

`OpenFermion <http://openfermion.org>`_ is an open source package for compiling and analyzing quantum algorithms that simulate fermionic systems.
This plugin library allows the circuit simulation and compilation package `ProjectQ <https://projectq.ch>`_ to interface with OpenFermion.

Getting started
===============

Installing OpenFermion-ProjectQ requires pip. Make sure that you are using an up-to-date version of it.
Once installation is complete, be sure to take a look at the
`ipython notebook demo <https://github.com/quantumlib/OpenFermion-ProjectQ/blob/master/examples/openfermionprojectq_demo.ipynb>`__
as well as our detailed `code documentation <http://openfermion-projectq.readthedocs.io/en/latest/openfermionprojectq.html>`__.

Developer install
-----------------

To install the latest versions of OpenFermion, ProjectQ and OpenFermion-ProjectQ (in development mode):

.. code-block:: bash

  git clone https://github.com/quantumlib/OpenFermion-ProjectQ
  cd OpenFermion-ProjectQ
  python -m pip install -e .

Library install
---------------

To install the latest PyPI releases as libraries (in user mode):

.. code-block:: bash

  python -m pip install --user openfermionprojectq

How to contribute
=================

We'd love to accept your contributions and patches to OpenFermion-ProjectQ.
There are a few guidelines you need to follow.
Contributions to OpenFermion-ProjectQ must be accompanied by a Contributor License Agreement.
You (or your employer) retain the copyright to your contribution,
this simply gives us permission to use and redistribute your contributions as part of the project.
Head over to https://cla.developers.google.com/
to see your current agreements on file or to sign a new one.

All submissions, including submissions by project members, require review.
We use GitHub pull requests for this purpose. Consult
`GitHub Help <https://help.github.com/articles/about-pull-requests/>`__ for
more information on using pull requests.
Furthermore, please make sure your new code comes with extensive tests!
We use automatic testing to make sure all pull requests pass tests and do not
decrease overall test coverage by too much. Make sure you adhere to our style
guide. Just have a look at our code for clues. We mostly follow
`PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_ and use
the corresponding `linter <https://pypi.python.org/pypi/pep8>`_ to check for it.
Code should always come with documentation.

Authors
=======

`Ryan Babbush <http://ryanbabbush.com>`__ (Google),
`Jarrod McClean <http://jarrodmcclean.com>`__ (Google),
`Ian Kivlichan <http://aspuru.chem.harvard.edu/ian-kivlichan/>`__ (Harvard),
`Kevin J. Sung <https://github.com/kevinsung>`__ (University of Michigan),
`Damian Steiger <https://github.com/damiansteiger>`__ (ETH Zurich),
`Dave Bacon <https://github.com/dabacon>`__ (Google),
`Yudong Cao <https://github.com/yudongcao>`__ (Harvard),
`Chengyu Dai <https://github.com/jdaaph>`__ (University of Michigan),
`E. Schuyler Fried <https://github.com/schuylerfried>`__ (Harvard),
`Craig Gidney <https://github.com/Strilanc>`__ (Google),
`Brendan Gimby <https://github.com/bgimby>`__ (University of Michigan),
`Thomas Häner <https://github.com/thomashaener>`__ (ETH Zurich),
`Tarini Hardikar <https://github.com/TariniHardikar>`__ (Dartmouth),
`Vojtĕch Havlíček <https://github.com/VojtaHavlicek>`__ (Oxford),
`Cupjin Huang <https://github.com/pertoX4726>`__ (University of Michigan),
`Zhang Jiang <https://ti.arc.nasa.gov/profile/zjiang3>`__ (NASA),
`Thomas O'Brien <https://github.com/obriente>`__ (Leiden University),
`Isil Ozfidan <https://github.com/conta877>`__ (D-Wave Systems),
`Matthew Neeley <https://github.com/maffoo>`__ (Google),
`Max Radin <https://github.com/max-radin>`__ (UC Santa Barbara),
`Jhonathan Romero <https://github.com/jromerofontalvo>`__ (Harvard),
`Nicholas Rubin <https://github.com/ncrubin>`__ (Rigetti),
`Daniel Sank <https://github.com/DanielSank>`__ (Google),
`Nicolas Sawaya <https://github.com/nicolassawaya>`__ (Harvard),
`Kanav Setia <https://github.com/kanavsetia>`__ (Dartmouth),
`Hannah Sim <https://github.com/hsim13372>`__ (Harvard),
`Mark Steudtner <https://github.com/msteudtner>`__  (Leiden University),
`Wei Sun <https://github.com/Spaceenter>`__ (Google) and
`Fang Zhang <https://github.com/fangzh-umich>`__ (University of Michigan).

How to cite
===========
When using OpenFermion-ProjectQ for research projects, please cite:

    Jarrod R. McClean, Ian D. Kivlichan, Kevin J. Sung, Damian S. Steiger,
    Yudong Cao, Chengyu Dai, E. Schuyler Fried, Craig Gidney, Brendan Gimby,
    Thomas Häner, Tarini Hardikar, Vojtĕch Havlíček, Cupjin Huang, Zhang Jiang,
    Matthew Neeley, Thomas O'Brien, Isil Ozfidan, Maxwell D. Radin, Jhonathan Romero,
    Nicholas Rubin, Nicolas P. D. Sawaya, Kanav Setia, Sukin Sim, Mark Steudtner,
    Wei Sun, Fang Zhang and Ryan Babbush.
    *OpenFermion: The Electronic Structure Package for Quantum Computers*.
    `arXiv:1710.07629 <https://arxiv.org/abs/1710.07629>`__. 2017.

as well as

    Damian S. Steiger, Thomas Häner and Matthias Troyer.
    *ProjectQ: An Open Source Software Framework for Quantum Computing*.
    `arXiv:1612.08091 <https://arxiv.org/abs/1612.08091>`__. 2016.

We are happy to include future contributors as authors on later OpenFermion releases.

Disclaimer
==========

Copyright 2017 The OpenFermion Developers.
This is not an official Google product.
