# R536：同一三十三行母库上从真实常态前缀到严格负累计 $p_1$ 的完整快回路

日期：2026-11-16。**原式纸面证明；没有执行求积、符号程序、profile 或矩阵秩计算、开发检查及新的科学运行。**

本稿继续 R533 的同一类初选母库和 R531 的一次固定第三规范。它支付的是一个此前没有支付的正向结论：从真实零 history 的常态入段出发，沿完整 $\mathscr K(s,\theta)=0$ 的同一有限路径，可以使一个实际八矩坐标的**全部累计值严格为负**。这个坐标是在固定中心 $\omega_c$ 下的
$$
p_1^{\omega_c}=p_1-2\omega_c p_2
=-k\{h(\omega-\omega_c)-k\}.
\tag{1}
$$
真实长常态前缀对(1)为零；短高度回路的正代价和切换代价全部计入。负号不再只是某时刻的负密度。

核心是完整混合速度记忆的一个可积快极限。不能单独用 R531 的负端密度除以前缀代价：高度速度的平方和交叉会产生真实八矩变化。本稿将这些变化一并缩放，证明高度闭回路把三个关键混合记忆在极限中准确送回零。随后负密度保持系统的同一二速度雅可比非零，其极限解为静止的 scalar 状态，从而任意**预先固定、有限**的保持时长都可支付。

这不是 $M=0$、末常态 germ、frame/pose 返回或完整第四 period 的构造。其余七个矩以及第三历史、位姿和成本都是同一路径的实际输出，没有重置。也不宣称某份先前已经冻结的母不作初选即可满足本稿新的尺度选择。

主要原源：[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md) 的点态八矩；[R520](R520-variable-mother-constant-ruling-and-same-gauge-nonconstant-local-departure.md) 的完整全相位缩减和主平方；[R531](R531-real-negative-p1-segments-in-the-three-zero-library-with-one-fixed-gauge.md) 的 Gram 规范及平滑保持切换；[R533](R533-complete-velocity-quadratic-form-and-all-history-regular-ruling-coordinates.md) 的三十三行实际正根、完整 $C^2$ 余项、能量上界和全 history 速度二次式。

## 1. 初选、有限尺度和不改变的原目标

固定 R533 的真实物理区间、共同右锚、共同 cap、宽度、原有理保护芽和全部正复制，取
$$
S_c=(h_c,0,\omega_c),\qquad h_c>0,\quad \omega_c\ne0,
\qquad x+\omega_c>0\quad(x\in I).
\tag{2}
$$
先固定一个合法 scalar 紧盒，含 $h_c$ 的小高度邻域和 $k=0,\omega=\omega_c$ 的邻域。后文所有路径留在这个盒内。

取 $0<L<1$，最终只取一个足够小的有限 $L$，并规定
$$
t_0=L^{-2},\qquad \Lambda=L^{-6}.
\tag{3}
$$
按 R533 的完整有限正根选一次实际母。其旧二十个数值目标原样保留；新增十三目标仍是该稿原目标，不增加 profile 行，也不缩放整个圆。该稿的正幅盒和有限频率选择给
$$
\begin{aligned}
\mathsf A[P]&=O(1),\\
\mathsf B[P]&=-\Lambda P(\xi_*)+O(1),\qquad \xi_*=-\omega_c/2,\\
|\mathsf C[P]|&\le C(1+\Lambda),\qquad \deg P\le6,
\end{aligned}
\tag{4}
$$
其中
$$
\mathsf A[P]=\sum_i\lambda_i\int P L_c^2t_i^2,\quad
\mathsf B[P]=\sum_i\lambda_i\int P L_cr_it_i^2,\quad
\mathsf C[P]=\sum_i\lambda_i\int P r_i^2t_i^2,
$$
$L_c=u_i'-(x+\omega_c)u_i''$，$r_i=u_i''$，$t_i=u_i'''$。所有几何系数及其有限阶 scalar 导数在所选盒中一致有界。

