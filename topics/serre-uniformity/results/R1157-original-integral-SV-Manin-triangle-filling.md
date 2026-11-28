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


## 10. 辅助数 2：保原常数的三个显式单位和 27 项 filling

### 10.1. 原来源确允许 2

本节把前文的辅助范围扩到 $n=2$，并保留所有原规范。
这不是另换一个只有相同 divisor 的 theta。

Sharifi–Venkatesh §6.3.1 在系数
$\mathbb Z[1/30]$ 中对任意辅助素数 $n\nmid N$ 定义
$\theta_n,\theta'_{n,C}$。该节脚注 19 特别说明：
Kato 在 $\mathbb Z$ 系数下排除 $2,3$；
本处已反除的 $24$ 则使 trace-fixed divisor 的提升存在且唯一。
因此 (1157.4)–(1157.7) 的原 theta 和范数恒等式适用于 $n=2$。

前文其余代数证明只反除 $n,2,3$。在本节
$|{\rm GL}_2(\mathbb F_2)|=6$，所以二扭点 splitting field
的次数也 prime-to-$p$。于是 §§2–8 的原三项上链、
固定函数整塔与 noncusp 延伸都继续成立。
特别不需将原 $E[p]$ 标记升级为 $E[p^r]$。

### 10.2. 从真正 norm 确定 theta 的全部常数

先在二扭点 splitting field 上写
$$
E:\quad y^2=(x-e_1)(x-e_2)(x-e_3),\qquad
A_i=(e_i,0),\qquad
K_i=\prod_{j\ne i}(e_i-e_j).
$$
采用原 Weierstrass 判别式
$$
\Delta=16\prod_{i<j}(e_i-e_j)^2=-16K_1K_2K_3.
\tag{1157.24}
$$
这里只使用 characteristic zero 的非退化纤维，三个 $K_i$ 都非零。

二扭点平移的实际坐标公式是
$$
x(T+A_i)=e_i+\frac{K_i}{x(T)-e_i},\qquad
y(T+A_i)=-\frac{K_i\,y(T)}{(x(T)-e_i)^2}.
\tag{1157.25}
$$
第一式来自原加法律；对其微分并使用
$dx/(2y)$ 的平移不变性，得到第二式，故其负号固定。

记 $t=[\theta_2]$ 为乘法群中的加法类。因为
$\operatorname{div}(-[y])=4[O]-[E[2]]$，两者仅相差一个
来自基域的常数类，该常数在平移比值中消失。
于是
$$
R_i(T):=-\frac{(x(T)-e_i)^2}{K_i},\qquad
t(T+A_i)-t(T)=[R_i(T)].
\tag{1157.26}
$$
$R_i$ 是实际函数，方括号才表示其 $K_1$ 类。
本节不把乘法比值与其加法类混写。

精确函数等式给
$$
\prod_{i=1}^3R_i(T)=\frac{16y(T)^4}{\Delta}.
$$
另一方面，原 (1157.7) 的全 $E[2]$ norm 为零，故
$4t+\sum_i[R_i]=0$。因此原 trace-fixed theta 的实际四次方
代表完全确定为
$$
\boxed{\quad
4[\theta_2]=[\Theta],\qquad
\Theta(T)=\frac{\Delta}{16y(T)^4}.
\quad}
\tag{1157.27}
$$
这一步使用实际 norm，而不只比较 divisor；
$\Delta$ 和 $16$ 都不能省去。

