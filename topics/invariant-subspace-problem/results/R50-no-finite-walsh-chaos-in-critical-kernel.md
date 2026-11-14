# R50：原临界核中不存在非零有限 Walsh 阶向量

日期：2026-11-12（UTC+8）。主会话 Astra-ISP-0c017065 提出前缀/尾部近似和向下消元机制；`l2_moments` 补齐全尾 creation 交换子左界与统一常数。

**状态：已证明的中间结论。** 这是对 R28/R43 原临界算子 $D=I-Q$ 本身的结论，不是对无进位替代模型的结论。它覆盖全部有限 Walsh chaos，包括无限秩系数和任意慢的系数尾；不要求整数迹存在。尚未排除无限 Walsh 次数的核向量，因此未决定 $D$ 的单射性及原临界向量的循环性，更未解决一般 ISP。

依赖 R9/R12 的有限链及归一化 dyadic 幂、R43 的对数与核等价，以及 R44 引理 2.1 的精确截断误差。下面给出近似、creation 左界及核排除的完整证明。

## 1. 原算子与主定理

仍令 $H=L^2(\mathbb Z_2,\mu)$，$\chi_j=(-1)^{b_j}$、$\chi_S=\prod_{j\in S}\chi_j$，

$$
(Af)(y)=w(y)f(y-1),\qquad w(y)=a_{v_2(y)},\quad w(0)=0,
$$

$$
a_j=e^{-L_j},\qquad
L_j=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3}.
$$

记

$$
N_j=\frac{A^{2^j}}{\|A^{2^j}\|},\qquad
\eta_j=\frac{a_{j+1}}{a_j},\qquad
\delta_j=\frac{2}{(j+2)^2+1},\qquad r_j=1-\delta_j.
\tag{1.1}
$$

原临界对数为

$$
L=\sum_{j\ge0}h_j(N_j),\qquad
h_j(T)=\log(I+T)-\log(I+r_jT).
\tag{1.2}
$$

R43 已证明此级数范数绝对收敛，且 $\ker L=\ker D$，其中

$$
Q=\prod_{j\ge0}(I+r_jN_j)(I+N_j)^{-1},\qquad D=I-Q.
$$

对 $d\ge0$ 定义闭空间

$$
H_{\le d}=\overline{\operatorname{span}}\{\chi_S:|S|\le d\}.
$$

**定理 1.1。** 对每个有限 $d$，

$$
\boxed{\ker L\cap H_{\le d}=\ker D\cap H_{\le d}=\{0\}.}
\tag{1.3}
$$

向量可含无限多个 Walsh 系数；这里只限制每项的次数，不限制涉及的最高位，也不要求有限秩张量结构。

## 2. 保留低位真实作用、将尾部替换成独立矩阵单位

记 $A_m$ 为删除 $v_2(y)\ge m$ 权的幂零截断。它在分解

$$
H=H_{<m}\otimes H_{\ge m}
$$

中只作用于低 $m$ 位。对 $j<m$ 置

$$
N_j^{[m]}=\frac{A_m^{2^j}}{\|A^{2^j}\|}.
$$

R12/R44 给出

$$
\|N_j\|\le1,\quad \|N_j^2\|\le\eta_j,
\quad\|N_j-E_j\|=\eta_j,
\tag{2.1}
$$

$$
\|N_j^{[m]}\|\le1,\quad
\|(N_j^{[m]})^2\|\le\eta_j,\quad
\|N_j-N_j^{[m]}\|=a_m/a_j.
\tag{2.2}
$$

这里 $E_j$ 在第 $j$ 位的物理基上为 $e_{10}$，在其他位上为恒等。式 (2.2) 的误差不是未经归一化的 $a_m$：每条长 $2^j$ 的路径只有一个赋值至少为 $j$ 的特殊权，截断部分的最大特殊权为 $a_m$，归一化后的精确比值是 $a_m/a_j$。

### 2.1 对数差的统一 Lipschitz 界

设 $\theta=\eta_0=e^{-1070}<1/4$。对于 $\|T\|\le1$、$\|T^2\|\le\theta$ 和 $s\in[0,1]$，

$$
(I+sT)^{-1}=(I-sT)(I-s^2T^2)^{-1},\qquad
\|(I+sT)^{-1}\|\le\frac2{1-\theta}\le\frac83.
\tag{2.3}
$$

幂级数按范数一致收敛，逐项积分给

$$
h_j(T)=\int_{r_j}^1 T(I+sT)^{-1}\,ds.
\tag{2.4}
$$

