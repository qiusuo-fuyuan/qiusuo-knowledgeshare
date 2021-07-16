Overlay file system(Define the business first). Overlay file system is just about
manipulating the inodes of existing file system. To understand file system, we have to 
understand inode and dentry. 

inode: representation of a file or directory. It contains the meta data of the file or directory. For example, file name, file size. How to represent the hierarchy of structures of
inodes. 

dentry: inode is like the elements of files and directories. DEntry should be a wrapper around inodes, and it contains the operations which could traverse against the inodes.


Experiment:
mkdir lower upper workdir merged
sudo mount -t overlay -o lowerdir=`pwd`/lower,upperdir=`pwd`/upper,workdir=`pwd`/workdir none `pwd`/merged

Run the following command
cd upperdir&&touch upper.test
ls merged => you will find that there is a file in the merged folder

cd lowerdir&&touch lower.test
ls merged => you will find that there are two files in the merged folder


What you see is not really what it is. Merging folder is just showing two inodes from two different folder.