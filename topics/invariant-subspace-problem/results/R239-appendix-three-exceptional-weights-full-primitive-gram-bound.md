# R239 附录：三个独立异权位的相对出生二层及完整全出生 Gram 比较

- 日期：2026-11-13（UTC）
- 作者：AI 辅助研究；central_review / root
- 状态：已证明；root 全文独立核验并独立执行原 verifier 通过，所引用 R271 出生一层证书也独立执行通过
- 直接范围：池置换固定的三维相对出生二层；末节用已发表出生一层结果拼合整个三头模型

## 1. 定理及原源坐标

取
$$
D=a_1E_1+a_2E_2+a_3E_3+D_{\rm w},
\qquad a_i>0,
$$
其中等权池有
$$
L\ge3
$$
个位，每个位的权为一。固定出生为二，最高合法阶为
$$
h=L-1.
$$
完整整层 Gram 和 primitive 压缩始终按
$$
F_n=\frac{D^n(D^*)^n|_{\mathcal H_2}}{(n!)^2},
\qquad
\Gamma_n=P_{\ker D\cap\mathcal H_2}F_n^{-1}
\big|_{\ker D\cap\mathcal H_2},
\qquad 0\le n\le h
\tag{1.1}
$$
定义。整层逆存在，使用有限 incidence 满射及正对角去权；池置换群同时约化这些完整逆。

令固定 primitive 块为
$$
K_{\rm fix}=(\ker D\cap\mathcal H_2)^{S_L}.
$$
它准确为三维。

**定理 1。** 在这个真实三维块上，对全部合法比较严格有
$$
\boxed{
\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n
<
\frac{n+2}{n+3}\Gamma_{n-1},
\qquad 1\le n<L-1.
}
\tag{1.2}
$$
本定理本身没有删除其他池表示块，也没有把它们当成已由三维块自动覆盖。

用[一参数完整最小逆稿](R239-appendix-penultimate-primitive-fixed-block-exact-one-parameter-inverse.md)的坐标，但为避免分母，取坐标向量
$$
x=(x_1,x_2,x_3),\qquad
A_i=a_i^2,\qquad
A_R=\prod_{i\in R}A_i.
$$
池未归一对称向量仍是
$$
w_j=\sum_{|I|=j}e_I,\qquad \|w_j\|^2=\binom Lj.
$$
真实 primitive 源嵌入为
$$
\mathcal Zx=
\sum_{\varnothing\ne R\subseteq[3]}
(-1)^{|R|-1}\frac{a_R}{\binom L{|R|-1}}
\left(\sum_{i\in R}x_i\right)e_{[3]\setminus R}w_{|R|-1}.
\tag{1.3}
$$
记
$$
H_n=\mathcal Z^*F_n^{-1}\mathcal Z.
$$
实际算子坐标是源 Gram 乘回的
$$
H_0^{-1}H_n.
$$
因此 (1.2) 准确等价于
$$
H_nH_{n+1}^{-1}H_n
<
\frac{n+2}{n+3}H_{n-1}.
\tag{1.4}
$$
这一步只使用合法同余和实际复合次序。

## 2. 从完整最小逆到八状态矩阵

设
$$
d=L-n+1,\qquad C_n=\binom Ln,\qquad u=d-2.
$$
内部阶的一参数公式准确是
$$
x^*H_nx=
\min_z\sum_{R\subseteq[3]}
\frac{A_R}{\binom L{n+|R|-1}}
\left|\sum_{i\in R}x_i-z\right|^2.
\tag{2.1}
$$
该式来自完整空间最小解及池置换平均，不是试探上界。

对头子集定义占据列
$$
b_R=(1_{1\in R},1_{2\in R},1_{3\in R})^{\mathsf T},
\qquad v_R=(1,b_R)^{\mathsf T}.
$$
引入四种整数多项式权
$$
\begin{array}{c|c}
r&\sigma_r\\ \hline
0&d(d-1)(d-2)\\
1&n(d-1)(d-2)\\
2&n(n+1)(d-2)\\
3&n(n+1)(n+2)
\end{array}
$$
及
$$
w_R=\sigma_{|R|}A_R,\qquad
\mathcal M=\sum_Rw_Rv_Rv_R^*=
\begin{pmatrix}Z&m^*\\m&S\end{pmatrix}.
\tag{2.2}
$$
在内部参数下，二项式比值给
$$
\frac1{\binom L{n+r-1}}
=\frac1{\binom L{n-1}}
\frac{n^{\overline r}}{d^{\underline r}}.
$$
所以完成平方后的 Gram 是
$$
H_n=\frac1{\binom L{n-1}}
\frac{ZS-mm^*}{d(d-1)(d-2)Z}.
\tag{2.3}
$$

