# R481 — 原三高轴的完整第三精度规范形与同一修正的 d2

日期：2026-11-14。**状态：已证明。** 本篇在相同有限来源内给出整个 $p^3$ 原评价的显示规范形。$\ell=1,2$ 的真实缺失行单独保留，随后的一次、二次 $p$ 修正均由原三个普通 Euler 值及完整 $s$ 阶移位计算。全部 $t$ 到 $w$ 高尾保留。

在真实立方首核上，一次修正缩为三组准确短尾。特别，R475 中对原首 Bockstein 不可见的高轴，在相对首 Bockstein、进而原第二障碍的 carry 投影中仍可出现。这里支付其确切单位系数与低 $\ell$ 符号；没有把环境尾秩当成真实余核秩。再给同一个实际来源修正 $R$ 的首提升方程、完整第二障碍代表及其到 $G_2$ 的准确投影。

## 1. 原评价与有限系数算子

保留 $p=6s-1>83$、$1\le\ell<s-13$、$L=2s+\ell$ 及原有限来源 $\mathcal W$。所有来源列、返回成本及预算均不改变。对相对 Euler 算子 $\mathcal E$，记同一参考 regularized 轴上的三个完整普通值为
$$
P_i(w)=(\mathcal E^iP)_{\rm reg,\circ}(w),\qquad i=0,1,2.
$$
原 Gaussian 常数 $a=p\kappa$ 是单位。记 $\pi_n$ 为取普通 $w$ 次数 $0,\ldots,n-1$ 后补零的算子，$\mathscr S$ 为准确的 $s$ 阶移位：
$$
\mathscr S\Bigl(\sum c_iw^i\Bigr)=\sum_{i\ge0}c_{s+i}w^i.
$$
这不是自由尾项，也不是在来源中除 $w^s$。

相对三个块准确为
$$
\boxed{J_\circ(P)=\left(
\pi_sP_0,\quad
\pi_s(aP_1+p\mathscr SP_0),\quad
\pi_\ell\left(\frac{a^2}{2}P_2+pa\mathscr SP_1+p^2\mathscr S^2P_0\right)
\right).}
\tag{1}
$$
所有公式均在原整系数上读到 $p^3$，不是只对约化后的形式模型。

高轴按 R468 保留整个
$$
\lambda_z(w)=w^{s-3}(u+vw+xw^2)+w^sH_z(w),\qquad
g_z=g_\circ e^{\lambda_z}.
\tag{2}
$$
令
$$
A_z(V)=\pi_s(\lambda_z V).
\tag{3}
$$
它只读取 $V$ 的前三项并输出最后三条 $s$ 块行；所有正次数高尾 $H_z$ 自动不进入 (3)。但下文的移位乘法仍保留整个 $\lambda_z$，不能据此删去 $H_z$。

## 2. 完整整目标变换及低 ell 的真实缺失行

在三个实际块上定义
$$
\boxed{T_z(C_0,C_1,C_2)=
\left(C_0+a^{-1}A_zC_1,\quad
C_1+2a^{-1}A_zC_2,\quad C_2\right).}
\tag{4}
$$
$C_2$ 只有原有的 $\ell$ 条行，按原长度补零。因 $\operatorname{ord}\lambda_z\ge s-3$、$s\ge15$，$A_z^2=0$，所以 $T_z$ 是整单位，逆矩阵把 (4) 中两个加号改为减号。

记 $\pi_{[\ell,3)}=\pi_3-\pi_{\min(\ell,3)}$。真实缺失行是
$$
\boxed{N_z(P)=\left(0,\ aA_z(\pi_{[\ell,3)}P_2),\ 0\right).}
\tag{5}
$$
它在 $\ell\ge3$ 时为零；$\ell=2$ 时是一行、$\ell=1$ 时是 R468 的两行原 Schur 项。特别，它没有用不存在的第三块行来消元。
由于 $N_z$ 的第二分量只在该块最高两行，$T_z^{-1}N_z=N_z$。

## 3. 整个 p³ 的两个显示修正

