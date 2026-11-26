# R149 补篇：同一共轭复合的完整96行算子误差

2026-11-27，visible-exact-astra-fb31ed6-20261127 / trial_restore。

**新增解析结论。** RW 的96行共用同一个真实 odd lift 与同一个有限复合 lift。对这两个 lift 之间的整个 homotopy 先付真实 Jacobian 下界，再对真 target 的96维 Fourier 空间用 Bernstein 不等式，可以直接估计联合 row operator。完整 DFT alias 与截断另以一个 joint Wiener bound 支付；无需把共轭误差按96个 scalar rows 独立相加。

本篇不运行 KAM、旧96个 row residual、或任何 PDE 列。它保持 RW 的原 exact DFT trial 定义、原反射轴、normalized measure、两 physical means 和 fixed \(J_s\)。所得新联合 row 界可直接替换 [JF.9–12](R149-supplement-joint-signed-finite-matrix-error.md) 中的 row-error 上界；完整 P224、真实列误差、signed matrix 与真正 Schur 的前置不变。

## JC1. 完整旧输入、物理 strip 与真实频率

使用 [W 的实际 run43588332723/1](R133-supplement-actual-physical-Wiener-conjugacy-strip.md)，唯一 selected loss 为 \(1/250\)。其整个原 native 为

`notes/phase_strip_refinement_ci/run-43588332723-1/consumers/R31-strip-refinement.json.gz`，3356 bytes，SHA256
`dfb2a174a010d399775240b2bd07a0f547dfee5fc137e12141be9fd8a46e3854`。

从完整已验证原件的以下路径直接读取完整 saved upper，不能从 RW 的 scalar error 反推：

| 本篇符号 | 原 native 路径 |
|---|---|
| \(E_H\) | `selected.physical_true_conjugacy_minus_G_norm` |
| \(G_0\) | `exact_G_periodic_norm` |
| \(G_1\) | `exact_G_derivative_norm` |
| \(H_1\) | `selected.physical_true_conjugacy_derivative_Astrip_upper` |

它们分别支配 \(\|\mathcal H-G\|_{\mathcal A_\sigma}\)、\(\|G-\mathrm{id}\|_{\mathcal A_\sigma}\)、\(\|G'\|_{\mathcal A_\sigma}\)、\(\|\mathcal H'\|_{\mathcal A_\sigma}\)，其中 \(\sigma=1/128\)，\(G=K_{48}\circ H_{\rm fin}\)。全部八个原 loss 结果及其真/假状态保持原件，不重新挑另一个 selected member。

这里的物理角是 \(\phi\)，周期 \(\ell=\pi/2\)，
\[
\|q\|_{\mathcal A_\sigma}
 =\sum_{n\in\mathbb Z}|\widehat q(n)|e^{4|n|\sigma},
\qquad
\partial_\phi e^{4in\phi}=4in e^{4in\phi}.
\tag{JC.1}
\]
这与 W 原 producer 使用 \((4j)^k e^{4j\sigma}\) 的 `trig_norm` 完全相同，不把 normalized angle \(4\phi\) 的宽度误用为物理 \(\sigma\)。由 \(x\le e^x\)，对于周期函数 \(q\)，
\[
\|q'\|_\infty\le\sigma^{-1}\|q\|_{\mathcal A_\sigma}.
\tag{JC.2}
\]
证明是在每个 \(n\ne0\) 上使用 \(4|n|\le\sigma^{-1}e^{4|n|\sigma}\)，零频的导数为零。实轴 \(L^\infty\) 与下文所有 \(L^2\) 都用同一物理角；normalized measure 是 \(d\phi/\ell\)。

## JC2. 两个完整 degree-one lift 间的统一 Jacobian 下界

[RW.1–10](R149-supplement-reflected-finite-waist-rows-from-complete-conjugacy.md) 给出
\[
\psi(\phi)=\mathcal H(\phi)-\mathcal H(0),\qquad
G_o(\phi)=\frac{G(\phi)-G(-\phi)}2,
\]
\[
\|\psi-G_o\|_{\mathcal A_\sigma}\le E_H,\qquad
\|G_o-\mathrm{id}\|_{\mathcal A_\sigma}\le G_0.
\tag{JC.3}
\]
两者都是实 odd degree-one lift。设
\[
F_t=(1-t)G_o+t\psi,\qquad 0\le t\le1.
\tag{JC.4}
\]
其周期部分的 Wiener norm 不超过 \(G_0+E_H\)，故 (JC.2) 给
\[
F_t'\ge m_0:=1-(G_0+E_H)/\sigma.
\tag{JC.5}
\]

