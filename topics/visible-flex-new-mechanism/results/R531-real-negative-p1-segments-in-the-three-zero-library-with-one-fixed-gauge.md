# R531：三平方系数全零母库中的实际负 $p_1$ 子段与同一固定规范

日期：2026-11-16。**完整原式纸面构造；没有执行符号、数值、profile、秩、开发检查或新的科学任务。**

[R529](R529-fixed-nonzero-quadratic-leaves-and-the-real-positive-matrix-increment.md) 已说明：沿固定非零三矩平方零叶走动，不能由原 $k=0$ 常态取得矩阵返回。[R527](R527-finite-amplitude-same-gauge-ruling-paths-with-complete-matrix-memory.md) 的那条有限幅族也有严格正的实际总 $p_1$。

本文改用同一种从起点加强选择的 R520 母库，但令三个**完整**平方系数全部为零。它给一条真正的正向结论：在一个同源母、一个固定第二规范 $w_\theta=0$、一个固定第三规范 $\chi_\theta$ 上，从真实常态前缀平滑出发，存在完整全相位 ruling 为零的实际路径，其末端原 $p_1$ 密度严格为负；因而同一实际路径包含一个具有严格负 $p_1$ 增量的正长度子段。

这个子段不是由任意几何轨道代入后宣称可实现。它由原完整速度反馈、真实八矩 ODE、两个实际高度脉冲以及一个标量隐函数修正构成。所有入射矩阵和第三历史均从常态前缀传入，不重置。

也必须保留尺度边界：整个小脉冲的总 $p_1$ 仍为正二阶量，负子段没有自动配平它，更没有支付其余七矩、末 scalar germ、frame、位置、period 或同一十三行。本文取得的是在同 $K=0$ 可达路径中真实改变 $p_1$ 密度符号的入口，后继闭路仍须使用这些实际输出继续构造。

## 1. 同一个从起点选择的三零母库

使用 [R520](R520-variable-mother-constant-ruling-and-same-gauge-nonconstant-local-departure.md) 与 R527 的可变母库类型。共同外 cap、宽度、四正常、完整有限低阶纤维 $\mathcal F_{\rm path}$、全部 $W$ outer、真实 copy、三矩以及原二十个指定目标均保留。特别，不对整圆作统一幅度缩放，不改变原 $d_f(P)=\eta_P\ne0$ 的数值。

固定
$$
S_c=(h_c,0,\omega_c),\qquad h_c>0,\quad \omega_c\ne0,
\qquad x+\omega_c>0\quad(x\in I).
\tag{1}
$$
令
$$
M_c=M_{\rm raw}(S_c,0,0),\qquad
A_c=\Phi_{M_c}
=-\frac{R_{x+\omega_c}}{8h_c^2}-\frac{T_{x+\omega_c}}8.
\tag{2}
$$
原完整配对的三个平方系数为
$$
q_j(A)=
-I_j(AD,AD)+2I_j\{\phi,A(\phi,AD)\},\qquad j=0,1,2.
\tag{3}
$$
这里 $\phi=g$、$D=f\odot f-g\odot g$；每个槽、右锚与真实左尾均与 R527 相同。

本次从起点规定
$$
\boxed{q_0(A_c)=q_1(A_c)=q_2(A_c)=0.}
\tag{4}
$$
这不是沿 R527 的非零 $\kappa$ 零叶改变已有 profile。可直接使用该稿第2、3节的三十行正根：将其中三条 $q_j(A_c)$ 的目标改为零，仍取
$$
\mathcal A_3=\mathcal A_4=0,\qquad
\mathcal B_j=-\Lambda x_0^j,\quad 0\le j\le4.
$$
其三十行 principal 独立性不使用三个 $q_j$ 目标非零；完整 $C^2$ 余项、同点四正常与限制最大 minor、严格正幅盒和有限 $N$ 原根亦原样保留。这里先取一个足够大的**有限** $\Lambda$，再取足够大的有限频率，所有原二十数值保持原值。

