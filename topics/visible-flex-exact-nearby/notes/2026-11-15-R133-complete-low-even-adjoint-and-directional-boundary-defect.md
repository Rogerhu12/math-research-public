# R133: complete low-even adjoint output and directional boundary error

2026-11-15, visible-exact-astra-0df9 / newton_source.

**Status: proved analytic identities and posterior consumption.** No new numerical bound is asserted. The full7908 adjoint residual and true finite193 Poisson certificates remain the required numerical inputs; none is recalculated here.

Use the same fixed physical $\eta_0$, repaired M32 centre, $\delta=0$, reflected odd/even spaces and normalized angular measures as [the full moving cap interface](../results/R133-supplement-full-frequency-moving-cap-boundary-and-Poisson-interface.md) and [the adjoint posterior theorem](../results/R133-supplement-full-cap-adjoint-high-to-low-boundary-grams.md). The centre definition is 440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47. Every endpoint value below is at the true $L=9/10$, including the declared first Hermite extension if the first binary64 node exceeds $L$.

## L.1. Full even input and the constant mode

Retain the exact signed mean $m<0$ and maps

$$
 \Theta=\phi+\psi,\quad\Theta_\phi=v/m,\quad
 Vf=f\circ\phi,\quad Ug=g\circ\Theta,\quad
 B=(u/v)\circ\phi,\quad C=(1/v)\circ\phi,\quad
 \mathcal S=M_vU,\quad\mathcal S^*=mV.
 \tag{L.1}
$$

The fixed reflected primitive normalization gives

$$
                  (I_\theta C)\circ\Theta=-\psi/m.
 \tag{L.2}
$$

Let $P_{{\rm e},L}$ retain the even modes $j=0,\ldots,96$ in the orthonormal basis $1,\sqrt2\cos(4\phi),\ldots,\sqrt2\cos(384\phi)$. The original regular-row input is $\lambda=(f,a)$, where $f$ uses the96 orthonormal odd sine modes and $a$ is the last, independent mean coordinate. Even mean is first in the even-input coordinates. These two97 dimensional coordinate orders must not be confused.

For the same adjoint trial define

$$
 z_0=\langle z_{\lambda,C}(L)\rangle_\theta,\qquad
 \zeta_\lambda=z_{\lambda,C}(L)-z_0.
 \tag{L.3}
$$

No equality $z_0=a$ and no exact adjoint equation are assumed. The negative full cap row is

$$
 \mathcal C_-w=
 \binom{-P_{96}\mathcal Ew}{-\mathcal Mw},\quad
 \mathcal E=\mathcal S(H_B-K_BP_\perp H_C),\quad
 \mathcal M=-m^{-2}\Pi_0-K_0P_\perp H_C.
 \tag{L.4}
$$

Its complete adjoint trial is

$$
          T_\lambda=-H_B^*\mathcal S^*f-H_C^*\zeta_\lambda+a/m^2.
 \tag{L.5}
$$

The last term is a constant moving even function. A high projection removed it in the earlier high-output formula; a low-even projection must retain it.

## L.2. Exact nonmean and mean formulas

The reflected parity cancels the two extra scalar means in the differentiated formulas (A.25) of the adjoint theorem. Therefore

$$
 P_\perp T_\lambda=
 I_\phi\left\{(u/v)f_\phi+
          m^{-2}\bigl(z_{\lambda,C,\theta}(L)\circ\Theta\bigr)\right\}.
 \tag{L.6}
$$

The derivative on $z_C$ is the physical $\theta$ derivative. The complete moving mean is

$$
 \boxed{
 \langle T_\lambda\rangle_\phi
 =\left\langle f\{u/v-\psi\,\partial_\phi(u/v)\}\right\rangle_\phi
 +m^{-2}\left\{
 a+\langle Uz_{\lambda,C}+\psi\,Uz_{\lambda,C,\theta}\rangle_\phi-z_0
 \right\}.}
 \tag{L.7}
$$

Here $a$ is an input and $z_0$ is the actual physical trial mean. Their discrepancy is already part of the complete left endpoint error, and is not set to zero.

For proof, the original derivatives give
$H_B1=-BC-B_\theta I_\theta C$ and
$H_C1=-C^2-C_\theta I_\theta C$. Equations (L.1)--(L.2) imply

$$
 (H_B1)\circ\Theta=-u/v^2+(\psi/v)\partial_\phi(u/v),\qquad
 (H_C1)\circ\Theta=-v^{-2}-\psi v_\phi/v^3.
 \tag{L.8}
$$

Pairing the first with $\mathcal S^*f=mVf$ and using
$d\theta=(v/m)d\phi$ gives the first term of (L.7). For the second,

