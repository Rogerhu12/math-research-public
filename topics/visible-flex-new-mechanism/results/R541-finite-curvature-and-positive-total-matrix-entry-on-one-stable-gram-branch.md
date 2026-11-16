# R541：同一正交母库的一条稳定 Gram 支、有限曲率访问与正总矩累计

日期：2026-11-16。**完整原式与有限区间 ODE 的纸面证明；没有执行数值、求积、符号、profile、秩或开发检查。**

本稿在 R521 的同一个有限正交母库内，构造真实完整 $K=0$ 路径，达到 $k>2$，并使包含整个入段的原 $t_1^{\omega_c}$ 总累计严格为正。其高度、时长和几何幅度都先有限固定，再取小参数；并非在 R537 的既有小 $k$ 估计外直接延长未知轨道。

本次从真正起点另选一个固定的大第三 Gram。它与 R539 的已冻结 $\chi^\delta$ **不是同一规范**，所以本稿的正 $t_1$ 不能直接与 R539 的负 $p_1$ 拼成一个矩阵零词。所有 profiles、实际 copy、右锚与第二规范 $w=0$ 保持 R521 的同一份数据；本稿最终实际路径只使用本次一条 $\chi^\delta$。

大 Gram 的零集合有一条明确、稳定的几何支。将原快变量移到这条支上后，R537 的完整慢历史与能量证明仍适用。初始有限 Gram 补偿还给准确强准备，因此全部 scalar 及速度以 $O(\delta^2)$ 跟踪该支。高处的“常高度尾”中，实际 $k,\omega$ 仍有小而真实的变化，用来平衡增长的 $A,T$；不能把极限常态称为实际 $K=0$ 常态。

## 1. 同一母库与新的从起点固定规范

固定 R521 的全部真实 profiles、正权副本、共同右锚及物理区间 $I$。选
$$
S_c=(H,0,\omega_c),\qquad y=x+\omega_c,\qquad
H y_{\min}>1,\quad y_{\min}=\min_I y>0.
\tag{1}
$$
令
$$
c=C_k(H,0)>0,\qquad
F_c=\mathcal F(S_c,0,0,0,0).
\tag{2}
$$
$\mathcal F$ 是原完整 ruling 中无加速度、无固定第三规范的部分：
$$
\mathcal F=
R_0+R_2+L_{\rm vel}(AD)
-E(AD,AD)-4E\{\phi,T(\phi;D)\}.
\tag{3}
$$
其中 $A,T$ 是从整个本次实际词起点累计的真实二、三阶历史。

先选一个固定 $\lambda>0$，使
$$
\boxed{
H^2\left\{y_{\min}^2-\left(\frac{\lambda}{4c}\right)^2\right\}>1.
}
\tag{4}
$$
由(1)，这样的正 $\lambda$ 存在。随后对每个最终固定的小 $\delta>0$，使用 R521 的同一个合法紧支撑 Gram 右逆，一次选择
$$
\boxed{
\nu^\delta=
\left(
-\frac{H^2\lambda}{\delta^2}+2HF_c,\
\frac{2c}{\delta^2},\
\frac{\lambda}{\delta^2}
\right),
\qquad
\mathbf I_y(\phi_\theta,\chi_\theta^\delta)
=\sin^2\theta\,\nu^\delta.
}
\tag{5}
$$
它是有限、真紧、光滑、周期、保 seed 的原允许第三规范；路径中途不再改它。规范幅度可以随 $\delta\to0$ 增长，原字段和成本并未被删掉或声称统一有界。

记
$$
\eta=\omega-\omega_c,\qquad d=h\eta-k,\qquad
\gamma=h_s,\qquad \upsilon=k_s.
$$
真实水平关系为 $\eta_s=\upsilon/(2h)$。由
$$
-2\mathbf w_y(S)\cdot\nu^\delta
=-\frac{\nu_0^\delta(1+d^2)}{2h}
-d\nu_1^\delta-\frac{h\nu_2^\delta}{2},
$$
原完整 ruling 准确成为
$$
\boxed{
C_hh_{ss}+C_kk_{ss}
+\mathcal F
-\delta^{-2}\Psi(h,d)
-\frac{HF_c(1+d^2)}h=0,
}
\tag{6}
$$
其中
$$
\boxed{
\Psi(h,d)
=-\frac{H^2\lambda(1+d^2)}{2h}
+2cd+\frac{\lambda h}{2}.
}
\tag{7}
$$
(7)是整个大 Gram 的完整作用，不只保某个线性主项。

