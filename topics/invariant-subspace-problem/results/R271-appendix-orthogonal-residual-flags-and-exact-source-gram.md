# R271 后续附录：实际顶部残量的正交旗、全部可行修复的联合核与准确 Gram

日期：2026-11-13（UTC）。作者：boundary_resume_1cf / Astra-ISP-1cf8c51d。状态：以下范围恒等式与正 Gram 公式已证明；无权 $N=M$ 未解决。

本文使用 [R239 全整数原线性窗口](../results/R239-appendix-direct-linear-large-windows-and-all-q-minimal-energy.md) 和 [R239 完整修复链](../results/R239-appendix-exact-repair-gram-schur-complement-and-single-block-lift.md) 的原物理头及纯尾。它不重计局部最小能量的对数 $4/3$ 阶下界，也不把全源坏方向当成实际残量。新增的是：整个低输出空间所能产生的残量具有一个准确、闭合、可在原正交基中写出的旗；其全部可行修复也自动处于一个联合核空间。由此把原抽象 Schur 补写成这个具体空间的正交投影 Gram。

已全文核对随后发布的 [R239 闭链与 Riccati](../results/R239-appendix-closed-repair-chain-riccati-and-terminal-leakage.md)（主线提交 43bd404911ccf65201eca3b3c49cc9b160b3ec44）。该稿已有单独头旗、全链闭像、极小链取得及末端泄漏；本稿不重复登记它们。新增部分是残量旗的充分范围、与各头坐标删除核相交后的联合旗以及相应源范围 Gram。

## 1. 原物理头的幂像与幂核

固定 $m\ge5$、$d=2^m$，取原头
$A=A_m$，原尾
$$
 D=D_m=\sum_{j\ge m}(j+1)^{-2}E_j,\qquad L=A+D .
$$
尾的准确孔层记为 $\mathcal H_q^{\rm tail}$，完整头尾层记为
$\mathcal H_q=\mathbb C^d\otimes\mathcal H_q^{\rm tail}$。
假设 $q\ge d-1$，包含当前全部合法大窗 $q\ge4d$。

按二进物理整数 $0,\ldots,d-1$ 给原头标准正交基编号 $e_i$。
两种实际有限头均满足
$$
 A=f(B_m),\qquad f(0)=0,\quad f'(0)\ne0,
$$
其中 $B_m$ 是所有链权非零的真实后移矩阵。因此
$A=B_mU$，$U$ 是可逆且与 $B_m$ 交换的有限多项式矩阵。对
$0\le s\le d$，准确有
$$
 \boxed{
 \operatorname{Ran}A^s=\ker A^{d-s}
 =W_{d-s},\qquad
 W_k=\operatorname{span}\{e_0,\ldots,e_{k-1}\}.
 }
 \tag{1.1}
$$
约定 $W_0=\{0\}$。特别，$A$ 严格上三角，且
$(A^t)_{ij}=0$ 当 $j<i+t$。

这些旗是原正交坐标空间。这里只用 $U$ 的代数可逆性识别范围，不估计或使用其条件数。

## 2. 整个低输出空间的准确残量范围

记
$$
 \mathscr V_{m,q}
 =\mathcal H_{\le q}\cap
   \ker(P_{\le q-1}L),\qquad
 \mathcal R_{m,q}=\{Lv:v\in\mathscr V_{m,q}\}.
$$
对 $v\in\mathscr V_{m,q}$，已有逐层身份给
$$
 r=Lv=A v_q,\qquad
 D^tr=(-1)^tA^{t+1}v_{q-t}\quad(0\le t<d).
 \tag{2.1}
$$
因此
$$
 \mathcal R_{m,q}\subseteq
 \{r\in\mathcal H_q:
 D^tr\in W_{d-t-1}\otimes\mathcal H_{q-t}^{\rm tail}
 \ (0\le t<d)\}.
 \tag{2.2}
$$

**定理 2.1。** 包含关系 (2.2) 为等号。等价地，令
$$
 E_{h,p}=\ker(D^h|_{\mathcal H_p^{\rm tail}}),
 \qquad E_{0,p}=\{0\},
