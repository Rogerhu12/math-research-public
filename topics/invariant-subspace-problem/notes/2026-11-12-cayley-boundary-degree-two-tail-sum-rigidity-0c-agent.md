# R205：Cayley 慢边界符号的二阶孔次数刚性

日期：2026-11-12（UTC）。作者：l2_moments。状态：完整实际算子证明。

本文处理 R188 的实际 Cayley 慢符号。证明只覆盖边界孔次数不超过二；不把 R202 对另一个符号的全有限次数结论自动移植过来，也不决定边界像的饱和问题 $N=M$。

## 1. 结论与两种有限性

在 R174 的负整数边界表示中，
$$
\mathcal H_-=\ell^2(\mathbb N_0),\qquad
Be_0=0,\qquad Be_n=\alpha_{v_2(n)}e_{n-1}\quad(n\ge1).
$$
沿用实际正权 $\alpha_j$。本文只使用它们严格递减、非零，以及已有的归一化幂和逆界。
记
$$
W_0=1,\qquad W_n=\prod_{\nu=1}^n\alpha_{v_2(\nu)},\qquad
d_j=W_{2^j},\qquad
\mathsf N_j=B^{2^j}/d_j,\qquad
\mathsf Y_j=\mathsf N_j(I+\mathsf N_j)^{-1}.
\tag{1.1}
$$
有 $\|\mathsf N_j\|=1$、$\|(I+\mathsf N_j)^{-1}\|\le3$。
因此
$$
T_Y=\sum_{j\ge0}a_j\mathsf Y_j,\qquad a_j=(j+1)^{-2},
\tag{1.2}
$$
按算子范数绝对收敛。

对有限集 $S\subseteq\mathbb N_0$，写
$$
n(S)=\sum_{j\in S}2^j,\qquad e_S=e_{n(S)}.
$$
定义孔次数空间和有限物理头
$$
\mathcal H^-_{\le p}
=\overline{\operatorname{span}}\{e_S:|S|\le p\},
\qquad
\mathcal F_m=\operatorname{span}\{e_n:0\le n<2^m\}\quad(m\ge0).
\tag{1.3}
$$
特别 $\mathcal F_0=\mathbb Ce_0$。有限孔次数允许孔的位置无限远，有限头则只允许有限多个物理位。这里的 $e_S$ 是边界孔基，不是原 Haar 空间的 Walsh 基。

**定理1.1。** 若 $m\ge0$，且
$$
x\in\mathcal H^-_{\le2},\qquad T_Yx\in\mathcal F_m,
$$
则
$$
\boxed{x\in\mathcal F_{\max(4,m)+2}.}
\tag{1.4}
$$
因此，对 R188 的非平凡边界核 $M_Y=\ker T_Y$，
$$
\boxed{M_Y\cap\mathcal H^-_{\le2}=\mathbb Ce_0.}
\tag{1.5}
$$
证明利用最低物理位分块后的精确 Cayley 系数，以及两条共享同一高位尾和的矩阵行。整个论证不需要未知向量的额外尾速率。

## 2. 最低物理位的实际分块

按偶数、奇数坐标识别
$$
\mathcal H_-=\widehat{\mathcal H}_-\oplus\widehat{\mathcal H}_-,
\qquad
e_{2n}\leftrightarrow(e_n,0),\qquad
e_{2n+1}\leftrightarrow(0,e_n).
\tag{2.1}
$$
帽号表示删去最低物理位后的尾空间。令
$$
\beta=\alpha_0,\qquad
Ce_0=0,\qquad Ce_n=w_ne_{n-1},\qquad
w_n=\alpha_{1+v_2(n)},\qquad Q=C/\beta.
$$
直接由实际权得到
$$
B=\begin{pmatrix}0&\beta I\\ C&0\end{pmatrix},
\qquad
\mathsf N_0=\begin{pmatrix}0&I\\ Q&0\end{pmatrix},
\qquad
\mathsf N_0^2=\begin{pmatrix}Q&0\\0&Q\end{pmatrix}.
\tag{2.2}
$$
因为 $\|Q\|=\alpha_1/\alpha_0<1$，$I-Q$ 可逆。
由 $(I+\mathsf N_0)^{-1}=(I-\mathsf N_0)(I-\mathsf N_0^2)^{-1}$，
$$
\boxed{
\mathsf Y_0
=(I-Q)^{-1}\begin{pmatrix}-Q&I\\Q&-Q\end{pmatrix}.
}
\tag{2.3}
$$
这里 $I-Q$ 在两分量上按相同对角算子作用。