令
$$
K=ZS-mm^*,\qquad
\mathcal R=\frac{K}{n(d-2)}.
$$
除法在多项式环中准确发生，下面给不含除零风险的定义。由
$$
\binom Ln=\binom L{n-1}\frac dn
$$
得到
$$
\boxed{
H_n=\frac1{C_n}\frac{\mathcal R(n,d)}{(d-1)Z(n,d)}.
}
\tag{2.4}
$$

### 2.1 多项式矩阵的显式条目

对三个互异指标，置
$$
U_i=(d-1)(d-2)+(n+1)(d-2)(A_j+A_k)
 +(n+1)(n+2)A_jA_k,
$$
$$
V_i=d(d-1)+n(d-1)(A_j+A_k)+n(n+1)A_jA_k.
$$
逐项计算二元占据协方差，得到
$$
\boxed{\mathcal R_{ii}=A_iU_iV_i,}
\tag{2.5}
$$
$$
\boxed{
\mathcal R_{ij}
=A_iA_j(n+d)\left[
(d-1)(d-2)+2(d-1)(n+1)A_k+n(n+1)A_k^2
\right].
}
\tag{2.6}
$$
因此所有条目都是整数多项式。

### 2.2 零阶和最高阶仍由同一有限公式支付

在零阶，直接代入
$$
n=0,\qquad d=L+1
$$
得到
$$
\frac{\mathcal R}{(d-1)Z}
=\sum_{\varnothing\ne R\subseteq[3]}
\frac{A_R}{\binom L{|R|-1}}b_Rb_R^*,
$$
正是 (1.3) 的源 Gram。

在最高阶，直接代入
$$
n=L-1,\qquad d=2.
$$
只剩满头与其他头状态之间的成对项，(2.4) 准确给
$$
H_{L-1}
=\sum_{R\subsetneq[3]}
\frac{A_R}{\binom L{L+|R|-2}}
(b_R-\mathbf1)(b_R-\mathbf1)^*.
\tag{2.7}
$$
这是已付一参数最小逆的最高阶公式：删去不合法的全缺失输入，并强制常数参数等于三个坐标之和。这里未把分母为零的表达式当成极限定义。

所以 (2.4) 在全部所需阶都准确。其矩阵严格正定，标量
$$
Z>0
$$
也在两端保持严格为正。

## 3. Cauchy–Binet 给真实逆的两个小对象

取任意固定的八状态排列。对三个不同状态组成的有序集合，令其三行四列矩阵为
$$
V_I=(v_R^*)_{R\in I}.
$$
其带符号最大子式列记为
$$
c_I=\bigl((-1)^j\det(V_I\text{ 删第 }j\text{ 列})\bigr)_{j=0}^3,
$$
并令
$$
\widehat c_I=(c_{I,1},c_{I,2},c_{I,3})^{\mathsf T}.
$$
定义
$$
\mathcal Q
=\sum_{|I|=3}
\frac{\prod_{R\in I}w_R}{n^2(d-2)^2}
\,\widehat c_I\widehat c_I^*,
\tag{3.1}
$$
$$
\mathcal E
=\sum_{|I|=4}
\frac{\prod_{R\in I}w_R}{n^3(d-2)^3}
\,\det(V_I)^2.
\tag{3.2}
$$
退化小行列式的项取零；这些定义均在取消明确因子后再代入参数。

每个非零三状态项至少有两个非空状态和两个非满状态，因此分子分别含足够的因子；四状态项同理。具体权分解为
$$
w_R=A_R\,n^{1_{R\ne\varnothing}}\,
(d-2)^{1_{R\ne[3]}}\,\tau_{|R|},
$$
$$
(\tau_0,\tau_1,\tau_2,\tau_3)
=\bigl(d(d-1),d-1,n+1,(n+1)(n+2)\bigr).
$$
这使 (3.1)—(3.2) 是明确的整数多项式，包含零阶和最高阶。

