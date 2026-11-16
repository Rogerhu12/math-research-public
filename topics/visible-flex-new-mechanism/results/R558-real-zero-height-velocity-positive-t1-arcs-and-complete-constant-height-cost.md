# R558：同一固定规范的真实零高度速度正弧与恒高度累计障碍

日期：2026-11-16。**完整原式纸面证明；没有执行数值、符号、profile、旧秩、测试或新的科学任务。**

本稿继续 R533/R540/R554 的同一三十三行母和一次固定的 $\chi$。
新增的是一个真实的速度接入：在已经实际到达的高曲率区，通过原正 $X$ 矩脉冲和同一个 conic 正则支，能够平滑进入
$$
h_s\equiv0,\qquad t_1(s)>0
$$
的一个开放区间。它给严格正的真实 $t_1$ 增量，不只是形式上把
$\gamma$ 设零或在一个未到达的状态观察密度。

与此同时，整段原矩有一个准确的成本关系。若在这个恒高度区间内最终把 $p_2$ 累计恢复到入端值，则
$$
\Delta m_{t_1}=-\frac18\,|\text{该段真实时间}|<0.
$$
因此新的正密度区间不能单靠延长，既支付原负 $t_1$ 又保已经清掉的
$p_2$。这是一条关于同一真实分支全部累计的结论，不排除后继改变高度的真实控制。

母、原二十数值、四自然约束、共同 cap、完整低阶纤维、右锚与第二规范不改；原 $m,T$、frame 和位置始终按真实方程恢复。本稿不拼入 R521 的另一母库或另一份 Gram，也不宣八矩、末 germ、pose 或原 period 已闭合。

