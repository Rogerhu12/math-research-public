# R271 附录：三个独立异权位的全部出生层相邻 Gram 比较

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf。  
状态：已证明；Astra-ISP-1cf8c51d 与 normal_resume_1cf 全文核对完整最小逆、真实同余及全部端点。全参数 BigInt 证书由 kernel_resume_1cf 与 normal_resume_1cf 分别完整执行通过。

本文使用[两异权全出生稿](R239-appendix-two-exceptional-weights-full-birth-one-primitive-gram-bound.md)的完整逆后压缩约定，并使用[全出生倒数权对偶](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)支付反向端点。新增范围是三个独立正异权位、任意等权池和整个出生一层 primitive 空间。这里的主要块为三维，通常不交换；不以二维比较逐坐标推导本结论。

已存在的任意异权头饱和固定线，以及[倒数第二出生块的一参数最小逆](R239-appendix-penultimate-primitive-fixed-block-exact-one-parameter-inverse.md)，均扣除。后续 §§8–9 已补齐相对出生二层及整个模型的全部出生层。

## 1. 定理、合法阶和真实整层逆

取池大小 $M\ge1$、三个任意正实权 $a_1,a_2,a_3$，总位数为
$$
N=M+3.
$$
在标准布尔 Hilbert 空间上令
$$
D=a_1E_1+a_2E_2+a_3E_3+\sum_{j=4}^{N}E_j,
\qquad K_1=\ker D\cap\mathcal H_1.
$$
定义最高合法阶
$$
h=N-2=M+1,
$$
以及先在整层求逆、再压缩的真实 Gram
$$
F_n=\frac{D^n(D^*)^n|_{\mathcal H_1}}{(n!)^2},
\qquad
\Gamma_n=P_{K_1}F_n^{-1}|_{K_1},
\qquad 0\le n\le h.
\tag{1.1}
$$

**定理。** 对全部 $1\le n<h$，在整个 $K_1$ 上严格有
$$
\boxed{\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n<\Gamma_{n-1}.}
\tag{1.2}
$$
因此同一模型出生一层的真实相邻第一下降块满足平方常数上界
$$
A_{\ell+1}A_{\ell+1}^*
<
\left(\frac{\ell}{\ell-1}\right)^2 A_\ell^*A_\ell,
\qquad 2\le\ell\le N-2.
\tag{1.3}
$$
(1.3) 使用 $\Gamma_n=(n!)^2J_n^*J_n$ 的既有准确字典；没有比较整个 $D$。

为核 (1.1) 的全部逆，令实际总权为 $a_i$，池位取 $a_i=1$。对 $x\in\mathcal H_1$，
$$
\frac{(D^*)^n}{n!}x
=
\sum_{|S|=n+1}
a_S\left(\sum_{i\in S}\frac{x_i}{a_i}\right)e_S.
\tag{1.4}
$$
因为 $1\le n+1\le N-1$，若所有子集和为零，比较相差一个元素的两个子集便使全部 $x_i/a_i$ 相等；再读一个子集即得 $x=0$。所以每个 $F_n$ 严格正定，包括零阶和最高阶。

## 2. 完整 primitive 空间及非正交源坐标

池置换群 $S_M$ 同时约化 $D,D^*$、各完整 $F_n$ 及其逆。在出生一层，
$$
K_1=K_{\rm fix}\oplus^\perp K_{\rm st}.
$$
其中
$$
K_{\rm st}
=\left\{\sum_{j=4}^N x_je_j:\sum_{j=4}^Nx_j=0\right\},
$$
$M=1$ 时此空间为零；固定部分为三维，
$$
\mathcal Zg
=
\sum_{i=1}^3g_ie_i-\frac{\sum_{i=1}^3a_ig_i}{M}
\sum_{j=4}^Ne_j,
\qquad g\in\mathbb C^3.
\tag{2.1}
$$
记 $a=(a_1,a_2,a_3)^{\mathsf T}$、$A=\operatorname{diag}(a_1,a_2,a_3)$。源 Gram 为
$$
H_0=\mathcal Z^*\mathcal Z=I+\frac{aa^*}{M}.
$$
各真实 Gram form 是
$$
H_n=\mathcal Z^*F_n^{-1}\mathcal Z.
\tag{2.2}
$$
实际算子坐标为 $H_0^{-1}H_n$，所以 (1.2) 在固定块上准确等价于
$$
H_nH_{n+1}^{-1}H_n<H_{n-1}.
\tag{2.3}
$$
这一同余按真实逆的顺序消去 $H_0$，不要求不同 $H_n$ 交换。