R527(12)在 $S_c$ 给
$$
\ell_k(S_c)
=\frac{\Lambda Q_c(x_0)^2}{64h_c^6}+O(1)>0,
\qquad Q_c(x)=1+h_c^2(x+\omega_c)^2.
$$
$O(1)$ 是同一固定 $C^2$ 小邻域中完整低阶余项的界，不随 $\Lambda$ 增长。因此本次实际母可同时满足
$$
\boxed{a:=\ell_h(S_c)\in\mathbb R,\qquad b:=\ell_k(S_c)>0.}
\tag{5}
$$
不强制 $b=1$，不在完成二十目标以后归一整圆。

以下冻结这个母和所有实际包装。本文不混用 R521 的另一 O(2) 母库，也不把 R518 的成本截面当作本路径上的点态 ruling。

## 2. 完整原方程及三条真正可选的第三 Gram 数据

记
$$
S=(h,k,\omega),\quad d=h\omega-k,\quad
\gamma=h_s,\quad \upsilon=k_s,\quad
\omega_s=\frac{\upsilon}{2h}.
$$
按 R520/R527，全部相位的原 ruling 是 $\sin^2\theta$ 乘同一个完整标量
$$
\boxed{
F_\nu(S,m,\gamma,\upsilon)
=\mathcal R_0(S,\gamma,\upsilon)
-2\mathbf w(S)\cdot\nu
+\mathcal L_S(\Phi_mD)+q_S(\Phi_m),
}
\tag{6}
$$
$$
\mathbf w(S)=
\left(\frac{1+d^2}{4h},\frac d2,\frac h4\right),\qquad
q_S(A)=\frac{(1+d^2)q_0(A)+2hdq_1(A)+h^2q_2(A)}{4h}.
\tag{7}
$$
$\mathcal R_0$ 保含 local 恢复、原 $M_{\rm raw}D$ chain、当前与真实初端的商势差。它不依赖累计 $m$。原两加速度系数由同一 $\mathcal F_{\rm path}$ 完整消去，不作为控制。

定义
$$
r(S)=\mathcal R_0(S,0,0),\qquad r_c=r(S_c).
$$
原 R520 第9节的分量奇偶及 R73 速度表给
$$
D_{(\gamma,\upsilon)}\mathcal R_0(S_c,0,0)=0,\qquad
D_{(\gamma,\upsilon)}M_{\rm raw}(S_c,0,0)=0.
\tag{8}
$$
第二式的原速度项只有 $\gamma^2,\gamma e_s,e_s^2$。下文用的是这些完整身份，不是忽略小速度。

选择一个任意固定数 $\alpha>0$。我们一次选择 $\nu$，使
$$
\begin{aligned}
2\mathbf w_c\cdot\nu&=r_c,\\
2\mathbf w_h\cdot\nu&=r_h-b\alpha,\\
2\mathbf w_e\cdot\nu&=r_e,
\end{aligned}
\tag{9}
$$
其中各偏导都在 $S_c$ 取值，
$$
r_e=\left(\partial_k+\frac1{2h_c}\partial_\omega\right)r,
\qquad
\mathbf w_e=
\left(\partial_k+\frac1{2h_c}\partial_\omega\right)\mathbf w .
$$
这不是三条未经证明可调的 profile 观察；它只是原第三齐次规范的三个真实 Gram 参数。

直接由(7)得
$$
\begin{aligned}
\mathbf w_c&=\left(
\frac{1+h_c^2\omega_c^2}{4h_c},
\frac{h_c\omega_c}{2},\frac{h_c}{4}\right),\\
\mathbf w_h&=\left(
\frac{\omega_c^2-h_c^{-2}}4,\frac{\omega_c}2,\frac14\right),\\
\mathbf w_e&=\left(-\frac{\omega_c}4,-\frac14,0\right).
\end{aligned}
\tag{10}
$$
三行行列式准确为
$$
\boxed{\det(\mathbf w_c,\mathbf w_h,\mathbf w_e)=\frac1{32h_c}>0.}
\tag{11}
$$
例如第一行减 $h_c$ 倍第二行成为 $(1/(2h_c),0,0)$，余二阶行列式为 $1/16$。故(9)有唯一有限解。

