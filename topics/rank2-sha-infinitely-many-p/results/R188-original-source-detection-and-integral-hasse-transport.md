# R188. 全次数原源的整检测与 Hasse 偏导的 Laurent 运输

日期：2026-11-12。**状态：以下原源检测、整左逆、全部 Hasse 阶的
运输和准确 Taylor 读取范围均已证明。** 它们属于同一个实际
theta 源；没有把环境 Taylor 系数当成曲线前缀，也没有证明全
前缀观测矩阵可逆。主目标的无穷素数非零仍未完成。

## 1. 实际原源与两组径向坐标

固定 R174/R179 的惰性素数 $p\ge7$，并排除 $p=11,17$。
置 $\mathcal O=\mathbb Z_p$。这里 $17$ 的排除明确支付径向
十七次幂换参；实际惰性素数本来不等于 $17$。

原固定函数为
$$
 A=a^{17}P(s),\qquad B=a^{17}Q(s),\qquad s=b/a,
 \tag{1}
$$
其中 $P,Q\in\mathbb Z[1/5][s]$，
$P=s+O(s^2)$、$Q-P=-22s^2+O(s^3)$。原有限源始终是
$$
 E_D=\mathcal O[A,B]_{\le D}.
 \tag{2}
$$
本文的 $A,B$ 是形式独立的源变量，随后才沿原曲线取值。

使用 R179 §6.1 已构造的同一整径向坐标 $(\Gamma-1,\zeta)$。
它们与 $(U,V)$ 的正反换参都整，线性部分为恒等。
在该坐标上，齐次次数 $17$ 给准确等式
$$
 A=\Gamma^{17}f(\zeta),\qquad
 B=\Gamma^{17}g(\zeta),\qquad
 f,g\in\mathcal O[[\zeta]],
 \tag{3}
$$
且
$$
 f(y)=y+O(y^2),\qquad
 g(y)-f(y)=-22y^2+O(y^3).
 \tag{4}
$$

为简化整数插值，本文改用
$$
 x=\Gamma^{17}-1,\qquad y=\zeta.
 \tag{5}
$$
它与 $(\Gamma-1,\zeta)$ 是整可逆的形式换参：正向线性
系数为 $17\in\mathcal O^\times$，反向由整隐函数定理得到。
这里不要求写成带有未审分母的二项式展开。
它保持每个极大理想幂及其商格；因此有限 Taylor 范数和
以下整性也可运回 $(\Gamma-1,\zeta)$ 或 $(U,V)$。
在 (5) 中，
$$
 A=(1+x)f(y),\qquad B=(1+x)g(y).
 \tag{6}
$$

令
$$
 T(y)=\frac{g(y)}{f(y)}-1=-22y+O(y^2).
 \tag{7}
$$
因为 $f/y$ 是整单位，(7) 是整级数，且有整形式逆
$T^{-1}\in y\mathcal O[[y]]$。这一步使用 $p\ne2,11$。
后文写 $T$ 只指 (7)，不指 R179 的全深度变量。

## 2. 原次数 D 的范数由总 Taylor 阶 2D 准确检测

原源 (2) 有整基
$$
 e_{m,c}=A^{m-c}(B-A)^c=A^mT^c,
 \qquad 0\le c\le m\le D.
 \tag{8}
$$
第二个表达式只用于准确形式等式；第一个表达式说明每一列
都是原次数 $m$ 的真实多项式，没有加入 $A^{-1}$。
基 (8) 与原单项式基的变换及逆变换均在
$\operatorname{GL}_{\binom{D+2}{2}}(\mathcal O)$ 中。

由 (6)–(7)，
$$
 e_{m,c}(x,y)
 =(1+x)^m f(y)^mT(y)^c
 =(-22)^c(1+x)^m y^{m+c}+O(y^{m+c+1}).
 \tag{9}
$$
记 $\mathfrak m=(x,y)$。

**整检测定理。** 对任意 $D\ge0$ 和任意 $P_0\in E_D$，有
$$
 \boxed{\quad
 \|P_0\|_{E_D,p}
 =\max_{i+l\le2D}
   \bigl|[x^iy^l]P_0((1+x)f,(1+x)g)\bigr|_p.
 \quad}
 \tag{10}
$$
这里左侧是原多项式 Gauss 范数。该等式对全部 $D$ 成立，
没有 $D<p$ 的限制。

**证明。** 整代入给右侧不超过左侧。通过乘同一个 $p$ 幂，
只需证明原 primitive 多项式在右侧有一个单位系数。
写
$$
 P_0=\sum_{m,c}a_{m,c}e_{m,c},\qquad a_{m,c}\in\mathcal O,
$$
并在所有 $a_{m,c}\notin p\mathcal O$ 中取最小
$l=m+c$。低于该 $l$ 的列系数全为 $p$ 倍；高于该 $l$ 的
列不影响模 $p$ 的 $y^l$ 行。因此该行准确为
$$
 [y^l]P_0\equiv
 \sum_{m=m_-}^{m_+}a_{m,l-m}(-22)^{l-m}(1+x)^m\pmod p,
 \tag{11}
$$
其中
$$
 m_-=\lceil l/2\rceil,\qquad m_+=\min(l,D),\qquad
 q_l=m_+-m_-+1.
$$
系数向量至少有一项为单位。读取 $x^h$、$0\le h<q_l$ 的
整数矩阵为
$$
 \left(\binom{m_-+j}{h}\right)_{0\le h,j<q_l}.
 \tag{12}
$$
其行列式为一：按次数 $h$ 的多项式 $\binom Xh$ 计算，
Vandermonde 分子为 $\prod_{j=1}^{q_l-1}j!$，恰与所有行的
最高项分母相消。因此 (11) 至少一个 $h<q_l$ 系数为单位。
而
$$
 l+h\le l+\min(l,D)-\lceil l/2\rceil\le2D.
 \tag{13}
$$
这证明 (10)。若保持 $x_0=\Gamma-1$，对应矩阵是
$\binom{17(m_-+j)}h$，行列式为
$17^{q_l(q_l-1)/2}$，仍为单位；两种规范一致。$\square$

### 2.1. 同一个整左逆，而非只有模 p 的存在性

设 $J_{2D}=\mathcal O[[x,y]]/\mathfrak m^{2D+1}$。代入定义
$$
 \iota_D:E_D\longrightarrow J_{2D}.
 \tag{14}
$$
由 (10)，它是等距注入，像是饱和子格。更具体地，可以
构造一个 $\mathcal O$ 线性的左逆
$\Pi_D:J_{2D}\to E_D$，不使用阶乘的 $p$ 分母。

按 $l=0,1,\ldots,2D$ 递增处理 (9)。先减去此前已恢复的
$m+c<l$ 各列对 $y^l$ 的完整贡献，再在当前行读取
$0\le h<q_l$，用 (12) 的整逆恢复
$a_{m,l-m}(-22)^{l-m}$，最后除以单位 $(-22)^{l-m}$。
所有用到的系数都在 (13) 的总次数范围内。
低于总阶 $2D+1$ 的整代入和所有回代都只涉及有限数据。
因此
$$
 \Pi_D\iota_D=1,
 \qquad \|\Pi_D\|_p\le1.
 \tag{15}
$$
对实际源，算法恢复的是同一个完整多项式；没有分别恢复
某些 summand 后假定它们各自满足曲线前缀。

## 3. 原 Hasse 偏导与准确 Laurent 逆代换

对 $a,b\ge0$，定义原 Hasse 算子
$$
 \partial_A^{[a]}\partial_B^{[b]}P_0
 =[u^av^b]P_0(A+u,B+v),\qquad h=a+b.
 \tag{16}
$$
它在原源上满足
$$
 \partial_A^{[a]}\partial_B^{[b]}E_D\subset E_{D-h},
 \qquad
 \|\partial_A^{[a]}\partial_B^{[b]}\|_p\le1,
 \tag{17}
$$
并在 $h>D$ 时为零。这里的 (16) 本身就是定义，不经过
普通偏导再除以 $a!b!$。

在 $\mathcal R=\mathcal O[[x,y]][1/y]$ 中，$A=(1+x)f(y)$
可逆。由 (6) 准确解出平移后的坐标：
$$
 \begin{aligned}
 y_{u,v}
 &=T^{-1}\left(\frac{A T(y)+v-u}{A+u}\right),\\
 1+x_{u,v}&=\frac{A+u}{f(y_{u,v})}.
 \end{aligned}
 \tag{18}
$$
每个 $u,v$ 总阶的系数都在 $\mathcal R$ 中；(18) 是
$\mathcal R[[u,v]]$ 中的形式恒等式。
对任意 $F\in\mathcal O[[x,y]]$，置
$$
 \mathscr D_{a,b}F=[u^av^b]F(x_{u,v},y_{u,v}).
 \tag{19}
$$
下文的极点界同时证明 (19) 逐系数有定义。对实际源
$F=\iota(P_0)$，(18) 直接给
$$
 \mathscr D_{a,b}\iota(P_0)
 =\iota\bigl(\partial_A^{[a]}\partial_B^{[b]}P_0\bigr).
 \tag{20}
$$
右侧是整的正幂形式级数。左侧表达式中的 Laurent 极点在
这个完整实际源上准确相消；不需要额外的普通性、非消失或
积分假设。

作为一阶校准，令 $W=fg'-gf'=f^2T'=-22y^2+O(y^3)$，则
$$
 \begin{aligned}
 \mathscr D_{1,0}
 &=\frac{g'}W\partial_x-
       \frac{g}{(1+x)W}\partial_y,\\
 \mathscr D_{0,1}
 &=-\frac{f'}W\partial_x+
       \frac{f}{(1+x)W}\partial_y.
 \end{aligned}
 \tag{21}
$$
它们与 (18) 的一次项一致。高阶估计使用 (18)，而不把
(21) 的迭代除以阶乘。

## 4. 任意 Hasse 阶的 p 整性与准确读取成本

记 $\Delta y=y_{u,v}-y$、$\Delta x=x_{u,v}-x$。
对每个总阶 $n\ge1$，有
$$
 \boxed{\quad
 [u^av^b]\Delta y\in y^{-n}\mathcal O[[x,y]],\qquad
 [u^av^b]\Delta x\in y^{-2n}\mathcal O[[x,y]],
 \quad a+b=n.
 \quad}
 \tag{22}
$$

**证明。** (18) 中送入 $T^{-1}$ 的增量为
$$
 Z=\frac{v-(1+T(y))u}{(1+x)f(y)}
       \left(1+\frac{u}{(1+x)f(y)}\right)^{-1}.
 \tag{23}
$$
其总阶 $n$ 的系数属于 $y^{-n}\mathcal O[[x,y]]$。
由于 $T^{-1}$ 是整级数，它在 $T(y)$ 处的所有 Hasse
展开系数也整。代入 (23) 后，同一总阶各乘积的极点阶相加
至多 $n$，证明 (22) 的第一式。

再置
$$
 E=\frac{f(y+\Delta y)-f(y)}{f(y)}.
$$
$E$ 的总阶 $n$ 系数属于 $y^{-n-1}\mathcal O[[x,y]]$。
在 $(1+E)^{-1}$ 的总阶 $n$ 项中，一个有 $j$ 个正阶因子的
乘积极点阶至多 $n+j\le2n$。于是
$$
 1+x_{u,v}
 =(1+x)\left(1+\frac{u}{(1+x)f(y)}\right)(1+E)^{-1}
$$
给 (22) 的第二式。全部展开只有整二项式系数和整单位的
反幂，没有任何 $p$ 分母。$\square$

由 (22)，对 $h=a+b$ 和任意单项式 $x^iy^l$，有
$$
 [x^Iy^J]\mathscr D_{a,b}(x^iy^l)\ne0
 \quad\Longrightarrow\quad
 i\le I+h,\qquad l\le J+2h.
 \tag{24}
$$
这里允许中间 $y$ 指数为负，最后读取的 $I,J$ 可取非负。
确实，在一个展开项中，设替换了 $\alpha$ 个 $x$ 因子和
$\beta$ 个 $y$ 因子；它们所分配的 $u,v$ 总阶分别为
$h_x,h_y$，其中 $h_x+h_y=h$、$\alpha\le h_x$、
$\beta\le h_y$。$x$ 指数至多降低 $\alpha\le h$；
$y$ 指数至多降低
$\beta+2h_x+h_y\le2h$。同时总 Taylor 次数至多降低
$\alpha+\beta+2h_x+h_y\le3h$。

因此有两种准确、可同时使用的有限读取规则：
$$
 \boxed{\quad
 \begin{array}{ll}
 \text{目标矩形 }0\le I\le I_0,\ 0\le J\le J_0:
 &\text{只需原 }i\le I_0+h,\ l\le J_0+2h;\\[2pt]
 \text{目标总阶 }I+J\le K:
 &\text{只需原 }i+l\le K+3h.
 \end{array}
 \quad}
 \tag{25}
$$
每一规则都是整数矩阵。源系数若只精确到 $p^N$，目标系数
仍精确到 $p^N$，没有 $v_p(h!)$ 损失。
另有整过滤表述
$$
 \mathscr D_{a,b}\bigl(\mathfrak m^K\bigr)
     \subset y^{-2h}\mathfrak m^{\max(K-h,0)}.
 \tag{26}
$$
在总次数过滤上，(26) 给同一个 $K-3h$ 下界。

## 5. 对同一个有限原源的联合使用

(10)、(15)、(20)、(25) 可以同时作用于一个完整
$P_0\in E_D$，包括全部 $a+b\le D$ 的 Hasse 偏导。
各偏导的原次数是 $D-a-b$；不把它们重新放入一个更大的
自由源，也不为每个偏导独立选择源范数。

具体地，若一个已证明的整条件行只读取
$\iota(\partial_A^{[a]}\partial_B^{[b]}P_0)$ 的目标矩形或
总次数截断，则 (25) 给一个作用于原 $\iota(P_0)$ 的准确
整行，并保留同一个模 $p^N$ 精度。这是把实际中央条件的
Hasse 族送入共同系数矩阵的合法接口。

也可以先用 (15) 恢复原多项式的全部系数，再按 (16) 及
(6) 计算任何指定有限目标截断。后一种算法在实际源上只
读取一次原总阶 $2D$，其余是固定整矩阵；它并不声明任意
环境级数由这 $2D$ 阶决定，也不把曲线前缀提升成环境前缀。

这里须保留三项范围：

- 若 $P_0(A(w),B(w))$ 在曲线上高阶消失，不能据此假定
  每个原偏导也高阶消失。本文只运输条件行，不运输一个
  未证明的偏导前缀。
- 原 $w$ 中的完整中央函数及其 Stokes 条件，仍须由
  R182/R185 的准确原输出公式支付。$v=V(w)$ 的真实前缀
  虽可等距运输，单个高中央系数不能因此直接换参。
- R179 的有限 core 并非一个由最大总次数描述的完整矩形。
  (25) 只给所需的实际输入索引；是否全落入某个模 $p^N$
  core，必须按每一项的带号和进位成本核算。

特别，(10) 仅证明实际源在环境 Taylor 截断中的整注入。
把这个截断继续沿真实 Cartan 曲线求值时，AS 关系仍可能
造成相消。本文没有把输入覆盖称为输出观测可逆，也未从
约 $D^2$ 个条件行的数量推出同样多的独立收益。

## 6. 依赖

- [R179：全深度共同 core 与实际整径向坐标 §6.1](../notes/2026-11-12-full-depth-common-jet-core-and-as-defect.md)。
- [R174：真实 CM 整形式坐标与共同前缀](R174-actual-cm-formal-cartan-and-common-prefix-matrix.md)。
- [R185：实际整轴 Stokes 行与完整中央条件](R185-integral-axis-stokes-functional-and-complete-central-tests.md)。
- [R182：原 w 的完整中央行及端点](../notes/2026-11-12-actual-first-as-carry-and-complete-central-rows.md)。

所有论证都是上述真实形式坐标及整数代数的证明；没有以
有限素数实验替代全次数结论。
