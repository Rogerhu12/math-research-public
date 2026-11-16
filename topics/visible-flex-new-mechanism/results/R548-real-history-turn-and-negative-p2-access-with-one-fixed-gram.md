# R548：同一固定规范下的真实高尾历史转向与负 $p_2$ 区间

日期：2026-11-16。**原式纸证；没有执行 profile、符号、求积、秩、数值或开发检查。**

本稿从 R544 的同一个真实 incoming 继续，不重置 $A,T$，不换其唯一第三规范(7)，也不借 33 母库的控制段。它得到一条实际延续：

- 全词仍有净 $p_1^{\omega_c}<0$、净 $t_1^{\omega_c}>0$；
- 曲率从 R544 的负值经过0，进入一个 $k>0$ 的开放区间，因而该区间原 $p_2=-kh/2<0$；
- 全部相位的完整 ruling 始终为0，原 frame、位置和所有历史／成本照常保留。

这里没有得到净 $p_2=0$ 或全矩阵零。此前正的 $p_2$ 累计不能仅由一个负密度区间宣告消失。

本稿需在 R544 从起点选择 $\omega_c$ 时先取它足够大。下面从同一个已冻结的 R521 profile 库证明这项有限选择可行；不改变母函数、不移动任何实际包，也不在已经运行的词中更换 $\omega_c$ 或 $\chi$。因此结论是 R544 原构造的一份明确从起点子族，而非所有预先冻结参数实例的免费后继。

## 1. 两个完整平方身份与一个可选的固定参考位置

采用原
$$
I_0(a,b)=\int a''b'',\qquad
I_{2,y}(a,b)=\int\{y^2a''b''+2a'b'\},\qquad y=x+\omega_c,
$$
并定义同一真右锚算子
$$
P(a,b)=J(a''b''),\qquad Y_y=\Phi_{p_2}^{\,y}.
\tag{1}
$$
对 $u$ 记 $p=u',r=u''$。R437 的完整原式为
$$
Y_y(u,u)
=-yu^2+y^2up-\frac{y^3}{2}p^2
-\frac{y^2}{4}J(y^2r^2+2p^2).
\tag{2}
$$
全部左尾均保留；特别一个实微包的 $Y_y(u,u)$ 左尾为
$-y^2 I_{2,y}(u,u)/4$。

令 $\Delta=f\odot f-g\odot g$，并定义真实四次量
$$
\mathcal Q_j(Z)=
-I_{j,y}(Z\Delta,Z\Delta)
+2I_{j,y}\{g,Z(g,Z\Delta)\},
\quad j=0,1,2.
\tag{3}
$$
$Z\Delta$ 真紧，因为 R521 的每个完整块已经有全部三矩圆。
另一个带尾槽不被截断；紧外槽使下述原 IBP 合法。

首先
$$
I_0\{u,P(u,u)\}
=-2\int r^2r'=-\frac23[r^3]=0.
$$
在真正紧变分方向 $v$ 上极化，得到
$$
2I_0\{u,P(u,v)\}=-I_0\{v,P(u,u)\}.
\tag{4}
$$
其次，R437(6)–(12)给完整身份
$$
I_{2,y}\{u,Y_y(u,u)\}=0,\qquad
2I_{2,y}\{u,Y_y(u,v)\}
=-I_{2,y}\{v,Y_y(u,u)\}.
\tag{5}
$$
坐标平移只改为 $y$，不改变同锚证明。

R521 的真实十六元正交平均使(3)对交换 $f,g$ 不变。这里可直接核所需范围：
$Y_y$ 的平移次数至多4，故(3)的次数至多 $8+j\le10$；
$P,I_0$ 的共同平移次数为0。原十一节点的正权矩准确支付这些多项式。
不同完整块的 $Z\Delta$ 真紧；其余二次左尾与紧外槽的三个 $I_j$ 配对为0，
所以没有新增跨块项。