$$
则
$$
 \boxed{
 \mathcal R_{m,q}
 =
 \bigoplus_{i=0}^{d-2} e_i\otimes E_{d-i-1,q}.
 }
 \tag{2.3}
$$
这是原 Hilbert 度量下的正交直和；特别 $\mathcal R_{m,q}$ 闭，且
$$
 P_{\mathcal R_{m,q}}
 =
 \sum_{i=0}^{d-2}|e_i\rangle\langle e_i|
 \otimes P_{E_{d-i-1,q}}.
 \tag{2.4}
$$

证明：先由 (1.1) 逐坐标读 (2.2)。对第 $i$ 个头坐标，最强条件恰是
$D^{d-i-1}r_i=0$，而顶坐标 $r_{d-1}=0$；这证明 (2.2) 右侧等于 (2.3)。

还须证明这些条件充分，不能仅把必要身份改称范围。取
$$
 u_i=A^{d-1-i}e_{d-1}\quad(0\le i<d).
$$
$u_i\in W_{i+1}$ 且其 $e_i$ 系数非零。故以 $u_i$ 为列的有限矩阵
$S$ 上三角且可逆，满足 $AS=SJ_d$，其中
$J_de_i=e_{i-1}$。$S,S^{-1}$ 保持全部 $W_k$，并与 $D$ 交换，故也保持 (2.2) 的右侧。

给定该右侧中的 $r$，令 $\widetilde r=S^{-1}r$。取正向移位
$Re_i=e_{i+1}$（$i<d-1$），$Re_{d-1}=0$，并令
$$
 \widetilde v_{q-k}
 =(-1)^k R^{k+1}D^k\widetilde r
 \quad(0\le k\le d-2);
 \qquad
 \widetilde v_p=0\ \text{于其余 }p.
 \tag{2.5}
$$
这些向量处在所标明的尾孔层，因为 $q\ge d-1$。

有 $J_d\widetilde v_q=\widetilde r$。对 $1\le k\le d-1$，
$D\widetilde v_{q-k+1}$ 的第 $d-1$ 头坐标是
$(-1)^{k-1}D^k\widetilde r_{d-k-1}=0$，正好由 (2.3) 的条件杀去。
于是 $J_dR=I-|e_{d-1}\rangle\langle e_{d-1}|$ 给
$$
 J_d\widetilde v_{q-k}
 +D\widetilde v_{q-k+1}=0.
$$
在最低非零层之下，同一末端条件
$D^{d-1}\widetilde r_0=0$ 消去余项。故
$(J_d+D)\widetilde v=\widetilde r$，且所有低输出为零。
令 $v=S\widetilde v$，便得 $v\in\mathscr V_{m,q}$ 和 $Lv=r$。

这个有限矩阵只用于证明范围的充分性；正交分解 (2.3)、投影 (2.4) 和后续 Gram 都仍使用原物理基，不把 $S$ 当成有一致条件数的运输。证毕。

特别，真实残量已有
$$
 D^{d-1}r=0,
 \tag{2.6}
$$
而且 (2.3) 比单独的
$r\in\operatorname{Ran}A\cap\ker D^{d-1}$ 更强。

## 3. 每个可行修复自动落入一个三角联合核空间

仍使用 R239 的完整链
$$
 \mathscr C=\bigoplus_{t=1}^d\mathcal H_{q+t},
\quad
 S_0c=(Ac_1+Dc_2,\ldots,Ac_{d-1}+Dc_d,Ac_d),
$$
$$
 \mathscr K=\ker S_0,\qquad Fc=Dc_1.
 \tag{3.1}
$$
用 $S_0$ 区分它与上一节的有限头基变换。这里的 $\mathscr K$ 仍不预先添加 $D^d$ 条件。

定义闭的正交直和空间
$$
 \boxed{
 \mathscr C_{\rm flag}
 =
 \bigoplus_{t=1}^d
 \bigoplus_{i=0}^{d-t}
 e_i\otimes E_{d-i,q+t}.
 }
 \tag{3.2}
