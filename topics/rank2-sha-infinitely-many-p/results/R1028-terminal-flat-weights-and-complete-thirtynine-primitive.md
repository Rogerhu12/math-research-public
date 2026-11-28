# R1028 — 末六个原 flat 权的固定有理分解、全39支第一 primitive 与统一双测试

日期：2026-11-27 UTC。**已证明。** 本篇在 R1026 的原完整
39支返回上，将末六个三处权写成同一个仿射权加六个固定有理函数。
全部水平项由原函数本身确定，不留下待选常数。
在目标截面的实际 $[\alpha]$ 拉回下，五个固定差在全部39条纤维
的同一第一 primitive 低窗内消失。十三处权、Miller 相位、
外部平移和原点留数仍逐项保留。

以下全函数分解是特征 $p$ 中的严格等式。
它不将特征零 $V_\delta$ 无证替换为一个新权；
R1026 的真实 $p^{K}$ 比较及全部特征零余带继续使用原式。

## 1. 同一个末六参数窗与固定 Hermite 问题

保持
$$
E:y^2=x^3+1,\quad X=x^3,\quad u=x/y,\quad
\omega_E=dx/(2y),\quad D=d/dz,
\quad p=6s-1>13^4.
$$
对 $1\le t\le6$ 置
$$
q_t=s-t-1,\qquad H_t=6q_t+5=p-6t,\qquad
K=5s-2.
\tag{1}
$$
R1026 已付：这六个参数全部在原十三处饱和区，
比较精度都准确为 $p^K$。
记原三处根为
$$
W_t=v^{2q_t+2}B_{2q_t+2,q_t}(v),\qquad
v=X/(X+1),\qquad
c_t=12(q_t+1)\binom{3q_t+2}{q_t}\in\mathbf F_p^\times.
\tag{2}
$$
于是
$$
DW_t=c_t u^{p-6t}.
\tag{3}
$$

先在特征零构造完全固定的有理函数。定义
$$
\mathcal Lr=6(X+1)r'(X)-(1+4/X)r(X).
$$
存在唯一
$$
r_t(X)=\sum_{j=1-2t}^{t}r_{t,j}X^j,\qquad
\mathcal R_t=\frac y{x^2}r_t(X),
$$
和唯一常数 $a_t$，满足
$$
\boxed{
\mathcal Lr_t=\frac{(X+1)^{3t}}{X^{2t}}-a_t,\qquad
d\mathcal R_t=(u^{-6t}-a_t)\omega_E.
}
\tag{4}
$$
这是有限 Laurent 线性问题，不是另选一个形式原函数。

其常数有闭式
$$
\boxed{
a_t=\frac{(1/2)_{3t}}{(2/3)_{2t}(5/6)_t}
=\left(\frac{27}{4}\right)^t
 \frac{(1/6)_t(1/2)_t}{(1/3)_t(5/6)_t}.
}
\tag{5}
$$
所有 $a_t$ 非零。

### 1.1 自给的有限系数证明与坏素数

在 Laurent 单项式上，
$$
\mathcal L(X^j)=(6j-1)X^j+(6j-4)X^{j-1}.
$$
以 $\ell(1)=1$ 及
$$
\ell(X^j)=(-1)^j(1/3)_j/(5/6)_j
$$
定义有限区间上的线性泛函，负整数下标按原有理积解释。
它严格杀掉上述 $\mathcal L(X^j)$。
$3t$ 个像线性独立，其最高项系数 $6j-1$ 均非零，
所以它们恰是这 $3t+1$ 维 Laurent 区间内的 $\ker\ell$。
这证明 (4) 的唯一性。

对 $\ell((X+1)^{3t}/X^{2t})$ 作有限二项式展开，
有限 Vandermonde 恒等式给
$$
\frac{(1/6)_{2t}}{(2/3)_{2t}}\,
\frac{(1/2)_{3t}}{(5/6-2t)_{3t}}
=\frac{(1/2)_{3t}}{(2/3)_{2t}(5/6)_t},
$$
证明 (5)，无需选择周期或引用一个未付的积分归属。