由(4)(5)和这条交换不变性，
$$
\boxed{
\mathcal Q_0(P)=-\frac12 I_0(P\Delta,P\Delta)<0,
\qquad
\mathcal Q_2(Y_y)=-\frac12 I_{2,y}(Y_y\Delta,Y_y\Delta)<0.
}
\tag{6}
$$
严格性也是真实的。R521 至少有一个微包的两系数平方不等。
若 $P\Delta$ 为零，则该微包上的 $P(u,u)$ 会为常数，与其真左右尾之差
$I_0(u,u)>0$ 矛盾。若 $Y_y\Delta$ 为零，则该微包上的 $Y_y(u,u)$
必须为一个二次多项式；它在右平端的全部 jet 为0，故该多项式为0，
又与其非零左尾及 $y>0$ 矛盾。两个紧输出的相应正二次范数因而非零。

再从完整(2)按固定 $\omega_c$ 展开：
$$
Y_y=-\frac{\omega_c^4}{4}P+
\text{关于 }\omega_c\text{ 次数至多3的原双线性算子}.
$$
因此(3)准确是有限多项式，且
$$
\boxed{
\mathcal Q_0(Y_y)
=\frac{\omega_c^8}{16}\mathcal Q_0(P)+O(\omega_c^7)<0
}
\tag{7}
$$
对充分大的正 $\omega_c$ 成立。所有系数来自同一冻结 profile 库。
这是一次有限的从起点选择，不是新的 profile 实验。

以后把这样的 $\omega_c$ 固定，写 $Y=Y_y$、$Q_j=\mathcal Q_j(Y)$。
于是
$$
Q_0<0,\qquad Q_2<0.
\tag{8}
$$

## 2. 原 R544 的同一个 incoming 与继续方式

在上述 $\omega_c$ 下完成 R544 的全部原选择：
$$
\nu=\delta^{-2}(-H_0^2\lambda,2c,\lambda),\qquad
\delta=\lambda^2\zeta,\qquad H_0>\sqrt3H .
\tag{9}
$$
母库、$\chi$、第二规范 $w=0$ 及共同右锚从此固定。
令 R544 的高处目标高度为
$$
h_1=L_h/\sqrt\lambda,
$$
并记其真实水平量
$$
j=\eta/h+d/h^2,\qquad K=h_1^2j .
$$
在该文全部快段、过渡与长尾之后，
$$
K=K_*+o(1),\qquad K_*<-4,
$$
$$
d=O(h_1^{-1}),\quad
\bar A=\delta A=O(h_1^{-3}),\quad
\bar T=\delta^2\widetilde T=O(h_1^{-4}).
\tag{10}
$$
这里先小 $\lambda$、最后小 $\zeta$；$o(1)$ 可按同一选择顺序任意缩小。
原净 $p_1<0,t_1>0$ 已包含全部前缀。

接下来只继续 R544 同一个吸引反馈，目标高度仍为 $h_1$。
因此新的高尾起点与旧尾在一个开放区间逐 germ 相同。
有效三 Gram 仍准确为
$$
\Gamma=\bar\nu+
\frac12\mathbf I_y(\bar A\Delta,\bar A\Delta)
+2\mathbf I_y\{g,\bar T(g;\Delta)\},
\tag{11}
$$
它依赖真实历史，实际 $\chi$ 不变。

## 3. 原静态矩阵的全表与高高度主方向

在固定高度 $h$ 的水平曲线上，
$$
k=K-2d,\qquad \eta=(K-d)/h.
\tag{12}
$$
令
$$
a_1=\frac{K^2-2Kd-1}{h},\qquad
a_0=\frac{(K-d)(Kd-2d^2-1)}{h^2}.
$$
把 R73(6)(9)(10)逐项收集，原静态八矩恰为
$$
\boxed{
M_0=
\begin{pmatrix}
(1+d^2)/h\\ 2d\\ h
\end{pmatrix}
\begin{pmatrix}
-k/2&a_1/4&-a_0/2
\end{pmatrix}.
}
\tag{13}
$$
该外积的 trace 准确为0。没有删掉 $p_1,t_1$ 或其它静态项。

在固定有限的 $K,d$ 盒内，
$$
\boxed{
M_0/h=-\frac k2\,E_{p_2}+O(h^{-1}),
}
\tag{14}
$$
因此原 profile 算子为
$\Phi_{M_0}/h=-kY/2+O(h^{-1})$。
(14)只是可控制余项的全表极限；有限 $h$ 的实际路径仍用整个(13)。

## 4. 高尾上的完整慢极限

