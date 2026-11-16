# W2C fixed-WVC signed-reference bridge: input and domain contract

This is a static source/interface specification. It reports no numerical run,
new bound, finite inverse, or changed original target.

Source: `topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_W2C_signed_reference_math.py`; Git `d38e283fac50c6db733a5e557491765327ba51b5`; 22165 bytes;
SHA256 `7d6bb7f9605bf55a5ee783b5ce5983c3287dfb2edd3fca197f2de5b8f675130b`.

## 1. The one original reference

The source consumes the complete WVC actual file
`notes/continuous_centre_tracefree_residual_ci/run-43891414339-1/actual-scientific-conclusion.json`,
Git `746ec1e16befe8914c64521ad087c1f1dd23ab73`, 78,627 bytes,
SHA256 `85fd5bc63c7cb558ef04ff9699f1f9be81dbd7e7b9638a2e0922818dc559cb88`.

It retains original153-parent definition chain
`6fd1cc7b7bc2fb449804263962199175763e3c2d7e4816dfa46778a4d26108ac`
and exact clipped-diagonal chain
`b19d7e319a9ea4e49909e12b1dfe71ddc23adf5a273708288b3fe6b0cc3af8d2`.
The low reference is WVC tracefree, not WCTR scalar-trace:
$$
D_j=\begin{pmatrix}a_j&c_jq^2\\c_j&-a_j\end{pmatrix},\qquad
c_j=4j\widehat\eta,\quad -c_j/32\le a_j\le c_j/16,\quad q\ge1/8.
$$
For high reference modes97..160, $a_j=0$. The original collar reference has
$\widehat\eta=0$, $D_j=0$, and physical $S=I$. The physical mean reference
is an independent scalar derivative, not a nonzero modal pair.

The exact original definition may be materialized from the already admitted
cubic/repair/current records in the new public child. No old norm, row
producer, q/rho bound, repair, or completed target is called.
The actual eta shared by $A$ and $A_c$ is a different interface: the complete
actual-minus-reference principal term remains in the residual.
Reference $\widehat\eta$ is never relabelled as a certified actual point.

The owner constructs this data-only identity after complete admission:

```json
{"kind":"complete_fixed_WVC_signed_reference_identity_v1","complete_original_WVC_file":{"role":"WVC_actual","path":"topics/visible-flex-exact-nearby/notes/continuous_centre_tracefree_residual_ci/run-43891414339-1/actual-scientific-conclusion.json","git_blob_sha":"746ec1e16befe8914c64521ad087c1f1dd23ab73","bytes":78627,"sha256":"85fd5bc63c7cb558ef04ff9699f1f9be81dbd7e7b9638a2e0922818dc559cb88"},"original_reference_chain":{"count":153,"sha256":"6fd1cc7b7bc2fb449804263962199175763e3c2d7e4816dfa46778a4d26108ac"},"selected_diagonal_chain":{"count":153,"sha256":"b19d7e319a9ea4e49909e12b1dfe71ddc23adf5a273708288b3fe6b0cc3af8d2"},"same_original_D_S_and_true_root":true,"all_original_parent_definitions_verified":true,"no_completed_bound_target_recomputed":true,"scalar_trace_identically_zero":true,"reference_outer_impedance":"13/80","fine_refinement":160,"fine_cell_count":24480,"finite_normalizer_rule":"rho2=1+h^2*(a^2+c^2*q^2)/12"}
```

These flags summarize the preceding reader's verification. The mathematical
helper does not confer qualification on arbitrary data carrying those flags.

## 2. Precise callable and true radial-domain contract

```python
profiles = prepare_signed_reference_profiles(
    api, domain, etas, qs, diagonals, parent_indices, identity,
    modes=tuple(range(1,161)))
```

Every list has the length of `domain.cells`. Parent indices are nondecreasing,
cover0..152, and map every comparison panel to the same original reference
parent. Etas, qs, and all96 diagonal entries per panel enclose the exact fixed
reference definitions. They are not samples or independent operator uppers.

The comparison partition refines reference D/S seams, collar cut, and cutoff
joins. It need not split all4650 actual coefficient rows if each complete
panel hull covers every original piece, raw transmission is identity, and
the complete4801-intersection admission remains. Independent affine jumps
and any genuine nonidentity transmission remain separate.

Domain supplies api, cells, validate_box, cell_index, cache_key,
whole_cell_box, full_length, partial_length, ordered_span.
In the declared RadialDomain a box is
`(cell, Fraction t0, Fraction t1)`, with a stable immutable
index/numerator/denominator cache key. A first edge None denotes the true
root together with its enclosure; no endpoint substitutes for that root.

Prefix and suffix lengths enclose the exact distances to the actual panel
edges. ordered_span encloses the entire conditionally ordered set, including
two boxes in one panel. These are integration enclosures, never quadrature
samples. Refining them does not alter the original finite projection,
24480 fine cells, same actual tail, physical Riesz coordinates, or193N+193
finite dimension. Any source/target Sobolev weights are separate explicit
factors of the complete ordered operator.

## 3. Exact signed profiles and zero-rate branch