所以 $\|h_j(T)\|\le(8/3)\delta_j$。对两个满足相同条件的算子 $T,S$，不要求彼此交换，有精确预解式差恒等式

$$
T(I+sT)^{-1}-S(I+sS)^{-1}
=(I+sT)^{-1}(T-S)(I+sS)^{-1}.
$$

从而

$$
\boxed{\|h_j(T)-h_j(S)\|
\le\frac{64}{9}\delta_j\|T-S\|.}
\tag{2.5}
$$

另外，由 $h_j(N_j)$ 的幂展开，

$$
\begin{aligned}
\|h_j(N_j)-\delta_jN_j\|
&\le\delta_j\sum_{k\ge2}\eta_j^{\lfloor k/2\rfloor}\\
&=\frac{2\delta_j\eta_j}{1-\eta_j}.
\end{aligned}
$$

结合 (2.1)，得到

$$
\boxed{\|h_j(N_j)-\delta_jE_j\|
\le\frac{11}{3}\delta_j\eta_j.}
\tag{2.6}
$$

### 2.2 真实模型的近似误差

令 $G_m$ 为低位算子

$$
G_m=\sum_{j<m}h_j(N_j^{[m]})\big|_{H_{<m}},
$$

并令

$$
B_m=\sum_{j\ge m}\delta_jE_j\big|_{H_{\ge m}},\qquad
T_m=G_m\otimes I+I\otimes B_m.
\tag{2.7}
$$

所有和都按范数收敛。记 $\Delta=\sum_j\delta_j$；由 $\delta_j\le2/(j+2)^2$ 和望远镜比较，有 $\Delta\le2$。

$\eta_j$ 随 $j$ 严格递减。事实上

$$
-\log\eta_j=1400\,16^j-630\,8^j+300\,2^j,
$$

其相邻差为 $21000\,16^j-4410\,8^j+300\,2^j>0$。

对前缀应用 (2.2)、(2.5)，得到

$$
\sum_{j<m}\|h_j(N_j)-h_j(N_j^{[m]})\|
\le\frac{64}{9}\sum_{j<m}\delta_j\frac{a_m}{a_j}
\le\frac{64}{9}\Delta\eta_{m-1}.
$$

对尾部应用 (2.6)，得到误差至多 $(11/3)\Delta\eta_m$。故对 $m\ge1$，

$$
\boxed{\|L-T_m\|\le22\eta_{m-1}.}
\tag{2.8}
$$

同时

$$
\|G_m\|\le\frac83\Delta,\qquad
\|B_m\|\le\Delta,\qquad
\boxed{\|T_m\|\le\frac{22}{3}<8.}
\tag{2.9}
$$

这些界与 $m$ 无关。$T_m$ 仅是近似工具，下面会把 (2.8) 的全部误差保留到最终核论证。

## 3. 全尾 creation 的定量左界

对尾位 $j\ge m$，在 Walsh 基上定义

$$
c_j\chi_S=
\begin{cases}\chi_{S\cup\{j\}},&j\notin S,\\0,&j\in S,\end{cases}
\qquad b_j=c_j^*,\qquad n_j=c_jb_j.
\tag{3.1}
$$

$c_j$ 是升阶算子，$b_j$ 是降阶算子，$n_j$ 是“集合含 $j$”的正交投影。各算子范数为一。不同位上的算子交换，同一位满足

$$
[b_j,c_j]=I-2n_j.
$$

设

$$
\mathsf C_m=\sum_{j\ge m}\delta_jc_j,\qquad
\mathsf A_m=\mathsf C_m^*,\qquad
\mathsf N_m=\sum_{j\ge m}\delta_jn_j,
$$

$$
s_m=\sum_{j\ge m}\delta_j,\qquad
\sigma_m^2=\sum_{j\ge m}\delta_j^2.
\tag{3.2}
$$

因为 $\delta\in\ell^1$，这些是整个尾 Hilbert 空间上的有界、按范数收敛的算子。先对有限和计算，再取范数极限，得到精确交换关系

$$
\boxed{[\mathsf A_m,\mathsf C_m]
=\sigma_m^2I-2\sum_{j\ge m}\delta_j^2n_j.}
\tag{3.3}
$$

记尾部纯 $k$ 阶空间为 $\mathcal H_k^{(m)}$。若 $u\in H_{<m}\otimes\mathcal H_k^{(m)}$，则

$$
\sum_{j\ge m}\langle (I\otimes n_j)u,u\rangle=k\|u\|^2;
$$

