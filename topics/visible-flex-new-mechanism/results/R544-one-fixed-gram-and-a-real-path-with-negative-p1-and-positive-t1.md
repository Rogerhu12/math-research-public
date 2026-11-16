# R544：一个固定 Gram 内净负 $p_1$ 与净正 $t_1$ 的完整实际路径

日期：2026-11-16。**原式纸证与有限维真实 ODE；没有运行数值、求积、符号、profile、秩或开发检查。**

本文固定 R521 的同一个正交母库，从真正零二、三阶历史的起点出发，只选一次第三规范 $\chi$，构造一条完整 ruling 恒为零的实际路径，并同时得到
$$
\boxed{\int M_{p_1}^{\omega_c}<0,\qquad
       \int M_{t_1}^{\omega_c}>0.}
\tag{1}
$$
积分包括全部快入段、反馈切换、有限高度过渡和长尾。这里没有把 R539 与 R541 两份不同 $\chi$ 的符号收据拼接。

两项新增机制缺一不可。第一，大 Gram 的稳定支不经过实际零历史起点；一个有限快控制把真实零初值送到含完整入历史修正的稳定支。第二，使用原唯一的高度加速度输入作吸引反馈，准确处理 $L_{\rm vel}(AD)$ 的可能大反阻尼。只把该项称为“小势”，不能证明本文结论。

实际长尾长度是 $C\lambda^2/\delta$。它与快段的负 $t_1$ 成本具有同一量级，且完整缩放历史仍保持在一个明确小盒内。本文没有声称矩阵零、pose 返回、全 period 或最终等距族已经得到。

## 1. 固定母库、坐标与唯一规范

全程使用 R521 已付的同一 profiles、正交副本、共同右锚、原相位与第二规范 $w=0$。固定
$$
S_c=(H,0,\omega_c),\qquad y=x+\omega_c,\qquad
Hy_{\min}>1,\quad y_{\min}=\min_I y>0.
\tag{2}
$$
令
$$
c=C_k(H,0)>0,\qquad
\beta_*=\frac{B(H,0)}{2c}>0.
\tag{3}
$$
这里 $B$ 是 R535/R537 的原正系数，
$$
C_h+2\eta C_k=-B(h,d),\qquad
\eta=\omega-\omega_c,\quad d=h\eta-k.
\tag{4}
$$

先固定
$$
H_0>\sqrt3\,H.
\tag{5}
$$
再取一个随后足够小的 $\lambda>0$，并置
$$
\delta=\lambda^2\zeta,\qquad 0<\zeta\le1.
\tag{6}
$$
$\lambda$ 在高处、尾长常数及各共同小盒确定后先固定；$\zeta$ 最后取小。最终每一条路径的 $\lambda,\zeta,\delta$ 都是正的有限常数。

用 R521 的原紧支撑 Gram 右逆，从起点一次选择
$$
\boxed{
\nu^{\lambda,\delta}
=\delta^{-2}(-H_0^2\lambda,\ 2c,\ \lambda),\qquad
\mathbf I_y(\phi_\theta,\chi_\theta)
=\sin^2\theta\,\nu^{\lambda,\delta}.
}
\tag{7}
$$
它保原 seed、原相位、真紧与光滑性。下文出现的“有效 Gram”只是对已经存在的真实历史作代数重写；**从未另换实际 $\chi$**。

在实际词的真正起点，
$$
h=H,\quad k=\eta=h_s=k_s=0,\qquad A=T=0.
\tag{8}
$$
frame、位置及所有下阶字段取原恢复的同一初值。不使用一条未付 ruling 的前缀去伪造(8)。

## 2. 把完整大历史写成准确三 Gram，而不删除它

在 $\theta=\pi/2$ 记 $\phi=g$、$D=\Delta$。R521 已付整个 ruling 是该值的 $\sin^2\theta$ 倍数，所以下面没有丢掉其它相位。

采用 R537 的完整第三变量
$$
\widetilde T=T-P_{\rm acc}(S,\gamma,\upsilon)
+\mathcal A(S)\gamma\upsilon,\qquad
\gamma=h_s,\quad\upsilon=k_s,
$$
并定义
$$
\bar A=\delta A,\qquad \bar T=\delta^2\widetilde T.
\tag{9}
$$
原对称配对准确为
$$
E_S(a,b)=\mathbf w_y(S)\cdot\mathbf I_y(a,b),\qquad
\mathbf w_y(S)=\left(\frac{1+d^2}{4h},\frac d2,\frac h4\right).
\tag{10}
$$
$A\Delta$ 是真实紧二阶 profile；$E_S(g,T(g;\Delta))$ 的第一槽 $g$ 真紧，所以原右锚 IBP 的边界也合法。没有把个体非紧原函数改锚。

