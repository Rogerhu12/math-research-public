# 全权一 Gauss–Manin 周期与普通、惰性的准确除素数行

日期：2026-11-12。状态：固定代数模函数、全部尺度、两条临界行、
Legendre 截断及首个非临界分母均已证明。
没有把形式系数 Frobenius 当成已经构造的 crystalline 比较，
也没有证明新的无穷素数非零结论。

## 1. 使用真正的中央 Borel

沿用 [R47](../results/R47-central-borel-modular-form-and-exact-growth.md)：
\[
\mathscr B(T)=\sum_{m\ge0}m!e_mT^m
 =\frac{\mathcal G(i(1+w)/(1-w))}
        {f\Omega_E(1-w)},\qquad w=\frac{T}{A_Ef^2},
\tag{1}
\]
其中 \(\mathcal G\) 是实际固定权一模形式，
\(A_E=\Omega_E^2/\pi_{\mathbb C}\)、\(f=34(1+i)\)。
这是全中央对角的准确恒等式；
没有把半权 \(F\) 的 Taylor 卷积平方认作其逐项平方。

取[半权 GM 笔记](2026-11-12-critical-gauss-manin-legendre-lift.md)
的模参数、周期和水平坐标：
\[
t=\lambda_{\rm Leg}-\tfrac12,\qquad
\mathscr D y=(1-4t^2)y''-8ty'-y=0,
\]
\[
K(0)=1,\ K'(0)=0,\quad L(0)=0,\ L'(0)=1,\quad
J=L/t,\quad u=L/K.
\tag{2}
\]
\(t\) 不是椭圆正式参数。Wronskian 给
\[
\frac{du}{dt}=\frac1{(1-4t^2)K^2}.
\tag{3}
\]
原点的 Cayley 坐标为 \(w=\gamma u\)，
\(\gamma=-\pi_{\mathbb C}/\Omega_0^2\)，
\(\Omega_E=17^{-1/4}\Omega_0\)。故准确缩放是
\[
q_0=\gamma A_Ef^2=-f^2/\sqrt{17}=-8i\,17^{3/2}.
\tag{4}
\]
R51 给 \(e_4=25/(2^9 17^{10})\ne0\)。定义
\[
\mathcal B_1(u)=
\frac{\mathscr B(q_0u)+\mathscr B(-q_0u)}
     {2\cdot24e_4q_0^4}=\sum_{m\ge0}C_mu^m.
\tag{5}
\]
中央对角只允许 \(m\equiv0,1\pmod4\)；
所以 (5) 只保留 \(4\mid m\)，且 \(C_4=1\)。
归一化后的实际对象满足
\[
\boxed{\quad \mathcal B_1(u)=K(t(u))M_1(t(u)),\qquad
                   M_1(t)=t^4+\tfrac72t^6+\cdots.\quad}
\tag{6}
\]

这里 \(M_1\) 是素数变化之前固定的代数函数。
确实，\(\mathcal G/(2\pi_{\mathbb C}i\,\vartheta_3^2)\)
是共同有限级别上的代数模函数；\(2\pi_{\mathbb C}i\)
消去 zeta/Eisenstein Fourier 展开中的共同超越常数。
又
\[
(1-w)^{-1}\vartheta_3(\tau(w))^2
                   =\vartheta_3(i)^2K(t).
\]
取偶部分并除非零的四次系数，正好得到 (6)。
因此代数性论证里没有遗留未经消去的周期常数。

令 \(A_1(z)=\sum\beta_mz^m\) 为 R51 在 \(D=1\) 的实际截面，
\(\beta_4=1\)、\(\beta_8=97/60\)。
R51 的平方公式及 \(D\)-缩放准确给
\[
\boxed{\quad
C_m=\frac{m!}{24}\frac{e_m}{e_4}q_0^{m-4}
    =\frac{m!}{24\,17^{m-4}}\beta_m^2
       \quad(4\mid m),\qquad C_m=0\ (4\nmid m).
\quad}
\tag{7}
\]
特别是所有 \(C_m\) 有理。由 (2)、(6) 反解，\(M_1\) 的所有
Taylor 系数也有理；它为偶函数，故是
\(\mathbb Q(t^2)\) 上的固定代数 germ。
在有限覆盖上，\(KM_1\) 确实是秩二 Gauss–Manin 系统的
一个 period，对应把不变微分乘以代数函数 \(M_1\)。
这没有宣称 \(u\)-展开仍属于有限秩线性系统。

