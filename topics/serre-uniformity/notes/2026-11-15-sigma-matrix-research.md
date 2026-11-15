# 2026-11-15：首 pole 经十二阶下降的准确高带与线性消去边界

状态：**研究记录；显示恒等式与所述线性策略的边界已证明。没有证明原同标签非零。**

本记录续接已经提交的 R784，专门核对 R782 的单位
$c_2=2^{12}3^9\cdot79$ 能否将 R765 的首 pole 直接降成所需
critical 非零。全部使用原 $c=0$ sigma；没有新数值窗，没有运行正式计算，
没有把未消高带另编为完成的主结果。

## 1. 同一个原展开及首 pole

固定
$$
p=6N+5\ge41,\quad F=z^4\sum_{i\ge0}f_i z^{6i},
\quad G=z\sum_{j\ge0}g_j z^{6j},
\quad f_0=g_0=1.
$$
由 R760，
$$
F=u^4T(w),\quad G=uT(w)/C(w),\quad z=uZ(w),\quad w=u^6,
$$
$$
C=(1-w)^{-1/2},\qquad
Z_j=\frac{\binom{2j}{j}}{4^j(6j+1)}.
$$
保留 R765 的同一个单位
$$
B=(-1)^{N+1}\binom{3N+2}{2N+1}\ne0\pmod p.
$$
R765 已证明 $t_0,\ldots,t_N$ 整，且
$$
v_p(t_{N+1})=-1,\qquad pt_{N+1}\equiv-6B\pmod p.
\tag{S1}
$$

在这里需要把整换参范围准确扩到 $N+1$。对 $j\le N+1$，
$C_j$ 整，且 $6j+1\le p+2$ 不会等于 $p$，故 $Z_j$ 也整。
首项为一的 $uZ(u^6)$ 的组合逆逐项以整多项式恢复，不要求除以 $p$。
因此除了 $t_{N+1}$ 本身，恢复 $f_{N+1},g_{N+1}$ 所需的所有输入都整。
$t_{N+1}$ 对各自首次出现系数的乘数均为一。准确得到
$$
f_0,\ldots,f_N,g_0,\ldots,g_N\in\mathbf Z_p,\qquad
pf_{N+1}\equiv pg_{N+1}\equiv-6B\pmod p.
\tag{S2}
$$
两个首 pole 的 $z$ 次数不同，分别为 $p+5$ 和 $p+2$；不能把它们
提前约化成零。

## 2. 第十二阶的完整系数式

记下降阶乘 $(m)_r=m(m-1)\cdots(m-r+1)$，并置
$$
H_r(m,n)=\sum_{a=0}^r(-1)^{r-a}\binom ra(m)_a(n)_{r-a}
=r![X^r](1+X)^m(1-X)^n.
\tag{S3}
$$
定义真正的未筛 critical 卷积
$$
C_{\rm crit}=\sum_{i=0}^{N-1}f_i g_{N-1-i}.
$$
R782 的特征零恒等式 $\mathcal D^{12}F\cdot G=c_2FG$
取 $z^{p-6}$ 后，**在约化以前**准确为
$$
c_2 C_{\rm crit}
=\sum_{i=0}^{N+1}
 H_{12}(6i+4,\,6(N+1-i)+1)f_i g_{N+1-i}.
\tag{S4}
$$
这里左侧总指标是 $N-1$，右侧是 $N+1$。

两个端点的下降阶乘有且只有所需的一项 $p$ 因子。第一个端点为
$$
H_{12}(p+5,1)
=(p+5)_{12}-12(p+5)_{11}
=(p+5)_{11}(p-18),
$$
故
$$
\frac{H_{12}(p+5,1)}p\equiv259200\pmod p.
\tag{S5}
$$
第二个端点只有 $0\le a\le4$：
$$
\frac{H_{12}(4,p+2)}p
\equiv-2\sum_{a=0}^4\binom{12}{a}(4)_a(9-a)!
=-23034240\pmod p.
\tag{S6}
$$
在 (S6) 中，$(p+2)_{12-a}/p$ 的剩余因子是
$2(-1)^{9-a}(9-a)!$；它和原 Hirota 号相乘给统一负号。
这一步保留了两个原普通阶乘，没有先将 $p$ 置零。

用 (S2) 乘上 (S5)、(S6)，得到
$$
\boxed{
\begin{aligned}
c_2C_{\rm crit}
={}&\sum_{i=1}^{N}
 H_{12}(6i+4,\,6(N+1-i)+1)f_i g_{N+1-i}\\
&+2^9\,3^4\,5\cdot659\,B
\qquad\text{于 }\mathbf F_p.
\end{aligned}}
\tag{S7}
$$
常数核对为
$$
-6(259200-23034240)=136650240
=2^9\,3^4\,5\cdot659.
$$

因此这次下降确实产生显式源项，却也精确保留全部
$f_i g_{N+1-i}$、$1\le i\le N$ 的整高带。没有一个
“乘单位 $c_2$”的操作能自行删掉这一和。甚至源项自身在允许的
$p=659$ 为零；这不表示原 critical 因子在该素数全零，只表示此
单个首 pole 源项不能承担全 $p$ 单位断言。

