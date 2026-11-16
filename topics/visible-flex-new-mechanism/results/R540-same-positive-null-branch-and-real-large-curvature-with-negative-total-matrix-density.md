# R540：同一正支上的有限大速度脉冲与保留净负累计的真实 $k>2$ 到达

日期：2026-11-16。**完整原式纸面证明；没有执行数值、符号、profile、矩阵秩或开发检查，没有启动科学任务。**

本稿继续 R533 的三十三行母和 R536 的一次固定第三规范。新的结论是：可以从真实零 history 的常态入 germ 出发，沿同一个全相位 ruling 恒零的有限光滑路径，先取得严格负的完整累计 $p_1^{\omega_c}$，再在不丢掉这个负累计的条件下进入真实 $k>2$ 区。

后半段不是将两个互不相接的 null 分支拼在一起。先用一个有完整八矩账的短高度下降段，把已有实际速度送进明确的 $X>0$ 支；随后所有控制都留在该支。大速度段的真实八矩平方成本一般很大。本稿仅使用原三个 $p$ 列没有速度平方项这一事实，压小它们的追加积分；不把整八矩或第三 history 的成本说成小量。

这仍不是 $M=0$、末常态 germ、frame/pose 返回或最终 period 的构造。它具体支付的是 R524 所要求的大曲率区域的实际到达，并保留先前真实取得的一个净负坐标。不存在“已越过全部必要门”或“其余七矩可免费配平”的推论。

直接原源：

- [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)：逐点八矩与真实第三恢复；
- [R520](R520-variable-mother-constant-ruling-and-same-gauge-nonconstant-local-departure.md)：完整 $\mathcal F_{\rm path}$、全相位当前状态方程及加速度消项；
- [R531](R531-real-negative-p1-segments-in-the-three-zero-library-with-one-fixed-gauge.md)：一次固定 Gram 规范和同规范平滑输入切换；
- [R533](R533-complete-velocity-quadratic-form-and-all-history-regular-ruling-coordinates.md)：三十三行实际正根、统一三导能量和全 history 不定速度二次型；
- [R536](R536-real-negative-total-matrix-density-from-a-complete-fast-height-loop.md)：真实常态前缀、完整快高度回路及严格负累计；
- [R524](R524-same-gauge-constant-return-gates-and-real-matrix-excursion-obstructions.md)：原 $M=0$ 的大幅必要条件。

## 1. 同一对象与本稿定理

从起点选
$$
S_c=(h_c,0,\omega_c),\qquad h_c>0,\quad \omega_c>0,
\qquad x+\omega_c>0\quad(x\in I).
\tag{1}
$$
$\omega_c>0$ 是本稿的初选条件，R533 原允许范围包含它。原物理窗口 $I$、宽度、cap、种子、有理保护芽、全部真实正权复制和旧二十个完整数值目标均不移动。特别不把代数点 $-\omega_c/2$ 当成物理支持点。

记
$$
\eta=\omega-\omega_c,\qquad d_c=h\eta-k,\qquad
\gamma=h_s,\qquad
\delta=\frac{k_s}{2}-\eta\gamma,\qquad z=(\gamma,\delta).
\tag{2}
$$
因此
$$
k_s=2(\delta+\eta\gamma),\qquad
\eta_s=\frac{\delta+\eta\gamma}{h},\qquad
(d_c)_s=-\delta .
\tag{3}
$$
原第二 history 始终满足
$$
m_s=M_{\rm raw}(S,z),\qquad A=\Phi_m.
\tag{4}
$$
全局第二规范为 $w_\theta=0$，第三规范 $\chi_\theta$ 按 R536 的 Gram 方程选一次，随后固定。

**定理。** 可以联合从起点选择 R533/R536 的一个有限母、一个有限 $L>0$ 和这一固定 $\chi$，使一条从原零 history 常态入 germ 开始的有限光滑真实路径满足：

