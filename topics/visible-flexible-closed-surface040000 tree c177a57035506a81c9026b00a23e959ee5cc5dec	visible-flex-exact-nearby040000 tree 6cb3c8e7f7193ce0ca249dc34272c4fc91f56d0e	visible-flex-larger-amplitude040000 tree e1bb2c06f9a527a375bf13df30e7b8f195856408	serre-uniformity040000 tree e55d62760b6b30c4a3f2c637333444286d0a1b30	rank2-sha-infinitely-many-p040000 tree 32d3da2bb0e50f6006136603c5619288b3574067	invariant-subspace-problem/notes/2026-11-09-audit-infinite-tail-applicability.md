# Independent applicability audit: exact infinite tails, threefold development, and the finite modified head

2026-11-09. Reviewer: independent_audit. The reviewer did not construct the current tail or solve its nonlinear BVP. This is a scope audit of already reviewed results, plus elementary conditional deductions needed to identify their interfaces. It does not reopen their accepted proofs or assert a new nonlinear existence theorem.

**Conclusion.** The current mode-three, default-source, protect160 candidate is not literally covered by R520 or R20's exact nonlinear tail statement. The threefold planar closure and flat-collar development present no symmetry obstruction: they follow conditionally from the complete scalar equations by the calculations below. R28 directly supplies the exact deep calibration-root bracket for the current source. The new N160 rotational background bound is independently verified. What remains unprovided by these citations is a full-frequency nonlinear tail for the new source and angular subspace, and its controlled continuation/matching through the finite modified head.

Exact source paths, current Git blobs, read-only cache matches, and SHA256 values are in `2026-11-09-audit-infinite-tail-sources.json`. All available cached sources were byte-checked against their stated Git blobs. No neighbor-topic file was modified.

## 1. What each result actually supplies

| Source | Directly usable content | Scope that must not be enlarged |
|---|---|---|
| Swarm R520 | Existence of one exact C² closed embedded phase family, after its own infinite construction; its scalar limit has two fixed open constant collars | Its metric/profile, protected mode two, and small parameter are chosen in that construction. It is not a boundary map for the present fixed geometry, mode three, or finite160 modification. It supplies no present diameter/reach/amplitude ratios. |
| Swarm R95 | Exact C² planar development and global annular embedding from its specified positive projected metric, full Darboux equation, two open round collars, and π symmetry | Its formal statement has a smooth rotational metric, a single monotone annular radial chart, and π-periodic height. It cannot be applied verbatim to the whole cylinder-plus-two-inward-tails band. The symmetry step has the conditional threefold extension in §4. |
| Swarm R78 extract | The phase action on an angularly invariant metric, and C² gluing to fixed exact round collars; no angular frequency restriction | Its explicit caps and embedding use its radial/height barriers. Those cap bounds and geometry are not the current two-cap construction, and do not certify reach. |
| Large R20 | An exact full-frequency, complete-mean, C² single tail and a restricted 18-parameter family on its literal deep source; planar periods and deep-tail embedding are paid | Only nonzero even cosine modes, a fixed literal source, and a sufficiently deep unspecified N. No arbitrary full Dirichlet DN, shallow prefix, second end, large amplitude, or cap follows. |
| Large R28 | Exact mode-two calibration-root existence/localization for the current default deep source, and background C² estimates | The nonlinear height and its stable trace set are not constructed. Old numerical bounds for r_c=.966 must be recalculated for r_c=.25. |
| Large R16 | Full C²-height/C¹-metric coframe identities, including actual curl and period errors, for general periodic data | Approximate scalar data are not automatically an exact isometric immersion, or even a C² actual development without the stated extra regularity. |
| Large R18 | Its finite-jet two-period implicit-function result and its conditional weighted-jet C² development | The finite root uses a nonzero m1 third-order coefficient and varies E. It does not solve full Darboux or give a fixed-metric threefold tail. |
| Large R31 | Conditional Cartesian C² taper onto one unchanged infinite rotational background, with all physical-width and mean costs | It assumes the actual Cartesian jets and their deep decay. Finite DN or a few successful taper depths do not supply them; a fixed taper does not remove a fixed angular residual. |
| Large R27 | No isolated non-C³ germs for a literal R20 tail plus its stated finite pieces, giving one marker-recognition route | It explicitly does not transfer to a selected different source or arbitrary boundary trace. C² convergence alone does not prove its regularity-locus assertion. |

## 2. R20's exact parameter range is not the current source or spectrum

