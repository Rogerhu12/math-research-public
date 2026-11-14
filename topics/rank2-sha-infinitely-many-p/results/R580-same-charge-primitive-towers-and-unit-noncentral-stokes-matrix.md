# R580 — 同一 Gaussian 次数原函数塔的非中央 Stokes 单位与严格半径

日期：2026-11-14。**状态：已证明。**

R575 的七条原函数有同一个 sigma 次数六；这与原
$S_{34},T_{72},U_{136}$ 的不同 Gaussian 次数排除不同。
本篇证明：即使允许组合系数依赖惰性素数 $p$，七条来源的任何
非零常数线性组合，除去共同 Gaussian 后仍有准确半径
$p^{-p/(p^2-1)}$，并且不属于该闭边界的 Tate 代数。
同一结论覆盖 R584 的任意固定长度两塔，包括其无 Dirac 子格。

证明没有把原函数写成有界测度，也不依赖负矩或中央值非零。
完整 shifted Euler 方程使不同移位在模过收敛函数的商中具有不同
特征值；每个共同移位上的两个真实非中央 Stokes 行有单位行列式。
这排除了常数线性组合带来的 wild 半径改善。
一般多项式九坐标格、原完整中央与 R578 同一修正的实际 forcing
均没有因此关闭。

## 1. 原来源、固定长塔与准确 Gaussian

保持同一个 $b=17$ 模型
$$
y^2=x^3+b,\qquad D_zx=2y,\qquad D_zy=3x^2,\qquad
D_z^2\log\sigma=-x ,
$$
$$
f_4=x\sigma^6,\qquad f_1=-xy\sigma^6.
$$
其固定零初值原函数为 R575/R584 的
$$
U_{\ell,r}(z)
=\frac1{(r-1)!}\int_0^z(z-u)^{r-1}f_\ell(u)\,du .
$$

取任意固定非负整数 $m_4,m_1$，置
$$
R_4=2+6m_4,\qquad R_1=5+6m_1,\qquad
q_4=R_4+4,\qquad q_1=R_1+1.
$$
于是 $q_\ell=6(m_\ell+1)$。
全塔仍是同一实际正幂规整
$$
V_{\ell,r}=z^{R_\ell-r}U_{\ell,r},
\qquad 1\le r\le R_\ell,\qquad \ell\in\{4,1\}.
\tag{1}
$$
没有改变任何积分常数。$m_4=m_1=0$ 时，(1) 正是原七坐标。

以下取
$$
\boxed{
p\equiv5\pmod6,\qquad
p>\max\{19,\max(q_4,q_1)+7\}.
}
\tag{2}
$$
这是显式充分范围，不声称最优。它包括所有需要的固定坏位排除；
特别 $p\nmid 2\cdot3\cdot5\cdot7\cdot17$，
且 $p>\max(R_4,R_1)$。

记
$$
d=p+1,\qquad
c=[z^d]\log(\sigma/z),\qquad a=6c,
$$
$$
S=p^{-p/(p^2-1)},\qquad
\rho=p^{-1/(2p)}.
\tag{3}
$$
R301 的固定 $b$ 单位缩放给 $v_p(c)=v_p(a)=-1$，
且 $S<\rho$。这是实际首坏 sigma 系数；
$a$ 不是为了消去某个来源而另选的参数。

定义两个真实被积来源
$$
A_4=z^{R_4}f_4,\qquad A_1=z^{R_1}f_1,
\qquad
G_\ell=e^{-az^d}A_\ell.
\tag{4}
$$
R301 的原高度二估计直接给
$$
\boxed{
G_\ell\in\mathbf Q_p\langle z/\rho\rangle,\qquad
\|G_\ell\|_\rho\le\rho^{q_\ell}.
}
\tag{5}
$$
为核定这里的来源，写
$$
W=z^2x,\qquad Y_0=-z^3y,\qquad F=\log(\sigma/z).
$$
原形式对数的整逆给 $W,Y_0$ 在闭 $\rho$ 盘解析、范数一；
R301 给 $e^{6(F-cz^d)}$ 及其逆在同盘解析、范数一。
因此准确有
$$
G_4=z^{q_4}W\,e^{6(F-cz^d)},\qquad
G_1=z^{q_1}WY_0\,e^{6(F-cz^d)},
$$
即得 (5)。在 $b=1$ 证明这些界后，$b=17$ 的第六根缩放在
(2) 中为单位，故原范数和实际 $c$ 一并运输。

