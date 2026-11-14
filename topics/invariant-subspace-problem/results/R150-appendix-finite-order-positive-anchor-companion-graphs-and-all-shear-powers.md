# R150 附录：有限阶正主行的相伴矩阵图排核与全部剪切碰撞点态幂

日期：2026-11-13（UTC）。kernel_resume_1cf / Astra-ISP-1cf8c51d；根与 normal_resume_1cf 分别全文独审全部 Bell 次数、逐深度图闭包、相伴矩阵保持、闭性与放大空间的实际域。
状态：已证明。先证明核内相伴矩阵（companion matrix）图的真实闭包，再应用已核二次半条带引理。
不把点态幂的 Bell 实现换成自然幂；不假设归一化算子的自然幂闭。

## 1. 定理

设实 first
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad
v=c_*+\sum_{j\ge0}c_j\chi_j
$$
满足
$$
a_j\ge0,\quad a\in\ell^2\setminus\ell^1,\quad
c_j\in\mathbb R,\quad |c_j|\le C_0a_j,\quad a_*,c_*\in\mathbb R.
\tag{1.1}
$$
不要求辅助行可和，不要求两个支持不交。
定义 $\Theta_a(t)=\sum_j\lfloor ta_j\rfloor$，
并假设对某个 $p>1,\gamma>0$ 和所有充分大的 $t$，
$$
\Theta_a(t)\ge\gamma t^p.
\tag{1.2}
$$
这是排序计数条件，允许任意物理排列。

令
$$
G(x,s)=s^m+\sum_{\substack{i+j\le m\\j<m}}g_{ij}x^is^j,
\qquad m\ge1,\quad g_{ij}\in\mathbb C.
\tag{1.3}
$$
即 $G$ 对 $s$ 首一，且 $(x,s)$ 总次数不超过 $m$。
则对每个 $\lambda\in\mathbb C$、整数 $r\ge1$
以及任意复 $\ell^2$ 指数权 $w$，
$$
\boxed{
[\,G(u,v-u^2)-\lambda\,]^r e^w
\text{ 对 }A\text{ 循环}.
}
\tag{1.4}
$$

特别取 $G(x,s)=s^2-\beta x^2$，得到
$$
\boxed{
[(v-u^2)^2-\beta u^2-\lambda]^r e^w
\text{ 对全部 }\beta,\lambda\in\mathbb C,\ r\ge1\text{ 循环}.
}
\tag{1.5}
$$
若主首位 $a_0=\alpha>0$，这包含原来真正剩余的实值
$\beta=4\alpha^2$。先前 R150 剪切附录已付互素平移边；
本稿不重复计入那些范围，新增的是所有碰撞边及其全部固定点态幂，
在 (1.1)—(1.2) 下均无须首位互素条件。

例如 $a_j=(j+1)^{-\sigma}$、$c_j=(-1)^ja_j$，
$1/2<\sigma<1$ 满足假设。
$\sigma=1$ 不由本稿的有限阶输入自动覆盖。

## 2. 使用的已核实际接口

令
$$
X=X_{\sum_j a_j\chi_j},\qquad Y=X_{\sum_j c_j\chi_j}.
$$
这里特意使用未倾斜、无常数的真实 first：
$X$ 最大增生、空谱，$Y$ 为实 first。
$L=X^{-1}\in A'$ 有界、单射、拟幂零。

R186 给任意有限有界交换系数的 $X,Y$ 多项式
规范最大闭实现、完整 $C$ 自伴、核内任意固定深度的共同自然域，
以及指定循环指数向量的混合图核心。
其共同正则器记为 $R(t)$：
每个足够深幂把 $H$ 送入所需有限自然词域，
属于 $A'$，单射，强趋于 $I$，并保每个闭 $A$ 不变空间。

[实际计数半群与有限阶整预解](R134-appendix-positive-counting-semigroup-and-finite-order-entire-resolvent.md)由 (1.2) 给
$$
\|(X-z)^{-1}\|\le C\exp[C(1+|z|)^{p/(p-1)}].
\tag{2.1}
$$
其实际预解在任何保持全部 $A'$ 的闭空间上可作限制，
且限制范数不增加。

[相反二次增生符号的半条带引理](R150-appendix-opposite-quadratic-accretivity-and-finite-order-resolvent-strip.md)
将用于一个有限正交直和中的真实闭子空间。
它只要求有界系数与 $X$ 的预解交换；
不要求这些系数为标量，也不要求两系数互相自伴。
本稿会逐项支付该子空间的正性、完整平方域及有限阶预解。

## 3. 完整普通 Bell 多项式的首一有界归一化

