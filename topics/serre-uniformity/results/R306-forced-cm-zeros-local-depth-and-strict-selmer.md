# R306：实际 CM 中心零、准确局部深度与严格 Selmer 条件

日期：2026-11-13。状态：**已证明；实际分支的全局条件，主要目标仍未完成。**

R302 的中心值二择一在两个二进分支中有不同作用：偶分支的指定 CM 曲线已有一个明确无限阶点，因此中心值为零是自动成立的；不能再尝试对这个分支证明统一中心非消失。本篇同时计算 R301 显式点在表示素数处的准确可除深度，把较深参数送入同一个 CM 曲线的严格 $p$-Selmer 群。最后核准另一条来自三次方程的 CM Jacobian：它也有正秩，但其 $p$ 惯性与实际同余根本不同。

## 1. 实际参数、曲线和两个显式点

保持 R301、R302 的全部实际假设和符号：
$$
\begin{gathered}
p>37,\quad p\equiv2,5\pmod9,\quad
a^3+db^3=1,\quad d>0\text{ 立方自由},\\
r=1-a^3=db^3,\quad a,b\in\mathbb Z,\quad
a\ne0,1,\quad b\ne0,\\
\varepsilon=-1\ \text{若 }4\mid a,\qquad
\varepsilon=1\ \text{若 }a\equiv1\pmod {16},\\
H_a:y^2=x^3+3ar\,x-r(2a^3-1),\qquad
B_a:y^2=x^3-\varepsilon r,\\
\phi:H_a[p]\xrightarrow{\sim}B_a[p]
\quad\text{为原来实际 }G_{\mathbb Q}\text{-模同构}.
\end{gathered}
\tag{306.1}
$$
这里还保留小惯性 $I_p=C^3$、$K=\mathbb Q(\sqrt{-3})$、$\sigma=1$、
整 $j$ 和相同的实际二除域、三除法 $S_3$ 商域。
定义
$$
C_a=A_r:\ y^2=x^3+r,\qquad
P_a=(a^2,1)\in H_a(\mathbb Q),\qquad
Q_a=(a,1)\in C_a(\mathbb Q).
\tag{306.2}
$$
$P_a$ 已由 R301 证明为无限阶。$Q_a$ 的存在直接来自 $a^3+r=1$。

## 2. 指定 CM 曲线的自动中心零

**定理 306.1。** 对全部 (306.1) 的允许参数，$Q_a$ 为无限阶，
因此
$$
\operatorname{rank}C_a(\mathbb Q)\ge1,\qquad
L(C_a/\mathbb Q,1)=0.
\tag{306.3}
$$
特别：
$$
\boxed{
\begin{array}{c|c|c}
\text{实际分支}&\text{有明确无限阶点的 CM 曲线}&\text{被迫为零的中心值}\\ \hline
4\mid a&B_a=C_a&L(B_a,1)=0\\
a\equiv1\bmod16&B_a^{(-1)}=C_a&L(B_a^{(-1)},1)=0
\end{array}}
\tag{306.4}
$$

**证明。** 在任意非奇异整短模型
$y^2=x^3+Ax+B$ 上，若一个二进有理点的 $x$ 坐标有负赋值，
它不是挠点。确实，形式参数 $t=-x/y$ 的赋值为正整数；
短模型给 $[-1](t)=-t$，所以整倍乘级数
$[2](t)=2t+O(t^3)$ 把其赋值准确提高一、永远不为零；
乘奇数则保持赋值。此论证包含 $v_2(t)=1$ 的边界，
不要求该模型极小或好约化。这也是 R301 所用的形式群事实。

对 $Q_a$ 倍点，斜率为 $3a^2/2$，于是
$$
x([2]Q_a)=\frac{a(9a^3-8)}4.
\tag{306.5}
$$
若 $a$ 为奇数，分子为奇数，故其二进赋值为 $-2$；
所以 $Q_a$ 无限阶。

若 $4\mid a$，记 $s=v_2(a)\ge2$。
在 $C_a$ 上，三除多项式及三倍点分子为
$$
\begin{aligned}
\psi_3(Q_a)&=3a(4-3a^3),\\
\phi_3(Q_a)&=a\psi_3(Q_a)^2-\psi_2(Q_a)\psi_4(Q_a)
             =81a^9-144a^3+64.
