# R290：非约化底环的 Hasse 不变量与实际 CM 参数的四阶、五阶接近

日期：2026-11-13。

**状态：已证明。** 对 R258、R287 的同一实际同构

$$
E_0[p]\simeq A_d[p],\qquad A_d:y^2=x^3+d,
\qquad p>37,
$$

保留 $H=\mathbb Q(\sqrt{-3})$、$\sigma=1$、整 $j$、正立方自由 $d$，写
$m=v_p(d)\in\{1,2\}$。R287 已从有限平坦切空间下降证明
$v_p(\Delta_{\min}(E_0))=2m$。本篇利用**同一个有限平坦 $p$ 挠点群方案在
$\mathcal O_L/(p)$ 上的 Verschiebung**，进一步证明

$$
\boxed{v_p(j(E))\in m+3\mathbb Z_{\ge1}.} \tag{290.1}
$$

所以两个实际分支分别满足

| $p\bmod9$ | $m$ | $v_p(\Delta_{\min}(E_0))$ | $v_p(j(E))$ 的新下界 |
|---:|---:|---:|---:|
| $2$ | $2$ | $4$ | $5$ |
| $5$ | $1$ | $2$ | $4$ |

若实际二、三除法商域都与 $A_d$ 相同，R287 只留下 R266 的第一族

$$
8-t^3=dw^3,\qquad j(E)=108t^3(8-t^3),\qquad t,w\in\mathbb Z.
$$

本篇在**同一个整数参数**上给出

$$
\boxed{p\mid w,\qquad t\equiv2\pmod{p^{m+3}}.} \tag{290.2}
$$

特别，非 CM 情形 $t\ne2$，故 $|t|\ge p^{m+3}-2$，从而有完全有效的

$$
\boxed{|j(E)|\ge
108\bigl(p^{m+3}-2\bigr)^3
\left(\bigl(p^{m+3}-2\bigr)^3-8\right).} \tag{290.3}
$$

这是一条新的必要条件，不控制变化的分裂导子素数，未完成主问题。
它也没有计算 O6 的忠实普通单位 Norm 原像或规范剩余量 $\mathcal L$。

## 1. 在整个 $\mathcal O_L/(p)$ 上保留 $p$ 挠点同构

先陈述局部版本。设 $p>13$、$p\equiv2\pmod3$，
$A_d/\mathbb Q_p$ 满足 $v_p(d)=m\in\{1,2\}$，
$E/\mathbb Q_p$ 潜在好约化且 $E[p]\simeq A_d[p]$。
R287 引理 287.1 适用，给共同实际 Galois 好约化扩张

$$L=\mathbb Q_p(E[3],A_d[3]),\qquad e=e(L/\mathbb Q_p)\le12<p-1,$$

以及极小判别式赋值 $\delta_E=\delta_A=2m$。
令 $\mathscr E,\mathscr A$ 为两条好约化模型。
Raynaud Corollaire 3.3.6(1) 将给定泛纤维同构及其逆唯一延拓为

$$\Phi:\mathscr E[p]\xrightarrow{\sim}\mathscr A[p]
\quad\text{于 }\mathcal O_L. \tag{290.4}$$

现在置

$$R=\mathcal O_L/(p). \tag{290.5}$$

这是特征 $p$ 的 Artin 局部环，通常不是剩余域：若 $\varpi$ 是
$L$ 的均匀化元，则 $R$ 仍保留 $\varpi,\ldots,\varpi^{e-1}$ 的精度。
将 (290.4) 降到这个完整的 $R$，而不是仅降到 $\mathcal O_L/(\varpi)$。
以下下标 $R$ 均指这一底环。

### 1.1 Verschiebung 的内在性和限制相容性

在任意特征 $p$ 底概形 $S$ 上，有限局部自由交换群方案 $G$ 的
Verschiebung 可内在定义为

$$
V_G=(F_{G^D})^D:G^{(p)}\longrightarrow G, \tag{290.6}
$$

其中 $G^D$ 是 Cartier 对偶，$F$ 是相对 Frobenius，
$G^{(p)}$ 是沿底环 Frobenius 的拉回。这一定义不要求 $S$ 约化或完美。
Cartier 对偶及相对 Frobenius 的函子性给：任一群方案同构
$\phi:G\to H$ 都满足

$$\phi\circ V_G=V_H\circ\phi^{(p)}. \tag{290.7}$$

