# 原连续尾高次创建观测的准确范围守卫

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_resume；AI-assisted，GPT-6 Astra Pro。
状态：完整辅助证明，供附在既有高孔观测笔记后。不登记新排核范围，不作为真实三 Gram 比较的反例。


## 恢复与当前去重记录

本稿按 `HANDOFF.md` 记录，从未推送源 blob
`c506f044f1865e23025b13a260d5bb5f8de76bab` 恢复。
2026-11-13 终端恢复后，Astra-ISP-0c017065 / boundary_nonprimitive_1856
重新核算有限补集酉、Vandermonde 两个核身份、远尾正交平方和、
实际左最小性及固定 $m$ 的合法上窗限制。下文历史正文保留完整。

**当前状态：已证明，但已被后续结果覆盖，不重复登记新范围。**
最新[高孔观测笔记 §10.1](2026-11-13-actual-high-hole-first-head-tests-and-transverse-observation-gap-1cf.md)
使用同一个有限补集向量，已经证明全部整数 $k\ge1$ 的更强准确式
$$
\|(D_m^*)^kg_{m,q}\|^2
=(k!)^2\bigl(e_k^{(J)}+a_{m,q}e_{k-1}^{(J)}\bigr),
\qquad J=m+2q,
$$
其中 $e_k^{(J)}$ 为原尾平方权的初等对称函数，
$a_{m,q}=\|D_I^*(\mathcal C_I X/\|X\|)\|^2$。
$k=2$ 正好给下文式 (4)。该笔记 §§10.2–10.4 又使用原真实
dyadic 头和原合法 $q_m=\lfloor e^{d^3/4}\rfloor$，
支付变化 $m$ 的定量观测障碍。其 §§11–14 则进一步保完整右源费用、
全部 primitive 尾位置和真实 $W$ 的投影，因此这些后续结论不能
从本历史守卫反向删去或降格。

本次恢复没有得到真实三 Gram 比较的反例，没有给非primitive 左费用上界，
也没有改变普通 ISP 的未解状态。

---

本段承接
[高孔观测笔记 §9](2026-11-13-actual-high-hole-first-head-tests-and-transverse-observation-gap-1cf.md)
已经保存的完整链与伴随身份，不重复构造那些测试。
该节对全头 primitive 源的真正左最小者
$v=\sum_{j=1}^{d-1}e_jv_j$，$Dv_j=0$，证明
$$
\left\|P_{\ker D_m^d\cap\mathcal H_{q+j}^{(m)}}(D_m^*)^jv_j\right\|
\le C_{m,j}\lambda(r^\flat).
\tag{1}
$$
当 $2j+1\le d$ 时可以去掉投影。这里给出不能仅凭一次纯尾环境下界反转高次观测的实际原权构造。

## 1. 原权前缀及补集酉

固定 $m\ge5$，令
$$
D=D_m=\sum_{i\ge m}a_iE_i,\qquad
a_i=(i+1)^{-2},\qquad
\nu_m=\|D_m\|\le m^{-1}.
$$
取任意整数 $q\ge1$，前缀
$I=\{m,\ldots,m+2q-1\}$，余尾起点 $J=m+2q$。
分别写 $D_I=\sum_{i\in I}a_iE_i$ 与 $D_J=\sum_{i\ge J}a_iE_i$。

已证的
[Vandermonde 反例](../results/R239-appendix-vandermonde-coprimitive-short-kernel-counterexamples.md)
在这 $2q$ 个两两不同的正权上给非零
$X\in\mathcal H_q(I)$，满足
$$
D_I^*X=0,\qquad D_I^2X=0.
\tag{2}
$$
这里 $D_I^2$ 是两次顺序删除，交叉系数为 $2a_ia_j$；
不是系数的点态平方。