$$
 \begin{aligned}
 -\langle H_C^*\zeta_\lambda,1\rangle_\phi
 &=m^{-1}\langle U\zeta_\lambda\{v^{-1}+\psi v_\phi/v^2\}\rangle_\phi\\
 &=m^{-2}\langle U\zeta_\lambda+\psi\,U\zeta_{\lambda,\theta}\rangle_\phi .
 \end{aligned}
 \tag{L.9}
$$

The second line follows from
$v^{-1}+\psi v_\phi/v^2=m^{-1}-\partial_\phi(\psi/v)$ and periodic integration by parts. Substitute (L.3) and add $a/m^2$. This proves (L.7). An intermediate $m$ cannot be replaced by $|m|$. For the constant background $u=0$, $v=m$, $\psi=0$, the formula reduces algebraically to $a/m^2$.

## L.3. The same complete posterior error

Suppose the full adjoint certificate supplies a PSD matrix $W_{\rm err}$ in the regular-row coordinates with

$$
 \|(K_B,K_0)^*(\mathcal S^*f,a)+\zeta_\lambda\|_2^2
                           \le\lambda^*W_{\rm err}\lambda.
 \tag{L.10}
$$

This requires all body residuals, true endpoints, mean, genuine jumps, residual Hessian and full physical Green gains. The full7908 Gram is usable only after its actual complete gates pass.

The exact adjoint of (L.4) gives

$$
 \mathcal C_-^*\lambda-T_\lambda
 =H_C^*\{(K_B,K_0)^*(\mathcal S^*f,a)+\zeta_\lambda\}.
$$

For the same full bound $\|H_C\|\le c_*$,

$$
 \|P_{{\rm e},L}(\mathcal C_-^*\lambda-T_\lambda)\|_2^2
                        \le c_*^2\lambda^*W_{\rm err}\lambda.
 \tag{L.11}
$$

No new cap inverse is assumed. Only the requested output projection is finite.

## L.4. True finite97 boundary-model difference

Let $\mathcal B_L=-\mathcal C_-P_{{\rm e},L}$ be the true even97 part of the regular row. Its odd96 block remains the exact identity. Let $B_0$ be a chosen exactly specified nominal even97 matrix in the same coordinates, with its independent mean row.

Let $T_L$ contain the columns $P_{{\rm e},L}T_\lambda$ for the regular-row basis. It maps regular coordinates into even coordinates. Set

$$
 E_0=-T_L^*-B_0,\qquad E=\mathcal B_L-B_0.
 \tag{L.12}
$$

Then (L.11) proves

$$
                (E-E_0)(E-E_0)^*\preceq c_*^2 W_{\rm err}.
 \tag{L.13}
$$

This is an output-side inequality. It does not put the same matrix on the right of $(E-E_0)^*(E-E_0)$ in the different even-input coordinates.

Every Fourier alias and rounding error in a numerical enclosure of $T_L$ must be retained. A selected dyadic midpoint defines an exact new trial matrix; its difference from the enclosed $T_L$ is an additional complete error. The nominal matrix $B_0$ needs its exact original array identity and coordinate order. An independently valid older error bound remains available as a whole bound; two upper bounds are not subtracted.

## L.5. True right Poisson consumption

Let $G_R$ already be the true finite193 right Poisson operator into $Y$, with

$$
                         G_R^*G_R\preceq H_Y.
 \tag{L.14}
$$

Use the matching actual $H_Y$ for whole-body $L^2$, the complete negative interval, or the true cut trace. No body norm is substituted for a trace.

For any exactly specified parameter-to-even-trace matrix $X$,

$$
 \|G_R(E-E_0)X\lambda\|_Y^2
 \le c_*^2\,{\rm tr}(H_YW_{\rm err})\,\lambda^*X^*X\lambda.
 \tag{L.15}
$$

Indeed the squared norm of $G_R(E-E_0)$ is at most the trace of
$H_Y(E-E_0)(E-E_0)^*$. Equation (L.13) proves the claim by PSD monotonicity. Signed off-diagonal entries remain through the trace. The explicit trial term has Gram bound

$$
                         X^*E_0^*H_YE_0X.
 \tag{L.16}
$$

These terms act on the same input and must be combined using fixed positive-weight Cauchy, not an orthogonality assertion. This is posterior consumption of an already true $G_R$, and is not a circular proof of (L.14). If $X$ was formed in a radial weighted frame, its exact conversion to ordinary moving even coordinates must be included.

## L.6. Numerical scope

A later consumer can compute only the previously unused low-even output and its complete signed difference. It need not repeat targets, the adjoint proposal, any completed7908 residual cell, or any completed5970 local propagator. The actual existing components should decide whether this refinement is useful.

No numerical improvement is claimed here. All original successful certificates remain unchanged. The negative high BVP inverse, complete coupled feedback, nonzero-parameter transfer and true nonlinear branch remain separate obligations.
