# R108：canonical 紧支流、完整均值列与真实帽能量费用

2026-11-12，independent-audit。

**状态：本篇的完整数学桥接及既有真实系数所导出的费用已证明。**
它给同一个未压缩正帽的合法 primal/dual 对，并准确保留均值、所有角模和
regular 端口。下文的 $R_1$ 是整个试函数的真实残差可去商，包含 cutoff 和
完整主矩阵误差；其新的整领口数值尚未取得。本篇不以已付的乘数代替 $R_1$，
也不宣称全反馈逆已闭合。

## 1. 同一个能量空间和实际范围

实际参数是 R99/R103 的
$$
 \delta_5=-7789843107295549/4611686018427387904,
 \qquad |\delta-\delta_5|\le10^{-9}.
 \tag{108.1}
$$
每个参数使用自己的真实根。采用 R96 已证图，置
$$
 0\le y\le H=49/102400,\qquad
 \phi\in\mathbb R/(\ell\mathbb Z),\qquad \ell=2\pi/q.
 \tag{108.2}
$$
四重模的频率为 $4qk$，$
e_\phi=\ell^{-1/2}$ 是单位常数。全部积分取未归一化的 $dy\,d\phi$；
物理角取 $d\theta$，单位常数 $e_\theta=(2\pi)^{-1/2}$。
因此以下矩阵系数使用正交归一基，不把平均角积分中的矩阵无变换搬来。

写物理 grounded 密度为 $B$，实际坐标变换为 $\Psi$，$J=\det D\Psi>0$。
canonical grounded 密度与 R96 height 为
$$
 A=J^{-1}D\Psi B D\Psi^T,\qquad
 \tau=A_{11}^{-1/2},\qquad C=\tau^2 A.
 \tag{108.3}
$$
实际 $C_{11}=1$；完整 $C_{12},C_{22}$ 保留。若为减少高阶导而另选
根匹配的多项式 height $\tau_*$，则
$C_* =\tau_*^2 A$ 的 $E_{11}$ 一般非零，不能删除。
本篇的 $A$ 及其能量不依赖这种 height 选择。

完整帽是 R69/R74 的同一闭外延，含真实无限尾 Robin 形式。对
$g=(a,\xi)$，其调和延拓 $u_g$ 满足根迹为 $a$、regular 均值为 $\xi$，
非零 regular 模仍服从真实 Robin 条件。R103 的全部 gap/contact 定理
均在这个完整空间使用；没有投影体内方程。

## 2. 真实 inverse-density 常数包含主矩阵扰动

R96 的全部 178 格严格给
$$
 (1-\varepsilon)\operatorname{diag}(1,y)
 \le C\le(1+\varepsilon)\operatorname{diag}(1,y),
 \quad \varepsilon<0.000001552858,
 \quad |\partial_y\log\tau|<G_0=33.417980.
 \tag{108.4}
$$
R99 根乘子给 $\tau(0,\phi)<1.477443$。沿固定 $\phi$ 积分，使用
$e^x\le(1-x)^{-1}$（$0\le x<1$），得到
$$
 \tau(y,\phi)\le T_{\max}
 :=\frac{1.477443}{1-G_0H}<1.501452769655641.
 \tag{108.5}
$$
所以对 $y>0$ 的真实逆矩阵，
$$
 \boxed{\quad
 A^{-1}=\tau^2 C^{-1}
 \le\frac{T_{\max}^2}{1-\varepsilon}
                 \operatorname{diag}(1,y^{-1})
 <2.257\operatorname{diag}(1,y^{-1}).\quad}
 \tag{108.6}
$$
完整系数为 $T_{\max}^2/(1-\varepsilon)<2.254363921$；这里明确支付
了 $C$ 的真实归一化扰动，而非仅以 $T_{\max}^2$ 代替逆矩阵。
若后续改变 height，则仍可使用同一个 $A^{-1}$ 界，但把残差换成
$-\tau_*^{-1}P_*U$ 时须另付 $\tau_*^{-1}$。以上常数仅覆盖(108.2)，
不能转授尚未真正计算的宽图。

## 3. 全角、零外通量的 canonical stream

取一个完整试函数 $U^\dagger$，其准确根残差已消去。取实 cutoff
$\chi$，在根附近为1，在 $H$ 附近恒为0。令
$$
 v=\tau\chi U^\dagger,\qquad
 p=(A\nabla v)_y,\qquad z=(A\nabla v)_\phi,
 \qquad f=p_y+z_\phi=-\tau^{-1}P(\chi U^\dagger).
 \tag{108.7}