令 $r_\nu=r-2\mathbf w\cdot\nu$。本次三个完整条件准确是
$$
\boxed{
r_\nu(S_c)=0,\qquad
(r_\nu)_h(S_c)=b\alpha>0,\qquad
\left(\partial_k+\frac1{2h_c}\partial_\omega\right)r_\nu(S_c)=0.
}
\tag{12}
$$

按 R47/R56/R520 的同一紧 Gram 右逆，固定一次相位光滑、周期、双 collar 紧的 $\chi_\theta$，满足
$$
\mathbf I(\phi_\theta,\chi_\theta)=\sin^2\theta\,\nu,
\qquad \chi_0=\chi_\pi=0.
\tag{13}
$$
整个后续路径都使用这个 $\chi_\theta$ 与 $w_\theta=0$。没有在高度脉冲、末端修正或负子段上重新选规范。本文没有将(9)移植到一个已被别的十三行锁定的 $\nu$ 上；同一十三行的最终安装仍未支付。

## 3. 真实常态前缀和原反馈分支

由(4)，对所有允许当前 $S$ 都有
$$
q_S(A_c)=0.
\tag{14}
$$
所以(12)第一式使任意有限正长度的原常态前缀逐点满足全相位 $K=0$。冻结一个有限长度 $T_0>0$。末端原输入为
$$
S=S_c,\qquad m=T_0M_c,\qquad
T=-\frac{T_0^2}{2}A_c\circ A_c,
\tag{15}
$$
并保固定(13)的第三齐次场。矩阵 $M_c^2=0$ 不代表算子 $A_c\circ A_c=0$；这里不删除第三历史。

将脉冲区间记为 $s\in[0,L]$。零控制的真实基准为
$$
S_0(s)=S_c,\qquad m_0(s)=(T_0+s)M_c.
$$
由(5)(8)，
$$
\boxed{
\partial_\upsilon F_\nu(S_c,(T_0+s)M_c,0,0)
=(T_0+s)b>0.
}
\tag{16}
$$
因此在固定短窗与一个固定小控制盒内，同一有限维 IFT 给光滑分支
$$
\upsilon=G(S,m,\gamma),
$$
并在整段基准上取零。实际路径始终解
$$
\begin{aligned}
h_s&=\gamma,\\
k_s&=G(S,m,\gamma),\\
\omega_s&=\frac{G(S,m,\gamma)}{2h},\\
m_s&=M_{\rm raw}\{S,\gamma,G(S,m,\gamma)\}.
\end{aligned}
\tag{17}
$$
第三历史按原 R73/R482 同步传递，frame 与位置按原方程同步恢复。右侧没有将八矩换成常数或任意目标。

下面所有端口、面积和积分均来自(17)的同一个解族。

## 4. 完整一阶响应只投影一个矩阵组合，不删除八矩

令 $x(s)$ 是一个真实高度输入的一阶变化；令 $y(s)=\delta k(s)$。入口全固定，真实水平式的线性化给
$$
\delta\omega(s)=\frac{y(s)}{2h_c}.
\tag{18}
$$
设 $\delta m(0)=0$。由(8)，它准确满足
$$
(\delta m)'=
M_hx+\left(M_k+\frac{M_\omega}{2h_c}\right)y,
\tag{19}
$$
这里 $M_h,M_k,M_\omega$ 是原静态密度 $M_{\rm raw}(S,0,0)$ 的真实偏导。

记(7)平方型的对称极化为 $b_S(\cdot,\cdot)$，并定义
$$
z(s)=2b_{S_c}(A_c,\Phi_{\delta m(s)}),
$$
$$
c_h=2b_{S_c}(A_c,\Phi_{M_h}),\qquad
c_k=2b_{S_c}\left(A_c,\Phi_{M_k+M_\omega/(2h_c)}\right).
\tag{20}
$$
因此
$$
z'=c_hx+c_ky.
$$
其它七个线性组合仍由(19)原样积分；(20)只是因为一阶 ruling 只读取这一个组合，而不是宣称其它矩阵分量消失。