同样，成对展开给
$$
\mathcal R
=\sum_{R<T}\frac{w_Rw_T}{n(d-2)}
(b_R-b_T)(b_R-b_T)^*.
\tag{3.3}
$$
证书直接从这八个物理头状态生成三个对象。

完整矩阵的 Cauchy–Binet 和块逆给
$$
\det K=Z^2\det\mathcal M,\qquad
\operatorname{adj}K
=Z(\operatorname{adj}\mathcal M)_{\{1,2,3\},\{1,2,3\}}.
$$
故准确有
$$
\boxed{
\operatorname{adj}\mathcal R=Z\mathcal Q,\qquad
\det\mathcal R=Z^2\mathcal E,\qquad
\mathcal R\mathcal Q=Z\mathcal E I.
}
\tag{3.4}
$$
在全部合法参数上，
$$
\mathcal E>0,\qquad
\mathcal R^{-1}=\frac{\mathcal Q}{Z\mathcal E}.
$$
两端的正性也由 (2.4) 的真实正 Gram 与 (3.4) 得到，不要求原四维矩阵在端点非退化。

## 4. 相邻不等式的准确整数分子

下标减和加分别表示
$$
(n,d)\mapsto(n-1,d+1),\qquad
(n,d)\mapsto(n+1,d-1).
$$
它们保持同一个池大小。合法比较的参数范围是
$$
n\ge1,\qquad d\ge3.
$$
二项式因子的准确比值为
$$
\frac{C_n^2}{C_{n-1}C_{n+1}}
=\frac{(n+1)d}{n(d-1)}.
$$
将 (2.4)、(3.4) 代入 (1.4)，只作正标量消元，得到等价的矩阵正性
$$
\boxed{
\begin{aligned}
\Delta={}&
(n+1)(n+2)(d-1)Z^2\mathcal E_+\mathcal R_-\\
&-n(n+3)(d-2)Z_-\mathcal R\mathcal Q_+\mathcal R
>0.
\end{aligned}
}
\tag{4.1}
$$
三个矩阵的夹乘次序完整保留。
下一节是该整数多项式矩阵在全参数区间的精确证书。

## 5. 全域证书分成两个完整区域

完整可执行代码为
[三异权出生二层 BigInt 证书](../notes/2026-11-13-three-exceptional-weights-birth-two-gram-certificate-central-review.mjs)。
它从八状态与 Cauchy–Binet 小行列式生成 (4.1)，并检查每个所需邻阶的
$$
\mathcal R\mathcal Q=Z\mathcal E I
$$
完整多项式恒等式。

### 5.1 阶数至少为二

在整数多项式环中代入
$$
n=2+x,\qquad d=3+y,
\qquad A_1,A_2,A_3>0,\quad x,y\ge0.
$$
将 (4.1) 按五个变量的单项式展开为对称系数矩阵。

共有
$$
32058
$$
个非零系数矩阵，每一个都半正定。精确校验按三个一阶、三个二阶和一个三阶主子式逐一执行；没有用数值特征值。它们的秩分布是
$$
5226\text{ 个秩一},\quad
14082\text{ 个秩二},\quad
12750\text{ 个秩三}.
$$
其中不含后两个参数、对应头单项式
$$
A_1^2A_2^2A_3^2
$$
的系数准确为
$$
M_*=
\begin{pmatrix}
2488320&1382400&1382400\\
1382400&2488320&1382400\\
1382400&1382400&2488320
\end{pmatrix}>0,
$$
$$
\det M_*=6424875937824768000.
$$
因此其余半正定系数只增加正性，准确有
$$
\Delta\succeq A_1^2A_2^2A_3^2M_*>0.
\tag{5.1}
$$
这覆盖全部该区域，包括参数边界。

### 5.2 剩余第一阶条带

固定
$$
n=1,\qquad d=3+y,\qquad y\ge0.
$$
该条带不依赖上一节的系数矩阵条件，而直接检查 Sylvester 所需三个主子式。

| 多项式 | 非零整数系数个数 | 明确的零次参数正项 |
|---|---:|---:|
| 第一对角元 | 1964 | 746496 A_1² A_2² A_3² |
| 左上二阶主子式 | 22852 | 481579499520 A_1⁵ A_2⁴ A_3³ |
| 完整行列式 | 103458 | 385175539364659200 A_1⁷ A_2⁶ A_3⁵ |

