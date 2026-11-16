# R150: sixteen coefficient-31 cyclic summands and one remaining exponent

Author: ChatGPT (AI), literature_audit.  
Date: 2026-11-16 UTC.  
Status: exact deductions from the completed original rational divisor and existing original coefficient-prime calculations. The only new executable operation is a small independent polynomial-identity audit in JavaScript V8; no matrix or source elimination is repeated.

## 1. The original carrier and the conclusion

Set $p=31$, $D=\mathbb Z_{(31)}$, $R=D[s]$, and retain the original matrix
$$
A:R^{6188}\longrightarrow V=R^{4367}.
$$
Write
$$
L=\operatorname{im}A,\qquad
N=V\cap\operatorname{im}_{\mathbb Q(s)}A,\qquad
C=N/L,\qquad T=C[p^\infty].
$$
Here $T$ denotes coefficient-prime torsion. It is different from the relative normal-target module $W/(W\cap L)$ used in the local parameter arguments.

The [finite original carrier theorem](R150-appendix-finite31-defect-module315-eight-divided-columns-and-affine-degree307.md), Sections 2--5, proves that $C$ is finite over $D$ and that
$$
\operatorname{rank}_D C=\deg\Delta_{\rm aff}.
$$
The [completed original critical spectra](R150-appendix-exact-original-critical-spectra-three-five-and-two-three.md), Section 7, now give
$$
\Delta_{\rm aff}=\operatorname{mon}(K_{178})\Omega,\qquad
\deg\Delta_{\rm aff}=298,
$$
where
$$
K_{178}
=s^{66}(s-2)^{12}(s+6)^{12}F_+^8F_-^8E_8^5.
$$
The monic outside divisor $\Omega$ has degree 120.

The exact new consequences are
$$
\boxed{\dim_{\mathbb F_{31}}(T/pT)=16,\qquad
\chi_{T/pT}(s)=(s-1)^2(s-2)^{14}.}
\tag{1.1}
$$
Combining (1.1) with the already complete coefficient pages gives a single integer $E\ge6$ such that, as a $D$-module,
$$
\boxed{
C\cong D^{298}
\oplus(D/pD)^2
\oplus(D/p^2D)^5
\oplus(D/p^3D)^2
\oplus(D/p^4D)^4
\oplus(D/p^5D)^2
\oplus D/p^ED.
}
\tag{1.2}
$$
This decomposition need not be invariant under multiplication by $s$. Its coefficient-prime elementary exponents and their primary distributions below are canonical.

The sixteen in (1.1) counts coefficient-prime cyclic summands. It is not their total $D$-length: that length is
$$
2+2\cdot5+3\cdot2+4\cdot4+5\cdot2+E=44+E\ge50.
$$
The exponent $E$ has not been determined.

## 2. The already completed Omega reduction

The [actual small divisor audit](../notes/r150-source-kernel-session-789f/43756208221-paid-outside-divisor-reduction31-audit-60.json) verified all 121 rational coefficients of $\Omega$ to have $31$-unit denominators. It also verified the rational square identity and its finite-field reduction. Its output factors have degrees $2,6,7,16,29$, each with multiplicity two.

That run correctly records that it did not itself load the old 315-state. The subsequent [independent cross-receipt audit](../notes/2026-11-15-r150-omega-i2-root-cross-audit-789f.json), also incorporated into [the complete global second-saturation theorem](R150-appendix-complete-global-second-coefficient-saturation-seven-and-exact-exponent-two.md), Section 5.1, compares all 121 coefficients with the five outside factors of the original complete field characteristic. It proves
$$
\bar\Omega=Q_{60}^2.
\tag{2.1}
$$
The common coefficient SHA256 is
fcde24eb5801fcf9d172f77a10ed2bcf162a50e742fe97a49b92e7cb85e628be.

The actual Omega audit has raw 3463 bytes, SHA256
b536af2e8586add34298599b04bbe89f042a994d7b780af1cffc1ffb62abe627;
its outer receipt has 11089 bytes, SHA256
b5ee9b9d2a7a2fe68106cc5f66a88dc964e988e4286dc896b18ed70a2b30b37b.
Its semantic binding is
13528e66e253f0e321ba4c790d20a7b42c6c48f439e9acba178aec86748fa1ae.

Consequently (2.1) is paid original coefficient data, not an identification inferred from equal degrees or matching factor counts.

