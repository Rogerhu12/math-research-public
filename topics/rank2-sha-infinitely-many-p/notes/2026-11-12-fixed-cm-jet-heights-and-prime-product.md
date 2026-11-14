# 固定 CM jets 的高度及跨辅助素数的乘积预算

日期：2026-11-12。状态：下述高度界、乘积命题以及实际完整迹的
相对密度一非零性均已证明并独立复核。
指定等差序列的非零输入已由同日的固定 ordinary ST/Mellin 笔记及
Cornut 迹笔记证明；不能以“形式级数非零”替代这一输入。

## 1. 固定对象与要证明的算术高度界

沿用 R114 的固定数据
\[
 F=\mathbb Q(\sqrt{-15}),\quad E:y^2=x^3-17x,\quad
 C=X_0(3N_E),\quad \Psi=[2](\pi d_1+\pi d_2).
\]
在一个固定有限的 canonical CM 中心集合 \(\Sigma\) 上，取代数
参数、CM de Rham 基和已规范的 Gauss--Manin period 比 \(v_c\)。记
\[
 \mathcal F_c(v)=\log_E\Psi(t_c(v))
       =\sum_{n\ge1} b_{c,n}v^n,\qquad h_{c,n}=n!b_{c,n}.
 \tag{1}
\]
所有系数都在一个固定数域 \(K\) 中，增大 \(K\) 可同时容纳全部
中心和规范。这里的固定性独立于输入素数 \(p\) 和辅助素数 \(\ell\)。

**高度引理。** 存在只依赖于这些固定数据的整数 \(A\ge2,d\ge2\)
及常数 \(C_0>0\)，对全部 \(c\in\Sigma,n\ge1\)，
\[
 B_{c,n}:=A^{dn+1}h_{c,n}\in\mathcal O_K,
 \qquad
 \log\max\{1,|N_{K/\mathbb Q}(B_{c,n})|\}
        \le C_0 n\log(n+2).
 \tag{2}
\]
若 \(h_{c,n}=0\)，(2) 本身仍成立，但该范数不能用于非零整数
的素因子预算。因此后面会明确使用指定的系数非零命题。

### 1.1 有限多项式微分系统

在 \(c\) 的一个固定 affine étale 邻域中，以 \(t\) 为局部参数。
代数曲线的坐标、所需分母的倒数以及 étale Jacobian 的倒数，
生成一个有限型代数，在其中 \(d/dt\) 是正则导子。
将 Gauss--Manin 连接矩阵的有限分母也倒置。

