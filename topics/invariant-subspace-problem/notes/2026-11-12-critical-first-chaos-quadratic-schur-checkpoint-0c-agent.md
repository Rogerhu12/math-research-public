# 临界第一 chaos：平方尾有界除法的全 H 排核检查点

日期：2026-11-12（UTC）。critical_kernel 独占后续；不修改已冻结 R95。此稿先保存新闭合的二次 Schur 机制，随后转根代理分配的 R101。

**已证明结论。** 对 R95 的临界一阶乘子 S=∑a_jY_j，令 k=min{j:a_j≠0}。如果

$$
\mathfrak Q=
\sum_{i>k}\frac{|a_i|}{\alpha_i}
\sum_{j\ge i}|a_j|<\infty,
\tag{1}
$$

则 S 在原 Haar 表示的整个 H 上单射且值域稠密，相应 f=-2S1 对 A 循环。允许任意复相位。

特别地，只要对某个 θ>1/2 有 |a_j|≤Cα_j^θ，条件成立。它覆盖 R95 中不可由 A 有界除法的交替例 a_j=(-1)^jα_j，因此“不可有界除法”不妨碍这类向量的实际循环性。

## 1. 实际模型与平方尾的有界除法

沿用 R95：

$$
Y_j=N_j(I+N_j)^{-1},\quad
N_j^2=\eta_jN_{j+1},\quad
\eta_j=\alpha_{j+1}/\alpha_j,\quad
\|(I+N_j)^{-1}\|<3.
$$

固定首位 k，记

$$
a=a_k\ne0,\qquad
T=N_{k+1},\qquad
B=\sum_{j>k}a_jY_j.
$$

对 k<i≤j，记

$$
P_i=\prod_{\ell=k+1}^{i-1}N_\ell.
$$

归一化幂恒等式给

$$
TP_i=\frac{\alpha_i}{\alpha_{k+1}}N_i.
$$

因此定义实际有界算子

$$
C_{ij}=
\frac{\alpha_{k+1}}{\alpha_i}
P_i(I+N_i)^{-1}Y_j
\quad(i\le j)
$$

时，有 TC_{ij}=Y_iY_j，且

$$
\|C_{ij}\|\le
\frac{9\alpha_{k+1}}{\alpha_i}.
\tag{2}
$$

i>j 时交换两指标。所有这些算子都属于尾解析范数代数，因为它们是 N_{k+1} 的多项式/有理函数的范数极限。

由 (1) 和 (2)，双级数

$$
C=\sum_{i,j>k}a_i a_j C_{ij}
$$

按算子范数绝对收敛，并且

$$
B^2=TC,\qquad
\|C\|\le18\alpha_{k+1}\mathfrak Q.
\tag{3}
$$

每个 C_{ij} 的形式最低次数在尾变量 N_{k+1} 中为正，因为 Y_iY_j 的最低次数至少为二，除去一个 T 后仍为正。因此 c₀(C)=0。这里的商由 (2)–(3) 实际构造，没有由形式次数自动推有界性。

## 2. 首位精确 Schur 消元

所有 N_j、j≥k 都不作用于低于 k 的位。忽略这个恒等因子，并在第 k 位的物理基 (0,1) 下写

$$
N_k=
\begin{pmatrix}
0&\eta_kT\\
I&0
\end{pmatrix}.
$$

令 η=η_k，D=I-ηT。D 在尾解析代数中可逆，且

$$
Y_k=
D^{-1}
\begin{pmatrix}
-\eta T&\eta T\\
I&-\eta T
\end{pmatrix}.
$$

因此 S=aY_k+I_2⊗B 满足

$$
(I_2\otimes D)S=
\begin{pmatrix}
Z&a\eta T\\
aI&Z
\end{pmatrix},
\qquad
Z=BD-a\eta T.
\tag{4}
$$

由 (3)，

$$
Z^2=T C',
\qquad
C'=CD^2-2a\eta BD+a^2\eta^2T.
\tag{5}
$$

C' 属于尾解析代数，且 c₀(C')=0。

若 S(x,y)=0，(4) 的第二行给 x=-Zy/a。代入第一行，

$$
T(C'-a^2\eta I)y=0.
\tag{6}
$$

T 单射，且 C'-a²ηI 的常数特征为 -a²η≠0，故后者在尾解析代数中可逆。因此 y=0，继而 x=0。

S∈𝓐 为 C 对称，故 S 单射等价于 S 的值域稠密。最后 f=-2S1 及常向量循环性给 f 循环。整个推导发生在原 Haar 表示中，不把单边链表示的核转回来。

## 3. 系数类

若 |a_j|≤Mα_j^θ，θ>1/2，则实际权的超快衰减给

$$
\sum_{j\ge i}\alpha_j^\theta\le C_\theta\alpha_i^\theta.
$$

于是

$$
\mathfrak Q
\le M^2C_\theta
\sum_{i>k}\alpha_i^{2\theta-1}<\infty.
$$

无需 a_i/α_i 的差分平方可和。例如 a_j=(-1)^jα_j 时，R95 已证明 S 不可由任何有界算子除以 A；本稿仍证明 S 单射稠密，f 循环。这两个结论相容。

更一般地，(1) 可以按实际尾和直接检查，无需固定渐近主项、固定相位或单调性。

## 4. 更高头块的候选推广，尚待完整写证

存在一个有力的有限头行列式推广方向。把 k 之后的 n=2^r 个头状态保留为真实 companion 块，清除有限个 I+N_j 分母。若头内首项在局部变量中为一次且系数非零，矩阵行列式在尾变量 T=0 时恰为 B^n；其 T 一次项在 B=0 时非零。因此形式上

$$
\det M(T,B)=B^n+T\,G(T,B),\qquad G(0,0)\ne0.
$$

若能实际构造 B^n=TC、c₀(C)=0，行列式将是 T 乘以可逆元，从而给全 H 单射。按最小尾指标除法，以下绝对收敛条件应足够：

$$
\sum_{i\ge m}
\frac{|a_i|}{\alpha_i}
\left(\sum_{j\ge i}|a_j|\right)^{n-1}<\infty.
$$

对于 |a_j|≤Cα_j^θ，选择 nθ>1 即可，因而有望覆盖任意 θ>0。此段目前只保存下一推导目标；尚未给出完整的有限头分母与行列式最低项证明，不能把它登记为已证定理。
