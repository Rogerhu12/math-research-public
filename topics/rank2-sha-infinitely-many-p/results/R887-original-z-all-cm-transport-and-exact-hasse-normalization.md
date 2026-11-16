# R887. 原 Z 的全部固定 CM 运输、同 P2 初值及精确 Hasse 归一

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


## 11. 原 Hasse 单位的准确归一与同一导数 primitive

本节的 $c_p=\binom{3s-1}{2s-1}$ 始终是特征 $p$ 的原 Hasse 横向值。
它不是将 R884 中完整特征零减项 $\widehat c_p=(p+1)c_p^{\rm int}$
提前改成 $c_p^{\rm int}$；这里没有作除 $p$ 的提升替换。

(3)的单位准确满足
$$
\boxed{\rho_p c_p=1.}
\tag{46}
$$
完整有限阶乘证明如下。在 $\mathbf F_p$ 中，$1/3=2s$，故
$$
\rho_p=\frac{(3s-1)!(2s-1)!}{6(5s-1)!},
\qquad
\rho_pc_p=\frac{(3s-1)!^2}{6s!(5s-1)!}.
$$
令 $m=3s-1=(p-1)/2$，Wilson 定理给
$m!^2=(-1)^{m+1}=(-1)^s$。
同样，将 $(p-1)!$ 在 $5s-1$ 截开，得到
$1/(5s-1)!=(-1)^s(s-1)!$。
因此上式恰等于 $1/(6s)=1$，最后一步用 $6s=p+1$。
所有所写阶乘均小于 $p$，没有除以非单位。

此外，原(31)的单极函数本身就是原 Hasse 导数：
$$
\boxed{
\mathscr F_p
=-c_p^{-1}D^{p-2}x,\qquad
Z=-c_p^{-1}\bigl(D^{p-2}x+r^p\bigr).
}
\tag{47}
$$
[R856(6)、(21)](../results/R856-original-full-hurwitz-frobenius-recurrence-and-universal-divisibility.md)
在原函数域已经给 $D^{p-1}x=-c_p$。
所以(47)右边第一式的导数为一。
它只在 $O$ 有至多 $p$ 阶极，而且为奇函数。
与(31)相减所得函数被 $D$ 杀掉，故是一个有理函数的 $p$ 次幂。
这个根只可能在 $O$ 有至多简单极；
椭圆曲线上 $L(O)=k$，所以它为常数。
奇性迫该常数为零，证明第一式。
第二式再由(31)、(46)得到，仍是原指定 $Z$，没有加水平项。

故(37)现在可以完全用原 $c_p$ 写为
$$
h_{\alpha,p}
=-c_p^{-1}\bigl(j_\alpha+r\circ[\alpha]-\bar\alpha r\bigr).
\tag{48}
$$
这是 §§7–10 与原全 Hurwitz/Hasse 规范的精确相接。
它不改变(39)中原 $G,P2$ 的定义，也不消去(41)、(42)的实际初值项。
本节没有新增数学运行。


## 12. 固定 torsion 的全部 addition 常数与原 Mumford 倍率

本节固定先于 $p$ 的非零挠点 $T$，其阶为 $M$，并排除 $p\mid M$
及固定代数数据的坏集。允许作固定常数扩张以定义全部 $E[M^2]$。
仍用原 $\omega=dx/(2y)$，故准确的 addition 函数是
$$
j_T(P)=\frac{y(P)-y(T)}{x(P)-x(T)},\qquad
D_Pj_T=-x(P+T)+x(P).
\tag{49}
$$
这里没有额外的二分之一：
$y=\wp'/2$ 已经包含该因子。
在泛点 $P=T$，连续值为
$3x(T)^2/(2y(T))=j_2(T)$，其中 $j_2$ 是(35)的二倍点函数。

同一个(31)的 $\mathscr F_p$ 满足
$$
\boxed{
\mathscr F_p(P+T)-\mathscr F_p(P)-\mathscr F_p(T)
=(-\rho_pj_T(P))^p.
}
\tag{50}
$$
先对泛点 $T$ 证明：左边不含 $\mathscr F_p(T)$ 的差被 $D_P$ 杀掉；
取 $p$ 次根后，极只在 $O,-T$，各简单。
其主系数与 $-\rho_pj_T$ 完全相同。
因此两者相差常数。
在 $P=T$ 以(36)的 $\alpha=2$ 定该常数，
正好给(50)。所得是有理 addition 恒等式，
故延拓到所有 $T\ne O$ 的适用纤维，特别包含非零二挠点。
没有把各点的常数分别自由归一。

定义一个先于 $p$ 固定的代数常数
$$
\lambda_T=-\frac1M\sum_{k=0}^{M-1}j_T(P+kT).
\tag{51}
$$
在特征零，(49)使该和的导数望远镜为零，故与 $P$ 无关；
因为全部项是固定代数曲线上的有理函数，所得常数是代数的。
其约化仍是原完整有限和。
将(50)沿整个 $M$ 周期求和，准确得到
$$
\boxed{\mathscr F_p(T)=(-\rho_p\lambda_T)^p.}
\tag{52}
$$
这里 $M^p=M$ 只在最后的特征 $p$ 运算使用。
没有假定 $\lambda_T^p=\lambda_T$，也没有假定 $T$ 在 $\mathbf F_p$ 上。

于是原 $Z$ 的完整平移为
$$
\boxed{
\begin{aligned}
Z(P+T)-Z(P)&=h_{T,p}(P)^p,\\
h_{T,p}(P)
&=-\rho_p\bigl(j_T(P)+\lambda_T+r(P+T)-r(P)\bigr).
\end{aligned}}
\tag{53}
$$
$h_{T,p}/\rho_p$ 是固定有理函数。
其极只可能在 $\mathcal D_2\cup(\mathcal D_2-T)$，各至多简单；
$j_T$ 在 $O,-T$ 的极与 $r(P+T)-r(P)$ 的相应极完整抵消，
除非该点本就在所示二挠极集合内。

若 $T\notin\mathcal D_2\cup\{O\}$，(52)还给准确原点值
$$
Z(T)=\bigl(-\rho_p(\lambda_T+r(T))\bigr)^p.
\tag{54}
$$
二挠点的 $Z(T)$ 不定义，不能在(54)代入；
它们的 $\mathscr F_p(T)=0$ 和 $\lambda_T=0$ 则均合法。

