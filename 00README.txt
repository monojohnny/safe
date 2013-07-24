PROJECT:

Create a simple 'card-file' that can be used for bank cards etc: bit like the 'safeplace' program that available for the Psion 5mx back in the good old days.
The output file is saved using 'gpg' to encrypt the contents: the UI is just a convenient way of viewing, adding and deleting records.
Since we are hooking out to 'gpg' the file on disk should be pretty secure - but try and minimize holding too much (plain) data in-memory.

Create Unit Tests to test a closed-loop create/save/load/compare.
Build simple UI to allow data-entry

TBD: use the StringVars of Tkinter to hold the (sole) copy of the data- REASON: try and minimize copies of data in memory.
This means we'll need to create a simple parser (rather being able to use 'eval').

The form should look like this:

[File->Save->Quit]
Record 1 of n. Current SHA1:xxxxxxx <---- this is not really a security thing - just always to check whether data has (really) changed.*
---------------------
Name: blah
acct: 12345
pin: 1111
....etc
--------------------
<prev> <next> <new> <delete current>


* not sure if this is actually introducing a security-hole to exploited - if the sha1 is in memory (or on screen) - could that be used to derive the contents (somehow) of the file?


# Should we have a check that 'gpg' is valid ? We aren't checking it's path or it's checksum (etc) : perhaps we should.
