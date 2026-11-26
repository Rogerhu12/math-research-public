# R149 补篇：真实 target 正交行的联合有限矩阵误差

2026-11-27，visible-exact-astra-fb31ed6-20261127 / trial_restore。

**新增解析结论。** 对 SC/TC 的完整96列，先应用原完整左 receiver、再取真 target 的正交 Fourier 坐标，可以直接控制整个矩阵误差。列误差项不需要把同一个 receiver 范数按96行重复作平方和。RW 的有限 trial rows 无需正交；它们的全部误差另用 Hilbert–Schmidt 界支付。下面同时保留 source/target 的不同权重，并给出完整 signed trial matrix 的可执行逆门。

这是已证明的误差公式及纯算法，没有在缺少完整实际 P224 时生产真 PDE 列、真矩阵或逆。实际消费仍须核准整个原低逆、physical58、P224 的全部224记录、原 source/execution/manifest 及同一 selected 方程身份。仅有下面实际使用的6个标量，不能完成这个前置。TC 的三个完整新目标与 RW 的96个已成完整行也须分别实际通过。

## JF1. 固定的真实 Hilbert 空间和全部96行

采用 [RW.1–4](R149-supplement-reflected-finite-waist-rows-from-complete-conjugacy.md) 的同一 selected 反射轴
\(a=2\mathcal H(0)\)、周期 \(\ell=\pi/2\) 和 normalized measure \(dx/\ell\)。真实 physical target 为
\[
Y_a^0=P\operatorname{Fix}(R_a)\cap L^2(\mathbb T;\mathbb R),
\qquad R_af(x)=f(a-x),\quad P=1-\Pi.
\]
其低 target 空间的完整实正交归一基是
\[
g_i(x)=\sqrt2\cos\bigl(4i(x-a/2)\bigr),\qquad 1\le i\le96.
\tag{JF.1}
\]
它们在整个实 \(L^2(\mathbb T,dx/\ell)\) 中也正交归一。因此坐标算子
\[
\mathcal Gv=(\langle g_i,v\rangle)_{i=1}^{96}
\tag{JF.2}
\]
由 Bessel 不等式满足 \(\|\mathcal G\|\le1\)，无论 \(v\) 是否已经属于反射子空间。这个事实适用于真 target 的 \(g_i\)，不适用于旧角上的 \(f_i=g_i\circ\mathcal H\) 或 RW 的有限 \(p_i\)。后两者均不被假设正交。

完整 waist 空间为
\[
\mathcal Y_0=L^2_0(\mathbb T;\mathbb R^2)\oplus\mathbb R^2.
\tag{JF.3}
\]
最后两维是原独立 physical density means。设 \(A_\partial=\mathcal L_\partial\) 为 RW.21 的完整 physical primitive receiver，\(A_{\rm in}=\mathcal R_i\) 为 [PN.15](R149-supplement-complete-positive-inverse-to-true-negative-and-incoming.md) 的原有序 incoming receiver。由 RW.21–22 和 PN.15–17，
\[
\|\mathcal G A_\partial\|\le\Gamma_\partial
 :=B_{H,0}/\sqrt2,\qquad
\|\mathcal G A_{\rm in}\|\le\Gamma_{\rm in}
 :=B_{H,0}K_{W,0}.
\tag{JF.4}
\]
证明是在完整 receiver 后才应用 (JF.2)。physical 情形中，\(\pi_y\) 与反射投影均为收缩，\(e^T/2\) 的 Euclidean 范数为 \(1/\sqrt2\)，最后真实 density 角变换使用已付 \(B_{H,0}\)。incoming 情形按 \(\widehat T_0^{-1}\)、完整 \(\mathscr J_+\)、真实 density 角变换的原顺序支付 \(K_{W,0}\)、1、\(B_{H,0}\)。\(\mathscr J_+\) 保留其 mean，角变换没有被当成等距。physical 行无需再撤销 \(\widehat T_0\)。

## JF2. 六个实际使用系数仍来自整个已验证 P224

