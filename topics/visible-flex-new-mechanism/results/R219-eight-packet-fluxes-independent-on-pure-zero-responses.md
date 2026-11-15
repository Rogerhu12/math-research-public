# R219：八 packet 的修正退化通量在 pure-zero 响应上独立

日期：2026-11-15。**完整纸面证明；没有新增研究计算。**

[R217](R217-two-left-tail-invariants-independent-on-pure-zero-responses.md) 排除了由两个左二次尾标量联合读出 $\lambda_+$。本稿再给一个真正包含多个局部退化点与平台信息的固定圆不变量组：在原 R183 的八个完整 packet 中，各取一个退化通量，并减去一个准确的平台二阶导数项。这八个读出都杀掉全部允许的二阶 hook gauge；它们在 universal pure-zero 响应空间上满射到 $\mathbb R^8$。

独立性来自同一真实响应的前八个代数导子及一个准确 Vandermonde 行列式。原八包、原三矩补偿、原七阶有限差分均保持；没有重新选择 profile 采样或增加研究计算。

这排除 $\lambda_+$ 经该八元组因子化。另有一个包含 R217 两左尾的三元组也已满射。**本文不把这两项结论合并成十元组满射，更没有证明全部 fixed-circle joint 观测都不能读出 $\lambda_+$。**

## 1. 固定同一个合法圆与每包退化点

使用 R217 第 5 节选定的 R183 合法三矩圆。它由同一个完整基本 pair $(f_*,g_*)$ 的八个不交等距平移组成：

$$
f(x)=\sum_{j=0}^7 a_j f_*(x-t_j),\qquad
g(x)=\sum_{j=0}^7 a_j g_*(x-t_j),\qquad
a_j=(-1)^j\binom7j^{1/3}.
\tag{1}
$$

共同正幅度可以吸收进基本 pair，最终正仿射 profile 坐标亦先固定。后文所有算子都在这个最终 x 坐标中定义。

基本 pair 的第一个原矩形 f 上升导数包，按 R215 选

$$
p_*=f_*'>0\quad\text{于 }(a,b),\qquad
q_*=f_*'',\qquad
A_*=6p_*q_*'-2q_*^2.
$$

这里 a 是三左矩补偿之后、第一次 f 上升导数包的平端左端点；在其左侧留开放零 profile 区间。R215 的 $p_*^{2/3}$ 最大斜率论证给内部点 $x_*$，满足

$$
A_*(x_*)=0,\qquad p_*(x_*)>0,\qquad q_*(x_*)>0.
\tag{2}
$$

定义

$$a_j^\circ=a+t_j,\qquad x_j^\circ=x_*+t_j.$$

这些点不与幅度 $a_j$ 混用。全 f 在每个区间
$[a_j^\circ,x_j^\circ]$ 上就是 $a_j f_*(x-t_j)$，所以

$$
A_f(x_j^\circ)=0,\qquad
f'=f''=f'''=0\quad\text{在 }a_j^\circ.
\tag{3}
$$

点 $a_j^\circ$ 的各阶 jet 与其左侧零平台相同。符号为负的 $a_j$ 不影响 A 的零点。全部二、三阶 range 由 R183 原构造支付；本稿不改变八包的幅度或完整包的右锚。

对 $V\in U_{\mathrm p0}=U\cap\ker\pi$，记
$V_d(x)=V(f^2,g)(x)$，即 R213 的 $s^2$ 系数。定义八个线性读出

$$
\boxed{\begin{aligned}
\mathcal F_j(V)={}&
\int_{a_j^\circ}^{x_j^\circ}f'(x)V_d''(x)\,dx\\
&-\bigl(f(x_j^\circ)-f(a_j^\circ)\bigr)V_d''(a_j^\circ),
\qquad 0\le j\le7.
\end{aligned}}
\tag{4}
$$

第二项是真实内部平台二阶导数的端值，不是把所有右尾或输入 history 置零。

## 2. 八个读出均对全部允许的 gauge 不变

R181 的准确通量身份是

$$
f'L_f(w)''
=\partial_x\{A_f(f'w''-f''w')\}.
\tag{5}
$$