同时，R533 保证所有 complete $C^2$ 系数一致有界，及
$$
\sum_i\|u_i'''\|_2^2\le C(1+\Lambda).
\tag{5}
$$
这些是实际正幅根上的界，不是只对 formal principal 的假设。$\xi_*$ 始终只是代数评价点；没有搬动任何真实支持点。

令
$$
A_c=-R_{x+\omega_c}/(8h_c^2)-T_{x+\omega_c}/8.
$$
同一个母准确满足三个完整 $q_j(A_c)=0$。固定任意 $\alpha>0$，照 R531 选一次第三 Gram 向量 $\nu$：
$$
2w_c\nu=r_c,\qquad
2w_h\nu=r_h-\ell_{k,c}\alpha,\qquad
2w_e\nu=r_e,
\tag{6}
$$
这里 $e=\partial_k+(2h_c)^{-1}\partial_\omega$，$r$ 是零矩、零速度的完整 canonical source。原三个 Gram 行独立，故得到同一个真实紧 $\chi_\theta$。其选择在路径开始前完成，后文不再修改。

从零 history 出发先走长为 $t_0$ 的真实常态段 $S=S_c$。该段
$$
A=tA_c,\qquad T=-t^2A_c^2/2,
\tag{7}
$$
含真实初端值。由三个 $q_j(A_c)=0$ 及(6)，全部相位的 ruling 在整段准确为零。该段的(1)密度为零，但其它矩、第三历史和位姿均不为零。

## 2. 完整八矩的三个混合坐标

对任意真实累计矩阵 $m$，沿 R73 原八坐标定义
$$
\mathcal R_m(x)=m_{r_1}+m_{s_1}x+m_{t_1}x^2,
\qquad
\mathcal P_m(x)=m_{r_0}+m_{s_0}x+m_{t_0}x^2,
$$
$$
m_{t_0}=m_{p_0}/4+m_{s_1}/2,\qquad
\mathcal J_m=\mathcal P_m-\omega_c\mathcal R_m.
\tag{8}
$$
这是三个真实矩阵坐标组成的二次多项式，不是新输入函数。

若 $p_0=p_1=p_2=0$，R73 原二导主项准确给
$$
\alpha_m/2=\mathcal R_m L_c-\mathcal J_m r.
\tag{9}
$$
一般情况下(9)另加一个对三个 $m_{p_j}$ 线性的原 jet 多项式；它在下文单独保留和估计。

写 $\gamma=h_s$，$d=h\omega-k$，$e=hx+d$，$Q=1+e^2$，并置
$$
a_1=2k\omega-(1+k^2)/h,\qquad
a_0=k\omega^2-(1+k^2)\omega/h.
$$
直接从 R73(6)(10)取原一次、常数系数，得到
$$
\begin{aligned}
\mathcal R_{M_{\rm raw}}
&=\frac{a_1Q}{8h}
+\gamma\left(\frac{\gamma Q}{8h^4}
-\frac{e e_s}{4h^3}\right),\\
\mathcal P_{M_{\rm raw}}
&=\frac{a_0Q}{8h}
+d_s\left(\frac{\gamma Q}{8h^4}
-\frac{e e_s}{4h^3}\right).
\end{aligned}
\tag{10}
$$
因此
$$
\boxed{
(\mathcal J_m)_s
=\frac{(a_0-\omega_ca_1)Q}{8h}
+\{h(\omega-\omega_c)-k\}_s
\left(\frac{\gamma Q}{8h^4}-\frac{e e_s}{4h^3}\right).
}
\tag{11}
$$
其中
$$
a_0-\omega_ca_1
=k\{(\omega-\omega_c)^2-\omega_c^2\}
-\frac{1+k^2}{h}(\omega-\omega_c).
\tag{12}
$$
式(11)保留完整静态项和两个速度项。尤其不能把混合项只估作一个任意符号的末常数。

## 3. 一套同时覆盖真实矩阵和速度的缩放

从常态前缀末端起写真实时间 $s-t_0=Lr$。设置
$$
k=\frac L{t_0}K,\qquad
\omega-\omega_c=\frac L{t_0}E,\qquad
D=hE-K,\qquad
\gamma=\frac{h_r}{L},\quad k_s=\frac{K_r}{t_0}.
\tag{13}
$$
水平关系仍逐点为
$$
E_r=\frac{K_r}{2h},\qquad
D_r=E h_r-\frac{K_r}{2}.
\tag{14}
$$
R533 的第二速度正是
$$
\delta=k_s/2-(\omega-\omega_c)\gamma=-D_r/t_0.
\tag{15}
$$
把三个混合矩记为完整多项式
$$
j(r,x)=t_0\mathcal J_{m(r)}(x),\qquad j_*=j(r,\xi_*).
\tag{16}
$$
另把两个 $R_{x+\omega_c},T_{x+\omega_c}$ 方向的真实累计偏差乘 $L$，把三个 $p$ 坐标乘 $t_0/L^2$。这八个量与原八矩是一个可逆线性坐标变换：例如用 $(m_{r_1},m_{t_1})$、三个 $\mathcal J$ 系数和三个 $m_{p_j}$，再由
$$
m_{s_1}=2[ x^2]\mathcal J_m-m_{p_0}/2+2\omega_c m_{t_1}
$$
恢复其余坐标。前两个方向先减去真实 $t_0A_c$，所有缩放变量在入端为零。

在固定有限 $r$ 区间及固定有限缩放状态、速度盒上，原 $M_{\rm raw}$ 方程给
$$
m_{R,T}-t_0(A_c)_{R,T}=O(L^{-1}),\quad
\mathcal J_m=O(t_0^{-1}),\quad
m_{p_j}=O(L^2/t_0).
\tag{17}
$$
这里不是预设某个实际轨道满足(17)：按上述缩放写出的八矩 ODE 的右端在该盒中平滑有界，后文由 ODE 连续依赖获得实际轨道和这些界。两个 $R,T$ 方向的快极限含 $h_r^2$；三个 $p$ 坐标的快极限保有真实静态漂移，**没有冻结 $m$**。

对(11)，有完全准确的代入
$$
e=h(x+\omega_c)+\frac L{t_0}D,\qquad
e_s=\frac{h_r}{L}(x+\omega_c)+\frac{D_r}{t_0}.
$$
因而 $Q-2he(x+\omega_c)=1-h^2(x+\omega_c)^2+(LD/t_0)^2$。静态项在 $j_r$ 中是 $O(L^2)$，其余小项亦平滑趋零。三个系数同时得到
$$
\boxed{
j_r(r,x)
=D_r h_r\frac{1-h^2(x+\omega_c)^2}{8h^4}+o_{C^1}(1).
}
\tag{18}
$$
这一步来自真实 R73，不是从一个投影为零猜全记忆为零。

## 4. 完整 ruling 的一致快极限

令
$$
y_0=\xi_*+\omega_c=\omega_c/2,\quad
q(h)=1+h^2y_0^2,\quad q_c=q(h_c),
$$
$$
a_D(h)=\frac{q(h)^2q_c}{32h^4h_c^2},\qquad
\kappa(h)=\frac{8h^3}{q(h)},\qquad
g_0(h)=\frac{\alpha q_c^2h^3(h^2-h_c^2)}{4h_c^4q(h)^2}.
\tag{19}
$$
$a_D$ 在高度盒上一致严格正。

**引理 1。** 在第3节的有限缩放盒上，完整同规范 scalar 方程满足
$$
\boxed{
\frac{F}{\Lambda}
\longrightarrow
a_D(h)\{g_0(h)-\kappa(h)j_*-D_r\}
\quad\text{于 }C^1.
}
\tag{20}
$$
这里包含对两个真实缩放速度 $(h_r,K_r)$ 的导数，不只是对方程值的收敛。

**证明。** R520/R533 的原完整主平方是
$$
\sum_i\lambda_i\int\frac Qh
\left(\frac{\alpha_m}{2}
+\frac{Q(\gamma L_c+\delta r)}{8h^3}\right)^2t_i^2.
\tag{21}
$$
在(13)—(17)中，$L_c$ 的系数为
$$
-\frac{t_0Q_c}{8h_c^2}+O(L^{-1}),
$$
$r$ 的系数为
$$
-\frac1{t_0}\left(j(r,x)+\frac{QD_r}{8h^3}\right).
$$
其中 $Q_c(x)=1+h_c^2(x+\omega_c)^2$。由于 $t_0L=L^{-1}$，高度速度和 $R,T$ 偏差相对于首项都是 $O(L)$。它们**不因 $\Lambda$ 大而自行消失**，而是由此明确的 $t_0$ 层级变小。

交叉项用(4)的完整 $\mathsf B$ 评价，除以 $\Lambda$ 后趋于
$$
-\frac{q(h)q_c}{4hh_c^2}
\left(j_*+\frac{q(h)D_r}{8h^3}\right).
\tag{22}
$$
$L_c^2$ 项由 $\mathsf A[P]=O(1)$ 控制；其最大尺度 $t_0^2/\Lambda=L^2$。$r^2$ 项由 $\mathsf C=O(\Lambda)$ 控制，除以 $\Lambda$ 后为 $O(t_0^{-2})$。三个 $p$ 坐标贡献的交叉最大为 $O(L^2)$。这些项及其缩放变量的一次导数都趋零。

全部 complete $C^2$ 余项按 R533 是 $m$、速度至多二次，其系数一致有界；故它们除以 $\Lambda$ 后由
$$
C(1+|m|+|\gamma|+|k_s|)^2/\Lambda=O(L^2)
\tag{23}
$$
控制。原左尾、初端商势和 first-derivative 项均在这一完整余项内，没有逐项删掉。

最后核固定规范。R533 给
$$
\ell_{k,c}/\Lambda\longrightarrow b_0:=q_c^3/(64h_c^6)>0.
$$
零矩、零速度的 canonical source 及其 scalar 导数是有界 $C^2$ 系数。由(6)准确解原三行，得到
$$
\frac\nu\Lambda\longrightarrow
b_0\alpha\,(h_c^2,-\omega_ch_c^2,h_c^2\omega_c^2-1).
\tag{24}
$$
以原能量权 $w=((1+d^2)/(4h),d/2,h/4)$ 代入，$k,\omega-\omega_c\to0$ 时
$$
-2w\nu/\Lambda
\longrightarrow b_0\alpha\frac{h^2-h_c^2}{2h}
=a_D(h)g_0(h).
\tag{25}
$$
(22)(25)相加正是(20)。原规范一次固定，(24)只证明其真实有限幅值的尺度，不是沿轨道重新选 $\nu$。证毕。

特别，固定高度输入时，$D_r=Eh_r-K_r/2$，故
$$
\partial_{K_r}(F/\Lambda)\longrightarrow a_D/2>0.
\tag{26}
$$
换回真实变量，$F_{k_s}=\Lambda t_0(a_D/2+o(1))$。短回路中的 $H_{12}h_s=O(\Lambda/L)$ 相对于这个下界是 $O(L)$。这明确处理了不能仅凭 $H_{11}=O(1)$ 就继承常态速度下界的问题。

## 5. 真混合记忆的可积返回

由(18)(20)得到极限系统
$$
D_r=g_0(h)-\kappa(h)j_*,\qquad
(j_*)_r=D_r h_r\frac{1-h^2y_0^2}{8h^4}.
\tag{27}
$$
设 $J(h)$ 是同一个一元线性初值解
$$
J'(h)+\frac{1-h^2y_0^2}{h q(h)}J(h)
=\frac{1-h^2y_0^2}{8h^4}g_0(h),\qquad J(h_c)=0.
\tag{28}
$$
其积分因子为 $h/q(h)$，在整个高度邻域真实非零。对任意光滑高度输入，唯一性准确给
$$
j_*(r)=J(h(r)),\qquad
D_r=g(h(r)),\quad g:=g_0-\kappa J.
\tag{29}
$$
高度可以多次转向；无需除以某个实际可能为零的 $h_r$。直接将 $J(h(r))$ 代入(27)即可验证并用初值唯一性。

其余两个系数也不被遗漏。由(18)，对每个实际多项式变量 $x$，
$$
j(r,x)=\int_{h_c}^{h(r)}
g(z)\frac{1-z^2(x+\omega_c)^2}{8z^4}\,dz.
\tag{30}
$$
因此任何返回 $h_c$ 的高度回路，都会使**整个二次多项式** $j(r,x)$ 返回零。

从(19)(28)有
$$
g(h_c)=0,\qquad J'(h_c)=0,\qquad g'(h_c)=\alpha/2>0.
\tag{31}
$$
这正是将完整混合历史转成实际端信号所需的符号，不能以任意余常数的粗界代替。

## 6. 一次实际 endpoint IFT 给负端态

取固定 $x_0,\psi\in C_c^\infty(0,1)$，满足
$$
\int_0^1x_0=0,\qquad x_0\not\equiv0,\qquad\int_0^1\psi\ne0.
$$
给定高度输入
$$
h(r)=h_c+\varepsilon x_0(r)+z\psi(r).
\tag{32}
$$
$\varepsilon>0$ 最终固定得足够小，$z$ 是唯一的实际端校正参数。整个输入在两个端点附近恒为 $h_c$。

极限系统中，记
$$
I(r)=\int_0^r\frac{g(h(t))}{h(t)^2}\,dt,\qquad
J_0(r)=\int_0^r g(h(t))\,dt.
$$
(14)(29)准确积分为
$$
E(r)=-h(r)I(r),\qquad
K(r)=-h(r)^2I(r)-J_0(r).
\tag{33}
$$
目标是同一个末端条件
$$
\frac32K(1)-h_cE(1)=0.
\tag{34}
$$
它等价于
$$
\int_0^1g(h(r))\left(3+\frac{h_c^2}{h(r)^2}\right)dr=0.
\tag{35}
$$
在 $(\varepsilon,z)=(0,0)$，对 $z$ 的导数为 $2\alpha\int\psi\ne0$，对 $\varepsilon$ 的导数为零。因此有真实极限根 $z=z_*(\varepsilon)=O(\varepsilon^2)$。

令 $\delta_*=E(1)-K(1)/(2h_c)$。由(33)，
$$
\delta_*=rac1{2h_c}\int_0^1
g(h(r))\left(1-\frac{h_c^2}{h(r)^2}\right)dr
=\frac{\alpha\varepsilon^2}{2h_c^2}\int_0^1x_0^2+O(\varepsilon^3)>0.
\tag{36}
$$
于是
$$
K_*:=K(1)=h_c\delta_*,\qquad
E_*:=E(1)=3\delta_*/2,\qquad
D_*:=h_cE_*-K_*=K_*/2>0,
$$
$$
P_*:=K_*^2-h_cK_*E_*=-K_*D_*<0.
\tag{37}
$$
同时由(30)，三个混合记忆末值全部为零。

现在固定这个有限小 $\varepsilon$。引理1、(18)和原八矩缩放系统给完整实际解对极限解的 $C^1$ 参数收敛。由同一个非零 endpoint 导数，对充分小但有限的 $L$，再对(32)中的 $z$ 作**一次有限 IFT**，得到实际精确(34)。不再调整母、$\chi$ 或前缀。实际末端
$$
\delta_L>0,\qquad
P_L^{\rm end}=-h_c^2\delta_L^2/2<0,
\tag{38}
$$
这里 $\delta_L=E_L-K_L/(2h_c)$ 是缩放端量；物理密度为 $(L/t_0)^2P_L^{\rm end}$。

实际三个 $j$ 末值是趋零的真实输出，不宣称它们在有限 $L$ 时准确为零。它们在下一段仍按原 $M_{\rm raw}$ 演化。

## 7. 同一二速度雅可比及平滑负保持

令缩放后的真实密度
$$
P=K^2-hKE=-KD.
$$
由水平关系逐点有
$$
P_r=(3K/2-hE)K_r-KEh_r.
\tag{39}
$$
将完整方程 $F/\Lambda=0$ 与 $P_r=\sigma(r)$ 联立，未知是同一 $(h_r,K_r)$。快极限的雅可比为
$$
\det
\begin{pmatrix}
-a_DE&a_D/2\\
-KE&3K/2-hE
\end{pmatrix}
=a_D E(hE-K)=a_D ED.
\tag{40}
$$
在(37)处严格正。没有分别使用两个不相容的速度消元。

在极限端态取 $\sigma=0$，由 $h=h_c,j_*=0,g_0(h_c)=0$，(27)(39)的唯一解为
$$
h_r=K_r=E_r=0,\qquad j_r=0.
\tag{41}
$$
两个 $R,T$ 缩放偏差也恒定；三个 $p$ 缩放坐标仍有原静态的线性累计。这是一个有限区间上的完整缩放解，不是把整个 $m$ 设成常数。

有限 $L$ 的拼接不能在端点直接把 $\sigma$ 改为零。先沿真实高度恒定的旧反馈短延续，读它的真实 $\sigma_{\rm old}=P_r$。由(34)及 $h_r=0$，其接点值为零。取一个固定、有限的缩放过渡窗，用光滑 cutoff
$$
\sigma(r)=\vartheta(r)\sigma_{\rm old}(r),
\tag{42}
$$
其中左开邻域 $\vartheta=1$、右开邻域 $\vartheta=0$。用同一(40)解原两方程，保全部 incoming。极限旧解正是(41)，故这一过渡收敛到同一个负静止态。实际整段仍 $P<0$，右端真正达到 $\sigma=0$ 的开 germ，随后准确保持某个
$$
P_L^{\rm hold}<0,\qquad P_L^{\rm hold}\longrightarrow P_*.
\tag{43}
$$
$P_L^{\rm hold}$ 一般不等于切换前的 $P_L^{\rm end}$。

对任意**事先固定的有限** $R>0$，极限解(41)及真实漂移的 $p$ 坐标在 $[0,R]$ 上处于有限盒，且(40)有正下界。完整 ODE 的连续依赖于是给：取足够小的同一个有限 $L$，实际过渡后可继续保持整段缩放时长 $R$，全部状态留在同一个合法 scalar 盒内，所有八矩有限。没有从“速度图全 history 正则”跳到任意长原时间不爆；这里的存在来自一条明确极限轨道在指定有限区间上的逼近。

## 8. 全部累计的严格负号

常态前缀的(1)为零。非恒段物理密度及时间准确缩放为
$$
p_1^{\omega_c}=(L/t_0)^2P(r),\qquad ds=L\,dr.
\tag{44}
$$
令 $I_*^{\rm loop}=\int_0^1P_*(r)\,dr$ 是第6节极限回路的完整值。它有限；小 $\varepsilon$ 时的二阶首项为正，这一代价不删。过渡的极限密度为负常数 $P_*$。

现在只需选一个有限 $R$，使
$$
I_*^{\rm loop}+R P_*<-2.
\tag{45}
$$
也可将右端换成任意预先固定的负数；不要求某个既定物理负量统一于 $L$。过渡只会使极限累计更小。再按第7节选同一个足够小的有限 $L$，得到
$$
\boxed{
\int_{\text{全部真实路径}}p_1^{\omega_c}(s)\,ds
< -\frac{L^3}{t_0^2}<0.
}
\tag{46}
$$
这是完整实际累计，包含原常态前缀、完整高度回路、真实 endpoint 校正、平滑切换及整个 hold。没有用某段负密度代替积分，也没有把未清的其它矩当成可任意补偿的基准。

高度位移虽小，原高度速度为 $O(L^{-1})$；整个非恒段的 R524 能量小盒条件并未被保为小于一。因此本稿不与该稿的小能量累计正性矛盾，也没有用小 scalar 位移替代它所需的完整速度范数。

### 8.1 同一规范还给一个准确为零的实际矩坐标

这不需新母或新控制。置 $X_0(r)=\int_0^r x_0(t)\,dt$，由(31)(33)和 $z_*(\varepsilon)=O(\varepsilon^2)$，
$$
K(r)=-\alpha\varepsilon X_0(r)+O(\varepsilon^2),\qquad
E(r)=-\frac{\alpha\varepsilon}{2h_c}X_0(r)+O(\varepsilon^2).
$$
因此完整回路积分为
$$
I_*^{\rm loop}
=\frac{\alpha^2\varepsilon^2}{2}\int_0^1X_0(r)^2\,dr
+O(\varepsilon^3)>0.
$$
固定长度的平滑过渡在极限中只增加 $O(\varepsilon^4)$ 的负值，故充分小的同一个 $\varepsilon$ 使保持段之前的完整缩放累计仍严格正。再取小 $L$，实际值 $I_L^{\rm pre}>0$。

由于右端保持的真实 $P_L^{\rm hold}$ 是常负数，在已经存在的同一保持段内取停止时间
$$
R_L^0=-I_L^{\rm pre}/P_L^{\rm hold}.
$$
它严格位于零和第8节选定的有限 $R$ 之间，并准确给
$$
\int_{\text{截至该真实时刻的全部路径}}p_1^{\omega_c}(s)\,ds=0.
$$
路径非恒，$M$ 的其它坐标和终端速度未被清零。这里仅截取已经完整定义、可继续的同规范路径，不将停止时刻改成常态 collar；尤其不把一个矩坐标为零写成 $M=0$。

## 9. 完整第三、固定规范与实际有限性

选择次序是：原合法盒和几何参数；固定 $\alpha,x_0,\psi$；一个有限小 $\varepsilon$ 和极限端根；有限 $R$；足够小有限 $L$；$t_0,\Lambda$；该 $\Lambda$ 的实际 R533 母及有限频率；一次固定 Gram $\chi$；一次实际端根；完整平滑控制。所有依赖均可按前述一致估计实行，未在路径中重新选择这些对象。

在非恒段，真实矩阵大小为 $O(t_0+L^{-1})$，原速度至多为 $O(L^{-1})$，原加速度在固定缩放控制下至多为有限的 $O(L^{-2})$。R482 原第三式仍按
$$
T_s=-M_{\rm raw}\circ A+C(S,j^2S)
\tag{47}
$$
积分；$C$ 保完整速度一次、速度三次及速度乘加速度项。长前缀给真实 $T=-t_0^2A_c^2/2$，后段 $-M\circ A$ 和这些局部项均可积。对固定的 $\varepsilon,R$，有限算子系数有例如 $O(L^{-4})$ 的共同粗界。这里没有把第三 history 或初端势扔进零，也没有声称其误差与约化 scalar 状态同阶。

固定 $\nu=O(\Lambda)$；原 Gram 右逆可在共同 $C^2$ 小图册中一次选择，故得到真实有限 $\chi$。它在整个长前缀、短回路和保持段上相同。原 frame 和位置方程用这些真实 scalar 输入继续积分，所有位姿及成本保留实际输出。没有使用一个无 ruling 的 R70/R518 桥，也没有借用 R521 正交母库的收据。

## 10. 已付范围及下一门

本稿得到同一个从起点选取的 R533 三十三行母、一个固定 $\chi$、一个真实常态入 germ 上，完整全相位 ruling 恒零且全累计 $p_1^{\omega_c}<0$ 的有限路径。它具体越过了“只有局部负密度、总前缀仍正”的缺口。

尚未支付：其它七个矩与(1)的同一次配平；末 scalar/germ 返回；frame、pose 与真正第三 period；同一个第二规范的全部十三门及最终闭合成本。不能把本稿路径直接重复当作可加零端口 prototype。式(46)也不授予任意指定负累计值的满射。

下一实际问题因此是：在同一完整、有记忆 ruling 方程中，将这些真实有限正负矩输出组织为返回控制；本稿提供一个此前没有的净负输出，但没有预先假定这些输出可以独立拼接。
