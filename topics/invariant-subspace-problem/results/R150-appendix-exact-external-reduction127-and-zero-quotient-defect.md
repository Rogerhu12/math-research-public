# R150: the exact external divisor reduces correctly at 127 and the original quotient defect is zero

Date: 2026-11-16 (UTC)

Author: AI (ChatGPT / literature_audit)

Status: two completed exact small calculations on the original paid
polynomial data. The external degree-$120$ divisor matches the corresponding
part of the full affine characteristic polynomial at $127$. The quotient
defect is zero. In particular, the extra factor $s+64$ does not come from
that quotient defect.

## 1. Same original modules

Let $p=127$, $D=\mathbb Z_{(127)}$, $k=\mathbb F_{127}$ and $R=D[s]$.
Use the full original matrix $A:R^{6188}\to V=R^{4367}$ and set
$$
L=\operatorname{im}A,\qquad
N=V\cap\operatorname{im}_{\mathbb Q(s)}A,\qquad
C=N/L,\qquad G=V/N.
\tag{1.1}
$$
The [complete infinity qualification and Gauss proof](R150-appendix-complete-original-infinity-prime127-spectrum66-and-affine-gauss-bound299.md)
establish the original full spectrum of length $66$ at this prime.
They give a monic full affine gcd $\Delta_A\in D[s]$ with
degree-preserving reduction, and
$$
\overline{\Delta_A}\mid\Delta_{127,\mathrm{aff}}.
\tag{1.2}
$$

For completeness, $C$ is finite over $D$. The same infinity equality
provides an original maximal minor with a $p$-unit leading
coefficient. Its Cramer identity annihilates every original generic
image class in $C$. After division by its unit leading coefficient,
this is a monic parameter annihilator. Since $C$ is finitely
generated over $R$, it is finite over $D$. Moreover,
$$
\operatorname{rank}_D C=\deg\Delta_A,
\tag{1.3}
$$
because extending coefficients to $\mathbb Q$ identifies $C_{\mathbb Q}$
with the parameter-torsion part of the original rational cokernel.

The [full affine computation](R150-appendix-complete-original-f127-torsion299-and-full-parameter-action.md)
has complete torsion dimension $299$, with characteristic polynomial
$$
\Delta_{127,\mathrm{aff}}
=s^{66}(s-2)^{12}(s+6)^{12}
 \widehat F_+^8\widehat F_-^8\widehat E_8^5
 (s+64)\Psi_{60}^2.
\tag{1.4}
$$
Hats denote monic reductions of the original rational factors.

## 2. Coefficientwise verification of the external divisor

The [exact original external-divisor theorem](R150-appendix-exact-original-external-divisor120-multiplier21-and-source-cost8411.md)
already proves
$$
\Omega=f_{60}^2
$$
over $\mathbb Q[s]$, with $f_{60}$ monic and squarefree. This equality
comes from the complete original $56$-row presentation, not just
three selected determinants.

The new [read-only reduction audit](../notes/r150-source-kernel-session-789f/43756208221-paid-outside-divisor-reduction127-audit-60.json)
reads the exact original upper polynomial and the completed
whole-$56$ equality receipt. It checks all $121$ coefficients of
$\Omega$ and all $61$ coefficients of $f_{60}$, including every
denominator being a $127$ unit. It checks the rational square
identity, degree-preserving monic reduction, and the reduced square
identity. Finally it compares all $121$ reduced coefficients with
the independently computed exterior factor of (1.4).

The actual result is
$$
\boxed{\overline{f_{60}}=\Psi_{60},\qquad
       \overline\Omega=\Psi_{60}^2.}
\tag{2.1}
$$
The reduced $f_{60}$ is squarefree. Its seven irreducible factors
have degrees
$$
1,1,1,1,5,9,42.
$$
The four linear factors are $s+8,s+68,s+73,s+81$. Thus $s+64$
is not a factor of $\overline\Omega$.

The entire reduced $\Omega$ coefficient list has SHA256
3cde54d358e0ca9ff6bb1676c20ed7dec7e5b49221dd2acfed9d7faba789fd72.
The reduced square-root list has SHA256
fde7b85dd4e307abd4c4a1b43cedfad5e1e7c5e81afa2555ff3d36f8c5312c49.

This audit does not rerun the determinant calculations, the global
row module, or the full $56$-row certificate.

## 3. The complete original thirteen-kernel presentation at 127