来源：
[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、
[R520](R520-variable-mother-constant-ruling-and-same-gauge-nonconstant-local-departure.md)、
[R533](R533-complete-velocity-quadratic-form-and-all-history-regular-ruling-coordinates.md)、
[R536](R536-real-negative-total-matrix-density-from-a-complete-fast-height-loop.md)、
[R540](R540-same-positive-null-branch-and-real-large-curvature-with-negative-total-matrix-density.md)、
[R546](R546-real-quadratic-matrix-pulses-and-an-exact-same-gauge-zero-coordinate.md)、
[R547](R547-complete-joint-matrix-cost-and-the-real-return-layer-after-large-curvature.md)、
[R551](R551-real-negative-delta-entry-on-the-same-thirty-three-mother-and-fixed-gauge.md)、
[R553](R553-complete-real-return-to-the-centered-zero-layer-with-one-fixed-gauge.md)、
[R554](R554-two-real-holds-and-exact-joint-p1-p2-control-with-one-fixed-gauge.md)。

## 1. 同一个原实际入端

仍写
$$
\eta=\omega-\omega_c,\quad d_c=h\eta-k,\quad
\gamma=h_s,\quad \delta=k_s/2-\eta\gamma,
$$
$$
k_s=2(\delta+\eta\gamma),\qquad
\eta_s=\frac{\delta+\eta\gamma}{h},\qquad (d_c)_s=-\delta .
\tag{1}
$$
$\omega_c>0$，物理合法性仍是 $h>0$、
$x+\omega>0$；不增加另一母的强窗口假设。

按 R551/R553 的原初选细分，可以在同一个真实前缀上实际到达
$$
k_*>2,\qquad -\frac12<d_{c,*}<0,\qquad
0<h_*\ll1,\qquad X_*>0,
$$
$$
|d_{c,*}|\le D h_*,\qquad W_+(S_*,\xi_*)>0.
\tag{2}
$$
所有号都有严格余量；$D$ 是先固定的有限常数。
这来自原正 $X$ 弧在一个小参考时刻的实际 shadow，不是将某个任意 R553 末历史假定为(2)。

在该状态，原零高度速度的静态密度满足
$$
8t_1^{\rm stat}
=k^2+2kd_c+2h\omega_ck-1
>k^2-k-1>0.
\tag{3}
$$
(3)尚不支付 $\gamma=0$，以下正是其真实接入证明。
完整 $k,\omega$ 可以很大但有限；先把所需全部状态放入一个合法紧盒，再完成同一母、有限 $\Lambda$ 和一次 $\chi$ 的选择。

若使用 R554 两保持族，(2)可在一个固定正时长紧盒上共同实现。
母和 $\chi$ 在该族中仍是同一份，变化的只是两个实际保持时长及已付的端 mean 校正。

## 2. 完整源及两个真实 null 方向

原完整 scalar ruling 为
$$
F(S,m,z)=z^{\mathsf T}H(S)z+l(S,m)^{\mathsf T}z
+q_S(m)+c_{\nu,0}(S),\qquad z=(\gamma,\delta),
\tag{4}
$$
其中 $m_s=M_0(S)+N(S,z)$，$N$ 对速度齐次二次。
$l$ 对 $m$ 线性，$q$ 对 $m$ 二次。所有 complete 低阶项、初端商势、
Green 项和原左尾都在(4)内；真实第三没有被归零。

在同一个小高度带，R533/R551 给
$$
H_{11}=O(1),\quad
H_{12}=-\frac{\Lambda Q_*^3}{64h^7}+O(1),\quad
-\det H>0,
$$
$$
b=\frac{H_{22}}{-H_{12}+\sqrt{H_{12}^2-H_{11}H_{22}}}
=\frac1{\omega_c}+O(h^2)+o_\Lambda(1)>0.
\tag{5}
$$
取 R540 的原显式 null frame
$$
n_+=(b,1),\qquad n_-=(1,\beta),\qquad
\kappa_N=n_+^{\mathsf T}Hn_-<0 .
$$
由 $n_+^{\mathsf T}Hn_+=0$，有准确关系
$$
H_{22}=-2bH_{12}-b^2H_{11}>0,
$$
$$
(Hn_+)_\delta=-b(Hn_+)_\gamma
=-b(H_{11}b+H_{12})>0.
\tag{6}
$$
最后的号由(5)及有限大 $\Lambda$ 支付，不是假定任意不定矩阵均有此号。

完成平方仍是同一个完整式
$$
z_c=-\frac12H^{-1}l,\qquad
\Delta=\frac14l^{\mathsf T}H^{-1}l-q_S(m)-c_{\nu,0}(S),
$$
$$
z=z_c+Xn_++Yn_-,\qquad
F=2\kappa_NXY-\Delta .
\tag{7}
$$

## 3. R553 完整比较延伸到两个速度变量

令
$$
N_+(S)=N(S,n_+(S)).
$$
它是原八矩的真实二次方向，$p_j(N_+)=0$。R546/R551 的准确多项式为
$$
\frac{\alpha_{N_+}}2=W(S,x)(bL_c+r),
$$
$$
W(S,x)=
\frac{b(1+d_c^2-h^2y^2)+2h(hy+d_c)}{8h^4},
\quad y=x+\omega_c.
\tag{8}
$$
置
$$
Q=1+(hy+d_c)^2,\quad Q_*=Q(S,\xi_*),\quad
\sigma(S)=\frac{8h^3W(S,\xi_*)}{Q_*}>0.
$$
在 $|d_c|\le Dh$ 的薄带内，
$$
W(S,x)=\frac{Q(S,x)}{8h^3}\sigma(S)+E_W(S,x),
\quad |E_W|\le Ch^{-2},\quad \sigma\asymp h^{-1}.
\tag{9}
$$

记 $F_2=z^{\mathsf T}Hz+l(S,m)^{\mathsf T}z+q_S(m)$。
R553 已保全原 principal 和低阶余项。本稿不只取其
$\widehat\delta=-1/4$ 截面，而在任意先固定的有界
$(\widehat\gamma,\widehat\delta)$ 盒中用同一原代入：
$$
\begin{aligned}
\frac{\alpha_{N_+}}2+
\frac{Q\sigma(\widehat\gamma L_c+\widehat\delta r)}{8h^3}
={}&\frac{Q\sigma}{8h^3}
\{(\widehat z+n_+)\cdot(L_c,r)\}\\
&+E_W(bL_c+r).
\end{aligned}
\tag{10}
$$
令 $\mathfrak h=\Lambda/(64h^7)$。由(10)的交叉项及余平方项，
$$
\boxed{
\frac{F_2(S,N_+,\sigma\widehat z)}{\sigma^2\mathfrak h}
=(\widehat z+n_+)^{\mathsf T}
\frac{H}{\mathfrak h}(\widehat z+n_+)
+\mathcal E(S,\widehat z),
}
\tag{11}
$$
$$
|\mathcal E|+|D_{\widehat z}\mathcal E|
\le C h^2+o_\Lambda(1).
\tag{12}
$$
这是对两速度的完整一次导数界。R553 原交叉项是
$O(\Lambda h^{-7})$，余平方为 $O(\Lambda h^{-5})$；
除以 $\sigma^2\mathfrak h\asymp\Lambda h^{-9}$ 分别给
$O(h^2),O(h^4)$。对任一速度求导只是去掉一个线性因子，所以相同界继续成立。全部 complete $C^2$ 余式在固定正高度下界和有限 scalar 盒上有界，最终再选有限 $\Lambda$ 把其归一值及导数压入最小高度平方以内。

因此(11)不是把 $q_S(N_+)$ 删去，也不由 $N_+^2=0$ 声称其 profile 算子平方为零。$q_S(N_+)$ 的完整值正是下一根中决定 $\delta$ 号的量之一。

## 4. 同一右投影支中的真实 $\gamma=0$ 根

在(11)的 $\widehat z=0$ 处，平移主项为零。由(6)，它对
$\widehat\delta$ 的导数为
$$
\frac{2(Hn_+)_\delta}{\mathfrak h}
=-\frac{2b(H_{11}b+H_{12})}{\mathfrak h}
=2bQ_*^3+o_\Lambda(1)>0.
\tag{13}
$$
其对 $\widehat\gamma$ 的导数则为
$$
\frac{2(Hn_+)_\gamma}{\mathfrak h}
=-2Q_*^3+o_\Lambda(1)<0.
\tag{14}
$$
薄带先取小，完整低项随后用有限 $\Lambda$ 控制。定量 IFT 于是给唯一小根
$$
F_2(S,N_+,\sigma(0,v_0(S)))=0,\qquad
\boxed{v_0(S)=O(h^2),}
\tag{15}
$$
并且该根的完整 $F_\delta>0,F_\gamma<0$。
没有给 $v_0$ 预先指定正负号。

现在从(2)的实际 $X>0$ germ 出发，使用 R546/R551 的真实平台：
先固定有限 $\tau$，再取有限大 $B$，平台真时长为 $\tau/B^2$。
完整恢复给
$$
S_B\to S_*,\qquad
m_B\to m_*+\tau N_+(S_*).
\tag{16}
$$
所有 ramps 先固定幅度、后取短真实时间，保原左 germ 和全部入值。

随后作为存在性选择令 $\tau$ 足够大，并取 $B=B(\tau)$ 更大，使
$$
S_{\tau,0}\to S_*,
\qquad m_{\tau,0}/\tau\to N_+(S_*).
\tag{17}
$$
每个最终选择仍是一个有限词。将原 $F$ 除以 $\tau^2$，
固定 $\chi$ 的完整项成为 $\tau^{-2}c_{\nu,0}$；它趋零仅用于证明存在，并在每个有限根中保留。

由(13)–(17)，真实末状态的原二次式
$F(S,m,0,\delta)$ 有一个根
$$
\delta=d_0(S,m),\qquad
\frac{d_0}{\tau\sigma}=v_0(S_*)+o(1),
\tag{18}
$$
其 $F_\delta>0,F_\gamma<0$。在其小开邻域中，可明确写成
$$
\boxed{
d_0=\frac{-l_\delta+
\sqrt{l_\delta^2-4H_{22}c_\nu}}{2H_{22}}
=-\frac{2c_\nu}
 {l_\delta+\sqrt{l_\delta^2-4H_{22}c_\nu}},
}
\tag{19}
$$
其中 $c_\nu=q_S(m)+c_{\nu,0}(S)$。这里
$H_{22}>0,l_\delta>0$，判别式严格正，全部量都是当前真实历史的值。

该根和原平台在同一个可达支上。R551 的完整中心及投影界给
$$
(z_c)_\delta/\tau=-\sigma+o(1)+O(\Lambda^{-1}),\qquad
r_\delta/\tau\le C/\sqrt\Lambda+o(1).
$$
由(18)及 $v_0=O(h^2)$，取上述有限参数后有
$$
d_0>(z_c)_\delta+r_\delta+c_*\tau\sigma
\tag{20}
$$
的一个严格正余量。平台原大正 $\delta$ 也在这个右投影区域。
其中通过实际平台的根满足 $F_\gamma<0$；(14)保证(18)是同一根，而不是另一条 conic 分支的形式速度。

## 5. 真平滑进入 $h_s=0$ 的开放 germ

不能直接在平台末把高度速度改成零。沿平台原解短延续，读其
$\delta_{\rm old}(s)$。取左开集为1、右开集为0的固定 smooth cutoff
$\vartheta(s)$，指定状态依赖的原控制
$$
\delta_{\rm in}(s,S,m)
=\vartheta(s)\delta_{\rm old}(s)
 +(1-\vartheta(s))d_0(S,m).
\tag{21}
$$
在(20)连接两个端值的紧正则弧上，用原 $F_\gamma<0$ 根解
$\gamma$，同时积分全部 $(S,m)$。最终幅度已经有限，故把切换窗取得足够短，就使整个实际状态留在此统一正则邻域。

左开集上(21)就是原控制，唯一性保完整入 germ。
右开集上 $\delta=d_0(S,m)$，而同支的唯一根准确为 $\gamma=0$。
所以右端真正得到
$$
\boxed{h_s=0\quad\text{在一个开邻域内}.}
\tag{22}
$$
加速度和第三 history 由这条真实 smooth 输入恢复，不只匹配速度值。
整个过程中不改 $\chi$，不重置 $m,T$，不使用无 ruling 桥。

式(19)同时保留一个关键未定号：
$$
\boxed{\operatorname{sgn}d_0=-\operatorname{sgn}c_\nu(S,m).}
\tag{23}
$$
因此(22)不授予 $\delta<0$，也不授予 $d_c$ 必然继续增加。
完整 $q_S(m)$ 和固定初端势不能为取得有利方向而省去。

## 6. 一个真实正 $t_1$ 区间及其严格增量

记(22)右侧入态为 $(S_{\tau,0},m_{\tau,0})$。用
$$
u=\tau(s-s_0),\qquad n=m/\tau,\qquad
\delta=\tau v,\qquad \gamma=0.
$$
同一个原方程准确成为
$$
H_{22}(S)v^2+l_\delta(S,n)v+q_S(n)
+\tau^{-2}c_{\nu,0}(S)=0.
\tag{24}
$$
其关于 $v$ 的导数在入端有共同非零下界。因此在先固定的小管内，
$v=V(S,n,\tau^{-2})$ 是同一真实根，原系统是
$$
\boxed{
h_u=0,\quad k_u=2V,\quad \eta_u=V/h,\qquad
n_u=N(S,0,V)+\tau^{-2}M_0(S).
}
\tag{25}
$$
这是全部八矩的方程，不是冻结 $n=N_+$。入值可通过(16)(21)
取得(17)的同一极限。

普通 ODE 连续依赖给一个 $u_0>0$，对所有最终充分大而有限的
$\tau$，实际路径存在于 $0\le u\le u_0$。缩小 $u_0$ 可使它留在
(3)的严格正邻域及原合法窗口，故有固定 $c_1,C_1>0$：
$$
c_1\le t_1(S(u),0)\le C_1 .
$$
因而新增真实积分满足
$$
\boxed{
0<\frac{c_1u_0}{\tau}
\le\Delta m_{t_1}^{\rm zero\text{-}height}
\le\frac{C_1u_0}{\tau}.
}
\tag{26}
$$
三个原 $p$ 列在同一管内有界，所以该段的 $p$ 增量为
$O(\tau^{-1})$。$u_0$ 是固定快时间长度，不是一个已付的固定正原时间驻留，也不将局部存在扩成任意长流。

整个区间的高度准确为其实际入值 $H>0$；它不是把某个输出硬改为
$h_c$。其余 scalar 和历史仍按(25)变化。原
$$
T_s=-M_{\rm raw}\circ\Phi_m+C(S,j^2S)
\tag{27}
$$
包含所有真实速度、加速度和累积项；每个最终参数有限，故 $T$、
frame 和位置均真实恢复。没有从(25)的收敛给第三添加同阶小误差。

## 7. 准备阶段的负费用没有被正区间抵消

R546 原二次速度矩给
$$
N_{t_1}(S,n_+)=-\frac{b^2}{8h^2}<0.
$$
在(16)的实际正 $X$ 平台上，依原顺序先选有限 $\tau$、再选
$B$，可使完整费用满足
$$
\Delta m_{t_1}^{\rm prep}
=-\tau\,\frac{b_*^2}{8h_*^2}+o(\tau).
\tag{28}
$$
这里 static 项和所有 ramps 都保留；ramp 的幅度先固定，其窗口再缩短，可将其积分误差控制为 $o(\tau)$。不把它的第三代价说成小。

新的正弧只给(26)的 $O(\tau^{-1})$ 正值。所以本次制备加该固定
$u_0$ 弧的完整 $t_1$ 费用，在足够大的实际 $\tau$ 上仍严格负。
此前长常态前缀 $-t_0/8$ 以及其它已累计费用也没有被删除。

因此本稿支付的是**真实正增量区的可达性**，不是净 $t_1\ge0$。
更大的驻留时间必须由原(24)(25)证明；不能用(26)中的局部存在自行取得。

## 8. 可以同时保原两个累计目标

这一段使用的是 R554 已付的同一两时长族。先固定一个正时长紧盒，
连同(2)及全部严格裕量；新的准备、切换、根(19)和有限 $u_0$ 段可在这个盒上共同选择。

正 $X$ 平台的幅度同时支配入 $m$ 和其两参数一阶导数。R554 §9 的原缩放 ODE 及变分方程给共同 $C^1$ 收敛。根(19)及切换(21)
均在同一个严格非退化开管内，故(24)(25)的参数导数亦有共同界。
所有原 $p$ 列没有速度平方。先固定 $L$，再选这些有限大幅和共同短 ramp，遂可把新增 $p$ 端费用在 $C^1$ 上压到任意指定小量。

将整个新后继**先放入**原两时长端映射，再使用其已经明确的非零雅可比
$$
AB(\delta_2-3\delta_1)\ne0
$$
作同一次有限 IFT。因此可从原零历史起点，使用同一份33母和
$\chi$，准确达到下列两种端口之一：

- 在(22)的真正零高度速度入 germ 上有
$$
m_{p_2}=0,\qquad \Pi:=m_{p_1}-2\omega_cm_{p_2}<0 ;
\tag{29}
$$
- 或在(26)的某个正增量区间末端，仍准确有(29)。

这只改变原起点预定的保持时长，不在已经冻结的 R553 末历史上重新选母或规范。两种选择不是在同一路径上都声称 $p_2$ 不变：
正弧起始 $k>0$，所以这段真实 $p_2$ 密度为负；若指定末端为零，
其入端必须保有对应的正累计基准。

## 9. 整个恒高度继续的三个准确矩关系

现在不再使用大 $\tau$ 近似。对任何实际存在的、始终满足
$\gamma=0$ 的有限继续，令其真实常高度为 $H$。由(1)准确有
$$
\zeta:=k+2d_c=\text{常数},\qquad
Z_{\rm raw}:=\zeta+2H\omega_c=2H\omega-k=\text{常数}.
\tag{30}
$$
三个原密度逐点为
$$
p_2=-\frac{Hk}{2},\qquad
\pi:=p_1-2\omega_cp_2=\frac{k^2-\zeta k}{2},
\qquad
t_1=\frac{Z_{\rm raw}k-1}{8}.
\tag{31}
$$
故完整恒等式是
$$
\boxed{
\pi-\frac{\zeta}{H}p_2=\frac{k^2}{2},
\qquad
8t_1+\frac{2Z_{\rm raw}}H p_2=-1.
}
\tag{32}
$$
它们使用固定的原 $\omega_c$；没有中途平移八矩坐标以改变符号。

设继续的真实时长为 $T>0$，对同一整段积分：
$$
\boxed{
\Delta\Pi-\frac{\zeta}{H}\Delta m_{p_2}
=\frac12\int k^2\,ds\ge0,
}
\tag{33}
$$
$$
\boxed{
8\Delta m_{t_1}
+\frac{2Z_{\rm raw}}H\Delta m_{p_2}
=-T .
}
\tag{34}
$$
全部入前缀仍作为累计初值保留，(33)(34)只描述真实新增量。

尤其若使用(29)的零 $p_2$ 入端，并要求本恒高度继续末端仍有
$m_{p_2}=0$，则
$$
\boxed{
\Delta m_{t_1}=-T/8<0,\qquad
\Delta\Pi=\frac12\int k^2\,ds\ge0.
}
\tag{35}
$$
这对该继续无论多长、无论 $k$ 是否换号都成立。它不先假设长时间存在；
对每条实际存在的有限继续，结论都准确。因此单靠这个恒高度分支不可能在保已清 $p_2$ 的同时修复负 $t_1$。

在本稿初始正区，$Z_{\rm raw}>0$。由(34)，要取得一个正的
$t_1$ 新增量，必须花费严格负的 $p_2$：
$$
-\Delta m_{p_2}
=\frac{H}{2Z_{\rm raw}}\{8\Delta m_{t_1}+T\}.
\tag{36}
$$
这笔真实矩费用不能在后续端点只写 $p_2=0$ 而不支付。

若不先把入端 $p_2$ 清零，R554 固定有限保持盒及本稿快后继可使
$m_{p_2,\rm in}=O(L^4)$，而完整
$m_{t_1,\rm in}\le-L^{-2}/16$。若仍由一个恒高度继续把末
$p_2$ 清零，(34)给
$$
m_{t_1,\rm out}
\le-\frac{L^{-2}}{16}+C L^4-\frac T8<0
\tag{37}
$$
对足够小的同一个有限 $L$ 成立。常数使用初选有限 scalar 盒；
$Z_{\rm raw}/H$ 在入端有限且共同有界。未来 $k$ 的大小不进入该常数，
因为(30)本来就是准确不变量。

## 10. 真实方向仍由 source 决定，下一控制必须付什么

在恒高度分支上，
$$
(d_c)_s=-d_0(S,m).
$$
其号由(19)(23)中的完整 $c_\nu(S,m)$ 决定。本稿不能用“希望
$d_c$ 进入正区”来选择另一二次根。当前(2)处 $d_c<0$，所以
$\pi=-kd_c>0$；虽有正 $t_1$，其初始 $\Pi$ 费用也为正。

纯几何上，若 $\zeta>0$ 并实际将 $k$ 降入
$$
1/Z_{\rm raw}<k<\zeta,
$$
才会在这个常高度上同时有 $t_1>0$、$\pi<0$。但这需要同一真实根的
$\delta$ 方向与持续性；它不由(15)的小根存在、也不由全 history
速度图正则自动推出。即使到达，该段仍受整条(34)的 $p_2$ 成本约束。

本稿完成了此前没有的真实正 $t_1$ 开放段，并准确判明“停留更久即可修复”的单高度路径为什么不足。下一步必须在同一个完整历史上加入真正改变 $Z_{\rm raw}/H$ 的高度段，或给另一条已实际接入的控制，同时支付新增的 $p_2,\Pi,t_1$ 及其它原矩。其余六矩、末 germ、第三 period、pose 和主机制仍未闭合。

本文只消费已有完整源和已付矩脉冲；对(11)的两速度扩展、实际根和全部累计关系均给原式推导，没有进行科学执行。
