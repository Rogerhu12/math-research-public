# Complete cap mismatch collector and a local uniform lift

Date: 2026-11-13.

## 1. What the collector consumes

The new source is
[scripts/fourfold_phase_cap_angular_mismatch_collect.py](../scripts/fourfold_phase_cap_angular_mismatch_collect.py).
It combines the actual whole-parameter outputs of:

- fourfold_phase_cap_angular_mismatch.py on every part of the physical body $[1/4,3]$;
- fourfold_phase_cap_graft_angular_mismatch.py on the complete natural graft $[3,25/8]$ and the genuine exterior Robin term;
- the actual R95 short-window point lift and the accepted R111 whole-parameter relative-form rows covering that same window.

The exact object remains the explicitly symmetrized affine family centered at
$$
p_5=-7789843107295549/4611686018427387904,\qquad |p-p_5|\le10^{-9}.
$$
A complete requested body subinterval is not a complete body. A tail-only graft report is not a complete graft. The collector verifies the exact interval union and rejects missing intervals, overlaps, incomplete mismatch reports, or a changed trial, object, parameter interval, source or dependency.

The finite trial has boundary modes $|k|\le4$, interior modes $|k|\le16$, and radial degree two. All ten input columns are retained: the nine physical left Fourier coefficients and the independent regular mean. The actual input functions are the exact saved binary coefficients; they are not assumed to solve the equation.

The collector independently checks the exact finite boundary data. At the left cut the saved primal trace is precisely the stipulated Fourier input, with every other interior-mode boundary coefficient zero. At the regular end its mean is precisely the separate regular input. It also checks the exact physical frequencies $4k$, the radial interval and the shared finite-element layout. FiniteTrial's representation gives continuous radial dual flux, constant mean radial flux, and
$$
q_k=-\frac{\partial_r p_k}{4ik}\quad(k\ne0),
$$
so $\operatorname{div}j=0$ identically, including all radial interfaces. No floating residual is used to infer this identity.

## 2. Complete matrix mismatch norms

The exact objects are those of §7 of
[the strong weak-residual contract](2026-11-12-core-strong-weak-residual-contract.md):
$$
z=B\nabla V-j,\qquad z_R=\Gamma V_R^\perp+p_R^\perp,
$$
$$
R_0^2=\int_{1/4}^{25/8}z^*B^{-1}z+
                   \langle\Gamma^{-1}z_R,z_R\rangle,
\qquad
R_1^2=\int_{1/4}^{25/8}(Dz)^*B^{-1}Dz+
                   \langle\Gamma^{-1}Dz_R,Dz_R\rangle .
$$
Here $D=\partial_\theta$ is physical angular differentiation of the unweighted mismatch. The inverse $\Gamma^{-1}$ acts only on nonmean modes. Every regular input column is retained, and the regular flux error is estimated separately.

Each accepted integration row encloses a complete ten-by-ten Hermitian input Gram by an exact binary midpoint plus a directed operator-norm error. Its error includes all actual primitive tails, angular aliases, radial Gaussian tails or whole graft coefficient variations, and arithmetic selection. The true Robin row is added exactly once, with its complete whole-family eigenvalue enclosures.

The collector adds every matrix before selecting the final exact Hermitian midpoint. If $C_j$ is that final selected matrix and $\epsilon_j$ the sum of all original errors plus the final directed selection error, then
$$
G_j=C_j+\epsilon_j I
$$
is a positive-semidefinite quadratic-form majorant of the true complete mismatch Gram. Thus, for every complex input vector $x$,
$$
R_j(x)^2\le x^*G_jx,\qquad j=0,1.                           \tag{1}
$$
The underlying true Gram is positive semidefinite; no numerical eigenvalue sign test is substituted for the enclosure proof.

The complete angular coefficient fee is
$$
C_B\ge\operatorname*{ess\,sup}_{[1/4,25/8]\times S^1\times I_\eta}
 \|B^{-1/2}(\partial_\theta B)B^{-1/2}\|.
$$
It is the maximum of the continuously proved body and graft fees. The exact radial Robin form commutes with $D$, so it adds no angular coefficient commutator. This accounts for the full eliminated infinite exterior; it does not set its Robin mismatch to zero.

The pair $(G_0,G_1)$ is not the Gram of a primal weak PDE residual. Replacing it by such a residual would invalidate the complementary projection argument.

## 3. Uniform lift needs only its actual short window

Let
$$
c=\frac14,\qquad
c+d=\frac{2448832297382707}{9007199254740992}.
$$
R95 saved a complete point-only bound $B_0\le M I$ on this window. It also saved exact positive rational upper bounds $A_i$ for $(B_0)_{11}$ on a closed interval partition $I_i$. Define
$$
J=\sum_i\frac{|I_i|}{A_i}.
$$

For a high left trace $a$ supported on $|k|>N$, R95 uses the explicit competitor
$$
Ea(r,\theta)=\sum_{|k|>N}
   \left(1-\frac{r-c}{h_k}\right)_+a_ke^{4ik\theta},
\qquad h_k=\min(d,|4k|^{-1}).
$$
It vanishes outside the window. For the regular input use the exact angle-independent competitor
$$
e(c)=0,\qquad e'(r)=\frac1{J A_i}\ (r\in I_i),\qquad
e(r)=1\ (r\ge c+d).
$$
Its gradient vanishes outside the window and its nonmean Robin component vanishes everywhere at the exterior boundary. Consequently both competitors have zero body energy outside the window and zero true Robin energy.

