# DNSEXFILL
**Summary problem : I have a PCAP file which contain many DNS capture and two logs file**
I used the strings command on the PCAP file and noticed many common website here :+1: ![image](https://hackmd.io/_uploads/BJ-m-O8Rge.png)
As I continue scrolling , I found some suspicious strings :+1: ![image](https://hackmd.io/_uploads/BJOEZdUAxg.png)


Press enter or click to view image in full size

I try filter this suspicious by command :

`tshark -r 10.10.0.53_ns_capture.pcap -Y 'dns.qry.name contains "hex.cloudflar3.com"' -T fields -e dns.qry.name | uniq`
This is result :

```
p.c7aec5d0d81ba8748acac6931e5add6c24b635181443d0b9d2.hex.cloudflar3.com
p.f8aad90d5fc7774c1e7ee451e755831cd02bfaac3204aed8a4.hex.cloudflar3.com
p.3dfec8a22cde4db4463db2c35742062a415441f526daecb59b.hex.cloudflar3.com
p.f6af1ecb8cc9827a259401e850e5e07fdc3c1137f1.hex.cloudflar3.com
f.6837abc6655c12c454abe0ca85a596e98473172829581235dd.hex.cloudflar3.com
f.95380b06bf6dd06b89118b0003ea044700a5f2c4c106c3.hex.cloudflar3.com
```
I reviewed the access file and logfile to see scan anything relative to hex that i find.

After some time, i finded keyword in the log file :+1: ![image](https://hackmd.io/_uploads/SJ0rWuURlg.png)


Press enter or click to view image in full size

Finally , i was able to encode SHA256 hash withAPP-SECREC key , divide it to an aes-key and aes-iv , and them use to decode hex values
![image](https://hackmd.io/_uploads/By8L-OL0ge.png)
![image](https://hackmd.io/_uploads/BkaIb_UAeg.png)


Flag :

`CSCV2025{DnS_Exf1ltr4ti0nnnnnnnnnnNN!!}`  