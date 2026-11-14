# R271 附录：四异权出生一的全部短池与完整固定块

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf。
状态：完整证明；四个短池的全部正权整数证书已经原样执行 PASS。

## 1. 新范围和真实 Gram

取四个任意正头权及 $L$ 个单位池位，
$$
D=\sum_{i=1}^4a_iE_i+\sum_{j=5}^{L+4}E_j,\qquad a_i>0.
$$
固定池置换群的出生一 primitive 块；串长为 $h=L+2$。
当 $L\ge1$ 时，该块维数为四。始终先取整个物理一孔层的逆，
$$
F_k=\frac{D^k(D^*)^k|_{\mathcal H_1}}{(k!)^2},
\qquad
\Gamma_k=P_{\ker D\cap\mathcal H_1}F_k^{-1}|_{\ker D\cap\mathcal H_1}.
$$
同一个源嵌入 $\mathcal E$ 的 Gram form 记为
$$
H_k=\mathcal E^*F_k^{-1}\mathcal E.
$$
非正交源坐标的真实算子是 $H_0^{-1}H_k$。所需比较准确等价于
$$
\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n\preceq c\Gamma_{n-1}
\quad\Longleftrightarrow\quad
H_nH_{n+1}^{-1}H_n\preceq cH_{n-1}.
\tag{1.1}
$$

[首低边](R271-appendix-four-exceptional-birth-one-first-low-edge-trace-bound.md)
已付 $L\ge3$ 的 $n=1$；
[第二低边](R271-appendix-four-exceptional-birth-one-second-low-edge-trace-bound.md)
已付 $L\ge4$ 的 $n=2$ 及全部长池固定块。
本稿补齐此前没有被这些范围覆盖的四个实际短池比较：
$$
\boxed{
(L,n)=(1,1),(2,1),(2,2),(3,2)
\ \Longrightarrow\
\operatorname{tr}(H_{n-1}^{-1}H_nH_{n+1}^{-1}H_n)<\frac94.
}
\tag{1.2}
$$
由正矩阵同余，(1.2) 同时给 (1.1) 的严格常数 $9/4$。
这些都是全正头权的有限恒等式结论，不以长池公式的形式边界代替真实短池约束。

## 2. 原多项式参数和全部非法状态

令 $X_I=\prod_{i\in I}X_i$，
$$
f(X)=\sum_{|I|=3}x_I X_I,\qquad
f_*=f([4])=\sum_{|I|=3}x_I,\qquad
z_R=\prod_{i\in R}a_i^2.
$$
源三元组按 $123,124,134,234$ 排列。
由 [R239 完整短池参数化 §11](R239-appendix-penultimate-primitive-fixed-block-exact-one-parameter-inverse.md)，
当 $L\ge1$ 时四个最高系数独立，源为
$$
\mathcal E f=
\sum_{r=3}^4(-1)^{r-3}
\frac{a_R}{\binom L{r-3}}f(R)e_{[4]\setminus R}w_{r-3}.
\tag{2.1}
$$
这里以及下文按所有相应大小的 $R$ 求和，且 $\|w_j\|^2=\binom Lj$。

第 $k$ 阶的合法状态准确是
$$
0\le k+|R|-3\le L.
\tag{2.2}
$$
全部真实解由次数至多三的多重仿射多项式
$$
F=f+P,\qquad \deg P\le2,\qquad
F(R)=0\quad\text{若 (2.2) 不成立}
$$
参数化，其完整最小范数是
$$
\boxed{
x^*H_kx=
\min_F\sum_{\text{合法 }R}
\frac{z_R}{\binom L{k+|R|-3}}\,|F(R)|^2.
}
\tag{2.3}
$$
所引 §11 逐项证明实际有限差分方程、参数穷尽性及完整 MP。
尤其，任意全空间解作池置换正交平均仍是解、范数不增加；
所以 (2.3) 给全 Hilbert 最小逆，而不是限制试探空间后的较大成本。

