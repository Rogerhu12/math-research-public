# 首次新输入：W/b0/cross0 的三个完整常数域与同 f 原五式返回

- 会话：Astra-ISP-8542378f-20261127。
- 日期：2026-11-28（Asia/Taipei）。
- 状态：未执行；不预报三域 gcd、矩阵秩、原正目标或交叉头零排空。
- 建议源名：2026-11-28-unit211-W-b0-cross-zero-three-entire-QQ-fields-original-return-8542.py。
- 唯一首次预算：180 秒、4 GiB；外层可为 195 秒。
- 源 SHA256：b5e9d1e1c19e15041f039f808b8cb65e26bd48cc4374ed84e6081f3b7afeb31c；21236 字节。
- 只有一个固定已刊小源码依赖，边界在第 2 节。没有参数缓存或大输出依赖。

## 1. 确切新范围与三个小参数

只接当前正确 W、distinct-singleton、物理 $D\ne0$ 的 $b_0=0$ **且交叉头零**分支。沿已刊原均值记号

$$
q_f=f^2+q_1f+q_0,\qquad
r_i=A_i(\lambda)+(B_{i0}+\lambda B_{i1})f.
$$

旧纯权行 $v$ 给 $vB_0=1,vB_1=0$，所以

$$
(B_0\times B_1)=(B_{11},B_{21},B_{31})
$$

是理想等式。三条 $B_{i1}=0$ 只在此分支施加，不外推到整个 b0。

唯一旧实际 run 46143877410/job 140975574446 已返

$$
G(u)=\sum_iw_iB_{i1}
=\frac{(4u+5)(6u-1)(20u^3-4u^2-20u+9)}{480},
\tag{1}
$$

三个因子都 QQ 不可约且重数一。因此本次只用三个**完整**常数域

$$
K_1=\mathbb Q[u]/(4u+5),\quad
K_2=\mathbb Q[u]/(6u-1),\quad
K_3=\mathbb Q[u]/(20u^3-4u^2-20u+9).
\tag{2}
$$

不是选取三个复根；$K_3$ 包含全部三个嵌入。其原规范哈希依次为

- 9b702a5320030eb66ea9572167b2589cb503a6035fd67b350256e6248dcbe9ec；
- c708effec8346a565d2ecf2264cb6635e4adeffe15c1ec12f222a57378d441ed；
- bf8d54f313b63c7f42b5f24b2bfc31e789f1c65ca2b4c5fd5bf3b8be236675b2。

源只检查三个小数学参数的规范表示与它们的小整数乘积；首一乘积 SHA 必须等于原 G5 的 9f9544b1500bc385df9f8a04d4693c3895655712721661a109854be0845ea8d2。这不是旧投影、旧 gcd 或旧 QQ 因式重算。

对应原证明为[三头五次覆盖与 G 补图的精确 I4](../results/R150-appendix-unit211-W-b0-cross-zero-five-weight-cover-and-G-open-exact-I4.md)。若三个新原域都实际返回物理单位，(1) 的原理想来源及三个互素简单因子才允许合成整个 cross0 关闭；任一未返回分量都继续保留。

## 2. 唯一依赖与只再生必要定义

依赖：

- 2026-11-28-unit211-W-b0-entire-cross-zero-three-original-lambda-f-heads-8542.py；
- Git blob 681d0a0b3d76b30cf572c3e28d2b296cc704f73c；
- SHA256 1e41e505bf925b8f5e4422c60267efc9e0db6cc5f311daef9524efa9f44f372f。

核完整 SHA 后，只执行从首个 ctx 定义到 def source_return 之前的 **10695 字节**；其 SHA256 为

$$
\texttt{ceecdcd9fcc81892ea2ad0c2918423ae283d1afbe63a2198583189e2b1e4ebeb}.
$$

该段只生成真正的原 Gram、四均值/N1、首一 qf、三个 ri 与 B0/B1 的必要系数及 b0 代入。它在旧三头归一、所有 nu-Sylvester、原 cover-gcd、因式分解之前结束。它没有 timer、资源、文件或 import 动作；旧 say 静音。

