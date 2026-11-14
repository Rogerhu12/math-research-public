# R271 附录：真实低旗上的完整头换序与加权有效源

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_resume_1cf；AI 辅助：GPT-6 Astra Pro。
状态：已证明。根完整核验高度块、上下端旗余量、受限伴随及 Schur 合同度量。

本稿在实际联合旗上证明完整头 $A_m$ 可以保留的换序式。归一化后，换序缺陷只剩 primitive 列；对实际中间源，它进一步只在第2段出现。最终 Schur 能量同步作准确合同变换，未交换中间逆。

## 1. 尾部正交高度块

沿用[出生层两带结构](../notes/2026-11-13-low-kernel-birth-layer-double-schur-bridge-1cf.md)的实际纯尾
$$
D=\sum_{j\ge m}b_jE_j,\quad C=D_3=\sum_{j\ge m}b_j^3E_j,\quad
W_2=\sum_{j\ge m}b_j^2n_j,\quad S_m=\sum_{j\ge m}b_j^2,
\quad b_j=(j+1)^{-2}.
$$
在每个孔层上置
$$
E_{h,p}=\ker D^h\cap\mathcal H_p,\qquad
U_{h,p}=E_{h,p}\ominus E_{h-1,p}.
$$
第一、第二下降仍记为 $D^{(0)},D^{(1)}$。定义占据算子的升、降一高度块和 $C$ 的保高度块：
$$
W_+=\bigoplus_{p,h}P_{U_{h+1,p}}W_2|_{U_{h,p}},
\qquad W_-=W_+^*,
$$
$$
C_0=\bigoplus_{p,h}P_{U_{h,p-1}}C|_{U_{h,p}}.
\tag{1.1}
$$
不同输入块及其输出块各自正交，因此这些都是全尾有界算子。特别，
$$
\|W_+\|=\|W_-\|\le S_m/2,\qquad
\|C_0\|\le s_{3,m}:=\sum_{j\ge m}b_j^3.
\tag{1.2}
$$
第一界来自 $0\le W_2\le S_mI$：任意两个正交高度间的块，在减去 $(S_m/2)I$ 后不变。

由 $[D,W_2]=C$、$[D,C]=0$，$W_2E_h\subset E_{h+1}$。
又因 $W_2$ 自伴，其高度带宽为1。$C$ 保持每个 $E_h$，所以它不增加高度。

抽取 $[D,D^*]=S_mI-2W_2$ 中增加高度一的部分，得到
$$
\boxed{[D^{(0)},D^{(1)*}]=-2W_+.}
\tag{1.3}
$$
抽取 $[D,W_2]=C$ 的保高度部分，以及 $[D,C]=0$ 中下降高度一的部分，分别得到
$$
\boxed{[D^{(0)},W_+]=C_0,\qquad [D^{(0)},C_0]=0.}
\tag{1.4}
$$
这些是固定孔层之间的有界块恒等式，继而在全直和上成立。

## 2. 实际联合旗与嵌入算子

固定原合法 $m,q$，$d=2^m$，使用
$$
C_t=\bigoplus_{i=0}^{d-t}e_iE_{d-i,q+t},\qquad
Y_t=\bigoplus_{i=0}^{d-t-1}e_iE_{d-i-1,q+t},
$$
$$
\mathscr C=\bigoplus_{t=1}^dC_t,\qquad
\mathscr Y=\bigoplus_{t=1}^{d-1}Y_t\subset\mathscr C.
$$
末段 $Y_d$ 按零空间理解。定义
$$
(S^{(0)}c)_t=A_mc_t+D^{(0)}c_{t+1},\qquad
(S^{(1)}c)_t=D^{(1)}c_{t+1}.
$$
两者都把 $\mathscr C$ 送入 $\mathscr Y$。经自然包含
$\iota:\mathscr Y\hookrightarrow\mathscr C$，记
$$
\mathbf S_0=\iota S^{(0)},\qquad
\mathbf S_1=\iota S^{(1)}.
$$
故 $\mathbf S_1^*=S^{(1)*}P_{\mathscr Y}$。下面在 $\mathscr Y$ 上写 $\mathbf S_1^*$ 时，正是原真实带旗伴随。

相对出生层为 $a=t-h+1$。记 $\mathscr Y_{\ge a}$ 为 $\mathscr Y$ 中相对出生层至少为 $a$ 的部分；特别
$$
\mathscr Y_2:=\mathscr Y_{\ge2}
=\bigoplus_{t=1}^{d-1}\bigoplus_{i=0}^{d-t-1}
e_iE_{\min(d-i-1,t-1),q+t}.
\tag{2.1}
$$
这是实际低核通量的空间。

