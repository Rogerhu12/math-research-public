# R150: fourteen true divided classes and affine divisor degree at most 301

Author: Astra-ISP-789f / literature_audit.  
AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-15 UTC.  
Status: exact deduction from already completed full-source calculations. No new matrix computation.

## 1. The finite coefficient module and the conclusion

Retain the original seventeen-equation matrix $A$, all $6188$ source coordinates, and all $4367$ output coordinates. Put

$$
p=31,\qquad D=\mathbb Z_{(31)},\qquad
L=\operatorname{im}_{D[s]}A,\qquad
N=\operatorname{im}_{\mathbb Q(s)}A\cap D[s]^{4367},\qquad C=N/L.
$$

The [finite defect-module theorem](R150-appendix-finite31-defect-module315-eight-divided-columns-and-affine-degree307.md) proves that $C$ is finite over $D$ and that reduction induces an $s$-linear injection

$$
C/pC\hookrightarrow
\operatorname{Tor}_{\mathbb F_{31}[s]}\operatorname{coker}\bar A,
\qquad \dim_{\mathbb F_{31}} C/pC\le315.
\tag{1.1}
$$

Write

$$
C\cong D^f\oplus\bigoplus_{a\ge1}(D/p^aD)^{t_a}.
$$

Then

$$
f=\deg\Delta_{\mathbb Q,\mathrm{aff}},\qquad
f+\sum_a t_a\le315,\qquad
\dim\operatorname{image}(C[p^r]\to C/pC)=\sum_{a\le r}t_a.
\tag{1.2}
$$

This appendix proves the stronger bounds

$$
\boxed{\sum_{a\le4}t_a\ge13,\qquad
       \sum_{a\le5}t_a\ge14,\qquad
       \deg\Delta_{\mathbb Q,\mathrm{aff}}\le301.}
\tag{1.3}
$$

The known full infinity length is $66$, so the total homogeneous divisor degree is at most $367$.

## 2. The four second-page columns were actually globalized

The [complete saturated second-image theorem](R150-appendix-complete-saturated-second-image-four-and-kernel208.md), original blob 8b0c7c2dd2ae4fd87ca2c124de4436c8be4067e2, constructs the four original second-page classes

$$
D_{4,15001},\ D_{4,15002},\ D_{4,15003},\ D_{4,15004}.
$$

Their classes modulo $U_9$ are independent and carry the exact action $2I_4$. This was initially a local source calculation. That fact alone would not put four global polynomial classes in $C[p^4]$.

The missing global source step is separately present in the completed [original mod-$31^6$ certificate](R150-appendix-all-nine-original-mod31six-identities-cost1339.md) and its [actual audit](../notes/2026-11-15-r150-all-nine-original-mod31six-complete-actual-789f.json). Its stage named global-four-W2-and-first-correction records:

- status completed;
- all four global W2 original sources verified;
- original divisor $923521=p^4$ for each of the four columns;
- actual original source cost $953$ for each column;
- all $505$ free observations and all $315$ original quotient coordinates verified;
- an explicit $9\times4$ matrix named globalW2DifferenceInU9.

Consequently there are actual integer polynomial source columns $H_1,\ldots,H_4$ in the original $6188$ coordinates such that

$$
d_a=\frac{AH_a}{p^4}\in\mathbb Z[s]^{4367},
\qquad
[\bar d_a]-[D_{4,15000+a}]\in U_9.
\tag{2.1}
$$

A finite modular verification suffices for this exact divisibility statement: taking the verified standard integer source representatives, the original product has every coefficient divisible by $p^4$. Here $d_a$ is defined by that exact product. Its residue class is exactly the one checked in the audit.

The [same-source comparison proof](R150-appendix-third-selected-source-comparison-and-six-slot-recovery.md), blob ae2facc80868515c01855bcd44ef792816cb0e11, explains the whole-source projectors, the canonical $s$-to-$s-2$ carry, and the successive original image corrections. The final audit completes its four-column requirement. Thus (2.1) is not inferred by discarding other primary components or replacing a local source with an arbitrary global lift.

Each $d_a$ belongs to $N$ and defines a class in $C[p^4]$.

## 3. Thirteen classes of exponent at most four and a fourteenth of exponent at most five

The old genuine divided columns

$$
b_i=A\kappa_i/p^{e_i},\qquad
(e_1,\ldots,e_9)=(1,1,2,2,2,2,2,3,4)
$$

have independent field classes spanning the invariant space $U_9$. Therefore all nine belong to $C[p^4]$.

The [second-target eigenline theorem](R150-appendix-saturated-second-target-eigenline.md), blob 5e637d6a9687283701031c8b5a528801fd737261, proves in all original $315$ quotient coordinates that

$$
V_{13}=U_9+\langle D_{4,15001},D_{4,15002},
                       D_{4,15003},D_{4,15004}\rangle
$$

has dimension $13$, and

$$
\dim\bigl(V_{13}+\langle\rho_2,\ldots,\rho_{10}\rangle\bigr)=14.
\tag{3.1}
$$

It also gives the full coordinate identities

$$
[\rho_j]=c_j[\rho_2]\quad\hbox{mod }V_{13},
\qquad
(c_2,\ldots,c_{10})=(1,28,16,11,7,7,4,1,11),
\tag{3.2}
$$

