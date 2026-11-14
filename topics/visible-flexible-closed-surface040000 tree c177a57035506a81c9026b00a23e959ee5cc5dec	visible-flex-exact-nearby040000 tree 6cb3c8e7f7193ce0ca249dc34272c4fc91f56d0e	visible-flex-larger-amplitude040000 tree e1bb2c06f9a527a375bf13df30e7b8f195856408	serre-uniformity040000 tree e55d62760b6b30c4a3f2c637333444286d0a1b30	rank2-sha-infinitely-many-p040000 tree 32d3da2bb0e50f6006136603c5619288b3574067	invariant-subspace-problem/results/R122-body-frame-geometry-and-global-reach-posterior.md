# R122：实际重建图的体标架几何后验与完整 reach 接口

2026-11-12，Astra-visible-flex-fd2d / root，接 R10、R119、R121。

**状态：以下条件后验及其全部证明已完成。** 给定 R119 的真实有限场，
位置到指定点的距离、包围球和辅助法向支撑可由三维反对称线性方程直接求出。
有限求值误差仍只有残差的积分，不需假设 Codazzi 初值问题稳定。
真实曲率和法向修正另由 R119 的相容缺陷支付；二者结合 R10 给完整闭核的
全局 reach，而不是只给局部曲率半径。本文尚未取得新的强目标非线性闭核。

## 1. 唯一实际位置图与体坐标

沿用 R119 的固定物理材料坐标 $(s,u)$，$g=ds^2+a(s)^2du^2$，以及

$$
A=\begin{pmatrix}0&0&-l\\0&0&-m\\l&m&0\end{pmatrix},
\qquad F_s=FA,\qquad X_s=F e_1^{\rm std},\qquad F\in SO(3).
\tag{1}
$$

初始准确闭曲线和准确定向标架与 R119 相同。所有量指 (1) 的准确 ODE 解，
不是把浮点积分节点本身当成连续曲面。上半活动核的约定是
$F=(e_1,e_2,N)$、中央 $N$ 指向内侧，故所需外法向接近 $-N$。

对任意**固定的空间点** $p\in\mathbb R^3$ 定义

$$
q_p=F^T(X-p).
$$

则逐个材料角准确有

$$
\boxed{(q_p)_s=-Aq_p+e_1^{\rm std},\qquad
q_p(0,u)=F(0,u)^T(\gamma(u)-p).}
\tag{2}
$$

因为 $(F^T)_s=-AF^T$ 且 $F^TX_s=e_1^{\rm std}$，(2) 由乘法法则直接得到。
反之，(2) 的唯一解就是上述 $F^T(X-p)$；不能另选初始数据后仍称为同一位置图。
特别地

$$
|q_p|=|X-p|,\qquad |q_0|=|X|,
\qquad -(q_0)_3=-X\cdot N.
\tag{3}
$$

因此包围球、held 见证球排除和辅助支撑可分别消费 $q_0,q_p$。
只关心这些量时，无需把每个 Cartesian 标架分量都加入非线性 BVP。

若还要投影到固定单位方向 $v$，令 $h_v=F^Tv$。准确方程及读数为

$$
(h_v)_s=-Ah_v,\qquad h_v(0,u)=F(0,u)^Tv,
\qquad X\cdot v=q_0\cdot h_v,\qquad |h_v|=1.
\tag{4}
$$

取 $v=e_y,e_z$ 即可检查 R121 的板宽和实际高度。这些只是同一个 X 的求值表示，
没有修改物理 g、材料角或近似曲面的定义。

## 2. 有限求值残差的无指数界

设 $\widehat q_p(s,u)$ 是连续、分段 $C^1$ 的实际有限表示，定义其**完整**残差

$$
r_p=(\widehat q_p)_s+A\widehat q_p-e_1^{\rm std}.
\tag{5}
$$

若 $|q_p(0,u)-\widehat q_p(0,u)|\le e_{p,0}(u)$，则

$$
\boxed{|q_p(s,u)-\widehat q_p(s,u)|
\le e_p(s,u):=e_{p,0}(u)+\int_0^s|r_p(v,u)|\,dv.}
\tag{6}
$$

证明：误差 $E=q_p-\widehat q_p$ 满足 $E_s=-AE-r_p$。
$-A$ 反对称，其齐次传播矩阵正交；变常数公式及三角不等式即给 (6)。
系数仅需连续，不用 $l_s,m_s$，也不出现 $\exp\int\|A\|$。
若有限表示在分段处有跳跃，还须把每个跳跃的范数加入累计误差；
采用共享节点值的表示可使这一项准确为零。

