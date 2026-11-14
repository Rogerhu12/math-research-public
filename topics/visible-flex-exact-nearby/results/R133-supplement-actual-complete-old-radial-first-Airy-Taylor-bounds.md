# Actual complete old-radial Taylor bounds for the first Airy correction

**Status: actual public Actions conclusion, fixed original intrinsic parameter.**
Public run [43653825736](https://github.com/Rogerhu12/math-research-public/actions/runs/43653825736) completed its mathematical child with return code $0$ and all $20$ gates true. This is the first actual complete Fourier Taylor evaluation of the same first correction $w_1=(a_1,b_1)$ on the physical inner root window. It reuses the completed high intrinsic root jets and the completed larger auxiliary fold. No original target, FFT, high-root jet or auxiliary-domain stage was recomputed.

The result supplies complete old-radial derivatives and a complete **local** $L_0w_1$ strip-supremum bound. It does not yet supply the old-circle $I/J$ contribution, the independent even mean equation, the final operator source norm, or a strong return inverse at cutoff $97$.

## T.1. Exact dependencies and corrected principal factor

The mathematical contracts are:

- [Complete old-radial Fourier recurrence](R133-supplement-old-radial-first-Airy-Taylor-and-complete-Fourier-root-recurrence.md).
- [Same-complex-parameter branch symmetry and the complete Wiener tail](R133-supplement-full-complex-branch-symmetry-and-old-Taylor-Wiener-tail.md).
- [Actual high intrinsic jets at the true root](R133-supplement-actual-complete-high-intrinsic-jets-at-the-true-root.md).
- [Actual larger anchored auxiliary fold](R133-supplement-actual-larger-anchored-auxiliary-fold-with-preserved-prefix.md).

This run uses the corrected exact identities
$$
 B_-=X_\phi^2-TT_\phi^2,\qquad
 B_+=X_\phi^2+TT_\phi^2,\qquad
 \mu=Q^2B_+,
$$
$$
 a_0=GB_-,\qquad b_0=-2i\epsilon GX_\phi T_\phi,\qquad
 \det M_0=G^2B_+^2.
$$
The earlier archived proof and the unexecuted draft source which confused $B_-$ with $B_+$ remain identified in the recurrence's erratum. They are not the source used here. The already paid absolute lower bound for $\mu$ is valid with $B_+$; no exact coefficient error is absorbed into an unnamed remainder.

## T.2. Execution and immutable evidence

The workflow event commit is `f8716934760b57c9a412102231a7079b3ba01c15`. The immutable scientific checkout is `481bb84991ff27a177f9524a38f8a4324dadefae`. These are recorded separately.

| Item | SHA-256 |
|---|---|
| Scientific producer | `e4ccbf4b343623d74d089f79b6605a0601975c6ea5c1d2e113bad568fe60167d` |
| Complete Laurent/Taylor algebra | `9eb4b99b9a6b569233a3b7c3da80da7d2738c4f0bd18040654ff5b7beace2d4b` |
| Scientific driver | `f1b824aad8d104d59876f86ccf9528fdb70124219502391c32cd173c89d444aa` |
| Input manifest | `226e5acac42026431acbd166f92d423b6292ba6f73e65f58f808647d4701f1ad` |
| Actual native, $52843$ bytes | `18990ac2c1ed8e559d00982b75d663c08ad7e193455de1f8482511c36938b719` |
| Actual mathematical process, $48844$ bytes | `eebbbf37419729069c28ef3cd7c7d34f02154b8c391b0cfa9ca093de8855a356` |
| Actual worker process, $2575$ bytes | `8b5b958a62f5230e32aea6cfc723c187d84b7ae7726c28a33e8b29bc4a998bac` |

The primary records are [mathematical process](../notes/old_rho_first_Airy_Taylor_ci/run-43653825736-1/consumers/process.json), [native](../notes/old_rho_first_Airy_Taylor_ci/run-43653825736-1/consumers/complete-old-rho-first-Airy-Taylor.json.gz), [worker process](../notes/old_rho_first_Airy_Taylor_ci/run-43653825736-1/worker-process.json) and [publication manifest](../notes/old_rho_first_Airy_Taylor_ci/run-43653825736-1/publication.json).

The actual mathematical wall time is $10.637003359999994$ seconds. The driver invocation takes $10.787922385999991$ seconds. Runtime is Python $3.12.14$, python-flint $0.9.0$, NumPy $2.3.5$, SciPy $1.17.0$, with the producer's $320$-bit Arb precision.

The worker performed real pulls at `2026-11-14T23:33:57.586210+00:00` and `2026-11-14T23:34:08.658127+00:00`. The first advanced `56951f9ddf8e661252b033af43f5d1d48e477150` to the scientific checkout above; the second retained that checkout. Both actual root/topic README diffs are empty.

## T.3. The actual family and the physical domain

The intrinsic parameter is the fixed original value
$$
 \eta_0=-\frac{7789843107295549}{4611686018427387904}.
$$
The full complex parameter disk $|\delta|\le10^{-8}$, the exact repaired candidate, the complete repaired $193$-component direction, the independent mean, and all original physical piece identities are retained. This is not a claim on a varying intrinsic parameter box.

The true root is enclosed by
$$
 r_*\in\left[
 \frac{1191984371497}{5000000000000},
 \frac{2383968743003}{10000000000000}\right].
$$
Let $\rho=r_*-r$, $h=9/10^6$. The fixed physical interval used by this result is
$$
 \left[
 \frac{1191939371497}{5000000000000},
 \frac{2384058743003}{10000000000000}\right]
 =[r_{\rm lo}-h,r_{\rm hi}+h].
$$
Its complete root-relative radius is
$$
 h_{\rm cover}=\frac{90000009}{10^{13}},
$$
which pays the whole root enclosure width.

The old-product Cauchy domain has $|\rho|\le1/6000$ and
$|\operatorname{Im}\phi|\le1/128$. Its actual fold image satisfies
$$
 |T|<0.000773326125793<\frac{27}{32000},
 \qquad
 |\operatorname{Im}X|<0.007817479146908<\frac3{256}.
$$
Thus it lies inside the already paid full canonical amplitude rectangle. On that rectangle the original complete bounds are
$$
 |a_1|<0.515180947652,\qquad |b_1|<1410.835059137.
$$
The auxiliary analytic continuation is identified with the physical family only inside the original physical piece. No neighboring physical spline piece is replaced by that continuation.

## T.4. What was actually computed and retained

The run evaluated $258$ new original cubic root-point component rows: all $65$ candidate components and all $193$ direction components, with their four ordinary radial derivatives. It reused the existing complete intrinsic root derivatives through order $9$ and the original completed finite root point. It did not rerun an FFT or an intrinsic target.

There are $75$ completed natural finite-algebra stages. Each is preserved as its original complete compressed stage with a hash in the native/publication records. The driver verified all natural stage files and their complete Fourier arrays. There are no discarded successful stages.

The fold and leading amplitudes are expanded through degree $8$; forcing and the first correction through degree $6$. Products use full noncircular Laurent convolution at physical angular frequencies $4j$. The actual supports are:

| Taylor degree $p$ | $a_{1,p}$ | $b_{1,p}$ |
|---:|---:|---:|
| $0$ | exact zero | $|j|\le384$ |
| $1$ | $|j|\le384$ | $|j|\le576$ |
| $2$ | $|j|\le576$ | $|j|\le768$ |
| $3$ | $|j|\le768$ | $|j|\le960$ |
| $4$ | $|j|\le960$ | $|j|\le1152$ |
| $5$ | $|j|\le1152$ | $|j|\le1344$ |
| $6$ | $|j|\le1344$ | $|j|\le1536$ |

These are complete finite Taylor coefficient supports, not projections of an unknown coefficient onto a convenient head. The full geometric radial Taylor tail and the full infinite angular tail are then paid separately.

The run computes $\epsilon=+1$ and uses the proved same-complex-parameter identities
$$
 a_{1,-}=-a_{1,+},\qquad b_{1,-}=b_{1,+}.
$$
This uses no complex conjugation and retains both original Airy carrier branches.

## T.5. Actual old-radial derivative bounds

Write $\partial_\rho^p\partial_\phi^q$ for the derivatives below. Radial derivatives in $r$ have the same absolute bounds. On the physical interval in T.3, at old physical strip width $1/512$, the following are upward decimal bounds for the **strip supremum**:

| $(p,q)$ | $a_1$ | $b_1$ |
|---|---:|---:|
| $(0,0)$ | $5.507416243277\,10^{-6}$ | $244.920973215968$ |
| $(0,1)$ | $4.606903284391\,10^{-5}$ | $4.282258097665$ |
| $(0,2)$ | $0.000443226419288$ | $21.887447541753$ |
| $(0,3)$ | $0.025471384443960$ | $192.312771872382$ |
| $(1,0)$ | $0.612671062596$ | $40301.487931302329$ |
| $(1,1)$ | $5.204390668160$ | $391.382472221478$ |
| $(1,2)$ | $77.849981355082$ | $91833.954540971628$ |
| $(2,0)$ | $439.850974419900$ | $14368937.610040$ |

The corresponding **analytic Wiener** bounds are a different table:

| $(p,q)$ | $a_1$ | $b_1$ |
|---|---:|---:|
| $(0,0)$ | $5.568911931246\,10^{-6}$ | $244.921141623346$ |
| $(0,1)$ | $5.656332472292\,10^{-5}$ | $4.310996961110$ |
| $(0,2)$ | $0.004025443963554$ | $31.697433962913$ |
| $(0,3)$ | $1.859566770219$ | $5215.025828025413$ |
| $(1,0)$ | $0.660891073422$ | $40433.539557310704$ |
| $(1,1)$ | $13.433176860103$ | $22926.105673165269$ |
| $(1,2)$ | $2886.739099804412$ | $7784042.417604$ |
| $(2,0)$ | $32938.167949087542$ | $103366337.765810$ |

The native retains all $(p,q)$ with $0\le p\le2$, $0\le q\le3$, as well as output widths $0$ and $1/1024$. It retains each complete finite Fourier prefix and each full tail contribution separately. A strip-supremum number is not substituted for a Wiener multiplier norm.

## T.6. Complete local $L_0w_1$ bounds

At width $1/512$, the complete local operator, after division by the paid lower bound for $\mu$, satisfies
$$
 \|(\mu^{-1}L_0w_1)_1\|_\infty<24.457019494816,
 \qquad
 \|(\mu^{-1}L_0w_1)_2\|_\infty<781421.481649.
$$
Here $L_0$ denotes the complete local operator used in the recurrence, including the exact $i\epsilon\vartheta QK(T)$ cross term. These two bounds are strip supremum bounds for the amplitude output. They are not yet a Fourier-column or global source operator bound.

The native retains every local contribution. At width $1/512$ its upward decimal decomposition is:

| Contribution | First row | Second row |
|---|---:|---:|
| Radial second derivative | $23.691826653900$ | $773958.451512$ |
| Radial-angular term | $0.016748640947$ | $1.259537363308$ |
| Angular second derivative | $9.426818204\,10^{-7}$ | $0.046551599801$ |
| Drift derivative | $0.000033099358402$ | $3.076687023627$ |
| First transport | $0.081154662252$ | $5338.356707060521$ |
| Scalar potential | $0.000047677922341$ | $2120.290645318817$ |
| Exact $QK$ cross coupling | $0.667207817757$ | $0.000008622592270$ |

The independent actual totals at the three declared output widths are:

| Old physical angle width | First row | Second row |
|---|---:|---:|
| $0$ | $24.412236013626$ | $781415.975155$ |
| $1/1024$ | $24.434532254016$ | $781418.706726$ |
| $1/512$ | $24.457019494816$ | $781421.481649$ |

The former complete Cauchy construction of the larger auxiliary fold gave the second local row below $19107989810.304$. The present complete Fourier Taylor prefix and its paid tail reduce that row to the value above. The original larger-domain certificate is retained and supplies the Cauchy tail; its mathematical stages were not rerun.

## T.7. Interface with the strict exterior pieces

The bounds above concern the same actual root-normalized first correction. The strict exterior pieces may use the [third-jet exterior contract](R133-supplement-third-jet-exterior-and-holomorphic-root-budget-for-first-Airy-residual.md) at $|\rho|\ge h$.

The fixed inner interval is $[r_{\rm lo}-h,r_{\rm hi}+h]$. On its complement, every allowed true root satisfies $|\rho|\ge h$. On the inner interval, T.3 already pays the larger $h_{\rm cover}$. Consequently the two regions can be used to split the norm integral of one function. No cutoff is applied to that function, no correction is renormalized at the artificial endpoints, and no artificial interface source is introduced.

This statement does not remove any original physical seam. The original one-sided derivatives, true reconstruction jumps and independent mean/source equations remain part of the global residual calculation.

## T.8. Exact remaining scope

The actual process explicitly records:

- all original target/FFT/high-root/auxiliary stages recomputed: $0$;
- complete finite Fourier arrays and natural checkpoint files verified: true;
- all original physical seams and independent mean equations retained: true;
- physical background replaced outside the original piece: false;
- old-circle $I/J$ and independent even mean budget paid: false;
- full strong return or cutoff-$97$ inverse claimed: false.

To complete the strong return estimate, the first correction still needs the full old-circle nonlocal and mean source terms, the strict exterior derivative/source calculation and its original seams, the actual Airy/Fourier operator conversion, and the resulting full source/return norm. The present result supplies the complete inner-window amplitude derivatives needed by those consumers.
