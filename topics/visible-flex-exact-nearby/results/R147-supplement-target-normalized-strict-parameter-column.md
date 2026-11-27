# R147 BNC：真正 target-normalized strict 参数列的完整96个带符号观测

2026-11-27，`visible-exact-astra-fb31ed6-20261127 / trial_restore`。

**已证明的新增接线。** 本篇给同一个 implicit selected member 的
\[
 b_\nu=E_{96}^{a*}\mathcal B^{-1}F_\nu,\qquad
 F_\nu=\mathcal L_\partial\mathfrak D_0v_\nu,
 \quad \mathcal B=Id+\mathcal T_w I
 \tag{BNC.1}
\]
一个首次可执行的完整 signed column。这里 \(v_\nu\) 是
[NP](R147-supplement-independent-strict-nu-particular-and-signed-waist-column.md)
的原 strict backward particular：在 \(r=9/50\) 全零、在其上精确零，
不是已经满足全部腰部匹配条件的全局解。物理目标行是
[BR](R149-supplement-target-normalizer-low-rows-by-whole-energy-residual.md)
的真正 \(E_{96}^{a*}\mathcal B^{-1}\)，不能用旧 physical96 配对代替。

实际前置是整个 [DWTB](../notes/2026-11-27-direct-w-and-first-original-B-rows.md)
九目标成功及其 whole row carrier、原 NP/PO/ASB/JC/W/RW 全部实际输入。
本篇不预报 DWTB 成功，也不运行旧 residual、cohomology、norm 或 pairing
目标。所有新数值只在公开 Actions 执行。

## BNC1. 同一物理列、独立两 mean 与原相位

周期 \(\ell=\pi/2\)，测度 \(d\phi/\ell\)，频率 \(4n\)。保持
\(a=2\mathcal H(0)\)、\(b=a+\Omega\)，不用均值平移代替 \(a/2\)。
密度作用和原完整左 receiver 是
\[
 U_Xf=X'f\circ X,\qquad
 \mathcal L_\partial=\tfrac12U_{\mathcal H^{-1}}e^TQ_{R,y}\pi_y,
 \quad e=(1,1),\quad Q_{R,y}=(Id+ER)/2 .
 \tag{BNC.2}
\]
这是 [RW.19--24](R149-supplement-reflected-finite-waist-rows-from-complete-conjugacy.md)
的算子。\(Q_{R,y}\) 是正交反射投影，\(\pi_y\) 留下两个 nonmean
primitive 分量；两 mean 在另两个独立 slots 中保留，不通过删掉它们
来降低原 PDE error。

取原 NP 完整四数组所定义的同一个有限 \(h\)，并令
\[
 Y^a=\mathfrak D_0h=(y_+^a,y_-^a;\mu_+^a,\mu_-^a),\quad
 f^a=\tfrac12(y_+^a+y_-^a),\quad F^a=U_{\mathcal H^{-1}}f^a .
 \tag{BNC.3}
\]
原 reflection qualification 给 \(Q_{R,y}\pi_yY^a=\pi_yY^a\)。
\(f^a\) 是 degree96、real、even、exact mean-zero polynomial；
\(F^a\) 在真物理角中通常有无限 Fourier support，绝不将其 high part 置零。

为明确 necessary carrier 的完整定义，写原193维 waist vector 为
\[
 u(\phi)=\sqrt2\sum_{n=1}^{96}c_n\sin(4n\phi),\quad
 v(\phi)=c_0+\sqrt2\sum_{n=1}^{96}d_n\cos(4n\phi).
\]
仍用原真实 \(q=\sqrt{-K(0)}>0\)、
\(n_g=a(0)^2/m_{\delta_*}(0)^2>0\)，以及整个 selected denominator，
\[
 f^a=\frac{n_g}{\sqrt{2q}}\,Iu,\qquad
 \widehat f^a(n)=-\frac{n_gc_n}{8n\sqrt q}\quad(1\le n\le96),
 \quad\widehat f^a(-n)=\widehat f^a(n),\quad \widehat f^a(0)=0.
 \tag{BNC.4}
\]
两 mean 来自原两 characteristic waves，不由这个 half-sum 公式推断为零。
NP 原 \(m_{\delta_*}(0)\) 的完整球继续使用；所有 q、\(n_g\) 的依赖
在新 directed evaluation 中保留，不选择 numerical selected state。