$$
必须保留 $P(\chi U^\dagger)$ 中的 $\chi',\chi''$、全部 $E_{ij}$、
height 项及所有角导；本式是完整算子的准确等式。
设 $f(0)=0$，写 $f=y f_1$，用真实径向导数积分定义可去商。
置 $\Pi=I-\langle\cdot,e_\phi\rangle e_\phi$，$\partial_\phi^{-1}$
在非零模上取 multiplier $(4iqk)^{-1}$，在均值上为0。定义
$$
 \boxed{\quad
 j_y=\Pi p,\qquad
 j_\phi=\langle z,e_\phi\rangle e_\phi
                    -\partial_\phi^{-1}\Pi p_y .\quad}
 \tag{108.8}
$$
直接微分给 $\operatorname{div}j=\Pi p_y-\Pi p_y=0$。
$v,p,z$ 在 $H$ 附近全部为0，故 $j$ 亦在该处为0。
把 $(v,j)$ 经真实 Piola 公式
$$
 j_{\rm ph}=J D\Psi^{-1}j
 \tag{108.9}
$$
拉回物理帽并零延拓，就得到完整帽上合法的 primal/solenoidal-dual 对。
(108.9)没有 height 除数，因为 $v$ 已经是真 grounded 函数。
全局 regular trace、regular dual flux 均为0；这不是另设人工外边界条件。

置 $d=A\nabla v-j$、$m=\langle p(0),e_\phi\rangle$。准确有
$$
 d_y=\left(m+\int_0^y s\langle f_1(s),e_\phi\rangle ds\right)e_\phi,
 \qquad d_\phi=\partial_\phi^{-1}\Pi(yf_1).
 \tag{108.10}
$$
因此完整 primal/dual gap 就是
$\mathcal R^2=\int d^*A^{-1}d$；外区以及 Robin mismatch 为准确零。
这保留了 $f$ 的真实均值，并没有要求每层 $\int f=0$。

假设对输入 Hilbert 空间 $\mathscr U$，完整商满足
$$
 R_1=\sup_{0\le y\le H}
 \left\|\frac{P(\chi U^\dagger)(y)}y:
                       \mathscr U\longrightarrow L^2_\phi\right\|<\infty.
 \tag{108.11}
$$
已证 $\tau>1.1568$、$q>9.72$，故由(108.6)、Minkowski 和
$\|\partial_\phi^{-1}\Pi\|\le(4q)^{-1}$，
$$
 \boxed{\quad
 \mathcal R\le c_m\|m\|+c_1R_1,\qquad
 c_m=\sqrt{2.257H},\quad
 c_1=\sqrt{\frac{2.257}{1.1568^2}
       \left(\frac{H^5}{20}+\frac{H^2}{2(4\cdot9.72)^2}\right)} .\quad}
 \tag{108.12}
$$
这里 $H^5/20$ 来自 $\int_0^H(y^2/2)^2dy$，
$H^2/2$ 来自 $\int_0^H y\,dy$，无端点奇异积分遗漏。
严格外舍入给
$$
 c_m<0.032863502030,\qquad c_1<0.000011302184.
 \tag{108.13}
$$
这是一条把**完整**残差可去商接到**完整帽** gap 的算子界。

## 4. 均值列、regular 槽与实际根数据

根处 $C_{11}=1,C_{12}=0$。置
$\mu=(\partial_y\log\tau)|_0$，则
$$
 p(0)=\tau_0^{-1}(U_y(0)+\mu U(0)).
 \tag{108.14}
$$
把 physical root conormal 接回 canonical trace，(108.8) 的 dual 根列为
$$
 d_j^{\rm can}=-(U_y+\mu U)|_0+m\tau_0e_\phi,
 \qquad d_{j,\rm reg}=0.
 \tag{108.15}
$$
因此修正列 $\tau_0e_\phi$ 的全部 Fourier 尾均保留。它不是只有均值行。
若另与携带常通量的完整外部 dual 比较，总通量恒等式是
$\sqrt\ell\,m=\sqrt{2\pi}\,\lambda$，故相应 regular 标量为
$\lambda=m/\sqrt q$。这种比较的 rank-one pair 是
$m(\tau_0e_\phi,-1/\sqrt q)$，不能把第二槽写成 $-m$。
当前紧支构造自身不需要这条尚未支付的外部延拓。

