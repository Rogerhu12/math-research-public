# R271 补录：原最低列的完整三阶真旗 Schur、远方差一致残余与显式受限逆费用

日期：2026-11-20 UTC。作者：Astra-ISP-b2a9acde-20261120 / r271_cost；AI-assisted GPT-6 Astra Pro，根会话独立核验完整真旗、Schur解与原物理费用。

## 0. 范围与原 forcing

本条只处理三孔高度 $r=3$，并始终使用完整物理真核。

原 forcing 的准确来源为
[原纯远孔代表](R271-appendix-dual-tower-kernel-only-error-pure-far-height-representatives-and-joint-reciprocal-budget.md)
§1，式 (1.1) 后明确规定
$$
f_1=e_1\otimes\Omega,\qquad Ce_1=e_0,\qquad Ce_0=0.
$$
这里 $e_1$ 是最低整数坐标，而非任意物理一孔 $e_{2^j}$。
所以原全部 carry 保留时仍有 $C^2f_1=0$。

最高 $t$ 的完整真核极限 $F_0$ 对 $C_0$ 不变：
将 $v_t\in\ker C_t^3$ 与 $C_tv_t\in\ker C_t^3$ 取极限即可。
又 $f_1\in\ker C_t^3$ 对全部 $t$ 成立，故
$$
f_1\in F_0\cap\ker C_0^2,\qquad C_0^3F_0=0.
$$
本条不把上述性质推广给任意一孔源。

将下文 $F,C$ 分别取为 $F_0,C_0$，即得到原最高极点所需残余。
同一有限维真旗公式也适用于 $F=\ker C_t^3$ 和原 $C_t$。

## 1. 完整物理真幂旗

更一般地，设 $F$ 为 $C$-不变有限维子空间，$C^3F=0$，
且 $f\in F\cap\ker C^2$。
按原物理内积正交分解
$$
W_0=F\cap\ker C,\qquad
W_1=(F\cap\ker C^2)\ominus W_0,\qquad
W_2=F\ominus(F\cap\ker C^2).
\tag{1.1}
$$
因此
$$
T=C|_F=
\begin{pmatrix}
0&B&E\\
0&0&D\\
0&0&0
\end{pmatrix}.
\tag{1.2}
$$
$B:W_1\to W_0$ 与 $BD:W_2\to W_0$ 都单射。
所有零维块按零空间处理。

记
$$
\beta_1=\|B^\dagger\|,\qquad
\beta_2=\|(BD)^\dagger\|,\qquad c\ge\|C\|.
\tag{1.3}
$$
这些是实际受限旗的逆成本，不能一般用环境 $C^\dagger$ 免费代替。
若 $W_1=0$，幂零性给 $T=0$，本条源残余直接为零。
以下写非平凡情形，并令 $f=f_0+f_{(1)}$，$f_{(1)}\in W_1$；
下标 $(1)$ 表示旗分量，不另造一个 forcing。

## 2. 完整 Galerkin 的精确两块 Schur

取 $0<S\le1$，令
$$
H_S=I+C^*C/S+(C^*)^2C^2/(2S^2).
$$
完整解与原残余为
$$
a_S\in F,\quad P_FH_Sa_S=f,\qquad
\xi_S=f-H_Sa_S.
\tag{2.1}
$$
$H_S\ge I$，故 $\|a_S\|\le\|f\|$。

由于 $F$ 不变，其压缩恰为
$I_F+T^*T/S+(T^*)^2T^2/(2S^2)$；
这一步保留了整个物理压缩。
$W_0$ 块直接给 $a_0=f_0$。
令
$$
R_S=(S+B^*B)^{-1},\qquad
K_S=I-BR_SB^*.
$$
$0\le K_S\le I$。
定义正定的完整 Schur 算子
$$
\mathcal A_S=
S^2I+S(D^*D+E^*K_SE)+\tfrac12(BD)^*(BD).
\tag{2.2}
$$
它在 $W_2$ 上满足
$$
\mathcal A_S\ge\tfrac12(BD)^*(BD).
\tag{2.3}
$$
准确解为
$$
z_S=-\mathcal A_S^{-1}E^*BR_S f_{(1)},
$$
$$
\boxed{
a_2=S^2z_S,\qquad
a_1=SR_Sf_{(1)}-S^2R_SB^*Ez_S,\qquad
a_0=f_0.
}
\tag{2.4}
$$
若 $W_2=0$，直接令 $z_S=0$。

