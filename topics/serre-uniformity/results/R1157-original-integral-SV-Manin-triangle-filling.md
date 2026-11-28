# R1157：原 SV Manin 三项的显式整四线 filling

日期：2026-11-28（Asia/Taipei）  
会话：Astra-serre-24b8836b-20261126  
状态：完整纸证；无新数学执行。一般 $p$ 主目标仍为 OPEN。

## 1. 实际结论：辅助数是 $n$，不是标记素数 $p$

固定 $p>37$，另取素数 $3<n<p$；始终可以取 $n=5$。
设 $E/k$ 为特征零椭圆曲线，$P,Q\in E[p](k)$，并假设
$$
P\ne0,\qquad Q\ne0,\qquad R=-P-Q\ne0.
\tag{1157.1}
$$
不要求 $P,Q$ 线性独立。因此下述结论同时包括独立的原
Manin bases 和非退化的 rank-one 配置。

用 [R1136](R1136-original-forced-compact-Manin-sources.md)
与 [R1138](R1138-original-integral-bare-cup-smoothing-comparison.md)
的同一 Sharifi–Venkatesh theta 规范，记
$$
t=\theta_n,\qquad t_C=\theta'_{n,C},\qquad
B_n(P,Q)=\{t(P),t(Q)\}
 -\sum_{C\ {\rm closed}}\operatorname{Cor}
       \{t_C(P),t_C(Q)\}.
\tag{1157.2}
$$
这里 $C\subset E[n]$ 是阶 $n$ 循环子群；$t_C$ 是加上 $C$
之后原 $E$ 上的函数，不能将这个符号的源误换成 $E/C$。
闭点项通过其真正定义域作 field $K_2$ corestriction。
在 $E[n]$ 分裂后，下文也用 $B_n$ 表示这个符号的指定
外积代表
$t(P)\wedge t(Q)-\sum_{C\subset E[n]}t_C(P)\wedge t_C(Q)$。
所有外积等式均先在分裂域书写；不对任意乘法群外平方
虚构一个 norm。最后的下降在实际 $K_2$ 和指定上链上进行。

本文在一个明确的 prime-to-$p$ 有限辅助域上给出有限、实际、
只含 $p$ 单位分母的四线表达式 $\mathcal B_{n;P,Q}$，
其完整边界为
$$
\delta_B\mathcal B_{n;P,Q}
 =B_n(P,Q)+B_n(Q,R)+B_n(R,P),
\qquad \delta_B[u]=u\wedge(1-u).
\tag{1157.3}
$$
式 (1157.3) 通过一个明确的 $K_3$ 三函数留数式证明，
不先借有理 Euler-complex 再约模 $p$。

将 [R1156](R1156-original-four-line-integral-cochain-and-transfer.md)
的同根、ordered 修正及 transfer 同伦逐项代入，便得到
指定三项 cup 的实际连续 $\mathbf Z_p(2)$ 值 primitive。
它的全部有限层相容，而且其原 raw 交换商只由非 cusp
曲线上的真正 theta 单位构成，所以整塔先在全 noncusp
曲线上延伸，然后才可约模 $p$。

这个结论解决的是**真正的 $B_n$ Manin relator**，
不以 aux-$c$ 的 $\Psi_c$ 相关和替代它。它尚不将任一
raw 三角形的提升识别为 R1147 的整个 moment 群提升，
也尚未给出原 $z_{12}$ 的值。

## 2. 原 theta 的两个有限范数恒等式

写 $A=E[n]$，$|A|=n^2$，并先在 $A$ 分裂的域上工作。
使用加法记号表示乘法群张量 $\mathbf Z_{(p)}$。
原除子是
$$
\delta_0=n^2[0]-[A],\qquad
\delta_C=n[C]-[A],\qquad
\operatorname{div}t=\delta_0,\quad
\operatorname{div}t_C=\delta_C.
\tag{1157.4}
$$
$t,t_C$ 取 SV §6.3.1 的同一 trace-fixed 元素。
它们是 universal elliptic curve 去掉 $E[n]$ 后的单位类，
不依赖另选的有零极 Hodge frame。

准确有
$$
\sum_{a\in A}t(T+a)=0,\qquad
\sum_{a\in C}t(T+a)=n\,t_C(T).
\tag{1157.5}
$$
这里包括所有规范常数。第一式左边除子为零；
第二式左边的除子为
$n^2[C]-n[A]=n\delta_C$，所以两式的待证差都是 base 常数。
若 $(m,n)=1$，$[m]$ 在 $A$ 和 $C$ 上置换，故这些平移和
同样 $[m]_*$-fixed。例如
$$
[m]_*\!\left(\sum_{a\in C}t(T+a)\right)
 =\sum_{a\in C}([m]_*t)(T+ma)
 =\sum_{a\in C}t(T+a).
$$
一个 base 常数在 $[m]_*$ 下乘 $m^2$，于是差被每个
$m^2-1$ 杀掉。SV §6.3.1 脚注 19 给出的公因子整除 $24$；
$24$ 在 $\mathbf Z_{(p)}$ 中可逆，故差确为零。
同理
$$
t(-T)=t(T),\qquad t_C(-T)=t_C(T)
\tag{1157.6}
$$
也按同一除子、同一 trace-fixed 规范成立。

这些是实际 $K_1\otimes\mathbf Z_{(p)}$ 等式。
若需逐个有理函数代表，先清除有限个与 $p$ 互素的分母；
可能留下的 prime-to-$p$ torsion 再用一个 $p$ 单位幂杀掉。
之后只反除这些单位。R1156 §2.1 对这种乘法关系所留下的
兼容根相位作实际修正；这里没有把它们在 cochain 上直接设零。

## 3. 原 $e_n$ 的三个零边际

定义整数函数
$$
w(a,b)=\delta_0(a)\delta_0(b)
       -\sum_{C\subset A,\ |C|=n}\delta_C(a)\delta_C(b).
\tag{1157.7}
$$
这就是 SV 的
$e_n=\delta_0\boxtimes\delta_0-
\operatorname{Nm}(\delta_C\boxtimes\delta_C)$
在全部 $n$-division 点分裂后的系数。

直接按 $(a,b)$ 的 $\mathbf F_n$-秩计数，得到

| $\dim_{\mathbf F_n}\langle a,b\rangle$ | $w(a,b)$ |
|---|---:|
| $0$ | $n(n+1)(n-1)^2$ |
| $1$ | $-n(n-1)$ |
| $2$ | $n$ |

例如 $a=0,b\ne0$ 时，唯一一个 $C$ 包含 $b$；
两个非零独立向量分别落在两个不同的 $C$ 中。
这逐项给出表中系数，也与 SV Remark 6.3.2 的
$n^4-n^3-n^2+n,\ n-n^2,\ n$ 一致。

所以 $w$ 对两槽的任意可逆 $\mathbf F_n$ 线性重组不变。
每个 $\delta$ 的总度数为零，又给
$$
\sum_a w(a,b)=0,\qquad
\sum_b w(a,b)=0,\qquad
\sum_{a+b=d}w(a,b)=0\quad(d\in A).
\tag{1157.8}
$$
最后一个等式由 $(a,b)\mapsto(a,a+b)$ 的可逆性化为前两个，
没有丢掉 rank-one 部分。

把两个差坐标改成三个顶点，置
$$
F(x,y,z)=\frac1{n^2}\,w(y-x,z-y).
\tag{1157.9}
$$
固定任意两个变量，沿第三个变量的和都为零。
因而若 $I_A=\ker(\mathbf Z_{(p)}[A]\to\mathbf Z_{(p)})$，
则
$$
\sum_{x,y,z}F(x,y,z)[x]\otimes[y]\otimes[z]\in I_A^{\otimes3}.
\tag{1157.10}
$$
这是实际整分解：用
$\mathbf Z_{(p)}[A]=\mathbf Z_{(p)}[0]\oplus I_A$
逐槽分解，三个 augmentation 的核的交就是 $I_A^{\otimes3}$。
没有借有限模外积注入完整乘法群的未经证明性质。

