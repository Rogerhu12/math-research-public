# 实际反障碍：全部自然幂域与逐项系数截断不是同一件事

日期：2026-11-12（UTC）。作者：critical_kernel。
状态：完整实际证明；不编号研究记录。

本稿给出一个明确的真实第一阶 $X$ 及一个单位连续向量 $x$，满足：

- $x$ 属于 $X$ 的全部自然幂域；
- 低位条件期望 $Q_mx$ 在每一个固定自然幂图范数中趋于 $x$；
- 但有界系数截断 $X_{<m}=\sum_{j<m}a_jV_j$ 在 $x$ 上的范数沿一列 $m$ 趋于无穷。

因此，即使未知有界分支中的向量已知具有全部自然幂，
也不能不加论证地使用 $X_{<m}x\to Xx$ 或“尾第一阶趋零”。
本例中的向量不被放入任何未知不变分支；末节还说明它本身可由已证分块定理判为循环。

## 1. 真实模型与记号

仍使用
$$
V_j=(I-N_j)(I+N_j)^{-1},\qquad
S_j=I-2E_j,\qquad
K(a)=\sum_ja_j(V_j-S_j).
$$
对 $a\in\ell^2$，R125 给
$$
X=X_a=X^0(a)+K(a),
\qquad X^0(a)=\overline{\sum_ja_jS_j},
$$
其有限柱作用决定实际闭实现。
有
$$
\|K(a)\|\le8\sum_j|a_j|\eta_j
\le8\|a\|_2\|\eta\|_2.
\tag{1.1}
$$
每个有界部分 carry
$$
K_{<m}=\sum_{j<m}a_j(V_j-S_j)
$$
具有同一个上界。记该共同界为 $k_0$。

Walsh 基写为 $\chi_F$，$F$ 是有限位集；
$J_F=M_{\chi_F}$ 为对应自伴酉乘法算子。
$Q_m$ 是只保留 $[0,m)$ 内 Walsh 支撑的条件期望。
记 $\Lambda=I+\mathcal N$，$\mathcal N\chi_F=|F|\chi_F$。

## 2. 明确的成对符号块

对 $n\ge1$，令
$$
L_n=2^{4n},\qquad \beta_n=2^{-3n},\qquad
h_0=0,\qquad h_n=h_{n-1}+2L_n.
$$
定义相邻两个半块
$$
I_n^+=[h_{n-1},h_{n-1}+L_n),\qquad
I_n^-=[h_{n-1}+L_n,h_n),
$$
并令
$$
a_j=
\begin{cases}
+\beta_n,&j\in I_n^+,\\
-\beta_n,&j\in I_n^-.
\end{cases}
\tag{2.1}
$$
这些有限块依次覆盖全部非负整数位。

准确地，
$$
\|a\|_2^2
=\sum_{n\ge1}2L_n\beta_n^2
=2\sum_{n\ge1}2^{-2n}
=\frac23,
\tag{2.2}
$$
而
$$
\sum_j|a_j|
=2\sum_{n\ge1}L_n\beta_n
=2\sum_{n\ge1}2^n=\infty.
\tag{2.3}
$$
正、负两支各自不可和。因此 R138 将这个实际第一阶判为全平面连续谱类型；
这一谱事实不参与下述截断反例的证明。

置
$$
F_n=I_n^+\cup I_n^-=[h_{n-1},h_n).
$$
各 $F_n$ 两两不交，且
$$
\sum_{j\in F_n}a_j=0.
\tag{2.4}
$$

定义
$$
c_n=2^{-n/2},\qquad
x=\sum_{n\ge1}c_n\chi_{F_n}.
\tag{2.5}
$$
由 Walsh 正交性，
$$
\|x\|^2=\sum_{n\ge1}2^{-n}=1.
\tag{2.6}
$$
又 $\sum_n c_n<\infty$，故 (2.5) 一致收敛；
$x$ 有连续有界代表，且具有无界 Walsh 次数。

## 3. R171 的一致界确实不含翻转位数

这里把所需接口连同真实 carry 的原因完整重述。

对 $m>j$，有限物理截断给局部差
$$
B_{j,m}=V_j^{[m+1]}-V_j^{[m]},\qquad
\operatorname{supp}B_{j,m}\subseteq[j,m],\qquad
\|B_{j,m}\|\le18\alpha_m/\alpha_j.
$$
并有
$$
V_j-S_j=\sum_{m\ge j+1}B_{j,m},\qquad
\alpha_m/\alpha_j\le\eta_j\eta_*^{m-j-1},
\quad \eta_*<1/4.
\tag{3.1}
$$