证明只是在完整 (1.2) 中消去 $W_1$ 块：
其对角为 $I+B^*B/S$，交叉为 $B^*E/S$；
剩下的 $W_2$ Schur 恰为 $\mathcal A_S/S^2$。
没有舍弃横向源；右端的 $W_2$ 分量为零来自明确的 $C^2f=0$ 前提。

## 3. 对原全部远方差的源一致界

由 (2.3)
$$
\|z_S\|\le2\beta_2^2c\beta_1\|f\|.
\tag{3.1}
$$
此外
$$
\|BD\,\mathcal A_S^{-1}\|\le2\beta_2.
$$
其证明是
$\mathcal A_S^{-1}(BD)^*(BD)\mathcal A_S^{-1}
\le2\mathcal A_S^{-1}\le4\beta_2^2I$。
所以
$$
\|BDz_S\|\le2c\beta_1\beta_2\|f\|.
\tag{3.2}
$$

准确代回得
$$
\frac{Ca_S}{S}
=BR_Sf_{(1)}+S( K_SEz_S\oplus Dz_S),
$$
$$
\frac{C^2a_S}{S^2}=BDz_S.
\tag{3.3}
$$
因 $K_S$ 收缩，$\|(K_SE,D)\|\le c$。
因此
$$
\boxed{
\|Ca_S\|/S
\le[\beta_1+2Sc^2\beta_1\beta_2^2]\|f\|,
}
\tag{3.4}
$$
$$
\boxed{
\|C^2a_S\|/S^2\le2c\beta_1\beta_2\|f\|.
}
\tag{3.5}
$$
最后用完整原 $C^*$，而不是其旗压缩，得到
$$
\boxed{
\|\xi_S\|
\le[\,2+c\beta_1+c^3\beta_1(2\beta_2^2+\beta_2)\,]\|f\|,
\qquad0<S\le1.
}
\tag{3.6}
$$
这是全实区间明确不等式，不是只有 $S\to0$ 的形式 $O(1)$。

## 4. 原残余在 $S=0$ 的准确有限极限

置
$$
u=(B^\dagger)^*f_{(1)},\qquad
v=(BD)^{\dagger *}E^*u.
\tag{4.1}
$$
由 (2.4)–(3.3)，在完整原物理空间中
$$
a_S\longrightarrow f_0,\qquad
Ca_S/S\longrightarrow u,\qquad
C^2a_S/(2S^2)\longrightarrow-v.
$$
所以
$$
\boxed{
\xi_S\longrightarrow
\xi_{\rm lim}=f_{(1)}-C^*u+(C^*)^2v.
}
\tag{4.2}
$$
三个项都在原空间中，不把 $C^*$ 压回 $F$。
$\xi_{\rm lim}\perp F$ 来自完整 Galerkin 极限。
此式也明确指出真正的逆费用在两个受限旗 Green 列中；
它没有因 $S$ 消失而自动消失。

## 5. 受限旗逆的完整整数约束证法

现在回到原最高极限 $F_0$，取 $m\ge5$、
$n=2^{m-1}$、$d=2n$、偶 $R\ge d$、
$$
a=16^{m-2},\qquad y=m+R/2.
$$
使用已证[最高可逆单位因子不改变同一完整 $F_0$](R271-appendix-highest-unit-invariant-true-kernel-and-graded-physical-energy.md)定理；
旧头相似以后，可在每条单位奇尾链上用
$$
C_\circ=J_n+bE_{\rm high}+J_l,\qquad b=m^{-2},
$$
$$
X_0=C_\circ^3,\qquad
X_1=\left.\partial_t(C_\circ+tN_\circ)^3\right|_0,
\quad
N_\circ=E_{\rm high}\otimes E_{n-1,0}.
\tag{5.1}
$$
规范头仍保同一个完整原 $F_0$，恢复旧头与强尾的物理费用在 §7 支付。