完整(6)的线性化为
$$
(T_0+s)(ax'+by')
+b\alpha x+2(T_0+s)b_{S_c}(A_c,\Phi_{\delta m})=0.
$$
这里 $q_S((T_0+s)A_c)$ 对 $S$ 的导数因(14)全零；固定初端势与规范的状态导数则已经完整进入(12)，未删去。于是
$$
\boxed{
by'+ax'+\frac{b\alpha}{T_0+s}x+z=0,\qquad
z'=c_hx+c_ky,\qquad y(0)=z(0)=0.
}
\tag{21}
$$
令
$$
v=y+\frac abx,\qquad C_0=c_h-\frac ab c_k.
$$
当 $x$ 在入口为零时，(21)等价于
$$
\boxed{
v'=-\frac{\alpha}{T_0+s}x-\frac zb,\qquad
z'=C_0x+c_kv,\qquad v(0)=z(0)=0.
}
\tag{22}
$$
这一有限系统仅用于精确读取真实解族的一阶导数，不替代(17)来作实际路径。

## 5. 短窗中的严格有向面积

以下 $L^2$ 范数都在 $[0,L]$ 上。Volterra 积分算子的范数不超过 $L$，故(22)给
$$
\|v\|_2\le L\left(\frac{\alpha}{T_0}\|x\|_2+\frac{\|z\|_2}{b}\right),
$$
$$
\|z\|_2\le L\left(|C_0|\|x\|_2+|c_k|\|v\|_2\right).
$$
先取足够短的固定正 $L$，使
$$
\frac{L^2|c_k|}{b}\le\frac12.
$$
则
$$
\boxed{
\|z\|_2\le
2L\left(|C_0|+\frac{L|c_k|\alpha}{T_0}\right)\|x\|_2.
}
\tag{23}
$$

对任意 $x\in C_c^\infty(0,L)$，原端点给
$$
\begin{aligned}
\mathcal A(x)
:=\int_0^L yx'\,ds
&=\int_0^L vx'\,ds\\
&=\int_0^L\frac{\alpha x^2}{T_0+s}\,ds
+\frac1b\int_0^Lzx\,ds .
\end{aligned}
\tag{24}
$$
第一步用 $\int xx'=0$；第二步只对这个真紧控制 $x$ 分部积分，未对原 profile 的非紧尾操作。

进一步缩短 $L$，使
$$
\frac{2L}{b}\left(|C_0|+\frac{L|c_k|\alpha}{T_0}\right)
\le\frac{\alpha}{2(T_0+L)}.
$$
结合(23)得到
$$
\boxed{
\mathcal A(x)\ge
\frac{\alpha}{2(T_0+L)}\|x\|_2^2>0
\quad(x\ne0).
}
\tag{25}
$$
这是同一个固定母、同一个固定 $\nu$、同一个真实前缀的一阶响应事实；不是假设可任意选择曲率。

## 6. 两个真实控制脉冲的有限选择

定义端口线性泛函
$$
\mathcal E_L(x)=y_x(L).
$$
它不是零泛函。确切地，取一个非负、非零的固定
$\psi\in C_c^\infty(0,1)$，令 $\psi_L(s)=\psi(s/L)$。由(22)(23)，当选择的 $L$ 足够小时，
$$
\mathcal E_L(\psi_L)
=-\frac{\alpha L}{T_0}\int_0^1\psi(t)\,dt+O(L^2)\ne0.
\tag{26}
$$
这里的余界只由已经冻结的有限常数与 $\psi$ 给出；它不是数值近似。可在选定 $L$ 时同时满足(23)、(25)、(26)。

再取一个与 $\psi_L$ 线性无关的真紧光滑函数 $\varphi_L$，例如取互不相交的内部支撑。置
$$
\boxed{
x_0=\varphi_L-
\frac{\mathcal E_L(\varphi_L)}
     {\mathcal E_L(\psi_L)}\psi_L .
}
\tag{27}
$$
于是
$$
x_0\ne0,\qquad y_{x_0}(L)=0,\qquad
\mathcal A_0:=\mathcal A(x_0)>0.
\tag{28}
$$
(27)只用两个实际光滑控制及其真实一阶端值；没有调用新的矩阵秩、profile 秩或未证明的多端口满射。