尾权和尾归一化幂定义为
$$
\widehat W_0=1,\qquad
\widehat W_n=\prod_{\nu=1}^n w_\nu,\qquad
\widehat d_j=\widehat W_{2^j},\qquad
\widehat{\mathsf N}_j=C^{2^j}/\widehat d_j,\qquad
\widehat{\mathsf Y}_j=\widehat{\mathsf N}_j(I+\widehat{\mathsf N}_j)^{-1}.
\tag{2.4}
$$
特别
$$
\widehat d_0=\alpha_1,\qquad
\widehat d_1=\alpha_1\alpha_2,\qquad
\frac{\widehat d_1}{\widehat d_0^2}=\frac{\alpha_2}{\alpha_1}<1.
\tag{2.5}
$$
对 $j\ge1$，分组奇偶权给
$$
d_j=\beta^{2^{j-1}}\widehat d_{j-1},\qquad
\mathsf N_j=\begin{pmatrix}\widehat{\mathsf N}_{j-1}&0\\0&\widehat{\mathsf N}_{j-1}\end{pmatrix}.
\tag{2.6}
$$
因此对应 Cayley 变换也有同一对角式。

记
$$
b_j=a_{j+1}=(j+2)^{-2},\qquad
D=\sum_{j\ge0}b_j\widehat{\mathsf Y}_j.
\tag{2.7}
$$
$D$ 是真实有界尾算子，并与 $C,Q$ 交换。由 $a_0=1$，(2.3) 和 (2.6) 给
$$
\boxed{
T_Y=(I-Q)^{-1}
\begin{pmatrix}(I-Q)D-Q&I\\Q&(I-Q)D-Q\end{pmatrix}.
}
\tag{2.8}
$$
这是精确等式，没有以纯消灭算子替换任一真实幂。

## 3. 输入次数分配与输出头部

写
$$
x=(u,v),\qquad f=T_Yx=(f_0,f_1)
$$
为 (2.1) 中的两分量。原第0位为1会占用一个孔，所以
$$
u\in\widehat{\mathcal H}^-_{\le2},\qquad
v\in\widehat{\mathcal H}^-_{\le1}.
\tag{3.1}
$$
故存在 $c_*\in\mathbb C$ 和 $(c_j)\in\ell^2$，使
$$
v=c_*e_0+\sum_{j\ge0}c_je_{2^j}.
\tag{3.2}
$$
若 $f\in\mathcal F_m$，则 $m\ge1$ 时
$$
f_0,f_1\in\widehat{\mathcal F}_{m-1};
\tag{3.3}
$$
$m=0$ 时 $f_1=0$。每个尾有限头都由 $Q,D$ 保持。

令 $g=Dv$。从 (2.8) 的下行得到
$$
\boxed{Qu=Qv-g+Qg+(I-Q)f_1.}
\tag{3.4}
$$
在坐标 $n-1$ 上，$n\ge1$，这等价于
$$
u_n=v_n+g_n-\frac\beta{w_n}g_{n-1}
+\frac\beta{w_n}\bigl((I-Q)f_1\bigr)_{n-1}.
\tag{3.5}
$$
令 $\nu(n)$ 表示 $n$ 的二进位1的数目。若 $\nu(n)\ge3$，且 $n-1$ 位于 $(I-Q)f_1$ 的有限头之外，则 (3.1) 给 $u_n=v_n=0$，从而
$$
\boxed{g_n-\frac\beta{w_n}g_{n-1}=0.}
\tag{3.6}
$$
这一行约束正是后面消元所需的全部信息。

## 4. 实际 Cayley 系数与坐标级数

令 $t_k$ 为 $D$ 作为 $C$ 的形式幂系数。对每个固定 $k\ge1$，只有有限个除数 $2^l$ 能贡献，精确地
$$
\boxed{
t_k=\sum_{l:\,2^l\mid k}
b_l(-1)^{k/2^l-1}\widehat d_l^{-k/2^l},\qquad t_0=0.
}
\tag{4.1}
$$
其证明完全在有限矩阵列上进行：$C$ 在每个有限头上幂零，故
$$
\widehat{\mathsf Y}_l
=\sum_{s\ge1}(-1)^{s-1}\widehat d_l^{-s}C^{s2^l}
$$
作用于任意固定有限头时是有限和；当 $2^l$ 超过该头时，整项严格为零。
因此 (4.1) 不要求形式幂级数有正收敛半径。

特别，
$$
t_k=b_0\widehat d_0^{-k}\qquad(k\text{ 为奇数}),
\tag{4.2}
$$
而当 $v_2(k)=1$ 时，
$$
t_k=b_1\widehat d_1^{-k/2}-b_0\widehat d_0^{-k}.
\tag{4.3}
$$

