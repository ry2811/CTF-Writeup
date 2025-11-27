# Solution : 
Firstly, I used Gobuster to enumerate subdomains and directories. During the scan, I discovered an interesting endpoint:
/image.

When accessing this endpoint, I noticed that the server allowed user input to be appended directly to the file path:

<img width="1672" height="458" alt="image" src="https://github.com/user-attachments/assets/974bcda3-e0a7-4900-b2c2-c9e572507f2f" />


This suggested the possibility of path traversal injection.
I began testing with common traversal payloads such as:

` ../
../../
....//
../../../ `


and quickly confirmed that the parameter was vulnerable.
The server responded by returning files outside the intended directory, proving successful path traversal exploitation:

<img width="1673" height="484" alt="image" src="https://github.com/user-attachments/assets/0a52c758-e858-4122-842a-2945c08c424d" />
