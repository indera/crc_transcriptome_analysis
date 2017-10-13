# Analysis of a Colorectal Cancer (CRC) Dataset

The goal of this repository is to document the analysis performed for the
Translational Bioinformatics Class at University of Florida (Spring 2017)

# Downloading the data

The following steps require python3 installed on your computer

    $ virtualenv crc -p `which python3`
    $ source ./crc/bin/activate
    $ pip install -r requirements.txt
    $ inv download_data
    $ inv extract_data
    $ inv describe_data


# Authors

* Andrei Sura
* Ronald Canepa
* Tianyao Huo
* Yan Gong