令新的继续段采用慢时间
$$
\tau=h_1^{3/2}\delta(s-s_{\rm in}),
$$
并置
$$
a=\sqrt{h_1}\,\bar A,\qquad t=h_1\bar T.
\tag{15}
$$
$r$、$t$ 在其它原稿中可能另有含义；本节 $t$ 是完整第三算子状态，
不是 profile 导数。

R544 的同一反馈使 $h=h_1+O(C(\lambda)\delta)$，
$h_s,k_s=O(C(\lambda)\delta)$，且
$d-q_\Gamma(h)=O(C(\lambda)\delta^2)$。
这些界可在新的有限 $\tau$ 区间上重新作联合 bootstrap：
要求 $a,t,K,d$ 处在固定紧盒，再用原(14)和同一个耗散估计关闭。
原正常矩阵的 $L_{\rm vel}$ 系数现在是 $O(h_1^{-1/2})$，
仍小于固定正阻尼与正刚度，不能把该项直接删掉。

全部真实缩放历史方程给
$$
a_\tau=\Phi_{M_{\rm raw}}/h_1,
$$
$$
t_\tau=-(\Phi_{M_{\rm raw}}/h_1)\circ a
+\frac{\delta}{\sqrt{h_1}}\,\mathcal C_{\rm slow}.
\tag{16}
$$
$\mathcal C_{\rm slow}$ 是 R544(14)的完整方括号；
其中两个加速度势、速度面积及变化-profile 项仍保留。
在上述反馈盒内它为 $O(C(\lambda)\delta)$。

原水平式还给 $j_s=-2dh_s/h^3$。
按 R544(51)对瞬时 $q_\Gamma$ 作真实分部积分，而非仅积分粗界，
在有限 $\tau$ 上得到 $K=K_*+o(1)$；
$\Gamma$ 的总变差在该段有界。所有误差先在固定 $\lambda$ 的有限几何盒上
按 $\zeta\to0$ 控制，再令 $\lambda$ 小。

由(10)(11)(14)–(16)，极限初值为 $a=t=d=0$，完整极限满足
$$
a_\tau=-\frac k2Y,\qquad
t_\tau=\frac k2Y\circ a,\qquad
k=K_*-2d,
$$
$$
\boxed{
2c\,d+\frac14 I_{2,y}(a\Delta,a\Delta)
+I_{2,y}\{g,t(g;\Delta)\}=0.
}
\tag{17}
$$
此处的代数约束来自真实 $\Psi_\Gamma(h,d)=o(1)$。
原 $\bar\nu_2h_1=\lambda h_1$ 趋0，$\Gamma_0/h_1$ 也趋0；
第三状态并没有被设为0。

(17)在该紧区间对 $d$ 的导数为 $2c>0$，所以它是一个普通光滑有限维 ODE。
原完整方程的系数及初值在此区间一致趋近它。
由普通 ODE 的有限时间连续依赖及前述联合 bootstrap，
实际反馈轨道真实跟踪下面的显式解；这不是只给一个形式主项。

## 5. 显式 Riccati 弧与真实 $\Gamma_0$ 变号

由(17)可令
$$
a=zY,\qquad t=-\frac{z^2}{2}Y\circ Y.
$$
定义
$$
A_Y=-Q_2/(8c)>0.
$$
准确化为
$$
\boxed{
d=-A_Yz^2,\qquad
z_\tau=-K_*/2-A_Yz^2,\qquad z(0)=0.
}
\tag{18}
$$
其解为
$$
z(\tau)=
\sqrt{\frac{-K_*}{2A_Y}}\,
\tanh\!\left(\sqrt{\frac{-K_*A_Y}{2}}\,\tau\right).
\tag{19}
$$
取一个固定有限 $\tau_*>0$ 使 $\tanh$ 恰为 $1/\sqrt2$。在该点
$$
d_*=K_*/4<0,\qquad k_*=K_*/2<0.
\tag{20}
$$
并且整段 $0\le\tau\le\tau_*$ 上 $k$ 位于 $K_*$ 与 $K_*/2$ 之间。
因为 $K_*<-4$，原静态 $t_1=(K_*k-1)/8$ 有统一正下界。
$p_1=-kd$ 的极限积分严格为负；无需预设实际每一点的微小误差同号。