The formal R20 source is
$$
R=64,\quad a=11/4,\quad
\delta_n=.08\,2^{-n},\quad
\eta_n=\frac{.05}{\sqrt{.08}}\delta_n^{3/2}
=.004\,2^{-3n/2}.
$$
Its angular space consists of real even, π-periodic heights with nonzero frequencies $m=2j$. The mean derivative is solved from the complete holonomy-one root. The exact 18 parameters are a mode-two center label and 17 unstable labels; this is a restricted stable trace family, not a map on all analytic Dirichlet data.

The current unchanged deep source has
$$
\delta_n=.006\,2^{-n},\qquad
\eta_n=.0003\,2^{-3n/2},
$$
and the current nonmean heights have frequencies $m=3j$. The local analytic-map source, its full-frequency cell estimate, and the R64 specialization were all inspected. Their displayed function spaces are also nonzero even frequencies, and their displayed source constants are the literal .08 source. Their estimates strongly suggest a route to extending fixed positive source constants, but that extension is not a theorem already stated for this candidate.

Uniform spatial scaling can change the cuff radius and the allowed once-fixed epsilon. It cannot change the dimensionless log-cell lengths .08 to .006. An angular relabeling from frequency two to three changes the polar metric and the global turning/holonomy, so it is not a valid direct substitution either. The current `rejoinR20At` is null. A separately specified rejoin to the literal sequence would be a different fixed source; even that would not introduce m3 into R20's stated angular space.

There is no contradiction in designing a background by its mode-two calibration and then studying a mode-three height. The calibration selects the background; it does not force the height to contain mode two. The missing item is the all-frequency nonlinear theorem and its bounds in the new invariant subspace.

### A concrete sufficient-depth gate already fails at n=160

R20 does not identify protect160 with its sufficiently deep nonlinear start. Its formal proof uses
$$
h_{ang}=\frac{\log2}{2},\qquad\gamma=h_{ang}/32,
\qquad M_n=2\left\lceil\frac{10016(1+|\log\delta_n|)}{2\gamma}\right\rceil,
$$
and requires $M_n\le\delta_n^{-1/16}$ among several other conditions.

On substituting the current default source at n=160, the two sides are approximately 108219928 and 1409.82596082. The failure is provable without trusting these decimals: since $.006>2^{-8}$,
$$
\delta_{160}^{-1/16}<2^{10.5}<1536,
\qquad M_{160}>10016\cdot64\cdot160=102563840.
$$
Even the literal .08 source fails this gate at n=160. On the default source the isolated displayed gate first passes near n=443 in a floating diagnostic; that is not a bound for the other analytic-radius, Green, and contraction conditions, and is not a certified sufficient N.

Thus the existing proof, even after a parameter/spectrum adaptation, would have to start much deeper and separately continue to the physical cut, or be replaced by sharper validated constants. This is failure of a known sufficient proof condition, not a nonexistence statement.

### Why the 18-parameter spectral count cannot simply be copied

The exact scalar linear equation is meaningful for all integer m. Its fixed-mode ideal transfer has $\nu_m=m^2(m^2-1)/12$, $d=2^{-11/4}$ and $\alpha_\infty=65/64$:
$$
T_{m,\infty}=\begin{pmatrix}1&0\\0&d\end{pmatrix}
\begin{pmatrix}
1-\alpha_\infty\nu_m64&\alpha_\infty\\
\alpha_\infty\nu_m^2 64-\nu_m65&1-\alpha_\infty\nu_m
\end{pmatrix}.
$$
For m=3j, the analogous normalized block is $(-1)^j2^{-5-3j/2}T_{3j,\infty}$. There is no mode-two center. For $\nu\ge6$ the large eigenvalue magnitude is strictly between $64\nu$ and $(65/64)^2 64\nu$. This follows directly from its negative trace and positive determinant d: if $A=(65/64)(64+d)\nu-(1+d)$, the magnitude is $(A+\sqrt{A^2-4d})/2$; use $0<d<1/4$ to compare it with $64\nu$ and $(65/64)^2 64\nu$.

Consequently the ideal normalized large eigenvalue has magnitude between
$$
\frac{2\nu_{3j}}{2^{3j/2}}
\quad\hbox{and}\quad
\left(\frac{65}{64}\right)^2\frac{2\nu_{3j}}{2^{3j/2}}.
$$
Direct integer comparisons of their squares show instability for j=1,...,12. At j=12 the lower bound is $139860/131072>1$; at j=13 the upper bound is below .537. The comparison decreases thereafter, because the ratio $\nu_{3(j+1)}/\nu_{3j}$ is decreasing and is already less than $2^{3/2}$ at j=4. Both eigenvalues are stable for j≥13; the small eigenvalue is bounded using their product. Thus this ideal normalization has twelve unstable directions and no center, rather than R20's center plus seventeen unstable directions.

