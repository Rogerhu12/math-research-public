# 工作笔记：真实头通量的相邻源层平移与末段已付源

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_resume_1cf。
状态：以下为同一实际联合旗中已核的完整坐标恒等式，保存为工作接口；不登记独立无权能量定理。

本笔记继续[完整链及真 Schur](../results/R271-appendix-complete-repair-chain-lowering-defects-and-true-schur-contraction.md)、[真实返回源](2026-11-13-actual-last-block-return-source-and-complete-low-chain-projection-1cf.md)和[首段边界先消元](../results/R239-appendix-boundary-first-elimination-small-sources-and-exact-return-energy.md)。它直接保留真实 $h_t=P_{\mathcal E_{q+t}}H_t^*z_t$ 的头位置，不用整个末块能量替代这些坐标。

## 1. 同头的有限个源层

固定原 $m\ge5,d=2^m,A=A_m,D=D_m$，取
$$
4d\le q,\qquad q+d-1\le e^{d^3/4}.
\tag{1.1}
$$
此较窄条件只为让以下 $q+k$ 全部直接使用同一个已付原窗口；不在移动源层时改变 $m$。

对任意 $j\in[q,q+d-1]$，沿用
$$
\mathscr C_{j,u}
=\bigoplus_{i=0}^{d-u}e_iE_{d-i,j+u},\qquad
\mathscr Y_{j,u}
=\bigoplus_{i=0}^{d-u-1}e_iE_{d-i-1,j+u},
$$
$$
\mathscr R_j
=\bigoplus_{i=0}^{d-2}e_iE_{d-i-1,j},\qquad
E_{h,p}=\ker D^h\cap\mathcal H_p.
$$
记
$$
S_jc=(Ac_u+Dc_{u+1})_{u=1}^{d-1},\qquad
\mathcal G_j=S_jS_j^*,
$$
并用 $\mathsf D_jc=Dc_1$ 表示整个联合输入上的首输出，
$\mathsf F_j=\mathsf D_j|_{\ker S_j}$，$G_j=\mathsf F_j\mathsf F_j^*$。
这些固定参数 Gram 都严格正。所有伴随均保原联合旗。

给定 $r\in\mathscr R_q$，写原最小链为
$$
y=G_q^{-1}r,\quad b=\mathsf D_q^*y,\quad
z=\mathcal G_q^{-1}S_qb,\quad
c=b-S_q^*z,\quad \lambda=\|c\|.
\tag{1.2}
$$
以下 $z_t$ 是完整对偶段，不能改成某一个出生块或某个中间逆的部分。

## 2. 真头通量及新增的头坐标

令
$$
\mathcal E_p=\bigoplus_{i=0}^{d-1}e_iE_{d-i,p},\qquad
h_t=P_{\mathcal E_{q+t}}H_t^*z_t\quad(1\le t<d),
\qquad h_d=0.
\tag{2.1}
$$
原
$$
H_t=P_{W_{d-t}}A(I-P_{W_{d-t+1}})
$$
给准确支持
$$
(h_t)_i=0\quad(i<d-t+1),\qquad
(h_t)_i\in E_{d-i,q+t}.
\tag{2.2}
$$
因此 $h_1=0$，并且 (2.1) 只读取 $z_t$ 中的
$E_{t-1,q+t}$；这仍是原真实窄通量，不是新的任意输出。

固定 $1\le k\le d-1$。旧第 $t=k+u$ 段与源 $q+k$ 的新第 $u$ 段有同一个孔数 $q+t$。新输入比旧输入恰好多出 $k$ 个头坐标：
$$
\mathscr C_{q+k,u}\ominus\mathscr C_{q,t}
=
\bigoplus_{i=d-t+1}^{d-t+k}e_iE_{d-i,q+t}.
\tag{2.3}
$$
这里只在 $t=k+u\le d$ 时比较；每个共有头坐标的尾核旗完全相同。

令
$$
(J_kc)_u=
\begin{cases}
c_{k+u},&1\le u\le d-k,\\
0,&u>d-k,
\end{cases}
$$
$$
(Z_kz)_u=
\begin{cases}
z_{k+u},&1\le u\le d-1-k,\\
0,&u>d-1-k,
\end{cases}
$$
分别作为新输入、新内部输出中的向量。定义只收新增头位的向量
$$
(h^{(k)})_u
=
\sum_{i=d-(k+u)+1}^{d-u}
e_i(h_{k+u})_i
\quad(1\le u\le d-k),
\tag{2.4}
$$
其余段为零。$h_d=0$ 使 (2.4) 的末段自动为零。