\end{aligned}
\tag{306.6}
$$
这里使用
$\psi_2(Q_a)=2$、
$\psi_4(Q_a)=4(a^6+20ra^3-8r^2)$ 并代入 $r=1-a^3$。
分母 $\psi_3(Q_a)^2$ 不为零，
$$
v_2(\psi_3(Q_a)^2)=2s+4,\qquad
v_2(\phi_3(Q_a))=6,
\tag{306.7}
$$
因为后者的三项赋值依次为 $9s$、$4+3s$、$6$，
唯一最低项是 $64$。因此
$$
v_2(x([3]Q_a))=2-2s<0.
\tag{306.8}
$$
同一形式群论证说明 $Q_a$ 无限阶。

若 $L(C_a,1)\ne0$，Burungale–Flach 的 CM 秩零定理使
$C_a(\mathbb Q)$ 有限，与上面的点矛盾。
故 (306.3) 成立。由 $B_a=A_{-\varepsilon r}$，
二次扭曲 $-1$ 将系数乘 $-1$，立即得到 (306.4)。$\square$

因此，R302 的
$L(B_a,1)=0$ 或 $v_p(L(B_a,1)/\Omega_{B_a})\ge2$
在 $4\mid a$ 分支的第一项已经自动成立。
这不是排除该分支的判据。奇分支中，已有点位于 $B_a^{(-1)}$，
不能移到 $B_a$；R301、R302 对 $B_a$ 本身的非零 Selmer 条件仍是额外要求。

## 3. 两个点在 $\mathbb Q_p$ 中的准确可除深度

R258 和 R290/R294 给
$$
m=v_p(d)=
\begin{cases}
2,&p\equiv2\pmod9,\\
1,&p\equiv5\pmod9,
\end{cases}
\qquad
k=v_p(b)\ge1,\qquad
v_p(r)=m+3k.
\tag{306.9}
$$
因为 $p\mid r=1-a^3$ 且 $p\equiv2\bmod3$，立方在
$\mathbb F_p^\times$ 上双射，所以 $a\equiv1\bmod p$。
令
$$
\ell=\left\lfloor\frac{m+3k}{6}\right\rfloor
=\left\lfloor\frac{k}{2}\right\rfloor,\qquad
e=m+3k-6\ell\in\{1,2,4,5\}.
\tag{306.10}
$$

**定理 306.2。** 准确有
$$
\boxed{
\begin{aligned}
P_a&\in p^\ell H_a(\mathbb Q_p)
          \setminus p^{\ell+1}H_a(\mathbb Q_p),\\
Q_a&\in p^\ell C_a(\mathbb Q_p)
          \setminus p^{\ell+1}C_a(\mathbb Q_p).
\end{aligned}}
\tag{306.11}
$$
这里 (306.11) 是两个实际局部群的可除性陈述，
不声称存在全局 $p^\ell$ 次原像。

**证明。** 先对两条曲线分别取
$x=p^{2\ell}X,y=p^{3\ell}Y$。
在 $H_a$ 的新短模型上，
$$
v_p(A_{\min})=2\ell+e,\qquad
v_p(B_{\min})=e,
\tag{306.12}
$$
因为 $a$ 和 $2a^3-1$ 均为 $p$ 进单位。
在 $C_a$ 的新短模型上，系数为 $A_{\min}=0$、
$v_p(B_{\min})=e$。
两者均有极小判别式赋值 $2e$：
原来的两个判别式均为 $-432r^2$，缩放除去 $p^{12\ell}$。
由于 $p>3$ 且 $e<6$，这些短模型极小，且为加性约化。

两条曲线都没有 $\mathbb Q_p$-有理 $p$ 挠点。
对 $H_a$，这来自 (306.1) 的实际表示与小惯性 $C^3$。
对 $C_a$，它与 $B_a$ 相差单位二次扭曲 $-\varepsilon$，
此扭曲在 $p>2$ 不分歧，故仍有同一 $C^3$ 惯性。
在非分裂 Cartan 上，任意非恒等标量乘法的固定空间为零；
$C^3$ 非平凡，因而两者的惯性不变量均为零。

