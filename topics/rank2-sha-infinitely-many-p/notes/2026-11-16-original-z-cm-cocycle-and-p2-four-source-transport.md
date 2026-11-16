# 原 Z 的完整 CM cocycle、P2 初值缺陷与四首行运输

日期：2026-11-16。**范围：本注在 R636/R853 的同一个指定 $M=1$ 模型中，准确计算 $[2]$、$[\delta]$ 对 $Z$ 的全部 Frobenius 差，保留原 $\mathcal P_2$ 的真实运输缺陷，并将其完整带入四个原加权 Cartier 行。没有证明四个原首行不能同时为零。**

本注不是另选一个满足 $DZ=1$ 的 primitive。所有公式都使用 R853(26)已经核定的原 $\mathscr R_p$。不改变原 Gaussian、四个 $R_\nu$ 或其 Frobenius 初始资料。

## 1. 同一个指定模型与一个明确单位

在原共同模型
$$
E:y^2=x^3+1,\quad X=x^3,\quad
\omega=\frac{dx}{2y},\quad D=\frac d{dz},\quad
\delta^2=-3,\quad p=6s-1>211
\tag{1}
$$
上工作，剩余域取包含 $\mu_6$ 的完美域 $k$。本注公式均在这个特征 $p$ 函数域中成立。置
$$
m=3s-1,\quad d=X-8,\quad A_2=X^2+20X-8,
$$
$$
\mathscr R_p(x)=\frac12\sum_{j=0}^{m}
 \binom mj\frac{x^{3j+1}}{3j+1},\qquad
Z=\frac{\mathscr R_p(x)}{y^p},\qquad DZ=1.
\tag{2}
$$
这是原指定多项式，不允许添加 $p$ 次幂。

记
$$
\boxed{\rho_p=\frac{m!}{6(1/3)_{m+1}}\in\mathbf F_p^\times.}
\tag{3}
$$
准确的有限二项式恒等式给
$$
\frac12\sum_{j=0}^{m}\frac{(-1)^j\binom mj}{3j+1}
=\frac{m!}{6(1/3)_{m+1}}.
\tag{4}
$$
例如可先在特征零对 $(1-t^3)^m$ 逐项积分，再约化；
没有在特征 $p$ 对非单位分母积分。
分子 $m!$ 为单位；$(1/3)_{m+1}$ 约化为
$(2s)(2s+1)\cdots(5s-1)$，每个因子均非零，故(3)确为单位。

在任一非零二挠点 $Q=(e,0)$，$e^3=-1$，
(2)、(4)给
$$
\mathscr R_p(e)=e\rho_p,\qquad
Z=\frac{e\rho_p}{y^p}+\text{正则项}.
\tag{5}
$$
后一个式子没有漏掉其它负幂：$\mathscr R_p'(x)=y^{p-1}/2$，
且 $x-e$ 在 $Q$ 的阶为二，所以
$\mathscr R_p(x)-\mathscr R_p(e)$ 的阶至少 $p+1$。
$Z$ 的唯一极点是三个这样的 $Q$，各阶恰为 $p$；在 $O$ 阶一。

## 2. 完整 norm-three Frobenius 差

原乘法公式为
$$
x_\delta=-\frac{X+4}{3x^2},\qquad
y_\delta=-\frac{yd}{3\delta X}.
\tag{6}
$$
有如下全函数域等式：
$$
\boxed{
Z\circ[\delta]-\delta Z=h_{\delta,p}^{\,p},\qquad
h_{\delta,p}=6\delta\rho_p\,\frac{x^2}{yd}.
}
\tag{7}
$$

以下证明同时支付全部极与原点条件。
左边被 $D$ 杀掉，故属于 $k(E)^p$；
这里 $D\ne0$ 且 $k$ 完美，曲线函数域的 $D$ 核准确是 $k(E)^p$。
取其唯一 $p$ 次根 $h$。

$Z\circ[\delta]$ 的极点是三个非零二挠点的全部九个逆像，
即 $yd=0$；各极阶为 $p$。
原二挠点也在该九点内，因为 $[\delta]$ 在 $E[2]$ 上为恒等。
故 $h$ 在这些九点至多有简单极，在其它点无极。

$Z\circ[\delta]-\delta Z$ 在 $O$ 正则且值为零，
又是 $\mu_6$ 型一。因此其 $p$ 次根是型五、在 $O$ 为正阶，
其阶至少五。这一步可用先于 $p$ 固定的代数参数 $-x/y$ 判断；
不引入一个随 $p$ 改选的 $du=\omega$ 参数。