在 $K_{\rm st}$ 上，各 $\Gamma_n$ 是标量
$$
\left[
e_n(a_1^2,a_2^2,a_3^2,\underbrace{1,\ldots,1}_{M-2})
\right]^{-1}.
\tag{2.4}
$$
这对 $M\ge2$ 由池 primitive 上升链及头位展开直接得到，和两异权稿 §2.1 同一计算；有效总位数恰为 $M+1=h$。实根多项式的 Newton 不等式给
$$
\frac{e_{n-1}e_{n+1}}{e_n^2}<\frac n{n+1}<1.
$$
所以完整标准块已付。余下严格处理三维固定块。

## 3. 条件子集协方差给的是完整最小逆

置
$$
z_i=a_i^2\quad(1\le i\le3),\qquad
k=n+1,\quad l=N-k,
$$
并在所有 $k$ 元物理子集上取概率正比于实际权平方乘积的分布。令 $I=(I_1,I_2,I_3)$ 为三个异权位的占据向量，$\mathsf C_k=\operatorname{Cov}(I)$。全部子集权的和是
$$
e_k=e_k(z_1,z_2,z_3,1,\ldots,1).
$$
准确有
$$
\boxed{H_n=A(e_k\mathsf C_k)^{-1}A.}
\tag{3.1}
$$

补足完整逆后压缩的步骤。对所有物理位，(1.4) 给
$$
F_n=e_k A_{\rm all}^{-1}\mathbb E(I_{\rm all}I_{\rm all}^*)A_{\rm all}^{-1}.
$$
以 $K_1\oplus\mathbb Ca_{\rm all}$ 作块逆，$\Gamma_n^{-1}$ 是 $F_n$ 对后一条线的 Schur 补。因此它在整层以零延拓的形式恰为
$$
e_k A_{\rm all}^{-1}\operatorname{Cov}(I_{\rm all})A_{\rm all}^{-1}.
\tag{3.2}
$$
这也由 $F_na_{\rm all}=ke_kA_{\rm all}^{-1}\mathbb EI_{\rm all}$ 直接核验。

对 $x=\mathcal Zg$，池位的 $x_j/a_j$ 为同一个常数；总占据数固定，所以协方差只读取三个头位与池值的差。该差列是
$$
A^{-1}H_0g.
$$
故 $\mathcal Z^*\Gamma_n^{-1}\mathcal Z$ 等于
$H_0A^{-1}(e_k\mathsf C_k)A^{-1}H_0$。另一方面，它由真实源 Gram 等于 $H_0H_n^{-1}H_0$，相消即得 (3.1)。没有把 $F_n$ 的 primitive 压缩直接当成 $\Gamma_n^{-1}$。

## 4. 四维矩阵与三个小多项式矩阵

对头子集 $J\subseteq\{1,2,3\}$，令
$$
u_J=(1,1_{1\in J},1_{2\in J},1_{3\in J})^{\mathsf T},
\qquad
w_J=z_J\,k^{\underline{|J|}}l^{\underline{3-|J|}}.
$$
定义真实 $4\times4$ 矩阵
$$
E=\sum_Jw_Ju_Ju_J^*,\qquad
Z=E_{00},\qquad b=(E_{10},E_{20},E_{30})^{\mathsf T},
\qquad E_H=(E_{ij})_{1\le i,j\le3}.
\tag{4.1}
$$
头状态的原质量为 $z_J\binom M{k-|J|}$，而
$$
\binom M{k-r}
=\frac{\binom Nk}{N^{\underline3}}k^{\underline r}l^{\underline{3-r}}
\quad(0\le r\le3),
\tag{4.2}
$$
越界二项式和相应下降阶乘均为零。这支付全部端点，不使用奇异极限。