$$
\mathscr K(s,\theta)=0\quad\text{对全部 }s,\theta,
\tag{5}
$$
$$
\int_{\rm entire\ path}p_1^{\omega_c}(s)\,ds<0,
\qquad
p_1^{\omega_c}=p_1-2\omega_cp_2=-kd_c,
\tag{6}
$$
且末态 $k>2$。整个 scalar 路径留在一个预先选定的有限合法紧盒内。八矩、第三 history、frame、位置和第四成本均为这一条路径的真实输出。

“同一个母”是指本稿与 R536 的选择在路径开始前一次完成；不声称任意已经冻结、只为某个小 scalar 盒选出的旧母，自动适用本稿较大的盒。

## 2. 先固定有限母族常数，再选较大的合法盒

这一选择顺序不能倒过来隐藏循环依赖。

R520 §3.2 的 $\mathcal F_{\rm path}$ 是全部完整函数的一个固定有限生成表。它从原有限恢复和几何系数展开得到，不是针对每个 scalar 紧盒另添 profile 观察。R533 的三十三行主列、严格正核、右逆、共同 $C^2$ 小邻域也可以先固定；它们依赖(1)、原窗口和原目标，不依赖稍后要证明不变性的辅助 scalar 盒。

按 R533 §§7–8，对每个最终选择的有限 $\Lambda$，选同一有限正幅构造中的真实根，得到
$$
\mathsf A[P]=O(1),\qquad
\mathsf B[P]=-\Lambda P(\xi_*)+O(1),\qquad
\xi_*=-\omega_c/2,\qquad \deg P\le6,
\tag{7}
$$
和
$$
\sum_i\|u_i'''\|_2^2\le C_*(1+\Lambda).
\tag{8}
$$
其中 $L_c=u'-(x+\omega_c)u''$，$\mathsf A,\mathsf B,\mathsf C$ 分别是完整有号积分的 $L_c^2t^2,L_crt^2,r^2t^2$ 矩；记号准确同 R533。所有 $O(1)$ 的系数矩界，以及 $C_*$，在先固定的正列和 $C^2$ 图册中与 $\Lambda$ 无关。

于是有一个先固定的 $K\ge1$，使
$$
|\mathsf C[P]|\le K(1+\Lambda)\sup_I|P|,
\tag{9}
$$
并且(7)的两个误差亦由 $K\sup_I|P|$ 控制。后两项只对 $\operatorname{Pol}_{\le6}$ 使用；这是固定有限维多项式空间的范数等价，不要求 $P$ 的系数有一个独立于当前几何的预先上界。

还有一个重要的准确零次关系。令 $W=p-xr=L_c+\omega_cr$。R533 保留真余项后有 $\mathsf W_0=O(1)$，而逐函数恒等给
$$
\mathsf W_0=\mathsf A_0+2\omega_c\mathsf B_0+\omega_c^2\mathsf C_0.
$$
由于 $\mathsf B_0=-\Lambda$，故
$$
\boxed{\mathsf C_0=\frac{2\Lambda}{\omega_c}+O(1).}
\tag{10}
$$
这里只用正的 $\omega_c$；没有另指定第十四个新目标。

写
$$
Q(x)=1+\{h(x+\omega_c)+d_c\}^2,\qquad
Q_*=Q(\xi_*)=1+(h\omega_c/2+d_c)^2.
$$
在 $h>0,-3\le d_c\le1$ 上有有限常数
$$
R_Q:=\sup\frac{\max_{x\in I}Q(x)^3}{Q_*^3}<\infty .
\tag{11}
$$
例如当 $h\ge\max(1,12/\omega_c)$ 时，
$|h\omega_c/2+d_c|\ge h\omega_c/4$；分子分母的最高次数同为6，比例有固定上界。其余 $h$ 属一个有界闭区间，分母至少为1。此论证包含 $h\downarrow0$。

原完整二次型为
$$
F=z^{\mathsf T}\mathsf H(S)z+\mathsf l(S,m)^{\mathsf T}z+
\mathsf c_\nu(S,m),
$$
$$
\mathsf H=\frac1{64h^7}
\begin{pmatrix}
\mathsf A[Q^3]&\mathsf B[Q^3]\\
\mathsf B[Q^3]&\mathsf C[Q^3]
\end{pmatrix}+\mathsf E(S).
\tag{12}
$$
$\mathsf E$ 在每个最终有限合法盒上有与 $\Lambda$ 无关的界；$\mathsf H$ 不依赖 $m,\chi$。

下面先只用(7)–(11)选常数。取一个足够大的固定 $M$，例如
$M=8KR_Q+4$。由(9)(10)，存在固定
$$
0<h_{\min}<h_c/4
\tag{13}
$$
使对 $-3\le d_c\le1$，
$$
\Lambda^{-1}\mathsf C[Q^3]>1/(2\omega_c)
\quad\text{在 }h=h_{\min},
\tag{14}
$$
只需随后把 $\Lambda$ 取足够大。确切地，
$Q^3=(1+d_c^2)^3+hP_{h,d_c}(x)$，
$P_{h,d_c}$ 在 $0<h\le h_c/4$、上述 $d_c$ 区间的系数一致有界；(9)控制后一项，(10)控制首项。

置
$$
h_{\max}=h_c+4M+2,\qquad
\eta_{\max}=2h_{\max}(1+4/h_{\min}^2).
\tag{15}
$$
选一个包含
$$
h_{\min}\le h\le h_{\max},\quad
-3\le d_c\le1,\quad 0\le\eta\le\eta_{\max}
\tag{16}
$$
及其小开邻域的有限 scalar 盒 $\mathcal B$。可先用
$k=h\eta-d_c$ 给 $|k|$ 的有限上界；盒的 $\eta$ 下边取为
$-\min_I(x+\omega_c)/2$，从而整个盒仍真实合法。

现在才在这个固定盒上确定 $\mathsf E$ 的界，再把有限 $\Lambda$ 取大。R533 的完整论证给整盒上
$$
\mathsf H_{12}<0,\qquad
\det\mathsf H<0,\qquad
|\mathsf H_{11}|\le C,\quad
-\mathsf H_{12}\asymp\Lambda,\quad
|\mathsf H_{22}|\le C\Lambda .
\tag{17}
$$
同时，由(7)(9)(11)，
$$
\frac{|\mathsf H_{22}|}{-\mathsf H_{12}}\le M
\quad\text{于(16)的整个区域},
\tag{18}
$$
并由(14)得 $\mathsf H_{22}>0$ 于其下边界 $h=h_{\min}$。低阶余项在这些不等式中由已经选定盒上的有限界吸收；没有先对无界 scalar 域声称完整余项有界。

最后取 $\Lambda=L^{-6}$。所有条件都是对 $L$ 的有限上界，故可与 R536 的小 $L$ 条件一同满足。有限频率、实际正幅根和 $\chi$ 依原顺序只选择一次。

## 3. 同一个显式 null 支

为避免 R533 一般正交 frame 的方向歧义，本稿在同一盒上取如下等价显式规范。写
$$
a_H=\mathsf H_{11},\quad b_H=\mathsf H_{12}<0,\quad
c_H=\mathsf H_{22},\quad
s_H=\sqrt{b_H^2-a_Hc_H},\quad D_H=-b_H+s_H.
$$
定义
$$
b=\frac{c_H}{D_H},\qquad
\beta=\frac{a_H}{D_H},\qquad
n_+=(b,1),\quad n_-=(1,\beta).
\tag{19}
$$
因为 $a_Hc_H=-D_H(s_H+b_H)$，
$$
n_\pm^{\mathsf T}\mathsf Hn_\pm=0,\qquad
1-b\beta=\frac{2s_H}{D_H}>0,
$$
$$
\kappa_N:=n_+^{\mathsf T}\mathsf Hn_-=-\frac{2s_H^2}{D_H}<0.
\tag{20}
$$
这些准确式在 $a_H=0$ 或 $c_H=0$ 时仍有效。

完成原完整平方：
$$
z_c=-\frac12\mathsf H^{-1}\mathsf l,\qquad
\Delta=\frac14\mathsf l^{\mathsf T}\mathsf H^{-1}\mathsf l-\mathsf c_\nu.
$$
于是
$$
z=z_c+Xn_++Yn_-,\qquad F=2\kappa_NXY-\Delta.
\tag{21}
$$
固定正支 $X>0$，用一个光滑正输入 $a(s)$ 写
$$
\boxed{
z=z_c+a\,n_++\frac{\Delta}{2\kappa_Na}\,n_-,
\qquad a>0 .
}
\tag{22}
$$
这给完整 $F=0$，不是只满足其主二次部分。唯一分母 $2\kappa_Na$ 在这个支上非零；$\Delta=0$ 时也没有奇点。

由 $D_H\ge-b_H$ 及(18)，
$$
|b|\le M,\qquad
b>0\quad\text{在 }h=h_{\min},\ -3\le d_c\le1 .
\tag{23}
$$
后续使用的是这些完整母上的实际 $b(S)$，没有将它换成只看高阶主项的极限。

## 4. R536 负末态的定量余量

R536 先固定 $\varepsilon$ 和有限负保持时长，再取小 $L$，
$t_0=L^{-2},\Lambda=L^{-6}$。其完整路径累计满足
$$
\mathfrak n_L:=-\int p_1^{\omega_c}\,ds>0 .
\tag{24}
$$
末态处可把该稿的 $o(1)$ 收敛按其原估计统一收紧为 $O(L)$。原因如下：

1. $L_c$ 首系数为 $-t_0Q_c/(8h_c^2)$，真实两个 $R,T$ 偏差及高度速度相对它为 $O(L)$；
2. $\mathsf A/\Lambda$、完整低阶余式及三个 $p$ 坐标的最大误差分别为 $O(L^2),O(L^2),O(L^2)$；
3. $\mathsf B$ 的误差为 $O(\Lambda^{-1})$，未给极限的 $\mathsf C/\Lambda$ 有界而只乘趋零的小系数；
4. 原三个混合矩方程的误差为 $O(L^2)$，固定有限缩放区间上的 ODE 和实际 endpoint IFT 都有一个固定非退化界。

故在 R536 负保持段的指定末时刻，原量满足
$$
\begin{aligned}
h&=h_c+O(L),\\
k&=L^3\{K_*+O(L)\},\qquad
\eta=L^3\{E_*+O(L)\},\\
d_c&=L^3\{D_*+O(L)\},\qquad
K_*,E_*,D_*>0,
\end{aligned}
\tag{25}
$$
$$
m_{R,T}-t_0(A_c)_{R,T}=O(L^{-1}),\qquad
t_0\mathcal J_m=O(L),\qquad m_{p_j}=O(L^4).
\tag{26}
$$
$\mathcal J_m=\mathcal P_m-\omega_c\mathcal R_m$ 是 R536 的整个二次多项式。末端真实速度有 $\gamma=O(1),k_s=O(L^3)$。这些界包含负保持中的真实静态 $p$ 漂移。

这里的常数可以依赖已先固定的 $\varepsilon$ 和保持时长；不要求它们对任意长保持一致。也没有改动 R536 的实际母、一次规范或负累计。

## 5. 一个真实短下降段选择 $X>0$

不能直接在(25)处选择任意正 $a$，因为已有速度可能在另一支。本节支付这一入口。

先沿原解短延续，读其实际高度速度 $\gamma_{\rm old}$。在一个真实时长 $L^2$ 的窗口内，以同一个光滑高度输入：

- 左开邻域准确等于 $\gamma_{\rm old}$；
- 内部加入总高度变化 $-\sqrt L$ 的光滑脉冲；
- 右开邻域准确为零。

可用一个固定 cutoff 和一个积分为1的内支撑 bump 构造。整个输入满足
$$
|\gamma|\le C L^{-3/2},\qquad
h_{\rm new}=h_c-\sqrt L+O(L).
\tag{27}
$$
旧延续在这一窗口贡献的高度变化为 $O(L^2)$。左、右的开 germ 都被保留，不在一个端点生硬改变 $h_s$。

在该段仍解原 $F=0$ 的 $k_s$ 分支。以下是从原式得到的闭合估计，而非预设一条路径：

$$
\delta=O(L^{5/2}),\quad
k_s=O(L^{3/2}),\quad
\Delta k,\Delta\eta=O(L^{7/2}),\quad
\Delta d_c=O(L^{9/2}),
\tag{28}
$$
$$
\Delta m_{R,T}=O(L^{-1}),\quad
\Delta\mathcal J_m=O(L^3),\quad
\Delta m_{p_j}=O(L^5).
\tag{29}
$$

具体地，用窗口坐标 $\sigma=(s-s_e)/L^2$，并把
$\delta$ 写成 $L^{5/2}\widehat\delta$。在原主平方内，
$L_c$ 系数仍为
$$
-\frac{t_0Q_c}{8h_c^2}+O(L^{-3/2}),
$$
其相对误差只有 $O(\sqrt L)$。
$r$ 系数为 $-\mathcal J_m+Q\delta/(8h^3)$，三个原 $p$ 项仍单独保留。原 $\mathsf B$ 交叉及固定 $\nu$ 给一个对
$\widehat\delta$ 有统一非零导数的有限方程；$\mathsf A$ 项除以
$\Lambda\sqrt L$ 是 $O(L^{3/2})$，$\mathsf C$ 项更小，完整 $C^2$ 余式同样趋零。原 IFT 因而在整个固定 $\sigma$ 窗口解出有界 $\widehat\delta$，且 $F_{k_s}>0$。

式(3)立刻给(28)。对矩阵，R536 的准确式
$$
(\mathcal J_m)_s
=\frac{(a_0-\omega_ca_1)Q}{8h}
-\delta\left(\frac{\gamma Q}{8h^4}
-\frac{e e_s}{4h^3}\right)
\tag{30}
$$
给右边 $O(L)$：这里 $\delta\gamma=O(L)$，静态项为 $O(L^3)$。
积分得到(29)的混合矩界。原 $R,T$ 平方项至多
$O(\gamma^2)=O(L^{-3})$，乘窗口长度给 $O(L^{-1})$。
三个原 $p$ 列只依当前 scalar，在此为 $O(L^3)$，故其增量是 $O(L^5)$。这些同一缩放 ODE 的有界右端关闭了前述 IFT 盒，不需假设 $m$ 不动。

在右端 $\gamma=0$，使用(25)–(30)及 R536 原 Gram 向量，有
$$
\frac F\Lambda
=-\alpha b_0\sqrt L+2b_0t_0\delta+O(L),\qquad
b_0=\frac{Q_c(\xi_*)^3}{64h_c^6}>0 .
$$
因此
$$
\boxed{
\delta_{\rm new}=\frac{\alpha}{2}L^{5/2}+O(L^3)>0.
}
\tag{31}
$$
所有 $k,\eta,d_c$ 仍严格正，故这一短段的 $p_1^{\omega_c}=-kd_c$ 也严格负。它不会消耗(24)的负余量。

还必须比较完成平方的中心，不能只由 $\delta>0$ 判分支。由原主平方、(26)(29)和完整低阶余项，在这个右端有
$$
\mathsf l_\gamma=O(L^{-3}),\qquad
\mathsf l_\delta=O(\Lambda t_0).
\tag{32}
$$
前者的三个最大来源分别是 $O(t_0)$、
$O(\Lambda\mathcal J_m)$、$O(\Lambda m_p)$；
都保在(32)中。结合
$$
(\mathsf H^{-1})_{\gamma\gamma},
(\mathsf H^{-1})_{\gamma\delta}=O(\Lambda^{-1}),
\qquad
(\mathsf H^{-1})_{\delta\delta}=O(\Lambda^{-2}),
$$
得到
$$
(z_c)_\gamma=O(L^{-2}),\qquad
(z_c)_\delta=O(L^3),\qquad
\beta=O(L^6),\qquad b=O(1).
\tag{33}
$$
由(21)实际恢复的坐标是
$$
X=\frac{\delta-(z_c)_\delta-\beta\{\gamma-(z_c)_\gamma\}}
{1-b\beta}.
\tag{34}
$$
把 $\gamma=0$、(31)(33)代入，分子为
$\alpha L^{5/2}/2+O(L^3)>0$，分母由(20)严格正。因此

$$
\boxed{\text{已有的完整实际解准确进入同一个 }X>0\text{ 支。}}
\tag{35}
$$

在右侧一个短开邻域内，原解的 $a_{\rm old}(s)=X(s)$ 仍光滑为正。下文从这个真实 germ 接入(22)，而非重新选择一个不相接的速度。

## 6. 同一完整二次型的有界 null 曲线

先考虑实际母给出的几何向量场
$$
h_\tau=b(S),\qquad
k_\tau=2\{1+\eta b(S)\},\qquad
\eta_\tau=\frac{1+\eta b(S)}h .
\tag{36}
$$
这是 $n_+=(b,1)$ 对应的 scalar 方向；它暂不声称是有限 history 下的完整 ruling 解。

两条准确恒等式为
$$
\boxed{
(d_c)_\tau=-1,\qquad
\left(\frac\eta h\right)_\tau=\frac1{h^2}.
}
\tag{37}
$$
以第5节右端作为初态。此时 $h=h_c-\sqrt L+O(L)$，$\eta,d_c>0$ 且趋零。对小 $L$，到达 $d_c=-2$ 的参考时长
$$
T_*=2+d_c(0)<3
\tag{38}
$$
固定有界。

由(23)，在 $h=h_{\min}$ 时 $h_\tau>0$，所以曲线不能越过这一向内边界。又 $|h_\tau|\le M$，故在(38)的时间内
$h<h_c+3M<h_{\max}$。从(37)，
$$
0<\frac{\eta(\tau)}{h(\tau)}
\le1+\frac3{h_{\min}^2},
\tag{39}
$$
因此 $\eta<\eta_{\max}$。$d_c$ 留在 $[-2,1]$，$k=h\eta-d_c$ 亦有预定有限界，$x+\omega=x+\omega_c+\eta$ 一直为正。

由有限盒内普通 ODE 延续，(36)准确存在到(38)，不是凭 null 向量全域有定义就声称流不爆。其末态
$$
k(T_*)=h(T_*)\eta(T_*)+2
>2+\frac{2h_{\min}^2}{h_{\max}^2}.
\tag{40}
$$
这里用 $\eta/h$ 的增量至少为 $T_*/h_{\max}^2$ 及 $T_*>2$。这给一个与稍后的 shadow 误差比较的真实正余量。

## 7. 全八矩的有限正支脉冲引理

以下引理把(36)变成完整 ruling 的实际轨道。固定本稿已经选择的母、$\chi$ 和合法盒；常数允许依赖这些**有限**对象。

**引理。** 设(36)的一段有限参考曲线留在合法盒的内部。对任意给定的 scalar 误差 $\epsilon>0$ 和任意给定的真实时长上界 $\vartheta>0$，可以从第5节的真实 $X>0$ germ 出发，用有限个光滑正输入 $a(s)$ 的脉冲，在同一完整方程(22)(4)中到达距该参考末态小于 $\epsilon$ 的实际 scalar 状态，追加真实总时长小于 $\vartheta$。全过程无 history 重置；全部八矩在每一步虽可能很大，却都有限。

**证明。** $\mathsf l$ 对 $m$ 线性，$\mathsf c_\nu$ 对 $m$ 至多二次。因此在固定盒上
$$
|z_c(S,m)|\le C(1+|m|),\qquad
\left|\frac{\Delta(S,m)}{\kappa_N(S)}\right|
\le C(1+|m|^2).
\tag{41}
$$
$M_{\rm raw}$ 的准确分解为
$$
M_{\rm raw}(S,z)=M_0(S)+M_2(S,z),
\tag{42}
$$
其中 $M_2$ 对 $z$ 齐次二次；原 R73 没有速度一次项。

在一段 $a=A>0$ 的平台上，置
$$
\tau=A(s-s_j),\qquad n=m/A,\qquad \zeta=z/A .
$$
由(22)，在 $|n|\le1$ 的有限盒内
$$
\zeta=n_+(S)+O(|n|+|n|^2+A^{-1}),
\tag{43}
$$
而真实方程准确为
$$
S_\tau=\mathcal B(S)\zeta,\qquad
n_\tau=A^{-2}M_0(S)+M_2(S,\zeta),
\tag{44}
$$
其中 $\mathcal B(S)(\gamma,\delta)$ 就是(3)连同 $h_s=\gamma$ 的三维 scalar 映射。注意(44)中没有将 $m$ 设零；快速平方成本正是右边的 $M_2$。

取一个小的参考步长 $q>0$。在每一步开始，根据此前实际输出的 $m_j$，选择一个足够大的有限 $A_j$，使
$$
|m_j|/A_j\le q,\qquad A_j^{-1}\le q.
\tag{45}
$$
在 $0\le\tau\le q$ 上，(44)的有界右端和局部唯一性给
$|n(\tau)|\le Cq$。于是(43)给该步 scalar 与(36)的末点误差
$O(q^2)$。全部常数取自参考曲线的一个固定紧管。

把有限参考时间分为有限个长度至多 $q$ 的小步，普通离散 Gronwall 估计给总误差 $O(q)$。因此先将 $q$ 取足够小，再在每一步增大 $A_j$，即可使平台总误差小于 $\epsilon/2$。每一步的真实 $m$ 是上一段的完整末值；(45)只是选择下一幅度，不改变它。$A_j$ 可以迅速增长，但步骤数有限，所有选择都是有限实数。

平台之间还须平滑拼接。取已有真实延续的正 $a_{\rm old}$，在一个短开窗口内从它平滑过渡到下一正数 $A_j$，左 germ 准确相同，右 germ 准确常值。每次过渡的 $a$ 都有一个有限正下界和有限上界；在当前有限状态的小闭邻域中，约化 $(S,m)$ 向量场有界且局部 Lipschitz。因此可把过渡时长取足够短，使其 scalar 误差及 $m$ 增量任意小，且仍在同一个 $X>0$ 图中。

这一步不能只靠端点速度连续；用的是一个真正光滑的 $a(s)$。约化方程不含 $a_s$，因为原两个加速度的完整系数已由同一母消去。实际加速度及第三 history 仍由该光滑输入恢复，没有宣称其误差与 $(S,m)$ 同阶。

如果某次平滑过渡稍改了下一个平台的实际 $m_j$，先为过渡保一个有限 $m$ 邻域，再取 $A_j$ 支配这个邻域的上界；由上述短时存在选过渡长度。这给严格的逐步选择，不形成用未知实际末值定义同一段的循环。

最后，平台真实时长为 $q_j/A_j$，且 $A_j$ 可在(45)以上任意增大。所有过渡窗口亦可任意缩短。对有限步骤逐项规定其时长小于 $\vartheta/(2N)$，即可保证总时长小于 $\vartheta$。平台与过渡的总 scalar 误差同时小于 $\epsilon$。证毕。

引理只给任意一个预定有限参考弧的有限逼近。它没有给一个固定有限速度上界下的快速可控性，也没有把 $m/A$ 在一个无限长脉冲中保持小：必须按(45)有限次提高幅度。

## 8. 真正 $k>2$ 与保留净负累计

取第6节参考曲线和一个小于(40)余量一半的 $\epsilon$，同时小于其到合法盒边界的余量。第7节给一条实际全相位 ruling 路径，末 $k>2$，全部 scalar 状态合法。

原三个 $p$ 列准确为
$$
p_0=-\frac{k\{1+(h\omega-k)^2\}}{2h},\qquad
p_1=-k(h\omega-k),\qquad
p_2=-\frac{kh}{2}.
\tag{46}
$$
它们没有 $h_s^2,h_sk_s,k_s^2$。所以在所选紧盒上存在有限 $C_p$，使任意追加段满足
$$
\left\|\int_{\rm added}(p_0,p_1,p_2)\,ds\right\|
\le C_p\,|\text{真实追加时间}|,
$$
$$
\left|\int_{\rm added}p_1^{\omega_c}\,ds\right|
\le C'_p\,|\text{真实追加时间}|.
\tag{47}
$$
第5节下降段的该密度严格负。令 $\mathfrak n'_L>0$ 为加上该段后的真实负累计余量。对第7节取
$$
0<\vartheta<\frac{\mathfrak n'_L}{2(C'_p+1)}.
\tag{48}
$$
于是最终完整路径
$$
\boxed{
\int p_1^{\omega_c}\,ds<-\mathfrak n'_L/2<0,\qquad k_{\rm final}>2 .
}
\tag{49}
$$
这一估计包括所有大速度平台和所有平滑过渡，并保原前缀和快回路的完整基准。只对原 $p$ 列使用了“短真实时长使费用小”的结论。

其它五个矩不满足(47)。例如原 $t_1$ 密度含
$-\gamma^2/(8h^2)$，其累计可在快脉冲中很大。全 history 仍是实际输出，不把(49)误写成八矩成本可忽略或任意返回均可做到。

## 9. 同一 $\chi$、完整第三与有限性

本稿的最终选择顺序为：

1. 原物理窗口、共同 cap、全部复制、旧二十个值，以及(1)；
2. $\mathcal F_{\rm path}$、R533 的同点有限正列、正核和统一能量常数；
3. (11)–(16)的合法紧盒；
4. R536 的有限小 $\varepsilon$、有限负保持时长及本稿全部固定常数；
5. 一个足够小但有限的 $L$，随后 $t_0=L^{-2},\Lambda=L^{-6}$、同一个实际正幅根和有限频率；
6. 原 Gram 一次选择的 $\chi$、R536 一次实际端根；
7. 第5节实际高度下降输入，再选择有限步数、有限正脉冲幅度与光滑过渡。

第7项只选真实输入，不再修改母、旧目标、$\chi$、累计锚或初端势。

原第三式始终是
$$
T_s=-M_{\rm raw}\circ A+C(S,j^2S).
\tag{50}
$$
每段的 scalar、$m$、速度和加速度均在一个有限闭区间上光滑有限；$C$ 保原全部速度和加速度项。故(50)给真实有限 $T$。其值可以很大，过渡中也不能由约化误差估计推出它同阶小。原 frame/位置及第四场照同一 smooth 输入恢复，绝不在脉冲边界重新取右端或左端常数。

R520 的完整原函数恒等把这些真实恢复的全相位 ruling 化为当前的 $F=0$，因此(22)逐点支付的是原 $\mathscr K=0$。没有将主平方、一个 formal null 方程或某个外积分为零替代完整 ruling。

## 10. 本稿支付与下一实际门

本稿在同一 R533/R536 母、同一固定规范和同一真实前缀上，得到一条有限、全相位 ruling 恒零的路径：一个八矩坐标的全部累计严格负，同时实际曲率进入 $k>2$。核心新增是同支入口、有限合法 null 参考弧和保真实八矩的有限快速 shadow。

八矩全部为零、末端的 scalar/导数 germ、frame/pose 和真正 period 仍未支付。尤其快速段的其它矩可能很大，不能把末态 $k>2$ 当作已出现足以抵消它们的正累计。下一步必须直接研究这些实际输出之间的配平，或给另一个同规范真实返回段；本稿没有预先假设这一步可行。

独立窄核：literature 代理只核(19)(20)的两个 null、混配系数，以及(36)(37)的水平恒等与符号；未将该窄核扩大为本稿整段实际 shadow 或完整成本证明。

