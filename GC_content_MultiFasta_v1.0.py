#!/usr/bin/env python

# -*- coding: utf-8 -*-

##########################################################################################

# GC_content_MultiFasta_v1.0.py is a Python script that is used to calculate
# the total length (bp) and G+C content (%) of each nucleotide sequence in a
# file with Fasta format. This file may contain DNA or RNA sequences.

# GC_content_MultiFasta_v1.0.py is designed, created and maintained both at
# the Laboratorio de Estudios Ecogenomicos (LEE) of Centro de Investigacion
# en Biotecnologia (CEIB), Universidad Autonoma del Estado de Morelos (UAEM)
# in Morelos, Mexico, and at the Unidad de Anaplasmosis of Centro Nacional de
# Investigacion Disciplinaria en Parasitologia Veterinaria (CeNID-PaVet),
# Instituto Nacional de Investigaciones Forestales, Agricolas y Pecuarias (INIFAP)
# in Morelos, Mexico.

# Author: Fernando Martinez-Ocampo.

# Contact to report bugs in the GC_content_MultiFasta_v1.0.py:
# fernando.martinezo@uaem.mx

##########################################################################################

# GC_content_MultiFasta_v1.0.py
# Copyright (C) 2018 Fernando Martinez-Ocampo
# All Rights Reserved
# See LICENSE file for details

# GC_content_MultiFasta_v1.0.py is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# GC_content_MultiFasta_v1.0.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

##########################################################################################

# Import modules
from __future__ import division
import argparse
import os

# Define arguments
parser = argparse.ArgumentParser()
parser.add_argument (
	"-u", "--usage",
	help="Syntax: python3 GC_content_MultiFasta_v1.0.py --input file.fasta --output file_output.txt",
	action="store_true")
parser.add_argument (
	"--input",
	help="Input file in Fasta format that may contain DNA or RNA sequences",
	required=True)
parser.add_argument (
	"--output",
	help="Output file in text (txt) format",
	required=True)
args = parser.parse_args()

# Open input file
input_file_name = args.input
input_file = open(input_file_name)

# Create output files
tmp_file = open("tmp.fasta","a")
output_file_name = args.output
output_file = open(output_file_name,"a")
output_file.write("# I removed the following nucleotides whose the letter code means that they could be two or more nucleotides and they were not considered for the total length:" + "\n")
output_file.write("# R = G or A" + "\n")
output_file.write("# Y = T or C" + "\n")
output_file.write("# K = G or T" + "\n")
output_file.write("# M = A or C" + "\n")
output_file.write("# S = G or C" + "\n")
output_file.write("# W = A or T" + "\n")
output_file.write("# B = G or T or C" + "\n")
output_file.write("# D = G or A or T" + "\n")
output_file.write("# H = A or C or T" + "\n")
output_file.write("# V = G or C or A" + "\n")
output_file.write("# N = A or G or C or T" + "\n\n\n\n\n")
output_file.write("# Results:" + "\n\n")
output_file.write("Label" + "\t" + "Length (bp)" + "\t" + "G+C content (%)" + "\n")

# Concatenate sequences
for line in input_file:
	if line.startswith(">"):
		label_file = line.replace('>','\n>')
		tmp_file.write(label_file)
	elif line.startswith(('A','a','T','t','U','u','C','c','G','g','N','n','R','r','Y','y','K','k','M','m','S','s','W','w','B','b','D','d','H','h','V','v','-')):
		sequence_file = line.upper()
		sequence_file_edit_N = sequence_file.replace('N','')
		sequence_file_edit_R = sequence_file_edit_N.replace('R','')
		sequence_file_edit_Y = sequence_file_edit_R.replace('Y','')
		sequence_file_edit_K = sequence_file_edit_Y.replace('K','')
		sequence_file_edit_M = sequence_file_edit_K.replace('M','')
		sequence_file_edit_S = sequence_file_edit_M.replace('S','')
		sequence_file_edit_W = sequence_file_edit_S.replace('W','')
		sequence_file_edit_B = sequence_file_edit_W.replace('B','')
		sequence_file_edit_D = sequence_file_edit_B.replace('D','')
		sequence_file_edit_H = sequence_file_edit_D.replace('H','')
		sequence_file_edit_V = sequence_file_edit_H.replace('V','')
		sequence_file_edit = sequence_file_edit_V.replace('-','')
		sequence_final = sequence_file_edit.replace('\n','')
		tmp_file.write(sequence_final)

# Open and close temporary output files
tmp_file.close()
tmp_file_2 = open("tmp.fasta")

# Get total length and G+C content
for line_2 in tmp_file_2:
	if line_2.startswith(">"):
		label_file_2 = line_2.replace('\n','\t')
		output_file.write(label_file_2)
	elif line_2.startswith(('A','a','T','t','U','u','C','c','G','g','N','n','R','r','Y','y','K','k','M','m','S','s','W','w','B','b','D','d','H','h','V','v','-')):
		sequence_file_2 = line_2.replace('\n','')
		GC_content = ((sequence_file_2.count('G') + sequence_file_2.count('C')) / len(sequence_file_2)) * 100
		output_file.write(str(len(sequence_file_2)) + "\t" + str(round(GC_content,2)) + "\n")

# Close and delete files
input_file.close()
tmp_file_2.close()
os.remove("tmp.fasta")
output_file.close()
