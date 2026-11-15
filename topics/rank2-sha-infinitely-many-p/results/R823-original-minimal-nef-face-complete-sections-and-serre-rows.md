# R823 — 原最小 nef 面的完整整截面基、真实 Serre 行与线性接触上界

后继：[R825 全 nef 上缺量及所有有界 S 次数区域](R825-original-nef-upper-gap-and-bounded-s-degree-exclusion.md)给统一实际p界；未排e随D增长的临界区。

日期：2026-11-15。**状态：下列最小面结论已证明。**
本篇只处理 R815/R819 下界取最小值的实际类
$C=bH_++mE_{0,1}$，不将整个901射线锥替成这个二参数子锥。

在原十九角曲面上，两个既有有理函数
$\mathsf S=a(t)Y/7$、$\mathsf U=\mathsf S/t$
给出一个明确的 $\mathbb F_1$ 模型。
该最小面的全部截面有显示的整单项式基，乘法满射；
原 Euler 导数保持整个基。对实际因子曲线，
全部对偶化微分也有显示基，且准确回到 $dt/e$。

最后，R805 的原有限接触门在此面变成
$h\le6(m+2)b-3m(m+1)$。
原 $r=2,m=3$ 窗给 $h\le30b-36$，
故 $p\le360b-421\le120D-421$。
因此 $p>120D-421$ 时这个整个最小面不存在合法强接触因子。
这是实际区域排除，不是把子格的 Serre 行当成杀全 $\mathcal W_D$ 的左行。

## 1. 同一个曲面和最小类

沿 R815 记
$$
a=t(t-1)h_7,\qquad h_7=7+4t+16t^2,\qquad
H_+=S_0+4f-\sum_{i\in N}E_{i,1}.
$$
$E_{i,j}$ 均是原普通吹起的全变换类。
令
$$
E=E_{0,1},\qquad D_{b,m}=bH_++mE,\qquad
b\ge m\ge0.
\tag{1}
$$
这里 $E$ 不是一条另造的 nef 素曲线，也没有删掉其后继例外分量。

在原正交基中，
$$
D_{b,m}
=bS_0+4bf-(b-m)E_{0,1}
-bE_{\alpha_+,1}-bE_{\alpha_-,1}-bE_{1,1}.
\tag{2}
$$
其余十五个例外坐标都是零。
因此 (1) 是 R815 固定零链亏量 $m$ 的最小自交类，且
$$
D_{b,m}^2=2bm-m^2,\qquad
-K_XD_{b,m}=2b+m,\qquad
D_{b,m}\cdot H_+=m.
\tag{3}
$$
R819 更广泛的其它等号链不包含在 (1) 中。

先在特征零或原 $p>101$ 的域上证明；
所有单项式与整性结论也在 $\mathbf Z[1/42]$ 上成立。
若需分开 $\alpha_\pm$，先作有限 étale 扩张，
最后由下述只含 $h_7$ 的公式下降。
四点互异以及所有框的过渡只需逆 $2,3,7$。

## 2. 完整截面基：没有遗漏移动系数

定义原有理函数
$$
\boxed{\mathsf S=\frac{aY}{7},\qquad
\mathsf U=\frac{\mathsf S}{t}
=\frac{(t-1)h_7}{7}Y.}
\tag{4}
$$
$\mathsf U$ 不是 R469 的第三中央来源 $U_{136}$。
它只是原同一函数域中的显式坐标。

**定理1。** 以 (1) 的有效代表作有理函数框，
$$
\boxed{
H^0(X,\mathcal O_X(D_{b,m}))
=\bigoplus_{\substack{0\le i\le m\\j\ge0,\ i+j\le b}}
k\,\mathsf S^j\mathsf U^i.
}
\tag{5}
$$
这也是原整格上的自由基，没有目标素数相关分母。
准确维数为
$$
\boxed{h^0(D_{b,m})
=(m+1)(b+1)-\frac{m(m+1)}2.}
\tag{6}
$$

**证明。** 在原 $\mathbb F_4$ 上，一个相应截面写为
$$
F(t,Y)=\sum_{n=0}^bf_n(t)Y^n,\qquad
\deg f_n\le4n.
\tag{7}
$$
这是原无穷框 $T=1/t,\ Z=t^4Y$ 给出的完整条件：
$f_n(t)Y^n=f_n(1/T)T^{4n}Z^n$。
没有把任意较大环境多项式替入。

