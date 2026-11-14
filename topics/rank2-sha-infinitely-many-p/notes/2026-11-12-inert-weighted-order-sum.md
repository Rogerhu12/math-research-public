# 惰性素数的加权阶数和：无条件 $O(\log k)$ 与显式常数

日期：2026-11-12。**状态：本文估计已证明；仍未达到主问题的算术阈值。**

前篇需要控制
$$
\sum_{\substack{p\equiv3\pmod4\\D_p\le k}}
\frac{c_p\log p}{D_p-1}.
$$
本篇把这一截断和无条件界为显式常数乘 $\log k$。
这里控制了全部惰性素数，不要求 GRH、非 Wieferich 猜想或接近最大阶数。

## 1. 固定底数、阶数和深度

设 $b\in\mathbb Z[i]$，
$$
A=b\bar b>1,
\qquad b/\bar b\text{ 不是根单位}.
\tag{1.1}
$$
对 $p\equiv3\pmod4$、$p\nmid2A$，采用 $v_p(p)=1$，定义
$$
\begin{aligned}
d_p&=\operatorname{ord}_{\mathbb F_{p^2}^{\times}}(b),&
D_p&=\operatorname{lcm}(d_p,2),\\
c_p&=v_p(b^{d_p}-1),&
a_p&=\operatorname{ord}_{\mathbb F_p^{\times}}(A),\\
r_p&=\operatorname{ord}_{\mathbb F_{p^2}^{\times}}(\bar b/b).
\end{aligned}
\tag{1.2}
$$
有 $c_p\ge1$、$a_p\mid p-1$、$r_p\mid p+1$。
删除任意固定有限素数集合不影响下面的主常数。

记
$$
M_b(k)=\sum_{\substack{p\equiv3\pmod4,\ p\nmid2A\\D_p\le k}}c_p\log p,
\qquad
W_b(k)=\sum_{\substack{p\equiv3\pmod4,\ p\nmid2A\\D_p\le k}}
\frac{c_p\log p}{D_p-1}.
\tag{1.3}
$$
每个固定 $k$ 的和有限，因为 $d_p\le D_p\le k$ 迫使 $p$ 整除
某个固定非零 Gaussian 整数 $b^d-1$，$d\le k$。

**主结论。** 令
$$
\boxed{C_b=\frac{\sqrt3+1/\sqrt2}{\pi^2}\log A.}
\tag{1.4}
$$
则当 $k\ge2$ 时，
$$
\boxed{M_b(k)\le C_bk+O_b(\sqrt k\log^2(k+2)),}
\tag{1.5}
$$
以及
$$
\boxed{W_b(k)\le C_b\log k+O_b(1).}
\tag{1.6}
$$
式 (1.4) 中的 $\pi$ 是圆周率。

## 2. 两个较小阶数的准确分解

惰性处有 $\bar b\equiv b^p\pmod p$。
所以在阶数为 $d=d_p$ 的循环群中，
$$
A\equiv b^{p+1},\qquad \bar b/b\equiv b^{p-1},
$$
从而
$$
a=a_p=\frac d{\gcd(d,p+1)},\qquad
r=r_p=\frac d{\gcd(d,p-1)}.
\tag{2.1}
$$
因为 $d\mid(p-1)(p+1)$、$\gcd(p-1,p+1)=2$，逐素因子比较得
$$
ar\in\{d,d/2\}.
\tag{2.2}
$$
尤其 $ar\le d$，不是只用较弱的 $ar\le2d$。

惰性条件还给更准确的二分。写 $v_2(p+1)=v\ge2$、$x=v_2(d)$。

- 若 $0\le x\le v$，则 $a$ 为奇数，并且 $D=2ar$。
- 若 $x=v+1$，则 $v_2(a)=1$、$4\mid r$，并且 $D=ar$。

第一种情形在 $x=0$ 时由 $d=ar,D=2d$ 得到；
在 $1\le x\le v$ 时由 $ar=d/2,D=d$ 得到。
第二种情形由 (2.1) 逐个取二阶赋值得到。
故
$$
\boxed{
\begin{array}{c|c|c}
&\text{阶数限制}&D_p\\ \hline
a_p\text{ 奇}&r_p\text{ 任意}&2a_pr_p\\
a_p\text{ 偶}&v_2(a_p)=1,\quad4\mid r_p&a_pr_p
\end{array}}
\tag{2.3}
$$

## 3. 深度由固定的两条幂序列控制