求 $r_t$ 只需上述有限三角消元：
分母来自 $6j-1,6j-4$，其中 $1-2t\le j\le t$，
以及 (5) 的有限有理积。
对 $t\le6$，这些非零整数的绝对值均不超过70；
$a_t$ 的分子、分母也只含这些固定小素数。
故 $\mathcal R_t$、$a_t^{\pm1}$ 的全部垂直分母只需删
素数不超过71。主范围 $p>13^4$ 已统一支付。

例如
$$
a_1=\frac{81}{40},\qquad
\mathcal R_1=\frac y{x^2}
\left(\frac X5-\frac{23}{40}-\frac1{10X}\right).
\tag{6}
$$

## 2. 全部水平项由原 W_t 严格确定

在原特征 $p$ 模型中 $DZ=1$，保持
$$
\rho_p c_p=1,\qquad
c_p=\binom{3s-1}{2s-1}.
$$
由 (3)–(4)，
$$
D\{W_t-c_tu^p(\mathcal R_t+a_tZ)\}=0.
$$
因此括号是函数域中的一个 $p$ 次幂。下面在整个曲线上确定它。

$\mathcal R_t$ 的极只可能在
$$
E[\delta]=\{O,S,-S\},\qquad S=(0,1),
$$
各极阶至多 $6t-1\le35$；在三个非零二挠点都为零。
$u$ 在上述三个点各有一次零，所以
$u^p\mathcal R_t$ 在它们正则。
在其它点，括号唯一可能的极是三处二挠，帽为 $2p$。

原 $\mu_6$ 作用下 $u,\mathcal R_t,Z$ 都具有参数的角色，
故 $u^p\mathcal R_t$ 和 $u^pZ$ 均不变。
括号的唯一 $p$ 次根也不变，并仅在
$\mathcal D_2=E[2]\setminus O$ 有至多二阶极。
不变量环为 $k(X)$，因此整个水平项必为
$$
A+\frac{B}{y^{2p}}.
$$
在 $O$，$W_t(O)=1$ 且 $u^p(\mathcal R_t+a_tZ)$ 为零，
所以 $A=1$。
在 $S$ 或 $-S$，原 $W_t=0$，
而 $u^p\mathcal R_t$ 仍为零，$Z$ 正则，
所以 $B=-1$。这同时支付全部三处二挠的水平唯一性。

在任一 $Q_e=(e,0)$，原 $Z$ 的最高主部是
$e\rho_p y^{-p}$，$u^p$ 的最高主部是 $e^p y^{-p}$。
因为 $e^{p+1}=1$，
$u^pZ$ 的最高 $2p$ 阶主部在全部三个点都是
$\rho_p y^{-2p}$。
原 $W_t$ 的极阶为 $H_t-1<p$，故 $2p$ 阶项必须消去，
严格给出 $c_ta_t\rho_p=1$。于是
$$
\boxed{c_ta_t=c_p.}
\tag{7}
$$

令固定有理函数
$$
T_t=\mathcal R_t/a_t.
$$
最终的完整函数等式为
$$
\boxed{
W_t=W_\infty+c_pu^pT_t,\qquad
W_\infty=1-y^{-2p}+c_pu^pZ.
}
\tag{8}
$$
这里没有待选 horizontal 或一个被丢掉的低项。
特别
$$
\boxed{
W_t-W_{t'}=c_pu^p(T_t-T_{t'}),\qquad
DW_\infty=c_pu^p,\qquad D^2W_\infty=0.
}
\tag{9}
$$

原特征零三处权的实际约化仍准确是
$$
\boxed{
\bar V_{\delta,t}=W_t^p
=W_\infty^p+c_pu^{p^2}T_t^p.
}
\tag{10}
$$
最后一项不是零，不能在全函数或模 $p^K$ 中直接删去。

## 3. 五个固定差的全部零极与末两条显示式

由 (4)，
$$
dT_t=(u^{-6t}/a_t-1)\omega_E.
$$
每个 $T_t$ 在三个二挠点为零。
对 $t\ge2$，
$$
d(T_t-T_1)=(u^{-6t}/a_t-u^{-6}/a_1)\omega_E,
$$
所以 $T_t-T_1$ 在每个二挠点都准确从七阶起。
这不是只看一个角或一个二挠点。