The saved original polynomial matrix $Q$ has size $155\times13$.
The [original thirteen-kernel presentation theorem](R150-appendix-coefficient-prime-quotient-defect-from-original-thirteen-free-kernels.md)
identifies
$$
G\cong\operatorname{im}Q^T,\qquad H=\operatorname{coker}Q^T.
\tag{3.1}
$$
The coordinate projection from the original output module is a
surjection. In the present computation its two fixed coordinate
determinants are $127$ units, reducing to $90$ and $112$.
All $6069$ rational coefficients of all $2015$ original polynomial
entries of $Q$ have been checked to be $127$-integral.
Consequently (3.1) is an assertion over this same $D[s]$.

The [actual small consumer](../notes/r150-source-kernel-session-789f/43756208221-original-free-thirteen-quotient-defect127-120.json)
checks the full support identity, not merely thirteen free values.
Ten columns are exactly isolated axes $D_{\rm lin}^2e_i$, and the
other three columns vanish on these ten coordinates. Therefore
$$
H\cong (R/(D_{\rm lin}^2))^{10}\oplus H_3.
\tag{3.2}
$$
The ten separated axes are $D$-free, of total rank $920$.
The complete presentation of $H_3$ has three rows and thirty
original columns.

The entire three-row maximal-minor ideal is computed by the
established $211$-expression formula. Independently over $\mathbb Q$
and $k$, the consumer incorporates every expression and verifies
all $211$ exact divisions by the final gcd. These are complete
characteristic polynomials, not upper divisors from selected
minors.

The rational result is
$$
\Delta_{H_3,\mathbb Q}
=\operatorname{mon}\!\left(
s^{40}(s-2)^{10}(s+6)^{10}
F_+^{15}F_-^{15}E_8^{10}
\right),
\qquad \deg\Delta_{H_3,\mathbb Q}=230.
\tag{3.3}
$$
The actual result at $127$ is precisely its reduction:
$$
\boxed{
\Delta_{H_3,k}
=\overline{\Delta_{H_3,\mathbb Q}}
=s^{40}(s-2)^{10}(s+6)^{10}
 \widehat F_+^{15}\widehat F_-^{15}\widehat E_8^{10}.
}
\tag{3.4}
$$

Every coefficient and every factor transport is checked. The
irreducible primary factors and their common multiplicities in
both sides of (3.4) are:

| Factor over $\mathbb F_{127}$ | Degree | Multiplicity in both polynomials |
|---|---:|---:|
| $s$ | 1 | 40 |
| $s-2$ | 1 | 10 |
| $s+6$ | 1 | 10 |
| $s^2+s+43$ | 2 | 10 |
| $s^2+91s+46$ | 2 | 10 |
| $s^3+122s^2+108s+100$ | 3 | 15 |
| $s^3+27s^2+122s+122$ | 3 | 15 |
| $s^4+45s^3+54s^2+7s+35$ | 4 | 10 |

The three factors of degrees $2,2,4$ multiply to $\widehat E_8$.
Both full $H$ characteristic degrees are $920+230=1150$.

## 4. The quotient defect is zero

Let
$$
J_{127}=\operatorname{Tor}_{k[s]}(G/pG).
$$
The exact sequence $0\to G\to R^{13}\to H\to0$ gives
$J_{127}\cong H[p]$: its kernel after reduction is $H[p]$,
which is finite over $k$, whereas the remaining image lies in the
torsion-free module $k[s]^{13}$.

Write $T_H=H[p^\infty]$ and $F_H=H/T_H$. The latter is finite free
over $D$. Thus
$$
0\longrightarrow T_H/pT_H\longrightarrow H/pH
\longrightarrow F_H/pF_H\longrightarrow0.
$$
Multiplication by $p$ on $T_H$ has kernel and cokernel with equal
classes in the Grothendieck group of finite $k[s]$-modules. This
follows by the finite $p$-filtration; no isomorphism between those
two modules is assumed. Therefore
$$
\chi_{J_{127}}
=\frac{\Delta_{H,k}}{\overline{\Delta_{H,\mathbb Q}}}
=\frac{\Delta_{H_3,k}}{\overline{\Delta_{H_3,\mathbb Q}}}
=1.
$$
A finite $k[s]$-module with degree-zero characteristic polynomial
is zero. Hence
$$
\boxed{J_{127}=0.}
\tag{4.1}
$$
In particular, the factor $s+64$ in (1.4) is not a defect of the
saturated generic-image quotient.

## 5. What is now known about the coefficient carrier

Reducing $0\to C\to V/L\to G\to0$ gives an injection of $C/pC$
because $G$ is $D$-torsion-free. The map between the free
$k[s]$-quotients is surjective and both free ranks are $13$;
it is therefore an isomorphism. The induced torsion sequence is
$$
0\longrightarrow C/pC
\longrightarrow\operatorname{Tor}_{k[s]}(\operatorname{coker}\overline A)
\longrightarrow J_{127}\longrightarrow0.
$$
Using (4.1),
$$
\boxed{
C/pC\cong\operatorname{Tor}_{k[s]}(\operatorname{coker}\overline A),
\qquad \dim_k(C/pC)=299.
}
\tag{5.1}
$$

