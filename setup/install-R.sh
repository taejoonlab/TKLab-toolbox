#!/usr/bin/env Rscript

if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("limma")
BiocManager::install("edgeR")
BiocManager::install("tximport")

#BiocManager::install("dada2", version = "3.10")
BiocManager::install("dada2")
