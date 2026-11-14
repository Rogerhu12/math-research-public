# R281：极强新增位传输及全出生首边与全高度的统一常数等价

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit。

**状态：已证明的有限 Boolean 传输定理。** 本文没有证明一般相邻常数有限，也没有证明常数一。它说明：若能对任意位数、任意正权及任意出生统一支付首边，则同一个常数已经支付全部相邻高度。相反，任何更高边的实际严格违反都能用有限个足够强的新增位转成首边的实际严格违反。因此在这些完整量词下，首边不是严格较弱的统一常数问题。

只讨论真正的 primitive Gram；不对原 graph 首物理头作任何替换。使用 [R275 的完整一位最小逆定理](R275-one-bit-full-primitive-schur-recursion-and-innovation.md)，包括其顶硬端。

## 1. 全部定义与一位低分支的准确极限

取旧 $M$ 位正权行 $d=\sum_{i=1}^{M}b_iE_i$，选择新出生 $s\ge1$，使新高度
$$
h=M+1-2s\ge2.
$$
旧上、下 primitive 空间分别是
$$
K=\ker d\cap\mathcal H_s,\qquad
L=\ker d\cap\mathcal H_{s-1}.
$$
旧上高度为 $h-1$，旧下高度为 $h+1$。记其实际归一最小逆 Gram 为 $G_j$、$L_j$，所以 $G_0=I_K,L_0=I_L$。所有最小逆始终先在完整物理层取，再把源限制到对应 primitive 空间。

添加权 $a>0$ 的一位，令 $t=a^2$、$R=d_s^\dagger|_L$。全部新 primitive 源由同一个可逆映射
$$
E_a(x,y)=(x-aRy,y),\qquad (x,y)\in K\oplus L
$$
表示。新 Gram 在该源中的同余为
$$
H_j(a)=E_a^*\Gamma_j^{\rm new}(a)E_a.
$$
R275 给全部 $0\le j\le h$ 的完整恒等式
$$
H_j(a)=
\begin{pmatrix}
P_j&-aP_jQ_j\\
-aQ_j^*P_j&L_j+tL_{j+1}+tQ_j^*P_jQ_j
\end{pmatrix},
\tag{1.1}
$$
其中
$$
P_0=I_K,\quad Q_0=0,
$$
$$
P_j=(G_j^{-1}+tG_{j-1}^{-1})^{-1}\quad(1\le j<h),
\qquad P_h=t^{-1}G_{h-1}.
\tag{1.2}
$$
$Q_j:L\to K$ 只依赖旧行、出生和高度，完全不依赖 $a$。

为明确此处所用的 $Q_j$ 确实固定，可按 R275 的原定义取
$$
F_j=\frac{d^j(d^*)^j}{(j!)^2}\bigg|_{\mathcal H_s},\qquad
T_j=G_j^{-1}P_KF_j^{-1}R\quad(0\le j<h),
$$
及 $Q_j=(j+1)T_j-jT_{j-1}$（$1\le j\le h$）。最高项令
$$
A_h=d^h/h!,\qquad
U=I-A_h(d_sA_h)^{-1}d_s,\qquad T_h=UR.
$$
这里 $d_sA_h$ 是旧合法中间阶梯的可逆方阵，$U$ 是沿 $\operatorname{Ran}A_h$ 到 $K$ 的实际斜投影。这保留了旧 $F_h$ 奇异的最高层，未作形式求逆。

对 $j\ge1$，(1.2) 直接给
$$
0\prec P_j\preceq t^{-1}G_{j-1},
\tag{1.3}
$$
最高层是等号。于是 (1.1) 的旧下源压缩满足准确极限
$$
\boxed{
\frac1t(H_j(a))_{LL}\longrightarrow L_{j+1}
\quad(a\to\infty),\qquad0\le j\le h.
}
\tag{1.4}
$$
这在有限维算子范数中成立。具体误差为
$$
\mathcal E_j(t):=\frac1t(H_j(a))_{LL}-L_{j+1}
=\frac{L_j}{t}+Q_j^*P_jQ_j.
$$
令
$$
W_0=I_L,\qquad
W_j=L_j+Q_j^*G_{j-1}Q_j\quad(1\le j\le h),
$$
则包括 $j=0$ 在内有
$$
\boxed{0\preceq\mathcal E_j(t)\preceq t^{-1}W_j.}
\tag{1.5}
$$
这里没有对趋于奇异的完整 $H_j(a)$ 直接取逆极限。$E_a$ 一般不是酉映射，准确源 Gram 是 $H_0=\operatorname{diag}(I,I+tL_1)$，没有替换成单位矩阵；下文使用同一源的完整正块同余，所以不引入 $E_a$ 的条件数。