还必须把 (290.6) 与椭圆曲线的 Verschiebung 接上。
SGA 3, Exposé VIIA, §4.3 在任意特征 $p$ 底概形上为所有**平坦交换**
群方案构造函子性的 $V$；§4.3.3 证明它在有限局部自由群方案上恰是
(290.6)，并且 $V\circ F=[p]$。对椭圆概形，其相对 Frobenius 有限平坦
且满，故这个 $V$ 与通常椭圆概形的 Verschiebung 相同。
将函子性用于闭浸入 $\mathscr E_R[p]\hookrightarrow\mathscr E_R$，便得

$$
V_{\mathscr E_R[p]}
 =V_{\mathscr E_R}|_{\mathscr E_R^{(p)}[p]}, \tag{290.8}
$$

同理适用于 $\mathscr A_R$。因此这里没有将一个仅在完美域成立的
Dieudonné 分类移用到非约化环，也没有额外要求 $\Phi$ 保持极化。

在特征 $p$ 下，$d[p]=0$。对任意 $R$-代数的双数点取 $[p]$ 的核，直接得到

$$
\operatorname{Lie}(\mathscr E_R[p])
=\operatorname{Lie}(\mathscr E_R),
\qquad
\operatorname{Lie}(\mathscr E_R^{(p)}[p])
=\operatorname{Lie}(\mathscr E_R^{(p)}). \tag{290.9}
$$

两边都是秩一自由 $R$-模。这些识别对 $\mathscr A$ 同样成立。
故 (290.7)–(290.9) 表明两条曲线的 $dV$ 矩阵只相差左右两个单位。
尤其

$$
\boxed{dV_{\mathscr A_R}=0\Longrightarrow dV_{\mathscr E_R}=0.}
\tag{290.10}
$$

这是在整个 $R$ 中的零等式，而非仅在其剩余域中的零。

## 2. 任意特征 $p$ 底环上的准确 Hasse 多项式

下面直接计算 (290.10) 所用的标量，以避免对非约化底环省略假设。
设 $R$ 是特征 $p>3$ 的局部环，

$$C:y^2=x^3+A x+B$$

为光滑椭圆曲线，并且 $B\in R^\times$。
定义

$$
H_p(A,B)=[x^{p-1}](x^3+A x+B)^{(p-1)/2}. \tag{290.11}
$$

则 $dV_C$ 在一维 Lie 模上的标量，按相容的基识别，恰由
$H_p(A,B)$ 给出；特别 $dV_C=0$ 当且仅当 $H_p(A,B)=0$。

### 2.1 不取任何 $p$ 次根的 Čech 证明

取仿射开覆盖

$$U=C\setminus\{O\},\qquad V=C\setminus\{x=0\}.$$

这里 $V$ 删除的是 $x$ 的零除子，故仍包含 $O$。
因为 $B$ 是单位，该零除子有限平坦、与 $O$ 不交。
$V$ 的显式仿射坐标为 $u=1/x,v=y/x^2$，方程是
$v^2=u+A u^3+B u^4$，且 $O$ 对应 $(u,v)=(0,0)$。
$y/x$ 在 $U\cap V$ 上正则，并代表 $H^1(C,\mathcal O_C)$ 的一个基：
与 $\omega=dx/(2y)$ 的 Serre 对偶留数为

$$\operatorname{Res}_O\!\left(\frac yx\frac{dx}{2y}\right)
 =\operatorname{Res}_O\frac{dx}{2x}=-1,$$

因为局部参数 $-x/y$ 下 $x$ 的极点阶为二。
这也证明该基在含幂零元的 $R$ 上仍为原始基。

记 $C^{(p)}$ 的对应坐标为 $x_{(p)},y_{(p)}$。
相对 Frobenius 对这个 Čech 基的拉回是

$$
F_C^*\!\left(\frac{y_{(p)}}{x_{(p)}}\right)
=\frac{y^p}{x^p}
=\frac{y(x^3+Ax+B)^{(p-1)/2}}{x^p}. \tag{290.12}
$$

若将右侧的多项式展开为 $\sum_n c_n yx^{n-p}$，则：

- $n\ge p$ 时，该项在 $U$ 上正则；
- $n\le p-2$ 时，该项为 $c_n y/x^r$、$r\ge2$，在 $V$ 上正则，包括
  $O$ 处，因为该处的赋值至少为 $2r-3\ge1$；
- 只剩 $n=p-1$ 的 $H_p(A,B)y/x$ 项。

