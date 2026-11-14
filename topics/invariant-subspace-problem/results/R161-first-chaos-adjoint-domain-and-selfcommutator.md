# R161：第一阶乘子的通常伴随同域、有界自交换子形式与共振压缩约束

日期：2026-11-12（UTC）。作者：critical_kernel。
状态：完整证明；核心进位恒等式、常数、双图核心及压缩公式已由 l2_moments 独立逐式核验。主会话预留 R161。
本稿给慢平方共振的一个新的必要条件，不宣称已排除其未知核。

## 1. 设置与结论

令
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a\in\ell^2,
$$
并令 $X=X_u$ 为 R125 的实际第一阶闭乘子。
有限柱空间 $\mathscr D$ 是 $X$ 及 $X^*$ 的图核心，
而
$$
X_n=a_*I+\sum_{j<n}a_jV_j,\qquad
V_j=(I-N_j)(I+N_j)^{-1},
$$
在 $\mathscr D$ 上分别满足
$$
X_nf\to Xf,\qquad X_n^*f\to X^*f.
\tag{1.1}
$$
第二个极限也可由 $X_n^*=CX_nC$、$X^*=CXC$ 以及 $C\mathscr D=\mathscr D$ 直接得到。

记
$$
S_j=I-2E_j,\qquad
\eta_*=\sup_j\eta_j<1,\qquad
\varepsilon_{\rm carry}
=144\eta_*+\frac{1296\eta_*}{1-\eta_*}.
\tag{1.2}
$$
本模型 $\eta_j\le e^{-770\,16^j}$，故该常数极小。
定义实际连续实函数
$$
r_a(y)=\sum_{j\ge0}|a_j|^2\chi_j(y).
\tag{1.3}
$$
因 $a\in\ell^2$，该级数绝对一致收敛。

**定理1.1。** 存在有界自伴算子 $C_a$，使
$$
\boxed{
\operatorname{Dom}X=\operatorname{Dom}X^*,\qquad
\|Xf\|^2-\|X^*f\|^2=\langle C_af,f\rangle
\quad(f\in\operatorname{Dom}X).
}
\tag{1.4}
$$
此外
$$
\boxed{
C_a=4M_{r_a}+K_a,\qquad
K_a=K_a^*,\qquad
\|K_a\|\le\varepsilon_{\rm carry}\|a\|_2^2.
}
\tag{1.5}
$$
特别
$$
\|C_a\|\le(4+\varepsilon_{\rm carry})\|a\|_2^2.
\tag{1.6}
$$

这里 $C_a$ 的符号对应 $X^*X-XX^*$：
它是两个图二次型之差的有界延拓。
本稿没有据此宣称未经另证的
$\operatorname{Dom}(X^*X)=\operatorname{Dom}(XX^*)$，
也没有把未共同定义的二阶自然算子差擅自当成全域有界算子。

若某个闭 $A$ 不变空间 $M$ 满足
$$
M\subseteq\operatorname{Dom}X,\qquad X|_M=Y_M\in B(M),
\tag{1.7}
$$
则 $X^*|_M:M\to H$ 亦有界，且相对 $H=M\oplus M^\perp$，
$X$ 具有有界非对角块。该块的精确正性约束见 §6。

## 2. 不同位的真实进位交换子

取正权 $\alpha_j$，使
$$
\alpha_{j+1}/\alpha_j=\eta_j,\qquad A=\alpha_0N_0.
$$
只使用其比值
$$
r_{ij}=\frac{\alpha_j}{\alpha_i}
=\prod_{\nu=i}^{j-1}\eta_\nu
\quad(i<j).
\tag{2.1}
$$

对 $i<j$，逐次展开
$N_i=E_i+\eta_iE_i^*N_{i+1}$，
得到精确算子恒等式
$$
\boxed{
N_i=N_i^{[j]}
+r_{ij}(E_i^*E_{i+1}^*\cdots E_{j-1}^*)N_j.
}
\tag{2.2}
$$
$N_i^{[j]}$ 只作用于低 $j$ 位；
它及所有列出的低位矩阵都与 $N_j,N_j^*$ 交换。
取伴随并交换，于是
$$
\boxed{
[N_i^*,N_j]
=r_{ij}(E_iE_{i+1}\cdots E_{j-1})[N_j^*,N_j].
}
\tag{2.3}
$$
由 $\|N_j\|=1$，
$$
\|[N_i^*,N_j]\|\le2r_{ij}.
\tag{2.4}
$$
对 $i>j$ 取伴随得到对称的界；
对 $i=j$，仍可使用上界2。

