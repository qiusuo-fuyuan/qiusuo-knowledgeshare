The cluster ip address is actually a cluster internal IP address. This IP
address is not supposed to be exposed to outside. 

We can use type: NodePort. Then we are able to access the application using
nodeip:port => curl 192.168.49.2:31236


Question: How to dynamically update Pod image?
Answer: