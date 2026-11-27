# R1097 — 原 full47 的奇好素 CM 交数：正四元数和与稀疏两平方和

**状态：已证明。** 本条给出原 $X_{\rm ns}^+(47)$ 上
$y_4$ 与 $T_ny_{16}$ 在全部奇好素处的实际水平交数，
允许该素数整除 $n$。原47项链标记把计算压到两个模 $47^2$
的整数进程；没有改成未标记的 $j$ 交数。
$2$ 处及坏47处不在本条公式内。尚未执行新的数学计算。

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126 / global_route。

## 1. 原对象与主公式

固定
$$
X=X_{\rm ns}^+(47),\qquad
y_4=c_{-4},\quad y_{16}=c_{-16}.
$$
两个点的底层 $j$ 值分别为 $1728,287496$，
均带原 CM 域在47挠点上给出的**规范**非分裂 Cartan 正规化子结构。
本条对任意正奇数 $n$、$47\nmid n$ 工作。
$T_n$ 始终是完整 Hecke 对应，按全部阶 $n$ 子群计数；
当 $n$ 含平方因子时不删掉非循环核。

在 $X$ 于 $\ell\ne47$ 的好整模型上记
$$
G_\ell(n)=(\overline{y_4}\cdot\overline{T_ny_{16}})_\ell .
\tag{1097.1}
$$
这是实际有理除子的交数；几何分支及剩余次数均按 pushforward 计入。
两除子在特征零支撑不交：奇度同源保持 CM 整环在2处的局部整序，
而 $\mathbf Z_2[i]$ 与 $\mathbf Z_2[2i]$ 不同。

置
$$
r_2(a)=\#\{(u,v)\in\mathbf Z^2:u^2+v^2=a\}
\quad(a>0),
$$
并在参数不是正整数时约定 $r_2=0$。
对奇素数 $\ell\ne47$ 有：

- 若 $\ell\equiv1\pmod4$，则 $G_\ell(n)=0$；
- 若 $\ell\equiv3\pmod4$，则
$$
\boxed{
G_\ell(n)=
\frac1{16}
\sum_{\substack{0<A<8n,\ 4\nmid A\\
47^2\mid A\ \text{或}\ 47^2\mid(8n-A)\\
\ell\mid(8n-A)}}
r_2(A)\,
r_2\!\left(\frac{8n-A}{\ell}\right)
\bigl(v_\ell(8n-A)+1\bigr).
}
\tag{1097.2}
$$
特别，式 (1097.2) **也包括 $\ell\mid n$**。
它不要求 $\ell$ 与原 Hecke 度数互素。

## 2. 两个真实二核及其正范数来源

采用
$$
E:\ y^2=x^3-x,\qquad i^2=-1.
$$
三个二子群都在 $\mathbf Q$ 上有理。其中唯一 CM 稳定的二子群是
$\ker(1+i)$；另外两个商在粗曲线上都给 $y_{16}$。
原47结构由二同源输运后仍是规范 CM Cartan，因为2在47处为单位。
因此旧的实际除子恒等式为
$$
T_2y_4=y_4+2y_{16},\qquad
2T_ny_{16}=(T_{2n}-T_n)y_4.
\tag{1097.3}
$$
第二式用 $(2,n)=1$；保留了两个非 CM 二核的真实重数。

更有利于计算的做法是直接保留这两个核。
设 $\ell$ 为奇素数。二核为有限 étale，因而在严格未分歧基变换后
唯一提升到各个无穷小厚化。
一个度 $2n$ 的同源 $\beta:E\to E$，由于 $v_2(2n)=1$，
在 $E[2]$ 上的核恰是一条直线。它含 $\ker(1+i)$ 当且仅当
$$
\beta=\gamma(1+i)
\quad\text{对某个整端态 }\gamma.
\tag{1097.4}
$$
若 (1097.4) 不成立，则 $\beta$ 经且仅经上述两个非 CM 二核之一分解：
$$
E\xrightarrow{\phi_H}E/H\xrightarrow{\psi}E,
\qquad \deg\phi_H=2,\quad\deg\psi=n.
$$
每个 $E/H$ 连同输运的47项链都是原 $y_{16}$。
选取其几何同构不改变计数；同构均与规范 CM Cartan 相容。
于是“不右整除 $1+i$”的 $\beta$ 给度 $n$ 的
$\operatorname{Hom}(y_{16},y_4)$ 的两份相同计数。
这不是两个差和的形式消去，而是正集合的分解。

## 3. 原超奇异端环与47标记

设 $\ell\equiv3\pmod4$ 且 $\ell\ne47$。
$E/\mathbf F_\ell$ 的 Frobenius $j$ 满足
$$
j^2=-\ell,\qquad ji=-ij .
$$
因为全部二挠点在 $\mathbf F_\ell$ 上有理，
$(1+j)/2$ 是实际端态。完整端环为
$$
R_\ell=\mathbf Z[i,(1+j)/2].
\tag{1097.5}
$$
证明与 [R188](R188-marked-cm-hecke-proper-intersections.md) §3 相同且不依赖41：
包含的序以 $1,i,(1+j)/2,(i+ij)/2$ 为基，
其约化判别式为 $\ell$，已经是极大序。

写
$$
\beta=\frac{a+bi+cj+dij}{2}.
$$
准确整性及范数条件是
$$
a\equiv c\pmod2,\qquad b\equiv d\pmod2,\qquad
a^2+b^2+\ell(c^2+d^2)=8n.
\tag{1097.6}
$$

47在 $\mathbf Q(i)$ 惰性，故原规范 Cartan 是
$\mathbf F_{47}[i]^\times$。因 $47\nmid2n$，
$\beta$ 在47挠点上可逆。保持同一个无向项链恰等价于
$$
\beta\bmod47\in
N_{\mathrm{GL}_2(\mathbf F_{47})}
   (\mathbf F_{47}[i]^\times).
$$
这个正规化子由与 $i$ 交换和反交换的两个陪集组成，所以
$$
(a,b)\equiv(0,0)\pmod{47}
\quad\text{或}\quad
(c,d)\equiv(0,0)\pmod{47}.
\tag{1097.7}
$$
这里没有借用 R188 的分裂41、20项链权重。

若置 $A=a^2+b^2$、$C=c^2+d^2$、$B=\ell C$，则47的惰性给
$$
(1097.7)
\quad\Longleftrightarrow\quad
47^2\mid A\ \text{或}\ 47^2\mid B .
\tag{1097.8}
$$
两种情形不能同时发生，因为 $A+B=8n$ 且 $47\nmid n$。
即使 $A$ 或 $B$ 在47处有更高赋值，(1097.8) 仍准确；
没有以标量迹判据替代向量条件。

### 3.1 特征3的额外自同构没有被误计

当 $\ell\ge7$ 时，$R_\ell^\times=\mu_4$。
$\ell=3$ 时未标记曲线有12个自同构，
但保持**这个规范47项链**的仍只有 $\mu_4$。

确实，对范数1的单位用 (1097.6)–(1097.7)，各坐标绝对值小于47。
若保持项链，则交换或反交换分量之一必须整齐地为零。
反交换分量单独范数1会给 $3(c^2+d^2)=4$，不可能。
交换分量恰为 $\pm1,\pm i$。
因此固定的带47标记对象在特征3没有额外三阶稳定子。
所有粗模计数都使用这个实际稳定子；不另除3。

## 4. 全部奇好素的局部 Hom–交数公式

本节把 $\ell\mid n$ 也包括进去，说明其局部来源，
而不套用要求全局奇判别式的 Gross–Zagier 主定理。

### 4.1 范数元素的提升长度

在 $\ell\equiv3\pmod4$ 处，两个 CM 序都在 $\ell$ 处极大，
相应形式群是未分歧二次 CM 的典范提升。
二同源 $\phi_H$ 的度数为 $\ell$-单位，
故在 $\ell$-divisible group 上是同构。
于是 $\psi$ 的提升等价于 $\beta=\psi\phi_H$ 的提升，
并保留 (1097.4) 与47标记。

置
$$
\beta_-=\frac{c+di}{2}j .
$$
未分歧典范提升的端环公式为
$$
\beta\text{ 提升到 }W/\ell^k
\quad\Longleftrightarrow\quad
v_\ell(N\beta_-)\ge2k-1.
\tag{1097.9}
$$
这里 $W=W(\overline{\mathbf F}_\ell)$。
因此当 $\beta_-\ne0$ 时，
$$
L_\ell(\beta)
=\sum_{k\ge1}{\bf1}_{\beta\text{ 可提升至 }W/\ell^k}
=1+\min\{v_\ell(c),v_\ell(d)\}.
\tag{1097.10}
$$
(1097.9) 是 Gross–Zagier III Proposition7.3 的局部未分歧情形：
其证明只用原 CM 形式群和 Serre–Tate，不使用全局判别式奇偶。
这里 $\ell$ 为奇数且 $\ell\nmid4$，确在该局部范围内。
由于2和47的群结构有限 étale，已成立的两种标记条件
在提升过程中不增添别的长度。

### 4.2 粗模的因子与 $\ell\nmid n$

在任意无穷小厚化，按实际核计数的同源以目标自同构为重复。
将相交截面拉回素于 $\ell$ 的完整辅助层 $M>3$，
在刚性曲线上交数为可提升同构的次数之和。
再用有限映射的投影公式下降，得到
$$
(\overline{x}\cdot\overline{y})_\ell
=\frac12\sum_{k\ge1}
\#\operatorname{Isom}_{W/\ell^k}(x,y)
\tag{1097.11}
$$
的标记版本，所有特殊纤维自同构都在右边计入。
这就是 Gross–Zagier III Proposition6.1 的局部证明。
在本题目标 $y_4$ 的粗稳定子阶为2、源 $y_{16}$ 在特征零只有 $\pm1$；
因子 $1/2$ 不可改成除4。
§3.1 已排除特征3额外稳定子造成的错误处理。

当 $\ell\nmid n$，全部度 $n$ 核也为 étale，
(1097.11) 可直接对 Hecke 纤维求和。
再用§2的两个非 CM 二核，得到
$$
G_\ell(n)=\frac14
\sum_{\substack{\beta\in R_\ell,\ N\beta=2n\\
\beta/(1+i)\notin R_\ell\\
\beta\bmod47\in N(\mathbf F_{47}[i]^\times)}}
L_\ell(\beta).
\tag{1097.12}
$$

### 4.3 $\ell\mid n$：完整准典范层计算

写 $n=\ell^t r$，$(r,\ell)=1$。
先取 $T_r y_{16}$ 的全部几何目标 $z$，按原核的重数求和。
每个 $z$ 的 CM 序在 $\ell$ 处仍极大，
所以在 $W$ 上是典范提升；其在2处仍为 conductor2。
它的典范 Frobenius 共轭也具有这个2处整序。
故这些零层点均不等于 $y_4$，不存在特征零返回分量。

在未分歧二次 CM 的原形式变形空间内，
$T_{\ell^t}z$ 按以下准典范层分解：

- 若 $t=2a$，有一条零层及正层 $s=2,4,\ldots,2a$；
- 若 $t=2a+1$，有正层 $s=1,3,\ldots,2a+1$，
  其典范中心为 Frobenius 共轭的零层。

正层 $s$ 的完整轨道度为
$$
e_s=(\ell+1)\ell^{s-1}.
$$
此度数在刚性辅助层并按原核重数读取；有额外粗稳定子时，
不将它误读成 $e_s$ 个互异粗几何点。
在刚性形式参数中，正层点与其典范中心的距离赋值恰为 $1/e_s$。
这是 Gross 的准典范提升公式以及 Gross–Zagier III §5
式(5.2)–(5.4) 所用的精确负同余。
所有零层点是 $W$-点。若其约化与 $y_4$ 相同，
它们与 $y_4$ 的距离至少为1；故一个正层完整轨道的交数
只读取特殊层的同构数，不能把每个 ramified 点当作 $W$-点。

在原标记的粗模型上记
$$
h_1(z,x)=\frac12
\#\operatorname{Isom}_{\overline{\mathbf F}_\ell}(\bar z,\bar x),
\qquad x=y_4.
$$
先于刚性辅助层求上述轨道和，再应用 (1097.11) 的下降因子：
$t=2a$ 时，贡献为零层的完整交数加 $a\,h_1(z,x)$；
$t=2a+1$ 时，贡献为 $(a+1)h_1(z^{(\ell)},x)$。
不相交的特殊层给0。这个计算保留了全部
$e_s$ 个 ramified 目标、全部核重数和 Frobenius 的实际47结构。

与之比较，四元数局部极大序是除代数的整数环。
若 $t=2a$，范数为 $2n$ 的元素唯一写成
$\beta=\ell^a\beta_0$，$N\beta_0=2r$；
(1097.10) 给 $L_\ell(\beta)=a+L_\ell(\beta_0)$。
若 $t=2a+1$，先除 $\ell^a$，再经实际相对 Frobenius 因子化；
剩余可分同源度为 $r$，而
$L_\ell(\beta)=a+1$。
这两条恰分别给上一段的两个交数。
标量 $\ell$ 与 Frobenius 在47处可逆；
Frobenius 以 $i\mapsto-i$ 输运原 CM Cartan。
两个非 CM 二核也随同输运，未被丢掉。
所以 (1097.12) 对 $\ell\mid n$ 同样成立。

该证明重现了 Gross–Zagier III §6 的局部计算，
并已逐项支付本题的 conductor2 来源与47标记。
若改由 $(T_{2n}-T_n)y_4$ 出发，
返回项的数目 $r_K(2n)=r_K(n)$，
且奇 $\ell$ 下 $v_\ell(2n)=v_\ell(n)$，
故同一准典范返回修正及共有 CM 切向自交准确相消。
正集合 (1097.12) 避免了显式计算这两个无穷自交和。

### 4.4 分裂素数

若 $\ell\equiv1\pmod4$，约化 ordinary。
在任何正准典范层之前，若典范中心与 $y_4$ 约化相同，
ordinary 典范提升的唯一性迫两个带原47结构的零层点相同。
但奇度同源始终保留 conductor2 的2处整序，
不可能得到 $y_4$。
故所有层均无交，$G_\ell(n)=0$。
这也包括 $\ell\mid n$，与 Gross–Zagier III §6 的普通情形一致。

## 5. 正范数和的完整两平方化

对 (1097.6) 中的元素置
$$
A=a^2+b^2,\qquad C=c^2+d^2,\qquad B=\ell C=8n-A.
$$
一个允许的元素不能有 $A=0$ 或 $C=0$：
$C=0$ 时高斯整数范数为 $2n$，必被 $1+i$ 整除；
$A=0$ 时同样对纯反交换分量使用 $2n/\ell$ 的偶范数，
仍可右除 $1+i$。
因此 $0<A<8n$。

右除条件的准确坐标是
$$
\frac{\beta}{1+i}
=\frac{(a+b)+(b-a)i+(c-d)j+(c+d)ij}{4}.
\tag{1097.13}
$$
结合 (1097.6)，可整除当且仅当
$a,b$ 同奇偶、$c,d$ 同奇偶，且
$$
a+b-c+d\equiv0\pmod4.
\tag{1097.14}
$$
另一所需模4同余由原整性自动等价。

现在固定正整数 $A,C$ 且 $A+\ell C=8n$。

**$A$ 为奇数。** 每对两平方表示中恰有一个坐标为奇数。
原整性要求两对表示的奇坐标处于同一位置，恰保留半数配对。
这些配对都不满足右除的同奇偶要求，故全部不可除。

**$A\equiv2\pmod4$。** 四个坐标全奇。
把 $a$ 换为 $-a$ 没有固定点，并交换 (1097.14) 的成立与不成立。
故恰有半数配对不可除。

**$4\mid A$。** 四个坐标全偶。
除以2后的范数等式为
$$
(a/2)^2+(b/2)^2+\ell\{(c/2)^2+(d/2)^2\}=2n.
$$
右端为偶数，故 (1097.14) 自动成立；所有元素都可右除。

因此合法且不可右除的配对数准确为
$$
\begin{cases}
\frac12r_2(A)r_2(C),&4\nmid A,\\
0,&4\mid A.
\end{cases}
\tag{1097.15}
$$
对每个这样的配对，$\ell$ 在 $\mathbf Z[i]$ 惰性给
$$
v_\ell(C)=2\min(v_\ell(c),v_\ell(d)),
\qquad
L_\ell(\beta)=\frac{v_\ell(B)+1}{2}.
\tag{1097.16}
$$
代入 (1097.12)，再使用原47条件 (1097.8)，即得 (1097.2)。

## 6. 有穷范围、实际实现与一个纸面尺度检查

公式只需读取
$$
A=47^2s
\quad\text{或}\quad
A=8n-47^2s,\qquad
1\le s<8n/47^2.
\tag{1097.17}
$$
两进程没有重复。再删去 $4\mid A$，并检查两平方表示。

若某个 $B=8n-A$ 要贡献，除 $\ell$ 外每个
$3\bmod4$ 素因子的赋值必须为偶数，
而 $\ell$ 的赋值必须为奇数。
所以一个固定 $B$ 至多指定一个有贡献的奇惰性素数 $\ell$。
两平方数可按原整数分解读取：
$$
r_2(s)=
\begin{cases}
4\displaystyle\prod_{r\equiv1(4)}(v_r(s)+1),
 &v_r(s)\text{ 对所有 }r\equiv3(4)\text{ 均偶},\\
0,&\text{否则}.
\end{cases}
\tag{1097.18}
$$
本条没有执行该有限算法；后继公开 CI 必须保留两进程、
全部素因子及完整 Hecke 指标。

直接推论是
$$
G_\ell(n)=0
\quad\text{对所有奇 }\ell\ne47
\quad\text{若 }n\text{ 为奇数且 }n\le275.
\tag{1097.19}
$$
原因是 $8n<47^2$ 时 (1097.17) 为空。
这不删除2、47处，也不删除后继 $nq,nq^2$ 的贡献。

一个不用于替代证明的纸面尺度检查：
暂去掉47标记筛选，取 $n=1$。
$\ell=3$ 时 $A=2,5$ 分别给2、4；
$\ell=7$ 时 $A=1$ 给2，其余奇素为0。
故未标记的奇部为 $3^6 7^2$，准确吻合
$$
287496-1728=2^3 3^6 7^2.
$$
原47标记在同一 $n=1$ 情形使所有奇部为0，
不能把上述未标记检查直接当成本层读数。

## 7. 接入原完整高度的三项式

保留 [R1094](R1094-original-disjoint-CM-heights-and-first-global-intersection-functional.md)
和 [R1096](R1096-certified-original-CM-moving-units-and-odd-Hecke-height-basis.md)
的实际对象
$$
q=4513,\quad
D_4=B_qu_4,\quad D_{16}=B_qu_{16},\qquad
B_q=q+1-T_q.
$$
若 $n$ 为奇数且 $(n,47q)=1$，则对奇好素 $\ell\ne q,47$，
完整投影公式给
$$
\boxed{
\begin{aligned}
I_\ell(D_4,T_nD_{16})
=23^2\{&
(q^2+3q+1)G_\ell(n)\\
&-2(q+1)G_\ell(nq)+G_\ell(nq^2)\}.
\end{aligned}}
\tag{1097.20}
$$
此处 $I_\ell$ 为同一原正则模型的 Néron交数。
好素只有一个几何分量， degree0 配对不另添垂直项。
尖点由 $B_qC_\infty=0$ 完整消去；
所有 CM 目标的 $j$ 整，所以没有遗失的 CM–尖点交数。
即使 $\ell\mid n$，§4.3 仍支付 (1097.20) 的三项来源。

式 (1097.20) 使用
$$
B_q^2=(q^2+3q+1)-2(q+1)T_q+T_{q^2}.
$$
其中 $T_{q^2}$ 按全部阶 $q^2$ 子群计数。
特别，$E[q]$ 的非循环核仍在正范数和内；
不得把它替换为循环 $q^2$ 对应。

模 $q$ 可把 (1097.20) 中三个整数系数写成 $1,-2,1$，
但三项对应及其全部素数支撑仍须保留。
将 (1097.20) 乘原 Fermat 商
$(\ell^{q-1}-1)/q$ 后求和，给 R1096
$\Gamma(T_n)$ 的整个奇好素贡献。
$2$ 处、坏47处的水平与垂直修正须另算。
本条不宣称已得到 $\Gamma$ 或其迹坐标 $\kappa$ 的单位性，
也不宣称八个 CM 圆盘内部已经唯一。

## 来源与准确使用范围

- B. H. Gross and D. B. Zagier, *Heegner points and derivatives of L-series*,
  Invent. Math. **84** (1986), 225–320，
  [作者公开原文](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/BF01388809/fulltext.pdf)。
  本条亲读 III §§5–8（印刷258–264页；PDF34–40页），
  使用 §5 的完整 Hecke/准典范分层、§6 的刚性辅助层与 ramified 轨道交数、
  Proposition7.3 的未分歧典范端环公式。
  对本题所需的 $\ell\mid n$ 与47标记已经在§4重证；
  没有调用其要求全局奇判别式的主定理，也没有据此覆盖2处。
- B. H. Gross, *On canonical and quasi-canonical liftings*,
  Invent. Math. **84** (1986), 321–326：
  所需未分歧正层次数和精确负同余，亦在上述
  Gross–Zagier III §5 原文列出；本条只使用奇 $\ell$ 的未分歧范围。
- [原 CM 二同源笔记§3](../notes/2026-11-12-qc-local-types-resume2.md)：
  原 $T_2y_4=y_4+2y_{16}$ 与尖点规范。
- [R188](R188-marked-cm-hecke-proper-intersections.md)：
  同一 Gaussian 曲线的真实奇惰性端环与局部长度；
  本条的47标记、两个二核和 $\ell\mid n$ 扩展均已重新证明，
  没有消费旧41的有限数值证书。
