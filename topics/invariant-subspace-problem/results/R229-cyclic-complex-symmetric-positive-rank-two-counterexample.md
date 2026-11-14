# R229：循环复对称交换代数上不能将每个正泛函降成一个正向量态

日期：2026-11-13（UTC+8）。作者：Astra-ISP-1cf8c51d。
状态：**已证明，中间结论。** 本稿在执行环境重置后从保全的完整论证重建；所有矩阵和行列式均为精确等式。

## 1. 要排除的命题及结论

即使一个有限维算子循环、其交换代数交换且全部元素对同一共轭复对称，也不能推出：该代数上每个正泛函都由一个正向量态表示。

下面给出一个明确的 $5\times5$ 循环复对称矩阵 $A_0$ 和一个正迹一密度 $\rho$，使
$$
\varphi(F)=\operatorname{Tr}(\rho F),\qquad F\in\{A_0\}',
$$
的最小**正向量和表示秩**恰为二。即存在 $f_1,f_2$ 使
$$
\varphi(F)=\langle Ff_1,f_1\rangle+\langle Ff_2,f_2\rangle,
\tag{1.1}
$$
但不存在 $h$ 使 $\varphi(F)=\langle Fh,h\rangle$ 对整个交换代数成立。内积第一变量线性。

这是对指定泛函的表示秩陈述。它不构造任何满足 $\varphi(S\mathcal A)=0$ 的非零主理想分离见证，不把有限维例子当作原 Haar 模型的反例，也不改变 R228A 关于最小分离秩的结论。

## 2. 一个明确的循环复对称矩阵

令 $C_0$ 为 $\mathbb C^5$ 上逐坐标共轭，置
$$
H_0=\operatorname{diag}(1,1,1,0,0),\qquad
G_0=
\begin{pmatrix}
0&0&0&1&1\\
0&1&0&1&2\\
0&0&2&1&3\\
1&1&1&0&0\\
1&2&3&0&1
\end{pmatrix},\qquad A_0=H_0+iG_0.
\tag{2.1}
$$
两实矩阵对称，故 $A_0^t=A_0$、$C_0A_0^*C_0=A_0$。第一标准基向量的 Krylov 矩阵为
$$
\begin{pmatrix}
1&1&-1&-3-i&25-2i\\
0&0&-3&-6-5i&47-13i\\
0&0&-4&-8-11i&82-30i\\
0&i&i&-8i&17-17i\\
0&i&-1+i&-1-20i&64-40i
\end{pmatrix}.
\tag{2.2}
$$
其行列式恰为 $230-92i\ne0$。所以 $e_1$ 对 $A_0$ 循环，最小多项式次数为五。

对任意 $F\in\{A_0\}'$，由循环性选唯一次数小于五的多项式 $p$，使 $Fe_1=p(A_0)e_1$。对 $0\le k\le4$，交换性给
$$
FA_0^ke_1=A_0^kFe_1=p(A_0)A_0^ke_1.
$$
这些向量为基，故 $F=p(A_0)$。因此
$$
\{A_0\}'=\mathbb C[A_0]
\tag{2.3}
$$
是交换代数，而且每个元素都为复对称矩阵。

## 3. 三维支撑上的全部实对称测试

令 $E=\operatorname{span}\{e_1,e_2,e_3\}$，$P=P_E$，置 $\rho=P/3$。若存在一个正向量态表示 $\varphi$，以 $F=I$ 测试得 $\|h\|=1$；再取 $F=A_0$ 的实部，得到
$$
\langle H_0h,h\rangle
=\operatorname{Re}\operatorname{Tr}(\rho A_0)=1.
$$
因 $H_0=P$ 为正交投影，必须 $h\in E$。

在 $E$ 上记
$$
R_k=\operatorname{Re}(PA_0^k|_E),\qquad
J_k=\operatorname{Im}(PA_0^k|_E),
$$
这里是矩阵逐项实、虚部；它们均为实对称矩阵，所以也正好给相应二次型的实、虚部。直接相乘得
$$
R_0=I_3,\qquad J_1=\operatorname{diag}(0,1,2),
$$
$$
R_2=\begin{pmatrix}-1&-3&-4\\-3&-5&-7\\-4&-7&-13\end{pmatrix},\qquad
R_3=\begin{pmatrix}-3&-6&-8\\-6&-12&-14\\-8&-14&-31\end{pmatrix},
$$
$$
J_3=\begin{pmatrix}-1&-5&-11\\-5&-12&-27\\-11&-27&-51\end{pmatrix},\qquad
R_4=\begin{pmatrix}25&47&82\\47&91&169\\82&169&293\end{pmatrix}.
\tag{3.1}
$$
这些六个矩阵张成 $\operatorname{Sym}_3(\mathbb R)$。以下给出精确检验，不依赖数值秩判定。

