# R150：任意原三次在规范均值理想中的纯二元三次替换

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。

## 1. 完整原理想结论

在[已刊规范四原式](R150-appendix-unit211-W-original-mean-ideal-three-plane-cubics-and-six-overlaps.md)的权系数环中，写

$$
R_0=F+A(\lambda,S),\quad
R_1=\lambda F+B(\lambda,S),\quad
R_2=SF+C(\lambda,S),\quad
Q_F=F^2+dF+E(\lambda,S).
\tag{1}
$$

这里 $d$ 仅依赖权，$A,B,C,E$ 的总几何次数至多 $2$，所有系数只含已经支付的权分母。令 $I=(R_0,R_1,R_2,Q_F)$；它就是此前保留完整原 $q_F$ 的同一均值理想。

**定理。** 每一条总几何次数至多 $3$ 的原多项式
$P(F,\lambda,S)$，都有一个显式的、总次数仍至多 $3$ 的纯二元多项式 $\widehat P(\lambda,S)$，使

$$
P-\widehat P\in I,
\qquad
(I,P)=(I,\widehat P).
\tag{2}
$$

下面给出全部原组合系数。过程没有任何新的除法，也不需要倒置 $F$、$\lambda$、$S$、几何 $D$ 或任一三次头子式。它不会因直接代入 $F=-A$ 而把一条三次式展开为六次式。

## 2. 先用完整原 QF 压低 F 次数

唯一写成

$$
P=c_3F^3+a_1(\lambda,S)F^2+
a_2(\lambda,S)F+a_3(\lambda,S),
\tag{3}
$$

其中 $c_3$ 是权系数，$\deg a_1\le1$、
$\deg a_2\le2$、$\deg a_3\le3$。缺少某一 F 次项时，对应系数取零。

定义

$$
U=a_2-da_1+c_3d^2-c_3E,\qquad
V=a_3-a_1E+c_3dE.
\tag{4}
$$

于是 $\deg U\le2,\ \deg V\le3$，并有完整恒等式

$$
P=(c_3F+a_1-c_3d)Q_F+FU+V.
\tag{5}
$$

将 (1) 的 $Q_F$ 代入右侧，$F^2$ 中的 $c_3d$ 两项、$F$ 中的 $c_3E$、$da_1$、$c_3d^2$ 及常数中的 $a_1E,c_3dE$ 分别成对抵消，余下正是 (3)。该身份在任意交换系数环上成立，不需要泛型主元假设。

## 3. F 乘二次的完整消去

写

$$
U=u_{20}\lambda^2+u_{11}\lambda S+u_{02}S^2
+u_{10}\lambda+u_{01}S+u_{00},
$$

并定义

$$
U_\lambda=u_{20}\lambda+u_{11}S+u_{10},
\qquad
U_S=u_{02}S+u_{01}.
$$

则

$$
U=\lambda U_\lambda+S U_S+u_{00}.
$$

用 (1) 的两条原一次乘法行，而不是倒置 $\lambda$ 或 $S$，得到

$$
FU=-U_\lambda B-U_SC+u_{00}F
+U_\lambda R_1+U_SR_2.
\tag{6}
$$

最后用 $F=R_0-A$，置

$$
\widehat P
=V-U_\lambda B-U_SC-u_{00}A.
\tag{7}
$$

每一项的总次数至多 $3$。合并 (5)–(7) 给出所需完整原系数身份

$$
\boxed{
P=\widehat P+
(c_3F+a_1-c_3d)Q_F+
U_\lambda R_1+U_SR_2+u_{00}R_0.
}
\tag{8}
$$

(8) 两向说明 (2)，并在所有系数退化、$c_3=0$、某个 $u_{ij}=0$ 的情形保持成立。不存在需要另开的首项零面。

## 4. 对完整 weighted NS/PS 的原输入