可以直接消费已成 \(G_1,H_1\) 得到另一完整下界。每个 degree-one lift 的导数的零 Fourier coefficient **精确等于1**，所以
\[
\|G_o'-1\|_{\mathcal A_\sigma}
 =\|G_o'\|_{\mathcal A_\sigma}-1\le G_1-1,
\quad
\|\psi'-1\|_{\mathcal A_\sigma}
 =\|\psi'\|_{\mathcal A_\sigma}-1\le H_1-1.
\tag{JC.6}
\]
第一式使用 \(G_o'=(G'(\phi)+G'(-\phi))/2\) 的 even projection 收缩；第二式有 \(\psi'=\mathcal H'\)。这次减1来自确切的 Fourier norm 分解，不是从两个无关 operator upper 中相减，也不要求 \(G'\) 与 \(\mathcal H'\) 相同。

因此对所有 \(t,\phi\)，
\[
F_t'\ge m_1:=2-\max\{G_1,H_1\},\qquad
F_t'\ge m:=\max\{m_0,m_1\}.
\tag{JC.7}
\]
实际 directed owner 保留两个完整 lower，再选择较大 lower 并核 \(m>0\)。原 W 已有两完整 derivative bounds 小于2，故这里有正的解析余量；本篇不以显示小数替代实际球生成一个新数值证书。

当 \(m>0\) 时，每个 \(F_t\) 是同一圆上的 orientation-preserving degree-one diffeomorphism。对任意周期 \(u\in L^2\)，真实变量替换给
\[
\|u\circ F_t\|_{L^2(d\phi/\ell)}^2
 =\int_{\mathbb T}|u(x)|^2
       \frac{dx/\ell}{F_t'(F_t^{-1}(x))}
 \le m^{-1}\|u\|_2^2.
\tag{JC.8}
\]
非等距角变换的 Jacobian 明确留在 \(m^{-1/2}\)，没有免费取消。

## JC3. 完整 target96 空间的联合 composition bound

仍取真实反射轴 \(a=2\mathcal H(0)\) 和原 target 的实正交归一基
\[
g_j(x)=\sqrt2\cos(4j(x-a/2)),\qquad1\le j\le M:=96.
\tag{JC.9}
\]
对任意 \(b\in\mathbb R^{96}\)，令
\[
q_b(x)=\sqrt2\sum_{j=1}^{M}b_j\cos(4jx).
\]
平移是 normalized circle 上的等距，所以这与 \(\sum b_jg_j\) 是同一个 norm 的 target polynomial。Parseval 给
\[
\|q_b\|_2=\|b\|_2,\qquad
\|q_b'\|_2^2=\sum_{j=1}^{M}(4j)^2b_j^2
 \le(4M)^2\|b\|_2^2.
\tag{JC.10}
\]
这是该真实有限空间的 Bernstein 界；不把 pullback 后的 \(f_j\) 或 finite \(p_j\) 当成正交基。

由积分形式的微分恒等式，
\[
q_b\circ\psi-q_b\circ G_o
 =(\psi-G_o)\int_0^1q_b'\circ F_t\,dt.
\]
使用 (JC.3) 的实轴 sup 控制、Minkowski、(JC.8)、(JC.10)，得到
\[
\boxed{\quad
\|q_b\circ\psi-q_b\circ G_o\|_2
 \le\frac{4M E_H}{\sqrt m}\,\|b\|_2.
\quad}
\tag{JC.11}
\]
这是同一个共同角误差对整个96维输入的算子界，而不是96个独立 pointwise residual 的重新计算。它继续使用原 \(E_H\)，没有从旧 scalar row error 减掉其他正项来制造一个更小共轭误差。

## JC4. 原 exact DFT 的全部 alias 与无限尾

保持 RW 的 \(L=4096\)、\(N=1024\) 和同一 exact finite sums。记 \(p_j\) 为 RW.14 的原 row trial，\(p_b=\sum b_jp_j\)。DFT 是线性的，故 \(p_b\) 正是 \(v_b=q_b\circ G_o\) 的同一 truncated DFT，而不是新选的 row。

完整 Wiener algebra exponential 估计给
\[
\|\sqrt2\cos(4jG_o)\|_{\mathcal A_\sigma}
 \le\sqrt2\exp(4j(\sigma+G_0)).
\]
对整个 \(b\)，先用 \(j\le M\)，再用 finite Cauchy–Schwarz，得到
\[
\|v_b\|_{\mathcal A_\sigma}
 \le B_{\rm joint}\|b\|_2,
\qquad
B_{\rm joint}:=\sqrt{2M}\exp(4M(\sigma+G_0)).
\tag{JC.12}
\]
这是一个新的联合 norm bound，不重新生产旧96个 RW 误差目标。

RW.16–17 的完整 alias identity 对这个 \(v_b\) 直接适用：\(2N<L\) 保证 alias 索引的唯一性，\(\mathcal A_\sigma\) 保证绝对收敛。故
\[
\|v_b-p_b\|_2
 \le T_{\rm joint}\|b\|_2,
\]
\[
T_{\rm joint}:=B_{\rm joint}
 \left(e^{-4\sigma(N+1)}+e^{-4\sigma(L-N)}\right).
\tag{JC.13}
\]
此式支付整个 Fourier truncation 和整个无限 DFT alias。\(G\) 的有限定义不会使 \(q_b\circ G_o\) 有有限 Fourier 支集；该无限尾没有被删去。

将 (JC.11)、(JC.13) 相加，记
\[
E_{\rm joint}:=4M E_H/\sqrt m+T_{\rm joint},
\]
\[
\boxed{\quad
\left\|\sum_{j=1}^{96}b_j(f_j-p_j)\right\|_2
 \le E_{\rm joint}\|b\|_2,
\qquad f_j=g_j\circ\mathcal H.
\quad}
\tag{JC.14}
\]
因此同一个完整 row analysis error 算子及其 adjoint 的范数都不超过 \(E_{\rm joint}\)。这是一个完整替代候选；若另有已验证的 \((\sum\varepsilon_j^2)^{1/2}\)，可对同一完整算子取二者较小的已保存 upper，但不能把两种证明的局部项任意混接。

## JC5. 原 physical、incoming 与 JF 的准确接线

在 \(\mathcal Y_0=L^2_0(\mathbb T;\mathbb R^2)\oplus\mathbb R^2\) 上，physical row injection 是 \(f\mapsto(Pf/2,Pf/2;0,0)\)，norm 为 \(1/\sqrt2\)；incoming scalar injection 是 \(\iota_+f=(Pf,0;\Pi f,0)\)，为等距。后者保留非零 old-angle mean。

故完整96行的 row-trial analysis errors 满足
\[
\|R_\partial-R^a_\partial\|\le E_{\rm joint}/\sqrt2,
\qquad
\|R_{\rm in}-R^a_{\rm in}\|\le K_{W,0}E_{\rm joint}.
\tag{JC.15}
\]
对于 TC 的原有限 trial 列空间，RW.7、RW.26 仍精确给
\[
\|(R_{\rm in}-R^a_{\rm in})|_{\operatorname{ran}Y^a}\|
 \le E_{\rm joint}.
\tag{JC.16}
\]
原因是该整个空间的 primitive Fourier 支集低于原 \(J_s\)，同时保留全部两 mean，故 \(\widehat T_0^{-1}Y^a=Y^a\)。真列误差的完整左 receiver 仍按 JF.4 支付 \(B_{H,0}K_{W,0}\)，不能把本消去扩大到它。

于是 JF.11 可以使用新的完整候选
\[
\Xi_A=\Gamma_A\Delta_s+\kappa_AE_{\rm joint}V_s,
\tag{JC.17}
\]
其中 \(\Gamma_A,\kappa_A\) 原样取 JF.12。真实角变换一方面在完整 receiver 的 \(B_{H,0}\) 中支付，另一方面在这个不同的 row approximation 问题中由实际 homotopy Jacobian 支付；没有把非等距变换当成 unitary。

纯算法 [fourfold_codazzi_joint_compound_waist_row_error_math.py](../scripts/fourfold_codazzi_joint_compound_waist_row_error_math.py) 实现 JC.5、7、11–14 的新联合标量公式。它提供原四球的精确路径和 whole-W metadata 检查，不读写、不导入数值库、不执行旧 producer。公开 owner 应先核整个 W native/source/process/publication 与同一 RW 定义，直接读上述四球，再公开执行新的联合标量目标；不得只给四个显示小数或以 metadata 布尔字段代替完整原件身份。

这个新 row 目标本身不需要尚未完成的 P224；将它用于真 PDE 列或有限逆时，仍须全部 JF/SC 前置。这里没有新的 signed entries，没有宣布96方阵已可逆，更未完成 high elimination、\(\mathcal B^{-1}\)、\(\Theta_{96}\)、physical mean、phase、\(\nu\) 的真实 Schur。