下面记两条曲线中任意一条为 $E$。在其极小模型上令
$$
E_1(\mathbb Q_p)\subset E_0(\mathbb Q_p)\subset E(\mathbb Q_p)
\tag{306.13}
$$
为形式群、恒等分支的逆像及完整局部群。
加性约化给
$E_0/E_1\simeq(\mathbb F_p,+)$；
形式对数在 $p>3$ 时给
$E_i\simeq p^i\mathbb Z_p$，$i\ge1$。
所以 $E_0$ 是有限生成的秩一紧致 $\mathbb Z_p$-模。
它没有 $p$ 挠点，因而同构于 $\mathbb Z_p$。
由 $[E_0:E_1]=p$ 及 $pE_0\subset E_1$ 可知
$$
pE_0=E_1,\qquad
p^iE_0=E_i\quad(i\ge1).
\tag{306.14}
$$
此外几何分支群阶至多四，故
$[E:E_0]$ 素于 $p$。若一个属于 $E_0$ 的点在 $E$ 中有
$p^i$ 次原像，该原像的分支类被 $p^i$ 杀掉，
从而原像也在 $E_0$。因此
$$
p^iE\cap E_0=p^iE_0.
\tag{306.15}
$$

在上述极小模型上，两个点的坐标及形式参数分别为
$$
\begin{aligned}
P_a&:\quad
(X,Y)=(a^2p^{-2\ell},p^{-3\ell}),&
t(P_a)&=-a^2p^\ell,\\
Q_a&:\quad
(X,Y)=(ap^{-2\ell},p^{-3\ell}),&
t(Q_a)&=-ap^\ell.
\end{aligned}
\tag{306.16}
$$
若 $\ell=0$，两者均约化为尖点三次曲线 $Y^2=X^3$ 的光滑点
$(1,1)$，位于 $E_0\setminus E_1$。
若 $\ell\ge1$，两者均属于 $E_\ell\setminus E_{\ell+1}$。
结合 (306.14)–(306.15) 就得到 (306.11)。$\square$

## 4. 实际严格 Selmer 群中的非零条件

定义严格的 $p$ 处局部条件
$$
\operatorname{Sel}_p^{\,0}(B_a/\mathbb Q)=
\ker\left(
\operatorname{Sel}_p(B_a/\mathbb Q)
\longrightarrow H^1(\mathbb Q_p,B_a[p])
\right).
\tag{306.17}
$$
这只把 $p$ 处局部条件改为零；其余位置保持原来的 Kummer 条件。
它不是在所有坏素数上同时施加零条件的另一种群。

仍令
$$
\xi_a=\phi_*\delta_{H_a,p}(P_a)
\in\operatorname{Sel}_p(B_a/\mathbb Q).
\tag{306.18}
$$
该类对所有实际 $p>37$ 均有定义；R302 证明
$p>16\,389\,085$ 时它非零。
R301 逐处保持 Kummer 条件，且同构 (306.1) 识别全部局部 $H^1$，
故定理 306.2 给准确判别：
$$
\boxed{
\operatorname{res}_p(\xi_a)\ne0\iff k=1,\qquad
\operatorname{res}_p(\xi_a)=0\iff k\ge2.}
\tag{306.19}
$$
第一种情形也直接证明 $\xi_a$ 在全局非零，
无需 R302 的大 $p$ 数值条件。

因此可将显式类分为两个真实分支：
$$
\boxed{
\begin{array}{ll}
k=1,\ p>37:&
\xi_a\ne0\text{，且在 }p\text{ 处局部像非零};\\
k\ge2,\ p>16\,389\,085:&
0\ne\xi_a\in\operatorname{Sel}_p^{\,0}(B_a/\mathbb Q).
\end{array}}
\tag{306.20}
$$
特别，对全部大 $p$ 的较深参数，
$$
\operatorname{Sel}_p^{\,0}(B_a/\mathbb Q)=0
\quad\Longrightarrow\quad
\text{不存在该实际候选}.
\tag{306.21}
$$
这个条件作用于同一个 $B_a$，不是固定 CM 曲线的严格 Selmer 消失结论的直接套用。

还有一个不要求 $p>16\,389\,085$ 的结论。
若 $L(B_a,1)\ne0$，R302 给
$s_a=\dim_{\mathbb F_p}\operatorname{Sel}_p(B_a/\mathbb Q)
\in2\mathbb Z_{\ge1}$。
由上节的局部群计算，
$$
\dim_{\mathbb F_p}B_a(\mathbb Q_p)/p=1.
\tag{306.22}
$$
因此 $\operatorname{Sel}_p$ 在 $p$ 处的像至多一维，必有
$$
\boxed{
L(B_a,1)\ne0
\Longrightarrow
\dim_{\mathbb F_p}\operatorname{Sel}_p^{\,0}(B_a/\mathbb Q)
\ge1.}
\tag{306.23}
$$
若再有 $k=1$，则 (306.19) 保证局部像恰为一维，从而
$$
\dim_{\mathbb F_p}\operatorname{Sel}_p^{\,0}(B_a/\mathbb Q)
=s_a-1\in2\mathbb Z_{\ge0}+1.
\tag{306.24}
$$
(306.22) 的证明同样适用于 $B_a$：
它在 $p$ 加性约化、没有有理 $p$ 挠点，
恒等分支同构于 $\mathbb Z_p$，分支群素于 $p$。
在偶分支，定理 306.1 使 (306.23) 的前提不成立；
较深参数仍可使用 (306.20) 的明确严格类。