## 4. 两槽 contraction 保留同一个循环子群

由 (1157.5)，
$$
\begin{aligned}
\sum_a\delta_0(a)t(P+a)&=n^2t(P),\\
\sum_a\delta_C(a)t(P+a)&=n^2t_C(P).
\end{aligned}
\tag{1157.11}
$$
所以外积双线性给出准确的
$$
\sum_{a,b\in A}w(a,b)\,
 t(P+a)\wedge t(Q+b)=n^4 B_n(P,Q).
\tag{1157.12}
$$
右边的每一项 $t_C(P)\wedge t_C(Q)$ 来自左边
同一个 $\delta_C\otimes\delta_C$。因此这个计算没有把
$\sum_C$ 的同子群相关乘积换成两个独立的 norm，也没有
省略 $\operatorname{Cor}$。回原域时，所有几何 $C$ 恰按
其 residue field 聚成 (1157.2) 的闭子群项。

## 5. 显式三函数：全部尺度与留数符号

取三个基点
$$
B_0=0,\qquad B_1=P,\qquad B_2=P+Q.
$$
对 $a\in A$，定义同一 theta 的实际比值
$$
f_a^{(i)}(T)=
 \frac{\theta_n(T-B_i-a)}{\theta_n(T-B_i)}.
\qquad
\operatorname{div}f_a^{(i)}
 =n^2([B_i+a]-[B_i]).
\tag{1157.13}
$$
在外积公式中也用 $f_a^{(i)}$ 表示它的加法类；
特别 $f_0^{(i)}=0$，乘法记号下就是 $1$。
这里没有任选 principal divisor 函数的常数。
由于 $(n,p)=1$ 和 (1157.1)，三个陪集 $B_i+A$ 两两不交。

定义
$$
\boxed{\displaystyle
\mathcal K_{n;P,Q}
=-\frac1{n^8}
 \sum_{x,y,z\in A}w(y-x,z-y)\,
 f_x^{(0)}\wedge f_y^{(1)}\wedge f_z^{(2)}.}
\tag{1157.14}
$$
它是 $k(E)^\times\otimes\mathbf Z_{(p)}$ 的第三外积中的
明确有限表达式；$n$ 是辅助数，所有 $n^{-8}$ 都是 $p$ 单位。

逐点计算完整留数。令
$$
\alpha=P+y-x,\quad \beta=Q+z-y,\quad
\gamma=R+x-z,\qquad \alpha+\beta+\gamma=0.
$$
先写
$$
\Xi=\sum_{x,y,z}F(x,y,z)
   f_x^{(0)}\wedge f_y^{(1)}\wedge f_z^{(2)},
\qquad \mathcal K=-n^{-6}\Xi.
$$
三个 divisor 陪集对 $\operatorname{Res}\Xi$ 的贡献为

| 支持陪集 | 按 $F(x,y,z)$ 求和后的贡献 |
|---|---|
| $B_0+A$ | $n^2\sum F\,t(\alpha)\wedge t(\gamma)$ |
| $B_1+A$ | $-n^2\sum F\,t(\alpha)\wedge t(\beta)$ |
| $B_2+A$ | $n^2\sum F\,t(\gamma)\wedge t(\beta)$ |

下面说明表中没有忽略负 divisor 或分母。
以第一行为例，正点 $B_0+x$ 的两个值槽是
$$
\bigl(t(P+y-x)-t(P-x)\bigr)
 \wedge