因为
$$
V_i=2(I+N_i)^{-1}-I,\qquad
\|(I+N_i)^{-1}\|<3,
$$
一般逆交换子恒等式
$$
[P^{-1},Q^{-1}]
=P^{-1}Q^{-1}[P,Q]Q^{-1}P^{-1}
$$
用于 $P=I+N_i^*$、$Q=I+N_j$，给
$$
\boxed{
\|[V_i^*,V_j]\|
\le648\,\frac{\alpha_{\max(i,j)}}{\alpha_{\min(i,j)}}
\quad(i\ne j).
}
\tag{2.5}
$$
常数为 $4\cdot3^4\cdot2$。
整个证明保留了真实的进位尾，没有把不同位实际算子与伴随假定为独立张量。

## 3. 对角纯项与离散 Schur 估计

R130 的实际差界给
$$
\|V_j-S_j\|\le8\eta_j,\qquad
\|V_j\|\le6,\quad\|S_j\|\le3.
$$
所以
$$
\begin{split}
\|[V_j^*,V_j]-[S_j^*,S_j]\|
&\le2(\|V_j\|+\|S_j\|)\|V_j-S_j\|\\
&\le144\eta_j.
\end{split}
\tag{3.1}
$$

在物理两点基中
$$
S_j=\begin{pmatrix}1&0\\-2&1\end{pmatrix}.
$$
直接计算
$$
\boxed{
[S_j^*,S_j]
=4\begin{pmatrix}1&0\\0&-1\end{pmatrix}
=4M_{\chi_j}.
}
\tag{3.2}
$$
这里 $\chi_j$ 是物理符号函数，不是数算子占据投影。

置
$$
R_{ij}=
\begin{cases}
\alpha_{\max(i,j)}/\alpha_{\min(i,j)},&i\ne j,\\
0,&i=j.
\end{cases}
$$
由 (2.1)，$R_{ij}\le\eta_*^{|i-j|}$，故每行和、每列和都不超过
$2\eta_* /(1-\eta_*)$。
离散 Schur 估计给
$$
\boxed{
\sum_{i\ne j}|a_i|\,|a_j|R_{ij}
\le\frac{2\eta_*}{1-\eta_*}\|a\|_2^2.
}
\tag{3.3}
$$

对有限和 $X_n$，常数项不影响交换子，
$$
C_{a,n}:=X_n^*X_n-X_nX_n^*
=\sum_{i,j<n}\overline{a_i}a_j[V_i^*,V_j].
\tag{3.4}
$$
其对角部分由 (3.1)—(3.2) 分成
$4M_{\sum_{j<n}|a_j|^2\chi_j}$ 与范数不超过
$144\eta_*\|a\|_2^2$ 的误差。
非对角部分由 (2.5)、(3.3) 控制为
$1296\eta_*\|a\|_2^2/(1-\eta_*)$。

这些双线性估计同时给任意两个 $\ell^2$ 系数列的连续界。
因此将 $a$ 换为有限截断 $a^{(n)}$ 后，
$C_{a,n}$ 按算子范数 Cauchy。
其极限 $C_a$ 自伴，且满足 (1.5)—(1.6)。
这也证明 $K_a$ 是有界自伴算子，而不是形式无穷交换子。

## 4. 两个图核心严格推出通常伴随同域

对 $f\in\mathscr D$，有限算子恒等式为
$$
\|X_nf\|^2-\|X_n^*f\|^2
=\langle C_{a,n}f,f\rangle.
$$
使用 (1.1) 以及 $C_{a,n}\to C_a$ 的范数收敛，得到
$$
\|Xf\|^2-\|X^*f\|^2
=\langle C_af,f\rangle
\quad(f\in\mathscr D).
\tag{4.1}
$$
于是两个图范数在同一个 $\mathscr D$ 上等价：
$$
\|X^*f\|^2\le\|Xf\|^2+\|C_a\|\|f\|^2,
$$
以及交换 $X,X^*$ 后的反向界。