由 (3)，(5) 在 (4) 积分两端的边项都为零，且
$L_f(w)''(a_j^\circ)=0$。后一个等式直接用 R181 的局部二阶导数式及 f 在该点的平端 jets。因此对任意全 I 光滑 w，

$$
\boxed{\mathcal F_j(L_f(w))=0,\qquad 0\le j\le7.}
\tag{6}
$$

这里沿用记号表示把 (4) 直接作用于单个输出函数。没有把 w 限定在本 packet 内；它可以有全部允许的外部支撑和右尾。

实际 hook 的二阶 gauge 改变 period 为 $2\kappa L_f(w_\theta)$。取 $\theta=\pi/2$ 即得 (6) 对 $V_d$ 的完整不变性。$M=0$ 下第三 gauge 不改 period。因此

$$\mathcal F_j(V)=0\quad(0\le j\le7)\tag{7}$$

是同一固定几何、同一圆的完整第四 period 可解的必要门。本文不把这八条必要门视为充分条件。

## 3. 起始响应的一层右积分结构

采用 R215/R217 的

$$
P(a,b)=J(a''b''),\quad
R(a,b)=a'b'+xJ(a''b''),\quad
K=K_{P,[P,R]},
\qquad J(F)(x)=\int_x^rF.
\tag{8}
$$

已知 $K\in\mathcal R_{\mathrm p0}$。R217 的代数导子

$$\mathscr D=x^2\partial_x-2x,\qquad
\delta A=\mathscr D_{\rm out}A-\sum A(\ldots,\mathscr D_{\rm in},\ldots)
\tag{9}$$

保 E8 及 R71 交换子响应，所以每个有限次 $\delta^nK$ 都属于
$\mathcal R_{\mathrm p0}$。

本节还需要一个更具体的结构：

**引理。** 每个 $\delta^nK$ 可写成局部四次微分多项式，以及有限个
$c(x)J(F)$ 的和；每个 F 是同一点输入 jets 的四次多项式，没有嵌套右原函数。其左尾次数至多二。

**证明。** 从 R217 的