全部 $1\le k\le N-1$ 时，$E$ 严格正定。确实，若 $c_0+\sum_{i=1}^3c_iI_i$ 在全部正质量的 $k$ 元物理子集上为零，固定任一头位 $i$ 和一个池位，再在其余 $N-2$ 位中任取 $k-1$ 位；分别加入该头位或该池位的两次等式相减，得 $c_i=0$。这种选择在 $1\le k\le N-1$ 始终合法，且所有物理权为正。三个头系数都为零后读任一子集，得 $c_0=0$。这也覆盖 $M=1,k=2$，无需假设全头状态有正质量。

定义
$$
T=\frac{\det E}{k^3l^3},\qquad
\mathsf N=\frac{(\operatorname{adj}E)_{H,H}}{k^2l^2},
\qquad
\mathsf M=\frac{ZE_H-bb^*}{kl}.
\tag{4.3}
$$
这三个对象的条目都是
$\mathbb Z[z_1,z_2,z_3,k,l]$ 中的多项式：附证书逐项执行了所写单项整除，任一不整除都会立即失败。它们在全部合法整数参数下严格正，且
$$
\boxed{
\mathsf N\mathsf M=ZT I,\qquad
\det\mathsf N=ZT^2,\qquad
\det\mathsf M=Z^2T.
}
\tag{4.4}
$$
也可不用展开验证：令 $S=E_H-bb^*/Z$，块逆给
$\mathsf N=kl\,T\,S^{-1}$、$\mathsf M=ZS/(kl)$，立即得到 (4.4)。

由 (3.1)、(4.2)，
$$
\boxed{
H_n=s_n\,A\frac{\mathsf N(k,l)}{T(k,l)}A,
\qquad
s_n=\frac{N^{\underline3}}{\binom Nk\,kl}.
}
\tag{4.5}
$$
因此从零阶到最高阶都是同一个有限公式。零阶也可单独核：
$e_1\mathsf C_1=\operatorname{diag}(z)-zz^*/(M+\sum z_i)$，
其逆给 $H_0=I+aa^*/M$。

## 5. 相邻差的真实同余与三个标量证书

下标 $+$ 表示把 $(k,l)$ 换成 $(k+1,l-1)$，下标 $-$ 则换成 $(k-1,l+1)$。所有邻居保持同一个总位数 $N=k+l$。令
$$
\alpha=kl,\qquad\beta=(k-1)(l-1).
$$
相邻标量因子的准确比值为
$$
\frac{s_{n-1}s_{n+1}}{s_n^2}
=\frac{\alpha}{\beta}.
$$
把固定正对角 $A$ 从 (2.3) 作同余消去，再以中间正矩阵的真实逆作同余，(2.3) 准确等价于
$$
\boxed{
\Delta=
\alpha Z_+\mathsf M\mathsf N_-\mathsf M
-\beta Z^2T_-\mathsf M_+>0.
}
\tag{5.1}
$$
所有被乘去的标量均严格正。特别，这不是交换 $\mathsf N_-$ 与 $\mathsf M$ 后得到的标量比较。

令
$$
\mathsf U=\mathsf M\mathsf N_-\mathsf M,\qquad
\mathsf V=\mathsf N\mathsf M_-\mathsf N,
$$
$$
\Xi=\mathsf U_{22}(\mathsf M_+)_{33}
+\mathsf U_{33}(\mathsf M_+)_{22}
-2\mathsf U_{23}(\mathsf M_+)_{23}.
$$
定义以下三个整数多项式：
$$
P_1=\frac{\Delta_{11}}{z_1z_2z_3},
\tag{5.2}
$$
$$
P_2=
\frac{
\alpha^2Z_+\mathsf V_{11}
-\alpha\beta\Xi
+\beta^2Z^2T_-(\mathsf N_+)_{11}
}{z_1z_2^2z_3^2},
\tag{5.3}
$$
$$
\begin{aligned}
P_3=\frac1{(z_1z_2z_3)^2}\big[
&\alpha^3Z_+T^2Z_-
-\alpha^2\beta\operatorname{tr}
(\mathsf N\mathsf M_-\mathsf N\mathsf M_+)\\
&+\alpha\beta^2\operatorname{tr}
(\mathsf N_+\mathsf M\mathsf N_-\mathsf M)
-\beta^3Z^2T_-T_+
\big].
\end{aligned}
\tag{5.4}
$$
附证书也逐项检查了这三个单项整除。