给 $f\in\operatorname{Dom}X$，
取 $\mathscr D$ 中 $f_n\to f$ 且 $Xf_n\to Xf$。
将上述界用于 $f_n-f_m$，可知 $X^*f_n$ Cauchy。
由 $X^*$ 闭，$f\in\operatorname{Dom}X^*$。
反向使用 $\mathscr D$ 是 $X^*$ 的图核心，同样给
$\operatorname{Dom}X^*\subseteq\operatorname{Dom}X$。
这证明真正的域相等。

再用图逼近取极限，(4.1) 延到共同完整域，得到 (1.4)。
极化后亦有
$$
\langle Xf,Xg\rangle-\langle X^*f,X^*g\rangle
=\langle C_af,g\rangle
\quad(f,g\in\operatorname{Dom}X).
\tag{4.2}
$$
这里内积取第一变量线性。
没有通过只在稠密核心上的等式直接跳到最大伴随域。

## 5. 附带的真实有界交换子与高位衰减

这节给进一步可重复使用的定量接口，不用于声称核已排除。

由 $V_i^*=2(I+N_i^*)^{-1}-I$ 及 (2.4)，
$$
\|[V_i^*,N_j]\|
\le36\,\widetilde R_{ij},
\quad
\widetilde R_{ij}=
\begin{cases}
R_{ij},&i\ne j,\\1,&i=j.
\end{cases}
\tag{5.1}
$$
所以
$$
D_j:=\sum_i\overline{a_i}[V_i^*,N_j]
$$
范数绝对收敛，且
$$
\|D_j\|\le36\sum_i|a_i|\widetilde R_{ij}.
\tag{5.2}
$$
离散 Schur 估计给
$$
\boxed{
\left(\sum_j\|D_j\|^2\right)^{1/2}
\le36\,\frac{1+\eta_*}{1-\eta_*}\|a\|_2.
}
\tag{5.3}
$$
特别 $\|D_j\|\to0$。

这是实际域恒等式
$$
\boxed{
N_j\operatorname{Dom}X^*\subseteq\operatorname{Dom}X^*,
\qquad X^*N_jf-N_jX^*f=D_jf.
}
\tag{5.4}
$$
可直接用 §4 的同域及 R125 的域保持先知左侧有定义；
为不依赖有限部分在任意输入上的收敛，也可从核心弱式验证：
对 $f,g\in\mathscr D$，
$$
\langle N_jf,X_ng\rangle-\langle N_jX_n^*f,g\rangle
=\left\langle\sum_{i<n}\overline{a_i}[V_i^*,N_j]f,g\right\rangle.
$$
各项取极限，$g$ 的 $X$ 图核心判据给
$X^*N_jf=N_jX^*f+D_jf$。
随后对任意 $f\in\operatorname{Dom}X^*$ 作图核心逼近，用闭性得到 (5.4)。

特别 $A=\alpha_0N_0$ 给 $[X^*,A]=\alpha_0D_0$ 有界。
也可用真实头尾展开直接得
$$
\|[V_i^*,A]\|\le36\alpha_i,
\qquad
\boxed{\|[X^*,A]\|\le36\sum_i|a_i|\alpha_i
\le36\|a\|_2\|\alpha\|_2.}
\tag{5.5}
$$
没有说 $X^*$ 与 $A$ 交换；
(5.4)—(5.5) 记录的正是其真实有界交换子。

## 6. 有界不变限制的准确块矩阵

设 $M$ 满足 (1.7)，并令 $P$ 为正交投影到 $M$。
由 (1.4)，对 $f\in M$，
$$
\|X^*f\|^2
\le\|Y_Mf\|^2+\|C_a\|\|f\|^2.
$$
因此
$$
\boxed{
X^*|_M:M\longrightarrow H\text{ 有界},\qquad
\|X^*|_M\|\le(\|Y_M\|^2+\|C_a\|)^{1/2}.
}
\tag{6.1}
$$

因为 $M\subseteq\operatorname{Dom}X$，
$P$ 保持 $\operatorname{Dom}X$，
$$
XP=Y_MP
$$
在全空间有界。
同时 $PX$ 在原域上等于有界算子 $(X^*P)^*$ 的限制。
所以 $[X,P]$ 在 $\operatorname{Dom}X$ 上有一个实际有界延拓。

