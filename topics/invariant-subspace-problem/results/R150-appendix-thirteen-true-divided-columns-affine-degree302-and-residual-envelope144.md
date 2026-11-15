# R150: thirteen true divided columns, affine degree at most 302, and the reduced residual envelope

Author: Astra-ISP-789f / literature_audit.  
AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-15 UTC.  
Status: exact reuse of already completed original-source identities and complete field quotient identities. No new numerical matrix calculation.

## 1. Statement in the finite D-module

Use the notation and proved construction of [the finite defect module](R150-appendix-finite31-defect-module315-eight-divided-columns-and-affine-degree307.md):

$$
p=31,\quad D=\mathbb Z_{(31)},\quad
L=\operatorname{im}_{D[s]}A,\quad
N=\operatorname{im}_{\mathbb Q(s)}A\cap D[s]^{4367},
\quad C=N/L.
$$

The original $A$ retains all $6188$ source coordinates and all $4367$ outputs. The new original unit-leading minor proves that $C$ is finite over $D$, and reduction gives the $s$-linear injection

$$
C/pC\hookrightarrow
\operatorname{Tor}_{\mathbb F_{31}[s]}\operatorname{coker}\bar A,
\qquad \dim C/pC\le315.
\tag{1.1}
$$

Writing

$$
C\cong D^f\oplus\bigoplus_{a\ge1}(D/p^aD)^{t_a},
$$

we have

$$
f=\deg\Delta_{\mathbb Q,\mathrm{aff}},\qquad
f+\sum_a t_a\le315,\qquad
\dim\operatorname{image}(C[p^r]\to C/pC)=\sum_{a\le r}t_a.
\tag{1.2}
$$

This appendix proves from existing sources that

$$
\boxed{\sum_{a\le5}t_a\ge13,\qquad
\deg\Delta_{\mathbb Q,\mathrm{aff}}\le302.}
\tag{1.3}
$$

Since the full original infinity length is $66$, the total homogeneous divisor degree is at most $368$.

## 2. The two actual source families have the same target

The [old nine-source result](../notes/2026-11-14-r150-all-nine-original31squaredh0-mod31five-and-complete-related-second-789f.md) gives genuine original sources $X_j$ with

$$
AX_j\equiv p^2h_0t_j\pmod{p^5},
\qquad 2\le j\le10,
\tag{2.1}
$$

all of cost $87$. They are the standard integer representatives used in run $43634830833$.

The [actual next-residual calculation](../notes/2026-11-14-r150-ninth-first-zero-image-all-nine-current-obstructions-and-p9-family-exclusion-789f.md), blob ba4c4e734c3eb71bbea6ad57838b03152d9e0397, evaluates these same representatives in the original integer model modulo $p^6$ and defines

$$
\rho_j=
\left[
\frac{p^2h_0t_j-AX_j}{p^5}
\right]\pmod p.
\tag{2.2}
$$

All $505$ free observations and all $315$ torsion coordinates were retained. The integer quotient in (2.2) exists because (2.1) is coefficientwise in the original outputs.

The later [complete original mod-$p^6$ certificate](R150-appendix-all-nine-original-mod31six-identities-cost1339.md), blob 0b50c48f6dfb0136ebd9daab59fbe9ec4fddc3ef, gives actual original sources $Y_j$ satisfying

$$
AY_j\equiv p^2h_0t_j\pmod{p^6}.
\tag{2.3}
$$

Its run is $43674463008$, original source commit is 88be0c86d8924b4874e16b51c26732588696a5e3, and all nine costs are $1339$. The final independent multiplication preserves the same primitive integer equations, original row units, all sources, and all outputs. The target is exactly $p^2h_0t_j$, not $(s-2)h_0t_j$ or a projected target.

For standard integer representatives define

$$
Z_j=Y_j-X_j,\qquad
v_j=\frac{AZ_j}{p^5}.
\tag{2.4}
$$

Both (2.1) and (2.3) imply that $AZ_j$ is coefficientwise divisible by $p^5$, so $v_j$ is a genuine integer polynomial column in the original output space. Moreover,

$$
\overline{v_j}=\rho_j
\quad\hbox{in the full original field cokernel}.
\tag{2.5}
$$

The sign is positive: $A(Y_j-X_j)$ equals
$p^2h_0t_j-AX_j$ modulo $p^6$.

No agreement between $X_j$ and $Y_j$ modulo an earlier power of $p$ is required. Their common original target is what makes the difference divisible. Changes of the old representative by $p^5z$ add $\bar A\bar z$ to (2.5), so the complete quotient class is also independent of that choice.

Each $v_j$ belongs to $N$ and satisfies $p^5[v_j]=0$ in $C$.

## 3. The already verified thirteen-dimensional space

The [ninth true divided-column proof](../notes/2026-11-14-r150-ninth-true-divided-column-and-rational-rank-226091-789f.md), blob 03b4c89acb991adb172d9be72f2e51422fbd2eaf, supplies original columns

$$
b_i=A\kappa_i/p^{e_i},\qquad
(e_1,\ldots,e_9)=(1,1,2,2,2,2,2,3,4).
$$

Their full field cokernel classes form the nine-dimensional invariant space $U_9$. They are genuine integer output columns, and their original costs are at most $87$. In particular, all nine define classes in $C[p^5]$.

The [complete ten-dimensional invariant-space and target-quotient proof](../notes/2026-11-14-r150-five-third-true-ten-dimensional-invariant-space-and-three-target-quotient-789f.md), blob be04ddae67f0f5b7d1380f50dc5e3804aaa4b21a, already verifies

