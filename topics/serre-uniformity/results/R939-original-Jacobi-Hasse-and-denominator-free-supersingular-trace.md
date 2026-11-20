# R939 — The original Jacobi Hasse equation and denominator-free supersingular trace

Date: 2026-11-20. Status: **proved for every prime $p\ge41$ with $p\equiv5\pmod6$.** The original Serre labels still require $p\equiv2,5\pmod9$. This result records the explicit Tate-normalization correction to R936 in §2, proves that its whole trace and original source interpretation are unchanged by that correction, identifies a fixed differential equation for its actual Hasse polynomial, and removes its supersingular denominator. For the $r=2$ row it also gives a unique fixed second-order equation for the original companion $C$. No new numerical calculation is made here, and uniform nonvanishing of the trace remains open.

## 1. The unchanged original objects

Use all of R936's notation:
$$
p=6N+5,\quad k=\mathbf F_p(s),\quad s^2=-3,\quad
D=1-4t,\quad x=1-8t,\quad H=H_N,
$$
$$
L=k[t]/(tH),\qquad e_0=H/H(0),\qquad
b=-D(H+3tH').
\tag{939.1}
$$
The two original rows are $r=2$, $k_-=p-1$, $J=N$ when $p\equiv11\pmod{12}$, and $r=8$, $k_-=p-7$, $J=N-1$ when $p\equiv5\pmod{12}$. Keep precisely
$$
F=V_{k_-}^{\dagger},\quad
C(t)=12s(6s)^J P_J(24s(1-8t)),\quad
F(E_u,\omega)=(-1)^J D^{J+1}C(t).
\tag{939.2}
$$
The sign in this evaluation is part of the correction proved in §2. In particular $C$ is not replaced by a similar hypergeometric polynomial or by its negative: its defining polynomial, original oldform phase, CM theta source and $p$-dependent $J$ remain those of R913/R936. In both original rows $J$ is odd.

R936 proves that $L$ is étale, $H(0)H(1/4)\ne0$, and $b$ is a unit in $L$. The $t=0$ summand has weight one, every root of $H$ has weight three, and the three elliptic $D=0$ points have their already proved zero contributions. None of these statements is changed below.

## 2. The actual scalar Serre derivative

On the same generic model and differential as R936,
$$
E_u:y^2=x_E^3+3uD x_E+D(1/2-4u^3),\quad
t=u^3,\quad\omega=dx_E/(2y),
$$
$$
E_4(E_u,\omega)=-144uD,\quad
\Delta(E_u,\omega)=-108D^2,\quad
\eta^{12}(E_u,\omega)=-6sD,\quad
\operatorname{KS}(\omega^2)=du/D.
\tag{939.3}
$$
The symbol $x_E$ is the Weierstrass coordinate, distinct from $x=1-8t$.

### 2.1 Explicit correction of the scalar signs in R936

For a short Weierstrass equation $y^2=x_E^3+A_E x_E+B_E$ with $\omega=dx_E/(2y)$, the Tate-normalized forms satisfy
$$
E_4=c_4=-48A_E,\qquad E_6=-c_6=864B_E.
\tag{939.3a}
$$
The minus sign in $E_6=-c_6$ is indispensable. A direct normalization check uses the Tate cusp $y^2+xy=x^3$: completing the square and translating $x$ gives $Y^2=X^3-X/48+1/864$. Thus $c_4=1$, $c_6=-1$, while the normalized Fourier expansions of $E_4,E_6$ both have constant term one. Independently, Baker's §1 evaluates $E_4$ and $E_6$ on $y^2=4x^3-ax-b$ as $12a$ and $-216b$; putting $a=-4A_E,b=-4B_E$ gives exactly (939.3a).

For the actual family this yields $E_6(E_u,\omega)=+432D(1-8t)$. Substitution into the modular identity $dj/j=-(E_6/E_4)\operatorname{KS}(\omega^2)$ proves the positive KS sign in (939.3).

Keep the same marked coordinate $u\sim(4s)^{-1}Q^{-1}$ established in R936. Its relation $u=E_4/(4sV_4^\dagger)$ still gives $V_4^\dagger(E_u,\omega)=12sD$. The corrected $E_6$ has leading term $-Q^{-6}/8$ in this frame, whereas its Fourier expansion begins with one. Since the original $\eta^{12}$ Fourier expansion begins with $Q^3$, its scalar evaluation begins with $-Q^{-3}/8$. Of the two roots of $\eta^{24}=-108D^2$, this is $-6sD$, proving its sign in (939.3) without changing the phase or cusp.

In particular
$$
\frac{E_6}{\eta^{12}}(E_u,\omega)=24s(1-8t)
\tag{939.3b}
$$
is unchanged. The original $C$ of R936 therefore acquires precisely the evaluation sign $(-1)^J$ in (939.2). This corrects R936's displayed $E_6$, $\eta^{12}$, KS and scalar $\mathcal B$ evaluations; it does not change its defining polynomials or original marked modular forms.

There is no correction to R920's separately proved marked identity $E_6/\eta^{12}=-24s$: it follows from its original theta identities, and (939.3b) gives the same value at the marked $t=1/4$. In particular the marked ratio used by R937 is unchanged.

### 2.2 The scalar derivation and the actual denominator

Let $f(u)$ be the scalar evaluation of a modular section of weight $w$. Since the ordinary Serre derivative satisfies $\partial_6\eta^{12}=0$, its connection is fixed by the displayed nonzero section. The derivation on weight-zero functions is $\delta=D\,d/du$. As $\delta(-6sD)/(-6sD)=-12u^2$, the exact scalar rule is
$$
\boxed{\partial_w f=D\frac{df}{du}+2wu^2f.}
\tag{939.4}
$$
This is in the original $\tau'$ normalization. R932's Katz operator is still $6(\mathcal A\partial_w+w\mathcal B)$, where $\mathcal B=\partial_{p-1}\mathcal A$; no factor six has been absorbed in (939.4).

R936 gives $\mathcal A(E_u,\omega)=uD^{N+1}H(t)$. Define the explicit polynomial
$$
\beta(t)=-(1-8t)H(t)-3tD(t)H'(t)=b(t)+4tH(t).
\tag{939.5}
$$
Applying (939.4), using $12(N+1)+2=2p+4$, gives the exact identity of scalar polynomials
$$
\mathcal B(E_u,\omega)=-D^{N+1}\beta(t).
\tag{939.6}
$$
Unlike R936's congruence for $b$, (939.6) is an equality before restriction to supersingular points. On the supersingular algebra the scalar evaluation is therefore $-D^{N+1}b$. Both sign corrections disappear separately in the original function $F^{p+1}/\mathcal B^{k_-}$, since $p+1$ and $k_-$ are even. Thus R936's polynomial $R$, whole trace, and every value already computed from it retain their original source interpretation. This is an exact cancellation after correcting the evaluations, not permission to choose a new normalization.

## 3. Fixed Hasse and Jacobi equations

The standard modular identities in our Serre normalization are
$$
\mathcal B=E_{p+1}/12,\qquad
\partial_{p+1}\mathcal B=-\mathcal A E_4/144
\quad\text{in characteristic }p.
\tag{939.7}
$$
For example, $\mathcal A(Q)=1$ gives $\mathcal B(Q)=E_2(Q)/12$, and the Ramanujan derivative gives the second equality; the weights supply the $\mathcal A$ factor. Equivalently, this is Baker's Proposition 1.3 with his derivation equal to twelve times ours and his $B$ equal to $E_{p+1}$.

Apply (939.4) to (939.6). Since $12(N+1)-2=2p$, its undifferentiated term vanishes and
$$
\partial_{p+1}\mathcal B=-3u^2D^{N+2}\beta'(t).
$$
By (939.3) and (939.7), the same expression equals $u^2D^{N+2}H(t)$. Hence
$$
\boxed{\beta'=-H/3.}
\tag{939.8}
$$
Differentiating (939.5) now gives
$$
\boxed{9tD H''+12(1-8t)H'-25H=0.}
\tag{939.9}
$$
These are polynomial identities in $\mathbf F_p[t]$. In particular
$$
9tD\beta''+3(1-8t)\beta'-\beta=0.
\tag{939.10}
$$
The old denominator also satisfies
$$
3Db'-4b=-9DH,\qquad (Db^3)'=-9DHb^2.
\tag{939.11}
$$
All these follow directly from (939.5), (939.8); no root enumeration or numerical recurrence is used.

For a precise hypergeometric identification, put $h(t)=H(t)/H(0)=\sum h_nt^n$. Equation (939.9) gives
$$
3(n+1)(3n+4)h_{n+1}=(6n+5)^2h_n.
\tag{939.12}
$$
The denominators are units for $0\le n<N$, and $6N+5=p$. Thus
$$
\boxed{\frac{H(t)}{H(0)}=
\sum_{j=0}^{N}\frac{(-N)_j^2}{(4/3)_j j!}(4t)^j.}
\tag{939.13}
$$
Here $(a)_j$ denotes the rising factorial. Equivalently this is the Jacobi polynomial $P_N^{(1/3,1/3)}(1-8t)$, normalized to value one at $t=0$, reduced modulo $p$. This equivalence is just the defining hypergeometric formula, since $N+5/3\equiv-N\pmod p$. In $x=1-8t$ its differential equation is
$$
(1-x^2)y''-(8/3)xy'-(25/36)y=0.
\tag{939.14}
$$
The fixed rational parameters concern $H$, not the distinct original companion $C$.

## 4. Baker's theorem removes the original denominator

The published primary input is Andrew Baker, *A supersingular congruence for modular forms*, Acta Arithmetica 86 (1998), 91–100, Theorem 1.4:
$$
E_{p+1}^{p-1}
=-\left(\frac{-1}{p}\right)\Delta^{(p^2-1)/12}
\quad\bmod(p,E_{p-1}).
\tag{939.15}
$$
It holds at every supersingular elliptic curve, including $j=0$ and $j=1728$. The [author PDF](https://www.maths.gla.ac.uk/~ajb/dvi-ps/modforms.pdf) gives the exact theorem and normalization. The source's derivation normalization does not alter (939.15).

Pull (939.15) back to the actual supersingular points of R936. Since $12^{p-1}=1$, use $\mathcal B=E_{p+1}/12$, (939.3), and (939.6). The $D$ powers cancel exactly because $(N+1)(p-1)=(p^2-1)/6$. Consequently
$$
\beta^{p-1}
=-\left(\frac{-1}{p}\right)(-108)^{(p^2-1)/12}
\quad\text{in }L.
\tag{939.16}
$$
This use of $L$ is justified by its étaleness and evaluation at every geometric root; the actual $D=0$ elliptic points are not members of $L$ and already have zero contribution in R936.

The remaining constant is fixed without a new numerical computation. At the original $t=0$ supersingular point, $\beta(0)=-H(0)$ lies in $\mathbf F_p^\times$. Evaluating (939.16) there shows its right side is exactly one. Therefore
$$
\boxed{\beta^{p-1}=1,\qquad \beta^p=\beta\quad\text{in }L.}
\tag{939.17}
$$
Moreover (939.5) gives $\beta=b$ in the whole algebra $L$, because $4tH=0$ there. This includes $t=0$, rather than only the roots of $H$.

Since $k_-=p+1-r=(p-1)+(2-r)$,
$$
\boxed{b^{-k_-}=\beta^{r-2}\quad\text{in }L.}
\tag{939.18}
$$
The $r=2$ row has no denominator at all; the $r=8$ row has the positive sixth power $\beta^6$.

## 5. The unchanged whole trace in polynomial form

Define
$$
R_{\rm poly}=D^{2N+2}C^{p+1}\beta^{r-2}\in L.
\tag{939.19}
$$
Then $R_{\rm poly}$ equals R936's original $R$ exactly. Thus
$$
\boxed{S^p=12[-6^{r-1}(r-1)!]^2
\operatorname{Tr}_{L/k}((3-2e_0)R_{\rm poly}).}
\tag{939.20}
$$
The $t=0$ coefficient remains one; every $H$-root coefficient remains three. The already proved zero elliptic contributions remain part of the full point accounting. R932's original functional is still
$$
\lambda_h(\Phi_{k_-}(F)_{\rm full})=
\frac{m_{\mathrm I}(c_h^{\mathrm F})^{1/p}}
{d_1\,6^r(r-1)!}\,S.
\tag{939.21}
$$
In particular $d_1$ is not replaced by twelve, and the original nonzero source scalar $c_h^{\mathrm F}$ is not normalized away. No finite-field norm positivity is used: eliminating a unit denominator does not prevent cancellation in the trace.

## 6. A unique fixed equation for the original r=2 companion

Assume $p\equiv11\pmod{12}$, so $r=2$, $J=N$ is odd, and the actual evaluation is $F=-D^{N+1}C$. Keep this original $F$. R932 gives
$$
G=\mathcal T_{p-1}F,
\qquad \partial_{2p}G=\mathcal A^2V_4^\dagger/6.
\tag{939.22}
$$
Because $p-1=-1$ in the residue field and $\mathcal B=\partial\mathcal A$,
$$
G=6\mathcal A^2\delta(F/\mathcal A),\qquad
\delta=D\,d/du,\qquad F/\mathcal A=-C/(uH).
\tag{939.23}
$$
The weight $2p$ is zero in (939.4). Consequently (939.22–23), and $V_4^\dagger(E_u,\omega)=12sD$, give
$$
\frac d{du}\left(\mathcal A^2D\frac d{du}\frac C{uH}\right)
=-\frac{\mathcal A^2V_4^\dagger}{36D}.
\tag{939.24}
$$
Put $K=3tHC'-C(H+3tH')$. Direct differentiation yields
$$
\mathcal A^2D\frac d{du}\frac C{uH}=D^{2N+3}K.
$$
Since $dt/du=3u^2$ and $2N+3=4/3$ modulo $p$, equation (939.24) becomes
$$
DK'-(16/3)K=-(s/9)H^2.
\tag{939.25}
$$
Using (939.9), its left side is exactly
$$
H\{3tDC''+(2-24t)C'-3C\}.
$$
Cancellation of the nonzero polynomial $H$ proves
$$
\boxed{3tDC''+(2-24t)C'-3C=-(s/9)H.}
\tag{939.26}
$$
This derivation retains both factors six in (939.22–24) and the factor three from $t=u^3$. No phase or source vector has changed.

The operator on the left of (939.26) preserves polynomials of degree at most $N$. On $t^n$ its diagonal coefficient is $-3(2n+1)^2$. Every such coefficient is a unit for $0\le n\le N$ because $2N+1<p$. Hence (939.26) has a unique polynomial solution of degree at most $N$, and the actual $C$ is that solution.

Explicitly, writing $H=\sum h_nt^n$ and $C=\sum c_nt^n$ with $c_{N+1}=0$ gives the descending recurrence
$$
c_n=\frac{(n+1)(3n+2)c_{n+1}+(s/9)h_n}{3(2n+1)^2}
\quad(n=N,N-1,\ldots,0).
\tag{939.27}
$$
This is an alternative finite construction of the same original companion, not a newly chosen form. It also proves $C/s\in\mathbf F_p[t]$ in this row. No recurrence has been numerically executed in this proof. No corresponding order-two assertion is made for the $r=8$ row.

## 6.1 Prime-field descent in both original rows

The [complete original-phase descent proof](../notes/R939-prime-field-descent-of-full-trace.md) gives $\bar c_j=(-1)^j c_j$ in the full original triangular Fourier basis. It follows that the unchanged $C$ belongs to $s\mathbf F_p[t]$ in both the $r=2$ and $r=8$ rows. Consequently $C^{p+1}$, $R_{\rm poly}$, the full trace and $S$ descend to $\mathbf F_p$. This uses the inert-two ideal identity and the original $\zeta^2$ phase, not Hecke semisimplicity or a positivity property. The actual unknown source scalar outside $S$ is not asserted to descend.

## 7. Scope and the next actual issue

The new conclusions are (939.8–14), (939.17–20), and the source-preserving $r=2$ identity (939.26–27). They can be checked against existing R936 outputs without regenerating any old source.

They do not prove that the trace in (939.20) is nonzero. The pointwise equality $\beta^p=\beta$ puts the denominator values in $\mathbf F_p^\times$ and removes their inverse powers, but it gives no ordering on the other summands. $C^{p+1}$ must remain the original Frobenius product, and its possible cancellations cannot be excluded by calling it a positive norm.

R932's still missing comparison with R925's $Q'_h(0)$ is not supplied here. The independent same-label Legendre factor remains unchanged as well. These conclusions therefore do not complete the uniform Serre goal.

## Sources

- [R936](R936-explicit-polynomial-trace-of-the-whole-supersingular-pairing.md): the entire finite algebra, exact $H_N$ and $C$, original model and Hodge frame, and complete supersingular point accounting.
- [R932](R932-original-Igusa-Frobenius-line-and-supersingular-residue-pairing.md), (932.15–19), (932.31), (932.36–37a): the actual Katz normalization, complete companion identity, and unchanged original-functional scalar.
- [R913](R913-original-Igusa-Cartier-functional-and-two-CM-companions.md): original same-label CM companions and fixed oldform phase.
- Andrew Baker, *A supersingular congruence for modular forms*, Acta Arithmetica 86 (1998), 91–100, Proposition 1.3 and Theorem 1.4; [author PDF](https://www.maths.gla.ac.uk/~ajb/dvi-ps/modforms.pdf). His derivation is twelve times the Serre derivative used here, and his $B$ is $E_{p+1}$, twelve times the present $\mathcal B$.

The proof above consists of displayed paper algebra. Its later public computational check is recorded in the [2026-11-20 receipt](../notes/2026-11-20-R939-window-and-weight34-sigma-receipt.md): run `44716895805` checked all 48 new original admissible primes between 109 and 1000, with every asserted identity verified and no zero full sum. This finite window is not a uniform nonvanishing theorem.
