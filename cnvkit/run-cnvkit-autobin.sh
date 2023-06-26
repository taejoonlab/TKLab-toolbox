#!/bin/bash
cnvkit autobin ../dragen.bam/*bam -t ./refFlat.no_alt_fix.bed -g ./hg38_ref.access.bed --annot ./refFlat.no_alt_fix.txt 
