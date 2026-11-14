# R360 — 原三挠局部缩放、完整截断 Jacobian 与两 Faber 行的准确对应

日期：2026-11-13。**状态：以下真实底部族的缩放方程、完整 tail Jacobian、
其单位 beta-Hankel 行列式，以及原两个 Faber 观察的指定线性/二次
转置均已证明。矩阵可逆并不单独证明两个指定观察非零；主目标未完成。**

本结果接 [R354](R354-original-hirota-bottom-unit-recursion-and-complete-truncation.md)、
[R355](R355-actual-hirota-isogeny-and-reduced-truncation-ideal.md)。
这里实际支付的是同一个原核的 Jacobian 与旧观察之间的坐标变换，
并保留在三挠点和原点出现的两种不同椭圆对数核。

## 1. 原参数与完整 tail 导数

保持 $p=6s+1>7$、$E_b:y^2=x^3+b$、$b=17$，以及
$$
t_*=-H^3\epsilon_3/24,\qquad
R(U;t)=\sum_{n\ge0}r_n(t)U^n,\quad r_0=1,\quad r_1=t.
$$
这里 $r_n$ 是 R354 的实际 Hirota 递推，$U=X/b=x^3/b$。
其前 $2s$ 项的全部分母在 $p$ 处为单位。
在真实参数上
$$R_*(U)=\sum_{n=0}^{s}r_n(t_*)U^n,\qquad r_s(t_*)\ne0.$$
以下记 $r_j=r_j(t_*)$，定义完整 tail Jacobian 向量
$$
\boxed{\mathfrak j_i=r_{s+1+i}'(t_*),\qquad 0\le i\le s-1.}
\tag{1}
$$
此处撇号是参数 $t$ 的导数，不是曲线导子。它的非零性在 R355
由原 $\mu_3$ 核刚性证明；下文给出整个向量的直接公式。

## 2. 原三挠点的局部缩放，包含真实椭圆对数

取原 $Q=(0,\beta)$、$\beta^2=b$，并令 $w(Q)=0$、$dw=dx/(2y)$。
其实际局部对数是
$$
w=\frac{x}{2\beta}h_Q(U),\qquad
h_Q(U)=\sum_{n\ge0}
\frac{(-1)^n(1/2)_n}{n!(3n+1)}U^n.
\tag{2}
$$
定义
$$K_Q(U)=\sqrt{1+U}\,h_Q(U)=\sum_{n\ge0}k_nU^n.\tag{3}$$
这不是原点处 R336 的 $h$；两种核的分母分别为 $3n+1$ 和 $6n+1$，
后文始终区分。

先在特征零正式级数中使用原 Hirota。作为 $w$ 的函数，底部族有
$$R(0;t)=1,\quad \partial_wR(0;t)=\partial_w^2R(0;t)=0,\quad
\partial_w^3R(0;t)=48\beta t.$$
四阶 Hirota 在 $R(0)=1$ 处唯一确定全部局部级数，而该微分方程
在 $w$ 缩放下齐次。因此改变 $t$ 等于将 $w$ 乘三次根尺度，准确给
$$3t\,\partial_tR=w\,\partial_wR.$$
再由 (2) 的真实换元算出
$w\partial_w=3U K_Q(U)\partial_U$，得到
$$
\boxed{t\,\partial_tR=U K_Q(U)\partial_UR.}
\tag{4}
$$
这个式子先在特征零形式族中证明，不是把实际全局同源自由地连续
改变为任意参数同源。

约化范围也须核准。(2) 的首个可能 $p$ 分母在 $x^p$；而
$\partial_wR$ 从 $x^2$ 开始，所以 (4) 中它首能影响的是
$x^{p+2}=U^{2s+1}$。因此直到 $U^{2s}$，(4) 的全部系数都整，
可直接约化并与 R354 的唯一递推比较。没有漏掉这个范围以外的
第一次共振，也没有删去 R349 在原点出现的临界 carry。

## 3. 完整 Jacobian 的显式矩阵

由 (2)，
$$h_Q+3Uh_Q'=(1+U)^{-1/2}.$$
故 (3) 满足
$$
6U(1+U)K_Q'+(2-U)K_Q=2(1+U).
$$
于是
$$k_0=1,\quad k_1=3/8,\quad
(6n+2)k_n=-(6n-7)k_{n-1}\quad(n\ge2),$$
即
$$
\boxed{
k_m=\frac38(-1)^{m-1}\frac{(5/6)_{m-1}}{(7/3)_{m-1}}
\qquad(m\ge1).
}
\tag{5}
$$
在所需 $1\le m\le2s-1$ 中，所有分母为单位。下一项才可能有
$6(2s)+2=2p$ 的分母。

在 (4) 上取 $U^{s+1+i}$，代入真实 degree-$s$ 截断，得到
$$
\boxed{
t_*\mathfrak j_i=\sum_{j=1}^{s}
j\,r_j\,k_{s+1+i-j},\qquad 0\le i\le s-1.
}
\tag{6}
$$
这条式子保留了全部 $s$ 个 tail 导数，而不是只读一个非零模数。

设
$$
a=5/6,\quad c=7/3,\qquad
M_{ih}=\frac{(a)_{i+h}}{(c)_{i+h}}\quad(0\le i,h\le s-1),
$$
$$
z_i=\frac{8t_*}{3}(-1)^i\mathfrak j_i,\qquad
q_h=(-1)^h(s-h)r_{s-h}.
\tag{7}
$$
那么 (6) 准确就是
$$\boxed{\boldsymbol z=M\boldsymbol q.}\tag{8}$$
所有反序、整数权和符号已在 (7) 中明确保留。

## 4. Hankel 行列式与结构化逆，不构造大稠密矩阵

完整行列式是
$$
\boxed{
\det M=
\prod_{n=0}^{s-1}
\frac{n!(5/6)_n(3/2)_n}{(7/3)_{s+n-1}}.
}
\tag{9}
$$
它对全部当前普通 $p>7$ 都是单位。
事实上分子中的 $5+6j$ 最高为 $p-8$，$3+2j$ 最高为 $2s-1$；
分母中的 $7+3j$ 最高为 $p-3$；阶乘也远低于 $p$。
因此每个实际因子都非零模 $p$。

这里可用一个自包含的有理数证明支付 (9)。
在实区间 $0<x<1$ 上取归一 beta 权
$x^{a-1}(1-x)^{c-a-1}/B(a,c-a)$。其第 $m$ 个矩恰为
$(a)_m/(c)_m$。对 $n\ge0$，monic 正交多项式为
$$
\pi_n(x)=
\frac{(-1)^n(a)_n}{(c+n-1)_n}
\sum_{k=0}^{n}
\frac{(-n)_k(c+n-1)_k}{(a)_k k!}x^k.
\tag{10}
$$
Rodrigues 式把“权乘 $\pi_n$”写为
$x^{a+n-1}(1-x)^{c-a+n-1}$ 的 $n$ 次导数，除以
$(-1)^n(c+n-1)_n$。分部积分 $n$ 次证明它与所有较低次数多项式
正交；各边界项因 $a,c-a>0$ 消失。其 monic 平方范数为
$$
h_n=\frac{n!(a)_n(c-a)_n}{(c)_{2n}(c+n-1)_n}.
\tag{11}
$$
Gram 行列式是 $\prod_{n=0}^{s-1}h_n$，约分恰给 (9)。
所有数都是有理数，所以该证明随后可在已核定的单位分母范围内
约化，不依赖有限样本推断。

同时，若 $\pi_{n,h}$ 为 (10) 的 $x^h$ 系数，则真实结构化逆是
$$
\boxed{
(M^{-1})_{hr}=
\sum_{n=\max(h,r)}^{s-1}
\frac{\pi_{n,h}\pi_{n,r}}{h_n}.
}
\tag{12}
$$
所有范数及系数分母也为单位。后续可只保存 (10)–(12) 的一维递推
和必要行，不需要生成或提交一个大稠密矩阵。

由 (8) 反解给
$$
\boxed{
r_j=\frac{(-1)^{s-j}}{j}(M^{-1}\boldsymbol z)_{s-j}.
}
\tag{13}
$$
因此整个真实 kernel 系数由完整 Jacobian 向量准确恢复。
特别 (9) 也独立证明该向量不可能全零，因为 $r_s$ 是单位。

## 5. 原 Faber 变换的实际 Lagrange 核

为了把 (13) 接回原两个观察，不能用一个未经支付的环境投影。
R354 的归一 Faber 基 $\mathfrak F_i(U)$ 是 $b=1$ 的同一原基。
其对应原点处的椭圆对数为
$$
z=u\,h_O(T),\qquad T=-u^6,\qquad
h_O(T)=\sum_{m\ge0}\frac{(1/2)_m}{m!(6m+1)}T^m.
\tag{14}
$$
由原不变微分 $dz=(1+u^6)^{-1/2}du$ 作留数换元，得到完整系数
$$
\boxed{
L_{i,n}:=[z^{-6i}]x(z)^{3n}
=(-1)^{n-i}[T^{n-i}]
h_O(T)^{6i-1}(1-T)^{-1/2},
\qquad 1\le i\le n\le s.
}
\tag{15}
$$
这里是实际单 principal 项 Faber 基的坐标；因此
$$
\boxed{\beta_i=\sum_{n=i}^{s}L_{i,n}r_n.}
\tag{16}
$$
所有 Lagrange 因子都保留，$L_{i,i}=1$。
最大所读次数 $n-i\le s-1$，仍严格低于原点的第一 $p$ 分母。
例如 $L_{1,2}=-6/7$，与
$\mathfrak F_2=U^2+6U/7+4/77$ 完全一致。

## 6. 两指定旧行的完整 Jacobian 转置

结合 (7)、(13)、(16)，定义准确的实际行
$$
\boxed{
w_{i,r}=\frac83(-1)^r
\sum_{h=0}^{s-i}
\frac{(-1)^h}{s-h}L_{i,s-h}(M^{-1})_{hr},
\qquad 0\le r\le s-1.
}
\tag{17}
$$
其全部分母为单位，并且
$$
\boxed{\beta_i=t_*\sum_{r=0}^{s-1}w_{i,r}\mathfrak j_r.}
\tag{18}
$$
(10)–(12)、(15)、(17) 给出这些行的完整有限展开；不是仅凭
维数或矩阵可逆性把一个泛函认作另一个。

设 $W_i=\sum_rw_{i,r}\mathfrak j_r$，并继续使用 R343 的原权
$q_{ik}=-18(i-k)^2-3(s+1)$。
那么 R354 的两指定行准确为
$$
\boxed{
\mathcal L=\frac{b^{s-1}t_*}{r_s}W_1,\qquad
\mathcal Q=\frac{b^{s-1}t_*^2}{r_s^2}
\sum_{i+k=s+1}q_{ik}W_iW_k.
}
\tag{19}
$$
这就是 R355 的实际 Jacobian 与原 $\alpha_1,\mathcal Q$ 的完整
线性/二次比较，保留所有 $b,t_*,r_s$ 单位尺度。

新三次行也可以同样写成
$$
\mathcal K=\frac{486b^st_*^3}{r_s^3}
\sum_{i+j+k=2s}ijk\,W_iW_jW_k
=-\eta-\frac92H.
\tag{20}
$$
右端仍是 R349 保留全部临界 carry 后的值，没有重新丢掉
$p t_0=-H$ 或 $y^p$ 的修正。

需要准确区分目前的非零输入：由 monicity 已知是单位的
Jacobian 组合是
$$t_*W_s=\beta_s=r_s.$$
它不是 (19) 的 $W_1$，也不是其中的二次组合。
因此 (8) 可逆、(9) 是单位，以及 (20) 非零，都不能单独宣布
两指定行至少一条非零。接下来的实际问题是在完整原 norm-three
关系下控制 (19) 这两个明确的组合。

## 7. 仅用既有 p13 纤维核所有尺度

复用原 $p=13,b=17$，有 $s=2,t_*=4,r_1=4,r_2=6$。
(5) 给 $k_1=2,k_2=3,k_3=12$，故
$$\boldsymbol{\mathfrak j}=(9,8),\qquad
M=\begin{pmatrix}1&5\\5&6\end{pmatrix},\quad
M^{-1}=\begin{pmatrix}12&3\\3&2\end{pmatrix}.$$
(7) 的向量为 $\boldsymbol z=(5,10)$、$\boldsymbol q=(12,9)$，
逐项满足 (8)。原 Faber 行得到
$$
\beta_1=r_1-\frac67r_2=10,\qquad \beta_2=6,\qquad Q_\beta=10.
$$
恢复原尺度后
$$\alpha_1=11,\qquad \mathcal Q=4,\qquad \mathcal K=3,$$
与 R336、R343、R349 的同一个核完全相合。
这些有限值仅核符号与尺度；全素数证明在 §§2–6，不含新素数扫描。

本文经 GitHub Contents API 提交小文本；没有把它称为本地 git pull。
