# sprint-005

## Background

This 'pipe' CLI acts as an inter-process server, using 'named pipes' to collect JSON packets from multiple pull commands and collate them into a single JSON packet. 

Using named pipes has the advantage (I think?) of avoiding writing to the disk (except for some initial metadata when creating the named pipe); the inter-process communication is done via system memory. (I'm hoping that by creating the named pipe (which I'm naming 'pipefile') once, and by checking to see whether it already exists before creating it, we only write to the disk once, ever, the first time that 'pipe' is run).  

Because opening a named pipe for writing will 'block' the process until a read from that named pipe is performed, we need to explicitly tell the shell to run the command in the background with a '&' at the end of the line.

Then, when the named pipe is read, the process 'unblocks'.

Additional code can be added to the 'pipe' CLI in order to perform checks on the packets that have been read; for example, there might be a "config.JSON" file in the directory that indicates which JSON packets *ought* to have been received; if they weren't all received, the code might then choose to write to a LOG file, or write what *was* received to disk to store for later; etc.

## Example

In the following example, three JSON packets (provided as example files in the repo) are processed by the 'pipe' cli, writing them one by one into a named pipe named 'pipefile'

The files being used are:

*packet1.json*:  {"hello":3,"temp":2}

*packet2.json*:  {"soup":6, "bubbles":2}

*packet3.json*:  {"cond":2, "up":2}

Below, we 'cat' the example files and pipe them into the 'pipe' CLI; but this could just as well have been any other 'stdout' process.

> cat packet1.json | ./pipe -w pipefile&

> cat packet2.json | ./pipe -w pipefile&

> cat packet3.json | ./pipe -w pipefile&

Note that 'pipefile' is a 'named pipe' that we've created for our process.  In order to avoid excessive reads/writes to the system, it may be optimal to use the same pipefile for all processes.


Now, let's gather everything we've written to the named pipe, and put it into one combined JSON packet:

> ./pipe -r pipefile> combined_packet.json

When we examine the contents of this packet, we see:

*combined_packet.json*: {{"hello":3,"temp":2},{"cond":2, "up":2},{"soup":6, "bubbles":2}}

## Next ste