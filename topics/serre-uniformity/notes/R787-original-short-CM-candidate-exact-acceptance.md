# 原短 CM 候选的准确接受：一个值零证及原转置算子

日期：2026-11-15。状态：**下述接受判据、转置公式与来源契约已证明；
对应的新数域身份、转置解或准确零证尚未计算。** 本文不把已有
$518$ 位乘回或短有理候选当成准确坐标，也不等待此方案才消费
已经完成的原点 DAG。

使用 [原 unit-chart 证明](R787-original-unit-chart-exact-expressions-and-CM-value-consumer.md)
及 [原点 DAG 接口](R792-original-source-bound-CM-DAG-beta-interface.md)。
实际 CM run `43773420733` 的
`R787-implicit-CM-point-coordinate-reconstruction-candidates.json.gz`
为 $6302$ 字节，SHA-256
`0be79ee2811881b0cbfe80a5fe71bf5dac0d9fdbeeb0631b69fa8e45596780f1`。
该文件的 $y,y'$ 各十四个标量 RR 都返回了候选，但其
`expanded_coordinates_exactly_certified=false` 原样保持。
以下只定义怎样取得缺失的准确接受证书。

## 1. 只需要一个大的值零证

写候选为 $q,d\in L$，分别拟代表 $y_0,y'_0$。它们的十四坐标
必须按原 $B_{\rm fld}=\lambda b,s=1+2\zeta$ 的顺序解释；任何
数域身份都在同一个准确原 $L$ 中执行。已成输入仍给
$B_0\ne0$、$h_0\ne0$，以及实际原点的 $y_0^2-b\ne0$。

真正的大接受条件只有

$$
A_0-qB_0=0\quad\text{在准确原 }L\text{ 中成立}.
\tag{A.1}
$$

一旦 (A.1) 已有准确证书，便有 $q=y_0$。随后对短候选只做原
十四维数域运算：核 $d\ne0$，定义

$$
\widehat x=\frac{3h_0(q^2-b)}{d},
\tag{A.2}
$$

并准确核

$$
\widehat x^3=q^2-b,
\qquad c(\widehat x)=\zeta^2\widehat x.
\tag{A.3}
$$

由 R792(792.6) 的唯一 $F_b$ 根，(A.3) 给
$\widehat x=x_0$。又 $x_0\ne0$，故 (A.2) 给

$$
d=3h_0(q^2-b)/x_0=3h_0x_0^2=y'_0.
\tag{A.4}
$$

因此不需要第二个 $A_1-qB_1-dB_0$ 大零证，也不需要重算
二十一次 Norm/因式分解。小检验 (A.3) 可以先算作为必要筛选；
即使通过，它在 (A.1) 尚未准确证明前也只给候选的条件性身份。
若它失败，只拒绝该候选对，不影响准确四响应或原点 DAG。
不得以曲线方程、共轭、系数短或有限精度吻合代替 (A.1)。

## 2. 固定原矩阵、负号和选行

沿原 R787 代码及 unit-chart 证明的未逐行清分母矩阵。记

$$
F_A\in\mathbf Q^{2560\times1234},\quad
C\in L^{2560\times1214},\quad F_Aa-Cc=0.
\tag{A.5}
$$

准确 $Z$ 保持原 `Z_pivot_integer_rows` 的负号，$B=Zc$。
原完整关系还保留最后 $129$ 阶身份；本判据使用其中已由原证明
足够确定同一准确解的 $2560$ 行，不改原全局注入来源。
原 $J$ 是 $1234$ 个 A 选行，$R$ 是其余 $1326$ 行；$I$ 是原
Schur 选行 $1186$ 项，$P$ 是原 Schur 选列 $1186$ 项。
令 $f=1186$ 为原 free column，其他 $27$ 个自由值均为零。
写

$$
F_0=F_A[J,:],\quad F_I=F_A[R[I],:],\quad
C_J=C[J,:],\quad C_I=C[R[I],:],
$$

$$
S=C_{I,P}-F_IF_0^{-1}C_{J,P},\qquad
s_f=C_{I,f}-F_IF_0^{-1}C_{J,f}.
\tag{A.6}
$$

那么 $c_P=-S^{-1}s_f$，且

$$
M=\begin{pmatrix}F_0&-C_{J,P}\\F_I&-C_{I,P}\end{pmatrix},
\quad r=\binom{C_{J,f}}{C_{I,f}},
\quad \xi=\binom a{c_P}=M^{-1}r.
\tag{A.7}
$$

