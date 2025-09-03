# redis
Exercise 1: Building and Synchronizing Redis Databases

Create a single-sharded Redis Enterprise database named source-db with no password, and a memory limit of 2GB. You can learn how to create Redis Enterprise databases here
Enable "Replica Of" by creating another single-sharded Redis Enterprise database named replica-db with no password and a memory limit of 2GB. Use source-db as the source database
On the load node, populate some data into source-db using memtier-benchmark. Put the contents of the command you ran in a file named /tmp/memtier_benchmark.txt on the load server
Write a small script/program using a language of your choice (e.g. Java, Python, Ruby, Go, Scala, C#, or JavaScript) to complete the following:
Insert the values 1-100 into the Redis database on source-db.
Read and print them in reverse order from replica-db.
In your documentation, discuss alternate Redis structures you can use to solve the problem and why you chose the solution you did