# R224：准确 gauge 第二因子、同核闭像及解析公共像障碍

日期：2026-11-12（UTC）。作者：kernel；任意解析头的边界核输入由 boundary 独立证明并由 kernel 全文核验。状态：以下定理已证明；不操作仓库共享状态。

本文先给完全独立的实际算子恒等式，再说明它对有限 gauge 根碰撞的准确含义。最后的全空间公共像排除使用已完成的 [任意真解析头下的慢平方边界无限支持核](R223-bell-minus-arbitrary-analytic-germ-boundary-kernels.md)。前五节不依赖该新增输入。

## 1. 实际对象和域

固定 R125 的闭第一 chaos 算子

$$
X=X_u,\qquad u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad (a_j)\in\ell^2,
$$

并设

$$
j_0=\min\{j:a_j\ne0\},\quad h=2^{j_0},\quad
a=a_{j_0}\ne0,\quad d=d_{j_0}.
$$

记

$$
V_j=(I-N_j)(I+N_j)^{-1},\qquad
B=\sum_j a_j^2(I-V_j^2)\in\mathcal A,
$$

其中级数在算子范数下绝对收敛。取字符为 $a$ 的实际解析平方根

$$
Y=(a^2I-B)^{1/2},\qquad T=X-Y,
\qquad M=\ker T.
\tag{1.1}
$$

本文的点态平方应用显式要求 $a_*=0$，即 $u=\sum_j a_j\chi_j$。在这一前提下，使用 R144 完整平方附录及 main 提交 `5c4fcb572b6805c0f95458ab2dbe0ea410cdad66` 中已澄清的危险平方接口：危险点态平方 $u^2-a^2$ 的相应实际闭核可使用此 $M$。不把这一应用不加条件地延伸到所有 $a_*$。

独立地，对任意 $a_*$，只要按 (1.1) 定义 $M=\ker(X-Y)$，就有 $M\subset\operatorname{Dom}X^n$ 对每个有限 $n$ 成立，且

$$
X_M=Y_M\in B(M).
\tag{1.2}
$$

以下只研究这个真实闭核。全部 gauge 分解、同核像闭包及商等式对 (1.1) 独立定义的核成立，不依赖点态平方解释。后文规范慢平方应用始终取 $a_*=0$。

对 dyadic 根 $\zeta\in\Gamma$，令 $U_\zeta f(y)=\zeta^yf(y)$，并记 $\gamma_\zeta(A)=\zeta A$。R125 给包括定义域的等式

$$
\gamma_\zeta X=X+D_\zeta,
\quad \operatorname{Dom}\gamma_\zeta X=\operatorname{Dom}X.
$$

每个 dyadic gauge 只改有限个 $V_j$，故

$$
D_\zeta=\sum_{j< m}a_j(\gamma_\zeta V_j-V_j),
\quad E_\zeta=\gamma_\zeta B-B
\tag{1.3}
$$

都是真正收敛的一元解析芽作用于 $A$，其中 $\zeta^{2^m}=1$。设

$$
Y_\zeta=\gamma_\zeta Y,
\quad T_\zeta=\gamma_\zeta T,
\quad M_\zeta=U_\zeta M=\ker T_\zeta.
$$

它们满足

$$
Y_\zeta^2=Y^2-E_\zeta,\qquad
T_\zeta-T=D_\zeta+Y-Y_\zeta\in\mathcal A.
\tag{1.4}
$$

## 2. 每个非平凡 gauge 的准确第二因子

以下设 $\zeta^h\ne1$。若 $\zeta^h=1$，全部非零行系数所在位都被固定，因而 $D_\zeta=E_\zeta=0$，没有可用差分。

由 $V_j=I-2N_j+O(N_j^2)$ 及 $I-V_j^2=4N_j+O(N_j^2)$，有真正解析因式

$$
D_\zeta=A^h d_\zeta(A),\qquad
E_\zeta=A^h e_\zeta(A),
\tag{2.1}
$$

且

$$
d_\zeta(0)=-\frac{2a(\zeta^h-1)}d\ne0,
\qquad e_\zeta(0)=\frac{4a^2(\zeta^h-1)}d.
\tag{2.2}
$$

所以 $d_\zeta(A)$ 是实际有界单位，$E_\zeta/D_\zeta$ 以下专指合法的一元解析芽 $e_\zeta/d_\zeta$，不是在未知核上取消一个未付清分母。定义

$$
s_\zeta(A)=-\frac12\left(D_\zeta+rac{E_\zeta}{D_\zeta}\right),
\qquad r_\zeta(A)=a^2I-s_\zeta(A)^2.
\tag{2.3}
$$