Suppose accepted R111 rows prove, on this entire window and for the same whole real parameter interval,
$$
B_p\le(1+\varepsilon)B_0.                                  \tag{2}
$$
Then the actual full-cap variational competitors give
$$
E_N^{(\eta)}
 \le(1+\varepsilon)M\left(z_N^{-1}+z_N/3\right),\qquad
 z_N=\min(1,4(N+1)d),                                      \tag{3}
$$
$$
E_\xi^{(\eta)}\le(1+\varepsilon)J^{-1}.                    \tag{4}
$$
No coefficient comparison outside this short window is required for these particular competitors. The existence of the actual full positive cap and genuine tail is still supplied by the separate complete cap inputs. Their whole-parameter ellipticity and Robin family must not be omitted.

The collector deliberately recomputes $J$ from the saved exact rational $A_i$ and uses $J^{-1}$. It does not transfer an accidentally smaller point-only global linear competitor that was one of R95's optional alternatives.

An R111 execution may have accepted a complete proof of this short window while its requested farther body interval remains unfinished. It is valid to consume those independently proved accepted rows after checking their actual source and parameter identity and their exact complete union on this window. The collector records the original report's global completion flag, rejects an unresolved row intersecting the window, and does not transfer any uncomputed farther interval. This is a restriction of already proved rows, not a claim that the original whole-body report is complete.

The original observed R111 execution receipt cannot substitute for those accepted rows: the full report still has to be restored or rerun after the environment loss.

## 4. Full strong input Gram and known dual output

The complementary projection theorem gives
$$
\|D\chi(x)\|_*\le R_1(x)+C_B R_0(x).
$$
For any exact $t>0$, the elementary scalar inequality yields the complete input majorant
$$
\big(R_1(x)+C_B R_0(x)\big)^2
 \le x^*H_t x,\qquad
H_t=(1+t)G_1+(1+t^{-1})C_B^2G_0.                            \tag{5}
$$
One may choose $t$ from the actual norms to reduce the bound, but any selected positive exact binary rational is valid. Its selection introduces no approximation to the inequality.

Using (3) and the physical identity
$$
\|D\Pi_{>N}f\|_{\dot H^{-1/2}}
       =\|\Pi_{>N}f\|_{\dot H^{1/2}},
$$
the complete strong error satisfies
$$
\|\Pi_{>N}(S_p-d_j)x\|_{\dot H^{1/2}}^2
 \le x^*\big(E_N^{(\eta)}H_t\big)x.                         \tag{6}
$$
The regular flux retains its distinct complete bound
$$
|(S_p-d_j)_{\rm reg}x|^2
       \le x^*\big(E_\xi^{(\eta)}G_0\big)x.                 \tag{7}
$$
The mean has not been removed by differentiating.

The exact dual output is saved in full:
$$
d_j=(-p_L,p_{R,0}),
$$
including every interior Fourier mode $-16,\ldots,16$ and the last regular row. For $N\ge16$ its high left part is exactly zero, so (6) directly bounds the entire true high output. For $N<16$ the nonzero known finite rows must be added. Let
$$
D_N^*\Lambda D_N=
 \sum_{N<|k|\le16}|4k|\,(d_j)_k^*(d_j)_k.
$$
For any exact $s>0$,
$$
\|\Pi_{>N}S_p x\|_{\dot H^{1/2}}^2
 \le x^*\left[(1+s)D_N^*\Lambda D_N+
          (1+s^{-1})E_N^{(\eta)}H_t\right]x.               \tag{8}
$$
The collector returns (6), the exact finite high-dual Gram, and (8) separately. It never discards the modes $5,\ldots,16$ when reporting the $N=4$ output.

These remain complete ten-input quadratic forms. Any later six-sector or canonical/physical injection has to be applied to the entire forms and its own actual error, not only to a scalar diagonal estimate. The complete core/cap feedback inverse and nonlinear repair are still separate tasks.

## 5. Concrete replay contract and current status

The new collector contains no new geometry sampler. Once the actual complete body/graft mismatch reports and the R111 short-window rows exist locally, a call from the topic directory has the form:
~~~sh
python scripts/fourfold_phase_cap_angular_mismatch_collect.py \
  --body data/cap_angular_mismatch/body/*.json.gz \
  --graft data/cap_angular_mismatch/graft_and_true_Robin.json.gz \
  --lift-comparison "$R111_BODY_REPORT_WITH_COMPLETE_LIFT_WINDOW" \
  --half-width 1/1000000000 --cutoffs 4 16 64 256 \
  --bits 320 --out notes/complete_cap_angular_mismatch.json.gz
~~~
The body/graft paths in this command are intended output locations, not assertions that those files have already been produced. Each supplied body report must itself certify its stated requested subinterval; their exact union must be $[1/4,3]$. The complete graft must cover $[3,25/8]$. A tail-only report is rejected.

The native source keeps all failed/incomplete output flags explicit. It first records a complete mismatch result, if available, before applying the uniform lift; a later missing lift cannot silently become a strong-flux certificate.

The source was written while the native executor was unavailable and has not been run. Actual work observed before the outage consisted of the successful true Robin-only calculation and one local continuous body coefficient/alias calculation. The attempted 1024-angle body integration was interrupted with zero accepted cells at inspection; its angular alias floor was preserved. The corrected 2048-angle body run and complete graft integral had not started when the executor disconnected.

Thus no complete new $R_0$, $R_1$, $C_B$, or numerical strong-flux bound is asserted by this source or note. Those full outputs must be genuinely produced and collected; neither an execution receipt nor missing intervals are replaced by zero.