## 2. 显式稳定支与共同合法域

在 $h\ge H$ 上，$\Psi(h,d)=0$ 有唯一经过 $(H,0)$ 且取非正值的支
$$
\boxed{
q(h)=
\frac{2ch-\sqrt{4c^2h^2+H^2\lambda^2(h^2-H^2)}}
{H^2\lambda}.
}
\tag{8}
$$
它在 $h=H$ 为0，在 $h>H$ 严格负。等价的无相减表达式是
$$
\frac{q(h)}h
=-\frac{\lambda(1-H^2/h^2)}
{2c+\sqrt{4c^2+H^2\lambda^2(1-H^2/h^2)}}.
\tag{9}
$$
所以
$$
\left|\frac{q(h)}h\right|\le\frac{\lambda}{4c},
\tag{10}
$$
并且
$$
\boxed{
\Psi_d(h,q(h))
=2c-\frac{H^2\lambda q(h)}h
=\sqrt{4c^2+H^2\lambda^2(1-H^2/h^2)}
\ge2c>0.
}
\tag{11}
$$
这里稳定性指原加速度方程中正快频率的号；没有以“支连续”替代(11)。

由(4)(10)，在全部 $h\ge H$ 上，
$$
h^2y^2>1+q(h)^2,\qquad
hy+q(h)\ge h\left(y_{\min}-\frac{\lambda}{4c}\right)>0.
\tag{12}
$$
因此 R535 的 $B(h,d)>0$、R521 的 $C_k(h,d)>0$ 在该支上始终成立。
实际能量证明只使用一段随后先固定的有限 $h$ 区间，其上这些量有统一正下界。

## 3. 支上的真实水平曲线会达到有限的大 $k$

定义
$$
J(h)=-2\int_H^h\frac{q(r)}{r^3}\,dr,
$$
$$
\boxed{
k_0(h)=h^2J(h)-2q(h),\qquad
\eta_0(h)=hJ(h)-\frac{q(h)}h.
}
\tag{13}
$$
这些函数从 $k_0(H)=\eta_0(H)=0$ 开始，且对 $h>H$ 有
$$
J(h)>0,\quad k_0(h)>0,\quad\eta_0(h)>0.
\tag{14}
$$
其来源是原水平恒等式
$$
j=\frac{\eta}{h}+\frac d{h^2},\qquad
j_s=-\frac{2d h_s}{h^3}.
\tag{15}
$$
特别，(13)给的是一条真实水平几何曲线，不是只在 Gram 零平面内任意选点。直接微分可核
$$
k_0'(h)=2\{\eta_0(h)-q'(h)\},\qquad
\eta_0'(h)=\frac{k_0'(h)}{2h}.
\tag{16}
$$

取任意一个固定 $h_b>H$。对 $h\ge h_b$，
$$
J(h)\ge J(h_b)>0,\qquad
k_0(h)\ge h^2J(h_b).
$$
因此
$$
k_0(h)\longrightarrow+\infty,\qquad
k_0(h)h^2J(h)\longrightarrow+\infty.
\tag{17}
$$
可以先选择一个有限 $h_1>h_b$，使
$$
\boxed{
k_1:=k_0(h_1)>2,\qquad
\rho_1:=\frac{k_1h_1^2J(h_1)-1}{8}>0.
}
\tag{18}
$$
所有选择只依赖固定母库与已固定 $\lambda,H$，不依赖尚未选择的 $\delta$。
沿(13)，$x+\omega=y+\eta_0\ge y_{\min}>0$，连同(12)给同一完整物理窗口的合法性。

## 4. 先选高度路径、尾长与真实初值

先取一条固定 $C^\infty$ 单调高度路径 $h(s)$：