\bigl(t(P+Q+z-x)-t(P+Q-x)\bigr).
$$
两个分母项分别不依赖 $y$ 或 $z$，故由固定另外两个变量时
的零边际全部消去。负点 $B_0$ 的系数则由
$\sum_xF(x,y,z)=0$ 消去。其余两行完全同样，
中间行保留三外积第二槽的负号；(1157.6) 支付各处的负点。

三行总和因此是
$$
\operatorname{Res}\Xi
=-n^2\sum_{x,y,z}F(x,y,z)
 \bigl(t(\alpha)\wedge t(\beta)
       +t(\beta)\wedge t(\gamma)
       +t(\gamma)\wedge t(\alpha)\bigr).
\tag{1157.15}
$$
改变量 $a=y-x,b=z-y$。每个 $(a,b)$ 有 $n^2$ 个同时平移
的顶点三元组，这准确消掉 (1157.9) 的 $n^{-2}$。
对第二、第三项，再用
$(a,b)\mapsto(b,-a-b)$ 的可逆性和 $w$ 的不变性。
三项分别由 (1157.12) 变成 $n^4 B_n(P,Q)$、
$n^4 B_n(Q,R)$、$n^4 B_n(R,P)$。于是
$$
\boxed{\displaystyle
\operatorname{Res}\mathcal K_{n;P,Q}
 =B_n(P,Q)+B_n(Q,R)+B_n(R,P).}
\tag{1157.16}
$$

直接使用 (1157.14) 时，$n^8$ 的来源依次是：
principal divisor 的 $n^2$、同时平移轨道的 $n^2$、
两槽 contraction 的 $n^4$。等价地，用已平均的 $\Xi$
只需除 $n^6$。符号是总负号，不能改成正号。

## 6. 从该 $K_3$ 式到实际固定函数整塔

先取 $L_0=k(E[n])$ 的 Galois splitting field。
因为 $3<n<p$，
$$
[L_0:k]\mid|\operatorname{GL}_2(\mathbf F_n)|
=n(n-1)^2(n+1)
$$
不含 $p$。特别 $n=5$ 时右边是 $480$，对所有 $p>37$
都适用。这里没有分裂新的 $E[p^r]$，原 $E[p]$ 标记一直固定。

在每个非零三函数项中，三个 principal divisor 的支持
已由 (1157.1) 分离。若 theta 类含 $p$ 单位分母，
先选择实际函数代表并清分母；三重外积的相应单位幂一并
保留。随后直接使用 R1156 §4 的弦线分解和一般位置选择：
仅再加入二次塔与三次 splitting fields，所得有限 Galois
扩张 $L/k$ 的次数仍 prime-to-$p$。
R1156 (1156.13)–(1156.17) 为每项给出有限四线表达式。

将这些表达式按 (1157.14) 的完整系数相加，得到
$\mathcal B_{n;P,Q}$ 在 $L$ 上的有限见证，其边界是
(1157.16) 的限制。全部 theta 范数恒等式、弦线的 leading
常数和反对称转换都保留为有限乘法关系。
R1156 §2 用这些见证修正实际根相位，给出 ordered primitive；
R1156 §5–6 再以实际右陪集及 cup 同伦将它下降至 $k$。

更明确地，记原同根 Kummer cocycle 为
$a_S=\kappa(t(S))$、$b_{C,S}=\kappa(t_C(S))$，并置
$$
\begin{aligned}
\Omega_{n;P,Q,R}={}&
 a_P\smile a_Q+a_Q\smile a_R+a_R\smile a_P\\
&-\sum_{C\ {\rm closed}}\operatorname{Cor}
 \bigl(b_{C,P}\smile b_{C,Q}
       +b_{C,Q}\smile b_{C,R}
       +b_{C,R}\smile b_{C,P}\bigr).
