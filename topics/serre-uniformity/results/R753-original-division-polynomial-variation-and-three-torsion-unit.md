# R753：原除法多项式模 $p^2$ 的完整微分变分与三挠点首单位

**状态：已证明。** 本文固定原曲线 $E_0:y^2=x^3-1$，给所有素数
$p\equiv5\pmod6$ 的标准除法多项式 $\psi_p$ 的一个精确模 $p^2$ 变分，
并确定其在原三挠点 $x=0$ 附近的第一个非恒定系数。
证明是全素数的代数恒等式，没有以有限计算代替推导。

所得单位是 $\psi_p$ 的 $x^{p+1}$ 变分系数。本文没有把它识别为
R697/R698 的原 $C_p$ 或 $A_p$，也不声称原两个 Cartier 系数同时为单位。
相反，完整微分恒等式精确留下 $(p-5)/6$ 个 Frobenius 常数系数；
这些数据不能由同一微分恒等式恢复。

## 1. 标准原规范与结论

始终令
$$
E_0:\ y^2=x^3-1,\qquad
\omega=\frac{dx}{2y},\qquad
D=2y\frac{d}{dx}.
\tag{753.1}
$$
在原复一致化中 $x=\wp(z)$、$y=\wp'(z)/2$，故 $D=d/dz$；
不改变原微分，也不把曲线换成另一个六次扭曲。

$\psi_n$ 取标准整除法多项式规范：
$$
\begin{aligned}
&\psi_0=0,\quad \psi_1=1,\quad\psi_2=2y,\\
&\psi_3=3x^4-12x,\\
&\psi_4=4y(x^6-20x^3-8),\\
&\psi_{2m+1}=\psi_{m+2}\psi_m^3-\psi_{m-1}\psi_{m+1}^3
\quad(m\ge2),\\
&\psi_{2m}=\frac{\psi_m}{2y}
  \left(\psi_{m+2}\psi_{m-1}^2-\psi_{m-2}\psi_{m+1}^2\right)
\quad(m\ge3).
\end{aligned}
\tag{753.2}
$$
商在曲线坐标环中是整多项式。另置
$$
\phi_n=x\psi_n^2-\psi_{n+1}\psi_{n-1},
\qquad
x([n]P)=\frac{\phi_n(x(P))}{\psi_n(x(P))^2}.
\tag{753.3}
$$
对奇数 $n$，$\psi_n\in\mathbf Z[x]$，次数为 $(n^2-1)/2$、
首系数为 $n$；$\phi_n\in\mathbf Z[x]$ 首一，次数为 $n^2$。

以下固定
$$
p=6N+5,\qquad q=p^2,\qquad
R=\frac{p^2-1}{2},\qquad r=\frac{p-1}{2}.
\tag{753.4}
$$

**定理 753.1。** 对每个上述素数，有
$$
\psi_p\equiv-1\pmod p,\qquad
\phi_p\equiv x^{p^2}\pmod p.
\tag{753.5}
$$
因此
$$
H_p=\frac{\psi_p+1}{p}\in\mathbf Z[x],\qquad
\Phi_p=\frac{\phi_p-x^{p^2}}p\in\mathbf Z[x],
\quad \deg H_p=R,\quad \deg\Phi_p<p^2.
\tag{753.6}
$$
在 $\mathbf F_p[x]$ 中精确成立
$$
\boxed{\;
\Phi_p'(x)+2x^{p^2}H_p'(x)
=-(x^3-1)^R.
\;}
\tag{753.7}
$$

记 $h_k=[x^k]\overline H_p$。对于 $1\le k\le R$ 且 $p\nmid k$，
$$
\boxed{\;
2k h_k=-[x^{p^2+k-1}](x^3-1)^R.
\;}
\tag{753.8}
$$
特别地，$3\nmid k$ 时 $h_k=0$；若 $3\mid k$，则
$$
\boxed{\;
h_k=-\frac{(-1)^{R-j}}{2k}\binom Rj,\qquad
j=\frac{p^2+k-1}{3}.
\;}
\tag{753.9}
$$
这些公式中的整数及逆元均在 $\mathbf F_p$ 中理解。

