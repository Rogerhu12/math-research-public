# 小辅助素数的实际 Heegner 迹与固定 CM 周期 jets

日期：2026-11-12。状态：下述整线性化、实际迹公式及有限 jet
非零充分条件已证明。后续 R116 已证明相对密度一输入可选实际首jet为单位。
本篇不把原代数参数中的邻点先验当作根单位旋转，也不把周期参数
中的模形式函数当成代数函数。

## 1. 固定映射、基点与局部化

固定 R103–R105 的
\[
F=\mathbb Q(\sqrt{-15}),\qquad E:y^2=x^3-17x,\qquad
C=X_0(3N_E),\qquad
\Phi=\pi\circ d_1+\pi\circ d_2:C\longrightarrow E.
\tag{1.1}
\]
对相容的导子为 \(\ell\) 的 CM 点 \(z_\ell\)，有精确等式
\(\Phi(z_\ell)=X_\ell=(1+\tau_3)P[\ell]\)。记 \(z_1\) 为最大阶
的相容基点；其像为最大环类域到 \(F\) 的 Heegner 迹。
R100 中已由 Gross–Zagier 及 \(L'(E/F,1)=0\) 证明此像为挠点，
R107 又证明 \(E(F^{\rm ab})_{\rm tors}=E[2]\)。因此
\[
\Psi=[2]\circ\Phi,\qquad \Psi(z_1)=O.
\tag{1.2}
\]
同样的等式对 \(z_1\) 的全部 Galois 共轭成立。
这个固定的乘二不改变奇数 \(p\) 的不可除性，且任何
\([2]Q\ne O\) 都给 \(Q\ne O\)。

取 \(\ell\) 在 \(F\) 与 \(\mathbb Q(i)\) 中均惰性，避开一个
只依赖于上述固定数据的有限素数集合。这个集合包含坏约化、
代数参数或 de Rham 基的分母，以及必要的细模曲线 étale 图的坏位。
基点所在的固定数域在这些位未分歧。
令 \(B/\mathbb Q_\ell\) 为一个有限未分歧扩张，包含相应基点和
标记的剩余定义域以及 \(\mu_{\ell^2-1}\)，写 \(\mathcal O_B\) 为其整数环。
估值规范为 \(v_\ell(\ell)=1\)。

所有次数 \(\ell\) 的商的剩余椭圆曲线都是源的 Frobenius 扭曲。
在这个目标剩余盘内，其 canonical CM 提升是一个固定 Galois 共轭
\(c\) 的 \(\ell\)-进实现，且 \(\Psi(c)=O\)。这里 \(c\) 只从一个
固定有限集合 \(\Sigma\) 中选择：不能把源基点与 Frobenius 后的
目标基点在没有标记的情况下认作同一点。

在每个 \(c\in\Sigma\) 固定一个代数局部参数 \(t\)，\(t(c)=0\)。
固定一次 de Rham CM 本征基，用 Gauss–Manin 水平化定义 Hodge 线的
period 比 \(v_c(t)\)，规范为
\[
v_c(0)=0,\qquad v_c'(0)=1.
\tag{1.3}
\]
其系数在一个固定数域内。除去上述固定有限坏位后，归一化所用
导数是单位。由 crystalline 水平化，\(v_c\) 在每个当前局部场中
正是相应 Gross–Hopkins period 比。只使用这个内在同一化，不使用
可能有不同基规范的显式超几何分母公式。

定义固定的形式级数
\[
\mathcal F_c(v)
 =\log_E\bigl(\Psi(t_c(v))\bigr)
 =\sum_{m\ge1}b_{c,m}v^m,
\qquad t_c=v_c^{-1}.
\tag{1.4}
\]
这里 \(\log_E\) 以固定不变微分规范。它是在形式邻域的恒等式；
并未断言 (1.4) 能在每个邻点的 period 值处直接代入。
特别地，邻点本身可以映到另一个 period 本征线，即 \(v_c=\infty\)。

## 2. 真正的整旋转参数与固定参数的低阶比较

写 \(d=\ell+1\)。canonical 形式群有未分歧二次 CM。
其 Teichmüller 单位群 \(\mu_{\ell^2-1}\) 通过改变 special-fiber
标记作用于完整的 deformation disc，保持 canonical 原点。
中心的 \(\mu_{\ell-1}\subset\mathbb Z_\ell^\times\) 在 deformation
空间上作用平凡，所以有效作用群为阶 \(d\) 的循环群。
这里取的是
\(\mathcal O_{F,\ell}^{\times}/\mathbb Z_\ell^{\times}\) 的 tame 商，
再用其忠实切空间特征将它标为 \(\mu_d\)；不是直接把原 torus
内的 norm-one \(\mu_d\) 子群当作忠实作用群。后者可能还有
\(\{\pm1\}\) 的核。

在 CM de Rham 本征基中，两个特征为 \(a\) 与 \(\bar a\)。
故 period 比及切空间上的比值特征是 \(a/\bar a\) 或其逆；
取与 (1.3) 相符的标签，把有效群写成 \(\mu_d\)，记其作用为
\(g_\zeta\)。于是
\[
g_\zeta'(0)=\zeta,\qquad
v_c(g_\zeta(t))=\zeta v_c(t).
\tag{2.1}
\]
相反的 Artin 规范只把全部 \(\zeta\) 同时取逆，不改变下面的投影。

因为 \(d\) 是 \(\ell\)-进单位，可定义
\[
w_\ell(t)=\frac1d\sum_{\zeta\in\mu_d}\zeta^{-1}g_\zeta(t)
\in t\mathcal O_B[[t]],\qquad w_\ell'(0)=1.
\tag{2.2}
\]
该级数及其复合逆都整，且
\(w_\ell(g_\zeta(t))=\zeta w_\ell(t)\)。由 (2.1)，
\(v_c(t_\ell(w))\) 的非零次数只能是 \(1\bmod d\)，首项为 \(w\)。
所以有精确的低阶恒等式
\[
v_c(t_\ell(w))=w+O(w^{d+1}),\qquad
t_\ell(w)=t_c(w)+O(w^{d+1}).
\tag{2.3}
\]
这里的 \(O\) 是特征零形式幂级数的阶数陈述，不预先宣称
其余项的系数整。\(w_\ell\) 一般随 \(\ell\) 改变；固定的是
\(v_c\)，以及 (2.3) 确定的低 jets。

取真实导子 \(\ell\) 邻点 \(z_\ell\)，置
\[
r=w_\ell(t(z_\ell)).
\]
未分歧 quadratic CM 的 level-one quasi-canonical lift 满足
\(v_\ell(t(z_\ell))=1/d\)。因 (2.2) 是整严格坐标变换，
\(v_\ell(r)=1/d\)。局部 CM 互反律把整 \(\mu_d\) 作用与
这 \(d\) 个不同商的 Galois 作用识别，因此
\[
\operatorname{Gal}(B(r)/B)=\mu_d,\qquad
\sigma_\zeta(r)=\zeta r,\qquad
c_\ell:=r^d\in\ell\mathcal O_B^\times.
\tag{2.4}
\]
也可由估值分母给 \([B(r):B]\ge d\)，再由恰有 \(d\) 个邻点给
反向不等式；\(X^d-c_\ell\) 是实际 Eisenstein 最小多项式。
本段使用带标记的商，而不是仅以邻点数相同猜测轨道。

## 3. 整对数微分给全部尾项的足够控制

令
\[
\mathcal A_\ell(w)
 =\log_E\bigl(\Psi(t_\ell(w))\bigr)
 =\sum_{m\ge1}a_{\ell,m}w^m.
\tag{3.1}
\]
固定映射在所选好位延伸为整数环上的态射；不变微分与
\(t_\ell(w)\) 都整。因此
\[
\mathcal A_\ell'(w)\in\mathcal O_B[[w]],\qquad
m a_{\ell,m}\in\mathcal O_B,\qquad
v_\ell(a_{\ell,m})\ge-v_\ell(m).
\tag{3.2}
\]
这同时证明 (3.1) 在整个开单位盘收敛，足以在 \(w=r\) 及其
全部共轭处代入。由 (2.3)，
\[
a_{\ell,m}=b_{c,m}\quad(1\le m\le d).
\tag{3.3}
\]
特别地，\(b_{c,m}\) 对 \(1\le m<\ell\) 在当前位整。
不需要假定 \(\log_E\) 或 period 比在整个盘上有同样的整数系数。

## 4. 完成 prime-to-p 迹的精确系数及非零证书

假定
\[
d=pu,\qquad p\ne\ell\text{ 为奇素数},\qquad u\ge3,
\]
并取 \(U\subset G_\ell\) 为阶 \(u\) 的子群。令
\[
Q=\operatorname{Tr}_U X_\ell,
\qquad s=r^u,\qquad s^p=c_\ell.
\]
全体点均约化到 \(\Psi(c)=O\)，故形式对数可逐项相加。
根单位正交性给精确的收敛等式
\[
\log_E([2]Q)
 =u\sum_{j=0}^{p-1}s^j B_{\ell,j},
\qquad
B_{\ell,j}
 =\sum_{k\ge0}a_{\ell,u(j+kp)}c_\ell^k,
\tag{4.1}
\]
其中 \(a_{\ell,0}=0\)。\(1,s,\ldots,s^{p-1}\) 是实际扩域
\(B(s)/B\) 的整基，而不仅是形式符号。

对 \(1\le j\le p-1\)、\(k\ge1\)，(3.2) 给
\[
v_\ell\bigl(a_{\ell,u(j+kp)}c_\ell^k\bigr)
\ge k-v_\ell(j+kp)\ge1.
\tag{4.2}
\]
最后一个不等式可直接核验：\(p\le(\ell+1)/3\)，所以
\(j+p<2p<\ell\)；当 \(k\ge2\) 时
\(j+kp<(k+1)p<\ell^k\)，故 \(v_\ell(j+kp)<k\)。
对 \(j=0\)，同样有 \(k-v_\ell(k)\ge1\)。各尾项估值趋于无穷，
因此 (4.1) 的逐项归并与模 \(\ell\) 化均合法。

于是
\[
B_{\ell,0}\in\ell\mathcal O_B,\qquad
B_{\ell,j}\equiv b_{c,ju}\pmod\ell\quad(1\le j\le p-1).
\tag{4.3}
\]
由于 \((p-1)u=d-u<\ell\)，右侧全部是已证整的固定低阶系数。
得到实际充分条件
\[
\boxed{\quad
\exists j\in\{1,\ldots,p-1\}:
b_{c,ju}\not\equiv0\pmod\ell
\quad\Longrightarrow\quad Q\ne O.
\quad}
\tag{4.4}
\]
反过来，\(Q=O\) 强迫
\[
(b_{c,u},b_{c,2u},\ldots,b_{c,(p-1)u})=0
\quad\text{于 }\mathcal O_B/\ell.
\tag{4.5}
\]
这不是双向判据：低阶向量为零时，(4.1) 的更深层仍可能非零。

还可以记录 (4.4) 的实际大小。令 \(j_0\) 为第一个单位系数的
指标。若前面的 \(b_{c,ju}\) 全被 \(\ell\) 整除，则
\[
v_\ell\bigl(\log_E([2]Q)\bigr)=\frac{j_0}{p}.
\tag{4.6}
\]
原因是不同 \(s^j\) 的估值分数不同，且其余基系数均整；前面
非单位项的估值至少为 \(1+j/p>j_0/p\)，常数项至少为 \(1\)。
因此这里不存在未受控的同估值高阶抵消。

## 5. 与 R110 的联立及尚需证明的全局命题

对 R110 的密度一输入，\(\ell\equiv-1\pmod{1020p}\)，所以
\(u\ge1020\)，以上尾界自动适用。若固定 \(L<2\) 且
\(\ell\ll p^L\)，则
\[
u^2=\frac{(\ell+1)^2}{p^2}=o(\ell).
\tag{5.1}
\]
因此，一个能保证在 \(j u\le C u^2\) 处出现模 \(\ell\) 单位的
统一定理，就会落在 (4.4) 的合法范围之内。后续 R116 改用固定非零进程与整数范数乘积，已证明对相对密度一输入可直接选首项为单位；没有需要这个更强的逐个 u 定理。

当 (4.4) 成立时，R110 已证明
\(Q\notin pE(H_\ell)\)，并给出对数长的实际增广不可除层。
这仍不自动证明 \(Q\notin(\sigma-1)\ker N_p\)，后者是原
Kolyvagin 底层所需的更强命题。

两项不能省略的限制如下。

- 固定的是 CM **period** 参数 \(v_c\) 及级数 (1.4)。它一般是模形式
  的局部 Eichler 原函数；\(\Psi\) 在代数参数 \(t\) 中的代数性，
  不会在逆 period 变换 \(t=t_c(v)\) 后自动保留。因而不能直接对
  (1.4) 套用固定代数函数的根单位平均零估计。
- 一个固定特征或局部对称可能使若干等差子序列恒零。要使用 (5.1)，
  必须证明本实际 \(\Phi\) 的向量 (4.5) 非零，而不是证明任意一个
  非恒定形式级数有某个非零系数。乘二、固定 \(3\) 类群和、以及
  可选的 \(5\) 类群和均需保留它们各自真实的特征。

## 6. 一手来源与本篇补充的证明

- J.-K. Yu, *On the moduli of quasi-canonical liftings*,
  Compositio Math. **96** (1995), 293–321：§2 的 deformation functor；
  §3 的 Frobenius 标记商；§4（印刷页 296–298）的局部 Artin 作用及
  最小定义域；§6 的 level-one 赋值；§11（印刷页 312）的
  Gross–Hopkins 等变性。
  [原文](https://www.numdam.org/article/CM_1995__96_3_293_0.pdf)。
- Y. André, *Period mappings and differential equations. From C to Cp*：
  II Lemma 6.1.3、§6.1.4 与 Lemma 6.2.5，将 crystalline period map
  与同一初值的水平 Gauss–Manin period map 识别。
  [作者预印本](https://arxiv.org/abs/math/0203194)。
- 固定映射与基底 Heegner 迹：
  [R105 笔记](2026-11-12-minus15-classgroup-trace-primitivity.md)、
  [R100 笔记 §4](2026-11-12-one-prime-heegner-class-and-explicit-points.md)。
- 精确挠点与小辅助素数：
  [R107 笔记](2026-11-12-heegner-orbits-and-logarithmic-augmentation-depth.md)、
  [R110 笔记](2026-11-12-density-one-small-heegner-auxiliary-primes.md)。

在这些输入上，本篇给出 (2.2) 的整平均线性化、(2.3) 的固定
低 jet 比较、全部对数尾项的 (4.2) 控制，以及实际迹的
(4.4)–(4.6) 非零证书；这些结论不以未知的角色非零定理为输入。