这些是原单位 chart，不把 R824 逐阶清分母算子在同一数字行号处
替换进来。若另用清分母行，必须同时准确运输 covector，不能
遗漏左乘逆或转置。

设准确 CM 行为 $e=e_0\in K^{1\times1234}$，
$E=eZ\in K^{1\times1214}$。则

$$
A_0-qB_0=\ell\xi+c_*,\quad
\ell=(e,-qE_P),\quad c_*=-qE_f.
\tag{A.8}
$$

故 (A.1) 等价于原 bordered determinant
$\det\left(\begin{smallmatrix}M&r\\-\ell&c_*\end{smallmatrix}\right)=0$。
这个等价式定义准确目标，不构成已执行的零判。

## 3. 可直接验证的原 row-space 证书

给出一个准确向量 $\lambda\in L^{2560}$，满足

$$
F_A^t\lambda=e^t,\qquad
(C^t\lambda)_P=qE_P^t,\qquad
(C^t\lambda)_f=qE_f.
\tag{A.9}
$$

则将 (A.5) 左乘 $\lambda^t$，使用其他自由坐标为零，得到

$$
0=e a-q(E_Pc_P+E_f)=A_0-qB_0.
$$

因此 (A.9) 是完整准确接受证书。它没有要求重构原 $a,c$，
没有重做原 $518$ 位 Dixon，也不靠一次模秩推测特征零相等。
可以把 $\lambda$ 的支撑固定为 $J\cup R[I]$，只有 $2420$ 项；
也可接受其他真实支撑，只要完整 (A.9) 全部准确乘回。
除 $f$ 外另 $27$ 个自由列不需要为这个指定原方向验零。

在固定 chart 下先求

$$
u_0=F_0^{-t}e^t,\quad
t=S^{-t}(C_{J,P}^tu_0-qE_P^t),\quad
u=u_0+F_0^{-t}F_I^tt.
\tag{A.10}
$$

令 $\lambda_J=u$、$\lambda_{R[I]}=-t$、其余为零。前两个
(A.9) 自动成立；最后的准确标量检验等价于

$$
u^tC_{J,f}-t^tC_{I,f}-qE_f=0.
\tag{A.11}
$$

符号可由 $M^t(u,-t)^t=(e,-qE_P)^t$ 直接核出。
这里 $F_0$ 是有理矩阵，$e\in K=\mathbf Q(s)$，因此可选的
$u_0$ 准确预计算只有两个有理 RHS。它不是现成的有理逆：旧
`A_inverse_mod_prime` 仅是 $F_0^{-1}\bmod\ell$。
准确 $t$ 仍有 $1186$ 个 $L$ 坐标，不能据候选 $q$ 很短就
声称这个 dual witness 必短、快速完成或已经得到。

## 4. 已成十四个模逆怎样只做新的转置 RHS

若实施 transposed Dixon，旧每个分支已经保存：

$$
F_0^{-1}\bmod\ell,\quad S^{-1}\bmod\ell,
\quad C_{J,P}\bmod\ell,
\qquad \ell=1000000753.
\tag{A.12}
$$

这就是原 `A_inverse_mod_prime`、
`Schur_minor_inverse_mod_prime`、`C_J_pivot_columns`。
对任意新转置 RHS $(b_A,b_P)$，在同一分支计算

$$
u_0=F_0^{-t}b_A,\quad
t=S^{-t}(C_{J,P}^tu_0+b_P),\quad
u=u_0+F_0^{-t}F_I^tt.
\tag{A.13}
$$

则 $M^t(u,-t)^t=(b_A,b_P)^t$。所有逆直接读旧完整阶段再转置，
不重新求逆、不重新选 Schur 行列、不扩原前缀。十四分支的
逆评价矩阵仍是原 selection 的已成矩阵。

新提升只能称新的 dual RHS，而不是原 $a,c$ 的续算。对目标
$M^tz=\ell^t$，若当前整数代表在模 $\ell^n$ 下成立，先准确
求正残差 $M^tz-\ell^t$，除 $\ell^n$，再用 (A.13) 解其负值
取得下一位；清分母后同样须保持对应精度和正负号。每个新
dual current 有独立 source/tag，不能冒充原 R787 current。
成功只在准确恢复的 $\lambda$ 完整满足 (A.9) 时宣布。

这是一个可执行的准确证书入口；它没有保证比原 primal 的
有理恢复更快。共享模逆与单值目标是确定的节省，dual 坐标
的高度则仍是实际运行问题。当前不启动这条新计算。

