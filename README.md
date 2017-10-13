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

Tianyao Huo<sup>1</sup>; Ronald Canepa<sup>2</sup>; Andrei Sura<sup>1</sup>; 
François Modave<sup>1</sup>; Yan Gong<sup>3,4</sup>

1. Department of Health Outcomes & Biomedical Informatics, College of Medicine, University of Florida, Gainesville, Florida, United States of America
2. Information Technology and Services, University of Florida, Gainesville, Florida, United States of America
3. Department of Pharmacotherapy and Translational Research and Center for Pharmacogenomics, College of Pharmacy, University of Florida, Gainesville, Florida, United States of America
4. UF Health Cancer Center, Gainesville, Florida, United States of America