在 $t=\alpha_\pm,1,\ Y=\infty$ 的第一次中心，
局部 $V=1/Y$ 的截面是
$\sum_nf_n(t)V^{b-n}$。
(2) 要求重数至少 $b$，逐个不同 $V$ 次数准确等价于
$\operatorname{ord}_{t=i}f_n\ge n$。
在 $t=0$ 要求重数至少 $b-m$，
准确等价于
$\operatorname{ord}_0 f_n\ge\max(0,n-m)$。
所以所有且只有以下系数可以出现：
$$
f_n(t)=((t-1)h_7)^n
t^{\max(0,n-m)}P_n(t),\qquad
\deg P_n\le\min(n,m).
\tag{8}
$$
这保每个 $P_n$ 的全部系数。
其余后继吹起的系数为零，(2) 是第一次四点吹起后的线束拉回，
不再产生额外条件。

将 (8) 改写为
$$
f_n(t)=\left(\frac{a(t)}7\right)^n
\sum_{i=0}^{\min(n,m)}c_{n-i,i}\,t^{-i}
\tag{9}
$$
便得 (5)，其中 $j=n-i$。
(9) 中的表面负幂全部由 $a^n$ 中的 $t^n$ 消去，
因此仍是原多项式。
不同 $n$ 给不同 $Y$ 次数，同一 $n$ 的不同 $i$ 给不同 $t$ 次数，
所以这些列独立。
整数系数的可逆变化只含 $7^n$；
所需各固定多项式在 $\mathbf Z[1/42]$ 上两两互素，
故整除条件与 (5) 的整自由基一致。
计数即 (6)。证毕。

特别，当非边界几何整曲线由 (7) 定义时，
$f_0$ 为非零常数；若 $f_0=0$，原方程可被 $Y$ 整除，
与该曲线经过 $(0,1)$ 且为非水平因子矛盾。
因此此面的原常数 charge 实际为
$$
\boxed{F(t,0)\in k^\times,\qquad \deg_tF\le4b.}
\tag{10}
$$

## 3. 原 $\mathbb F_1$ 模型：完整映射而非数值识别

式 (5) 在 $(b,m)=(1,1)$ 给三截面 $1,\mathsf S,\mathsf U$。
它们在原 $X$ 上无公共零点。

可先在仅完成四个 $N$ 首次吹起的曲面 $X_1$ 上核验。
记严格底纤维为 $f_i^{(1)}$，原零截面仍为 $S_0$。
由 R815 的原 $\mathsf S$ 铅笔，
$$
(\mathsf S)_0=S_0+\sum_{i\in N}f_i^{(1)},\qquad
(\mathsf S)_\infty=H_+,
$$
而
$$
(t)=f_0^{(1)}+E-f_\infty.
$$
故在 $\mathcal O(H_++E)$ 的框中，
$1$ 的零除子是 $H_++E$，
$\mathsf S$ 的零除子是 $(\mathsf S)_0+E$，
$\mathsf U$ 的零除子是
$$
S_0+f_{\alpha_+}^{(1)}+f_{\alpha_-}^{(1)}
+f_1^{(1)}+f_\infty.
\tag{11}
$$
两个不同 $\mathsf S$ 纤维不相交，
而 (11) 与 $E$ 不相交。
所以无基点。其余吹起后仍无基点。

由此得到
$$
\pi:X\longrightarrow\mathbf P^2,\qquad
[1:\mathsf S:\mathsf U].
$$
其函数域映射是双有理的，因为
$$
t=\mathsf S/\mathsf U,\qquad
Y=7\mathsf S/a(\mathsf S/\mathsf U)
$$
在稠密开集成立。

设 $q=[0:0:1]$。
前两截面的共同零理想恰为可逆理想 $\mathcal O_X(-E)$：
在 (11) 的补集上即由上述两个零除子的共同因子读出，
且两个剩余 $\mathsf S$ 纤维不相交。
吹起的普遍性质于是给实际双有理态射
$$
\boxed{\iota:X\longrightarrow\operatorname{Bl}_q\mathbf P^2
=\mathbb F_1.}
\tag{12}
$$
令 $\mathbb F_1$ 的负截面、纤维分别为 $E_*,f_*$，则
$$
\boxed{\iota^*E_*=E,\qquad\iota^*f_*=H_+.}
\tag{13}
$$
这里 $E$ 的全部例外分量是实际拉回的一部分，
没有把 $E$ 无证改成 $X$ 上自交 $-1$ 的素截面。

## 4. 这个面的全部乘法与原 Euler 作用

