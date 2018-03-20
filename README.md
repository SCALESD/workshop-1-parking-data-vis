# Workshop 1: Parking Data Visualization
This repository contains example code for working with parking meter and transaction data from City of San Diego.

## Setup

### Required Packages

The required packages are listed in the `requirements.txt` file. We recommend installing them into a [virtual environment](https://virtualenv.pypa.io/en/stable/userguide/).

### Google Maps API
Google requires an API key when requesting images from its service. The account is free and instructions on setting one up and getting an API key can be found here:

[https://developers.google.com/maps/documentation/javascript/get-api-key link](https://developers.google.com/maps/documentation/javascript/get-api-key)

Once you have your API key, update the `config.json` file with your key and then run the example scripts.

### Running the scripts
The first four scripts are run from the command line like this: `python3 workshop-1.1.py`

The final three scripts include interactions and require Bokeh to be running in the background.  Run them like this:
`bokeh serve workshop-1.5.py`



