# sprint-005

## Background

This 'pipe' CLI acts as an inter-process server, using 'named pipes' to collect JSON packets from multiple pull commands and collate them into a single JSON packet. 

Using named pipes has the advantage (I think?) of avoiding writing to the disk (except for some initial metadata when creating the named pipe); the inter-process communication is done via system memory. (I'm hoping that by creating the named pipe (which I'm naming 'pipefile') once, and by checking to see whether it already exists before creating it, we only write to the disk once, ever, the first time that 'pipe' is run).  

Because opening a named pipe for writing will 'block' the process until a read from that named pipe is performed, we need to explicitly tell the shell to run the command in the background with a '&' at the end of the line.

Then, when the named pipe is read, the process 'unblocks'.

(Additional code can be added to the 'pipe' CLI in order to perform checks on the packets that have been read; for example, there might be a "config.JSON" file in the directory that indicates which JSON packets *ought* to have been received; if they weren't all received, the code might then choose to write to a LOG file, or write what *was* received to disk to store for later; etc.)

## Example

Use the files provided in the repo to test the code:

> cat packet1.json | ./pipe -w &

> cat packet2.json | ./pipe -w &

> cat packet3.json | ./pipe -w &

> ./pipe > combined_packet.json