第一个非恒定系数为
$$
h_k=0\quad(1\le k<p+1),\qquad
\boxed{\;
h_{p+1}=-\frac12\binom{(p-1)/2}{(p+1)/3}\ne0
\quad\text{于 }\mathbf F_p.
\;}
\tag{753.10}
$$
原常数也精确已知：
$$
\boxed{\;
\psi_p(0)=-(-4)^{(p^2-1)/6}.
\;}
\tag{753.11}
$$
合并可在 $\mathbf Z_{(p)}[x]$ 中写成
$$
\boxed{\;
\psi_p(x)\equiv
-(-4)^{(p^2-1)/6}
-\frac p2\binom{(p-1)/2}{(p+1)/3}x^{p+1}
\pmod{(p^2,x^{p+4})}.
\;}
\tag{753.12}
$$

式 (753.8) 确定所有非 $p$ 倍数指数的模 $p$ 变分。
除去 (753.11) 已知的常数后，该微分输入本身留下且只留下
$$
x^{3p},x^{6p},\ldots,x^{3Np}
\tag{753.13}
$$
这 $N$ 个方向。此处“留下”是说这些项对 (753.7) 的贡献均为零，
并非说实际 $\psi_p$ 的对应系数可任意改变而仍是一条除法多项式。

## 2. 三挠点上精确的原除法值

先在 $E_b:y^2=x^3+b$、$b\ne0$ 上，取
$$
P_b=(0,y_0),\qquad y_0^2=b,\qquad c=2y_0.
$$
切线 $y=y_0$ 与曲线在 $P_b$ 三重相交，所以 $P_b$ 为非零三挠点。
由标准初值，
$$
\psi_1(P_b)=1,\quad
\psi_2(P_b)=c,\quad
\psi_3(P_b)=0,\quad
\psi_4(P_b)=-c^5.
\tag{753.14}
$$
定义周期六的符号
$$
\epsilon_n=
\begin{cases}
 1,&n\equiv1,2\pmod6,\\
-1,&n\equiv4,5\pmod6,\\
 0,&n\equiv0,3\pmod6.
\end{cases}
$$
则对所有 $n\ge1$，
$$
\psi_n(P_b)=
\begin{cases}
0,&3\mid n,\\
\epsilon_n\,c^{(n^2-1)/3},&3\nmid n.
\end{cases}
\tag{753.15}
$$

为说明此式没有隐藏的除三或零分母问题，可直接用 (753.2) 归纳。
偶数递推的唯一分母是 $c\ne0$；对于奇数 $2m+1$：

- $m\equiv1\pmod3$ 时两项各含一个三倍指标，故均为零；
- $m\equiv0\pmod3$ 时只剩第二项；
- $m\equiv2\pmod3$ 时只剩第一项。

后两种情形的 $c$ 指数都为
$((2m+1)^2-1)/3$，周期六符号分别给原 $\epsilon_{2m+1}$。
对于偶数 $2m$，$3\mid m$ 时外因子为零；其余两类的括号各只有一项非零，
其乘上 $\psi_m/c$ 后的指数为 $((2m)^2-1)/3$，
符号分别为 $+1$（$m\equiv1\pmod3$）和 $-1$（$m\equiv2\pmod3$），
即 $\epsilon_{2m}$。初值 (753.14) 完成归纳。
因此只在指数本来为整数的非零情形使用幂式。

对 $b=-1$、$n=p\equiv5\pmod6$，
$\epsilon_p=-1$，而 $(p^2-1)/3$ 是偶数，得到
$$
\psi_p(0)
=-c^{(p^2-1)/3}
=-(c^2)^{(p^2-1)/6}
=-(-4)^{(p^2-1)/6}.
$$
这证明 (753.11)。因为 $(p^2-1)/6=(p-1)(p+1)/6$ 是 $p-1$ 的倍数，
Fermat 恒等式又给
$$
\psi_p(0)\equiv-1\pmod p.
\tag{753.16}
$$
所以原 $\psi_p$ 在特征 $p$ 的约化不是零多项式。

## 3. 原超奇异 Frobenius 与模 $p$ 规范