为核对符号和 $T,-T$：
$$
\lambda_{-T}=-\lambda_T,\quad
j_{-T}(P+T)=-j_T(P),\quad
h_{-T,p}(P+T)=-h_{T,p}(P).
\tag{55}
$$
第一式由(51)在特征零重排，或由(49)的奇性得到；
其余逐项代入(53)。更一般的平移复合式
$h_{T+U,p}=h_{T,p}\circ t_U+h_{U,p}$
只在同一个原 $Z$ 上取唯一 $p$ 次根，因而没有附加自由常数。

### 12.1 固定 cover 上的绝对 multiplier

用复 uniformization 只为识别原绝对规范。
写 $T=t\bmod\Lambda$、$Mt=\ell\in\Lambda$，令
$\pi=[M]$，cover 上的变量为 $w$。
在这一固定 cover 上取
$$
q_T(w)=
e^{-\eta_\ell w}
\frac{\sigma(Mw+t)}{\sigma(Mw)\sigma(t)}.
\tag{56}
$$
其全部周期倍率为
$e^{\eta_{\ell'}\ell-\eta_\ell\ell'}=1$；
分子分母 sigma 的符号同时抵消。
更换 $t$ 的格代表时，新增指数也准确抵消，故(56)不依赖该选择。

$q_T$ 的除子是
$\pi^*(-T)-\pi^*(O)$，在 $w=0$ 的首项准确为 $1/(Mw)$。
因此它是由这个代数除子和首项唯一确定的代数有理函数，
定义于固定 $E[M^2]$ 域。这个论证保留了原 Mumford 相位，
没有只保其对数导数后再选一个不同常数。
此外(51)的绝对解析值是
$\lambda_T=\zeta(t)-\eta_\ell/M$，所以
$$
D_w\log q_T
=M\bigl(j_T+\lambda_T\bigr)\circ\pi.
\tag{57}
$$

## 13. 同固定 cover 上必须保留的 G/P2 平移初值

记 $\pi_0=[M]$、$\pi_T=[M]+T$，
$Z_i=Z\circ\pi_i$、$G_i=G\circ\pi_i$、
$H_i=H\circ\pi_i$、$P_i=\mathcal P_2\circ\pi_i$，
其中 $i=0,T$。
令 $h=h_{T,p}\circ\pi_0$。全部是原指定函数的拉回，且
$Z_T-Z_0=h^p$、$D_wZ_i=M$。
定义
$$
\mathcal J_{T,p}=M(G_T-G_0)-D_w\log q_T,\qquad
Q_{T,p}=q_T^2P_0,\qquad
\Xi_{T,p}=P_T-Q_{T,p}.
\tag{58}
$$
由(49)、(57)和原 $DG$ 式，准确有
$$
D_w\mathcal J_{T,p}
=M^2c_p\{(Z_0+h^p)^{p-1}-Z_0^{p-1}\}.
$$
因此
$$
\boxed{
\mathcal J_{T,p}
=-Mc_p\sum_{j=1}^{p-1}\frac{(-1)^j}{j}
h^{pj}Z_0^{p-j}
+\kappa_{T,p}^{\,p}.
}
\tag{59}
$$
$\kappa_{T,p}^p$ 仍定义为(58)的原函数减去显示和。
(53)已经确定整个 $h$，但不能据此删掉这一指定水平项。

同一 $P2$ 的完整方程为
$$
\boxed{
\begin{aligned}
&(D_w-2MG_T)\Xi_{T,p}\\
&=2M H_T^p(Z_0+h^p)^{p+1}
 +2\mathcal J_{T,p}Q_{T,p}
 -2Mq_T^2H_0^pZ_0^{p+1}.
\end{aligned}}
\tag{60}
$$
这由对(58)的整个 $q_T^2P_0$ 作乘积微分直接得到。
特别当 $T$ 不是二挠点时，$Q_{T,p}$ 在 cover 原点的值为一，
而 $P_T$ 的值是原实际 $\mathcal P_2(T)$：
$$
\Xi_{T,p}(0)=\mathcal P_2(T)-1.
\tag{61}
$$
(52)、(54)没有将此值变成零。
若 $T$ 为非零二挠点，则 $P_T$ 在该点有原极，
不能套用(61)。

本节完成的是固定 torsion 的整个 $Z$ cocycle 和绝对 multiplier，
以及它们对原 $G/P2$ 的准确缺陷式。
四个原 $\alpha_\nu$ 与(30)的低配对保持原样。
后续需要使用的是(58)–(61)及原有限 $p$ 基初始资料，
不能由固定 torsion 常数已显式就断言四个指定读数非零。
本增补没有数学执行或素数扫描。


## 14. 同一个原 G/P2 的完整有限 p 基

下面保持原 $K=k(E)$，记 $K_0=K^p$、$q=Z^p$。
因为 $DZ=1$，准确有
$$
K=K_0\oplus K_0Z\oplus\cdots\oplus K_0Z^{p-1}.
$$
定义
$$
\pi_Z(f)=\sum_{i=0}^{p-1}\frac{(-Z)^i}{i!}D^if,\qquad
[f]_j=\frac1{j!}\pi_Z(D^jf).
\tag{62}
$$
于是 $\pi_Z(f)\in K_0$、$f=\sum_{j=0}^{p-1}[f]_jZ^j$。
证明只需在每个基向量 $Z^j$ 上用有限二项式和；
系数 $K_0$ 被 $D$ 杀掉。
$\pi_Z$ 是这个直和的常数坐标投影，**不是乘法同态**。
乘法须完整使用 $Z^p=q$，不能把高次项当成零。

设 $x_j=[x]_j$。原(13)的有限和逐项给
$$
\boxed{
G=-\sum_{j=0}^{p-2}\frac{x_j}{j+1}Z^{j+1},
\qquad x_{p-1}=c_p,\quad x_{p-2}=-r^p.
}
\tag{63}
$$
对 $j\le p-2$ 使用
$\sum_{i=0}^j(-1)^i\binom ji/(i+1)=1/(j+1)$；
对 $j=p-1$，原有限和只到 $p-2$，其值为
$\sum_{i=1}^{p-1}1/i=0$。
后两个坐标分别由
$D^{p-1}x=-c_p$、$D^{p-2}x=-c_pZ-r^p$
及 $(p-1)!=-1,(p-2)!=1$ 得到。
这也直接给 $D^{p-1}G=r^p$。

对任一整数 $1\le a<p$，令
$$
\nabla_a=D-aG.
$$
标量连接的准确 $p$ 曲率为
$$
\nabla_a^p=-a(G^p+r^p)=-aH^p.
\tag{64}
$$
这里 $D^p=0$，且原 $H=(3/5)Z^5+\cdots$ 非零。
令 $\mathsf A_a$ 为 $\nabla_a$ 在(62)原有序基上的矩阵。
其导数部分为 $D(Z^j)=jZ^{j-1}$，乘法部分由(63)并用 $Z^p=q$ 完整形成。
于是
$$
\det\mathsf A_a=-aH^p,\qquad
\operatorname{adj}(\mathsf A_a)=\mathsf A_a^{p-1}.
\tag{65}
$$
事实上(64)使全部特征根等于 $(-aH^p)^{1/p}$，
故特征多项式准确为 $T^p+aH^p$；(65)随之成立。
这些式子也重证 R647 的全局有理解唯一性，
不把局部共振的自由项冒充全局有理水平解。

特别原指定 $P=\mathcal P_2$ 的完整坐标向量是
$$
\boxed{
[P]_{\rm vec}=-q\,\operatorname{adj}(\mathsf A_2)e_1.
}
\tag{66}
$$
这里 $e_1$ 表示基向量 $Z$。
(66)是原定义 $P=-\nabla_2^{p-1}Z^{p+1}$，没有改初始资料。
四个 $P^{n_\nu}R_\nu$ 都用这同一向量、同一乘法 $Z^p=q$
及原 $R_\nu$ 形成。

还可直接读一次 Cartier。写
$P^{n_\nu}R_\nu=\sum\beta_{\nu,j}Z^j$，$\beta_{\nu,j}\in K_0$，
则
$$
\boxed{
\mathcal C(\eta_{\nu,p})
=Z^{-2}\beta_{\nu,1}^{1/p}\,\omega.
}
\tag{67}
$$
证明是 $Z^{-p-2}=q^{-2}Z^{p-2}$；
乘积中只有 $j=1$ 贡献 $Z^{p-1}$ 坐标，
其它高项的 $q$ 折回不贡献这一坐标。
因此原首行问题已完全保留在同一个指定有限 $p$ 基中。
(65)的全矩阵可逆不表示四个指定 $\beta_{\nu,1}$ 或其原点留数非零。

## 15. 降低二挠极阶的同源线性模型及全部新增零点补项

本节直接推广 R636 的实际 $P_6$，并明确保留其与 $P_2$ 幂的区别。
对原四个 degree
$$
m_\nu=2n_\nu\in\{34,72,136,66\},\qquad p>211,
$$
置
$$
Q_m=-\nabla_m^{p-1}Z^{m-1},\qquad
P_m=Z^pQ_m=-\nabla_m^{p-1}Z^{p+m-1}.
\tag{68}
$$
由(64)，这是
$$
\nabla_mQ_m=mH^pZ^{m-1},\qquad
\nabla_mP_m=mH^pZ^{p+m-1}
\tag{69}
$$
各自唯一的全局有理解。
也有完整有限和
$P_m=\sum_{j=0}^{p-1}(-Z)^j\nabla_m^j(Z^m)/j!$，
故在 $O$，$P_m=Z^m(1+\cdots)$，型为 $m$。

### 15.1 原有限窗口保持，但不能删除其它 Z 零点

记 $n=m/2$。在 $O$，$P_2/Z^2=1+O(Z^6)$，
$H=(3/5)Z^5+\cdots$。
对 $C=P_m/P_2^n$，(69)与原 $P_2$ 方程给
$$
DC=\frac{mH^pZ^{p+1}}{P_2}
\left[\left(\frac{Z^2}{P_2}\right)^{n-1}-C\right].
$$
$C$ 的首项为一且型零，所以括号至少从 $Z^6$ 起，
右边阶至少 $6p+5$。
所有 $Z^{6j}$、$1\le j<p$ 的导数系数均为单位。
因此
$$
\boxed{
P_m-P_2^{m/2}=O(Z^{6p+m}),\qquad
(P_m-P_2^{m/2})R_\nu=O(Z^{6p+6}).
}
\tag{70}
$$
所以原首行 $\alpha_\nu$ 保持，R647 中首 Gaussian 规范的前五块模 $p$
也保持。这里没有支付新的模 $p^2,p^3$ 除商，
没有将 $P_m$ 加入原固定预算列。

原 $G$ 在二挠点的准确极阶为 $p^2-p-1$。
$D$ 至多增加一阶，故(68)给
$$
(P_m)_\infty
\le\bigl(p^3-p^2+(m-1)p+1\bigr)\mathcal D_2.
\tag{71}
$$
定义真正新输入
$$
\widetilde\eta_{\nu,p}
=Z^{-p-2}P_{m_\nu}R_\nu\omega
=Z^{-2}Q_{m_\nu}R_\nu\omega .
$$
其二挠极阶至多
$p^3-2p^2+(m_\nu-3)p+1<p^3$，所以三次 Cartier 后至多简单。
其在 $O$ 的留数仍为 $\alpha_\nu$。

但是，若 $Q\ne O$、$Z(Q)=0$，只能由(68)推出 $P_m$ 在 $Q$ 至少阶 $p$，
不能沿用原 $P_2^n$ 的 $np$ 零阶。
实际 $\widetilde\eta$ 在这些点可能有双极。
原有限 $G$ 满足 $G(Q)=0$；
由(69)及 $m>1$，$DQ_m(Q)=0$。
因 $Z$ 是该点参数，准确补留数是
$$
\boxed{
\operatorname{Res}_Q\widetilde\eta_{\nu,p}
=Q_{m_\nu}(Q)\,DR_\nu(Q).
}
\tag{72}
$$
没有已付理由令 $Q_m(Q)$ 为零。

### 15.2 这些补留数是同一个明确低多项式的值

补项不需要新增逐点测试。对泛代数点 $B=(x,y)$，
使用 R856 原单位平移截面
$$
\mathscr S_B(v)
=\exp(-\zeta(B)v)\frac{\sigma(v+B)}{\sigma(B)},\qquad
\mathscr S_B(0)=1.
$$
其实际定义亦可全代数地采用
$D_v\log\mathscr S_B=-\sum_{i\ge0}(D^ix)(B)v^{i+1}/(i+1)!$。
这里只使用次数严格小于 $p$ 的系数，所有阶乘为单位；
没有调用一个未付的奇 degree 全 Hurwitz 定理。

令 $k=p-m$，定义实际多项式
$$
T_{m,p}(B)=[v^{p-m}]\,\mathscr S_B(v)^{p-m}.
\tag{73}
$$
在(72)的每个 $Q$，原 $G$ 的所需低 jet 与
$D_v\log\mathscr S_Q$ 完全相同。
将 $\nabla_m$ 在这个有限窗口共轭为
$\mathscr S_Q^m D_v\mathscr S_Q^{-m}$，并用 $(p-1)!=-1$，得到
$$
Q_m(Q)
=[v^{p-m}]\mathscr S_Q(v)^{-m}
=T_{m,p}(Q).
$$
最后一步使用
$\mathscr S_Q(v)^p=1+O(v^p)$，因为 $p-m<p$。
它不把原 $G$ 的较高 Frobenius 系数删掉；这些系数根本不进入此处的实际读数。

所以定义
$$
F_{\nu,p}(x,y):=T_{m_\nu,p}(x,y)\,DR_\nu(x,y)
$$
就已完整支付(72)。
$T_{m,p}$ 是权 $p-m$ 的代数多项式，
$DR_\nu$ 是权 $m-5$ 的原多项式。
二者乘积型零、只在 $O$ 有极且极阶至多 $p-5=6(s-1)$，故
$$
\boxed{
F_{\nu,p}\in k[X]_{\le s-1},\qquad
X(X+1)\mid F_{\nu,p}.
}
\tag{74}
$$
后一整除还可逐原来源核对：
$R_S,R_U\in x^2k[X]$，此时 $T_{m,p}\in yx^2k[X]$；
$R_T,R_V\in Xk[X]$，此时 $T_{m,p}\in yxk[X]$。
对原 $R_\nu$ 微分后，乘积均含 $x^3y^2=X(X+1)$。
因此两个 $x=0$ 的额外 $Z$ 零点处无补留数；
事实上原 $R_\nu$ 在那里至少阶二，$\widetilde\eta$ 已正则。
没有据(74)宣称 $F_{\nu,p}$ 本身非零或某个指定值非零。

### 15.3 全部三次 Cartier 补项在一个原有限代数内

令 $A(t)=A_{3s-1}(t)$ 为 R853(27)的原多项式，
不是另选的 Hasse 多项式。其根均简单、非 $0,1$。
除 $O,x=0$ 外，原 $Z$ 的全部零点正是这些根的六点纤维。

置
$$
\mathcal E_p=k[T]/(A(T)),\qquad
\phi_{\nu,p}=F_{\nu,p}(-1/T)\in\mathcal E_p.
$$
因为 $A(0)=1$，这里 $T$ 可逆。
$\mathcal E_p$ 有限 étale，底域完美，
故存在唯一 $\phi_{\nu,p}^{[-3]}$ 满足
$(\phi_{\nu,p}^{[-3]})^{p^3}=\phi_{\nu,p}$。
这使用整个有限代数的 Frobenius 逆，
不是只对显示多项式的系数取根。

记 $\widetilde\rho_{\nu,p}=\mathcal C^3\widetilde\eta_{\nu,p}$，
并沿原 $t=-x^{-3}$ 下降为 $\overline{\widetilde\rho}_{\nu,p}$。
(71)、(72)使它的全部极至多简单，
仅在 $t=0,1$ 和 $A(t)=0$，在 $\infty$ 正则。
各留数已经支付，所以有唯一的完整式
$$
\boxed{
\begin{aligned}
\overline{\widetilde\rho}_{\nu,p}
={}&\frac{\alpha_\nu^{1/p^3}}6\,d\log\frac{t}{1-t}\\
&+\operatorname{Tr}_{\mathcal E_p/k}
\left[
\phi_{\nu,p}^{[-3]}
\left(\frac1{t-T}-\frac1{t-1}\right)
\right]dt .
\end{aligned}}
\tag{75}
$$
在 $0$，原分歧六给留数 $\alpha_\nu^{1/p^3}/6$；
在每个 $A$ 根，留数是(72)的 $p^3$ 次根。
$1$ 处的补偿由全留数和确定；
在 $\infty$ 每个括号都正则。
两个满足这些条件的差是 $\mathbf P^1$ 上的全纯微分，故为零。
这也证明(75)没有遗漏一个 exact 余项。

R853 的原 $\eta_{\nu,p}$ 没有这些 $A$ 根处的极。
因此，若其三次 Cartier exact 项记为 R853(19)的 $dH_{\nu,p}$，
原两个模型的完整差正是
$$
\mathcal C^3(\eta_{\nu,p}-\widetilde\eta_{\nu,p})
=t^*\!\left\{
dH_{\nu,p}
-\operatorname{Tr}_{\mathcal E_p/k}
\left[
\phi_{\nu,p}^{[-3]}
\left(\frac1{t-T}-\frac1{t-1}\right)
\right]dt
\right\}.
\tag{76}
$$
所以不能将降低二挠极阶所得的好处解释为免费删去(72)。
真正四首行零给的是(75)第一行同时消失，
留下四个同 $\mathcal E_p$、同原 $G$ 的实际多项式补项。
这个联合条件尚未证明不相容。

本节支付了原 $P2$ 的完整有限 $p$ 基、
同源线性投影的原窗口与降低的二挠极帽，
以及全部新增 $Z$ 零点留数的原有限多项式和 étale trace。
所有推导均为手证，没有数学执行或目标素数扫描。


## 16. 四个固定倒幂的真实平移分解与原零点纤维

本节固定原四个 $m\in\{34,72,136,66\}$，
仍取 $k=p-m<p$，只读取严格小于 $p$ 的原 sigma 系数。
对变化的点 $B$ 设
$$
j_B(P)=\frac{y(P)-y(B)}{x(P)-x(B)}.
$$
所有泛点公式随后在有定义的原 $Z(B)=0$ 点特化；
不把 $B$ 预先换成任意有利的挠点。

### 16.1 固定 m 的准确伴随及低系数递推

在原绝对 sigma 规范下令
$$
\Phi_B(v)=\frac{\sigma(v+B)}{\sigma(v)\sigma(B)}
                 e^{-\zeta(B)v}.
$$
准确的 addition 身份给
$$
D_v\log\Phi_B=j_B(v),\qquad
\Phi_B\Phi_{-B}=x(v)-x(B).
$$
因此原(73)的输入完整满足
$$
\boxed{
\mathscr S_B(v)^{-m}
=\sigma(v)^{-m}\,
 \frac{\Phi_{-B}(v)^m}{(x(v)-x(B))^m}.
}
\tag{77}
$$
$\Phi_{-B}^m$ 满足固定 $m$ 的一阶有理连接
$D_v\Phi_{-B}^m=mj_{-B}\Phi_{-B}^m$。
(77)同时保留原 $\sigma^{-m}$ 和全部有理乘子；
它没有把原输入认成单个有理函数。

若 $a_j(B)=[v^j]\mathscr S_B(v)^{-m}$，
则
$$
\boxed{
(j+1)a_{j+1}=D_Ba_j+m x(B)a_{j-1},\qquad
a_0=1,\quad a_1=0,\quad a_{-1}=0 .
}
\tag{78}
$$
这里使用的 $j+1<p$，所以分母为单位；
$T_{m,p}=a_{p-m}$，没有新增初始变量。
证明是直接求导
$$
D_B\log\mathscr S_B(v)
=D_v\log\mathscr S_B(v)+x(B)v
$$
并逐项比较。
这些是同一原 sigma 的实际多项式，不是按目标值选择的 Jacobi 行。

### 16.2 同一个原 Z 恰为平移连接的曲率退化除子

本篇(50)的 $\mathscr F_p=Z+c_p^{-1}r^p$ 满足准确的通用 addition 公式
$$
\mathscr F_p(P+B)-\mathscr F_p(P)-\mathscr F_p(B)=(-c_p^{-1}j_B(P))^p.
\tag{79}
$$
也可不借任何挠点稠密性来核(79)：
其两边相减后在 $P=O,-B$ 的 $p$ 阶主部全消，
无其它极，所以是常数。
再在 $P=B$ 使用已付 $[2]$ 公式及
$j_B(B)=3r(B)/2$，得到该常数为零。
一般 $B$ 的身份成立后，所有有定义的特化均合法。

对(79)求所需原导数，利用
$D^{p-2}x=-c_p\mathscr F_p$，得到
$$
D_P^{p-1}j_B+j_B^p=c_p\mathscr F_p(B).
$$
从而
$$
\boxed{
\left(D_P-m(j_B-r(B))\right)^p
=-m c_p Z(B).
}
\tag{80}
$$
$B$ 在此是 $D_P$ 的常数，原 $m$ 的像在 $\mathbf F_p^\times$。
这不是只在零点处猜测的平坦公式；右端保留完整原 $Z(B)$。

在 $P$ 的同一 $p$ 基(62)上，(80)的矩阵特征多项式和行列式是
$$
T^p+m c_p Z(B),\qquad -m c_p Z(B).
\tag{81}
$$
在任一实际简单零点 $B_0$，把 $P$ 保为泛点，
矩阵各项在 $B$ 的该局部环内均正则：
分母 $x(P)-x(B_0)$ 在泛 $P$ 函数域中是单位。
因 $D_BZ=1$，(81)在 $B_0$ 的赋值准确为一。
故其局部 Smith 形有 $p-1$ 个单位项及一个一次项；
特化的核、余核各一维，核到余核的法向一阶映射是单位。

这条一阶性质属于完整原连接族。
它没有说明四个指定 $\alpha_\nu$ 中任一个非零，
也没有把四个不同 $R_\nu$ 变为可任意选择的核向量。

### 16.3 原零点上的绝对除点函数及完整 T 读取

现在令 $B\ne O$ 为原 $Z(B)=0$ 点。它不在 $\mathcal D_2$。
在包含 $B$ 的完美域中，超奇异 $[p]$ 是纯不可分同源，
故有唯一点 $C$ 满足 $[p]C=B$。
取唯一正规化有理函数 $h_B$：
$$
\operatorname{div}(h_B)
=[-B]+(p-1)O-p[-C],\qquad
h_B(v)=v^{p-1}(1+\cdots)\quad\text{at }O .
\tag{82}
$$
存在性来自该除子的群和为零，唯一性由首项固定；
若支点重合，(82)按实际除子相加，极帽仍不超过 $p[-C]$。

有完整的有理恒等式
$$
\boxed{D_P\log h_B=j_B-r(B).}
\tag{83}
$$
证明：$j_B-D\log h_B$ 在 $O,-B$ 的主部相消；
$-C$ 的整 $p$ 倍极不给对数微分留下极，因此差为常数 $\mu$。
对数导数满足
$D^{p-1}(D\log h_B)+(D\log h_B)^p=0$，
所以由(80)之前的等式，
$$
\mu^p=c_p\mathscr F_p(B)=r(B)^p .
$$
完美域中唯一的 $p$ 次根给 $\mu=r(B)$。
没有添加任意的指数常数。

记 $E_{p-1}(u)=\sum_{j=0}^{p-1}u^j/j!$。
原(73)于是有完整有限式
$$
\boxed{
T_{m,p}(B)
=[v^{p-m}]
\left(\frac{\sigma(v)}v\right)^{-m}
\left(\frac{h_B(v)}{v^{p-1}}\right)^{-m}
E_{p-1}(-m r(B)v).
}
\tag{84}
$$
这里只用原 $\sigma/v$ 的严格 $<p$ 系数，全部已整；
在该窗口与首 Gaussian 规范一致。
(83)与 $D\log\Phi_B=j_B$ 说明
$\Phi_B(v)v$ 与
$(h_B(v)/v^{p-1})E_{p-1}(r(B)v)$
的首项同为一，对数导数之差从 $v^{p-1}$ 起。
低于 $p$ 的每个正指数都是单位，所以这些低系数准确相同。
取 $-m$ 次幂，并保完整截断指数，便得(84)。
使用原 $Z$ 作为模 $p$ 参数也不改变此式：
$Z=v+O(v^{5p})$，而 $h_B$ 的实际读取只到
$(p-1)+(p-m)<2p$。

(82)的极帽随 $p$ 增长；(84)中原 $\sigma/v$ 的倒幂仍在。
所以它支付的是四个实际 $T_{m,p}$ 的除点函数表达，
不是先于 $p$ 固定的全输入 Riemann–Roch 格。
特别不能将 $D_B$ 免费穿过(83)：
(80)在零点法向的导数是 $-m c_p$，不是零，
且 $D_B$ 不保原零点理想 $(Z(B))$。
若需使用(74)中的 $DR_\nu(B)$，必须仍保这一正常方向及原低卷积。

式(84)可直接放入同一 $\mathcal E_p$ 的(75)；
六点纤维所需的坐标扩张、$p$ 除点和正规化均由(82)确定。
本节没有删去该 trace，没有给新来源赋中央零，
亦没有将一次退化的单位法向项代替原四个指定首行。


## 17. 同原首行的二因子模型：第三次 Cartier 已完整落固定对数线

本节仍用原 $p=6s-1>211$、$b=1$、同一个 $Z,G,H$，
以及(68)的指定 $P_a=Z^pQ_a$。
只取四个实际 degree $m_\nu=34,72,136,66$，并置
$$
b_\nu=m_\nu-6\in\{28,66,130,60\},\qquad
\eta_{\nu,p}^{[2]}
=Z^{-p-2}P_6P_{b_\nu}R_\nu\,\omega .
\tag{85}
$$
方括号 $[2]$ 在此仅表示两个指定因子，不是二倍点拉回。
它也不是把原 $R_\nu$ 或原中央条件换成一个新测试。
这四行使用同一个 $P_6$，其余四因子在 $O$ 对应
$\sigma^{m_\nu-6}R_\nu$ 的原质量一伙伴。

完整结论是
$$
\boxed{
\mathcal C^3\eta_{\nu,p}^{[2]}
=-\alpha_\nu^{\,1/p^3}r\,\omega
=t^*\!\left\{
\frac{\alpha_\nu^{\,1/p^3}}6
\,d\log\frac{t}{1-t}
\right\},
\qquad t=-x^{-3}.
}
\tag{86}
$$
相比 R853 的原 $P_2^{n_\nu}$，这里第三次 Cartier 后已经没有
exact 尾；相比本篇单因子 $P_{m_\nu}$，这里没有其它 $Z$ 零点的补极。
两种改进同时成立，但输入(85)仍依赖 $p$。
(86)不将其认成先于 $p$ 固定的 Hasse--Witt 输入，
亦不证明四个 $\alpha_\nu$ 不能同时为零。

### 17.1 原初始化和首窗口逐项保持

(70)的同一证明适用于这里全部正偶整数 $a<p$：
$$
P_a-P_2^{a/2}=O(z^{6p+a}).
$$
因而
$$
\boxed{
P_6P_{b_\nu}-P_2^{m_\nu/2}
=O(z^{6p+m_\nu}),\qquad
(P_6P_{b_\nu}-P_2^{m_\nu/2})R_\nu
=O(z^{6p+6}).
}
\tag{87}
$$
用到的是原 $P_a$ 的首项 $z^a$、同型规范和原 $G$，
没有给任一因子另选水平解。
原 $R_\nu$ 在 $O$ 的极阶准确为 $m_\nu-6$。
故(85)在 $O$ 的极阶为 $p-4$，其留数准确为
原 $\alpha_\nu$。
这里 $Z=z+O(z^{5p})$ 的误差高于该留数所读取的整个窗口。

(87)同时保持前五个已付模 $p$ Gaussian 块，
但没有支付原模 $p^2,p^3$ 除商的新替代。
特别不能把(85)作为旧同预算 $M$ 的新增列。

### 17.2 全部 Z 零点确实被两个因子消去

在任一 $Q\ne O$ 且 $Z(Q)=0$ 的点，
原 $G$ 和 $Q_a=-\nabla_a^{p-1}Z^{a-1}$ 都正则。
所以每个 $P_a=Z^pQ_a$ 在 $Q$ 至少有 $p$ 阶零。
两个因子共同给
$$
\operatorname{ord}_Q
\left(Z^{-p-2}P_6P_{b_\nu}R_\nu\right)
\ge p-2\ge0 .
\tag{88}
$$
原 $R_\nu$ 在这些点没有极。
这包括原 $A(t)$ 的所有六点纤维及 $x=0$ 的额外零点。
因而(88)是真正逐点的正则性，不是把(72)的补留数规定为零。
一个单独的 $P_m$ 只有 $p$ 阶零，不能沿用本论证。

除 $O$ 外，(85)的极因此只可能在原三个非零二挠点
$\mathcal D_2$。
由(71)，每个二挠点的完整极阶可取上界
$$
\begin{aligned}
d_{\nu,p}
&=\{p^3-p^2+5p+1\}
 +\{p^3-p^2+(b_\nu-1)p+1\}
 -p(p+2)\\
&=2p^3-3p^2+(m_\nu-4)p+2
<2p^3 .
\end{aligned}
\tag{89}
$$
这里只使用 $R_\nu$ 在二挠点正则；它们实际共有的 $y^2$ 零因子
还可把上界减二，但证明不需要该加强。
由于 $m_\nu\le136<p$，(89)的严格不等式在原 $p>211$ 范围成立。

### 17.3 极阶、原偶性和全部留数共同确定输出

若有理微分在一点的极阶至多 $d$，则三次 Cartier 后的极阶
至多 $\lceil d/p^3\rceil$。
这是在局部参数中逐项读取指数 $p^3j-1$ 的直接结果；
Cartier 不会在原正则点新造极。
因此(89)给 $\mathcal C^3\eta^{[2]}$ 在每个二挠点的极阶至多二，
在 $O$ 至多一。

原 $P_a$ 的 $\mu_6$ 型为 $a$，$R_\nu$ 的型为 $-m_\nu$。
连同 $Z$ 的型一和 $\omega$ 的型一，
$p\equiv-1\pmod6$ 使(85)为完整 $\mu_6$ 不变微分。
Cartier 与这些实际自同构拉回相容，故其输出仍不变。
在任一非零二挠点，$[-1]$ 固定该点；
可用反不变局部参数，例如 $y$ 的单位倍数。
不变微分的 Laurent 极阶只能是奇数，
所以刚才的“至多二”严格降成“至多一”。

沿原 $t=-x^{-3}$ 的商映射下降后，输出在 $\mathbf P^1$ 上
仅可能在 $0,1$ 有简单极，在 $\infty$ 正则。
$O$ 上 Cartier 保留留数并取 $p^3$ 次根，
且 $t$ 在 $O$ 分歧六，故 $0$ 处留数为
$\alpha_\nu^{1/p^3}/6$。
全留数和使 $1$ 处留数为其相反数。
具有这些极和留数的微分唯一，因为 $\mathbf P^1$ 没有全纯微分。
这证明(86)，包括整个函数域中的等式。
最后使用
$$
d\log\frac{t}{1-t}=-2\,d\log y=-6r\,\omega
$$
得到(86)的第一个表达式。
证明没有省去二挠点的分歧二或 $x=0$ 的分歧三。

### 17.4 同一有限 p 基中的实际双线性读者

所有输入仍可在(62)的同一原 $p$ 基中形成。
写
$$
Q_6Q_{b_\nu}R_\nu
=\sum_{j=0}^{p-1}\gamma_{\nu,j}Z^j,
\qquad \gamma_{\nu,j}\in K^p .
$$
由(85)及 $P_a=Z^pQ_a$，准确有
$$
\eta_{\nu,p}^{[2]}
=Z^{p-2}Q_6Q_{b_\nu}R_\nu\,\omega,
\qquad
\boxed{
\mathcal C(\eta_{\nu,p}^{[2]})
=\gamma_{\nu,1}^{1/p}\omega .
}
\tag{90}
$$
在 $Z^{p-2+j}$ 中，只有 $j=1$ 给 Cartier 所读的 $Z^{p-1}$；
$j\ge2$ 的全部 $Z^p=q$ 折回也没有第二个这样的指数。
与(67)不同，(90)没有输出端的 $Z^{-2}$ 乘子。
这正是(88)在原有限基中的表现。

各 $Q_a$ 均为原矩阵的指定列
$-\mathsf A_a^{p-1}e_{a-1}$；
所以(90)给同一 $Q_6$ 与四个完整 $Q_{b_\nu}R_\nu$ 的真实双线性读取，
并由(86)付清其随后两次 Cartier：
$$
\mathcal C^2\bigl(\gamma_{\nu,1}^{1/p}\omega\bigr)
=-\alpha_\nu^{1/p^3}r\omega .
\tag{91}
$$
矩阵可逆或双线性配对非退化仍不表示这四个指定读数非零。

### 17.5 单因子补项和原 exact 尾都准确保留在比较式中

记(75)的完整补项为
$$
\mathscr T_{\nu,p}
=\operatorname{Tr}_{\mathcal E_p/k}
\left[
\phi_{\nu,p}^{[-3]}
\left(\frac1{t-T}-\frac1{t-1}\right)
\right]dt .
$$
结合(75)、(86)，得到整个微分的准确恒等式
$$
\boxed{
\mathcal C^3
\bigl(\eta_{\nu,p}^{[2]}-\widetilde\eta_{\nu,p}\bigr)
=-t^*\mathscr T_{\nu,p}.
}
\tag{92}
$$
所以单因子的全部实际 $T_{m,p}DR_\nu$ 没有被删除，
而是完整成为两个指定模型之差。

若 $\eta_{\nu,p}$ 仍表示原 $P_2^{n_\nu}$ 输入，
R853 的 exact 项记为 $dH_{\nu,p}$，则同样有
$$
\boxed{
\mathcal C^3
\bigl(\eta_{\nu,p}-\eta_{\nu,p}^{[2]}\bigr)
=t^*(dH_{\nu,p}).
}
\tag{93}
$$
(92)、(93)共同说明这里没有将原剩余未知赋零。
新得到的是保同一个 $\alpha_\nu$ 的二因子输入及其完整第三 Cartier 返回，
并把两个旧补偿分别定位为准确的模型差。
后续若要由四个原中央条件推出矛盾，
仍须证明同一(90)中四个指定方向不能同时进入最后的零读数；
(86)本身没有增加第五条中央条件。

本节为手证的原窗口、全部极与有限 $p$ 基运算，没有数学执行或目标素数扫描。


## 18. 原四个倒幂的完整 Hurwitz 顶边与同 Z 的非齐次链

本节仍保持原 $b=1$、$p=6s-1>211$ 及四个实际
$m=34,72,136,66$。参数点记为 $B$，以区别于形式平移变量 $v$；
$D_Bx=2y,\ D_By=3x^2$。以下所有 $D_B$ 都先在整条原曲线上取，
再在有定义的点特化，不能把它当作原除子 $Z(B)=0$ 上的导子。

令
$$
F_m(B,v)=\mathscr S_B(v)^{-m}
=\sum_{n\ge0}J_{m,n}(B)\frac{v^n}{n!}.
\tag{94}
$$
这里 Hurwitz 记号表示完整分次幂级数。
它由以下原初值唯一确定：
$$
F_m(B,0)=1,\qquad
\partial_vF_m
=m\left(\sum_{i\ge0}D_B^ix(B)\frac{v^{i+1}}{(i+1)!}\right)F_m .
\tag{95}
$$
在特征零，(95)正是(73)、(77)所用同一个
$e^{-\zeta(B)v}\sigma(B+v)/\sigma(B)$ 的 $-m$ 次幂。
(95)对 Hurwitz 系数的递推只用整数二项式和原整导子 $D_B$，
所以全部 $J_{m,n}$ 都在原
$\mathbf Z[1/6,m,x,y]/(y^2-x^3-1)$ 中。
因此下面的全 Hurwitz 约化不依赖一个未付的奇 degree whole-theta 整性结论。

### 18.1 完整顶端不是零，而是同一个原 Fp

在特征 $p$ 的完整 Hurwitz 环中，准确有
$$
\boxed{
\partial_v^pF_m
=-m c_p\bigl(\mathscr F_p(B)+v\bigr)F_m.
}
\tag{96}
$$
特别
$$
\boxed{
J_{m,p+k}
=-m c_p\bigl(\mathscr F_p(B)J_{m,k}
+kJ_{m,k-1}\bigr)\quad(k\ge0),
}
\tag{97}
$$
其中 $J_{m,-1}=0$，$k$ 按其特征 $p$ 的像读取。于是
$$
J_{m,p}=-m c_p\mathscr F_p(B),\qquad
J_{m,p+1}=-m c_p\ne0.
\tag{98}
$$
第二个式子用 $J_{m,0}=1,J_{m,1}=0$；
它是原负幂单位截面的顶边，不是任一 $A_\nu$ 的中央零或非零结论。

为证明(96)，置
$$
h_m=m\sum_{i\ge0}D_B^ix(B)v^{[i+1]},\qquad F_m'=h_mF_m.
$$
正增广 Hurwitz 元的 $p$ 次幂为零，故 $h_m^p=0$。
但 $\partial_v^p$ 在完整 Hurwitz 环中不是零导子。
标量 Bell/Jacobson 恒等式给
$$
F_m^{-1}\partial_v^pF_m
=h_m^p+\partial_v^{p-1}h_m.
$$
原超奇异曲线上的 $D_B^p=0$ 使后一式只剩 $i=p-2,p-1$ 两项。
再用本篇(50)的准确原归一
$$
D_B^{p-2}x=-c_p\mathscr F_p,\qquad
D_B^{p-1}x=-c_p
$$
即得(96)。这里没有以普通截断多项式环中的
$\partial_v^p=0$ 替代实际 Hurwitz 作用。

### 18.2 原 r 相位准确把常数项变成 Z，而不是免费删掉它

记完整 Hurwitz 指数为
$$
\mathrm E(u v)=\sum_{n\ge0}u^n v^{[n]},
\qquad
\widehat F_m(B,v)=\mathrm E(mr(B)v)F_m(B,v).
$$
本篇原式 $\mathscr F_p=Z+c_p^{-1}r^p$ 给整个参数族上的等式
$$
\boxed{
\partial_v^p\widehat F_m
=-m c_p\bigl(Z(B)+v\bigr)\widehat F_m.
}
\tag{99}
$$
事实上 $\partial_v^p$ 是导子，
$\partial_v^p\mathrm E(mrv)=m r^p\mathrm E(mrv)$；
与(96)的常数项相减后恰为 $-m c_pZ(B)$。
这个相位是同一个原 $r=x^2/y$，没有另选常数。

在每个实际 $Z(B)=0$、$B\ne O$ 的点，$r(B)$ 正则，
所以(99)可合法特化。若
$\widehat F_m=\sum\widehat J_{m,n}v^{[n]}$，则
$$
\widehat J_{m,r_0p+k}
=(-m c_p)^{r_0}(k)_{r_0}\,
\widehat J_{m,k-r_0},
\qquad 0\le k<p,
\tag{100}
$$
右端在 $r_0>k$ 时按零读取。
尤其这些特化后的全 Hurwitz jet 在索引至少 $p^2$ 时为零。
这由 $\partial_v^p\widehat F_m=-m c_p v\widehat F_m$
反复作用直接得到：$\partial_v^p(v)=0$，
而完整 Hurwitz 环中 $v^p=0$。

(100)并未改变原 $T_{m,p}$。
令 $\widehat a_i=\widehat J_{m,i}/i!$，原读数仍准确为
$$
\boxed{
T_{m,p}(B)=
\sum_{j=0}^{p-m}
\frac{(-m r(B))^j}{j!}\,
\widehat a_{p-m-j}(B).
}
\tag{101}
$$
每个指标严格小于 $p$，故全部阶乘是单位。
这是原(84)中指数相位的同一低窗运输，不能只保
$\widehat a_{p-m}$ 或将其余项删除。
此外(99)在零点的法向常数项导数是 $-m c_p$，因为 $D_BZ=1$；
所以仍不能对已经令 $Z(B)=0$ 的式子自由取 $D_B$。
这一点与(80)、(81)的实际法向单位相符。

### 18.3 四个 T 的固定长度逆序链及必须保留的实际顶值

写 $a_n=J_{m,n}/n!$，仅对 $n<p$ 使用这个普通系数。
由原(78)及(98)，最高一步准确是
$$
\boxed{
D_Ba_{p-1}+m x\,a_{p-2}
=m c_p\mathscr F_p(B).
}
\tag{102}
$$
也可完全用整 Hurwitz 式核对符号：
$J_{m,p}=D_BJ_{m,p-1}+m x(p-1)J_{m,p-2}$，
且 $(p-1)!=-1,(p-2)!=1$。

对同一个指定 $m$ 令
$$
A_{r,m}=a_{p-r},\qquad 1\le r\le m .
$$
在 $x\ne0$ 的开集，完整反向读取为
$$
\boxed{
\begin{aligned}
A_{1,m}&=\frac{J_{m,p-1}}{(p-1)!},\\
A_{2,m}&=\frac{m c_p\mathscr F_p-D_BA_{1,m}}{m x},\\
A_{r+1,m}
&=-\frac{D_BA_{r,m}+(r-1)A_{r-1,m}}{m x},
\qquad 2\le r<m,\\
T_{m,p}&=A_{m,m}.
\end{aligned}}
\tag{103}
$$
因此四个原 $T_{m,p}$ 各由固定的 $m-1$ 步从真实
$J_{m,p-1}$ 与同一个非零 $c_p\mathscr F_p$ 读出；
$D_B\mathscr F_p=1$，故该已知项的后续导数也完全固定。
(103)的 $A_{1,m}$ 是(94)、(95)已经确定的实际多项式，
不是四个可独立选择的参数。

(103)中除 $x$ 只用于显示这个逆序式。
在 $x=0$ 处，应使用清分母后的(102)、(103)；
由原整系数构造，全部 $A_{r,m}$ 本身仍是原正则多项式。
不能凭逆序式的形式分母添加或忽略额外极。

这条链保留了此前低递推之外的实际非齐次顶边。
它尚未证明本篇(90)中四个
$Q_6Q_{m_\nu-6}R_\nu$ 的指定读数不能同时为零：
(98)的单位属于平移负幂单位截面，
(101)的原相位以及(103)的实际顶值都还在。
后续若将(103)转置到四个原 $DR_\nu$ 或同 $Q_6$ 配对，
必须同时运输这些项，不能把顶端单位直接当成原 $\alpha_\nu$。

本节为原 sigma 单位初值、完整 Hurwitz 递推和同一原 $Z$ 的手证；
没有数学执行或目标素数扫描。