置
$$
\boxed{
\Gamma=\bar\nu+
\frac12\mathbf I_y(\bar A\Delta,\bar A\Delta)
+2\mathbf I_y\{g,\bar T(g;\Delta)\},
\quad
\bar\nu=(-H_0^2\lambda,2c,\lambda).
}
\tag{11}
$$
这是三个真实实数，随同一实际历史演化。原完整 ruling 乘 $\delta^2$ 后恰可写成
$$
\boxed{
\delta^2\{C_hh_{ss}+C_kk_{ss}+\mathcal R_{\rm loc}\}
+\delta\,L_S(\bar A\Delta)
-\Psi_\Gamma(h,d)=0,
}
\tag{12}
$$
其中
$$
\Psi_\Gamma(h,d)
=\frac{\Gamma_0(1+d^2)}{2h}+\Gamma_1d+\frac{\Gamma_2h}{2}.
\tag{13}
$$
$\mathcal R_{\rm loc}$ 保原 $R_0,R_2$ 及把(9)还原到 $T$ 时的全部速度二次项；
$L_S(\bar A\Delta)$ 对 $(\gamma,\upsilon)$ 真线性。原 $-E(A\Delta,A\Delta)$ 与 $-4E(g,T(g;\Delta))$ 都已完整进入(11)，未被取模或丢弃。

原缩放慢状态准确满足
$$
\bar A_s=\delta\,\Phi_{M_{\rm raw}},
$$
$$
\begin{aligned}
\bar T_s={}&-\delta\,\Phi_{M_{\rm raw}}\circ\bar A\\
&+\delta^2\left[
\mathcal C^{[1]}+
2\mathcal A h_{ss}\upsilon+
\{(X\mathcal A)\gamma+(Y\mathcal A)\upsilon\}\gamma\upsilon+
\sum_{r=0}^3\mathcal B_r\gamma^{3-r}\upsilon^r
\right].
\end{aligned}
\tag{14}
$$
特别保留原有序复合及 $2\mathcal A h_{ss}\upsilon$。右边没有 $k_{ss}$，这是后面的单输入反馈能够准确闭合的原因。

## 3. 稳定二次支及所需全高区间系数界

若
$$
\Gamma_0=-H_0^2\lambda+O(\lambda^2),\quad
\Gamma_1=2c+O(\lambda^2),\quad
\Gamma_2=\lambda+O(\lambda^2),
\tag{15}
$$
则对所有 $h\ge H$，(13)有唯一靠近0、满足
$\partial_d\Psi_\Gamma>0$ 的支 $q_\Gamma(h)$。有理化给准确式
$$
\frac{q_\Gamma(h)}h
=-\frac{\Gamma_2+\Gamma_0/h^2}
{\Gamma_1+\sqrt{\Gamma_1^2-\Gamma_0\Gamma_2-\Gamma_0^2/h^2}}.
\tag{16}
$$
故在(15)的一个固定常数盒内，充分小 $\lambda$ 时，一致有
$$
\frac{q_\Gamma(h)}h
=-\frac{\lambda}{4c}\left(1-\frac{H_0^2}{h^2}\right)
+O(\lambda^2),
\quad
|q_{\Gamma,h}|\le C\lambda,\quad
\partial_d\Psi_\Gamma\ge c.
\tag{17}
$$
这里 $O(\lambda^2)$ 对全部 $h\ge H$ 的**比值** $q/h$ 一致，而非只在一个事后扩大的固定高度盒上成立。