with $[\rho_2]\ne0$ in that quotient.

The [thirteen-class appendix](R150-appendix-thirteen-true-divided-columns-affine-degree302-and-residual-envelope144.md) has already identified these same residual classes with true global divided sources. Explicitly, let the old original sources $X_j$ and the completed original sources $Y_j$ satisfy

$$
AX_j\equiv p^2h_0t_j\pmod{p^5},\qquad
AY_j\equiv p^2h_0t_j\pmod{p^6}.
$$

Then

$$
v_j=\frac{A(Y_j-X_j)}{p^5}\in N,\qquad
p^5[v_j]=0,\qquad [\bar v_j]=\rho_j.
\tag{3.3}
$$

There is no assumption that $Y_j-X_j$ has a prescribed earlier source initial value. The common original target proves (3.3), with the positive sign shown.

By (2.1), replacing the four local classes in (3.1) by the four actual global $d_a$ only adds columns from $U_9$. Hence

$$
b_1,\ldots,b_9,d_1,\ldots,d_4
$$

give thirteen independent classes in the image of $C[p^4]\to C/pC$, and

$$
b_1,\ldots,b_9,d_1,\ldots,d_4,v_2
\tag{3.4}
$$

give fourteen independent classes in the image of $C[p^5]\to C/pC$. Equations (1.2) now prove (1.3).

The same columns also give the finite-budget original rational-rank lower bound

$$
\operatorname{rank}_{\mathbb Q}A_B
\ge4354(B+1)-157070+14,\qquad B\ge1339.
$$

This auxiliary bound is not used as an exact rank calculation.

## 4. The exact s-characteristic factor of the fourteen-dimensional space

Let $\mathcal T_{14}$ be the field space in (3.1). It is $s$ invariant:

- $U_9$ is invariant, with characteristic polynomial $(s-1)^2(s-2)^7$.
- $V_{13}/U_9$ has the exact action $2I_4$.
- The nonzero line $\mathcal T_{14}/V_{13}$ has the exact action $2$, by (3.2) and the already verified target action.

Therefore

$$
\chi_{\mathcal T_{14}}(s)=(s-1)^2(s-2)^{12}.
\tag{4.1}
$$

This is the characteristic polynomial of the original parameter action on a known field subspace. It is not a list of exact coefficient-$p$ exponents.

Let $E$ be the coefficient-$p$ torsion submodule of $C$, and $F=C/E$. Since $F$ is finite free over $D$,

$$
0\longrightarrow E/pE\longrightarrow C/pC
\longrightarrow F/pF\longrightarrow0.
$$

Every class in (3.4) comes from $E$, so $\mathcal T_{14}\subset E/pE$. Moreover the characteristic polynomial of multiplication by $s$ on $F$ is the true monic rational affine divisor $\Delta_{\mathbb Q,\mathrm{aff}}\in D[s]$. Applying characteristic-polynomial multiplicativity to this exact sequence and to (1.1) gives

$$
\boxed{
\overline{\Delta_{\mathbb Q,\mathrm{aff}}}
(s-1)^2(s-2)^{12}\mid\Delta_{31,\mathrm{aff}}.
}
\tag{4.2}
$$

The two factors multiply; they come from different terms of the exact sequence.

The complete original field divisor is

$$
\Delta_{31,\mathrm{aff}}
=s^{66}(s-2)^{32}(s+6)^{12}(s-1)^7
P_+^8P_-^8E_6^5Q_{60}^2.
$$

For the monic known divisor $\widehat K_{158}$, put

$$
R_{\mathrm{res}}
=\Delta_{\mathbb Q,\mathrm{aff}}/\widehat K_{158}\in D[s].
$$

The established reduction $\bar E_8=5(s-1)(s-2)E_6$ and (4.2) imply

$$
\boxed{
\overline{R_{\mathrm{res}}}
\mid (s-1)(s-2)^4P_+^2P_-^2E_6Q_{60}^2.
}
\tag{4.3}
$$

The right side has degree $143$, exactly $301-158$.

## 5. Outside multiplier and the original source budget

Use the [outside projection exact sequence](R150-appendix-external-projection-divisor-removes-target-residual-and-source-cost.md). If the exact outside projection divisor is $\Omega$ and $d=\deg\Omega$, its divisibility into the outside residual gives $0\le d\le143$ and an original target multiplier $M$ with

$$
\deg M\le143-d,\qquad
\deg(Mh_*)\le166-d,\qquad h_*=h_0/(s-2).
$$

The same original selected-minor source division gives the three branches

$$
8526-d,\qquad8531-d,\qquad314-d.
$$

Thus all nine $Mh_*t_j$ have original polynomial sources of cost at most $8531-d$. No value of $\Omega$ is asserted here.

The complete first Bockstein still gives $t_1=2$ and the old seven true columns give $t_2\ge5$. The new information is the two cumulative bounds in (1.3). It does not prove $t_5\ge1$: a class constructed with a $p^5$ divisor can already belong to the reduction of a smaller-exponent summand. It also does not bound the largest coefficient-$p$ exponent or promote the finite mod-$p^6$ target certificate to an exact characteristic-zero identity.
