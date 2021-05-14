###create a new pid namespace, at the same time, create a mount namespace. Otherwise, 
our original shell will lose its original /proc folder content####


unshare -fpm ##we have to add -m parameter.
echo $$ ## show the parent pid
mount -t proc proc /proc ##mount proc file system to show the pid number. 
ps ## we will see that our bash will have pid equals 1