令 \(F_{c,j},F_{b,j},F_{L,j}\) 为 TC 同一第 \(j\) 列的三个完整 positive ordinary residual 上界，\(F_{-,j},F_{{\rm st},j}\) 为其两个完整 negative residual 上界。原真实 radial partition、ordinary \(dr\)、两 source 分量、均值和 Sobolev 窗全部保持 [TC.12–16](R149-supplement-true-root-continuous-PDE-trials-and-complete-residuals.md) 的定义。

TC 的精确根 even96 identity、零高支集、零外端及连续性给出原14输入向量只有 \(k=1,2,7\) 非零。于是从**整个已准入的** P224 表取
\[
d_j=P_{\mathrm{low\_root97},1}F_{c,j}
    +P_{\mathrm{low\_root97},2}F_{b,j}
    +P_{\mathrm{low\_root97},7}F_{L,j},
\]
\[
z_j=P_{\mathrm{high\_root\_mixed},1}F_{c,j}
    +P_{\mathrm{high\_root\_mixed},2}F_{b,j}
    +P_{\mathrm{high\_root\_mixed},7}F_{L,j}.
\tag{JF.5}
\]
按 [SC.17–20](R149-supplement-signed-finite-columns-and-full-negative-residual-sources.md)，真实列 \(Y_j\) 与同一 exact finite trial \(Y_j^a\) 满足
\[
\|Y_j-Y_j^a\|_{\mathcal Y_0}\le D_j,
\qquad
D_j=C_R\sqrt{d_j^2+z_j^2}+C_OF_{-,j}+C_2F_{{\rm st},j}.
\tag{JF.6}
\]
high-root-mixed 已包含原 stable/returning 输出，不再乘9；low97 包含 moving mean。两项根输出使用原正交物理块，两个 negative residual 使用完整已证明源域。两个 physical waist means 在 \(D_j\) 的完整范数内，并未设零。这里只对 TC 的连续齐次 root96 列成立；真实 \(\nu\)、mean、phase 或有 jumps 的列不能沿用这些零条件。

令 \(D_s=\operatorname{diag}(s_j)\)、\(D_t=\operatorname{diag}(t_i)\) 为原各自的正 source/target 权重，\(s_j,t_i>0\)。记
\[
\Delta_s=\left(\sum_{j=1}^{96}(D_j/s_j)^2\right)^{1/2},
\qquad
V_s=\left(\sum_{j=1}^{96}(v_j/s_j)^2\right)^{1/2},
\quad v_j\ge\|Y_j^a\|_{\mathcal Y_0}.
\tag{JF.7}
\]
对任意实系数向量 \(x\)，三角和 Cauchy–Schwarz 给
\[
\left\|\sum_j(Y_j-Y_j^a)x_j/s_j\right\|
 \le\Delta_s\|x\|_2,
\qquad
\left\|\sum_jY_j^a x_j/s_j\right\|
 \le V_s\|x\|_2.
\tag{JF.8}
\]
这里没有假设96个误差列彼此正交。

## JF3. 同一完整 signed trial matrix 的联合误差

以 \(\varepsilon_i\) 表示 RW.18 的原完整已成 scalar row error，并置
\[
E_{\rm row}=\left(\sum_{i=1}^{96}\varepsilon_i^2\right)^{1/2}.
\tag{JF.9}
\]
设 \(M_{ij}=\langle g_i,A Y_j\rangle\)，\(M^a\) 是 TC 已定义的完整 signed trial matrix。TC 的 \(Y_j^a\) 在两 primitive 分量中的 Fourier 支集为96，同时保留全部两 mean，故整个 trial 列空间位于 RW.7 的固定 \(J_s=268435456\) 以下。由 RW.22、RW.26，对其任意线性组合 \(y\) 都有
\[
\left\|\bigl(\langle g_i,A_\partial y\rangle
             -\langle z^\partial_{i,a},y\rangle\bigr)_i\right\|_2
 \le E_{\rm row}\|y\|/\sqrt2,
\]
\[
\left\|\bigl(\langle g_i,A_{\rm in}y\rangle
             -\langle\iota_+p_i,y\rangle\bigr)_i\right\|_2
 \le E_{\rm row}\|y\|.
\tag{JF.10}
\]
第二式是在完整有限 trial 子空间上使用 \(\widehat T_0^{-1}y=y\)。这仅消去 trial-row 项的 \(K_{W,0}\)，(JF.4) 对真正列误差的 \(K_{W,0}\) 不变。第一式使用两相同 primitive 分量的确切 \(1/\sqrt2\) 因子。两式由每一完整 row error 的平方和给出，不把近似行当成正交系。