若 $B$ 支撑于一个含 $\ell$ 位的物理块，
则按块外 Walsh 次数分解可得
$$
\|\Lambda^sBy\|\le(\ell+1)^s\|B\|\,\|\Lambda^sy\|
\quad(s\in\mathbb N_0).
\tag{3.2}
$$
对任意有限 $F$，
$J_FBJ_F$ 仍支撑于同一块、范数相同：
块外 Walsh 乘法两次相消。
因此 (3.2) 的常数不受 $F$ 的位置或 $|F|$ 影响。

逐项应用 (3.1)—(3.2)，得到
$$
\|\Lambda^sJ_FK(a)J_F y\|
\le\kappa_s\|a\|_2\|\Lambda^s y\|,
\tag{3.3}
$$
其中可取
$$
\kappa_s
=18\|\eta\|_2\sum_{\ell\ge1}(\ell+2)^s\eta_*^{\ell-1}<\infty.
\tag{3.4}
$$
这一估计包含真正的次数域保持：局部部分和先在该加权范数下 Cauchy，
再用 $\Lambda^s$ 的闭性取极限。

纯第一阶的创建、消去、对角三部分给
$$
\|\Lambda^sX^0(b)y\|
\le(2^s+3)\|b\|_2\|\Lambda^{s+1}y\|,
\qquad
X^0(b)\operatorname{Dom}\Lambda^{s+1}
\subseteq\operatorname{Dom}\Lambda^s.
\tag{3.5}
$$

令 $a^F$ 在 $F$ 中把 $a_j$ 改为 $-a_j$，其余不变。
有限柱上的实际共轭恒等式及闭包给
$$
J_FXJ_F-2\sum_{j\in F}a_j
=X^0(a^F)+J_FK(a)J_F=:L_F.
\tag{3.6}
$$
这里 $\|a^F\|_2=\|a\|_2$。
因此，若
$$
D_s=(2^s+3+\kappa_s)\|a\|_2,
$$
则
$$
L_F\operatorname{Dom}\Lambda^{s+1}
\subseteq\operatorname{Dom}\Lambda^s,\qquad
\|\Lambda^sL_Fy\|\le D_s\|\Lambda^{s+1}y\|.
\tag{3.7}
$$
常数真正对所有有限 $F$ 一致，不是只对固定 $|F|$ 一致。

取真空 $1$，其 $\Lambda^p$ 范数为1。由 (3.7) 逐次作用，
$$
1\in\operatorname{Dom}L_F^p,\qquad
\|L_F^p1\|\le C_p:=\prod_{s=0}^{p-1}D_s.
\tag{3.8}
$$
规定 $C_0=1$。

对 $F=F_n$，(2.4) 使 (3.6) 的标量中心恰为零。
故真实自然幂均有定义，且
$$
\boxed{
\chi_{F_n}\in\bigcap_{p\ge0}\operatorname{Dom}X^p,\qquad
\|X^p\chi_{F_n}\|\le C_p\quad(n\ge1).
}
\tag{3.9}
$$
没有出现 $6^{|F_n|}$、$|F_n|^s$ 或其他块大小损失。

## 4. x 属于全部自然幂域，条件期望也在各幂图中收敛

对每个固定 $p$，
$$
\sum_n\|c_nX^p\chi_{F_n}\|
\le C_p\sum_n c_n<\infty.
\tag{4.1}
$$
令
$$
y_p=\sum_n c_nX^p\chi_{F_n}.
$$
有限部分和分别属于全部自然幂域。
从 $p=0$ 开始，用 $X$ 的闭性归纳：
若部分和的第 $p-1$ 次像趋于 $y_{p-1}$、
第 $p$ 次像趋于 $y_p$，则
$y_{p-1}\in\operatorname{Dom}X$ 且 $Xy_{p-1}=y_p$。
因此
$$
\boxed{x\in\bigcap_{p\ge0}\operatorname{Dom}X^p,\qquad X^px=y_p.}
\tag{4.2}
$$
此论证甚至不需要先调用每个 $X^p$ 的闭性定理。

由于每个 $F_n$ 是完整的相邻块，
$$
Q_mx=\sum_{\{n:h_n\le m\}}c_n\chi_{F_n}.
\tag{4.3}
$$
所以对每个固定 $p$，
$$
\boxed{
\|X^p(x-Q_mx)\|
\le C_p\sum_{\{n:h_n>m\}}2^{-n/2}
\longrightarrow0.
}
\tag{4.4}
$$
特别，$Q_mx\to x$ 同时在所有固定有限阶图范数中成立。
这比单独声明 $x$ 属于所有幂域更强。

