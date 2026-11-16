# R460：多个简单临界点的自动无留数与完整 period 的光滑拼接

日期：2026-11-16。**原式纸面证明；没有执行新的 profile、积分、符号消元、秩、零点计数或科学作业。**

[R455](R455-four-natural-moments-with-one-common-degenerate-pair-and-twenty-targets.md) 的同一最终母库有且仅有一对简单 $A_f$ 零点，但内部允许有限多个简单 $p=f'$ 零点；周期核及内支撑纠正也不必在整个活动包实解析。不能直接把旧单峰解析描述搬到这个库，更不能因变参数式在 $p=0$ 出现二阶极点就增加一个通量条件。

本文将 [R225 §5](R225-complete-period-range-flat-end-germs-and-finite-observation-quotient.md)、
[R391 §8](R391-analytic-simple-degeneracies-and-complete-selected-inverse-germs-on-the-rational-circle.md)
已有的 simple-$p$ 结论写成不需解析性的完整光滑局部式，并接回全包、端部、原右锚及同一十三行系统。实质结论是：

- 每个简单 $p$ 零点的对数留数由原 forcing 恒等式自动消失，真实累计通量在该点不必为零；
- 多个这样的点不增加包内齐次参数；光滑解跨点的常数由原导数匹配唯一确定；
- 在原平台、总通量和两个平端 germ 已支付的条件下，整个 period 内部只剩全部简单 $A_f$ 点的原 partial 通量；
- 对 R455 的当前两根母库，这意味着每包每个 period 只有那两个真实 $A_f$ 点门；这里仍不宣布它们已由某个 signed 见证实际支付，也不宣布十三行同规范已解。

## 1. 原算子、实际目标与不重置的累计量

