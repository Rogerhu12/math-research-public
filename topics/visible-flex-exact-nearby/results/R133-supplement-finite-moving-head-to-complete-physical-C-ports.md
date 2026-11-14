# R133 supplement: finite moving head to complete physical C ports

2026-11-14, visible-exact-astra-ac0d / phase_inverse.

**Proved for the exactly continuous repaired final centre, uniformly on
$[.9,25/8]$ and the whole original affine parameter interval.** A
complete moving variation whose second component has Fourier indices
$|j|\le96$, including its mean, has physical curvature variation

$$
 \boxed{\quad
 \|P_{|j|>112}\,\delta C\|_{L^2_\theta}
 <4.422619\,10^{-7}\|h_2\|_{L^2_\phi},\qquad
 \|P_{|j|>128}\,\delta C\|_{L^2_\theta}
 <1.757236\,10^{-14}\|h_2\|_{L^2_\phi}.
 \quad}                                               \tag{P.1}
$$

Both circles have normalized measure and physical frequency $4j$.
The first moving component contributes exactly zero to this particular
physical $C$ port. The actual physical mean is
$\delta C_0=-\langle h_2\rangle_\phi/m^2$ and is retained separately.
No finite moving head is identified with the same finite physical
head, and no small norm for composition minus identity is asserted.

## 1. Exact physical moments and their full derivative

For the complete repaired moving state let

$$
 m=\langle v\rangle_\phi<0,\qquad
 \theta=\phi+\psi(\phi),\qquad
 \psi=\frac1m I(v-m),\qquad \theta_\phi=v/m>0.
                                                               \tag{P.2}
$$

Since $C(\theta)=1/v(\phi)$, its complete physical Fourier moments are

$$
 C_k=\frac1m\left\langle e^{-ik(\phi+\psi)}\right\rangle_\phi,
       \qquad k\in4\mathbb Z.                        \tag{P.3}
$$

For an arbitrary physical, unnormalized moving variation $h=(h_1,h_2)$,
write $z=\langle h_2\rangle$. Then
$\delta\psi=(Ih_2-z\psi)/m$, so exactly

$$
 \boxed{\begin{aligned}
 \delta C_k={}&-\frac{z}{m^2}\langle e^{-ik\theta}\rangle
 -\frac{ik}{m^2}\langle e^{-ik\theta}Ih_2\rangle
 +\frac{ikz}{m^2}\langle e^{-ik\theta}\psi\rangle,\\
 \delta C_0={}&-z/m^2.
 \end{aligned}}                                       \tag{P.4}
$$

This formula is a derivative of the true moments. It includes the
physical measure change and the parameter-dependent angle; there is
no hidden $1/v$ in it. In particular the $h_1$ column is zero without
assuming the centre solves Codazzi. Equation (P.4) agrees with the
complete physical-state variation in the residual-sensitive cap bridge,
and uses its same physical normalization.

## 2. The actual repair is paid before contour weights

The existing full cap native stores all 65 coefficientwise suprema of
the original finite sine polynomial $\psi$. For any positive width
$\sigma$ these give its complete entire-function bound

$$ p_\sigma^{\rm old}=
  \sum_{j=-32}^{32}p_j e^{4|j|\sigma}.                 \tag{P.5}
$$

The repair native stores exact coefficientwise correction bounds
$e_j$ and $e_0$ for the mean. With original mean gap $g_0$, put

$$
 g=g_0-e_0>0,\qquad
 E_{I,\sigma}=\sum_{j=1}^{32}\frac{e_j}{4j}e^{4j\sigma}.
$$

The exact identity
$\psi^{\rm new}-\psi^{\rm old}
 =(Ie_{\ne0}-e_0^{\rm signed}\psi^{\rm old})/(m+e_0^{\rm signed})$
therefore gives

$$
 p_\sigma=p_\sigma^{\rm old}
       +\frac{E_{I,\sigma}+e_0p_\sigma^{\rm old}}g.    \tag{P.6}
$$