## 5. 准确乘回不必展开整个 C 或 S

以下是 (A.9) 的实际小内存 verifier。令
$T=L[t]/g(t)$，$\deg g=20$，使用原 $1,t,\ldots,t^{19}$ 坐标。
记完整原 $F$ 的 $v$ 系数块为 $F_j\in\mathbf Q^{20\times1234}$，
$0\le j\le128$，并记原

$$
Y(v)=v\,y(v)=\sum_{m=0}^{128}Y_mv^m,
\quad Y_m=-R_m\kappa^{-m-1}/246^3\in T.
\tag{A.14}
$$

这些 $R_m,\kappa$ 均是已成 R781 真实源。原 $C$ 是
$Y(v)\sum_jF_jZc\,v^j$ 的 $v^1,\ldots,v^{128}$、各二十个
$t$ 坐标。令 $\mu(a)$ 表示 $T$ 上乘 $a$ 的原 $20\times20$
矩阵。将 $\lambda$ 按这些 $v^n$ 行分成 $\lambda_n\in L^{20}$，置

$$
w_j=\sum_{n=\max(1,j)}^{128}\mu(Y_{n-j})^t\lambda_n,
\qquad 0\le j\le128.
\tag{A.15}
$$

有限求和交换给准确恒等式

$$
\boxed{C^t\lambda=Z^t\sum_{j=0}^{128}F_j^tw_j.}
\tag{A.16}
$$

这里是原系数坐标的普通转置，不是 Hermitian adjoint，也不是
未经换基的域 trace 配对。$\mu(Y)^t$ 必须用原 $g(t)$ 的
reduction 矩阵；不能把乘 $Y$ 的代码直接当作其转置。
$j=0$ 项可以保留，原 $F_0^{\rm cusp}Z=0$ 自行消掉它。
不得把此 cusp 常数块与 (A.6) 的选行方阵 $F_0$ 混同。

因此准确验证仅生成 $129$ 个二十维 $L$ 向量，再乘原有理
$F$ 和稀疏 $Z$；没有生成 $2560\times1214$ 个 $L$ 数或
准确 Schur 矩阵。$Z^t$ 最后用二十个原稠密行与其原 free
diagonal。第一项 $F_A^t\lambda=e^t$ 同样只读原矩阵行。
整个 verifier 可以按 $j$ 与原列分块原子保存，完整乘回是
准确零证，不依赖随机点或高度猜测。

## 6. 真正的最小来源及状态边界

| 来源 | 必须消费的已成对象 |
|---|---|
| 本次 CM run `43773420733` | 原准确表达式、$e_0$ 与 $e_0Z$、真实 $B_0$ 非零见证、候选文件；不能只读模商 |
| 原 R787 真 $518$ source `4092d1cc4d1156bc24a10ff820fd39c5713e8ad7` | 原 chart/selection/rational-blocks、1234 个真实 $129\times20$ 行；原 manifest `7a22beb22912c1d5c4c56a5faa577a529f6c5dab5bb4ea5251e9cd5c4264ba3f` |
| 同一原 R787 完整十四分支阶段 | (A.12) 的旧逆与 $C_{J,P}$；不在当前小 CM 子集内，须从其原 manifest 指定源实际取回 |
| 原 R781 源闭包 | 准确原字段、$\kappa,R_0,\ldots,R_{128}$ 与原 $t$ reduction；从原已绑 carrier 读取，不重新 Laurent 递推 |
| 原 R791 | 已成 $h_0$ 与共轭方向，只用于 (A.2)–(A.4) 的小准确检查 |

当前最小 DAG carrier 已保 CM 准确值/jet 与 $eZ$，也保短候选。
它没有保原大 $F$ 行或十四个 Schur 逆；后继必须显式补齐这些
真实成员，不能假定它们已经存在，或将一个不可读引用当作已取回。
所有选择均从真实源 manifest 逐文件 bytes/SHA 绑定。

最终应逐项记录：原值零证是否成立、小曲线与共轭检查是否成立、
准确 $x,y,y'$ 是否被接受、以及实际恢复的坐标来源。失败保
具体准确残差或未完成状态。全新的算术只在公开 Actions；源码、
参数、纸证与简明 run/SHA 入 Git，可重算机器向量/回执只在
一日 active artifact/carrier 续传。本文不制造新 run、pins 或
尚未存在的 dual witness。