由 (2.3)，$J_kc$ 与 $h^{(k)}$ 在每一段的头支持不交，故
$$
\langle J_kc,h^{(k)}\rangle=0,\qquad
\|J_kc\|^2=\sum_{t=k+1}^d\|c_t\|^2.
\tag{2.5}
$$

## 3. 包含首段源的完整平移式

原 $z_k$ 满足头指标 $i\le d-k-1$ 和尾核阶 $d-i-1$，所以
$$
z_k\in\mathscr R_{q+k}.
\tag{3.1}
$$
下面的源是这个完整 $z_k$；不把它当成相邻原见证的最优对偶。

准确有
$$
\boxed{
\mathsf D_{q+k}^*z_k+S_{q+k}^*Z_kz
=h^{(k)}-J_kc.
}
\tag{3.2}
$$

证明：旧 $t\ge2$ 的极小链满足
$$
c_t=-P_{\mathscr C_{q,t}}
\bigl(A^*z_t+D^*z_{t-1}\bigr),
\qquad z_d=0.
\tag{3.3}
$$
因为 $z_{t-1}$ 的头指标至多为 $d-t$，$D^*z_{t-1}$ 的全部头坐标已经位于旧 $\mathscr C_{q,t}$ 的头范围内。新旧投影在这些头坐标上采用完全相同的 $E_{d-i,q+t}$；所以新增部分只来自 $A^*z_t$，且正好为 (2.4)。

新第1段缺少 $D^*z_k$，由 $\mathsf D_{q+k}^*z_k$ 补上；其余各段由 $S_{q+k}^*Z_kz$ 给出 (3.3) 中的同一个和。末段使用 $z_d=0$。这证明 (3.2)，没有移掉任何尾旗投影。

## 4. 新源的真正最小链和准确 Pythagoras

