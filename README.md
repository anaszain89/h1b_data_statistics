# Statistics from H1B Data
This repo contains code/submission used for Insight Data Engineering (2018).


## Problem Statement

Statistics regarding immigration data trends (H1B) are available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). While there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years. 

You are asked to create a mechanism to analyze data from the past years data, specificially calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.

More details about this coding assignment can be found [here](https://github.com/InsightDataScience/h1b_statistics).

## Solution
All codes are inclued in the `src/` folder.
The output is generated in the requested format after parsing all of the sample files.

This repo only has the following dependencies (no additional external libraries)

1. re (for basic text processing)
2. sys (for io)

Class/functions implemented are included in the `src/h1b_statistic_lib.py`

#### The repo is passing the tests in the simulation [suite](http://ec2-18-210-131-67.compute-1.amazonaws.com/test-my-repo-link) 

