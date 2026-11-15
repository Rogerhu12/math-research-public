# R150 appendix: the original quotient defect is one-dimensional at s = 2, and the affine divisor degree is at most 299

Author: AI (ChatGPT / literature_audit), 2026-11-15 UTC.

Status: complete characteristic-zero and characteristic-31 calculations on the same paid original thirteen polynomial free kernels. The actual quotient defect has dimension one. No larger expected dimension is used.

## 1. Original modules and the exact small presentation

Put $D=\mathbb Z_{(31)}$, $p=31$, $k=\mathbb F_{31}$ and $R=D[s]$. For the original source matrix $A:R^{6188}\to V=R^{4367}$, set

$$
L=\operatorname{im}A,\qquad
N=V\cap\operatorname{im}_{\mathbb Q(s)}A,\qquad
C=N/L,\qquad G=V/N.
$$

The [finite coefficient-prime carrier](R150-appendix-finite31-defect-module315-eight-divided-columns-and-affine-degree307.md) proves that $C$ is finite over $D$, that

$$
\operatorname{rank}_D C=\deg\Delta_A,
$$

and that $C/pC$ embeds in the complete 315-dimensional torsion module of $\operatorname{coker}\overline A$. Here $\Delta_A$ is the monic full original affine determinantal divisor over $\mathbb Q[s]$.

The [original thirteen-kernel theorem](R150-appendix-coefficient-prime-quotient-defect-from-original-thirteen-free-kernels.md) identifies

$$
G\cong\operatorname{im}Q^T,\qquad
H=\operatorname{coker}Q^T,\qquad
J:=\operatorname{Tor}_{k[s]}(G/pG)\cong H[p],
\tag{1.1}
$$

where $Q$ is the saved original $155$ by $13$ polynomial kernel matrix. That theorem required every coefficient of $Q$ to be $31$-integral. The actual calculation has now verified this condition for all 6069 rational coefficients, together with all 2015 polynomial matrix entries and the full thirteen-coordinate normalization.

Ten columns are exactly isolated axes $D_{\rm lin}^2e_i$, and the other three columns vanish on those ten coordinates. Thus

$$
H\cong (R/(D_{\rm lin}^2))^{10}\oplus H_3,
$$

with the first summand $D$-free of rank $920$. The complete presentation of $H_3$ has three rows and thirty original columns. Its entire maximal-minor ideal is the 211-expression gcd of the cited theorem, computed independently over $\mathbb Q[s]$ and $k[s]$.

## 2. Both complete characteristic polynomials

Let $\operatorname{mon}(\cdot)$ denote the monic normalization of a nonzero polynomial. The complete rational calculation gives

$$
\boxed{
\Delta_{H_3,\mathbb Q}
=\operatorname{mon}\!\left(
s^{40}(s-2)^{10}(s+6)^{10}
F_+^{15}F_-^{15}E_8^{10}
\right),
\qquad \deg\Delta_{H_3,\mathbb Q}=230.
}
\tag{2.1}
$$

The rational polynomial is $31$-integral and has degree-preserving monic reduction. The original relation

$$
\overline{E_8}=5(s-1)(s-2)E_6
$$

is checked explicitly. Consequently its complete reduction is

$$
\overline{\Delta_{H_3,\mathbb Q}}
=s^{40}(s-1)^{10}(s-2)^{20}(s+6)^{10}
P_+^{15}P_-^{15}E_6^{10}.
\tag{2.2}
$$

The independent complete finite-field calculation gives

$$
\boxed{
\Delta_{H_3,k}
=s^{40}(s-1)^{10}(s-2)^{21}(s+6)^{10}
P_+^{15}P_-^{15}E_6^{10},
\qquad \deg\Delta_{H_3,k}=231.
}
\tag{2.3}
$$

All seven displayed finite-field factors were checked to be irreducible and pairwise coprime. The exact exponent table is:

| Residue factor | Degree | Reduced rational multiplicity | Actual finite-field multiplicity | Quotient multiplicity |
|---|---:|---:|---:|---:|
| $s$ | 1 | 40 | 40 | 0 |
| $s-1$ | 1 | 10 | 10 | 0 |
| $s-2$ | 1 | 20 | 21 | 1 |
| $s+6$ | 1 | 10 | 10 | 0 |
| $P_+$ | 3 | 15 | 15 | 0 |
| $P_-$ | 3 | 15 | 15 | 0 |
| $E_6$ | 6 | 10 | 10 | 0 |