原最前两项为
$$
\boxed{
A_4=z^{q_4}
 \left(1-\frac{4b}{35}z^6+\cdots\right),\qquad
A_1=z^{q_1}
 \left(1+\frac{6b}{35}z^6+\cdots\right).
}
\tag{6}
$$
例如 $x=z^{-2}-bz^4/7+\cdots$、
$y=-z^{-3}-2bz^3/7+\cdots$、
$\sigma=z+bz^7/210+\cdots$ 直接给 (6)。
所有来源仅含六的倍数次幂。

## 2. 全塔到真实 shifted Euler 来源的整可逆变换

令 $\theta=zD_z$。对 $0\le j<R_\ell$ 定义实际形式原函数
$$
E_j(A_\ell)
=(\theta-j)^{-1}A_\ell
=\sum_{n\ge q_\ell}\frac{[z^n]A_\ell}{n-j}z^n .
\tag{7}
$$
因为 $q_\ell>R_\ell-1\ge j$，分母作为有理数都非零；
这正对应 (1) 的固定零初值，而没有增加齐次解 $z^j$。

对每一条 (1)，逐个系数准确有
$$
\boxed{
V_{\ell,r}
=\left\{\prod_{j=R_\ell-r}^{R_\ell-1}(\theta-j)\right\}^{-1}A_\ell .
}
\tag{8}
$$
这是因为 $n=m+R_\ell$ 项的真实积分分母为
$(m+1)\cdots(m+r)$，即
$(n-R_\ell+1)\cdots(n-R_\ell+r)$。

部分分式公式为
$$
\frac1{\prod_{i=h}^{R-1}(X-i)}
=
\sum_{j=h}^{R-1}
\frac{(-1)^{R-1-j}}
 {(j-h)!(R-1-j)!}\frac1{X-j}.
\tag{9}
$$
按 $r=1,\ldots,R$ 和 $j=R-1,\ldots,0$ 排序，
(9) 是三角变换，对角为
$(-1)^{r-1}/(r-1)!$。
在 (2) 中各对角都是单位，故 (8)–(9) 给
$$
\boxed{
\bigoplus_{r=1}^{R_\ell}\mathcal O_p V_{\ell,r}
=
\bigoplus_{j=0}^{R_\ell-1}\mathcal O_p E_j(A_\ell)
}
\tag{10}
$$
的固定整可逆基变换。
这里的格由所列实际函数生成；R575/R584 的独立性也保证没有
遗漏的常数线性关系。不能将 (10) 换成对所有多项式来源的自由
Gaussian 坐标变换。

原七塔的两块特别为
$$
V_{4,1}=E_1(A_4),\qquad
V_{4,2}=E_1(A_4)-E_0(A_4),
$$
以及 $E_j(A_1)$、$j=0,\ldots,4$ 的同一个三角变换。

## 3. 固定非中央余类的全 Stokes 公式

令
$$
K_{\ell,j}=e^{-az^d}E_j(A_\ell),\qquad
\mathscr L=\theta+ad z^d.
$$
完整形式方程准确为
$$
\boxed{(\mathscr L-j)K_{\ell,j}=G_\ell.}
\tag{11}
$$

以下只需一些明确的非中央余类。取六的倍数 $r$，满足
$$
0<r<d,\qquad 2\le r-j\le p-1,
\qquad x=(r-j)/d\in\mathbf Z_p^\times .
\tag{12}
$$
写 $r\bmod d$ 部分为
$$
P_rG_\ell=z^r\sum_{h\ge0}g_{\ell,r,h}z^{dh},
\qquad
P_rK_{\ell,j}=z^r\sum_{h\ge0}k_{\ell,j,r,h}z^{dh}.
$$
(11) 逐项给
$$
(h+x)k_{\ell,j,r,h}+a k_{\ell,j,r,h-1}
=g_{\ell,r,h}/d,\qquad k_{\ell,j,r,-1}=0.
$$
其准确解是
$$
k_{\ell,j,r,h}
=\frac{(-a)^h}{d(x)_{\overline{h+1}}}
 \sum_{l=0}^h(-1)^l(x)_{\overline l}a^{-l}
 g_{\ell,r,l},
\tag{13}
$$
其中 $(x)_{\overline l}=x(x+1)\cdots(x+l-1)$。

