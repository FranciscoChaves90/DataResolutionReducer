# DataResolutionReducer

The resolution of bathymetric and topographic survey data is ever-increasing and with it, the size of the associated data-files. Such high resolution data is often unnecessary and pose obstancles to an efficient processing of the data.

The present script allows the user to reduce the resolution of a given bathymetric and topographic data set to the desired spacing.

## Input

1. Bathymetric and topographic data set in a delimited text file (any delimiter).
2. The data should be in **x y z** or **E N Z** format.

## Instructions

1. Provide all the required parameters in the "User Input" Section.
  - 'threshold'       Desired minimum distance between points / Desired resolution
  - 'inputFilename'   Name of the input file
  - 'headerLines'     Number of header lines in the input file
  - 'delimiter'       Delimiter type: comma **','** / point **'.'** / white-space (space or tab or multiple spaces) **'.'**
  - 'outputFilename'  Name of the output file
  
## Requirements

1. [Pyhton 3](https://www.python.org/downloads/)
2. [Numpy](https://scipy.org/install.html)
