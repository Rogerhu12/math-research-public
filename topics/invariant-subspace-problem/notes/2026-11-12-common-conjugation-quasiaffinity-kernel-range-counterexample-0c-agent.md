# 共同共轭对称与全空间 quasiaffinity 不推出核限制像稠密

日期：2026-11-12（UTC）。
构造由 literature 提出；critical_kernel 独立核验全部伴随、核、范围和双倍共轭步骤并保存此完整证明。
本稿不另编号，也不是实际候选算子的反例。

## 1. 要否定的结构捷径

不能仅由以下条件推出 $\overline{T\ker B}=\ker B$：

- $B,T$ 是两个有界且交换的算子；
- $T$ 单射且值域稠密；
- 存在同一个共轭 $J$，使 $B^*=JBJ$、$T^*=JTJ$。

下面给出显式反例；其中还可要求 $T$ 紧且拟幂零。
本例的 $B$ 非零且 $B^2=0$，所以它违反实际 $\mathcal A$ 的无零因子性质。
因此它只否定一般结构推理，不能用来否定 R140/R151 对实际模型另行证明的限制稠密结论。

全篇内积取第一变量线性。

## 2. Volterra 的全部所需事实

令 $H=L^2(0,1)$、$e(t)=1$，定义
$$
(Vf)(t)=\int_0^t f(s)\,ds.
\tag{2.1}
$$
其通常伴随为
$$
(V^*f)(t)=\int_t^1 f(s)\,ds.
\tag{2.2}
$$
由绝对连续代表的导数，$Vf=0$ 或 $V^*f=0$ 都迫 $f=0$。
所以 $V,V^*$ 单射，而且各自像稠密，因为
$$
\overline{\operatorname{Ran}V}=(\ker V^*)^\perp=H,\qquad
\overline{\operatorname{Ran}V^*}=(\ker V)^\perp=H.
\tag{2.3}
$$

另一方面，
$$
\boxed{e\notin\operatorname{Ran}V,\qquad e\notin\operatorname{Ran}V^*.}
\tag{2.4}
$$
确实，$Vf$ 的绝对连续代表在0为零，$V^*f$ 的绝对连续代表在1为零。
若其中一个等于 $e$ 的 $L^2$ 类，其连续代表就必须在整个闭区间等于常数1，与对应端点值矛盾。

$V$ 的核为 $1_{\{0<s<t<1\}}$，故它是 Hilbert–Schmidt 算子，特别紧。
对 $n\ge1$，
$$
(V^nf)(t)=\frac1{(n-1)!}\int_0^t(t-s)^{n-1}f(s)\,ds.
\tag{2.5}
$$
该非负核的行、列积分都不超过 $1/n!$，由 Schur 估计
$$
\|V^n\|\le\frac1{n!}.
$$
因此 $r(V)=0$，$V$ 拟幂零；$V^*$ 同样成立。

## 3. 未双倍的三个分量块

置
$$
H_0=\mathbb C\oplus H\oplus H,
$$
并定义
$$
B_0(c,x,y)=(0,y,0),
\tag{3.1}
$$
$$
T_0(c,x,y)=\bigl(\langle y,e\rangle,\ ce+Vx,\ Vy\bigr).
\tag{3.2}
$$
这些都是实际有界算子。$B_0\ne0$，而直接代入给 $B_0^2=0$。

它们交换：
$$
B_0T_0(c,x,y)=(0,Vy,0)
=T_0B_0(c,x,y).
\tag{3.3}
$$

通常伴随为
$$
B_0^*(c,x,y)=(0,0,x),
\tag{3.4}
$$
$$
\boxed{
T_0^*(c,x,y)
=\bigl(\langle x,e\rangle,\ V^*x,\ ce+V^*y\bigr).
}
\tag{3.5}
$$
例如将 (3.2) 与 $(d,z,w)$ 配对，得到
$$
\langle y,e\rangle\overline d
+c\langle e,z\rangle
+\langle x,V^*z\rangle+\langle y,V^*w\rangle,
$$
这正是与 (3.5) 所列向量的内积。

### 3.1 $T_0$ 单射且像稠密

若 $T_0(c,x,y)=0$，则 $Vy=0$ 先给 $y=0$。
再由 $ce+Vx=0$ 及 $e\notin\operatorname{Ran}V$ 得 $c=0$，
最后 $Vx=0$ 给 $x=0$。
故
$$
\ker T_0=0.
\tag{3.6}
$$

若 $T_0^*(c,x,y)=0$，则第二分量 $V^*x=0$ 给 $x=0$。
第三分量 $ce+V^*y=0$ 结合 (2.4) 给 $c=0$，继而 $y=0$。
故
$$
\ker T_0^*=0,\qquad
\overline{\operatorname{Ran}T_0}=H_0.
\tag{3.7}
$$
所以 $T_0$ 是 quasiaffinity。