直接消费
[PO actual](R147-supplement-actual-physical-parameter-observation-inverse-and-high-tail.md)
的完整 \(N_0\ge\|f^a\|_2\)，及
[ASB actual](R147-supplement-actual-short-parameter-errors-and-refined-signed-borders.md)
的完整 \(D_b\ge\|\mathfrak D_0(v_\nu-h)\|_{\mathcal Y_0}\)。
令原整个 \(B_H\ge\|U_{\mathcal H^{-1}}\|_{2\to2}\)。则
\[
 \|F^a\|_2\le B_HN_0,\qquad
 \|F_\nu-F^a\|_2\le B_HD_b/\sqrt2.
 \tag{BNC.5}
\]
后一 \(1/\sqrt2\) 是 (BNC.2) 的完整 half-sum norm。它没有
\(K_W\)，没有正区间 inverse，也没有由 trace point 代替普通 source
积分。所有 ordinary/jump/source/mean 误差已包含在已成 ASB 的 \(D_b\)。

## BNC2. 已成 B rows 与完整 G/H homotopy

记 \(R=E_{96}^{a*}\mathcal B^{-1}\)。DWTB 必须提供全部96个 exact
finite row trials \(\widehat r_j=G_{\rm abs}\widehat y_j\)，
\(G_{\rm abs}=|\partial_\phi|^{-1}\)，degree \(M=192\)，以及完整
\[
 \|R-\widehat R\|_{L^2_0\to\mathbb R^{96}}\le e_R,\qquad
 J\ge\left(2\sum_{j=1}^{96}\sum_{n=1}^{192}
                    |\widehat r_j(n)|^2\right)^{1/2}.
 \tag{BNC.6}
\]
这里 \(J\) 就是 DWTB 已成的
`complete_I_trial_Hilbert_Schmidt_upper`；因为 \(I\) 与
\(G_{\rm abs}\) 的 Fourier multiplier 只差模为1的 sign factor，
两者的上述完整 norm 相同。不重新计算此旧 norm。
[BR.4](R149-supplement-target-normalizer-low-rows-by-whole-energy-residual.md)
给真正的 \(\|R:L^2_0\to\mathbb R^{96}\|\le\sqrt{96}\)。

以下 \(G=K_{48}\circ H_{24}\) 是原 finite compound degree-one lift，
不是 \(G_{\rm abs}\)。用它的完整相位，不换成 \(G_o\)，亦不
忽略未知 \(\mathcal H(0)\)。原 W/JC 给整个
\[
 E_H\ge\|\mathcal H-G\|_{\mathcal A_\sigma},\quad
 G_0\ge\|G-Id\|_{\mathcal A_\sigma},\quad
 G_1\ge\|G'\|_{\mathcal A_\sigma},\quad
 H_1\ge\|\mathcal H'\|_{\mathcal A_\sigma},\quad \sigma=1/128 .
\]
[JC.5--8](R149-supplement-joint-compound-waist-row-error.md) 的两个
下界也适用于这里完整未减常数的
\(X_t=(1-t)G+t\mathcal H\)。证明完全保留如下：
\[
 X_t'\ge1-(G_0+E_H)/\sigma=:m_0,\qquad
 X_t'\ge2-\max(G_1,H_1)=:m_1.
 \tag{BNC.7}
\]
第一式由周期部分的 \(\mathcal A_\sigma\) norm 和
\(\|\partial_\phi q\|_\infty\le\sigma^{-1}\|q\|_{\mathcal A_\sigma}\)。
第二式用两 degree-one derivatives 的零 Fourier 系数精确为1，
故 \(\|G'-1\|_{\mathcal A_\sigma}\le G_1-1\)，\(\mathcal H'\) 同理。
不需要 odd projection；常数相位的导数是零。因此可直接消费 JC
已保存的两个完整 lower 及其正式选择 \(m=\max(m_0,m_1)>0\)，
不重生产旧 lower 目标。真实变量替换仍给
\(\|u\circ X_t\|_2\le m^{-1/2}\|u\|_2\)。

