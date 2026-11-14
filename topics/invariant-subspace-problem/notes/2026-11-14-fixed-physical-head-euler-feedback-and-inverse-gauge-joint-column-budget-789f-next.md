# 固定物理头测试的 Euler 调整与完整 inverse-gauge 联合列预算

日期：2026-11-14。作者：literature_audit / 789f；固定列的真实抵消与 boundary_core 同步独立推导。

**状态：完整证明的固定测试预算。** 对同一个原测试
\(f_a=e_a\otimes\Omega\)，下文先保留全部实际零源 Schur 补，
再用原头的逆芽构造准确 Euler 调整。新的定量结论是：
完整 joined 核中，inverse-gauge 后的零源列和源列具有同一个平方和界
\[
 \frac{(a!)^2 e_a((b_j^2)_{j\ge m})}{W_a^2}
 \le \frac{a!S_m^a}{W_a^2},\qquad
 S_m=\sum_{j\ge m}(j+1)^{-4}\le\frac1{3m^3}.
\]
它对全部 \(q\ge a\)、\(d=2^m>a\) 一致，且使用原物理源和原完整最小 lift。
对 \(a\ge1\) 这是 \(O_a(m^{-3a})\) 的能量界。

恢复原源列时，两个完整交叉项仍须共同控制。本稿没有给正向 gauge 的算子范数、
原两费比较或 \(N=M\) 的结论。

依赖及接口：
[原首物理头商 Gram](../results/R239-appendix-first-physical-head-quotient-gram-for-left-plus-bare.md)、
[完整零源 Schur 与实际全源导数障碍](2026-11-14-actual-source-schur-relative-hole-derivative-obstruction-and-paid-test-null-family-789f-next.md)、
[真实逆芽与保权系数](2026-11-14-true-head-inverse-germ-twelve-half-radius-and-weighted-coefficients-789f-next.md)。

## 1. 原 joined 商、全部零源和两正交等距

固定 \(m\)、\(d=2^m\) 和有限孔切口 \(q\)。
\(A=A_m=F_m(B_m)\) 是原 \(N\) 或 \(Y\) 的有限真实头；
\[
 D=D_m=\sum_{j\ge m}b_jE_j,\qquad b_j=(j+1)^{-2}.
\]
物理头权仍是
\[
 B_me_i=(W_i/W_{i-1})e_{i-1},\qquad W_0=1.
\]
设 \(E_{r,p}=\ker D^r\cap\mathcal H_p\)，\(E_{0,p}=\{0\}\)。
原商首头空间为
\[
 \mathcal F=
 \bigoplus_{p\le q} E_{d,p}\ \oplus\
 \bigoplus_{j=1}^{d}
    (E_{d,q+j}\cap E_{j-1,q+j}^{\perp}).
\tag{1.1}
\]
令 \(\delta\) 为原高出生共同不变商中的压缩删除。
在 \(\mathcal F\) 上 \(\delta^d=0\)。
其有界真实尾孔数算子记为 \(\mathsf N\)，满足
\([\,\mathsf N,\delta\,]=-\delta\)。

取实际链基 \(A=VJ_dV^{-1}\)，并置
\[
 T=\sum_{i=0}^{d-1}Ve_i(-\delta)^i,\qquad
 \Gamma=T^*T\succeq I.
\tag{1.2}
\]
第一物理头是原输入本身；所以最后的下界是原物理 Gram 的下界。
\(T\) 的像是原完整 joined 核，以下称为 \(\mathcal K_{\rm jo}\)。
所有物理高商和头旗都保持原定义。

准确 cut 源映射为
\[
 \mathcal Bf
 =\sum_{j=1}^{d-1}(-1)^j Ve_{j-1}D^jf_{q+j}.
\tag{1.3}
\]
其全部零源空间与欧氏正交补是
\[
 \mathcal C=\ker\mathcal B
 =\bigoplus_{p\le q}E_{d,p}
   \ \oplus\ \bigoplus_{j=1}^{d}
                  (E_{j,q+j}\ominus E_{j-1,q+j}),
\]
\[
 \mathcal U=\mathcal C^\perp
 =\bigoplus_{j=1}^{d-1}(E_{d,q+j}\cap E_{j,q+j}^{\perp}).
\tag{1.4}
\]
它们都约化 \(\mathsf N\)。\(\mathcal C\) 还在 \(\delta\) 下不变：
真实核列满足 \(T\delta=-AT\)，源映射因此满足
\(\mathcal B\delta=-A\mathcal B\)；原短核旗由 \(A\) 保持。