定义两个实际整线性算子 $\mathfrak A_z,\mathfrak B_z:\mathcal W\to\Gamma_L$，其三个块为
$$
\boxed{
\begin{aligned}
\mathfrak A_z^0(P)&=-a^{-1}A_z(\mathscr SP_0),\\
\mathfrak A_z^1(P)&=\pi_s\mathscr S(\lambda_zP_1)
-2A_z(\pi_\ell\mathscr SP_1)
+\frac12\pi_s\mathscr S(\lambda_z^2P_2),\\
\mathfrak A_z^2(P)&=a\pi_\ell\mathscr S(\lambda_zP_2),
\end{aligned}}
\tag{6}
$$
$$
\boxed{
\begin{aligned}
\mathfrak B_z^0(P)&=0,\\
\mathfrak B_z^1(P)&=-2a^{-1}A_z(\pi_\ell\mathscr S^2P_0),\\
\mathfrak B_z^2(P)&=\pi_\ell\mathscr S^2(\lambda_zP_1)
+\frac12\pi_\ell\mathscr S^2(\lambda_z^2P_2).
\end{aligned}}
\tag{7}
$$
这里所有乘法首先是原完整普通系数乘法，再作显示移位和截断。负角幂或不在预算内的新列都没有出现。

**定理 1。** 对整个同一来源，而不只对首核，准确有
$$
\boxed{J_z-T_zJ_\circ
=N_z+p\mathfrak A_z+p^2\mathfrak B_z\pmod{p^3}.}
\tag{8}
$$
令
$$
K_z=J_\circ+N_z,\qquad
\mathcal A_z=T_z^{-1}\mathfrak A_z,\qquad
\mathcal B_z=T_z^{-1}\mathfrak B_z,
$$
则等价的完整规范形是
$$
\boxed{\widehat J_z:=T_z^{-1}J_z
=K_z+p\mathcal A_z+p^2\mathcal B_z\pmod{p^3}.}
\tag{9}
$$
$K_z$ 是显示的实际有限矩阵及其原 rank 至多二的缺失行修正，不是新增来源。

**证明。** 在整个原 $\Gamma_L$ 中，$\epsilon^2\lambda_z$、$\epsilon\lambda_z^2$、$\lambda_z^3$ 都为零：其最终第三块最低指数分别为 $s-3,s-6,s-9$，均严格超过 $\ell-1$。所以全部 Gaussian 与高轴 Taylor 展开准确缩为
$$
J_z(P)=P_0+(a\epsilon+\lambda_z)P_1
+\frac12(a\epsilon+\lambda_z)^2P_2.
\tag{10}
$$
这里已经包括整个来源的 Euler 展开；没有删除某个尚可读的 $P_3$ 项。

把 (10) 按 $w^s=p\epsilon$ 分为三个块，得到
$$
\begin{aligned}
C_{0,z}-C_{0,\circ}&=\pi_s(\lambda_zP_1),\\
C_{1,z}-C_{1,\circ}&=
a\pi_s(\lambda_zP_2)
+p\pi_s\mathscr S(\lambda_zP_1)
+\frac p2\pi_s\mathscr S(\lambda_z^2P_2),\\
C_{2,z}-C_{2,\circ}&=
pa\pi_\ell\mathscr S(\lambda_zP_2)
+p^2\pi_\ell\mathscr S^2(\lambda_zP_1)
+\frac{p^2}{2}\pi_\ell\mathscr S^2(\lambda_z^2P_2).
\end{aligned}
\tag{11}
$$
将 (1) 代入 (4)。第零块的已有 $aP_1$ 消去后留下 $-p a^{-1}A_z\mathscr SP_0$。
第一块中 $aA_zP_2$ 只消去 $\pi_\ell P_2$ 的部分，余下正是 (5)；同一已有第三块还产生 (6) 中的 $-2$ 和 (7) 中的 $-2/a$。第三块不作变换，直接给 (6)–(7)。这证明 (8)，再用 $T_z^{-1}N_z=N_z$ 得 (9)。$\square$

特别，$H_z$ 通过 $\mathscr S(\lambda_zV)$ 和 $\mathscr S^2(\lambda_z^2V)$ 真正进入完整下一位；只有完成上面的目标运算后，才能判断某个特定核向量上的项是否消失。

## 4. 保原 M、两条十三行及总 charge 四十

$T_z$ 只把行加到前两块的最后三条行。因此它保持 R479 的完整
$$
\mathscr B_{26}=w^{s-13}k[w]_{<13}\oplus
\epsilon w^{s-13}k[w]_{<13},
$$
且在除去这两条 carry 的商上为恒等。
在整对角表示 $m_{13}\simeq\operatorname{diag}(1,p)$ 中，$T_z$ 没有把 carry 方向送到单位方向。因此
$$
m_{13}T_z=V_zm_{13}
$$
有一个整可逆目标矩阵 $V_z$；原最初十三条自由行上以恒等延拓。