## 5. 但普通系数截断在 x 上发散

定义实际有界截断
$$
X_{<m}=\sum_{j<m}a_jV_j
=X^0_{<m}+K_{<m}.
$$
Walsh 基上的纯作用是
$$
S_j\chi_F=
\begin{cases}
\chi_{F\cup\{j\}},&j\notin F,\\
2\chi_F-\chi_{F\setminus\{j\}},&j\in F.
\end{cases}
$$
故
$$
X^0_{<m}=2D_m+H_m,
\tag{5.1}
$$
其中
$$
D_m\chi_F=\left(\sum_{j<m,\ j\in F}a_j\right)\chi_F
$$
为对角项，$H_m$ 只在集合中翻转一个位，系数为 $\pm a_j$。

取第 $n$ 块的正半截终点
$$
m_n=h_{n-1}+L_n.
$$
此前各完整块的系数和为零，此后各块尚未出现；
因此
$$
D_{m_n}x
=c_nL_n\beta_n\chi_{F_n}
=2^{n/2}\chi_{F_n}.
\tag{5.2}
$$

另一方面，不同 $F_n$ 的 Hamming 距离大于2。
所以全部集合
$$
F_n\triangle\{j\}
$$
在不同 $(n,j)$ 之间互异，且没有一个等于任意 $F_k$。
于是 $H_mx$ 的各项两两正交，也与 $D_mx$ 正交，并且
$$
\|H_mx\|^2
=\left(\sum_n|c_n|^2\right)\sum_{j<m}|a_j|^2
\le\|a\|_2^2.
\tag{5.3}
$$
由 (5.1)—(5.3)，
$$
\|X^0_{<m_n}x\|\ge2^{n/2+1}.
$$
真实 carry 部分满足 $\|K_{<m_n}\|\le k_0$，且 $\|x\|=1$。
所以
$$
\boxed{
\|X_{<m_n}x\|
\ge2^{n/2+1}-k_0
\longrightarrow\infty.
}
\tag{5.4}
$$
因此不只没有 $X_{<m}x\to Xx$，其范数还沿明确子列发散。

这里每个 $X_{<m}$ 都是已经有定义的有界算子。
没有把无限级数擅自重新排序，也没有用纯模型结果替换实际 carry。

## 6. 两类“有限头逼近”必须区别

本例同时有
$$
X(Q_mx)\longrightarrow Xx
$$
和
$$
\sup_m\|X_{<m}x\|=\infty.
$$
前一式截断的是向量的 Walsh 支撑，后一式截断的是算子的系数行。
两种截断不相同，也不能由共同有限柱核心自动互换。

特别，从未知 $M$ 上 $X|_M$ 有界可以推出
$M\subseteq\operatorname{Dom}X^p$、各 $X^p|_M$ 有界；
即使另外得到某个 $x\in M$ 的所有条件期望图逼近，
仍不能仅凭这些事实写
$$
\left(X-\sum_{j<m}a_jV_j\right)x\longrightarrow0.
$$
要使用该极限，必须给出真正的系数截断估计或额外的域定理。

本例没有把 $x$ 放入一个 $A$ 不变有界分支。
事实上，$\overline{\operatorname{span}}\{\chi_{F_n}\}$ 并不因本证明而成为
$A$ 或 $X$ 不变空间。

## 7. 可选的进一步定位：这个 x 本身已有循环性证明

本节不用于截断反例。

R136 的分块定理适用于 (2.5)：
每个 $c_n\chi_{F_n}$ 是一个不交有限物理块上的零均值柱向量，
且 $\sum_n c_n^2<\infty$。
其所需真实 carry 和可由
$$
\sum_n c_n C^{|F_n|}
\sum_{j\in F_n}\eta_j<\infty
\tag{7.1}
$$
保证，其中 $C$ 是 R136 的固定有限常数。

第一个块只有有限项，不影响收敛。
对于 $n\ge2$，$|F_n|=2\cdot16^n$ 与 $h_{n-1}$ 成固定比例，
而
$$
\sum_{j\in F_n}\eta_j\le|F_n|\eta_{h_{n-1}},
\qquad
\eta_{h_{n-1}}\le\exp(-770\cdot16^{h_{n-1}}).
$$
这个双指数衰减压过 $C^{|F_n|}$，故 (7.1) 成立。
因此 R136 还给出 $x$ 对实际 $A$ 循环。

所以此例没有给原 Hilbert 不变子空间问题制造反例；
它只是一个完全实际、甚至已知循环的向量，
用来严格排除“全部自然幂域即可逐项截断第一阶”的推理。
