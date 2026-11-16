# R552：同一固定规范下三个 $p$ 矩的真实联合零与正的 $t_1$ 余量

日期：2026-11-16。**完整原式纸证；没有执行数值、符号、profile、求积、秩或开发检查。**

本稿继续 R544/R548/R550 的同一 R521 正交母库。新增控制不是自由拼接正负矩原子，而是在原高尾饱和之后插入一个真实低处驻留。其原 $-Z/8$ 静态项同时改变第三历史和下一次水平上升的入值。把这两个作用共同保留，得到两个真实参数，准确支付
$$
\boxed{P_0=P_1=P_2=0,\qquad T_1>0.}
\tag{1}
$$
这里所有累计都从原零历史起点开始；整条词共用一个 $\chi$、一个 $w=0$、同一 profiles 和同一右锚。$T_1$ 的正号包含快入、对数等待、低处负成本、所有实际高度过渡及最后高尾。

本稿不把 R550 已完成的 $P_2=0$ 末端删去成本后重新开始。采用的是它所支付的**共同高尾饱和前缀**，然后选择下述新的实际后继。没有中途换规范。全八矩仍未闭，末端 frame、位置、第三／第四 period 以及原同十三规范也未返回。

## 1. 固定坐标、三个原矩和完整有序配对

固定 $y=x+\omega_c$，写
$$
\eta=\omega-\omega_c,\qquad d=h\eta-k,\qquad
j=\frac{\eta}{h}+\frac d{h^2},\qquad
\mathfrak r=hj=\frac{k+2d}{h}.
$$
R73/R549 的完整原式为
$$
\begin{gathered}
p_2=-kh/2,\qquad p_1=-kd,\qquad
p_0=-\frac{k(1+d^2)}{2h},\\
8t_1=k^2+2kd-1-(h_s/h)^2,\qquad
j_s=-2d h_s/h^3.
\end{gathered}
\tag{2}
$$
因此，令 $u=d/h$，
$$
(p_0,p_1,p_2)=p_2(u^2+h^{-2},\,2u,\,1),
$$
$$
t_1=-\frac{\mathfrak r}{4}p_2-\frac18-\frac{h_s^2}{8h^2}.
\tag{3}
$$
$P_i,T_1$ 分别表示整条真实词上对应密度的积分。全部时间都是原 $s$，后文的慢时间只用于分析。