The current bounds use all exact repair coefficients before the
exponential weight. They do not extrapolate the previously proved
$A_{1/32}$ correction to a larger strip by fiat. The derived centre is
identified by SHA256
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`.

Only $a_\sigma=\sigma-p_\sigma>0$ is needed below. There is no claim
that the complex physical inverse angle exists throughout these
larger contour widths. The finite moving-angle integrands in (P.4)
are entire and periodic, so their Fourier integrals can be shifted
directly. The true real inverse angle was already proved on the cap.

## 3. Full contour bound and every output frequency

Let $h_2=z+h_{2,\ne0}$ have moving indices $|j|\le N$.
For normalized angular $L^2$, Cauchy--Schwarz gives

$$
 \|Ih_{2,\ne0}\|_{S_\sigma}
 \le B_N(\sigma)\|h_{2,\ne0}\|_2,
 \qquad
 B_N(\sigma)^2=2\sum_{j=1}^{N}
                      \frac{e^{8j\sigma}}{(4j)^2}.    \tag{P.7}
$$

The two-sided factor two is explicit. For a positive physical output
$k=4l$, shift the contour to $\operatorname{Im}\phi=-\sigma$;
for negative output use the opposite contour. Equations (P.4)--(P.7)
then give

$$
 |\delta C_{4l}^{\ne0\text{-input}}|
 \le\frac{4|l|B_N}{g^2}e^{-4|l|a_\sigma}
                       \|h_{2,\ne0}\|_2,
 \quad
 |\delta C_{4l}^{\text{mean-input}}|
 \le\frac{1+4|l|p_\sigma}{g^2}e^{-4|l|a_\sigma}|z|.
                                                               \tag{P.8}
$$

These are estimates of every true physical output coefficient, not a
finite DFT. Put $t=e^{-8a_\sigma}$ and define

$$
 \begin{aligned}
 S_0(K)&=\frac{t^{K+1}}{1-t},\\
 S_1(K)&=t^{K+1}\left(\frac{K+1}{1-t}
                          +\frac{t}{(1-t)^2}\right),\\
 S_2(K)&=t^{K+1}\left(\frac{(K+1)^2}{1-t}
       +\frac{2(K+1)t}{(1-t)^2}+\frac{t(1+t)}{(1-t)^3}\right).
 \end{aligned}                                       \tag{P.9}
$$

Thus $S_j(K)=\sum_{l>K}l^jt^l$ exactly for $j=0,1,2$.
The complete nonmean-input and mean-input tail constants are

$$
 C_{\ne0}=\frac{4B_N}{g^2}\sqrt{2S_2},\qquad
 C_0=\frac1{g^2}\sqrt{2(S_0+8p_\sigma S_1+16p_\sigma^2S_2)}.
                                                               \tag{P.10}
$$

Both signs of every output frequency are included. The full operator
norm is at most $\sqrt{C_{\ne0}^2+C_0^2}$ because the moving mean
and nonmean input subspaces are orthogonal. The same coefficientwise
argument gives the Hilbert module of radial suprema if the input is
bounded in $L_r^\infty L_\phi^2$; no interchange of a radial supremum
and an infinite output sum is required.

## 4. Actual complete computation

The 256-bit Arb consumer evaluates all coefficients in (P.5), all
repair coefficients in (P.6), the full 96-mode sum (P.7), and the
infinite sums (P.9). It tests widths $j/32$, $1\le j\le32$, accepting
only those with $a_\sigma>0$. Choosing the smallest bound among these
proved estimates is legitimate. All eight actual gates passed.

| Physical retained indices $|j|\le K$ | Chosen contour | Full physical C tail gain |
| --- | ---: | ---: |
| 96 | $1/8$ | $<1.657551$ |
| 104 | $1/4$ | $<.001478525$ |
| 112 | $9/32$ | $<4.422619\,10^{-7}$ |
| 128 | $9/32$ | $<1.757236\,10^{-14}$ |
| 160 | $9/32$ | $<2.656946\,10^{-29}$ |
| 192 | $9/32$ | $<3.858870\,10^{-44}$ |

The unpadded bound is not small. In particular this theorem does not
justify throwing away the physical outputs above 96 when assembling
a moving 193-state head. It supplies a quantitatively small full
remainder after padding the physical ports to 112 or 128 instead.
The finite conversion columns below that cutoff must still be computed
or enclosed with their exact moment formula and original mean row.

The omitted physical input can be consumed by the already proved
complete cap Green; its all-frequency multiplication feedback and
the true exterior remain intact. This does not mean that the retained
physical columns alone furnish the complete negative/positive Schur.

## 5. Reproduction and scope

Source:
`scripts/fourfold_codazzi_final_head_to_physical_C_tail.py`.
Native with explicit complete cap SHA check:
`notes/2026-11-14-R133-repaired-moving-head96-physical-C-tail-v2-native.json.gz`.
The earlier v1 native had the same arithmetic; v2 adds the explicit
published cap byte identity and is the output used here.

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps python \
  scripts/fourfold_codazzi_final_head_to_physical_C_tail.py \
  --out notes/2026-11-14-R133-repaired-moving-head96-physical-C-tail-v2-native.json.gz
```

Replay uses a fresh output. The complete cap input is SHA256
`ad6efc2a226131245ff4197a0b5da2843578224368a340f7a50d383c03a1819b`;
the full exact repair input is SHA256
`6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc`.
This is the actual derivative at the identified repaired centre, not
an assertion that an unknown infinite background correction remains
finite or has the same tail. The full body inverse, parameter Schur
and nonlinear closure remain separate.