因为 $p\equiv2\pmod3$，$x\mapsto x^3$ 是 $\mathbf F_p$ 的双射。
若 $\chi$ 是二次特征并置 $\chi(0)=0$，则
$$
\#E_0(\mathbf F_p)
=1+\sum_{x\in\mathbf F_p}(1+\chi(x^3-1))
=p+1+\sum_{t\in\mathbf F_p}\chi(t-1)
=p+1.
\tag{753.17}
$$
因此 $p$ 次 Frobenius $\pi:(x,y)\mapsto(x^p,y^p)$ 的迹为零。
Frobenius 的标准特征恒等式给
$$
\pi^2+[p]=0,\qquad
[p]=-\pi^2.
\tag{753.18}
$$
从而在约化曲线函数域中
$$
x([p]P)=x^{p^2},\qquad y([p]P)=-y^{p^2}.
\tag{753.19}
$$

下面用单项次数固定 $\psi_p$ 的符号，而不只断言“超奇异所以常数”。
由 (753.16)，(753.3) 的分母在 $\mathbf F_p[x]$ 中不是零；
结合 (753.19)，
$$
\overline\phi_p=x^{p^2}\overline\psi_p^{\,2}.
\tag{753.20}
$$
标准 $\phi_p$ 首一且次数 $p^2$。此事实也可从 (753.3) 的最高项直接看出：
$x\psi_p^2$ 的最高项系数为 $p^2$，
$\psi_{p+1}\psi_{p-1}$ 的最高项系数为 $p^2-1$，
所以差的最高项恰为 $x^{p^2}$。
若 $\overline\psi_p$ 非恒定，(753.20) 右边次数严格大于 $p^2$，矛盾。
它是非零常数，再由 $x=0$ 的 (753.16)，必为 $-1$。
于是 $\overline\phi_p=x^{p^2}$，证明 (753.5) 和 (753.6)。

这里保留了原 $y$ 的符号：(753.18) 是负的二次 Frobenius，
故 (753.19) 第二式是 $-y^{p^2}$。后面的变分负号由此决定。

## 4. 模 $p^2$ 的完整微分恒等式

写
$$
X_p=x\circ[p],\qquad Y_p=y\circ[p].
$$
原不变微分满足 $[p]^*\omega=p\omega$，所以在特征零函数域中
$$
D X_p=2pY_p.
\tag{753.21}
$$
由 $\psi_p=-1+pH_p$，
$$
\psi_p^2\equiv1-2pH_p\pmod{p^2},
\qquad
\psi_p^{-2}\equiv1+2pH_p\pmod{p^2}.
$$
因原分母模 $p$ 为单位，这些式子可以在曲线坐标环的模 $p^2$ 局部化中使用。
于是
$$
X_p=\frac{x^{p^2}+p\Phi_p}{(-1+pH_p)^2}
\equiv x^{p^2}+p\bigl(\Phi_p+2x^{p^2}H_p\bigr)
\pmod{p^2}.
\tag{753.22}
$$
求 $D=2y\,d/dx$ 导数时，$D(x^{p^2})=2p^2yx^{p^2-1}$ 在模 $p^2$ 下为零，
括号内 $D(x^{p^2})$ 产生的项更有外因子 $p$。
因此
$$
D X_p\equiv
2py\bigl(\Phi_p'+2x^{p^2}H_p'\bigr)\pmod{p^2}.
\tag{753.23}
$$
另一方面 (753.19)、(753.21) 给
$$
D X_p\equiv-2p y^{p^2}\pmod{p^2}.
\tag{753.24}
$$
先在 $\mathbf Z_{(p)}$ 的局部化中消去公共因子 $2py$，
再约化模 $p$，得到
$$
\Phi_p'+2x^{p^2}H_p'
=-y^{p^2-1}
=-(x^3-1)^{(p^2-1)/2}.
$$
两边已是 $\mathbf F_p[x]$ 的多项式，故该函数域恒等式就是 (753.7)。
消去 $y$ 仅用于证明恒等式；最终结果在所有 $x$ 上成立，
没有去掉三挠点、二挠点或无穷远的额外假设。

