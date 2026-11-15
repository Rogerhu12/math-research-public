# R306：导数 rank-one 的完整分类与真正重叠圆的一层正障碍

日期：2026-11-15。**完整纸面原式推导。** 未执行求积、符号程序、profile 扫描、人工测试或研究计算。

[R304](R304-positive-one-history-remainder-excludes-disjoint-real-rank-one-circles.md) 的不交实微包假设可以准确放宽：只要整个实 profile 平面的两条导数处处平行，同一小共振端芽仍有完全相同的一层严格正余量。profiles 的值可以真正重叠，也可以在不同活动段有不同的仿射偏移；不要求有限个微包、同形、同宽或某个常数换基后不交。

更进一步，对实紧 $C^\infty$ profiles，
$$
\mathfrak H(g;f,f)=\mathfrak H(f;g,g)=0
\quad\Longleftrightarrow\quad
g'f''-f'g''\equiv0 .
\tag{1}
$$
因此当前“整个二维平面对第三 hook 不可见”的强构造类全部受到这一正障碍，包括 R183 的真正重叠平面。这里不能省掉左边的第二个 hook：一般固定 seed 的第三周期只要求第一个，本稿没有把第二个偷加为原问题的普遍必要条件。

主要来源：[R181 原退化方程及通量](R181-degenerate-self-adjoint-equation-for-fixed-circle-period-gauges.md)、[R183 导数分包重叠圆](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md)、[R221 完整局部配对与周期核](R221-complete-fixed-circle-ruling-moment-map-and-joint-right-inverse.md)、[R250 完整三槽面积及弱 hook 范围](R250-complete-circle-Gaussian-area-and-nonuniform-profile-cancellation.md)、[R259 原 cubic 变分与真实尾](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R300 完整一层](R300-one-history-tail-compensation-and-thirty-eight-dimensional-principal-space.md)及 R304。

## 1. 同一真实对象与两个必须区分的第三条件

共同区间、双零 collar 与右锚固定：
$$
I=[\ell,r_*],\qquad
Jv(x)=\int_x^{r_*}v(t)\,dt.
$$
$f,g$ 为实紧光滑函数，满足原三个对称矩的圆条件
$$
\mathbf I(f,f)=\mathbf I(g,g),\qquad \mathbf I(f,g)=0,
$$
$$
\mathbf I(u,v)=
\left(\int u''v'',\ \int xu''v'',\
\int(x^2u''v''+2u'v')\right).
\tag{2}
$$
取
$$
u=\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D=f\odot f-u\odot u.
\tag{3}
$$
$\odot$ 是原对称算子槽。不能把 $D$ 当作一个普通函数先求导。

所讨论的是原已安装几何
$$
M=0,\qquad T=\kappa_H\mathfrak H,\qquad \kappa_H\ne0,
\tag{4}
$$
及 R304 的同一小共振偶端芽
$$
h=h_e e^{\varepsilon\sigma^2},\quad
k=\kappa(1-2\varepsilon\sigma^2),\quad
\omega=\kappa/h,\quad
\varepsilon=\kappa^2/4,\quad
0<t:=\kappa^2<1/100 .
\tag{5}
$$
$\kappa_H$ 与 $\kappa$ 不是同一个参数。所有原前缀、中心初值、允许 gauge 与偶部 $\mathcal W_e$ 的范围沿 R243/R304 保留；本稿不重新选取历史常数。

R250(17)–(18) 已从原完整第三周期给
$$
\mathfrak H(\phi_\theta;D)
=\sin\theta\,\mathfrak H(g;f,f).
\tag{6}
$$
所以一般固定 seed 圆的**第三周期必要条件**只有
$$
\mathfrak H(g;f,f)=0.
\tag{7}
$$
独立二阶 homogeneous gauge 在 $M=0$ 时不能改变这个周期条件。

另一方面，R183 为分别获得四条原第三 forcing 的完整 range，使用了整个平面上的强身份
$$
\mathfrak H\big|_{\operatorname{span}(f,g)
\times\operatorname{Sym}^2\operatorname{span}(f,g)}=0.
\tag{8}
$$
由真实对角身份 $\mathfrak H(q;q,q)=0$ 的三次极化，
$$
2\mathfrak H(f;f,g)=-\mathfrak H(g;f,f),\qquad
2\mathfrak H(g;f,g)=-\mathfrak H(f;g,g),
$$
故 (8) 恰等价于 (1) 左边的两个零式。