- 在一个初始开放区间上 $h=H$；
- 在固定有限的入段 $[0,T_{\rm in}]$ 内由 $H$ 上升至 $h_1$；
- 在一个末端开放区间准确为 $h_1$，随后继续恒为 $h_1$ 达固定时长 $L$。

$L$ 将在第9节按一个明确有限积分选定。总区间
$[0,T_{\rm in}+L]$ 和所需 $C^4$ 界均在 $\delta$ 之前固定。
没有把随 $\delta$ 发散的高度或时长放入证明。

在本次整个真实词的起点，取 canonical 初值
$$
\boxed{
h=H,\quad k=\eta=\gamma=\upsilon=0,\qquad
A=T=0,\qquad w=0.
}
\tag{19}
$$
初始 frame 和中心线取同一原恢复的合法初值。这里的 $A=T=0$ 是本次全字真实起点的定义，不是对一个既有非零前缀重置历史。

在初始开放区间虽规定 $h=H$，但并未规定整个 scalar 状态恒定。原完整反馈会根据正在累计的 $A,T$ 给出小而真实的 $k,\omega$ 变化。因而这不预设一个已被 R528 排除的常 scalar $K=0$ germ。

## 5. 移到稳定支后的完整快慢方程

继续用(15)，并记 $v=d_s$。原恒等式给
$$
\eta=hj-\frac dh,\qquad k=h^2j-2d,\qquad
\upsilon=2\eta\gamma-2v,
$$
$$
k_{ss}=2\eta h_{ss}+2(\eta/h)\gamma^2
-\frac{2\gamma v}{h}-2d_{ss}.
\tag{20}
$$
由 $C_h+2\eta C_k=-B(h,d)$，代入完整(6)，得
$$
d_{ss}+\frac{\Psi(h,d)}{2C_k(h,d)\delta^2}
=G_d(t,d,v,j,A,T),
\tag{21}
$$
$$
G_d=
\frac{\mathcal F-HF_c(1+d^2)/h-B(h,d)h_{ss}}
{2C_k(h,d)}
+\frac{\eta}{h}\gamma^2-\frac{\gamma v}{h}.
\tag{22}
$$

置
$$
e=d-q(h),\qquad v_e=e_s,\qquad
v=q'(h)\gamma+v_e.
\tag{23}
$$
$v_e$ 是快偏移的实标量速度；原第二 profile 规范仍始终为 $w=0$。

由 $\Psi(h,q)=0$，准确得到
$$
\boxed{
e_{ss}+\delta^{-2}\alpha(t,e)e
=G_e(t,e,v_e,Z),
}
\tag{24}
$$
其中
$$
\boxed{
\alpha(t,e)=
\frac{\Psi_d(h,q(h))-H^2\lambda e/(2h)}
{2C_k(h,q(h)+e)},
}
\tag{25}
$$
$$
G_e=G_d-q'(h)h_{ss}-q''(h)\gamma^2.
\tag{26}
$$
(25)由原二次多项式(7)逐项分解所得；在 $e=0$ 光滑，且在已固定支的一个共同小管内有
$$
0<\alpha_-\le\alpha(t,e)\le\alpha_+.
\tag{27}
$$
因此正频率不是仅在一个中心点检验的。

与 R537 相同，完整第三状态必须重写为
$$
\widetilde T=T-P_{\rm acc}(S,\gamma,\upsilon)
+\mathcal A(S)\gamma\upsilon,\qquad
Z=(j,A,\widetilde T).
\tag{28}
$$
它的真实方程是
$$
j_s=-\frac{2(q(h)+e)\gamma}{h^3},\qquad
A_s=\Phi_{M_{\rm raw}},
$$
$$
\begin{aligned}
\widetilde T_s={}&-\Phi_{M_{\rm raw}}\circ A
+\mathcal C_s^{[1]}+2\mathcal A h_{ss}\upsilon\\
&+\{(X\mathcal A)\gamma+(Y\mathcal A)\upsilon\}\gamma\upsilon
+\sum_{r=0}^3\mathcal B_r\gamma^{3-r}\upsilon^r.
\end{aligned}
\tag{29}
$$
真实 $T$ 始终由(28)恢复。原两个 $\mathcal A h_{ss}\upsilon$ 合成的因子2、全部有序复合和两端速度势都保留。