写真实倾斜和常数为
$$
X_b=X+H,\qquad Y_b=Y+K,\qquad H,K\in A'.
\tag{3.1}
$$
$H,K$ 包括 $a_*,c_*$；任意复 $w$ 的倾斜项均是已核的实际有界交换扰动。
令 $B_{ij}$ 为完整联合 Bell 系数，包含所有交叉 cumulant 和 Bell 乘积。

置 $d=mr$，并考虑标量普通点态符号
$$
F(x,y)=[G(x,y-x^2)-\lambda]^r.
$$
其真实 Bell 多项式是
$$
P(X,Y)=
\sum_{i,j}\frac{B_{ij}}{i!j!}
(\partial_x^i\partial_y^jF)(X+H,Y+K).
\tag{3.2}
$$
规范最大闭实现记为 $\mathsf P$。
(3.2) 是 $F$ 的完整一次 Bell 变换，
没有把它写作 $P_{G-\lambda}^{\,r}$。

在标量变量 $s=y-x^2$ 下，
$$
\partial_x\big|_y=\partial_x\big|_s-2x\partial_s,\qquad
\partial_y=\partial_s.
\tag{3.3}
$$
对赋予 $x,s$ 都为1的总次数，
第一个微分不增加次数，第二个降低次数。
$(G(x,s)-\lambda)^r$ 总次数不超过 $d$，
且 $s^d$ 的系数为1；
任何正阶微分项的 $s$ 次数都不超过 $d-1$。
因此全部混合 Bell 项在 (3.3) 后仍满足这两条准确界。

倾斜代入把
$$
x\mapsto x+H,\qquad
s\mapsto s-2Hx+(K-H^2).
\tag{3.4}
$$
这是 $(x,s)$ 的有界交换系数仿射替换，
不增加总次数，也不改变最高 $s^d$ 系数。
故有有限的真正有界交换系数 $C_{ij}\in A'$，使
$$
\boxed{
P(X,Y)=(Y-X^2)^d+
\sum_{\substack{i+j\le d\\j<d}}C_{ij}X^i(Y-X^2)^j.
}
\tag{3.5}
$$
所有等式先放在覆盖全部中间词的 R186 共同自然域，
再谈规范最大闭实现。

定义实际闭算子
$$
\mathsf T=\overline{Y-X^2}_{\rm can},\qquad
Z=\mathsf T L,\qquad
\operatorname{Dom}Z=\{f:Lf\in\operatorname{Dom}\mathsf T\}.
\tag{3.6}
$$
有界预复合使 $Z$ 闭。
全部 $A'$ 保持它的域并与之交换；
这直接来自 $\mathsf T$ 的最大闭图及 $L\in A'$。
不假定 $YL$ 全域有界。

在充分深的共同自然域上，(3.5) 给
$$
L^dP=Q(Z),\qquad
Q(z)=z^d+\sum_{j<d}A_jz^j,
\tag{3.7}
$$
其中
$$
A_j=\sum_{i\le d-j}C_{ij}L^{d-i-j}\in A'.
\tag{3.8}
$$
所有 $L$ 指数非负，最高系数是真正的 $I$。
这是核心上真实自然词恒等式，不是关于 $Z^d$ 自动闭性的声明。

## 4. 深核图的层次与闭包确实一致

设
$$
M=\ker\mathsf P.
$$
暂假设 $M\ne0$。
它闭且 $A$ 不变，因此被全部 $A'$ 保持。

令 $\mathcal D_k$ 为 $X,Y$ 所有长度不超过 $k$ 的有序自然词的共同域。
可明确取 $k_0=4d+4$：$P$ 在原 $X,Y$ 中的词次数不超过 $2d$，
$Z$ 消耗至多两层自然词域，$j\le d$ 的 $PZ^j$ 至多消耗 $4d$ 层；
全部有界系数和 $L$ 保持每个 $\mathcal D_k$。
因此
$f\in M\cap\mathcal D_{k_0}$ 时 $Z^j f$（$j\le d$）、
(3.7) 及所有出现的 $PZ^j$ 计算都有真实定义。
若需要更深的中间词，只增大固定阈值；R186 为每个有限阈值提供稠密深核。

