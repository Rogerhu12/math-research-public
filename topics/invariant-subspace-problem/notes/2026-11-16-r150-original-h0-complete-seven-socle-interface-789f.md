# R150: a complete seven-dimensional test for one or two factors of 31

Author: ChatGPT (AI), literature_audit. Date: 2026-11-16.  
Status: conditional implementation contract. It requires a completed positive original fourth-page probe proving E=6; that result is not assumed to have occurred.

## 1. The exact question and its finite carrier

Let p=31, D=Z_(31), R=D[s], L=im A, and
C=(V intersect im_(Q(s)) A)/L for the same original 17 equations,
6188 source monomials and 4367 target monomials. Put b_j=h0 t_j,
j=2,...,10. Every b_j is already in the original Q[s] image.

The [sixteen-summand theorem](../results/R150-appendix-coefficient31-sixteen-cyclic-summands-and-one-remaining-exponent.md)
leaves one coefficient exponent E>=6. Under the additional completed
positive-probe hypothesis E=6, the coefficient torsion T of C is

$$
(D/p)^2\oplus(D/p^2)^5\oplus(D/p^3)^2
\oplus(D/p^4)^4\oplus(D/p^5)^2\oplus D/p^6.
$$

The quotient C/T is D-free. Consequently

$$
T\cap p^a C=p^aT.
\tag{1.1}
$$

The existing complete original identity modulo p^6 for p^2 b_j, together
with p-saturation of N=V intersect im_(Q(s)) A, gives
p^2[b_j] in p^6C. Since [b_j] is torsion and p^6T=0, this is the exact
identity p^2[b_j]=0. This uses the original h0, not h*=h0/(s-2).

The [complete one-denominator identity](2026-11-14-r150-original-h0-full-original-one31-denominator-cost87-789f.md)
provides actual integer polynomial sources Z_j with

$$
A Z_j=p b_j\pmod {p^3}.
\tag{1.2}
$$

It follows that p[b_j] belongs to the socle subspace

$$
\mathcal S=T[p]\cap p^3T,
\qquad \dim_{\mathbb F_{31}}\mathcal S=4+2+1=7.
\tag{1.3}
$$

All seven dimensions lie in the root2 primary component. The root1
coefficient summands have exponents at most two and contribute nothing
to (1.3).

The older complete mod p^2 obstruction excludes exponent zero for each
original b_j. Hence an exact zero in this complete seven-dimensional
test means minimum denominator exponent one; a nonzero value means
minimum exponent two. A failure of a selected source family is not used.

## 2. The true generators and the socle basis

Write I_a=im(C[p^a] -> C/pC). The paid true generators through exponent
five have divisor exponents

$$
(1,1,2,2,2,2,2,3,3,4,4,4,4,5,5).
\tag{2.1}
$$

They are the original U7, the genuine b8 and L3_K2, the four actual
L4 sections, and the two actual L5 sections. A positive selected L6
column supplies the last generator g16 of exponent six. Let g_i
denote these true divided outputs, with their retained original source
cochains k_i:

$$
A k_i=p^{e_i}g_i.
\tag{2.2}
$$

For local cochains, (2.2) is an identity in the faithful completed
root2 component, with the precise Taylor lengths below. It is not
claimed to be an already restored global polynomial source identity.

The implementation must verify the whole315 reductions and the
independence of these sixteen classes. It must form its source-compatible
matrices as

$$
U_{13}=\text{true13Full315},\qquad
U_{15}=[U_{13},D5_{10},D5_{11}],\qquad
U_{16}=[U_{15},D6_{\rm chosen}].
\tag{2.3}
$$

The paid array futureCompleteIncoming15Full315 begins with canonical13,
not with true13. Thus U15 must be checked to have rank15 and the same
span as that paid array. Coordinates in canonical13 must not be
directly applied to the true original k_i.

The actual seven socle vectors are

$$
p^3g_{10},\ldots,p^3g_{13},\quad
p^4g_{14},p^4g_{15},\quad p^5g_{16}.
\tag{2.4}
$$

