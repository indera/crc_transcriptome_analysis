"""
Goal: Implement descriptive statistics for the COAD_READ dataset

Race, Ethnicity, Stage


@authors:
    Andrei Sura <sura.andrei@gmail.com>
    Ronald Canepa
    Tianyao Huo
    Yan Gong
"""
import pandas as pd
import numpy as np  # noqa
# import pandas_profiling as pd_prof  # noqa

# from tasks import FILE_EXPR, FILE_CLIN  # noqa
FILE_EXPR = 'data/expr/COADREAD.rnaseqv2__illuminahiseq_rnaseqv2__unc_edu__Level_3__RSEM_genes_normalized__data.data.txt'  # noqa

# 817 rows
FILE_CLIN = 'data/clin/COADREAD.merged_only_clinical_clin_format.txt'

# 2549 rows
FILE_BIOSPECIMEN = 'data/clin/COADREAD.merged_only_biospecimen_clin_format.txt'

# shipment_portion.shipment_portion_bcr_aliquot_barcode


def show_clin():
    """
    Show stats...
    """
    print("Reading file: {}".format(FILE_CLIN))
    df_clin = pd.read_csv(FILE_CLIN, sep="\t")
    print("Clinical data stats:")
    print(df_clin.describe())


    print("Reading file: {}".format(FILE_BIOSPECIMEN))
    df_bio = pd.read_csv(FILE_CLIN, sep="\t")
    print("Biospecimen data stats:")
    print(df_bio.describe())

    # profile = pd_prof.ProfileReport(df)
    # profile.to_file(outputfile="clin.html")