以下原系数界也对 $h\ge H$ 一致。令 $u=d/h$、$t=1/h$，并写
$$
Q/h^2=t^2+(y+u)^2,
$$
$$
F/h^2=\{t^2+(y+u)^2\}r-2(y+u)p+2u_{\rm profile}.
$$
R521/R535 的 $C_k,B$ 积分于是分别成为以
$$
y+u,\qquad y^2-u^2-t^2
$$
为正权、以同一个 $(F/h^2)^4/(Q/h^2)^2$ 为密度的积分。取 $|u|$ 小，
由(2)第二个权也有严格正下界。参数 $(t,u)$ 属固定紧集。
若全部这些密度为零，则一个非零紧微包满足首项系数正的齐次二阶 ODE，从其平端初值唯一性会迫其为零，矛盾。因此
$$
0<c_0\le C_k,\ B,\ B/(2C_k)\le C_0
\tag{18}
$$
在这一区域成立。实际管允许 $h$ 比 $H$ 略小：先固定 $H_-<H$ 且 $H_-y_{\min}>1$，同一证明在 $h\ge H_-$ 仍给这些严格界。

此外，若 $k,\eta$ 有界，R221(17)的完整 $T_s$ 逐项除去 $h^4$ 后给
$$
L_S(\bar A\Delta)=\ell_\gamma(S,\bar A)\gamma+
\ell_\upsilon(S,\bar A)\upsilon,\qquad
|\ell_\gamma|+|\ell_\upsilon|\le C\|\bar A\|.
\tag{19}
$$
该界对 $h\ge H$ 一致：例如 $Q^2/h^4$、$heQ/h^4$、
$FQ/h^4$、$h^2F/h^4$ 及所需乘 $z=y+\eta$ 的系数均有界。
这里只估计原有限 profile 算子范数，不生成新算子或新秩。

## 4. 为什么这条支会给相反于 R541 的高处符号

暂把 $\Gamma$ 固定为快入段真实末值，记为 $\Gamma_* $。后面会证明它满足(15)。快段的真实水平累计满足 $j_*=O(\lambda^2)$，其中
$$
j=\frac{\eta}{h}+\frac d{h^2},\qquad
j_s=-\frac{2d h_s}{h^3}.
\tag{20}
$$
因此支上从 $h=H$ 出发的水平曲线是
$$
J_*(h)=j_*-2\int_H^h\frac{q_{\Gamma_*}(r)}{r^3}\,dr,\qquad
k_*(h)=h^2J_*(h)-2q_{\Gamma_*}(h).
\tag{21}
$$
由(17)，一致到 $h=\infty$，
$$
\lim_{h\to\infty}\frac{k_*(h)}{h^2}
=\lambda\kappa_0+O(\lambda^2),\qquad
\kappa_0=\frac1{2cH}\left(1-\frac{H_0^2}{3H^2}\right)<0.
\tag{22}
$$
$O(\lambda^2)$ 的积分余量由 $\int_H^\infty r^{-2}dr$ 直接控制。

先选一个有限常数 $L_h$，使
$$
K_*:=\kappa_0L_h^2<-4,
\qquad h_1=L_h/\sqrt\lambda.
\tag{23}
$$
于是
$$
k_*(h_1)=K_*+O(\sqrt\lambda),\qquad
q_{\Gamma_*}(h_1)=-\frac{L_h}{4c}\sqrt\lambda+O(\lambda^{3/2}),
$$
$$
\eta_*(h_1)=O(\sqrt\lambda).
\tag{24}
$$
沿 $H\le h\le h_1$，同样有 $|k_*|\le C$、
$|\eta_*|\le C\sqrt\lambda$、$|q|/h\le C\lambda$。
因此小 $\lambda$ 下 $x+\omega=y+\eta>y_{\min}/2$，
$h y+d>0$，且 $B,C_k$ 保正。

(22)的关键是稳定支的零高度为 $H_0> \sqrt3H$，而真实起点高度仍为 $H$。
本稿没有把“稳定支穿过原零初值”的 R541 接口换个符号使用。

由(21)还一致有 $|k_*/h|\le C\sqrt\lambda$；结合 $|\eta_*|\le C\sqrt\lambda$ 与 $H_-y_{\min}>1$，得到 $h^2(y+\eta_*)^2-k_*^2-1>0$ 的共同严格余量。后面的真实小误差与快入段的 $O(\lambda)$ 变化仍保这一完整强合法门，不只保两个一次因子的正号。

## 5. 真零历史快入段与四个有限端点控制

令 $\tau=s/\delta$。R73、R77、R79 及(14)给一个完整正规快系统：
$$
\bar A_\tau=M_2(S,h_\tau,k_\tau)+\delta^2M_0(S),
\tag{25}
$$
而 $\bar T_\tau$ 保留
$-\{M_2+\delta^2M_0\}\circ\bar A$、全部真实速度面积、
速度三次项及 $\delta^2\mathcal C^{[1]}$。
ruling 则是(12)以快导数表达的准确式。没有恢复旧科学输入或删去 $YC$。