在 $O$，$T_t$ 的最高极项是
$$
-\frac{z^{1-6t}}{(6t-1)a_t}.
$$
因此 $T_2-T_1,\ldots,T_6-T_1$ 是五个固定线性独立有理函数；
它们各在 $O,\pm S$ 的极阶不超过
$11,17,23,29,35$，无其它极。

末两条有完全短式
$$
a_2=\frac{137781}{14080},\qquad
\frac{a_2}{a_1}=\frac{1701}{352},
$$
$$
\boxed{
T_2-T_1=
\frac{81v^2-33v-16}{352a_2}\,u^{-11}.
}
\tag{11}
$$
可将 (11) 全微分，与 (4) 相比，再以二挠零值固定常数；
它也直接给三个二挠的准确七阶零。

## 4. 原完整39支中的固定差：因子保持 source 位置

取 R1022 的原反次序权
$$
V_{\alpha,t}^{\rm alt}(P)
=V_{\delta,t}(P)V_{\pi,t}(\delta P).
$$
记
$$
\widetilde v=v_\pi\circ[\delta],\qquad A=u\widetilde v.
$$
在全部末六参数上，R1026 的原十三处饱和给
$$
\bar V_{\alpha,t}^{\rm alt}
=W_t^p\,\widetilde v^{\,p^2}.
\tag{12}
$$
$A$ 在整个 $\ker[\alpha]$ 的39个点各有一次零：
$u$ 支付 $\ker[\delta]$ 的三个点，
$\widetilde v$ 支付其余36个点。
更完整地，
$$
\operatorname{div}(A)=
\ker[\alpha]
-5\mathcal D_2
-4\bigl([\delta]^{-1}\mathcal D_2\setminus\mathcal D_2\bigr).
\tag{13}
$$
这给原因子的位置与全部补极；没有把它移出 trace。

对原任一完整来源 $f\in S_{390}$，
以及全部 $0\le b<p$，在最终 target 记
$$
\eta_{t,b}=Z^{-b-1}P_{10}A_{10,\alpha,t}(f)\omega_E.
$$
在原 source 上定义与 $t$ 无关的完整微分
$$
\vartheta_b=
[\alpha]^*(Z^{-b-1}P_{10}\omega_E)\,
\frac{R_f}{R_\alpha^{10}}.
$$
原未平均 trace 准确给
$$
\eta_{t,b}=\alpha^{-10}
 \operatorname{Tr}_{[\alpha]}(\bar V_{\alpha,t}^{\rm alt}\vartheta_b).
$$
令 $\nu_b=C\vartheta_b$。Cartier 与 trace 的真实交织给
$$
\boxed{
C\eta_{t,b}
=\alpha^{-10/p}
 \operatorname{Tr}_{[\alpha]}
 \bigl(W_t\,\widetilde v^p\nu_b\bigr).
}
\tag{14}
$$
$\alpha^{-10/p}$ 表示原有限常数域中的真实 $p$ 次根，
不是另选复根。所有 source 的完整 Miller 规范、
十三字符和外部 $\tau$ 都已经在 $R_f$ 与原 pullback 中；
(14) 不对各个词额外赋零。