**定理2。** 对 $b\ge m\ge0,\ b'\ge m'\ge0$，
完整乘法
$$
\boxed{
H^0(D_{b,m})\otimes H^0(D_{b',m'})
\longrightarrow H^0(D_{b+b',m+m'})
}
\tag{14}
$$
在同一整格上满射。

确实，对目标单项式 $\mathsf S^j\mathsf U^i$，
先取 $i=i_1+i_2$、$0\le i_1\le m$、$0\le i_2\le m'$。
因 $b\ge m,b'\ge m'$，两份剩余容量
$b-i_1,b'-i_2$ 非负，且它们之和至少 $j$。
再将 $j=j_1+j_2$ 分配到这两份容量，
目标列就是两个实际基列的乘积，系数为一。
这支付的是本二参数面内的整乘法，不外推整个 nef 半群。

原 $\mathcal E=Y\partial_Y$ 同时缩放 (4) 的两个坐标，因此
$$
\boxed{
\mathcal E=\mathsf S\partial_{\mathsf S}
+\mathsf U\partial_{\mathsf U},\qquad
\mathcal E^q(\mathsf S^j\mathsf U^i)
=(i+j)^q\mathsf S^j\mathsf U^i.
}
\tag{15}
$$
这保整个截面空间，未换成另一个连接。
在正特征中整数 $(i+j)^q$ 按原域读取；
(15) 不声称它总是单位。

## 5. 与原轴的全部接触行

在原正规有限轴 $Y=\rho=d\Theta^{17}$ 上置
$$
\phi(t)=\frac{(t-1)h_7d}{7}\Theta(t)^{17},
\qquad\phi(0)=-1.
$$
则原两个坐标准确为
$$
\mathsf S=t\phi(t),\qquad \mathsf U=\phi(t).
\tag{16}
$$
所以整个 (5) 的原接触矩阵是
$$
\boxed{
[t^k]\mathcal E^q(\mathsf S^j\mathsf U^i)|_\rho
=(i+j)^q[t^{k-j}]\phi(t)^{i+j}.
}
\tag{17}
$$
负的系数下标取零。
这是所有未知 $c_{j,i}$ 的真实矩阵，不只取最高项或标量 $q$。

因 $\mathsf S=-t+O(t^2)$，它在原点也是真参数。
设 $U_*(S)=\phi(t(S))$ 为有限形式反解，则同一接触问题也可写成
$$
\sum_{i=0}^mP_i(S)U_*(S)^i,\qquad
\deg P_i\le b-i.
\tag{18}
$$
对原 $m=3$，这有完整 $4b-2$ 列，
不允许先冻结其中某些多项式系数。
(17)–(18) 没有证明其任一前缀为单位，
也没有把 char0 的 Padé 秩搬到目标 $p$。

## 6. 全部对偶化微分与原 dt/e 的准确尺度

设 $C$ 为本面中非边界的几何整曲线，并通过原 $P=(0,1)$。
其与 (12) 的每条收缩曲线交数为零；
因它不包含这些曲线，它与整个例外集合不交。
所以 $C$ 与其在 $\mathbb F_1$ 上的像同构，
但仍允许 $C$ 本身存在其它奇点。

在 $(S,U)$ 仿射图写其原方程
$$
P(S,U)=0,\qquad P\in H^0(bf_*+mE_*).
$$
为避免与原点混淆，下文 $P(S,U)$ 专指这份方程。
原假设 $e(P_0)\ne0$、$P_0:(S,U)=(0,-1)$
给 $P_U(P_0)\ne0$，故 $P_U$ 在函数域中非零。

$\mathbb F_1$ 的典范类是
$$
K_{\mathbb F_1}=-2E_*-3f_*.
\tag{19}
$$
也可直接由 $dS\wedge dU$ 读取：
在 $U=\infty$ 有二阶极；
在底无穷图 $T=1/S,\ V=U/S$ 有
$dS\wedge dU=-T^{-3}dT\wedge dV$。
曲面为有理曲面，$H^0(K)=H^1(K)=0$；
将 $0\to K\to K+C\to\omega_C\to0$ 取上同调，得完整 adjunction 基
$$
\boxed{
H^0(C,\omega_C)=
\left\{
Q(S,U)\frac{dS}{P_U}:
Q=\sum_{\substack{0\le i\le m-2\\j\ge0,\ i+j\le b-3}}
q_{j,i}S^jU^i
\right\}.
}
\tag{20}
$$
若指标区间为空，则空间为零。
当 $b=m$ 时，$(b-3,m-2)$ 不在定理1的参数半锥内，(20) 应直接由同一极除子的逐单项式条件读取；其显示指标仍准确，最后一个无容量的指标不产生列。
这是 Gorenstein 曲线的对偶化层；
奇异曲线正规化上的正则微分还需导子条件，
不能将两者无证相认。
其维数是算术亏格
$$
p_a(C)=1+\frac{2bm-m^2-2b-m}{2}.
\tag{21}
$$