## 5. 全部可见系数与 Frobenius 常数核

由于 $\deg\Phi_p<p^2$，$\Phi_p'$ 没有 $x^{p^2}$ 及更高次数项。
在 (753.7) 中取 $x^{p^2+k-1}$ 系数，得到
$$
2k[x^k]\overline H_p
=-[x^{p^2+k-1}](x^3-1)^R.
$$
当 $p\nmid k$ 时可以除 $2k$，这给 (753.8)。
右边只含三的倍数次数；由于 $p^2\equiv1\pmod3$，
其可能非零当且仅当 $3\mid k$。
若 $3\mid k$，按二项式展开取 $j=(p^2+k-1)/3$，
即得 (753.9)。

原 $\psi_p$ 事实上属于 $\mathbf Z[x^3]$。例如从原整递推的加权齐次性可看出：
在一般 $y^2=x^3+Ax+B$ 上令
$\operatorname{wt}(x,y,A,B)=(2,3,4,6)$，
则 $\psi_n$ 的权为 $n^2-1$。
令 $A=0$ 后，奇数 $\psi_p$ 的每项为 $x^iB^j$，
且 $2i+6j=p^2-1$；因 $p^2-1$ 被六整除，必有 $3\mid i$。
于是 $H_p\in\mathbf Z[x^3]$。

微分算子在 $\mathbf F_p[x]$ 的核恰为 $\mathbf F_p[x^p]$；
与 $\mathbf F_p[x^3]$ 相交后，核恰为 $\mathbf F_p[x^{3p}]$。
所以在次数至多 $R$ 的范围内，(753.7) 所留下的 $H_p$ 方向正是
$$
1,\ x^{3p},\ x^{6p},\ldots,
x^{3p\lfloor R/(3p)\rfloor}.
$$
而
$$
\left\lfloor\frac{R}{3p}\right\rfloor
=\left\lfloor\frac{p^2-1}{6p}\right\rfloor
=N.
\tag{753.25}
$$
常数由 (753.11) 精确确定后，只剩 (753.13) 的 $N$ 个方向。

此“正是”有双向意义：凡两个 $H$ 在所有非 $p$ 倍数指数有相同系数，
它们的差在该核中；反过来，任意加上该核中的多项式，保持同一 $\Phi$，
(753.7) 都不会改变。我们没有声称这些修改保持乘法映射或除法递推。
因此这准确说明本微分信息的可辨识范围。

## 6. 首非恒定项及原 Hasse 导数比例

写
$$
p=6N+5,\qquad r=3N+2,\qquad
R=r+rp.
\tag{753.26}
$$
若 $k=3\ell$ 且 $1\le k<p+1$，则 $1\le\ell\le2N+1$。
此时
$$
j=\frac{p^2-1}{3}+\ell
=(2N+1)p+(4N+3+\ell),
\tag{753.27}
$$
末位满足
$$
r=3N+2<4N+3+\ell\le6N+4=p-1.
$$
由模 $p$ 二项式恒等式
$(1+X)^R=(1+X)^r(1+X^p)^r$，
也就是该两位情形的 Lucas 公式，
$$
\binom Rj
\equiv\binom r{2N+1}\binom r{4N+3+\ell}=0\pmod p.
\tag{753.28}
$$
式 (753.9) 因而给这些 $h_k=0$。
这个范围内唯一的正 $p$ 倍数指数为 $p$，但 $3\nmid p$，
已经由 $H_p\in\mathbf Z[x^3]$ 排除；所以没有漏掉不可除的 $k=p$。

在首个可能指数 $k=p+1=6N+6$，
$$
j=\frac{p(p+1)}3=p(2N+2),\qquad
R-j=\frac{(p-3)(p+1)}6=2(3N+1)(N+1)
$$
为偶数。于是
$$
\binom Rj\equiv\binom r{2N+2},\qquad
2k\equiv2\pmod p,
$$
从而
$$
h_{p+1}=-\frac12\binom{3N+2}{2N+2}.
$$
分子分母中的所有阶乘都小于 $p$；且 $0\le2N+2\le3N+2<p$，
所以该值非零，完成 (753.10)。
再利用三次支撑，$p+1$ 后下一个可能指数为 $p+4$，
所以 (753.11) 和 (753.10) 合并确实给模理想 $(p^2,x^{p+4})$ 的 (753.12)。