以下简写 $\psi_L=\psi$。将真实高度直接指定为
$$
\boxed{h_{\varepsilon,\zeta}(s)=h_c+\varepsilon x_0(s)+\zeta\psi(s).}
\tag{29}
$$
两个控制均在两端开放 collar 为零。因此高度始终在这些 collars 精确等于 $h_c$。对一个足够小的固定参数盒，$h>0$，并且(17)的同一个解分支在整个 $[0,L]$ 存在、光滑依赖于 $(\varepsilon,\zeta)$，保持原合法物理窗口。

前缀不随 $(\varepsilon,\zeta)$ 改变。实际几何的全部初端 jets 因控制平坦及 ODE 唯一性与该前缀平滑相接。

## 7. 真水平面积与一个准确末端修正

记(17)(29)的实际末态为
$$
k_L=k(L),\qquad \omega_L=\omega(L),\qquad h_L=h_c.
$$
定义真正的末端水平偏移
$$
\boxed{
\delta_L=\omega_L-\omega_c-\frac{k_L}{2h_c}.
}
\tag{30}
$$
原 $k(0)=0$、$\omega_s=k_s/(2h)$ 和 $h_L=h_c$ 给准确身份
$$
\boxed{
\delta_L=\frac12\int_0^L\frac{k h_s}{h^2}\,ds.
}
\tag{31}
$$
没有把 $\omega_L-\omega_c$ 与 $\delta_L$ 混同；后一项明确扣除了真实末曲率。

考虑一个标量端口
$$
\mathcal G(\varepsilon,\zeta)=k_L-h_c\delta_L
=\frac32k_L-h_c(\omega_L-\omega_c).
\tag{32}
$$
在零参数处，(18)给 $\delta\delta_L=0$，所以
$$
\mathcal G_\varepsilon(0,0)=y_{x_0}(L)=0,\qquad
\mathcal G_\zeta(0,0)=\mathcal E_L(\psi)\ne0.
$$
普通一维 IFT 给同一固定小盒内的光滑函数
$$
\zeta=\zeta(\varepsilon),\qquad
\zeta(0)=\zeta'(0)=0,
$$
使
$$
\boxed{k_L=h_c\delta_L}
\tag{33}
$$
对所有足够小的 $\varepsilon$ **准确**成立。没有仅把一阶端值设成零代替(33)。

将 $\zeta(\varepsilon)=O(\varepsilon^2)$ 与实际解的一阶导数放回完整(31)，得到
$$
\boxed{
\delta_L(\varepsilon)
=\frac{\varepsilon^2}{2h_c^2}
\int_0^L y_{x_0}x_0'\,ds+O(\varepsilon^3)
=\frac{\varepsilon^2\mathcal A_0}{2h_c^2}
+O(\varepsilon^3)>0.
}
\tag{34}
$$
此处 $L,T_0$、母、$\chi$ 和两个控制先全部固定，再取足够小的非零 $\varepsilon$。余项来自同一有限 ODE 解族的参数 Taylor 展开，未丢原八矩对该解的影响。

## 8. 原固定坐标中的严格负密度和真实负子段

始终使用同一个 $y=x+\omega_c$ 坐标。R73/R524 的真实原矩阵密度是
$$
p_1^{\,\omega_c}=k^2-kh(\omega-\omega_c).
\tag{35}
$$
由(30)(33)，末态准确满足
$$
h_L=h_c,\qquad
k_L=h_c\delta_L,\qquad
\omega_L-\omega_c=\frac32\delta_L.
$$
故
$$
\boxed{
p_1^{\,\omega_c}(L)
=-\frac{h_c^2}{2}\delta_L^2<0.
}
\tag{36}
$$
这是真实原 $M_{\rm raw}$ 的一条坐标，不是扣掉端势后的替代量。

