# 有限 Walsh 阶对整数局部迹的唯一性

日期：2026-11-12（UTC+8）。分工：`l2_moments`。

**状态：以下命题已证明，是 R40/R44 局部迹路线的中间边界。** 它覆盖全部有限 Walsh chaos，而非只覆盖有限秩导数类。没有证明一般有限 chaos 的向量必有这些迹，也没有证明核方程自动给出迹正则性；不解决普通不变子空间问题。

## 1. 设定

在 $H=L^2(\mathbb Z_2,\mu)$ 上写 $\chi_j=(-1)^{b_j}$，$\chi_S=\prod_{j\in S}\chi_j$，并令

$$
H_{\le d}=\left\{f=\sum_{|S|\le d}\widehat f(S)\chi_S:
\sum_S|\widehat f(S)|^2<\infty\right\}.
$$

对一个固定非负整数 $r$，说 $f$ 在 $r$ 的局部平方均值迹为零，是指

$$
\|f(r+2^m\,\cdot)\|_{L^2(\mathbb Z_2)}\longrightarrow0
\quad(m\to\infty).
\tag{1.1}
$$

此处只需取 $2^m>r$。每个固定 $m,r$ 的重标度限制在 $L^2$ 等价类上良定义，算子范数至多 $2^{m/2}$。它不是点值评价。

## 2. 精确最高阶差分公式

固定 $S\subset\mathbb N_0$，$|S|=d$。对 $\varepsilon\in\{0,1\}^S$，定义整数

$$
r_\varepsilon=\sum_{j\in S}\varepsilon_j2^j.
$$

对每个 $m>\max S$，在 $L^2(\mathbb Z_2)$ 中有精确恒等式

$$
\boxed{
\sum_{\varepsilon\in\{0,1\}^S}
(-1)^{\sum_{j\in S}\varepsilon_j}
f(r_\varepsilon+2^m z)
=2^d\widehat f(S)
\qquad(f\in H_{\le d}).
}
\tag{2.1}
$$

证明先对有限 Walsh 和计算。对于一个 $\chi_T$，若 $S\not\subseteq T$，选择 $j\in S\setminus T$，对 $\varepsilon_j$ 的两个取值相消。若 $S\subseteq T$，由于 $|T|\le d=|S|$，只能 $T=S$，此时每项的乘积符号恰好抵消，留下 $2^d$。这就给出 (2.1)。对一般 $f\in H_{\le d}$，用有限 Walsh 和逼近；对于固定 $m$，有限多个重标度限制都是有界算子，故恒等式传到 $L^2$ 极限。

特别地，

$$
|\widehat f(S)|
\le2^{-d}\sum_{\varepsilon\in\{0,1\}^S}
\|f(r_\varepsilon+2^m\,\cdot)\|_2.
\tag{2.2}
$$

公式的要点是先固定 $S$，再让 $m\to\infty$；所需的 $2^d$ 个整数 $r_\varepsilon$ 不随 $m$ 变化。

## 3. 全部整数零迹迫使有限阶向量为零

**定理 3.1。** 若 $f\in H_{\le d}$，且 (1.1) 对每个非负整数 $r$ 成立，则 $f=0$。

证明对 $d$ 归纳。$d=0$ 时 $f$ 为常数，任意一个零迹就迫使它为零。设 $d\ge1$。对任意 $|S|=d$，将各个固定整数 $r_\varepsilon$ 的零迹代入 (2.2)，令 $m\to\infty$，得 $\widehat f(S)=0$。所以 $f\in H_{\le d-1}$，仍具有相同的全部零迹。归纳给 $f=0$。证毕。

更一般地，若 $f,g\in H_{\le d}$ 在每个非负整数处都具有相同的有限局部平方均值迹，应用于 $f-g$ 得 $f=g$。这里只证明迹映射在其定义域上的单射性，不声称迹对每个有限阶向量都存在。

## 4. 与 R44 幂值域的直接联系

R44 已证明

$$
\mathcal R_\infty:=\bigcap_{n\ge1}\operatorname{Ran}A^n
$$

在整个 $H$ 中稠密，而且其中每个向量都在所有非负整数处具有零局部平方均值迹。由定理 3.1，得到

$$
\boxed{
\mathcal R_\infty\cap H_{\le d}=\{0\}
\qquad\text{对每个有限 }d.
}
\tag{4.1}
$$

这和两个空间各自在不同意义下稠密并不矛盾；没有把稠密线性空间的交误认为必非零。

还可保留有限幂的精确信息。若 $f=A^nh\in H_{\le d}$，且 $S$ 满足 $|S|=d$ 和

$$
\sum_{j\in S}2^j<n,
$$

那么 $\widehat f(S)=0$。因为 (2.1) 使用的全部整数 $r_\varepsilon$ 都小于 $n$，而在柱集 $r+2^m\mathbb Z_2$ 上，$A^n$ 的权积至少有一个因子不大于 $a_m$，其余因子不大于一，所以

$$
\|f(r+2^m\,\cdot)\|_2
\le2^{m/2}a_m\|h\|_2\longrightarrow0.
$$

将这些零迹代入 (2.2) 即得所述最高阶系数消失。这里没有对尚未满足这个二进制位置条件的其他系数作断言。

## 5. 对原临界核的准确意义

R43/R44 对原 $D=I-Q$ 的核已经证明：若一个核向量在全部非负整数处存在局部平方均值迹，则这些迹全为零。因而本条给出条件性推论：

$$
v\in\ker D\cap H_{\le d},\quad
v\text{ 在每个非负整数具有局部平方均值迹}
\quad\Longrightarrow\quad v=0.
$$

这个推论仍要求真实的迹存在性，不能仅由有限 Walsh 次数代替。任意慢的系数尾未必在这些指定整数点收敛；更高阶的低位收缩也可能放大尾部。下一缺口是从 $Dv=0$ 得到这些迹，而本条没有证明它。