They are a basis of S. One proof uses the filtration
T[p] intersect p^3T, T[p] intersect p^4T,
T[p] intersect p^5T, 0.
The four first vectors give the basis induced by I4/I3 in the first
quotient, the next two by I5/I4 in the second, and the last by I6/I5.
These quotients have dimensions4,2,1. This proof permits lower triangular
mixing between the actual true generators; no unspecified Smith
coordinates are used as source data.

## 3. Two field solves compute all nine exact socle coordinates

Define the genuine initial residual

$$
r_{3,j}=\frac{p b_j-AZ_j}{p^3}.
\tag{3.1}
$$

Equation (1.2) is a full integer polynomial identity modulo p^3,
so this is an actual integer output column. In C,

$$
p[b_j]=p^3[r_{3,j}],\qquad p^4[r_{3,j}]=0.
\tag{3.2}
$$

In particular its reduction lies in I4. The first step reads its full
315-coordinate class and solves the complete span identity

$$
[\bar r_3]=U_{13}a.
\tag{3.3}
$$

All nine columns are retained. The coefficients a are canonical integers
0,...,30. Solve the complete original field equation

$$
\bar A q_3=\overline{r_3-\sum_{i\le13}g_i a_i}.
\tag{3.4}
$$

Define

$$
r_4=\frac{r_3-\sum_{i\le13}g_i a_i-Aq_3}{p}.
\tag{3.5}
$$

Now r4 lies in C[p^5]. Read its full315 class, solve

$$
[\bar r_4]=U_{15}d,\qquad
\bar A q_4=\overline{r_4-\sum_{i\le15}g_i d_i},
\tag{3.6}
$$

and define

$$
r_5=\frac{r_4-\sum_{i\le15}g_i d_i-Aq_4}{p}.
\tag{3.7}
$$

The last residual is torsion and has reduction in I6. Read its full315
class and solve

$$
[\bar r_5]=U_{16}f.
\tag{3.8}
$$

No third field source solve is needed. The difference in (3.8) is in pC,
so multiplying it by p^5 gives zero by (1.1) and p^6T=0. The exact result is

$$
\boxed{
p[b_j]
=\sum_{i=10}^{13}p^3[g_i]a_{ij}
 +\sum_{i=14}^{15}p^4[g_i]d_{ij}
 +p^5[g_{16}]f_{16,j}.}
\tag{3.9}
$$

Thus the complete obstruction is the seven by nine matrix

$$
\mathcal O=
\begin{pmatrix}
a_{10,*}\\a_{11,*}\\a_{12,*}\\a_{13,*}\\
d_{14,*}\\d_{15,*}\\f_{16,*}
\end{pmatrix}\in\mathbb F_{31}^{7\times9}.
\tag{3.10}
$$

Every column is classified: zero means exact one-factor denominator,
nonzero means exact two-factor denominator. The kernel of O also
describes all constant F31 combinations of the nine p[b_j] that vanish.
Its rank is the dimension of the span of these nine socle elements.

The complete scalar span identities, rather than particular field
source choices, make this a full membership test. A different actual
q3 or q4 changes later true generator coordinates but does not change
the element represented in (3.9), and hence does not change the outcome.

## 4. Integral source formulas: no negative powers are passed to a native

Although (3.5) is convenient notation, g10,...,g13 have divisor p^4.
The implementation must not use a fictitious integer coefficient p^-1.
All computations instead use the following common-denominator identities.

From the original Z, form the actual integer source

$$
S_3=pZ+\sum_{i\le13}p^{4-e_i}k_i a_i.
$$

Then

$$
\frac{p^2b-AS_3}{p^4}
=r_3-\sum_{i\le13}g_i a_i.
\tag{4.1}
$$

After the first actual field source q3, put

$$
S_4=S_3+p^4q_3,\qquad
r_4=\frac{p^2b-AS_4}{p^5}.
\tag{4.2}
$$

Next form

$$
S'_4=S_4+\sum_{i\le15}p^{5-e_i}k_i d_i.
$$