把(28)代入(22)(26)后，完整系统为
$$
e_s=v_e,\qquad
(v_e)_s=-\delta^{-2}\alpha(t,e)e+G_e(t,e,v_e,Z),
$$
$$
\boxed{Z_s=\mathcal H(t,e,v_e,Z).}
\tag{30}
$$
$\mathcal H$ 不含 $e_{ss}$ 或 $k_{ss}$，也没有 $\delta^{-2}$。
其显式时间数据只有已预给高度及有限导数；$G_e$ 仍含真实 $A,\widetilde T$。

## 6. 合法管、全部历史与有限区间能量

先在最大存在区间的初段作 bootstrap：
$$
|e|<e_*,\qquad |v_e|<1.
\tag{31}
$$
因为高度已固定，(15)(23)给
$$
j(s)-J(h(s))
=-2\int_0^s e(t)\frac{h'(t)}{h(t)^3}\,dt.
\tag{32}
$$
单调性使右边绝对值不超过 $e_*/H^2$。
因此先取 $e_*>0$ 足够小，即可使 $k,\eta$ 与(13)保持在同一个合法紧管，
原 $x+\omega$、$hy+d$ 和 $B,C_k$ 都保严格正下界。
管的大小可依赖已固定 $h_1,T$，不能借此涵盖无界几何。

由(20)(23)(31)，所有速度均有限有界。
原 $M_{\rm raw}$ 只对速度二次，所以先得到
$$
\|A(s)\|\le C_M T.
$$
再由完整(29)，其右边对 $A$ 至多一次且不依赖 $\widetilde T$ 本身，得到
$$
\|\widetilde T(s)\|\le C_T(T+T^2).
\tag{33}
$$
这两个先验界没有使用未知的 $e_{ss}$。固定严格包含它们的慢状态盒后，全部
$G_e,\mathcal H$ 及所需偏导有统一有限界。

定义
$$
f(t,Z)=G_e(t,0,0,Z),\qquad
V(t,e)=\int_0^e\alpha(t,z)z\,dz .
$$
有
$$
\alpha_-e^2/2\le V\le\alpha_+e^2/2,\qquad
|V_t|\le C e^2,
$$
且沿实际慢状态
$$
f_s=f_t+f_Z\mathcal H
$$
有界。这里 $f_t$ 读取预给的至多三阶高度导数，不冻结 $A,T$。

取足够大的固定 $C_E$，
$$
\mathscr E=\frac12v_e^2+\delta^{-2}V-fe+C_E\delta^2.
\tag{34}
$$
同 R537 的准确微分给
$$
\mathscr E_s
=v_e(G_e-f)+\delta^{-2}V_t
-(f_t+f_Z\mathcal H)e
\le C\mathscr E,
$$
并有
$$
\mathscr E\ge
\frac12v_e^2+\frac{\alpha_-}{4\delta^2}e^2+\delta^2.
$$
初值(19)给 $e=v_e=0$，所以 $\mathscr E(0)=C_E\delta^2$。
于是整个固定区间上
$$
\boxed{e=O(\delta^2),\qquad v_e=O(\delta),\qquad e_{ss}=O(1).}
\tag{35}
$$
充分小 $\delta$ 下严格改进(31)，而(33)已在有限盒内。普通 ODE 延拓准则由此覆盖整个
$[0,T_{\rm in}+L]$。没有先假定长期存在再引用其历史上界。

## 7. 初始真实强准备与 $C^1$ 跟踪

预给高度有统一有限 $C^4$ 界。由(29)(35)，完整
$\mathcal H_s$ 只额外读取有界的 $(v_e)_s$，故如 R538(14)逐项微分可得
$$
f,\quad f_s,\quad f_{ss}
$$
在实际轨道上一致有界。令
$$
\alpha_0(t)=\alpha(t,0),\qquad
D_\delta(t)=f(t,Z(t))/\alpha_0(t).
\tag{36}
$$
$D_\delta,D_\delta',D_\delta''$ 均有界。

本次初始强准备不借 R534 的另一开放固定 $d$ 段。
在真正起点，$h$ 在开放区间恒为 $H$，所以 $\gamma,h_{ss},h_{sss}=0$；
(19)的历史与速度均为0。由(22)(26)及(5)的有限补偿，准确有
$$
f(0,Z_0)=\frac{F_c-F_c}{2c}=0.
\tag{37}
$$
又有
$$
j_s(0)=0,\qquad A_s(0)=A_c,\qquad \widetilde T_s(0)=0.
$$
在零速度、$A=0$ 处，$L_{\rm vel}(AD)$ 的 $A$ 导数为0，
$E(AD,AD)$ 没有一次项，而 $T$ 的初导为0。因此完整式的总时间导数给
$$
f_s(0,Z_0)=0.
\tag{38}
$$
原常态 $A_c$ 非零，(38)没有把它删除；其可能贡献因原式对 $A$ 的一次系数在该点为0而准确消失。

置
$$
r=e-\delta^2D_\delta.
$$
由(37)(38)，有真正初值
$$
r(0)=r_s(0)=0.
\tag{39}
$$
Taylor 展开完整(24)，如 R538 一样给
$$
r_{ss}-b(t)r_s+\delta^{-2}\alpha_0(t)r=O(\delta^2),
\qquad b=G_{e,v_e}(t,0,0,Z).
$$
其能量
$r_s^2/2+\alpha_0r^2/(2\delta^2)$ 给
$$
\boxed{
r=O(\delta^3),\quad r_s=O(\delta^2),\quad
e=\delta^2D_\delta+O(\delta^3),\quad e_s=O(\delta^2).
}
\tag{40}
$$
不需要估计未付的快高导数。

由(32)(40)，实际 scalar 与(13)准确满足
$$
\boxed{
d^\delta=q(h)+O(\delta^2),\quad
j^\delta=J(h)+O(\delta^2),\quad
k^\delta=k_0(h)+O(\delta^2),\quad
\eta^\delta=\eta_0(h)+O(\delta^2).
}
\tag{41}
$$
速度也以 $O(\delta^2)$ 一致接近相应真水平曲线的速度。
完整慢系统的有限区间连续依赖进一步给
$$
A^\delta=A_0+O(\delta^2),\qquad
\widetilde T^\delta=\widetilde T_0+O(\delta^2),
\qquad T^\delta=T_0+O(\delta^2).
\tag{42}
$$
其中 $A_0,T_0$ 是该极限几何的完整原 canonical 历史，绝非0。
原全部八矩密度只依赖 scalar 和速度，因此也一致收敛，误差为 $O(\delta^2)$。

## 8. 达到 $k>2$，但实际尾段不是常 scalar

由(18)(41)，充分小 $\delta$ 时，在整个末端常高度尾上
$$
k^\delta>2
$$
并保同一完整合法窗口。实际路径从 $k(0)=0$ 连续到达这一有限值，不需要另一条无 ruling 桥或 signed 拼接。

末端 $h=h_1$ 准确恒定，极限 $q,J,k_0,\eta_0$ 也恒定；
但实际
$$
d^\delta=q(h_1)+O(\delta^2),\qquad
k^\delta=k_1+O(\delta^2)
$$
仍按完整(30)变化。随着 $A^\delta,T^\delta$ 继续累计，(36)(40)的微小偏移正是平衡它们在原(6)中作用的真实响应。

因此本稿没有在常 scalar 背景上删除随时间增长的二次第四项。R528 的常态障碍不被违反：这里得到的是一族在 $\delta\to0$ 时趋近常态的**非恒真实解**，同时规范幅度按(5)增长。原 $A,T$、第三恢复及第四成本均在同一个有限词内保留。

若另外先把 $h_1$ 取大到
$k_1\min_I(h_1y+q(h_1))>1$，则极限末端也属于 R528 的无极点域；
该文反而确认实际解不能在一个开放尾段变成全部 scalar 皆恒的 $K=0$ 解。本稿不需要这条额外选择来证明可达性。

## 9. 有限尾长支付原总 $t_1>0$

本节及第10节的 $M_{t_1},M_{p_1}$ 均在固定 $y=x+\omega_c$ 坐标读取，即原八矩的固定线性读出 $t_1^{\omega_c},p_1^{\omega_c}$；没有沿路径移动中心，亦不与未平移的原 $t_1$ 混记。

原 R73/R524 的准确几何式是
$$
8M_{t_1}
=2kh\eta-k^2-1-(h_s/h)^2.
\tag{43}
$$
在极限支(13)上，$h\eta_0=k_0+q$，所以
$$
\boxed{
8M_{t_1}^{0}
=k_0(h)h^2J(h)-1-(h_s/h)^2.
}
\tag{44}
$$
在入段上，(44)是已经固定的连续函数，故
$$
C_{\rm in}:=\int_0^{T_{\rm in}}|M_{t_1}^{0}(s)|\,ds<\infty.
$$
在常高度尾上，(18)(44)给准确常值
$$
M_{t_1}^{0}=\rho_1>0.
$$
先选一个固定有限的
$$
\boxed{L>(C_{\rm in}+1)/\rho_1.}
\tag{45}
$$
于是这整条极限几何的真实矩积分大于1。
第4–7节对这个先固定的 $h_1,L$ 适用；最后取充分小 $\delta$。
由全部密度的一致收敛，
$$
\boxed{
\int_0^{T_{\rm in}+L}M_{t_1}^{\delta}(s)\,ds>0.
}
\tag{46}
$$
这是包括全部入段的净累计，不只是某一点的正密度。
整个实际区间逐点满足同一原完整 $\mathscr K(s,\theta)=0$。

该选择顺序不能反过来：本稿没有在已经冻结的 $\delta$ 后任意增加无界尾长，也没有宣称其全部第四成本与 $\delta$ 一致有界。

## 10. 原其它矩与没有支付的闭合

在本稿单调支上，$q(h)<0,k_0(h)>0$ 于 $h>H$。
因此原另两个矩有明确极限号：
$$
M_{p_1}^{0}=-k_0q>0,\qquad
M_{p_2}^{0}=-k_0h/2<0
\tag{47}
$$
于非平凡入段及整个高尾上。相应实际总积分在充分小 $\delta$ 时保号。
故(46)并不等于一个矩阵零块，尤其不能将其与 R539 的另一固定规范下的负
$p_1$ 视为可直接拼接的两条实际控制段。

本稿完整保留全部八矩、$A,T$、frame、中心线、第四字段及其成本。
末端 scalar germs 是真实反馈输出；仅高度平坦并不意味着原反射所需的全部偶 germs 或端口条件。frame/位置返回、第三和第四 period、同一十三规范以及最终 fixed-metric 的完整目标都没有由(46)自动得到。

新的已付可达性是准确的：同一 R521 母库，允许从起点一次选择(5)后，存在真实完整
$K=0$ 路径达到 $k>2$，并有净正 $t_1^{\omega_c}$。这解除的是该原矩在此前近
$k=0$ 跟踪族中的固定负号；同一新规范下的其它矩配平仍须继续真实构造。

### 原来源

- [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)：完整矩密度与有序第三累计；
- [R77](R77-weight-three-local-operator-actual-finite-controllability.md)(2)、[R79](R79-closed-horizontal-C1-control-and-endpoint-potential.md)：完整速度势及导数权结构；
- [R482](R482-pointwise-third-memory-elimination-and-constrained-prototype-ruling-system.md)：未消历史的完整第四 ruling；
- [R521](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md)：唯一母库、固定 Gram、正加速度行及全部相位；
- [R524](R524-same-gauge-constant-return-gates-and-real-matrix-excursion-obstructions.md)：原矩的几何必要门；本稿实际使用的(43)也直接来自 R73；
- [R528](R528-positive-orthogonal-library-and-strict-pole-free-constant-state-obstruction.md)：真实常态与近常态极限的边界；
- [R537](R537-prescribed-finite-height-paths-with-one-gauge-and-complete-history-energy-bounds.md)、[R538](R538-complete-fourth-order-matrix-functional-for-prescribed-height-paths.md)：完整慢状态、修改能量及强准备方法；本稿已重新支付非零中心支和本次真实初值。

全稿没有新科学执行，也没有把两份不同规范的存在结果拼成一条闭路径。
