# R546：同一固定规范的真实二次矩脉冲与一个负前缀坐标的准确归零

日期：2026-11-16。**完整原式纸面证明；没有执行数值、符号、profile、秩或新的科学任务。**

本稿沿 R540/R542 的同一个三十三行母和固定 $\chi$ 继续。R542 已证明，仅继续压缩同一 null 参考弧不能清掉 $t_1$ 的负累计。本稿没有改变这一结论，而是支付另一条真实八矩方向：从 R540 的实际 $k>2$、净负 $p_1^{\omega_c}$ 入端出发，可以选定一个原先在常态前缀上严格为负的固定矩阵线性坐标，用同规范有限光滑脉冲将其准确调到零，甚至任意一个给定的有限实目标。

选定坐标来自四个预先列出的固定读出，不是沿路径更换坐标。脉冲全过程保原 $M_{\rm raw}$、真实第三、frame、位置和原初端势。scalar 和原三个 $p$ 坐标的追加变化可以任意小，因而原 $k>2$ 与净负 $p_1^{\omega_c}$ 同时保留。其余矩并未保持不变；尤其速度平方对 $t_1$ 仍非正。

这是一条实际的单矩控制，不是全八矩返回，也不是用 formal 二次像代替真实路径。末端仍是可继续的原 smooth germ，不被改成一个无费用常态 collar。