由于 $yd$ 的九个零点均简单，$h\,yd$ 只可能在 $O$ 有至多四阶极。
它的型为二，而 $L(4O)=\langle1,x,y,x^2\rangle$ 中型二子空间恰为
$k x^2$。所以 $h=c\,x^2/(yd)$，尚只剩一个常数。

在(5)的 $Q$ 上，(6)给 $[\delta]Q=Q$、$y_\delta/y=\delta+O(y)$。
因此左边(7)的主部为
$$
(\delta^{-p}-\delta)\frac{e\rho_p}{y^p}
=\frac{2e\rho_p}{\delta y^p}.
\tag{8}
$$
这里 $\delta^p=-\delta$。
另一方面 $e^{2p}=-e$、$d(Q)=-9$，故
$$
\left(6\delta\rho_p\frac{x^2}{yd}\right)^p
=\frac{2e\rho_p}{\delta y^p}+\text{正则项}.
$$
这确定了唯一常数，并证明(7)。特别整个 cocycle 非零，
不是仅一个未说明的连接常数。

## 3. 同一原 Z 的完整二倍点差

同一个模型还准确给
$$
\boxed{
Z\circ[2]-2Z=h_{2,p}^{\,p},\qquad
h_{2,p}=18\rho_p\,\frac{x^2(X-2)}{yA_2}.
}
\tag{9}
$$
证明同样从原差的 $D$ 核出发。
其极只在 $yA_2=0$ 的十五点，取 $p$ 次根后至多简单；
根在 $O$ 阶至少五、型五。
因此它必形如
$$
h_{2,p}=\frac{x^2(c_0+c_1X)}{yA_2}.
\tag{10}
$$
此处所有数据在 $\mathbf F_p$ 上，故 $c_0,c_1\in\mathbf F_p$。

在非零二挠点，$[2]Q=O$，故 $Z\circ[2]$ 正则，
左边(9)的主部为 $-2e\rho_p/y^p$。
由 $A_2(Q)=-27$ 得
$$
c_0-c_1=-54\rho_p.
\tag{11}
$$
第二个准确条件来自同一原 $[2][\delta]=[\delta][2]$，而非另选一条数据。
对两种复合次序取 $p$ 次根，得到
$$
h_{\delta,p}\circ[2]-2h_{\delta,p}
=h_{2,p}\circ[\delta]+\delta h_{2,p}.
\tag{12}
$$
在固定参数 $t_0=-x/y$ 下，
$h_{\delta,p}=-6\delta\rho_p t_0^5+\cdots$、
$h_{2,p}=-c_1t_0^5+\cdots$。
读取(12)的首项给
$$
-6\delta\rho_p(2^5-2)
=-c_1(\delta^5+\delta),
$$
即 $c_1=18\rho_p$；(11)遂给 $c_0=-36\rho_p$。
这证明整个(9)，包括所有十五个极，而不是只匹配一个局部展开。

### 3.1 同一个原 Jp 的完整有理函数方程

为直接接 R853(25)的共用输入，令
$$
t=-X^{-1},\qquad u_0=-x/y,\qquad J_p(t)=Z/u_0,
$$
$$
T_\delta(t)=-\frac{27t}{(1-4t)^3},\qquad
T_2(t)=\frac{64t(1-t)^3}{(1+8t)^3},\qquad
a_2(t)=1-20t-8t^2 .
$$
原 $J_p=A_m/(1-t)^m$ 仍逐字为 R853(27)指定的有限多项式比。
将(7)、(9)分别除以 $\delta u_0$、$2u_0$，准确得到
$$
\boxed{
\frac{1-4t}{1+8t}J_p(T_\delta(t))-J_p(t)
=
\frac{6(-1)^{s+1}\rho_p\,t^{5s-1}}
 {(1-t)^m(1+8t)^p},
}
\tag{12a}
$$
$$
\boxed{
\frac{(1-t)(1+8t)}{a_2(t)}J_p(T_2(t))-J_p(t)
=
\frac{9(-1)^s\rho_p\,t^{5s-1}(1+2t)^p}
 {(1-t)^m a_2(t)^p}.
}
\tag{12b}
$$
例如(12a)用
$u_0\circ[\delta]=\delta u_0(X+4)/(X-8)$；
余项中 $x^{2p-1}=X^{4s-1}$，
除去 $(X+1)^m(X-8)^p$ 后剩 $X^{1-5s}=
(-1)^{s+1}t^{5s-1}$。
(12b)用
$u_0\circ[2]=2u_0(X+1)(X-8)/A_2$，同样计算符号。
这两条都是原整个 $J_p$ 的恒等式，没有截去高于首共振的项。
其右端在 $t=0$ 恰从 $t^{5s-1}$ 起，不能将这个高阶事实误用于删去下节在其它固定点出现的 $P2$ 缺陷。