定义
$$
r^{(k)}=G_{q+k}z_k,\qquad
c^{(k)}=\mathsf F_{q+k}^*z_k,\qquad
\lambda_k'=\|c^{(k)}\|
=\lambda_{q+k}(r^{(k)}),
$$
$$
z_{\rm opt}^{(k)}
=\mathcal G_{q+k}^{-1}S_{q+k}\mathsf D_{q+k}^*z_k.
\tag{4.1}
$$
于是
$$
\mathsf D_{q+k}^*z_k
=c^{(k)}+S_{q+k}^*z_{\rm opt}^{(k)}.
$$
代入 (3.2)：
$$
\boxed{
h^{(k)}-J_kc
=c^{(k)}+
S_{q+k}^*\bigl(z_{\rm opt}^{(k)}+Z_kz\bigr).
}
\tag{4.2}
$$
右边两项分别在 $\ker S_{q+k}$ 与其正交补，结合 (2.5)，得到
$$
\boxed{
(\lambda_k')^2+
\|z_{\rm opt}^{(k)}+Z_kz\|_{\mathcal G_{q+k}}^2
=
\|h^{(k)}\|^2+\sum_{t=k+1}^d\|c_t\|^2.
}
\tag{4.3}
$$
这里 $\|\xi\|_{\mathcal G}^2=\langle\mathcal G\xi,\xi\rangle$，仍是原输入范数的准确正交分解。

新残量 $r^{(k)}$ 已写出真实范围和真正最小修复；目前没有把它认作 $r_{m,q+k}(w)$，也没有将其范数免费换成原 $\lambda$。一般 $h^{(k)}$ 的增长正好留在 (4.3) 中。

### 4.1 旧末链本身仍在新内部核

原内部等式逐段给 $S_{q+k}J_kc=0$：新窗口只扩大相同头位之外的空间，各旧输出仍为零；截断后的末段使用 $Ac_d=0$。记 $P_k=P_{\ker S_{q+k}}$，则 (4.2) 给
$$
c^{(k)}=P_kh^{(k)}-J_kc.
$$
又因为 $J_kc\in\ker S_{q+k}$ 和 (2.5)，有
$$
\langle P_kh^{(k)},J_kc\rangle=\langle h^{(k)},J_kc\rangle=0.
$$
因此准确细化为
$$
\boxed{(\lambda_k')^2=\sum_{t=k+1}^d\|c_t\|^2+\|P_kh^{(k)}\|^2,}
$$
$$
\|z_{\rm opt}^{(k)}+Z_kz\|_{\mathcal G_{q+k}}^2
=\|(I-P_k)h^{(k)}\|^2.
$$
它给出的只是新源能量的下界；没有支付窄通量在新核中的投影，也不把 $J_kc$ 自动称为它自身首段源的最小链。

### 4.2 同一个相邻窗口内的完整零源投影

以下补充 §4.1 的内部核身份，并明确它与旧双宽投影的关系。记
$$
P_k=P_{\ker S_{q+k}},\qquad
\mathcal Z_k=\ker S_{q+k}\cap\ker\mathsf D_{q+k},
\qquad \Pi_k=P_{\mathcal Z_k}.
$$
$\mathcal Z_k$ 是新原宽 $d$ 联合旗中的完整零源闭空间。它的向量满足 $L f=0$，孔支持位于 $[q+k+1,q+k+d]$。内部核 $\ker S_{q+k}$ 本身不具有这个零源结论。

因为 $J_kc\in\ker S_{q+k}$，且
$$
\mathsf D_{q+k}J_kc=Dc_{k+1}=-Ac_k,
$$
它是源
$$
s_k=-Ac_k\in\mathscr R_{q+k}
$$
的一个实际可行完整修复。源旗归属也可直接由上式及 $c_{k+1}$ 的原联合旗核阶验证。

令 $\mathcal R_{q+k}(s)$ 为新窗口中源 $s$ 的真正最小修复。极小元投影给
$$
J_kc=\mathcal R_{q+k}(s_k)+\Pi_kJ_kc.
\tag{4.4}
$$
另一方面，$c^{(k)}=P_kh^{(k)}-J_kc$ 是源 $r^{(k)}$ 的真正极小元，故 $c^{(k)}\perp\mathcal Z_k$。于是
$$
\boxed{
\Pi_kh^{(k)}=\Pi_kJ_kc
=J_kc-\mathcal R_{q+k}(-Ac_k).
}
\tag{4.5}
$$
准确的已付能量是
$$
\boxed{
\|\Pi_kh^{(k)}\|^2
=\sum_{t=k+1}^{d}\|c_t\|^2
-\lambda_{q+k}(-Ac_k)^2
\le\lambda^2.
}
\tag{4.6}
$$
这里没有把 $J_kc$ 本身当成源 $-Ac_k$ 的最小解。

若 $w\in W$，(1.1) 保证
$$
q+k+d\le q+2d-1
\le e^{d^3/4}+d\le e^{d^3/3}.
$$
因此原逐头 lift 可准确作用于 (4.5)，给
$$
|\langle w,\Pi_kh^{(k)}\rangle|
\le e^{-75d^4}\|w\|
\sqrt{\sum_{t=k+1}^{d}\|c_t\|^2
-\lambda_{q+k}(-Ac_k)^2}.
\tag{4.7}
$$
这是完整 $L$ 核的配对预算，不是对整个内部核的预算。

### 4.3 扣除旧双宽结论及剩余两个正交部分

把 $h^{(k)},J_kc$ 按其真实孔层放回原 Hilbert 空间，并令 $h=\sum_t h_t$。它们恰为
$$
h^{(k)}=P_{\mathscr C_{q+k}}h,\qquad
J_kc=P_{\mathscr C_{q+k}}c.
\tag{4.8}
$$
新空间 $\mathcal Z_k$ 包含于旧
$$
Z_{2d}=\ker L\cap\mathcal H_{[q+1,q+2d]}.
$$
[原双宽投影](../results/R239-appendix-double-width-head-flux-projection-and-exact-energy-drop.md)
已证 $P_{Z_{2d}}h=P_{Z_{2d}}c=c-c_{2d}$。
对这个身份再投到 $\mathcal Z_k$，并用 (4.8)，正好得到
$\Pi_kh^{(k)}=\Pi_kJ_kc$。所以 (4.5) 的去核投影身份是旧结论在一个具体相邻源窗口上的限制，不重计为新无权进展。这里补出的准确可行源为 $-Ac_k$，其同窗极小修复给 (4.6) 的具体能量下降。

剩余部分仍须保留。定义
$$
\rho_k
=\mathsf D_{q+k}P_kh^{(k)}
=r^{(k)}-Ac_k\in\mathscr R_{q+k}.
\tag{4.9}
$$
第二式用 $P_kh^{(k)}=c^{(k)}+J_kc$ 和
$\mathsf D_{q+k}J_kc=-Ac_k$。在内部核中再分离零源核，得到
$$
\boxed{
(I-\Pi_k)h^{(k)}
=(I-P_k)h^{(k)}+\mathcal R_{q+k}(\rho_k).
}
\tag{4.10}
$$
右边两项分别属于 $(\ker S_{q+k})^\perp$ 与
$\ker S_{q+k}\ominus\mathcal Z_k$，所以准确有
$$
\boxed{
\|(I-\Pi_k)h^{(k)}\|^2
=
\|(I-P_k)h^{(k)}\|^2
+\lambda_{q+k}(r^{(k)}-Ac_k)^2.
}
\tag{4.11}
$$
第一项就是 §4.1 的完整内部对偶余量；
第二项是明确新源 $\rho_k$ 的同窗完整修复费，不能因
$-Ac_k$ 有试探链 $J_kc$ 就把两者等同。

还有一个需保留符号的交叉式。由
$\langle P_kh^{(k)},J_kc\rangle
=\langle h^{(k)},J_kc\rangle=0$，
以及各自的 $\mathcal Z_k$ 正交分解，
$$
\boxed{
\left\langle
\mathcal R_{q+k}(\rho_k),
\mathcal R_{q+k}(-Ac_k)
\right\rangle
=-\|\Pi_kJ_kc\|^2.
}
\tag{4.12}
$$
该配对为实非正数；它是准确身份，不提供 (4.11) 中任一未付部分的上界。
特别，未把 $\rho_k$ 认成旧 $r_{\rm ret}$，也未把 $r^{(k)}$ 认成同一实际见证的相邻投影源。


## 5. 末段是已付源，其他段还不能倒推

取 $k=d-1$。此时 $Z_kz=0,h^{(k)}=0$，并且 $c_d$ 只有头 $e_0$。因此
$$
\mathsf D_{q+d-1}^*z_{d-1}=-c_d,\qquad
S_{q+d-1}c_d=0.
$$
所以 (4.1) 的新最小链准确为
$$
\boxed{
c^{(d-1)}=-c_d,\quad
z_{\rm opt}^{(d-1)}=0,\quad
(\lambda_{d-1}')^2=\|c_d\|^2\le\lambda^2.
}
\tag{5.1}
$$
它的残量还可直接写成
$$
r^{(d-1)}=-Dc_d=Ac_{d-1},
\tag{5.2}
$$
其中最后一步来自原最后一条内部方程。右端只在 $e_0$ 头，正符合[最低头精确分块](2026-11-13-boundary-variation-checkpoint-0c.md) §7；该最低头分块不重计。

对于 $k<d-1$，(4.3) 仍有真实 $h^{(k)}$。没有一个已证单调性允许从 (5.1) 倒推所有 $\lambda_k'$ 或所有 $h^{(k)}$ 都由 $\lambda$ 控制。

## 6. 所有平移的准确头权计数

把原 $h_t$ 按头坐标写为 $(h_t)_i$。
一个非零坐标满足 $d-t+1\le i\le d-1$。它在 (2.4) 中出现的 $k$ 恰为
$$
i-d+t\le k\le t-1,
$$
所以出现次数为 $d-i$，且每次保持原范数。于是
$$
\boxed{
\sum_{k=1}^{d-1}\|h^{(k)}\|^2
=
\sum_{t=2}^{d-1}
\sum_{i=d-t+1}^{d-1}
(d-i)\|(h_t)_i\|^2.
}
\tag{6.1}
$$
同样
$$
\sum_{k=1}^{d-1}\sum_{t=k+1}^d\|c_t\|^2
=\sum_{t=2}^d(t-1)\|c_t\|^2.
\tag{6.2}
$$
把 (4.3) 相加可得这两个准确加权能量的总和，未丢弃不同源层的新最优链或对偶余量。特别 (6.1) 是一个正的坐标计数，不是 $h$ 的新上界。

## 7. 与首段先消元的范围

最新首段先消元已经将真实残量的裸低链原像 $a_q(r)$ 由未来带支付，并给
$$
\mathcal H_2^\circ=A_H+B P_{\ker\mathsf F}B^*,\qquad
\sigma^\circ=Ba,\qquad
\mathcal E_2^\circ=\lambda^2-\|a\|^2.
$$
旧返回量仍为
$$
\mathcal E_2-\mathcal E_2^\circ
=\|\mathsf F^\dagger r_{\rm ret}\|^2.
$$
本笔记没有改动这些身份，也没有将 (4.3) 中的任意新源与它们自动相认。可继续使用的具体信息是：真实头通量逐位落入哪些相邻源层、其完整对偶余量以及 (5.1) 已支付的末端。所需倒推成本或真实返回项仍待证明。
