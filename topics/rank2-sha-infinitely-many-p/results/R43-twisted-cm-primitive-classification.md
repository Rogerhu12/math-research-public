# R43：带常数 twist 的 CM 共同原函数分类

日期：2026-11-12。**状态：以下标量差分幂的分类已证明。**

R42 排除了无 twist 的非代数共同原函数。
本篇准确计算加入固定常数 twist 后保留下来的例外。
对本题的两个互素乘子，只有两种非有理来源：

- 整数权的椭圆对数单项式 \(z^k\)；
- 反 CM 字符对应的 Weierstrass \(\zeta(z)\)。

取任意有限的差分幂不会再增加广义特征方向。
证明只为这些标量幂构造一个有限 Jordan 向量；
没有声称分类所有一般矩阵差分系统。

## 1. 完整陈述

沿用 R42：
\[
E:y^2=x^3-17x,\quad \Lambda=\Omega\mathbb Z[i],\quad
b=2+i,\quad c=3+2i,\quad \mathcal R=\mathbb C(E),
\]
\[
(\sigma_aF)(z)=F(az),\qquad z=\log_E(t).
\]
固定
\[
\lambda_b,\lambda_c\in\mathbb C^\times,\qquad r,s\ge1,
\]
并置
\[
L_b=\sigma_b-\lambda_b,\qquad L_c=\sigma_c-\lambda_c.
\]

**分类定理。** 假定 \(F\in\mathbb C((z))\) 且
\[
L_b^rF\in\mathcal R,\qquad L_c^sF\in\mathcal R.
\tag{1.1}
\]
则恰有以下分类：

1. 若存在 \(k\in\mathbb Z\setminus\{0\}\) 使
   \[
   (\lambda_b,\lambda_c)=(b^k,c^k),
   \tag{1.2}
   \]
   则
   \[
   F\in\mathcal R+\mathbb C z^k.
   \tag{1.3}
   \]

2. 若
   \[
   (\lambda_b,\lambda_c)=(\bar b,\bar c),
   \tag{1.4}
   \]
   则
   \[
   F\in\mathcal R+\mathbb C\zeta(z,\Lambda).
   \tag{1.5}
   \]

3. 除以上两种情形外，
   \[
   F\in\mathcal R.
   \tag{1.6}
   \]

三个情形相互排斥。
\(k=0\) 只给常数，已经包含在 \(\mathcal R\)，所以不列作额外方向。
负整数 \(k\) 完整包含在 (1.2)，不假定 \(F\) 在原点正则。

这些也是充分的描述：
\(z^k\) 在 (1.2) 下被两个一阶 \(L_a\) 消去；
而在 (1.4) 下，
\[
\sigma_a\zeta-\bar a\zeta\in\mathcal R,
\qquad a=b,c.
\tag{1.7}
\]
因此所列各空间的元素都满足 (1.1)。

## 2. 不会重合的字符与最后的常数项

对于固定 \(b=2+i\)，\(b^k=\lambda_b\) 最多有一个整数解 \(k\)，
因为 \(|b|>1\)。
此外 \(b^k=\bar b\) 不可能：
绝对值先给 \(k=1\)，随后要求 \(b=\bar b\)，矛盾。
所以 (1.2) 与 (1.4) 不重合。

下文会多次用到一个形式系数事实。
若一个 Laurent 向量 \(G=\sum_kv_kz^k\) 满足
\[
\sigma_bG=BG+e_b,\qquad \sigma_cG=CG+e_c,
\tag{2.1}
\]
其中 \(B,C\) 为常数矩阵，\(e_b,e_c\) 为常数向量，
则对每个 \(k\ne0\)，
\[
Bv_k=b^kv_k,\qquad Cv_k=c^kv_k.
\tag{2.2}
\]
这是**真正的共同特征向量**条件，不是广义特征向量条件。
而 \(v_0\) 只满足
\[
(I-B)v_0=e_b,\qquad (I-C)v_0=e_c.
\tag{2.3}
\]
无论这些常数怎样取，\(v_0\) 都是有理函数的一部分，
不能据此引入 \(\log z\) 等不属于 \(\mathbb C((z))\) 的项。

