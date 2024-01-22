cd ~/Code/MCB185/data
gunzip -c dictionary.gz | grep -E "^[z,o,n,r,c,i,a]{4,}$" | grep "r" 