为了说明这个单位与原超奇异变形的关系，定义通常的 Hasse 系数多项式
$$
\mathcal A_p(A,B)
=[x^{p-1}](x^3+Ax+B)^{(p-1)/2}.
\tag{753.29}
$$
对 $A$ 求一次导数、再置 $A=0,B=-1$，只有选取一次 $Ax$、
$2N+1$ 次 $x^3$ 和 $N$ 次 $B$ 的项贡献，故
$$
\partial_A\mathcal A_p(0,-1)
=(-1)^N\frac{(3N+2)!}{(2N+1)!\,N!}.
\tag{753.30}
$$
此值同样为模 $p$ 单位，而且
$$
\boxed{\;
h_{p+1}
=-\frac32(-1)^N\,\partial_A\mathcal A_p(0,-1)
\pmod p.
\;}
\tag{753.31}
$$
确实，
$\binom{3N+2}{2N+2}=(-1)^N
\partial_A\mathcal A_p(0,-1)/(2N+2)$，
而 $2N+2=(p+1)/3\equiv1/3\pmod p$。
这给出了同一原曲线、同一 $x$ 坐标的精确比例，没有仅凭权重匹配。

## 7. 对原 sigma 路线已经给出的内容与尚缺的桥

原 $x=0$ 的两点是 $P_\pm=(0,\pm i)$，均为非零三挠点。
$p\ge5$ 时 $2y(P_\pm)$ 是单位，所以 $x$ 是各点的整局部参数。
因此 (753.12) 是原三挠点的真实局部展开：
原 $\psi_p$ 的常数精确，模 $p^2$ 首非恒定项恰在 $x^{p+1}$，
其除以 $p$ 后的系数为单位。

R697/R698 的临界对象则固定为无穷远 $O$ 的同一原对数参数 $z$ 下
$x\sigma(z)^6$、$-xy\sigma(z)^6$ 的指定导数，
并保留六挠标记、三次角色和阶乘。
对于奇数 $p$，标准恒等式
$$
\psi_p(\wp(z))=\frac{\sigma(pz)}{\sigma(z)^{p^2}}
$$
只提供函数之间的准确关系；它本身不把三挠点的
$x^{p+1}$ 系数变成 $O$ 处的临界 $(p-1)$ 阶截面导数。
移动展开中心时必须保留 sigma 的平移指数、原微分和每个 $p$ 分母。

尤其，(753.13) 的 Frobenius 常数项对全部已用微分信息不可见。
没有另外求出这些项及原截面的转换，不能把 (753.31) 的 Hasse 导数单位
称为原 $C_p$ 单位。本文也没有构造 $C_p$ 的反例。
它给后续的确切输入是：

1. 原 $\psi_p\bmod p^2$ 的全部非 $p$ 倍数指数系数由 (753.9) 显式给出；
2. 在原三挠点的首变分是已证明的单位，比例为 (753.31)；
3. 剩余待确定的线性数据恰是原 $N=(p-5)/6$ 个 $x^{3p\ell}$ 系数；
4. 原同一真本原 $h$ 的 $N_h,C_{h-2},C_{p-h-2}$ 同时单位，以及其全素数结论，
   仍需独立的原参数桥接。

## 来源与依赖

- Joseph H. Silverman, *The Arithmetic of Elliptic Curves*, second edition,
  Graduate Texts in Mathematics 106, Springer, 2009：
  Exercise III.3.7 给标准除法多项式、整性、最高项和乘法映射；
  Theorem V.2.3.1 给 Frobenius 的特征恒等式。
  [出版社 DOI](https://doi.org/10.1007/978-0-387-09494-6)；
  [公开全文](https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf)。
  本文所需的符号、模 $p^2$ 变分和所有系数计算均在上文完整推导。
- 原截面与原系数定义沿用 R697、R698；本结果不修改它们，也不依赖任何新有限窗口。

