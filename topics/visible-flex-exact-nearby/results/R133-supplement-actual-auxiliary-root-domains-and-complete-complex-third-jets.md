# R133 supplement: actual auxiliary root domains and complete complex third jets

2026-11-14, phase_inverse.

**Two larger auxiliary domains are proved. Two still larger domains failed their stated interval gap tests and are retained.** Public run [43640181602](https://github.com/Rogerhu12/math-research-public/actions/runs/43640181602) evaluated all four requested complex rectangles of the same original root-piece extension. The radii $10^{-4}$ and $5\cdot10^{-4}$ passed the complete domain and family tests. The run returned $1$ because its requested all-four-domain criterion was not met. Its native correctly records `complete=true`, `proved=false` and the two unsuccessful gaps.

The result is a new derivative input for the [auxiliary continuation contract](R133-supplement-auxiliary-root-piece-analytic-extension-and-complete-complex-third-jets.md), not a continuation of the piecewise physical background across its seams. No prior successful small-domain calculation was repeated. The enlarged fold, direct leading-amplitude derivative budget, next-amplitude operator remainder and strong return norm remain separate.

## 1. Actual execution and exact object

The workflow event was `d2c6b992114b4d4573c183f6260afb6d74e56276`. The immutable scientific checkout was `6460b0ae596484b3d8a83766e26d7d9b43239cc3`. The seven input/identity gates passed, including all original $65$ background and $193$ response components in their untouched original shards, the fixed scalar anchor and the complete affine intrinsic parameter box.

The exact intrinsic center and retained half-width were
$$
 \eta_0=-\frac{7789843107295549}{4611686018427387904},
 \qquad \tau_\eta=\frac1{10^9}.
 \tag{A.1}
$$
This whole real intrinsic box is an enclosure for the fixed $\eta_0$ calculation. The explicit moving family still has the full complex disk $|\delta|\le10^{-8}$. The compact metric bump vanishes on the original germ. The independent even mean and the constant value repairs are retained.

The true-root interval is
$$
 [r_-,r_+]=
 \left[\frac{1191984371497}{5000000000000},
       \frac{2383968743003}{10000000000000}\right].
 \tag{A.2}
$$
The frozen scalar germ and original cubic piece $2549$ are respectively
$$
 \left[\frac{8556839292003943}{36028797018963968},
       \frac{8636031980136455}{36028797018963968}\right],
$$
$$
 \left[\frac{2147184947341121}{9007199254740992},
       \frac{4295308144604611}{18014398509481984}\right].
 \tag{A.3}
$$
On each attempted auxiliary radius $R$, the evaluated domain was the whole rectangle
$$
 \operatorname{Re}r\in[r_--R,r_++R],
 \qquad |\operatorname{Im}r|\le R .
 \tag{A.4}
$$
The auxiliary functions agree with the actual family on the original intersection in (A.3). Outside that intersection, only the declared auxiliary analytic extension is being bounded.

The exact runtime was Python $3.12.14$, python-flint $0.9.0$, NumPy $2.3.5$, SciPy $1.17.0$, with $320$ Arb bits. The mathematical child actually ran for $4.824215924000001$ seconds. It completed four intrinsic-domain evaluations and $774$ original cubic component rows, each containing ordinary derivatives $0$ through $3$. This is $3(65+193)$ rows: the last radius failed before its polynomial-family stage. Every evaluated domain, accepted row, full primitive error and failed test remains in the original native.

## 2. The two proved auxiliary domains

The following decimal inequalities are outward weakenings of the saved directed balls. Here $k(\rho)=-K(r_*-\rho)/\rho$ is the analytic divided curvature, and $a=\eta\sqrt{k}$ denotes the characteristic coefficient, not the physical radius.

| Whole auxiliary radius $R$ | $\operatorname{Re}K_r$ lower bound | $\operatorname{Re}a$ lower bound | $|a|$ upper bound |
|---|---:|---:|---:|
| $1/10000$ | $56.390738711362$ | $9.390726240329$ | $10.321383684874$ |
| $1/2000$ | $37.789985092760$ | $4.660953335021$ | $14.381508186460$ |

The required physical-radius, energy and rotational-gap real parts are positive on both whole rectangles. The complete rotational branch has $\operatorname{Re}s<0$, the full mean has negative real part, and $\eta$ has positive real part. The characteristic gap in the table is separately evaluated after the full $193$-component parameter direction.

The intrinsic third derivatives are genuine complex-domain derivatives, not values sampled on the real interval:

| $R$ | $|K|$ | $|K_r|$ | $|K_{rr}|$ | $|K_{rrr}|$ |
|---|---:|---:|---:|---:|
| $1/10000$ | $0.015358744452$ | $63.927882134915$ | $18621.906204224$ | $415335.992188$ |
| $1/2000$ | $0.091694297735$ | $85.446771025658$ | $25404.876647950$ | $2044887.779297$ |

The saved native also contains every ordinary derivative of $\beta,\gamma,s$, the true mean and $\eta$ through order three. For example the complete $\eta$ bounds are:

| $R$ | $|\eta|$ | $|\eta_r|$ | $|\eta_{rr}|$ | $|\eta_{rrr}|$ |
|---|---:|---:|---:|---:|
| $1/10000$ | $1.254569508136$ | $0.657753674780$ | $119.650847077370$ | $53163.979370118$ |
| $1/2000$ | $1.270758230240$ | $1.701049292461$ | $610.248526573182$ | $302004.320800782$ |

These bounds immediately pay the complex divided-curvature estimates
$$
 |k_\rho|\le\tfrac12\sup|K_{rr}|,\qquad
 |k_{\rho\rho}|\le\tfrac13\sup|K_{rrr}|
 \tag{A.5}
$$
on the corresponding root disks. They do not by themselves construct a larger fold.

The finite angular fields remain accompanied by their full intrinsic primitive remainder. On $R=1/10000$ the primitive remainder is less than $1.471021\cdot10^{-33}$; the saved sixth entry, paying the fifth radial primitive derivative, is less than $7.975120\cdot10^{-19}$. On $R=1/2000$ the corresponding bounds are $1.599627\cdot10^{-33}$ and $8.673826\cdot10^{-19}$. All product-mean errors use the analytic bilinear convolution, with no complex conjugation or extraction of a real part.

For the angular Wiener strip $1/32$, the complete drift bounds are:

| $R$ | $\|d\|$ | $\|d_\phi\|$ | $\|d_{\phi\phi}\|$ |
|---|---:|---:|---:|
| $1/10000$ | $0.028731043968$ | $0.114924175871$ | $0.937461433930$ |
| $1/2000$ | $0.038010271187$ | $0.152041084748$ | $1.133640722350$ |

The sharper drift estimate removes only the scalar mean of $u^2+Kv^2$ before applying the old primitive. It does not remove the actual even mean from $v$, from $\eta$, or from their radial derivatives. The native retains all radial/angular norm arrays on widths $1/64$, $1/32$ and $1/16$, as well as every individual original cubic component.

## 3. The two larger failed tests

At $R=1/1000$, the complete intrinsic denominators, rotational branch, root-slope real part, mean and $\eta$ passed. In particular
$$
 \operatorname{Re}K_r>1.497552795672 .
$$
All $258$ polynomial components were evaluated. However the resulting interval evaluation of $a=\eta\sqrt{k}$ had a real-part lower endpoint below $-0.925999811100$. The demanded positive-real characteristic test therefore failed. This is not a proof that the actual characteristic coefficient vanishes; it is a failure of the displayed whole-rectangle enclosure to prove the requested gap.

At $R=1/500$, the energy and rotational denominators and rotational branch still passed, but the real-part lower endpoint of the complete $K_r$ enclosure was below $-173.885757022875$. The characteristic/root continuation test failed before any cubic component was evaluated at that radius. The full six primitive jets and all computed intrinsic third-jet evidence were nevertheless saved.

No larger-radius claim is obtained by taking an absolute value of either failed lower endpoint. No failed domain is relabelled as successful. A later consumer may use already valid derivative enclosures to prove a separately declared smaller-domain or anchored estimate, but it must record that new argument and its own actual gates.

## 4. Original evidence and reproducibility

All paths below are relative to `topics/visible-flex-exact-nearby/notes/auxiliary_root_complex_third_jets_ci/run-43640181602-1/`.

| Evidence | Bytes | SHA256 |
|---|---:|---|
| `consumers/auxiliary-root-complex-third-jets.json.gz` | 432808 | `6276b4b8bd117b3092ce633b7164ff99968100f10b09cbaef8850d4c03f6b24f` |
| `consumers/process.json` | 38267 | `a6783642ae2c49f66c3a7b54f1506389f24771790f3bd5a324646df8229f9728` |
| `consumers/auxiliary-root-complex-third-jets.stdout.log` | 1197 | `fc2f7915dca21390283636225ff471707fb107d2e89f283e9885e316451e4a23` |
| `worker-process.json` | 2345 | `6e0a857df0aacb8900e4d3ef6c86d437a46f84af7a55f3df2787d10328d23ae4` |

The mathematical source SHA256 is
`70f848effb2e57c64b2c9e8100d6ac0af01968c13c939a4874c6f44b0a759d21`.
The exact $57$-input manifest SHA256 is
`404e8352112f38cd5b96dc42ebe49c9c11ebab3a2f2fc53db3f1e247314285da`.
It binds the original affine object and its two original intrinsic NPZ files, the complete recursive source closure, both unchanged cubic shards, the prior root identities and the new proof/source/driver.

The worker performed genuine pulls
`d2c6b992114b4d4573c183f6260afb6d74e56276`
to `6460b0ae596484b3d8a83766e26d7d9b43239cc3`,
then to `42292594b1b1ed6a72bfc377a0b32449d9c5b2b8`.
Both root/topic README diffs were empty. The original failure stdout, native and all accepted prefixes were published and preserved in the Actions artifact.

The two successful auxiliary rectangles are now usable complex derivative evidence. Their actual fold, leading and next-amplitude budgets must be paid on domains satisfying the corresponding flow and inverse-image gates. The original physical seams, complete old $I/J$ remainders, both source ports and independent mean remain part of the global problem. This result does not give a numerical strong-return constant, cutoff-$97$ high inverse or genuine nonlinear PDE branch.