## 4. 同原 G、P2 必须保留的运输缺陷

继续用 R853(2)的全部指定数据
$$
G=\sum_{i=0}^{p-2}\frac{(-1)^iZ^{i+1}D^i(-x)}{(i+1)!},
\quad r=\frac{x^2}{y},\quad H=G+r,
$$
$$
\mathcal P_2=-\nabla_2^{p-1}(Z^{p+1}),\quad
\nabla_2=D-2G,\quad
\nabla_2\mathcal P_2=2H^pZ^{p+1}.
\tag{13}
$$
记 $c_p=\binom{3s-1}{2s-1}\in\mathbf F_p^\times$，则原式为
$DG=-x+c_pZ^{p-1}$。

原特征零 sigma 倍率是
$\sigma(\delta z)^2=-3x^2\sigma(z)^6$。
对(13)不能直接以它作全函数域替换。准确设
$$
\begin{aligned}
J_{\delta,p}&=\delta G\circ[\delta]-3G-\frac{2y}{x},\\
Q_{\delta,p}&=-3x^2\mathcal P_2^3,\\
\Xi_{\delta,p}&=\mathcal P_2\circ[\delta]-Q_{\delta,p}.
\end{aligned}
\tag{14}
$$
这些全是原有限表达式确定的函数，没有增添自由水平项。

由(6)、(7)、(13)逐项微分，完整地有
$$
DJ_{\delta,p}
=-3c_p\bigl((\delta Z+h_{\delta,p}^p)^{p-1}+Z^{p-1}\bigr).
\tag{15}
$$
例如 $3x_\delta+x+4/x^2=0$ 恰消所有非 Frobenius 项。
若要把(15)积分，准确形式是
$$
J_{\delta,p}
=-3c_p\sum_{j=1}^{p-1}
 \frac{(-1)^j}{j\delta^j}h_{\delta,p}^{pj}Z^{p-j}
+k_{\delta,p}^p,
\tag{16}
$$
其中 $k_{\delta,p}^p$ **定义为(14)原函数减去显示有限和**。
它由原 $G$ 固定，不能设为零或任意选取。
每个 $j$ 都是单位；对(16)微分即回到(15)。

同样，完整 $P2$ 缺陷满足
$$
\begin{aligned}
&(D-2\delta G\circ[\delta])\Xi_{\delta,p}\\
&\quad=
2\delta(H\circ[\delta])^p(\delta Z+h_{\delta,p}^p)^{p+1}
+18x^2\mathcal P_2^2 H^p Z^{p+1}
-6J_{\delta,p}x^2\mathcal P_2^3.
\end{aligned}
\tag{17}
$$
这里使用 $D(-3x^2\mathcal P_2^3)$ 的全部三项，
没有漏掉 $18x^2\mathcal P_2^2H^pZ^{p+1}$。

### 4.1 原初值在两个非零 δ 核上的可见缺陷

令 $Q=(0,\pm1)\in E[\delta]\setminus\{O\}$。
原(2)给 $Z(Q)=0$，且 $DZ=1$。
R853 §2 对指定(13)已经证明
$\operatorname{ord}_Q\mathcal P_2\ge p$。
但是 $[\delta]Q=O$，原 $\mathcal P_2=z^2+\cdots$，
所以在固定局部参数 $x$ 上
$$
\boxed{
\Xi_{\delta,p}
=-\frac34x^2+O(x^3),\qquad
\operatorname{ord}_Q Q_{\delta,p}\ge3p+2.
}
\tag{18}
$$
首系数可直接由
$-x_\delta/y_\delta=\delta x/(2y)+O(x^2)$ 得到。
因此 $\Xi_{\delta,p}$ 的整条函数不能删除：
它在同两个固定点有真实单位首项。
这也说明仅付(7)的 $Z$ cocycle 还不等于付了 theta frame。

令 $d_p=p^3-p^2+p+1$。
原 $\mathcal P_2$ 的全极帽还给：
$\Xi_{\delta,p}$ 在原三个非零二挠点极阶至多 $3d_p$，
在 $d=0$ 六点至多 $d_p$，在其它点正则。
在 $O$ 两项都阶二，故无极。
(18)并没有改变任何原 Frobenius 初始资料。

## 5. 完整加权 Cartier 运输和八个固定点的原留数