从单列 $e_{2^j}$ 的实际加权后移矩阵元得到
$$
(De_{2^j})_n
=\frac{\widehat d_j}{\widehat W_n}\,t_{2^j-n}
\quad(0\le n<2^j),
\tag{4.4}
$$
且 $n\ge2^j$ 时该坐标为零。$De_0=0$。
于是对于 (3.2)，
$$
\boxed{
g_n=\frac1{\widehat W_n}
\sum_{j:\,2^j>n}c_j\widehat d_jt_{2^j-n}.
}
\tag{4.5}
$$
这个坐标级数绝对收敛：由有界性，
$$
\sum_j |(De_{2^j})_n|^2\le\|D^*e_n\|^2,
$$
再与 $(c_j)\in\ell^2$ 使用 Cauchy–Schwarz。这样先证明坐标级数的合法性，再使用显式系数拆分，避免交换未经控制的无穷和。

## 5. 两个共享尾和的合法性

对 $r\ge4$ 定义
$$
U_r=\sum_{j\ge r}c_j\widehat d_j\widehat d_0^{-2^j},
\qquad
V_r=\sum_{j\ge r}c_j\widehat d_j\widehat d_1^{-2^{j-1}}.
\tag{5.1}
$$
两者均绝对收敛。为看清这一点，直接使用实际权的分组，而非依赖形式系数的大小猜测。

对 $j\ge1$，$1\le\nu\le2^j$ 中有 $2^{j-1}$ 个偶数。其权至多为 $\alpha_2$，奇数的权等于 $\alpha_1$，故
$$
0<\frac{\widehat d_j}{\widehat d_0^{2^j}}
\le\left(\frac{\alpha_2}{\alpha_1}\right)^{2^{j-1}}.
\tag{5.2}
$$
对第二个比值，将权按相邻的奇偶对分组。第 $l$ 对的乘积为
$$
w_{2l-1}w_{2l}
=\alpha_1\alpha_{2+v_2(l)}.
$$
当 $l$ 为奇数时恰为 $\widehat d_1=\alpha_1\alpha_2$；
当 $l$ 为偶数时至多是 $\widehat d_1(\alpha_3/\alpha_2)$。
因此对 $j\ge2$，
$$
0<\frac{\widehat d_j}{\widehat d_1^{2^{j-1}}}
\le\left(\frac{\alpha_3}{\alpha_2}\right)^{2^{j-2}}.
\tag{5.3}
$$
右边都是关于 $j$ 的双指数衰减列，尤其属于 $\ell^2$。
与 $c\in\ell^2$ 再次使用 Cauchy–Schwarz，即得 (5.1) 的绝对收敛。
此后可以对 $U_r,U_{r+1}$ 逐项相减。

## 6. 两条真实矩阵行强制全部高位一孔系数为零

置
$$
r_0=\max(4,m).
$$
固定任意 $r\ge r_0$，选
$$
n=2^r-1,\qquad n'=2^r-5=n-4.
\tag{6.1}
$$
这两个整数都严格位于 $(2^{r-1},2^r)$，且都模4等于3。
它们的孔次数分别是 $r$ 和 $r-1$，均至少为3。
另外
$$
n'-1=2^r-6\ge2^{\max(m-1,0)}.
$$
结合 (3.3)，$(I-Q)f_1$ 在 $n-1,n'-1$ 上都为零。因此 (3.6) 对这两个 $n$ 同时成立。

对任一所选 $n$，(4.5) 中 $g_n,g_{n-1}$ 的源指标恰好都是 $j\ge r$。
乘 (3.6) 以 $\widehat W_n$，并用 $w_n=\widehat W_n/\widehat W_{n-1}$，得到
$$
\sum_{j\ge r}c_j\widehat d_j
\bigl(t_{2^j-n}-\beta t_{2^j-n+1}\bigr)=0.
\tag{6.2}
$$
因为 $n\equiv3\pmod4$ 且 $j\ge r\ge4$，
$$
2^j-n\equiv1\pmod4,
\qquad
v_2(2^j-n+1)=1.
$$
所以 (4.2)—(4.3) 给
$$
\begin{split}
t_{2^j-n}-\beta t_{2^j-n+1}
&=b_0(1+\beta/\widehat d_0)
  \widehat d_0^{n}\widehat d_0^{-2^j}\\
&\quad-\beta b_1\widehat d_1^{(n-1)/2}
  \widehat d_1^{-2^{j-1}}.