对 (4) 的有限表示 $\widehat h_v$，同样令
$r_v=(\widehat h_v)_s+A\widehat h_v$，得到

$$
|h_v-\widehat h_v|\le e_v:=e_{v,0}+\int_0^s|r_v|.
\tag{7}
$$

该表示不要求 $\widehat h_v$ 或 $\widehat q_p$ 人为重新正交化。
由 (3)、(6) 直接得到每一点的严格读数

$$
\max\{0,|\widehat q_p|-e_p\}\le |X-p|
\le|\widehat q_p|+e_p,
\tag{8}
$$
$$
-X\cdot N\ge-(\widehat q_0)_3-e_0,
\tag{9}
$$
$$
|X\cdot v-\widehat q_0\cdot\widehat h_v|
\le e_0+|\widehat q_0|e_v.
\tag{10}
$$

最后一式用
$q_0\cdot h_v-\widehat q_0\cdot\widehat h_v
=(q_0-\widehat q_0)\cdot h_v+\widehat q_0\cdot(h_v-\widehat h_v)$
以及准确的 $|h_v|=1$。所有积分和初值误差必须用真实连续上界支付；
普通 ODE 容差或几个点的差值本身不是 (6) 的证书。

## 3. 从辅助 N 到实际外法向

用 R119 的记号

$$
C=X_u-ae_2,\qquad |C|\le k(s),\qquad \eta=k/a<1.
$$

实际单位法向 $N_X$ 取与 $N$ 同向，即

$$
N_X=\frac{e_1\times(e_2+C/a)}{|e_1\times(e_2+C/a)|}.
\tag{11}
$$

在正交基 $(e_1,e_2,N)$ 下写 $C/a=c_1e_1+c_2e_2+c_3N$。
则分子为 $(1+c_2)N-c_3e_2$，且 $c_2^2+c_3^2\le\eta^2$。
因为 $1+c_2>0$，它与 N 的夹角小于 $\pi/2$。对圆盘
$(c_2,c_3)$ 的切线，或直接将 $c_3^2/( (1+c_2)^2+c_3^2)$ 最大化，得到

$$
\sin\angle(N_X,N)\le\eta,
\qquad |N_X-N|\le\sqrt{2(1-\sqrt{1-\eta^2})}\le2\eta.
\tag{12}
$$

最后一个松界在整个 $0\le\eta<1$ 上成立，并包括 $\eta=0$。
因此实际外法向 $\nu=-N_X$ 的支撑满足

$$
\boxed{X\cdot\nu\ge-X\cdot N-2\eta|X|
\ge-(\widehat q_0)_3-e_0-2\eta(|\widehat q_0|+e_0).}
\tag{13}
$$

这是实际法向的界；不能直接把 $-X\cdot N$ 当成最终支撑。
若需要更紧余量，可在 (13) 中用 (12) 的平方根表达式替代 $2\eta$。
也可将固定中心改为 c：把 $q_0$ 换成 $q_c$，得到 $(X-c)\cdot\nu$ 的同一公式。

## 4. 角向和径向盒的完整覆盖

无需依赖节点本身就覆盖整个角圈。若已证 R119 的
$\|D\|\le d$、$|C|\le k$，则由真实导数准确有

$$
|X_s|=1,\qquad |X_u|\le a+k,
\tag{14}
$$
$$
|N_s|=\sqrt{l^2+m^2},\qquad
|N_u|\le a\sqrt{m^2+n^2}+d.
\tag{15}
$$

第二行由 $N_s=-le_1-me_2$ 及 $F_u=FB+D$ 的第三列得到。
对以 $(s_c,u_c)$ 为中心、半宽 $(\Delta_s,\Delta_u)$ 的物理材料矩形，
先在 $s=s_c$ 沿 u，再沿固定 u 走径向。若相应完整线段上
$a+k\le V$、$\sqrt{l^2+m^2}\le L_N$、
$a\sqrt{m^2+n^2}+d\le U_N$，则

$$
|X(s,u)-X(s_c,u_c)|\le b_X:=\Delta_s+V\Delta_u,
\tag{16}
$$
$$
|N(s,u)-N(s_c,u_c)|\le b_N:=L_N\Delta_s+U_N\Delta_u.
\tag{17}
$$

将中心点的求值误差计入后，(16) 直接扩充球包、板宽、cuff 高度及见证距离；
例如 $|X_c-p|\ge d_c$ 给整盒 $|X-p|\ge\max\{0,d_c-b_X\}$。
若 $|X_c|\le R_c$、$-X_c\cdot N_c\ge s_c^*$，则整盒

$$
|X|\le R_c+b_X,\qquad
-X\cdot N\ge s_c^*-b_X-R_cb_N.
\tag{18}
$$