它们准确控制所需主子式：
$$
\Delta_{11}=z_1z_2z_3P_1,
$$
$$
(\operatorname{adj}\Delta)_{11}
=Z^2T_-Z_+\,z_1z_2^2z_3^2P_2,
\tag{5.5}
$$
$$
\det\Delta
=Z^4T_-^2Z_+^2(z_1z_2z_3)^2P_3.
\tag{5.6}
$$
(5.5) 来自 $3\times3$ 伴随矩阵的二次展开和
$\operatorname{adj}\mathsf M=Z\mathsf N$、
$\operatorname{adj}\mathsf N_-=T_-\mathsf M_-$。
(5.6) 使用
$$
\det(aU-bV)
=a^3\det U-a^2b\,\operatorname{tr}((\operatorname{adj}U)V)
+ab^2\,\operatorname{tr}((\operatorname{adj}V)U)-b^3\det V
$$
及 (4.4)。矩阵的次序在这些迹中保留；只用合法的迹循环，没有假设可交换。

## 6. 全参数整数系数正性

完整可执行证书见
[三异权出生一层 BigInt 证书](../notes/2026-11-13-three-exceptional-weights-birth-one-gram-certificate-1cf.mjs)。
它直接从八个 $u_J,w_J$ 生成 (4.1)，不是抄入参数样本的矩阵。

### 6.1 内部与单边

在多项式环 $\mathbb Z[z_1,z_2,z_3,x,y]$ 中，代入
$$
k=3+x,\qquad l=3+y,
$$
所得 $P_1,P_2,P_3$ 的全部非零系数均严格为正。
在 $\mathbb Z[z_1,z_2,z_3,y]$ 中，代入
$$
k=2,\qquad l=3+y
$$
也成立。证书给出的准确支持大小和一个 $x,y$ 零次的正系数如下：

| 区域 | 多项式 | 非零项数 | 明确包括的项 |
|---|---:|---:|---:|
| $k=3+x,l=3+y$ | $P_1$ | 21735 | $2239488z_1^2$ |
| 同上 | $P_2$ | 33977 | $11943936z_1$ |
| 同上 | $P_3$ | 51785 | $143327232z_1$ |
| $k=2,l=3+y$ | $P_1$ | 1184 | $1119744z_1^2$ |
| 同上 | $P_2$ | 2163 | $5038848z_1$ |
| 同上 | $P_3$ | 3571 | $40310784z_1$ |

因为 $z_i>0$、$x,y\ge0$，这给三个标量的严格正性。
同时置换三个头位，得到全部对角元和全部二阶主子式的对应正性。因此 (5.5)–(5.6) 及 Sylvester 判据给 $\Delta>0$。

### 6.2 反向端点

尚余 $l=2,k\ge3$。对物理权取倒数，等权池仍为一，三个头权变成 $a_i^{-1}$。全出生倒数权定理将阶 $n$ 变成
$$
h-n,
$$
在当前参数上恰交换 $k,l$，并保持相邻常数 $1$。更明确地，反向后的两个邻居先互换，再以
$$
A B^{-1}A\le cC
\quad\Longleftrightarrow\quad
A C^{-1}A\le cB
$$
恢复通常次序。该等价也保严格不等式。因此 §6.1 的 $k=2,l\ge3$ 完整结论支付另一端，而没有误把反向对偶写成同序。

### 6.3 唯一的四位角

$k=l=2$ 恰为 $N=4,M=1,n=1$。
此时只有一个池位；在四个正物理权中选最小者，作整体正缩放并置换使它成为权为一的池位。其他三个权平方满足 $z_i\ge1$。
整体缩放只给 $\Gamma_n$ 乘同一几何因子，故不改变 (1.2)。

直接在 $k=l=2$ 代入
$$
z_1=1+x_1,\quad z_2=1+x_2,\quad z_3=1+x_3.
$$
三个证书多项式的全部非零系数也严格为正：