对四个原 $A_\nu=\sigma^{2n_\nu}R_\nu$，
$n_\nu=17,36,68,33$，保 R853 的
$$
\eta_{\nu,p}=Z^{-p-2}\mathcal P_2^{n_\nu}R_\nu\,\omega,\qquad
\alpha_\nu=[z^{p+1}]\mathcal P_2^{n_\nu}R_\nu .
\tag{19}
$$
原拉回来源的函数部分准确为
$$
R_\nu^{(\delta)}
=\delta^{2n_\nu}x^{2n_\nu}(R_\nu\circ[\delta]),\qquad
[\delta]^*A_\nu=\sigma^{6n_\nu}R_\nu^{(\delta)}.
\tag{20}
$$
这是完整原 sigma 倍率；$R_\nu^{(\delta)}$ 在两个非零 $\delta$ 核正则且阶六，
在 $O$ 极阶 $6n_\nu-6$，没有添加其它极。
定义其同模型加权输入
$$
\eta_{\nu,p}^{(\delta)}
=Z^{-p-2}\mathcal P_2^{3n_\nu}R_\nu^{(\delta)}\,\omega.
\tag{21}
$$
原有限整窗口保持其首系数为
$\delta^{p+1}\alpha_\nu=3\alpha_\nu$。
这里需要的固定最高极为 $6n_\nu-6\le402$，
所需 $p+1+6n_\nu\le p+409<p^2-1$，仍在原窗口内；
没有把原点窗身份冒充全函数域的 sigma 等式。
R853 的全极证明同样适用(21)：最大
$\lfloor(3n_\nu+1)/2\rfloor=102<p$，
故第四 Cartier 返回仍合法。

现在取同一个完整差
$$
\Delta_{\delta,\nu,p}
=\eta_{\nu,p}^{(\delta)}-3[\delta]^*\eta_{\nu,p}.
\tag{22}
$$
它的原输入不是自由测试，而是以下全式：
$$
\boxed{
\begin{aligned}
\Delta_{\delta,\nu,p}
={}&Z^{-p-2}(R_\nu\circ[\delta])\\
&\cdot\left[
Q_{\delta,p}^{n_\nu}
-\left(\frac{\delta Z}{\delta Z+h_{\delta,p}^p}\right)^{p+2}
 (Q_{\delta,p}+\Xi_{\delta,p})^{n_\nu}
\right]\omega .
\end{aligned}}
\tag{23}
$$
这里 $3\delta=\delta^{p+2}$。
式(23)完整保留(7)和(14)两种不同的缺陷；
特别不能只保第一种分母校正，也不能从 Cartier 中提出一个不是 $p$ 次幂的完整括号。

Cartier 与可分拉回相容，R853(22)于是逐项给
$$
\begin{aligned}
\mathcal C^4\Delta_{\delta,\nu,p}
&=3\alpha_\nu^{1/p^4}
 \bigl(\delta(r\circ[\delta])-r\bigr)\omega\\
&=\boxed{48\alpha_\nu^{1/p^4}\frac{y}{xd}\,\omega}.
\end{aligned}
\tag{24}
$$
最后一步是原(6)的准确恒等式
$$
\delta(r\circ[\delta])-r=\frac{16y}{xd}.
\tag{25}
$$
亦可由
$\frac13d\log(y_\delta/y)=\frac13d\log(d/X)$ 验证符号。
在同一 $\mu_6$ 商 $t=-X^{-1}$ 上，(24)的底微分更准确地是
$$
\boxed{\mathcal C^4\overline{\Delta}_{\delta,\nu,p}
=\alpha_\nu^{1/p^4}\,d\log(1+8t).}
\tag{25a}
$$
因为 $\omega=x^4dt/(6y)$。
也可直接使用
$T_\delta(t)/(1-T_\delta(t))
=-27t/((1-t)(1+8t)^2)$，
核对原 R853 对数行在两个真实 frame 之间的全部差。

(24)的全留数表为
$$
\begin{array}{c|c|c}
\text{点集}&\text{点数}&\operatorname{Res}(\mathcal C^4\Delta)\\ \hline
E[\delta]\setminus\{O\},\ x=0&2&-3\alpha_\nu^{1/p^4}\\
d=0&6&\alpha_\nu^{1/p^4}\\
O\text{ 与原非零二挠点}&4&0
\end{array}
\tag{26}
$$
总和为零。在原 $\Delta$ 本身的留数表中，以 $\alpha_\nu$ 替换
$\alpha_\nu^{1/p^4}$ 即可。
所以原指定值准确满足
$$
\boxed{\alpha_\nu=0\iff\mathcal C^4\Delta_{\delta,\nu,p}=0.}
\tag{27}
$$
这是保持全部原数据的同源运输。
(18)的单位是 $\Xi$ 的二阶局部系数，不是(26)所读的 $p+1$ 阶留数；
不能由那个单位跳到(27)的非零。