The full $H$ characteristic degrees, including the ten separated $D$-free axes, are respectively $1150$ and $1151$.

Each field incorporated all 211 expressions and then verified all 211 exact divisibilities by its final gcd. In particular, (2.1) and (2.3) are complete characteristic polynomials, not upper divisors from a selected collection of original minors.

## 3. Exact determination of J

For completeness, the characteristic comparison does not assume that $H[p]$ and $H[p^\infty]/pH[p^\infty]$ are isomorphic. Write $T_H=H[p^\infty]$ and $F_H=H/T_H$. The module $F_H$ is finite free over $D$, and

$$
0\longrightarrow T_H/pT_H\longrightarrow H/pH
\longrightarrow F_H/pF_H\longrightarrow0.
$$

The kernel and cokernel of multiplication by $p$ on the finite $p$-power torsion module have the same characteristic polynomial, by the finite $p$-filtration. Hence

$$
\chi_J
=\frac{\Delta_{H,k}}{\overline{\Delta_{H,\mathbb Q}}}
=\frac{\Delta_{H_3,k}}{\overline{\Delta_{H_3,\mathbb Q}}}
=s-2.
$$

It follows that

$$
\boxed{
J\cong k[s]/(s-2),\qquad \dim_kJ=1.
}
\tag{3.1}
$$

The last isomorphism follows because the whole characteristic polynomial has degree one. There is no quotient defect at any other residue primary component.

## 4. Exact reduction of the finite carrier and the bound 299

Let $Q_{315}=\operatorname{Tor}_{k[s]}(\operatorname{coker}\overline A)$. The original exact sequence induces

$$
0\longrightarrow C/pC\longrightarrow Q_{315}
\longrightarrow J\longrightarrow0.
\tag{4.1}
$$

Here the last torsion map is surjective: the map of the equal-rank free quotients is itself surjective, hence is an isomorphism. Thus any torsion class on the right has a torsion lift. Equal generic rank alone would not justify that step.

Using (3.1) and the complete original characteristic-31 divisor,

$$
\dim_k(C/pC)=314,
$$

$$
\chi_{C/pC}
=s^{66}(s-2)^{31}(s+6)^{12}(s-1)^7
P_+^8P_-^8E_6^5Q_{60}^2.
\tag{4.2}
$$

The [completed root-$2$ coefficient spectrum through five](R150-appendix-root2-coefficient31-spectrum-through-five-and-affine-degree300.md) provides thirteen independent $p$-power torsion directions at the residue prime $s-2$, with exact successive counts

$$
(1,4,2,4,2).
$$

The two earlier directions at $s-1$ are independent of these. They give a stable fifteen-dimensional submodule in the reduction of $C[p^\infty]$, with characteristic polynomial

$$
\chi_{15}=(s-1)^2(s-2)^{13}.
$$

Write $T_C=C[p^\infty]$. Since $C/T_C$ is finite free over $D$, reduction of
$0\to T_C\to C\to C/T_C\to0$ and characteristic multiplicativity give

$$
\overline{\Delta_A}\,\chi(T_C/pT_C)=\chi_{C/pC}.
$$

The known fifteen-dimensional torsion submodule yields the exact divisibility

$$
\boxed{
\overline{\Delta_A}\,(s-1)^2(s-2)^{13}
\mid
s^{66}(s-2)^{31}(s+6)^{12}(s-1)^7
P_+^8P_-^8E_6^5Q_{60}^2.
}
\tag{4.3}
$$

Taking degrees proves

$$
\boxed{\deg\Delta_A\le314-15=299.}
\tag{4.4}
$$

Equivalently, if $t_a$ are the multiplicities of $D/p^a$ in the coefficient-prime torsion of $C$,

$$
\deg\Delta_A+\sum_{a\ge1}t_a=314,
\qquad \sum_{a\ge1}t_a\ge15.
\tag{4.5}
$$

No equality in the second inequality is asserted. The full natural infinity length is exactly 66, so the corresponding full homogeneous common-divisor degree is at most $365$.

## 5. The refined residual envelope and the two remaining root-2 possibilities

Use the true common factor

$$
K=K_{158}
=s^{66}(s-2)^{12}(s+6)^{12}F_+^6F_-^6E_8^4.
$$

After monic normalization,

$$
\overline K=
s^{66}(s-2)^{16}(s+6)^{12}(s-1)^4P_+^6P_-^6E_6^4.
$$

Let $R_A=\Delta_A/K$. The original unit-leading maximal minor and monic Gauss division put $\Delta_A$, $K$, and $R_A$ in $D[s]$. Subtracting these actual multiplicities from (4.3) proves