令
$$
\mathscr D_2=\operatorname{Dom}X\cap M^\perp,\qquad
Z=(I-P)X|_{\mathscr D_2}.
$$
则
$$
\operatorname{Dom}X=M\oplus\mathscr D_2.
$$
$\mathscr D_2$ 在 $M^\perp$ 稠密，且 $Z$ 闭：
若 $f_n\to f$、$Zf_n\to g$，下面的有界非对角块使
$Xf_n$ 也收敛，故由 $X$ 闭得到结论。

定义
$$
B=PX|_{\mathscr D_2},
$$
并使用其来自 $(X^*P)^*$ 的有界延拓到 $M^\perp$。
由于 $X(M)\subseteq M$，精确块式为
$$
\boxed{
X=
\begin{pmatrix}
Y_M&B\\0&Z
\end{pmatrix},
\qquad
\operatorname{Dom}X=M\oplus\operatorname{Dom}Z,
\quad B\in B(M^\perp,M).
}
\tag{6.2}
$$
其伴随是通常的闭块伴随，特别对 $f\in M$，
$$
X^*f=Y_M^*f\oplus B^*f.
\tag{6.3}
$$

把 (6.3) 代入 (1.4)，对全部 $f\in M$ 有
$$
\langle
(Y_M^*Y_M-Y_MY_M^*-BB^*)f,f\rangle
=\langle C_af,f\rangle.
$$
极化得到严格的有界算子等式
$$
\boxed{
BB^*
=Y_M^*Y_M-Y_MY_M^*-P C_a|_M
\ \ge0.
}
\tag{6.4}
$$
(6.4) 的自交换子符号与 (1.4) 一致。
这里 $Y_M^*$ 是限制算子在 $M$ 内的通常伴随；
它不被误写成 $Y^*|_M$，也不要求 $M$ 被原共轭 $C$ 保持。

## 7. 用于慢平方共振核

R144 的共振附注已证明：对最低非零第一系数 $a=a_{j_0}$，
令
$$
B_2=\sum_j a_j^2(I-V_j^2),\qquad
Y=(a^2I-B_2)^{1/2},\qquad\chi(Y)=a,
$$
则
$$
\ker X_{u^2-a^2}
=\ker(X-Y)=:M.
\tag{7.1}
$$
而且
$$
M\subseteq\bigcap_{n\ge1}\operatorname{Dom}X^n,\qquad
X^n|_M=Y^n|_M.
\tag{7.2}
$$
因此 (1.7) 对 $Y_M=Y|_M$ 确实成立。

本稿给这一个可能核新增了：
$$
M\subseteq\operatorname{Dom}X^*,\qquad
\|X^*|_M\|<\infty,
\tag{7.3}
$$
及由实际权决定的必要压缩不等式
$$
\boxed{
Y_M^*Y_M-Y_MY_M^*
-4P M_{r_a}|_M-PK_a|_M
=BB^*\ge0.
}
\tag{7.4}
$$
$K_a$ 的完整定量界是 (1.5)，而 $r_a$ 是 (1.3) 的真实连续乘法符号。
这比只知道 $X|_M$ 有界更强，也不来自重复同一个 gauge 的幂配对。

但是 $P M_{r_a}|_M$ 不等同于在某个未知支撑集上的点态乘法。
$M$ 的总本质支撑全测，仍不足以断言这个压缩具有某个正谱点，
更不能由 $r_a$ 在某处为正就把 (7.4) 当成矛盾。
同样，全空间 $C$ 自伴性不能自动下传为 $Y_M$ 的 $C$ 自伴性。

## 8. 仍未闭合的步骤

以上证明全部适用于任意复杂 $\ell^2$ 第一系数；
不要求 $\ell^1$、统一相位或快尾。
它没有证明一般第一阶的全部不变限制像稠密，也没有证明慢平方共振核为零。

若要从 (7.4) 继续排核，必须使用实际 $A$ 不变性来证明足够强的压缩符号或块结构约束。
单独的有界自交换子形式、共同通常伴随域、全空间稠密像和全本质支撑都没有提供这一最后结论。
完整 ISP 保持开放。


## 附录 A. 有界自交换子形式排除图核心上的无界闭平方根