取
$$
Y=\Phi_{p_2}^{\,y},\quad Z=\Phi_{t_1}^{\,y},\quad
\mathcal R=\Phi_{r_1}^{\,y},\quad
\Delta=f\odot f-g\odot g.
$$
原完整 profiles 是
$$
Z(v,v)=y^2(v')^2+yJ\{y^2(v'')^2+2(v')^2\},
$$
$$
\mathcal R(v,v)=(v')^2+yJ((v'')^2).
\tag{4}
$$
$J$ 始终是真右积分，其左多项式尾没有删除。

记 $I_0$ 与 $I_{2,y}$ 为原第一、第三二阶配对，定义
$$
\mathcal B_j(E,F)
=I_{j,y}(F\Delta,E\Delta)
-2I_{j,y}\{g,E(g,F\Delta)\}.
\tag{5}
$$
这个双线性形式一般不对称。R548 已付
$$
Q_j=-\mathcal B_j(Y,Y)<0\quad(j=0,2).
$$
若
$$
\Xi_j(a,b)=\frac12 I_{j,y}(a\Delta,a\Delta)
+2I_{j,y}\{g,b(g;\Delta)\},
$$
且完整第三历史的主式为 $db=-da\circ a$，则
$$
d\Xi_j=\mathcal B_j(da,a).
\tag{6}
$$
(6)中的复合次序来自原 $T_s=-\Phi_{M_{\rm raw}}\circ A+C_s$，不能对称化。

### 1.1 从起点同时固定一个新的严格号

置
$$
B_{21}=\mathcal B_2(Z,Y),\quad
B_{12}=\mathcal B_2(Y,Z),\quad
D_*=2B_{21}-B_{12}.
$$
本稿在 R550 原 $B_{21}<0$ 之外，同时要求
$$
\boxed{D_*<0.}
\tag{7}
$$
它由同一次足够大的有限正 $\omega_c$ 支付，不需换母。
令 $P(v,v)=J((v'')^2)$。R437、(4)和 R548 的真实正交库给
$$
Y=-\omega_c^4P/4+O_{\rm op}(\omega_c^3),\quad
Z=\omega_c^3P+O_{\rm op}(\omega_c^2),\quad
I_{2,x+\omega_c}=\omega_c^2I_0+O(\omega_c),
$$
$$
\mathcal Q_0(P)=-\frac12I_0(P\Delta,P\Delta)<0.
$$
由(5)，两个不同次序具有同一最高系数：
$$
B_{21}=\frac{\omega_c^9}{4}\mathcal Q_0(P)+O(\omega_c^8),
\qquad
B_{12}=\frac{\omega_c^9}{4}\mathcal Q_0(P)+O(\omega_c^8).
$$
故
$$
D_*=\frac{\omega_c^9}{4}\mathcal Q_0(P)+O(\omega_c^8)<0.
\tag{8}
$$
这是冻结 profiles 上的有限多项式展开；没有交换未固定 profiles 的极限。
以后 $\omega_c$ 不再变化。本定理是原 R544/R550 从起点选择中的一份明确子族；不把(7)授予任意另行冻结的旧参数。

## 2. 同一个 $\chi$、真历史及已付共同前缀

沿用 R544 的唯一 Gram 数据
$$
\nu=\delta^{-2}(-H_0^2\lambda,2c,\lambda),\qquad
\delta=\lambda^2\zeta,\qquad
R=L_h/\sqrt\lambda .
\tag{9}
$$
这里 $H,H_0,c,L_h$ 及原快入控制已按该稿选择，$c>0$、$H_0>\sqrt3H$、
$K_*<-4$。定义
$$
A_Y=-Q_2/(8c)>0,\qquad
z_\infty=\sqrt{-K_*/(2A_Y)}>0,
$$
$$
g_j=-z_\infty^2Q_j/2>0\ (j=0,2),\qquad
g_2=-2cK_* .
\tag{10}
$$

采用完整慢状态
$$
\bar A=\delta A,\qquad
\bar T=\delta^2\widetilde T,\qquad
a=\sqrt R\,\bar A,\qquad b=R\bar T,
$$
$$
\Gamma_j=\bar\nu_j+\Xi_j(a,b)/R.
\tag{11}
$$
$\widetilde T$ 包括 R544 的原加速度势校正；没有把它替换为对称的 $-A^2/2$。
原 $p_2$ 累计的准确坐标为
$$
\boxed{z=a_{p_2}=\sqrt R\,\delta\,\mathsf m_{p_2}.}
\tag{12}
$$
从快入开始，所有段均使用同一 $(R,\delta)$；所以真正停在 $z=0$ 就是整词 $P_2=0$。

取 R550 第3节已付的对数高尾末端为共同前缀末端。该前缀真实地从零 $A,T$ 开始。完整末值满足
$$
\begin{gathered}
k_e=\kappa_e/R+O((1+\log R)^2/R^2)>0,\qquad
\kappa_e=B_{21}/(4Q_2)>0,\\
a_e=z_\infty Y+O((1+\log R)^2/R),\\
b_e=-z_\infty^2Y\circ Y/2+O((1+\log R)^2/R),\\
\Gamma_0^e=g_0/R+O((1+\log R)^2/R^2),\\
\Gamma_2^e=g_2/R+O((1+\log R)^2/R^2),\qquad
\Gamma_1^e=2c+O(R^{-1}).
\end{gathered}
\tag{13}
$$
同一个真实入值的水平无穷高系数为
$$
W_\infty^e=\kappa_e/R^3+O((1+\log R)^2/R^4)>0.
\tag{14}
$$
$z_e-z_\infty$ 的差及前缀中全部非 $Y$ 历史都保留在(13)，后文没有把它们置零。

### 2.1 本稿再次使用的完整反馈接口

瞬时稳定支始终是
$$
\frac{q_\Gamma(h)}h
=-\frac{\Gamma_2+\Gamma_0/h^2}
{\Gamma_1+\sqrt{\Gamma_1^2-\Gamma_0\Gamma_2-\Gamma_0^2/h^2}}.
\tag{15}
$$
同 R544 的真实单输入反馈支付
$$
h-\bar h=O(C_R\delta),\qquad
h_s-v_*=O(C_R\delta),
$$
$$
d-q_\Gamma(h)
=\delta\,\ell_{\rm vel}v_*/\alpha+O(C_R\delta^2),
\qquad
d_s-q_{\Gamma,h}h_s=O(C_R\delta).
\tag{16}
$$
非恒参考高度段第一项确为 $O(\delta)$，不能误写成 $O(\delta^2)$。
开放恒参考段上则 $h_s,k_s=O(C_R\delta)$。

本文后继允许 $k$ 随 $R$ 增大，但始终
$$
|k/h|+|d/h|+|\eta|=o(1).
\tag{17}
$$
R544 的速度线性界仍适用：直接看 R221(17)，
$e/h=y+d/h$、$e_s=h_s(y+\eta)-k_s/2$；所有除以 $h^4$ 后的系数只需
$h^{-1},d/h,\eta$ 有界，不需未除以 $h$ 的 $k$ 有一个与 $R$ 无关的上界。
故 $\ell_\gamma,\ell_\upsilon=O(\|\bar A\|)$，而本稿始终
$\|\bar A\|=O(R^{-1/2})$。$C_k,B$ 仍有原严格正界，
$\partial_d\Psi_\Gamma\ge c$，反馈质量、刚度、阻尼不退化。

完整历史方程仍是
$$
\bar A_s=\delta\Phi_{M_{\rm raw}},\qquad
\bar T_s=-\delta\Phi_{M_{\rm raw}}\circ\bar A
+\delta^2\mathcal C_{\rm slow}.
\tag{18}
$$
$\mathcal C_{\rm slow}$ 保原速度面积、速度三次项及
$2\mathcal A h_{ss}k_s$ 等全部项。它不被静态矩阵替代。
在有限参考过渡上，其完整范数界记入 $C_R$；在下述两段长尾上，
用(16)(18)和真实联合状态盒支付统一延拓。

## 3. 两个新参数及非循环选择次序

先固定一个正数 $\mathfrak b>0$。置
$$
M=(1+\log R)^6,\qquad \epsilon_R=M/R.
\tag{19}
$$
后面两个新参数记为
$$
\ell>0,\qquad \xi>0.
$$
它们最终在一个固定、严格位于正象限内的紧盒 $\mathcal P$ 中变化。
$\chi$ 的(9)完全不依赖 $\ell,\xi$。

从共同前缀末端沿原反馈下降到参考高度
$$
H_{\rm low}=\sqrt{M\xi}.
\tag{20}
$$
该高度的可调参数是 $\xi$。
然后保持这个参考高度，原真实时长取
$$
\boxed{T_{\rm low}=\frac{M\ell}{\delta R^{3/2}}.}
\tag{21}
$$
这里没有自由指定 $p_2$ 密度或冻结 $\Gamma$。接着按第5节的真实水平末值确定一个有限高目标，再作最后一段高尾，准确停在 $z=0$。

先固定 $\mathfrak b,\mathcal P$，再取充分大的有限 $R$；由此固定 $M,\lambda$。
之后才选所有有限高度参考路径及其导数界。最后选一个统一小的正
$\zeta$，即固定(9)中的唯一 $\delta$ 和 $\chi$。一切 $\delta C_R$ 误差及有限过渡的真实成本在这最后一步共同控制。不能先令高度或时长依赖 $\delta$，再借有限盒估计。


## 4. 低处驻留的真实历史与成本

下文的 $o^1_{\mathcal P}$ 表示参数盒 $\mathcal P$ 上的值和一阶参数导数都小。
其极限次序是先 $R\to\infty$，再在每个固定 $R$ 上统一取小 $\delta$。
对于只由 $R$ 产生的误差，可用
$$
\varepsilon_{\rm rem}(R)=
\frac{(1+\log R)^4}{M}+\frac{M^2}{R}+\frac1M
\longrightarrow0
\tag{22}
$$
作一个保守统一模量；另加最后选择的 $C_R\delta$ 项。
本稿不以值的一致收敛代替最后 IFT 所需的 $C^1$ 收敛。

### 4.1 真低入点及长期存在

暂用共同前缀的真实 $\Gamma^e$ 作参考，原水平式给
$$
\frac{k_g(h)}{h^2}
=W_\infty^e+
2\Gamma_0^e\int_h^\infty
\frac{dr}{r^4
\sqrt{(\Gamma_1^e)^2-\Gamma_0^e\Gamma_2^e-(\Gamma_0^e)^2/r^2}} .
\tag{23}
$$
所以整个下降上 $k_g>0$。在(20)处，
$$
k_{\rm in}
=\frac{g_0}{3cH_{\rm low} R}\{1+o^1_{\mathcal P}(1)\},
\qquad
\frac{d_{\rm in}}{H_{\rm low}}
=-\frac{g_2}{4cR}
-\frac{g_0}{4cM\xi R}+o^1_{\mathcal P}(R^{-1}).
\tag{24}
$$
实际有限下降的全部历史和法向误差为 $O(C_R\delta)$；
通过最后选择 $\delta$，(24)同样适用于真入点。

在低尾用
$$
\theta=\frac{\delta R^{3/2}}M(s-s_{\rm low}),\qquad 0\le\theta\le\ell .
$$
在 $a,b$ 的固定大盒中，原静态全矩阵逐列给
$$
\Phi_{M_0}
=-\frac18Z-\frac1{8H_{\rm low}^2}\mathcal R
+O_{\rm op}(R^{-1}).
\tag{25}
$$
首两项正是原 $k=\eta=0$ 的完整 $\Phi_{M_0}$。误差保实际
$k=O((\sqrt M R)^{-1})$、$d=O(\sqrt M/R)$ 及所有八列；没有删掉原 potential。
真实 $M_2$、$h-H_{\rm low}$ 及完整速度误差另记入 $o_\delta(1)$。

由(18)，准确的低尾慢方程为
$$
a_\theta=\frac MR\Phi_{M_{\rm raw}},\qquad
b_\theta=-\frac MR\Phi_{M_{\rm raw}}\circ a
+\frac{M\delta}{\sqrt R}\mathcal C_{\rm slow}.
\tag{26}
$$
它先给 $\Delta a,\Delta b=O(M/R)$，进而
$\Delta\Gamma=O(M/R^2)$。
结合真实 $j$ 的长尾分部积分，曲率的改变量为
$$
\Delta k=O(M^{3/2}/R^2)+O(C_R\delta).
$$
相对于(24)的正首项，其比值为 $O(M^2/R)=o(1)$。故整段
$$
k>0,\quad d<0,\quad
p_2=-\frac{g_0}{6cR}\{1+o^1_{\mathcal P}(1)\}.
\tag{27}
$$
这不是预先把 $p_2$ 指定成常数；(27)由同一全状态 ODE 得出。

(26)改进最初的 $a,b$ 盒；(16)的耗散法向估计改进几何管。
因此在整个固定 $\theta$ 区间上可延拓，真实物理时长虽为
$M\ell/(\delta R^{3/2})$，不会产生普通 Gronwall 的指数时间损失。
参数变分用同一个耗散法向基解和有限 $\theta$ 的慢状态变分方程控制，
故上述结论及下面的首项均为 $C^1(\mathcal P)$。

### 4.2 不对称第三历史的实际增量

由(25)(26)，低尾末端准确有
$$
\Delta a
=-\frac{M\ell}{8R}Z-\frac{\ell}{8\xi R}\mathcal R
+o^1_{\mathcal P}(M/R),
$$
$$
\Delta b
=\frac{M\ell z_\infty}{8R}\,Z\circ Y
+o^1_{\mathcal P}(M/R).
\tag{28}
$$
第二行的正号及 $Z\circ Y$ 次序来自 $-\Phi_M\circ a$。
$\mathcal R$ 对应的完整复合也在余项中保留，其大小为 $O(R^{-1})$，
相对于 $M/R$ 严格低阶；没有以“尾常数”名义删去它。

用(6)，
$$
\boxed{
\Delta\Gamma_2
=-\frac{M\ell z_\infty B_{21}}{8R^2}
+o^1_{\mathcal P}(M/R^2)>0.
}
\tag{29}
$$
这是真第三历史改变有效 Gram，物理 $\nu$ 和 $\chi$ 均未改变。
其它两个 $\Delta\Gamma_j$ 也为 $O(M/R^2)$，后文一起带入水平式。

### 4.3 低尾四个实际成本

(3)(20)(21)(27)给
$$
\delta\Delta P_2^{\rm low}
=-\frac{g_0M\ell}{6cR^{5/2}}
+o^1_{\mathcal P}(M/R^{5/2}),
$$
$$
\boxed{
\delta\Delta P_0^{\rm low}
=-\frac{g_0\ell}{6c\xi R^{5/2}}
+o^1_{\mathcal P}(R^{-5/2}),
}
$$
$$
\delta\Delta P_1^{\rm low}=O_{\mathcal P}(M/R^{7/2}),
$$
$$
\boxed{
\delta\Delta T_1^{\rm low}
=-\frac{M\ell}{8R^{3/2}}
+o^1_{\mathcal P}(M/R^{3/2}).
}
\tag{30}
$$
$P_0$ 的首项是实际 $h^{-2}p_2$；$u^2p_2$ 仍在较低阶中。
$T_1$ 包含 $-(h_s/h)^2/8$：开放恒参考段的真实
$h_s=O(C_R\delta)$，故其缩放积分在最后选择 $\delta$ 时为小量。
低尾的负 $T_1$ 首项不能丢掉。

## 5. 真实水平量改变与后继高度

### 5.1 新的 $W_\infty$ 不是原 R550 的值

设低尾末端的真入值为 $(h_l,j_l,\Gamma^l)$。
在其固定-$\Gamma^l$ 水平参考曲线上，准确有
$$
W_\infty^l
=j_l-\frac{2q_{\Gamma^l}(h_l)}{h_l^2}
-2\Gamma_0^l\int_{h_l}^\infty
\frac{dr}{r^4\sqrt{(\Gamma_1^l)^2-\Gamma_0^l\Gamma_2^l-(\Gamma_0^l)^2/r^2}}.
\tag{31}
$$
在本稿的小 $\Gamma_0,\Gamma_2$ 域中，
$$
W_\infty^l
=j_l+\frac{\Gamma_2^l}{\Gamma_1^l h_l}
+\frac{\Gamma_0^l}{3\Gamma_1^l h_l^3}
+\text{更低阶项}.
\tag{32}
$$
比较低尾前后，原真实水平 $j$ 在恒参考段的变化为
$O(C_R\delta)$；其长期界由 R544 的水平分部积分支付。
(29)经(32)的 $1/(\Gamma_1h_l)$ 系数给主增量。
$\Delta\Gamma_0$ 的贡献低 $M^{-1}$，$\Delta\Gamma_1$ 的贡献低 $R^{-1}$。
原(14)同样严格低阶。因此
$$
\boxed{
W_\infty^l
=C_W\frac{\ell}{\sqrt\xi}\frac{\sqrt M}{R^2}
\{1+o^1_{\mathcal P}(1)\}>0,
\qquad
C_W=-\frac{z_\infty B_{21}}{16c}>0 .
}
\tag{33}
$$
这里特别不能沿用 R550 的 $W_\infty\asymp R^{-3}$，也不能免费指定一个可比高度的负曲率端口。

### 5.2 一个由真入值确定的有限高目标

从 $(h_l,j_l,\Gamma^l)$ 作固定-$\Gamma^l$ 的精确水平参考。
其
$$
\mathfrak r_g(h)=h j_g(h),\qquad
(\mathfrak r_g)_h=k_g(h)/h^2>0
\tag{34}
$$
在 $h\ge h_l$ 成立：$\Gamma_0^l>0$ 且(33)使(23)的对应版本全正。
又 $\mathfrak r_g(h)\to+\infty$，所以存在唯一有限 $H_f$ 使
$$
\boxed{\mathfrak r_g(H_f)=\mathfrak b M/R.}
\tag{35}
$$
$H_f$ 对低尾的真实入值和 $\ell,\xi$ 光滑依赖。由(33)，
$$
\boxed{
H_f=\frac{\mathfrak b\sqrt\xi}{C_W\ell}\sqrt M\,R
\{1+o^1_{\mathcal P}(1)\}.
}
\tag{36}
$$
这是一个已确定的有限参考高度，不是任意赋予 $j$ 或重锚矩阵。

现在沿同一个反馈，由 $H_{\rm low}$ 真实升到 $H_f$。
在每个固定 $R$ 及紧参数盒上，选一族两端参考高度平坦的有限光滑过渡；
其导数、全原矩和速度平方成本界皆有限，记入 $C_R$。
由(16)(18)，实际 $\Gamma$ 变化和相对于(34)的水平误差为 $O(C_R\delta)$。
因此真高入点满足
$$
\mathfrak r=\mathfrak b M/R+o^1_{\mathcal P}(M/R),\qquad
h=H_f+O(C_R\delta).
\tag{37}
$$
上升没有冻结第三历史。(35)只是用于选择实际控制的参考目标。

所有这些过渡上 $|u|=O(R^{-1})$、
$|k/h|+|\eta|=O(M/R)$；最小新高度为 $\asymp\sqrt M$。
所以原 $y+\eta>0$、$hy+d>0$ 以及
$$
h^2(y+\eta)^2-k^2-1>0
\tag{38}
$$
都有严格余量。全部真右尾、$YC$、第三原函数和反馈质量仍在同一个合法域。


## 6. 最后高尾与准确 $P_2=0$

到达(37)后参考高度恒为 $H_f$，仍使用同一个反馈。令
$$
\sigma=\delta M^2R^{3/2}(s-s_f).
\tag{39}
$$
$H_f/(\sqrt M R)$ 在 $\mathcal P$ 上有严格正的上下界。
在包含 $[0,z_\infty]$ 的固定 $z$ 盒内，原稳定约束给
$$
u=\frac dh=-\frac{A_Yz^2}{R}+O_{\mathcal P}(M/R^2)
+o_\delta(R^{-1}),
$$
$$
\frac kh=\mathfrak b M/R+2A_Yz^2/R+o^1_{\mathcal P}(M/R).
\tag{40}
$$
特别 $k\asymp M^{3/2}>1$。

在这段上准确有
$$
a_\sigma=\frac{\Phi_{M_{\rm raw}}}{M^2R},\qquad
b_\sigma=-\frac{\Phi_{M_{\rm raw}}}{M^2R}\circ a
+\frac{\delta}{M^2\sqrt R}\mathcal C_{\rm slow}.
\tag{41}
$$
原矩阵全表说明，除 $p_2$ 外，唯一相对大小达到 $M/R$ 的列是 $t_1$；
$p_1/p_2=2u=O(R^{-1})$，其余列更小。
完整 $M_2$ 和 $\mathcal C_{\rm slow}$ 用(16)(18)控制，不把(41)改成静态方程。

由(12)，原 $p_2$ 密度给**准确**导数
$$
\boxed{z_\sigma=-\frac{kh}{2M^2R}<0.}
\tag{42}
$$
(36)(40)使它在参数盒和整个目标 $z$ 区间上一致远离0。
联合状态盒与(41)的有限慢时间连续依赖因此保证到达 $z=0$。
该停止时刻唯一，且对 $\ell,\xi$ 为 $C^1$；准确满足
$$
\boxed{P_2=0.}
\tag{43}
$$
停止时刻仍在一个统一有限的 $\sigma$ 区间中。没有把极限 $z=0$
代替实际原矩坐标的零。

### 6.1 第一横向历史的完整形状

定义
$$
w=\frac{a_{t_1}}{\epsilon_R},\qquad \epsilon_R=M/R.
$$
由于(3)，在最后高尾上
$$
\frac{da_{t_1}}{dz}
=\frac{t_1}{p_2}
=-\frac{\mathfrak r}{4}
+\frac{1+(h_s/h)^2}{4kh}.
\tag{44}
$$
第二项相对于 $\epsilon_R$ 为 $O(M^{-3})+o_\delta(1)$，
而第一项由真实水平长尾估计保持(37)。
结合低尾的(28)，得到
$$
\boxed{
w(z)=-\ell/8+\mathfrak b(z_\infty-z)/4
+o^1_{\mathcal P}(1).
}
\tag{45}
$$
此前共同高尾的 $a_{t_1}=O((1+\log R)^2/R)$，
除以 $\epsilon_R$ 后为 $o(1)$；未把这个已发生的原成本删掉。

整条新词在足够的积分精度下可以写成
$$
a=zY+\epsilon_R wZ+o^1_{\mathcal P}(\epsilon_R).
\tag{46}
$$
出程的领先 $w=0$；低尾在领先层保持 $z=z_\infty$，
把 $w$ 从0改为 $-\ell/8$；回程使用(45)。
低尾的真实 $\Delta z=O(M/R^2)$ 仍保留，但在这一阶比 $\epsilon_R$
低一个 $R$ 次数。最终 $z$ **准确**为0。

(46)还具有沿分段路径的一阶总变差控制，而不只是逐点控制。
理由是：第一高尾的 $Y$ 总变差由 R550 的
$\int|k|\,d\tau\le C+C\log R/R$ 控制，非 $Y$ 部分总变差为
$O((1+\log R)^2/R)$；低尾由(26)给该界；最后高尾由(41)(42)
在一个有限慢时间区间给该界；全部有限过渡的缩放增量及变差为
$O(C_R\delta)$。所以对完整有序积分可将余项合法地估为
$o^1_{\mathcal P}(\epsilon_R)$。

## 7. $P_1$ 的新首项：两个次序都必须保留

沿(46)，原第三历史满足
$$
db=-da\circ a+\text{已控制的完整余项}.
$$
一阶横向部分具体为
$$
db^{[1]}=-w\,Y\circ Z\,dz-z\,Z\circ Y\,dw.
\tag{47}
$$
低尾入值的 $+\ell z_\infty Z\circ Y/8$ 正是(47)在
$dw=-d\theta/8$ 时的实际累积。不能用 $-(a\circ a)/2$
代替它，后者会丢掉本稿需要的方向。

由(5)(6)(46)，
$$
d\Xi_2
=\mathcal B_2(Y,Y)z\,dz
+\epsilon_R\{B_{12}w\,dz+B_{21}z\,dw\}
+o^1_{\mathcal P}(\epsilon_R)
\tag{48}
$$
以积分及总变差意义成立。完整 $z$ 起末均为0，所以分部积分给
$$
\begin{aligned}
\oint\Xi_2\,dz
&=-\oint z\,d\Xi_2\\
&=\epsilon_R(2B_{21}-B_{12})\oint zw\,dz
+o^1_{\mathcal P}(\epsilon_R).
\end{aligned}
\tag{49}
$$
这里 $\oint z^2dw=-2\oint zw\,dz$ 的边项因 $z=0$ 两端准确为零；
不要求第三历史自身返回。

出程的领先 $w=0$，低尾没有领先 $dz$，而回程从 $z_\infty$ 到0。
因此(45)给
$$
\boxed{
\oint zw\,dz
=\frac{\ell z_\infty^2}{16}
-\frac{\mathfrak b z_\infty^3}{24}
+o^1_{\mathcal P}(1).
}
\tag{50}
$$

### 7.1 从原稳定约束恢复真实 $p_1$

将 $\Psi_\Gamma(h,d)=0$ 除以 $h$，准确为
$$
\Gamma_1u+\frac{\Gamma_2}{2}
+\frac{\Gamma_0}{2}(u^2+h^{-2})=0.
\tag{51}
$$
真实法向误差由(16)保留。使用
$\Gamma_2=\lambda+\Xi_2/R$、
$\Gamma_1=2c+\Xi_1/R$ 及
$\delta\,d\mathsf m_{p_2}=dz/\sqrt R$，原(3)给
$$
\delta P_1
=-\frac1{2cR^{3/2}}\oint\Xi_2\,dz
+o^1_{\mathcal P}(M/R^{5/2}).
\tag{52}
$$
误差中的三类原项没有被省略：

1. 同一个常数 $\lambda$ 的领先积分因总 $z$ 起末为0准确相消；
   $\Gamma_1$ 的真实变化给 $O((1+\log R)^4/R^{5/2})$，
   除以目标尺度后由 $M\gg(1+\log R)^4$ 控制；
2. $\Gamma_0(u^2+h^{-2})$ 在两个高尾严格低阶，
   在低尾以其真实 $\Delta z=O(M/R^2)$ 相乘，也严格低阶；
3. 原快入、有限高度过渡和正常反馈误差，统一在最后选小 $\delta$
   时进入上述余项。非恒高度段使用的是(16)的 $O(\delta)$ 项。

所以，在**实际** $P_2=0$ 的停止时刻，
$$
\boxed{
F_{1,R,\delta}(\ell,\xi)
:=\frac{\delta R^{5/2}}M P_1
\longrightarrow
-\frac{D_*}{2c}
\left(\frac{\ell z_\infty^2}{16}
-\frac{\mathfrak b z_\infty^3}{24}\right)
}
\tag{53}
$$
于 $C^1(\mathcal P)$。真实 $P_1$ 的号和零来自这一个原端点映射，
不由两段形式矩质量配平来替代。

## 8. $P_0$ 的原逆高度项

由(3)，
$$
\delta P_0=\frac1{\sqrt R}\int(u^2+h^{-2})\,dz.
\tag{54}
$$
第一高尾与最后高尾的领先
$u=-A_Yz^2/R$ 使 $u^2$ 项相消。横向历史改变 $u$ 的大小为
$O(M/R^2)$，故这部分对 $\delta R^{5/2}P_0$ 的误差为
$O(M/R)=o(1)$，并保 $C^1$ 估计。

原 $h^{-2}$ 项则没有相消：

- 第一高尾在真实 $h=R+O(C_R\delta)$，
  给 $\delta P_0=z_\infty/R^{5/2}+o(R^{-5/2})$；
- 最后高尾的 $H_f^2\asymp MR^2$，
  其负贡献在这个尺度上只有 $O(M^{-1})$；
- 低尾的真实负贡献正是(30)，没有将它当作自由负原子；
- 原快入及有限过渡的全部贡献仍在最后选择的小量中。

于是，在同一个实际 $P_2=0$ 停止时刻，
$$
\boxed{
F_{0,R,\delta}(\ell,\xi)
:=\delta R^{5/2}P_0
\longrightarrow z_\infty-\frac{g_0\ell}{6c\xi}
}
\tag{55}
$$
于 $C^1(\mathcal P)$。
这也说明低尾为何必须同时保其高度与第三历史：
只取一个能抵消(55)的形式质量，不会自动支付(53)。

## 9. 真实两参数 IFT 与净 $t_1$ 符号

(53)(55)的极限映射有一个严格正的共同零
$$
\boxed{
\ell_0=\frac{2\mathfrak b z_\infty}{3},\qquad
\xi_0=\frac{g_0\mathfrak b}{9c}.
}
\tag{56}
$$
在该点，其 Jacobian 的第一行为
$$
\partial_\ell F_1=-\frac{D_*z_\infty^2}{32c}>0,\qquad
\partial_\xi F_1=0,
$$
第二行为
$$
\partial_\ell F_0=-\frac{g_0}{6c\xi_0},\qquad
\partial_\xi F_0=\frac{g_0\ell_0}{6c\xi_0^2}>0.
\tag{57}
$$
所以真实二维 Jacobian 可逆。

现先固定一个以(56)为内点的小紧参数盒 $\mathcal P$。
由(53)(55)的 $C^1$ 收敛，充分大的有限 $R$、再统一小的有限 $\delta$
使真实端点映射有近于(56)的共同零
$$
(\ell_{R,\delta},\xi_{R,\delta})\to(\ell_0,\xi_0).
$$
这是有限维 IFT／稳定简单零，不是仅由两个主项的零宣称成功。
每个参数值的最后高尾都已按(42)准确停在总 $P_2=0$；故这个共同零真实地满足(1)的三个等式。

### 9.1 全部 $t_1$ 成本与严格正余量

低尾的负首项是(30)。最后高尾由(3)(37)(42)给
$$
\delta T_1^{\rm high}
=\frac{\mathfrak b Mz_\infty}{4R^{3/2}}
+o^1_{\mathcal P}(M/R^{3/2}).
\tag{58}
$$
两个负项都保留：其真实长度满足
$\delta T_{\rm high}=O((M^2R^{3/2})^{-1})$，
故 $-1/8$ 相对于(58)低 $M^{-3}$；原速度平方项用(16)
及最后选择的小 $\delta$ 控制。

原对数等待的完整成本为
$O((1+\log R)/(\delta R^{3/2}))$，在本稿尺度上为 $o(1)$；
原 R544 快入及此前高尾账仍完整计入。
所有有限高度过渡的真实速度平方和其它矩成本至多 $C_R$，
最后使 $\delta C_R=o(M/R^{3/2})$。

因此整个同一实际词满足
$$
\boxed{
\frac{\delta R^{3/2}}M T_1
\longrightarrow
\frac{\mathfrak b z_\infty}{4}-\frac{\ell}{8}.
}
\tag{59}
$$
也可直接从原准确坐标 $a_{t_1}=\sqrt R\,\delta T_1$
及(45)在 $z=0$ 的值读出同一身份；这两种读法包含相同的原成本。
在实际三 $p$ 零处，由(56)，
$$
\boxed{
\frac{\delta R^{3/2}}M T_1
\longrightarrow \frac{\mathfrak b z_\infty}{6}>0.
}
\tag{60}
$$
于是 $T_1>0$ 与三个准确零在同一个参数值、同一真实词上同时成立。


## 10. 同一全系统的 $C^1$ 支付、原锚与范围

### 10.1 为什么没有长期延拓或参数微分的循环

本稿用的是 R544 的同一个两变量耗散法向系统，不是逐段重新挑选一个近似解。其居中法向量满足
$$
X_\tau=\mathcal A_n X+O(C_R\delta),\qquad
\mathcal E_\tau\le-c_*\mathcal E+C_R\delta^2.
\tag{61}
$$
在本文联合盒上，$\mathcal A_n$ 的刚度、阻尼、反馈质量有共同严格余量；
$a,b$ 有界，$\bar A=O(R^{-1/2})$，
$\Gamma_1=2c+O(R^{-1})$，
$\Gamma_0,\Gamma_2=O(R^{-1})$。
最后高尾接近 $z=0$ 时不再需要 $\Gamma_0>0$；
判别式和刚度仍严格正，$k$ 的正下界来自(37)(40)。

固定 $R$ 和紧参数盒后，对居中的(61)作参数微分。
稳定基解的指数衰减保留，参数强迫由
$O(C_R\delta)(1+|\partial_{\ell,\xi}(a,b)|)$ 控制。
在低尾的 $\theta$ 与高尾的 $\sigma$ 坐标中，完整慢状态变分方程
分别由(26)(41)给出：前者增量 $O(M/R)$，后者在有限区间内有界。
其归一化系数及一阶参数导数有同一界。
因此先在慢时间上作有限区间 Gronwall，再用稳定法向卷积，就得到
(16)(28)(40)(45)的参数导数界。不能反过来对原 $O(\delta^{-1})$
时长使用一个未缩放的指数 Gronwall。

共同前缀不依赖 $\ell,\xi$，其对数时间不会新增参数微分增长。
两条有限高度过渡的参数变化均在固定 $R$ 的有限时间内处理；
(35)的严格正导数给 $H_f$ 的真实参数导数，
(36)给它的归一化界。最后停止时间由(42)的严格导数支付。

在任一恒参考长尾，准确采用
$$
\mathcal J(h,\Gamma)
=-2\int_{\bar h}^{h}\frac{q_\Gamma(r)}{r^3}\,dr
$$
来控制水平量。原式直接给
$$
j(s)-j(s_0)
=[\mathcal J]_{s_0}^{s}
-\int_{s_0}^{s}\mathcal J_\Gamma\Gamma_s\,ds
-2\int_{s_0}^{s}
\frac{(d-q_\Gamma)h_s}{h^3}\,ds .
\tag{62}
$$
$h-\bar h=O(C_R\delta)$、$\mathcal J_\Gamma=O(C_R\delta)$，
而两个慢区间的 $\Gamma$ 总变差受(26)(41)控制；
最后积分使用恒参考处的 $d-q_\Gamma=O(C_R\delta^2)$。
所以 $j$ 的误差及其一阶参数导数均为 $O(C_R\delta)$，
没有按逐点小导数乘原长时间作错误估计。

这些估计先在一个固定放大的联合盒成立。
(26)(41)、法向耗散、水平式(62)及(42)分别改进该盒的历史、
几何、水平和停止时间边界，因而按最大存在区间论证闭合。
不需要先假定已经延拓到了所要的长尾末端。

### 10.2 全部选择次序

完整次序如下：

1. 固定同一个 R521 正交母库、真实 profile 右锚；
   一次选足够大的有限 $\omega_c$，同时支付
   $Q_0,Q_2,B_{21},D_*$ 的严格号；
2. 固定 R544 的 $H,H_0,c,L_h$、真零历史快入控制、
   反馈增益与 R550 的共同饱和前缀；
3. 固定 $\mathfrak b>0$，按(56)选择一个严格位于正象限的紧参数盒；
4. 取充分大的有限 $R$，令 $M=(1+\log R)^6$、
   $\lambda=L_h^2/R^2$，先支付所有纯 $R$ 的 $C^1$ 小量；
5. 在该盒上固定有限参考下降和上升的光滑规则、时长及所需导数界，
   高目标按真实低入值的(35)选取；
6. 最后统一取一个有限正 $\zeta$，令 $\delta=\lambda^2\zeta$。
   所有归一化矩误差、法向误差、真实参考目标误差、
   有限过渡成本及其一阶参数导数共同小于 IFT 所需余量；
7. 在这个已经固定的 $\chi$ 上求实际两参数零
   $(\ell_{R,\delta},\xi_{R,\delta})$，并用原准确坐标停止在 $P_2=0$。

第7步只选择几何控制参数，不再修改 $\nu$ 或 profiles。
它也不是把这些控制参数宣称成最终固定度量上的等距形变参数。

### 10.3 坐标识别及仍欠的原目标

本稿的三个 $p$ 是固定 $y=x+\omega_c$ 坐标中的原矩。
与未平移坐标的关系准确为
$$
P_2^{y}=P_2^{x},\qquad
P_1^{y}=P_1^{x}-2\omega_cP_2^{x},
$$
$$
P_0^{y}=P_0^{x}-\omega_cP_1^{x}+\omega_c^2P_2^{x},
\qquad
T_1^{y}=T_1^{x}+\frac{\omega_c}{2}P_2^{x}.
\tag{63}
$$
所以(1)同时给原未平移的三个 $p$ 精确为0，
且原 $T_1$ 仍严格正。这不是坐标变换制造的矩消失。

原第二、第三字段在全部段上由同一
$A_s=\Phi_{M_{\rm raw}}$、
$T_s=-\Phi_{M_{\rm raw}}\circ A+C_s$ 恢复；
所有 incoming 常数、真左／右尾和第四累计都保留。
(47)正是其中不能省略的有序交叉项。
参数化几何、frame 和位置按原 ODE 恢复，每个最终对象都是真实、
有限、光滑的词。R521 的全部相位因子及同一反馈使原完整第四 ruling
始终为0，而非只在某一个相位为0。

**实际定理。** 在上述从起点一次选择的同一个母库与 $\chi$ 上，
存在由真实零历史开始的有限光滑几何词，准确满足
$$
P_0=P_1=P_2=0,\qquad T_1>0,
$$
并保完整全相位第四 ruling、真实合法窗口及全部原历史。

仍有其余五个独立二阶矩待处理，其中 $T_1$ 只是已知正而非零。
末端不是已返回的周期 germ；frame／位置、第三／第四 period、
同十三规范与最终主问题均未因此完成。
本稿没有使用另一 33 母库的任何轨道、规范或正负成本收据。

### 原来源

- [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)：
  原八矩、真实静态 $-Z/8-\mathcal R/(8h^2)$、
  水平式和有序第三历史；
- [R221](R221-complete-fixed-circle-ruling-moment-map-and-joint-right-inverse.md)：
  完整速度线性三槽式，保真实尾及高高度系数界；
- [R437](R437-highest-rational-gauge-row-vanishes-on-the-complete-period-kernel.md)：
  完整 $Y$ profile 与原三次配对；
- [R521](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md)：
  同一正交母库、全相位、原非退化加速度控制；
- [R544](R544-one-fixed-gram-and-a-real-path-with-negative-p1-and-positive-t1.md)：
  唯一 $\chi$、真零历史入点、全慢状态与真实吸引反馈；
- [R548](R548-real-history-turn-and-negative-p2-access-with-one-fixed-gram.md)：
  完整 $Q_j$ 符号、原高尾及有限下降；
- [R549](R549-three-p-moment-balance-and-real-horizontal-repair-obstructions.md)：
  三个 $p$ 的联合矩结构与真实水平门；
- [R550](R550-positive-horizontal-branch-and-exact-p2-zero-with-one-fixed-gauge.md)：
  原 $t_1$ 次阶项、实际饱和前缀、完整对数成本与准确 $p_2$ 停止接口。

本稿没有执行任何新科学计算。