以下准确取 \(\Sigma=\{2,3,5,17\}\)。
[固定除法单位模型](2026-11-12-weight-one-division-unit-relative-model.md)
已用原来全部 \(68\) 阶挠点的 étale 整模型、
\(D\Psi_{68}(P)\) 的单位性及准确归一常数证明
\[
M_1\in\mathbb Z_p[[t]]\qquad(p\notin\Sigma).
\tag{8}
\]
不需要另加未计算的覆盖判别式或分支坏位。

## 2. 准确留数与两个整数 \(p\) 次幂

由 (3)、(6)，对每个 \(n\ge0\) 有
\[
\boxed{\quad
C_n=\operatorname{res}_{t=0}
 \frac{M_1K^n}{(1-4t^2)L^{n+1}}\,dt
 =[t^n]\frac{M_1K^n}{(1-4t^2)J^{n+1}}.
\quad}
\tag{9}
\]
写 \(\zeta=K/L=1/u\)，等价地
\[
\boxed{\quad C_n=-\operatorname{res}_{t=0}
                         M_1K\,\zeta^{\,n-1}d\zeta.\quad}
\tag{10}
\]
负号和指数来自 \(du/u^{n+1}=-\zeta^{n-1}d\zeta\)。
因此惰性 \(n=p+1\) 恰有整数幂 \(\zeta^p\)；
普通 \(n=p-1\) 则为 \(\zeta^{p-2}\)，二者不能混用。

固定
\[
B=K/J=1+O(t^2),\qquad \ell=\log B,\qquad
W_i=\frac{M_1K}{(1-4t^2)J^2},\quad
W_o=\frac{M_1}{(1-4t^2)K}.
\tag{11}
\]
两个 \(W\) 都从 \(t^4\) 开始，首系数为 \(1\)。准确地
\[
C_{p+1}=[t^{p+1}]W_iB^p,\qquad
C_{p-1}=[t^{p-1}]W_oB^p.
\tag{12}
\]
它们使用同一个固定 \(M_1,K,L\)。

## 3. 惰性的第一除 \(p\) 行

设 \(p\equiv3\pmod4\)、\(p\ge7\)、\(p\notin\Sigma\)。
由于 \(M_1\) 起于 \(t^4\)，(12) 第一式只需 \(K,J,B\)
到次数 \(p-3\)，亦即 \(L\) 到次数 \(p-2\)。
周期递推
\[
c_{n+2}=\frac{(2n+1)^2}{(n+1)(n+2)}c_n
\tag{13}
\]
在这个范围没有除以 \(p\)。
取对数和展开指数时，所需乘积项数至多 \((p-3)/2<p\)，
也不引入 \(p\) 分母。因此
\[
C_{p+1}\equiv[t^{p+1}]W_i+
             p[t^{p+1}]W_i\ell\pmod{p^2}.
\tag{14}
\]
由 (7)、实际 \(\beta_{p+1}\) 的整性及 \(v_p((p+1)!)=1\)，
\[
v_p(C_{p+1})=1+2v_p(\beta_{p+1})\ge1.
\tag{15}
\]
故 (14) 也证明 \([t^{p+1}]W_i\in p\mathbb Z_p\)。

定义固定的 Euler 原函数和行
\[
(t\partial_t-1)Z_i=W_i,\qquad [t]Z_i=0,\qquad
\mathcal G_i=Z_i+W_i\ell .
\tag{16}
\]
其余系数是 \([t^n]Z_i=[t^n]W_i/(n-1)\)。于是
\[
\boxed{\quad
\frac{C_{p+1}}p\equiv[t^{p+1}]\mathcal G_i\pmod p.
\quad}
\tag{17}
\]
该值非零准确等价于 \(\beta_{p+1}\) 为 \(p\) 单位，
因而是 R50/R54 的 Sha 有限性充分判据。
这里没有把首层判据称作完整导数判据。

### 3.1 延长的 Legendre 替换不经过 \(t^p\) 修正