不能从 (7) 推出 (8)。四条第三 forcing 的逐条周期性是 R183 使用的充分构造方式；原组合 $W_\theta$ 的周期性可以有 (6) 的准确抵消。第三 ruling 和其余 range 条件也不能由 (7) 单独省掉。

## 2. 原通量给弱 hook 的准确充要条件

置
$$
p=f',\quad s=f'',\qquad v=g',\quad r=g'',\qquad
\mathcal W=vs-pr,
$$
$$
A_f=6pp''-2(p')^2,\qquad V_f=6(p'p'')'.
\tag{9}
$$
R181/R221 的原右锚算子为
$$
L_f(g)=\mathfrak H(g;f,f),\qquad
L_f(g)''=(A_fg'')'-V_fg'.
\tag{10}
$$
另有真实恒等
$$
(A_fp')'=V_fp.
$$
因此
$$
\left[A_f(pg''-p'g')\right]'=p\,L_f(g)''.
\tag{11}
$$

**引理 1。** 对上述紧 profiles，
$$
\boxed{\mathfrak H(g;f,f)=0
\quad\Longleftrightarrow\quad A_f\mathcal W=0\ \text{逐点}.}
\tag{12}
$$

若左边为零，(11) 给通量为常数。共同零 collar 中该常数准确为零，所以右边成立。

反过来，$A_f\mathcal W=0$ 给 $pL_f(g)''=0$。在 $p\ne0$ 的开集上，$L_f(g)''=0$。在 $p=0$ 集合的内部，$p$ 及其全部导数为零，故 (10) 同样为零；其余点由连续性得到。于是 $L_f(g)''$ 在全区间恒零。

最后，原右锚在共同右 collar 给 $L_f(g)=L_f(g)'=0$，这个仿射函数准确为零。这里支付了求两次导数可能丢掉的两个常数，没有将它们任意设定。证毕。

交换 $f,g$ 给
$$
\mathfrak H(f;g,g)=0\quad\Longleftrightarrow\quad
A_g\mathcal W=0.
\tag{13}
$$

## 3. 两个 hook 同时为零时，退化开段也不能保留 rank-two

**定理 1。** 对紧 $C^\infty$ profiles，(1) 成立。实际上其中排除非零 $\mathcal W$ 的拼口论证只需相应 derivatives 至少保持 $C^2$，即原 profiles 的 $C^3$ 正则。

先设两个 hook 均零。如果 $\mathcal W\ne0$，取集合 $\{\mathcal W\ne0\}$ 的一个连通分支 $(a,b)$。由 (12)–(13)，此处
$$
A_f=A_g=0.
\tag{14}
$$
$p$、$v$ 都不能为零。例如 $p(x_0)=0$ 时，$A_f(x_0)=-2p'(x_0)^2=0$，于是 $\mathcal W(x_0)=0$，矛盾。对 $v$ 同理。

$p,v$ 各自符号固定。由 (14)，
$$
\left(|p|^{2/3}\right)''=0,\qquad
\left(|v|^{2/3}\right)''=0.
$$
故在该整个连通分支上有
$$
|p|^{2/3}=\alpha x+\beta>0,\qquad
|v|^{2/3}=\gamma x+\delta>0.
\tag{15}
$$
直接求导，得到
$$
\boxed{
\mathcal W
=\frac32\operatorname{sgn}(pv)
(\alpha\delta-\gamma\beta)
\sqrt{(\alpha x+\beta)(\gamma x+\delta)}.
}
\tag{16}
$$
行列式 $\alpha\delta-\gamma\beta$ 非零，否则整个分支上的 $\mathcal W$ 为零。

紧支撑使该分支具有有限边界，且 $\mathcal W$ 在其边界趋零。式 (16) 因而迫至少一个正仿射因子在边界归零。若 $\alpha a+\beta=0$，其斜率非零，并有
$$
|p(x)|=|\alpha|^{3/2}|x-a|^{3/2}
$$
在一侧准确成立。于是 $p''$ 按 $|x-a|^{-1/2}$ 发散，违背 $f\in C^3$。另一仿射因子归零同样违背 $g\in C^3$。这排除了每一个非零分支，所以 $\mathcal W\equiv0$。

反向若 $\mathcal W=0$，(12) 与 (13) 直接给两个 hook 均零；三次极化随后给整个 (8)。证毕。

这个证明没有假定活动区间有限，也没有把 $A_f=0$ 的开集丢掉。允许一个 profile 在某些区间为常数，允许比值在共同平端点改变；得到的是导数的逐点 rank-one，不是 profiles 的值沿同一条固定直线。

因此 R183 的不可 GL2 分离性与本定理完全相容：其值可以经过三条不同射影方向，而导数仍在每个活动段处处平行。

## 4. 只要导数平行，三个 mixed 积分就有准确全局身份

以下固定任意 $\theta$，重新写
$$
p=f',\ s=f'',\ \dot s=f''',\qquad
v=u',\ r=u'',\ \dot r=u''',
$$
$$
F=s^2,\quad R=r^2,\quad d_0=F-R,\quad A=Jd_0 .
\tag{17}
$$
$d_0$ 是二次槽 $D$ 的 $[2,2]$ 密度；$A=PD$。原三矩保证 $A$ 及以下各 $XD$ 真正紧支撑。

假设
$$
vs-pr=0.
\tag{18}
$$
因为 $u$ 是 $f,g$ 的线性组合，若 $\mathcal W(f,g)=0$，则 (18) 对所有角成立。

令
$$
C_\theta=\int R(F-R),\qquad
D_\theta^{(4)}=\int(F-R)^2.
\tag{19}
$$
定义三个真实 mixed 积分
$$
Y=\int vr\,d_0',\qquad
Z_1=\int xR\,d_0',\qquad
B=\int ps\,d_0'.
$$
则
$$
\boxed{
Y=-\frac23C_\theta,\qquad
Z_1=-\frac12C_\theta,\qquad
B=-\frac23(D_\theta^{(4)}+C_\theta).
}
\tag{20}
$$

证明不依赖逐包非紧函数。由 (18) 及其导数，
$$
vs=pr,\qquad v\dot s=p\dot r.
$$
对 $psr^2$ 作真正全区间分部积分，
$$
0=\int (psr^2)'=\int F R+3\int vrs\dot s.
\tag{21}
$$
边界因原 $f,g$ 的共同零 collar 消失。这给第一条和第三条。

另有 $FR'-RF'=0$ 逐点。可先在 $p\ne0$ 处由上述两个恒等推出；在 $p=0,v\ne0$ 处有 $s=0$；在两者同时为零的集合内部，相关导数均零，余点用连续性。于是
$$
\int xRF'=-\frac12\int FR.
$$
再用 $\int xRR'=-\int R^2/2$，得到第二条。所有积分都含真实 whole profiles，未把某个 step 或单包原函数的左尾假置为零。证毕。

## 5. 用完整 $A_{-2,-3}$ 面积消掉 $C_\theta$

原 Gaussian 方向沿 R304 记为
$$
P=\Phi_{r_0},\quad R_0=\Phi_{r_1},\quad S_0=\Phi_{s_0},
\quad L=\Phi_{p_0},\quad U=\Phi_{s_1},
$$
$$
W_*=aR_0+bS_0,\quad Z_*=d_*L+e_*U,\quad B_{-3}=c_PP,
$$
$$
\begin{aligned}
a&=-\frac{51t^2+2t+8}{64h_e^2},&
b&=-\frac{17t^2+4t}{32h_e^2},\\
d_*&=6\kappa^3/h_e,&
e_*&=-\frac{\kappa(15t+1)}{4h_e},&
c_P&=-\frac{\kappa(41t^2+27)}{216h_e^3}.
\end{aligned}
\tag{22}
$$
$R_0,S_0$ 是算子，勿与 (17) 的密度 $R$ 混同。

R250 的完整三槽身份是
$$
[W_*,P](u;D)
=\frac13\{(a+3b)J(rd_0)+a\mathfrak H(u;D)\}.
\tag{23}
$$
在 (18) 下，定理 1 给整个 hook 平面零，后一项准确为零。R250 的真实一阶外矩为
$$
I_1\{u,J(rd_0)\}
=\frac12\int RF-\frac34\int R^2
-\frac12\int xRF'
=\frac34C_\theta,
$$
其中最后一步用第4节的全局恒等。

所以
$$
\boxed{
I_1\{u,[W_*,P](u;D)\}
=\frac{a+3b}{4}C_\theta.
}
\tag{24}
$$
这是完整原函数面积的外矩，已经保住 $J(rd_0)$ 的真实左常尾。它不使用 R304 仅适用于不交微包的单包 $[Z_*,P]$ self 表。

因为
$$
a+3b=-\frac{153t^2+26t+8}{64h_e^2}\ne0,
$$
完整 $A_{-2,-3}$ 面积为零准确迫
$$
C_\theta=0\qquad\text{对所有 }\theta.
\tag{25}
$$

## 6. 在一般重叠 profiles 上直接提取完整一层

沿 R300 定义 whole directed 行
$$
H^X_j=-I_j(XD,PD)+2I_j\{u,X(u,PD)\}.
\tag{26}
$$
Gaussian 二层的对称部分及相应面积一起给
$$
H^P_2=0,\qquad aH^{R_0}_1+bH^{S_0}_1=0,\qquad
d_*H^L_0+e_*H^U_0=0.
\tag{27}
$$
这里不能只从对称项删除某个 directed 行。

为使本稿的重叠推广可逐项核对，再置
$$
X_2=\int x^2F'd_0',\qquad
T_1=\int xp\dot s\,d_0'.
$$
由 R259 的真实 cubic 密度及原二导，直接得到
$$
\begin{aligned}
H^P_2&=-X_2-4Z_1+4Y-2D_\theta^{(4)},\\
H^{R_0}_1&=-X_2+2T_1-Z_1+2Y+C_\theta,\\
H^{S_0}_1&=-X_2-2Z_1+\frac12D_\theta^{(4)},\\
H^U_0&=-\frac32X_2+2T_1-2Y+Z_1+2B
+D_\theta^{(4)}-C_\theta .
\end{aligned}
\tag{28}
$$
例如对紧 $A=PD$，
$$
H^X_j=DF_{X,j}(u)[A]-I_j(A,X(f,f)).
\tag{29}
$$
这保留了第二项的真正 inner 原函数；$X(f,f)$ 不必紧。所用密度是
$$
F_{U,0}=\int(vr^2-xr^3),\quad
F_{R_0,1}=\int(xr^3/3-vr^2),\quad
F_{S_0,1}=\int xr^3/3,
$$
$$
F_{P,2}=\int(4xr^3/3-2vr^2).
$$
由 $A'=-d_0,A''=-d_0'$ 及原二导，(28)逐项成立。没有作不交分解。

由 (20)、(25) 得
$$
Y=Z_1=0,\qquad B=-\frac23D_\theta^{(4)}.
$$
代入 (27)–(28)，
$$
X_2=-2D_\theta^{(4)},\qquad
H^{S_0}_1=\frac52D_\theta^{(4)},\qquad
H^U_0=\left(\frac23-\frac52\frac ba\right)D_\theta^{(4)}.
\tag{30}
$$

再从 R221(17) 的完整 local 式抽取与 R304 相同的独立行。对任意合法 whole 槽，
$$
[\sigma h^{-2}j^0]\mathcal T(c;a,b)
=-\frac{\kappa^3}{16}\int a''b''(x^2c'''+xc'').
$$
因此不假定 (18) 的一般 mixed local 值就是
$$
\boxed{
[\sigma h^{-2}j^0]\{2\mathcal T(A;D)-4\mathcal T(u;u,A)\}
=-\frac{\kappa^3}{8}X_2
+\frac{\kappa^3}{16}D_\theta^{(4)}
-\frac{\kappa^3}{4}Z_1 .
}
\tag{31}
$$
这里 $A=PD$ 真紧，原右尾和 Green 项均已支付。式 (30) 把它化为 $5\kappa^3D_\theta^{(4)}/16$。

原 elementary history 的三个常数仍为
$$
\ell_0=-\kappa/2-6\kappa^3,\qquad
m_0=\kappa(15t+1)/4,\qquad p_0=41\kappa^5/216 .
$$
故以去掉非零 $c_P$ 的一层行记
$$
\mathscr O_\theta=
[\sigma h^{-2}j^0](\mathscr R_{-3,\theta}/c_P),
$$
准确有
$$
\mathscr O_\theta
=\frac{\ell_0}2H^L_0+\frac{m_0}2H^U_0+
\frac{p_0}2H^P_2+\text{(31)}.
\tag{32}
$$
(27)给
$$
\frac12(m_0-\ell_0e_*/d_*)=-\frac{1+15t}{96\kappa}.
$$
于是
$$
\boxed{
\mathscr O_\theta=-D_\kappa D_\theta^{(4)},\qquad
D_\kappa=
\frac{16+184t-1713t^2-2475t^3-4590t^4}
{288\kappa(51t^2+2t+8)} .
}
\tag{33}
$$
这是完整系数身份，不是模 $C^2$ 或仅 principal 的式子。

## 7. 完整正障碍及其适用类

由 (25) 的整个相位恒等，令
$$
A_4=\int(f'')^4,\quad C_{22}=\int(f'')^2(g'')^2,\quad
E_4=\int(g'')^4 .
$$
在 $\theta=\pi/2$ 及取整角平均，分别得到
$$
C_{22}=E_4,\qquad A_4=5C_{22}.
$$
因此
$$
D_{\pi/2}^{(4)}
=\int\{(f'')^2-(g'')^2\}^2=4E_4>0.
$$
非退化实圆保证 $g\ne0$，所以 $E_4>0$。

乘回原 $c_P$，得到与 R304 完全相同的严格值：
$$
\boxed{
[\sigma h^{-2}j^0]\mathscr R_{-3,\pi/2}
=
\frac{(41t^2+27)
(16+184t-1713t^2-2475t^3-4590t^4)}
{15552h_e^3(51t^2+2t+8)}
\int(g'')^4>0.
}
\tag{34}
$$
例如 $0<t<1/100$ 时分子括号大于
$16-1713/10^4-2475/10^6-4590/10^8>15$。
符号不依赖 $\kappa$ 正负，因为原 $c_P$ 与 (33) 中的 $1/\kappa$ 已正确相乘。

**定理 2。** 在 (5) 的同一原偶部商范围内，任何非退化实三矩圆只要满足 $g'f''-f'g''=0$，就不能通过完整第四 ruling。特别：

1. 所有整个平面对 $\mathfrak H$ 不可见的实紧 profile 圆均被排除；
2. R183 的真正重叠导数分包圆及其正交换基、有限完整副本和正幅组合均在此范围；
3. 若只施加弱 (7)，但 $f$ 满足 R221 的 regular 活动包假设，则其核分类给每段 $g=C_jf+B_j$，常平台上 $f'=f''=0$，仍有 $\mathcal W=0$，故同样被排除。

第三点不要求这些仿射偏移相同。上述结论也不把某个形式矩空间的 rank 认作 profile 的点态 rank。

原 Gaussian 词独立性与 R243/R304 的 gauge 偶部商保证 (34) 不能被零层、别的 history 或 $\mathcal W_e$ 项抵消。它不是仅在一个小正 $\sigma$ 的近似正值。

## 8. 尚未排除的弱 hook 通道必须真实保留

只有 (7) 时，(12)允许
$$
A_f=0
$$
的开区间内出现 $\mathcal W\ne0$。若其中 $f'\ne0$，则
$$
|f'|^{2/3}=\alpha x+\beta>0.
\tag{35}
$$
这包括 $f'$ 常数的退化情形以及真正曲的 $3/2$ 幂段。不能把一个孤立零点冒作自由开区间。

该自由没有被本稿赋予完整第三合法性：仍须原三矩、交三矩、第三 ruling 和真实拼接的所有端 jets。尤其不能先要求第二 hook 为零，再声称利用 (35) 逃逸；定理1已经证明两者在紧光滑类中不兼容。

(12)同时给一个可以继续真实构造的入口：若紧 $f$ 在严格内部 $J$ 上准确满足 $A_f=0$，则任一 $w\in C_c^\infty(J)$ 满足
$$
A_f\{w'f''-f'w''\}=0,
\qquad \mathfrak H(w;f,f)=0.
$$
最后一个零式包含原右锚两常数，不只是微分方程。它仍不自动满足 (2)，也不把完整第三 forcing 的四个 period 分别置零。下一建设必须对固定 seed 的原组合使用 (6)，并重新支付其余 range。

因此本稿既不宣布一般重叠或局部 rank-two 圆可行，也不把它们全部排除。已完成的新增内容是 (1) 的全局分类、(28)–(33) 的完整 mixed 推导，以及对当前强 hook-invisible 平面和 regular 弱核类的严格第四障碍。