二者都是真解析演算，且

$$
s_\zeta(0)=a,\qquad r_\zeta(0)=0.
$$

置 $F_\zeta=T_\zeta-T$。因 (1.4) 的各有界因子交换，直接相乘得到

$$
\begin{aligned}
F_\zeta(D_\zeta+Y+Y_\zeta)
&=(D_\zeta+Y)^2-Y_\zeta^2\\
&=D_\zeta^2+2D_\zeta Y+E_\zeta\\
&=2D_\zeta(Y-s_\zeta).
\end{aligned}
\tag{2.4}
$$

又有

$$
(Y-s_\zeta)(Y+s_\zeta)=r_\zeta-B.
\tag{2.5}
$$

两个分母 $D_\zeta+Y+Y_\zeta$ 与 $Y+s_\zeta$ 的字符都为 $2a\ne0$，所以均为 $\mathcal A$ 的实际单位。于是得到全空间有界恒等式

$$
\boxed{
F_\zeta=A^h W_\zeta(B-r_\zeta(A)),
\qquad
W_\zeta=
\frac{-2d_\zeta(A)}{(D_\zeta+Y+Y_\zeta)(Y+s_\zeta(A))}.
}
\tag{2.6}
$$

其中 $W_\zeta\in\mathcal A$ 是单位。该式既没有形式亚纯分母，也没有从全空间有界性推断未知限制的有界性。

### 2.1 最低位翻转恰好留下尾 Bell 算子

取 $\zeta_0^h=-1$ 且 $\zeta_0^{2h}=1$。低于 $j_0$ 的系数为零，高于 $j_0$ 的位被固定。置 $v=V_{j_0}$、$v'=\gamma_{\zeta_0}v=v^{-1}$。于是

