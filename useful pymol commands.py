""" useful pymol commands """

### iterate selected residues or if you want, entire named molecule

iterate "sele" and name CA, print(resi, resn)

iterate "7AUY" and name CA, print(resi, resn)

# resi = residue index, resn = residue name


### select residues within distance of target

select "7auy_chain_A" near_to 15.0 of (resn FDS) # selects only residues, target is the ligand FDS

select "7auy_chain_A" within 15.0 of (resn FDS) # selects residues and target


# selects residues of distance = 12A < residues < 15A
select ("7auy_chain_A" near_to 15.0 of (resn FDS) and "7auy_chain_A" beyond 12.0 of (resn FDS))


### get sequence as fasta

print(cmd.get_fastastr('sele')