令 $C_Ie_F=e_{I\setminus F}$ 为有限布尔前缀的补集酉。
它不改变原正交度量，且
$$
D_IC_I=C_ID_I^*,\qquad D_I^*C_I=C_ID_I.
$$
定义
$$
y_q=\frac{C_IX}{\|X\|}\otimes\Omega_J.
$$
由于 $|I|=2q$，它仍在原尾孔层 $\mathcal H_q^{(m)}$，并且
$$
\boxed{\|y_q\|=1,\qquad Dy_q=0,\qquad
(D_I^*)^2(C_IX)=0.}
\tag{3}
$$
这是同一个原连续尾中的 primitive 单位向量，不涉及有限模型权重的重标度。

## 2. 二次创建范数的精确账

令
$$
S_J=\sum_{i\ge J}a_i^2.
$$
头尾交换以及 (3) 给
$$
(D^*)^2y_q
=
2D_I^*\frac{C_IX}{\|X\|}\otimes D_J^*\Omega_J
+\frac{C_IX}{\|X\|}\otimes(D_J^*)^2\Omega_J.
$$
两项分别具有余尾孔数一和二，故正交。因此
$$
\begin{aligned}
\|(D^*)^2y_q\|^2
&=4\left\|D_I^*\frac{C_IX}{\|X\|}\right\|^2S_J
+4\sum_{J\le i<k}a_i^2a_k^2\\
&\le4\nu_m^2S_J+2S_J^2.
\end{aligned}
\tag{4}
$$
全部级数因 $\sum a_i^2<\infty$ 收敛。积分估计给
$$
S_J\le\frac1{3J^3}.
$$
固定 $m$ 而 $q\to\infty$，(4) 趋于零。每个固定 $j\ge2$ 进一步满足
$$
\boxed{
\|(D^*)^jy_q\|
\le\nu_m^{\,j-2}
\bigl(4\nu_m^2S_{m+2q}+2S_{m+2q}^2\bigr)^{1/2}
\longrightarrow0.
}
\tag{5}
$$
因此对任意固定 $j\ge2$，原算子
$(D_m^*)^j$ 在所有孔层 primitive 单位向量的并集上没有严格正下界。
这与一次的已证环境下界不矛盾；后者在 $Dy_q=0$ 上仍给
$\|D_m^*y_q\|\ge2^{-7}(m+2)^{-5}$。

## 3. 对已付全头测试意味着什么

固定 $d=2^m$ 与 $2\le j\le d-1$，取
$v=e_jy_q$、$r=A_me_jy_q$。
它是 (1) 允许的全头 primitive 源，真正左最小费用恰为
$\mu(r)=1$。
其所有非零坐标的创建观测只有第 $j$ 项，而由正交投影收缩和 (5)，
$$
\left\|P_{\ker D_m^d\cap\mathcal H_{q+j}^{(m)}}(D_m^*)^jy_q\right\|
\longrightarrow0.
\tag{6}
$$
所以仅凭 (1) 左侧的整组创建观测，不能用一个对全部 $q$ 相同的正系数反向控制 $\mu$。
当 $2j+1\le d$ 时，已证
$D^{2j+1}(D^*)^jy_q=0$，投影确实恒等；(6) 并非由投影损失造成。

必须同时保留以下范围：

- (5) 是固定 $m$、全部孔层上的环境结论。$q\to\infty$ 最终超过同一个 $m$ 的实际 lift 合法上窗；它不声称在该有限上窗内没有依赖 $m$ 的正下界。
- (1) 是创建观测被 $\lambda(r^\flat)$ 控制。观测趋零不能反向推出 $\lambda(r^\flat)\to0$。
- 本构造没有估计裸费用 $\alpha(r)$，没有把源置于原 $w\in W$ 的实际窄来源，也不反驳任何已付的固定前缀逆界。
- 固定 $j$ 的头前缀本来有直接有限矩阵逆。这里不新增排核范围；将 $j$ 随 $m$ 增长时，仍须原样支付实际头费用、完整源 Gram 与真实窄通量。

一般非primitive 源的左最小者还含较低孔层；不能把其与测试源的配对只保留顶层。
后续仍需使用原 $A_m$ 的长跳跃或真正 $\overline f$ 的相容来源，控制完整最小费用。