取
$$
h=H+\lambda X(\tau),\qquad d=\lambda D(\tau).
$$
从(8)出发，在 $\lambda=0$ 的正规化一阶系统为
$$
\boxed{
D''+D=a_0-\beta_*X'',\qquad
a_0=\frac{H_0^2/H-H}{4c}>0.
}
\tag{26}
$$
所有 $R_2$、$L(\bar A)$、速度面积及历史平方在该系统中从二次开始。
(6)使 $\delta^2/\lambda=\lambda^3\zeta^2$，故这个一阶结论及下面的参数 IFT
对 $0\le\zeta\le1$ 统一正规。

先在一个固定有限快区间内用四个紧支撑光滑加速度控制。
对状态 $(X,X',D,D')$，控制 $X''$ 的四列可控矩阵为
$$
B=(0,1,0,-\beta_*)^t,\quad
AB=(1,0,-\beta_*,0)^t,\quad
A^2B=(0,0,0,\beta_*)^t,\quad
A^3B=(0,0,\beta_*,0)^t.
\tag{27}
$$
$\beta_*>0$ 使其线性独立。等价地，原端点核由
$1,\tau,\sin\tau,\cos\tau$ 生成；可选四个真实内点及足够窄的光滑 bump
使相应四列可逆。这是有限存在证明，不执行新秩。

在后面的一个开放快区间，先平滑切入第6节同一个反馈的**加速度形式**。
在线性极限上，这只是一个可逆的四维有限时流，因此不破(27)的端点满秩。
有限参数 IFT 于是准确支付
$$
\boxed{
h=H,\quad h_\tau=0,\quad
d=q_{\Gamma_*}(H),\quad d_\tau=0
}
\tag{28}
$$
及原实际 $\Gamma_*$ 对控制的全部依赖。
规范仍为(7)，初值仍为(8)。

末端控制已在开放区间退场，只留下后文相同的反馈 ODE。
在(28)上该反馈的一阶约束恰为0，所以它在末端开放区间已经成立。
由此连接的是同一个实际 germ；不是把预给的平高度段硬接到另一个加速度。

完整快系统直接给统一界
$$
h-H,\ k,\eta,d,\ h_\tau,k_\tau=O(\lambda),
$$
$$
\boxed{\bar A_*=O(\lambda^2),\quad
\bar T_*=O(\lambda^2),\quad j_*=O(\lambda^2).}
\tag{29}
$$
特别，末速度为0只消掉 $P_{\rm acc}$ 的端值，**不消掉原速度面积**；
所以这里不能把 $\bar T_*$ 改写成 $O(\lambda^3)$。
(11)与(29)准确给(15)。

令该快段长度为固定 $T_f$。原矩恒等式给
$$
\left|\int_{\rm fast}M_{p_1}\,ds\right|
\le C\delta\lambda^2,
$$
$$
\boxed{
\int_{\rm fast}M_{t_1}\,ds
\ge -C_f\frac{\lambda^2}{\delta}-C\delta .
}
\tag{30}
$$
第二式完整保
$-\frac1{8\delta}\int(h_\tau/h)^2d\tau$，包括控制及反馈切换部分。
$C_f$ 可在先选定的有限控制族上统一固定。

## 6. 一个真实单输入反馈及其非奇异闭合

在入段后，先选一条有限光滑参考高度 $\bar h(s)$：起始开放段为 $H$，
经一段固定有限过渡到 $h_1$，以后恒为 $h_1$。
这一过渡在固定 $\lambda$ 后选择，全部所需导数界有限。
取固定 $\kappa>0,\kappa_h>0$。

所有以下系数先在同一个瞬时支 $d=q_\Gamma(h)$ 上评价；置
$$
\eta_q=hj-q_\Gamma/h,\quad
\alpha=\frac{\Psi_{\Gamma,d}(h,q_\Gamma)}{2C_k(h,q_\Gamma)},\quad
\beta=\frac{B(h,q_\Gamma)}{2C_k(h,q_\Gamma)},
$$
$$
\ell=\frac{\ell_\gamma+2(\eta_q-q_{\Gamma,h})\ell_\upsilon}{2C_k},
\qquad b=-\frac{\ell_\upsilon}{C_k}.
\tag{31}
$$
令
$$
v_*=\bar h_s-\kappa_h(h-\bar h),\qquad
V=(1-\kappa\ell/\alpha)v_*,
$$
$$
\boxed{\gamma=V+\frac{\kappa}{\delta}\{d-q_\Gamma(h)\}.}
\tag{32}
$$
这是一条状态反馈约束，不是新增第二个几何控制。
物理 $\chi$ 仍为(7)。

