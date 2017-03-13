"""
Goal: store shortcuts to common tasks

@authors:
    Andrei Sura <sura.andrei@gmail.com>


-- Data access
    - http://firebrowse.org/?cohort=COADREAD&download_dialog=true
    - ./firehose_get data 2016_01_28 COADREAD
    - ./firehose_get -tasks rna clinical stddata 2013_05_23 -- Retrieves: any data package with (case-insensitive) "rna" or "clinical" in its name, from the May 23, 2013 data run

-- Call R from python:
    https://sites.google.com/site/aslugsguidetopython/data-analysis/pandas/calling-r-from-python

-- DiffExp
    - https://bcbio.wordpress.com/2009/09/13/differential-expression-analysis-with-bioconductor-and-python/
    - https://github.com/chapmanb/bcbb/blob/master/stats/count_diffexp.py  # noqa

    - https://wikis.utexas.edu/display/bioiteam/Differential+gene+expression+analysis  # noqa
    - http://www.bioconductor.org/help/workflows/rnaseqGene/

-- Usage of exons
    - https://www.biostars.org/p/64541/
    - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3460195/
    - http://www.nature.com/nmeth/journal/v7/n12/full/nmeth.1528.html
"""
import os
import sys  # noqa
from invoke import task
from describer import show_clin

URL_EXPR = 'http://gdac.broadinstitute.org/runs/stddata__2016_01_28/data/COADREAD/20160128/gdac.broadinstitute.org_COADREAD.Merge_rnaseqv2__illuminahiseq_rnaseqv2__unc_edu__Level_3__RSEM_genes_normalized__data.Level_3.2016012800.0.0.tar.gz'  # noqa
URL_CLIN = 'http://gdac.broadinstitute.org/runs/stddata__2016_01_28/data/COADREAD/20160128/gdac.broadinstitute.org_COADREAD.Merge_Clinical.Level_1.2016012800.0.0.tar.gz'  # noqa

FILE_EXPR_TGZ = "data/expr.tar.gz"
FILE_CLIN_TGZ = "data/clin.tar.gz"

DIR_EXPR = 'data/expr'
DIR_CLIN = 'data/clin'


@task
def list(ctx):
    """ Show available tasks """
    ctx.run('inv -l')

@task
def prep(ctx):
    """ Install the requirements """
    ctx.run('pip install -r requirements.txt')
    print("==> Pip packages installed:")
    ctx.run('pip freeze')


@task
def download_data(ctx):
    """ Download the source files"""
    print("Downloading files: \n{}\n{}".format(URL_EXPR, URL_CLIN))

    if not os.path.isfile(FILE_EXPR_TGZ):
        ctx.run('wget {} -q -O {}'.format(URL_EXPR, FILE_EXPR_TGZ))

    if not os.path.isfile(FILE_CLIN_TGZ):
        ctx.run('wget {} -q -O {}'.format(URL_CLIN, FILE_CLIN_TGZ))

    print("See files: {}, {}".format(FILE_EXPR_TGZ, FILE_CLIN_TGZ))

@task
def extract_data(ctx):
    """ Extract the source data """
    ctx.run("tar xzf {}".format(FILE_EXPR_TGZ), warn=True)
    ctx.run("tar xzf {}".format(FILE_CLIN_TGZ), warn=True)
    ctx.run("mv gdac.broadinstitute.org_COADREAD.Merge_rnaseqv2* {}".format(DIR_EXPR))  # noqa
    ctx.run("mv gdac.broadinstitute.org_COADREAD.Merge_Clinical* {}".format(DIR_CLIN))  # noqa
    print("==> Extracted files\n")
    ctx.run('ls -alh {} {}'.format(DIR_EXPR, DIR_CLIN))


@task
def describe_data(ctx):
    """ Print statistics about the demographic data """
    show_clin()