令 $C_i=\{O,A_i\}$。同一原范数式
$2[\theta'_{2,C_i}](T)=t(T)+t(T+A_i)$ 给
$$
\boxed{\quad
4[\theta'_{2,C_i}]=[\Theta_i],\qquad
\Theta_i(T)=\Theta(T)R_i(T)^2
 =\frac{\Delta(x(T)-e_i)^4}{16y(T)^4K_i^2}.
\quad}
\tag{1157.28}
$$
所以无需另选 $K_i$ 的平方根，也没有新留待校准的 theta 常数。

$\Theta,\Theta_i$ 均为真实 weight-zero 函数：
在 Weierstrass 变换 $x\mapsto u^2x,\ y\mapsto u^3y$ 下，
$\Delta\mapsto u^{12}\Delta$、$K_i\mapsto u^4K_i$，
两式的权恰相消。它们在非退化族的 $E-E[2]$ 上为单位。
非零 $p$-扭点代入因而给原全 noncusp 标记曲线上的实际单位，
而非未消 Hodge 权的单个 division polynomial。

### 10.3. 可直接用于兼容根的精确函数关系

上述代表满足以下字面上的乘法恒等式：
$$
\begin{aligned}
\prod_iR_i(T)&=\Theta(T)^{-1},\\
\Theta(T+A_i)&=\Theta(T)R_i(T)^4,\\
\Theta_i(T)^2&=\Theta(T)\Theta(T+A_i),\\
\prod_i\Theta_i(T)&=\Theta(T),\\
\prod_{A\in E[2]}\Theta(T+A)&=1.
\end{aligned}
\tag{1157.29}
$$
例如第二式由 (1157.25) 直接给出；第三、四、五式
再分别由 (1157.28) 和第一式得到。
对平移比值还精确有
$$
R_i(T+A_i)=R_i(T)^{-1},\qquad
R_j(T+A_i)=\frac{R_k(T)}{R_i(T)}
\quad(i,j,k\text{ 两两不同}).
\tag{1157.30}
$$
后一式也可直接写成
$y(T+A_i)/y(T+A_i+A_j)$，不需重新选择常数。

因此可以从 $\Theta,\Theta_i,R_i$ 的同一兼容
$p^\infty$ 根塔开始，按 $4\in\mathbb Z_p^\times$ 的逆映射
恢复原 $\theta_2,\theta'_{2,C_i}$ Kummer 塔。
每个 (1157.29)–(1157.30) 等于 $1$ 的乘积仍记录其实际根相位；
它们作为 R1156 的 $d\rho$ 输入，而非被假设在任意选根下为零。
这些原关系只涉及二扭点 splitting field，不要求另加平方根。

### 10.4. 原三角形成为 27 个完全指定的三函数项

仍取前文的非零 $P,Q,-P-Q\in E[p]$，
并令 $B_0=0,B_1=P,B_2=P+Q$。
(1157.13) 的原函数此时就是
$$
f_{A_i}^{(j)}(T)=[R_i(T-B_j)],\qquad f_0^{(j)}=0
$$
的加法记号。故 (1157.14) 完全变为
$$
\boxed{\displaystyle
\mathcal K_{2;P,Q}
 =-\frac1{256}\sum_{i,j,k=1}^3 w_{ijk}\,
 [R_i(T)]\wedge[R_j(T-P)]\wedge[R_k(T-P-Q)],
}
\tag{1157.31}
$$
其中
$$
w_{ijk}=
\begin{cases}
6,&i=j=k,\\
-2,&\text{恰有两个下标相同},\\
2,&i,j,k\text{ 两两不同}.
\end{cases}
\tag{1157.32}
$$
这是 $w(A_j-A_i,A_k-A_j)$ 的原 rank 表：
三下标全同给 rank 0；恰两同给 rank 1；
三个非零二扭点全异时两差独立，给 rank 2。
所以仍保原 $-2^{-8}$，不能凭函数中的平方另猜一个总尺度。

三个支持陪集仍两两不交；原 §5 的全部分母和负 base 点
消去逐字适用。因此
$$
\operatorname{Res}\mathcal K_{2;P,Q}
 =B_2(P,Q)+B_2(Q,-P-Q)+B_2(-P-Q,P).
\tag{1157.33}
$$
把 (1157.31) 的实际函数代入 R1156 四线程序，给出同一
原三项的连续整 primitive，并保全部常数 $-K_i^{-1}$。
不能把每个 $R_i$ 擅自换成 $(x-e_i)^2$：
常数在 $K_3$ 三槽中的交叉项仍属于原有限关系见证。

27 项只是三函数源的项数，不是声称最终四线展开恰有 27 项。
所有辅助二、三次域、Cor/res 同伦和完整兼容根规范仍照原文保留。

### 10.5. 接到已成的最高矩相关 torsor

[R1158](R1158-original-weighted-Manin-pushout-and-correlation-torsor.md)
已将 §9 当时保留的共同商、完整 ordered 双线性 pushout
及算术下降全部支付。
它的显式 S/U polynomial filling 也只反除 $2,3$，
因此以本节 $n=2$ 的原 raw primitive 作输入后，
同样给真实 $\mathcal G_2^{\rm corr}$-torsor。
rank-one 项仍完整；需要零 theta 的三项权仍严格为零。

R1158 (1158.21)–(1158.24) 的原 theta 比较和根 gauge 给
$$
\begin{aligned}
X_{2,4}&=\frac{63}{16}\mathsf M_4,&
X_{2,8}&=\frac{1023}{256}\mathsf M_8,\\
X'_{2,C,d}&=2\mathsf M_d^{\,C}-2^{-d}\mathsf M_d,
&&d=4,8.
\end{aligned}
\tag{1157.34}
$$
这里仍是按 $\operatorname{Sym}^d(\psi_C^{-1})$ 运输的
原 $2$-isogeny quotient，Tate factor 不另改规范。
由于 $63=3^2\cdot7$、$1023=3\cdot11\cdot31$，
两个显示平滑系数对所有 $p>37$ 都是单位。
这是实际交换商的简化，不是中央 cochain 的反除。

还可准确记录后继中央比较的几何标量。
相同 theta 范数对 $d=12$ 给
$$
T_2\mathsf M_{12}=(2+2^{-12})\mathsf M_{12}.
\tag{1157.35}
$$
事实上，$\sum_CX'_{2,C,12}=X_{2,12}$；代入
$X'_{2,C,12}=2\mathsf M_{12}^{\,C}-2^{-12}\mathsf M_{12}$
和 $X_{2,12}=(4-2^{-12})\mathsf M_{12}$，
再除唯一的单位 $2$，即得此式。
原 $\mathsf M_{12}$ 的几何 cusp residue 是 $1/12$，所以
(1157.35) 确给最高 $\operatorname{Sym}^{12}\mathcal H(2)$
一维几何 $H^1$ 的同一 eigenvalue。

因此在该一维层上
$$
\begin{aligned}
V_2&=16-4T_2+2^{-11},\\
v_{\rm top,2}
 &=16-4(2+2^{-12})+2^{-11}
   =\frac{16383}{2048}
   =\frac{3\cdot43\cdot127}{2^{11}}.
\end{aligned}
\tag{1157.36}
$$
对 $p>37$，其且仅可能在 $p=43,127$ 失去单位性。
本式不声称已经构造 $V_2-v_{\rm top,2}$ 的算术链同伦。
尤其不能只由 (1157.36) 将 (1157.31) 给的相关中央 primitive
除以这个数，并称所得就是原未平滑 $z_{12}$。

### 10.6. 实际使用范围

本节给出了原 $n=2$ 来源的全部 theta 常数、严格平移关系、
27 项三函数式和可直接复用的原 moment/root 接口。
新证明仅使用 SV 原允许的 $n=2$ 及明确函数代数；
没有执行数学程序。

在 supersingular $p$-进退化中，原 $p$-扭点可同时趋向原点。
故合法的 characteristic-zero 四线展开仍可能出现
cross-ratio 的约化为 $0,1,\infty$。
本节没有据此把所有四线参数都宣成 R1155 的 good-unit 输入，
也没有删去坏参数的相位、局部或五项修正。
同样，(1157.36) 只记录真正几何 Hecke 标量；
算术路径修正和未平滑中央读数仍各自保留。

o2_high_coefficient 已独立纸核本节的函数符号、四次方常数、
27 项权、两个平滑系数和 $v_{\rm top,2}$ 的显示标量。

root 已亲读 SV §6.3.1 与脚注19，并逐式核准二扭平移、Δ/16 的实际 norm 常数、五条严格乘法关系及所有27项的权；原各前节保留，n=2 的范围由本节明确扩展。原算术 Hecke 上链的后继接口已由 R1159 给出完整 J_n，未平滑同伦仍继续。


## 11. 二同源源的实际两切线展开与并发四线分支

### 11.1. 用一个非零五扭点统一分离支撑

本节沿用 §10 的 $E[2]$ splitting field，再加入 $E[5]$
并选 $T_0\in E[5]\setminus0$。总 splitting degree 的质因子
只可能为 $2,3,5$，所以对 $p>37$ 仍为 $p$ 单位。
$T_0$ 只用于平面模型和实际函数分解；原原点、$p$-标记、
$\theta_2$ 及其 Kummer 根均不改换。

以
$$
X(T)=x(T-T_0),\qquad Y(T)=y(T-T_0)
$$
给出平面模型，平面无穷远点是物理点 $T_0$。
原群法记号保持不变。置
$$
B_0=0,\quad B_1=P,\quad B_2=P+Q,\qquad
R_{j,a}=B_j+a\ (a\in E[2]),\qquad
S_j=3T_0-2B_j.
\tag{1157.37}
$$
对于 $W=R_{j,a}-T_0$，取 $Y$ 系数为 $1$ 的实际切线
$$
\ell_{j,a}(T)
 =Y(T)-y(W)
   -\frac{3x(W)^2+A}{2y(W)}(X(T)-x(W)),
\tag{1157.38}
$$
其中原短模型是 $y^2=x^3+Ax+B$。
$W$ 的 $5$-primary 分量为 $-T_0$，因此它既不是原点，
也不是二扭或三扭点；式中分母非零，切线不是 flex 切线。

三次平面曲线的切线 divisor 给
$$
\operatorname{div}(\ell_{j,a})
 =2[R_{j,a}]+[S_j]-3[T_0].
\tag{1157.39}
$$
这里第三交点是 $S_j$，与同组的 $a$ 无关。
因此
$$
\operatorname{div}\frac{\ell_{j,A_i}}{\ell_{j,0}}
 =2[B_j+A_i]-2[B_j].
$$
两个切线在 $T_0$ 的最高极项系数相同，故比值在 $T_0$
的极限为 $1$。与原 $x$ 函数比较，得到完整常数式
$$
\begin{aligned}
x(T-B_j)-e_i
 &=\bigl(x(T_0-B_j)-e_i\bigr)
       \frac{\ell_{j,A_i}(T)}{\ell_{j,0}(T)},\\
\boxed{\quad
R_i(T-B_j)
 =R_i(T_0-B_j)
       \left(\frac{\ell_{j,A_i}(T)}{\ell_{j,0}(T)}\right)^2.
\quad}
\end{aligned}
\tag{1157.40}
$$
它对 $j=0$ 也成立。这里没有将归一常数
$R_i(T_0-B_j)$ 设为 $1$。

选择五扭点使全部支撑分离成为确定事实。
若 $j\ne k$，则 $B_j-B_k$ 是非零 $p$-扭点，所以
$B_j+a\ne B_k+b$。
每个 $S_j$ 的 $5$-primary 分量为 $3T_0\ne0$，故
$S_j\ne B_k+b$；而 $S_j=S_k$ 会迫 $2(B_j-B_k)=0$，
也不可能。
所以来自两个不同 $j$ 的切线的零 divisor 没有公共点。
这些线的两两交点都不在 $E$ 上，线本身也不相同。
所有依赖点对仍在此范围，未排除任何形如 $Q=aP$ 的分支。

### 11.2. 只需三条切线和一条参考线

取参考直线 $\ell_0$，避开上面有限个零点及全部切线的
两两交点，并使 $\ell_0\cap E$ 横截。
这些条件构成直线参数空间中的非空 Zariski 开集，
可在当前无限 characteristic-zero 基域中取值。
其三次交点的 splitting field 次数至多 $6$，仍 prime-to-$p$。

由 (1157.40)，每个三函数项都是
$$
[R_i(T-B_j)]
 =[R_i(T_0-B_j)]
  +2\left(
       [\ell_{j,A_i}/\ell_0]-[\ell_{j,0}/\ell_0]
     \right).
\tag{1157.41}
$$
将它逐槽代入 (1157.31)，只是有限三线性展开。
每个非常数三槽从三个不同的 $j$ 各取一条实际切线。

含常数的项仍须保留。
它们的总 residue 由 degree-zero 及实际 Weil reciprocity
变成有限乘法关系；R1156 的同根 $d\rho$ 修正消费这些关系。
不能因为其外积总 residue 为零，就把原 ordered 中央上链
中的相位也删掉。

若所取三条切线不并发，连同 $\ell_0$ 就是 R1156 §4
所需的四线一般位置，直接消费该节的有限 Bloch 见证。
若三条切线并发，下一段给完整替代式；
因此本节不需要通过删除某些点对来强迫所有三线项一般位置。

### 11.3. 三线并发时的精确 finite Bloch 见证

设三个不同的切线 $\ell_1,\ell_2,\ell_3$ 并发。
其交点不在 $E$ 上，已由 §11.1 支付。
在保留原线尺度的情况下写
$$
f=\ell_1/\ell_0,\qquad g=\ell_2/\ell_0,\qquad
h=\ell_3/\ell_0=\alpha f+\beta g,\qquad \alpha\beta\ne0.
$$
令
$$
u=-\frac{\alpha f}{\beta g},\qquad c=-\frac{\beta}{\alpha}.
$$
于是 $f=cug$、$h=\beta g(1-u)$，给出字面三外积恒等式
$$
\begin{aligned}
[f]\wedge[g]\wedge[h]
={}&[c]\wedge[g]\wedge[\beta]
 +[c]\wedge[g]\wedge[1-u]\\
&+[u]\wedge[g]\wedge[\beta]
 -[u]\wedge[1-u]\wedge[g].
\end{aligned}
\tag{1157.42}
$$
所有 $\alpha,\beta,c$ 都是实际函数域常数，并被保留。
式 (1157.42) 不先将三条线各自任意规范化。

对前三项沿整条 $E$ 求 residue：
第一项由 $\deg\operatorname{div}g=0$ 消去；
另两项分别由 $(g,1-u)$ 和 $(u,g)$ 的真实 Weil
乘法关系消去。消去在有限自由单位模的关系见证中进行，
之后仍作相应的根相位修正。

最后一项给
$$
\mathcal B_{\rm conc}
 =-\sum_{Z\in E}\operatorname{ord}_Z(g)\,[u(Z)]_{\rm Bl}.
\tag{1157.43}
$$
这里先在分裂相关闭点的共同有限域上求和，
$[\,]_{\rm Bl}$ 是 pre-Bloch 生成元；
$u(Z)=0,1,\infty$ 的项按退化值 $0$ 处理。
这不是在未定义处选一个普通 dilogarithm 值。

该退化约定直接来自 residue：
$u=0$ 或 $1$ 时另一个 Steinberg 因子的首值为 $1$；
$u=\infty$ 时 $u$ 与 $1-u$ 的首值比为 $-1$，
只余二扭项，在本处反除 $2$ 后消失。
因此没有遗漏 $g$ 在这些点的阶。

$g$ 的零点位于 $\ell_2\cap E$，其 $u$ 值为 $\infty$；
参考线的避点条件则保证在 $\ell_0\cap E$ 上
$u$ 不为 $0,1,\infty$。故 (1157.43) 简化为
$$
\boxed{\quad
\mathcal B_{\rm conc}
 =\sum_{Z\in\ell_0\cap E}
        \operatorname{mult}_Z(\ell_0\cap E)\,[u(Z)]_{\rm Bl}.
\quad}
\tag{1157.44}
$$
其 $\delta_{\rm Bl}[u]=[u]\wedge[1-u]$ 边界，
连同已明确的 degree/Weil 关系，正是原三外积的总 residue。
所有闭点的实际 Cor 及 R1156 的 cup 同伦仍在同一分裂域、
同一陪集和根规范下下降；未另外假造 pre-Bloch 群上的 norm。

于是 (1157.41) 的每一项都有确定的有限来源：
不并发时用原四线公式，并发时用 (1157.42)–(1157.44)。
这替代了通用 Miller 分解中再选三个辅助点的步骤，
但没有省掉常数或 ordered cochain 修正。

### 11.4. Supersingular 退化中哪些部分已是整单位

这一段只记录本来源的局部性质。
设原 $E$ 在未分歧 $p$-进域上有 good supersingular reduction。
可先作未分歧扩张分裂 $E[2]$ 和 $E[5]$，再加入原 $p$-标记；
后一扩张允许分歧。

所有原 $p$-扭点都约化到原点，而 $E[2],E[5]$ 的非零点
仍保相应阶。因此
$$
R_{j,a}-T_0\ \longmapsto\ a-\bar T_0
$$
既不是原点也不是二扭点。
(1157.38) 的 $Y$ 系数 $1$ 规范、斜率以及
(1157.40) 的常数 $R_i(T_0-B_j)$ 都为整的，
且该常数是单位。$\Delta$ 和全部 $K_i$ 也是单位。

参考线也可选择为整线，约化后避开
$E[2]\cup\{3\bar T_0,\bar T_0\}$ 并横截于 $E$。
为说明存在性，令剩余域大小为 $q\ge p>37$：
至多六个指定点排除 $6(q+1)$ 条线；
一条有理切线的切点必为有理点，因为三次曲线的同一条线
不可能在两个不同点各有至少二重交。故有理切线条数至多
$\#E(\mathbb F_q)\le q+1+2\sqrt q$。
其和严格小于 $q^2+q+1$，所以存在所需剩余域直线。
再在该 residue class 内选择 characteristic-zero lift，
可同时避开前面有限个额外的实际交点。
此时 $\ell_0\cap E$ 为有限 étale 的三次局部代数。

这些结论没有使所有 primitive 参数都成为 good-unit。
实际三条切线可能不并发，却在约化后并发；
相同二扭下标的切线还可能约化为同一条线。
一般四线式因而仍可出现趋向 $0,1,\infty$ 的参数。
(1157.44) 只用于真正 characteristic-zero 并发的分支，
不能因为 mod-$p$ determinant 为零就提前使用它。
原 R1155 的运输、五项和坏参数修正继续按实际分支保留。

本节由 root 的实际两切线恒等式出发；
$E[5]$ 的统一避位、全部原常数以及并发分支在正文另给证明。
o2_high_coefficient 已纸核 (1157.42)–(1157.44) 的符号和
$u=\infty$ 的完整 residue。未执行数学程序，
也未将本源的整性升级为原 $z_{12}$ 已读出。

root 全文核准统一五扭平移、切线最高极项及准确常数，核定三个支撑组全部分离、并发式的逐valuation residue（含u=∞的二扭项）与剩余域参考线计数。局部整参考线的选择仅描述所选分解；若替换已固定的 global filling，仍保同根/五项与ordered修正，不借局部中心唯一性直接替换。R1160已付最高矩的算术未平滑上链接口，一般Frobenius读数继续。


## 12. 三次辅助点给原全部二同源四线参数的精确 SS 阶

本节在一个明确的原局部范围内补全 §11.4 的坏参数检测。
设 $p>37$，原 $E/\mathbb Q_p$ 有 good supersingular reduction，
取整短模型及 $\omega=dx/(2y)$。
以下也适用于同一模型的未分歧扩张。
不把仅在 $\mathbb F_{p^2}$ 上存在的另一条曲线冒充这个原模型。

原 $P,Q,P+Q\in E[p]$ 均非零；允许 $Q=aP$。
仍取 $B_0=0,B_1=P,B_2=P+Q$。
本节只更换用于有限函数分解的辅助点，不改这些标记、
原点、$\theta_2$、(1157.31) 的27个权或目标 moment。

### 12.1. 一个确实三次且避免所有首项抵消的辅助点

令 $\bar E/\mathbb F_p$ 为原约化。
Supersingular 的迹被 $p$ 整除，Hasse 界及 $p>3$ 给迹为零，
故原 Frobenius 满足
$$
\pi^2=[-p].
$$
因此 $\bar E[2]$ 全在 $\mathbb F_{p^2}$ 上。
置
$$
M=p^2-p+1
$$
并在 $\bar E[M]$ 中选一个准确阶为 $M$ 的点 $\bar T_0$。
这里 $p\nmid M$，故这样的几何点存在。
$\sigma=\pi^2$ 在它上面是 $[-p]$，而
$$
p^3+1=(p+1)M,\qquad
1+\sigma+\sigma^2=[1-p+p^2]=[M].
$$
所以 $\bar T_0$ 属于 $\bar E(\mathbb F_{p^6})$，
在 $\mathbb F_{p^2}$ 上恰有三个不同共轭，
且三点的和为零。它们在原平面模型中位于同一条
$\mathbb F_{p^2}$ 直线，该直线与 $\bar E$ 横截。

还有本节真正需要的严格条件
$$
\boxed{\qquad
x(3\bar T_0)\notin\mathbb F_{p^2}.
\qquad}
\tag{1157.45}
$$
若该 $x$ 坐标在 $\mathbb F_{p^2}$，则
$\sigma(3\bar T_0)=\pm3\bar T_0$，
从而 $3\bar T_0$ 的阶整除 $p-1$ 或 $p+1$。
但其阶为 $M/\gcd(M,3)>p+1$，矛盾。
同样 $x(\bar T_0)\notin\mathbb F_{p^2}$。
特别 $\bar T_0\notin\bar E[6]$，
$3\bar T_0$ 与全部二扭点不同。

把上述横截直线提升成整直线，其与 $E$ 的交是
有限 étale 的三次代数。选约化到 $\bar T_0$ 的点 $T_0$。
只需这一实际三次闭点及其至多六次 splitting field；
**不需要加入整个 $E[M]$**，也不要求所选特征零 $T_0$
仍为 $M$-torsion。
从原 $\mathbb Q_p$ 出发，局部只增加未分歧二次、三次域。
在原全局函数域中，也可先用一个二次常数域实现所需剩余域，
按同余条件提升直线，再取其三次交点；
所用额外 Galois splitting degrees 的质因子只有 $2,3$。

原有限域迹结论可见 Sutherland 的
[18.783 Lecture13，Theorem13.3、Corollary13.4及紧随的Frobenius特征式](https://ocw.mit.edu/courses/18-783-elliptic-curves-spring-2021/6b139f926bbbe94db322ea23300b0246_MIT18_783S21_notes13.pdf)；
本节的 $M$、三次点及 (1157.45) 另由上述整式证明。

### 12.2. 原 $p$-点的共同首项与两切线函数

记
$$
e=p^2-1,\qquad \rho=e\,v_p.
$$
高度二 formal group 的 $[p](T)$ 在 $T^{p^2}$ 项有单位系数，
其所有更低非线性项都被 $p$ 整除。
$[p](T)/T$ 的首个 Newton polygon 线段端点为
$(0,1),(e,0)$。因此每个非零原 $p$-点都有
$$
v_p(t(P'))=\frac1e
$$
且任意两个不同原 $p$-点的参数差也有该赋值。
后一事实也可由整 formal-group 差
$t(P')-t(P'')=t(P'-P'')\cdot\text{unit}$ 得到。

固定一个非零首项作尺度。
由同一 $[p]$ 方程，各非零 $t(P')$ 的首项之比是
$(p^2-1)$ 次单位根；原 formal 加法使全部首项组成
一个准确的 $\mathbb F_p$ 二维空间。
所以在这一尺度下，首项恰为 $\mathbb F_{p^2}$，
而不同点的首项不同。
这里没有把完整 $p$-标记域误当未分歧域。

沿 §11 使用 $X(T)=x(T-T_0),Y(T)=y(T-T_0)$。
对 $a\in E[2]$ 和 $B$ 在原点的小盘，令 $L_a(B)$
为 $Y$ 系数等于一、在物理点 $B+a$ 相切的直线。
其零 divisor 仍准确为
$$
2[B+a]+[3T_0-2B].
\tag{1157.46}
$$
因为 $\bar T_0\notin E[6]$，
$y(a-T_0)$ 及切线的所有分母都是单位；
切线在 $B+a$ 非 flex，并在第三点有单零。
于是 §11 的所有实际常数式 (1157.40)–(1157.41)
对本节的 $T_0$ 原样成立，
$R_i(T_0-B_j)$ 仍都是单位。

取整参考线 $L_0$，其约化避开
$E[2]\cup\{T_0,3T_0\}$ 并横截于 $E$。
在含 $T_0$ 的有限剩余域上，§11.4 的同一 Hasse 计数
保证可选。参考线交点为有限 étale 的三次代数。
下文证明还会给全部所需 line determinants 非零，
所以无需通过删除某些依赖点对来补一般位置。

### 12.3. 三种标签模式的实际 determinant 阶

从三个不同的 $B_j$ 各取一条切线，记为 $L_1,L_2,L_3$，
其二扭标签记为 $a_1,a_2,a_3$。
令 $D_{ijk}$ 表示三个实际 coefficient vectors 的 determinant。
则
$$
\boxed{\begin{array}{c|c}
\text{标签条件}&\rho(D)\\ \hline
D_{0ij},\ a_i\ne a_j&0\\
D_{0ij},\ a_i=a_j&1\\
D_{123},\ \text{三个标签不全相同}&1\\
D_{123},\ a_1=a_2=a_3&3
\end{array}}
\tag{1157.47}
$$
这些是精确阶，尤其全部 determinant 在特征零非零。

先看两条不同约化切线。
它们都经过 $S=3\bar T_0$，而 $L_0(S)\ne0$，
故 $D_{0ij}$ 是单位。
同标签时，$L_a(B)$ 与其一阶导数的交点是物理点 $a$：
切点的一阶移动仍使导数线经过该点。
参考线避开 $a$，且原切点非 flex，所以
$D_{0ij}=(t(B_j)-t(B_i))\cdot\text{unit}$。

恰两个标签相同时，同样先除这两个参数的差。
剩余 leading determinant 是 $L_a,L_a',L_b$。
在 $S$ 处，对
$L_a(B)(3T_0-2B)=0$ 求导得到
$$
L_a'(0)(S)=2\,\partial_T L_a(0)(S),
$$
右边是单位，因为第三交点是单交。
另一个 $L_b$ 与 $L_a$ 在 $S$ 横向相交，
故这个 determinant 是单位。

三个标签不同的首项需要使用 (1157.45)，不能只称一般位置。
设 $x_a=x(a)$ 对非零二扭点，并置
$$
l_a(Z)=Z-x_a\quad(a\ne0),\qquad l_0(Z)=1.
$$
任意三个不同的这些一次式有唯一线性关系
$$
\sum_{j=1}^3\mu_j l_{a_j}(Z)=0,
\qquad 0\ne\mu_j\in\mathbb F_{p^2}.
$$
原精确切线比值是
$$
\frac{L_a(B)(T)}{L_{a=0}(B)(T)}
=\frac{l_a(x(T-B))}{l_a(x(T_0-B))}.
\tag{1157.48}
$$
这里 $l_0=1$ 包括零二扭标签；参考线 $L_0$ 与该
$L_{a=0}$ 是不同记号。
令 $b_j$ 为 $t(B_j)$ 按共同尺度归一的首项。
在三线的共同约化交点 $S$ 对 (1157.48) 求导，
$D_{123}$ 的一次项相差一个非零公因子，正是
$$
\sum_j\mu_j\,l_{a_j}\bigl(x(S)\bigr)b_j.
\tag{1157.49}
$$
$\mu_j,b_j$ 都在 $\mathbb F_{p^2}$，
而 $x(S)\notin\mathbb F_{p^2}$。
故此式若为零，其常数及 $x(S)$ 系数都必须为零。
两行系数矩阵的秩为二，共同核是
$b_1=b_2=b_3$ 这一条线；
这与原三个 $B_j$ 不同矛盾。
所以一次项不消，支付第三行中全部三个不同标签的情形，
包括原 $P,Q$ 依赖时的首项。

最后考虑全同标签。
写 $\mathbf P=(x,y,1)$，导数按原不灭微分取。
$Y$ 系数一的切线向量是
$\ell=(\mathbf P\times\mathbf P')/(2y)$。
直接行列式运算给
$$
\det(\ell,\ell',\ell'')
=\frac{\det(\mathbf P,\mathbf P',\mathbf P'')^2}{(2y)^3},
\qquad
\det(\mathbf P,\mathbf P',\mathbf P'')=2\psi_3(x),
$$
其中
$\psi_3=3x^4+6Ax^2+12Bx-A^2$。
在 $a-T_0$ 处，$y$ 和 $\psi_3$ 都是单位：
该点既非二扭也非三扭。
因此三个切线 determinant 除以
$\prod_{i<j}(t(B_j)-t(B_i))$
后的常数是
$\det(\ell,\ell',\ell'')/2$，为单位。
余项整，证明最后一行的精确阶三。
不同整参数与不灭微分的二阶导数只相差一阶项，
不改变这个 determinant 的单位性。

### 12.4. 原全部四线 Bloch 参数的完整阶表

每条 $L_i$ 的交点写成
$$
R_i=B_i+a_i\ \text{（重数二）},\qquad
S_i=3T_0-2B_i\ \text{（重数一）}.
$$
这里 $B_i$ 只是给所选三条线重新编的三个原点；
它们的集合仍为 $\{0,P,P+Q\}$。
由 (1157.46) 的真实零阶与支撑分离，对 $k\ne i$ 有
$$
\begin{array}{c|c}
\text{值}&\rho\\ \hline
L_k(R_i),\ a_k=a_i&2\\
L_k(R_i),\ a_k\ne a_i&0\\
L_k(S_i)&1\\
L_0(R_i),L_0(S_i)&0
\end{array}
\tag{1157.50}
$$
参考线的三个交点处，所有 $L_i$ 也都是单位。

写原线关系为
$$
L_3=\alpha_0L_0+\alpha_1L_1+\alpha_2L_2.
$$
按 (1157.47)，三个模式的
$(\rho(\alpha_0),\rho(\alpha_1),\rho(\alpha_2))$ 为
$$
(1,0,0),\qquad(1,0,1),\qquad(2,0,0),
\tag{1157.51}
$$
中间模式按 $a_1=a_3\ne a_2$ 写。
这只是为显示表格重标三槽；
在原外积和 ordered filling 中保留重标产生的符号。

将四线归一成
$l_0=\alpha_0L_0,l_1=\alpha_1L_1,l_2=\alpha_2L_2,
l_3=L_3=l_0+l_1+l_2$。
沿 R1156 的同一四线约定，参数分别为
$$
\begin{array}{c|c|c}
\text{所在直线}&u&1-u\\ \hline
L_1&-\alpha_2L_2/(\alpha_0L_0)&L_3/(\alpha_0L_0)\\
L_2&-\alpha_1L_1/(\alpha_0L_0)&L_3/(\alpha_0L_0)\\
L_3&-\alpha_1L_1/(\alpha_0L_0)&-\alpha_2L_2/(\alpha_0L_0)\\
L_0&-\alpha_2L_2/(\alpha_1L_1)&L_3/(\alpha_1L_1)
\end{array}
\tag{1157.52}
$$
因此连 $1-u$ 的阶也由实际另一个线值给出，
没有把两个单位相减后的可能抵消略去。

以下每项是 $(\rho(u),\rho(1-u))$：
$$
\boxed{
\begin{array}{c|c|c|c}
\text{点}&a_1,a_2,a_3\text{ 全异}
&a_1=a_3\ne a_2&a_1=a_2=a_3\\ \hline
R_1&(-1,-1)&(0,1)&(0,0)\\
S_1&(0,0)&(1,0)&(-1,-1)\\
R_2&(-1,-1)&(-1,-1)&(0,0)\\
S_2&(0,0)&(0,0)&(-1,-1)\\
R_3&(-1,-1)&(1,0)&(0,0)\\
S_3&(0,0)&(0,1)&(-1,-1)\\
L_0\cap E&(0,0)&(1,0)&(0,0)
\end{array}}
\tag{1157.53}
$$
最后一行逐个适用于参考线的三个实际交点。
原 $R_i$ 的重数二、$S_i$ 的重数一、
四线交替符号以及 (1157.32) 的 $6,-2,2$ 都保持，
未把该表当成不带重数的求和。

于是每个原非常数三槽产生的四线 primitive，
要么 $u,1-u$ 均为单位，
要么在 $u,\ 1-u,\ u^{-1}$ 中有一个的赋值准确等于
$1/(p^2-1)$。
本节实际上也排除了这些输入在特征零真正并发，
但没有将“约化并发”直接换成 §11.3 的并发式。

### 12.5. 全部这些参数的通用 Frobenius 已落入有限读取域

若 $u$ 整，由 (1157.53) 得
$$
\max\{v_p(u^p),v_p(1-u^p)\}
\in\left\{0,\frac{p}{p^2-1}\right\}<\frac13.
\tag{1157.54}
$$
近一情形的等式也准确：
若 $v_p(1-u)=1/e$，则在
$1-u^p=\sum_{j=1}^p(-1)^{j-1}\binom pj(1-u)^j$
中，末项的赋值 $p/e$ 严格小于前面每项。
因此不是只证明 $u^p$ 与某个 residue 常数接近。

本处读取的是
$$
R^\dagger(u)=R_{u^p}(u),
$$
即从 $u^p$ fibre 到 $u$ fibre 的原通用 Frobenius。
在 R1155 (1155.70)–(1155.73) 中
第二输入准确取 $v=u^p$、$\varepsilon=0$。
故对全部整的参数，完整有限值是
$$
\boxed{\quad
R^\dagger(u)\equiv
\mathcal H\left(
0,\
-\frac{\ell_{1,p}(u)}{1-u^p}
 +\frac{pu^p\ell_{2,p}(u)}{(1-u^p)^2},\
-\frac{\ell_{2,p}(u)}{1-u^p}
 +\frac{2pu^p\ell_{3,p}(u)}{(1-u^p)^2}
\right)\pmod{p\mathcal O_L}.
\quad}
\tag{1157.55}
$$
近一时保留两个显示的 $p$ 项；
坐标可非整，后续乘法仍按 R1155 §13.3 提高精度。

若 $v_p(u)=-1/e$，取同一实际逆参数 $t=u^{-1}$。
其第二输入也必须取 $(u^p)^{-1}=t^p$。
原 exact Coleman / Heisenberg 参数同构给
$J(a,b,h)=(-a,b-a,-h+a^2/2)$。
因 $R^\dagger(t)$ 的第一槽准确为零，得到
$$
\boxed{\quad
R^\dagger(u)\equiv
\mathcal H\left(
0,-\frac{\ell_{1,p}(t)}{1-t^p},
  \frac{\ell_{2,p}(t)}{1-t^p}
\right)\pmod{p\mathcal O_L}.
\quad}
\tag{1157.56}
$$
这里 $t$ 近零，分母为单位，所删的 Eulerian $p$ 项确入
$p\mathcal O_L$。这一步也没有把任意分歧域变成未分歧域。

**不能把 (1157.55) 的第二输入换成 $v=u$。**
坏参数时 $(u-u^p)/p$ 可以有负赋值，
不满足 R1155 的加法 carry 假设。
若后继已有共同底上的实际 $\psi$，还须逐参数保
$(\psi(u)-u^p)/p$；只有它整时才直接调用 (1155.73)。
本节没有构造这个共同 $\psi$。

### 12.6. 原分解、根规范及计算范围

三次辅助点给了一个真正的有限函数分解选择，
并逐项检测了其全部四线 primitive，包括原依赖点对。
(1157.40) 的 leading 常数全部保留。
同时，(1157.51) 中有正阶的 $\alpha_i$；
这些线归一常数并非全部单位，
其原 Kummer 根、相位及 ordered 修正也继续保留。

可以从一开始用这个三次点运行同一 R1156–1158 有限关系程序。
若要替换一份已经固定的 $E[5]$ 分解，
则使用那份程序的实际有限单位关系、
四线/五项见证、同根 $d\rho$ 以及 Cor/res 同伦来比较。
不能仅由一个局部中心空间的抽象唯一性宣布数值相同。

所以本节关闭的是原二同源四线源在所列
$\mathbb Q_p$-supersingular 代入处的坏参数阶门，
并给其全部 $u^p\to u$ 通用 primitive 的有限函数。
它不删任何有限 transfer、跨项乘积、算术路径或提升 carry，
不把单个 primitive 的读数直接称为
R1147–50 原 $F_0$ 的 $z_{12}$。
原 $n=2$ 在 $p=43,127$ 的未平滑标量例外仍沿
R1160 保持，未从本节的参数估值改变。

在原 Gaussian/cubic CM 模型、$p$ 对相应 CM 二次域惰性时，
还有一个实际形式源入口。$\mathcal O_{CM}/p=\mathbb F_{p^2}$
在 $E[p]$ 上的作用使后者为一维模，故每个上述实际点对都可写成
$Q=[\alpha]P$，$\alpha\in\mathbb F_{p^2}\setminus\{0,-1\}$。
选一个 CM 整数提升，在定义 CM 的未分歧二次域上，
$P(z),[\alpha]P(z),[1+\alpha]P(z)$ 是同一个整形式参数的实际端点。
本节首项证明只用它们在 $\mathbb F_{p^2}$ 中的首比，
故不限制为 $\mathbb F_p$-rank-one 点对。
完整函数的 $z$ 阶也按同一表给出 $u=z^j\cdot\text{unit}$、
$1-u=z^{j'}\cdot\text{unit}$，其中 $j,j'\in\{-1,0,1\}$；
这里 divisor 身份先给整幂的精确因子，表中的非零首系数再给单位。
这为整个 CM 形式源使用共同提升提供入口。
但形式操作 $z\mapsto z^p$ 一般不保持原 $E[p]$ 理想，
其与实际有限 FL/Frobenius 纤维的比较另须支付；
本节没有把这一形式入口当作该比较。

全部为原函数、有限域及正式幂级数的纸面推导。
没有数学程序执行。