令局部维数 $N_l=dl$，对 $j=1,2$ 定义完整约束矩阵
$$
\boxed{
\mathcal J_j=
\begin{pmatrix}
X_0&0\\
X_1&X_0\\
C_\circ^j&0
\end{pmatrix}.
}
\tag{5.2}
$$
这只是短小理论构造公式，不登记消元向量或行列式输出表。

### 引理 5.1

$$
\boxed{
\|(C_\circ^j|_{F_\circ})^\dagger\|
\le\|\mathcal J_j^\dagger\|,\qquad j=1,2.
}
\tag{5.3}
$$

**证明。** 对任意 $x\in F_\circ$，完整 Schur 兼容性给某个 $z$ 使
$$
X_0x=0,\qquad X_1x+X_0z=0.
$$
因此
$$
\mathcal J_j(x,z)=(0,0,C_\circ^jx).
$$
将 $(x,z)$ 正交投到 $\ker\mathcal J_j$。
其第一分量 $x'$ 属于
$F_\circ\cap\ker C_\circ^j$，且
$$
\|x-x'\|\le
\operatorname{dist}((x,z),\ker\mathcal J_j)
\le\|\mathcal J_j^\dagger\|\|C_\circ^jx\|.
$$
在 $F_\circ$ 内对核取正交补，得到 (5.3)。
不需要事先为辅助 $z$ 的范数付费，也没有把受限核当环境核。证毕。

## 6. 坏链与好链的明确局部常数

$R$ 为偶数，全部强尾 Boolean Jordan 链长 $l=R-2j+1$ 都为奇数；$d$ 为偶数。因此每条链恰落在 $l\le d+1$ 或 $l\ge d+3$，没有漏掉长度 $d+2$ 的边界。

### 6.1 全部坏链 $l\le d+1$

$\|C_\circ\|<3$，所以
$$
\|X_0\|\le27,\qquad \|X_1\|\le27,\qquad
\|C_\circ^j\|\le9.
$$
可统一取 $\|\mathcal J_j\|<90$。
乘 $m^6$ 后 (5.2) 是整数矩阵，
秩不超过 $2N_l$。

任意非零秩整数矩阵的非零奇值平方乘积，
由 Cauchy–Binet 等于其最高阶整数余子式平方和，至少为 $1$。
若其算子范数至多 $M$、秩 $k$，则
$\sigma_{\min}^+\ge M^{-(k-1)}$。
因此由 (5.3)
$$
\boxed{
\|(C_\circ^j|_{F_\circ})^\dagger\|
\le (90m^6)^{2d(d+1)}
=:K_{\rm bad},\qquad j=1,2.
}
\tag{6.1}
$$
本界是完整理论整数界，无需附带任何可重算的数组。

### 6.2 全部好链 $l\ge d+3$

此时不掉秩，$F_\circ=\ker C_\circ^3$。
完整长链参数化
$$
\Phi_p(u)=\sum_{k=0}^n(-1)^k
\binom{p+k-1}{k}H_0^ku\otimes e_{p-1+k},
\quad p=1,2,3,
$$
满足 $C_\circ\Phi_p=\Phi_{p-1}$。
规范 $H_0=J_n+bE$ 的范数小于 $2$，所以
$$
\|\Phi\|\le3(n+2)^3 2^n.
$$
前三级左逆为
$u_1=v_0,u_2=v_1+H_0v_0,u_3=v_2+2H_0v_1+H_0^2v_0$，
其范数不超过 $9$。
故单位尾链上的完整受限 $C_\circ,C_\circ^2$ MP 均不超过
$$
\boxed{K_{\rm good}=27(n+2)^3 2^n.}
\tag{6.2}
$$

## 7. 原强权及旧头还原

原强段用中位尺度 $c=y^{-2}$ 归一化，成本至多 $4^R$。
标准链是 $cL_l$。

