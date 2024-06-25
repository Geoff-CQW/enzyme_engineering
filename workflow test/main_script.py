import os

# see #https://stackoverflow.com/questions/61843030/how-to-use-one-python-script-to-run-another-python-script-and-pass-variables-to



os.system("python rfdiff_all_atom/run_inference.py")

print('diffusion done!')

os.system("python ligand_mpnn/run_mpnn.py")

print("all done!")