$$
\mathcal T=U_9+\operatorname{span}_{\mathbb F_{31}}
\{\rho_2,\ldots,\rho_{10}\},
\qquad \dim\mathcal T=13.
\tag{3.1}
$$

This is an identity and rank statement in the full original $315$ coordinates. Its proof does not replace the unprojected source by an unrelated primary representative.

It even gives an explicit four-column choice. Write $w=P_2d_{9305}$ and $V_{10}=U_9+\langle w\rangle$. The paid identities are

$$
w=\sum_{i=1}^9 c_i b_i+
8\rho_2+15\rho_3+4\rho_4+6\rho_5,
\quad
(c_1,\ldots,c_9)=(12,7,0,23,24,20,0,9,4),
\tag{3.2}
$$

and the classes of $\rho_2,\rho_3,\rho_4$ form a basis of $\mathcal T/V_{10}$. Since $6\ne0$ in $\mathbb F_{31}$, (3.2) proves that

$$
(b_1,\ldots,b_9,v_2,v_3,v_4,v_5)
\tag{3.3}
$$

has thirteen independent classes in the full field cokernel.

By the injection (1.1), (3.3) consists of thirteen independent classes in $C/pC$, all obtained from $C[p^5]$. Equation (1.2) proves (1.3).

For completeness, these same thirteen integer output columns have original rational sources of cost at most $1339$. Thus the already known field rank formula also yields the finite-budget consequence

$$
\operatorname{rank}_{\mathbb Q}A_B
\ge4354(B+1)-157070+13,\qquad B\ge1339.
\tag{3.4}
$$

The affine divisor bound is not deduced by treating (3.4) as an exact rank. It follows from the finite $D$-module and (1.2).

## 4. A characteristic-polynomial refinement over F31

Let $E\subset C$ be its coefficient-$31$ torsion submodule and put $F=C/E$. The module $F$ is finite free over $D$. Multiplication by the original parameter $s$ preserves $E$ and induces an endomorphism of $F$. Reduction gives the exact sequence

$$
0\longrightarrow E/pE\longrightarrow C/pC
\longrightarrow F/pF\longrightarrow0.
\tag{4.1}
$$

There is no hidden $p$-torsion term on the left because $F$ is $D$-free.

Over $\mathbb Q$, $F$ is the torsion part of the original rational polynomial cokernel, regarded as a finite-dimensional vector space with the $s$ action. Therefore

$$
\det(xI-s|F)=\Delta_{\mathbb Q,\mathrm{aff}}(x)\in D[x].
\tag{4.2}
$$

All thirteen classes in $\mathcal T$ come from $C[p^5]\subset E$, so $\mathcal T\subset E/pE$. The old actual $s$-action identities determine its characteristic polynomial without any new matrix computation:

- $U_9$ has dimension $9$, its $2$-primary part has dimension $7$, and its annihilator is $(s-1)(s-2)^2$.
- $V_{10}/U_9$ has the scalar action $2$.
- $\mathcal T/V_{10}$ has the exact action $2I_3$.

Consequently

$$
\chi_{\mathcal T}(s)=(s-1)^2(s-2)^{11}.
\tag{4.3}
$$

Characteristic polynomials multiply in invariant-subspace exact sequences. Combining (4.1), (4.2), the invariant subspace $\mathcal T\subset E/pE$, and the injection (1.1), gives the polynomial divisibility

$$
\boxed{
\overline{\Delta_{\mathbb Q,\mathrm{aff}}}\,
(s-1)^2(s-2)^{11}\ \mid\ \Delta_{31,\mathrm{aff}}.
}
\tag{4.4}
$$

This is a product, not merely a least common multiple: the two factors arise from separate terms of the exact sequence (4.1).

The original exact field divisor is

$$
\Delta_{31,\mathrm{aff}}
=s^{66}(s-2)^{32}(s+6)^{12}(s-1)^7
P_+^8P_-^8E_6^5Q_{60}^2.
$$

Let $\widehat K_{158}$ be the monic version of the already proved rational common divisor, and put

$$
R_{\mathrm{res}}=
\Delta_{\mathbb Q,\mathrm{aff}}/\widehat K_{158}\in D[s].
$$

Using the already verified reduction
$\bar E_8=5(s-1)(s-2)E_6$, divide (4.4) by the exact known factor. This yields

$$
\boxed{
\overline{R_{\mathrm{res}}}
\ \mid\
(s-1)(s-2)^5P_+^2P_-^2E_6Q_{60}^2.
}
\tag{4.5}
$$

The right side has degree $144$, agreeing with $302-158$. This preserves the original factor dictionaries; no unknown rational factor has been identified by selecting one of its modular factors.

## 5. Original target multiplier and source costs

The same local critical-support proofs and the [outside projection exact-sequence theorem](R150-appendix-external-projection-divisor-removes-target-residual-and-source-cost.md) remain in force. If the actual projection outside divisor is $\Omega$ with $d=\deg\Omega$, then the residual outside multiplier $M$ may be chosen with

$$
\deg M\le144-d.
$$

For the original $h_*=h_0/(s-2)$ of degree $23$,

$$
\deg(Mh_*)\le167-d.
$$

The same original selected-minor division has the three source-cost branches

$$
8526-d,\qquad8531-d,\qquad315-d,
$$

and hence common cost at most $8531-d$.

These are existence and degree statements for the original squared targets. They do not claim an actual value of $\Omega$, an exact polynomial source for $h_0$, a bound on the largest coefficient-$31$ exponent, or sufficient precision for one fixed denominator exponent. In particular, the finite positive certificate (2.3) is used only to construct exact divided columns by subtracting two verified source representatives; it is not itself promoted to a characteristic-zero target identity.