在 $\mathscr C$ 上逐段作用 $W_+$；对 $\mathscr Y_2$ 输入，它无需额外旗截断。另定义降一链段的保高度算子
$$
(\mathbf C_0^-z)_t=C_0z_{t+1}.
\tag{2.2}
$$
头因子均保持不变。

## 3. 低旗上的完整头换序没有漏掉边界项

**命题 3.1。** 对每个 $z\in\mathscr Y_2$，
$$
\boxed{
\mathbf S_0\mathbf S_1^*z-\mathbf S_1^*\mathbf S_0z=-2W_+z.
}
\tag{3.1}
$$
而且在同一输入空间上，
$$
\boxed{
[\mathbf S_0,W_+]z=\mathbf C_0^-z,\qquad
[\mathbf S_0,\mathbf C_0^-]z=0.
}
\tag{3.2}
$$

### 真实旗检查

第 $t$ 段的输入满足
$$
i\le d-t-1,\qquad h\le t-1.
$$
原 $D^{(1)*}$ 送到第 $t+1$ 段、高度 $h+2\le t+1$，而
$d-i\ge t+1$。所以其整个输出在 $C_{t+1}$；它没有先出旗再被头 $A_m$ 带回的漏项。

$\mathbf S_0$ 保持 $\mathscr Y_2$：头 $A_m$ 只降低头指标，$D^{(0)}$ 同时降低一段和一高度。最早非零段的 primitive 输入被 $D^{(0)}$ 杀掉，故没有下端漏项。

$W_+z$ 的高度至多 $t$，仍小于等于 $d-i-1$，故属于
$\mathscr Y_{\ge1}$。$\mathbf C_0^-z$ 也在 $\mathscr Y_{\ge1}$。
$\mathbf S_0$ 同样保持这个较大的空间。

因此 (3.1) 可以在未截断矩阵中计算后直接放回实际旗。头 $A_m$ 与所有纯尾块交换；两个相反的段位移抵消，剩下 (1.3)。
同理，(3.2) 分别由 (1.4) 得到。全部中间项都在上述已检查的空间中。证毕。

归纳即给对 $n\ge2$ 的完整式
$$
\boxed{
\begin{aligned}
\mathbf S_0^n\mathbf S_1^*z
={}&\mathbf S_1^*\mathbf S_0^nz
-2nW_+\mathbf S_0^{n-1}z\\
&-n(n-1)\mathbf C_0^-\mathbf S_0^{n-2}z .
\end{aligned}
}
\tag{3.3}
$$
因此原范数中的余项满足
$$
\|\mathbf S_0^n\mathbf S_1^*z-\mathbf S_1^*\mathbf S_0^nz\|
\le nS_m\|\mathbf S_0^{n-1}z\|
+n(n-1)s_{3,m}\|\mathbf S_0^{n-2}z\|.
\tag{3.4}
$$
这保留了真实输入范数，并不把 $\|z\|$ 自动换成最小修复能量。

## 4. 归一化后只剩 primitive 列

令高度乘子 $\Phi$ 在每个 $U_{h,p}$ 上取
$$
\Phi|_{U_{h,p}}=\frac1{h(h+1)}I,\qquad h\ge1.
\tag{4.1}
$$
它保留全部联合旗，$\|\Phi\|\le1/2$。置
$$
\mathbf J=\mathbf S_1^*\Phi.
\tag{4.2}
$$

[占据交换子与最小能量稿](R271-appendix-occupation-commutator-known-source-minimum-energy.md) 的全高度消逆式给，在 $U_{h,p}$ 上，
$$
D^{(0)}D^{(1)*}=-(h+1)W_+.
$$
结合 (1.3)，还得
$$
D^{(1)*}D^{(0)}=-(h-1)W_+,
\tag{4.3}
$$
其中 $h=1$ 时右侧与左侧都为零。

若 $h\ge2$，用 (4.1)--(4.3) 直接计算：
$$
D^{(0)}D^{(1)*}\Phi=-\frac1hW_+,\qquad
D^{(1)*}\Phi D^{(0)}=-\frac1hW_+.
$$
$h=1$ 时第一式为 $-W_+$，第二式为零。因此，若 $P_K$ 逐段表示 primitive 高度1的正交投影，
$$
\boxed{
[\mathbf S_0,\mathbf J]z=-W_+P_Kz,\qquad z\in\mathscr Y_2.
}
\tag{4.4}
$$
头项仍然完全保留：$A_m$ 不改变高度，与 $\Phi$ 及纯尾块交换；
(3.1) 的同一实际旗余量保证 (4.4) 没有增加边界项。

式 (4.4) 比未归一化式更精确地定位了换序缺陷。它没有说
$\mathbf J$ 在整个 $\mathscr C$ 上与 $\mathbf S_0$ 交换。

## 5. 真实有效源的加权换序式