为使短池的两端约束完全可见，以下逐项解出本稿用到的全部参数。
记 $Q_I=X_I$（$|I|=2$）、$Q_*=X_3X_4$。

### 2.1 零阶

所有 $L=1,2,3$ 都有 $F_0=f$，合法秩为 $3,4$，无低次自由参数。
这给原源 Gram $H_0$，不是单位矩阵。

### 2.2 第一阶

当 $L=2,3$ 时，合法秩为 $2,3,4$，所以
$$
F_1=f+\sum_{|I|=2}\beta_IQ_I.
\tag{2.4}
$$
有六个低次参数。

当 $L=1$ 时，合法秩只有 $2,3$。除低秩零条件外还须 $F([4])=0$，
准确解为
$$
\boxed{
F_1=f-f_*Q_*+\sum_{\substack{|I|=2\\I\ne\{3,4\}}}
\beta_I(Q_I-Q_*).
}
\tag{2.5}
$$
只有五个自由参数，不能沿用六参数长池式。

### 2.3 第二阶

当 $L=3$ 时，合法秩为 $1,2,3,4$，所以
$$
F_2=f+\sum_i\beta_iX_i+\sum_{|I|=2}\gamma_IQ_I
\tag{2.6}
$$
有十个低次参数。

当 $L=2$ 时，合法秩为 $1,2,3$，空集及全头状态必须同时为零。
准确的九参数式为
$$
\boxed{
F_2=f-f_*X_4+
\sum_{i=1}^3\beta_i(X_i-X_4)
+\sum_{|I|=2}\gamma_I(Q_I-X_4).
}
\tag{2.7}
$$

当 $L=1$ 时，合法秩为 $1,2$。
将 (2.5) 的任意可行多项式取 $-F_1(1-X)$，恰得到全部解：
$$
\boxed{
F_2(X)=-f(1-X)+f_*Q_*(1-X)
-\sum_{I\ne\{3,4\}}\beta_I\bigl(Q_I(1-X)-Q_*(1-X)\bigr).
}
\tag{2.8}
$$
其三次齐次部分仍是原 $f$，不是换了源。
补集把合法秩 $2,3$ 双射到 $1,2$，反向同样成立，故仍为五参数。

### 2.4 第三阶

当 $L=3$ 时，合法秩为 $0,1,2,3$，唯一非法状态是全头。
全部十参数解为
$$
\boxed{
F_3=f-f_*X_4+\beta_0(1-X_4)
+\sum_{i=1}^3\beta_i(X_i-X_4)
+\sum_{|I|=2}\gamma_I(Q_I-X_4).
}
\tag{2.9}
$$
当 $L=2$ 时，合法秩为 $0,1,2$，全部六参数解是
$$
\boxed{
F_3(X)=-f(1-X)-\sum_{|I|=2}\beta_IQ_I(1-X).
}
\tag{2.10}
$$
这是 (2.4) 的准确补集式，三次齐次部分仍为 $f$。

以上每一式的独立性可直接从最高三次系数和随后二次、一次、常数系数读取。
它们在所有非法点为零；反过来依次解这些非法评价条件，或使用所列补集双射，
就得到全部允许的 $f+P$。没有删去一条可能影响最小范数的真实自由方向。

## 3. 同尺度的完整 Gram 与实际逆次序

四个待证例的前、中、后三阶低次维数分别为
$$
\begin{array}{c|c}
(L,n)&(\ell_{n-1},\ell_n,\ell_{n+1})\\ \hline
(1,1)&(0,5,5)\\
(2,1)&(0,6,9)\\
(2,2)&(6,9,6)\\
(3,2)&(6,10,10).
\end{array}
\tag{3.1}
$$
按 §2，将第 $k$ 阶可行多项式的合法评价写成
$$
F_k(R)=v_{k,R}^{\,T}x+u_{k,R}^{\,T}y.
$$
所有评价列都是整数列。设 $t_{k,R}=(v_{k,R},u_{k,R})$，置
$$
\mathcal G_k=\sum_{\text{合法 }R}
w_{k,R}z_R\,t_{k,R}t_{k,R}^{\,T},
\qquad
w_{k,R}=\frac L{\binom L{k+|R|-3}}.
\tag{3.2}
$$
在 $L=1,2,3$ 中，每个二项式只有 $1$ 或 $L$，故所有 $w_{k,R}$ 都是正整数。
三阶使用同一个真实尺度 $L$。