对 $k\ge k_0$ 定义
$$
\mathcal V_k=
\{(f,Zf,\ldots,Z^{d-1}f):f\in M\cap\mathcal D_k\}
\subset H^d.
\tag{4.1}
$$
这些图闭包不依赖充分大的 $k$。
确实，若 $\ell>k$，取足够深的正则幂
$f_t=R(t)^Nf$，使其属于 $\mathcal D_\ell$。
它仍在 $M$，并且对每个 $j<d$，
$$
Z^jf_t=R(t)^NZ^jf\longrightarrow Z^jf.
\tag{4.2}
$$
域交换逐次支付自然 $Z$ 幂；这里只用已存在于 (4.1) 的向量。
故 $\mathcal V_k\subset\overline{\mathcal V_\ell}$；
反向由 $\mathcal D_\ell\subset\mathcal D_k$。
记共同闭包为
$$
\mathcal M=\overline{\mathcal V_k}\subset H^d.
\tag{4.3}
$$
$M\cap\mathcal D_k$ 稠密且非零，所以 $\mathcal M\ne0$。

对任意 $D\in A'$，
$\operatorname{diag}(D,\ldots,D)$ 保持每个 $\mathcal V_k$，
因而保持 $\mathcal M$。
这里没有声称放大后的整个交换子代数都保持 $\mathcal M$。

还要支付作用后的核条件。
若 $f$ 足够深，则 $Z^j f\in M$：
在相应真实混合域上，由有限多项式和 $L$ 的域交换，
$$
PZ^jf=Z^jPf=0.
\tag{4.4}
$$
这只在所需有限深度使用，不假设全体核向量预先在任何 $Z$ 幂域。

## 5. 相伴矩阵使整个放大图进入 Z 的真实域

定义实际有界相伴矩阵
$$
\mathcal C=
\begin{pmatrix}
0&I&0&\cdots&0\\
0&0&I&\cdots&0\\
\vdots&&&\ddots&\vdots\\
0&0&0&\cdots&I\\
-A_0&-A_1&-A_2&\cdots&-A_{d-1}
\end{pmatrix}\in B(H^d).
\tag{5.1}
$$
$d=1$ 时它就是 $-A_0$。
其每个条目属于 $A'$，因此与所有对角的 $X,Y$ 自然词及其预解交换。

对足够深的 $f\in M$，(3.7) 给 $Q(Z)f=0$，
故
$$
\mathcal C(f,Zf,\ldots,Z^{d-1}f)
=(Zf,Z^2f,\ldots,Z^df).
\tag{5.2}
$$
由 (4.4)，$Zf$ 仍在 $M$；具体从 $f\in M\cap\mathcal D_{k+2}$ 出发，$Zf\in M\cap\mathcal D_k$，
右侧便属于 $\mathcal V_k$；更深的固定起点不改变闭包。
所有充分深图在 $\mathcal M$ 中稠密，$\mathcal C$ 有界，
因此
$$
\mathcal C\mathcal M\subseteq\mathcal M.
\tag{5.3}
$$

令 $\mathbb Z=\operatorname{diag}(Z,\ldots,Z)$，
它是 $H^d$ 上的闭算子。
(5.2) 同时给，在一个稠密图集上
$\mathbb Z v=\mathcal C v$。
若 $v_n\to v\in\mathcal M$ 来自该图集，
则 $\mathbb Z v_n=\mathcal C v_n\to\mathcal C v$。
闭性遂给
$$
\boxed{
\mathcal M\subseteq\operatorname{Dom}\mathbb Z,\qquad
\mathbb Z|_{\mathcal M}=\mathcal C|_{\mathcal M}\in B(\mathcal M).
}
\tag{5.4}
$$
这是整个放大核图上的有界限制。
它来自真正的闭图与有界相伴矩阵，不是从 $Q(Z)=0$ 直接推断 $Z$ 有界。

## 6. 放大空间内的 first 部分仍有准确正性和空谱

写 $\mathbb X=\operatorname{diag}(X,\ldots,X)$、$\mathbb Y$ 类似。
$\mathcal M$ 被所有对角 $A'$ 保持，足以重复 R128 的实际部分论证：

- 正 first 的收缩预解和 $X$ 的全部空谱预解都是对角 $A'$，保持 $\mathcal M$；
- 对任意 first $T$，共同 $R(t)$ 及 $TR(t)^N$ 有界且为对角 $A'$；
  对 $f\in\operatorname{Dom}\mathbb T\cap\mathcal M$ 取图极限，
  得 $\mathbb T f\in\mathcal M$；
- 正 first 的自然部分定义域稠密、闭，且 $(I+t\mathbb T)$ 在该部分上满射，
  逆为原对角收缩预解的限制，所以它真正最大增生；
- $\mathbb X_{\mathcal M}$ 空谱，其预解就是对角 $(X-z)^{-1}$ 的限制，
  因而沿用 (2.1) 的有限阶增长。

这些都是原预解的实际限制；没有在 $\mathcal M$ 上继承未知通常伴随或 $C$。

令 $J=\mathcal C|_{\mathcal M}$。
由 (5.3) 及条目的原域交换，
$J$ 与 $\mathbb X_{\mathcal M}$ 的所有预解交换。