令 $e=\mathcal E P=SP_S+UP_U$。
由 $t=S/U$ 及 $P_SdS+P_UdU=0$，
在同一个函数域中准确有
$$
dt=\frac{UP_U+SP_S}{U^2P_U}dS,
\qquad
\boxed{\frac{dS}{P_U}=U^2\frac{dt}{e}.}
\tag{22}
$$
因此 (20) 给真实的原 $(t,Y)$ 对偶化微分
$U^2Q(S,U)\,dt/e$，不是只在原点相差一个未知单位。

原 $m=3$ 时，全部这些行为
$$
\boxed{
\left(A(S)+U B(S)\right)U^2\frac{dt}{e},
\quad
\deg A\le b-3,\quad \deg B\le b-4,
}
\tag{23}
$$
总维数 $2b-5$。
它们可供 R822 的指定留数做真实 Serre 对偶比较；
还须使用被配线束、所有主部及全来源的实际消元，
不能因 (23) 是完整 $\omega_C$ 基就声称杀全部 $\mathcal W_D$。

## 7. 原接触在整个最小面内只允许线性增长

现在加回 R805 的原实际因子假设：
同原 $qt^rF^3\in\overline{\mathcal W}_D$、
$f_D<p$、$0<h<s$、准确接触首项非零，
以及原点光滑且 $e_0q_0\ne0$。
这里不借用新的截面存在假设。

(10) 给其原常数 charge 的 $c=z=0$，
$a=\deg_tF\le4b$。
正规化属 $\gamma$ 至多 (21)。
故 R805 的实际目标特征内不等式给
$$
\begin{aligned}
h
&\le6\gamma+2a+10b-6\\
&\le6p_a(C)+18b-6\\
&=\boxed{6(m+2)b-3m(m+1)}.
\end{aligned}
\tag{24}
$$
只在满足原 R805 来源范围时使用 (24)；
不将它赋给任意辅助微分或任意形式矩阵。

特别，对原 $r=2,k_{\rm carry}=0,m=3$ 窗，
$s=2h+2$、$p=12h+11$，于是
$$
\boxed{h\le30b-36,\qquad p\le360b-421.}
\tag{25}
$$
原来源的径向预算完整保
$3b+\deg_YQ\le D$，所以
$$
\boxed{p\le120D-421.}
\tag{26}
$$
因此当 $p>120D-421$ 时，
这个面上任意 $b$、任意合法 $q$ 的原强接触因子均不存在。
没有扫描任何目标素数，没有把只对固定 $b$ 的矩阵结论外推。

在原需研究的 $p$ 为 $D^2$ 量级的临界族里，
(26) 排除充分大的整个最小面。
它不排 R819 的正余量区域，
更不排实际 $\kappa\sim47b^2/12$、$e_S$ 随 $b$ 增长的剩余区域。

## 8. 全来源与主目标的界限

(5)、(14) 已支付这个实际面内的全部截面及整乘法；
(20)–(23) 已支付同曲线的真实对偶化行。
它们不支付原 $\mathcal W_D$ 所有其它列的消失，
不把较小 $\mathcal H_3$ 的左行当成全 $M$ 的左行，
也不把 (17) 的环境列数当成目标素数上的单位前缀。

同一个 $R$ 的原值解、normal、两个十三行和下一位必须继续联合。
R822 的分歧与边界补偿仍取同一个联合核，
不能先在 (23) 的子格消元后删掉其余来源列。
本篇的无条件新排除是 (26) 所明确限定的原最小面，
主目标的跨素数中央非零仍未完成。

依赖：
[R815](R815-complete-original-mori-nef-cones-and-s-fibration.md)；
[R819](R819-original-nef-surplus-and-s-projection-degree.md)；
[R805](R805-original-constant-charge-genus-gate-and-all-profile-rank.md)；
[R822](R822-original-cartier-residue-descent-and-actual-ramification-trace.md)。
全文为原整截面、显式吹起映射、adjunction 与既有实际属门的符号证明，
没有程序执行或新增可重算输出。
