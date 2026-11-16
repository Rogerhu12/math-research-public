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