定义真实 shifted Stokes 常数
$$
\boxed{
\mathcal S_{\ell;j,r}
=\sum_{l\ge0}(-1)^l(x)_{\overline l}a^{-l}g_{\ell,r,l}.
}
\tag{14}
$$
由 (5)，
$$
v_p(a^{-l}g_{\ell,r,l})
\ge l+\frac{q_\ell-r-dl}{2p}
=\frac{l(p-1)+q_\ell-r}{2p}.
\tag{15}
$$
故 (14) 收敛。对于下文所选的 $r$，(2) 保证 (15) 在
$l\ge1$ 时严格正，因而准确有
$$
\boxed{\mathcal S_{\ell;j,r}\equiv [z^r]A_\ell\pmod p.}
\tag{16}
$$
这里 $r<d$，所以 $[z^r]G_\ell=[z^r]A_\ell$。
(16) 是完整无限 Stokes 和的同余，不是只截取首项后忽略尾部。

令
$$
\mathcal E_{r,j}(z)=
z^r\sum_{h\ge0}\frac{(-a)^h}{(x)_{\overline{h+1}}}z^{dh}.
$$
把 (13) 的和补到无穷，得到
$$
\boxed{
P_rK_{\ell,j}
=\frac{\mathcal S_{\ell;j,r}}d\mathcal E_{r,j}
+\mathcal R_{\ell;j,r},\qquad
\mathcal R_{\ell;j,r}\in\mathbf Q_p\langle z/\rho\rangle,
\quad
\|\mathcal R_{\ell;j,r}\|_\rho\le\rho^{p-1+q_\ell}.
}
\tag{17}
$$

**尾界证明。**
余项第 $h$ 个系数是
$$
-\frac{(-a)^h}{d(x)_{\overline{h+1}}}
 \sum_{l>h}(-1)^l(x)_{\overline l}a^{-l}g_{\ell,r,l}.
$$
对 $l\ge h+1$，
$(x)_{\overline l}/(x)_{\overline{h+1}}$ 是整因子的乘积，
包括 $l=h+1$ 时的空乘积一。
加上 $z^{r+dh}$ 的 $\rho$ 权后，每项赋值至少
$$
(l-h)\frac{p-1}{2p}+\frac{q_\ell}{2p}
\ge\frac{p-1+q_\ell}{2p}.
$$
而 $G_\ell$ 在闭 $\rho$ 盘的加权系数趋于零，
所以在 $l>h$ 的尾中这些加权赋值的下确界随 $h$ 趋于无穷。
这同时支付有界性和 Tate 条件，证明 (17)。

## 4. 所选模型的准确半径与闭边界失败

对 (12) 中的 $x$，
$$
v_p((x)_{\overline{h+1}})
=\sum_{k=0}^h v_p(r-j+dk)
=\frac{h+1}{p-1}+O_p(\log(h+2)).
$$
因此 $\mathcal E_{r,j}$ 的收敛半径准确为 (3) 的 $S$。

闭边界需要额外核定。取 $h=p^n$、$n\ge1$。
对每个 $1\le e\le n$，序列
$r-j+dk$、$0\le k\le p^n$ 中被 $p^e$ 整除的项恰有
$p^{n-e}$ 个，因为 $k=0$ 不是其零剩余类。
对 $e=n+1$，唯一可能的正倍数是 $p^{n+1}$；
但其模 $d$ 为 $\pm1$，而 (12) 的 $r-j$ 既不是 $1$，
也不是 $d-1=p$，所以这一项不存在。
更高幂已经超过全部正整数。于是
$$
v_p((x)_{\overline{p^n+1}})
=\frac{p^n-1}{p-1}.
$$
相应 $S$ 加权系数的赋值准确等于
$$
\boxed{\frac1{p-1}+\frac{rp}{p^2-1},}
\tag{18}
$$
不随 $n$ 增长。
所以 $\mathcal E_{r,j}$ 不属于闭 $S$ 盘的 Tate 代数。

(17) 的余项在严格更大闭盘解析。
因此
$$
\mathcal S_{\ell;j,r}\ne0
\quad\Longrightarrow\quad
P_rK_{\ell,j}
\text{ 半径恰为 }S,\ \text{且不在闭 }S\text{ Tate 代数中}.
\tag{19}
$$
同一结论适用于任意两个输入的常数线性组合；
此时必须使用它们相同的 $j,r,a$，所以模型确实相同。
不同 $r$ 的系数支撑不交，不能相互抵消。

## 5. 真实两个低行给每个共同 j 的整单射