## 6. 同四来源的全部首行可以只用严格低配对

[R884 附 H](../results/R884-original-t72-norm-three-heat-and-c24-h22-pairing.md)
已经以原 $\sigma(\delta z)=\delta x\sigma^3$ 证明
$$
\mathfrak B(\sigma^6)
=-\frac9{10}\mathscr X_p(\sigma^6,\Theta^6).
\tag{28}
$$
原四个 $R_\nu$ 的极阶正是 $2n_\nu-6$，
故以下不是任选伙伴：
$$
K_\nu:=\sigma^{2n_\nu-6}R_\nu,\qquad
A_\nu=\sigma^6K_\nu,\qquad K_\nu(0)=1.
\tag{29}
$$
其 degree 依次为 $28,66,130,60$，全为实际 whole 来源；
全部一阶 jet 为零。
原整 Leibniz 行与(28)给
$$
\boxed{
\mathfrak B(A_\nu)
=\mathscr X_p(\sigma^6,K_\nu)
-\frac9{10}\mathscr X_p(\sigma^6,\Theta^6).
}
\tag{30}
$$
这里
$$
\mathscr X_p(F,G)=
\sum_{\substack{6\le j\le p-5\\j\equiv0\ (6)}}
 \frac{j_j(F)j_{p+1-j}(G)}{j(j-1)}
$$
保全部真实低卷积，两指标都严格小于 $p$。
因而四个原首行的第一行及三个差都能采用(30)，
无需另留一个未评价的高 $\mathfrak B(\sigma^6)$。
同时 R855 给 $\alpha_\nu=-\mathfrak B(A_\nu)$，所以(24)、(30)
读取的是同四个指定标量。

本注新付的是原 $Z$ 的非零完整有限 CM cocycle、同 $P2$ 的不能删的真实初值缺陷，
以及它们在(23)中的联合运输。
四中央零仍只迫四个(30)为零；
没有增加一个关于 $K_\nu$、$\Xi_{\delta,p}$、新 trace 或任意配对的算术零。
尚需处理的是这些完整低配对／同(23)的共同相容性。

所有证明均为原固定有理函数、全极帽、有限 Newton/Beta 恒等式和 Cartier 自然性的手证；
没有新数学执行、目标素数扫描或可重算输出文件。

依赖：
[R636 原指定有理模型](../results/R636-original-rational-cartier-return-for-two-critical-rows.md)；
[R853 原全极与第四 Cartier 行](../results/R853-original-weighted-cartier-return-and-fixed-logarithmic-line.md)；
[R855 原 canonical 除 p 首行](../results/R855-original-full-heat-connection-and-canonical-divided-jet.md)。


## 7. 原 Z 的单极 primitive 与完整有限多项式

本节仍在(1)的同一个 $b=1$ 模型，所有等式均在特征 $p$。
写 $r=x^2/y$，定义
$$
\mathscr F_p:=Z+\rho_p r^p.
\tag{31}
$$
这不是改变原 $Z$ 的定义；下面始终以(31)的等式恢复原 $Z$。
在任一非零二挠点 $Q=(e,0)$，有 $e^{2p}=-e$，
故 $r^p$ 的整个负主部恰为 $-e/y^p$。
由(5)，(31)在三个二挠点均正则。在 $O$，
固定参数 $u=-x/y$ 给 $r=-u^{-1}+O(u^5)$，故
$\mathscr F_p=-\rho_pu^{-p}+\cdots$，极阶恰 $p$。
又
$$
D\mathscr F_p=1.
$$
$\mathscr F_p$ 为奇函数且 $\mu_6$ 型一。
所以原 $L(pO)$ 中的准确型一基给
$$
\boxed{\mathscr F_p=xy\,P_{s-1}(X),\qquad
P_{s-1}(X)=\frac12\sum_{k=0}^{s-1}
(-1)^k\frac{(5/6)_k}{(4/3)_k}X^k.}
\tag{32}
$$