实际路径光滑，故其末端附近有一个正长度子区间，使(35)处处严格为负。它可以取在(29)的末高度 collar 内；若需要把末端放在子段内部，也可将自由高度控制保持为零并按(17)短暂继续。由同一个反馈分支的局部存在性和连续性，
$$
\boxed{\int_{s_1}^{s_2}p_1^{\,\omega_c}(s)\,ds<0}
\tag{37}
$$
在这个**真实连接着前缀和脉冲**的子段上成立。

这里的子段入值是(17)的实际 $m,T$，没有在 $s_1$ 重新设零。子段长度可依赖已经选定的非零 $\varepsilon$；不宣称它在 $\varepsilon\to0$ 时有统一正下界。高度 collar 也不是完整 scalar 常态 germ：$k_s$、$\omega_s$ 仍由(17)决定。

与此同时，沿全部前缀、脉冲和该短继续段，
$$
F_\nu=0,\qquad \mathscr K(s,\theta)=\sin^2\theta F_\nu=0
$$
是准确的全相位身份。两加速度是实际 ODE 的导数，其完整系数早已由同一母纤维消去，未额外控制它们。

## 9. 完整账目：为什么这还不是矩阵返回

负子段不能替换整条路径的总矩。实际上，在原脉冲 $[0,L]$ 上，
$$
k(s)=\varepsilon y_{x_0}(s)+O(\varepsilon^2),\qquad
\omega(s)-\omega_c=
\frac{\varepsilon y_{x_0}(s)}{2h_c}+O(\varepsilon^2).
$$
因此原(35)给
$$
\boxed{
\int_0^L p_1^{\,\omega_c}\,ds
=\frac{\varepsilon^2}{2}\int_0^L y_{x_0}^2\,ds
+O(\varepsilon^3)>0.
}
\tag{38}
$$
$\mathcal A_0>0$ 使 $y_{x_0}$ 不恒为零。真实常态前缀的 $p_1$ 密度为零，所以把前缀也加入不改变(38)的严格正号。式(36)的负值是四阶小量，与(38)没有冲突。

其它七矩、第三传递、完整第四成本、frame 与位置均按原方程保留。特别，本稿没有：

- 宣称整个脉冲或 prefix 加脉冲为 $M=0$；
- 宣称负子段可在任意入值上无代价重复；
- 将负 $p_1$ 的单坐标修正升为八矩满射；
- 宣称完整常态末 germ、period、十三行或 pose 已经闭合。

本文真正新增的是：R529 的点态非负号不再困住三零母库的实际同规范可达路径。原 $K=0$ 反馈确能带着真实 history 到达 $p_1<0$ 区域。下一步须从这个实际末态继续放大或配平负增量，同时控制其余七矩与固定 $\chi$；不能由一个瞬时负值推断全闭词。

## 10. 平滑切换后真正保持负密度的控制坐标

末端负值还给一个实际继续规则，但不能在 $L$ 直接把新密度控制改为常数而冒称全 germ 已匹配。以下明确完成同一真实解的平滑过渡。

记
$$
\eta=\omega-\omega_c,\qquad P(S)=p_1^{\,\omega_c}=k^2-kh\eta.
$$
原水平关系准确给
$$
\boxed{
P_s=\left(\frac{3k}{2}-h\eta\right)\upsilon-k\eta\,\gamma.
}
\tag{39}
$$
在整个 $P<0$ 区域，$k\ne0$ 且 $k\eta>0$。因此可将原自由高度速度改写成一个真实密度控制 $\sigma=P_s$：
$$
\gamma=R(S)\upsilon-\frac{\sigma}{k\eta},
\qquad
R(S)=\frac{3k/2-h\eta}{k\eta}.
\tag{40}
$$
这只是原两个速度之间的准确可逆改写，没有增加一个独立控制。

在(36)的真实末态，
$$
h\eta=\frac32k,\qquad R=0.
$$
由于原高度脉冲在末 collar 平坦，实际末速度有 $\gamma=0$，从而由(39)也有 $\sigma=0$。把(40)代入同一个完整 $F_\nu$，其关于 $\upsilon$ 的导数为
$$
\mathscr D=
\partial_\upsilon F_\nu+R(S)\partial_\gamma F_\nu.
\tag{41}
$$
在这个实际入口，$\mathscr D=\partial_\upsilon F_\nu>0$。故一个局部 IFT 只是同一原解集的坐标改写，给
$$
\upsilon=\widetilde G(S,m,\sigma),\qquad
\gamma=R(S)\widetilde G-\frac{\sigma}{k\eta}.
\tag{42}
$$
原 $\omega_s=\upsilon/(2h)$、$m_s=M_{\rm raw}$、第三历史、frame 和位置仍同时积分。