因而完整差为
$$
\boxed{
C(\eta_{t,b}-\eta_{t',b})
=c_p\alpha^{-10/p}
\operatorname{Tr}_{[\alpha]}
 \bigl(A^p(T_t-T_{t'})\nu_b\bigr).
}
\tag{15}
$$

## 5. 同一个 target 截面与全部第一 primitive 低窗

必须统一选择 **最终 target** 的
$$
H_*=p-6,\qquad \varphi_*=\varphi-dJ_{H_*},
\qquad C\varphi_*=\omega_E.
$$
然后在 source 使用它的实际 $[\alpha]$ 拉回。
它在全部39个核点都从 $p-1$ 阶起。
若误用 source 自己的 $\varphi_*$，
它在 $\pm S$ 不具有这个平坦度，以下结论便不能成立。

记 target 截面及唯一 primitive 类为
$$
\mathfrak S_*(g\omega_E)=g^p\varphi_*,
\qquad
[\mathfrak P_*(\xi)]
=D^{-1}(\xi-\mathfrak S_*C\xi)\pmod{F^p}.
$$
在 source 以 $[\alpha]^*\omega_E$ 为基，
用 $[\alpha]^*\varphi_*$ 定义同一截面的拉回
$\mathfrak S_*^\alpha,\mathfrak P_*^\alpha$。
trace 与这两个算子在 primitive 类上交织：
$$
[\mathfrak P_*\operatorname{Tr}\xi]
=[\operatorname{Tr}\mathfrak P_*^\alpha\xi].
\tag{16}
$$
证明是 trace 与 $C$ 交织，
且 $\operatorname{Tr}(g^p)=(\operatorname{Tr}g)^p$；
全导数的 primitive 差恰属 $F^p$。

两个 primitive 算子都对 $F^p$ 线性。
因此 (15) 的同一个第一 primitive 准确为
$$
\boxed{
[\mathfrak P_*C(\eta_{t,b}-\eta_{t',b})]
=c_p\alpha^{-10/p}
\left[
\operatorname{Tr}_{[\alpha]}
 \left(A^p
 \mathfrak P_*^\alpha((T_t-T_{t'})\nu_b)\right)
\right].
}
\tag{17}
$$
$A^p$ 始终在实际39支 trace 内。

### 5.1 完整局部帽，包括真实四阶 adjoint cut

在每个 $\ker[\alpha]$ 点，
$\vartheta_b$ 的极至多 $b+1\le p$：
原 $P_{10}$ 在 target $O$ 的十阶零，
与 $R_\alpha^{-10}$、完整 theta 来源的实际零极准确抵消。
这适用于完整词，而非只对其质量项。

若把 R1021 §8 的真实四阶伴随全部置于 cut 上，
至多再增加四阶极。原 $G$ 在 target $O$ 至多简单极，首项为 $1/z$，
Miller 对数导数至多简单极，
原 $x$ 势的平方至多四阶极。
所以这一完整范围内总极不超过 $p+4$，
其第一次 Cartier $\nu$ 在核点的极至多二阶。

$T_t$ 的极只在三个 $\ker[\delta]$ 点，帽35。
故 $T_t\nu$ 在任何核点的极至多37。
由于 $p>37$，$C(T_t\nu)$ 在这些点至多有简单极。
拉回截面从 $p-1$ 阶起，所以
$$
\operatorname{pole}_{\ker\alpha}
\bigl(\mathfrak S_*^\alpha C(T_t\nu)\bigr)\le1.
$$
因此其准确 exact 部分在核点的极仍至多37；
primitive 类可在每个核点选择极至多36的局部代表。
所有积分分母小于 $p$，没有隐藏的除 $p$。

利用 (13)，
$$
\boxed{
\operatorname{ord}_{\ker\alpha}
\left(A^p\mathfrak P_*^\alpha(T_t\nu)\right)
\ge p-36>K.
}
\tag{18}
$$
(18) 按每个核点的局部 primitive 代表计算；这足以计算完整的已完成局部 trace。
未平均 trace 在 target $O$ 保持这个下界。
局部 primitive 的 $F^p$ 代表歧义，经乘 $A^p$ 和 trace 后
仍是 target 的 $p$ 次函数；全部 $0<r<p$ 读数不受影响。

### 5.2 真正可以替换的整个低窗

(18) 不仅适用于五个差，也分别适用于每个 $T_t$。
因此在同一个原 first-Cartier/第一 primitive 读者中，
全部
$$
0<r\le K
$$
的实际系数可将 (14) 内的 $W_t$ 统一替换为 $W_\infty$。
这适用于全部 $b<p$ 以及刚支付的完整四阶 adjoint cut，
不是只支付 diagonal 角或第三 Cartier。

原 $r=0$ 仍读真实留数
$\alpha^{-b}c_b(f)$；
R1020 的 $b\equiv5$ 截面 scalar、
$-\rho_b r_0\omega_E$ 修正和原 affine $aZ$
全部保留在同一个 primitive 规范中。
六个原返回的留数相同，故比较它们时该修正确实相消；
没有将每个来源的全部质量或低 jet 都宣称为零。

这里得到的是 **特征 $p$ 的整个有限 reader 低窗替换**。
(10) 的全函数余项仍在，特征零的 (7) 型中央比较
仍须保留 R1026 的全部原 $V$ 与较低位精度。

## 6. 两个固定 Frobenius 权与一次 Z 测试

(8) 的共同权已是原 source $Z$ 上的仿射函数：
$$
W_\infty=(1-y^{-2})^p+(c_pu)^pZ.
\tag{19}
$$
因此对同一 source primitive 类严格有
$$
\mathfrak P_*^\alpha(W_\infty\nu)
=(1-y^{-2})^p\mathfrak P_*^\alpha(\nu)
 +(c_pu)^p\mathfrak P_*^\alpha(Z\nu).
\tag{20}
$$
这是完整算子的 $F^p$ 线性，不是把某个中央函数当成乘法同态。

也可使用实际 $\delta$ target 参数。
保持 R887 的原全部 cocycle
$$
Z_\delta=\delta Z+h_\delta^p,\qquad
h_\delta=\frac{6\delta\rho_p x^2}{y(X-8)}.
$$
令固定有理函数
$$
A_\delta=\frac{X(X-2)}{(X+1)(X-8)},\qquad
B_\delta=-\frac{c_p x}{\delta y}.
$$
由 $\delta^p=-\delta$ 及 $c_p\rho_p=1$，
完整函数恒等式是
$$
\boxed{W_\infty=A_\delta^p+B_\delta^pZ_\delta.}
\tag{21}
$$
直接代回可见
$A_\delta=v+(c_p/\delta)u h_\delta$，
全部 $X=8$ 补极在两个项之和中准确抵消。
它们不能分别作为新增 canonical 零。

在原反次序 trace 中，(21) 允许先取完整三支 trace：
$Z_\delta$ 是这一层的 base 参数；
随后仍保原十三支的 $\widetilde v^p$、全部字符及其相位。
这样只剩两个固定的加权三支 trace 与一次真实 $Z_\delta$ 测试。
不得把 $Z_\delta$ 未经原十三处 cocycle 直接改成最终 $Z$。


### 6.1 三个字的完整固定系数与同一个原单极 primitive

为免混淆，本小节用 $(x_0,y_0)$ 表示 $\delta$ target，
$X_0=x_0^3$、$h=1-y_0$，并保持 R1022 的原
$\kappa^3=h$ 规范。上述两个 source 函数的全三字为
$$
\begin{aligned}
A_\delta&=
\frac{X_0+2-x_0(y_0+1)\kappa+x_0^2\kappa^2}{3y_0^2},\\
B_\delta&=
\frac{c_p}{3y_0}
 \left(-x_0+\frac{x_0^2}{1-y_0}\kappa+\kappa^2\right).
\end{aligned}
\tag{21a}
$$
可从原
$x_{\rm up}/y_{\rm up}=-2\kappa/[\delta(\kappa^2+x_0)]$
及
$$
(\kappa^2+x_0)^{-1}
=\frac{x_0^2-x_0\kappa^2+h\kappa}{-2y_0h}
$$
直接逐列核对，不需要选择新的三次根。

令 $r_{0,\delta}=x_0^2/y_0$。
(21a) 的三个系数分别严格给
$$
A_\delta=\frac23+\rho_p r_{0,\delta}B_\delta.
$$
因此
$$
\boxed{
W_\infty=\frac23+B_\delta^p F_{p,\delta},\qquad
F_{p,\delta}=Z_\delta+\rho_p r_{0,\delta}^{\,p}.
}
\tag{21b}
$$
$F_p$ 正是 R887 §7(31)–(34) 已付的原单极 primitive；
其 $DF_p=1$、全部二挠主部抵消以及
$F_p=xy\,P(X)$ 的完整多项式规范继续沿用。
它在 $O$ 有真实 $p$ 阶极，不能被当成无极的全纯 primitive。

若 $B_\delta=B_0+B_1\kappa+B_2\kappa^2$，
则 $p=6s-1$ 给
$\kappa^p=h^{2s-1}\kappa^2$、
$\kappa^{2p}=h^{4s-1}\kappa$。
故原三个字完整为
$$
\boxed{
g_{0,\infty}=\frac23+B_0^pF_{p,\delta},\qquad
g_{1,\infty}=h^{4s-1}B_2^pF_{p,\delta},\qquad
g_{2,\infty}=h^{2s-1}B_1^pF_{p,\delta}.
}
\tag{21c}
$$
正三支仍是 R1022 的原 mode2，不能误改成 mode1。
实际 trace 的 $h^{e_i}$、全部 $h_i$、十三字符及其标准化
外部平移仍与 (21c) 一起使用。
式 (10) 的余项也未消失；(21c) 描述的是经第5节支付的
共同低窗权本身。


## 7. 与原 Lamé 源相接的一个准确单位曲率

R1021 §8 的实际低层 $f=U_B=xy$ 满足
$D^2f=30xf$。
本篇另付这一连接的完整非零 nilpotent 项。
全函数恒等式
$$
\boxed{
\frac{\omega_E}{f^2}
=-\frac12d(1/f)-\frac52\frac{x\omega_E}{y^2}
}
\tag{22}
$$
结合原 $C(-3x\omega_E/(c_py^2))=\omega_E$，给
$$
\boxed{
C(\omega_E/f^2)=\kappa_p\omega_E,\qquad
\kappa_p=\frac{5c_p}{6}\in\mathbf F_p^\times.
}
\tag{23}
$$
原 $f$ 在 $O,\pm S,\mathcal D_2$ 的全部零极均已包含在 (22)；
在 $\pm S$ 的极属于显示的 exact 项，没有漏删。

对任意实际 torsion 平移 $R$，取 $f_R=f\circ t_R$。
Cartier 与平移交织，所以 (23) 的标量在全部这些词中完全相同。
写 Lamé 变量 $Y=f_Rv$、$w=f_R^2Dv$，
其连接成为
$$
D\binom vw-
\begin{pmatrix}0&f_R^{-2}\\0&0\end{pmatrix}\binom vw.
$$
令 $E_{12}^2=0$，从
$D^{p-1}(f_R^{-2})=-\kappa_p$ 得
$$
\boxed{
(D-f_R^{-2}E_{12})^p=\kappa_pE_{12}.
}
\tag{24}
$$
本式明确采用 $D-A$ 的连接符号。

与同一个原 $L=D-10G$ 张量后，
所有交叉项在共同上三角 gauge 中精确给
$$
\boxed{
(L-f_R^{-2}E_{12})^p
=-10\mathcal H^p I+\kappa_pE_{12}.
}
\tag{25}
$$
这保留原 scalar 曲率和非零 nilpotent 项。
原完整 Miller 的可逆 rank1 gauge 只共轭这个矩阵；
它不将任一项设为零。
在函数域中还可准确写逆
$$
(-10\mathcal H^p I+\kappa_pE_{12})^{-1}
=-\frac1{10\mathcal H^p}I
-\frac{\kappa_p}{100\mathcal H^{2p}}E_{12}.
$$
这是可继续与 (20) 的两个原 primitive 测试联立的固定二阶输入，
不是从单位曲率直接推出 canonical 导数非零。


### 7.1 同一个实际单极因子的完整四阶交换子

在同一实际 $S_{10}$ 坐标中，设 $F=F_p$；
逐个标准化词若带平移，则同时使用它的真实平移。
这些 $F$ 都满足 $DF=1$。
令
$$
\mathcal O=D^4-54xD^2,\qquad
\mathcal O_L=L^4-54xL^2,\qquad
e=LP_{10}=10\mathcal H^pZ^{p+9}.
$$
R1021 的整个源端关系给
$$
\mathcal O(FU_B)-60FU_A
=(4D^3-108xD)U_B
=R,\qquad R=12x(25X+22).
\tag{25a}
$$
同一关系的完整 $P_{10}$ 费用是
$$
\boxed{
[\mathcal O_L,F](P_{10}U_B)
=P_{10}R+(4L^2e+252xe)U_B+12(Le)DU_B.
}
\tag{25b}
$$
它由 $[L,F]=1$ 和完整 Leibniz 式直接得到；
特别保留了全部 $e$ 项，不能只留 $P_{10}R$。

该真实裸交换子还具有显示的非零 Cartier 返回：
$$
uR\omega_E=100y\,dy-12\,d\log y,\qquad
C(uR\omega_E)=-12\,d\log y.
\tag{25c}
$$
这是原交换子的准确单位对数方向。
它并未删除 (25b) 的 $P_{10}$、$\mathcal H$ 与原全部字权；
尤其 R887 §20 的 $C(\mathcal H\omega_E)=0$
不能被误用为对任意乘积的零。
后继应将 (25b) 整体放入 (20)–(21c) 的实际测试，
而非只搬运 (25c) 的留数。


## 8. 与已付曲率非零及算术行的准确连接

R1025 §12 的实际特征零系数在末六个参数中至少有一条为单位；
§12.4 的末两条实际特征零系数更满足固定组合
$\lambda_1-(10/81)\lambda_2$ 为全部目标素数上的单位。
本篇给它们同一 $K$、同一十三处乘子、
同一个 target 截面，以及固定的全部第一 primitive 测试。

原两条新 rank2 来源的实际算子身份仍是
R1021 §8 的整个 $\chi_8$ 加权像；
其中央零来自真实 canonical 来源与原 parity。
本篇没有把单个十三字、两项固定三支 trace、
一个新乘子或 (25) 的 Jordan 分量另外赋零。
后继消元须在 (20)–(21) 的完整测试中保留原
$P_{10}$ 曲率、$GP_{10}$ 与全部外部平移，
并按 R1026 的原特征零权支付高精度费用。

全部结果为手证，未运行本地数学、未新增素数扫描。

## 9. 提高精度后，原四阶 cut 仍看不到六个 T_t 余项

追加日期：2026-11-28 UTC。R1026 §9 已将同一个特征零比较
提高到 $p^{H_t+1}$，其中 $H_t=p-6t$。不能仅将第5节的统一
$p-36$ 界与这个新精度比较，就声称末端出现新独立行。
逐个保留原 $T_t$ 的准确极帽后，整个真正 native 三角窗仍不读该余项。

### 9.1 完整原权差在全部三十九处的消失阶

沿(12)–(14)，保持
$A=u(v_\pi\circ[\delta])$ 及同一个完整 source $R_f$、
十三字、Miller 相位和外部位置。
把原三处约化权 $W_t^p$ 与共同 $W_\infty^p$ 比较，
整个 source 权差准确为
$$
\boxed{
\Delta V_t=c_pA^{p^2}T_t^p.
}
\tag{26}
$$
这只是(10)乘回同一个十三处权，不改变特征零 $V_t$。

在每个 $R\in\ker[\alpha]$，$A$ 有一次零；
$T_t$ 只在 $\ker[\delta]$ 的三点可能有极，帽为 $6t-1$。
因此在全部三十九点统一有
$$
\boxed{
\operatorname{ord}_R\Delta V_t
\ge p^2-p(6t-1)=p(H_t+1).
}
\tag{27}
$$
在其它三十六点还可加强；以下不删除它们，只使用统一界。

令 $q=[\alpha]^*Z$ 为各点的真实局部参数。
因为 $[\alpha]$ 为 étale 且 $Z$ 在 target $O$ 为参数，
在每条完成局部纤维中都可使用同一个 target $q$；
没有以 source 的另一个平坦截面代替它。
(27)在此参数中保持。

### 9.2 实际 cut 与完整 native 窗

先取本篇已经支付的真实至多四阶 adjoint cut。
第5.1节的同一点计算给完整
$\vartheta_b^{\rm cut}$ 的极帽 $b+1+c$，$0\le c\le4$；
这里 $c$ 记录已经支付的局部耗费，
不对任意微分或乘子新增 canonical 零。

对 $n=rp+b$，$0\le b<p$，读取 native 系数时在 source
再乘 $q^{-rp}$。在特征 $p$ 中 $d(q^{-rp})=0$，
所以这一步与同一个实际有限 cut 相容；
完整微分的极帽是 $n+1+c$。
于是(26)给
$$
\operatorname{ord}_R
 \bigl(\Delta V_t\,\vartheta_n^{\rm cut}\bigr)
\ge p(H_t+1)-n-1-c.
\tag{28}
$$
所有原常数、未平均 trace 和半线性尺度都保留；
极帽不将其中某一字的值赋零。

若 $n\le(p+1)H_t$，则右边至少为
$6t-1-c\ge1$，因此每条原纤维的微分都正则，
在该点的留数为零。完整 trace 与留数交织，
所以这一差对全部真正 native 系数都不贡献：
$$
\boxed{
\Delta t_n^{\rm cut}=0
\quad
(0\le n\le(p+1)H_t,\ 1\le t\le6,\ 0\le c\le4).
}
\tag{29}
$$
这里 $\Delta t_n^{\rm cut}$ 指同一个原有限测试中的差；
未施 cut 时就是
$t_n^{10}(A_t)-t_n^{10}(A_\infty)$。
$A_\infty$ 仅表示上述完整特征 $p$ 权的有限 trace，
不是新增的特征零 canonical 来源。
所有三十九支都分别有(28)，故没有利用未付的纤维间抵消。

### 9.3 同一个第一 primitive 的核对与真实阈值

也可直接在第5节已经固定的 primitive 类中检查。
第一次 Cartier 的准确极帽是
$$
\operatorname{pole}_R\nu_b^{\rm cut}
\le1+\left\lfloor\frac{b+c}{p}\right\rfloor.
$$
当前 $c\le4$，括号只可能为零或一。
因为 $6t+1\le37<p$，乘 $T_t$ 后再作 Cartier，
在核点至多留下 simple 极。
原 target 截面的实际拉回从 $p-1$ 阶起，
所以该截面项至多 simple；它不改变负次数至少二的主部。
同一 primitive 因而可取局部极帽
$$
6t-1+\left\lfloor\frac{b+c}{p}\right\rfloor.
$$
乘 $A^p$ 并取完整 trace 后，所有非 $p$ 次幂系数至少从
$$
r=H_t+1-\left\lfloor\frac{b+c}{p}\right\rfloor
\tag{30}
$$
起。局部 primitive 的 $F^p$ 歧义仍只给 target 的 $p$ 次函数，
不影响当前 $0<r<p$。

若想在 $r\le H_t$ 中读到该差，(30)强迫
$r=H_t$、$b+c\ge p$。
但 native 三角 $rp+b\le(p+1)H_t$ 又强迫 $b\le H_t$，
从而必须 $c\ge6t$。原 $c\le4$ 不可能满足。
这与直接全纤维留数证明(28)–(29)一致，
也保了原点留数、第二 Cartier 截面和同一个第一 primitive。

更一般，若另一个**真正已授权**的 cut 在全部原点位满足
同样的局部耗费 $c<6t$，(28)仍给正则微分和同样的零差；
这不是授权使用该新 cut。
当 $c=6,t=1$ 时，估计首次只准留下
$n=(p+1)(p-6)$ 的一个端点候选。
其实际最高系数仍可能为零；
某个任意 $D^6$、环境六阶矩或另一个 charge 不支付该候选。
必须先证明原 canonical 来源、完整投影及全部其它极
确实给出相应 cut，才可计算它。

### 9.4 对实际中央求和的范围

(29)是同一特征 $p$ 完整有限读者的精确等式。
R1034(22)的物理矩阵、所有 native 系数的高 $p$ 位、
两个真实 Gaussian 及原 Newton 阶乘仍必须按原式消费。
它不把整个特征零 $V_t$ 换为 $W_\infty^p$，
也不把一个中央 Newton 和为零拆成每个系数为零。

因此 R1026 §9 的精度加强可以使用，
但在原已经支付的四阶读者内，它没有使
$T_2-T_1,\ldots,T_6-T_1$ 成为新增 canonical 约束。
后继所需的是实际更高耗费且有算术授权的来源关系，
或另外完整的非零比较；单纯扩大截断精度不填这个门。
