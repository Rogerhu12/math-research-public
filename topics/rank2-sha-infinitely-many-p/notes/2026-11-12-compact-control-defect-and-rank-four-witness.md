# Compact Selmer 特化的余核与一个真实秩四检验

日期：2026-11-12。本文核清一个可能误导本题的控制措辞，
并给出完全独立的有限域秩证书。没有从这个问题否定
Castella 的广义 Kato 类非零判据，也没有证明原 E17 的 Sha 有限。

## 1. 原文中的两个不同特化映射

Castella，*Generalised Kato classes on CM elliptic curves of rank 2*，
[arXiv:2204.09608v3](https://arxiv.org/pdf/2204.09608v3)，
[作者稿](https://web.math.ucsb.edu/~castella/Kato-Schoen.pdf)，
§6.2 Proposition 6.2.1（印刷 p.22）把以下两条箭头都列为同构：

\[
\begin{split}
r^*:\operatorname{Sel}_{\varnothing,0}(K,A_{\psi^c})
&\longrightarrow
\operatorname{Sel}_{\varnothing,0}
 (K,A_{\psi^c}\otimes\Psi_S^{1-c})[S],\\
r:\operatorname{Sel}_{0,\varnothing}
 (K,T_\psi\otimes\Psi_S^{c-1})/S
&\longrightarrow\operatorname{Sel}_{0,\varnothing}(K,T_\psi).
\end{split}
\tag{1}
\]

其中 \(\Lambda=\mathcal O[[S]]\)。其 p.23 的两张图及
snake-lemma 论证处理第一条离散箭头；对第二条 compact 箭头
只说同理。可是 §6.3 证明末尾（pp.25–26）实际仅使用第二条
箭头的**注入性**，而不是满射。

这一区别不能删去。第一条同构对偶后给离散 Selmer 对偶模
的 coinvariants；它不把另一个 compact Selmer 模的
coinvariants 自动认成基层 compact Selmer。

以下证明 compact 满射的字面解释过强，并把本题还缺的余核
准确保留下来。引用论文的最终非零判据时，仅使用它真正需要的
注入性和零阶判据。

## 2. 从大模秩一到底层，还差什么

记
\[
M=\operatorname{Sel}_{0,\varnothing}
 (K,T_\psi\otimes\Psi_S^{c-1}),\qquad
M_0=\operatorname{Sel}_{0,\varnothing}(K,T_\psi).
\]
在论文所用的正根数、中央复值为零的情形，§6.3，p.25，
由 Theorem 5.2.1 和各分量分解得到
\[
\operatorname{rank}_\Lambda M=1.
\tag{2}
\]

令 \(R=\Lambda_{(S)}\)、\(k=\operatorname{Frac}(\mathcal O)\)。
这是剩余域为 \(k\)、参数为 \(S\) 的 DVR。
由短正合列
\[
0\longrightarrow\mathbb T\xrightarrow{S}\mathbb T
\longrightarrow T_\psi\longrightarrow0,
\quad \mathbb T=T_\psi\otimes\Psi_S^{c-1},
\]
以及 \(H^0(K,T_\psi)=0\)，大局部化一阶上同调没有
\(S\)-扭子；它的子模 \(M_R\) 也没有。
有限生成性与 (2) 因而给
\[
M_R\simeq R,\qquad
\dim_k((M/SM)\otimes_{\mathcal O}k)=1.
\tag{3}
\]
这里没有假设 \(M\) 在整个二维 \(\Lambda\) 上自由。

论文 Lemma 6.2.2（pp.23–24）的全局对偶论证则给
\[
\dim_k(M_0\otimes k)
=\dim_{\mathbb Q_p}\operatorname{Sel}(\mathbb Q,V_pE)-1
\tag{4}
\]
只要有理点的 \(p\)-进局部化非零。
对任意正秩 \(E(\mathbb Q)\)，这个条件成立：
非扭有理点在 \(E(\mathbb Q_p)\widehat\otimes\mathbb Q_p\)
中不为零，因为 \(p\)-进椭圆对数在有限指数正式群上的核为零，
在整个局部群上的核只有挠点。

对原曲线 E17，设
\(t_p=\operatorname{corank}_{\mathbb Z_p}\Sha(E17/\mathbb Q)[p^\infty]\)。
已证秩二和 Kummer 正合列使 (4) 等于 \(1+t_p\)。
因此，即使已经有 compact 注入，仍准确留下
\[
\boxed{\quad
\dim_k\operatorname{coker}(r\otimes k)=t_p.
\quad}
\tag{5}
\]
特别地，直接把这个箭头称为有理同构，已经额外断言了
本题正在寻求的 \(p\)-初级有限性。

### 2.1 长正合列中的位置

对用实际全局及局部 cochain 构成、并正确交换特化的 Selmer
复形 \(\mathcal C\)，乘 \(S\) 的三角给出
\[
0\longrightarrow H^1(\mathcal C)/S
\longrightarrow H^1(\mathcal C\otimes_R^{\mathbf L}k)
\longrightarrow H^2(\mathcal C)[S]
\longrightarrow0.
\tag{6}
\]
这个式子直接来自上同调长正合列；最后一项是乘 \(S\)
在 \(H^2\) 上的核，不是可以略去的有限误差。
对于严格/全局部条件，复形可写成实际全局限制映射的
mapping fibre；采用其他局部条件时，必须同时检查局部
特化修正，不能只写 (6) 就假定它们消失。

这里 (5) 已由实际 compact 注入、(2) 和基层对偶独立得到，
并不依赖未经证明的额外 Selmer-complex 识别。
(6) 说明任何想用 cochain 补完满射的论证必须支付什么。

一个简单的代数检验是
\[
\mathcal C^1=R\oplus R,\quad\mathcal C^2=R,
\qquad d(x,y)=Sy.
\]
此时 \(H^1(\mathcal C)=R\)、\(H^2(\mathcal C)=R/S\)，
而特化后 \(H^1=k^2\)；大 \(H^1\) 自由秩一并不提供满射。
这只是对形式推理的检验，不冒充原椭圆曲线的 Selmer 复形。

## 3. 字面满射还有一个真实 CM 曲线检验

取
\[
B=635318657=158^4+59^4=134^4+133^4
 =41\cdot113\cdot241\cdot569,
\qquad E_*:y^2=x^3-Bx.
\tag{7}
\]
四个明确有理点为
\[
\begin{split}
R_1&=(-24964,549998),&R_2&=(-3481,-1472876),\\
R_3&=(-17956,2370326),&R_4&=(-17689,2388148).
\end{split}
\tag{8}
\]
它们出现在 Aguirre–Peral，*Sums of biquadrates and elliptic curves*，
Glasnik Matematički **48(68)** (2013), 49–58，§3.1。
本文不用其数值 regulator 或 mwrank 输出作独立性输入，
而给如下完整有限域证书。

对表中每个好素数 \(q\)，令
\(\rho_q(R)=[\#E_*(\mathbb F_q)/3]\overline R\)。
点数准确只有一个因子 \(3\)，所以 \(\rho_q\) 的像落在
阶为三的群中。按给定基点 \(g_q\) 写成 \(\mathbb F_3\) 坐标：

| \(q\) | \(\#E_*(\mathbb F_q)\) | \(g_q\) | \(\rho_q(R_1),\ldots,\rho_q(R_4)\) |
|---:|---:|---|---|
| 11 | 12 | (9,2) | 1, 2, 0, 2 |
| 23 | 24 | (3,11) | 0, 1, 1, 1 |
| 47 | 48 | (8,1) | 1, 2, 0, 0 |
| 59 | 60 | (29,31) | 0, 0, 1, 1 |

此四阶矩阵的行列式模三为 \(2\)。另有
\(\#E_*(\mathbb F_5)=10\)，故 \(E_*(\mathbb Q)[3]=0\)。
若 (8) 满足非零整数关系，去掉系数的最大共同三次幂。
去掉后点和是三次幂挠点，仍必须为零。
至少一个新系数为模三单位，与上述可逆矩阵矛盾。
这证明
\[
\operatorname{rank}E_*(\mathbb Q)\ge4.
\tag{9}
\]

所有点方程、点数和群律由
[精确脚本](../scripts/check-compact-control-rank-four-witness.py)
仅用整数和有限域运算核查；另一个研究者用独立代码得到同一证书。

该曲线有 \(\mathbb Z[i]\)-CM。由 Aguirre–Peral §1.1
的根数公式，互素的 \(m,n\) 且 \(m^4+n^4\) 为奇数时根数为
\(+1\)，所以 \(E_*\) 的根数为正。
正秩及 CM 的 Coates–Wiles 定理给 \(L(E_*,1)=0\)，
因此它在 Castella §6 所用的正偶中央消失情形内。
取 \(p=13\)：精确点数为 \(20\)，故 \(a_{13}=-6\)，
是好普通素数。

对这个实际例子，(3) 的源维数为一；而 (4)、(9) 给
\[
\dim_k(M_0\otimes k)\ge3.
\]
所以在同文的大模秩一结论和标准基层对偶下，
Proposition 6.2.1 的 compact 箭头不能照字面当成同构。
这是源、目标的真实秩不相容；并不假设存在任何无限 Sha。
它也不否定广义 Kato 类的最后判据：该判据本来允许
此曲线的 \(\kappa_p\) 为零。

## 4. 特征理想与 coinvariants 的区别

另一个需要保持的区别出现在 §6.3 式 (6.7) 后。
特征理想记录 \(R\)-长度，而 \(\dim_k X/SX\)
记录 \(S\)-初等因子的个数。两者一般不同。
例如
\[
Z=R/(S^2),\qquad X=R\oplus(R/S)^4
\]
满足
\(\operatorname{char}_R(X_{\rm tors})
=\operatorname{char}_R(Z)^2=(S^4)\)，
但
\[
\dim_k(X/SX)=5\ne1+2\dim_k(Z/SZ)=3.
\tag{10}
\]
因此仅凭式 (6.7) 不能推出后面的完整数值秩等式；
还需更强的初等因子或伪同构输入。
这个代数例子也不是原曲线反例。

论文最终需要的较弱零阶等价则没有这个问题：
对秩一 \(X\) 和扭 \(Z\)，若
\(\operatorname{char}(X_{\rm tors})=
\operatorname{char}(Z)^2\) 乘一个在 \(S=0\) 非零的因子，
则
\[
\dim_k(X/SX)=1
\iff Z_R=0
\iff Z/SZ=0\quad\text{在 }k\text{ 上}.
\tag{11}
\]
用紧模的注入和大类模 \(S\) 的像，(11) 正好保留
\(\kappa_p\ne0\) 与基层最小余秩的比较。
本仓库的 O4 使用这个非零判据，不使用过强的 compact 满射
或未经初等因子证明的数值秩公式。

## 5. 对当前目标的作用

原 E17 已有一个已知非零的严格 MW 向量
\(v_p=\log_p(Q)P-\log_p(P)Q\)。
(3) 只说大 compact 模的特化像是一条线；它没有说明这条线
等于 \(\mathbb Q_pv_p\)，更没有说明实际大 Kato 类在这条线上
的系数不为零。
剩余 \(t_p\) 维方向正是 (5) 不能丢去的余核。

继续 O4 的实际单素数 Heegner 点不可整除性或 O6 的中心核，
不能把原文中这一处过强措辞作为本题完成证明。

## 原始来源

- Castella，以上 v3 的 Proposition 6.2.1、Lemma 6.2.2、
  §6.3 式 (6.5)–(6.8)，印刷 pp.22–26；原文及实际使用的位置均已核。
- Aguirre–Peral（2013），§1.1、§3.1：
  <https://web.math.pmf.unizg.hr/glasnik/48.1/48(1)-04.pdf>。
  曲线来源及根数用其公式；秩下界另由本文有限域证书证明。
- 本仓库 [R8](../results/R8-strict-selmer-comparison.md)、
  [R34](../results/R34-strict-selmer-and-odd-central-classgroup-rank.md)：
  通常/严格 Selmer 与 Tate–Sha 的准确基层关系。