首先
$$
D=2R_2-R_3-I_3=\operatorname{diag}(0,1,4),
$$
故 $I_3,J_1,D$ 张成全部对角矩阵：它们的对角坐标矩阵的行列式为二。
其次
$$
L=2I_3-3R_2+R_3
=\begin{pmatrix}2&3&4\\3&5&7\\4&7&10\end{pmatrix}.
$$
$L,J_3,R_4$ 的三个非对角坐标 $(12,13,23)$ 组成矩阵
$$
\begin{pmatrix}
3&-5&47\\
4&-11&82\\
7&-27&169
\end{pmatrix},
$$
其行列式为 $118\ne0$。模去已得到的全部对角矩阵，这三项又张成全部非对角部分，所述张成性成立。

## 4. 排除单个正向量态

设 $h=a+ib\in E$，其中 $a,b\in\mathbb R^3$。对任意实对称 $K$，交叉项相消，故
$$
\langle Kh,h\rangle
=a^tKa+b^tKb
=\operatorname{Tr}\bigl(K(aa^t+bb^t)\bigr).
\tag{4.1}
$$
如果 $h$ 与 $\rho$ 在 $I,A_0,A_0^2,A_0^3,A_0^4$ 上给相同泛函，那么取实、虚部并使用 §3 的张成性，必有
$$
\operatorname{Tr}\bigl(K(aa^t+bb^t)\bigr)
=\frac13\operatorname{Tr}K
\quad\text{对每个 }K\in\operatorname{Sym}_3(\mathbb R).
$$
实对称矩阵上的迹配对非退化，因此
$$
aa^t+bb^t=\frac13I_3.
\tag{4.2}
$$
左边秩至多二，右边秩为三，矛盾。故不存在单个正向量态表示。

## 5. 二个向量足够，并得非凸联合数值域

取
$$
f_1=\frac{e_1+ie_2}{\sqrt3},\qquad f_2=\frac{e_3}{\sqrt3}.
$$
对任意复对称矩阵 $F$，因 $F_{12}=F_{21}$，直接展开得到
$$
\langle Ff_1,f_1\rangle
=\frac13(F_{11}+F_{22}),\qquad
\langle Ff_2,f_2\rangle=\frac13F_{33}.
$$
这证明 (1.1)，与 §4 合起来给最小正表示秩准确为二。

再令 $v_1=(e_1+ie_2)/\sqrt2$、$v_2=e_3$。两者单位长度，且对 $k=1,2,3,4$，
$$
\operatorname{Tr}(\rho A_0^k)
=\frac23\langle A_0^kv_1,v_1\rangle
+\frac13\langle A_0^kv_2,v_2\rangle.
$$
§4 证明这个凸组合不能由任何单位向量实现。因此四元组
$(A_0,A_0^2,A_0^3,A_0^4)$ 的联合数值域不是凸集，尽管四项交换且共同复对称。

## 6. 对原问题的准确作用范围

本例排除“交换＋循环＋共同复对称就能把任意正有限秩泛函降为正秩一”的抽象捷径。R228 的配对降秩界在此实例中确实达到二，不能继续免费下降。

这里没有一个指定非零 $S$ 及主理想湮灭方程，因此不能用它否定原 Haar 模型上的一般正常见证排除，也不能与 R228A 的最小正/一般分离秩等价混淆。由于 $e_1$ 循环，代数上任意线性泛函仍可写成某个 $\langle Fe_1,g\rangle$；该表示不要求两个向量相同，完全不与本稿矛盾。

文献背景：T. C. Lau、C.-K. Li、Y.-T. Poon，*The joint numerical range of commuting matrices*，Studia Mathematica 267 (2022), 241–259，Example 3.1，印刷页244–245（作者PDF页4–5），DOI [10.4064/sm200622-31-5](https://doi.org/10.4064/sm200622-31-5)，[作者全文](https://faculty.sites.iastate.edu/ytpoon/files/inline-files/doiA-sm200622-31-5.pdf)。该文给交换矩阵联合数值域的相关反例；本稿没有假定其例子共同复对称，§2–5 的共同复对称例子和证明均独立给出。