在 \(\mathcal C\oplus\mathcal U\) 上定义
\[
 B_0=\Gamma_{CC}^{-1}\Gamma_{CU},\qquad
 R u=(-B_0u,u),\qquad
 S=R^*\Gamma R
 =\Gamma_{UU}-\Gamma_{UC}\Gamma_{CC}^{-1}\Gamma_{CU}.
\tag{1.5}
\]
这里 \(\Gamma_{CC}\succeq I\)、\(S\succeq I\)，且
\(S=\mathcal B_U^*(L+B_{\rm bare})\mathcal B_U\)。
因此 \(TRu\) 是同一实际源的完整最小左加 bare 列；不是删除部分 nuisance 的压缩。

令
\[
 I_C=T|_{\mathcal C}\,\Gamma_{CC}^{-1/2},\qquad
 I_U=TRS^{-1/2}.
\tag{1.6}
\]
这两个映射是相互正交的真正物理等距。
记其像投影为 \(P_C,P_U\)，则
\(P_{\rm jo}=P_C+P_U\) 是 \(\mathcal K_{\rm jo}\) 的正交投影。
对只在低左侧的测试，\(P_Cf\) 正是原左零源核投影；
未来零源块因物理支撑正交而没有分量。

## 2. 真实 Euler 算子与固定头调整