令 \(a=(p-1)/2\) 为奇数，取
\[
\widetilde L=\frac{P_a(2t)}{2P_a'(0)},\qquad
\widetilde K=\frac{Q_a^{\rm Leg}(2t)}{Q_a^{\rm Leg}(0)}.
\tag{18}
\]
它们与 \(L,K\) 的初值相同，并满足
\(\mathscr D\widetilde L=-p^2\widetilde L\)、
\(\mathscr D\widetilde K=-p^2\widetilde K\)。
由 (13)，所需分母仍是 \(p\) 单位，故
\[
\widetilde L\equiv L\pmod{p^2,t^{p-1}},\qquad
\widetilde K\equiv K\pmod{p^2,t^{p-2}}.
\tag{19}
\]
所以 \(\widetilde J=\widetilde L/t\) 与 \(J\)
在 (14) 的全部相关 jet 中模 \(p^2\) 一致。
实际 \(L\) 在 \(t^p\) 项有赋值 \(1\) 的新增修正；
这里没有将它误删，而是 \(M_1\) 的四阶零点使它不进入目标。
\(K\) 首个非整项 \(t^{p+1}\) 同样不进入。

因此 (14)、(17) 可使用显式 Legendre 多项式及其第二解。
第二解只含对数 \(\log((1+2t)/(1-2t))\) 与有理多项式；
但多项式次数仍为 \((p-1)/2\)，不是固定次数的模型。

## 4. 普通的第二除 \(p\) 行

设 \(p\equiv1\pmod4\)、\(p\ge13\)、\(p\notin\Sigma\)。
(12) 第二式只需 \(K,J,B\) 到次数 \(p-5\)。
这些系数均整，所需对数及指数项数小于 \(p\)。故
\[
C_{p-1}\equiv[t^{p-1}]
 \left(W_o+pW_o\ell+\frac{p^2}{2}W_o\ell^2\right)\pmod{p^3}.
\tag{20}
\]
R58 的实际普通整除及 (7) 给
\[
v_p(C_{p-1})=2v_p(\beta_{p-1})\ge2.
\tag{21}
\]
定义固定的第二行
\[
\boxed{\quad
\mathcal G_o=(t\partial_t+1)^{-2}W_o
 +(t\partial_t+1)^{-1}(W_o\ell)+\tfrac12W_o\ell^2.
\quad}
\tag{22}
\]
Euler 逆逐项除以 \(n+1\)，不存在自由的齐次解。得到
\[
\boxed{\quad
\frac{C_{p-1}}{p^2}\equiv[t^{p-1}]\mathcal G_o\pmod p.
\quad}
\tag{23}
\]
右侧三个分量可以各自非整；(20)–(21) 证明的是它们的
准确和在该系数整。不能把 \([t^{p-1}]W_o\) 单独说成被 \(p^2\) 整除。
(23) 非零准确等价于 \(v_p(\beta_{p-1})=1\)，
从而给同一固定曲线的普通首层有限性充分判据。

## 5. 首个非临界分母不会被中央条件自动消去

所需周期估计可直接由
\[
[t^{2r}]K=
 \frac{\prod_{j=0}^{r-1}(4j+1)^2}{(2r)!},\qquad
[t^{2r}]J=
 \frac{\prod_{j=0}^{r-1}(4j+3)^2}{(2r+1)!}
\tag{24}
\]
核查，也与[完整周期分母笔记](2026-11-12-gauss-manin-period-denominators.md)
一致。

惰性处 \(K\) 首非整项为 \(t^{p+1}\)，赋值 \(-1\)；
\(J\) 至少到 \(t^{p+5}\) 都整。置
\(\kappa_p=p[t^{p+1}]K\in\mathbb Z_p^\times\)。
由于 \(M_1=t^4+\cdots\)，
\[
p[t^{p+5}]W_i\equiv\kappa_p,\qquad
p[t^{p+5}]W_i\ell\equiv\kappa_p\pmod p.
\]
Euler 原函数在这一系数只除以 \(p+4\)，所以
\[
\boxed{\quad
p[t^{p+5}]\mathcal G_i\equiv\tfrac54\kappa_p\not\equiv0\pmod p.
\quad}
\tag{25}
\]
所有更低系数均整：唯一可能的额外 Euler 分母在次数 \(p+1\)，
已由 (14)–(15) 消去。首坏次数因此准确为 \(p+5\)。

普通处 \(J\) 首非整项为 \(t^{p-1}\)，赋值 \(-1\)；
\(K\) 至少到 \(t^{p+3}\) 都整。置
\(\eta_p=p[t^{p-1}]J\in\mathbb Z_p^\times\)。
\(\ell\) 在次数 \(p-1\) 的非整剩余为 \(-\eta_p/p\)，
故 \(W_o\ell\) 首坏次数为 \(p+3\)。
同阶的 \(W_o\ell^2\) 仍整，因为 \(\ell\) 没有常数项且从二阶开始。
因此
\[
\boxed{\quad
p[t^{p+3}]\mathcal G_o\equiv-\tfrac14\eta_p\not\equiv0\pmod p.
\quad}
\tag{26}
\]
更低系数整；次数 \(p-1\) 的三项消去由 (20)–(21) 保证。
所以普通的首坏次数准确为 \(p+3\)。

这里仅排除把中央一个系数的额外整除直接升级成完整标量 germ
的整性；没有排除真正的相对 cohomology 或 Frobenius 比较。

## 6. 保留整数 Frobenius 幂的实际相对接口

惰性处 (10) 成为
\[
C_{p+1}=-\operatorname{res}_{t=0}M_1K\,\zeta^p\,d\zeta .
\tag{27}
\]
在 \(\zeta=t^{-1}B(t)\) 的实际相关整单位 jet 上可定义
\[
\mathcal Q_p(\zeta)=
 \frac{\zeta(t)^p-\zeta^\sigma(t^p)}p.
\tag{28}
\]
此处 \(\sigma\) 对有理系数为恒等；
只在 (27) 实际用到的有限 jet 上作除法，
没有声称整个 \(\zeta\) 是有界整级数。
因为 \(B=1+O(t^2)\)，
\(\zeta^\sigma(t^p)=t^{-p}(1+O(t^{2p}))\)，且
\[
\mathcal Q_p(\zeta)\equiv t^{-p}\log B(t)\pmod p
\]
在这些相关次数内成立。
由 (3) 还有 \(B-tB'=1/((1-4t^2)J^2)\)，
故 \(d\zeta=-t^{-2}dt/((1-4t^2)J^2)\)。
代入 (27) 恰好恢复 (14) 的两个项；
第一项的留数本身仅知被 \(p\) 整除，不能删掉。
这是 (17) 的实际除 \(p\) 结构，不是公式相似的类比。

另一方面，\(\zeta=K/L\) 是水平周期之比，
并非固定模函数覆盖上的代数函数。
它可以视作投影化 GM bundle 上的代数坐标沿指定水平 germ 的值；
但把 (28) 与该 bundle 的 crystalline Frobenius 矩阵比较，
仍须证明相应框架、初值及除 \(p\) 的一致性。
对 \(M_1\) 单独作
\((M_1^\sigma(t^p)-M_1(t)^p)/p\)，其四阶零点使所得差
起于 \(t^{4p}\)，不能提供 (27) 的临界低阶信息。
需要保留的接口是固定 \(M_1\) 与真实秩二 GM period 的联合式 (27)。

## 7. 精确有限核验

[核验脚本](../scripts/check-full-weight-one-gm-row.py)
先用 R57 的独立整数多项式流生成实际 \(\beta_m\)，
再构造 (7)、(6) 的 \(M_1\)，最后比较两条 Euler/log 行。
默认精确有理运算为：

| \(p\) | 类型 | 临界除素数行模 \(p\) | 首坏次数 | 首坏系数乘 \(p\) 后模 \(p\) |
|---:|:---|---:|---:|---:|
| 7 | 惰性 | 2 | 12 | 1 |
| 11 | 惰性 | 9 | 16 | 7 |
| 13 | 普通 | 7 | 16 | 4 |
| 19 | 惰性 | 12 | 24 | 10 |
| 29 | 普通 | 1 | 32 | 4 |
| 37 | 普通 | 8 | 40 | 36 |

脚本还检查首坏次数以前全部系数的整性及 (25)–(26) 的准确常数。
有限核验不代替代数性或无穷素数证明；
它们检查实际尺度、普通第二除 \(p\) 行的三个项及首坏相消。

### 来源与范围

- R47 的权一模形式及全中央 Borel：
  [完整证明](2026-11-12-central-borel-modular-uniformization.md)，
  基于 Bannai–Kobayashi (2010) 的 Eisenstein–Kronecker 参数微分。
- R51、R54、R57、R58：实际截面、平方常数、首层有限性及整数流。
- 固定 Legendre PF 方程、Cayley 尺度和其出版公式来源：
  [GM/Legendre 证明](2026-11-12-critical-gauss-manin-legendre-lift.md)。
- 本文的全权归一、残数指数、两条除素数行及首坏分析均在上文推导；
  尚未调用未知的 Frobenius 非零定理。