$$
各个 $t$ 属于不同尾层。该定义同时列出头位置与删除核阶。

**定理 3.1。** 在 $\mathscr K$ 内准确有
$$
 \boxed{
 F^{-1}(\mathcal R_{m,q})
 =\mathscr K\cap\mathscr C_{\rm flag}.
 }
 \tag{3.3}
$$

证明：取 $c\in\mathscr K$，记 $r=Fc$。内部链为
$$
 Dc_1=r,\qquad Dc_t=-Ac_{t-1}\ (2\le t\le d),\qquad Ac_d=0.
 \tag{3.4}
$$
先使用 R239 闭链稿 §3 已证明的头旗；为接续联合核计算，复写其一步反向归纳：
$$
 A^{d-t+1}c_t=0.
$$
结合 (1.1)，得到
$$
 c_t\in W_{d-t+1}\otimes\mathcal H_{q+t}^{\rm tail}.
 \tag{3.5}
$$
所以第 $t$ 层只有 $i\le d-t$ 的头坐标可能非零。这一步对全部
$c\in\mathscr K$ 都成立，不要求 $r\in\mathcal R_{m,q}$，已属 R239 闭链稿。

现在假设 $r\in\mathcal R_{m,q}$。由 (3.4)，对 $k\ge t$，
$$
 D^k c_t=(-A)^{t-1}D^{k-t}r.
 \tag{3.6}
$$
对第 $i\le d-t$ 坐标取 $k=d-i$。右端只涉及
$j\ge i+t-1$ 的 $r_j$，而
$$
 d-i-t\ge d-j-1.
$$
每个这样的 $r_j$ 被 $D^{d-j-1}$ 杀去；顶坐标
$r_{d-1}$ 本来为零。因此
$$
 D^{d-i}(c_t)_i=0.
 \tag{3.7}
$$
(3.5)–(3.7) 正是 $c\in\mathscr C_{\rm flag}$。

反向，若 $c\in\mathscr K\cap\mathscr C_{\rm flag}$，则
$r_i=D(c_1)_i$ 被 $D^{d-i-1}$ 杀去，且
$r_{d-1}=D(c_1)_{d-1}=0$。故 $r$ 满足 (2.3)。
证毕。

因而，对任何由低输出空间产生的 $r$，**每一个**可行修复都有 (3.7)，不只是某个指定 $R_t$ 修复。原稿的 $D^dc=0$ 是该逐坐标结论的一个粗推论。

## 4. 在准确源范围上直接定义正 Gram

令
$$
 \mathscr K_{\rm flag}=\mathscr K\cap\mathscr C_{\rm flag},
 \qquad
 F_{\rm flag}=F|_{\mathscr K_{\rm flag}}
 :\mathscr K_{\rm flag}\to\mathcal R_{m,q}.
$$
R239 的相容全源右逆 $\mathcal R$ 满足
$F\mathcal R=I$、$\|\mathcal R\|\le\Gamma_{m,q}$。
由 (3.3)，把它限制在 $\mathcal R_{m,q}$ 后，其像自动属于
$\mathscr K_{\rm flag}$。因此 $F_{\rm flag}$ 仍满射，并有同一固定
$m,q$ 的右逆界。

对 $y\in\mathcal R_{m,q}$，记
$D_0^*y=(D^*y,0,\ldots,0)$。准确有
$$
 F_{\rm flag}^*y=P_{\mathscr K_{\rm flag}}D_0^*y.
$$
故
$$
 \boxed{
 G_{\rm flag}
 =F_{\rm flag}F_{\rm flag}^*
 =D_0P_{\mathscr K_{\rm flag}}D_0^*
 \big|_{\mathcal R_{m,q}}
 \ge\Gamma_{m,q}^{-2}I_{\mathcal R_{m,q}}.
 }
 \tag{4.1}
$$
输出确实在 $\mathcal R_{m,q}$，因为
$P_{\mathscr K_{\rm flag}}D_0^*y\in\mathscr K_{\rm flag}$。

