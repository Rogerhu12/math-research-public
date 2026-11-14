# R706：至200000的完整剩余素数窗口及原sigma系数的真实零值

日期：2026-11-14。状态：**精确有限结论已证明，并由原平坦坐标的独立算法确认关键零值。** 这反驳原两个系数对所有剩余素数均为单位的猜想；不是Serre一致性的反例，也不证明原$M_2$本身为零。

## 1. 完整有限命题

令

$$\mathcal P=\{p\text{ prime}:41\le p\le200000,\ p\equiv2\text{ or }5\pmod9\}.$$

该集合恰有 **5992** 个素数。沿R615/R697的同一角色、周期、原$E_0:y^2=x^3-1$及$dz=dx/(2y)$规范：

- 每个$p\in\mathcal P$均有$C_p\not\equiv0\pmod p$；
- 除$p=137147$外，每个$p\in\mathcal P$均有$C_{p-3}\not\equiv0\pmod p$；
- 在$p=137147\equiv5\pmod9$，有准确值

$$A_p=103259,\qquad A_{p-3}=0,\qquad C_p=80155,\qquad C_{p-3}=0\quad\text{in }\mathbf F_p.$$

其中41..2000的99个素数由[R689](R689-exact-remaining-prime-window-through-2000.md)完整证明；本次只计算不相交的2001..200000范围，共5893个素数。四片长度为1474、1473、1473、1473，无遗漏、无重算旧窗口。

## 2. 真正原系数的计算与完整覆盖

[R698](R698-two-actual-square-roots-at-one-low-degree.md)给$p=6N+5$时准确的有限域公式

$$A_p=-\left(\frac2p\right)[w^N]T(w)C(w),\qquad
 A_{p-3}=\frac23\left(\frac2p\right)[w^N]T(w)Z(w)^3,$$

$$c_j=\binom{2j}{j}/4^j,\quad C=\sum c_jw^j,\quad
 Z=\sum\frac{c_j}{6j+1}w^j,$$

$$h_0=1,\quad (6j-1)h_j=(6j-4)h_{j-1},\quad
 T=\exp\left(\sum_{j=1}^N\frac{h_j}{j}w^j\right)\pmod{w^{N+1}}.$$

一切只保留到$N=(p-5)/6$；此范围全部除数小于$p$。第一个被排除的$H$分母恰为$p$，故没有把无限$p$非整级数直接约化。由[R697](R697-original-sigma-six-sections-and-integral-square-roots.md)原普通导数归一，两方向均有$C=-3A^2\pmod p$。