对任意实 unit vector \(z\in\mathbb R^{96}\)，
\(r_z=\sum_jz_j\widehat r_j\) 满足
\(\|r_z\|_2\le J\)、\(\|r_z'\|_2\le4MJ\)。沿完整 homotopy 积分，
\[
 \|r_z\circ\mathcal H-r_z\circ G\|_2
       \le 4ME_HJ/\sqrt m.
 \tag{BNC.8}
\]
于是整个96维 signed vector 的 composition error 不超过
\(4ME_HJN_0/\sqrt m\)。\(J\) 已经是完整行算子的合法 upper；
没有把 \(\widehat r_j\) 当成正交基，也没有额外乘 \(\sqrt{96}\)。

## BNC3. 新192个完整 Fourier observations 与全 alias

新 signed target 先定义
\[
 Q_n=\frac1N\sum_{\ell=0}^{N-1}
       f^a(\phi_\ell)e^{-4inG(\phi_\ell)},\quad
 \phi_\ell=\frac{\ell\pi}{2N},\quad N=8192,\quad1\le n\le M .
 \tag{BNC.9}
\]
这192个 observations 是新的完整函数输入，不是旧 NP 的96个 raw
pairings。它们用 (BNC.4) 的全部96源 modes、原整个 G、全8192点。
保存全部192个 directed disks \(Q_n\in c_n^{\rm quad}+D(0,\rho_n)\)
以后才计算完整 signed vector
\[
 d_j=2\operatorname{Re}\sum_{n=1}^{M}
           \overline{\widehat r_j(n)}c_n^{\rm quad}.
 \tag{BNC.10}
\]
\(c_n^{\rm quad}\) 选 exact dyadic，\(\widehat r_j(n)\) 使用
原 exact rational carrier；(BNC.10) 可直接用有理数求和，保存整个
96个 exact signed rationals。负 modes 全为 conjugates，zero mode
精确为零。行 trial 的真正 \(a\) 误差已由 \(e_R\) 支付；此处不
另做未支付的 target rotation。

完整 finite quadrature 的联合 rounding/input-radius fee 为
\[
 E_{\rm disk}=J\left(2\sum_{n=1}^{M}\rho_n^2\right)^{1/2}.
 \tag{BNC.11}
\]
证明：将 \(\delta Q_n\) 和其 conjugate 组成完整 real polynomial，
其 \(L^2\) norm 至多括号内值，再作用整个 \(\widehat R\)。
因此是全192个 disks，而非96次 scalar row radii 的额外堆加。

真实复合 \(r_z\circ G\) 虽由 finite inputs 定义，仍可能有无限
Fourier support。令 \(L=96\)。归一 Parseval、有限 Cauchy--Schwarz
及整个 Wiener algebra exponential 给
\[
 \|f^a\|_{\mathcal A_\sigma}\le\sqrt{2L}e^{4L\sigma}N_0,\quad
 \|r_z\circ G\|_{\mathcal A_\sigma}
       \le\sqrt{2M}e^{4M(\sigma+G_0)}J.
\]
全 trapezoid alias identity 的非零项只有 frequencies \(kN\)，故
\[
 E_{\rm alias}=
 2\sqrt{LM}\,JN_0
 \exp\!\big(4L\sigma+4M(\sigma+G_0)-4N\sigma\big)
 \tag{BNC.12}
\]
支配整个96维向量从 (BNC.9) finite sums 到真实 integral 的差。
这是 weighted Fourier \(l^1\) 的完整估计：
\(\sum_{k\ne0}|p_{kN}|\le e^{-4N\sigma}\|p\|_{\mathcal A_\sigma}\)，
没有漏掉第一 alias 之后的无限系列，也不需要假定复合有限支集。

每个 \(\rho_n\) 可由下面的 exact unit-circle disk recurrence 生成。
在每个 grid point 取 raw real center \(u\)、phase-step complex center
\(s\)，完整误差 \(|f^a-u|\le\eta\)、\(|e^{-4iG}-s|\le\tau\)。
置 \(z_0=1,r_0=0\)，每步取 exact midpoint \(z_{n+1}\) of \(z_ns\)，
\[
 r_{n+1}= \operatorname{up}\{r_n+(1+r_n)\tau
                                  +|z_ns-z_{n+1}|\}.
 \tag{BNC.13}
\]
因为真实 phase-step 的模精确等于1、\(|z_n|\le1+r_n\)，此式包住
全部幂误差。把所有 raw radii 的平均、全部 \(|u|r_n\) 的平均、
和最后 finite sum 的 midpoint error 相加即得 \(\rho_n\)。
这与旧 ASR rectangular recurrence 的巨量包裹误差不同，但既不
改旧 ASR 结论，也不调用旧 alpha/cohomology/norm 目标。
8192个新 disk input、每个完整 mode 和所有192个 mode 的全文件
都先保存读回；任何 prefix 都不能冒充整个列。

## BNC4. 整个真实列的联合误差与消费合同

将 (BNC.5--12) 相加，得到
\[
 \boxed{\;
 \|b_\nu-d\|_{\mathbb R^{96}}
 \le E_\nu :=
 e_RB_HN_0+\sqrt{96}\,B_HD_b/\sqrt2+
 \frac{4ME_HJN_0}{\sqrt m}+E_{\rm alias}+E_{\rm disk}.
 \;}
 \tag{BNC.14}
\]
分解先在完整 physical \(L^2_0\) 中进行：
\[
 RF_\nu-d=(R-\widehat R)F^a+R(F_\nu-F^a)
 +\{\widehat RF^a-\langle\widehat r_j\circ G,f^a\rangle_j\}
 +\{\langle\widehat r_j\circ G,f^a\rangle_j-d\}.
\]
密度 adjoint 是 \(U_{\mathcal H^{-1}}^*r=r\circ\mathcal H\)，
这里没有额外 Jacobian；其非等距性已分别由 \(B_H\) 与 \(m^{-1/2}\)
付清。只有第二项使用真正 whole receiver 的 \(\sqrt{96}\)；
第一项和其他联合项没有额外行数损失。

首次 actual 保存五个完整非负 component fees，再从其正式读回球
保存 \(E_\nu\)，最后保存一个完整96列 signed object。它同时保留
原两独立 mean 的既成 balls 及完整NP身份，不称这些 mean 已由
\(\mathcal B^{-1}\) 作用或已经完成非局部 physical-height matching。
96个 \([d_j-E_\nu,d_j+E_\nu]\) 是方便逐项消费的包络；后继必须同时
保留更强的 joint \(l^2\) 资格 (BNC.14)。

必要恢复只允许原 NP 四数组和 DWTB 整个 row trial 的原 SHA：
不再运行 NP residual、旧194 observations、PO inverse/norm、
ASB source/norm、DWT 两 scalar 或 BR 七 residual/norm 目标。
未来 owner 需完整验证这些 predecessors 的 source/manifest/process/
whole actual/execution，不能只凭展示小数或一个 success 布尔。

纯模块
[fourfold_codazzi_target_normalized_strict_nu_column.py](../scripts/fourfold_codazzi_target_normalized_strict_nu_column.py)
给 (BNC.4)、(BNC.9--14) 的完整公式、natural192-mode prefix 和
whole signed rational contraction。它不做 IO、不导入数值库、也不
在本地执行科学目标。此列可作为原有限 bordered system 的真正
target-normalized \(\nu\) 右端；完整 homogeneous96、high incoming、
physical means、非局部 phase、full Schur 及最终嵌入族仍分别保留。