## 5. 三次曲线 Jacobian 的正秩与不相容的 $p$ 惯性

方程 $a^3+db^3=1$ 也给出光滑三次曲线
$$
\mathcal C_d:\ X^3+dY^3=Z^3,
\qquad O=(1:0:1),
\tag{306.25}
$$
上的有理点。以下证明这个曲线的 Jacobian 不能替代实际 CM 参考。

**定理 306.3。** 令
$$
J_d:\ y^2=x^3-432d^2.
\tag{306.26}
$$
则：

1. $(\mathcal C_d,O)$ 与 $J_d$ 有理同构，点 $(a:b:1)$ 的像为
   $$
   R_d=
   \left(
   \frac{12(a^2+a+1)}{b^2},
   \frac{36(a^2+a+1)(a+1)}{b^3}
   \right).
   \tag{306.27}
   $$
2. $J_d(\mathbb Q)_{\mathrm{tors}}=0$，因此 $R_d$ 无限阶，
   $\operatorname{rank}J_d(\mathbb Q)\ge1$ 且 $L(J_d,1)=0$。
3. 对 $J_d$ 的每个有理二次扭曲，模 $p$ 惯性像均为完整
   $C_{\mathrm{ns}}(p)$；实际 $B_a[p]$、$H_a[p]$ 的惯性像为
   $C_{\mathrm{ns}}(p)^3$。因此 $J_d$ 的任何有理二次扭曲都不可能
   与实际 $B_a$ 或 $H_a$ 模 $p$ 同构。

**证明。** 在 $Z\ne X$ 的仿射开集上定义
$$
x=\frac{12dY}{Z-X},\qquad
y=\frac{36d(Z+X)}{Z-X}.
\tag{306.28}
$$
利用 $dY^3=Z^3-X^3$ 直接计算得到
$x^3-y^2=432d^2$。在 $Z=1$ 上的逆映射为
$$
X=\frac{y-36d}{y+36d},\qquad
Y=\frac{6x}{y+36d}.
\tag{306.29}
$$
这给出两条光滑射影曲线的双有理映射，因而延拓为同构，
并把 $O$ 送到无穷远原点。代入 $a^3+db^3=1$ 即得 (306.27)；
$b\ne0$ 保证 $R_d$ 不是原点。

先排除 $J_d$ 的有理二挠点。其 $x$ 坐标须满足
$x^3=432d^2$，但 $p>3$ 且 $v_p(d)=m\in\{1,2\}$，
右端的 $p$ 赋值为 $2m\not\equiv0\bmod3$，不可能为有理立方。
三除多项式为
$$
\psi_3(x)=3x(x^3-1728d^2).
\tag{306.30}
$$
$x=0$ 要求 $y^2=-432d^2<0$，不可能；
另一个因子也因 $p$ 赋值 $2m$ 不是三的倍数而不可能给有理 $x$。
所以没有有理三挠点。

对任意素数 $q\ge5$，若有有理 $q$ 阶点 $T$，
考虑定义在 $K=\mathbb Q(\zeta_3)$ 上的 CM 自同构 $[\zeta_3]$。
若 $T,[\zeta_3]T$ 在 $\mathbb F_q$ 上线性独立，则
$J_d[q]\subseteq J_d(K)$，Weil 配对给 $\mu_q\subset K$，
与 $[K:\mathbb Q]=2<q-1$ 矛盾。
若线性相关，写 $[\zeta_3]T=uT$，
$u\in\mathbb F_q^\times$。
复共轭固定 $T$，并将 $[\zeta_3]$ 共轭成 $[\zeta_3^2]$，
所以 $u^2T=uT$，从而 $u=1$。
再由 $[\zeta_3^2]+[\zeta_3]+1=0$ 得 $3T=0$，仍矛盾。
故不存在任何素数阶有理点，全部有理挠点群平凡。
由此 $R_d$ 无限阶；中心值为零再由 CM 秩零定理的逆否命题得到。