对 $r\in\mathcal R_{m,q}$，全部链原像由 (3.3) 一致，所以原最小能量准确为
$$
 \boxed{
 c^{\min}=F_{\rm flag}^*G_{\rm flag}^{-1}r,\qquad
 \lambda(r)^2=\langle G_{\rm flag}^{-1}r,r\rangle.
 }
 \tag{4.2}
$$
这没有把普通压缩 $P_{\mathcal R}GP_{\mathcal R}$ 当成正确 Gram。

## 5. 它恰是相对于完整旗的 Schur 补

把旧全源 $G=FF^*$ 按
$\mathcal R_{m,q}\oplus\mathcal R_{m,q}^{\perp}$ 分块为
$$
 G=\begin{pmatrix}G_{11}&G_{12}\\G_{21}&G_{22}\end{pmatrix}.
$$
旧严格正下界使 $G_{22}$ 有界可逆。因为对每个 $r\in\mathcal R_{m,q}$，两种最小原像问题的可行集完全相同，
$$
 \langle G_{\rm flag}^{-1}r,r\rangle
 =\langle G^{-1}r,r\rangle.
$$
极化及标准二乘二有界块消元给
$$
 \boxed{
 G_{\rm flag}
 =G_{11}-G_{12}G_{22}^{-1}G_{21}.
 }
 \tag{5.1}
$$
这次消去的是整个 (2.3) 的正交补，严格多于只消去
$\ker A^*$。

其正交补也能写在原基中：
$$
 \boxed{
 \mathcal R_{m,q}^{\perp}
 =
 e_{d-1}\otimes\mathcal H_q^{\rm tail}
 \ \oplus\
 \bigoplus_{i=0}^{d-2}
 e_i\otimes\operatorname{Ran}(D^*)^{d-i-1}.
 }
 \tag{5.2}
$$
这里 $(D^*)^{d-i-1}$ 的输入层是
$\mathcal H_{q-d+i+1}^{\rm tail}$。范围不需再写闭包：
$D^{d-i-1}:\mathcal H_q^{\rm tail}\to
\mathcal H_{q-d+i+1}^{\rm tail}$ 是固定有限阶的满射，有相容
$R_{d-i-1}$ 作有界右逆，所以其伴随像闭。

## 6. 具体的完整对偶能量

令 $S_{\rm flag}=S_0|_{\mathscr C_{\rm flag}}$。因为
$\ker S_{\rm flag}=\mathscr K_{\rm flag}$，对 $y\in\mathcal R_{m,q}$，有
$$
 \boxed{
 \begin{aligned}
 \langle G_{\rm flag}y,y\rangle
 &=\|P_{\mathscr K_{\rm flag}}D_0^*y\|^2\\
 &=\inf_z
 \bigl\|P_{\mathscr C_{\rm flag}}
       (D_0^*y-S_0^*z)\bigr\|^2.
 \end{aligned}
 }
 \tag{6.1}
$$
$z$ 遍历旧链的完整输出 Hilbert 空间；仍只用 inf，不假定
$\operatorname{Ran}S_{\rm flag}^*$ 闭。投影
$P_{\mathscr C_{\rm flag}}$ 按 (3.2) 在原头坐标逐一投到
$E_{d-i,q+t}$，其余头坐标置零。于是 (6.1) 中所有被压缩的纯尾创建项都落在明确的有限阶删除核之间；这是一个真实正交压缩，不能再用环境 $\|D^*y\|$ 代替。

对原实际 $w\in M$ 的低输出投影 $v_{m,q}(w)$，它的残量自动属于
$\mathcal R_{m,q}$，所以 (4.2)、(6.1) 正是原 $\lambda_q(w)$ 的公式。

本稿还没有给 (6.1) 足够强的统一下界。相容 $R_t$ 的旧有限阶估计可以验证固定 $q$ 的严格正性，但不能据此删除全部伴随链抵消或终端项。真正原核的全局条件是否进一步控制这个准确旗 Gram，仍是下一待证问题；无权 $N=M$ 和普通 ISP 均未完成。
