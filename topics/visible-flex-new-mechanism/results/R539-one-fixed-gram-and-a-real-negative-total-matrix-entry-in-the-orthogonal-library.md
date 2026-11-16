# R539：同一正交母库内从起点固定新 Gram 的真实净负矩累计

日期：2026-11-16。**完整原式、有限参数与 ODE 渐近的纸面证明；没有执行数值、求积、符号、profile、秩或开发检查。**

本稿沿 R521 的同一正交母库，构造一条真实完整 ruling 路径，使包含全部入段的原 $p_1^{\omega_c}$ 累计严格为负。它不是把 R534 的局部负密度乘以一个未经证明可走的长时间，也不在路径中途更换第三规范。

本次从起点重新选择一个**有限的第三 Gram 分量 $\nu_2$**，并相应选择 $\nu_0$。全部有限参数冻结后，才选择 R534 的小参数 $\delta$。最终整条路径只使用一个 $\chi^\delta$，母 profiles、所有实际 copy、物理窗口、原右锚和第二规范 $w=0$ 均不改变。

证明分为两个真实步骤。先用一段高度只增加 $\varepsilon$、时长为 $\varepsilon^2$ 的光滑路径，产生一个严格负的缩放水平 holonomy。再用同一个从起点选择的 $\nu_2$，把这段末端的完整 canonical 缺额准确放到常高度段的负密度中心。末端虽有较大的第三历史，其后常高度展开的一次、二次系数仍一致有界。因此一个先固定的有限常高度时长足以压过前段的全部正累计上界。

结论只支付净 $p_1^{\omega_c}<0$。同一真实路径的 $t_1^{\omega_c}$ 仍严格负，全部八矩尚未回零；scalar 末 germ、frame、位置、第三及第四 period 也不因此闭合。

## 1. 原母库、完整 ruling 与记号

固定 R521 的同一个有限正交库及实际物理区间，选
$$
S_c=(H,0,\omega_c),\qquad y=x+\omega_c,
\qquad H\min_I y>1
\tag{1}
$$
并保严格余量。令
$$
c:=C_k(H,0)>0,\qquad
B_*:=B(H,0)=-C_h(S_c)>0.
\tag{2}
$$
这里 $B(h,d)$、$C_k(h,d)$ 是 R535/R537 的完整原加速度系数，并有
$$
C_h+2\eta C_k=-B(h,d),\qquad
d=h\eta-k,\quad \eta=\omega-\omega_c.
\tag{3}
$$
母库、窗口与这些系数在本稿全部参数选择中固定。

在固定坐标 $y$ 中，同一个合法第三 Gram 的作用为
$$
-2\mathbf w_y(S)\cdot\nu
=-\frac{\nu_0(1+d^2)}{2h}-d\nu_1-\frac{h\nu_2}{2}.
\tag{4}
$$
原完整第四 ruling 是
$$
\boxed{
C_hh_{ss}+C_kk_{ss}
+\mathcal F(S,h_s,k_s,A,T)
-\frac{\nu_0(1+d^2)}{2h}-d\nu_1-\frac{h\nu_2}{2}=0.
}
\tag{5}
$$
$\mathcal F$ 保留
$$
R_0+R_2+L_{\rm vel}(AD)-E(AD,AD)
-4E\{\phi,T(\phi;D)\}.
\tag{6}
$$
后文在 $\theta=\pi/2$ 读取标量系数，因此可取
$\phi=g,D=\Delta$；原 R521 已付全相位恰为该标量乘 $\sin^2\theta$。这不把任何有序第三项变为局部近似。

记
$$
F_c=\mathcal F(S_c,0,0,0,0).
$$

## 2. 允许的新规范必须从起点选择