$$
[P,R](a;b,c)
=a'b''c''+
J\{a''(b'''c'+b'c''')+(x-\eta)a''(b''c'')'\}
\tag{10}
$$

看 R83 响应的三个项。设 $d_2=(f'')^2-(\phi'')^2$：

- 第一项外槽 $PD=J(d_2)$ 在 (10) 中只以一、二阶导数出现，这些导数已经局部；
- 第二项内槽 $PD$ 也只以正阶导数出现，所以仍只有一层 J；
- 第三项 $P(\phi,[P,R](\phi;D))$ 只使用内层的二阶导数。(10) 的二阶导数完全局部：$J(F)$ 两次微分是局部项，$xJ(G)-J(\eta G)$ 也在两次微分后局部化。

因此 K 具有所述结构。对局部项施 (9) 仍局部；对 $c(x)J(F)$ 施 (9)，输出导数及输入变分仍只产生局部项或单层 J，不会新增嵌套。四次齐次性也保留。

K 的左尾至多仿射，见 R217(15)–(17)。若左尾为二次多项式 b，$\mathscr Db$ 仍至多二次，因为
$\mathscr D(x^2)=0$；输入变分只改变系数。归纳完成。$\square$

这一引理**只用于本稿的响应模**。不把一般完整成本 U、一般第四恢复或逐 ruling forcing 声称为单层右积分。

由引理及完整 packet 的值支撑不交，对 $A=\delta^nK$ 有准确分解

$$
A(f^2,g)=\sum_{j=0}^7a_j^4
A(f_*^2(\,\cdot-t_j),g_*(\,\cdot-t_j)).
\tag{11}
$$

它是对局部四次密度及其单层 J 的分解，不是凭“导数分包”丢掉原本存在的嵌套历史。K 的全部真实历史已经在 R83 完整响应和 (10) 中支付。

## 4. 平台修正准确消掉其他 packet 的尾

对一个单独基本 pair，定义

$$
\mathcal F_*(A)
=\int_a^{x_*}p_*(x)\,[A(f_*^2,g_*)]''(x)\,dx
-\bigl(f_*(x_*)-f_*(a)\bigr)[A(f_*^2,g_*)]''(a).
\tag{12}
$$

设 $\mathcal T_t$ 是算子在平移输入后搬回基本坐标的原式：

$$
(\mathcal T_tA)(f,\phi)(y)
=A(f(\,\cdot-t)^2,\phi(\,\cdot-t))(y+t).
\tag{13}
$$

右锚随表达式的真实变量换元处理；profiles 在两锚之间全零，因此这只是同一个零右尾原函数的准确平移身份，不产生新的积分常数。

在第 j 个 packet 的 (4) 中：

- 所有左方完整 packet 的输出已在其右侧为零；
- 所有右方完整 packet 在该整个区间上只留下二次多项式尾，故二阶导数为常数；
- (4) 的第二项逐个准确消掉这些常数贡献。

因此 (11) 给

$$
\boxed{
\mathcal F_j(\delta^nK)
=a_j^5\,\mathcal F_*(\mathcal T_{t_j}\delta^nK).
}
\tag{14}
$$

第五次幅度来自输出的四次齐次性和读出中的一个 $f'$（或 f 值差）。这里没有声称一般 U 也满足 (11) 或 (14)。

对于 n=0，R215 的原式
$K=-q^2(q^2-z^2)/3-2L_f(PD)/3$
适用于这个导数分包基本 pair。因此在 a 的平端 jets 上直接有
$[K(f_*^2,g_*)]''(a)=0$，(12) 的平台修正为零。
这一步未要求全部右尾为零。R215 的局部原式和退化通量计算给

$$
\boxed{
\mathcal F_*(K)=-\frac8{45}q_*(x_*)^5\ne0.
}
\tag{15}
$$

右方仍存在的 g 和 f 下降包完整保留在 K 中；(15) 正是 R215 对全 I 右尾已经证明的身份。

## 5. 八列的 Vandermonde 独立性

对任意 unary profile 微分算子 X，记
$\mathscr L_XA=X_{\rm out}A-\sum A(\ldots,X_{\rm in},\ldots)$。
这是算子组合代数上的导子，满足

$$[\mathscr L_X,\mathscr L_Y]=\mathscr L_{[X,Y]}.$$

令

$$
\mathcal N=\mathscr L_{\partial_x},\qquad
\mathcal H=\mathscr L_{x\partial_x-1},\qquad
\delta=\mathscr L_{x^2\partial_x-2x}.
$$

直接 unary 交换子给

$$
[\mathcal N,\delta]=2\mathcal H,\qquad
[\mathcal H,\delta]=\delta.
\tag{16}
$$

P 平移不变，而 $\mathcal NR=P$；因此
$\mathcal N[P,R]=[P,P]=0$，进而

$$\mathcal NK=0.$$

此外 $\mathcal HP=-2P$、$\mathcal HR=-R$；组合 Leibniz 法则给

$$
\mathcal H[P,R]=-3[P,R],\qquad
\mathcal HK=-5K.
\tag{17}
$$

这些是完整原算子恒等式，未把有限维表示猜测作为前提。

由 (16)–(17) 归纳：

$$
\boxed{\mathcal N\delta^nK=n(n-11)\delta^{n-1}K.}
\tag{18}
$$

所有算子的 x 系数都是多项式，故 (13) 的实际平移在这个有限串上是有限 Taylor 和
$\mathcal T_t=e^{t\mathcal N}$。于是

$$
\mathcal F_*(\mathcal T_t\delta^nK)=P_n(t)
\tag{19}
$$

是一个次数恰为 n 的实多项式，且当 $0\le n\le7$ 时其最高系数为

$$
\boxed{
[t^n]P_n(t)
=(-1)^n\frac{10!}{(10-n)!}\,\mathcal F_*(K)\ne0.
}
\tag{20}
$$

式 (20) 的 n! 来自 Taylor 分母，准确约掉 (18) 连乘中的
$1\cdot2\cdots n$。

八个 $t_j$ 互异，故 (14) 的八行八列矩阵满足

$$
\begin{aligned}
\det\bigl[\mathcal F_j(\delta^nK)\bigr]_{j,n=0}^7
={}&
\left(\prod_{j=0}^7a_j^5\right)
\left(\prod_{n=0}^7
(-1)^n\frac{10!}{(10-n)!}\mathcal F_*(K)\right)\\
&\hspace{8mm}\cdot\prod_{0\le i<j\le7}(t_j-t_i)\ne0.
\end{aligned}
\tag{21}
$$

于是得到真实函数结论

$$
\boxed{
(\mathcal F_0,\ldots,\mathcal F_7)(\mathcal R_{\mathrm p0})
=\mathbb R^8.
}
\tag{22}
$$

这里只用了八个响应 $\delta^nK,\ 0\le n\le7$；没有新求真实 U 或 R 的秩，也没有利用不完备正规形的非零余项宣告函数独立。

## 6. 正字符的八元组与三元组因子化均失败

R196 的 $\lambda_+$ 杀 $\mathcal R$；R201 的完整
$H\in U_{\mathrm p0}$ 满足 $\lambda_+(H)=1$。
由 (22)，任何消掉 $\mathcal R_{\mathrm p0}$ 的八元组线性组合都为零。故

$$
\boxed{
\lambda_+|_{U_{\mathrm p0}}
\ne \ell\circ(\mathcal F_0,\ldots,\mathcal F_7)
\quad\text{对每个 }\ell\in(\mathbb R^8)^*.
}
\tag{23}
$$

等价地，由可逆矩阵 (21)，可唯一选八个实数 $c_n$ 使

$$H^\sharp=H-\sum_{n=0}^7c_n\delta^nK$$

满足全部 $\mathcal F_j(H^\sharp)=0$，但
$\pi H^\sharp=0$、$\lambda_+(H^\sharp)=1$。这仍只是 U 内的线性空间反例，不把有符号组合冒作一条实际成本。

还有一个与 R217 直接嵌套的结论。设
$\mathcal L_d,\mathcal L_e$ 是两个左二次尾。原 K 的左尾仿射，故
$\mathcal L(K)=0$；(15) 给 $\mathcal F_j(K)\ne0$。
R217 已证明 $\mathcal L(\delta K)$ 与
$\mathcal L(\delta^3K)$ 独立。因此对任意固定 j，

$$
\boxed{
(\mathcal L_d,\mathcal L_e,\mathcal F_j)(\mathcal R_{\mathrm p0})
=\mathbb R^3.
}
\tag{24}
$$

同理 $\lambda_+$ 也不能经该三元组因子化。式 (24) 不需要评价
$\mathcal F_j(\delta K)$ 或 $\mathcal F_j(\delta^3K)$。

**不能把 (22) 和 (24) 拼成十元组满射。**
本文未求
$(\mathcal L_d,\mathcal L_e,\mathcal F_0,\ldots,\mathcal F_7)$
在响应上的完整像，也没有排除 $\lambda_+$ 经更大观测组读出的可能。

## 7. 真实几何含义与保留的 joint 问题

各 $\delta^nK$ 的真实来源已由 R217 的 E8 导子表、R71 交换子实现与 R83 配对词支付。若要把 (22) 作实际几何见证，可对八个方向分别采用有限正、负参数配对字，然后采用 R215/R217 的同一个 pure 校正与 Klein 闭合。

每一个方向的正、负字成本差是其非零实倍数，且 universal pure 差为零。有限个符号组合因此有同一个未校正 pure 值；同一实际 D 可清掉它，所有基准和偶项仍保留。所得有限实际闭 hook 具有相同 $M=0$、$T=\kappa\mathfrak H$、整 pure 零以及同一个严格正 $\lambda_+$ 值，而八个读出的相邻差方向由 (21) 独立。

全部有限控制字、背景和 D 先选定，再选共同物理 I 与同一个基本 pair、八 packet。这里没有要求给定总长，没有假定插入块的空间位移为零，也没有把代数导子当作允许的几何变换。

式 (6) 与 (22) 的组合表明：固定圆的多个真实 gauge 不变量可以被 canonical 响应独立改变，所以它们并不自动携带那个消掉全部响应的 universal 正字符。另一方面，这些读出仍只是一组必要门；它们全部为零不推出完整 period 属于 $L_f$ 的像，更不推出同一个 w 同时支付 R184 的逐 ruling 商。

本稿不展开新的 $\mathcal B_\theta(w)$，不评估新的几何样本，也不触及 R218/R220 的非平端口和 Morse 改造。下一较大的 joint 因子化问题必须使用尚未包含在本稿有限读出中的真实信息。
