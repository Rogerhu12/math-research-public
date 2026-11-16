# R150: zero complete first coefficient-127 image on the E8-1 primary

Author: Astra-ISP-789f / normal_annihilator.  
AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-16.

## 1. Result

Let $p=127$, $k=\mathbb F_p$, and $h(s)=s^2+s+43$. For the original polynomial matrix
$$
A(s):D[s]^{6188}\longrightarrow D[s]^{4367},
\qquad D=\mathbb Z_{(127)},
$$
the complete first coefficient Bockstein has **zero image on the entire $h$-primary summand** of $\operatorname{Tor}_{k[s]}\operatorname{coker}\bar A$.

This summand has dimension 10 over $k$, with invariant factors $h^2,h^3$. Both nilpotent blocks are covered. The conclusion is not limited to an evaluation at a root of $h$ or to one chosen source family.

In the previously established integral saturation notation, the $h$-primary component of
$$
I_1^{(127)}
=\operatorname{im}\bigl(\mathcal C[p]\longrightarrow\mathcal C/p\mathcal C\bigr)
$$
is zero. This excludes an exponent-one coefficient-127 contribution at this parameter primary. It does not exclude coefficient torsion of exponent at least two, and it gives no characteristic-zero target membership or additional affine degree improvement.

The actual receipt is
[43772109844-original127-complete-generalized-E8-one-source-bockstein300.json](../notes/r150-source-kernel-session-789f/43772109844-original127-complete-generalized-E8-one-source-bockstein300.json).
The complete generalized detectors are established in
[the original E8-1 detector proof](R150-appendix-original127-complete-generalized-E8-one-detectors.md).
The integral/field quotient identification uses
[the exact external reduction and zero defect at 127](R150-appendix-exact-external-reduction127-and-zero-quotient-defect.md).

## 2. Why all global source relations suffice

For $\bar y\in\ker_{k[s]}\bar A$, choose an integer polynomial lift $y$. The first coefficient map is
$$
\beta(\bar y)=\left[\overline{A(s)y(s)/p}\right]
\in\operatorname{coker}_{k[s]}\bar A.
$$
It is independent of the lift: changing $y$ by $p z$ changes the divided product by $A z$, hence does not change its cokernel class. It is $k[s]$-linear.

The paid full source calculation uses the actual partition
$$
6188=3333+2855.
$$
The prebasis source transformations, all 2855 complement sources, and all original polynomial GB transformations are retained. Source reduction and swapping are elementary polynomial transformations. The 1021 final nonzero NF rows have distinct leading components and are polynomially independent. The 1834 saved zero endpoints consequently form a complete polynomial source-kernel basis, transported back through the original NF source transformations. They are not pointwise kernels.

The original generic ranks in characteristic zero and characteristic 127 both equal 4354. For every divided product $A y/p$, the augmented rational matrix has that same generic rank; reducing its vanishing larger minors modulo $p$ shows that its cokernel class is torsion over $k[s]$. Thus its primary part can be tested in the paid complete 299-dimensional torsion module.

It is therefore sufficient to compute the $h$-primary detector values of $\beta$ on all 1834 original polynomial zero relations, and then use the completeness of the detector restrictions.

## 3. Original-output transport and integer carry

The two paid detectors take values in
$$
L=k[\alpha,t]/(h(\alpha),t^3),\qquad s=\alpha+t.
$$
Their restrictions to the original complete $h$-primary basis have stacked rank 10 and satisfy the actual parameter-intertwining identities. In particular, their joint restriction is injective on this entire primary.

The new computation first transports those detector jets from the 1034 NF components to every original output monomial. It verifies all same-degree prebasis pivot identities and the lower-degree tails in the actual parameter. It checks all
$$
3333\cdot2\cdot2\cdot3=39996
$$
prebasis jet products and retains all 4367 output coordinates.

The complete original 17 primitive equations are then read as integer parameter polynomials. All 4433 coefficients and all 6188 source identities are rechecked. All physical-to-primitive constants are 127-units.

For the integer computation, use the unramified finite-jet quotient
$$
\widetilde L=(\mathbb Z/p^2\mathbb Z)[\alpha,t]/
(\widetilde h(\alpha),t^3),
$$
with the canonical integer lift of $h$. Every original scalar source product against each lifted detector is divisible by $p$. The computation checks all
$$
6188\cdot12=74256
$$
such coefficients. There are 24985 nonzero divided leaf coefficients; the later zero source result is not obtained by declaring the original leaves zero.