采用 [真实中间源和头角消元](R271-appendix-actual-middle-source-corner-elimination-and-positive-gram.md) 的准确记号：
$\mathscr Y_1$ 是相对出生层恰为1的部分，
$$
x=Q_1^{-1}\zeta,\qquad
\sigma=V_2x,\qquad
V_2=S^{(1)}S^{(0)*}|_{\mathscr Y_1}.
$$
这里 $x$ 不是完整对偶的 $z_1$。

将 (4.4) 作为从 $\mathscr Y_2$ 到 $\mathscr C$ 的有界算子恒等式取伴随，得到
$$
P_{\mathscr Y_2}
(\mathbf J^*\mathbf S_0^*-\mathbf S_0^*\mathbf J^*)
=-P_{\mathscr Y_2}P_KW_-.
\tag{5.1}
$$
对 $x\in\mathscr Y_1$，有
$\mathbf J^*x=\Phi\mathbf S_1x\in\mathscr Y_2$，并且
$$
P_{\mathscr Y_2}\mathbf J^*\mathbf S_0^*x
=\Phi V_2x.
$$
因此定义
$$
\mathcal B_2=
P_{\mathscr Y_2}P_KW_-|_{\mathscr Y_1},
$$
就有准确式
$$
\boxed{
\Phi\sigma
=P_{\mathscr Y_2}\mathbf S_0^*\mathbf J^*x-\mathcal B_2x,
\qquad x=Q_1^{-1}\zeta.
}
\tag{5.2}
$$

$\mathscr Y_1$ 在第 $t$ 段的高度恰为 $t$，而 $W_-$ 只降低一高度。
故 $P_KW_-$ 只可能读取 $t=2$：
$$
\boxed{
(\mathcal B_2x)_t=0\ (t\ne2),\qquad
(\mathcal B_2x)_2=P_{U_{1,q+2}}W_-(x_2),\qquad
\|\mathcal B_2\|\le S_m/2.
}
\tag{5.3}
$$
第二式逐头作用；第2段仍保留原允许头指标 $i\le d-3$。

由于 $\mathbf S_0$ 保持 $\mathscr Y_2$，其限制
$S_{0,2}=\mathbf S_0|_{\mathscr Y_2}$ 的真实伴随是
$S_{0,2}^*=P_{\mathscr Y_2}\mathbf S_0^*|_{\mathscr Y_2}$。
于是 (5.2) 也可写成
$$
\boxed{
\Phi\sigma=S_{0,2}^*u-\mathcal B_2x,\qquad
u=\mathbf J^*x\in\mathscr Y_2.
}
\tag{5.4}
$$
这是一个伴随像加第2段 primitive 项；不能把第一个算子换成
$S_{0,2}$，也不能删去 $u$ 的实际成本。

## 6. Schur 度量同步合同，真实测试保持不变

在 $\mathscr Y_2$ 上，非零高度满足 $1\le h\le d-2$，
故 $\Phi$ 为正的有界可逆算子。定义
$$
\widetilde{\mathcal H}_2=\Phi\mathcal H_2\Phi,\qquad
\widetilde\sigma=\Phi\sigma.
$$
则原末块能量准确为
$$
\boxed{
\mathcal E_2
=\langle\mathcal H_2^{-1}\sigma,\sigma\rangle
=\langle\widetilde{\mathcal H}_2^{-1}
\widetilde\sigma,\widetilde\sigma\rangle.
}
\tag{6.1}
$$
这里使用合同变换，不假定 $\Phi$ 与 $\mathcal H_2$ 交换。

若 $F\in\mathscr Y_2$ 是原真实未来向量给出的通量源，旧式
$Su=-F$ 已支付
$\langle\mathcal H_2^{-1}F,F\rangle\le\beta_+^2$。
令 $\widetilde F=\Phi F$，则
$$
\langle\widetilde{\mathcal H}_2^{-1}
\widetilde F,\widetilde F\rangle\le\beta_+^2,
\qquad
\langle F,\mathcal H_2^{-1}\sigma\rangle
=\langle\widetilde F,
\widetilde{\mathcal H}_2^{-1}\widetilde\sigma\rangle.
\tag{6.2}
$$
所以 (5.2) 接入的是同一个实际源、实际测试和实际正能量，没有额外的度量替换误差。

本文没有移动 $Q_1^{-1}$。剩余问题是用
$x=Q_1^{-1}\zeta$ 的真实角约束，控制 (5.4) 的
$S_{0,2}^*u$ 与第2段 primitive 项在 (6.1) 中的合成能量。
仅凭 $\|\mathcal B_2\|\le S_m/2$ 或 $\|\mathbf J\|\le\|D^{(1)}\|/2$，
不能删除未知的 $x$，也不能推出无权 $N=M$。