先保持原控制 $\gamma=0$，从 $L$ 按(17)真延续一小段，记这份参考解为 $(S^{\rm old},m^{\rm old})$，并读取其**实际**
$$
\sigma_{\rm old}(s)=\frac d{ds}P(S^{\rm old}(s)).
$$
由于 $P(S^{\rm old}(L))<0$ 和(41)在 $L$ 为正，可取一个固定的充分短过渡长度 $\tau_{\rm tr}>0$，使这份参考解在 $[L,L+\tau_{\rm tr}]$ 始终处于同一个负密度、合法窗口和新速度图中。特别，$\sigma_{\rm old}(L)=0$；对已经固定的非零 $\varepsilon$，其短窗上界为 $O(\tau_{\rm tr})$。

固定一个光滑 cutoff $\vartheta$，在过渡窗左端的开放邻域恒为 $1$，在右端开放邻域恒为 $0$，且 $0\le\vartheta\le1$。在(42)中使用一次固定的输入
$$
\boxed{\sigma(s)=\vartheta(s)\sigma_{\rm old}(s).}
\tag{42a}
$$
从 $L$ 的同一个真实全入值启动。左侧开放邻域中，参考旧解也解(42)及同一输入；ODE 唯一性使两份解在那里完全相同。因此不是只匹配 $\gamma(L)$，而是全部 scalar、frame、位置和真实历史的接点 jets 都原样保留。

对固定非零 $\varepsilon$，(42a)与参考输入的 $C^0$ 差为 $O(\tau_{\rm tr})$。约化 $(S,m)$ 系统的连续依赖在短窗给该状态差 $O(\tau_{\rm tr}^2)$。完整第三历史按真实平滑方程恢复，可能读取加速度或 $\sigma_s$；这里不对它宣称同阶误差界。缩短 $\tau_{\rm tr}$ 后，新解仍有 $P<0$、$k\eta>0$、$\mathscr D\ne0$，并保全部原合法条件。该论证只需输入值；cutoff 的高阶导数可以随所选有限短窗变大，但均有限，不被当成一个统一于 $\varepsilon\to0$ 的界。

在右端开放邻域，(42a)已经恒为零。故从这里开始，新的实际路径准确满足
$$
\boxed{
p_1^{\,\omega_c}(s)\equiv-P_{\rm hold}<0.
}
\tag{43}
$$
$P_{\rm hold}$ 是这条**真实过渡后**路径的值，通常不等于(36)的
$P_*=h_c^2\delta_L^2/2$。可由上述短窗选择保证
$P_*/2<P_{\rm hold}<3P_*/2$，不把二者写成相等。此后继续同一个 $\sigma=0$ 方程，得到一个正长度实际保持段；长度为 $\ell_{\rm hold}>0$ 时，其准确矩阵坐标增量为
$-P_{\rm hold}\ell_{\rm hold}$。

cutoff 只改变原自由控制的坐标输入，没有重选 $\chi_\theta$、$\nu$、母、锚或入射 $m,T$。右端开放邻域已经使用保持方程，所以后续保持段的全 germ 亦准确匹配。全部过渡成本与历史是原 ODE 的输出，未添加零矩桥。

负密度水平曲线的几何可完整积分。对本稿实际选定的正 $k$ 分支，(43)与水平式给
$$
h\eta=k+\frac{P_{\rm hold}}{k},\qquad
d\log h=\frac{k^2-2P_{\rm hold}}{2k(k^2+P_{\rm hold})}\,dk.
$$
因此
$$
\boxed{
h=C_{\rm hold}(k^2+P_{\rm hold})^{3/4}/k,\qquad
\eta=(k^2+P_{\rm hold})^{1/4}/C_{\rm hold},
}
\tag{44}
$$
其中 $C_{\rm hold}>0$ 由过渡后实际入口确定。微分身份没有除以 $k_s$，所以停顿或转向不破坏它。这条几何曲线的高度最小点为 $k^2=2P_{\rm hold}$，但**不宣称过渡后的入口恰在该点，也不把该最小值写成 $h_c$**。正分支始终有 $\omega>\omega_c$，所以原合法条件 $x+\omega_c>0$ 在整条几何曲线上保持。