\end{aligned}
\tag{1157.17}
$$
闭子群的两槽使用同一个 coinduced permutation–Tate 格
上的逐陪集配对。所构连续一次上链满足
$$
H_{n;P,Q}\in C^1_{\rm cont}(G_k,\mathbf Z_p(2)),\qquad
dH_{n;P,Q}=-\Omega_{n;P,Q,R}.
\tag{1157.18}
$$
它是同一套 $p^\infty$ 路径根和关系相位构成的整上链，
不是逐层另选解。因此全部 $\bmod p^r$ 层相容。

若写
$\Omega_{n;P,Q,R}=\mathcal B(a\smile a)$，
其中 $a$ 为 (1157.17) 的全部实际 theta 单位的 Kummer 向量，
则
$$
(v,z)(v',z')=(v+v',\,z+z'+\mathcal B(v,v'))
\tag{1157.19}
$$
定义实际有限秩 class-two 群，$(a,H_{n;P,Q})$ 是其 cocycle。
四线中其他 cross-ratio 函数只用于构造中央上链，
不必将它们添加成最终 raw 交换商的坐标。

这里的精确结果是原 $B_n$ 的三项 primitive。
它不同于 aux-$c$ 三函数直接给出的 $\Psi_c$；
(1157.7)、(1157.12) 已明确支付二者之间此前不能跳过的
同子群、双槽相关结构。

## 7. 原 S 关系和退化 rank-one 三项

反对称关系无需评价 $\theta_n(0)$。在相同根规范下，
$$
d\!\left(a_Pa_Q-
 \sum_C\operatorname{Cor}(b_{C,P}b_{C,Q})\right)
=-\Omega_{B_n(P,Q)+B_n(Q,P)}.
\tag{1157.20}
$$
这是 R1156 (1156.5) 的直接应用，不把 ordered cup 当作
逐上链反对称。

若 $Q=-P\ne0$，(1157.6) 使相应两个槽相同；
这个实际非零点对的 $B_n(P,-P)$ 有 primitive
$$
\frac12\left(a_P^2-
 \sum_C\operatorname{Cor}b_{C,P}^2\right).
\tag{1157.21}
$$
如果同一函数的两次出现预先用了不同根，则先加 R1156
(1156.6) 的零次相位修正。没有在极点 $0$ 处代入 theta。
故非退化 rank-one 三项由 (1157.18) 处理，
$Q=-P$ 的非零点对项由 (1157.21) 处理。真正含零标签的
Manin 边仍使用原 SV parabolic 来源的 regularization；
本节没有另用 $\theta_n(0)$ 的裸值定义它，也没有删除
全部 rank-one 来源。

## 8. 先在全 noncusp 上延伸，及严格的整轨道 raw 下降

### 8.1. 固定函数整塔的水平延伸

令 $Y$ 为原 full-level 非 cusp 模曲线，保持其实际
Weil component 与数域结构。若 $S\in E[p]$ 非零，
则 $S+a$ 不属于 $E[n]$。因此
$t(S),t_C(S)$ 在相应有限 étale $n$-division cover 上
都是全局单位类。它们来自 (1157.4) 的真正 universal theta，
不是未消 Hodge 权的 $\psi_n$ 单项。

所以 (1157.19) 的交换商和系数格都在 $Y$ 上无分歧。
在 $x\in Y$ 的几何离散赋值处，整个兼容 raw 塔的惯性
落入中心 $\mathbf Z_p(2)$，其分解群等变性给
$$
\operatorname{Hom}_{G_{k(x)}}(\mathbf Z_p(1),\mathbf Z_p(2))
=H^0(k(x),\mathbf Z_p(1))=0.
\tag{1157.22}
$$
R1156 §8.2 的正规化、purity 与唯一延伸因而原样适用。
每层在全 $Y$ 有限 étale，层间态射相容。
这里仍使用整个无挠 $\mathbf Z_p$ 中心；
单独的有限层不变量未被断言为零。

### 8.2. 全 deck 轨道的诱导乘积不需要除群阶

还有一个真实下降方式，但其对象须说准确。
设 $Y\to\mathcal M$ 是保留全部 Weil components 和完整
level descent data 的 full-level cover，记
$G=\operatorname{GL}_2(\mathbf F_p)$。
在模叠上理解这一 level torsor；不把固定一个 Weil component
冒称为已经带全部 $G$ 作用的几何连通 cover。

对已经构造并延伸的一个 raw 塔 $\mathcal T$，取
$$
\mathcal T^{\rm ind}=\prod_{g\in G}g^*\mathcal T.
\tag{1157.23}
$$
群、系数和交换商也取同一 pullback 乘积。
deck 元素 $h$ 将第 $g$ 因子运输到第 $gh$ 因子，
因此重指标给严格 descent datum；其 cocycle 条件来自群乘法，
不需先比较任意两份四线 primitive。有限 étale descent
逐层生效，全部层间态射相容。

对一个固定椭圆曲线的独立有序 $p$-基，
$G$ 在这些标记上的作用自由且传递，所以 (1157.23)
恰可按全部独立标记编号。中心是整的有限直和
$\bigoplus_{g\in G}\mathbf Z_p(2)$。
没有反除含 $p$ 的 $|G|$，也没有声称各因子选取的 primitive
本来逐项相同。对于 rank-one 标记不能将此乘积擅自压成
较小轨道再除稳定子，因为该稳定子含 $p$。

这付的是诱导 raw 对象的实际全轨道下降。
它仍不提供到指定 moment 群的双线性 pushout：
不同因子之间的 bracket 是否正好变成目标的交叉项，
必须用原权和与指定 S/U filling 另作真实等式。
特别不能把 (1157.23) 的 block-diagonal bracket
直接当成两个总 norm 的 bracket。

## 9. 此次已闭与下一条实际接口

本文现在给出：

- 原 $e_n$ 的三零边际及其 $I_A^{\otimes3}$ 表达；
- 同一 theta 规范下保完整常数的有限范数恒等式；
- 正确总号和 $n^{-8}$ 的原 $B_n$ 三项 $K_3$ 留数；
- 与 p-level 分离的 prime-to-$p$ 四线 filling；
- 实际固定函数整上链、全 noncusp raw 延伸；
- 可保全部独立标记的诱导 raw 下降，而不除 $|G|$。

后继应将原 R1140 的指定 S/U 多项式 filling 逐项代入
(1157.18)、(1157.20)，同时保全部 norm/correlation。
最终目标的双线性形式、根规范和 finite coefficient action
若能由该有限家族的实际群态射给出，才可使用 R1147
在原 $\mathcal M$ 上的唯一性，识别 canonical moment lift。
本文没有用 cohomology 相等代替这条群态射，也没有将
一个尚未完成目标比较的 raw 中央值称为原 $z_{12}$。

## 来源与核验

- R. Sharifi and A. Venkatesh，*Eisenstein cocycles in motivic
  cohomology*，作者全文 §6.3.1，(6.5)–(6.11)，脚注 19，
  Remark 6.3.2，Lemma 6.4.2 与 Theorem 6.4.1：
  https://www.math.ucla.edu/~sharifi/publ/eisensymbol.pdf 。
  原 $e_n$ 的 rank 表、trace-fixed theta 与闭 subgroup norm
  均按该文读取；本文 (1157.9)–(1157.18) 的整三函数 filling
  另给完整证明。
- R1156 §§2–6、§8：原 dilogarithm 上链、有限乘法关系见证、
  四线符号、prime-to-$p$ 辅助域、实际 Cor/res 同伦及整塔补点。
  这里消费主线版本，包括其有限自由模见证和 ordered 修正。
- R1136、R1138：实际 $B_n$ 源、physical norm 的方向、
  两槽同子群相关项及原 moment comparison。
- o2_high_coefficient 已独立纸核原 rank/marginal、$n^4$
  contraction、三个留数的号与 $n^8$ 总尺度。
  无新数学程序执行，未加入任何数值非零或 $z_{12}$ 读数断言。