把 $\bar Z=(\bar A,\bar T)$ 的准确方程写作
$$
\bar Z_s=Z^0+\delta^2Z^1a,\qquad
a=h_{ss},\qquad Z^1=(0,2\mathcal A\upsilon).
$$
微分(32)后，$a$ 的准确系数为
$$
\boxed{
\mathfrak m=
1-\delta^2 V_{\bar Z}Z^1+\kappa\delta q_{\bar Z}Z^1.
}
\tag{33}
$$
右边其余项准确为
$$
V_s+V_h\gamma+V_jj_s+V_{\bar Z}Z^0
+\frac{\kappa}{\delta}
\{d_s-q_h\gamma-q_{\bar Z}Z^0\}.
\tag{34}
$$
这里 $V_s$ 是显式时间偏导。先解(33)(34)得到真实 $h_{ss}$，再由原(12)
解 $k_{ss}$；全过程没有替换原 $M_{\rm raw}$ 或第三方程。

在快入段，$\upsilon=O(\lambda/\delta)$，故(33)为 $1+O(\lambda)$；
在后续有限状态盒内，它为 $1+O(\delta)$。小 $\lambda$、再小 $\zeta$
使它始终非零。第5节末端采用的就是这个加速度形式。
量 $\gamma-V-\kappa(d-q)/\delta$ 的导数准确为0，而(28)使其值为0；
因此开放末 germ 与后续(32)逐 jet 相同。

## 7. 完整快法向矩阵的阻尼号

令
$$
r=\frac{d-q_\Gamma(h)}{\delta},\qquad
w_n=d_s-q_{\Gamma,h}\gamma,\qquad \tau=s/\delta .
\tag{35}
$$
$w_n$ 是法向实标量速度；原第二 profile 规范仍为0。

由(12)–(14)(33)，在一个固定合法状态盒内准确有
$$
r_\tau=w_n+O(\delta),
$$
$$
(w_n)_\tau
=-(\alpha-\kappa\ell)r
-\{\kappa(\beta+q_h)-b\}w_n+\ell V+O(\delta).
\tag{36}
$$
余项完整含移动 $\Gamma$、原 $R_0,R_2$、速度势、$j_s$ 和全部第三累计；
其界只依赖该盒与预给参考高度的有限导数。
例如 $q_{\bar Z}\bar Z_s$ 中的加速度项由(33)变为 $O(\delta)$，
并未在推导 $r_\tau$ 时删除。

在实际所用盒中 $\|\bar A\|\le C_A\lambda^{3/2}$。
由(17)–(19)，充分小 $\lambda$ 给
$$
\boxed{
\alpha-\kappa\ell\ge a_*>0,\qquad
\kappa(\beta+q_h)-b\ge d_*>0.
}
\tag{37}
$$
这同时支付刚度与阻尼。原 $L_{\rm vel}$ 的速度系数没有被预设符号；
它是(37)中真实的 $b$，由原高度反馈压住。

令
$$
r_*=\ell v_*/\alpha .
$$
因为 $(\alpha-\kappa\ell)r_*=\ell V$，
$R=r-r_*$ 与 $w_n$ 的主系统为
$$
R_\tau=w_n+O(\delta),\qquad
(w_n)_\tau=-a_nR-d_nw_n+O(\delta),
$$
其中 $a_n=\alpha-\kappa\ell$、$d_n=\kappa(\beta+q_h)-b$。
系数的快时间导数为 $O(\delta)$；这来自真实状态方程，不是假定它们恒定。