本附录是一个独立的闭算子引理，给 R143 的无界 head 商提供明确的充分障碍。
它不声称该 head 商已经继承 R161 对第一阶乘子的估计。

**引理 A.1。** 设 $J$ 是稠密定义的闭算子，满足
$$
\operatorname{Dom}J=\operatorname{Dom}J^*,
$$
并存在有界自伴 $C_J$，使
$$
\|Jv\|^2-\|J^*v\|^2=\langle C_Jv,v\rangle
\quad(v\in\operatorname{Dom}J).
\tag{A.1}
$$
设 $\mathscr E$ 是 $J$ 的一个图核心，且
$$
\mathscr E\subseteq\operatorname{Dom}J^2,\qquad
\|J^2x\|\le K\|x\|\quad(x\in\mathscr E)
\tag{A.2}
$$
对某个有限 $K\ge0$ 成立。
则 $J$ 必为全域有界算子，并且
$$
\boxed{
\|J\|^2\le
\frac{\|C_J\|+\sqrt{\|C_J\|^2+4K^2}}2.
}
\tag{A.3}
$$

**证明。** 取 $x\in\mathscr E$。
因 $x\in\operatorname{Dom}J^2$，$Jx\in\operatorname{Dom}J$；
共同域又保证 $Jx\in\operatorname{Dom}J^*$，所以 $J^*Jx$ 真实有定义。
置
$$
a=\|Jx\|^2,\qquad b=\|x\|^2,\qquad c=\|C_J\|.
$$
在 (A.1) 中取 $v=Jx$，有
$$
\|J^*Jx\|^2
=\|J^2x\|^2-\langle C_JJx,Jx\rangle
\le K^2b+ca.
$$
另一方面，通常伴随关系及 Cauchy–Schwarz 给
$$
a^2=|\langle J^*Jx,x\rangle|^2
\le b\,\|J^*Jx\|^2
\le K^2b^2+cab.
\tag{A.4}
$$
当 $x\ne0$，令 $t=a/b$，得到
$t^2-ct-K^2\le0$，所以
$$
\|Jx\|^2\le
\frac{c+\sqrt{c^2+4K^2}}2\,\|x\|^2.
$$
$x=0$ 时也成立。

由于 $\mathscr E$ 是 $J$ 的图核心，对任意
$x\in\operatorname{Dom}J$ 取图逼近后，上界延到完整定义域。
$J$ 在其稠密定义域上有统一的通常范数界；
闭性遂迫定义域为整个 Hilbert 空间。
得到 (A.3)。证毕。

### A.1 为什么只需要在图核心上控制平方

(A.2) 不要求预先知道
$\operatorname{Dom}J^2=\operatorname{Dom}J$，
也不要求 $J^2$ 已经等于某个全域有界算子。
若只知道某个 $J$ 图核心包含于自然平方域，
并且平方在这个核心上有统一界，(A.4) 已经足够。
因此此引理也适用于“自然平方的闭包有界”的情形，
但还必须核验所用平方域确实含有 $J$ 的图核心。

例如在 R143 的受控分母情形，若 $B^2L$ 已由有限放大证明为
$J_L$ 图核心、自然 $J_L^2$ 在其上等于有界尾算子 $t|_L$，
则 (A.2) 可取 $K=\|t|_L\|$。
剩下关键条件正是 $J_L$ 的通常伴随共同域和有界自交换子形式，
不能从原空间某个商的 $C$ 对称性直接继承。

### A.2 与当前实际问题的区别

本稿 §1–4 已经证明真实第一阶 $X$ 满足
共同通常伴随域与有界自交换子形式这两项条件。
但一般 head 商是 $B^{-1}P$ 的最大闭实现，
其中分母的连续谱附近可能放大伴随交换子；
目前没有证明它满足 (A.1)。

R143 的无界闭平方根直和反例不满足所需的
有界自交换子条件：其局部块具有大小为 $n$ 的非对角项，
两个图范数之差含大小为 $n^2$ 的无界对角部分。
因此它与引理 A.1 不冲突。

反过来，本附录也没有使实际共振核自动消失。
需要从具体一阶核结构导出 head 商的上述共同域与二次型估计，
或给出其他同样足够的 $J$ 图范数界。
在取得这一桥接之前，不得把 (A.3) 用于那个尚未核准条件的商。
