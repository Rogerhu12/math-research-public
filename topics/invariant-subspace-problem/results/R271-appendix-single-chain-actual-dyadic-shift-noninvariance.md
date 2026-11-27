# R271 附录：单链子空间确实不被任何原 dyadic 移位或单个位算子保持

日期：2026-11-27（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127 / stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

本稿用[完整交织及有界表示](R271-appendix-single-chain-complete-intertwiners-and-bounded-commutant-representation.md)中的同一个实际 $U,T_U,\rho$。它支付一个此前明确未定的范围：虽 $U$ 是原慢算子 $T=T_N$ 或 $T_Y$ 的真闭不变子空间，却不是原 $B$ 的不变子空间。完整 Y 型 Cayley 级数在系数比较中保留。

## 1. 结论

对每个整数 $q\ge0$，
$$
\boxed{B^{2^q}U\not\subset U.}
\tag{1.1}
$$
因而每个原单个位算子均不保持该 $U$：
$$
\mathsf N_qU\not\subset U,\qquad
\mathsf Y_qU\not\subset U,\qquad
\mathsf N_q=B^{2^q}/d_q,\quad
\mathsf Y_q=\mathsf N_q(I+\mathsf N_q)^{-1}.
\tag{1.2}
$$
这不是新的普通 ISP 结论：该 $U$ 的不变性只针对相应慢算子 $T$。

## 2. 若 B 保 U，实际有界表示会产生三次费用的形式反解

设反面 $BU\subset U$，令 $D=B|_U$。原 $B,T$ 交换，故 $D$ 与 $T_U$ 交换。前稿给实际范数收敛
$$
\rho(D)=g(B)=\sum_{n\ge0}g_nB^n,\qquad
|g_n|\le K e^{A n^3}
\tag{2.1}
$$
的固定有限常数 $K\ge1,A\ge0$。又 $g_0=\langle Be_0,e_0\rangle=0$。

写原两个形式符号
$$
F_N(z)=\sum_{i\ge0}a_i\frac{z^{2^i}}{d_i},
\qquad
F_Y(z)=\sum_{i\ge0}a_i
\frac{z^{2^i}/d_i}{1+z^{2^i}/d_i},
\qquad a_i=(i+1)^{-2}.
\tag{2.2}
$$
原 $T$ 的定义级数按算子范数绝对收敛。限制到 $U$ 后仍成立。Y 型的逆也保持 $U$，因为相应 $\mathsf N_i$ 拟幂零，其实际逆是范数收敛的幂级数。将有界保单位代数同态 $\rho$ 作用到这些实际身份，利用 $\rho(T_U)=B$，得到
$$
F_N(g(B))=B\quad\hbox{或}\quad F_Y(g(B))=B.
\tag{2.3}
$$
这里的范数收敛是由原身份和有界 $\rho$ 支付；未声称任意满足 (2.1) 的 $g$ 都可以在全 $H$ 任意代入 $F$。

对每个固定整数坐标，普通 $B$ 幂系数的读取是算子范数连续的；$g_0=0$ 也保证每个有限次数的形式组合仅含有限项。因此 (2.3) 给真正的形式身份
$$
F_\bullet(g(z))=z.
\tag{2.4}
$$
原首项是 $a_0/d_0=e^{20}$，故
$$
g_1=d_0=\alpha_0=e^{-20}.
\tag{2.5}
$$

## 3. 两型共同的完整系数比较

记
$$
\Lambda_i=-\log d_i
=100\,16^i-105\,8^i+(150i+25)2^i.
$$
固定 $j\ge1$，置 $n=2^j$，并记 $F_{<j}$ 为 (2.2) 中所有 $i<j$ 的完整和。定义
$$
H_j=\max_{0\le i<j}\frac{\Lambda_i}{2^i}
\le100\,8^{j-1}+150j+25
=\frac{25}{2}n^3+150j+25.
\tag{3.1}
$$

对 N 型，$F_{<j}$ 的系数只在有限个 dyadic 次数非零；对 Y 型，保留所有几何幂后，
每个 $m\ge1$ 的系数是所有满足 $2^i\mid m$ 的 $i<j$ 项之和，其单项绝对值为
$a_i d_i^{-m/2^i}$。因此两型都满足
$$
\bigl|[z^m]F_{<j}(z)\bigr|
\le\sum_{i<j}a_i e^{mH_j}
\le2e^{mH_j}.
\tag{3.2}
$$
该界包括 Y 型低位 Cayley 逆在任意高幂 $m$ 的全部贡献。