恢复 $c_*U_{0,z}$ 时继续使用其整个整单位，包括 $P_{134}$ 与总 charge 四十。故原 $M_z$ 整等价于 $m_{13}\widehat J_z$，而 R449 的
$$
K_2^{\rm red}(M_z)=\ker(\pi\beta_{\widehat J_z}),\qquad
G_{2,z}=C_2(\widehat J_z)/\overline H_z
\tag{12}
$$
保持原义。这里的 $\overline H_z$ 是真实 carry 像，勿与 (2) 的换参级数 $H_z(w)$ 混同。没有将目标单位运输误作来源饱和，也没有减去原二十六个 carry 因子。

## 5. 真立方首核的一次缺陷全部缩为短尾

取 R459/R475 的真实
$$
\bar P=t^rF^3Q,\qquad
h_F=\operatorname{ord}F(g_\circ),\qquad
k=2h_F+r-s\ge0,
$$
$$
k<\min(s-h_F,\ell,h_F),\qquad
\delta=r+h_F-\ell\ge0.
\tag{13}
$$
记 $C_F,u_F,e_F$ 为 R475 的实际三个首值，则
$$
\mathscr SP_0=C_Fu_F^3w^{h_F+k}+\cdots,\quad
\mathscr SP_1=3C_Fu_F^2e_Fw^k+\cdots,
$$
$$
P_2=6C_Fu_Fe_F^2w^{\ell+\delta}+\cdots.
\tag{14}
$$
由 $r+2h_F\ge s,r\ge1$，有 $r+h_F\ge\lceil(s+1)/2\rceil\ge8$。
因此 $\overline{N_z(P)}=0$，同一个 $P$ 同时在 $\ker\bar K_z$ 中。

**定理 2。** 在这个真实首核上，(9) 的一次缺陷准确为
$$
\boxed{
\overline{\mathcal A_z(P)}=
\left(
-a^{-1}A_z\mathscr SP_0,\quad
A_z\bigl((1-2\pi_\ell)\mathscr SP_1\bigr),\quad
a\pi_\ell\mathscr S(\lambda_zP_2)
\right)\pmod p.}
\tag{15}
$$
式中低 $\ell$ 的符号 $1-2\pi_\ell$ 必须保留。

**证明。** $P_1$ 模 $p$ 从 $w^s$ 起，所以
$\pi_s\mathscr S(\lambda_zP_1)=A_z\mathscr SP_1$。
二次项 $\mathscr S(\lambda_z^2P_2)$ 的最低阶至少是
$s-6+r+h_F\ge s+2$，不进入第一块长度 $s$。
这给 (6) 的显示约化。

第一、第二分量只在各自最高三行。第三分量若非零，必须 $\delta\le2$，从而 $\ell\ge r+h_F-2\ge6$；它也只在第三块最高三行，最低局部指数至少三。因此对这些向量再施 $T_z^{-1}$ 没有变化。得到 (15)。$\square$

三组尾的可能长度依次为
$$
\max(0,3-h_F-k),\qquad
\max(0,3-k),\qquad
\max(0,3-\delta).
\tag{16}
$$
它们的首单位系数由 (14) 给出。
在 $h_F+k\ge3$、$\delta\ge3$ 的深窗，只有第二组存在。
若 $k=0,1,2$，三个高轴到这一环境尾的秩准确为三、二、一；主三角块的对角是
$$
\boxed{-3C_Fu_F^2e_F\in k^\times.}
\tag{17}
$$
因为 $k<\ell$，首项的符号始终为负；其后的系数在 $\ell=1,2$ 处按 (15) 改号。
当 $k\ge3$，这组也为零。

特别，$\ell=1$ 的 $N_z$ 首位只含 $u,v$，而当 $k=0$ 时，$x$ 在 $p\mathcal A_z$ 中已有真实单位尾系数。这是下一位的实际来源关系，不是增加第三个自由 Gaussian 变量。

在 $\ell\ge3$ 时 $K_z=J_\circ$，所以 (15) 直接给共同首余核中的
$\beta_{\widehat J_z}(P)-\beta_{J_\circ}(P)$。
在 $\ell=1,2$ 时必须使用同一个 $\bar K_z$ 的首余核，不能沿用一个已经改变的 $\bar J_\circ$ 左核。
上述秩只属于显示环境尾；投到真正 $C_1(\bar K_z)$ 后可以下降。
由 R449，真实相对首 Bockstein 又是原 $d_2(M_z)$ 的 carry 投影。故 R475 的原首 Bockstein 不变，不使 (15) 的下一层真实尾自动消失。