| 多项式 | 非零项数 | 常数项 |
|---|---:|---:|
| $P_1$ | 127 | 2985984 |
| $P_2$ | 160 | 11943936 |
| $P_3$ | 245 | 35831808 |

这支付了任意四个正权，而不是只验证等权角点。$M=1$ 没有标准块，所以它已经是整个 $K_1$。

### 6.4 证书的精确性

脚本仅用任意精度整数加、减、乘及已检查的单项整除：

1. 构造八个物理头状态与完整 $4\times4$ 矩阵；
2. 检查 $\mathsf N\mathsf M=ZT I$、$\det\mathsf N=ZT^2$、$\det\mathsf M=Z^2T$ 及对称性；
3. 按 (5.2)–(5.4) 生成三个多项式；
4. 执行上述三种有限变量代换；
5. 遍历每一个非零 BigInt 系数，检查符号、支持大小及表中的明确系数。

五个非负指数用底数 $64$ 编码，每次乘法先检查每一指数的次数上界不达到 $64$；编码整数也检查在安全整数范围内。故不会因进位混同单项，也没有浮点多项式运算、数值特征值或随机参数验证。作者完整执行报告为 PASS。

由 §§6.1–6.3，全部合法比较 $k,l\ge2$ 都已支付。再与 §2 的真实标准块合并，(1.2) 在完整 $K_1$ 上成立。

## 7. 范围与下一项

本结果给出了三个独立异权位的完整非交换出生一层比较，包含任意池大小、最高所需逆和四位边角。它证明的是平方常数所对应的 $\Gamma$ 系数 $1$，没有声称更小的出生因子。

等权池的完整正交串分解可使一般出生层约化到三个头位的相对出生 $0,1,2,3$：相对出生 $0$ 的真空 Newton、相对出生 $1$ 的本文结果、相对出生 $3$ 的既有饱和正矩均已付；相对出生 $2$ 的真实三维相邻序现由后续 §8 支付，§9 再合并全部真实弱池串。仍不把有限模型上界直接用到任意连续尾或真实窄 Schur 返回源。

## 8. 相对出生二层：同一有限多项式证书在负参数下的准确应用

日期：2026-11-13（UTC）。本节单独补齐三个异权头的相对出生二层。使用的是[倒数第二出生块稿](R239-appendix-penultimate-primitive-fixed-block-exact-one-parameter-inverse.md)已证明的完整一参数最小逆；不将该公式重新登记为本稿结果。新结论是其真实非交换相邻序。

### 8.1 固定三维源、全部内部阶与两个端点

现在池大小记为 $L\ge3$，头位仍为三个，权为 $a_i>0$。固定
$$
s=2,\qquad N=L+3,\qquad h=N-2s=L-1,\qquad d=h-n.
$$
为区别第 2 节的出生一层源，令
$$
\mathcal E f=
\sum_{\varnothing\ne R\subseteq[3]}
(-1)^{|R|-1}
\frac{a_R}{\binom L{|R|-1}}
s_R(f)\,e_{[3]\setminus R}w_{|R|-1},
\qquad
s_R(f)=\sum_{i\in R}\frac{f_i}{a_i}.
\tag{8.1}
$$
这是池固定的完整三维 primitive 块；$w_j$ 为未归一的池对称向量，$\|w_j\|^2=\binom Lj$。仍先在整个物理第 $2$ 孔层取 $F_n^{-1}$，然后定义 Gram form
$$
H_n=\mathcal E^*F_n^{-1}\mathcal E.
$$
实际算子坐标是 $H_0^{-1}H_n$，所以所需相邻序仍等价于 (2.3)。

