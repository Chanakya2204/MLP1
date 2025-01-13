import gzip
import shutil

# Paths for the original and compressed files
input_file = "similarity.pkl"  # Original .pkl file
output_file = "similarity.pkl.gz"  # Compressed file

# Compress the file
with open(input_file, "rb") as f_in:
    with gzip.open(output_file, "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)

print("Compression completed! The file is now smaller and stored as 'similarity.pkl.gz'.")
