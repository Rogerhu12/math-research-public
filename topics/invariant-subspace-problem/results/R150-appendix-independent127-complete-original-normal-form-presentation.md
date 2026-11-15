# R150: complete original normal-form presentation over F127

Date: 2026-11-15 UTC.  
Author: Astra-ISP-789f / root and normal_annihilator; AI-assisted, GPT-6 Astra Pro.

Status: completed original-source normal forms. The complete parameter-module basis and affine torsion have not yet been computed by this result.

## 1. The complete original source set

Let $k=\mathbb F_{127}$. Reduce the same primitive integer seventeen equations, with all their original parameter coefficients, over $k$. The actual model checks all $4433$ coefficients against the pinned integer input and the old original dictionary. All eighteen row-normalization constants are units in $k$; thus the normalization does not change this field module.

The source set is exactly the $17$ equations multiplied by all $364$ moment monomials of degree at most three. The raw label is

$$
\operatorname{raw}(e,m)=17\operatorname{index}(m)+e+1,
\qquad 0\le e<17.
$$

The old dictionary supplied $3333$ proposed prebasis sources and a further $2195$ sources. Their sum is only $5528$. The first new-prime model correctly failed its completeness assertion before any native normal-form calculation. Its [actual failure receipt](../notes/r150-source-kernel-session-789f/43772109844-original127-original-model.json) remains part of the record.

The corrected generator enumerates all $6188$ labels and takes the exact complement of the $3333$ prebasis labels. The complement has $2855$ sources. The legacy $2195$ are checked to be a distinct subset, disjoint from the prebasis. The remaining $660$ sources are reconstructed from the original equation/multiplier dictionary. No vanishing claim about them is imported from another field.

The [actual corrected model](../notes/r150-source-kernel-session-789f/43772109844-original127-original-model-all6188.json) completed in $0.025017904$ seconds. It verifies every coefficient, label, partition and row-unit gate. Its raw receipt is $3207$ bytes with SHA256

~~~text
fcaeb3959c0851c2853239c8f9e00567c24172554bca479e01b7071530c9058f
~~~

## 2. Exact quotient presentation

The native program constructs the constant-head prebasis anew over $k$. It does not reuse any numerical elimination from $\mathbb F_{31}$. Sources are grouped by moment degree; their complete parameter-dependent lower-degree tails accompany every operation.

The actual constant pivot block has rank $3333$. Every normalization is by a nonzero scalar of $k$, and forward and same-degree backward operations preserve the full original source expression. Ordering the moment-degree blocks makes these eliminations triangular. Consequently they are invertible polynomial row and column operations, without inverting a nonconstant parameter polynomial.

After these operations the complete original matrix has the block form

$$
U A_{127} V=
\begin{pmatrix}
I_{3333}&0\\
0&P_{127}
\end{pmatrix},
\qquad
P_{127}\in k[s]^{1034\times2855}.
$$

Here the second block contains the actual normal forms of every source outside the prebasis. In particular,

$$
\operatorname{coker}A_{127}\cong\operatorname{coker}P_{127},
\qquad
\operatorname{rank}_{k(s)}A_{127}
=3333+\operatorname{rank}_{k(s)}P_{127}.
$$

This statement does not assert a value for the second rank. The nine original target vectors are transported through the same operations and retained separately. All their source labels and output records are checked.

## 3. Actual complete calculation

The [complete normal-form receipt](../notes/r150-source-kernel-session-789f/43772109844-original127-complete-normal-forms-all6188-180.json) comes from run43772109844 and execution commit dc96b799e7083a0f6863e7b1d9d8ee90d39a337d.

| Checked quantity | Actual result |
|---|---:|
| Native arithmetic and matrix time | 63.3021 seconds |
| Complete wrapper time | 68.613773982 seconds |
| Original prebasis rank | 3333 |
| Changed pivot positions relative to the old field | 243 |
| Complementary original source records | 2855 |
| Original target records | 9 |
| Exhaustive comparisons with scalar field arithmetic | 244990 |
| Same-degree unit-block products checked | 6865903 |
| Forward source operations | 801468 |
| Backward source operations | 1041956 |
| Normal-form source operations | 29606398 |
| Canonical polynomial coefficients read at completion | 27390796 |

The wrapper independently reads every source and target binary record, checks its exact original label, the component ordering, the parameter degree bound $45$, canonical field representatives, and the final EOF. All $2855$ source records are retained, including zero normal forms.

Among the $660$ restored sources, exactly $658$ have zero normal form and exactly two have nonzero normal form:

$$
\operatorname{raw}=6046,\quad6063.
$$

This is nonvanishing in the quotient by the $3333$ prebasis sources. It does not assert that these two rows are independent of the other $2195$ complementary rows or give an additional final torsion dimension. Their actual rows must both be consumed by the complete module calculation.

The new normal-form input and dictionary have SHA256 values

~~~text
input:      f29e09f075efc20cf9dbc0b78ddffc58c35d46fe26212515397938ba78e853a3
dictionary: 02fc28dd5d81b2be05ae1c2efc6220d69f97d1f09baf19b8a50997d80b9c536b
~~~

The complete normal-form binding is

~~~text
36cdc5a084df381a91838d58a8a9f8adbc255bae39e267f2956fb1170ec0a994
~~~

The raw complete receipt is $4468$ bytes, SHA256

~~~text
e77db837596bfbd988a4dc58dbb631b7ea46cdbeca331be241b82b3ba9b48cfe
~~~

The actual normal-form binary is $33009372$ bytes, SHA256

~~~text
0655289d4b14f4d5134e3fde02dc83c651f3eea7437515c55e3db52ce771aca4
~~~

The original forward/backward source DAG and complete reduction trace are identified in the same receipt. All such arrays stay in the temporary research job.

## 4. Scope and continuation

The frozen [model and normal-form inputs](../notes/2026-11-15-r150-original127-model-and-normal-forms-inputs-789f.json) specify the exact integer input, model, native arithmetic and wrapper sources. The [complete module consumer](../notes/2026-11-15-r150-original127-graded-module-gb-interface-789f.md) consumes all $2855$ sources and preserves zero relations and the original source DAG.

The module basis rank, free rank, degree profile and entire affine torsion must be computed from this new field data. No old $315$, $716$ or $820$ dimension is an acceptance assumption. The independent natural-infinity qualification must also be proved before the new affine degree can bound the characteristic-zero divisor.

This completes the original-field normal-form subproblem only. It does not prove $\mu=1$, the nine unmultiplied target memberships, the full Jacobian statement, or the ordinary Hilbert-space invariant-subspace problem.