沿原共同合法窗口 $I$、共同右锚及固定光滑首阶圆，记
$$
p=f',\qquad r=p',\qquad t=p'',\qquad
A=6pt-2r^2,\qquad V_f=6(rt)'.
\tag{1}
$$
R225(3)—(4)给的是不除退化系数的身份
$$
\mathcal M_fv=(Av')'-V_fv,\qquad
(L_fk)''=\mathcal M_f(k'),\qquad
\mathcal M_fp=0,
$$
$$
p\mathcal M_fv=\{A(pv'-rv)\}'.
\tag{2}
$$

固定一个活动包 $(a,b)$。全部正阶 $f$ jets 在两个端点全平；包间和共同外 collar 有正长度空隙。对一个真实目标 $G$，始终定义
$$
H(x;G)=\int_a^x p(y)G''(y)\,dy.
\tag{3}
$$
这一个 $H$ 跨过全部内部临界点；不在每个点另选积分常数，不在右端减去 $H(b;G)$。

若 $k$ 是光滑逆，令 $v=k'$，则原左平端把(2)的积分常数固定为零：
$$
A(pv'-rv)=H.
\tag{4}
$$
在 $pA\ne0$ 上，
$$
v=p\left(C+\int\frac{H}{Ap^2}\right).
\tag{5}
$$
本文判断的是(4)—(5)恢复的 $v$，而不是孤立地要求被积函数处处有界。

### 1.1 两个真实 period 的 $2\tau$ 规范

实际背景保
$$
M=0,\qquad T=\tau\mathfrak H,\qquad \tau\ne0.
$$
采用 R394/R407 的同一规范
$$
V_\theta^0=\sin^2\theta\,V_d+2\sin\theta\cos\theta\,V_e,
\qquad X=\Phi_{m_*},\qquad \Delta=f^2-g^2.
$$
原传入 history 的已选 gauge 为 $w_c=-XD_\theta$，其中
$D_\theta=\sin^2\theta\,\Delta-2\sin\theta\cos\theta(f,g)$。
其后两个准确目标是
$$
G_d=-\frac{V_d-2\tau L_f(X\Delta)}{2\tau},
\qquad
G_e=-\frac{V_e+2\tau L_f(X(f,g))}{2\tau}.
\tag{6}
$$
若 $L_fk_d=G_d$、$L_fk_e=G_e$，则
$k_\theta=\sin^2\theta\,k_d+2\sin\theta\cos\theta\,k_e$
正好消掉剩余 period，因为允许二阶 gauge 的完整变化为
$2\tau L_f(k_\theta)$。

原三矩使 $X\Delta$ 与 $X(f,g)$ 是整个窗口内的真紧函数；没有把单个 $X(u_i,u_i)$ 假定为紧。(6)后面一直保留。

## 2. 简单 p 零点的精确光滑正规式

设 $x_0$ 是一个简单零点：
$$
p(x_0)=0,\qquad r_0=p'(x_0)\ne0,\qquad t_0=p''(x_0).
$$
写 $z=x-x_0$、$p=z\,a(z)$，则
$$
a(0)=r_0,\qquad a'(0)=t_0/2,
$$
$$
A(x_0)=-2r_0^2,\qquad A'(x_0)=2r_0t_0.
\tag{7}
$$
所以 $A$ 在一个完整邻域内不为零。置
$$
w=\frac HA,\qquad \beta(z)=\frac{w(z)}{a(z)^2}.
$$
因为原累计量满足 $H'=pG''$，准确有 $H'(x_0)=0$。于是
$$
w'(0)=\frac{t_0}{r_0}w(0),\qquad
\beta'(0)=\frac{w'(0)}{r_0^2}
-\frac{t_0w(0)}{r_0^3}=0.
\tag{8}
$$
若 $G$ 光滑，$\beta$ 光滑。两次 Hadamard 除法给一个真实光滑函数 $b_0(z)$，使
$$
\beta(z)=\beta_0+z^2b_0(z),
\qquad
\beta_0=-\frac{H(x_0)}{2r_0^4}.
$$
因此原变参数 integrand 的精确形式为
$$
\boxed{\frac{H}{Ap^2}=\frac{\beta_0}{z^2}+b_0(z).}
\tag{9}
$$
它没有 $z^{-1}$ 项；这里的“无留数”是光滑 Hadamard 身份，不要求亚纯或实解析展开。

用同一个普通原函数，(5)成为
$$
\boxed{
v(z)=-a(z)\beta_0+
z\,a(z)\left(C+\int_0^z b_0(y)\,dy\right).
}
\tag{10}
$$
这个式子在 $z=0$ 真正光滑。特别
$$
\boxed{
k'(x_0)=v(0)=\frac{H(x_0;G)}{2r_0^3}.
}
\tag{11}
$$
主二阶极点被 $p$ 精确抵消；不需要 $H(x_0;G)=0$。

与 R391 的短 Taylor 写法一致，
$$
Ap^2=-2r_0^4z^2+O(z^4),\qquad
H=H(x_0)+O(z^2).
\tag{12}
$$
(9)—(10)比仅看有限 Taylor 阶更强：它直接证明全部高阶 jets 都能光滑穿越，也适用于 R455 的非解析中心。

### 2.1 同一个齐次常数怎样跨点

在两侧分别写(10)，其值在 $z=0$ 自动同为(11)，但
$$
v'(0)=-a'(0)\beta_0+r_0C.
\tag{13}
$$
所以 $v'$ 连续准确要求两个侧解采用同一个 $C$；一旦这个条件成立，整条(10)就是共同光滑延拓。

对原 gauge，$k\in C^2$ 已要求 $v'=k''$ 连续，不能保留两个独立的侧常数。随后对 $v$ 积分并匹配 $k(x_0)$，也不产生内部跳量自由。多个简单 $p$ 零点不会把一个活动包分裂成多个可独立选择的 gauge。

### 2.2 一个真实像内的非零值例子

在 $x_0$ 附近取 $k(x)=x-x_0$，再以一个活动包内的光滑 cutoff 将它扩成真紧 gauge。令 $G=L_fk$。邻近 $x_0$ 有 $v=1$，故(4)给
$$
H(x_0;G)=-A(x_0)r_0=2r_0^3\ne0.
\tag{14}
$$
这是原 $L_f$ 像中的目标；它明确排除“在所有 $p$ 零点追加 $H=0$”这个错误条件。本例只说明原空间算子，不声称该 $G$ 是某个新实际成本的 canonical period。

## 3. 低正则目标也没有 simple-p 门

这一节仍固定光滑 $f$，只降低目标 $G$ 的正则性。

**引理 1。** 若 $G\in C^m$、$m\ge2$，在简单 $p$ 零点附近，对任意实数 $\nu$ 都有唯一局部解
$$
\mathcal M_fv=G'',\qquad
v(x_0)=\frac{H(x_0)}{2r_0^3},\qquad v'(x_0)=\nu.
\tag{15}
$$
它满足 $v\in C^m$，积分后 $k\in C^{m+1}$，且完整通量恒等于原 $H$。

**证明。** 因 $A(x_0)\ne0$，方程
$$
Av''+A'v'-V_fv=G''
$$
在邻域内是普通二阶线性方程。连续 forcing 给 $C^2$ 解，高阶正则由方程逐阶恢复。由(2)，其通量导数是 $pG''=H'$；(15)的值使起点通量恰为 $H(x_0)$，所以差恒为零。证毕。

特别，只有 $G\in C^2$ 时也已得到一个 $C^3$ 的 $k$；此处并不存在一个隐藏的 $C^2$ 对数门。解对固定初值及 $G''$ 在相应局部范数中连续且线性；在固定有限维光滑目标族上还给同一光滑选择。

这条低正则结论仅针对 $A\ne0$ 的 simple-$p$ 点。后面的全局 iff 按原光滑目标陈述；本文不把 $C^2$ forcing 在退化的 simple-$A$ 点的商自动提升成任意阶光滑函数。

## 4. 任意有限多个内部点：只保 A 的真实通量条件

现在在一个活动包内假定：

1. $p$ 的内部零点有限且全部简单；
2. $A$ 的内部零点有限且全部简单；
3. 靠两个平端 $pA\ne0$。

简单 $p$ 点上 $A=-2r^2\ne0$，所以两类点不相交。R455 的每个最终包满足这些条件；它允许的多个简单 $p$ 点不需要重新计数或重新构造。

对光滑 $G$，simple-$A$ 点 $x_*$ 上 $p(x_*)\ne0$。若 $H(x_*)\ne0$，(5)的 integrand 有非零简单极点，$v$ 带不可消的对数项。若 $H(x_*)=0$，Hadamard 除法使 $H/A$ 光滑，原一阶式
$$
pv'-rv=H/A
$$
正规，局部光滑解存在。因此
$$
\boxed{
\text{全部内部逆 germ 光滑}
\quad\Longleftrightarrow\quad
H(x_*;G)=0
\ \text{对全部 }A(x_*)=0 .
}
\tag{16}
$$
此处的同一个 $H$ 始终由包左端累计；不因某处存在局部解就重置下一段的积分常数。

**全包匹配。** 从一个正则小段用(5)出发，逐个跨过有限内部点。simple-$A$ 点使用光滑商；simple-$p$ 点使用(10)。每一步都匹配同一个光滑解，而不是另加一个自由轨道。两个全包解之差满足零通量；在正则小段是 $Cp$。

跨 $A=0$ 时，$p\ne0$，$v$ 的连续性迫同一个 $C$。跨 $p=0$ 时，$r\ne0$，$v'$ 的连续性迫同一个 $C$。所以
$$
\boxed{v=v_G+C\,p\quad\text{在整个活动包上。}}
\tag{17}
$$
若包内 $f=a_i u_i$ 且两端 $f=0$，积分后只有
$k=\widetilde k_G+\gamma_i u_i+b_i$。多个极值点不增加这些参数的数目。

## 5. 平端与 k 的值闭合仍是独立步骤

一般光滑目标不能只凭(16)就认定属于全局 $L_f$ 像。完整陈述仍保 R225 的三项外部信息：

- 在所有 $f$ 常平台上 $G''=0$，共同右 collar 还须保原 $G=G'=0$；
- 每包同一累计量满足 $H(b;G)=0$；
- 在两端，真实分支
$$
v_a^0=p\int_{x_a}^x\frac{H}{Ap^2},
\qquad
v_b^0=p\int_{x_b}^x\frac{H}{Ap^2}
\tag{18}
$$
均可作 $C^\infty$ 伸延。

(18)右端绝不另扣 $H(b)$。改变参考点只加全平的 $Cp$，故 germ 条件不依赖该选择。可伸延不等于全部端 jets 为零。

**定理 1。** 在第4节的光滑有限简单退化类中，一个光滑、同右锚的目标 $G$ 属于双 collar 为零的 $L_f$ 像，当且仅当上述平台、包总通量、两个真平端 germ 及(16)全部成立。

必要性由原(2)—(4)和合法 $k$ 的端 jets。充分性先在每包构造(17)，由(18)将 $v=k'$ 光滑接入正间隙；间隙上 $A=V_f=G''=0$，可用固定 cutoff 连接。令该连接为 $\widetilde v$，在一个固定间隙选择 $\eta\in C_c^\infty$、$\int_I\eta=1$，再置
$$
v^\#=\widetilde v-\left(\int_I\widetilde v\right)\eta,
\qquad
k(x)=\int_{r_*}^{x}v^\#(y)\,dy.
\tag{19}
$$
这使 $k$ 在两个共同 collar 都为零，且不改变活动包上的微分方程或端 jets。最后
$(L_fk-G)''=0$；原同右锚在右 collar 同时给该差及其一阶导数为零，所以全局仿射差准确消失。

这三个步骤不可交换或合并：

- 内部匹配解决 $k'$ 的光滑性；
- (19)解决 $k$ 自身的两个端值；
- 原右 collar 消掉算子输出的仿射差。

每包 $\int_a^b v_G$ 一般不为零；加 $Cp$ 不改变它，因为本类紧包有
$\int_a^bp=f(b)-f(a)=0$。所以(19)确有内容。它通常改变 $k$ 在其左侧活动包上的常值，不能当成十三行的盲调整。

R225 §8 已给一般目标的平端反例：内部与总通量条件全过而 $k'$ 仍可像 $1/p$ 发散。本文不撤销该反例，也不把任意光滑目标的两端条件删掉。

## 6. 当前 canonical 目标的端部只需原有限 totals

现在回到 R455 的固定最终 profiles 和(6)的真实成本。作与 R389/R407 相同的实际前提：
$$
\pi V=0,\qquad \mathcal QV=0.
\tag{20}
$$
它们是当前成本的 universal whole pure/self 条件；不能换成另一背景的旧值或仅一个有限 self 尾查询。

R389 的完整 pure 极化与 whole self 给所有平台 $G''=0$、原右 collar 的零值和零导数。R455 在全部内修正后保留原两侧解析全平 cap。故 R389 §7 消掉一次指数层并恢复二次零端的证明仍适用：该论证只使用端部类别、同包比例输入、原完整 pure 身份及同右锚恢复，不需要整个多周期中心解析。

具体地，靠一个实际零端，使用相应距离坐标 $\zeta$，
$$
p=\zeta^{-2}a(\zeta)e^{-c/\zeta},\quad
a(0)\ne0,\ c>0,\qquad
G^0=P_e+p^2\zeta^{-4}B(\zeta),\quad B\in C^\infty,
\tag{21}
$$
$P_e$ 是原平台多项式，(20)使 $P_e''=0$。
这里先对未加 incoming $L_f$ 项的 canonical 目标使用(21)，然后加回(6)的已知光滑 $L_f$ 像；其逆 germ 类不变。

原左零分支由(3)固定，(21)保证其平端光滑。原右分支光滑恰需
$$
H(b;G_d)=H(b;G_e)=0.
\tag{22}
$$
当(22)成立，$H(x)=-\int_x^b pG''$ 是同一个原累计量，不是另选右常数。原加权原函数证明遂给光滑右 germ。

(22)由实际两个 mixed 整包 totals 承载。具体用 R407 的
$$
\mathcal T_{d,i}
=a_i^3\{R_i\omega_i+\mathcal A_{V,u_i}(n_{R,i})\},\qquad
\mathcal T_{e,i}
=-a_i^3\{T_i\omega_i+\mathcal A_{V,u_i}(n_{T,i})\},
\tag{23}
$$
其中所有真实幅度、宽度、位置、原顺序和 suffix 都不变。已知 incoming $L_f$ 像的整个包端通量为零，故
$$
H(b;G_{d/e})=-\mathcal T_{d/e,i}/(2\tau).
\tag{24}
$$
因此这里只需这份有限实际总量为零，不需被 R406 排除的 universal $\Lambda_{\rm all}=0$。R433 的同一实际 $J^+=(E,\mathcal A,\mathcal O)=0$ 能提供(20)与(22)，因为有限 self 查询覆盖实际母包而全 ordered 查询保所有真实有序 $3+2$ 项；没有额外加入辅助包 self。

若当前实际成本尚未支付(20)或(23)，必须恢复那些原条件；本文不以 signed 核见证替代它们。

## 7. 两个 period 在所有临界点的准确值与范围

记未扣原平台的实际 partial 为
$$
H_{d,i}(x)=\int_{\ell_i}^{x}f'V_d'',\qquad
H_{e,i}(x)=\int_{\ell_i}^{x}f'V_e''.
\tag{25}
$$
由(2)，对于任意光滑 $z$，
$$
\int_{\ell_i}^{x}p(L_fz)''
=A(x)\{p(x)z''(x)-r(x)z'(x)\}.
\tag{26}
$$
左平端常数为零，$z$ 不必在每个最细包单独紧支撑。

在 $A(x_*)=0$ 处，(26)为零，(6)因而给
$$
H(x_*;G_d)=-\frac{H_{d,i}(x_*)}{2\tau},
\qquad
H(x_*;G_e)=-\frac{H_{e,i}(x_*)}{2\tau}.
\tag{27}
$$
这正是原两通道 partial 门的规范，不因当前内部多了其它 $p$ 零点而改变。

在简单 $p$ 零点 $x_0$ 处则不同：令 $r_0=f''(x_0)\ne0$，(26)准确是
$2r_0^3z'(x_0)$。把(11)与(6)合并得
$$
\boxed{
\begin{aligned}
k_d'(x_0)&=-\frac{H_{d,i}(x_0)}{4\tau r_0^3}
 +(X\Delta)'(x_0),\\
k_e'(x_0)&=-\frac{H_{e,i}(x_0)}{4\tau r_0^3}
 -(X(f,g))'(x_0).
\end{aligned}}
\tag{28}
$$
这是逆解必须取的真实值，不是一组需要调成零的新目标。incoming history 在 $A$ 点不改变通量门，却在 $p$ 点改变原 $k'$；其后续端口配对仍须保留。

**推论。** 对 R455 同一最终两根库，在当前 actual 成本满足(20)、(23)的前提下，两个完整 period 方程同时有双 collar 光滑特解，当且仅当
$$
\boxed{
H_{d,i}(x_i^-)=H_{d,i}(x_i^+)
=H_{e,i}(x_i^-)=H_{e,i}(x_i^+)=0
\quad\text{对全部实际包 }i.
}
\tag{29}
$$
没有额外的 simple-$p$ 留数行，也没有额外的 $p$ 零点值行。(29)使用同一个最终成本与同一个真实库；它不是已经完成的 actual 全 partial 控制定理。

## 8. 核与十三行同规范没有因多峰而增维

若 $L_fk=0$，每包左端把(4)的常数定为零。第4节的匹配证明给同一包上 $k'=\gamma_i u_i'$，因此
$$
\ker L_f
=\operatorname{span}\{u_i,\chi_i:1\le i\le n\}\oplus\mathscr G
\tag{30}
$$
仍是 R327/R394 的原式：$\chi_i$ 为实际常平台列，$\mathscr G$ 是 $k$ 本身在全部活动包上为零的 gap 函数。多个简单 $p$ 点不产生新的列。

在一个固定有限维可解目标子空间上，先对有限基完成第5节的延拓、gap 修正及原右锚恢复，再线性延拓，可选一个固定线性右逆。这里只用有限个真实选择，不宣称对任意无限维 germ 空间有未说明的统一有界右逆。

取得 $k_d,k_e$ 后，R394 的同一系统仍是
$$
C_\theta\eta_\theta
=-\mathcal A_\theta(\sin\theta\,k_d+2\cos\theta\,k_e),
\tag{31}
$$
并以
$$
k_\theta=\sin\theta\left[
\sin\theta\,k_d+2\cos\theta\,k_e+
\sum_\nu\eta_\nu(\theta)v_\nu\right]
$$
保两个 seed 与全相位光滑性。母包列、平台列、真实 $m_*$、全部二次尾与原 $I_2$ 的补偿项均沿原定义。

(19)改变平台值所产生的代价进入(31)右端；(28)也进入同一真实特解。只有原 $\mathscr G$ 是这十三行的盲方向。相位秩降点的整除条件仍需实际支付，不能因(29)变得简洁就宣布(31)可解。

本稿新增的是：原多峰光滑母不再带任何未解释的 simple-$p$ 局部极性门。剩余问题准确位于同成本的四类镜点 partial 实际共同像、原全局特解的真实平台基准，以及同一十三行兼容；高阶可动族、其它路径段与最终几何目标均不由此自动获得。