写
\[
 F=F_m,\quad \psi=F^{-1},\quad
 f_0(z)=F(z)/z,\quad
 h_F(z)=\frac{F(z)}{zF'(z)}.
\]
这些都是零点附近的有限真实解析芽，
\(f_0(0)=d_0^{-1}\ne0\)、\(h_F(0)=1\)。
在 \(B_m\) 上只取模 \(B_m^d\) 的有限多项式，故所用逆均为真正有限矩阵逆。

令 \(N_B=\operatorname{diag}(0,\ldots,d-1)\)。原链分级算子满足
\[
 Z=V\operatorname{diag}(0,\ldots,d-1)V^{-1}
   =N_Bh_F(B_m).
\tag{2.1}
\]
可直接核验：右侧第零行是零，且
\[
 [A,N_Bh_F(B_m)]
 =B_mF'(B_m)h_F(B_m)=A.
\]
它与 \(Z\) 的差和循环矩阵 \(A\) 对易，且第零行是零。
因为 \(e_0\) 对 \(A^*\) 循环，该差必为零。
这也保留了物理 \(N_B\) 与链指标的区别。

固定 \(0\le a<d\)，取
\[
 f_a=e_a\otimes\Omega,\qquad
 Z_a=(N_B-aI)h_F(B_m),\qquad
 \mathcal J_a=Z_a+\mathsf N_{\rm out}.
\tag{2.2}
\]
\(\Omega\) 是原尾真空，\(\mathsf N_{\rm out}\) 是物理输出尾孔数。
有准确等式
\[
 [A,Z_a]=A,\qquad Z_a^*e_a=0,\qquad
 \mathcal J_a^*f_a=0.
\tag{2.3}
\]
其中第二式使用次序
\(Z_a^*=h_F(B_m)^*(N_B-aI)\)，没有交换两个因子。

置
\[
 h_\psi(w)=\frac{w\psi'(w)}{\psi(w)},\qquad h_\psi(0)=1,
 \qquad
 \mathcal W_a=\mathsf N-a\,h_\psi(-\delta).
\tag{2.4}
\]
原真核列满足
\[
 \mathcal J_aT=T\mathcal W_a.
\tag{2.5}
\]
因为 \(ZT+ \mathsf N_{\rm out}T=T\mathsf N\)，
且 \(B_mT=T\psi(-\delta)\)，(2.5) 由
\(h_F(\psi(w))=h_\psi(w)\) 得到。
所以 \(\mathcal J_a\) 保持 joined 核及其全部零源子核。
没有声称它保持 (1.6) 的正交最小源分量。

## 3. 完整规范化反馈行

按 \(\mathcal C\oplus\mathcal U\) 写 \(\mathcal W_a\) 的块。
由 \(\mathcal C\) 不变，其 \(UC\) 块为零。设
\[
 F_a=(\mathcal W_a)_{CU}
       -(\mathcal W_a)_{CC}B_0
       +B_0(\mathcal W_a)_{UU}.
\]
准确有
\[
 \mathcal W_aR=R(\mathcal W_a)_{UU}+\iota_C F_a.
\tag{3.1}
\]
因此真正归一后的反馈行是
\[
 \mathscr F_a
 =\Gamma_{CC}^{1/2}F_aS^{-1/2}
 =I_C^*\mathcal J_a I_U,
\qquad
 \widehat W_U=S^{1/2}(\mathcal W_a)_{UU}S^{-1/2}.
\tag{3.2}
\]
对同一个原测试定义
\[
 c_a=I_C^*f_a,\qquad b_a=I_U^*f_a.
\]
在 \(\mathcal K_{\rm jo}\) 内的真实分解是
\(P_{\rm jo}f_a=I_Cc_a+I_Ub_a\)。
由 (2.3)、joined 核在 \(\mathcal J_a\) 下不变，得到
\[
 \boxed{\widehat W_U^*b_a=-\mathscr F_a^*c_a.}
\tag{3.3}
\]
\(b_a\) 是原最小 joined 源的 \(S^{1/2}\) 坐标。
(3.3) 保留 \(k_q=P_Cf_a=I_Cc_a\) 的完整跨块反馈。
不能删除右端后以源谱 \(q+j-a>0\) 断言 \(b_a=0\)。

## 4. 完整 inverse-gauge 正好取消固定列的巨大系数

定义
\[
 g_a(w)=\left(\frac{\psi(w)}w\right)^a,\qquad
 G_a=f_0(B_m)^{-a}.
\tag{4.1}
\]
\(a=0\) 时均为恒等。其余情形常数项非零，所以在原有限域上可逆。
因
\[
 \frac{w g_a'(w)}{g_a(w)}=a(h_\psi(w)-1),
\]
\[
 \boxed{
 \mathcal W_a=g_a(-\delta)^{-1}
                     (\mathsf N-aI)g_a(-\delta),\qquad
 G_aT=Tg_a(-\delta).
 }
\tag{4.2}
\]
\(G_a\)、\(G_a^{-1}\) 都保持 joined 核和全部零源子核。
以下所有伴随都相对于原物理 Hilbert 内积。

令
\[
 h_a=G_a^{-*}f_a=f_0(B_m)^{*a}f_a.
\]
原权的位置给一个完整抵消：
\[
 \boxed{
 h_a=\frac{(A_m^*)^a(e_0\otimes\Omega)}{W_a}.
 }
\tag{4.3}
\]
确实，\((B_m^*)^ae_0=W_ae_a\)，且
\(B_m^af_0(B_m)^a=A_m^a\)。
因此
\[
 \|h_a\|\le6^a/W_a.
\tag{4.4}
\]
这里 \(W_a\) 是固定物理索引 \(a\) 的原链权；
对固定 \(a\)，它不随 \(m\) 改变。
(4.3) 使用完整 \(f_0(B_m)^{*a}\)；
逐项估计 \(h_F(B_m)^*e_a\) 不会得到这个抵消。

## 5. 原真核方程进一步给统一 \(m^{-3a/2}\) 小列

现在假设 \(q\ge a\)。
因为 \(a<d\)，第 \(a\) 次数的整个输入层都在 (1.1) 的左部分，
属于 \(\mathcal C\)，无高出生商损失。
原核方程 \(AT=-\delta_{\rm out}T\) 及第一物理头为恒等给
\[
 \boxed{
 T^*h_a=\frac{(-D_m^*)^a\Omega}{W_a}.
 }
\tag{5.1}
\]
这是原输入空间中的准确向量；此低次数上受限 \(\delta^*\) 与完整
\(D_m^*\) 的作用相同。

对原尾真空，
\[
 (D_m^*)^a\Omega
 =a!\sum_{\substack{I\subset\{m,m+1,\ldots\}\\|I|=a}}
                    b_I e_I.
\]
所以
\[
 \|(D_m^*)^a\Omega\|^2
 =(a!)^2e_a((b_j^2)_{j\ge m})
 \le a!S_m^a,\qquad
 S_m=\sum_{j\ge m}b_j^2\le\frac1{3m^3}.
\tag{5.2}
\]
这里的 \(e_a\) 是初等对称多项式，最后一步来自
\(a!e_a(b^2)\le(\sum b_j^2)^a\)。

由于 \(\Gamma\succeq I\)，完整正交投影有
\[
 \boxed{
 \|P_{\rm jo}h_a\|^2
 =\langle T^*h_a,\Gamma^{-1}T^*h_a\rangle
 \le\frac{(a!)^2e_a(b^2)}{W_a^2}
 \le\frac{a!}{3^aW_a^2m^{3a}}.
 }
\tag{5.3}
\]
同一完整逆后取任何真实正交分量均保持此界，尤其包括原全部零源分量
及真正最小源分量；没有先压缩 \(\Gamma\) 再倒置。

## 6. 两列的同源平方和及恢复时未付的共同项

在相互正交的物理等距 \(I_C,I_U\) 中，\(G_a\) 的真实 joined 限制为
\[
 \begin{pmatrix}G_C&K_a\\0&G_U\end{pmatrix},\qquad
 G_C=I_C^*G_aI_C,\quad
 G_U=I_U^*G_aI_U,\quad K_a=I_C^*G_aI_U.
\tag{6.1}
\]
两对角块可逆。这是因为 \(G_a,G_a^{-1}\) 都保持零源子核，
而非假设 \(G_a\) 约化它。

令
\[
 c'_a=G_C^{-*}c_a,\qquad
 b'_a=G_U^{-*}(b_a-K_a^*c'_a).
\tag{6.2}
\]
joined 核及其逆都不变给
\[
 (c'_a,b'_a)=(I_C^*h_a,I_U^*h_a).
\]
结合 (5.3)，得到本稿的完整联合预算
\[
 \boxed{
 \|G_C^{-*}c_a\|^2+
 \|G_U^{-*}(b_a-K_a^*G_C^{-*}c_a)\|^2
 \le\frac{(a!)^2e_a(b^2)}{W_a^2}
 \le\frac{a!S_m^a}{W_a^2}.
 }
\tag{6.3}
\]
特别，它没有把左列的反变换和源列的反变换分开后丢掉
\(K_a^*G_C^{-*}c_a\)。

恢复原测试的准确公式是
\[
 \boxed{
 c_a=G_C^*c'_a,\qquad
 b_a=K_a^*c'_a+G_U^*b'_a.
 }
\tag{6.4}
\]
两个变换后列的平方和已经由同一个原测试支付，
但 (6.4) 的共同正向恢复尚无本稿所需的 \(e^{O(d^3)}\) 预算。
不能把 (6.3) 的小量直接乘一个未估计的恢复范数，
也不能只估其中一项而丢掉另一项。

补充一个保固定测试的真实列权：若
\(B_C=I_C^*B_mI_C\)，零源核在 \(B_m\) 下不变，故
\[
 (B_C^*)^\ell c_a=I_C^*(B_m^*)^\ell f_a,\qquad
 \|(B_C^*)^\ell c_a\|\le W_{a+\ell}/W_a
\tag{6.5}
\]
当 \(a+\ell<d\)；否则该列严格为零。
(6.5) 可用于共同展开，仍不许可拆开 (6.4) 的真实回馈。

## 7. 准确边界

(6.3) 对每个固定物理索引 \(a\)、所有 \(q\ge a\) 和 \(2^m>a\) 成立，
不需要旧联合旗的孔窗口。若调用此前的 \(m\ge10\) 逆芽尺度，
可再使用 \(\rho_m=e^{-(25/2)d^3}\)，但本稿并未给
\(G_C^*,G_U^*,K_a^*\) 的所需共同恢复界。

\(a=0\) 时原测试本来就在左零源核，\(b_0=0\)；
\(a\ge1\) 时变换后列趋零不是原列已趋零的结论。
对一般有限物理测试可逐个固定 \(a\) 使用本稿，
但各 \(a\) 的 gauge 不同，不能擅自将它们当成一个共同的算子收缩。

完整全源相对孔导数已被原实际反例排除。
本稿只保固定物理列及其完整零源反馈，未改变原源、原两费、
真正高返回或剩余负图条件。原边界 \(N=M\) 和普通 Hilbert ISP 仍未完成。
