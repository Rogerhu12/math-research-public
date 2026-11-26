# R1012：原 p-similitude 的四个 divided 高坐标与临界系数桥

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；o1_theta / root。

**已证明：每个 norm −1 方向的实际 p-similitude、首极块的完整抵消，以及四个 divided 高坐标的差分到原临界系数的单位倍数桥。原同标签临界非零仍 OPEN。** 特别得到同一原函数的平衡导数系数等于 \((B/5)\kappa^p(\beta\overline\alpha)^{p-3}H_p(\kappa)\)。这里证明准确比较，不预设这两个等价读数非零；原 primitive 和 Legendre 因子继续保留。

## 1. 每个 norm −1 方向恰有十二个表示

令
\[
\mathcal O=\mathbf Z[\zeta],\quad \zeta^2+\zeta+1=0,\quad
K=\mathbf Q(\zeta),\qquad
N(a+b\zeta)=a^2-ab+b^2.
\]
设 \(p\ge5,\ p\equiv2\pmod3\)。于是
\(\mathcal O/p=\mathbf F_{p^2}\)，模 \(p\) 的共轭为 \(x\mapsto x^p\)。记
\[
T^-=\{\kappa\in\mathbf F_{p^2}^{\times}:\kappa^{p+1}=-1\},
\qquad |T^-|=p+1,
\]
\[
L_\kappa=\{(a,b)\in\mathcal O^2:a\equiv\kappa b\pmod p\}.
\]