本次从头到尾只有外层一次 real-time 180 秒计时、4 GiB 硬界。没有再次生成 C2/Loww、旧四乘五矩阵、六投影、PRS 或已冻结的其它正目标。

所有原系数继续只用既有 W 权单位；nu+2 仅因 b0 的已付 Astar=uQ(nu+2) 可用。完整原 $E_1$ 独立保留，true dual 平方没有错误 compact 替代。

## 3. 先在整 K[nu] 中专门化，再求三原头

对每个 (2)，全部原多项式先将 u 映到完整常数域。$K$ 的每一个实际非零逆均由 $\mathbb Q[u]$ 扩展 gcd 生成，并双向乘回为 1。没有假设数值近似域或选复嵌入。

记专门化后的原头为

$$
B_{i1}=n_i(\nu)/d_i(\nu).
$$

$d_i$ 只由原已付权支持组成。先检查每个旧付费原多项式是否在整个 K[nu] 上恒零；只有真恒零时，原单位本身已排除此整个 u 域。

随后按固定次序对三条 $n_i$ 在 $K[\nu]$ 做完整扩展 gcd，保全部首项降次。每步返回

$$
h(\nu)=\sum_i s_i(\nu)n_i(\nu)
      =\sum_i s_i(\nu)d_i(\nu)B_{i1}.
\tag{3}
$$

最后再以三个真实分母的共同乘积完整清分母回乘。若三头都恒零，不构造虚假的有限 nu 代数，直接保留该整个 nu 线并准确结束此域。

这与旧 $\mathbb Q[u,\nu]$ 三个投影不同：输入是三个新的完整常数域，目标是同一 nu 的原三头返回；原全部头退化在专门化之后实取，不能沿用泛型 nu 次数。

## 4. 只删除原已付的整个 primary 分量

设 $a(\nu)$ 为某个原已付权支持。对 $h$ 反复取真正

$$
g=\gcd(h,a),\qquad h=g\,h_{\rm new}.
$$

只从 h 删除这些 g。每步都返回两个整除乘回，直到剩余 good 与所有旧付费支持互素。反复操作保证若 h 含某因子的高重数，而 a 只含一次，该不允许的整个 primary 分量仍被全部删去；其他 nu 重数完整保留。

源同时保存一个具体的纯权逆见证。若 pa=g·qa，则

$$
g^{-1}=qa/pa
$$

只用旧原单位 pa。累计记 h=removed·good 和 removed·invnum=invden，全多项式乘回；invden 是实际旧付费多项式的乘积。

如果 good 是非零常数，(3) 与这个见证给出某个实际旧付费乘积 U 的完整三原头组合，即

$$
U=\sum_i\Omega_i B_{i1}.
\tag{4}
$$

源在 K[nu] 中完整清分母乘回。只有 (4) 真成立才关闭整个 u 域，不仅凭 gcd 支持或秩判断空。

若 good 非常数，则保整个

$$
A=K[\nu]/(\mathrm{good}).
\tag{5}
$$

它可以可约、非约化；不挑 nu 根或剩余域。所有后续原权分母均在整个 A 内以真实扩展 gcd 求逆并回乘为 1。新几何量、D、lambda 头、范数及行列式都不倒置。

## 5. 整个 A 中的新同 f 消去，回到五条完整原式

在 (5) 中，三条 B_i1 实际返回为零。利用已刊 B0 的原单位组合存在性，本源再在整个 A 中真正求出

$$
\sum_i v_iB_{i0}=1.
\tag{6}
$$

执行方法是对 good 与三个 B_i0 的整 A 代表作扩展 gcd，保 good 的原组合，并返回 (6)；没有选择单个 B_i0 作单位。

令

$$
g_\lambda=\sum_i v_i A_i(\lambda),\qquad R=f+g_\lambda.
$$

于是同一点的完整原来源是