If $t_a^{(127)}$ counts the $D/p^aD$ summands in the coefficient
torsion of $C$, then
$$
\boxed{\deg\Delta_A+\sum_{a\ge1}t_a^{(127)}=299.}
\tag{5.2}
$$
There is no independently paid positive lower bound for the sum
on the left at prime $127$. The fifteen previously proved
coefficient-torsion directions at prime $31$ cannot be subtracted
from (5.2).

The known monic divisor $K_{158}^{\mathrm{mon}}\Omega$ has degree $278$.
Here $K_{158}^{\mathrm{mon}}$ denotes the monic normalization over
$\mathbb Q[s]$ of the known degree-$158$ rational factor; its reduction
is the corresponding product of the hatted field factors.
Using (2.1), (1.2), and monic division,
$$
\frac{\Delta_A}{K_{158}^{\mathrm{mon}}\Omega}\in D[s],
\qquad
\overline{\frac{\Delta_A}{K_{158}^{\mathrm{mon}}\Omega}}
\mid \widehat F_+^2\widehat F_-^2\widehat E_8(s+64).
\tag{5.3}
$$
The right side has degree $21$.

The previously constructed outside target multiplier
$\mu=R_{\rm out}/\Omega$ is a monic rational divisor of the quotient
in (5.3). Monic factor integrality gives $\mu\in D[s]$ and
$$
\boxed{
\overline\mu\mid
\widehat F_+^2\widehat F_-^2\widehat E_8(s+64),
\qquad \deg\mu\le21.
}
\tag{5.4}
$$
This is an additional exact residue envelope. It does not locate
the characteristic-zero support of $\mu$: distinct rational
factors may coincide after reduction.

The linear residue-primary part at $s+64$ has length one in
$C/pC$. It may come from coefficient-$127$ torsion or from the
reduction of the rational parameter torsion. Its presence alone
does not choose between these alternatives, and does not identify
a rational linear factor of $\Delta_A$.

The established nine-target existence statement remains
$\mu h_*t_j\in\operatorname{im}_{\mathbb Q[s]}A$, with
$\deg(\mu h_*)\le44$ and common rational source cost $8411$.
Neither actual calculation proves $\mu=1$ or the nine $h_*$
memberships themselves.

## 6. Actual executions

Both computations ran in the existing temporary research run
$43756208221$ and used only small pinned input phases.

The external-divisor audit, step
paid-outside-divisor-reduction127-audit-60, took
$0.002748026$ seconds. Its source SHA256 is
e4ca530ceeb301f31c0744907809a1ede0c1cf7f1ced134475ab41e40348767d;
its raw receipt is $5501$ bytes with SHA256
a5d6feb9e9f2dacdde2fa18c71c62eef6d111eecd46b6bf91210ec45541563e9.
Its binding is
298f34cecbb3043da4482b70952fadf4a35616eadac40a6ed2bce97f504b9012.

The thirteen-kernel consumer, step
original-free-thirteen-quotient-defect127-120, took
$1.056657023$ seconds. Its source SHA256 is
eba857040649223034e043008d50e2d7f2f48169a8b2c392c8f58c7ee9b74dd3;
its raw receipt is $9610$ bytes with SHA256
d4c07d28db70e5c62fc693168e6a647a54ade29fe3e4999ac2221c3e0e8e2e1f.
Its binding is
bf3b119e046d7e6ffad6f7ff7b1a26a2d3c8d345e4a1f279b151cfc14732664e.

The reduced rational and the independently computed field
$H_3$ polynomial have the same SHA256
ab63ec0bcd392003c53de71fedb7562078aeb93d2bdf03137251c20ca7aa60ab.
The exact $J$ polynomial is $[1]$, with SHA256
080a9ed428559ef602668b4c00f114f1a11c3f6b02a435f0bdc154578e4d7f22.
No dimension or primary factor was supplied as an expected answer.

An independent root calculation also multiplies back all $121$ square
coefficients, all $300$ whole-characteristic coefficients, and all
$231$ coefficients of the $H_3$ characteristic polynomial. Its
[small audit](../notes/2026-11-16-r150-omega127-jzero-root-cross-audit-789f.json)
records the full degree-$21$ envelope, whose ascending-list SHA256 is
7fe313c97a1d001e2848d1f3df5d475b3d71b9c10860e93855fc3961014ae400.
