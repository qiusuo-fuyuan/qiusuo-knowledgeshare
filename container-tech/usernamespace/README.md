#####Create a new user namespace. Normally, we create all the namespace together. Fork means. unshare will fork 

unshare -Umpf

####Write the mapping into uid_map. Only the process which creates the namespace write to this file => Because we are actually creating a mapping between child-namespace to parent-namespace

echo "0 1000 1" > /proc/22704/uid_map => if we use 0 1000 2, we still fail in this case
echo "deny" > /proc/13577/setgroups  => we have to disallow setgroups, then we are able to write into the gid_map. The reason is described here
https://lwn.net/Articles/626665/

echo "0 1000 1" > /proc/20822/uid_map

echo "0 0 1\n1 1000 1" > /proc/22704/uid_map

#####print the capablities owned by the current process#####
grep Cap /proc/$BASHPID/status => these output the capablities 
capsh --decode=0000003fffffffff
