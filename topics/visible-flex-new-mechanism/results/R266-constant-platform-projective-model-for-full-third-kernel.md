# R266：全第三核在常平台上的三维射影模型与真实二次尾

日期：2026-11-15。**完整纸面证明；没有新研究计算、人工执行或旧目标重跑。** 本稿准确计算 $Z=\mathfrak H_7\oplus\mathfrak J_3\oplus\chi_8$ 的局部源在非零常平台上的全部像，并把它接到 R264 的真实尾矩。局部源的三维像不等于完整 $K$ 的像，后者仍保原右锚决定的二次尾。

来源：[R258](R258-self-adjoint-hook-green-operator-and-complete-period-interface.md)、[R260](R260-actual-activity-flux-green-boundary-and-step-baseline.md)、[R261](R261-eight-local-self-adjoint-hook-operators-and-full-third-kernel.md)、[R264](R264-potential-tail-moments-and-complete-platform-flux-equivalence.md)。

## 1. 正确的有限射影作用

记 $D=d/dx$，原 $\delta$ 链的生成元及其形式伴随为

$$
Z=x^2D-2x,\qquad Z^*=-x^2D-4x.
\tag{1}
$$

沿用未除阶乘的链规范

$$
\mathfrak H_\ell=\delta^\ell\mathfrak H
\quad(0\le\ell\le6),\qquad
\mathfrak J_\ell=\delta^\ell\mathfrak J
\quad(0\le\ell\le2).
\tag{2}
$$

对 $D^3K_f^\tau=\mathscr A_f^\tau$，R258 的准确微分作用是

$$
\mathscr A_f^{\delta\tau}
=-Z^*\mathscr A_f^\tau-\mathscr A_f^\tau Z
-D_f\mathscr A_f^\tau[Zf].
\tag{3}
$$

最后的 seed 导数不可漏掉。两个有限流为

$$
\rho_tu(y):=e^{-tZ}u(y)
=(1+ty)^2u\!\left(\frac y{1+ty}\right),
$$

$$
e^{-tZ^*}v(x)
=(1-tx)^{-4}v\!\left(\frac x{1-tx}\right).
\tag{4}
$$

直接对 $t$ 微分并用流的群性质，(3) 积分成

$$
\boxed{
\mathscr A_f^{e^{t\delta}\tau}
=e^{-tZ^*}\,\mathscr A_{\rho_tf}^\tau\,e^{-tZ}.}
\tag{5}
$$

以下在 $f=F$ 的一个真实开放常平台上作局部计算。取足够小的 $t$，射影坐标仍落在这个平台；因此只消费原 $f$ 的局部常值 jets。没有把一个全局非紧支撑常函数当作合法新 seed，也不移动原积分锚。

置 $A=1+ty$、$z=y/A$。在该局部图中 $\rho_t f=FA^2$。对任意输入 $w$，逐次乘法求导给

$$
D_y^3(\rho_tw)=A^{-4}w'''(z),\qquad
D_y^4(\rho_tw)=A^{-6}w^{(4)}(z)-4tA^{-5}w'''(z).
\tag{6}
$$

这些式子保留输入的全部低阶项直到准确相消；不假定 $w$ 本身为多项式。

## 2. 七维 H 链的完整平台表

H 根的已付源是

