#!/bin/bash

if [ -d $1 ]; then
	echo "The directory $1 exists"
else
	echo "Creating a $1 directory"\
		&& mkdir $1\
		&& touch $1/{test_$1,$1}.py\
		&& echo "__pycache__" > $1/.gitignore\
		&& echo "Finished"
fi