## 3. 截断残差确实降到了 critical 次数，但它不是 critical 卷积

令 $\widehat T=\sum_{j=0}^N t_jw^j$，这是使用原有理整系数的截断；
令 $F_{\widehat T}=u^4\widehat T$、
$G_{\widehat T}=u\widehat T/C$。二者与原 $F,G$ 的系数至指标 $N$
完全相同。其指标 $N+1$ 系数则整。

(S5)、(S6) 说明，截断的两个整端点对模 $p$ 的十二阶系数均为零。
于是 (S7) 等价于
$$
\boxed{
\mathcal D^{12}F_{\widehat T}\cdot G_{\widehat T}
-c_2F_{\widehat T}G_{\widehat T}
\equiv-2^9\,3^4\,5\cdot659\,B\,z^{p-6}
\pmod{(p,z^p)}.}
\tag{S8}
$$
首个可能差异确在 $p-6$：两个被去掉的原项分别有次数 $p+5$、
$p+2$，再分别配上 $G$ 的首项 $z$、$F$ 的首项 $z^4$，
最后下降十二阶。所有次数仍按六递增。

(S8) 是一个非零残差公式（$p\ne659$），并不是
$C_{\rm crit}\ne0$。假使 $C_{\rm crit}=0$，(S8) 只要求十二阶
导数的整高带承担显示的残差；没有矛盾。

## 4. 全部常系数总阶十二算子不能逐项消高带而保住 critical 项

这项边界覆盖将 R784 的各通道以普通总导数补足总阶十二，
再作 $p$ 整常系数线性组合的方案。它不声称排除带额外算术关系、
非恒定系数、任意更高阶或不同精度的其他方法。

写 $D_+=\partial_1+\partial_2$、$D_-=\partial_1-\partial_2$。
因为二可逆，全部常系数齐次十二阶双变量微分算子均唯一写成
$$
\mathcal O=\sum_{r=0}^{12}\lambda_rD_+^{12-r}D_-^r,
\qquad \lambda_r\in\mathbf Z_p.
\tag{S9}
$$
先作用于 $F(z_1)G(z_2)$，再取 $z_1=z_2=z$。
对总次数 $S=p+6$ 的单项 $z_1^mz_2^{S-m}$，其 $z^{p-6}$
系数权准确为
$$
W(m)=\sum_{r=0}^{12}\lambda_r(S-r)_{12-r}H_r(m,S-m).
\tag{S10}
$$
模 $p$ 后，$r\le6$ 的外层下降阶乘含 $p$，所以这些项对每个
**整的**高带单项均为零。余下
$$
\overline W(m)=\sum_{r=7}^{12}
 \overline\lambda_r(6-r)_{12-r}H_r(m,6-m).
\tag{S11}
$$

对 $r\ge7$，多项式 $H_r(m,6-m)$ 在 $m=0,1,\ldots,6$ 全为零：
此时 $(1+X)^m(1-X)^{6-m}$ 的次数至多六。因此它含公因子
$$
D_7(m)=m(m-1)\cdots(m-6).
$$
而 $H_r(m,6-m)$ 关于 $m$ 的首项为 $2^rm^r$；
这是直接在 (S3) 各下降阶乘取首项，再用二项式定理得到的。
于是
$$
H_r(m,6-m)/D_7(m),\qquad r=7,\ldots,12,
\tag{S12}
$$
的次数依次是 $0,\ldots,5$，首系数 $2^r$ 均为单位。
(S11) 的外层因子 $(6-r)_{12-r}$ 也都是单位。

真实整高带的节点是
$$
m_i=6i+4,\qquad 1\le i\le N.
$$
这些是 $N\ge6$ 个模 $p$ 互异的节点；其整数代表在 $10$ 至 $p-1$
之间，故 $D_7(m_i)\ne0$。如果要求不使用高带值的其他关系，
而对每个 $f_i g_{N+1-i}$ 的系数逐项消去，则
$$
\overline W(m_i)=0\quad(1\le i\le N).
$$
除以 $D_7$ 后，一个次数至多五的多项式有至少六个不同根，
故它恒为零。由 (S12) 的三角次数立即得到
$$
\boxed{\lambda_7\equiv\cdots\equiv\lambda_{12}\equiv0\pmod p.}
\tag{S13}
$$
特别 $\lambda_{12}c_2C_{\rm crit}$ 也被同时消去。
因此在这一完整总阶十二常系数算子空间里，没有可以逐项消去
全部整高带、却保留非零 critical 系数的组合。该证明对全部
允许的 $p\ge41$ 成立，不只是大于某个未处理有限窗。

### 4.1 被留下的低 $r$ 项只是已知首 pole 源项