为完整证明(32)，型一奇基正是
$xy,xyX,\ldots,xyX^{s-1}$，因为其极阶依次为
$5,11,\ldots,6s-1=p$。
对 $xyP(X)$ 微分得
$$
6X(X+1)P'(X)+(5X+2)P(X)=1.
\tag{33}
$$
若 $P=\sum P_kX^k$，则 $P_0=1/2$，
$$
P_k=-\frac{6k-1}{6k+2}P_{k-1}\quad(1\le k\le s-1).
$$
全部分母 $6k+2$ 为单位；最顶方程的系数
$6(s-1)+5=p$ 为零。因此这些方程唯一给(32)。
比较 $O$ 的完整最高极项，还给 $P_{s-1}=\rho_p$。

将(31)乘 $y^p/x$，得到同一原多项式的精确恒等式
$$
\boxed{
\frac12\sum_{j=0}^{3s-1}\binom{3s-1}{j}\frac{X^j}{3j+1}
+\rho_p X^{4s-1}
=(X+1)^{3s}P_{s-1}(X).
}
\tag{34}
$$
这里使用 $2p-1=3(4s-1)$、$y^{p+1}=(X+1)^{3s}$。
(34)保留全部高项，不只是首共振以前的截断。

## 8. 任意固定 CM 倍乘的原 Z 全 cocycle

先于 $p$ 固定非零 $\alpha\in\mathcal O_K$，记
$d_\alpha=\alpha\bar\alpha$，并排除 $p\mid6d_\alpha$
及该固定代数模型的分母坏集。
这里 $d_\alpha$ 与前文 $d=X-8$ 不同。
在原惰性剩余域内 $\alpha^p=\bar\alpha$。

取原绝对 sigma division 函数
$$
q_\alpha(z)=\frac{\sigma(\alpha z)}{\sigma(z)^{d_\alpha}},
\qquad
j_\alpha=\frac1\alpha D\log q_\alpha.
\tag{35}
$$
此处 $q_\alpha$ 的常数和半特征均固定：
在 $O$ 的首项为 $\alpha z^{1-d_\alpha}$。
它是原曲线上的代数有理函数，除子为
$$
\operatorname{div}(q_\alpha)
=[\alpha]^*(O)-d_\alpha(O).
$$
一个直接的规范核对如下。
原等边格的准周期满足
$\eta(\alpha\ell)=\bar\alpha\eta(\ell)$，所以 sigma 商的指数倍率抵消。
其半特征在 $\Lambda/2\Lambda$ 的三个非零类上均为 $-1$。
若 $\alpha$ 在模二为单位，它置换这三个类且 $d_\alpha$ 为奇数；
若模二为零，则 $\alpha\Lambda\subset2\Lambda$ 且
$d_\alpha$ 为四的倍数。因此符号倍率也抵消。
该固定函数及其首项在好约化下保持，不能另乘一个未记的 sigma frame。

有整个函数域中的恒等式
$$
\boxed{
\mathscr F_p\circ[\alpha]-\alpha\mathscr F_p
=(-\rho_p j_\alpha)^p.
}
\tag{36}
$$
证明不依赖任何有限素数样本。
左边被 $D$ 杀掉，故有唯一有理 $p$ 次根 $g$；
其极只在 $E[\alpha]$，各至多简单。
在任一非零核点，以不变微分 $\omega$ 归一切向参数，
$g$ 的主系数是 $-\rho_p/\alpha$；
这是(31)的极系数 $-\rho_p$ 与
$[\alpha]^*\omega=\alpha\omega$ 的直接结果。
而 $j_\alpha$ 在该点的主系数为 $1/\alpha$。

在 $O$，同一计算给 $g$ 的主系数
$\rho_p(\bar\alpha-\alpha^{-1})$；
$j_\alpha$ 的主系数则是
$(1-d_\alpha)/\alpha=\alpha^{-1}-\bar\alpha$。
因此 $g$ 与 $-\rho_pj_\alpha$ 的全部主部一致。
两者都是奇函数，故其无极差为奇常数，只能为零。
这里只以切向归一计算简单极的系数；没有把随 $p$ 的局部积分参数
当成先于 $p$ 固定的全局 frame。

将(31)代回(36)，准确得到
$$
\boxed{
\begin{aligned}
Z\circ[\alpha]-\alpha Z&=h_{\alpha,p}^{\,p},\\
h_{\alpha,p}
&=-\rho_p\bigl(j_\alpha+r\circ[\alpha]-\bar\alpha r\bigr).
\end{aligned}}
\tag{37}
$$
所以对任一固定 $\alpha$，$h_{\alpha,p}/\rho_p$
是先于 $p$ 固定的有理函数。
这包括原 norm-seven 和 norm-thirteen 倍乘的完整函数，
不只是其连接或指定一条特征线。