复共轭保持惰性赋值，故 $\bar b^d\equiv b^d\equiv1\pmod{p^{c_p}}$。
相乘或相除，分别得到
$$
v_p(A^d-1)\ge c_p,\qquad
v_p((\bar b/b)^d-1)\ge c_p.
$$
$p\nmid d$，而 $a,r\mid d$，提升指数公式于是给
$$
\boxed{
c_p\le v_p(A^{a_p}-1),\qquad
c_p\le v_p(\bar b^{r_p}-b^{r_p}).}
\tag{3.1}
$$
第二式中 $b$ 是局部单位，故乘以 $b^{r_p}$ 不改变赋值。

令 $\Phi_n(X,Y)$ 为齐次圆分多项式，$\Phi_n(X)=\Phi_n(X,1)$。
因为 $a_p$、$r_p$ 都素于 $p$，阶数的定义及分解
$X^n-Y^n=\prod_{d\mid n}\Phi_d(X,Y)$ 表明
$$
\begin{aligned}
c_p&\le v_p(\Phi_{a_p}(A)),\\
c_p&\le v_p(\Phi_{r_p}(\bar b,b)).
\end{aligned}
\tag{3.2}
$$
在右边较小的真因子上，剩余阶数不匹配，所以赋值为零。
这使每个素数只需使用其实际 primitive 因子，而不必重复计入所有倍数。

对 $n>1$，$\Phi_n(b,\bar b)$ 是非零有理整数：它为代数整数，
齐次圆分多项式的对称性使其被共轭固定；非零性由 (1.1) 保证。
$n=1$ 的有限例外只给 $O_b(1)$，因为其素因子整除固定的 $b-\bar b$。
所以对任意阶数集合 $I,J$，
$$
\begin{aligned}
\sum_{p:\ a_p\in I}c_p\log p
&\le\sum_{n\in I}\log\Phi_n(A),\\
\sum_{p:\ r_p\in J}c_p\log p
&\le\sum_{n\in J}\log|\Phi_n(b,\bar b)|+O_b(1).
\end{aligned}
\tag{3.3}
$$
这里左边可进一步限制到任意惰性素数子集。
若改用理想范数，惰性位满足 $N(p)=p^2$，左右都出现因子二，
得到的仍是 (3.3)，没有丢失惯性次数。

## 4. Primitive 因子的总高度

对整数 $A>1$，Möbius 乘积公式给
$$
\log\Phi_n(A)=\varphi(n)\log A+O_A(1).
\tag{4.1}
$$
误差一致有界，因为它的绝对值不超过
$\sum_{d\ge1}|\log(1-A^{-d})|<\infty$。

对 $b,\bar b$，Stewart，*On divisors of Lucas and Lehmer numbers*，
Acta Math. **211** (2013)，Lemma 4.1，p.303，式 (4.3) 给
$$
\log|\Phi_n(b,\bar b)|
=\frac{\varphi(n)}2\log A
+O_b(2^{\omega(n)}\log(n+1)).
\tag{4.2}
$$
所需假设逐项成立：$(b+\bar b)^2$ 与 $b\bar b$ 为非零整数，
$b/\bar b$ 不是根单位，且 $|b|=|\bar b|=\sqrt A>1$。
这里使用的是固定次数、固定代数数的复对数估计；
并非把变化的 $p$-division 域代入常数。
其证明在原文由固定代数数的 Baker 下界和 Möbius 乘积公式给出。

因为 $2^{\omega(n)}\le\tau(n)$，且
$\sum_{n\le x}\tau(n)\le x(1+\log x)$，(4.2) 的累计误差为
$O_b(x\log^2(x+2))$。

下面四个 totient 和都有误差 $O(x\log(x+2))$：
$$
\begin{aligned}
\sum_{n\le x}\varphi(n)&=\frac3{\pi^2}x^2+O(x\log(x+2)),\\
\sum_{\substack{n\le x\\n\text{ 奇}}}\varphi(n)
&=\frac2{\pi^2}x^2+O(x\log(x+2)),\\
\sum_{\substack{n\le x\\v_2(n)=1}}\varphi(n)
&=\frac1{2\pi^2}x^2+O(x\log(x+2)),\\
\sum_{\substack{n\le x\\4\mid n}}\varphi(n)
&=\frac1{2\pi^2}x^2+O(x\log(x+2)).
\end{aligned}
\tag{4.3}
$$
为说明常数：由 $\varphi(n)=n\sum_{d\mid n}\mu(d)/d$，全和的主项为
$\frac12x^2\sum\mu(d)/d^2=3x^2/\pi^2$。
奇数和使用 $\sum_{m\le y,m\text{ 奇}}m=y^2/4+O(y)$，主项为
$\frac14x^2\prod_{\ell\ne2}(1-\ell^{-2})=2x^2/\pi^2$。
第三式把 $n=2m$、$m$ 奇代入第二式，第四式由前三式相减。