$$
\mathscr A_f^{\mathfrak H}
=D^2\!\left[(6f'f'''-2(f'')^2)D^2\right]
-D\!\left[6(f''f''')'D\right].
\tag{7}
$$

对 $f(y)=F(1+ty)^2$，有 $f''=2Ft^2$、$f'''=0$，所以

$$
\mathscr A_{\rho_tf}^{\mathfrak H}=-8F^2t^4D_y^4.
\tag{8}
$$

把 (6)、(8) 代 (5)，外射影点满足
$y=x/(1-tx)$、$A=(1-tx)^{-1}$、$z=x$，得到完整有限式

$$
\boxed{
\mathscr A_F^{e^{t\delta}\mathfrak H}
=-8F^2t^4\{(1-tx)^2D^4-4t(1-tx)D^3\}.}
\tag{9}
$$

由 $e^{t\delta}\mathfrak H=\sum t^\ell\mathfrak H_\ell/\ell!$，必须把多项式系数乘回阶乘。因此

| 方向 | 常平台上的完整局部源 |
|---|---|
| $\mathfrak H_0,\mathfrak H_1,\mathfrak H_2,\mathfrak H_3$ | $0$ |
| $\mathfrak H_4$ | $-192F^2D^4$ |
| $\mathfrak H_5$ | $1920F^2(xD^4+2D^3)$ |
| $\mathfrak H_6$ | $-5760F^2(x^2D^4+4xD^3)$ |

式 (9) 的最高次数为六，与原七维链相合；这只是已有链在平台上的准确限制，不从局部表反推整个算子在别处为零。

## 3. 三维 J 链的完整平台表

J 根的自伴系数按 R258 为

$$
\begin{aligned}
a&=-4\{(f')^2+ff''\},\\
b&=12(f'')^2+8f'f'''-4ff^{(4)},\\
c&=8(f''')^2+12f''f^{(4)}+4f'f^{(5)}.
\end{aligned}
\tag{10}
$$

最后一项是 $4f'f^{(5)}$，不是 $4ff^{(5)}$。完整源是
$\mathscr A=D^2(aD^2)+D(bD)+c$。

对 $\rho_tf=FA^2$，

$$
a=-24F^2t^2A^2,\qquad b=48F^2t^4,\qquad c=0,
\qquad a''+b=0.
$$

因此

$$
\mathscr A_{\rho_tf}^{\mathfrak J}
=-24F^2t^2\{A^2D_y^4+4tA D_y^3\}.
\tag{11}
$$

把 (6) 代入大括号，两项 $D^3$ 准确相消；再应用 (5) 的外因子，得到

$$
\boxed{\mathscr A_F^{e^{t\delta}\mathfrak J}
=-24F^2t^2D^4.}
\tag{12}
$$

同样乘回链阶乘，

$$
\boxed{
\mathscr A_F^{\mathfrak J_0}=
\mathscr A_F^{\mathfrak J_1}=0,\qquad
\mathscr A_F^{\mathfrak J_2}=-48F^2D^4.}
\tag{13}
$$

## 4. 八个额外方向与全 Z 的三维平台像

R261 已在真实完整原式上证明：常平台只有

$$
\mathscr A_F^{\chi_{104}}=\frac38F^2D^4
=-\frac1{512}\mathscr A_F^{\mathfrak H_4},
\tag{14}
$$

其余七个 $\chi_{30},\chi_{32},\chi_{34},\chi_{37},
\chi_{40},\chi_{100},\chi_{109}$ 的局部源为零。这里直接消费该已付实际结论，不重跑原式或人工。

结合 (9)、(13)、(14)，对任意 $\tau\in Z$，存在唯一二次以下多项式

$$
P_\tau(x)=\alpha_\tau+\beta_\tau x+\gamma_\tau x^2
$$

使该常平台上

$$
\boxed{
\mathscr A_F^\tau
=F^2\{P_\tau D^4+2P_\tau'D^3\}.}
\tag{15}
$$

当 $F\ne0$，H 的后三行给 $1,x,x^2$ 三个独立 leading 系数，所以整个开放平台上的算子函数像准确为三维。若 $F=0$，局部源像为零。

这不否定 R261 的十八维 universal 忠实表示：后者允许任意合法 $f$，这里把 $f$ 限制在一个常平台。也不能由某方向在 (15) 为零推断其完整 $K$ 在该平台为零。

从自伴形式看，(15) 等价于

$$
a=F^2P_\tau,\qquad b=-F^2P_\tau'',\qquad c=0
\quad\text{在该平台上}.
\tag{16}
$$

$c=0$ 只说平台本地；右侧活动区间的 $c$ 通常非零，真实 $\mathcal J(cw)$ 不能因此删去。

## 5. 完整 K 必须附上原右锚决定的二次尾

因为 $P_\tau'''=0$，直接求导给

$$
D^3(P_\tau w'-P_\tau'w)
=P_\tau w^{(4)}+2P_\tau'w'''.
\tag{17}
$$

于是完整 $K_f^\tau(w)$ 在每个常平台上准确写为

$$
\boxed{
K_f^\tau(w)=F^2(P_\tau w'-P_\tau'w)+Q_{\tau,w}(x),
\qquad \deg Q_{\tau,w}\le2.}
\tag{18}
$$

$Q_{\tau,w}$ 由整个实际 $f,w$、原右锚及右侧所有活动共同决定，不能自由指定或在每个平台重置。

R264 已证明

$$
K_f^\tau(w)''
=(aw'')'+bw'-T,\qquad
T=\left.\mathcal J(cw)\right|_{\rm platform}.
$$

结合 (16)–(18) 得

$$
\boxed{
K_f^\tau(w)''
=F^2(P_\tau w'''+P_\tau'w''-P_\tau''w')-T,
\qquad Q_{\tau,w}''=-T.}
\tag{19}
$$

$T$ 在平台上为常数，且是原右侧活动势矩之和。若选平台内一点 $x_0$，可更明确写为

$$
Q_{\tau,w}(x)=q_0+q_1(x-x_0)-\frac T2(x-x_0)^2,
\tag{20}
$$

其中

$$
q_0=K(x_0)-F^2(P_\tau w'-P_\tau'w)(x_0),
$$

$$
q_1=K'(x_0)-F^2(P_\tau w''-P_\tau''w)(x_0).
$$

$q_0,q_1$ 也是原 $K$ 的真实读数，不是额外 gauge。即使 (15) 的局部源完全为零，(20) 仍可能是非零二次尾。

## 6. 与 R264 联合条件的准确衔接

在 R264 的有限活动类上，全部活动总通量为零已强迫每个非零常平台 $T=0$。再要求该平台 $K''=0$，其剩余门准确变为

$$
\boxed{
P_\tau w'''+P_\tau'w''-P_\tau''w'=0.}
\tag{21}
$$

全部平台与总通量同时成立，仍须 R264 的各活动势矩为零；不能只在某个非零平台使用 (21) 而漏掉零平台的真尾。

若已由原式证明输入在所研究平台确为二次多项式

$$
w=A_2x^2+A_1x+A_0,
$$

则 (19) 简化成

$$
\boxed{
K''=2F^2(\beta_\tau A_2-\gamma_\tau A_1)-T.}
\tag{22}
$$

$P_\tau$ 的常数项与 $w$ 的常数项不进入这个平台二导条件。只有在 $T=0$ 已支付时，才可把 (22) 化成 $\beta_\tau A_2-\gamma_\tau A_1=0$。

“$f$ 在平台为常数”不保证 $\Phi_E(f^2-g^2)$ 或 $\Phi_E(fg)$ 在那里为二次：若 $g$ 正在变化，完整 $\Phi_E$ 仍有局部源。使用 (22) 前必须从实际输入证明二次性，不能由 $f$ 一项冻结就推断。

有限控制组合按线性性使用各方向的 (19) 总和；允许平台微分项和势尾相互抵消，不把总条件加强成每项分别零。

## 7. 完整 mixed 与尚未付的部分

原 mixed 仍须保

$$
D=2K_f^\tau\!\left(\Phi_E(f^2-g^2)\right)
+4\Phi_E(g,\zeta),
$$

$$
E=-4K_f^\tau\!\left(\Phi_E(fg)\right)
+4\Phi_E(f,\zeta),\qquad \zeta=K_f^\tau(g).
\tag{23}
$$

本文只精确化其中的 K 项。除非另有完整 $\zeta=0$ 证明，第二 history 项仍参与平台和通量条件；采用 $2\cos\theta\sin\theta$ 规范时 E 列仍须除二。

本稿已经支付全 Z 的常平台局部像、全部 H/J 阶乘系数、八额外方向的精确从属，以及完整 K 的真实二次尾模型。它没有给出固定圆完整 period 的秩或满射，没有消掉 R225 的内部 Laurent/两平端 germ，也没有扩大真实可实现带符号成本、删除全 $\mathcal R_{p0}$ 的其余项或解出同一二阶校正的第四 ruling。

本文件由已核数学关系重新编辑；终端断连前的临时稿字节没有恢复，故没有沿用其旧字节数或摘要。全部结论来自以上有限纸面微分和已付 R261，不含新的科学执行。