$$
R=\sum_i v_i r_i=\sum_{j=1}^{4}\kappa_jF_j,
\qquad
(F_1,F_2,F_3,F_4)=(E_1,E_{B,e},E_{B,o},N_1).
\tag{7}
$$

源在普通 A[lambda,f] 中逐系数返回 (7)。$g_\lambda$ 的 lambda 次数至多二。

另加本 b0 物理图的原 q2，令 $F_5=q_2$。它来自已刊

$$
C_4=mD\ell q_2,
$$

所以仅在本文原物理 D≠0 范围施加 q2。源码直接使用原 ad 定义 q2=2ad/ell，保持所有 lambda 头零。若 q2=a2 lambda²+a1 lambda+a0，还在整个 A 中返回

$$
a_2+3a_1+4a_0=-32uQ\delta\ell\kappa^2,
\tag{8}
$$

右边是真原权单位。没有单独反演 a2。

每个完整原 Fi 对 f 次数至多二，设

$$
F_i=F_{i0}(\lambda)+F_{i1}(\lambda)f+F_{i2}(\lambda)f^2.
$$

以同一个 $g_\lambda$ 定义

$$
\begin{aligned}
U_i&=F_{i0}-F_{i1}g_\lambda+F_{i2}g_\lambda^2,\\
Q_i&=F_{i1}+F_{i2}(f-g_\lambda).
\end{aligned}
$$

源完整返回

$$
F_i=U_i+Q_iR.
\tag{9}
$$

全部 U_i 是 lambda 次数至多四的原多项式；它们没有被取数值或只取某个约化点。q2 的次数仍至多二。

## 6. 新固定 lambda≤6 普通容器与真正正目标

本源只使用普通多项式容器

$$
A[\lambda]_{\le6},
$$

它作为 QQ 向量空间有 $7\dim_{\mathbb Q}A$ 个固定坐标。它**不是** lambda 商代数，不称原方程商自由或据此给商维数。

对每个非零 Ui，只取

$$
\lambda^j U_i\quad(0\le j\le6-\deg U_i)
$$

及其全部 A 基倍作为实际原列。A 的基为所有 nu 幂和完整 K 的 u 幂；全部 nu 重数及常数域嵌入都在同一矩阵内。

Gaussian 仅选择实际原列。选定方阵逆须双向回乘为 I，并返回所有原矩阵列。随后固定按顺序尝试

$$
1,\qquad D,\qquad D^2,\qquad D^3.
\tag{10}
$$

它们都在这个普通容器中；D 对 lambda 至多二。矩阵秩本身不作为空性或有限商维数结论。

只有某个目标真的满足全部容器坐标，才组装实际多项式

$$
T=\sum_i\omega_i(\lambda)U_i.
$$

再由 (7)、(9) 得

$$
T
=\sum_i\left\{\omega_i-
       \left(\sum_j\omega_jQ_j\right)\kappa_i\right\}F_i,
\qquad \kappa_5=0.
\tag{11}
$$

源在**完整普通 A[lambda,f]** 中重新返回 (11)，不限于原矩阵的七个 lambda 坐标。原 A 的所有降幂都有实际商乘回，good 来自 (3) 与旧权单位；故此式确属于三个常数域上的原 cross0、五原式局部化理想。

若目标为 D 的正幂，关闭只使用当前真实 D≠0 范围；代码不倒 D。若四个目标都未返回，保整个 A 与全部原条件，不增容器、换顺序或重跑同门。

## 7. 完整覆盖和执行边界

若三个整个域各由 (4) 或 (11) 完整关闭，才合成“整个当前 W/b0 的交叉头零支关闭”。这仍然不代表 b0 或整个 W 已关闭。

如果只完成部分域，逐域记录实际返回、原始 nu gcd、已付 primary 删除、剩余完整 good、每个矩阵/目标的准确结果；没有系数域转换或资源失败被标成数学排空。

只输出定义/次数/项数/字节/SHA、小统计与实际状态，不写矩阵、原乘子、系数数组、编码分片或可重算大缓存。三个小参数作为本次数学输入直接写在源中，不读取或重造旧 G5 投影数据。