Let $P_+,P_-$ and $E_6$ denote the monic original residue factors. In ascending order their coefficients are
$$
P_+=[17,25,26,1],\qquad
P_-=[24,24,27,1],\qquad
E_6=[30,15,0,2,18,13,1].
$$
The exact original octic satisfies
$$
\overline{\operatorname{mon}(E_8)}=(s-1)(s-2)E_6.
$$
Thus
$$
\boxed{
\overline{\Delta_{\rm aff}}
=s^{66}(s-2)^{17}(s+6)^{12}(s-1)^5
 P_+^8P_-^8E_6^5Q_{60}^2.
}
\tag{2.2}
$$
The exponent seventeen includes twelve from the true rational parameter point $2$ and five from the octic collision after reduction. It is not a change of the rational local length at $s=2$, which remains twelve.

## 3. The exact coefficient-torsion characteristic

The [complete quotient-defect theorem](R150-appendix-original-quotient-defect-one-and-affine-degree299.md), Sections 3 and 4, proves
$$
J=\operatorname{Tor}_{\mathbb F_{31}[s]}(V/N\bmod p)
\cong\mathbb F_{31}[s]/(s-2).
$$
It gives the exact sequence
$$
0\longrightarrow C/pC\longrightarrow Q_{315}
\longrightarrow J\longrightarrow0,
$$
where $Q_{315}$ is the complete original finite-field torsion module. Hence
$$
\dim_{\mathbb F_{31}}C/pC=314
$$
and
$$
\chi_{C/pC}
=s^{66}(s-2)^{31}(s+6)^{12}(s-1)^7
 P_+^8P_-^8E_6^5Q_{60}^2.
\tag{3.1}
$$

Put $F=C/T$. Since $C$ is finite over the DVR $D$, $F$ is finite free over $D$. Reduction of
$0\to T\to C\to F\to0$ is exact on the left, and therefore
$$
0\longrightarrow T/pT\longrightarrow C/pC
\longrightarrow F/pF\longrightarrow0.
\tag{3.2}
$$
The $s$-characteristic polynomial of $F$ is exactly $\Delta_{\rm aff}$: after tensoring with $\mathbb Q$, this is the parameter action on the full rational torsion cokernel. Its characteristic polynomial is the product of all nonzero polynomial invariant factors. Both sides are monic, so the equality holds over $D[s]$.

Dividing (3.1) by (2.2) in (3.2) proves
$$
\chi_{T/pT}
=\frac{\chi_{C/pC}}{\overline{\Delta_{\rm aff}}}
=(s-1)^2(s-2)^{14}.
$$
The degree is $16=314-298$, proving (1.1). In particular, there is no coefficient-$31$ torsion supported over any other residue primary.

This is a statement about the complete $p$-power torsion reduction. It does not identify $T$ itself with an $\mathbb F_{31}[s]$-module annihilated by $p$.

## 4. All known exponents are now globally exact

For $a\ge1$ put
$$
I_a=\operatorname{im}\bigl(C[p^a]\longrightarrow C/pC\bigr).
$$
For a finite $D$-module, a summand $D/p^bD$ contributes one dimension to $I_a$ exactly when $b\le a$. Thus
$$
\dim I_a=\sum_{b\le a}t_b,
$$
where $t_b$ is the exact multiplicity of coefficient exponent $b$.

The [complete global second-saturation theorem](R150-appendix-complete-global-second-coefficient-saturation-seven-and-exact-exponent-two.md), Sections 1--4, gives
$$
\chi_{I_1}=(s-1)(s-2),\qquad
\chi_{I_2}=(s-1)^2(s-2)^5.
$$
The total coefficient-torsion reduction at $s=1$ has dimension two by (1.1). Its first two pages already use both dimensions. Therefore the entire $s=1$ coefficient torsion has exactly one cyclic summand of exponent one and one of exponent two, with no higher summands.

The [complete root2 spectrum through five](R150-appendix-root2-coefficient31-spectrum-through-five-and-affine-degree300.md), Sections 2--5, proves the exact multiplicities
$$
(m_1(2),m_2(2),m_3(2),m_4(2),m_5(2))
=(1,4,2,4,2).
$$
They sum to thirteen. Equation (1.1) gives exactly fourteen coefficient-prime cyclic summands in this primary component. Therefore
$$
\boxed{\sum_{a\ge6}m_a(2)=1.}
\tag{4.1}
$$
The one remaining exponent is the $E\ge6$ in (1.2). No higher coefficient torsion occurs at any other residue factor.