取一个足够小、固定的 $\varepsilon_E>0$，
$$
\mathcal E_n=\frac12(w_n^2+a_nR^2)+\varepsilon_E Rw_n.
$$
用 $a_*,d_*$ 及其有限上界，可一次选 $\varepsilon_E$ 使此式正定，
并由(36)逐项得到
$$
\boxed{
(\mathcal E_n)_\tau\le-c_*\mathcal E_n+C(\lambda)\delta^2.
}
\tag{38}
$$
例如交叉项为
$-\varepsilon_Ea_nR^2+\varepsilon_Ew_n^2-\varepsilon_Ed_nRw_n$，
分别用 Young 不等式吸收到负二次项；$(a_n)_\tau=O(\delta)$
在最后取小 $\zeta$ 时吸收。这给真正的耗散估计，而不是随总时长增长的 Gronwall 常数。

入端(28)使 $r=w_n=r_*=0$。因此只要联合状态盒还成立，
$$
\boxed{|R|+|w_n|\le C(\lambda)\delta}
\tag{39}
$$
对任意已讨论的快时间长度统一成立。
由(32)及 $r_*=\ell v_*/\alpha$，还有准确恒等式
$$
h_s=v_*+\kappa R=v_*+O(C(\lambda)\delta),
$$
故
$$
\boxed{|h-\bar h|\le C(\lambda)\delta}
\tag{40}
$$
也不随长尾时长增长。这是 $\kappa_h>0$ 的实际用途。

## 8. 过渡段后的统一历史盒

在有限高度过渡上，(39)(40)使 scalar、速度及加速度都处于一个
只依赖已固定 $\lambda$ 的有限盒；由(33)，加速度没有留下 $1/\delta$ 的发散。
(14)因此给
$$
\bar A=\bar A_*+O(C(\lambda)\delta),\qquad
\bar T=\bar T_*+O(C(\lambda)\delta).
\tag{41}
$$
在最后取小 $\zeta$ 时，可使这两个增量及对 $\Gamma$ 的影响小于任意预定的
$\lambda^3$ 量。

由(20)，在这段有限过渡上，真实 $j$ 与(21)相差
$O(C(\lambda)\delta)$。故到达高处开放尾段时，(24)以及以下严格余量都成立：
$$
k<-3,\qquad
d<-\frac{L_h}{8c}\sqrt\lambda,\qquad
|\eta|\le C\sqrt\lambda .
\tag{42}
$$
同时 $h=h_1+O(C(\lambda)\delta)$。有限过渡本身的
$p_1,t_1$ 全累计绝对值均不超过一个有限 $C_{\rm mid}(\lambda)$，
该数与随后取小的 $\zeta$ 无关。

这里实际 $h$ 是(32)的真实输出；它不被声称与预给 $\bar h$ 逐点相等。
只有从原完整 ODE 得到的(40)(42)被用于后面。

## 9. 长度 $C_{\rm tail}\lambda^2/\delta$ 的真实尾段

选定一个稍后固定的有限 $C_{\rm tail}>0$，令尾段长度为
$$
\boxed{T_{\rm tail}=C_{\rm tail}\lambda^2/\delta=C_{\rm tail}/\zeta.}
\tag{43}
$$
参考高度在整个尾段为 $h_1$。证明采用一个联合最大区间：
scalar 保持在(42)的稍大合法盒内，正常变量有界，并且
$$
\|\bar A\|\le C_A\lambda^{3/2},\qquad
\|\bar T\|\le C_T\lambda^2.
\tag{44}
$$
先在此区间上应用(38)–(40)，再用以下原式积分严格改进(44)。
这是联合 bootstrap，不先假设解已经存在到(43)。

### 9.1 全部速度与加速度

尾段 $v_*=-\kappa_h(h-h_1)=O(C(\lambda)\delta)$，
所以(39)给
$$
r_*=O(C(\lambda)\delta),\quad
r=O(C(\lambda)\delta),\quad w_n=O(C(\lambda)\delta).
$$
因而
$$
\boxed{
h_s,k_s=O(C(\lambda)\delta),\qquad
d-q_\Gamma(h)=O(C(\lambda)\delta^2),\qquad
h_{ss},k_{ss}=O(C(\lambda)).
}
\tag{45}
$$
加速度界直接由(33)(34)及 $w_n/\delta=O(C(\lambda))$ 得到；
不能只从小位置误差推小导数。

### 9.2 原八矩和完整第三历史

使用固定 $y=x+\omega_c$ 的八坐标，R73 的原静态式在
$$
h\asymp h_1=L_h/\sqrt\lambda,\quad |k|\le C,\quad
|\eta|,|d|\le C\sqrt\lambda
$$
上给
$$
\|M_0\|\le C(1+h_1)\le C\lambda^{-1/2}.
\tag{46}
$$
例如唯一可能线性长大的 $p_2=-kh/2$ 保留；$t_1=O(1)$，
而其它坐标由 R73(6)(9)(10)逐项有同一上界。
固定坐标平移不改变该量级。速度二次部分由(45)另受
$C(\lambda)\delta^2$ 控制。