Its original quotient (p^2b-AS'_4)/p^5 is the right side of (3.6).
After the second actual field source q4, put

$$
S_5=S'_4+p^5q_4,\qquad
r_5=\frac{p^2b-AS_5}{p^6}.
\tag{4.3}
$$

All displayed powers in source coordinates are nonnegative. Original
arithmetic modulo p^7 is sufficient for every quotient and every
required carry, including the mod p value after division by p^6.
The signs in (4.1)--(4.3) are fixed: all corrections are added to S,
and the integer residual is target minus A times S.

The native must preserve all6188 source rows and4367 output monomials,
the exact original h0 and all nine original squares t_j. It must
check every requested Taylor coefficient before division. The target
scalar is p for (3.1) and p^2 for (4.1)--(4.3). It must never silently
replace h0 by H0 or h*.

## 5. Exact finite-to-formal precision

The initial Z_j are actual polynomial sources, so r3 can be evaluated
directly to15 terms. The true thirteen generators from the completed
p7 probe have at least15 valid formal terms. The first complete
Gq=rhs solve to15 terms loses at most5 source terms, by the original
root2 Smith maximum5. It produces r4 with10 valid terms.

The two e5 true generators have at least10 valid terms. The second
complete solve to10 terms gives r5 with5 valid terms. The e6 generator
has5 valid terms, and the complete root2 torsion is detected by those
five terms. Therefore the necessary chain is only

$$
15\longrightarrow10\longrightarrow5.
$$

The source choice, not merely a projected right side, is carried at
every step. Each local solve must verify Gq=rhs in all1034 original
prequotient rows and in every requested coefficient, not merely in the
shorter valid prefix. Every integer residual is reconstructed from
the original p7 model and the full source coordinates.

The formal image hypothesis follows as in the p7 probe interface:
the residual belongs to the original characteristic-zero generic
image, reduction has the same generic rank, and the complete actual
five-term torsion class vanishes after the indicated true correction.
Finite free observations alone do not supply generic image membership.

All quotient readings keep104 local free conditions, the full315
coordinate reconstruction, and505 original global free observations
on that reconstructed state. The old primary map may represent the
root2 component in the global315 dictionary; it is not a global
polynomial-source claim.

## 6. Minimal input reuse and the new execution boundary

No extra one-denominator artifact is needed. The already restored
newOriginal.bin is the complete sixteen-column primitive source file

seven-and-current-original-primitive-source-mod923521.bin,

17260416 bytes, SHA256
0258b6690b107a3cd45d9f6ace7ddb3003bb64ff1345ab0eab7ac4d650c49f34.

Its labels are7001,...,7007,2,...,10. The last nine columns are precisely
the original Z_j used in (1.2), as recorded in
[the complete seven-relation calculation, Sections1 and3](2026-11-14-r150-seven-real-relations-complete-next-bockstein-rank-one-789f.md).
Their new p7 multiplication must recheck (1.2); the old p4 products
must not be padded to higher precision.

The implementation reuses the successful p7 probe's actual G/V25,
the seven L3 sources, six L4 sources, two L5 sources, chosen L6,
complete210 recipe, original ten input files, four true source
families, exact original model and quotient map. All parent output
hashes and validity lengths are checked before reuse. The child
binding includes its own source identity and the exact completed
parent binding. Binary-header transport must be explicit and must
preserve every payload byte.

Only the following new mathematical work is required:

1. Nine original r3 products at15 terms and a whole315 reading.
2. A complete13-basis span identity and nine first field sources.
3. Nine original r4 products at10 valid terms and a whole315 reading.
4. A complete15-basis span identity and nine second field sources.
5. Nine original r5 products at5 valid terms and a complete16-basis span.
6. The actual7 by9 matrix O and its original-generator interpretation.

Each completed stage is saved before a more expensive successor.
All arrays and source cochains remain temporary. The job publishes
only the source, parameters, run and completed-output SHA under the
current repository policy. This contract reports no new rank, no E6
result, and no minimum denominator until those actual checks complete.