$$
\boxed{
\overline{R_A}\mid
(s-1)(s-2)^2P_+^2P_-^2E_6Q_{60}^2,
\qquad
\deg R_A\le141.
}
\tag{5.1}
$$

The right side has degree $1+2+6+6+6+120=141$. This is an envelope for the entire monic rational residual after reduction, with all residue collisions retained.

In the notation of the completed root-$2$ carrier, let $f_2$ be the $D$-free rank of that Hensel component, let

$$
u=f_2-16,\qquad
v=\sum_{a\ge6}m_a(2).
$$

The already proved exact three-term budget was $u+v+\dim J_2=3$. By (3.1),

$$
\boxed{u+v=2,\qquad u,v\ge0.}
\tag{5.2}
$$

Thus the remaining two dimensions split between additional rational parameter length and coefficient-$p$ directions of order at least six. This does not prove either term zero. In particular, $f_2$ counts the complete residue component after all rational-to-residue collisions; it is not merely the rational local length at the single point $s=2$.

## 6. Consequences of the separately proved external factor of degree 60

The [complete original residue-rank theorem](R150-appendix-original56-residue-rank21-external-factor60-and-source-cost8471.md) proves a monic factor $f$ of degree 60 with

$$
f\mid\Omega\mid f^2,
$$

where $\Omega$ is the exact original projection divisor outside the known critical support. This result does not require completion of the later precision-two replay.

Let $R_{\rm out}$ be the outside-critical part of $R_A$. By (5.1), $\deg R_{\rm out}\le141$. The exact original cokernel length sequence gives the common target multiplier

$$
M_{60}=R_{\rm out}/f,\qquad \deg M_{60}\le81.
$$

With $h_*=s^3F_+^2F_-^2E_8$ and the nine original square targets $t_j$,

$$
\boxed{
M_{60}h_*t_j\in\operatorname{im}_{\mathbb Q[s]}A,\qquad
\deg(M_{60}h_*)\le104.
}
\tag{6.1}
$$

The unchanged rational source descent has three bounds $8466$, $8471$, and now $252$. Thus the common original rational source cost remains $8471$. The uniform existing-congruence source bound over $D/(31^n)$ remains $8595$ with the proved factor $K_{158}f$.

Neither the factor $f$ nor (3.1) proves that $M_{60}$ is constant. The present computation does not close the nine $h_*$ global memberships, does not fix the complete coefficient-$p$ spectrum of $C$, and does not upgrade the old finite-precision certificates to exact $p^2h_0$ sources.

## 7. Actual run and complete verification

Actual run: 43756208221. Step:

    original-free-thirteen-quotient-defect-120-parent-copy

Execution source:

    e5c7e7bdeda7211d0ad538ef7731df71f8416e10

Mathematical elapsed time: 0.9774976860007882 seconds. Wall time: 1.066027122999003 seconds. Exit code 0, status completed.

The raw mathematical receipt has 8459 bytes and SHA256

    3601de023334179feb350ce884df383b5acd3991834d14dea77570c61f87ced0.

The [complete small actual receipt](../notes/r150-source-kernel-session-789f/43756208221-original-free-thirteen-quotient-defect-120-parent-copy.json) binds:

    source SHA256 7f092c2327864ed01d93095ae8f44af5bb42022f262fabbe5d5cd3801c2385b6
    semantic binding 6f140e28ed8968703af6a645fdeb537d2f12f6b8bf85f08996828268866ec949
    original Q SHA256 0094105c15f99860016767a662e27b7b60ddfb04b085f044f50bacfe694aabe6
    three-row matrix SHA256 7b36840aee02edd40665c8edbecc0e85e5303fff8f8de1d1331a29936ef7b5c4

The two complete small characteristic polynomials have canonical coefficient SHA256:

    rational: 83b3490ffd03f27b2ed0d68b9ee778a5dab7e4e737803e4eae0487fbc77cfdf7
    field31:  6f26798a1514d0b60d809272414f5022ef512c1fd19a2922fbc417a8c945abe1

The complete $J$ polynomial has SHA256

    6dae6c475add4f7851fb5eadaa1636c48751b4f51314566b28294ba9fa279ffa.

All coefficient arrays remain reproducible temporary checkpoints. The published proof uses the original source identity, exact support, both complete gcds, all primary factors, and the actual characteristic quotient. The earlier path-only failed attempt did not execute mathematics and is not used.