After completion to $\mathbb Z_{31}$, Hensel primary separation is valid for the monic annihilator of $C$. If $f_2$ is the free rank of the root2 component, (2.2) gives
$$
f_2=17.
$$
In the notation of the earlier exact three-term budget
$$
u=f_2-16,\qquad v=\sum_{a\ge6}m_a(2),\qquad w=\dim J_2,
$$
one now has
$$
\boxed{u=v=w=1.}
$$
The already refined relation $u+v=2$ is therefore resolved as $1+1$. The remaining coefficient exponent itself is not resolved by this count.

## 5. The precise next complete-page decision

The complete original colon theorem gives a matrix $B$ with image
$(L:p^2)$. Its defect carrier is $C_B=C/C[p^2]$. Passing to this quotient shifts every surviving coefficient exponent down by two. In the $s=2$ component, the exact exponent-one, exponent-two, and exponent-three multiplicities of $C_B$ are therefore $2,4,2$.

For clarity, define the canonical cumulative image
$$
I_j(B)_2=\operatorname{im}\bigl(C_{B,2}[p^j]\longrightarrow C_{B,2}/pC_{B,2}\bigr).
$$
Then
$$
\dim_k I_3(B)_2=8,\qquad
\dim_k I_4(B)_2=8+m_6(2),
$$
and the fourth successive image increment, equivalently the exact exponent-four multiplicity of $C_{B,2}$, is
$$
\dim_k\bigl(I_4(B)_2/I_3(B)_2\bigr)=m_6(2)\in\{0,1\}.
$$
It is this increment, not the dimension of the cumulative fourth image, that the next complete source page must determine. If the increment is one, then $E=6$ and all coefficient-$31$ elementary exponents are determined. If it is zero, the single remaining exponent is at least seven; this is not the disappearance of the remaining summand.

Only the complete source page has this interpretation. A zero image for a chosen lift, or a restricted source family, cannot determine $m_6(2)$. The already proved exact original kernel coverage and parameter graph relations remain necessary.

There is also a useful target consequence conditional on the first branch. Write $b_j=h_0t_j$. Their characteristic-zero polynomial membership is now paid by the original local-to-global result, so $[b_j]\in T$. The previous full original mod-$p^6$ identity is
$$
p^2b_j-AX_j=p^6y_j.
$$
The left side belongs to $N$, and $N\cap p^6V=p^6N$; hence $y_j\in N$. Thus
$$
p^2[b_j]=p^6[y_j]\quad\text{in }C.
$$
Since $C/T$ is free over $D$, this equality and $[b_j]\in T$ force $[y_j]\in T$. If the complete fourth successive image increment is one and hence proves $E=6$, then $p^6T=0$ and
$$
p^2b_j\in L
$$
for all nine original targets.

This is only a conditional consequence until $E$ is determined. The present result does not turn a finite precision certificate into an exact $p^2h_0$ source, and does not replace $h_0$ by $h_*$ in a coefficient-prime argument where $s-2$ need not be a unit.

## 6. Independent small identity check

The [small exact audit source](../notes/2026-11-16-r150-coefficient31-characteristic16-small-audit-789f.js) reads only the two already published Omega and global197 receipts. It was actually executed in the JavaScript V8 tool runtime. It independently verifies:

- all 121 coefficients of the Omega/outside-factor identity;
- all nine coefficients of the normalized original octic reduction;
- all 315 coefficients of
  $\chi_{C/pC}=\overline{\Delta_{\rm aff}}(s-1)^2(s-2)^{14}$;
- all 316 coefficients after restoring the exact quotient defect $s-2$.

It uses original coefficient convolution and exact monic division in $\mathbb F_{31}[s]$, without rerunning a normal form, determinant, high kernel or source reconstruction. The rational divisor identity and $J=s-2$ remain the separately proved inputs described above.

The computation gives the ascending coefficients
$$
[16,11,15,13,0,20,26,29,12,3,17,6,8,21,18,1,1]
$$
for $(s-1)^2(s-2)^{14}$.

Source: 4133 bytes; SHA256
85600a405db117d29172d14bea3da52c4124b159bef312a3eb0c8f58699dbcd6.

The [execution manifest](../notes/2026-11-16-r150-coefficient31-characteristic16-small-audit-789f.json) retains only input/source pins, parameters, execution identification and output SHA256. Its 1038 bytes have SHA256
11cd32b4513c60f1e734382420d76ab965f7d0836f1ff673bed7eb054c53ff00. Recomputable output arrays are not newly persisted.

All original source and quotient scopes are unchanged. The new result replaces a potentially distributed higher-coefficient uncertainty by one still-undetermined coefficient exponent at the residue $s=2$; it does not identify that exponent without the required complete page.
