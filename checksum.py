
# import zlib and adler32 
import zlib 
import sys
s=b'(sys.argv[1])'

t = zlib.adler32(s) 
  
print(t) 