## 2. 同一个相邻常数严格向旧下一高度传输

**定理 2.1。** 固定上述旧行及 $1\le n<h$。若某个有限 $C\ge0$ 满足：对每个 $a>0$，新增一位后的实际第 $n$ 边均有
$$
\Gamma_n^{\rm new}(a)
(\Gamma_{n+1}^{\rm new}(a))^{-1}
\Gamma_n^{\rm new}(a)
\preceq C\Gamma_{n-1}^{\rm new}(a),
\tag{2.1}
$$
则旧下出生 $s-1$ 的第 $n+1$ 边满足
$$
\boxed{L_{n+1}L_{n+2}^{-1}L_{n+1}\preceq C L_n.}
\tag{2.2}
$$
假设中“每个 $a>0$”也可换成“某个趋于无穷的 $a$ 序列”。

**证明。** 同源可逆同余把 (2.1) 等价变为 $H_nH_{n+1}^{-1}H_n\preceq C H_{n-1}$。正定 $H_{n+1}$ 的 Schur 补进一步给
$$
\begin{pmatrix}C H_{n-1}&H_n\\H_n&H_{n+1}\end{pmatrix}\succeq0.
$$
把两个源副本均压到其旧下分量 $L$，再除以 $t$。由 (1.4) 及正锥的闭性，得
$$
\begin{pmatrix}C L_n&L_{n+1}\\L_{n+1}&L_{n+2}\end{pmatrix}\succeq0.
$$
旧 $L_{n+2}>0$，其 Schur 补正是 (2.2)。$\square$

这里使用的是原相邻正块本身，**不要求**更强首边铅笔 $P(t)$ 或其两条未证充分式。特别，旧低出生第二边的必要性不只是那个更强铅笔附带的要求；它已经被“全部新增权的真实首边”强制。

## 3. 严格违反可在有限新增权处保持

定理 2.1 不只是一个形式无穷权极限。设旧目标正块
$$
\mathcal B_\infty=
\begin{pmatrix}C L_n&L_{n+1}\\L_{n+1}&L_{n+2}\end{pmatrix}
$$
有单位负见证 $z=(x,y)\in L\oplus L$，
$$
\langle\mathcal B_\infty z,z\rangle=-\eta<0.
$$
对应的新压缩正块除以 $t$ 等于
$$
\mathcal B_t=\mathcal B_\infty+
\begin{pmatrix}C\mathcal E_{n-1}(t)&\mathcal E_n(t)\\
\mathcal E_n(t)&\mathcal E_{n+1}(t)\end{pmatrix}.
$$
由 (1.5)，其误差范数可粗略但准确地界为
$$
\|\mathcal B_t-\mathcal B_\infty\|
\le\frac{C\|W_{n-1}\|+2\|W_n\|+\|W_{n+1}\|}{t}.
\tag{3.1}
$$
所以只要选择有限正权满足
$$
\boxed{
a^2>
\frac{C\|W_{n-1}\|+2\|W_n\|+\|W_{n+1}\|}{\eta},
}
\tag{3.2}
$$
同一个 $z$ 仍给 $\langle\mathcal B_tz,z\rangle<0$。于是新完整相邻正块也不正，新实际第 $n$ 边严格违反同一 $C$。

全部 $W_j$ 都由旧真实完整逆、固定剪切和合法顶硬端定义，故 (3.2) 是可计算的有限阈值。不需要把无穷大权当成一个允许模型。

## 4. 全出生首边已包含全部高度的统一常数问题

对旧 $N$ 位行、出生 $r\ge0$、合法边 $m\ge1$，定义实际最佳比
$$
c_{N,r,m}(b)=
\left\|\Gamma_{m-1,r}^{-1/2}\Gamma_{m,r}
\Gamma_{m+1,r}^{-1}\Gamma_{m,r}
\Gamma_{m-1,r}^{-1/2}\right\|.
$$
合法性为 $N\ge2r+m+1$。令
$$
\mathfrak C_{r,m}
=\sup_{N\ge2r+m+1}\ \sup_{b\in(0,\infty)^N}c_{N,r,m}(b).
\tag{4.1}
$$
允许这些上确界为 $+\infty$。

**推论 4.1。** 对 $m\ge2$，
$$
\boxed{\mathfrak C_{r,m}\le\mathfrak C_{r+1,m-1},\qquad
\mathfrak C_{r,m}\le\mathfrak C_{r+m-1,1}.}
\tag{4.2}
$$
**证明。** 在旧行添加一位，把出生改为 $r+1$。新高度为 $N-2r-1\ge m$，所以新第 $m-1$ 边合法。把定理 2.1 应用于 $s=r+1,n=m-1$，即得第一式；也可直接用 §3 的有限严格违反传输证明上确界的比较。重复 $m-1$ 次给第二式。$\square$