The exact integer/Fraction comparisons are reproducible with `scripts/audit_infinite_tail_scope.py`; its output is `notes/2026-11-09-audit-infinite-tail-scope-checks.json`.

This calculation only identifies the ideal split that a threefold proof would need to use. It does not pay the actual all-mode high-frequency bound, nonnormal projection constants, finite-cell perturbations, nonlinear contraction, or any finite-cut DN.

## 3. Directly applicable R28 input and the present epsilon

R28 §1 proves, for the default source and every n≥80, an exact calibration root in $[1/2,2]$, with
$$
|\alpha_n-65/64|\le B(\delta_n,c_n)/64,
\qquad B=792e^{384c_n}(384c_n+36\delta_n^2),
\quad c_n=.05\,2^{-n/2}.
$$
It establishes a bracket root and this localization, not uniqueness. One may define the source by selecting once a root in this bracket; the numerical root is its approximation. These facts are independent of cuff radius and epsilon. They apply directly to the unchanged cells n≥160 of the current source.

The new closing-geometry candidate recalculates the background for $r_c=1/4$, $w_{cut}=1/2$. Its full independent audit is `2026-11-09-audit-deep-background-n160.md`. The source normalization is
$$
Y=6\delta_0+\frac{6(.05\delta_0)}{1-2^{-3/2}},\qquad
\epsilon=\frac{w_{cut}(r_c e^{Y/\sqrt{12}})^7}{(2\delta_0)^{11/4}},
\quad\delta_0=3/500.
$$
A rigorous rational bound is $\epsilon<1953125/248832<7.85$; its diagnostic value is about 6.32176709. Direct cancellation of the fractional power in the derivative bound gives
$$
W_n<\frac{80000}{81}2^{-7n/4},\qquad
B_{160}<.018942193<.02,
$$
with B_n decreasing for all n≥160. Therefore the entire unchanged rotational deep background has meridian curvature below .02 and joins the flat disk in C². This resolves the deep-background alpha bracket and curvature issue for this source. It proves nothing about the nonrotational height or its finite-head transport.

## 4. Exact threefold scalar data do close in the plane

This is a conditional adaptation of the R16 identities, not a new source of scalar solutions. Let $u\in C^2$, $E\in C^1$ on a radial annulus, with $u(r,\theta+\tau)=u(r,\theta)$ for $\tau=2\pi/3$. Suppose
$$
g=E(r)dr^2+r^2d\theta^2,\quad q=g-du^2>0,
$$
and the complete Darboux density Q is zero, not merely a projected finite system. Use R16's coframe
$$
S=r^2-u_\theta^2,\quad\Delta=ES-r^2u_r^2,
\quad\rho=\sqrt S,\quad\alpha=\sqrt\Delta/\rho,
\quad\beta=-u_ru_\theta/\rho,
$$
and its continuous connection $\omega$. All these coefficients are τ-periodic. Assume its complete angular flux $\Phi=\langle\omega_\theta\rangle$ is one. R16 gives distributional curl zero, hence a C¹ angular potential with $\psi_r=\omega_r$, $\psi_\theta=\omega_\theta$ on the universal cover. Then
$$
\psi(r,\theta+\tau)-\psi(r,\theta)=\int_\theta^{\theta+\tau}\omega_\theta\,d\vartheta
=\tau.
$$
Writing $e_1=(\cos\psi,\sin\psi)$ and $e_2=Je_1$, the tangent $\rho e_2$ on successive sectors rotates by $R_\tau$. The full translation period is therefore
$$
v+R_\tau v+R_\tau^2v=0.
$$
Both rotational and translational holonomy are now paid. The compatible fields
$$
\Gamma_r=\alpha e_1+\beta e_2,\qquad \Gamma_\theta=\rho e_2
$$
integrate to a single-valued C² planar development, and $(\Gamma,u)$ induces g exactly.

Threefold symmetry alone does not imply flux one, the full scalar equation, or spacelikeness. Conversely, flux one alone does not imply zero translation period for general nonsymmetric data. The displayed three-sector cancellation is the missing reason here.

For even threefold heights, $\omega_r$ is odd, so its angular mean vanishes. The zero-mean phase correction has a fixed radial phase gauge, just as in R31. The radial target vector is equivariant under $R_\tau$, so its full angular average is zero. Consequently the centered primitive and one fixed phase are compatible with the exact radial development. This replaces R31's two-sector antiperiodicity argument without changing its product-rule estimates.