$$
D_{\zeta_0}=a(v'-v),\qquad
E_{\zeta_0}=-a(v'+v)D_{\zeta_0}.
$$

代入 (2.3) 得到准确等式

$$
\boxed{s_{\zeta_0}=av,\qquad
r_{\zeta_0}=a^2(I-v^2).}
\tag{2.7}
$$

因此

$$
\boxed{F_{\zeta_0}=A^hW_{\zeta_0}Z,
\qquad Z=\sum_{j>j_0}a_j^2(I-V_j^2).}
\tag{2.8}
$$

这把首个共振的第二次除法准确识别为尾 Bell 因子 $Z$，而不是一个未明确的误差。

## 3. 在同一个未知闭核上的结论

所有 $\mathcal A$ 元素都保持 $M$。R23 的 $A^h$ 普遍限制稠密性应用于闭不变空间 $\overline{(B-r_\zeta)M}$，再用 $W_\zeta$ 及其逆保持 $M$，由 (2.6) 得

$$
\boxed{
N_\zeta:=\overline{F_\zeta M}
=\overline{(B-r_\zeta(A))M}
=\overline{(Y-s_\zeta(A))M}.
}
\tag{3.1}
$$

最后一步使用 (2.5) 中 $Y+s_\zeta$ 的单位性。
由 (1.2)，还可写成真正有界限制上的

$$
\boxed{N_\zeta=\overline{(X_M-s_\zeta(A_M))M}.}
\tag{3.2}
$$

如果 $Q_\zeta=M/N_\zeta\ne0$，那么诱导算子满足实际等式

$$
\boxed{B_{Q_\zeta}=r_\zeta(A_{Q_\zeta}),\qquad
X_{Q_\zeta}=Y_{Q_\zeta}=s_\zeta(A_{Q_\zeta}).}
\tag{3.3}
$$

这里的 $X_{Q_\zeta}$ 是有界 $X_M=Y_M$ 的商，并未把无界 $X$ 随意压缩到商空间。

令 $\mathcal B(f,g)=\langle f,Cg\rangle$。因 $T$ 与 $T_\zeta$ 都在同一真实域上 $C$ 对称，对 $f\in M,g\in M_\zeta$ 有

$$
\mathcal B(F_\zeta f,g)
=\mathcal B(T_\zeta f,g)-\mathcal B(Tf,g)=0.
$$

所以

$$
\boxed{\mathcal B(N_\zeta,M_\zeta)=0.}
\tag{3.4}
$$

要从这里推出 $\mathcal B(M,M_\zeta)=0$，仍需证明 $N_\zeta=M$，或另造一个对全部相关 $\zeta$ 有效的固定非零公共像。R152 仅保证非零 $B-r_\zeta(A)$ 在全 $H$ 单射稠密；超越慢方向没有普遍限制稠密定理。R153 的快分式结果也不能把该慢因子自动列入快场。

若 $r_\zeta-r_\xi$ 是非零解析芽，确实有

$$
\overline{N_\zeta+N_\xi}=M,
\tag{3.5}
$$

因为 $(r_\zeta-r_\xi)(A)M\subset N_\zeta+N_\xi$，而非零解析芽在 $M$ 上像稠密。
但 (3.4) 的第二个空间分别是 $M_\zeta$ 和 $M_\xi$；(3.5) 不能使它们变成同一个目标核。

## 4. 为什么增加有限个首阶 gauge 不消除根碰撞

R144 对一般单变量点态多项式给

$$
P(w)=\sum_{k=0}^{\deg q}\frac{B_k}{k!}q^{(k)}(w),
\qquad Q_\zeta-P=A^hL_\zeta,
$$

且

$$
\chi P(w)=q(w),\qquad
\chi L_\zeta(w)=\frac{\zeta^h-1}{d}\,[q(w-2a)-q(w)].
\tag{4.1}
$$

假定 $c$ 是实际剩余碰撞，即 $q(c)=q(c-2a)=0$。则同一个代数同态

$$
\operatorname{ev}_c:\mathcal A[w]\to\mathbb C,
\qquad \sum C_kw^k\mapsto\sum\chi(C_k)c^k
$$

杀掉 $P$ 及每个 $L_\zeta$。因此对任意有限个 $\zeta_1,\ldots,\zeta_n$，都不可能存在 $A_0,\ldots,A_n\in\mathcal A[w]$ 满足

$$
1=A_0P+\sum_{i=1}^n A_iL_{\zeta_i}.
\tag{4.2}
$$

这是真正的有限 gauge 首阶单位消元障碍：所有首阶差在字符层面带着相同的碰撞根，增加数量不改变该事实。
更深的清分母证书可以包含非零快因子，R173/R180 已给联合核结论；但若证书同时用不同 $Q_{\zeta_i}$，跨核配对中并没有一个向量同时属于全部目标核。联合循环因而不能被当作原单向量循环。

对 $q(w)=w^2-a^2$，唯一碰撞根为 $c=a$，而 (2.6) 已把继续消元所需的慢第二因子完全写出。

## 5. 不同 gauge 的解析根确实有无限多个

设第一和第二个非零系数分别为 $a=a_{j_0}$ 与 $b=a_{j_1}$，其中 $j_1>j_0$，并假定 $b\ne a$。置

$$
n=2^{j_1-j_0}\ge2,\quad x=A^h/d,\quad
\rho=d_{j_1}/d^n,\quad u=\zeta^h,
\quad H_n(u)=\frac{u^n-1}{u-1}=1+u+\cdots+u^{n-1}.
$$

以下是固定有限阶的解析芽计算，故不涉及无界 $X$ 的形式求值。
记 $v(x)=(1-x)/(1+x)$，将 $D=D_0+D_1+O(x^{2n})$、$E=E_0+E_1+O(x^{2n})$ 分出前两非零位，则

$$
D_0=a(v(ux)-v(x)),\quad E_0=-a(v(ux)+v(x))D_0,
$$

$$
D_1=-\frac{2b(u^n-1)}\rho x^n+O(x^{2n}),\qquad
E_1=\frac{4b^2(u^n-1)}\rho x^n+O(x^{2n}).
$$

由于 $D_0=-2a(u-1)x+O(x^2)$，除法给

$$
\frac ED=\frac{E_0}{D_0}
-\frac{2b(b-a)}{a\rho}H_n(u)x^{n-1}+O(x^n).
$$

所以

$$
\boxed{
s_\zeta=av(x)+\frac{b(b-a)}{a\rho}H_n(u)x^{n-1}+O(x^n),
}
\tag{5.1}
$$

进而

$$
\boxed{
r_\zeta=a^2(1-v(x)^2)
-\frac{2b(b-a)}\rho H_n(u)x^{n-1}+O(x^n).
}
\tag{5.2}
$$

dyadic $u\ne1$ 有无限多个，非恒定多项式 $H_n$ 在其中取无限多个不同值。因此 $r_\zeta$ 至少有无限多个不同解析芽。
规范交替幂行 $a_j=(-1)^j(j+1)^{-\sigma}$、$1/2<\sigma\le1$ 满足此假设，且 $j_0=0,j_1=1,n=2,H_2(u)=1+u$。

## 6. 规范 Bell 非解析性及公共像排除所需的边界输入

先验证以后使用的非零性，而不从边界核的存在倒推。
由

$$
I-V_j^2=4\sum_{k\ge1}(-1)^{k-1}kA^{k2^j}/d_j^k,
$$

规范行的 $B$ 在次数 $2^m$ 的忠实形式系数为

$$
\beta_{2^m}=\frac{4a_m^2}{d_m}
-4\sum_{j<m}\frac{2^{m-j}a_j^2}{d_j^{2^{m-j}}}.
\tag{6.1}
$$

递推 $N_j^2=\eta_jN_{j+1}$ 给

$$
\frac{d_m}{d_j^{2^{m-j}}}
=\eta_j^{2^{m-j-1}}\eta_{j+1}^{2^{m-j-2}}\cdots\eta_{m-1}
\le\eta_{m-1}.
$$

所以 (6.1) 的低位部分乘 $d_m$ 后，绝对值至多
$4\,2^m\|a\|_2^2\eta_{m-1}$。由
$\eta_{m-1}\le e^{-770\,16^{m-1}}$ 及
$|a_m|^2=(m+1)^{-2\sigma}$，充分大的 $m$ 满足

$$
|\beta_{2^m}|\ge \frac{2(m+1)^{-2\sigma}}{d_m}.
\tag{6.2}
$$

实际权的准确公式为

$$
-\log d_m=100\,16^m-105\,8^m+(150m+25)2^m.
$$

因此 $|\beta_{2^m}|^{1/2^m}\to\infty$，$B$ 的形式级数收敛半径为零，不能等于任何真解析 $r(A)$。R152 的忠实性及加性解析 gauge 定理遂说明：对每个真解析 $r$，$B-r(A)$ 实际非零，且单射稠密；二元解析求值 $F\mapsto F(A,B)$ 也忠实。

本节以下所需输入见 [boundary 完整证明的定理 1.1 及 §§2–8](R223-bell-minus-arbitrary-analytic-germ-boundary-kernels.md)。该证明已经逐项核验真实空白间隔预解式、复系数块右逆、迭代误差以及保留坐标。对规范慢系数

$$
a_j=(-1)^j(j+1)^{-\sigma},\qquad 1/2<\sigma\le1,
$$

记实际 UHF 代数的负整数边界表示为 $\pi$，$A_-=\pi(A)$。对任意真解析零常数芽 $r$，存在

$$
0\ne f_r\in\ker\pi(B-r(A))
\tag{6.3}
$$

且 $f_r$ 不属于任何有限标准旗 $\operatorname{span}\{e_0,\ldots,e_k\}$。
原始 Bell 算子正是

$$
B=\sum_j4(j+1)^{-2\sigma}N_j(I+N_j)^{-2}.
\tag{6.4}
$$

该边界定理对任意固定的真解析头给独立常数与起始尺度；它不要求这些常数随 $\zeta$ 一致。全纯演算通过足够小圆上的预解式估计，所以也允许解析芽半径小于 $\|A\|$。

另用已有边界事实：若 $g$ 是非零真解析芽，$g(z)=z^k v(z)$、$v(0)\ne0$，则

$$
\ker g(A_-)=\ker A_-^k
=\operatorname{span}\{e_0,\ldots,e_{k-1}\}.
\tag{6.5}
$$

因此 (6.3) 的无限支持向量不能被任何非零真解析 $g(A_-)$ 杀掉。

## 7. 全空间公共像在单 Bell 解析分式场中必为零

先给一个不要求未知商属于 UHF 的单因子引理。

**引理 7.1。** 假定 (6.3)。设 $F\in\mathbb C\{z,w\}$，且存在 $C\in\{A\}'$ 有界，使

$$
F(A,B)=(B-r(A))C.
\tag{7.1}
$$

则

$$
F(z,r(z))\equiv0,
\qquad F(z,w)=(w-r(z))G(z,w)
\tag{7.2}
$$

对某个真二元解析芽 $G$ 成立。

**证明。** 因 $C$ 与 $A$ 交换，它与 $B-r(A)$ 交换，故

$$
\|F(A,B)x\|\le\|C\|\,\|(B-r(A))x\|.
\tag{7.3}
$$

式中两算子都属于实际 UHF 代数，而 Haar 表示忠实。因此 UHF 元素

$$
\|C\|^2(B-r(A))^*(B-r(A))-F(A,B)^*F(A,B)
$$

为正，其正性在 $\pi$ 下保持。由 (6.3)，$\pi(F(A,B))f_r=0$。
在闭 $A_-$ 不变核 $\ker\pi(B-r(A))$ 上，$\pi B=r(A_-)$；绝对范数收敛的二元解析演算遂给

$$
F(A_-,r(A_-))f_r=0.
$$

(6.5) 迫 $F(z,r(z))\equiv0$。最后令 $w=r(z)+v$，常数项为零的解析芽可被 $v$ 整除，得 (7.2)。证毕。

**定理 7.2。** 假定 (6.3)，且 $\{r_\zeta\}$ 含无限多个不同解析芽。若某个

$$
R=F(A,B),\qquad F\in\mathbb C\{z,w\},
$$

满足

$$
\operatorname{Ran}R\subseteq\operatorname{Ran}(B-r_\zeta(A))
\quad\text{对每个相关 }\zeta,
\tag{7.4}
$$

则 $F=0$，从而 $R=0$。

**证明。** §6 已独立证明每个 $S_\zeta=B-r_\zeta(A)$ 实际非零，且由 R152 单射。
由 (7.4)，最大闭商 $C_\zeta=S_\zeta^{-1}R$ 全域定义，闭图定理给有界性；由 $S_\zeta$ 单射可取消并验证 $C_\zeta A=AC_\zeta$。
引理 7.1 于是给 $F(z,r_\zeta(z))=0$。

若 $F\ne0$，先提取最大的公共 $z$ 次幂，再用固定 $z$ 坐标的 Weierstrass 准备，写

$$
F(z,w)=z^kU(z,w)P(z,w),
$$

其中 $U$ 为解析单位，$P$ 为有限次数首一 $w$ 多项式。每个不同 $r_\zeta\in\mathbb C\{z\}\subset\mathbb C((z))$ 都是 $P$ 的根；一个非零有限次数多项式不能有无限多个不同域内根，矛盾。证毕。

### 7.1 清一个真实解析分母后的加强

允许 $R\in\{A\}'$ 本身不属于 UHF，只要求它是单 Bell 二元解析分式的有界实现，即存在 $P,Q\in\mathbb C\{z,w\}$、实际 $Q(A,B)$ 单射，满足

$$
Q(A,B)R=P(A,B).
\tag{7.5}
$$

若 (7.4) 仍成立，则 $R=S_\zeta C_\zeta$，由交换性有

$$
P(A,B)=S_\zeta\,[Q(A,B)C_\zeta].
$$

括号为有界交换子，所以引理 7.1 对 $P$ 成立。无限多个不同 $r_\zeta$ 迫 $P=0$，再由 $Q(A,B)$ 单射得 $R=0$。

因此整个单 Bell 解析分式场都不能提供非零的、对这些 gauge 同时有效的**全空间**公共像。此结论允许每个商的范数任意依赖 $\zeta$，不要求一致界，也不把商送到边界表示。

### 7.2 相同的闭理想交结论

对 $J_\zeta=\overline{(B-r_\zeta(A))\mathcal A}^{\|\cdot\|}$，若 $R=F(A,B)\in J_\zeta$，连续边界表示直接说明 $\pi R$ 杀掉 (6.3) 的 $f_{r_\zeta}$。因此引理 7.1 后半段仍给 $F(z,r_\zeta(z))=0$。无限根论证遂给

$$
\boxed{\bigcap_\zeta J_\zeta\ \cap\ \{F(A,B):F\in\mathbb C\{z,w\}\}=\{0\}.}
\tag{7.6}
$$

若公共元素是 §7.1 的有界解析分式且属于这些闭理想，乘同一个有界解析分母使其分子也属于全部 $J_\zeta$，同理迫元素为零。这里只排相应解析分式子类，没有宣称 $\bigcap_\zeta J_\zeta=0$ 对整个 $\mathcal A$ 成立。

## 8. 准确范围

本稿没有排除未知 $M$ 特有的包含

$$
RM\subseteq (B-r_\zeta(A))M,
$$

因为只在 $M$ 上成立的范数不等式不自动给 UHF 中的全空间正序，也不能送到负整数边界。
它也没有排除单 Bell 解析分式场之外的全空间公共像。

已得到的确定信息是：

1. 每个 dyadic gauge 的剩余除法都是明确的 $(B-r_\zeta(A))_M$；最低位翻转就是尾 Bell $Z_M$。
2. 有限个首阶 gauge 共享同一个字符碰撞根，不能产生单位消元；不同余因子的联合稠密像仍对应不同目标核。
3. 对规范慢行，若采用全空间解析分式公共像方案，任意解析头的真实边界核会把该方案排除。尚有用的公共像必须依赖原未知核，或越出这个解析分式场，并支付真实有界预算。

输入：R23；R125；R144 及平方附录；R152/R153；R173/R178；实际 UHF 与负整数边界的忠实性及标准有限旗；[boundary 的完整任意解析头 Bell 核定理](R223-bell-minus-arbitrary-analytic-germ-boundary-kernels.md)。