设 $\Gamma$ 在非零模上为 $4q|k|$，$c=\sqrt{\operatorname{Ai}(0)/[-\operatorname{Ai}'(0)]}$，
$A_0=\operatorname{Ai}(0)$、$A_1=\operatorname{Ai}'(0)$，$b=v_1/3$。
R53 的 canonical 根两迹为
$$
 U_0=c A_0\Gamma^{-1/3}-c A_1 M_{v_0}\Gamma^{-5/3},\qquad
 U_y(0)=c A_1\Gamma^{1/3}+c A_1M_b\Gamma^{-5/3}.
 \tag{108.16}
$$
乘法在左，频率乘子在右。任意保持两根迹的 completion 均保留(108.16)。
置 $h_1=e_\phi/\tau_0$、$h_2=e_\phi\mu/\tau_0$。内积取第一变量线性，
实际均值泛函准确为
$$
 \begin{split}
 m(u)={}&cA_1\langle\Gamma^{1/3}u,h_1\rangle
       +cA_1\langle\Gamma^{-5/3}u,bh_1\rangle\\
       &+cA_0\langle\Gamma^{-1/3}u,h_2\rangle
       -cA_1\langle\Gamma^{-5/3}u,v_0h_2\rangle .
 \end{split}
 \tag{108.17}
$$
全部输入和输出均使用上述正交归一基。R99 的平均角标量乘子界作为
$L^\infty$ 或 Wiener 乘子界不变；单位常数使 $\|h_1\|_2\le\|1/\tau_0\|_\infty$。
涉及 T0 的矩阵若从两个平均角基转到两个正交归一基，须乘 $\sqrt q$，
正是 R103 末节的归一；(108.17)已直接在正确基中推导。

取完整实际上界
$$
 \begin{gathered}
 I_0=.831,\ I_1=1.489006,\ M_0=24.940215,\ M_1=31.245346,
 \quad Y_*=.055953,\\
 L_1=I_1/Y_*,\quad H_2=I_0M_0,
 \quad L_2=(I_0M_1+M_0I_1)/Y_*,\\
 B_0=692327,\ B_1=143113,\quad V_0=5176,\ V_1=1186,\quad
 D_b=40B_1,\ D_v=40V_1.
 \end{gathered}
 \tag{108.18}
$$
$I_1,M_1$ 是真实物理角一阶 Wiener 界；除以真实 $Y_0'$ 的下界得到
canonical 导数。$B_1,V_1$ 是 canonical index 的完整一阶矩，$4q<40$。
由 $c|A_1|<.39,cA_0<.54$、对均值测试函数先取一阶导数、再用高频谱下界，
得到对 $P_{>K}$、$\Lambda<4q(K+1)$，
$$
 \boxed{\quad
 \|mP_{>K}\|\le
 .39 L_1\Lambda^{-2/3}+.54L_2\Lambda^{-4/3}
 +.39(D_bI_0+B_0L_1+D_vH_2+V_0L_2)\Lambda^{-8/3}.
 \quad}
 \tag{108.19}
$$
例如第一项用
$\|\Gamma^{1/3}P_{>K}h_1\|\le\Lambda^{-2/3}\|\partial_\phi h_1\|$。
其余三项完全相同。这是完整 rank-one 泛函的算子界，不删低输出或跨号。

## 5. 已付实际 gap/contact 系数

结合 R96 的完整 harmonic extension 能量及 R103 的 gap/contact 恒等式，
对 canonical 高输入 $P_{>K}$ 有下表。每格是严格向上舍入；root+regular
一列始终保留 regular 均值测试，不是把它压缩掉。

| $K$ | $\|mP_{>K}\|$ 上界 | 高根 contact 的均值费 | 高根 contact 的 $R_1$ 系数 | 高根与 regular 联合均值费 | 联合 $R_1$ 系数 |
|---:|---:|---:|---:|---:|---:|
|64|.083628975067|.010060689544|.000041373238|.022040469289|.000090638477|
|128|.044138082420|.004205985993|.000032771996|.011171990215|.000087049368|
|256|.025473398447|.001924866798|.000025987370|.006275788157|.000084728579|

本表由同族五个完整有向报告作准确有理数组合；原始文件身份和所有通过检查
写在 `notes/2026-11-12-R108-canonical-stream-gap-budget.json`。
重建后的原生入口是 `scripts/fourfold_phase_canonical_stream_gap_budget.py`。
该程序验证源报告 SHA、参数域、完整 v0/v1 一阶矩、根乘子及主矩阵费用；
不会重采样一个未覆盖的几何域。执行报告另明确
`proved_new_full_cap_gap=false`。

## 6. 保强阶的根 completion：必须在输入侧局部化

R103 的固定 $y^2R_0/2$ completion 保持 Cauchy 两迹并准确消根残差；
但若直接用于无穷高输入，不能据此免费声称仍有原来的 source gain。
一个保留 Airy 尺度的选择是
$$
 U^\dagger(y)=U(y)+\frac{y^2}{2}R_0
                \frac{\operatorname{Ai}(y\Gamma^{2/3})}{A_0}.
 \tag{108.20}
$$
Airy multiplier 始终作用在输入右侧。它在根为 $I$，故(103.7)的根
消去和两迹保持仍准确成立；正轴 $0<\operatorname{Ai}(z)/A_0\le1$
使 R103 已付的 $C^0_yL^2$ completion 幅度不增加。

对真正 canonical 的 $B=-v_0+yb$、$C_+=y^2(v_0)_\phi/2$，
(108.20)的虚部准确消去原 $i\epsilon C_+/\lambda$ 项。因此逐输入列为
$$
 U_k^\dagger=c\lambda^{-1/3}e^{i\epsilon\lambda\phi}
 \left[\operatorname{Ai}(z)+\lambda^{-4/3}B\operatorname{Ai}'(z)
 +\kappa_A y^2\lambda^{-4/3}v_0^2\operatorname{Ai}(z)\right],
 \quad z=y\lambda^{2/3},\quad \kappa_A=A_1/(2A_0).
 \tag{108.21}
$$
这是列公式；不能把左侧的 $M_{v_0}$ 与右侧 $\Gamma$ 交换。
所有新增项的两个径向导数、自由 Airy 抵消以及角向交叉均可由 R47 的
完整 lag 求和验证。对 $y^2\lambda^{-r}\operatorname{Ai}(z)$，径向二阶
最坏的 $L^2_y$ gain 是 $r+1/3$，此处 $r\ge4/3$，故不低于 $5/3$。
这只识别准确阶数；所需的实际系数范数仍要付。

为避免在根除以一个含零的区间，可把残差根抵消写成同一 Airy 函数。
置 $D=y^2v_0^2$，$\mathcal L=-\partial_y^2-y\partial_\phi^2+V$，
$\Delta B=V-B-2yB_y$。不含 $E$ 的完整残差为
$$
 \begin{split}
 P_0U_k^\dagger=c e^{i\epsilon\lambda\phi}\{&
 \lambda^{-1/3}\Delta B\operatorname{Ai}(z)
 +\kappa_A\lambda^{-5/3}\mathcal LD\operatorname{Ai}(z)
 -2i\epsilon\kappa_A\lambda^{-2/3}yD_\phi\operatorname{Ai}(z)\\
 &+\lambda^{-5/3}\mathcal LB\operatorname{Ai}'(z)
 -2i\epsilon\lambda^{-2/3}yB_\phi\operatorname{Ai}'(z)
 -2\kappa_A\lambda^{-1}D_y\operatorname{Ai}'(z)\}.
 \end{split}
 \tag{108.22}
$$
其中 $\Delta B=y^2V_2$，$V_2=(V+v_0-yv_1)/y^2$。
两项根常数组合成
$$
 v_0^2\lambda^{-5/3}
 \left[\operatorname{Ai}'(z)-(A_1/A_0)\operatorname{Ai}(z)\right]
 =y v_0^2\lambda^{-1}K(z),
 \quad K(z)=\frac{\operatorname{Ai}'(z)-(A_1/A_0)\operatorname{Ai}(z)}z.
 \tag{108.23}
$$
$K$ 在0解析。R96 的正轴 Airy 界给
$$
 |K(z)|\le2(1+z)^{1/4}e^{-2z^{3/2}/3},\qquad z\ge0.
 \tag{108.24}
$$
证明：当 $z\ge1$，分别用 $\operatorname{Ai}$、$\operatorname{Ai}'$ 的
R96 界及 $|A_1/A_0|<6/5$；两项除以 $z$ 后均不超过右侧。
当 $0\le z\le1$，令分子为 $W(z)$，$W(0)=0$，
$W'=z\operatorname{Ai}-(A_1/A_0)\operatorname{Ai}'$。
正轴单调性及 $A_0<.36,|A_1|<.26$ 给 $|W'|<.672$。
右侧在此段不小于 $2e^{-2/3}>1$，故成立。
$|A_1/A_0|<6/5$ 可直接由 R96 的有向初值证书，或
$A_0>2/9,|A_1|<.26$ 得到。

完整 $P$ 还须加入 $-\operatorname{div}(E\nabla U^\dagger)$，再加入全部
cutoff 项；本篇没有把它们写成零。若另选 $\tau_*$，还包括真实 $E_{11}$。
(108.22)–(108.24)提供实际 $R_1$ 积分可实现的无根相消表达，
其连续全角/径向预算是本篇之后继续支付的工作。

## 7. 已完成范围和下一真实输入

已完成的是同一个完整帽的紧支 dual、均值和 regular 正确接线、真实
$A^{-1}$ 扰动因子、完整高输入均值列，以及由它们导出的 contact 系数。
要把本篇用于强反馈，仍须真正给出(108.11)或更细的整领口加权 gap、
所需角向强窗口及与 R98/R99 根 frame 的同一规范接合。
不能用一块局部 pilot、根 Taylor 值或仅 $\chi=1$ 的内部残差替代它们。