设 $z_*=z(\tau_*)$。由(11)(17)，实际段末
$$
\boxed{
h_1\Gamma_0\longrightarrow g_0:=-z_*^2Q_0/2>0,\qquad
h_1\Gamma_2\longrightarrow g_2:=-z_*^2Q_2/2>0,
}
\tag{21}
$$
且 $\Gamma_1=2c+O(h_1^{-1})$。
原 $\bar\nu_0h_1=-H_0^2\lambda h_1$ 趋0，所以(21)确实使完整有效
$\Gamma_0$ 从 R544 的初始负值变为正。改变的是同一个真实第三历史，
不是规范向量(9)。

实际累计还满足，对某些固定 $c_1,c_t>0$，
$$
\boxed{
\int_{\rm coast}M_{p_1}\,ds
\le-\frac{c_1}{h_1^{3/2}\delta},\qquad
\int_{\rm coast}M_{t_1}\,ds
\ge\frac{c_t}{h_1^{3/2}\delta}.
}
\tag{22}
$$
完整 $h_s^2/h^2$ 项由同一反馈估计趋0；未用极限静态代替它。
这两项强化 R544 原来的两个净符号。

## 6. 不换规范的有限下降与真正 $k>0$ 入口

现在停止的是预选高尾的慢时间长度，不是历史演化。取(21)对应的真实末值
$\Gamma^{e}$，并从该点继续同一个 R544(32)反馈。只把参考高度从
$h_1$ 经一条光滑有限路径降到 $H$；该参考路径在两端开放区间恒定。
其时长及全部所需导数在固定 $\lambda$ 后有限选定，不依赖最后取小的
$\zeta$。新旧段的原控制与全部端 jets 因而通过同一开放高尾连接。

写 $g_j=\Gamma_j^{e}$。由(21)，
$$
g_0=\frac{g_0^*+o(1)}{h_1}>0,\qquad
g_2=\frac{g_2^*+o(1)}{h_1}>0,\qquad
g_1=2c+O(h_1^{-1}),
\tag{23}
$$
其中 $g_0^*,g_2^*>0$ 就是(21)的两个极限常数。
在 $H\le h\le h_1$，
$$
g_1^2-g_0g_2-g_0^2/h^2>c^2
$$
对充分小 $\lambda$ 一致成立。于是同一个稳定支仍由准确公式
$$
\frac{q_g(h)}h=
-\frac{g_2+g_0/h^2}
{g_1+\sqrt{g_1^2-g_0g_2-g_0^2/h^2}}
\tag{24}
$$
给出。它没有经过分支判别式为0的点。

对这一固定有限高度路径，完整反馈的同一个法向能量给
$$
h-\bar h=O(C_\lambda\delta),\qquad
\gamma-v_*=O(C_\lambda\delta),
$$
$$
d-q_\Gamma(h)
=\delta\,\ell v_*/\alpha+O(C_\lambda\delta^2),
\qquad
d_s-q_{\Gamma,h}\gamma=O(C_\lambda\delta).
\tag{25}
$$
这里 $v_*=\bar h_s-\kappa_h(h-\bar h)$，$\alpha,\ell$ 仍是 R544(31)
的完整系数。尤其在非恒高度段不能把第一法向误差误写成 $O(\delta^2)$；
它的真实速度线性平衡项已经显示在(25)中。
加速度由原反馈质量系数及 ruling 同时确定，均为 $O(C_\lambda)$。
在固定 $\lambda$ 的有限过渡上，原 $M_{\rm raw}$ 及
$\mathcal C_{\rm slow}$ 因而有界。完整历史方程给
$$
\Gamma(s)-\Gamma^e=O(C_\lambda\delta).
\tag{26}
$$
选 $\delta$ 足够小可令此误差比 $h_1^{-2}$ 更小。
(26)是原 $A,T$ 的实际累计估计，不是把 $\Gamma$ 冻结成控制。

为给出末端符号，先计算固定 $g=\Gamma^e$ 的精确参考水平输运。
由(24)有一致展开
$$
q_g(h)=-\frac{g_2h+g_0/h}{2g_1}
       +O\!\left(\frac{h+h^{-1}}{h_1^3}\right).