当前 W 的两个原 weighted 必要式 $N_s,P_s$ 在同一原
$(F,\lambda,S)$ 坐标中总次数至多 $3$。其原 Gram、
N4 极化、P2 以及通过同一 $HA,HB$ 返回单值的迹，已经在[中心化原物理输入](R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-centered-physical-coordinate-and-original-S-linear-row.md)及后续完整原值源中固定。

把它们分别代入 (3)–(8)，得到 $\widehat N_s,\widehat P_s$，故

$$
(I,N_s,P_s)=(I,\widehat N_s,\widehat P_s).
\tag{9}
$$

这是一条准确的原理想替换，不只是充分条件或数值拟合。当前只替换这两个 weighted 式；完整个别 N/P、同一个原值与 $N_4(V)$ 的其余条件仍保留。没有把 (9) 宣称为整个原问题的等价两式系统。

## 5. 新的固定六阶原参数输入

在明确的 $H_{265}\ne0$ 图上，[已完成的四规则与十二真乘法](R150-appendix-unit211-W-first-binary-head-open-original-value-six-coordinate-return.md)可用于这两个新的纯三次输入。设它们在真实六生成元

$$
v=(1,\lambda,S,\lambda^2,\lambda S,S^2)
$$

上的必要列为 $n,p$，真实乘法矩阵为 $M_\lambda,M_S$。新固定矩阵定义为

$$
\mathcal N=
[n,\ p,\ M_\lambda n,\ M_Sn,\ M_\lambda p,\ M_Sp].
\tag{10}
$$

每个完整原点满足 $v\mathcal N=0$，且 $v$ 的第一坐标恒为 $1$。因此每个原点必满足

$$
\det\mathcal N=0.
\tag{11}
$$

这不要求六生成元自由，也不要求两个所选矩阵在一个自由六维空间中逐项交换；只需已经实际返回的
$vM_\lambda=\lambda v,\ vM_S=Sv$。

新源先用每列已付公分母及已付内容把 (10) 规范为权多项式矩阵，逐系数核回；再计算一个固定六阶多项式行列式。若用 Bareiss 中间除法，全部商在 $\mathbb Q[e,k]$ 中乘回，因此中间主元零面不被当作点态分母删除。只有实际形成非零行列式后，才能把它作为补图中的新必要权曲线；若再剥已付因子，整个 $H_{265}=0$ 必须乘回全局覆盖。

本页只定义并证明这个新输入的必要性。尚未运行时，不声称 (10) 已构造、不声称行列式非零或补图已空；其实际结果另以唯一运行回执登记。

## 6. 冻结源及与旧负门的区别

新源建议路径：

[2026-11-28-unit211-W-original-NSPS-pure-binary-cubics-and-fixed-six-determinant-8542.py](../notes/2026-11-28-unit211-W-original-NSPS-pure-binary-cubics-and-fixed-six-determinant-8542.py)

Git blob：7168d1fca285aca72ec4cfd21e8e36575df44ebf。SHA256：

d5c514ea047fbc4fb7f3589cf9a75fce1cae0ae60e063e3b4e08001a1f5b4925。

源码只使用旧 8222 源的 $5393$ 字节四规则/十二真乘法构造前缀，其 SHA256 为

2a69d39d3240309cbbd47523ecd1bf6156c4dae862a7cb83e4dd04dee9dc71d7。

该前缀结束于旧四条原值输入开始之前，所以没有执行已经冻结的 R3/q4 四行约化、QQ(e,k) 主元扩展或常数目标门。新数学输入是完整 NS/PS 的 (8) 及新的固定矩阵 (10)，不是旧门加时或换主元顺序。

限额仍为 $180$ 秒、$4$ GiB。源码不输出编码分片，不保存矩阵或证书缓存，仅保源、参数定义、运行身份及小摘要。本页 (2)、(8)、(9) 已由完整纸面证明成立；(10) 的计算结果以及全部有限纤维排除均未在本页预先宣称。
