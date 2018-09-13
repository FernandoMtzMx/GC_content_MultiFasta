##########################################################################################

Program: GC_content_MultiFasta_v1.0.py

Version: 1.0

Copyright (C) 2018 Fernando Martinez-Ocampo

All Rights Reserved

See LICENSE file for details

Author: Fernando Martinez-Ocampo

Contact to report bugs: fernando.martinezo@uaem.mx

##########################################################################################

1. INTRODUCTION

GC_content_MultiFasta_v1.0.py is a Python script that is used to calculate
the total length (bp) and G+C content (%) of each nucleotide sequence in a
file with Fasta format. This file may contain DNA or RNA sequences.

##########################################################################################

2. PREREQUISITES

GC_content_MultiFasta_v1.0.py requires a Linux system or Mac OS and Python
(version 2 or 3) to be pre-installed on it.

##########################################################################################

3. INSTALATION

i) Download Python script.
Download the GC_content_MultiFasta.tar.gz file from the website:
https://github.com/FernandoMtzMx/GC_content_MultiFasta.tar.gz

ii) Create the bin directory. This directory is used to store the binary files.
$ cd $HOME
$ mkdir bin && cd bin

iii) Move the GC_content_MultiFasta.tar.gz file from the Downloads directory
to the bin directory.
$ mv $HOME/Downloads/GC_content_MultiFasta.tar.gz .

iv) Untar the GC_content_MultiFasta.tar.gz file.
$ tar -zxvf GC_content_MultiFasta.tar.gz

v) Delete the GC_content_MultiFasta.tar.gz file and change the execution
permissions of GC_content_MultiFasta_v1.0.py script.
$ rm -rf GC_content_MultiFasta.tar.gz
$ cd GC_content_MultiFasta
$ chmod ugo+x GC_content_MultiFasta_v1.0.py

vi) Edite or create the .bashrc file.
cd $HOME
nano .bashrc

vii) Add the following line to the end of .bashrc file:
export PATH=$PATH:$HOME/bin/GC_content_MultiFasta/

##########################################################################################

4. COMMAND LINE

$ python3 GC_content_MultiFasta_v1.0.py --input input_file.fasta --output output_file.txt

##########################################################################################

5. DETAILED OPTIONS

Usage: python3 GC_content_MultiFasta_v1.0.py [-h] [-u] --input "INPUT" --output "OUTPUT"

Optional arguments:
  -h or --help       	Show help message and exit
  -u or --usage      	Show syntax of command line and exit
  --input "INPUT"    	Request the input file in Fasta format
  --output "OUTPUT"  	Request the name of output file in text (txt) format

##########################################################################################

6. Output file


First section of the output file shows the following comment:

I removed the following nucleotides whose the letter code means that they
could be two or more nucleotides and they were not considered for the total length:
R = G or A;
Y = T or C;
K = G or T;
M = A or C;
S = G or C;
W = A or T;
B = G or T or C;
D = G or A or T;
H = A or C or T;
V = G or C or A;
N = A or G or C or T.



Second section of the output file shows the result in tabular format:

i) First column shows the name of the label of each nucleotide sequence
ii) Second column shows the total length (in base pairs - bp) of each nucleotide sequence
iii) Third column shows the G+C content (in percentage - %) of each nucleotide sequence

##########################################################################################

7. EXAMPLES

i) Example of Anaplasma marginale str. Gypsy Plains chromosome that contains nucleotides
whose the letter code means that they could be two or more nucleotides and they were not
considered for the total length:

$ python3 GC_content_MultiFasta_v1.0.py --input $HOME/bin/GC_content_MultiFasta/examples/Anaplasma_marginale_str_Gypsy_Plains_chromosome.fna --output Gypsy_Plains_output.txt



ii) Example of 34 contigs of Anaplasma marginale str. Mex-01-001-01 genome

$ python3 GC_content_MultiFasta_v1.0.py --input $HOME/bin/GC_content_MultiFasta/examples/Anaplasma_marginale_str_Mex-01-001-01_contigs.fna --output Mex-01-001-01_output.txt

##########################################################################################
