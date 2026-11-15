# R281：完整观测纤维的解析微包选择与 canonical 零端有限判据

日期：2026-11-15。**完整纸面证明；未执行新的秩计算、尾值评价、求积、符号程序、参数扫描或人工测试。**

本稿从一开始在固定平端因子乘解析前因子的空间中，重新完成 [R277 的真最大秩选择](R277-low-jet-observation-fibers-and-high-jet-energy-control-for-equal-background-circles.md) 与 [R279 的有限频率双能量求根](R279-finite-frequency-fiber-control-pays-both-even-profile-energies.md)。不是把 R274 的特定 EL 母包结论套到任意最大秩母函数，也不把一个已经求得的圆事后换成解析近似。

新构造的每个最终微包准确形如

$$
u(y)=\psi_a(y)\left[
P_0(y)+\sum_{\ell=1}^r a_\ell P_\ell(y)
+zN^{-3}Q(y)\cos(Ny)
\right],
\tag{1}
$$

其中所有 P、Q 都是固定实偶多项式，N 是最后选定的有限整数；括号在两端非零。完整数据 $\mathcal F$ 始终准确保留，R279 的有限 N 真根仍成立。

因此每个真实零端都有 $p=f'=t^{-2}a_e(t)e^{-c_e/t}$，$a_e(0)\ne0$；活动内部的 p 与 $A_H$ 退化有限。结合 [R276 从原 R56 推出的 canonical 界](R276-canonical-fourth-periods-at-analytic-zero-ends-and-finite-first-layer-conditions.md)，本稿再把整个一次层 $T_ef$ 化为有限个准确的有理—三角系数条件。这些条件保全部真实历史，本稿没有评价或支付它们。

## 1. 固定支撑的加权多项式稠密域

固定母支撑 $[-b,b]$，$b>0$，以及一个固定 $a>0$。定义

$$
\psi_a(y)=
\begin{cases}
\exp[-a/(b^2-y^2)],&|y|<b,\\
0,&|y|\ge b.
\end{cases}
\tag{2}
$$

它是实 even $C^\infty$ 紧函数，开支撑内实解析。其对数导数为