极点也由(37)完整支付。
在 $E[\alpha]\setminus\{O\}$，
$j_\alpha$ 的主项 $1/(\alpha u)$
与 $r\circ[\alpha]$ 的主项 $-1/(\alpha u)$ 抵消；
在 $O$，三个显示项的主项同样抵消。
所以 $h_{\alpha,p}$ 的极只可能在
$$
\mathcal D_2\ \cup\ [\alpha]^{-1}(\mathcal D_2),
$$
各至多简单；交叠处按同式保留实际相消。
它在 $O$ 正则、型五，故为零或阶至少五。
不能从这个上界断言任意 $\alpha$ 都有非零 cocycle，例如单位 $\alpha$ 的式子为零。

由 $q_\delta=\delta x$、$q_2=-2y$，
(37)逐字恢复(7)、(9)：
$j_\delta=2y/(\delta x)$，
$j_2=3r/2$。
特别 norm-three 的固定括号为
$-6\delta x^2/(y(X-8))$。
对任意两个已固定的 $\alpha,\beta$，
同一个原 $Z$ 还给准确复合式
$$
h_{\alpha\beta,p}
=h_{\alpha,p}\circ[\beta]+\bar\alpha h_{\beta,p}
=h_{\beta,p}\circ[\alpha]+\bar\beta h_{\alpha,p}.
\tag{38}
$$
这保留 Frobenius 对系数的共轭；不能将 $\bar\alpha$ 换成 $\alpha$。

## 9. 全 CM frame 中原 G 与 P2 的两个不同缺陷

令 $P=\mathcal P_2$ 为(13)的原指定函数，并定义
$$
\begin{aligned}
J_{\alpha,p}
&=\alpha G\circ[\alpha]-d_\alpha G-D\log q_\alpha,\\
Q_{\alpha,p}&=q_\alpha^2P^{d_\alpha},\\
\Xi_{\alpha,p}&=P\circ[\alpha]-Q_{\alpha,p}.
\end{aligned}
\tag{39}
$$
这里必须保留原绝对 $q_\alpha^2$。
虽然(35)的对数导数不读取它的常数，
$Q_{\alpha,p}$ 与 $\Xi_{\alpha,p}$ 读取该常数。

原 sigma 微分恒等式
$$
D^2\log q_\alpha
=-\alpha^2x\circ[\alpha]+d_\alpha x
$$
与 $DG=-x+c_pZ^{p-1}$ 给
$$
\begin{aligned}
DJ_{\alpha,p}
&=c_p\{\alpha^2(\alpha Z+h_{\alpha,p}^p)^{p-1}
-d_\alpha Z^{p-1}\}\\
&=c_p d_\alpha
\sum_{j=1}^{p-1}(-1)^j\alpha^{-j}
h_{\alpha,p}^{pj}Z^{p-1-j}.
\end{aligned}
\tag{40}
$$
因为 $\alpha^{p+1}=d_\alpha$，
零次项确切抵消。
因此完整积分式为
$$
\boxed{
J_{\alpha,p}
=-c_p d_\alpha
\sum_{j=1}^{p-1}\frac{(-1)^j}{j\alpha^j}
h_{\alpha,p}^{pj}Z^{p-j}
+k_{\alpha,p}^{\,p}.
}
\tag{41}
$$
$k_{\alpha,p}^p$ 定义为(39)中的原函数减去显示有限和，
其唯一 $p$ 次根存在是(40)的结果。
它仍由原有限 $G$ 确定，不是一个可任意置零的常数或自由参数。

原 $P2$ 的全部运输式为
$$
\boxed{
\begin{aligned}
&(D-2\alpha G\circ[\alpha])\Xi_{\alpha,p}\\
&=2\alpha(H\circ[\alpha])^p
       (\alpha Z+h_{\alpha,p}^p)^{p+1}
 +2J_{\alpha,p}Q_{\alpha,p}\\
&\hspace{1em}
 -2d_\alpha q_\alpha^2P^{d_\alpha-1}H^pZ^{p+1}.
\end{aligned}}
\tag{42}
$$
证明只需对 $Q=q_\alpha^2P^{d_\alpha}$ 保全乘积微分：
$$
DQ=2(\alpha G\circ[\alpha]-J_{\alpha,p})Q
 +2d_\alpha q_\alpha^2P^{d_\alpha-1}H^pZ^{p+1}.
$$
以原 $(D-2\alpha G\circ[\alpha])(P\circ[\alpha])$ 的方程减去本式的相应部分，
便得(42)的全部符号。
代 $d_\delta=3,q_\delta^2=-3x^2$，正好得到(17)。