\tag{27}
$$
余项不仅在每个点小；乘 $h^{-3}$ 后的积分在整个 $[H,h_1]$
为 $O(h_1^{-3})$。令高处的 $K=h_1^2j_{\rm in}=K_*+o(1)$。
原水平式准确给
$$
j_g(H)=\frac K{h_1^2}
       -2\int_{h_1}^{H}\frac{q_g(r)}{r^3}\,dr .
\tag{28}
$$
用(27)并保全部端项，
$$
\begin{aligned}
k_g(H)
={}&H^2j_g(H)-2q_g(H)\\
={}&\frac{H^2K}{h_1^2}
+\frac{g_2H^2}{g_1h_1}
+\frac{2g_0}{3g_1H}
+\frac{g_0H^2}{3g_1h_1^3}
+O(h_1^{-3}).
\end{aligned}
\tag{29}
$$
首项仍包含 R544 与整个新高尾的真实水平入值；
它并没有被任意调成0。

对实际路径使用(25)(26)和原 $j_s=-2dh_s/h^3$，有限时间连续依赖
把(28)(29)的末值误差控制为 $O(C_\lambda\delta)$。
结合(23)，先小 $\lambda$、最后小 $\zeta$，得到
$$
\boxed{
k_{\rm low}
=\frac{g_0^*}{3cH\,h_1}+o(h_1^{-1})>0,
}
$$
$$
\boxed{
d_{\rm low}
=-\frac{g_2^*H+g_0^*/H}{4c\,h_1}
+o(h_1^{-1})<0.
}
\tag{30}
$$
这里的 $o(h_1^{-1})$ 保留了高尾连续依赖的真实精度；
没有把仅已知的小量自动提升为 $O(h_1^{-2})$。

由连续性，在继续使用相同反馈、参考高度恒为 $H$ 的一个固定正长度
开放区间内，(30)的两个严格号仍成立。长度可以在固定 $\lambda$ 后选定，
再取更小 $\zeta$ 保其统一余量。在此区间
$$
\boxed{M_{p_2}=-kh/2<0.}
\tag{31}
$$
前面的高尾有 $k<0$，所以同一实际路径确实经过了 $k=0$，
而非仅改变固定坐标记号。低处开段的实际 $h,k,\Gamma$ 仍按全 ODE 演化；
“参考高度恒定”不等于把真实 scalar 或历史强行置为常数。

## 7. 整条路径的合法窗口与全部累计

### 7.1 原合法性没有在下降时丢失

(27)–(29)在任意中间 $h\in[H,h_1]$ 的同一计算给
$$
|k(h)|\le C,\qquad
\left|\frac{k(h)}h\right|
+\left|\frac{d(h)}h\right|+|\eta(h)|
\le C/h_1 .
\tag{32}
$$
实际误差由(25)(26)最后取小 $\delta$ 控制。
因此原固定 $Hy_{\min}>1$ 给
$$
y+\eta>0,\qquad hy+d>0,
$$
以及更强的真实余量
$$
\boxed{
h^2(y+\eta)^2-k^2-1>0
}
\tag{33}
$$
在整个下降和低处开段成立。
新的高尾上 $k,d$ 有界而 $h\asymp h_1$，同样满足(33)。
$C_k,B$ 的完整正性和反馈质量系数因而始终保留。
所有涉及 profile 的原真右尾、$YC$ 与端点势仍在同一个合法域计算。

### 7.2 有限下降成本由长高尾的真实符号控制

固定 $\lambda$ 后，下降及所选低处开放段的 scalar、速度、加速度处于一个
固定有限盒中。即使原 $A,T$ 随 $\delta^{-1},\delta^{-2}$ 很大，
其缩放状态仍按(16)(26)受控，(25)给真实几何速度界。因此存在有限
$C_{\rm desc}(\lambda)$，与最终取小的 $\zeta$ 无关，使
$$
\left|\int_{\rm descent+low}M_{p_1}\,ds\right|
+\left|\int_{\rm descent+low}M_{t_1}\,ds\right|
\le C_{\rm desc}(\lambda).
\tag{34}
$$
这包含 $-(h_s/h)^2/8$ 的全部真实负成本，不只计静态项。