$r\le6$ 对整高带的权为零，并不允许丢掉原两个有 pole 的端点。
保留它们时，端点的共同剩余多项式为
$$
(1+X)^5(1-X)+(1+X)^4(1-X)^2
=2(1+X)^4(1-X).
$$
故对 $0\le r\le5$，
$$
[z^{p-6}]D_+^{12-r}D_-^r(F\otimes G)|_{\rm diag}
=720B(6-r)!\,r![X^r]\bigl(2(1+X)^4(1-X)\bigr).
\tag{S14}
$$
$r=6$ 的值为零。六个源项的系数依次为
$$
1036800,\quad518400,\quad138240,\quad
-103680,\quad-207360,\quad-172800.
$$
它们记录原首 pole／移位 Cartier 单位，均没有留下所需
$N-1$ 的带原标签乘积。将其称为 critical 非零会再次混淆残差与目标。

## 5. 与 R765 原二阶残差的精确比较

R770 的原坐标恒等式是
$$
R_2(A):=\mathcal D^2F_A\cdot G_A
-\left(4x+\frac8{x^2}\right)F_AG_A
=\frac{12u^9}{C}\mathscr Q(A).
$$
因此 $A=\widehat T$ 时，$[z^{p+4}]R_2(A)\equiv12B$。
直接再取普通十阶导数，相关阶乘是
$$
(p+4)_{10},\qquad
\frac{(p+4)_{10}}p\equiv-2880\pmod p.
$$
所以未经归一的 $z^{p-6}$ 系数为零模 $p$。
若保留这一个系数的已知整除性并除以 $p$，准确得到
$$
\frac{[z^{p-6}]D_z^{10}R_2(\widehat T)}p
\equiv-34560B\pmod p.
\tag{S15}
$$
这里只对显示的单个已证可除系数除 $p$，没有宣称整个幂级数可除。

(S15) 依然是 R765 的同一残差。乘积求导后含全部混合导数，
以及对原非恒定势 $4x+8/x^2$ 的导数，不能把它置换为
$\mathcal D^{12}F\cdot G$。不经证明删去这些项会错误地制造
critical 单位。

## 6. 尚缺的实际信息

目前没有获得使 (S7) 高带和无法恰好抵消源项的定理。
原高带并不是可自由选择的参数；它们已由同一个原 sigma 决定，
所缺的是对这些实际值足够强的关系或共同零排除。
(S13) 仅说明常系数总阶十二的逐项消去不能供应这种新信息。

即便先证明未筛的某个 $f_i g_{N-1-i}$ 非零，仍必须保留同一个
真本原标签和原 Legendre 因子
$$
\mathbf1_{\gcd(6i+7,p+1)=1}P_{6i+6}(1/s),\qquad s^2=-3.
$$
R784 (784.27) 已给该权的准确运输，本记录没有证明其泛函非零，
也没有将不同标签的单位拼接。原主目标及真实高度排除均未完成。

## 7. 已有证书排除一个过强的反射猜想

直接读取已完成的 [R702 p41证书](R702-prime41.json)，不运行新计算，得到
$A_{35}=0$、$A_2=1$、$A_{32}=15$。
依原 R697/R770 的非零单位归一，$p=41$、$N=6$ 时
前两项分别给 $f_5=0$ 与 $g_0=1$。
所以 $f_i$ 与 $g_{N-1-i}$ 的零支撑并不相同；
不能假定 Frobenius 将这一对系数按逐标签单位倍反射。

这不是只出现在被原筛排除的标签上：
[R739 (739.2)、(739.10)](../results/R739-exact-original-p47-and-p41-valuation-continuation.md)
已经准确证明 $h=37$ 满足 $(37,42)=1$，且
$$
N_{37}\equiv33\ne0,\qquad
P_{36}(1/s)=19/9\ne0\quad\text{于 }\mathbf F_{41}.
$$
因此 $i=5$ 属于真正的 primitive/Legendre 可见集合，
仍有 $f_5=0$、$g_0=1$。R739 还给实际
$v_{41}(M_{2,37})=-1$，不能把这一非最小赋值冒认成
R770 三单位所给的 $-2$。所以将逐项单位反射仅限制到可见集合，
也不能挽救该猜想。

同一证书的 $A_{32}\ne0$ 与原 $f_0=1$ 给另一端
$f_0g_5\ne0$，但其原标签 $h=7$ 在 $p+1=42$ 时并不本原。
这只说明筛选不可丢掉，不将固定 $p=41$ 的既有数据重开为新数值窗口。
R788 的完整跨 $p$ 修正式与 Schur 耦合继续成立，真正筛后共同非零仍待。

## 依赖

- [R760](../results/R760-original-critical-sigma-jets-from-four-digit-division-data.md)，原换参、低阶整性和同标签定义。
- [R765](../results/R765-first-obstructed-sigma-coefficient-and-Cartier-unit-residual.md)，原首 pole 和单位残差。
- [R770](../results/R770-same-primitive-label-square-and-finite-bilinear-pairing.md)，原二阶残差换参和 primitive／Legendre 接口。
- [R782](../results/R782-original-sigma-six-Hirota-square-addition-kernel.md)，原十二阶常数及完整恒等式。
- [R784](../results/R784-original-full-sigma-kernel-and-primitive-preserving-left-inverse.md)，原六秩三通道及正确权运输。
- [R739](../results/R739-exact-original-p47-and-p41-valuation-continuation.md)，真正可见标签 $p=41,h=37$ 的原范数和准确赋值反例。