故 (3.3) 的四种预算为
$$
\begin{aligned}
N_{\rm odd}(x)&:=\sum_{\substack{n\le x\\n\text{ 奇}}}\log\Phi_n(A)
=\frac{2\log A}{\pi^2}x^2+O_A(x\log(x+2)),\\
N_{2\rm odd}(x)&:=\sum_{\substack{n\le x\\v_2(n)=1}}\log\Phi_n(A)
=\frac{\log A}{2\pi^2}x^2+O_A(x\log(x+2)),\\
R_{\rm all}(y)&:=\sum_{n\le y}\log|\Phi_n(b,\bar b)|
=\frac{3\log A}{2\pi^2}y^2+O_b(y\log^2(y+2)),\\
R_4(y)&:=\sum_{\substack{n\le y\\4\mid n}}\log|\Phi_n(b,\bar b)|
=\frac{\log A}{4\pi^2}y^2+O_b(y\log^2(y+2)).
\end{aligned}
\tag{4.4}
$$
低阶常数项统一并入误差。

## 5. 可调阈值与常数优化

先考虑 $a_p$ 为奇数且 $D_p\le k$。
由 (2.3)，$a_pr_p\le k/2$。
对任意 $x>0$，这类素数或满足 $a_p\le x$，或满足 $r_p\le k/(2x)$。
所以其加权质量至多为
$$
N_{\rm odd}(x)+R_{\rm all}(k/(2x))+O_b(1).
$$
取
$$
x=\frac{3^{1/4}}2\sqrt k,
$$
两项的二次主项相等，给
$$
\sum_{\substack{p:\ D_p\le k\\a_p\text{ 奇}}}c_p\log p
\le\frac{\sqrt3\log A}{\pi^2}k
+O_b(\sqrt k\log^2(k+2)).
\tag{5.1}
$$

再考虑 $a_p$ 为偶数。
此时 $v_2(a_p)=1$、$4\mid r_p$，且 $a_pr_p=D_p\le k$。
因此质量至多为
$$
N_{2\rm odd}(x)+R_4(k/x)+O_b(1).
$$
取 $x=2^{-1/4}\sqrt k$，得到
$$
\sum_{\substack{p:\ D_p\le k\\a_p\text{ 偶}}}c_p\log p
\le\frac{\log A}{\sqrt2\pi^2}k
+O_b(\sqrt k\log^2(k+2)).
\tag{5.2}
$$
相加就是 (1.5)。

这也说明为何没有只用“对每个固定阶数的公因子小”这一逐项说法：
这里用 $a_pr_p$ 的乘积约束，以两个可调阈值覆盖整个素数集合，
直接得到全体质量的线性上界。

## 6. 分部求和

$D_p\ge2$，所以 Stieltjes 分部求和给
$$
W_b(k)=\frac{M_b(k)}{k-1}
+\int_2^k\frac{M_b(t)}{(t-1)^2}\,dt.
\tag{6.1}
$$
主项贡献 $C_b\log k+O_b(1)$。
误差的积分收敛，因为
$$
\int_2^\infty\frac{\sqrt t\log^2(t+2)}{(t-1)^2}\,dt<\infty.
$$
于是得到 (1.6)。没有丢掉 $c_p$：任意高的 Wieferich 深度已包含在 (3.2) 的赋值预算中。

## 7. 对现有图像的实际意义

加法逆像的惰性图像估计为
$$
s_p(k)\le\frac1{p^2-1}+\frac{m c_p}{D_p-1}
\quad(D_p\le k),
$$
而 $D_p>k$ 时该截断整。
因此其 $\mathbb Q$-迹图像的全部惰性位，确实满足
$$
\boxed{\mathcal B_{\rm inert}(k)
\le m C_b\log k+O_{b,m}(1).}
\tag{7.1}
$$
这是一个实际 jet 高度充分量的上界；不只是逐点对数非零或单独收敛半径。
在惰性处，共轭保持 $d_p,D_p,c_p$，所以取迹不增加这项上界。

数值仅用于解释已证明常数的大小：

| 固定 $b$ | $N(b)$ | $C_b$ | $4C_b$ |
|---|---:|---:|---:|
| $35+34i$ | $2381$ | $1.9215687189\ldots$ | $7.6862748758\ldots$ |
| $2+i$ | $5$ | $0.3977538043\ldots$ | $1.5910152173\ldots$ |