若 $d_p=p^3-p^2+p+1$，
$\Xi_{\alpha,p}$ 的极支撑只在
$\mathcal D_2\cup[\alpha]^{-1}\mathcal D_2$：
原 $\mathcal D_2$ 上可用上界 $d_\alpha d_p$，
其余逆像上可用 $d_p$。
在 $O$，$q_\alpha^2P^{d_\alpha}$ 与 $P\circ[\alpha]$ 都阶二；
在其它核点两者均正则。
这些是实际极上界，不把相交或零点的可能消去省掉。
因此(37)解决了原 $Z$ 的全 CM 函数，却没有消掉(41)、(42)的指定初值。
前文(18)已给 $\Xi_{\delta,p}$ 真实非零的直接例证。

## 10. 原四加权行在任意固定 CM 下的完整公式

本节另加一个明确的充分大素数门：
对本节固定的 $\alpha$，要求
$$
p>\max\!\left(211,\left\lfloor\frac{68d_\alpha+1}{2}\right\rfloor\right),
\qquad p+1+136d_\alpha<p^2-1,
\tag{43}
$$
并保留全部原坏集。
norm-three 已在前文 $p>211$ 范围支付；norm-thirteen 不能免费沿用那个界。
对任何先于 $p$ 固定的有限 CM 集，(43)只排除有限多个 $p$。

仍只取原四个 $R_\nu$。记
$$
R_\nu^{(\alpha)}
=q_\alpha^{2n_\nu}(R_\nu\circ[\alpha]),\qquad
\eta_{\nu,p}^{(\alpha)}
=Z^{-p-2}P^{d_\alpha n_\nu}R_\nu^{(\alpha)}\omega .
$$
这正是原来源 $A_\nu(\alpha z)$ 的完整函数部分。
在每个非零 $\alpha$ 核点，$q_\alpha^{2n_\nu}$ 的零
与 $R_\nu\circ[\alpha]$ 的原极相消，余阶恰六；
唯一极点是 $O$，极阶 $2d_\alpha n_\nu-6$。
(43)因此支付原有限 sigma 窗以及 R853 第四 Cartier 所需的整个极帽，
其首读数准确为 $\alpha^{p+1}\alpha_\nu=d_\alpha\alpha_\nu$。

定义
$$
\Delta_{\alpha,\nu,p}
=\eta_{\nu,p}^{(\alpha)}-d_\alpha[\alpha]^*\eta_{\nu,p}.
$$
以(37)、(39)写成完整同输入公式是
$$
\boxed{
\begin{aligned}
\Delta_{\alpha,\nu,p}
={}&Z^{-p-2}(R_\nu\circ[\alpha])\\
&\cdot\left[
Q_{\alpha,p}^{n_\nu}
-\left(\frac{\alpha Z}{\alpha Z+h_{\alpha,p}^p}\right)^{p+2}
 (Q_{\alpha,p}+\Xi_{\alpha,p})^{n_\nu}
\right]\omega .
\end{aligned}}
\tag{44}
$$
这里 $d_\alpha\alpha=\alpha^{p+2}$；
所有原 $P2$、绝对倍率及非 $p$ 次幂乘数均显示保留。

R853 与 Cartier 自然性遂给
$$
\boxed{
\begin{aligned}
\mathcal C^4\Delta_{\alpha,\nu,p}
&=d_\alpha\alpha_\nu^{1/p^4}
  \bigl(\alpha r\circ[\alpha]-r\bigr)\omega\\
&=\frac{d_\alpha}{3}\alpha_\nu^{1/p^4}
  \,d\log\frac{y\circ[\alpha]}y .
\end{aligned}}
\tag{45}
$$
最后一步使用 $D\log y=3r$，
没有从 Cartier 中提出(44)的整个括号。
$\alpha$ 及 division 数据在 $\mathbf F_{p^2}$ 上，
而 $p^4$ Frobenius 固定该域，故式中系数和原拉回规范一致。

(45)在 $\alpha=\delta$ 时就是(24)–(26)。
对于单位 $\alpha$ 其右端可为零；
本节不把所有 $\alpha$ 的差都说成首行的等价非零检验。
其实际用途是将同四个未知 $\alpha_\nu$
准确运输到包括 norm-seven/norm-thirteen 的全部指定 frame，
同时显示应保留的(41)、(42)。
四条中央条件没有因此增加，
(30)的四个完整低配对仍是需要联立处理的原标量。

本增补为手证的有限多项式、全部极主部与原代数函数微分推导；
没有数学执行、目标素数扫描或新增可重算输出。
