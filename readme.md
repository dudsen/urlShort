Crappy python code that will end up as a url shortener nobody should use, no unit testing, hardcoded database paths and all the things that make sysadmins cry, it exists solely because i wanted to know the inner mechanics of how an url shortener could work and writing one is a good way to teach yourself the hidden complecity of what is otherwise fairly simple stuff. 

Python and sqlite3 because anthing else would be too cool for me to handle.

In essence what you have is a db file with url to randum number mapping my code is simply using integers then trying to make pythons crc32 algoritm play nice or working in hex. i have not yet added tracking features not user auth but it is likely comming. 