\end{split}
\tag{6.3}
$$
由第5节的绝对收敛，(6.2) 等价于
$$
A_nU_r-B_nV_r=0,
\tag{6.4}
$$
其中
$$
A_n=b_0(1+\beta/\widehat d_0)\widehat d_0^n,
\qquad
B_n=\beta b_1\widehat d_1^{(n-1)/2}.
\tag{6.5}
$$
$b_0=1/4,b_1=1/9$，所以所有这些系数非零。
对 $n'=n-4$ 得同一对 $U_r,V_r$ 的第二条方程。
两个系数比是
$$
\frac{A_n}{A_{n-4}}=\widehat d_0^4,
\qquad
\frac{B_n}{B_{n-4}}=\widehat d_1^2.
\tag{6.6}
$$
由 (2.5)，两者不相等。
故两行组成的 $2\times2$ 矩阵可逆，得到
$$
\boxed{U_r=V_r=0\qquad(r\ge r_0).}
\tag{6.7}
$$
最后，(5.1) 的逐项相减给
$$
0=U_r-U_{r+1}
=c_r\widehat d_r\widehat d_0^{-2^r}.
$$
实际权都非零，因而
$$
\boxed{c_r=0\qquad(r\ge r_0).}
\tag{6.8}
$$
这里没有使用 $c_r$ 的定量下界，也没有用紧性或密集类近似替代消元。

## 7. 从奇分量有限头恢复整个输入

(6.8) 说明
$$
v\in\widehat{\mathcal F}_{r_0}.
$$
因此 $Qv,Dv,QDv$ 都属于同一个尾有限头。
同时 $f_1\in\widehat{\mathcal F}_{r_0}$ 或 $f_1=0$。
由精确方程 (3.4)，
$$
Qu\in\widehat{\mathcal F}_{r_0}.
\tag{7.1}
$$
$Q$ 是所有权都非零的单步后移，所以对 $n\ge2^{r_0}$，
$$
0=(Qu)_n=\frac{w_{n+1}}\beta u_{n+1}.
$$
故 $u_k=0$ 对所有 $k\ge2^{r_0}+1$ 成立，特别
$$
u\in\widehat{\mathcal F}_{r_0+1}.
\tag{7.2}
$$
重新放回最低位时，尾指标乘2，奇分量再加1；于是
$$
x\in\mathcal F_{r_0+2},
$$
证明 (1.4)。所给支撑界不追求最优，但每个有限头参数均已明确。

## 8. 核结论及适用边界

每个 $\mathcal F_s$ 都由 $T_Y$ 保持。在该有限头上，各 Cayley 逆化为有限多项式，$T_Y$ 是有限加权后移 $B_s$ 的无常数多项式，首项为
$$
\frac{a_0}{d_0}B_s=\frac1\beta B_s.
$$
因此
$$
T_Y|_{\mathcal F_s}=B_sU_s,
$$
其中 $U_s$ 是与 $B_s$ 交换的可逆有限矩阵。于是
$$
\ker(T_Y|_{\mathcal F_s})=\ker B_s=\mathbb Ce_0.
\tag{8.1}
$$
将 (1.4) 用于 $T_Yx=0$，再用 (8.1)，即得 (1.5)。

R188 已构造 $M_Y$ 中的非真空向量。因此本稿说明这些向量不可能只有0、1、2阶孔分量。它尚未证明每个非真空向量都具有无界孔次数：对于 $p\ge3$，最低位分块后的奇分量有 $p-1$ 阶，(4.5) 不再只是一孔源的两个共享尾和。

另记 $N_Y=\overline{BM_Y}$。本稿没有证明 $N_Y=M_Y$。即使有限孔次数空间在整个边界 Hilbert 空间中稠密，它与 $M_Y$ 的交也不必在 $M_Y$ 中稠密；不能用 (1.5) 对未知核作该推断。

最后，本文始终在负整数边界表示内工作，没有构造到原 Haar 表示的有界交织，也没有从边界核推出原空间的非平凡不变子空间。

## 9. 内部来源

- R174：实际负整数边界表示、权与有限头结构；
- [R188：零锚有界第一 chaos 的非标准闭主理想](../results/R188-critical-first-chaos-nonstandard-closed-principal-ideal.md)：$T_Y$ 的范数收敛、实际逆界及非真空边界核；
- [R200：边界标准右移域与前向除法饱和](../results/R200-boundary-right-shift-domains-and-forward-division-saturation.md)：Cayley 的有限列形式系数与待解决的 $N=M$；
- [R202：慢边界符号的有限孔次数刚性](../results/R202-slow-boundary-finite-hole-degree-rigidity.md)：另一个慢符号 $T_N$ 的唯一长进位机制，用于比较适用范围。

本稿第2—7节的分块、系数、绝对收敛和消元均在此独立给出。