## 7. Y 的完整限制域变为 X 的平方域

在 $\mathcal M$ 的共同深域上，
$\mathbb Xf\in\mathcal M$，且 (3.6)、(5.4) 给
$$
\mathbb Y f-\mathbb X^2 f
=\mathbb Z\,\mathbb X f
=J\,\mathbb X f.
\tag{7.1}
$$
$\mathbb X_{\mathcal M}$ 空谱且 $J$ 有界、与其预解交换；
因此
$$
\mathbb X_{\mathcal M}^2+J\mathbb X_{\mathcal M}
$$
在准确域 $\operatorname{Dom}\mathbb X_{\mathcal M}^2$ 上闭，
例如用其有界逆 $L_{\mathcal M}$ 写成
$(I+J L_{\mathcal M})\mathbb X_{\mathcal M}^2$；
$J L_{\mathcal M}$ 拟幂零，括号为单位。

用对角共同正则器在 $\mathcal M$ 内双向图逼近：
从 $f\in\operatorname{Dom}\mathbb Y_{\mathcal M}$ 出发，
(7.1) 的右侧闭性迫 $f$ 在平方域；
从平方域出发，$\mathbb Y_{\mathcal M}$ 闭性给反向包含。
所以
$$
\boxed{
\operatorname{Dom}\mathbb Y_{\mathcal M}
=\operatorname{Dom}\mathbb X_{\mathcal M}^2,\qquad
\mathbb Y_{\mathcal M}
=\mathbb X_{\mathcal M}^2+J\mathbb X_{\mathcal M}.
}
\tag{7.2}
$$

对任意实 $c>C_0$，$ca_j\pm c_j$ 非负且不可和，
故对应正 first $\mathbb T_\pm(c)$ 的自然部分最大增生。
共同深域上它等于
$$
\pm\mathbb X_{\mathcal M}^2+(cI_{\mathcal M}\pm J)\mathbb X_{\mathcal M}.
$$
把这两条 first 也纳入 R186 的有限共同正则器，
与 (7.2) 同样作双向图闭包，
得到其准确域恰为 $\operatorname{Dom}\mathbb X_{\mathcal M}^2$。
因此两个相反二次式
$$
\mathbb X_{\mathcal M}^2+(cI+J)\mathbb X_{\mathcal M},
\qquad
-\mathbb X_{\mathcal M}^2+(cI-J)\mathbb X_{\mathcal M}
\tag{7.3}
$$
都在这个准确平方域上最大增生。
为明确其中的闭性，记 $L_{\mathcal M}=\mathbb X_{\mathcal M}^{-1}$，
两个多项式分别是
$
[I+(cI+J)L_{\mathcal M}]\mathbb X_{\mathcal M}^2,
\qquad
-[I+(J-cI)L_{\mathcal M}]\mathbb X_{\mathcal M}^2.
$
方括号均为真正的有界单位，因为 $L_{\mathcal M}$ 拟幂零且与 $J$ 交换；
它们及其逆保持平方域。

## 8. 半条带矛盾与原指定向量

$\mathcal M\ne0$；
$\mathbb X_{\mathcal M}$ 最大增生、空谱且整预解有限阶；
$J$ 有界并与其全部预解交换；
(7.3) 对每个 $c>C_0$ 都有真实最大增生性与准确平方域。
这些逐项满足“两个相反二次符号”引理，取其中 $K=0$ 即得矛盾。

所以原 $M=\ker\mathsf P$ 必为零。
原 $H$ 上 R186 的完整 $C$ 自伴给 $\mathsf P$ 像稠密；
$\xi_w=e^w$ 的真实混合图核心给
$$
[F(u,v)e^w]_A=\overline{\operatorname{Ran}\mathsf P}=H.
$$
这证明 (1.4)，包括 (1.5) 的全部固定点态幂。

## 9. 仍保留的边界

本稿没有以下步骤：

- 把 $\mathbb Z$ 的一般自然高幂称为闭算子；
- 把两个已循环点态因子的乘积自动称为循环；
- 把放大空间的完整交换子不变性或通常伴随同域赠送给 $\mathcal M$；
- 把全空间单射稠密免费传给未知限制；
- 由空谱本身推出有限阶整预解；
- 由尾 $\ell^2$ 小推出未知尾限制的统一范数界。

实际新增机制是：完整 Bell 多项式的首一有界归一化、
核内有限相伴矩阵图的闭包、
以及该非零放大图所迫的两个相反二次正 first。
完整 ISP 与不满足 (1.1)—(1.2) 的其它慢核仍按原 open 保留。
