# Complete global second coefficient-prime image from the original197 sources

Date: 2026-11-15. Author: ChatGPT (AI), literature_audit.

This note specifies a finite exact computation. It records no new numerical
rank before the corresponding complete receipt exists.

## 1. The original module and the exact global colon theorem

Put $p=31$, $D=\mathbb Z_{(31)}$, $R=D[s]$. Let
$A:R^{6188}\longrightarrow V=R^{4367}$ be the original seventeen-equation
Macaulay map with source multipliers of degree at most3. Put
$$
 L=\operatorname{im}A,\qquad
 N=(L\otimes_R\mathbb Q(s))\cap V,\qquad C=N/L.
$$
The finite $D$-module construction of $C$, and its injection modulo $p$
into the full315-dimensional torsion part of $\operatorname{coker}\bar A$,
are already proved. The original thirteen free coordinates are not discarded
before that injection is checked.

The exact global colon theorem is
[the complete197-source theorem](2026-11-14-r150-full-p2-source-envelope-by-197-unscaled-columns-789f.md).
It gives, as an equality of $D[s]$-submodules of $V$,
$$
 (L:p^2)
 =\operatorname{im}[A,b_1,\ldots,b_7,pb_8,p^2b_9,R_{2,2},\ldots,R_{2,198}].
 \tag{1}
$$
Here every displayed divided column is an actual polynomial in the original
4367 target coordinates. In particular $b_8,b_9\in N$. Their appearances
as $pb_8,p^2b_9$ therefore vanish in $C/pC$, as do the columns of $A$.
Consequently
$$
 I_2(A):=\operatorname{image}\bigl(C[p^2]\longrightarrow C/pC\bigr)
 =\mathbb F_{31}[s]\operatorname{span}
   (\bar b_1,\ldots,\bar b_7,\bar R_{2,2},\ldots,\bar R_{2,198}).
 \tag{2}
$$
The previously paid seven-dimensional submodule $U_7$ is precisely the
span of the first seven columns and is already stable under $s$.
Equation (2) concerns every primary component. A calculation only at
$s=2$, or a calculation of197 constant vectors without their $s$-span,
does not compute this module.

## 2. Choice of the global first correction

For $2\leq j\leq198$, write $\widehat K_j$ for the fixed original integer
lift of the corresponding saved mod31 source kernel. A global polynomial
first correction is any $q_j\in\mathbb F_{31}[s]^{6188}$ satisfying
$$
 \bar A q_j=\overline{A\widehat K_j/p}.
$$
With canonical integer lifts set
$$
 \widetilde K_j=\widehat K_j-p\widehat q_j,\qquad
 R_{2,j}=A\widetilde K_j/p^2.                 \tag{3}
$$
The original product is coefficientwise divisible by $p^2$; multiplication
modulo $p^3$, followed by division by $p^2$, determines the whole class
$\bar R_{2,j}$.

Changing $q_j$ does not alter (2). Indeed, the difference of two corrections
is a full polynomial mod31 source kernel. The change of $\bar R_{2,j}$,
modulo $\operatorname{im}\bar A$, lies in the original first Bockstein image.
That complete image is contained in $U_7$. Changing the integer lift of a
fixed $q_j$ changes $R_{2,j}$ by an original image column. This also explains
why complete polynomial reconstruction is sufficient: it need not reproduce
an arbitrary earlier local lift coefficient by coefficient.

The new program uses the paid unnormalized T96 $VQ$ section, rather than
normalizing its zero-output source component. The original complete NF,
quotients, remainders, forward/backward DAG, and source dictionary are all
pinned by byte identities.

## 3. Why the finite polynomial bounds retain every original coefficient

The first198 saved source kernels have weighted cost at most81. The original
T96 graph gives first corrections of cost at most
$$
 81+96=177.                                \tag{4}
$$
For an original row $m^\alpha N_i$ the source weight is
$10(|\alpha|+1)$; for $m^\alpha\Gamma_i$ it is
$10(|\alpha|+1)+5$. The $N_i$ terms are quadratic with constant
parameter coefficients, or linear with parameter degree at most10.
The $\Gamma_i$ terms are quadratic with parameter degree at most5.
Thus a source of weighted cost at most177 produces, in the output monomial
of moment degree $d$, a complete parameter polynomial of degree at most
$$
 177-10(d-1),\qquad 1\leq d\leq5.            \tag{5}
$$
There are4367 such original monomials. The product code allocates every one
of the resulting620796 coefficient positions per source column. It checks
all6188 source-row labels, the original integer row-unit transport,
every bound in (4)-(5), and divisibility of every product coefficient by961
modulo29791. It retains the complete quotient polynomial, not a Taylor jet.

For application of the old normal form to these new quotient polynomials,
the fixed3333-row F/B DAG is replayed on the original quadratic and linear
rows. Every saved elimination coefficient is checked against the current
original row, every saved scale is checked against the actual pivot, and
the final same-degree pivot block is checked to be the identity. The two
rewritten DAG files must have the exact original paid SHA256 values.
No new pivot selection, old NF computation, or Gaussian search is performed.