证明后式时用
$X\cdot N-X_c\cdot N_c=(X-X_c)\cdot N+X_c\cdot(N-N_c)$
及 $|N|=1$。这样不把一个全局范数重复乘入误差，也不漏角向变化。
周期跨界盒可先提升到实数角，再用周期性还原。

若 BVP 使用移动计算角 $u=U(s,\xi)$，必须先按真实物理 u 的定义评价，
或者显式将物理矩形包含进计算坐标域。不能把 $(s,\xi)$ 的宽度直接代入 (16)。
这些是同一个固定材料图的覆盖方法，并不要求额外的三阶径向正则性。

## 5. 完整闭核的嵌入与 reach

假设实际上核、其对称下核和两个真实平圆盘已按共同二 jet 接成 C² 浸入
$\overline X:S^2\to\mathbb R^3$。每处使用相容的同一个外法向。
由 (13) 或 (18) 加 (12) 在活动部分证明

$$
X\cdot\nu\ge\sigma>0.
$$

上下平盘位于 $z=\pm Z$、外法向分别为 $\pm e_z$，故它们的支撑准确为 Z，
主曲率准确为零。令活动部分的实际曲率上界由 R119 (14) 给出为 $K_*$。
于是 R10 的全部假设适用于**完整同一闭图**，从而

$$
\boxed{\overline X\text{ 为嵌入},\qquad
\operatorname{reach}(\overline X(S^2))
\ge\min\{\sigma,Z,K_*^{-1}\}.}
\tag{19}
$$

若 $K_*=0$，按 $K_*^{-1}=+\infty$ 理解。
这里使用 R10 的完整证明：小平行面保持浸入及正支撑，径向投影均为单层覆盖，
各平行面沿射线严格嵌套，故法向映射在所给距离内单射，最近点唯一。
因此 (19) 同时排除了远处曲面自靠近，不是从曲率界孤立地推断 reach。

正支撑是一条充分认证途径。某候选不能通过 (13) 的松预算并不证明它没有 reach，
也不把本途径添加为 README 之外的必要验收标准。

## 6. 与 R121 强比例条件的直接组合

假设一个实际闭核已经支付共同 g、全域误差及加密、所有接缝，且有
真实中央长轴点 $p=(0,A_q,0)$ 的旋转对应，$A_q\ge1.28$。
通过上述完整覆盖在相位零验证

$$
|X|\le2.25,\quad |y|\le.85,\quad |z|\le Z,
\quad |X-p|\ge.9,\quad .9\le Z\le z_{c,\rm corner},
\tag{20}
$$

并使 (19) 的下界至少 $.136$。其中 p 的数值误差也须计入 (8)；
不能把种子长轴值冒作变化中央的真实 $A_q$。
活动相位是共同中心的空间正交变换与材料重参数化，故球包、支撑、曲率和 reach
对所有相位相同；所需两个相位间的 held 与板宽比较则按 R121 使用 (20)。

R121 的完整固定帽及其跨片滚动球证明遂给

$$
D\le4.5,\qquad \delta_{\rm hold}/D\ge.2,\qquad
\delta_E/D\ge2299/45000>.05,\qquad
\operatorname{reach}/D\ge34/1125>.03.
\tag{21}
$$

这些结论消费的是 (1) 的实际 X，以及 R119 对它的实际度量和曲率估计。
只满足形式 l,m,n 的特征值、有限点采样、线性 m2 轨道或未闭合 BVP 都不足以应用 (21)。
尤其，非零 Codazzi 残差下的 cut 位置和二 jet 接合仍须单独实付；
本结果没有替任何尚未得到的非线性尾或闭核补造接缝。

## 7. 可复现的有限求值核对

`scripts/fd2d_gc_body_geometry.py` 实现 (2)、(4)、完整残差 (5) 及读数 (3)。
其残差接口要求传入所保存有限表示的真实导数，不能把重新计算的 RHS 当作导数。
`scripts/fd2d-gc-body-background-check.py` 在同一 p148 完整旋转背景的全部89个实际径向片上，
逐片积分体坐标，并与显式旋转面及独立高度 Gauss 积分比较。
输出是 `notes/2026-11-12-fd2d-gc-body-background-check-01.json`。

真实运行 session16340 自然 exit0，约5.82秒；8个角、每片17个径向点的距离、
支撑和 y/z 读数对照差最大约 $2.311\times10^{-12}$。全部输入和源码 SHA 在报告中。
这是对实现符号和求值的有限检查，既非区间 ODE 证书，也非实际非圆强核。
正文的条件定理不以这些有限对照差充作 (6) 所需的连续残差上界。