Herblot 的原 $\mathbb Q$-迹曲面门槛为 $\alpha<1/4$。
即便使用较小的 $b=2+i$，$m=4$ 时本篇可证上界的惰性项本身也没有小到该预算内，
且普通位的额外共振尚须另行计算。
这只是说**当前上界不足**，并不证明真实的算术常数大于 $1/4$。
在偶性商中增长阶数减半，但同一系数界的算术常数约加倍，不能改变这一比较。

## 8. 为什么可合法改用 $b=2+i$

原加法笔记取 $b\equiv1\pmod f$，以简化留数说明。
代数障碍的稳定覆盖证明实际只需 $(b,f)=1$。
把固定极点支撑扩大为 $S^*=E[f]$，则 $[b]$ 在 $S^*$ 上为双射。
RHS 的所有极点仍在其中，有限极点引理和稳定覆盖的下降证明逐字成立。

普通处的局部中心比较也只需塔中满足 $\rho_E(\sigma_b)=b$ 的 Galois 元。
满的 $\pi$-division 塔给出这个元素，Coleman 作用就是 $t\mapsto[b](t)$。
不必把它认作固定理想 $(b)$ 的 Frobenius。
因此 $\sigma_b-b$ 的中心因子与非 Wieferich 单位商比较，不要求 $b\equiv1\pmod f$。

取 $b=2+i$ 时，$N(b)=5$ 与 $N(f)=2^3\cdot17^2$ 互素，
$b/\bar b=(3+4i)/5$ 不是根单位，且 $(b,\bar b)=1$。
所以本篇及加法局部整性估计的全部假设成立。

### 8.1 保留 $\mathbb Q$-迹的非代数性

为了不把旧的“逐点固定”留数式原样搬来，下面给出有限轨道版本。
令 $B$ 为 $[b]$ 在 $S^*$ 上的置换，令
$r(s)=\operatorname{Res}_s\ell\omega_E$，在非极点处定义为零。
这是一个非零向量。因为 $|b|>1$，有限维算子 $1-b^{-1}B$ 可逆。
因此存在 $s\in S^*$，使
$$
L_s=\sum_{j\ge0}r([b]^js)b^{-j}\ne0.
\tag{8.1}
$$
这里的数列为周期数列，级数绝对收敛；它等于一个有限和除以 $1-b^{-L}$。
原点的整条轨道留数为零，故可选 $s\ne O$。

取 $s$ 的复对数 $z_s=\Omega\eta/f$，并用 CRT 使
$\eta\equiv1\pmod{b\bar b}$。
在 $z_n=b^{m+n}z_s$ 处，恰好前 $n+1$ 层可能有极点；
后层若有极点就迫使 $b\mid\eta$。
其总留数为
$$
A_n=b^m\sum_{j=0}^n\binom{m+j-1}{j}b^j
r([b]^{n-j}s),
$$
并且
$$
\frac{A_n}{b^{m+n}\binom{m+n-1}{n}}
\longrightarrow L_s\ne0.
\tag{8.2}
$$
证明同样是有界周期系数与几何级数的支配收敛。
因此留数绝对值无界。
限制 $n$ 到一个同余类，使 $[b]^{m+n}s$ 为固定点。
共轭逆像的任何一层若在 $z_n$ 有极点，就迫使
$\bar b\mid b^{m+n}\eta$，与互素性矛盾。
所以 $F_b+\overline F_b$ 的留数仍无界，不能满足该固定基点上的有限个代数 Laurent 分支。
这证明其 $\mathbb Q$-迹仍超越。
二阶复增长的证明没有使用逐点固定，故 Herblot 的同一阈值接口也保留。

## 9. Primitive 因子和公因子界还没有给出的改进

Primitive 因子已经用于 (3.2)，它把未去重的二次总高度常数有效降低。
二进阶数分拆再给 (1.4)，但尚未把 $M_b(k)$ 改进为 $o(k)$。

若能证明 $M_b(k)=o(k)$，则 (6.1) 立即给 $W_b(k)=o(\log k)$，
惰性部分将不再贡献正的 $\alpha$ 常数。
单独对每一对 $(a,r)$ 引用一个 $S$-unit gcd 的小量界不能直接做到这一点：
需要控制 $ar\le k$ 区域内的全部实际素数质量，不能再把逐项的 $o(\max(a,r))$
乘以增长的指标对数量后丢掉这个数量。
当前没有得到这一同时平均改进，也没有完成普通处的剩余预算。

## 10. 先取 $\mu_4$ 不变部分的进一步改良