## 3. 先看一阶：唯一的 principal-parts 障碍

固定 pole order \(\ell\)，令 \(M\) 为 \(E(\mathbb C)\) 上有限支持函数的复向量空间。
pullback 算子仍为
\[
(T_af)(P)=a^{-\ell}f([a]P).
\]
现在使用
\[
S_b=T_b-\lambda_b,\qquad S_c=T_c-\lambda_c.
\]

R42 的有限支持证明原样成立：

- \(S_b\) 单射。若 \(T_bf=\lambda_bf\ne0\)，其有限非零支持满足
  \([b]^{-1}S=S\)，与 \(5|S|>|S|\) 矛盾。
- 选 \(c\)-primary 分裂并按深度 \(n\) 分层。
  \(S_b\) 保持每层。
- 不加标量的 pushforward \(P_c\) 与 \(S_b\) 交换；
  这是 \(b\) 在每个 \(c\)-fiber 上的双射。
- 在 \(M/S_bM\) 上，\(T_c\) 的最高层左逆常数仍为
  \[
  13c^{-\ell}\quad(n>0),\qquad12c^{-\ell}\quad(n=0).
  \]
  \(-\lambda_c\) 项不升层，故不能抵消这个最高层。
  因此 \(S_c\) 在 \(M/S_bM\) 上单射。

所以
\[
S_cu=S_bv
\quad\Longrightarrow\quad
u=S_bw,\ v=S_cw
\tag{3.1}
\]
具有真正有限支持的共同解 \(w\)。
各 pole order 直和后，结论对全部 principal parts 成立。

现在令 \(L_bF=h_b\)、\(L_cF=h_c\) 为有理函数。
它们满足
\[
L_ch_b=L_bh_c.
\tag{3.2}
\]
按 (3.1) 取共同 principal part \(w\)，记总 simple residue 为 \(a\)。
有理函数乘不变微分的总留数为零，因此
\[
(\bar b-\lambda_b)a=0,\qquad
(\bar c-\lambda_c)a=0.
\tag{3.3}
\]

如果不是 (1.4)，至少一个系数非零，故 \(a=0\)。
Mittag–Leffler 给一个 \(g\in\mathcal R\) 实现 \(w\)；
于是 \(L_b(F-g)\)、\(L_c(F-g)\) 为常数。
第 2 节逐系数比较给 (1.3) 或 (1.6)。

如果是 (1.4)，则 \(a\) 可以非零。
用 R42 的显式有限 \(\zeta\) 和导数公式实现 \(w\)，
得到一个
\[
g\in\mathcal R+a\zeta.
\]
其准周期增量为 \(a\eta(\lambda)\)。
由方格的
\[
\eta(b\lambda)=\bar b\,\eta(\lambda),\qquad
\eta(c\lambda)=\bar c\,\eta(\lambda),
\]
\(L_bg,L_cg\) 都是椭圆函数。
它们具有所需的 principal parts，因此 \(L_b(F-g),L_c(F-g)\) 为常数。
不存在整数 \(k\) 同时给 \(b^k=\bar b,c^k=\bar c\)，
故 \(F-g\) 为常数，得到 (1.5)。

这已经完整证明 \(r=s=1\)，包括常数和负 Laurent 权。

## 4. 高次只使用一个有限的 Jordan 向量

对一般 \(r,s\)，定义 \(rs\) 个分量
\[
F_{ij}=L_b^iL_c^jF,
\qquad 0\le i<r,\quad0\le j<s,
\]
并把它们组成列向量 \(\mathbf F\)。