将 \(M-M^a\) 分为真 receiver 对列误差的作用及 row-trial 对 trial 列的误差，利用 (JF.4)、(JF.8)、(JF.10)，得到
\[
\boxed{\quad
\|(M-M^a)D_s^{-1}\|_2
 \le\Gamma_A\Delta_s+\kappa_AE_{\rm row}V_s=:\Xi_A,
\quad}
\tag{JF.11}
\]
其中
\[
(\Gamma_A,\kappa_A)=
\begin{cases}
(B_{H,0}/\sqrt2,\ 1/\sqrt2),& A=A_\partial,\\
(B_{H,0}K_{W,0},\ 1),& A=A_{\rm in}.
\end{cases}
\tag{JF.12}
\]
完整96行在第一项中的联合 norm 已由 Bessel 支付，不产生额外 \(\sqrt{96}\)。这并不把两个不同物理矩阵合并。

## JF4. 保持全部有符号乘法和不同权重的逆门

令 \(\mathbb M^a\) 为同一个完整 signed trial carrier 的 interval enclosure。它必须包含其有限配对 evaluation error，不能只读显示中心，也不能由 unsigned 表恢复。选择一张完整 exact dyadic trial inverse \(B\)，按有符号矩阵乘法形成
\[
\mathbb E_0=I-BD_t\mathbb M^aD_s^{-1},\qquad
L=BD_t.
\tag{JF.13}
\]
由每一完整矩阵的全 row/column absolute sums 得到
\[
r_0\ge\|I-BD_tM^aD_s^{-1}\|_2,\qquad
b_t\ge\|BD_t\|_2,\qquad b\ge\|B\|_2.
\tag{JF.14}
\]
不能先逐条取绝对值再形成 (JF.13)。finite evaluation error 已在 \(\mathbb M^a\) 内，不在 (JF.11) 重复添加。现在
\[
\|I-BD_tMD_s^{-1}\|_2\le r_0+b_t\Xi_A=:\rho.
\tag{JF.15}
\]
如果完整保存并读回的有向 upper 满足 \(\rho<1\)，Neumann 定理及有限维方阵单射性给
\[
\|(D_tMD_s^{-1})^{-1}\|_2\le b/(1-\rho).
\tag{JF.16}
\]
此门使用96行96列的完整 signed carrier，而不是一个 principal submatrix。它与 SC.25–27 的 entrywise enclosure 门是同一实际矩阵的两种合法误差证法；不能把两个门的不同局部项拼成一个没有推导的更小 residual。门失败仍只是该 trial 和 bounds 未闭合。

## JF5. 纯实现及实际执行边界

[fourfold_codazzi_joint_signed_finite_trial_error_math.py](../scripts/fourfold_codazzi_joint_signed_finite_trial_error_math.py) 仅实现 (JF.5–16)。它不导入数值库、不读写、不生成 future actual，也不执行旧 residual、row 或 norm 目标。column 接口要求完整224个已准入上界和全部96列的五源记录；表的完整文件身份、真实 inverse 资格和原通道单位由 public owner 在调用前核准，读取6个实际非零系数不能代替此事。

后继 owner 先消费已成完整 TC/RW/P224，再为同一已定义 signed trial carrier 作必要重物化并核原 whole hash。该重物化不是再次生产96列残差或旧 row error。新保存目标为所选完整矩阵的实际列误差和 (JF.15–16)；所有新有向球须完整保存读回，严格门取保存球的上端。当前本文没有这次新数值执行。

本结论的两个矩阵仍分别是原 physical primitive96 和声明型 incoming cosine96。完整 high elimination、target \(\mathcal B^{-1}\)、transported \(\Theta_{96}\)、两个 mean 匹配方程、independent function input、真实 phase 与 \(\nu\) 的所有交叉块仍独立。未完成这些项时，即便 (JF.15) 对96方阵通过，也不等于 BF/FC 的完整 Schur 或本课题完成。