最后核惯性。令 $N=p^2-1$，则 $v_3(N)=1$。
对 $A_t:y^2=x^3+t$，$p>3$、$p\equiv2\bmod3$，
令 $n=v_p(t)\bmod6$。
R258 的直接 CM 形式参数计算给其两个惯性特征为
$$
\omega_2^{\,1-nN/6},\qquad
\omega_2^{\,p(1-nN/6)}.
\tag{306.31}
$$
单位部分的六次根只需不分歧扩张，故不改变这个惯性计算。
在 $J_d$ 的任意二次扭曲上，
$$
n\equiv2m\pmod3.
\tag{306.32}
$$
具体地，$-432d^2$ 在 $p$ 的赋值为 $2m$，
二次扭曲把该赋值增加三的倍数。
由 R258 的实际方向，
$$
mN/6\equiv1\pmod3,
\quad\text{故}\quad
1-nN/6\equiv1-2=-1\pmod3.
\tag{306.33}
$$
同时，$N$ 的每一个不同于三的素因子都整除 $N/6$；
包括二，因为 $24\mid N$。
因此
$$
\gcd(1-nN/6,N)=1.
\tag{306.34}
$$
(306.31) 的像为完整 $C_{\mathrm{ns}}(p)$。
相反，实际 $B_a$ 的系数赋值模三为 $m$，
同一公式的 gcd 准确为三，像为 $C^3$；
$H_a$ 的实际同构保留这个像。
惯性像阶不同，任何局部、进而全局模 $p$ 同构都不可能。$\square$

## 6. 现在可用的全局分支和剩余缺口

对同一个指定 $B_a$，目前得到以下分解：

- $4\mid a$：$B_a$ 已有明确正秩，故中心值为零无法作为排除。
  当 $k\ge2$ 且 $p>16\,389\,085$，实际同余进一步迫使其严格
  $p$-Selmer 群含 (306.18) 的非零类。
- $a\equiv1\bmod16$：已知正秩的是另一个扭曲 $B_a^{(-1)}$。
  实际 $B_a$ 仍须满足 R301 的非零 Selmer 条件和 R302 的中心值二择一；
  若中心值非零，则本篇还迫使严格 $p$-Selmer 群非零。
- 两个分支均有另一条正秩 CM 曲线 $J_d$，
  但它及其所有二次扭曲在 $p$ 的惯性像都不正确。
  不能把它的中心零、Selmer 群或秩直接转给实际 $B_a$。

这些结论为一个实际严格 Selmer 计算指定了对象、类和局部条件，
但没有证明这些随 $d,b$ 变化的严格群统一为零。
特别，某条固定 CM 曲线已有的严格 Selmer 消失定理，
若没有处理这里变化的六次扭曲导子，就不能用于 (306.21) 或 (306.23)。
当前尚无反向导子上界，也尚未排除整个正秩偶分支。

## 7. 来源和依赖

- [R258](R258-sextic-cm-normal-form-and-exact-integral-j-level.md)，
  实际有理六次 CM 下降、小惯性方向
  $m=2$ 或 $1$、以及式 (258.9) 的两个准确惯性特征。
- [R289](R289-dyadic-supersingularity-and-actual-integral-cubic-normal-form.md)，
  实际二进符号和整数正规形；
  [R294](R294-cartan-scalars-hasse-vanishing-and-exact-inertia.md)
  的非约化 Hasse 消失给这里 $k=v_p(b)\ge1$。
- [R301](R301-universal-selmer-transport-and-canonical-cm-obstruction.md)，
  实际 Kummer 条件运输及 $P_a$；
  [R302](R302-explicit-selmer-class-and-cm-central-value-divisibility.md)，
  显式点的绝对可除性界、中心非零时有限 $\Sha$ 及正偶数 Selmer 维数。
- A. Burungale、M. Flach，
  *The conjecture of Birch and Swinnerton-Dyer for certain elliptic curves with complex multiplication*，
  Cambridge Journal of Mathematics **12** (2024), 357–415，
  Theorem 1.1、Corollary 2，
  [期刊全文](https://par.nsf.gov/servlets/purl/10609724)，第 359、362 页。
  本篇只用其 $L(C,1)\ne0\Rightarrow C(\mathbb Q)$ 有限的已证明结论。
- 局部约化过滤、形式对数及标准除法多项式：
  J. H. Silverman，*The Arithmetic of Elliptic Curves*，2nd ed., 2009，
  Chapters III、IV、VII。本篇已展开所需深度、分支群及两个点的全部具体计算。

本文为纯证明产物，证明不依赖数值搜索；无数据证书或验证脚本。主要目标仍为 OPEN。
