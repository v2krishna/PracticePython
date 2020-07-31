"""
File Handling
===============
open(filename, mode="r")  --> it opens the file from specified location / path given with given mode(default read)
                             and it returns an file object which can be used for performing file operations.

Types of mode:
===============
r - read --> it opens a file on read only mode , if file is already exists, it raises an exception if file doesnot exists
w - write --> it opens a file on write mode, it creates a new file if not exists, it overrides the data if file already exists
a - append --> it opens a file on append mode, it creates a new file if not exists,  it appends the data if file already exists

sub-modes in file modes:
====================
read                            write                           append
r  -> read                      w -> write                      a  -> append
r+ -> read+write                w+ -> read+writ e               a+ -> read+append
rb -> read+binary               wb -> write+binary              ab -> append+binary
rb+ -> read+write+binary        wb+ -> read+write+binary        ab+ -> read+append+binary

If file already exits (r+ and a+) the content will be appended.
w+ -> will overwrite always


File opening ways:
==================
1) Using File Object
====================
f = open(filename, mode=r)
when we open a file using file object we've to close the file object to flush the data into file

2) Using with statement --> When we open file using with statement, the with statement will take care of closing file
====================
with open(filename, mode=r) as f:
     <file operations>

Methods of File:
====================
1) write(text): It writes string to the stream, it returns the number of character writtens
2) close(): it flush and close the IO object, this method has no effect if the file is already closed
3) detach(): it separates the underlying buffer from the TextIOBase, and return it.
             After the underlying buffer has been detached the TextIO is an unusable state.
4) flush(): it flushes the write buffer if file is opened on write mode , this method is not implemented for read only mode.
5) read(size=-1): it reads atmost n characters from stream until we've n characters or we hit EOF(control C)
                  if size is negative or omitted it reads until EOF
6) readline(size=-1) -- it reads until newline or EOF. It returns an empty string if EOF is hit immediately.
7) readlines(hint=-1) -- it returns list of lines from the stream. hint can be specified to control the number of lines read,
                         no more lines will be read, if the total size (in bytes or characters) of all lines, so far exceeds hint
8)seek(cookie,whence=0) --it change the stream position to the given byte offset.
                         The offset is interpreted relative to the position indicated by whence, the values for whence are
                                 0 --> start of the stream
                                 1 --> current stream position
                                 2 --> end of stream , off set is usually negative
                         It returns new absolute position
9)tell() -->returns current stream position
10)truncate(pos=None) --> it truncate file to size bytes, the file pointer is left unchanged, the size defaults to the current IO position as reported tell method,
                          it returns new absolute position.

===================================================
f = open('squares.txt','w')
for i in range(1,21):
    f.write(f'the square of {i} is {i*i}\n')
f.close()
===================================================
f =open('squares2.txt')
for line in f.readlines():
    print(line,end="")
===================================================
f = open('squares2.txt','a+')
# for i in range(21,31):
#     f.write(f'the square of {i} is {i*i}\n')
# f.flush()
f.seek(0)
for line in f.readlines():
    print(line,end="")
===================================================
f = open('squares2.txt', 'r+')
# for i in f.readlines():
#     print(i,end="")

f.truncate(5)
f.flush()
print(f.tell())
for i in f.readlines():
    print(i,end="")
===================================================
Object serizalization
pickle python object serialization
===================================
The pickle implements binary protocols for serializing and deserializing python object structure.
Pickling is the process where by python object hirerachy is converted into byte stream, and unpickling is the inverse
operation whereby byte stream is converted back into an object hirerachy.

methods of pickle module
========================
1) pickle.dump(py_object, file_object)
It write pickled representation of the python object to the open file object, this is equivalent to pickling.

2) pickle.load(file_object)
It reads the pickled representation of an object from the open file object and return the reconstituted  object hirerachy
specified.
This is equivalent to unpickling

3) pickle.dumps(py_object)
It returns the pickled representation of the object as a bytes object, instead of writing to a file.

3) pickle.loads(byte_object)
It returns the reconstituted the object hirerachy of the pickled representation data of an object, data must be a bytes like object

f = open('squares.txt', 'w')

for i in range(1,201):
    f.write(f'the square of {i} is {i*i}\n')
f.close()
==============================================================

"""
try:
    f = open('squares3.txt','r')
except FileNotFoundError  as f1:
    print(f1)