来源：
[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、
[R520](R520-variable-mother-constant-ruling-and-same-gauge-nonconstant-local-departure.md)、
[R533](R533-complete-velocity-quadratic-form-and-all-history-regular-ruling-coordinates.md)、
[R536](R536-real-negative-total-matrix-density-from-a-complete-fast-height-loop.md)、
[R540](R540-same-positive-null-branch-and-real-large-curvature-with-negative-total-matrix-density.md)、
[R542](R542-complete-second-matrix-sign-and-duration-gates-for-the-fast-ruling-family.md)。

## 1. 完整二次矩的原八坐标

继续固定
$$
\eta=\omega-\omega_c,\qquad d_c=h\eta-k,\qquad
d=h\omega-k=h\omega_c+d_c,
$$
$$
z=(\gamma,\delta),\qquad
\gamma=h_s,\quad \delta=k_s/2-\eta\gamma.
\tag{1}
$$
于是
$$
d_s=\omega_c\gamma-\delta.
$$
下文用
$$
\ell_v=\omega_c\gamma-\delta,\qquad
G_v=\frac{\gamma(1+d^2)}h-2d\ell_v
\tag{2}
$$
简写速度的线性式，避免与原窗口左端或固定第三规范混淆。

原 R73(6)(9)(10)给准确分解
$$
M_{\rm raw}(S,z)=M_0(S)+N(S,z),
\tag{3}
$$
其中 $N$ 对 $z$ 齐次二次，其全部八坐标为
$$
\boxed{
\begin{aligned}
&p_0(N)=p_1(N)=p_2(N)=0,\\
&r_1(N)=\frac{\gamma G_v}{8h^3},
\qquad r_0(N)=\frac{\ell_v G_v}{8h^3},\\
&s_1(N)=-\frac{\gamma\ell_v}{4h^2},
\qquad s_0(N)=-\frac{\ell_v^2}{4h^2},\\
&t_1(N)=-\frac{\gamma^2}{8h^2},
\qquad t_0(N)=-\frac{\gamma\ell_v}{8h^2}
=\frac{s_1(N)}2 .
\end{aligned}
}
\tag{4}
$$
这里 $t_0$ 仍是原 trace 关系给出的非独立坐标。

为核(4)，原速度部分是
$$
B_{0,v}=\frac{(\gamma x+\ell_v)G_v}{8h^3},\qquad
B_{1,v}=-\frac{(\gamma x+\ell_v)\ell_v}{4h^2},\qquad
B_{2,v}=-\frac{\gamma(\gamma x+\ell_v)}{8h^2}.
$$
取其常数、一次项即得到(4)。没有使用端点条件或先对 $s$ 积分。

也可把整个原矩阵写成
$$
N=
\begin{pmatrix}
G_v/(8h^3)\\
-\ell_v/(4h^2)\\
-\gamma/(8h^2)
\end{pmatrix}
\begin{pmatrix}0&2\gamma&-4\ell_v\end{pmatrix}.
\tag{5}
$$
两向量的内积为零。因此非零速度给一个真实 rank-one、trace-zero、平方为零的矩阵 $N$。这只是描述完整原速度项；下文仍按(3)保静态项，绝不把 $M_{\rm raw}$ 整个换成(5)。

## 2. 两个固定多项式读出的准确速度因子

使用 R536 原矩阵坐标
$$
\mathcal R_m(x)=m_{r_1}+m_{s_1}x+m_{t_1}x^2,
$$
$$
\mathcal P_m(x)=m_{r_0}+m_{s_0}x+m_{t_0}x^2,\qquad
\mathcal J_m=\mathcal P_m-\omega_c\mathcal R_m,
\quad m_{t_0}=m_{p_0}/4+m_{s_1}/2.
\tag{6}
$$
令 $x=y-\omega_c$。直接代(4)，整个速度二次项有
$$
\boxed{
\bigl(\mathcal R_N(y-\omega_c),\mathcal J_N(y-\omega_c)\bigr)
=(\gamma,-\delta)\,W_y(S,z),
}
\tag{7}
$$
其中
$$
W_y(S,z)=
\frac{\gamma(1-h^2y^2+d_c^2)+2h(hy+d_c)\delta}{8h^4}.
\tag{8}
$$
这是对两个固定线性读出的共同因子式。$y$ 是用来读一个有限矩阵多项式的实数，不是新物理包中心；不要求 $y-\omega_c$ 位于 profile 支持中，也不改变真实窗口。

## 3. 同一完整 ruling 的两个正则图

沿 R540 用实际完整 $\mathsf H$ 定义
$$
b=\frac{\mathsf H_{22}}{-\mathsf H_{12}+
\sqrt{\mathsf H_{12}^2-\mathsf H_{11}\mathsf H_{22}}},
\qquad
\beta=\frac{\mathsf H_{11}}{-\mathsf H_{12}+
\sqrt{\mathsf H_{12}^2-\mathsf H_{11}\mathsf H_{22}}},
$$
$$
n_+=(b,1),\qquad n_-=(1,\beta),\qquad
\kappa_N=n_+^{\mathsf T}\mathsf Hn_-<0.
\tag{9}
$$
完成平方后，完整方程准确是
$$
z=z_c+Xn_++Yn_-,
\qquad
F=2\kappa_NXY-\Delta(S,m).
\tag{10}
$$
因此既有 R540 的 $X$ 图，也有相同原方程的 $Y$ 图：
$$
X=a\ne0,\qquad Y=\frac{\Delta}{2\kappa_Na};
\tag{11}
$$
$$
Y=b_{\rm in}\ne0,\qquad X=\frac{\Delta}{2\kappa_Nb_{\rm in}}.
\tag{12}
$$
$b_{\rm in}$ 只是本节输入，不是(9)的 null 斜率 $b$。

(12)的原正则偏导为 $F_X=2\kappa_Nb_{\rm in}\ne0$。当 $\Delta$ 沿实际轨道过零时，$X$ 可以平滑过零，但 $Y$ 仍非零；这不是经过速度锥的奇异顶点，也不是跳到另一份不相接的解。后文选哪一个图，都先与真实已有的开 germ 相接。

R540 对同一有限盒保
$$
|b|\le M,\qquad |\beta|=O(\Lambda^{-1}).
\tag{13}
$$
本稿只把“充分大”的有限 $\Lambda$ 再明定到以下有限不等式。它在共同母的初选时支付，不在已经走出的路径中修改母或规范。

## 4. 四个预定矩阵坐标中有一个真实双号读出

设 $h_{\max}$ 是 R540 已选盒中的高度上界，$|d_c|\le D_{\max}$ 是它的有限界。先固定
$$
0<r_y\le\min\{1,(4h_{\max})^{-1}\},\qquad c_0=M+2.
\tag{14}
$$
取有限 $\Lambda$ 足够大，使整盒上
$$
c_0|\beta|<1/2
\tag{15}
$$
以及
$$
2h_{\max}(h_{\max}r_y+D_{\max})|\beta|<1/4.
\tag{16}
$$
由 R533/R540 的统一界，这些只是原小 $L$ 的有限加强条件，不增加任何 profile 目标。

在同一个原八矩空间中，预先列四个固定线性坐标
$$
\boxed{
\rho_{\varepsilon,\sigma}(m)=
\mathcal R_m(\varepsilon r_y-\omega_c)
+\sigma c_0\mathcal J_m(\varepsilon r_y-\omega_c),
\qquad\varepsilon,\sigma\in\{-1,1\}.
}
\tag{17}
$$
这些行在后继过程中不变。它们可以有线性相关，本文不声称四行联合满射；只将选择其中一行。

固定一个实际入端 $S_0$，以后所有符号 $b_0,\beta_0,h_0,d_0$ 均为它的真实值。记
$$
W_+(y)=W_y(S_0,n_+),\qquad
W_-(y)=W_y(S_0,n_-).
$$
由(8)，
$$
W_-(y)=\frac{1-h_0^2y^2+d_0^2+
2h_0(h_0y+d_0)\beta_0}{8h_0^4}>0
\quad(|y|\le r_y).
\tag{18}
$$
严格号来自 $1-h_0^2y^2+d_0^2\ge15/16$ 与(16)。

另一方面，
$$
W_+(y)=
\frac{b_0(1-h_0^2y^2+d_0^2)+2h_0(h_0y+d_0)}
{8h_0^4},
$$
所以准确有
$$
W_+(r_y)-W_+(-r_y)=\frac{r_y}{2h_0^2}.
\tag{19}
$$
因此至少一个 $\varepsilon\in\{-1,1\}$ 满足
$$
|W_+(\varepsilon r_y)|\ge\frac{r_y}{4h_0^2}>0.
\tag{20}
$$
选这个 $\varepsilon$，再令
$\sigma=\operatorname{sign}W_+(\varepsilon r_y)$。
从此固定 $\rho=\rho_{\varepsilon,\sigma}$。

定义两个**完整原二次矩**
$$
N_+=N(S_0,n_+),\qquad N_-=N(S_0,n_-).
$$
由(7)，
$$
\boxed{
\rho(N_+)=(b_0-\sigma c_0)W_+(\varepsilon r_y)<0,
}
$$
$$
\boxed{
\rho(N_-)=(1-\sigma c_0\beta_0)W_-(\varepsilon r_y)>0.
}
\tag{21}
$$
第一式甚至不大于 $-2|W_+(\varepsilon r_y)|$，第二式由(15)(18)有严格正下界。

这不是只比较两个 formal 方向后宣称可控制。第6节将用两个同规范真实图实现相应有限矩增量，并在有限参数处准确求根。

还要保该坐标的原前缀基准。R536 的真实常态前缀满足
$$
\mathcal R_m(x)=-\frac{t_0}{8h_c^2}
\{1+h_c^2(x+\omega_c)^2\},\qquad
\mathcal J_m(x)=0 .
$$
故四个预定行在这个前缀末端都准确为
$$
\boxed{
\rho_{\varepsilon,\sigma}(m_{\rm prefix})
=-\frac{t_0(1+h_c^2r_y^2)}{8h_c^2}<0.
}
\tag{22}
$$
选择其中一行不会改变这个真负号。$\rho$ 是原八矩的一个非零固定线性泛函，可以补成八维坐标系；并未引入一个替代 $M$ 的外部观察。

## 5. R540 可以把实际入端选为两图同时正则

后文需要 $\Delta(S_0,m_0)\ne0$，使实际 $X,Y$ 都非零。不能免费假设任意 R540 末态都满足它。这里在该稿原有限输入选择中准确支付。

在 R540 的短高度下降段右端，已付
$$
X>0,\qquad \gamma=0,\qquad
\delta=\frac\alpha2L^{5/2}+O(L^3).
$$
该稿对 $\mathsf l_\delta$ 的原主交叉稍作保系数写法给
$$
\mathsf l_\delta=\Lambda t_0a_D(h)\{1+O(\sqrt L)\},
\qquad
\mathsf H_{12}=-\Lambda\frac{q(h)^3}{64h^7}+O(1),
$$
$$
a_D(h)=\frac{q(h)^2q_c}{32h^4h_c^2},\qquad
q(h)=1+h^2\omega_c^2/4.
$$
因而由原完成平方中心，
$$
(z_c)_\gamma
=\frac{t_0q_ch^3}{q(h)h_c^2}\{1+O(\sqrt L)\}
=h_ct_0\{1+O(\sqrt L)\}>0.
\tag{23}
$$
其余项仍有 $(z_c)_\delta=O(L^3)$、$\beta=O(L^6)$。
从(10)恢复另一坐标，得到
$$
Y=\frac{\gamma-(z_c)_\gamma-b\{\delta-(z_c)_\delta\}}
{1-b\beta}
=-h_ct_0\{1+O(\sqrt L)\}<0.
$$
因此在这一真实入口
$$
\Delta=2\kappa_NXY>0.
\tag{24}
$$

R520 的有限 Laurent/log 几何系数和有限算子展开，使固定母、固定 $\chi$ 后的 $(S,m)$ 方程在合法盒内实解析。null frame 的平方根也在严格正判别式上实解析。因此，R540 每一段常数 $X=a>0$ 平台上的实际状态解及 $\Delta(S,m)$ 都实解析。

从一个 $\Delta\ne0$ 的入端开始，$\Delta$ 不可能在同一有限解析平台的某个后开区间突然恒零；其零点在平台内部是离散的。故可以把每个平台末时刻作任意小的真实改变，使它仍满足 $\Delta\ne0$。这些微调总和先取在 R540 的 strict shadow 误差、严格 $k>2$ 和负累计余量以内。平台间的 smooth ramp 取足够短，使其状态变化不跨过当前非零 $\Delta$ 的开邻域。

有限次递推即给 R540 同一个母、同一个 $\chi$、同一完整真实起点上的一个末态
$$
\boxed{
k_0>2,\qquad
\int_{\rm prefix\ to\ }S_0 p_1^{\omega_c}<0,\qquad
X_0>0,\quad Y_0\ne0.
}
\tag{25}
$$
所有微调之后的 $m_0,T_0$ 是实际输出。没有在末端重置它们，也没有声称一个指定的 $\Delta=0$ 旧末态可以直接套用双图。

## 6. 真实矩脉冲极限：scalar 小变、矩阵有限变

现在冻结(25)这个实际入端和第4节选中的 $\rho$。给一个有限 $\tau_*>0$。

若使用 $X$ 图，取一个有限大 $B>0$，平台输入 $X=B$；若使用 $Y$ 图，取
$$
Y=\operatorname{sign}(Y_0)B.
$$
输入与已有真实 germ 之间用光滑短 ramp 接上，保持所用输入的符号非零。先定幅度，再把 ramp 时长选足够短，可使其 $(S,m)$ 变化为 $o(1)$。这里用的是当前有限状态邻域上的完整 ODE 存在性，不以大幅度为由忽略 ramp 的平方项。

在平台上置
$$
\tau=B^2(s-s_{\rm platform}),\qquad \zeta=z/B.
$$
固定母、固定 $\chi$ 后，$z_c$ 对 $m$ 至多一次，$\Delta$ 对 $m$ 至多二次。因此在一个先固定的有限 $m$ 盒上：

- 对 $X$ 平台，$\zeta=n_+(S)+O(B^{-1})$；
- 对 $Y$ 平台，$\zeta=\operatorname{sign}(Y_0)n_-(S)+O(B^{-1})$。

更准确地，误差由 $C(1+|m|)/B+C(1+|m|^2)/B^2$ 控制。原完整方程为
$$
S_\tau=B^{-1}\mathcal B(S)\zeta,\qquad
m_\tau=B^{-2}M_0(S)+N(S,\zeta),
\tag{26}
$$
$\mathcal B$ 仍是 R540 的真实水平 scalar 映射。

在 $0\le\tau\le\tau_*$ 上，普通 ODE 连续依赖给完整的 $C^1$ 端时间收敛
$$
\boxed{
S_B(\tau)\longrightarrow S_0,\qquad
m_B(\tau)\longrightarrow m_0+\tau N_\pm.
}
\tag{27}
$$
证明可在极限路径 $m_0+\tau N_\pm$ 的一个固定有限管中进行；先用这一管取得界，再取 $B$ 大，实际解保持在管内。因此(27)不是先假设 $m$ 有界后无限延续，也没有要求同一个 $B$ 处理无界 $\tau$。

符号 $\operatorname{sign}(Y_0)$ 在 $N$ 中消失，因为(4)是齐次二次。原静态 $M_0$ 在(26)中保留为 $B^{-2}M_0$，不是声称它准确等于零。

平台真实时长是 $\tau_*/B^2$，ramp 亦可使真实长度趋零。真实矩阵增量却趋于有限非零的 $\tau N_\pm$。这与 R540 的 $m/B$ 小步不同：本节直接对有限矩增量使用 $B^2$ 快时钟，并完整保留原二次矩。

## 7. 任意有限单矩目标的准确有限根

令 $\rho_0=\rho(m_0)$，给定任意有限实目标 $\rho_{\rm tar}$。

若 $\rho_{\rm tar}>\rho_0$，选 $Y$ 图的 $N_-$ 平台；若
$\rho_{\rm tar}<\rho_0$，选 $X$ 图的 $N_+$ 平台。对应的
$v=\rho(N_\pm)$ 与目标差同号，由(21)严格非零。令
$$
\tau_0=\frac{\rho_{\rm tar}-\rho_0}{v}>0.
\tag{28}
$$
在一个包含 $\tau_0$ 的固定有限小闭区间上，(27)给
$$
\rho(m_B(\tau))=\rho_0+\tau v+o_{C^1}(1).
$$
所以对一个足够大但有限的 $B$，同一个端时间变量有准确根
$$
\tau_B\longrightarrow\tau_0,\qquad
\boxed{\rho(m_B(\tau_B))=\rho_{\rm tar}.}
\tag{29}
$$
其实际导数趋于非零的 $v$；这是有限 IFT/严格单调求根，不是只把极限 signed 方向当成真实控制。若目标等于 $\rho_0$，入端已经支付该坐标，不需要另接一段。

ramp 先固定为与 $\tau$ 无关的同一个 smooth 输入；它的真实 $m$ 变化在(27)中一同收敛，因此(28)(29)没有漏掉原型基准。选定 $B$ 后，目标附近还得到一个实际 $C^1$ 单坐标端时间截面；没有据此授予四个候选读出或全八矩联合满射。

特别，取 $\rho_{\rm tar}=0$，就从同一个原起点得到一个先在(22)严格为负、如今准确归零的原矩坐标。也可取一个正目标，得到真正改变总号的有限路径。两者均使用同一固定母、固定 $\chi$ 和实际 incoming。

## 8. 同时保留净负 $p_1^{\omega_c}$ 与 $k>2$

由(27)，整个新平台的 scalar 变化为 $O(B^{-1})$；ramp 的变化也可任意小。选择 $B$ 大后，$k>2$ 的原 strict margin 和物理合法性均保持。

原三个 $p$ 列是 R73 的当前 scalar 函数，不含速度平方。因此由整个新段的真实长度趋零，
$$
\left\|\int_{\rm new}(p_0,p_1,p_2)\,ds\right\|\longrightarrow0.
\tag{30}
$$
取其对 $p_1^{\omega_c}$ 的影响小于(25)中实际负余量的一半，即可在(29)的有限根上同时保持
$$
\boxed{
\rho(M_{\rm total})=\rho_{\rm tar},\qquad
\int p_1^{\omega_c}<0,\qquad k_{\rm final}>2.
}
\tag{31}
$$
这里 $M_{\rm total}=m_{\rm final}$ 始终从原零 history 起累计。

但本节不能用于 $t_1$。两个快方向准确满足
$$
t_1(N_+)=-\frac{b_0^2}{8h_0^2}\le0,\qquad
t_1(N_-)=-\frac1{8h_0^2}<0.
\tag{32}
$$
所以用于(29)的矩阵脉冲一般继续增加 R542 的负 $t_1$ 欠额。本稿已清的是另一个真实固定读出，不把它包装为慢轨道的正 $t_1$ 收据。

## 9. 完整 history、真实图切换和边界

在 $Y$ 图中若 $\Delta$ 过零，$X$ 可以换号。整个过程由(12)在
$Y\ne0$ 下光滑解出，正则偏导 $F_X$ 从未为零。它是实际方程的一条连续 smooth 解，不是将不同 $X$ 支的速度直接粘合。原问题并未要求一个所选坐标 $X$ 在所有后继中永远正；R540 的 $X>0$ 只为那份实际入口和高曲率弧提供了一个不奇异图。

第三 history 始终按
$$
T_s=-M_{\rm raw}\circ A+C(S,j^2S)
\tag{33}
$$
真实积分。每个最终选定的 $B,\tau_B$ 和 ramp 都有限且 smooth，因此原速度、加速度和(33)在有限区间上可积。$T$ 可以很大，不能由(27)推出它趋零或与 scalar 同阶。原初端势、固定 $\chi$、共同右锚、frame/位置和第四成本全部保实际输出。

没有新增母形观察，没有移动共同 cap 或任何包，没有重做原33行，也没有使用 R518 的无 ruling 桥或 R521 的另一份母/Gram。唯一在 R540 允许构造内作的加强，是初选的有限小 $L$ 界及第5节对平台末时刻的任意小真实选择。

## 10. 已付结论与仍欠的总矩

本稿证明一个具体正向事实：同一33母和固定 $\chi$ 上，不只有 $p_1^{\omega_c}$ 的净负输出。完整 ruling 的两个真实正则图还能实现有限的二次矩脉冲；它们使四个预定原矩读出中的一个具有真实双号方向，并给任意有限单矩目标的准确有限解。取零目标时可同时保 R540 的 $k>2$ 和净负 $p_1^{\omega_c}$。

其它矩的代价没有被消去，尤其(32)说明 $t_1$ 问题仍需真正不同的长时或慢控制。全 $M=0$、末 scalar/germ、第三 period、frame/pose 和最终共同规范没有由(31)自动支付。后续必须继续在这同一个真实 history 上处理这些剩余量。