令 \(N_b,N_c\) 为常数移位矩阵：
\[
(N_bv)_{ij}=
\begin{cases}
v_{i+1,j},&i<r-1,\\
0,&i=r-1,
\end{cases}
\qquad
(N_cv)_{ij}=
\begin{cases}
v_{i,j+1},&j<s-1,\\
0,&j=s-1.
\end{cases}
\]
它们幂零且交换。置
\[
B=\lambda_bI+N_b,\qquad C=\lambda_cI+N_c.
\tag{4.1}
\]
因为两 \(\lambda\ne0\)，\(B,C\) 可逆。
每个矩阵只具有对应的一个特征值 \(\lambda_b,\lambda_c\)。

定义边界向量
\[
(h_b)_{ij}=
\begin{cases}
0,&i<r-1,\\
L_c^jL_b^rF,&i=r-1,
\end{cases}
\]
\[
(h_c)_{ij}=
\begin{cases}
0,&j<s-1,\\
L_b^iL_c^sF,&j=s-1.
\end{cases}
\]
(1.1) 及有理函数域对各算子的稳定性说明
\(\mathbf h_b,\mathbf h_c\in\mathcal R^{rs}\)。
并且
\[
\sigma_b\mathbf F=B\mathbf F+\mathbf h_b,\qquad
\sigma_c\mathbf F=C\mathbf F+\mathbf h_c.
\tag{4.2}
\]

边界向量确实具有证明所需的相容式：
交换 \(\sigma_b,\sigma_c\) 并使用 \(BC=CB\)，得到
\[
\boxed{\quad
(\sigma_c-C)\mathbf h_b
=
(\sigma_b-B)\mathbf h_c.
\quad}
\tag{4.3}
\]
因此没有把各高次边界当作互不相关的有理右端。

## 5. 有限支持论证用于这个 Jordan 向量

在每个 pole order \(\ell\) 中，改用 \(M^{rs}\) 并置
\[
\mathcal S_b=T_bI-B,\qquad
\mathcal S_c=T_cI-C.
\]

\(\mathcal S_b\) 单射：
若 \(T_b\mathbf f=B\mathbf f\)，因为 \(B\) 可逆，
右端的非零支持等于 \(\mathbf f\) 的支持；
左端的非零支持是其全部 \(b\)-原像。
有限支持的度数矛盾与第 3 节相同。

\(c\)-primary 分层由坐标逐项给出。
\(B,C\) 只在线性坐标之间作用，不改变点或其深度。
此外
\[
P_c\mathcal S_b=\mathcal S_bP_c,
\]
因为 \(P_cT_b=T_bP_c\) 且 \(P_c\) 与常数矩阵 \(B\) 交换。
最高层仍完全来自 \(T_cI\)，所以其左逆仍是
\(13c^{-\ell}I\) 或 \(12c^{-\ell}I\)。
因此
\[
\mathcal S_c
\text{ 在 }M^{rs}/\mathcal S_bM^{rs}\text{ 上单射。}
\]
由 (4.3)，全部 principal parts 有一个共同有限原像
\[
\mathbf w,\qquad
\mathcal S_b\mathbf w=\operatorname{pp}(\mathbf h_b),\quad
\mathcal S_c\mathbf w=\operatorname{pp}(\mathbf h_c).
\tag{5.1}
\]

令 \(\mathbf a\) 是 \(\mathbf w\) 各分量的总 simple residue。
与标量式 (3.3) 相同，
\[
(\bar bI-B)\mathbf a=0,\qquad
(\bar cI-C)\mathbf a=0.
\tag{5.2}
\]
所以当至少一个 \(\lambda_a\ne\bar a\) 时，
相应矩阵可逆，迫使 \(\mathbf a=0\)。
当 \((\lambda_b,\lambda_c)=(\bar b,\bar c)\) 时，
(5.2) 要求
\[
N_b\mathbf a=N_c\mathbf a=0.
\tag{5.3}
\]