把(46)积到(43)中，得到
$$
\|\bar A-\bar A_{\rm in}\|
\le C C_{\rm tail}\lambda^{3/2}
+C(\lambda)\delta^2\lambda^2 .
\tag{47}
$$
再对完整(14)积分，其主有序项满足
$$
\delta\int\|\Phi_M\circ\bar A\|
\le C C_{\rm tail}\lambda^2\lambda^{-1/2}
                   C_A\lambda^{3/2}
\le C\lambda^3 .
\tag{48}
$$
其余原第三项都保有速度因子。
由(45)，包括 $2\mathcal A h_{ss}\upsilon$ 在内的方括号是
$O(C(\lambda)\delta)$；故它对 $\bar T$ 的全尾增量是
$$
O(C(\lambda)\delta^2\lambda^2).
\tag{49}
$$
这一步明确保留原速度面积及两个端点势，没有把真实 $T$ 当成缓慢的常数。

先固定足够大的 $C_A,C_T$，再取小 $\lambda$，最后取小 $\zeta$；
(29)(41)(47)–(49)严格改进(44)。特别
$$
\boxed{
\bar A=O(\lambda^{3/2}),\qquad
\bar T=O(\lambda^2),\qquad
\Gamma-\bar\nu=O(\lambda^2)
}
\tag{50}
$$
对整个长尾统一。这里常数不随 $\zeta\to0$ 或尾长发散。
$O(\lambda^2)$ 的第三入值不是0；它正是(11)(16)中的真实势修正。

### 9.3 水平累计不会在长尾暗中漂移

只用 $j_s=O(\delta)$ 和长时长不能得到所需结论。
对每个瞬时 $\Gamma$ 定义
$$
\mathcal J(h,\Gamma)
=-2\int_{h_1}^{h}q_\Gamma(r)r^{-3}\,dr.
$$
由 $|h-h_1|=O(C(\lambda)\delta)$，
$\mathcal J$ 及 $\mathcal J_\Gamma$ 都是 $O(C(\lambda)\delta)$。
而(14)(45)–(50)给 $\Gamma$ 在整个尾段上的有界总变差，
其主增量为 $O(\lambda^3)$，剩余量按(49)计入。

对(20)准确分部得到
$$
j-j_{\rm in}
=[\mathcal J]_{\rm in}^{s}
-\int\mathcal J_\Gamma\Gamma_s\,ds
-2\int\{d-q_\Gamma(h)\}\frac{h_s}{h^3}\,ds.
\tag{51}
$$
最后一项由(43)(45)为 $O(C(\lambda)\delta^2\lambda^2)$。
因此
$$
\boxed{j-j_{\rm in}=O(C(\lambda)\delta)}
\tag{52}
$$
一致到整个尾端。结合(16)(24)(50)，实际 $k,d,\eta$ 始终保持(42)
及同一合法窗口，并严格改进初始 scalar 盒。

(39)(40)(44)(52)共同关闭最大区间。
原 ODE 的有限维延拓准则由此保证整段(43)真实存在，
而非先假定长期存在再用其历史估计。

## 10. 同一尾段同时付两个严格密度号

由(42)(45)，充分小 $\lambda$、再充分小 $\zeta$ 时，
$$
\boxed{
M_{p_1}=-kd\le-c_p\sqrt\lambda<0
}
\tag{53}
$$
其中 $c_p>0$ 可以在先选定的 $L_h,K_*$ 上固定。

原准确另一行是
$$
8M_{t_1}=k^2+2kd-1-(h_s/h)^2 .
\tag{54}
$$
在尾段 $k<-3,d<0$，且(45)使末项小。因此可固定一个
$\rho_t>0$（例如充分缩小参数后取 $\rho_t=1/2$），使
$$
\boxed{M_{t_1}\ge\rho_t>0.}
\tag{55}
$$
真实反馈中的 $\gamma=h_s$ 没有被置0。其全尾负成本还准确满足
$$
\int_{\rm tail}(\gamma/h)^2\,ds
\le C(\lambda)\delta\lambda^2,
\tag{56}
$$
与(45)(43)一致。因而没有用极限常高度替代原矩积分。