The divided values are propagated through the original integer lifts of every F/B/NF operation and every polynomial GB source operation. Multiplication by $s^e$ uses the full $(\alpha+t)^e$ action. Every GB subtraction is checked against its modulo-$p^2$ divided identity, so the result is the detector value of the genuine divided original source product.

The final products here are finite-jet evaluations. Global polynomial divisibility of each zero-source product follows from the original all-parameter characteristic-127 DAG. This computation does not claim to have materialized the large full-parameter integer source polynomials.

## 4. Complete zero image

The new scan verifies and retains:

| Original source operation | Actual complete count |
|---|---:|
| Forward prebasis operations | 801468 |
| Backward prebasis operations | 1041956 |
| NF operations, including the retained target records | 29606398 |
| Original complement sources | 2855 |
| Polynomial GB reductions | 69407428 |
| Polynomial GB swaps | 11591 |
| Original polynomial zero endpoints | 1834 |

All 69407428 GB reductions are checked on 12 detector coefficients, giving 832889136 integer divided recurrence checks. Every one of the 1834 final vectors is zero.

Let $R$ denote the stacked $12\times10$ complete primary restriction matrix, and let $V$ be the $12\times1834$ matrix of divided detector values. An actual unit row submatrix of $R$ reconstructs the original primary coordinates $U$, and the consumer checks
$$
RU=V
$$
on all 22008 entries. In this execution $V=0$. Since $R$ is injective, $U=0$ as well. Consequently the full parameter-stable image is zero, its characteristic and minimal polynomials are both 1, and the theorem follows from Section 2.

No positive endpoint was selected, so the reverse-source and positive full-product branches were not run. The receipt's “all selected positive generators verified” flag is vacuous with count zero; it is not an additional positive witness or a claim of new materialized sources.

## 5. Actual record

| Item | Actual value |
|---|---|
| Run | 43772109844 |
| Step | original127-complete-generalized-E8-one-source-bockstein300 |
| Execution source | e70f5b5406d0a2648190a81122a6de5e8afcdaf0 |
| Exit code | 0 |
| Entry elapsed, including compilation | 15.502927346999058 seconds |
| Compilation within that elapsed | 5.432326404001287 seconds |
| Native complete GB source scan | 6.42785 seconds |
| Outer wall time | 15.596754708001754 seconds |
| Raw receipt | 12201 bytes |
| Raw SHA-256 | 660068006e30746d8787530cb9a1651435b26489dce72802e0922f91a51912b4 |
| Published outer receipt | 19465 bytes |
| Outer SHA-256 | c40fc4430cacd131c2c4cabd4f9a63bd0730980208cc5f335176c5331bc5ee20 |

The source and native SHA-256 values are respectively
~~~text
ef64345c95bdb156843ce346c269ed6fc84ef6d94746848118ab201f1aba2261
61e2c2dbbbb0c07e4c936f29ab17bb74b18e453aacea7e3ff207e627f8dbdc55
~~~

The semantic binding is
~~~text
787000d206c7b80e6874745b4306f6728c1d24c808dfa36c662a879415b91593
~~~

The completed image phase is 1146 bytes, SHA-256
~~~text
32cc797a64babcabfb7c79b50b34fd4315d3b1a5e0bd434e112e747872335d37
~~~
with payload SHA-256
~~~text
97427a8d58d6d5bda4779e5ae5a06d5511bbbfc9af69d4b80a89e3493024268b
~~~

The complete zero-source phase is 777 bytes, SHA-256
~~~text
571752de10ad504c99ce98c7066b821759e4828e72219347a5f339341eba3d2c
~~~
with payload SHA-256
~~~text
3321b4daa45978cd12ca86c0b41afd01c99fc9ceefaf2f3bff46e751b4a2e575
~~~

The temporary manifest is 5686 bytes, SHA-256
~~~text
9d48c724e4ef093cc21cd5cf20097d5686610a287e5e0ad44556dbb06d8a52d8
~~~
and the final source-scan state is generation 1, 77817 bytes, SHA-256
~~~text
d363c9df88aee97f1b3a1beb284fff07b4d1203fe973c56ab1737273c3e23774
~~~

All arrays remain temporary. The complete detector parent can append other factors without changing this child's immutable selected phase or its binding. Other factors and higher coefficient pages are outside this result.
