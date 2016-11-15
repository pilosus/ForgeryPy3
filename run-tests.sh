#!/usr/bin/env bash

######################################################################
#  Run nose tests with coverage                                      #
######################################################################
#                                                                    #
# Usage:                                                             #
#  $ ./run-tests.sh [--no-coverage]                                  #
#      --no-coverage: run tests without generating                   #
#                     a test coverage report.                        #
#                                                                    #
# Requirements:                                                      #
#  $ pip install -r requirements/common.txt                          #
#                                                                    #
######################################################################

if [ "$1" == "--no-coverage" ] ; then
    nosetests
else
    nosetests --with-coverage --cover-erase --cover-html --cover-html-dir=tmp/
fi