增加水平基本解矩阵 \(Y\) 及其逆矩阵的条目为变量；它们满足
\[
       Y'=-\mathcal A(t)Y,\qquad (Y^{-1})'=Y^{-1}\mathcal A(t).
\]
Hodge 线向量的水平坐标和它们的比给出 \(v_c(t)\)。其分母在
\(c\) 非零。增加这些分母的倒数，并增加 \(v_c'(t)^{-1}\)；
后者在初值处存在，因为 \(v_c'(0)=1\)。

每个倒数变量 \(z=f^{-1}\) 的导数为 \(-z^2 f'\)，所以仍只需
有限多个变量，全部导数可以写成这些变量的多项式。
将导子改为
\[
                       D=\frac{d}{dv}=v_c'(t)^{-1}\frac{d}{dt}.
\]
最后加入变量 \(Z=\log_E\Psi(t)\)。其 \(t\)-导数是代数微分
\(\Psi^*\omega_E/dt\)，因而也已在同一有限生成的局部代数中。
于是得到一个**固定有限多项式向量场**
\[
 D=\sum_{j=1}^{s} P_j(X_1,\ldots,X_s)\frac{\partial}{\partial X_j},
 \qquad P_j\in K[X_1,\ldots,X_s],\quad X(0)\in K^s,
 \tag{3}
\]
其中某一坐标是 \(Z\)，且
\[
                       h_{c,n}=(D^n Z)(X(0)).                 \tag{4}
\]
这是多项式微分系统的陈述，**没有断言** \(\mathcal F_c(v)\)
为代数函数，也不需要其满足一个线性微分方程。

### 1.2 分母和每个无穷位的估计

取共同的 \(A\) 清去 (3) 所有系数和初值的分母；取
\(d\ge2\) 不小于所有 \(P_j\) 的次数。归纳得到
\[
 \deg(D^nZ)\le1+n(d-1),\qquad
                   A^nD^nZ\in\mathcal O_K[X_1,\ldots,X_s].
\]
在 \(A^{-1}\mathcal O_K\) 初值处求值，额外分母至多是
\(A^{1+n(d-1)}\)，给出 (2) 的整性。

固定 \(K\) 的任一复嵌入，以多项式系数的 \(\ell^1\) 范数计。
存在固定 \(M\) 使对次数 \(r\) 的多项式 \(Q\)，
\[
                         \|DQ\|_1\le Mr\|Q\|_1.
\]
初值的绝对值也由固定常数控制。因此
\[
 |(D^nZ)(X(0))|
 \le C_1^{n+1}\prod_{j=0}^{n-1}(1+j(d-1))
 \le (C_2n)^{n+1}.
\]
乘上 \(A^{dn+1}\) 并取所有嵌入的乘积，得到 (2)。
有限个中心可同时放大 \(A,d,C_0\)，故所有常数统一。

## 2. 一份真实的零迹耗用一个整数素因子

固定普通 ST/Mellin 比较与 Cornut 配套证明已给出：
存在固定整数 \(C=60\cdot61^k,n_0\)，使
\[
       h_{c,n}\ne0\qquad
       (c\in\Sigma,\ C\mid n,\ n\ge n_0).                  \tag{5}
\]
这里可取 \(\Sigma\) 为 Cornut 配套证明 §5.1 的八个最大阶
CM 中心或实际所需子集。各中心的 \(k\) 和阈值取最大，得到
这个统一且不随 \(p,\ell\) 改变的进程。因此可定义非零整数
\[
                 J_n=\prod_{c\in\Sigma}N_{K/\mathbb Q}(B_{c,n})
       \quad(C\mid n,n\ge n_0),
 \qquad \log|J_n|\ll n\log(n+2).                           \tag{6}
\]
重复中心或共轭只增加固定重数，不影响估计。若选择了完全
Galois 相容的规范，也可用一个中心的范数代替这个有限乘积。

取 R110/R114 的实际辅助素数
\[
 \ell+1=pu,\qquad \ell\equiv-1\pmod{1020Cp},\qquad
 Q_{p,\ell}=\operatorname{Tr}_{U}X_\ell,\quad |U|=u.
\]
除去固定坏位，\(\ell\nmid A\)，而 \(u<\ell\)。若这个**真实点**
\(Q_{p,\ell}=O\)，R114 的式 (4.5) 对实际中心 \(c\) 给出
\(b_{c,u}=0\pmod\ell\)。由于 \(u!\) 为 \(\ell\)-进单位，
\(B_{c,u}\) 在 \(K\) 的一个 \(\ell\)-上方素理想中为零，故
\[
                 Q_{p,\ell}=O\quad\Longrightarrow\quad \ell\mid J_u.
 \tag{7}
\]
只要 \(C\mid u,u\ge n_0\)，(7) 右侧就是一个非零整数的整除
关系。无需在当前素位把 \(J_u\) 的其他共轭与 CM 点作额外识别。

## 3. Mikawa--Fouvry 的小素数数量与不重复性

固定一个实数
\[
                         32/17<L<2.                           \tag{8}
\]
令输入素数 \(p\in(X,2X]\cap\mathcal P_F\)，其中
\[
 \mathcal P_F=\{p\ne17:p\equiv1,17,49,53\pmod{60}\}.
\]
对模数 \(1020Cp\) 使用 R110 已核定的 Fouvry Lemma 7
（其输入为 Mikawa 的平均短区间等差数列结果）。固定因子 \(C\)
只改变常数和所需排除的有限素数。
除去 \(o(X/\log X)\) 个输入 \(p\)，每个剩余的 \(p\) 有
\[
 \gg_C\frac{X^{L-1}}{\log X}
 \quad\text{个素数}\quad
 \ell\in(X^L,2X^L],\quad \ell\equiv-1\pmod{1020Cp}.
 \tag{9}
\]
这些 \(\ell\) 在 \(F\) 和 \(\mathbb Q(i)\) 都惰性；
\(a_\ell(E)=0\)。因 \(L<2\)，对充分大 \(X\)，
\[
 \ell+1< X^2<p^2,
 \qquad v_p(\ell+1)=1,
 \qquad u\le2X^{L-1}+1.                                    \tag{10}
\]
而 \(u\ge X^{L-1}/2\to\infty\)，故 (5) 的阈值最终自动满足。

**一个 \(\ell\) 最多对应本区间的一个 \(p\)。**
否则不同 \(p_1,p_2>X\) 的乘积整除 \(\ell+1< X^2\)，矛盾。
这条不重复性使全部输入素数的零迹可共同使用一次整数预算。

## 4. 相对密度一的实际非零迹

令 \(U_X=\lceil2X^{L-1}+1\rceil\)。由 (6)，
\[
 \log\prod_{\substack{n_0\le n\le U_X\\C\mid n}}|J_n|
                         \ll U_X^2\log U_X.                  \tag{11}
\]
将坏候选扩大为 \(\ell\mid J_u\) 的全部候选；这包含每个实际
零迹候选，也包含实际首系数 \(b_{c,u}\equiv0\pmod\ell\) 的候选。
这些 \(\ell\) 都是 (11) 非零整数的不同素因子，
且 \(\log\ell\ge L\log X\)。因此全部这些 \(\ell\) 的数量至多
\[
                              O(X^{2L-2}).                    \tag{12}
\]
若 (9) 中某个输入 \(p\) 的全部候选都为这种坏候选，它独占至少
\(\gg X^{L-1}/\log X\) 个 (12) 中的素数。因此这种输入至多
\[
                 O(X^{L-1}\log X)=o(X/\log X),               \tag{13}
\]
最后一步正是使用 \(L<2\)。合并 (9) 的例外，在
\(\mathcal P_F\) 中相对密度一的输入素数，都存在满足 (9) 的
真实辅助素数，使
\[
                              Q_{p,\ell}\ne O.               \tag{14}
\]
实际上可选 \(\ell\nmid J_u\)，故实际中心的 \(b_{c,u}\) 已为
单位。R114 式 (4.6) 给这个更准确的局部结论：
\[
                v_\ell\bigl(\log_E([2]Q_{p,\ell})\bigr)=1/p.
 \tag{14a}
\]
这仍只是辅助位的真实形式群大小，不是 \(\Delta\) 原始性判据。

dyadic 区间上的例外估计给通常的相对自然密度一：对任意
\(\varepsilon>0\)，从固定阈值以后每个 dyadic 区间的例外比例
小于 \(\varepsilon\)，累加并让 \(\varepsilon\to0\) 即得。

## 5. 得到的不可除性及仍需完成的步骤

由 R107 的 \(E(F^{\rm ab})_{\rm tors}=E[2]\) 和
\(N_{C_p}Q_{p,\ell}=O\)，非零 \(Q_{p,\ell}\) 必为非挠点：
在二挠点上 \(C_p\) 作用平凡，奇数 \(p\) 的范数就是恒等。
R110 的实际高度估计给
\[
 \widehat h(Q_{p,\ell})\ll u^2\log\ell
                 \ll p^{2L-2}\log p=o(p^2).
\]
若 \(Q_{p,\ell}=pR\) 且 \(R\in E(F[\ell])\)，Baker 在
\(F^{\rm ab}\) 上的统一正高度下界给
\(\widehat h(Q)\ge c_Ep^2\)，矛盾。因此充分大输入还有
\[
                    Q_{p,\ell}\notin pE(F[\ell]).             \tag{15}
\]

这些结论涉及实际全部 prime-to-\(p\) 迹，强于只对原始 Heegner 点
或固定大小的迹证明非扭。但 (15) **仍未证明**
\[
 Q_{p,\ell}\notin(\tau-1)\ker N_{C_p},
\]
后者才是 R104/R113 给出的指定 Kolyvagin 类非零条件。
本课题的 Sha 有限性目标不能因 (14) 或 (15) 而改为完成。

## 来源与依赖

- 固定 period/实际邻点/迹的模 \(\ell\) 关系：
  [R114](../results/R114-small-heegner-trace-and-cm-period-jets.md)。
- 小辅助素数的定量版本、全部同余条件及真实高度估计：
  [R110](../results/R110-density-one-small-heegner-auxiliary-primes.md)。
  一手可读来源为 E. Fouvry，*On binary cyclotomic polynomials*，
  Algebra & Number Theory **7** (2013)，1207--1223，
  §2.6，Lemmas 6--7：
  [出版全文](https://msp.org/ant/2013/7-5/ant-v7-n5-p07-p.pdf)。
- 指定进程 (5)：
  [固定普通 ST/Mellin 比较](2026-11-12-fixed-ordinary-st-mellin-branch.md)
  与 [Cornut 的真实全迹及固定非零进程](2026-11-12-cornut-fixed-branch-and-nonzero-progression.md)。
- 第 1 节为本篇对固定代数微分系统的直接分母和增长证明；
  第 2--4 节为使用 (5) 的直接整数乘积论证。
- 指定等差序列 (5) 的证明已经单独核验，不从普通系数非零或一般
  无穷多个非零系数推断。