对 $1\le m\le n$，将 $n$ 写成 $m$ 个正整数之和并用 (2.1)，得到
$$
\bigl|[z^n]g(z)^m\bigr|
\le {n-1\choose m-1}K^m
\exp\!\left(A\max_{\substack{r_1+\cdots+r_m=n\\r_i\ge1}}
\sum_i r_i^3\right)
\le {n-1\choose m-1}K^n e^{An^3}.
\tag{3.3}
$$
所以完整低位余项
$$
R_j:=[z^n]F_{<j}(g(z))
$$
满足
$$
\begin{aligned}
|R_j|
&\le 2^n K^n e^{An^3+nH_j}\\
&\le
\exp\!\left[
\frac{25}{2}n^4+An^3+n\bigl(150j+25+\log(2K)\bigr)
\right].
\end{aligned}
\tag{3.4}
$$

在第 $n=2^j$ 阶，所有 $i>j$ 均无贡献；第 $j$ 位只有一次幂有贡献。Y 型该位的第二及更高 Cayley 幂的最低次数已是 $2n$。所以两型的准确系数都是
$$
[z^n]F_\bullet(g(z))
=\frac{a_jg_1^n}{d_j}+R_j.
\tag{3.5}
$$
由 (2.5)，主项的绝对值对数为
$$
\log\left|\frac{a_jg_1^n}{d_j}\right|
=100n^4-105n^3+(150j+5)n-2\log(j+1).
\tag{3.6}
$$
(3.6) 减去 (3.4) 的对数上界至少为
$$
\frac{175}{2}n^4-(105+A)n^3
-\bigl(20+\log(2K)\bigr)n-2\log(j+1),
\tag{3.7}
$$
它随 $j\to\infty$ 趋于正无穷。因此所有充分大 $j$ 的主项严格大于完整低位余项，(3.5) 不可能为零。这与 (2.4) 在 $n\ge2$ 的系数为零矛盾。

故 $BU\not\subset U$，两种原模型同时成立。证明没有依赖相位同号，也没有把 Y 型改成 N 型；全部可能抵消由 (3.2)–(3.7) 一次支付。

## 4. 每个 dyadic 幂也不能保持 U

若某个 $q\ge1$ 满足 $B^{2^q}U\subset U$，则所有 $i\ge q$ 的原 $\mathsf N_i$、$\mathsf Y_i$ 及其范数收敛尾和均保持 $U$。$T$ 本身保持 $U$，故有限低位部分
$$
H_q(B)=\sum_{i<q}a_i\frac{B^{2^i}}{d_i}
\quad\hbox{或}\quad
H_q(B)=\sum_{i<q}a_i
\frac{B^{2^i}/d_i}{1+B^{2^i}/d_i}
\tag{4.1}
$$
也保持 $U$。

$H_q(z)$ 在零附近解析，$H_q(0)=0$ 且
$H_q'(0)=e^{20}\ne0$。其局部解析反函数 $h_q$ 满足
$h_q(H_q(z))=z$。原 $B$ 拟幂零，故 $H_q(B)$ 亦拟幂零；$h_q$ 的零点 Taylor 级数可在 $H_q(B)$ 上按算子范数求和，函数演算给
$$
h_q(H_q(B))=B.
\tag{4.2}
$$
准确地，虽 $h_q$ 只有某个正收敛半径，拟幂零性仍使
$\|H_q(B)^m\|^{1/m}\to0$，所以该 Taylor 级数范数收敛。
由闭子空间 $U$ 对 $H_q(B)$ 的不变性，(4.2) 迫 $BU\subset U$，与第三节矛盾。这证明 (1.1)。

最后，$\mathsf N_q$ 只是 $B^{2^q}$ 的非零标量倍数；若 $\mathsf Y_q$ 保持 $U$，其拟幂零性及
$$
\mathsf N_q=\mathsf Y_q(I-\mathsf Y_q)^{-1}
$$
又使 $\mathsf N_q$ 保持 $U$，同样矛盾。故 (1.2) 成立。

本稿关闭的是新单链子空间对原移位、dyadic 幂和各单个位算子的实际不变性问题。它不改变原 $M,N,W$ 的范围目标，也没有支付真正 Green 来源的循环残量或 $N=M$。