正式新窗口在公开仓库[Actions43585949869](https://github.com/Rogerhu12/math-research-public/actions/runs/43585949869)运行，源提交`0202228ff67b38a0e41302cd491cf40e949b7396`。算术为FLINT0.9.0的精确有限域多项式运算；每个素数均检查完整$wT'=T(H-1)$系数方程。零值是合法结果，流程不会将零当失败后排除。

收集器[`R706_collect_exact_window.py`](../scripts/R706_collect_exact_window.py)独立用确定性筛法形成整个素数集合，逐片核请求、源码、预期集合、原始证书SHA、全部实际输出及平方回代，再核其不重不漏并集。它不重跑系数运算。合并证书为[`R706-exact-window-through-200000.json`](../notes/R706-exact-window-through-200000.json)。逐素数完整数值及其各自证书链接由下面四份rows保存：

| 片 | 素数数 | 原返回rows | SHA256 |
|---:|---:|---|---|
| 0 | 1474 | [rows](../computations/R698-window-0/43585949869-1/rows.json.gz) | `bc53f2ec6e844c5b46a4a18ef9111d8ed98f47e7cb7c8b18532b880df60f5bf9` |
| 1 | 1473 | [rows](../computations/R698-window-1/43585949869-1/rows.json.gz) | `562269b7c436ec23759e63d20a4a01b52a8f96d57c211689178937619b3f7ac7` |
| 2 | 1473 | [rows](../computations/R698-window-2/43585949869-1/rows.json.gz) | `8f93f710ac6d091b660a4d6121e398d72e2e01a3c50ed895a781db462d82785e` |
| 3 | 1473 | [rows](../computations/R698-window-3/43585949869-1/rows.json.gz) | `4138b78c7d48fc1ec00aeaf640c744052a54f148bbf4eef9ea591eb5633812d5` |


## 3. 零值的完整证书与不同坐标复核

原零证书位于[prime-137147.json.gz](../computations/R698-window-0/43585949869-1/prime-137147.json.gz)，SHA256为`e9b682e8fdbba4551790dc4b3afc5a704455f408d9b8f2b3ca734e8c4400c5a0`。它保存全部22858个$C,Z,H,T$系数和两次末卷积的各22858个加数。独立检查器[`R698_verify_zero_certificate.py`](../scripts/R698_verify_zero_certificate.py)已逐项核全部递推、完整指数方程、两卷积及原平方归一；[完整回执](../notes/R698-zero137147-full-check.json)保留准确计数和SHA。

为另行解决R698换元/有限Frobenius化简可能有误这一风险，又在**原平坦$z$坐标**中直接解Weierstrass能量方程及sigma微分方程，未调用$H,T,Z$或Lagrange公式。该正式运算在公开[Actions43587480525](https://github.com/Rogerhu12/math-research-public/actions/runs/43587480525)成功，源提交`fdb4c969bfd5f3e3a3e921875d1f10f34e52b5ba`。

原坐标结果[original-z-137147.json.gz](../computations/R706-original-z-137147/43587480525-1/original-z-137147.json.gz)的SHA256为`54fcc49e58f9f53eaf459d2c59379578ed64281874dede30d097e69c115afc05`。全部Newton精度层能量恒等式、22857个sigma系数方程和两末卷积给出同样的$103259,0,80155,0$。下面给该独立算法的完整证明，所以一致性不仅是一项未说明归一的数值比较。

## 4. 对实际Abel系数的准确后果

R658/R683保持原六挠点与有限角色，证明

$$r_2=cC_p,\quad r_3=-27cB^3C_{p-3},\quad
 c=\left(\frac3p\right)\frac{\alpha^2}{2},\quad\alpha^3=4.$$

$B,c$均为单位。R605及R683的完整尾与范数归一给

$$(pM_2)^2\equiv5184\zeta^2B^5\alpha^{-2}r_2r_3\pmod p.$$

逐个素数应用这一准确恒等式可得：在上述5992个素数中，**除137147以外的5991个素数均有$v_p(M_2)=-1$**。在137147则$r_2\ne0$、$r_3=0$，故

$$v_p(M_2)\ge-\frac12,\qquad v_p(M_2)\ne-1.$$

这是$p$进首项最小赋值的真实例外。它不推出$M_2=0$、Abel共同首阶$m>1$、某个真实高度jet为零，或存在任何非CM椭圆曲线反例。原R616本原非消失、实际高度及R699的规范常数仍须分别计算。R702只证明移后$p+3,p+6$两权单位，也不能向负移位跨界修复这两个原权。

## 5. 原平坦坐标核验算法的完整证明

### 1. Exact target and independence

The R698 window reports a zero of $C_{p-3}$ at the actual remaining
prime $p=137147\equiv5\pmod9$.  The companion
[`R698_verify_original_z.py`](../scripts/R698_verify_original_z.py) checks the two roots directly from the
original sigma-six sections of R697, without using the series $H,T,Z$
of R698, its Lagrange inversion, or its finite Frobenius simplification.

Write $p=6N+5$.  Here $N=22857$.  In the original elliptic coordinate
$dz=dx/(2y)$ on $y^2=x^3-1$, set

$$
w=z^6,\quad x(z)=z^{-2}X(w),\quad
y(z)=\tfrac12z^{-3}V(w),\quad \sigma(z)^6=z^6Q(w).
\tag{V.1}
$$

Then $X(0)=Q(0)=1$, $V=-2X+6wX'$, and the original curve equation is

$$
\boxed{V^2=4X^3-4w.}
\tag{V.2}
$$

The derivative of its degree-$n$ coefficient with respect to $X_n$
is $-4(6n+1)$.  Thus $X$ is uniquely determined through degree $N$
over $\mathbf F_p$: each $6n+1\le p-4$ is a unit.  The branch
$V(0)=-2$ is the original $y\sim-z^{-3}$ branch, not its negative.

For $L=\log(\sigma/z)$, the original identity
$(\log\sigma)''=-x$ gives

$$
6n(6n-1)L_n=-X_n\quad(n\ge1).
$$

Consequently

$$
\boxed{Q(w)=\exp\left(-\sum_{n=1}^{N}
\frac{X_n}{n(6n-1)}w^n\right)\pmod{w^{N+1}}.}
\tag{V.3}
$$

The normalization $\sigma/z\to1$ and the sixfold CM symmetry remove
the constant and linear integration ambiguities.  All denominators
$n$, $6n-1$, $6n+1$ in (V.2)--(V.3) are units through this cutoff.
No unrestricted infinite series is reduced modulo $p$.

The two actual sections are now

$$
x\sigma^6=z^4XQ,\qquad -xy\sigma^6=-\tfrac12zXVQ.
\tag{V.4}
$$

With $f_N=[w^N]XQ$ and $g_N=-[w^N]XVQ/2$, R697 and Wilson's theorem
give

$$
\boxed{A_p=-\ell_2 f_N,\qquad A_{p-3}=\tfrac23\ell_2 g_N,\qquad
C_p=-3A_p^2,\quad C_{p-3}=-3A_{p-3}^2\pmod p,}
\tag{V.5}
$$

where $\ell_2=(2/p)$.  The factorial reductions used are
$(p-1)!=-1$, $(p-4)!=1/6$,
$2^{-(p-1)/2}=\ell_2$, and $2^{-(p-5)/2}=4\ell_2$.

### 2. Fast exact solution of the original energy equation

Suppose $X$ solves (V.2) modulo $w^n$, and let
$r=\min(2n,N+1)$.  Form $V=-2X+6wX'$ and residual
$R=V^2-4X^3+4w$ modulo $w^r$.  The exact linearized equation for the
Newton correction $d$ is

$$
w d'+a(w)d=b(w),\qquad
a=-\frac{V+3X^2}{3V},\quad b=-\frac{R}{12V},\quad a(0)=\frac16.
\tag{V.6}
$$

The inverse of $V$ exists because $V(0)=-2$.  Let

$$
I=\exp\left(\sum_{j=1}^{r-1}\frac{a_j}{j}w^j\right),\qquad
J\left(\sum d_jw^j\right)=\sum\frac{6d_j}{6j+1}w^j.
\tag{V.7}
$$

Then $wI'/I=a-1/6$, and the solution with the required zero low
coefficients is

$$
d=I^{-1}J(Ib)\pmod{w^r}.
\tag{V.8}
$$

Since $R=O(w^n)$, one has $d=O(w^n)$.  The omitted nonlinear terms
in the equation for $X+d$ are $O(w^{2n})$, so the update doubles the
correct precision.  Starting with $X=1\pmod w$ gives the unique
solution of (V.2).  All divisions in (V.7) remain in the proved unit
range.  The implementation checks the complete equation (V.2) after
every Newton update, rather than relying only on the iteration's
formula.

Both exponentials are computed by the ordinary finite-series Newton
step $g\mapsto g(1+f-\log g)$, with
$\log g=\int g'/g$ and constant coefficient zero.  Every integrated
index is below $p$.  The final $Q$ is also checked coefficientwise by

$$
wQ'=Q\left(-\sum_{j=1}^{N}\frac{X_j}{6j-1}w^j\right)
\pmod{w^{N+1}}.
\tag{V.9}
$$

Together, (V.2) and (V.9), with constant coefficients one, uniquely
certify all retained coefficients.  The implementation saves the
complete $X,V,Q$ arrays and every summand of both last convolutions
under `--full`.

Using FLINT polynomial multiplication, the running cost is bounded by
$O(M(N)\log N+p)$ field operations and $O(N+p)$ storage; the linear
$p$ term constructs integer inverses.  This avoids an $O(p^2)$ Bell
recurrence or an $O(p^2)$ original Cartier coefficient index.

### 3. Executed small checks and the public single-prime run

The original-coordinate checks at $p=41,47$ have already been executed:

| $p$ | $f_N$ | $g_N$ | $A_p$ | $A_{p-3}$ | $C_p$ | $C_{p-3}$ |
|---:|---:|---:|---:|---:|---:|---:|
| 41 | 31 | 36 | 10 | 24 | 28 | 35 |
| 47 | 45 | 45 | 2 | 30 | 35 | 26 |

Their full certificates are [`R698-original-z-prime41.json`](../notes/R698-original-z-prime41.json) and
[`R698-original-z-prime47.json`](../notes/R698-original-z-prime47.json).  The public verification command for
the reported exception is

```bash
python R698_verify_original_z.py --prime 137147 --full --output original-z-137147.json.gz
```

The latter command has now completed in public Actions run 43587480525.
Its complete output and digest are bound in Section 3 above; all six requested
values agree with the first method.

### 4. The already executed complete audit of the original zero certificate

[`R698_verify_zero_certificate.py`](../scripts/R698_verify_zero_certificate.py) has checked the existing public
certificate with gzip SHA256
`e9b682e8fdbba4551790dc4b3afc5a704455f408d9b8f2b3ca734e8c4400c5a0`.
It verified all $22857$ coefficient relations for each of $C,Z,H,T$,
then checked each of the $22858$ summands in each of the two final
convolutions.  The exact outputs are

$$
[w^N]TC=103259,\quad [w^N]TZ^3=0,\quad
A_p=103259,\quad A_{p-3}=0,\quad C_p=80155,\quad C_{p-3}=0.
$$

The audit receipt is [`R698-zero137147-full-check.json`](../notes/R698-zero137147-full-check.json).  The
independent method above addresses the separate risk of an erroneous
R698 change of coordinate, rather than repeating that audit.

The independent output agrees. The exact original R605/R683
criterion therefore implies $v_p(M_2)\ne-1$ at this prime; its justified lower
bound is $v_p(M_2)\ge-1/2$.  It does not imply $M_2=0$, $u_1=0$,
a vanishing height jet, or a counterexample to the Serre theorem.


本仓库原规范依赖：[R605](R605-middle-CM-block-as-one-characteristic-p-coefficient.md)、[R658](R658-Cartier-trace-comparison-and-actual-Cp-channel.md)、[R683](R683-even-weight-Cartier-channel-and-actual-r3.md)、[R697](R697-original-sigma-six-sections-and-integral-square-roots.md)、[R698](R698-two-actual-square-roots-at-one-low-degree.md)、[R699](R699-actual-height-finite-jets-and-complete-exterior-tail.md)、[R702](R702-first-pole-block-and-uniform-shifted-units.md)。