已证的一参数公式是
$$
f^*H_nf=
\min_{\xi\in\mathbb C}
\sum_{R\subseteq[3]}
\frac{a_R^2}{\binom L{n+|R|-1}}
|s_R(f)-\xi|^2,
\qquad 1\le n<h.
\tag{8.2}
$$
它通过池置换平均和完整方程的唯一自由参数，给全 Hilbert 空间的真正最小解。零阶与最高阶分别是
$$
f^*H_0f=
\sum_{R\ne\varnothing}
\frac{a_R^2}{\binom L{|R|-1}}|s_R(f)|^2,
\tag{8.3}
$$
$$
f^*H_hf=
\sum_{R\subsetneq[3]}
\frac{a_R^2}{\binom L{h+|R|-1}}
|s_R(f)-s_{[3]}(f)|^2.
\tag{8.4}
$$
(8.3) 没有自由参数，(8.4) 的自由参数被强制为全头和；不在端点使用无限大的二项式权。

### 8.2 同一四维矩阵的有限多项式代换

记 $z_i=a_i^2$，仍用第 4 节由八个头子集定义的多项式
$E(k,l),Z(k,l),\mathsf M(k,l),\mathsf N(k,l),T(k,l)$。
这里只作这些有限多项式的数值代换，不把负数当作物理池大小，也不对任何无界算子作解析延拓。

在内部 $n,d\ge1$，(8.2) 中的四种质量可共同提出
$$
c_n=\frac1{\binom Ln\,n d(d+1)}.
$$
剩下的头子集质量为 $z_Rq_{|R|}$，其中
$$
\begin{aligned}
q_0&=d(d+1)(d+2),&
q_1&=n d(d+1),\\
q_2&=n(n+1)d,&
q_3&=n(n+1)(n+2).
\end{aligned}
\tag{8.5}
$$
逐项检查二项式相邻比即可验证这个提出因子。
并且准确有
$$
E^\#:=\sum_Rz_Rq_{|R|}u_Ru_R^*=-E(-n,-d).
\tag{8.6}
$$
所有内部质量为正，所以 $E^\#>0$。置
$$
Z^\#=-Z(-n,-d)>0,\qquad
\mathsf M^\#=\mathsf M(-n,-d).
$$
若 $S^\#$ 是 $E^\#$ 对其常数坐标的 Schur 补，则 (4.3) 给
$$
\mathsf M^\#=\frac{Z^\#S^\#}{nd}>0.
$$
对 (8.2) 的标量参数完成平方，得到
$$
\boxed{
H_n=\sigma_n A^{-1}
\frac{\mathsf M(-n,-d)}{-Z(-n,-d)}
A^{-1},
\qquad
\sigma_n=\frac1{L\binom hn}
=\frac1{\binom Ln(d+1)}.
}
\tag{8.7}
$$
这里 $A=\operatorname{diag}(a_1,a_2,a_3)$。与 (4.5) 相比，矩阵从精度形式变成协方差形式；这一步实际来自 (8.2)，不是将正参数结论免费延拓到负参数。

### 8.3 零阶、最高阶及相邻正分母

(8.7) 在 $n=0$ 与 $d=0$ 仍给准确的真实端点。给出有限系数核验。

当 $n=0,d=h=L-1$ 时，$E^\#$ 的零次质量只在空头；其余头质量的一次系数分别为
$$
d(d+1),\quad d,\quad 2
$$
（对应缺失数 $1,2,3$）。
Schur 修正的分子此时至少二次，所以在 $\mathsf M^\#/Z^\#$ 中除去已经出现的 $nd$ 后，乘 $\sigma_0=1/L=1/(d+1)$，三个系数恰为
$$
1,\qquad \frac1L,\qquad \frac2{L(L-1)}.
$$
它们就是 (8.3) 的 $1/\binom L{r-1}$。

当 $d=0,n=h=L-1$ 时，零次质量只在全头。协方差的一次项因此读取
$1_R-1_{[3]}$，三个真子集大小 $r=0,1,2$ 的一次质量系数分别为
$$
2,\quad n,\quad n(n+1).
$$
除去 $nd$ 的 $d$ 因子，并乘 $\sigma_h=1/L$ 后，准确得到
$$
\frac2{L(L-1)},\qquad\frac1L,\qquad1,
$$
恰为 (8.4) 的三个权。这只是读取有限多项式的系数，不假定一个尚未建立的算子图极限。