这些完整 Gram 都严格正定。
若一个参数列在所有合法点评价为零，§2 的构造使它在非法点也为零；
多重仿射布尔插值唯一性使整个多项式为零。
其最高三次系数先给 $x=0$，独立低次基随后给 $y=0$。
同理每个低次主块严格正定。

对中阶写
$$
\mathcal G_n=\begin{pmatrix}S&M\\M^T&C\end{pmatrix},
\quad
\Delta=\det C,\quad
K=\Delta S-M\operatorname{adj}(C)M^T.
$$
前、后完整 Gram 记为 $B=\mathcal G_{n-1}$、$G=\mathcal G_{n+1}$，置
$$
J_-=(\operatorname{adj}B)_{\rm top\,4},\qquad
J_+=(\operatorname{adj}G)_{\rm top\,4}.
$$
真实完整块逆及 (2.3) 给
$$
\boxed{
H_{n-1}^{-1}=\frac{LJ_-}{\det B},\qquad
H_n=\frac K{L\Delta},\qquad
H_{n+1}^{-1}=\frac{LJ_+}{\det G}.
}
\tag{3.3}
$$
尤其 $n=2$ 时前阶不是原始源 Gram；这里保留了全部低次参数的完整前逆。

因此，按实际矩阵乘序定义
$$
\mathscr N=\operatorname{tr}(J_-KJ_+K),
\qquad
\mathscr D=(\det B)\Delta^2(\det G)>0,
$$
准确有
$$
\boxed{
\operatorname{tr}(H_{n-1}^{-1}H_nH_{n+1}^{-1}H_n)
=\mathscr N/\mathscr D.
}
\tag{3.4}
$$
同尺度的 $L$ 因子相消，不额外乘长池的相邻阶乘比。

## 4. 四个完整整数系数证书

代码为：

[短池完整迹证书](../notes/2026-11-13-four-exceptional-birth-one-short-pool-trace-certificates-1cf.mjs)

原始代码 blob：
$$
\texttt{224054b13045ed45a0b45a0ed683f32642962449}.
$$

该自含脚本从 §2 的合法状态、完整评价列和 (3.2) 的正整数权开始。
Cauchy--Binet 生成三个完整行列式及伴随矩阵；
中阶用低次列的有符号余子式生成真实 $K$。
它另逐项检查
$$
B\operatorname{adj}B=(\det B)I,\quad
C\operatorname{adj}C=(\det C)I,\quad
G\operatorname{adj}G=(\det G)I,
$$
以及
$$
K=\Delta S-M\operatorname{adj}(C)M^T.
$$
这些身份在每一个短池例分别核验，使用完整矩阵，不只抽查其顶块。

以四个变量 $z_i=a_i^2$ 展开，准确结果为：

| $(L,n)$ | $\mathscr D$ 支持项数 | $9\mathscr D-4\mathscr N$ 最小正整数系数 | 取得最小值的一个指数 |
|---|---:|---:|---|
| $(1,1)$ | 1980 | 9 | $(13,13,10,10)$ |
| $(2,1)$ | 2285 | 589824 | $(23,15,15,15)$ |
| $(2,2)$ | 5949 | 9437184 | $(18,18,15,15)$ |
| $(3,2)$ | 6254 | 1594323 | $(28,28,25,25)$ |

