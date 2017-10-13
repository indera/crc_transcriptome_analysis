# Analysis of a Colorectal Cancer (CRC) Dataset

The goal of this repository is to document a part of the analysis performed
for the PLOS One paper "Colorectal cancer stages transcriptome analysis"


# Downloading the data

The following steps require python3 installed on your computer.

Please clone the repository and obtain the data by executing:

    $ git clone https://github.com/indera/crc_transcriptome_analysis.git && cd crc_transcriptome_analysis
    $ virtualenv crc -p `which python3`
    $ source ./crc/bin/activate
    $ pip install -r requirements.txt
    $ inv download-data
    $ inv extract-data
    $ inv describe-data


# Authors

* Andrei Sura
* Ronald Canepa
* Tianyao Huo
* Yan Gong