R544 的原完整前缀已有净 $p_1<0,t_1>0$。
本稿的新高尾另给(22)，故最后再令 $\zeta$ 足够小，
$$
\frac{\min(c_1,c_t)}{h_1^{3/2}\delta}
>C_{\rm desc}(\lambda)+1
\tag{35}
$$
就保证加入下降后，整条同一实际词仍满足
$$
\boxed{
\int_{\rm whole}M_{p_1}^{\omega_c}\,ds<0,\qquad
\int_{\rm whole}M_{t_1}^{\omega_c}\,ds>0.
}
\tag{36}
$$
并同时具有(31)的实际负 $p_2$ 开段。

这项选择不循环。顺序为：

1. 在同一已付 R521 库中一次选足够大的合法 $\omega_c$，付(8)；
2. 固定 R544 的 $H,H_0,c,L_h$、快入控制与原尾长常数；
3. 由(18)(19)固定新的有限慢时间 $\tau_*$；
4. 取足够小的固定 $\lambda$，并据此固定 $h_1$、有限下降路径及低处开段；
5. 最后取一个固定正 $\zeta$，同时支付 R544 的全部原门、
   新高尾的真实有限时间跟踪、(25)–(35)。

在最后得到的这一条词上，$\delta,\lambda,\chi$ 都只是有限固定数据。
长高尾虽然随最后选择增长，但它的最大区间延拓已由第4节的联合状态盒、
耗散估计与有限慢时间 ODE 支付，不能以“有限时长”一词替代该证明。

## 8. 完整结论与下一项真实缺口

**定理。** 对 R521 已付的一个实际正交母库，可从起点选择一个有限
$\omega_c$，再完成 R544 的唯一规范(9)及全部真实零历史入段，使同一
光滑实际路径在不更换任何 profile 或规范、不重锚累计的条件下：

1. 全部相位的完整 fourth ruling 逐点为0；
2. 整个词的两个净矩满足(36)；
3. 实际曲率从负值穿过0，并在一个开放区间为正；
4. 该区间的原 $p_2$ 密度严格为负，且原完整合法窗口保持。

新增作用来自真实高尾的 $A,T$ 演化，使有效 $\Gamma_0$ 发生(21)的严格变号。
它准确绕过了“冻结 R544 初始有效 Gram 后 $k$ 一直为负”的限制。
这没有给沿路径自由改 $\Gamma$ 的权利；$\Gamma$ 全程由(11)(16)唯一决定。

本稿**没有**证明总 $p_2=0$。新高尾的 $p_2$ 仍为正，其真实累计一般很大，
后面一个负密度区间不自动把它抵消；其余五矩也没有被删除。
scalar 末端不被称为原周期 germ，frame／位置、第三和第四 period、
同十三规范及最终主问题仍待支付。

后继必须利用这条已经到达的同规范真实入态，继续研究足够的负 $p_2$
累计或其它矩的联合返回。不能拼接另一母库的分支、重置高尾历史，
也不能用 R70 的无 ruling 桥代替本稿原反馈内部。

### 原来源与窄核范围

- [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)(6)(9)(10)(17)：
  原八矩全表、水平式与有序第三累计；(13)是其直接完整收集；
- [R437](R437-highest-rational-gauge-row-vanishes-on-the-complete-period-kernel.md)(6)–(12)：
  真右锚 $Y_y$ 及完整 $I_2$ 三次身份；
- [R521](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md)：
  同一个有限正 $O(2)$ 库、0…10真实共同位置矩、三矩圆与双 collar，
  以及全部 third history 下的完整 ruling；
- [R537](R537-prescribed-finite-height-paths-with-one-gauge-and-complete-history-energy-bounds.md)：
  无 $k_{ss}$ 的完整第三变量及其速度面积；
- [R544](R544-one-fixed-gram-and-a-real-path-with-negative-p1-and-positive-t1.md)：
  本稿逐 germ 接续的实际零历史词、同一吸引反馈和两个原净矩。

proof_review 仅纸核了(4)–(7)在准确 $\Delta=f\odot f-g\odot g$
与交换不变前提下的 $-1/2$ 系数及有限大 $\omega_c$ 选择；
本稿没有把这项窄核称为全篇审核。全部新高尾、真实历史转向、
有限下降及累计界均由以上原式证明承担。没有任何新科学执行。
