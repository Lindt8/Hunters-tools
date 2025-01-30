# Open a pickle file or several (CLI arguments) and recompress with LZMA
import sys 
import lzma
import pickle 
fl = sys.argv[1:]
for f in fl:
    with open(f, 'rb') as h1:
        d = pickle.load(h1)
        with lzma.open(f+'.xz','wb') as h2:
            pickle.dump(d, h2, protocol=pickle.HIGHEST_PROTOCOL)