## 6. 同一个 R 的首提升与真正第二障碍代表

取任一实际来源提升 $P^{\rm base}$，其约化是 (13) 的 $P$。因为 $\bar K_zP=0$，
$$
\mu_z=K_zP^{\rm base}/p
$$
在整个目标中整。
由 (9)，存在同格的相对 $p^2$ 提升
$P^{(2)}=P^{\rm base}+pR_z$，当且仅当实际来源 $R_z$ 解
$$
\boxed{\bar K_z\bar R_z
=-\overline{\mu_z+\mathcal A_zP^{\rm base}}.}
\tag{18}
$$
这是同一个原有限矩阵的完整方程，不只读 (15) 中的环境尾。
如果因子提升的 $R^{\rm base}$ 非零，R459 的正规分支条件须用
$R^{\rm base}+\bar R_z$；不能另挑一个满足 normal jet 的修正。

解 (18) 后，以下商整：
$$
\boxed{
\Xi_z(P,R_z)=
\overline{\frac{\mu_z+K_zR_z+\mathcal A_zP^{\rm base}}p
+\mathcal A_zR_z+\mathcal B_zP^{\rm base}}.}
\tag{19}
$$
它在 $C_2(\widehat J_z)$ 中的类就是同一真实 $d_2^{\widehat J_z}(P)$。

**证明。** 在 (9) 中代入同一个 $P^{\rm base}+pR_z$：
$$
\widehat J_z(P^{\rm base}+pR_z)
=p(\mu_z+K_zR_z+\mathcal A_zP^{\rm base})
+p^2(\mathcal A_zR_z+\mathcal B_zP^{\rm base})\pmod{p^3}.
$$
(18) 使第一括号被 $p$ 整除，除以 $p^2$ 即得 (19)。
如果换同一首次提升，差 $Q$ 满足 $\bar K_zQ=0$，(19) 的变化为
$K_zQ/p+\mathcal A_zQ$；这正是 $\widehat J_z$ 的首 Bockstein 像，在真实 $C_2$ 中被商掉。$\square$

因此，保原十三行与 R449 的准确运输后，真正的原第三核条件是
$$
\boxed{
\text{先在同一来源解 (18)，再有 }
[\Xi_z(P,R_z)]=0\quad\text{于 }G_{2,z}.
}
\tag{20}
$$
这没有把一个非零显示向量冒称非零余核类。
实际三个完整中央失败时，只能代入 R468 的实际 $z_*$ 和整个 $H_{z_*}$；(18)–(20) 仍必须由原格证明，不能由三个 Hensel 方程自动赋给 $R_z$。

## 7. 一个实际来源的完整 p³ 与同一修正证书

[check-r481-full-third-precision-normal-form.py](../scripts/check-r481-full-third-precision-normal-form.py)
复用 R475 的一个真实 $p=239,D=40$ canonical 立方来源。
对其四个已经支付的电荷分量 $37,38,39,40$，在
$\ell=1,2,3,22,23,24,25$ 上直接核整个 $p^3$ 恒等式 (9)，包括低 $\ell$ 的 $N_z$ 和全部原 $t$ 高尾。
共二十八个完整身份均成立；没有扫描目标素数。

再在 $\ell=25$ 用原 $\mathcal W_{12}\subset\mathcal W_{40}$ 求解同一个 (18)，其真实 $105\times369$ 约化矩阵满行秩。得到的一个修正有 $103$ 个非零 canonical 系数，同时满足
$$
[w^{15}](\mathcal ER_z)|_\psi=194,\qquad
[w^{30}]R_z|_\psi=123\quad(\bmod239),
$$
且各自低于这两阶的系数均为零。这次是相对 $J_z$ 层提升，故单位 $5$ 与单位 $-2$ 两式由**同一个 $R_z$** 实现；与 R479 保非零 $B_0$ 的另一修正严格区分。

脚本随后用这个相同 $R_z$ 核 (19) 与整个 $p^3$ 实际评价除 $p^2$ 后逐项一致。该样本首矩阵满行秩，故不把其商前非零向量称为非零 $C_2$ 或 $G_2$。本篇的全参数内容是 (8)–(20) 的原矩阵规范形、短尾兼容性和同格第二障碍公式；跨素数的真实余核限制及主目标仍待证明。
