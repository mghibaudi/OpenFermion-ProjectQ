=================================
OpenFermion-ProjectQ (Deprecated)
=================================

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
However, OpenFermion-ProjectQ is now archived and deprecated since it is NO LONGER MAINTAINED.
If you are interested in maintaining the package and qualified to do so, please contact us.

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

This package is deprecated and no longer accepting contributions.
However, if you are interested in maintaining the package and qualified to do so, please contact us.
We would be happy to transfer the repository to responsible owners if there is interest in continuing development.

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
`Pranav Gokhale <https://github.com/singular-value>`__ (University of Chicago),
`Thomas Häner <https://github.com/thomashaener>`__ (ETH Zurich),
`Tarini Hardikar <https://github.com/TariniHardikar>`__ (Dartmouth),
`Vojtĕch Havlíček <https://github.com/VojtaHavlicek>`__ (Oxford),
`Cupjin Huang <https://github.com/pertoX4726>`__ (University of Michigan),
`Josh Izaac <https://github.com/josh146>`__ (Xanadu),
`Zhang Jiang <https://ti.arc.nasa.gov/profile/zjiang3>`__ (NASA),
`Xinle Liu <https://github.com/sheilaliuxl>`__ (Google),
`Sam McArdle <https://github.com/sammcardle30>`__ (Oxford),
`Matthew Neeley <https://github.com/maffoo>`__ (Google),
`Thomas O'Brien <https://github.com/obriente>`__ (Leiden University),
`Isil Ozfidan <https://github.com/conta877>`__ (D-Wave Systems),
`Max Radin <https://github.com/max-radin>`__ (UC Santa Barbara),
`Jhonathan Romero <https://github.com/jromerofontalvo>`__ (Harvard),
`Nicholas Rubin <https://github.com/ncrubin>`__ (Rigetti),
`Daniel Sank <https://github.com/DanielSank>`__ (Google),
`Nicolas Sawaya <https://github.com/nicolassawaya>`__ (Harvard),
`Kanav Setia <https://github.com/kanavsetia>`__ (Dartmouth),
`Hannah Sim <https://github.com/hsim13372>`__ (Harvard),
`Mark Steudtner <https://github.com/msteudtner>`__  (Leiden University),
`Qiming Sun <https://github.com/sunqm>`__ (Caltech),
`Wei Sun <https://github.com/Spaceenter>`__ (Google),
`Daochen Wang <https://github.com/daochenw>`__ (River Lane Research),
`Chris Winkler <https://github.com/quid256>`__ (University of Chicago) and
`Fang Zhang <https://github.com/fangzh-umich>`__ (University of Michigan).

How to cite
===========
When using OpenFermion-ProjectQ for research projects, please cite:

    Jarrod R. McClean, Ian D. Kivlichan, Kevin J. Sung, Damian S. Steiger,
    Yudong Cao, Chengyu Dai, E. Schuyler Fried, Craig Gidney, Brendan Gimby,
    Pranav Gokhale, Thomas Häner, Tarini Hardikar, Vojtĕch Havlíček,
    Cupjin Huang, Josh Izaac, Zhang Jiang, Xinle Liu, Matthew Neeley,
    Thomas O'Brien, Isil Ozfidan, Maxwell D. Radin, Jhonathan Romero,
    Nicholas Rubin, Nicolas P. D. Sawaya, Kanav Setia, Sukin Sim,
    Mark Steudtner, Qiming Sun, Wei Sun, Fang Zhang and Ryan Babbush.
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