每一例中，$\mathscr D$ 的全部非零系数严格正，
$\mathscr N$ 的系数非负且支持包含于 $\mathscr D$；
表列支持上的 $9\mathscr D-4\mathscr N$ 全部严格正。
所以对所有 $z_i>0$，
$$
9\mathscr D-4\mathscr N>0.
$$

为便于完整复算，六组非零 Cauchy--Binet 项数
$(\det B,\operatorname{adj}B,\Delta,K,\det G,\operatorname{adj}G)$ 分别是
$$
\begin{array}{c|c}
(1,1)&(5,10,162,195,10,45)\\
(2,1)&(5,10,303,309,14,91)\\
(2,2)&(11,55,1360,944,11,55)\\
(3,2)&(11,55,2068,1290,15,105).
\end{array}
$$
对应总头权次数是 $54,74,86,106$，最大单变量指数是 $18,23,23,28$。

所有符号和行列式都使用 BigInt 整数。
四变量指数以 base-$64$ 独立槽表示；每次乘法前检查指数和至多 $44$。
这一统一界也可从最大因子数读出：最大分母为
$10+10+10+14=44$ 个状态单项式，最大分子为 $9+11+13+11=44$。
实际最大输入指数是 $28$，没有槽间进位。
代码中的浮点比值仅为未用于任何断言的诊断输出；
结论的全部判断是逐整数系数符号与上述身份。
原样最终脚本已全部 PASS。

由 (3.4)，真实归一化迹严格小于 $9/4$。
以 $H_{n-1}^{-1/2}$ 同余后得到正矩阵，
其最大特征值不超过迹，所以 (1.2) 同时给 (1.1) 的严格算子序。

## 5. 反向短边和出生一固定块的全部池大小

[倒数权反向对偶](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)
保持单位池及其置换固定 primitive 块。
其实际 $B_1$ 是同一个全空间对偶映射的限制，并与池平均交换。
它把阶 $n$ 送到 $h-n$，邻居反转后使用
$$
AB^{-1}A\prec cC
\quad\Longleftrightarrow\quad
AC^{-1}A\prec cB
$$
恢复真实相邻次序。故表中每条边支付它的反向边；对应归一化迹也由相似和迹循环保持。

逐个池长核对全部合法相邻阶：

| 池长 | $h$ | 全部相邻阶及来源 |
|---|---:|---|
| $L=1$ | 3 | $n=1$ 由本稿；$n=2$ 由反向，均 $<9/4$ |
| $L=2$ | 4 | $n=1,2$ 由本稿，$n=3$ 由反向，均 $<9/4$ |
| $L=3$ | 5 | $n=1,4$ 用已证首低边常数 $2$；$n=2,3$ 用本稿及反向，常数 $9/4$ |
| $L\ge4$ | $L+2$ | 已证首边 $2$、次边 $8/3$，中段 R239 §10.4 的 $4L/(L-3)\le16$ |

还须付 $L=0$。此时不是四维源：R239 §11 的源条件为 $f([4])=0$，维数三，且 $h=2$。
将最小物理权整体缩放为一，这就是
[三个异权加一位池的完整四位角](R271-appendix-three-exceptional-weights-full-birth-one-primitive-gram-bound.md) §6.3，
其唯一相邻比较已有严格常数 $1$。
整体缩放仅给 $\Gamma_k$ 乘几何因子，不改变相邻常数。

因此本稿和已发布来源合在一起，得到：

**完整出生一固定块定理。** 对任意四个正头权、任意整数池长 $L\ge0$，在整个池固定出生一 primitive 块上，
$$
\boxed{
\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n\preceq16\Gamma_{n-1},
\qquad 1\le n<L+2.
}
\tag{5.1}
$$
各短池的更小常数见上表。所有最高所需逆、两端约束及无池角均已付清。

这一步完成的是固定出生一块。整个四异权模型的所有出生和所有弱池表示，还须按真实 $D,D^*$ 的共同正交串逐块运输完整逆；本文不以一般压缩自动代替那一步。