这由 Walsh 系数展开和非负项的 Tonelli 求和直接成立。因此 (3.3) 给

$$
\begin{aligned}
\|(I\otimes\mathsf C_m)u\|^2
&=\|(I\otimes\mathsf A_m)u\|^2
+\sigma_m^2\|u\|^2
-2\sum_{j\ge m}\delta_j^2\langle(I\otimes n_j)u,u\rangle\\
&\ge(\sigma_m^2-2k\delta_m^2)\|u\|^2.
\end{aligned}
\tag{3.4}
$$

这里使用 $\delta_j$ 递减。所有结论允许任意低位 Hilbert 空间系数，常数不随低位维数增长。

置 $M=m+2$。由

$$
\frac1{(j+2)^2}\le\delta_j\le\frac2{(j+2)^2}
$$

及递减函数积分比较，

$$
\sigma_m^2\ge\sum_{j\ge m}(j+2)^{-4}
\ge\frac1{3M^3},\qquad
\delta_m^2\le\frac4{M^4}.
\tag{3.5}
$$

若 $M\ge48d$，对所有 $0\le k\le d$ 有

$$
\sigma_m^2-2k\delta_m^2
\ge\frac1{M^3}\left(\frac13-\frac{8d}{M}\right)
\ge\frac1{6M^3}.
$$

所以

$$
\boxed{
\|(I\otimes\mathsf C_m)u\|
\ge\frac1{\sqrt6\,M^{3/2}}\|u\|
\quad(0\le k\le d,\ M\ge48d).
}
\tag{3.6}
$$

这比逐个有限块反演更直接；尤其不存在把有限维单射性无常数地传到无限尾的步骤。下界的来源是尾部权的平方和 $\asymp m^{-3}$ 大于固定 $d$ 个最大权平方的总量 $O_d(m^{-4})$。

## 4. T_m 的尾次数三对角结构

在单个位的 Walsh 基 $(1,\chi_j)$ 中，

$$
E_j=\frac12\begin{pmatrix}1&1\\-1&-1\end{pmatrix}
=\frac12I+\frac12b_j-\frac12c_j-n_j.
$$

因此 (2.7) 的尾算子精确为

$$
B_m=\frac{s_m}{2}I-\mathsf N_m
+\frac12\mathsf A_m-\frac12\mathsf C_m.
\tag{4.1}
$$

它只改变尾 Walsh 次数 $-1,0,+1$。$G_m\otimes I$ 保持尾次数，尽管它在低位的真实作用不必保持低位 Walsh 次数。

令

$$
u=\sum_{k=0}^d u_k,
\qquad u_k\in H_{<m}\otimes\mathcal H_k^{(m)},
\qquad v=T_mu.
$$

记 $v_k$ 为其尾次数 $k$ 分量，并令 $u_{d+1}=0$。最高一阶满足

$$
v_{d+1}=-\frac12(I\otimes\mathsf C_m)u_d.
\tag{4.2}
$$

其余对 $1\le k\le d$ 满足

$$
v_k=-\frac12(I\otimes\mathsf C_m)u_{k-1}
+\mathcal D_{m,k}u_k
+\frac12(I\otimes\mathsf A_m)u_{k+1},
\tag{4.3}
$$

其中 $\mathcal D_{m,k}$ 是保持尾次数的对角块。由 (2.9)，它以及每个相邻阶块的范数都小于 $8$：这些块是 $T_m$ 的正交压缩，范数不超过 $\|T_m\|$。

## 5. 在有界尾次数空间上反向递推，得到多项式左界

假设 $m\ge1$、$M=m+2\ge48d$。置

$$
K_m=2\sqrt6\,M^{3/2}\ge1.
$$

由 (3.6)、(4.2)，

$$
\|u_d\|\le K_m\|v\|.
$$

再从 $k=d$ 向 $k=1$ 应用 (3.6)、(4.3)，每一步给

$$
\|u_{k-1}\|
\le K_m\bigl(\|v\|+8\|u_k\|+8\|u_{k+1}\|\bigr).
\tag{5.1}
$$

归纳得到

$$
\|u_k\|\le(17K_m)^{d-k+1}\|v\|
\qquad(0\le k\le d).
$$

核实递推常数：若已有相邻两项的界，较小指数不超过较大指数，且后者至少一，所以 (5.1) 的括号至多 $17$ 倍较大项的界，恰给下一阶。初始最高项的界也被 $(17K_m)$ 控制。

各尾次数正交，故得到明确的统一左界