### 3.2 紧性与拟幂零性

$T_0$ 由两个 Volterra 块及两个有限秩块组成，故紧。

把 $H_0$ 写成 $(\mathbb C\oplus H)\oplus H$。定义
$$
D(c,x)=(0,ce+Vx),\qquad
E y=(\langle y,e\rangle,0).
$$
则
$$
T_0=
\begin{pmatrix}D&E\\0&V\end{pmatrix}.
\tag{3.8}
$$
对每个 $\lambda\ne0$，$D-\lambda I$ 可逆：
第一分量先解 $-\lambda c=s$，随后用 $V-\lambda I$ 解第二分量。
因此 $D-\lambda I$、$V-\lambda I$ 都是有界单位。
上三角块逆公式遂给 $T_0-\lambda I$ 可逆。
有界算子的谱非空，所以
$$
\sigma(T_0)=\{0\}.
\tag{3.9}
$$
$T_0$ 紧且拟幂零，$T_0^*$ 亦然。

## 4. 核限制已经失去稠密像

由 (3.1)，
$$
M_0:=\ker B_0=\mathbb C\oplus H\oplus\{0\}.
\tag{4.1}
$$
这是闭 $T_0$ 不变子空间，因为 $B_0,T_0$ 交换。
其像为
$$
T_0M_0
=\{0\}\oplus(\mathbb Ce+\operatorname{Ran}V)\oplus\{0\}.
$$
由 $\operatorname{Ran}V$ 稠密，
$$
\boxed{
\overline{T_0M_0}
=\{0\}\oplus H\oplus\{0\}
\subsetneq M_0.
}
\tag{4.2}
$$
缺失恰为一个标量维度。

同样，
$$
\ker B_0^*=\mathbb C\oplus\{0\}\oplus H,
$$
而
$$
\boxed{
\overline{T_0^*(\ker B_0^*)}
=\{0\}\oplus\{0\}\oplus H
\subsetneq\ker B_0^*.
}
\tag{4.3}
$$
这同样缺失一个维度。

## 5. 双倍后获得同一个共轭

令 $J_0$ 为 $H_0$ 上逐分量的通常复共轭：
$$
J_0(c,x,y)=(\overline c,\overline x,\overline y).
$$
(3.1)—(3.5) 的积分核和向量 $e$ 都为实，因此
$J_0$ 分别与 $B_0,T_0,B_0^*,T_0^*$ 交换。

在
$$
\mathscr H=H_0\oplus H_0
$$
上定义
$$
B=B_0\oplus B_0^*,\qquad
T=T_0\oplus T_0^*,
\tag{5.1}
$$
以及
$$
J(u,v)=(J_0v,J_0u).
\tag{5.2}
$$
$J$ 反线性、等距且 $J^2=I$，确实是共轭。
直接计算
$$
JBJ=B_0^*\oplus B_0=B^*,\qquad
JTJ=T_0^*\oplus T_0=T^*.
\tag{5.3}
$$
因此 $B,T$ 对同一个 $J$ 对称。

$B,T$ 仍交换，因为 (3.3) 及其伴随分别给出两个块上的交换性。
$T$ 单射且值域稠密，由 $T_0,T_0^*$ 的对应性质立即得到；
$T$ 紧且拟幂零，因为它是两个紧拟幂零算子的有限直和。
另外
$$
B\ne0,\qquad B^2=0.
\tag{5.4}
$$

## 6. 最终严格不等式

记
$$
M=\ker B
=(\mathbb C\oplus H\oplus0)
\oplus(\mathbb C\oplus0\oplus H).
$$
由 (4.2)—(4.3)，
$$
\boxed{
\overline{TM}
=(0\oplus H\oplus0)
\oplus(0\oplus0\oplus H)
\subsetneq M.
}
\tag{6.1}
$$
在 $M$ 中的余维恰为2。

所以共同共轭对称、交换、全空间单射稠密、甚至紧拟幂零性，仍不足以把全空间稠密像传给另一个交换子的核。

## 7. 对实际研究的准确边界

本例不能直接移植成实际候选 $\mathcal A$ 内的两个算子：
$B\ne0$ 且 $B^2=0$ 与 R32 的 $\mathcal A$ 无零因子性质冲突。
它也没有同时保留本题的所有高位归一化幂结构。

其作用仅是阻止下述无效一步：
“$T$ 全空间单射稠密且与 $B$ 共同 $C$ 对称，因此 $T$ 在 $\ker B$ 上像稠密。”

R140/R151 的正确限制密度使用实际四次型、真实有限放大或强主理想逼近；
这些额外机制没有被本例否定。
在慢平方共振或一般临界二阶核中，如果需要 $\overline{TM}=M$，仍须给出适用于那个实际 $T,M$ 的独立论证。