继续(42)的准确条件是：状态、速度与全部真实历史留在原有限恢复的合法域内，且(41)不为零。局部保持段已经由实际入口、平滑过渡和 ODE 存在性支付；本文不宣称这些条件在任意长时间自动保持，也不把几何曲线(44)的全局定义当成完整反馈流已经全局存在。完整 $\mathscr D$ 含真实 $\Phi_m$，不能只用 $T_0\ell_k$ 代替。

因此该入口不仅给一个瞬时负值，还给同一个规范下能够平滑接入并实际保持一段负密度的控制坐标。要抵消(38)及其它七矩，仍须支付足够长的继续、其它矩阵方向和真实返回端口。这是后继实际控制的问题，不由(43)的局部持有时间自行完成。

## 11. 附：固定非零零叶换入口也不能支付 $M=0$

这段补足 R529 的一个范围，避免在三零分支之外以换一个初始曲率绕过其几何号。

若一个非空正高度非零二次零叶满足 $q_0\ne0$，沿 R529 记号可写
$$
h=\frac{\cosh t}{b},\qquad d=\sinh t-ah,\qquad b>0.
$$
任意真实水平积分常数给
$$
k=\cosh^2t\{\mathfrak c-f(t)\},\qquad
f(t)=\arctan(\sinh t)+\frac{\sinh t}{\cosh^2t},
$$
$$
f'(t)=2\operatorname{sech}^3t>0,\qquad
f(\mathbb R)=(-\pi/2,\pi/2).
\tag{45}
$$
若 $\mathfrak c$ 在这个开区间内，整叶经过唯一 $k=0$ 点。使用该点的固定 $\omega_*$ 坐标，R529 的完整式给 $p_1^{\omega_*}\ge0$，且仅在该点为零。任意非恒正长度段的这条总矩严格为正；若只停在该点，原 $t_1<0$。

若 $\mathfrak c\notin(-\pi/2,\pi/2)$，包括两个边界值，有限 $t$ 上的 $k$ 始终严格单号。原 $p_2=-kh/2$ 因而严格单号，其正长度积分不为零。

若 $q_0=0$，非空非零叶是 $d=\lambda h$。原水平式给 $(\omega-\lambda)/h$ 为常数，从而 $k/h^2$ 为常数。非零时仍由 $p_2$ 单号分离；零时 $k=0$ 且
$$
t_1^\lambda=-\{1+(h_s/h)^2\}/8<0.
$$
所以任意固定非零三矩二次零叶上的正长度水平路径，不论入口曲率是否为零，都不能给原全 $M=0$。这不约束本文(4)的三零情形，也不排穿越不同二次曲面或改变主导 history 方向的真实路径。

## 原式来源与审核范围

- R520：完整 $\mathcal F_{\rm path}$、原第三配对、全部 acceleration 消项、固定第三 Gram 与真实八矩反馈；
- R527：三十行独立 principal、共同实际正根、三完整 $q_j$ 与严格正 $\ell_k$ 的同点选择；
- R73/R524：原 $M_{\rm raw}$、真实水平关系和固定 $\omega_c$ 下的 $p_1$ 密度；
- R47/R56：一次紧第三 Gram 右逆及原恢复的同锚范围；
- 本稿(10)–(44)：完整状态斜率选择、真前缀线性化、Volterra 有向面积、两实际脉冲、单端口有限 IFT 与平滑负密度继续坐标；
- R529：附录所用的非零零叶水平第一积分。

所有新路径和控制只通过纸面存在性与原有限 ODE 定义。没有用数值近似、模拟曲线或未付的额外样点替代任何准确端口。
