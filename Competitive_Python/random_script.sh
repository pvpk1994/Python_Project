#!/bin/sh
flag=`(gcc -v) | grep -c "gcc version 6"`;
if [ $flag -gt 0 ];then
 echo "gcc version fits."
else
 isApple=`gcc -v | grep -c "Apple"`;
 if [ ${isApple} -gt 0 ];then
  ${flag}=``gcc -v | grep -c "clang version 11"``
  if [ ${flag} -gt 0 ];
  then
   echo "gcc version fits."
  else
   echo "clang 11 is not supported, will start installation now."
   #`brew install gcc`
  fi
 else
  echo "gcc version 6 is not supported, will start installation now."
 fi
fi