对坏链，整体转为单位 $J_l$ 的条件数至多 $y^{2d}$。
对好链，不应支付整个长链的单位相似成本：
上述 $\Phi$ 仅用前 $n+3$ 个尾级。
单位相似对角
$$
q_k=c^k\sqrt{\frac{k!(l-1)!}{(l-1-k)!}}
$$
满足
$
\frac{q_k}{q_{k-1}}=c\sqrt{k(l-k)}\le\frac{R+1}{2y^2}<1,\qquad q_0=1.
$
因而全部所需 $q_k\le1$；又根号中的整数因子至少一，所以在 $k\le n+2$ 上 $q_k\ge c^k$，即 $q_k^{-1}\le y^{2n+4}$。
前三个尾级的左逆因此只乘不超过一的 $q_k$。
所以完整好链受限 MP 只需乘
$y^{2n+4}\le y^{2d}$。

旧真实头相似条件数至多 $e^{221a}$，准确来源是 [R239 的真实头 Jordan 费用](R239-appendix-true-head-jordan-cost-and-pure-graded-formal-range.md) §3、式 (3.9)：$h$ 位头的费用为 $e^{221\cdot16^{h-1}}$，此处取 $h=m-1\ge4$，所以正好是 $a=16^{m-2}$。
在完整 primitive 直和中取各块真解，再还原，最小物理解至多该候选；
只取最大块费用，不乘链条数量。
于是设
$$
\boxed{
K_{\rm flag}=
e^{221a}4^R y^{2d}
\big[(90m^6)^{2d(d+1)}+27(n+2)^3 2^n\big].
}
\tag{7.1}
$$
对原完整 $F_0$，
$$
\boxed{
\|B^\dagger\|\le K_{\rm flag},\qquad
\|(BD)^\dagger\|\le K_{\rm flag}.
}
\tag{7.2}
$$
第一式因为 $W_1\subset F_0\ominus\ker(C_0|_{F_0})$，
第二式就是第二真幂的核正交补。
没有把 $F_0\cap\ker C_0^j$ 擅换成更大的环境核。

原旧头最大 carry 重标度也可使用同一 $221a$ 界，
其逆芽/输入权单调性已在[一般头高孔费用](R271-appendix-general-head-high-hole-schur-complement-and-complete-residue-cost.md) §8 单独证明。
最高参考 $U^{-1}$ 和最高 $t^{-1}$ 不进入 (7.1)：
本条估的是同一个 $F_0,C_0$ 的源，不是最高极点的逆算子。

## 8. 原完整源的显式、远方差无损上界

原 $C_0$ 可取 $\|C_0\|<8$，$K_{\rm flag}\ge1$，
单位 $f_1$ 的 (3.6) 因此给
$$
\boxed{
\|\xi_0(S)\|\le1600K_{\rm flag}^3,\qquad0<S\le1.
}
\tag{8.1}
$$
特别可以直接代入原 $S=S_x$，不用假设它进入未知邻域。
明确对数费用为
$$
663a+R\log64+6d\log y+O(d^2\log m+d).
\tag{8.2}
$$
这去掉了粗 $H$ 范数带来的 $S^{-2}$ 或更高伪发散，
并把受限真旗的全部逆成本真正支付。

(8.1) 是原完整残余的无权界。
它尚不是 $\gamma^{1-g}$ 物理孔加权界；
不能把 $64^R$ 上界直接解释为原高孔源已足够小。
原 $\mathcal Z_\gamma$、最高极点与正则部分之间的实际费用配平仍未闭。


## 9. 证明的可核边界

本条为有限维算子不等式证明，不依赖抽样矩阵或新增计算证书。根会话逐项核验 (2.4) 的原Schur消元、(3.2) 的正算子夹逼、(4.2) 的完整环境伴随极限、(5.3) 的增广约束距离、整数矩阵奇值乘积下界，以及 (7.1) 中好/坏链与原相似费用。特别保留 $F_0\cap\ker C_0^j$ 的真核，未换成环境核；$1600$ 来自 $2+8+8^3(2+1)=1546<1600$ 与 $K_{\rm flag}\ge1$。

主问题及原物理孔加权残余费用仍按 §8 的严格范围保持开放。