可以把固定右端改为
$$
\ell_0=\frac{\ell+\ell\circ[i]}2.
\tag{10.1}
$$
由于 $\ell$ 已为偶函数，$\ell_0$ 在 $[i]$ 下不变，
其 $z$ 展开只含 $k\equiv0\pmod4$ 的项。
它仍非零。事实上，R19 的完整奇权公式给
$$
\delta^5\log\Phi(O)
=-2\cdot4!\,f^5\Omega_\infty^{-5}
L_{\mathfrak f}(\bar\psi^5,5)\ne0.
\tag{10.2}
$$
最后的非零性来自绝对收敛的 Euler 乘积：
各好素理想项的绝对值为 $(N\mathfrak q)^{-5/2}$，其总和收敛，
有限个 imprimitive 修正因子也非零。
式 (10.2) 正是 $\ell_0$ 的四次系数乘 $4!$。

在普通目标素数处，$i\in\Delta=\mu_{p-1}$，所以
$e_0\ell_0=e_0\ell$。
因此本投影保留局部中心目标块。
其加法逆像、共轭迹、非代数性和复增长都由 §8 的一般证明处理：
$\ell_0$ 为非零有理函数，极点仍在 $E[f]$，留数向量只需非零而不必为整数。

现在应把首个共振权改为
$$
D_p^{(4)}=\operatorname{lcm}(d_p,4).
$$
由 §2 的同一次二进分析，准确地有
$$
\begin{array}{c|c}
\text{条件}&D_p^{(4)}\\ \hline
a_p\text{ 奇},\ r_p\text{ 奇}&4a_pr_p\\
a_p\text{ 奇},\ r_p\text{ 偶}&2a_pr_p\\
a_p\text{ 偶}&a_pr_p\quad(v_2(a_p)=1,\ 4\mid r_p).
\end{array}
\tag{10.3}
$$

对 $a_p$ 奇数部分，统一按 $a_p\le x$ 与 $a_p>x$ 划分。
后者若 $r_p$ 奇，则 $r_p\le k/(4x)$；若 $r_p$ 偶，则 $r_p\le k/(2x)$。
由 (4.3)，相应两个 $r$ 预算的二次主系数分别为
$\log A/\pi^2$ 和 $\log A/(2\pi^2)$。
故此部分主项为
$$
\frac{\log A}{\pi^2}
\left(2x^2+\frac{k^2}{16x^2}+\frac{k^2}{8x^2}\right).
$$
取 $x^4=3k^2/32$，主常数是 $\sqrt{3/2}\log A/\pi^2$。
$a_p$ 偶数部分仍为 $\log A/(\sqrt2\pi^2)$。
因此 (1.5)–(1.6) 对 $D_p^{(4)}$ 成立，并可把常数加强为
$$
\boxed{C_b^{(4)}=
\frac{\sqrt{3/2}+1/\sqrt2}{\pi^2}\log A.}
\tag{10.4}
$$

对 $b=2+i$，有
$$
C_b^{(4)}=0.3150273470\ldots,
\qquad 3C_b^{(4)}=0.9450820411\ldots.
$$
若反设额外 Sha 余秩始终存在，目标中心阶数至少四，
那么为了区别已知的中心二重零，采用 $m=3$ 已是一个可行的差分次数；
不必固定使用 $m=4$。
即便如此，本篇可证的惰性上界仍未小到原迹图像的 $1/4$ 门槛。

还可用 $[i]$ 商的参数 $u=1/x^2$，其中
$$
t^4=\frac{u}{(1-17u)^2},
$$
以及 $w=z^4$，把复增长阶数写为 $\rho=1/2$，从而把商图像的门槛写为 $\alpha<1$。
但同一系数的 jet 阶数也缩为原来的四分之一，
截断大小的系数约乘四；所以这仍不自动改进当前预算。

## 来源

- C. L. Stewart，*On divisors of Lucas and Lehmer numbers*，Acta Math. **211** (2013)，
  291–314，§4，Lemma 4.1，式 (4.1)–(4.3)；
  [作者保存的出版原文](https://uwaterloo.ca/pure-mathematics/sites/default/files/uploads/documents/s11511-013-0105-y.pdf)，
  [DOI](https://doi.org/10.1007/s11511-013-0105-y)。已读取原始假设及证明。
- 本课题 `2026-11-12-additive-cm-difference-inverse.md`、
  `2026-11-12-herblot-trace-curve-threshold.md`：固定图像、局部大小及实际 jet 接口。
- 其余阶数分解、深度比较、totient 常数、阈值优化和分部求和均在本文证明。