所以 $F_C^*:H^1(C^{(p)},\mathcal O)\to H^1(C,\mathcal O)$ 的矩阵为
(290.11)。以 $C\simeq\operatorname{Pic}^0(C)$ 的典范极化识别，
$F_C$ 的 Picard 拉回为其对偶同源 $V_C$，而
$\operatorname{Lie}\operatorname{Pic}^0(C)=H^1(C,\mathcal O_C)$。
最后一个切空间识别也直接来自过渡函数 $1+\varepsilon f$ 的 Čech 描述。
因此这正是 $dV_C$ 的标量，证明了 (290.11) 的解释。

所有等式都在 $R$ 上进行；没有用 $R$ 完美，也没有把系数的
$p$ 次方逆或一个形式 Cartier 根引入计算。

### 2.2 $j=0$ 邻域的简单零及全部系数

写

$$p=6h+5,\qquad (p-1)/2=3h+2.$$

要在 $(x^3+Ax+B)^{3h+2}$ 中取得 $x^{p-1}=x^{6h+4}$，
三项选取次数必须是

$$
(r,s,t)=(2h+1-j,\ 1+3j,\ h-2j),
\qquad 0\le j\le\lfloor h/2\rfloor.
$$

所以有完整整数系数公式

$$
H_p(A,B)=
\sum_{j=0}^{\lfloor h/2\rfloor}
\frac{(3h+2)!}{(2h+1-j)!(1+3j)!(h-2j)!}
A^{1+3j}B^{h-2j}. \tag{290.13}
$$

每个阶乘的参数均小于 $p$。特别，首系数

$$c_0=\frac{(3h+2)!}{(2h+1)!h!}$$

模 $p$ 非零。若 $A$ 在极大理想中、$B$ 为单位，则

$$
H_p(A,B)=A B^h
\left(c_0+\sum_{j=1}^{\lfloor h/2\rfloor}
 c_j\left(\frac{A^3}{B^2}\right)^j\right), \tag{290.14}
$$

括号中的元素为单位。因此，即使 $R$ 含幂零元，仍准确有

$$\boxed{H_p(A,B)=0\iff A=0.} \tag{290.15}$$

对于 $A=0$ 的参考曲线，(290.13) 则直接给 $H_p(0,B)=0$。
这里的零不仅是“特殊纤维超奇异”这一点态陈述。

## 3. 从模 $p$ 的 Hasse 零恢复原来 $\mathbb Q_p$ 模型的精度

回到第 1 节，取 $E$ 的极小短模型

$$E:y^2=x^3+a x+b,\qquad a,b\in\mathbb Z_p,$$

令 $\delta=v_p(\Delta_E)=2m$。
局部整 $j$ 和 $c_6^2=c_4^3-1728\Delta$ 给

$$3v_p(a)\ge2m,\qquad 2v_p(b)\ge2m.$$

因为 $m=1,2$，$3v_p(a)$ 严格大于 $2m$。
由 $\Delta=-16(4a^3+27b^2)$，遂有

$$v_p(b)=m. \tag{290.16}$$

共同好约化扩张 $L$ 中置

$$k=e m/6\in\mathbb Z,\qquad u=\varpi^k.$$

两个好模型可同时写成

$$
\mathscr E:\ Y^2=X^3+A'X+B',
\quad A'=a/u^4,\quad B'=b/u^6,
$$
$$
\mathscr A:\ Y^2=X^3+D',
\quad D'=d/u^6. \tag{290.17}
$$

由 (290.16)，$B',D'$ 都是 $\mathcal O_L$ 单位。
又

$$v_L(A')=e\left(v_p(a)-\frac{2m}{3}\right)>0,$$

故 $A'$ 在极大理想中。
将 (290.17) 降到 $R=\mathcal O_L/(p)$，参考模型的 Hasse 不变量为零。
(290.10) 使 $\mathscr E_R$ 的 Hasse 不变量也为零。
由 (290.15) 得

$$A'\equiv0\pmod{p\mathcal O_L},\qquad v_L(A')\ge e. \tag{290.18}$$

所以

$$v_p(a)\ge\left\lceil1+\frac{2m}{3}\right\rceil
=\begin{cases}2,&m=1,\\3,&m=2.\end{cases} \tag{290.19}$$

而 $p>3$ 下 $c_4=-48a$，故

$$v_p(j(E))=3v_p(a)-2m
\in\begin{cases}1+3\mathbb Z_{\ge1},&m=1,\\
2+3\mathbb Z_{\ge1},&m=2.
\end{cases} \tag{290.20}$$

这证明局部版本及实际分支的 (290.1)。如果 $j(E)=0$，可以把其赋值
解释为无穷大；本文的非 CM 结论始终在 $j(E)\ne0$ 的分支使用。