先取原七塔，即 $m_4=m_1=0$。
共同移位只有 $j=0,1$。
对于其中任何一个 $j$，取真实非中央余类 $r=6,12$；
它们均满足 (12)。
由 (6)、(16)，有
$$
\boxed{
\begin{pmatrix}
\mathcal S_{4;j,6}&\mathcal S_{1;j,6}\\
\mathcal S_{4;j,12}&\mathcal S_{1;j,12}
\end{pmatrix}
\equiv
\begin{pmatrix}
1&1\\
-4b/35&6b/35
\end{pmatrix}\pmod p,
\qquad
\det\equiv\frac{2b}{7}\in\mathbf F_p^\times .
}
\tag{20}
$$
因此这个完整 Stokes 映射是整可逆的；
对任意非零常数对 $(u_4,u_1)$，
两个 Stokes 值不可能同时为零。
若将系数最大范数归一为一，则至少一个值为单位。
这一结论允许系数依赖 $p$，也允许有限系数域扩张。

对于单独存在的 $j=2,3,4$，只有 $A_1$ 来源，
而 $\mathcal S_{1;j,6}\equiv1\pmod p$ 已足够。

任意固定长塔的全部移位同样得到支付：

* 若某个 $j$ 只属于一条塔，使用该输入自己的 $r=q_\ell$，
  其 Stokes 值模 $p$ 为一。
* 若 $j$ 属于两条塔且 $m_4=m_1$，令 $q=q_4=q_1$，
  使用 $r=q,q+6$，(20) 的矩阵和行列式原样成立。
* 若 $j$ 属于两条塔且 $q_4\ne q_1$，使用 $r=q_4,q_1$。
  按两首阶的大小排列，低阶输入另一列为零，高阶各自首项为一；
  矩阵模 $p$ 为单位三角矩阵。

这些所选 $r$ 全满足 $r<d$ 和 $2\le r-j\le p-1$。
其最高次数至多 $\max(q_4,q_1)+6$，
所以 (2) 同时保证全部 (15) 的正尾界。
较低输入在较高行的系数亦为整：
其次数差小于 $d$，可直接由 (5) 的整数赋值读取整性。
没有将一个未经证明的局部常数替换为一。

故对每一个实际移位 $j$，任意非零的同移位输入组合
$$
K_j=\sum_{\ell:\ j<R_\ell}u_{\ell,j}K_{\ell,j}
$$
都具有准确半径 $S$，并且闭 $S$ 非 Tate。

## 6. 不同 Euler 移位不能在模过收敛商中相消

这是同一 Gaussian 次数所需的额外步骤。
只知道各列分别有坏半径，不足以排除它们的和具有较大半径。

令
$$
\mathcal A_\rho=L\langle z/\rho\rangle,\qquad
\mathcal Q_\rho=L[[z]]/\mathcal A_\rho
$$
为任意允许系数域 $L$ 上的向量空间商。
$\mathscr L=\theta+ad z^d$ 保持 $\mathcal A_\rho$：
$\theta$ 把第 $n$ 个系数乘以 $n$，不破坏 Tate 条件；
另一个操作是固定多项式乘法。
因此 $\mathscr L$ 真正诱导 $\mathcal Q_\rho$ 上的线性算子。

(11) 与 $G_\ell\in\mathcal A_\rho$ 给
$$
(\mathscr L-j)[K_j]=0.
\tag{21}
$$
不同 $j$ 是不同的特征值，并且在 (2) 中其差均为 $p$ 单位。
若 $\sum_j[K_j]=0$，对每个 $j$ 使用多项式
$$
\prod_{i\ne j}(\mathscr L-i)
$$
得到
$$
\left(\prod_{i\ne j}(j-i)\right)[K_j]=0.
$$
所以所有 $[K_j]=0$。
第5节却证明任何非零输入组合的 $K_j$ 不在
$\mathcal A_\rho$，故只能全部输入系数为零。

同一论证可在任何 $S<R<\rho$ 的闭盘 Tate 商中使用，
因为 (11) 的右边仍在那个 Tate 代数。
它还可直接在闭 $S$ Tate 商中使用。
这证明不同移位既不能消掉准确半径，也不能消掉 (18) 的闭边界失败。
这里没有假定各移位的模型支撑不同；
它们支撑可以相同，真正起作用的是 (21) 的不同特征值。

## 7. 完整常数线性组合的半径定理