$$
\boxed{
\|u\|
\le C_d M^{3(d+1)/2}\|T_mu\|,
\qquad
C_d=\sqrt{d+1}\,(34\sqrt6)^{d+1}.
}
\tag{5.2}
$$

这对整个 $H_{<m}\otimes\bigoplus_{k=0}^d\mathcal H_k^{(m)}$ 成立，不限制低位系数，也不限制每一纯阶中的无限秩。

## 6. 将真实误差带回原核方程

设 $u\in\ker L\cap H_{\le d}$。对于每个 $m$，全局 Walsh 次数不超过 $d$ 保证其尾次数也不超过 $d$，所以 (5.2) 适用。由 $Lu=0$ 和 (2.8)，

$$
\|T_mu\|\le22\eta_{m-1}\|u\|.
$$

因此对全部充分大的 $m$，

$$
\|u\|\le22C_d(m+2)^{3(d+1)/2}\eta_{m-1}\|u\|.
\tag{6.1}
$$

本模型的 $\eta_{m-1}=\exp(-1400\,16^{m-1}+630\,8^{m-1}-300\,2^{m-1})$ 比每个 $m$ 的负幂更快趋零。故 (6.1) 右边的标量系数最终小于一，迫使 $u=0$。结合 R43 的 $\ker D=\ker L$，定理 1.1 得证。

证明没有对一般核向量定义整数点值或局部迹；实际进位项全部由 (2.8) 以算子范数保留并消除。

## 7. 对临界向量的矩分离与准确边界

令 $f_*=D1$。R43 给

$$
B(A^nf_*,u)=B(A^n1,Du).
$$

由于 $1$ 对 $A$ 循环，左边全部为零当且仅当 $Du=0$。所以定理 1.1 还证明：

$$
\boxed{
u\in H_{\le d},\quad B(A^nf_*,u)=0\ (n\ge0)
\quad\Longrightarrow\quad u=0.
}
\tag{7.1}
$$

$C$ 保持有限 Walsh 次数，因此同样排除任何非零有限阶通常内积向量与 $f_*$ 的全部轨道正交。这覆盖一般无限秩有限 chaos，超出单个标量级数的指数多项式类。

但 $\bigcup_dH_{\le d}$ 虽稠密，仍不等于整个 $H$；非零闭子空间可以与一个指定的稠密线性子空间仅交于零。也不能令 $d\to\infty$ 忽略 $C_d$ 及 $(m+2)^{3(d+1)/2}$ 的增长。对于一般向量，还需控制高尾次数的误差；本条没有提供足以对每个 $L^2$ 向量完成这一步的统一估计。

## 8. 可供后续使用的一般定量条件

上述机制不依赖 $\delta_j$ 的精确有理式。更一般地，设 $\delta_j\ge0$、$\sum_j\delta_j<\infty$，并有

$$
T_m=G_m\otimes I+I\otimes\sum_{j\ge m}\delta_jE_j,
\quad\sup_m\|T_m\|\le B<\infty,
\quad\|L-T_m\|\le\varepsilon_m.
$$

定义

$$
\sigma_m^2=\sum_{j\ge m}\delta_j^2,\qquad
q_m=\sup_{j\ge m}\delta_j,
\qquad
\kappa_{m,d}=\left(\sigma_m^2-2d q_m^2\right)^{1/2}
$$

（只在括号严格正时使用）。§3 的交换关系直接给各纯 $k\le d$ 阶上的左界 $\kappa_{m,d}$。§5 的递推因此给

$$
\|u\|
\le\sqrt{d+1}
\left[(1+2B)\max\left(1,\frac2{\kappa_{m,d}}\right)\right]^{d+1}
\|T_mu\|
\tag{8.1}
$$

对尾次数不超过 $d$ 的 $u$ 成立。

所以，只要对某个趋于无穷的 $m$ 子列有

$$
\sigma_m^2>2d q_m^2,
\qquad
\varepsilon_m
\max\left(1,\frac2{\kappa_{m,d}}\right)^{d+1}
\longrightarrow0,
\tag{8.2}
$$

就同样得到 $\ker L\cap H_{\le d}=0$。特别地，若 $\kappa_{m,d}$ 有一个负多项式下界，而 $\varepsilon_m$ 比任意负幂更快趋零，条件成立。

这里不能只保留 $\sigma_m^2>2dq_m^2$ 而丢掉误差与其差值之间的比较；如果差值趋零过快，反演常数仍可能放大近似误差。原模型在 §2–6 已对二者同时给出足够的定量控制。