## 4. Packed batches and their original provenance

The197 source indices are exactly $2,\ldots,198$, each once. Six batches
contain31 active columns each. The last batch contains $K_{188},\ldots,K_{198}$
and20 identically zero padding columns. The native labels $2,\ldots,32$
are batch-local labels only. Each batch's selection matrix and original
product recipe preserve the mapping to the actual saved source kernels.

The final consumer verifies the last20 padding sources have cost $-1$
and zero full820-state residues. They are not counted among the197 columns.
Using a single31-column compilation keeps the packed arithmetic within one
32-bit word and avoids undefined shifts by32.

For each batch, the independent complete $GQ+\mathrm{remainder}$ identity
is checked in all1034 normal-form components. A nonzero remainder term
outside the paid820-state dictionary is an error. In particular, no high
free polynomial term is dropped because it is outside a local window.

## 5. Full505 free checks,315 coordinates, and the $s$-closure

Let $K:\mathbb F_{31}^{315}\longrightarrow\mathbb F_{31}^{820}$ be the
paid normalized torsion embedding, $O$ its505-row observation matrix,
and $J$ the actual315-by315 multiplication-by-$s$ matrix. For a batch
remainder matrix $V$, the program forms the candidate coordinates $D_V$
using the paid free coordinate projection and verifies
$$
 O V=0,\qquad K D_V=V.                     \tag{6}
$$
Both identities involve the complete matrices. They are not primary
projections.

Starting with the204 columns $U_7,D_{R_2}$, insert columns into an exact
field echelon basis. Then successively insert $J$ times each newly
independent basis column. At most315 columns can be inserted. When the
queue is exhausted, let $B_I$ be the resulting basis. The final gates are
$$
 [U_7,D_{R_2}]=B_I S,\qquad J B_I=B_I J_I,
 \qquad \operatorname{rank}B_I=\dim B_I.    \tag{7}
$$
Every basis insertion is retained as a source DAG: it begins with one of
the204 actual source classes or $s$ times an earlier basis element,
subtracts specified earlier basis elements, and multiplies by one field
unit. Replaying this whole DAG in all315 original coordinates must reproduce
$B_I$. Thus the forward inclusion in (2) and the reverse generation
inclusion are both certified.

It follows from (2), (6), and (7) that
$$
 \dim I_2(A)=\operatorname{ncols}B_I,\qquad
 \chi_{I_2(A)}=\det(XI-J_I).                 \tag{8}
$$
The entire characteristic polynomial is computed and factored. No expected
total rank or expected primary rank is used as a success condition.

## 6. Coefficient-prime consequences after the actual rank is known

Let $t_e$ denote the number of cyclic coefficient-prime summands $D/(31^e)$
in the finite $D$-module $C$. The structure theorem gives
$$
 \dim I_2(A)=t_1+t_2.
$$
The complete original first Bockstein image already proves $t_1=2$.
Accordingly, an actual value $r=\dim I_2(A)$ proves the exact equality
$$
 t_2=r-2.                                 \tag{9}
$$
This is an exact coefficient-prime statement; it is not a statement about
the finite precision of a chosen target lift.

The paid $s=2$ component has the successive coefficient-prime multiplicities
$(1,4,2,4,2)$ through exponent5. Its contributions above exponent2 therefore
give eight additional directions, disjoint from $I_2(A)$. The actual
quotient-defect computation gives $\dim(C/pC)=314$. Hence
$$
 \deg\Delta_{\rm aff}=\operatorname{rank}_D C
 \leq314-(r+8)=306-r.                      \tag{10}
$$
At the polynomial level, the complete torsion characteristic is divisible by
$(s-2)^9\chi_{I_2(A)}$: one factor comes from the paid quotient defect and
eight from these later $s=2$ coefficient-prime directions. The reduction
of the characteristic-zero affine divisor divides the corresponding
remaining polynomial. This may allocate the improvement among primary
supports once (8) is actually known.

The paid exact external divisor now has degree120, and the critical factor
has degree158. Combining (10) with those already proved facts would give
$$
 \deg\mu\leq28-r,\qquad \deg(\mu h_*)\leq51-r,
$$
provided the actual rank and the complete-module gates above have passed.
These are formulas to apply to the receipt; no numerical value of $r$ is
asserted in this preparation note.

## 7. Execution and preservation contract

Use the frozen source manifest and input manifest accompanying this note.
All old arrays are restored temporarily and checked against their original
byte identities. All generated arrays, partial actual products, DAG states,
and complete source-system matrices remain temporary in the same job.
Publish only source, parameters, small receipts and hashes.

A stage is completed only after its original identities and all output
identities pass. A time pause exits75 and preserves the real partial phase.
It is not a completed dependency and not a mathematical negative result.
Reusing the same source and input binding resumes actual saved stages;
nothing in this contract authorizes rerunning the old graph or discarding
a nonzero free component.
