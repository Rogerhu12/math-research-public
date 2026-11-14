\\ Independent PARI/GP class-polynomial check for all 55 orders in R115.
\\ Run: gp -q -s 268435456 class_number_nine_polynomials.gp
\\ Each JSON-compatible line is [M,[constant,linear,...,1]].
Ds=[199,236,332,367,419,428,491,556,563,796,823,844,972,1087,1132,1187,1228,1291,1324,1423,1468,1516,1579,1996,2003,2187,2188,2572,2803,3163,3259,3292,3307,3532,3547,3628,3643,4027,4243,4348,4363,4483,4723,4987,5443,5692,6043,6427,6763,6883,7723,8563,8803,9067,10627];
for(k=1,#Ds, my(H=polclass(-Ds[k])); print([Ds[k],vector(10,i,polcoef(H,i-1))]));
quit