$$
\frac{\psi_a'}{\psi_a}
=-\frac{2ay}{(b^2-y^2)^2}.
\tag{3}
$$

令 X 为实 even $C^2(\mathbb R)$、支撑在 $[-b,b]$ 的闭 Banach 子空间，使用原 $C^2$ 范数。所有实际有限 profile 最后仍取 $C^\infty$；X 只用于真实有限维 IFT 所需的连续微分拓扑。

**引理1。** 集合

$$
\mathscr A_a=\{\psi_a P:\ P\in\mathbb R[y]\text{ 为 even 多项式}\}
\tag{4}
$$

在 X 中稠密。

**证明。** 对 $u\in X$，零延拓的 $C^2$ 性给端点距离 $d\downarrow0$ 时

$$
u=o(d^2),\qquad u'=o(d),\qquad u''=o(1).
$$

取两端对称的普通光滑 cutoff，截去宽度 $\delta$ 的端邻域。cutoff 的第 k 阶导为 $O(\delta^{-k})$，上述三式逐项给截断 $u_\delta\to u$ 于 $C^2$。这个步骤不要求 u 原本无限平端。

$u_\delta/\psi_a$ 在支撑内部为 even $C^2$，并因 $u_\delta$ 在端邻域准确为零而可零延拓为整个 $[-b,b]$ 上的 even $C^2$ 函数。先用 even 多项式一致逼近它的连续二阶导，再从0两次积分并匹配零阶值，便得到 even 多项式的 $C^2$ 逼近。最后乘固定光滑 $\psi_a$，在 $C^2$ 中得到 $u_\delta$，再令 $\delta$ 小即得结论。□

该引理只用于在真实函数空间中选参数，不把有限多项式近似误作原积分的准确身份。

## 2. 在这个域中实现真最大 minor

固定 R277 的完整有限多项式观测

$$
\mathcal F:X\longrightarrow\mathbb R^d.
$$

它含三个原二次矩及全部 Gaussian self 的实际平移系数；原 Green 左尾已经在其定义中保留。R277 证明其是原函数数据的 $C^2$ 多项式映射，不是只在一个近似词空间上的呈示。

令 r 为 $D\mathcal F$ 在 X 上达到的最大秩。选一个达到该秩的点及 r 个方向、r 个输出行，其 minor 非零。由引理1同时逼近这个点和有限方向，minor 的连续性给一个

$$
u_*=\psi_a P_*,\qquad e_\ell=\psi_a P_\ell
\tag{5}
$$

及同样非零的真实 minor。所有 $P_*,P_\ell$ 均可取实 even 多项式。因此加权解析域的最大秩就是整个 X 的真最大秩，不是另定义一个可能较小的解析秩。

还可把正则母包选在参考 $\psi_a$ 的任意小 $C^2$ 邻域内。固定(5)的方向和输出行，记其 minor 为 $\Delta(u)$。由于 $\mathcal F$ 是多项式，沿

$$
u_t=\psi_a\{(1-t)+tP_*\}
$$

的 $\Delta(u_t)$ 是 t 的有限多项式，并在 $t=1$ 非零。因此可在任意小正 t 中避开其有限零集。取足够小的这样一个 t，得到

$$
u_0=\psi_a P_0,\qquad \Delta(u_0)\ne0,\qquad
u_0''(0)\ne0.
\tag{6}
$$

这里 $\psi_a''(0)=-2a\psi_a(0)/b^4\ne0$。还可以同时要求

$$
\min_{[-b,b]}P_0>0,
\tag{7}
$$

因为在这个有限多项式直线上 $P_0\to1$ 一致成立。特别两端 prefactor 非零。

固定这个真实 minor 后，在一个 X 的开邻域内秩恒为 r，所选输出 $\mathcal F_*$ 满足

$$
\ker D\mathcal F_*=\ker D\mathcal F.
\tag{8}
$$

于是 R277/R279 的有限纠正可以使用同一组解析方向 $e_\ell=\psi_aP_\ell$。本稿没有主张任意旧母包都正则，也没有给任意外部指定数据 c 构造 $\mathcal F^{-1}(c)$；这里保留的数据是新选真实 $u_0$ 的 $\mathcal F(u_0)$。

## 3. 解析振荡因子不要求虚假的内部紧支撑

R279 选中心 even cutoff，只需它给一个严格正的

$$
K=\int (u_0'')^2\chi^2
$$

以及完整副本聚合后 principal 比值的严格次序。先在参考 $\psi_a$ 的小 $C^2$ 邻域中固定一个普通 cutoff $\chi_0$，使 K 有统一正下界。由引理1，选一个

$$
\chi=\psi_a Q,\qquad Q\text{ 为实 even 多项式},
\tag{9}
$$

足够接近 $\chi_0$ 于 $C^2$，便保同一个严格正下界。

$\chi$ 一般不再支撑在母包内部的某个更小开区间。这没有损害任何已用条件：它仍支撑在整个固定母包内，仍 even，且 K 严格正。不得要求一个非零解析函数同时在活动内部的开放子区间上准确为零。

R279 的真实聚合 principal 公式只用二阶 jets、上述 K、even 性及固定有限副本权。其大正位置的严格比值顺序，在这个选择下原样成立。可先用固定参考邻域的统一界选择最终大正位置与共同合法 I，再在该邻域中取第2节的具体正则 $u_0$。这样没有因选择解析母包而在求根以后搬动一个实际能量零解。

## 4. 完整观测纤维与有限 N 根仍在解析类内

对固定有限幅度盒使用

$$
w_N(z,y)=zN^{-3}\chi(y)\cos(Ny)
=zN^{-3}\psi_a(y)Q(y)\cos(Ny).
$$

用(5)、(8)的真实有限 IFT 纠正所选 r 个坐标，得

$$
u_N(z)=u_0+w_N(z)+\sum_\ell a_{\ell,N}(z)e_\ell,
$$

$$
\boxed{\mathcal F(u_N(z))=\mathcal F(u_0).}
\tag{10}
$$

全坐标恒定的理由仍是(8)及纠正路径的实际导数，不是把未选坐标省掉。固定光滑方向的估计为

$$
|a_{\ell,N}|+|\partial_z a_{\ell,N}|=O(N^{-1}),
$$

$$
u_N'''=u_0'''+z\chi\sin(Ny)+O(N^{-1}),
\qquad
\partial_z u_N'''=\chi\sin(Ny)+O(N^{-1}),
\tag{11}
$$

对预先固定的有限正幅度盒一致成立。

于是原两个完整 bulk 的能量映射仍有 R279 的 $C^1$ 收敛，三个真实向量的严格正 balance 和二维非退化根不变。选择一个足够大的有限整数 N 后，原收缩/IFT 给真实 $L_c=M_c=0$，并按已有一般微包身份得到六个已识别能量零。没有把离散 $1/N$ 当作光滑参数；也没有把 principal 等式当作最后原方程。

重要的是，在整个盒中都有准确分解

$$
u_N(z,y)=\psi_a(y)H_N(z,y),
$$

$$
H_N=P_0+\sum_\ell a_{\ell,N}(z)P_\ell
+zN^{-3}Q\cos(Ny).
\tag{12}
$$

$P_\ell,Q$ 已固定，其在 $[-b,b]$ 上的范数有限。由(7)、(11)，可以在选有限 N 时再要求

$$
H_N(z,y)\ge \frac12\min_{[-b,b]}P_0>0
\quad
(z\text{ 在原盒中},\ |y|\le b).
\tag{13}
$$

这只是对已经允许增大的同一个 N 加一个有限下界，不增加未知方程。因此每个最后根的 prefactor 都是一个在闭支撑邻域实解析的有限三角多项式，且两端准确非零。未受扰动母包取 $H=P_0$，也属同类。

所有真实平移、正宽缩放、非零实幅及完整副本只把(12)作一次固定仿射代入；相应 prefactor 仍为有限频率的指数多项式。最后的频率和全部系数都是固定有限数据。


## 5. 实际零端及内部退化

取最后圆中的任一真实微包。其两方向在该活动区间仍为同一实函数的常数倍；所有非零实际幅和正宽均已固定。令 e 为左端或右端，使用真实向内材料坐标

$$
x=e+\sigma t,\qquad t>0,\qquad \sigma\in\{1,-1\}.
$$

若实际宽缩放为 w，则由(2)的准确分解，

$$
\psi_a(y(e+\sigma t))
=\alpha_e(t)e^{-c_e/t},\qquad
c_e=\frac{aw}{2b}>0,
\tag{14}
$$

其中 $\alpha_e$ 在0邻域实解析且 $\alpha_e(0)>0$。把非零实际幅与(12)的 prefactor 一并写入 $b_e(t)$，有

$$
f(e+\sigma t)=b_e(t)e^{-c_e/t},
\qquad b_e\text{ 实解析},\quad b_e(0)\ne0.
$$

因此真实导数准确为

$$
\boxed{
p=f'=t^{-2}a_e(t)e^{-c_e/t},\qquad
a_e(t)=\sigma\{c_eb_e(t)+t^2b_e'(t)\},\quad
a_e(0)\ne0.
}
\tag{15}
$$

没有将高频项当作较高指数层删除；它与所有有限纠正项都已在同一个 $b_e$ 内。即使 N 很大，它仍是一个已经固定的有限频率。

对原退化算子系数

$$
A_H=6pp''-2(p')^2
$$

直接用(15)，得到

$$
A_H=p^2t^{-4}\{4c_e^2+t\,b_H(t)\},
\tag{16}
$$

$b_H$ 实解析。因此充分靠近每个端点时 $pA_H\ne0$。

活动内部的 f、p、$A_H$ 都实解析。它们不能恒为零，因为(15)–(16)给端邻域非零。去掉这些端邻域后的紧内部，若零点无限则有内部聚点，解析唯一性将迫恒零。故 p 与 $A_H$ 的内部零点都有限，且各为有限阶。

本稿不预设这些零点简单、不列出其实际位置，也不把 p 的零自动视为原二阶方程的奇点。特别 even 母中心可能有 $p=0$ 而 $A_H\ne0$，仍须按原 R225 的准确 Laurent 规则处理。

## 6. 只用 R276 的一般 canonical 原式界

[R276 §1–4](R276-canonical-fourth-periods-at-analytic-zero-ends-and-finite-first-layer-conditions.md) 从 R56 的完整原恢复证明：对任何具有(15)的比例零端、固定真实几何及 canonical 四阶周期目标 G，有准确 germ

$$
\boxed{
G=P_e+T_ef+p^2t^{-4}B_e,\qquad B_e\in C^\infty.
}
\tag{17}
$$

$P_e$ 是相邻真实零平台上原多项式的延拓；$T_e$ 含同一实际输入的真实三次历史尾。本文只调用这个一般原式界，不调用 R276 §5 中 $\psi+\psi^3R$ 的特殊 EL 表示，因为(12)是另一类实际 profile。

准确的一次层可写为

$$
T_ef(x)=
\sum_{\ell=0}^{L}P_\ell^e(x)f^{(\ell)}(x)
+\sum_{j=0}^{J}Q_j^e(x)\int_e^x y^jf(y)\,dy,
\tag{18}
$$

所有 $P_\ell^e,Q_j^e$ 为有限多项式。其系数取最后圆、最后有限 N、原右锚和全部真实 s 历史给出的值。不能用基点 $u_0$ 的尾替代它们，也不能因(10)就推这些新尾不变。

把局部积分写成 $\int_e^x$ 不改变全局右锚。原 $\int_{r_*}^e$ 的数据始终保存在 $P_e$ 及(18)的系数中；未另设一个自由初值。

## 7. 整个一次层的有限有理—三角 iff

### 7.1 终止的消积分运算

记端点正平因子

$$
\psi_e(t)=\psi_a(y(e+\sigma t)),\qquad
f(e+\sigma t)=\psi_e(t)H_e(t).
$$

$H_e$ 是实际(12)的仿射代入并含非零实幅。它是有限指数多项式：多项式加有限个固定频率的正弦、余弦多项式。在当前单频率包中，只需频率 $0,\pm N/w$；不同实际包可有不同但都有限的频率。定义

$$
\lambda_e=\frac{\psi_e'}{\psi_e}\in\mathbb R(t),
\qquad
\mathscr D_e=D_t+\lambda_e
=\psi_e^{-1}D_t\psi_e.
\tag{19}
$$

把(18)换到 t 坐标并吸收 $\sigma$。置

$$
I_j^{H}(t)=\int_0^t s^j\psi_e(s)H_e(s)\,ds,\qquad
R_j^{H}=I_j^{H}/\psi_e.
\tag{20}
$$

这里新上标 H 指实际解析 prefactor，不是几何 Gaussian 函数。准确有

$$
\mathscr D_eR_j^{H}=t^jH_e,\qquad
\mathscr D_e(bR_j^{H})=b'R_j^{H}+b\,t^jH_e.
\tag{21}
$$

令

$$
S_e=\frac{T_ef}{\psi_e}
=A_e(t)+\sum_{j=0}^J b_j(t)R_j^{H}(t).
\tag{22}
$$

其中 $b_j$ 为多项式；$A_e$ 是有理函数系数乘有限频率指数多项式的有限和。后者来自 $\mathscr D_e^\ell H_e$，没有漏掉真实高频导数。

取一个有限整数

$$
n>\max_j\deg b_j
$$

，空和时取 $n=1$。由(21)反复使用乘法规则，所有 $R_j^H$ 的系数最终成为 $b_j^{(n)}=0$。因此

$$
\boxed{
Q_{e,n}:=\mathscr D_e^nS_e
=\psi_e^{-1}D_t^n(T_ef)
\in\sum_{\omega\in\Omega_e}\mathbb C(t)e^{i\omega t},
}
\tag{23}
$$

其中 $\Omega_e$ 是去重后的实际有限频率集。微分与乘有理函数都不增加新频率。

**定理2。** 对这些真实输入及真实尾，

$$
\boxed{
T_ef\equiv0
\quad\Longleftrightarrow\quad Q_{e,n}\equiv0.
}
\tag{24}
$$

**证明。** 右式等价 $D_t^n(T_ef)=0$，所以 $T_ef$ 在该端邻域是次数小于 n 的多项式。式(18)的每个导数和从真实端点起算的矩都全平于 $t=0$，故这个多项式只能为零。反向直接。□

### 7.2 有限个准确系数，不是假定生成元独立

清除(23)所有已知有理分母，得到

$$
d_e(t)Q_{e,n}(t)
=\sum_{\omega\in\Omega_e}\Pi_\omega(t)e^{i\omega t},
\qquad \Pi_\omega\in\mathbb C[t].
\tag{25}
$$

把重复频率先合并后，不同频率的这些项在线性组合中独立。先删除零多项式项。一个直接证明如下：若存在非零 $\Pi_{\omega_0}$ 的零关系，对其施加

$$
\prod_{\omega\ne\omega_0}
(D_t-i\omega)^{\deg\Pi_\omega+1}.
$$

所有其他项被准确消掉；剩下

$$
e^{i\omega_0t}
\prod_{\omega\ne\omega_0}
\bigl(D_t+i(\omega_0-\omega)\bigr)^{\deg\Pi_\omega+1}
\Pi_{\omega_0}(t).
$$

对多项式而言，$D_t+c$ 在 $c\ne0$ 时可逆：其最高非零次项被非零常数 c 保留。所以上式非零，矛盾。这个证明也支付了有理系数的独立性，因为已先统一清分母。

故(24)准确等价

$$
\boxed{
\text{每个 }\Pi_\omega\text{ 的全部有限多项式系数为零。}
}
\tag{26}
$$

系数是实际历史、有限 IFT 参数、固定频率及相位给出的准确实/复数，不一定是有理数。本文没有赋值、求秩或求它们的解。对固定最后圆和固定几何的指定有限线性目标空间，可以统一取其 L、J、n 上界、公共分母及频率并集；这些于是成为作用于同一目标组合的一份有限线性等式，不需要逐候选更换定义。


## 8. 一次层没有非零而全平的隐匿例外

仅有(24)还不够：端点逆解需要知道一个非零一次层确有有限首幂，而不是一个所有渐近系数都为零的非零商。

R276 的精确指数积分 kernel 对实际解析 $H_e$ 仍给

$$
R_j^H\in t^{j+2}C^\infty.
$$

因此 $S_e$ 属于 $t^{-M}C^\infty$ 的某个有限 M 类。$\mathscr D_e$ 只是微分加一个有限极点的有理函数，任何固定次数作用仍属于这样的有限极点光滑类。

若 $t^MS_e$ 全平，则 $\mathscr D_e^nS_e$ 乘足够的有限 t 幂后也全平。但(23)是端点的亚纯解析函数：其指数因子在0解析，有理因子只有有限极点。非零亚纯解析函数必有非零有限 Laurent 首项。因此这个全平的 $Q_{e,n}$ 只能恒零，由(24)得 $T_ef=0$。

同样考虑

$$
S_{e,2}=\frac{D_t^2(T_ef)}{\psi_e}
=\mathscr D_e^2S_e.
\tag{27}
$$

若它乘有限 t 幂后全平，再作用 $\mathscr D_e^n$ 得到
$\mathscr D_e^2Q_{e,n}$，仍是亚纯解析且全平，故恒零。这迫
$D_t^{n+2}(T_ef)=0$；端全平再次迫 $T_ef=0$。

因此当 $T_ef\ne0$ 时，(27)一定有一个非零有限首幂。由(15)中 $p/\psi_e$ 的非退化二阶极点，存在某个整数 $\rho$ 及真实光滑 b，使

$$
\boxed{
(T_ef)''=p\,t^\rho b(t),\qquad b(0)\ne0.
}
\tag{28}
$$

这里双撇仍是物理 x 导数；二阶导数不受左右端的 $\sigma$ 改变。式(28)不要求 $I_j^H/\psi_e$ 的渐近 Taylor 级数收敛；有限终止的(23)已排除了它可能引入的非零全平例外。

## 9. 与真实零端逆解的 iff

为避免与母包 u 混淆，把二阶 gauge 的导数记为 $v=w'$。原退化方程是

$$
(A_Hv')'-V_Hv=G'',\qquad
V_H=6(p'p'')'.
\tag{29}
$$

光滑零端需要原 Lagrange 通量取零端分支。仍保真实平台必要门 $P_e''=0$，并记

$$
F(x)=\int_e^x p(y)G''(y)\,dy,
$$

$$
v(x)=p(x)\left[
C+\int_{x_*}^x\frac{F(y)}{A_H(y)p(y)^2}\,dy
\right].
\tag{30}
$$

所有积分和常数按原右锚恢复；C 是允许的齐次分支，不能替换原目标的历史尾。

若(26)成立，则 $T_ef=0$，由(17)有

$$
G''\in p^2t^{-8}C^\infty.
$$

[R272](R272-smooth-inverse-germs-for-the-full-third-kernel-at-flat-zero-ends.md) 与 R276 的精确 kernel 于是给(30)真实 $C^\infty$ 延拓。这个延拓未必全平；若(17)的二次系数为 $B_e$，端值是
$-B_e(0)/(3c_e^2)$，不同 C 只相差全平项 Cp。

若(26)不成立，则(28)、(17)给

$$
G''=p\,t^\rho b(t)+p^2t^{-8}C^\infty,\qquad b(0)\ne0.
$$

R276 §7 的两次准确 kernel 运算，适用(15)同一个 $c_e$，给

$$
\boxed{
v=-p^{-1}t^{\rho+8}U(t)+Cp+v_2(t),
\quad
U,v_2\in C^\infty,\quad
U(0)=\frac{b(0)}{16c_e^4}\ne0.
}
\tag{31}
$$

左右方向的两个 $\sigma$ 相乘为1。$p^{-1}$ 的指数增长不能由有限次幂、全平 Cp 或光滑 $v_2$ 抵消，故没有光滑零端延拓。

于是对本稿实际有限频率圆、原 canonical 目标，在该端真实平台门及零通量分支已经付清时，

$$
\boxed{
\text{该端逆解为 }C^\infty
\quad\Longleftrightarrow\quad
T_ef=0
\quad\Longleftrightarrow\quad
\text{(25)的全部有限系数为零。}
}
\tag{32}
$$

这是实际函数 germ 的 iff，不是某个任意截断阶数的 Taylor 检查。它只把一个未付问题准确有限化，没有宣称右侧已经成立。

## 10. 全部选择顺序及保留的未付条件

这次兼容性证明采用以下次序。

1. 固定真实 scalar 几何、允许的共振端芽、有限格点及全部完整副本相对布局。选择共同母支撑、固定 $\psi_a$ 及其小 $C^2$ 参考邻域。
2. 用(9)选固定解析振荡因子，保严格正 K。按 R279 的统一界一次选足够大的最终正位置，再固定共同合法 I、collars 和右锚；不扩张一个已经冻结的旧窄 I。
3. 对这个实际完整 $\mathcal F$，用(4)–(8)选择加权解析的真最大秩母包及固定纠正方向。其 prefactor 全区正且 $u_0''(0)\ne0$。
4. 用真实副本能量构造严格正 balance 和有限幅度盒。最后选一个有限整数 N，同时满足 R279 的 $C^1$ 根条件和(13)，在其内部求准确双能量根。
5. 冻结最后 profiles、位置、频率与所有 IFT 系数。之后才提取同一实际 canonical 目标的 $P_e,T_e$；不得继续使用基点母包或另一旧圆的尾值。
6. 以(25)–(26)定义端点的有限系数门。本文不评价这些系数，不计算某个原目标或控制呈示的实际秩，也不据存在公式自动选出控制。

因此可以从一开始把 R277/R279 的新构造放入如下真实类：

- 每个活动包内部解析，相邻开放零平台及共同外 collar 保留；
- 每个零端有(15)的非退化指数 germ；
- 内部 p、$A_H$ 只有有限个有限阶退化点；
- 同一完整 $\mathcal F$ 的全部 Gaussian 数据与原最大秩基点准确相同；
- R279 已付的六个能量条件与36个 odd、30个 even 零同时保持。

单独消费 R277/R279 时，高频或纠正不改变那六条剩余 Gaussian even；其原值仍未由这一步消去。若从最初接入 [R280 的五个最终完整 block](R280-ordered-three-moment-areas-and-five-block-Gaussian-cancellation.md)，则可先固定两个编码模板及五块的实际布局、正四次权，再逐 block 使用本稿的解析同 $\mathcal F$ 有限 N 构造。R280 的权以 $\mathcal A_{01}^{\pm}/m^2$ 归一，中心化参数也不依 m；两个 $\chi$ 的共同 $-\nu$ 项相消，所以 $\chi_--\chi_+$ 不依母包。故这些布局和权确可先定，不与此处真最大秩母包的选择循环依赖。

随后在共同正则解析母包及同一完整数据上，五块各自求得有限 N 根，仍逐包保持原 self、三矩及全部实际平移系数。于是 R280 已付的全部72条 Gaussian 零不变，六能量也同时为零。这里是从一开始同步采用两个存在构造，不是把一个旧光滑圆事后换成解析近似。

无论采用哪个版本，都没有从这些 Gaussian/能量零推出 $P_e''=0$、活动总通量零或(26)；同一新圆的 canonical 原尾仍须实际提取和支付。

对于最终固定圆，[R225](R225-complete-period-range-flat-end-germs-and-finite-observation-quotient.md) 的内部 Laurent 门现在确为有限个：每个内部零点上使用原 $F/(A_Hp^2)$，保允许的低阶极点并消禁止主部与 residue。还须支付全部真实平台条件、活动总通量、这里的端点系数、原右 collar 常数和同一 gauge 的原矩约束。任何进一步 ruling/joint 条件仍作用于同一个真实解，不能各自另选控制。

本稿得到的是一个与新高阶形状纤维真正兼容的解析类别及 canonical 零端有限判据。它没有继承旧 EL 圆的数值尾、没有把 C² 近似当作 period 零的稳定性，也没有宣称完整 period 或完整第四 ruling 已经可解。