For approximate data, a Fourier construction may enforce a closed curve by subtracting means even though the scalar curl is nonzero. Exact discrete closure is therefore not evidence that the induced metric is exact; the full R16 radial correction must still be included and bounded.

### Coaxial round collars

In the R95 setting, replace its π symmetry by τ symmetry. Normalize the development on one open round collar. The two developments $P\circ S_\tau$ and $R_\tau P$ agree there; uniqueness makes them equal throughout the connected annulus. On the second collar write $P(x)=R_\alpha x+c$. Equivariance gives
$$
c=R_\tau c,\qquad (I-R_\tau)c=0.
$$
Since a nontrivial planar rotation fixes only zero, c=0. Thus the second collar is coaxial. The proper local-diffeomorphism argument for global annular injectivity is unchanged when its other hypotheses hold.

This does not justify treating the present entire band as one monotone radial annulus. A cylindrical core, turns of the material radius, and two inward tails need piecewise development, actual C² seams, and their own global embedding/separation proof. The R95 extension is an interface for appropriate annular pieces.

## 5. What is actually required for the C² flat limit

R20 proves a bound on every whole cell, not merely its port values:
$$
\|\operatorname{jets}_{\le2,\perp}v\|_{cell\ n}
+\|\operatorname{jets}_{1,2}\overline v\|_{cell\ n}
\le C\epsilon(1+M_n)^{15}\delta_n^{3/2}\longrightarrow0.
$$
Its cells satisfy the actual scalar equation, matching height values and radial derivatives; the complete mean root matches the mean gradient. The nonzero common branch and the actual equation supply the second-jet matching. A single integral fixes the mean height. These facts, together with the background w,w_r→0, give the C² flat limit. A finite far Robin condition does not give any of them by itself.

The same conclusion would follow for threefold solutions if these whole-cell and seam hypotheses were established there. Indeed as r approaches a positive cuff radius,
$$
\rho\to r,\quad\alpha\to1,\quad\beta\to0,
\quad\omega_\theta\to1,\quad\omega_r\to0.
$$
The coframe's first derivatives also approach the Euclidean ones. In the fixed gauge the development's first and second derivatives therefore approach those of the round planar map. For example
$$
\Gamma_{rr}=(\alpha_r-\beta\psi_r)e_1+(\alpha\psi_r+\beta_r)e_2\to0,
$$
while $\Gamma_{r\theta}\to e_2$ and $\Gamma_{\theta\theta}\to-r e_1$. This is enough for a C² extension by a constant-height disk. A genuine open collar is then obtained by retaining an interval inside that flat extension; vanishing endpoint jets are not themselves constancy on an interval of the nonflat tail.

### Relation to the fixed-background Cartesian taper

R31 §§2–3 can be applied without any frequency restriction once the actual Cartesian maps and jets exist. Its weighted costs are necessary inputs, including $A_{00}/d^2$, $A_{10}/d$, and $A_{01}/d$, with d the actual physical transition width.

There is a useful sufficient deduction when the taper uses whole deep cells. Suppose the fixed-gauge relative field V has V=V_r=0 at the cuff and its full Cartesian second derivatives tend uniformly to zero on the entire deeper region. If $d_n\ge c(r_{s,n}-r_c)$ for a fixed c>0, the fundamental theorem of calculus gives
$$
|V_r|\le(r_s-r_c)\varepsilon_n,\quad
|V|\le\tfrac12(r_s-r_c)^2\varepsilon_n,\quad
|V_\theta|\le(r_s-r_c)\varepsilon_n,
$$
where $\varepsilon_n$ is the supremum of the corresponding second jets on the deeper region. All the R31 weighted costs then tend to zero. Choosing a nearby constant mean height changes only the same order of position bound. The unchanged geometric cell sequence has comparable full-cell width and remaining cuff distance; a much thinner subtransition would require its actual different ratio.

This implication explains why a proved full C² tail can admit a vanishing-error fixed-background taper. It does not infer that full C² tail from finite numerical checkpoints. With a fixed Fourier cutoff, deeper tapering also leaves the shallower angular residual unchanged.

## 6. What finite160 physical modification does and does not preserve

A finite modification of the head leaves the equations on the unchanged deeper source identical. Therefore an exact family constructed wholly in that deeper region, if available, remains a family there. It need not have the required Cauchy data at the current outer cut.

To transport its trace set outward, one needs the **actual nonlinear full-frequency Cauchy map** for each intervening part of the fixed modified metric. The following are substantive hypotheses, not consequences of finite dimensionality:

1. One exact profile and its actual physical radial coordinate are fixed. Its required derivatives and joins agree; numerical interpolants are compared against that same profile.
2. The full projected metric stays positive, and the denominator used for the chosen Darboux Cauchy branch stays nonzero throughout propagation. The relative-w small balls in R20 are sufficient local conditions, not necessary geometric conditions for all solutions. In particular the true angular projection condition is $|u_\theta|<r$, not $|u_\theta|<rw$.
3. All angular analytic-width loss and nonlinear input/output radii are paid through the finite product. Finitely many cells may have extremely poor constants; the word finite does not give a useful amplitude range. R20 explicitly excludes this step.
4. The deep trace family is propagated as its actual full Cauchy data, including the nonlinear mean. Recasting that set as a DN map for selected boundary coordinates requires a valid projection chart or a transversality/invertibility argument on those coordinates. R20 never provides a full DN for arbitrary analytic Dirichlet data.
5. The resulting trace must match the actual core/prefix in complete compatible two-jets. Our independently reviewed cut two-jet lemma applies after its exact hypotheses hold; approximate use also needs first-derivative metric-defect control or a direct Cartesian seam check.

For positive smooth finite modifications, continuation of a sufficiently tiny analytic germ is a plausible route through local Cauchy theory. Neither its quantitative radius at the current cut nor the required visible-amplitude match is an already established consequence of the cited infinite-tail theorem. Arbitrary finite edits that introduce a degenerate branch are not covered even by that informal small-germ expectation.

The independent momentum audit of the current p160 mode-three linear port is in `2026-11-09-audit-cut-tail-p160-m3.md`. Its far32/48/64 agreement supports the finite linear diagnostic. It does not identify an exact infinite nonlinear stable manifold. The earlier physical-RK deep log-gain discrepancy is another reason not to use a finite numerical transfer as a certified all-depth operator bound.

## 7. Phase fixing, markers, and the actual completion scope

Once an actual band has an angularly invariant material metric and true open round collars, the phase formula $F_\alpha(s,\theta)=R_{-\alpha}F(s,\theta+\alpha)$ fixes those collars pointwise. The action is continuous in the C² topology without requiring a third derivative. This part of the R78 mechanism works for threefold data and for any continuous phase interval. Fixed caps then glue in C² when their actual collar geometry agrees. All-phase embedding still needs the complete band/cap separation proof; neither a period computation nor local tail embedding supplies cross-piece separation or reach.

R27's marker-recognition theorem is literal to R20. Its finite-piece criterion may be reused under its stated analytic-jump hypotheses, but the new accumulation cuff needs its own regularity argument if that marker route is used. Alternatively the present R4 marker theorem can be invoked once its explicit recognition and reach assumptions are paid. No finite Fourier truncation mismatch is a C² seam.

The current README permits numerical realization with honestly stated distance from strict existence, but still requires a fixed geometry and refinement toward an exact solution rather than a fixed construction defect. This audit is not imposing a new requirement that the whole new nonlinear theorem be proved before numerical work can continue. It does rule out citing R520/R20 as if they already proved that the current finite DN data lie on such an exact tail. A numerical completion route must independently show the full actual Cartesian residuals and all required refinement/closure controls on the same fixed source. R31 supplies a suitable conditional taper accounting framework if its real hypotheses are verified.

## 8. Source blobs

- Swarm R520: `ef3b50315efc59f62fafb30dbed516a2e3cd6f51`.
- Swarm R95: `c1a6ecae12f96996eda0d02897079a9d5df11847`.
- Swarm R78 cap/phase extract: `f12cdbd899b5906aa100391a0083b87a920de41e`.
- Large R20: `6c4a7c974386a864749b2c72b2e9cc7a922947d8`.
- Large R28: `cf9881e3ae2c2797a61213ab099dbec239be5f0d`.
- Large R16: `f7d2f7c290bd30a87583214b65b90b2b006b4ceb`.
- Large R18: `003d950ce98dafbc3e034577ded5a4ed0613ad76`.
- Large R27: `16b958826e77d1ad53c5aed64f0fe19b28554147`.
- Large R31: `7e39efd65086347ff6a0d20e557067bf4e3b7fcb`.
- Local full analytic-map proof used by R20: `e4d1e503796a2968e27e66ef4bdb16c888fda8d0`.
- Full-frequency cell-estimate dependency: `e02e594c8db2cb29ea71a86802104c87e5059906`.
- R64 exact single-tail specialization: `21c17f53a7c713527aa0a0e093c7bd2900829a63`.