**定理。**
在 (1)–(3) 中，取任意非零常数系数向量
$(c_{\ell,r})$，允许依赖 $p$。
令
$$
V=\sum_{\ell,r}c_{\ell,r}V_{\ell,r},\qquad
K=e^{-az^d}V .
$$
则
$$
\boxed{
\operatorname{rad}(K)=p^{-p/(p^2-1)}=S,\qquad
K\notin L\langle z/S\rangle .
}
\tag{22}
$$

**证明。**
由 (10) 将 $V$ 整可逆地写成各 $E_j(A_\ell)$ 的组合。
每个原 $A_\ell$ 在任意严格小于 $S$ 的圆盘解析：
这是 (4)–(5) 与指数的真实半径。
除以系数 $n-j$ 至多损失 $O_p(\log n)$ 赋值，
所以每个 $E_j(A_\ell)$ 仍在所有这些圆盘解析。
乘 $e^{-az^d}$ 亦保持之。因此 $\operatorname{rad}(K)\ge S$。

若半径大于 $S$，可选 $S<R<\rho$ 使 $K$ 属于闭 $R$ Tate 代数。
第6节分离所有非零移位后，每个相应 $K_j$ 也属该代数，
与第5节的准确半径矛盾。
若 $K$ 属闭 $S$ Tate 代数，用同一商空间论证和第5节的闭边界失败，
仍矛盾。这证明 (22)。

真实同次数参考也不会改变结论。
例如
$$
\frac{\sigma^6}{z^6}
=e^{az^d}\,e^{6(F-cz^d)}
$$
的第二因子及其逆在闭 $\rho$ 盘解析。
所以
$$
\boxed{
\operatorname{rad}\left(\frac{V}{\sigma^6/z^6}\right)=S,
\qquad
\frac{V}{\sigma^6/z^6}\notin L\langle z/S\rangle .
}
\tag{23}
$$
$V$ 至少有六阶零，故 $V/\sigma^6$ 也在原点正规；
乘除这个固定 $z^6$ 只移位系数，
同样保持准确半径与闭边界失败。
这里只使用实际解析参考，不给该参考增加任何算术身份。

换成共同参数 $w=z^6$ 时，(22)–(23) 的半径准确为
$$
p^{-6p/(p^2-1)}.
$$
R584 的无 Dirac 常数子格是 (1) 的实际子空间，
故其任何非零向量同样受此定理约束。
没有从原点 Dirac 缺陷消失推出较大半径。

## 8. 与完整中央、九坐标和原 forcing 的边界

(20) 所用的是明确的非中央 shifted Stokes 行，
而不是原 $S/T/U$ 的完整中央导数，也不是 ordinary 的
$I_4,I_1$。本篇没有证明这些目标值非零。
即使已知某些中央或 Dirac 缺陷为零，(22) 的单位非中央行仍在。

定理允许全部常数系数依赖 $p$，
所以不能通过在每个惰性位重新挑一条线性组合逃开 (22)。
但它只处理常数线性组合：
一般多项式 $P(S,T,V_{\ell,r})$ 的同一饱和 jet、
非线性对消、以及可能的其他全局算术结构并未被排除。
R574/579/581/583/584 对这些实际格的成本继续按各自全文使用，
不能由本篇的准确半径读出某个未付的全饱和 Smith 下界。

原 R578 的完整 $\mathcal D_\psi$ 图像和同一个 $R$ 的两条十三行、
$U_0$、第三精度及真正 $d_2$ 继续开放。
本篇不给七个原函数或其乘积新增原中央零，也不把
(20) 的单位改称原 $M$ 余核的非零。
新增的是：同次数六、任意固定长塔的线性 wild 相消路线
已被其实际整 Stokes 单射和完整谱分离排除。

## 依赖与证书范围

* [R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)
  的原首 Gaussian 和较大圆盘，按同一 $b=17$ 单位尺度运输。
* [R575](R575-fixed-primitive-towers-and-complete-ordinary-dirac-defects.md)
  的实际七塔、全部零初值和真实独立性。
* [R584](R584-arbitrary-fixed-primitive-towers-dirac-jets-and-full-lattice-budgets.md)
  的固定长塔及无 Dirac 子格。
* [R62](R62-actual-euler-primitive-stokes-constants.md)
  是原四次 CM 的 Euler/Stokes 前例；本篇 (11)–(21)
  重新支付了当前实际 shifted 来源、全部尾界及不同移位的谱分离，
  不把该旧结论未经运输套到新来源。

本篇是全部参数证明，没有新素数扫描。