On one panel put $\omega^2=a^2+c^2q^2$. For a true segment length $\ell$
and its right impedance $p_+$, use
$$
A_s=(1+e^{-2\omega\ell})/2,\quad
B_s=(1-e^{-2\omega\ell})/(2\omega),\quad
d_s=A_s+B_s(a+cp_+),
$$
$$
p_-=\frac{B_scq^2+p_+(A_s-B_sa)}{d_s},\quad
\tau=\frac{e^{-\omega\ell}}{d_s},\quad
\sigma=\frac{B_sc}{d_s},\quad
\tau^{-1}=e^{\omega\ell}d_s.
$$
The source never divides by a tiny global decay enclosure.
For $c=a=0$, the exact branch is $(p_-,\tau,\sigma,\tau^{-1})=(p_+,1,0,1)$.

The backward boundary is $p(R)=13/80$. The forward boundary is $H(r_*)=0$,
and $H_+=\tau^2H_-+\sigma$. The proved reference invariants are
$$
p\ge1/16,\quad 0\le H\le1/p,\quad K=1-pH\in[0,1],\quad
g(r)=\exp\!\left(-\int_{r_*}^r(a+cp)\,ds\right)>0.
$$
Intersections are complete interval intersections. Every min/max extracts
directed endpoints first, including the upper candidate $1/p_{\rm lower}$.

`profiles.at(j,box)` gives whole-box enclosures of these exact
$p,H,K,g,g^{-1}$ functions. It never reads old pmax/Hsup as their values.
`ordered_decay` combines whole segment transfers with an O(log n) product
tree; it does not subtract upper prefixes or divide global g enclosures.
`to_right` includes the complete interval to $R$. Reference positivity
does not imply an actual inverse.

## 4. Signed continuous Green kernel and all observations

```python
Gf = complete_signed_reference_kernel(
    api, domain, profiles, tuple(range(1,97)), profiles.qs, thetas,
    True, True, kernel_api, label="fixed_WVC_Gf")
G0 = complete_signed_reference_kernel(
    api, domain, profiles, tuple(range(97,161)),
    [api.one]*len(domain.cells), thetas, False, False, kernel_api,
    coordinates=H288, label="fixed_WVC_G0_zero_extended")
```

H288 contains both physical parities for97..288, but G0 remains active only
on97..160. This is explicit zero extension, not finite truncation of the
actual infinite high inverse. Centre224, intermediate288, and full-family
error416 retain their separate supports and complete error legs.

For $F=(-p,1)^t$, $U=(K,H)^t$, $L=(1,p)$ and $J=(-H,K)$,
$$
G_D(r,s)=
\begin{cases}
S(r)F(r)\,[g(r)/g(s)]J(s),&s<r,\\
-S(r)U(r)\,[g(s)/g(r)]L(s),&r<s.
\end{cases}
$$
Here $S=\operatorname{diag}(1,q)$ for low and $I$ for high.
Factor fields and the ordered-decay direct evaluator enclose this same exact
kernel. All nonmean coordinates are normalized real sine/cosine with
frequency4j; the mean basis is1.

Low output atoms are root odd1..96, root mean, outer even1..96.
Their complete source rows are
$$
-g(s)(1,p(s)),\qquad -1\ \text{for mean},\qquad
\theta_j e^{-\int_s^R(a+cp)}(-H(s),K(s)).
$$
Theta is exactly the original outer $H^{-5/6}$ Riesz factor supplied by the
owner, not a newly inferred convention. Mean body is
$-q(r)\mathbf1_{r<s}$, with no extra $\sqrt2$ and no outer mean atom.

Raw reference states are continuous at handoffs. A panel change in S
acts only on the reported body coordinate and does not insert an uncharged
state transmission. All193 original output observations occur once.

## 5. Full adjoint and finite dual inputs

```python
dual = complete_reference_adjoint_blocks(Gf, kernel_api, "fixed_WVC_Gfstar")
```

The return contains both the true body-kernel adjoint and
`finite_port_columns = Gf.atoms(r).transpose()`, with193 finite columns.
A body-only view is used solely to invoke the library's body_adjoint;
its omitted observation transpose is returned as a mandatory second block.
The complete adjoint is not identified with the body view.

Supplied S/outer-Riesz factors are already transposed in order. Additional
source Sobolev weights wrap the full operator. All actual high, mean,
root, outer, affine, and jump ports retain their genuine domains/receivers.
Reference zero boundary conditions do not identify the actual stable-root
chart with raw high even zero.

## 6. New private work and completed bounds

The signed function profiles and fields are private work for the newly
declared W2C joint candidate. The module has no owner, emit, entry point,
file IO, numerical import, launch, or artifact publication.
There is no pointwise rho2 division in the continuous Green kernel.

The finite circuit keeps its original rho2 and endpoint factors.
The owner retains the exact paired identity
$J_\rho=(I-Q_f\Delta_\rho)P_fG_D$ and the complete old q, rho-defect,
endpoint, mean and tail bounds wherever the unchanged original operator
is used. They are read as whole completed objects. No WCTR5/4 lift,
scalar-trace propagation rate, or changed reference fee is substituted.

Storage is O(160 n) private boundary records and O(n) product-tree values
per active mode, plus requested full-box cache entries. No4724833-square
matrix is formed. This is a structural bound, not a measured runtime or
a claim that a finite comparison will pass. The new owner freezes its
actual panel/resource cap, whole target list, complete saved-prefix schema,
and output byte model before the first public scientific run.