## 11. 全词累计、选择顺序及同一个 $\chi$

先固定 $H,H_0,\kappa,\kappa_h$ 及第5节的有限控制族，取其统一 $C_f$；再固定满足(23)的 $L_h$ 与(55)的 $\rho_t$，并选
$$
C_{\rm tail}>(C_f+2)/\rho_t.
\tag{57}
$$
随后按所有明确小盒取一个固定小 $\lambda>0$，令 $h_1=L_h/\sqrt\lambda$。
参考有限高度过渡、其时间与全部导数界随后固定。
最后取 $\zeta>0$ 足够小，使前述完整反馈估计、入段 IFT 和所有严格余量同时成立。

由(30)(43)(55)，
$$
\int_{\rm all}M_{t_1}\,ds
\ge(\rho_tC_{\rm tail}-C_f)\frac{\lambda^2}{\delta}
-C_{\rm mid}(\lambda)-C\delta>0 .
\tag{58}
$$
所有快切换都已经包含在 $C_f$；整个有限高度过渡包含在
$C_{\rm mid}(\lambda)$；长尾反馈的真实速度成本见(56)。

同时由(30)(43)(53)，
$$
\int_{\rm all}M_{p_1}\,ds
\le C\delta\lambda^2+C_{\rm mid}(\lambda)
-c_p C_{\rm tail}\frac{\lambda^{5/2}}{\delta}<0 .
\tag{59}
$$
这里 $\lambda$ 已先固定，所以最后令 $\zeta$ 小确实同时使
(58)(59)严格成立。没有将两个不同参数选择的结论拼接。

**定理。** 固定 R521 的同一实际正交母库，在(2)的合法起点，
存在从(8)真实零历史出发、只使用(7)这一份固定第三规范且 $w=0$ 的
有限光滑实际路径，使全部相位的完整 fourth ruling 逐点为零，并满足(1)。
其末段实际曲率 $k<-3$，仍在同一完整物理窗口中。
全快入段、切换、过渡和长尾均为同一个原 ODE 的连续实际词。

(7)的 $\chi$ 在整个词中完全不变；(11)只是其与真实 $A,T$ 相合后的
精确代数势，不能解释成沿路径自由更换第三规范。
原 frame、位置、第四字段及全部成本按真实方程恢复，在每个最终固定的
$\lambda,\zeta>0$ 上都有限并保全部入端常数。

## 12. 尚未支付的完整返回

本定理支付的是同一实际词上的两个净符号，仍没有清八矩。
例如高尾的 $p_2=-kh/2$ 为正，不能从(58)(59)推它的总值为零。
当前末端也不是一个已经反射配好的全偶 germ。

下一步必须在同一(7)规范下处理其余真实矩、frame/位置、完整第三和第四
period 及原十三规范；本稿没有引用 R70 的无 ruling 桥，也没有借另一母库的
负矩控制。净符号相容只是实际闭合所需的一步，不是主问题的完成。

### 原来源

- [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)：全八矩、水平式及原有序第三累计；
- [R77](R77-weight-three-local-operator-actual-finite-controllability.md)、[R79](R79-closed-horizontal-C1-control-and-endpoint-potential.md)：完整速度势、速度面积与真实导数权；
- [R221](R221-complete-fixed-circle-ruling-moment-map-and-joint-right-inverse.md)(17)：完整速度线性配对；本文(19)不删其原右尾；
- [R482](R482-pointwise-third-memory-elimination-and-constrained-prototype-ruling-system.md)：未消第三历史的完整 ruling；
- [R521](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md)：唯一母库、全部相位、合法 Gram 与正加速度行；
- [R537](R537-prescribed-finite-height-paths-with-one-gauge-and-complete-history-energy-bounds.md)：无 $k_{ss}$ 的完整第三变量；
- [R541](R541-finite-curvature-and-positive-total-matrix-entry-on-one-stable-gram-branch.md)：稳定支的精确水平输运；本稿重新支付不同 Gram、入历史和吸引反馈；
- [R545](R545-complete-fast-height-loops-and-the-signed-oscillator-energy-transfer.md)：完整正规快系统及不能删除的二阶第三面积；本文第5节另付四端控制与同反馈 germ。

全稿没有新科学执行，也没有把符号、history 势或规范选择作跨词拼接。