给任意先固定的有限 $a_*>0$ 和有限 $\nu_2$，把 R534 的 Gram 改为
$$
\boxed{
\nu_1^\delta=\frac{2c}{\delta^2},\qquad
\nu_0^\delta=
2H\{\mathcal F(S_c,0,\delta^2,0,0)-B_*a_*\}
-H^2\nu_2.
}
\tag{7}
$$
R521/R530 的同一个紧支撑 Gram 右逆给一条合法、平滑、周期且保 seed 的
$\chi^\delta$，满足
$$
\mathbf I_y(\phi_\theta,\chi_\theta^\delta)
=\sin^2\theta\,(\nu_0^\delta,\nu_1^\delta,\nu_2).
\tag{8}
$$
对每个最终固定的正 $\delta$，所有系数有限。整个真实词从开始到结束使用这一条 $\chi^\delta$，不是先使用 $\nu_2=0$ 的旧路径再在中间改变它。

原中心初值仍为
$$
h=H,\quad k=\eta=h_s=0,\quad k_s=\delta^2,
\quad A=T=0.
\tag{9}
$$
由(4)(7)，中心的两个完整 ruling 方程准确给
$$
h_{ss}(0)=a_*,\qquad k_{ss}(0)=0.
\tag{10}
$$
新增的 $\nu_2$ 项在此被 $\nu_0^\delta$ 的对应项准确补偿。

### 2.1 R534 的真实入段仍成立

与同一 $a_*$、$\nu_2=0$ 的原 Gram 相比，新增的完整 ruling 项恰为
$$
\frac{\nu_2}{2}
\left\{\frac{H^2(1+d^2)}h-h\right\}.
\tag{11}
$$
在 R534 的真双边缩放中，$h=H+O(\delta^2)$、$d=O(\delta^3)$。对已经固定的有限 $\nu_2$，(11)是 $O(\delta^2)$；它对正反时两半为偶，因而两条方程的差没有新增主项。原提出 $\nu_1^\delta$ 后的正规有限 ODE 极限、首零与负极小构造不变。其误差常数允许依赖已固定的 $a_*,\nu_2$。

因此仍得到 R534 的真实负密度点、R535 的长度 $\delta^4$ 平滑刹停，以及一个开放的固定 $d$ 解段。其尺度保留为
$$
d_0=O(\delta^5),\quad d_s=0,\quad
j_0=O(\delta^5),\quad A_0=O(\delta),\quad T_0=O(\delta^2).
\tag{12}
$$
原正前缀的累计是
$$
m_{p_1}^{\rm prefix}
=\frac{\pi}{4}\delta^7+O(\delta^9)>0.
\tag{13}
$$
这里所有 $O$ 常数可以依赖本稿随后先冻结的有限参数；没有把该式当作 $\varepsilon$ 与 $\delta$ 同时任意趋零的统一估计。

### 2.2 R535—R538 的完整扩展

在固定 $d$ 支中，新项只是高度方程的
$-h\nu_2/2$。原大参数 $\nu_1^\delta$ 仍只通过
$d\nu_1^\delta$ 出现，故把有限 $\nu_2$ 加入正规参数表即可；完整
$M_{\rm raw},\mathcal C_s$ 不依赖固定齐次第三规范。

在 R537 的振子方程中，新项是
$$
-\frac{h\nu_2}{4C_k(h,d)}
$$
这一光滑强迫；正快频率仍准确为
$c/(\delta^2C_k)$。原无快加速度的慢第三重写、顺次历史界及能量证明均不改变。R538 在预给有限 $C^4$ 高度界下的强准备和四阶极限也不改变。