因此
$$
\boxed{
\sup_{r\ge0,m\ge1}\mathfrak C_{r,m}
=\sup_{r\ge0}\mathfrak C_{r,1}.
}
\tag{4.3}
$$
右边包含在左边的上确界中，反向由 (4.2) 得到。特别，下列两命题对任意固定 $C<\infty$ 等价：

1. 所有有限正权 Boolean 行、所有合法出生的首处相邻边都有常数 $C$；
2. 所有有限正权 Boolean 行、所有合法出生及全部合法相邻高度都有同一个常数 $C$。

若某条旧第 $m$ 边严格违反一个候选 $C$，则 §3 逐次添加 $m-1$ 个足够强的有限正权，构造出生 $r+m-1$ 的首边严格违反；总位数只增加 $m-1$。

## 5. 边界与后续含义

- 本文保留非严格常数比较。即使每个有限首边在常数一处严格，取极限也只立即给其余边的非严格常数一；不能免费声称所有更高边严格。
- R271 的已证结论只覆盖固定出生一的首/末边；(4.2) 把旧 $(r,m)$ 送到出生 $r+m-1$ 的首边，故它没有用出生一结果填平高出生缺口。
- 因而可以把一般问题完全聚焦于首边，但必须保留“任意出生”的量词。证明该量词下的首边常数一或统一有限常数，确实足以通过本稿完成整个有限 primitive 相邻常数问题。
- 它仍不独自完成原 graph 传播、真实返回费用、无权 $N=M$ 或普通复 Hilbert 不变子空间问题。


## 6. 不能用巨大强等权池免费进入低占据范围

有一个与本稿相邻的量词陷阱：把一个极强位改成很多同样强的位，看似可以把最大单权占总平方权的比例 $\delta$ 压小。然而若要在真实约化块中保留同一个有效长度一的强位，必须同时支付强池内部的 primitive 出生。

具体取 $R=2k+1$ 个同权 $a$ 的强池位。其内部出生 $k$ 的等权正交升降串长度为 $R-2k=1$。把单位 primitive 向量及其归一上升像作为正交基，该串上的删除算子恰为权 $a$ 的二阶幂零单个位：唯一非零删除系数为
$$
a\sqrt{R-2k}=a.
$$
这也可直接由 $[d_{\rm pool},d_{\rm pool}^*]=a^2(RI-2\mathcal N)$ 核验：对单位出生 $k$ 向量 $v$，有 $\|d_{\rm pool}^*v\|=a$、$d_{\rm pool}d_{\rm pool}^*v=a^2v$，而 $\|(d_{\rm pool}^*)^2v\|^2=2a^4(R-2k)(R-2k-1)=0$。因而该正交串同时约化删除、伴随、全部层 Gram 及其完整逆，故与旧行张量后确实保留原来的一强位模型。但原新出生 $s$ 变成实际物理出生 $s+k$。

令旧平方权总和为 $S_{\rm old}$。在 $a^2$ 大于全部旧平方权时，新稀散参数为
$$
\delta_R=\frac{a^2}{S_{\rm old}+(2k+1)a^2}.
$$
所以极强位极限给
$$
\boxed{
\lim_{a\to\infty}(s+k)\delta_R
=\frac{s+k}{2k+1}
=\frac12+\frac{s-1/2}{2k+1}>\frac12,
\qquad s\ge1.
}
\tag{6.1}
$$
再令 $k\to\infty$，只能从上方趋于 $1/2$。这仍在 [玻色仿射传输](R279-bosonic-affine-primitive-gram-transfer-and-low-occupation-bounds.md) 已付首边阈值 $s\delta\le1/(2\sqrt2)$ 之外。

因此不能同时保留“一有效强位”的实际 MP 模型，又忽略强池内部出生，用巨大强等权池声称已把本稿所有源化到现有低占据首边定理中。这个限制不反驳玻色定理或一般相邻猜想；它只排除上述省略出生费用的推论。

## 7. 普适首边常数不可能小于一

### 7.1 等权真空的中边及回传

对 $h$ 个单位权、出生零，primitive 是真空直线，准确有
$$
\Gamma_j=\binom hj^{-1},\qquad
c_{h,0,n}=\frac{n(h-n)}{(n+1)(h-n+1)}.
\tag{7.1}
$$
因为 $(D^j/j!)^*$ 把真空送到全部 $j$ 元子集的和，完整源 Gram 为 $\binom hj$，所以这不是归一化猜测。

