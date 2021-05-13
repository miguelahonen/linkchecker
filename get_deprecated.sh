#!/bin/bash

sudo echo "*** If you are a sudoer, type a password"
echo " "
CURDIR=$(pwd)
GITDIR=/home/********/codes/Finto-data
VOCDIR=/home/********/codes/Finto-data/vocabularies/yso/ysoKehitys.rdf
LCSHFILE=./lcsh.both.nt
URIFILE=./list_of_broken_uris_new.txt
ZIP=".zip"
echo "*** The next following variables assigned"
echo "CURDIR $CURDIR"
echo "GITDIR $GITDIR"
echo "VOCDIR $VOCDIR"
echo "LCSHFILE $LCSHFILE"
echo "URIFILE $URIFILE"
echo "ZIP $ZIP"
echo " "
if test -f "$URIFILE"; then
    rm -rf $URIFILE
fi
touch $URIFILE
chmod 777 $URIFILE
echo "*** A new URIFILE created"

echo "*** Pulls the vocabularies from the GitHub"
cd $GITDIR
git pull
echo "*** The vocabularies pulled"

sleep 2

cd $CURDIR
echo "*** Back in business in $CURDIR"

wget https://lds-downloads.s3.amazonaws.com/lcsh.both.nt.zip
echo "*** The newest data fetched from the LOC"

sleep 2

echo "*** Unzipping fetched data -> $LCSHFILE$ZIP "
unzip $LCSHFILE$ZIP
sleep 1
chmod 777 $LCSHFILE
echo "*** Data unzipped"

sleep 2

echo "*** The ceremony for matching the deprecated concepts is about to begin. It will take a long time"
./get_deprecated.py $VOCDIR $LCSHFILE

echo "*** Done! Check the $URIFILE"

 
#https://id.loc.gov/download/

