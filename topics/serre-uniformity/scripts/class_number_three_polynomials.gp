\\ Independent PARI/GP recomputation of R90's class polynomials.
\\ Run: gp -q -s 268435456 class_number_three_polynomials.gp
\\ Each JSON-compatible line is [M, [constant, linear, quadratic, 1]].
Ds=[23,31,44,59,76,83,107,108,139,172,211,243,268,283,307,331,379,499,547,643,652,883,907];
for(k=1,#Ds, my(H=polclass(-Ds[k])); print([Ds[k],vector(4,i,polcoef(H,i-1))]));
quit