**定理。** 对每个 \(\kappa\in T^-\)，恰有十二个有序向量
\(v=(\alpha,\beta)\in\mathcal O^2\) 满足
\[
N\alpha+N\beta=p,\qquad \alpha\equiv\kappa\beta\pmod p.
\tag{1012.1}
\]
任取一个，置 \(v'=(-\overline\beta,\overline\alpha)\)，则
\[
L_\kappa=\mathcal Ov\oplus\mathcal Ov',
\qquad
\langle v,v\rangle=\langle v',v'\rangle=p,\qquad
\langle v,v'\rangle=0.
\tag{1012.2}
\]
十二个向量正是 \(\epsilon v,\epsilon v'\)，\(\epsilon\in\mu_6\)。

### 总表示数

\(\mathcal O^2\) 作为偶 \(\mathbf Z\)-格的 Gram 矩阵为
\[
\operatorname{diag}(A_2,A_2),\qquad
A_2=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
\]
其行列式为九、水平为三。以下给完整低权 theta 恒等式，不作有限插值。

令
\[
\Theta_{\mathcal O^2}(\tau)
 =\sum_{\alpha,\beta\in\mathcal O}q^{N\alpha+N\beta}.
\]
Poisson 求和给
\(\Theta_{\mathcal O^2}|_2S=-\Theta_{(\mathcal O^2)^*}/3\)；
对偶格的 theta 级数在 \(T^3\) 下不变。再对对偶格用 Poisson，
可得原 theta 在
\(\begin{psmallmatrix}1&0\\3&1\end{psmallmatrix}\) 下不变。
它与 \(T,-I\) 生成 \(\Gamma_0(3)\)。两个尖点的全纯性由这两个正定 theta 级数得到。因此
\[
\Theta_{\mathcal O^2}\in M_2(\Gamma_0(3))
\]
且角色平凡。

同空间的形式
\[
E(\tau)=\frac{3E_2(3\tau)-E_2(\tau)}2
\]
在无穷尖点的常数项为一，等于 \(\Theta_{\mathcal O^2}\) 的常数项。
\(\Gamma_0(3)\) 指数为四；权二非零全纯形式的 valence 总重为 \(2/3\)。
若二者之差非零，它在无穷尖点至少一阶消失，已经超过总重。因此
\[
\boxed{\quad
\Theta_{\mathcal O^2}
=\frac{3E_2(3\tau)-E_2(\tau)}2
=1+12\sum_{n\ge1}
 \bigl(\sigma_1(n)-3\sigma_1(n/3)\bigr)q^n.
\quad}
\tag{1012.3}
\]
非整数输入的 \(\sigma_1(n/3)\) 记为零。故 \(p\ne3\) 时，总表示数准确为
\[
r_{\mathcal O^2}(p)=12(p+1).
\tag{1012.4}
\]

### 逐方向计数

若 \(N\alpha+N\beta=p\)，则 \(N\alpha,N\beta\) 都在 \(1,\ldots,p-1\)。
否则 \(p\) 是 \(\mathcal O\) 中一个元素的 norm，与惰性矛盾。
于是 \(\beta\bmod p\ne0\)，且
\[
\kappa=\alpha/\beta\bmod p,\qquad
\kappa^{p+1}=-1.
\]
每个表示恰落在一个 \(L_\kappa\)。

若 \(L_\kappa\) 含一个 norm \(p\) 向量 \(v\)，则
\[
-\overline\beta-\kappa\overline\alpha
=-(1+\kappa\kappa^p)\overline\beta=0\pmod p,
\]
所以 \(v'\in L_\kappa\)。矩阵
\[
A_v=[v\ v']
=\begin{pmatrix}\alpha&-\overline\beta\\
                 \beta&\overline\alpha\end{pmatrix},
\qquad \det A_v=p,
\tag{1012.5}
\]
给出的子格 \(\mathcal Ov+\mathcal Ov'\) 在 \(\mathcal O^2\) 中的
\(\mathbf Z\)-指数为 \(N(p)=p^2\)；\(L_\kappa\) 的指数也为 \(p^2\)，
因为 \((a,b)\mapsto a-\kappa b\) 满射到 \(\mathcal O/p\)。故两格相等。

其 Gram 矩阵为 \(pI\)，所以 norm \(p\) 向量恰对应 \(\mathcal O^2\)
中的 norm 一向量；后者只有 \((\epsilon,0),(0,\epsilon)\)，共十二个。
每个方向的表示数于是为零或十二。结合 (1012.4) 和方向总数 \(p+1\)，
每个方向必须恰有十二个表示。这证明 (1012.1)–(1012.2)。

## 2. 同一个原椭圆源的实际同源

现在回到原范围 \(p=6N+5\ge41\)，并保持
\[
E_0:y^2=x^3-1,\qquad dz=\frac{dx}{2y},\qquad
\sigma(z)=z+O(z^7),\qquad D_z^2\log\sigma=-x.
\]
使用 [R770](R770-same-primitive-label-square-and-finite-bilinear-pairing.md)
的原函数和普通 Taylor 系数：
\[
F=x\sigma^6=\sum_{i\ge0}f_i z^{6i+4},\qquad
G=-xy\sigma^6=\sum_{j\ge0}g_j z^{6j+1},\qquad f_0=g_0=1.
\tag{1012.6}
\]
仅在已证整的有限范围内约化。

矩阵 (1012.5) 是实际的 \(E_0^2\) 自同源，且
\[
A_v^\dagger A_v=[p]I,\qquad \deg A_v=p^2.
\tag{1012.7}
\]
这里 \(\dagger\) 是相对于乘积主极化的 Rosati 共轭转置。
因此拉回的乘积极化为原极化的 \(p\) 倍；不能将它当成保持原 index 的自作用。

在原加性形式坐标中记
\[
u=\alpha z-\overline\beta t,\qquad
w=\beta z+\overline\alpha t.
\tag{1012.8}
\]
模 \(p\) 的微分像是直线 \(\{(\kappa a,a)\}\)，因为
\(u\equiv\kappa w\) 且 \(\beta\) 为单位。实际拉回就是
\[
A_v^*(F\boxtimes G)=F(u)G(w);
\]
此处没有选择新的 Gaussian 或对原 CM 源换规范。

R702 §2 已证明原 \(F,G\) 在所有次数小于 \(p\) 的系数为 \(p\)-整。
因此临界总次数 \(d=p-6\) 满足
\[
\boxed{\quad
\overline{[A_v^*(F\boxtimes G)]_{p-6}}
 =H_p(\kappa)\,w^{p-6},\qquad
H_p(\kappa)=\sum_{i+j=N-1}
 \kappa^{6i+4}\,\overline f_i\,\overline g_j.
\quad}
\tag{1012.9}
\]
方括号表示总次数的齐次部分；右侧的 \(w\) 已约化。
这把每一个 norm \(-1\) 方向实现为真正的 \(p\)-同源，但没有证明
\(H_p(\kappa)\) 或其原筛选版本非零。

## 3. 原 first-pole 在矩形中的真实抵消

本节固定
\[
\mathcal R_p=\{z^at^b:0\le a,b<p\},
\]
只取这个矩形的实际普通 Taylor 系数，总次数至多 \(2p-2\)。
不能先将整个非整 sigma 级数约化。

R702 使用同一个单位 \(B\) 构造 \(p\)-整有限级数 \(F_0,G_0\)，并给
\[
pF(z)\equiv-6Bz^{p+1}F_0(z),\qquad
pG(z)\equiv-6Bz^{p+1}G_0(z)\pmod{p,z^{2p}}.
\tag{1012.10}
\]
\(F-F_0\) 始于次数 \(p+5\)，\(G-G_0\) 始于次数 \(p+2\)。
选同一个整升换 \(a\equiv-6B\pmod p\)，在这个有限范围内置
\[
F_{\rm reg}=F-\frac ap z^{p+1}F_0,\qquad
G_{\rm reg}=G-\frac ap z^{p+1}G_0.
\tag{1012.11}
\]
两者均整；它们与 \(F_0,G_0\) 的差仍分别始于 \(p+5,p+2\)。

将 (1012.11) 代入 \(F(u)G(w)\)。在总次数不超过 \(2p-2\) 时，
可以把两个极项的伴随因子分别换成 \(G_0(w),F_0(u)\)：
误差及二重极项最早总次数均为 \(2p+7\)。所以唯一需审的非整块为
\[
\frac ap\bigl(u^{p+1}+w^{p+1}\bigr)F_0(u)G_0(w).
\tag{1012.12}
\]

考察 \(u^{p+1}+w^{p+1}\) 的系数：
\[
[z^rt^{p+1-r}]
  \bigl(u^{p+1}+w^{p+1}\bigr)
=\binom{p+1}{r}
 \left(\alpha^r(-\overline\beta)^{p+1-r}
       +\beta^r\overline\alpha^{\,p+1-r}\right).
\tag{1012.13}
\]
对 \(2\le r\le p-1\)，二项式系数含 \(p\)。括号中的和也含 \(p\)，
因为模 \(p\) 有
\[
\alpha=\kappa\beta,\qquad
-\overline\beta=\kappa\overline\alpha,\qquad
\kappa^{p+1}=-1.
\]
所以这些中间系数含 \(p^2\)。剩余 \(r=0,1,p,p+1\) 的单项式均在
\(\mathcal R_p\) 之外；乘以整的非负幂级数也不能重新进入矩形。
故 (1012.12) 在矩形中的系数均属于 \(p\mathcal O_{K,p}\)。

结论是：整个实际拉回在 \(\mathcal R_p\) 中为整，其约化准确等于
\[
\boxed{\quad
F_{<p}(\kappa w)\,G_{<p}(w)
\quad\text{于 }
\mathbf F_{p^2}[z,t]/(z^p,t^p).
\quad}
\tag{1012.14}
\]
这里 \(F_{<p},G_{<p}\) 是原低阶截断。正则整高带含 \(u^p\) 或 \(w^p\)，
约化后也消失；因为 \(w^p=0\) 于此环，(1012.14) 中总次数至少 \(p\) 的部分为零。

所以这一批实际 \(p\)-同源的第一次 first-pole carry **确实相消**。
它不产生一个可直接降到 (1012.9) 的已知非零首层。下一层必须保模 \(p^2\)
矩阵升换、原 \(F_{\rm reg},G_{\rm reg}\) 的实际整高带，不能只保首极留数。

还有两个准确的原坐标恒等式，可供下一层使用：
\[
\lambda=\alpha/\beta,\qquad
u=\lambda w-\frac p\beta t,\qquad
\mathscr L=\overline\alpha\,\partial_z-\beta\,\partial_t,
\]
\[
\mathscr Lw=0,\qquad \mathscr Lu=p,\qquad
\mathscr L^k(F(u)G(w))=p^kF^{(k)}(u)G(w).
\tag{1012.15}
\]
它们保留真实的特征零矩阵，不将 \(\lambda\) 擅换成某个 Teichmüller 升换。

## 4. 四个 divided 高坐标准确消去未知整高带

本节在自由的 \(\mathcal O_{K,p}\)-模
\[
R=\mathcal O_{K,p}[z,t]/(z^p,t^p)
\]
内保持原有限级数和总次数，先证明可整除再除以 \(p\)。
原特征零微分在未截断级数中使用，不将它擅称为 \(R\) 的导子。

置
\[
d=2p-5,\qquad k_j=p-j,\qquad l_j=p-5+j,
\]
\[
Q_j=[z^{k_j}t^{l_j}]F(u)G(w),\qquad 1\le j\le4.
\tag{1012.16}
\]
四个位置都严格在原矩形内。由 (1012.14)，\(Q_j\in p\mathcal O_{K,p}\)。
定义单位
\[
b_j=-\frac{(j-1)!(4-j)!}{24},
\qquad
q_j=\overline{\frac{Q_j}
 {p\,b_j\,\beta^{k_j}\overline\alpha^{\,l_j}}}
 \in\mathbf F_{p^2}.
\tag{1012.17}
\]
\(\alpha,\beta\) 的 norm 都在 \(1,\ldots,p-1\)，所以这里的全部显示分母，
除已处理的 \(p\) 外，均为单位。

以下有限域等式中的 \(\alpha,\beta,a\) 直接表示对应整元素的约化；
\(\overline\alpha\) 始终表示 CM 共轭的约化。

**定理 1012.1。** 四个实际高坐标满足
\[
\boxed{\quad
q_{j+1}-q_j
 =\frac{a\kappa^p}{5\beta\overline\alpha}\,
 H_p(\kappa),\qquad j=1,2,3.
\quad}
\tag{1012.18}
\]
系数是单位。证明必须同时控制未知整高带与首极块，不能只算后者。

### 4.1 两个基本方向

Wilson 定理给
\[
\frac1p\binom{2p-5}{p-j}\equiv b_j\pmod p.
\tag{1012.19}
\]
确切地，\((2p-5)!/p\equiv1/24\)，两个分母阶乘的积约化为
\(-1/((j-1)!(4-j)!)\)。

在 \(R\) 中 \(w^p\in pR\)：纯端项已被取商消去，其余二项式系数含 \(p\)。
因此
\[
J_w=\frac{w^p}{p}\in R
\tag{1012.20}
\]
是合法且唯一的整元素。四个所需位置满足
\[
\frac1p[z^{k_j}t^{l_j}]w^d
 \equiv b_j\beta^{k_j}\overline\alpha^{\,l_j},
\]
\[
\frac{\binom{d-1}{k_j}}{\binom d{k_j}}
 =\frac{d-k_j}{d}\equiv\frac{5-j}{5}\pmod p.
\tag{1012.21}
\]
第二式的分子、分母同含一个 \(p\)，其约化是先取这个有理比值再约化，
没有在有限域中除以零。

### 4.2 未知整高带只进共同常数

把 \(F_{\rm reg}(u)G_{\rm reg}(w)\) 的总次数 \(d\) 部分写成
\[
\sum_m c_mu^mw^{d-m},\qquad c_m\in\mathcal O_{K,p}.
\]
用准确等式 \(u=\lambda w-pt/\beta\) 展开。零阶项是
\((\sum_mc_m\lambda^m)w^d\)。
一次横向项带一个 \(p\)，且正比于 \(tw^{d-1}\)；
四个所需系数的 \(\binom{d-1}{p-j}\) 又都含 \(p\)，因为
\(d-1=2p-6\) 的低 \(p\) 位为 \(p-6<p-j\)。
二次以上项自带 \(p^2\)。

因此在这四个系数中除以 \(p\) 并约化后，全部未知整高带只贡献
\[
R_dJ_ww^{p-5}
\tag{1012.22}
\]
这一个方向，\(R_d\in\mathbf F_{p^2}\) 保留为未知标量。
这里仅断言四个指定坐标的相等，不把 (1012.22) 宣称为整个商环中的恒等式。

### 4.3 完整首极块的第二层

置
\[
A_\lambda=\frac{\lambda^{p+1}+1}{p}\in\mathcal O_{K,p}.
\]
二项展开在 \(R\) 中给
\[
\frac{u^{p+1}+w^{p+1}}{p^2}
 \equiv J_w\left(A_\lambda w-\frac{\kappa^p}{\beta}t\right)
 \pmod p.
\tag{1012.23}
\]
左侧在 \(R\) 中确实整：零阶项为 \(pA_\lambda w^{p+1}\)，
一次项为 \(-p(p+1)\lambda^ptw^p/\beta\)，均因 \(w^p\in pR\)
再含一个 \(p\)；二次至 \(p-1\) 次项含
\(\binom{p+1}{r}p^r\subset p^3\)，最后两项更高。

由 §3 的完整次数预算，极部分在总次数 \(d\) 只剩 (1012.12)。
该项在 \(R\) 中已有一个 \(p\)，所以再除以 \(p\) 后，其伴随因子只需模 \(p\)：
\[
[F_0(u)G_0(w)]_{p-6}
 \equiv H_p(\kappa)w^{p-6}.
\]
结合 (1012.22)–(1012.23)，在四个指定坐标中，完整除 \(p\) 的约化为
\[
(R_d+aA_\lambda H_p(\kappa))J_ww^{p-5}
-\frac{a\kappa^p}{\beta}H_p(\kappa)J_ww^{p-6}t.
\tag{1012.24}
\]
全部整高带、极部分和真实矩阵升换均已包括。

按 (1012.17) 归一化，再用 (1012.21)，得到
\[
q_j=R_d+aA_\lambda H_p(\kappa)
-\frac{a\kappa^p}{5\beta\overline\alpha}(5-j)H_p(\kappa).
\]
相邻差消去两个共同常数，准确给出 (1012.18)。

### 4.4 同一个桥的原一阶导数版本

保原加性参数的普通导数 \(F'=dF/dz\)，不换成模参数导数或新的连接规范。
有更紧凑的实际平衡系数公式：
\[
\boxed{\quad
\overline{[z^{p-3}t^{p-3}]F'(u)G(w)}
 =\frac B5\,\kappa^p(\beta\overline\alpha)^{p-3}H_p(\kappa).
\quad}
\tag{1012.25}
\]
左侧在原 \(p\)-进模型中为整；\(B\) 是 R702 的同一个单位
\[
B=(-1)^{N+1}\binom{3N+2}{2N+1}\pmod p.
\]
(1012.25) 的所有外乘因子都是单位，但它不是 bare Kronecker 系数的重命名。

直接证明如下。对 (1012.11) 求原参数导数；在总次数 \(D=2p-6\) 中，
换伴因子误差及二重极项最早总次数 \(2p+6\)，均在范围之外。剩下
\[
F_{\rm reg}'(u)G_{\rm reg}(w)
+\frac ap\left\{
 (p+1)u^pF_0(u)G_0(w)
 +(u^{p+1}+w^{p+1})F_0'(u)G_0(w)
\right\}.
\tag{1012.26}
\]
第一项整，且模 \(p\) 的总次数为 \(D\ge p\)，故在 \(R\) 中为零。
大括号第二项经除 \(p\) 后仍在 \(pR\)，由 (1012.23) 可见。
第一项整，因为 \(u^p\in pR\)，而
\[
u^p/p\equiv\kappa^pJ_w\pmod p.
\]
于是所需系数就是
\[
a\kappa^pH_p(\kappa)\,
 [z^{p-3}t^{p-3}]\,w^{2p-6}/p.
\]
Wilson 公式再给
\[
\frac1p\binom{2p-6}{p-3}\equiv-\frac1{30}\pmod p.
\]
代入 \(a\equiv-6B\) 得到 (1012.25)。

也可从未截断级数中的 (1012.15)
\(\mathscr L(F(u)G(w))=pF'(u)G(w)\) 取严格内部的平衡系数，
得到四高坐标的中间差。此核对保留了商环边界；
没有把普通微分错误地下降到特征零的截断商环。

**精确后继目标。** 继续识别 (1012.25) 左侧或 (1012.18) 四个 \(Q_j\)
的真实 theta/Poincaré 来源，并证明所需原筛选读数非零。
本篇只证明同一个源的单位倍数桥，未证明任何一侧非零，
也未建立它与 O2 的 bare \(c_{p-r}^{\pm}\) 的单位等价。

## 5. Gaussian 指标与原筛选仍不能删除

R812 的 Gaussian 频率属于 \(\mathbf Z^2\)，并在 split 情形使用
\(\iota\in\mathbf F_p\)，故
\[
(a+\iota b)^{p-1}
 =1-\mathbf1_{a+\iota b=0}.
\]
本篇的频率一般属于 \(\mathcal O\)，约化落在 \(\mathbf F_{p^2}\)。
对非零 \(L\)，\(L^{p-1}=L^p/L\) 是共轭比值，并非一。

真正的零指标必须写作
\[
N(L)^{p-1}=L^{p^2-1}.
\]
其中 norm 是原频率的二次形式，所以作为频率多项式的总次数为
\(2p-2\)。逐方向同源覆盖不能据此照搬 R812 的低五阶 Frobenius 公式；
它恰把问题带回原高 balanced 层及 §§3–4 已完整保留的 carry；
四高坐标差分提供准确下降公式，仍须为其左侧给出非零来源。

原标签仍为 \(h=6i+7\)，必须同时保留
\[
(h,p+1)=1,\qquad P_{h-1}(1/s),\qquad s^2=-3.
\]
式 (1012.9) 仅给未经这两项处理的真实源。本文既未删除 mask，
也没有由同源存在性、矩形高层零或 norm 指标推出原同 \(h\) 非零。

## 6. 依赖与核准

- [R702](R702-first-pole-block-and-uniform-shifted-units.md) §2：原有限 \(F_0,G_0\)、首极块及准确起始次数；本篇未重新计算其系数。
- [R770](R770-same-primitive-label-square-and-finite-bilinear-pairing.md)：原 \(F,G,f_i,g_j\)、临界总次数、真本原筛选和 Legendre 因子。
- [R812 的原 Gaussian 源](R812-original-apolar-source-and-Gaussian-Frobenius-low-moment.md)：原 split 指标及其低阶来源。旧同源输入不包含本篇逐 \(\kappa\) 的十二表示结论。
- theta 计数、逐方向格、矩阵同源及四高坐标/原导数桥在上文给出纸面证明。o1_theta 与 root 独立核准；root 特别复核极项的完整正则分拆、\(2p+7\)/\(2p+6\) 误差阈值、矩形外端点、两个 Wilson 常数及整高带只进共同方向。没有数学程序执行，也没有重跑有限窗口。