因此，对任何按其开放入段拼接条件预给的有限高度路径 $h$，仍有
$$
m_{p_1}^{\rm total}
=\delta^4\mathcal P[h]+o(\delta^4),
\tag{14}
$$
其中
$$
D_h=
\frac{
\mathcal F(S_h,h',0,A_h,T_h)
-B(h,0)h''-\nu_0^0/(2h)-h\nu_2/2
}{2c},
\tag{15}
$$
$$
S_h=(h,0,\omega_c),\qquad
\nu_0^0=2H(F_c-B_*a_*)-H^2\nu_2,
$$
$$
J_h(s)=-2\int_0^s D_h(t)\frac{h'(t)}{h(t)^3}\,dt,
\qquad
\mathcal P[h]=\int\{2D_h^2-h^2J_hD_h\}\,ds.
\tag{16}
$$
$A_h,T_h$ 是原零历史、$k=0$ canonical 字段的完整累计，不是把实际
$k^\delta$ 提前设成零。最终真实路径由原完整反馈求出；(15)(16)只是它已证明的四阶系数。

## 3. 本次有限参数的选择及高度段目标

引入一个新的有限参数 $\varepsilon>0$。最终将先固定它，再取 $\delta$。设置
$$
\sigma=\varepsilon^2,\qquad
a_*=\frac{\varepsilon}{\sigma^2}=\varepsilon^{-3},
\qquad
\nu_2=\frac{\vartheta}{\sigma^2}
=\vartheta\varepsilon^{-4},
\tag{17}
$$
其中 $\vartheta$ 在 $B_*>0$ 的一个固定小邻域内。所有这些数在最终选
$\delta$ 之前已经有限冻结。

在 $0\le s\le\sigma$，规定极限高度
$$
h(s)=H+\varepsilon f(s/\sigma).
\tag{18}
$$
将构造一个对 $(\varepsilon,\vartheta)$ 光滑的 $f$，满足
$$
f(0)=f'(0)=0,\quad f''(0)=1,\quad
f(1)=1,\quad f'=0\ \text{于末端开放区间},
\tag{19}
$$
且 $f'\ge0$、有限阶 $\tau$ 导数统一有界，其中 $\tau=s/\sigma$。
初始开放区间上，(18)必须等于(7)在 $\delta=0$ 的真实固定 $d=0$ 高度 germ；这一兼容性将在下一节构造，而不是额外假设某条初始桥。

本段高度仅在 $[H,H+\varepsilon]$，所以(1)的合法余量一直保留。其真实时间导数可以大，例如
$h_s=O(\varepsilon^{-1})$、$h_{ssss}=O(\varepsilon^{-7})$。这些是本次有限路径的明确成本，不称为统一小导数。

## 4. 初始真 germ 与完整历史的正规缩放

先在 $k=0,\omega=\omega_c$ 的 canonical 路径上书写原密度。原 R73/R77 给有限完整算子
$$
A_s=\mathcal M_0(h)+\gamma^2\mathcal M_2(h),
\qquad \gamma=h_s,
\tag{20}
$$
$$
T=\widetilde T+\gamma^2P_{20}(h),
$$
$$
\widetilde T_s
=-\{\mathcal M_0+\gamma^2\mathcal M_2\}\circ A
+\gamma\mathcal C_{10}(h)+\gamma^3\mathcal C_{30}(h).
\tag{21}
$$
这是 R537 完整第三变换在 $k_s=0$ 时的准确限制。原速度面积项为0，两个端点势仍由 $\gamma^2P_{20}$ 保存，未将任何项投到 $W$ 后删除。

写
$$
\mathcal U=\varepsilon\widetilde T.
$$
代入(17)(18)，(20)(21)准确成为
$$
\boxed{
A_\tau=\varepsilon^2\mathcal M_0(h)
+(f')^2\mathcal M_2(h),
}
\tag{22}
$$
$$
\boxed{
\mathcal U_\tau
=-\varepsilon^3\mathcal M_0\circ A
-\varepsilon(f')^2\mathcal M_2\circ A
+\varepsilon^2 f'\mathcal C_{10}
+(f')^3\mathcal C_{30}.
}
\tag{23}
$$
初值均为0。这是一个没有负幂参数的真实重写。

在同一 scalar 上，把(6)中原 $T$ 的速度势保留后，可写
$$
\mathcal F
=R_0(h)+\gamma^2V_2(h)+\gamma L_1(h)[A]
-E_h(A\Delta,A\Delta)
-4E_h\{g,\widetilde T(g;\Delta)\},
\tag{24}
$$
其中 $V_2$ 已准确含原 $R_2$ 与
$-4E_h\{g,P_{20}(g;\Delta)\}$。因此
$$
\begin{aligned}
\varepsilon^3\mathcal F={}&
\varepsilon^3R_0+\varepsilon(f')^2V_2
+\varepsilon^2 f'L_1[A]\\
&-\varepsilon^3E_h(A\Delta,A\Delta)
-4\varepsilon^2E_h\{g,\mathcal U(g;\Delta)\}.
\end{aligned}
\tag{25}
$$
所有系数都是原有限 profile 算子的实际配对。

初始参考 germ 满足 $k=d=0$ 的完整 ruling：
$$
B(h,0)h_{ss}
=\mathcal F-\nu_0^0/(2h)-h\nu_2/2 .
$$
用(17)(18)(25)除去公共尺度后，得到一个在
$\varepsilon=0$ 仍光滑的有限系统，其高度行是
$$
\begin{aligned}
B(h,0)f''={}&
\frac{HB_*}{h}
-\frac{\vartheta f(2H+\varepsilon f)}{2h}\\
&+\varepsilon(f')^2V_2
+\varepsilon^2\{f'L_1[A]-4E_h(g,\mathcal U(g;\Delta))\}\\
&+\varepsilon^3\{R_0-HF_c/h-E_h(A\Delta,A\Delta)\}.
\end{aligned}
\tag{26}
$$
$\varepsilon=0$ 的精确极限为
$$
f''=1-\frac{\vartheta}{B_*}f,\qquad f(0)=f'(0)=0.
\tag{27}
$$
(22)(23)(26)的系数光滑，$B(h,0)>0$。所以存在一个与小
$\varepsilon$ 和 $\vartheta$ 所在紧邻域共同适用的短 $\tau$ 区间，
上有真实参考解，其 $f'>0$ 于正的短区间，所有有限阶导数及参数导数有统一界。
这里的均匀性来自正规 ODE，而不是忽略可能很大的原 $T$。

选固定小 $\tau_0>0$，在 $[0,2\tau_0]$ 使用该参考解。取一个固定非负 cutoff
$\zeta$，初段为1、在 $2\tau_0$ 前平坦归零；再取一个支撑于
$(3\tau_0,3/4)$ 的非负光滑函数 $\beta$，$\int_0^1\beta=1$。定义
$$
f'=\zeta f_{\rm ref}'
+\left(1-\int_0^1\zeta f_{\rm ref}'\,d\tau\right)\beta.
\tag{28}
$$
先将 $\tau_0$ 取小，可使括号统一大于 $1/2$。积分并令 $f(0)=0$，得到(19)及
$f'\ge0$；初段逐 germ 为真参考解，末段高度准确恒为 $H+\varepsilon$。
整个 $f$ 对参数光滑，所需有限阶界一致。

在参考段外，(18)是实际允许的高度输入；(22)(23)仍是其 canonical 历史的准确方程，不要求(26)继续成立。最后应用 R537 时，将其实际 $\delta$ 拼接 cutoff 的支撑严格放在这里的精确参考 germ 内部，例如取在 $[0,\sigma\tau_0/2]$ 内；因此两次 cutoff 的作用区间不会混淆。

## 5. 前段内部与末端的历史界必须分开

由(22)(23)、固定 $\tau$ 区间及 $f$ 的统一界，直接先后得到
$$
A=O(1),\qquad \mathcal U=O(1),\qquad
\widetilde T=O(\varepsilon^{-1})
\tag{29}
$$
及相同的有限参数导数界。原第三历史在内部为
$$
\boxed{
T=\varepsilon^{-2}(f')^2P_{20}(h)
+\varepsilon^{-1}\mathcal U
=O(\varepsilon^{-2}).
}
\tag{30}
$$
因此内部不能把 $T$ 只记成 $O(\varepsilon^{-1})$。

用(24)，整个前段有
$$
\sigma^2\mathcal F=O(\varepsilon^2).
\tag{31}
$$
但末端 $f'=0$ 于开放区间，故速度势准确为0，且 $R_2,L_{\rm vel}$ 也准确为0。于是
$$
\boxed{
A_e=O(1),\qquad
T_e=\widetilde T_e=O(\varepsilon^{-1}),\qquad
\sigma^2\mathcal F_e=O(\varepsilon^3).
}
\tag{32}
$$
这些界均保完整有序 $-\mathcal M\circ A$，也保全部第三原算子。
(29)–(32)对 $\vartheta$ 的一阶导数同样成立，供下面真实 IFT 使用。

## 6. 真实水平 holonomy 的统一首项

对(15)(16)定义
$$
\widehat D=\sigma^2D_h,\qquad
\widehat J=\sigma^2J_h.
$$
由(17)(18)(31)，在整个前段上
$$
\boxed{
\widehat D
=\frac{\varepsilon}{2c}
\{B_*(1-f'')-\vartheta f\}+O(\varepsilon^2).
}
\tag{33}
$$
误差一致保完整 $\mathcal F$ 和所有参数导数，不把其低项设置为零。

现在只考虑
$$
\vartheta=B_*+\varepsilon z
\tag{34}
$$
且 $z$ 在一个固定有界区间。由(19)，准确有
$$
\int_0^1(1-f-f'')f'\,d\tau
=\left[f-\frac{f^2}{2}-\frac{(f')^2}{2}\right]_0^1
=\frac12 .
\tag{35}
$$
这是完整端条件给出的恒等式，与过渡段的具体形状无关。

将(33)代入(16)，有
$$
\widehat J_e
=-2\varepsilon\int_0^1
\widehat D\,\frac{f'}{(H+\varepsilon f)^3}\,d\tau,
$$
从而
$$
\boxed{
\widehat J_e
=-\frac{B_*}{2cH^3}\varepsilon^2+O(\varepsilon^3).
}
\tag{36}
$$
该式在有界 $z$ 集合上以 $C^1$ 意义成立。由于 $\sigma^2=\varepsilon^4$，
$$
J_e=-\frac{B_*}{2cH^3}\varepsilon^{-2}
+O(\varepsilon^{-1})<0
\tag{37}
$$
于充分小正 $\varepsilon$。这是真实缺额 $D_h$ 与高度输入联动产生的首项，不是另给 $J$ 一个自由值。

## 7. 一个有限 Gram 参数准确支付末端中心

令 $h_1=H+\varepsilon$。由末端更强界(32)，
$$
\widehat D_e
=\frac1{2c}\left\{
\frac{HB_*\varepsilon}{h_1}
+\frac{\vartheta}{2}\left(\frac{H^2}{h_1}-h_1\right)
\right\}
+O(\varepsilon^3).
\tag{38}
$$
这里 $-\sigma^2 HF_c/h_1=O(\varepsilon^4)$ 也已经包含在余项中。

定义完整的末端方程
$$
\Psi(\varepsilon,z)=
\widehat D_e-\frac{h_1^2\widehat J_e}{4},
\qquad \vartheta=B_*+\varepsilon z.
\tag{39}
$$
代入(36)(38)，得到
$$
\boxed{
\varepsilon^{-2}\Psi(\varepsilon,z)
=-\frac{z}{2c}-\frac{B_*}{8cH}+O(\varepsilon)
}
\tag{40}
$$
并保 $C^1$ 参数余项。前面已经给完整参考 germ、(28)、全部 $A,T$ 对参数的光滑依赖；故(40)不是只对 formal principal 的 IFT。

在 $\varepsilon=0$，(40)对 $z$ 的导数为 $-1/(2c)\ne0$。因此存在真实小参数支
$$
z(\varepsilon)=-\frac{B_*}{4H}+O(\varepsilon),
$$
$$
\boxed{
\vartheta(\varepsilon)
=B_*-\frac{B_*}{4H}\varepsilon+O(\varepsilon^2)>0
}
\tag{41}
$$
使完整方程(39)准确为0。换回未缩放量：
$$
\boxed{D_e=\frac{h_1^2J_e}{4}.}
\tag{42}
$$
对每个最终固定 $\varepsilon$，(41)只选定一次 $\nu_2$ 和相应 $\nu_0^\delta$。
没有在末端重新设置 $A_e,T_e$ 或改变同一个 $\chi^\delta$。

## 8. 常高度后段的完整第三历史及时间二次式

在前段之后，规定 $h\equiv h_1$，保持一个随后先固定的有限时长 $L$。
这一段仍只是 R538 的预给高度输入；真正的 ruling 路径由完整快慢系统求出，实际
$k^\delta,\eta^\delta$ 不会在这里被假设为零。

为计算其四阶系数(15)，考虑同一 canonical 极限历史。
原 R73/R56 在常
$$
S_1=(h_1,0,\omega_c)
$$
上给
$$
A_c=-\frac{1}{8h_1^2}R_y-\frac18T_y,\qquad
\mathcal C_s=0.
\tag{43}
$$
第二个等式是原完整三线性密度恒等式：不是第三 local 字段为零，也不是一个 $W$ 商的判断。其原场理由是常 $k=0$ scalar 下，$Y$ 的分子在 $T/B$ 平面，协变 $s$ 导在 $N$；原 second local 场在 $N$，其协变 $s$ 导在 $T/B$。R56 的配对分子 $P,\mathcal B,T_s$ 均为0，R73 的变化-profile 项在常态也为0。这个原式证明见 R520 §2，几何恒等式本身不依赖该文另选的母库。

从本稿真实 canonical 入值 $(A_e,T_e)$ 出发，原有序演化准确积分为
$$
\boxed{
A(t)=A_e+tA_c,\qquad
T(t)=T_e-t\,A_c\circ A_e-\frac{t^2}{2}A_c\circ A_c,
\quad0\le t\le L.
}
\tag{44}
$$
次序 $A_c\circ A_e$ 由 $T_s=-A_s\circ A$ 给出，不能反过来。
这里不重锚，不删除 $T_e$。

常态速度为0，所以(6)中的 $R_2,L_{\rm vel}$ 都为0。令
$$
q_e=A_e\Delta,\qquad q_c=A_c\Delta,\qquad E=E_{S_1}.
$$
把(44)代入完整(15)，得到精确多项式
$$
\boxed{D_h(t)=D_e+b_1t+b_2t^2,}
\tag{45}
$$
其中
$$
2c\,b_1
=-2E(q_e,q_c)
+4E\{g,(A_c\circ A_e)(g;\Delta)\},
\tag{46}
$$
$$
2c\,b_2
=-E(q_c,q_c)
+2E\{g,(A_c\circ A_c)(g;\Delta)\}.
\tag{47}
$$
(47)就是原完整常态二次系数；本稿不需要其符号。

由 $A_e=O(1)$、$h_1$ 的固定紧域及原 profiles 固定，有
$$
|b_1|+|b_2|\le C
\tag{48}
$$
一致成立。大的 $T_e=O(\varepsilon^{-1})$ 和固定 Gram 都准确进入
$D_e$，不进入(46)(47)。这正是后段可取得统一负累计的原因。

## 9. 固定有限后段足以压过整个前段

常高度段上，(16)给 $J_h(t)\equiv J_e$。结合准确调节(42)，有
$$
\begin{aligned}
2D_h^2-h_1^2J_eD_h
&=2\left(D_h-\frac{h_1^2J_e}{4}\right)^2
-\frac{h_1^4J_e^2}{8}\\
&=2(b_1t+b_2t^2)^2-\frac{h_1^4J_e^2}{8}.
\end{aligned}
\tag{49}
$$
因此
$$
\boxed{
\mathcal P_{\rm tail}(L)
=-\frac{h_1^4J_e^2}{8}L+O_L(1).
}
\tag{50}
$$
由(37)，存在只依赖固定母库与 $H$ 的 $q_*>0$，例如取极限正系数的一半，使
$$
\frac{h_1^4J_e^2}{8}\ge q_*\varepsilon^{-4}
\tag{51}
$$
于充分小 $\varepsilon$。

另一方面，整个前段由(33)(36)有
$$
D_h=O(\varepsilon^{-3}),\qquad
J_h=O(\varepsilon^{-2}),\qquad \text{时长 } \sigma=\varepsilon^2.
$$
故存在一个统一有限 $C_{\rm in}$，保全部完整历史，满足
$$
\boxed{|\mathcal P_{\rm in}|\le C_{\rm in}\varepsilon^{-4}.}
\tag{52}
$$
这包括前段可能的正贡献，没有以端点密度替代累计。

先选择一个固定有限 $L$，使
$$
q_*L>2C_{\rm in}+1.
\tag{53}
$$
再选充分小但固定的正 $\varepsilon$。由于(48)，(50)中的 $O_L(1)$ 在这次固定
$L$ 后与 $\varepsilon$ 无关，所以(50)–(53)给
$$
\boxed{
\mathcal P[h_{\rm in}\ \text{接常高尾}]
\le -c_*\varepsilon^{-4}<0
}
\tag{54}
$$
对某个固定 $c_*>0$ 成立。这里只先固定一个有限后段；没有证明对一份已冻结的
$\delta$ 可走无界时长。

## 10. 回到同一实际 $K=0$ 路径

现在按顺序冻结：

1. R521 的唯一母库、原窗口、$H,\omega_c$；
2. 上述固定过渡函数及统一常数，有限 $L$；
3. 一个满足(54)的有限 $\varepsilon$，随后
   $\sigma,a_*,\vartheta(\varepsilon),\nu_2$；
4. 最后选充分小的正 $\delta$，用(7)(8)一次选定完整 $\chi^\delta$。

高度目标在初始开放区间正是本次新 Gram 的真实 $d=0$ 参考 germ。按 R537 的原 cutoff 方法，只在该开放起段用实际固定 $d_0^\delta$ 高度替换其极限，后面逐函数准确等于已经选好的 loader 和常高尾。对这次固定的有限数据，所有高度的 $C^4$ 界有限；它们可以依赖 $\varepsilon,L$，不会被当成对两小参数统一的界。

第2节已经证明本次有限 $\nu_2$ 不改变原完整反馈、强准备和四阶极限的适用性。
因此有同一母、同一 $w=0$、同一固定 $\chi^\delta$ 的真实全段解，满足
$$
\mathscr K(s,\theta)=0
$$
对所有真实 $s,\theta$ 成立；原二、三阶条件同样保持。完整 $A,T$、frame、位置与第四字段按原同锚方程恢复，所有新增成本均保留。

由(14)(54)，包括 R534/R535 全部正前缀的实际总累计为
$$
\boxed{
m_{p_1^{\omega_c}}^{\rm total}
=\delta^4\mathcal P[h]+o(\delta^4)<0
}
\tag{55}
$$
于充分小正 $\delta$。原正项(13)是 $O(\delta^7)$，已经被(14)纳入，而不是另要求它为零。

这支付的是净矩累计，严格强于仅在某时刻有 $M_{p_1}<0$。整个证明没有逐段选择不同规范，也没有把 signed 算子当成负时间实际路径。

### 10.1 同一固定规范下的准确单矩零点

这一补充只改变同一真实路径的停止时间，不改变母库、任何 Gram 分量或入历史。

令
$$
q_\varepsilon=1-f-f''.
$$
(35)准确给 $\int_0^1q_\varepsilon f'\,d\tau=1/2$。
由于 $f'$ 有统一有限 $L^2$ 上界，
$$
\int_0^1q_\varepsilon^2\,d\tau
\ge\frac1{4\int_0^1(f')^2\,d\tau}\ge c_0>0.
$$
由(33)(34)，完整前段四阶系数比(52)更具体：
$$
\mathcal P_{\rm in}
=\frac{B_*^2}{2c^2}\varepsilon^{-4}
\int_0^1q_\varepsilon^2\,d\tau+O(\varepsilon^{-3})>0.
$$
原 $J_hD_h$ 项对这一式的贡献仅为 $O(\varepsilon^{-3})$，并未删掉。

在已经固定的 $0\le t\le L$ 上，由(48)(49)(51)，充分小 $\varepsilon$ 时有
$$
2D_h(t)^2-h_1^2J_eD_h(t)
\le-\frac{q_*}{2}\varepsilon^{-4}<0.
$$
所以极限累计
$$
\mathcal P_{\rm in}+\int_0^\ell
\{2D_h^2-h_1^2J_eD_h\}\,dt
$$
对 $0\le\ell\le L$ 严格递减，从正值变为(54)的负值，恰有一个零点
$\ell_\varepsilon\in(0,L)$。

对这次已经冻结的 $\varepsilon,L,\chi^\delta$，R538 的一致强收敛不仅给累计极限，也给整个尾段上的密度极限
$$
\delta^{-4}M_{p_1}^\delta(t)
\longrightarrow 2D_h(t)^2-h_1^2J_eD_h(t).
$$
因此充分小的实际 $\delta>0$ 下，包含真实正前缀的累计在尾段开始时严格正，在 $\ell=L$ 时严格负，且对停止时间严格递减。存在唯一实际
$\ell_{\varepsilon,\delta}\in(0,L)$，满足
$$
m_{p_1^{\omega_c}}^{\rm total}(\ell_{\varepsilon,\delta})=0.
$$
它是真实完整 $K=0$ 解的一个停止时间，第三历史和其它场由同一条已经存在的解直接读取。对固定正 $\delta$，端点导数
$M_{p_1}^\delta(\ell_{\varepsilon,\delta})<0$ 给通常的局部光滑单端口图；没有另取一条规范或把端点历史重设为零。

若 $f_0=\lim_{\varepsilon\to0}f_{\varepsilon,\vartheta(\varepsilon)}$，
则两个已付首项还给
$$
\ell_\varepsilon\longrightarrow
16H^2\int_0^1(1-f_0-f_0'')^2\,d\tau>0.
$$
此式只说明所需停止时间有有限正极限；最后的实际 $\delta$ 仍在
$\varepsilon$ 和全部有限数据冻结以后选择。

这个准确零点只清原八矩中的 $p_1^{\omega_c}$。同一路径的总 $t_1^{\omega_c}$ 仍由(56)严格为负，故不授 $M=0$、frame/位置返回或 period。

## 11. 仍未闭合的矩及端口

本次实际解仍处于 R537 的近 $k=0$ 范围；对冻结的有限
$\varepsilon,L$，
$$
k^\delta,\eta^\delta=O(\delta^2)
$$
但其常数可大。原恒等式仍给
$$
8M_{t_1}
=2kh\eta-k^2-1-(h_s/h)^2.
$$
于是本次新段的总 $t_1$ 极限准确为
$$
\boxed{
-\frac18\left\{
L+\varepsilon^2+
\int_0^1\frac{(f'(\tau))^2}{(H+\varepsilon f(\tau))^2}\,d\tau
\right\}<0.
}
\tag{56}
$$
此前缩短的真实前缀对这一极限贡献为0。因此本稿仍不产生 $M=0$，也没有支付 R524 所要求的有限幅 $k$ 与 $\omega$ 变化。

其它矩、scalar 末值及末 jets、frame、位置、$T$、第四 period 和同一十三规范均是真实联动输出。R526 的闭合词需要真正的 $M=0$ 块；不能直接把本稿净负 $p_1$ 段代进去。

本稿改变的是原可达性中的一个确切门：在同一 R521 母库和一个从起点固定的合法规范下，已经能够让全部正入段之后的总 $p_1^{\omega_c}$ 严格为负。要同时配平其它矩，仍须在同一实际词和同一规范中继续构造。

### 原来源

- [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)：完整矩阵密度、有序第三累计及 $p_1=-kd$；
- [R77](R77-weight-three-local-operator-actual-finite-controllability.md)(2)、[R79](R79-closed-horizontal-C1-control-and-endpoint-potential.md)：完整速度势、速度一次与三次项；
- [R482](R482-pointwise-third-memory-elimination-and-constrained-prototype-ruling-system.md)：未消第三历史的原完整 ruling；
- [R520](R520-variable-mother-constant-ruling-and-same-gauge-nonconstant-local-departure.md) §2：原常 $k=0$ scalar 的完整 $\mathcal C_s=0$ 几何身份；本稿不借用其另一母库的控制收据；
- [R521](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md)：本稿唯一母库、完整两加速度行及固定 Gram 右逆；
- [R534](R534-real-zero-history-entry-into-negative-matrix-density-and-fixed-gauge-continuation.md)、[R535](R535-fixed-geometric-d-and-uniform-negative-matrix-increment-with-one-gauge.md)：真实 canonical 前缀、平滑切换及开放固定 $d$ 入段；
- [R537](R537-prescribed-finite-height-paths-with-one-gauge-and-complete-history-energy-bounds.md)、[R538](R538-complete-fourth-order-matrix-functional-for-prescribed-height-paths.md)：完整有限区间延续、强准备与四阶矩泛函。

全文没有新科学执行。