## 4. 对同一全局三次参数的作用

R287 在共同实际三除法 $S_3$ 商域下已证明

$$j(E)=4d r^3,\qquad r\in\mathbb Q^\times.$$

因为 $p\nmid4$，(290.1) 立即给

$$v_p(r)\ge1. \tag{290.21}$$

若完整二除法域也相同，则 R263、R266 的第一族有 primitive 整数模型

$$
E_{a,b}:y^2=x^3+3abd\,x+d(a^3-db^3),
\qquad a^3+db^3=z^3,
$$

其中 $z=\pm1$ 或 $\pm2$，且

$$
j(E)=\frac{6912d a^3b^3}{z^6}. \tag{290.22}
$$

因为 $p\mid d$、$p\nmid z$，方程迫 $p\nmid a$。
所以 (290.22) 的准确 $p$ 赋值为

$$v_p(j(E))=m+3v_p(b).$$

(290.1) 因而直接给 $p\mid b$；该推论只用 $j$，不需要为实际二次
扭曲额外选择一个可能在 $p$ 分歧的模型。

设

$$t=2a/z,\qquad w=2b/z.$$

由于 $z=\pm1,\pm2$，$t,w$ 都为整数，并且

$$8-t^3=dw^3,\qquad j(E)=108t^3(8-t^3). \tag{290.23}$$

已知 $p\mid w$，故 $v_p(8-t^3)\ge m+3$。
又 $p\equiv2\pmod3$，三次幂在 $\mathbb F_p^\times$ 上为双射；
$t^3\equiv8\pmod p$ 迫 $t\equiv2\pmod p$。
因 $t^2+2t+4\equiv12\not\equiv0\pmod p$，分解

$$8-t^3=-(t-2)(t^2+2t+4)$$

给更准确的等式

$$
\boxed{v_p(t-2)=m+3v_p(w)\ge m+3.} \tag{290.24}
$$

这就是 (290.2)。非 CM 情形 $w\ne0$、$t\ne2$，所以
$t=2+p^{m+3}n$、$0\ne n\in\mathbb Z$，从而
$|t|\ge p^{m+3}-2$。再用
$|8-t^3|\ge|t|^3-8$，即得 (290.3)。

## 5. 适用边界

本篇使用的是 $p$ 挠点**有限平坦群方案**的完整同构与
$\mathcal O_L/(p)$ 的非约化精度。若仅知道特殊纤维超奇异、仅知道相同
有限惯性阶数，或只知道 $j$ 在剩余域等于零，均不足以推出 (290.18)。

(290.1) 适用于上述同一实际局部同构，并不要求两条小挠点商域相同；
(290.21) 另外使用共同三次商域；(290.2)–(290.3) 才使用双同域的
primitive 整数参数。三个范围没有互相替换。

这些条件并未证明 $j$ 或 $c$ 的上界，也没有排除变化的分裂素因子。
尤其不能把 (290.3) 的高度下界反用成导子上界。
O6 的固定 $p=43$ 忠实普通 Norm 原像与 $\mathcal L$ 仍未求出；
本篇不以抽象存在性或小特征结果代入那个数值。

## 来源与产物

- M. Raynaud, *Schémas en groupes de type $(p,\ldots,p)$*, Bull. Soc. Math.
  France **102** (1974), 241–280，Corollaire 3.3.6(1)，印刷页 268；
  [原文 PDF](https://www.numdam.org/article/BSMF_1974__102__241_0.pdf)。
  同一个实际 Galois 扩张及 $e<p-1$ 的核对见 R287，本篇保留该扩张。
- P. Gabriel, SGA 3, Exposé VIIA, §4.3、§4.3.2、§4.3.3：任意特征 $p$
  底概形上平坦交换群方案的函子性 Verschiebung、$VF=FV=[p]$，以及
  有限局部自由时与 Cartier 对偶 Frobenius 的一致性；
  [Polo–Gille 重排原文](https://webusers.imj-prg.fr/~patrick.polo/SGA3/origExp7A.pdf)，
  PDF 第 19–21 页（重排页 269–271；原文页码旁注 441–443）。
  已直接核读 §4.3 的一般底概形量词和 §4.3.3 的自对偶图。
- R258、R263、R266、R287：实际曲线、$m$、精确判别式、共同商域及
  primitive 参数的既有接口。本篇的非约化 Hasse 传递、Čech 系数公式、
  新的赋值界及同一整数参数的高阶同余均在正文证明。

本篇为纯证明产物。没有以有限个素数上的实验替代全部 $p$ 的论证。