用各分量的有限 \(\zeta\) 和导数公式实现 \(\mathbf w\)，得到
\[
\mathbf g\in\mathcal R^{rs}+\mathbf a\,\zeta.
\tag{5.4}
\]
因 (5.2)，
\((\sigma_b-B)\mathbf g\)、\((\sigma_c-C)\mathbf g\) 的准周期全部消去，
故它们都是有理函数向量。
(5.1) 随后使
\[
\mathbf h_b-(\sigma_b-B)\mathbf g,\qquad
\mathbf h_c-(\sigma_c-C)\mathbf g
\]
成为常数向量。

## 6. Laurent 系数消去所有广义特征新项

置
\[
\mathbf G=\mathbf F-\mathbf g.
\]
它满足第 2 节的 (2.1)。
对每个 \(k\ne0\)，(2.2) 给出
\[
(B-b^kI)v_k=0,\qquad (C-c^kI)v_k=0.
\tag{6.1}
\]
如果没有整数 \(k\ne0\) 同时满足
\((\lambda_b,\lambda_c)=(b^k,c^k)\)，则所有这些 \(v_k\) 都为零。
如果存在，最多只有这一个权；而在该权，
\[
N_bv_k=N_cv_k=0.
\tag{6.2}
\]

对当前具体移位矩阵，
\[
\ker N_b\cap\ker N_c
=
\mathbb C e_{00}.
\tag{6.3}
\]
确实，\(N_bv=0\) 迫使所有 \(i\ge1\) 的分量为零；
\(N_cv=0\) 再迫使所有 \(j\ge1\) 的分量为零。
因此 (6.2) 只给原来的 \(F_{00}=F\) 增加 \(z^k\)，
而不出现 \(z^k\log z\)、更高 Jordan 项或额外权。

同理，反 CM 情形下 (5.3) 使
\(\mathbf a=a e_{00}\)。
所以 (5.4) 也只给 \(F\) 增加一个 \(\zeta\) 方向，
不会产生 \(\zeta^2\) 或其与 \(z\) 的乘积。

常数向量 \(v_0\) 完整保留在有理部分中。
取 \(\mathbf F\) 的 \((0,0)\) 分量，便得到第 1 节的全部分类。

## 7. Robert cocycle 的准确位置

标准 Robert 函数按本仓库规范具有
\[
\operatorname{div}\Theta_b
=
12\bigl(Nb[O]-[b]^*[O]\bigr).
\]
它的对数导数满足
\[
\delta\log\Theta_b
=
12\{Nb\,\zeta-b\,\zeta(bz)\}
=
-12b(\sigma_b-\bar b)\zeta.
\tag{7.1}
\]
因此 Robert 的两个反 CM 有理右端不是一个尚未辨认的共同原函数来源：
在当前标量设置下，R43 说明其全部非有理共同原函数部分恰为
\(\mathbb C\zeta\)，再加椭圆有理函数。

整数权例外也有明确含义：
它来自形式椭圆对数的幂 \(z^k=\log_E(t)^k\)。
这些例外的局部整性须分别检查；
分类没有把它们变成 R41 的 \(b_j^k-1\) 共同浅深度对象。
例如反 CM 的首个惰性 Frobenius 共振仍为
\[
b^p\equiv\bar b\pmod p,\qquad c^p\equiv\bar c\pmod p,
\]
这与无 twist 的共同阶数条件不同。

本篇也没有覆盖所有“使用两个乘子”的方法。
真正的非线性等变、在额外变量上作用的系统、非有理右端，
以及非恒定有理矩阵都不属于 (1.1) 的标量幂假设。
本题的无穷多个 \(p\) 结论仍需新的比较或新的兼容对象。

### 依赖与核查范围

本篇唯一较长的支持论证是 R42 已完整证明的
\(c\)-primary 分层和有限支持左逆。
第 3、5 节重新核查了 twist 与有限 Jordan 向量所需的全部改动，
尤其边界层的 \(13-1=12\) 因子、矩阵相容式和真正特征向量条件。
没有将 de Shalit 文献未展开的 CM 推广当作外部定理。