于是所有 $0\le n\le h$ 都有
$$
\mathsf M(-n,-d)>0,\qquad -Z(-n,-d)>0.
\tag{8.8}
$$
内部已在 §8.2 证明；两端由 (8.3)、(8.4) 的真实正定源 Gram 和 (8.7) 得到。恒等式
$$
\det\mathsf M=Z^2T
$$
进一步给
$$
T(-n,-d)>0
\quad(0\le n\le h).
\tag{8.9}
$$
因此后续相邻比较中出现的所有 $T_-,Z_+$，包括邻居为零阶或最高阶时，都有已付的真实符号。

### 8.4 相邻序准确等价于负的旧差矩阵

在当前出生二层参数中，
$$
\frac{\sigma_{n-1}\sigma_{n+1}}{\sigma_n^2}
=\frac{(n+1)(d+1)}{nd}.
$$
在旧多项式处代入 $k=-n,l=-d$，其
$$
\alpha=kl=nd,\qquad
\beta=(k-1)(l-1)=(n+1)(d+1)
$$
都为正。新阶的 $n+1$ 对应旧多项式的下标 $-$，新阶的 $n-1$ 对应旧下标 $+$；两个邻居必须反向。

从 (8.7) 消去同一个正对角 $A^{-1}$。使用 (4.4) 并乘严格正的标量
$$
(-Z_+)Z^2T_-,
$$
准确得到
$$
\boxed{
H_nH_{n+1}^{-1}H_n<H_{n-1}
\quad\Longleftrightarrow\quad
-\Delta(-n,-d)>0.
}
\tag{8.10}
$$
例如令 $R_n=\mathsf M(-n,-d)/[-Z(-n,-d)]$，则
$R_{n+1}^{-1}=-\mathsf N_-/T_-$。
将 $\beta R_{n-1}-\alpha R_nR_{n+1}^{-1}R_n$ 乘上述正标量，恰为
$$
\beta Z^2T_-\mathsf M_+
-\alpha Z_+\mathsf M\mathsf N_-\mathsf M=-\Delta.
$$
没有改变非交换乘积的顺序。

### 8.5 反射后的三个严格正证书

证书脚本新增的部分直接检查
$$
-P_i(-1-x,-1-y)\qquad(i=1,2,3)
$$
在 $\mathbb Z[z_1,z_2,z_3,x,y]$ 中全部非零系数为正。准确结果为：

| 多项式 | 非零项数 | $x,y$ 零次的明确正项 |
|---|---:|---:|
| $-P_1(-1-x,-1-y)$ | 21251 | $248832z_1z_2z_3$ |
| $-P_2(-1-x,-1-y)$ | 33584 | $1327104z_2z_3$ |
| $-P_3(-1-x,-1-y)$ | 51515 | $15925248z_2z_3$ |

这是与 §6 同一组多项式的有限符号代换；整个更新脚本连同原九项检查已再次完整执行 PASS。

对 $n,d\ge1$，取 $x=n-1,y=d-1$。由 (8.8)–(8.9)，在 (5.5) 的反射参数下 $T_->0$、$Z_+<0$。又
$\operatorname{adj}(-\Delta)=\operatorname{adj}\Delta$、$\det(-\Delta)=-\det\Delta$。
于是三个表项分别给
$$
-\Delta_{11}>0,\qquad
(\operatorname{adj}(-\Delta))_{11}>0,\qquad
\det(-\Delta)>0.
$$
同时置换头指标给其余对应主子式的正性，Sylvester 判据遂给 (8.10)。这包括最小池 $L=3$ 的 $n=d=1$；零阶与最高阶的逆已由 §8.3 支付。

所以相对出生二层的整个三维固定 primitive 块满足
$$
\boxed{
\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n<\Gamma_{n-1},
\qquad 1\le n<L-1.
}
\tag{8.11}
$$
这才是本节新增的算子序结论。

## 9. 三个独立异权位的全部出生层

回到任意池大小 $M\ge1$、总位数 $N=M+3$。现在允许任意
$$
0\le s\le\lfloor N/2\rfloor,
\qquad h=N-2s,
$$
并按完整整层逆定义
$$
\Gamma_n^{(s)}
=P_{\ker D\cap\mathcal H_s}
\left[\frac{D^n(D^*)^n|_{\mathcal H_s}}{(n!)^2}\right]^{-1}
\big|_{\ker D\cap\mathcal H_s}.
$$
全部逆对 $0\le n\le h$ 合法，由有限等权 Lefschetz 链与正权对角去权保持秩得到。