取 $h=2m,n=m$，得 $c_{2m,0,m}=m^2/(m+1)^2\to1$。由 (4.2)，
$$
\mathfrak C_{m-1,1}\ge\frac{m^2}{(m+1)^2}.
$$
因而
$$
\boxed{\sup_{s\ge0}\mathfrak C_{s,1}\ge1.}
\tag{7.2}
$$
这已经严格排除任何普适 $C<1$；没有证明普适 $C=1$ 的上界。每个固定有限模型严格小于一与这个上确界下界完全相容。

### 7.2 八位、出生二的精确首边比大于二分之一

取两个头权 $a,b>0$ 及六个单位池位。只在此节令物理出生为二。池置换的固定子空间同时约化 $D,D^*$、全部完整层 Gram 及其逆。在出生二和高度一、二的输入层，固定子空间分别都有四个完整基向量，对应头状态 $00,10,01,11$；池部分采用所有相应大小子集的**未归一和**。

在出生二，四个基的池占据数为 $2,1,1,0$，范数平方为 $15,6,6,1$。由真实一阶删除直接得到 primitive 线的共同坐标
$$
v=\left(\frac{ab}{15},-\frac b6,-\frac a6,1\right)^\mathsf T.
\tag{7.3}
$$
确实，出生一的三个输出坐标是
$5v_{00}+av_{10}+bv_{01}$、$6v_{10}+bv_{11}$、$6v_{01}+av_{11}$，均为零。

为了保留完整输入而不把试探源当最小源，现直接求完整 $A_n=D^n/n!$ 的逆。对 $n=0,1,2$，源行的头集合为 $I$，输入列的头集合为 $J$。令源池数 $p=2-|I|$。当 $I\subseteq J$ 时，实际矩阵条目为
$$
(A_n)_{I,J}=a_{J\setminus I}
\binom{6-p}{n-|J\setminus I|},
\tag{7.4}
$$
否则为零；非法二项式为零。这里池上的 $q$ 次归一删除系数恰为 $\binom{6-p}{q}$，头删除系数为相应权乘积。四阶方阵按头包含关系为三角形，且合法 $n$ 的对角均非零。

解 $A_nx_n=v$，得到准确全输入解
$$
(x_n)_{11}=\binom6n^{-1},\qquad
(x_n)_{10}=-\frac{b(n+1)}{6\binom5n},\qquad
(x_n)_{01}=-\frac{a(n+1)}{6\binom5n},
$$
$$
(x_n)_{00}=\frac{ab(n+1)(n+2)}{30\binom4n}.
\tag{7.5}
$$
可逐行代入 (7.4) 核验。该固定输入块的逆唯一；而任何全物理原像经池置换平均后仍保留同一固定源，范数不增。于是 (7.5) 的范数就是**整个物理层**的真正最小逆费用，非固定输入只给额外正交核方向。

按目标池数 $n+2,n+1,n+1,n$ 乘以对应二项式范数，得到共同源费用
$$
\gamma_n=
\frac{a^2b^2(n+1)(n+2)}{30\binom4n}
+\frac{(a^2+b^2)(n+1)}{6\binom5n}
+\binom6n^{-1}.
\tag{7.6}
$$
特别
$$
\gamma_0=\frac{a^2b^2}{15}+\frac{a^2+b^2}{6}+1,
$$
$$
\gamma_1=\frac{a^2b^2}{20}+\frac{a^2+b^2}{15}+\frac16,
\qquad
\gamma_2=\frac{a^2b^2}{15}+\frac{a^2+b^2}{20}+\frac1{15}.
\tag{7.7}
$$
归一 primitive Gram 在线上的本征值为 $\gamma_j/\gamma_0$，所以首边比准确是 $\gamma_1^2/(\gamma_0\gamma_2)$。

取 $a=b=4$，即实际八位权行
$$
(4,4,1,1,1,1,1,1),
$$
就有
$$
\gamma_0=\frac{117}{5},\qquad
\gamma_1=\frac{151}{10},\qquad
\gamma_2=\frac{281}{15},
$$
$$
\boxed{\frac{\gamma_1^2}{\gamma_0\gamma_2}
=\frac{22801}{43836}>\frac12.}
\tag{7.8}
$$
这是整个实际出生二空间中的一个正交约化 primitive 分支，足以否定普适首边常数二分之一。它没有违反原常数一猜想。

令 $a=b\to\infty$，由 (7.7) 首边比趋于 $9/16$，与六位等权真空中央边 $c_{6,0,3}=9/16$ 的两次回传一致。这里给出的有限权 $4$ 不依赖数值优化或无穷权模型。[四维真实输入的精确有理校验](../notes/2026-11-14-heavy-bit-first-edge-half-counterexample-789f-next.py)从 (7.4) 重新生成矩阵、求解、计算原基范数，并断言 (7.8)。
