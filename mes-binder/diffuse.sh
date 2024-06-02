#!/bin/sh

python run_inference.py inference.deterministic=True diffuser.T=200 inference.output_prefix=output/ligand_protein_motif/mes_fixcap_ inference.input_pdb=input/design_1.pdb contigmap.contigs=[\'1-10,A2-43,5-50,A86-86,50-200,A172-179,5-30,A198-216,1-5,A218-225,5-50,A268-268,1-50\'] contigmap.length="150-350" inference.ligand=MES inference.num_designs=5 inference.design_startnum=0

python run_inference.py inference.deterministic=True diffuser.T=200 inference.output_prefix=output/ligand_protein_motif/mes_activesite_ inference.input_pdb=input/design_1.pdb contigmap.contigs=[\'1-10,A2-12,2-5,A14-26,2-5,A28-30,1-5,A32-45,1-5,A48-58,1-5,A60-67,1-5,A69-73,5-10,A82-85,1-5,A87-108,5-15,A120-142,1-5,A146-179,5-20,A198-201,1-5,A205-216,1-5,A218-265,10-50\'] contigmap.length="150-350" inference.ligand=MES inference.num_designs=5 inference.design_startnum=0