**全出生定理。** 对全部 $1\le n<h$，
$$
\boxed{
\Gamma_n^{(s)}(\Gamma_{n+1}^{(s)})^{-1}\Gamma_n^{(s)}
<
\Gamma_{n-1}^{(s)}
}
\tag{9.1}
$$
在整个 primitive 空间上成立。

### 9.1 原弱池的完整正交串

沿两异权全出生稿 §9.1，对弱池的任意单位 primitive
$\zeta\in\ker D_{\rm w}\cap\mathcal H_j^{\rm w}$，置
$$
L=M-2j,\qquad
\zeta_l=\frac{(D_{\rm w}^*)^l\zeta}
{\sqrt{l!\,L^{\underline l}}},\quad0\le l\le L.
$$
等权交换关系给
$$
D_{\rm w}\zeta_l=\sqrt{l(L-l+1)}\,\zeta_{l-1},
\quad
D_{\rm w}^*\zeta_l=\sqrt{(l+1)(L-l)}\,\zeta_{l+1}.
$$
各串正交、同时约化删除和伴随，且低层 primitive 维数的望远镜和穷尽整个弱池。与三个头位张量后，完整 $F_n$、完整逆及 primitive 压缩也都按这些正交约化块分解；没有把一般压缩的逆当成完整逆。

在原出生层 $s$ 中，一条弱串的相对出生为
$$
t=s-j,\qquad h=L+3-2t.
\tag{9.2}
$$
只需处理 $h\ge2$，否则没有相邻比较。

若 $t<0$，该块没有源。若 $t\ge4$，(9.2) 给 $L\ge2t-1$。
相对第 $t$ 和第 $t-1$ 层都以全部八个头集合为基，池删除三角对角系数
$$
L-t+|F|+1>0
$$
全部非零，因而该 primitive 核为零。故非零块只可能有 $t=0,1,2,3$。

### 9.2 四种相对出生逐一支付，含短串

- $t=0$：真空标量 Gram 是
  $e_n(a_1^2,a_2^2,a_3^2,1,\ldots,1)^{-1}$。
  其有效位数为 $L+3=h$，Newton 不等式给严格系数 $n/(n+1)<1$。
- $t=1$：由 $h=L+1\ge2$ 自动有 $L\ge1$。这是 §§1–6 的三维固定块，包含 $L=1$ 的任意四位角及全部端点，故系数 $1$ 已付。
- $t=2$：由 $h=L-1\ge2$ 自动有 $L\ge3$，正好是 §8 的范围，系数 $1$ 已付。
- $t=3$：由 $h=L-3\ge2$ 自动有 $L\ge5$。两异权全出生稿 §8 已证明任意三个独立头权的饱和固定线正矩；全部所需阶满足 $n+1\le L-3$，其严格系数 $(3+n)/(4+n)<1$ 足够。

短串没有被略去：$L=0$ 只能有 $t=0$；$L=1$ 只可能有 $t=0,1$，后一种已由四位角支付；$L=2$ 同样只可能有 $t=0,1$。这些判断均来自 (9.2) 和 $h\ge2$，没有把短池套进要求 $L\ge3$ 的 §8。

所有真实 primitive 块都已支付，有限正交直和即给 (9.1)。特别此模型全部出生层的相邻第一下降块都有
$$
A_{\ell+1}A_{\ell+1}^*
<
\left(\frac{\ell}{\ell-1}\right)^2A_\ell^*A_\ell
$$
在其完整合法范围成立，常数不依赖池大小、出生层或三个异权的比例。

### 9.3 本次完成的边界

新完成的是“三个独立正异权加等权池”的整个有限模型，不只一条对称源。它仍未证明任意数量独立异权的普遍比较；前述有限模型与连续尾的归约也要求覆盖任意有限权型，不能从三个异权的结果直接推出原连续尾上界。

本文不恢复已否定的额外有限总位数因子或全 Hankel 正性，也不据本有限相邻比较删除原窄 Schur 源的真实费用。