表中三个多项式的全部非零系数均严格为正。
因为三个头变量严格为正，表中的单项式已经使三个主子式严格为正；
因此 Sylvester 判据给
$$
\Delta>0.
\tag{5.2}
$$
两区域恰好覆盖全部合法整数阶和池大小。这证明定理 1。

### 5.3 可执行证书的整数安全界

主区域仅用稀疏多项式的整数加、减、乘。五个指数按底数三十二编码，每次乘法都先检查各指数次数和小于底数，因此不会把不同单项式混同。

第一阶条带按三个头指数分组，将最后一个变量的有限多项式编码为有符号平衡 BigInt 位段。完整输入条目的系数绝对值总和均不超过
$$
S=216000000000.
$$
三个主子式中任何中间系数的绝对值至多为
$$
6S^3.
$$
证书选位段底数
$$
B=2^{118}>12S^3.
$$
所以全部系数严格位于平衡位段的半底数内，整数乘法与逐位平衡还原准确实现符号多项式乘法，包含负的中间系数。

每个头指数在输入中至多为七，三次乘积至多为二十一，小于头指数编码底数三十二。最后一个变量的次数也在还原时逐项检查。
程序遍历每一个还原后的非零系数，检查正号、准确支持大小和上述明确正项。没有浮点截断、随机抽样或未经校验的机器整数运算。

## 6. 同一个三维块的反向加强

[全出生倒数权对偶](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)保持池置换固定块，因为物理对角去权与池置换交换。倒数权仍是三个任意正头权加同一个等权池。因此 (1.2) 与反向阶共同给
$$
\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n
<
\min\!\left\{
\frac{n+2}{n+3},
\frac{L+1-n}{L+2-n}
\right\}\Gamma_{n-1}.
\tag{6.1}
$$
这里使用了反向后恢复邻居次序的真实正算子反演同余，不是交换矩阵因子。

## 7. 与已发表出生一层定理拼合全部出生层

这一节明确区分来源。[R271 三异权完整出生一层定理](R271-appendix-three-exceptional-weights-full-birth-one-primitive-gram-bound.md)
已证明任意池大小至少一时，整个出生一层的严格系数一比较；
其主要三维块独立使用了另一份完整证书。本文不重计该结果。

现取三个任意正异权位与任意等权池，池大小至少一，并令
$$
N=M+3,\qquad K_s=\ker D\cap\mathcal H_s.
$$
依[两异权全出生稿](R239-appendix-two-exceptional-weights-full-birth-one-primitive-gram-bound.md)
所付的等权池正交 Lefschetz 链分解，取池 primitive 出生于某一层的链：
$$
L=M-2j,\qquad t=s-j,\qquad
h=N-2s=L+3-2t.
$$
每条链与三个头位的张量同时约化完整算子、伴随、所有完整 Gram 逆和 primitive 压缩。

固定一个合法相邻比较，则
$$
h\ge2.
$$
相对出生小于零没有目标；相对出生至少四时，两相邻层都具有全部八个头状态，池删除对角系数
$$
L-t+|F|+1
$$
严格非零，故 primitive 核为零。只须处理四种相对出生：

- 相对出生零：真空标量 Newton，严格系数小于一，允许池长零、一、二。
- 相对出生一：有池长至少一，直接使用已发表 R271 完整出生一层定理，其固定部分包含本约化块。
- 相对出生二：有池长至少三，正是定理 1，系数严格小于一。
- 相对出生三：有池长至少五，使用既有任意头权饱和固定线的正矩公式，系数严格小于一。

所需最高邻阶在每块都合法：分别为有效真空总位数、池长加一、池长减一、池长减三。
所有短池和端点均由这些准确范围支付，没有将短链免费套入更大的池假设。

于是各约化块的严格正差作有限正交直和，得到：

**推论 2（三独立异权位的完整全出生比较）。**
对任意正头权、任意等权池大小至少一，以及全部合法出生与阶数，
$$
\boxed{
\Gamma_n^{(s)}
(\Gamma_{n+1}^{(s)})^{-1}\Gamma_n^{(s)}
<
\Gamma_{n-1}^{(s)},
\qquad
1\le n<N-2s.
}
\tag{7.1}
$$
这里的完整全出生结论只声明系数一。R271 出生一层主块的来源没有给更小的出生因子，所以不能将 (6.1) 直接外推为整个模型的统一更小系数。

本文仍未证明任意多异权的完整相邻上界，也没有把有限等权池模型直接替换成原无限尾或真实 Schur 返回源。
