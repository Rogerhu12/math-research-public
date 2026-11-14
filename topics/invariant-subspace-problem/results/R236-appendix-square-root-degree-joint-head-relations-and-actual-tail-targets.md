# R236 附录：平方根次数联合头关系、真实非零尾目标与完整源费用

- 日期：2026-11-13。
- 作者线：normal-complex；root 与 central_review 已全文独立核验。
- 状态：完整辅助接口；未排除原联合正常见证，普通 ISP 未完成。
- 对象：同一个正正常泛函湮灭的两条实际行 $S,Z$。不把不同相位所给的见证合并。
- 扣除旧结果：[R253](../results/R253-positive-tail-partial-traces-and-dyadic-phase-product-elimination.md) 已用完整相位范数消去有限头并保正部分迹。本稿改用两条局部头在同一 $H$ 维代数中的标量关系，关系总次数为 $O(\sqrt H)$，并给出全部实际右因子和误差。它不声称取代 R253 的完整尾理想。
- 联合见证输入：[迟首二次核与同一个正正规两行湮灭者](../results/R236-appendix-late-support-quadratic-kernels-and-positive-joint-first-annihilators.md)。真实头与纯比较的范围仍分开。

## 1. 纯线性代数中的低次数关系

设 $\mathcal C_H$ 是一个维数不超过 $H$ 的复交换含单位代数，带字符 $\chi$。取

$$
s,z\in\mathcal C_H,\qquad \chi(s)=\chi(z)=0.
$$

令

$$
D=\lceil\sqrt{2H}\rceil,
\qquad
N_D=\frac{(D+1)(D+2)}2.
\tag{1.1}
$$

因为 $N_D>H$，线性映射

$$
\mathbb C[x,y]_{\le D}\longrightarrow\mathcal C_H,
\qquad P\longmapsto P(s,z)
$$

有非零核。因此存在非零标量多项式

$$
P(x,y)=\sum_{i+j\le D}p_{ij}x^iy^j
$$

满足

$$
\boxed{
P(s,z)=0,\quad P(0,0)=0,\quad
\sum_{i,j}|p_{ij}|=1.
}
\tag{1.2}
$$

其中常数项为零来自对关系施加 $\chi$，不是额外损失一个独立条件。最后的归一化只除以有限个系数的 $\ell^1$ 范数。

这一步没有控制某个预先指定的系数，也没有给出真空均值。它只是保证一个非零的、全部系数已归一化的关系。可用固定单项式顺序下的有限核空间选取规则选 $P$；无需把所选系数矩阵的逆范数计入下面的存在性估计。

在原模型中，取 $H=2^n$，$\mathcal C_H=\mathbb C[A^{[n]}]$。有限头 $A^{[n]}$ 是有正权的单 Jordan 链，因此该代数恰有维数 $H$；其字符是常数项。

## 2. 两条实际行与准确的近头

沿用同一联合见证的记号

$$
X=\sum_j a_jQ_j,\quad
Y=\sum_j c_jQ_j,\quad
B_0=\sum_j a_j^2Q_j^2,
$$

$$
Q_j=-2N_j(I+N_j)^{-1},
\quad
S=X+H_\zeta,\quad
Z=Y-B_0+H_\zeta^2.
\tag{2.1}
$$

这里 $H_\zeta=h_\zeta(A)$ 是已经固定的真解析芽，$h_\zeta(0)=0$。原正态只属于这一个固定 $\zeta$。

定义真实尾

$$
A_n^{\rm tail}=\sum_{j\ge n}a_jQ_j,
\qquad
C_n^{\rm tail}=\sum_{j\ge n}c_jQ_j,
\tag{2.2}
$$

及真实近头

$$
\widehat S_n=S-A_n^{\rm tail},
\qquad
\widehat Z_n=Z-C_n^{\rm tail}.
\tag{2.3}
$$

这些算子全在 $\mathcal A$，互相交换；$\widehat Z_n$ 保留整个 $B_0,H_\zeta^2$，并没有把它们误当成只作用于前 $n$ 位的矩阵。

令 $N_j^{[n]}$、$Q_j^{[n]}$ 为截断于前 $n$ 位的真实有限头算子，$j<n$；令

$$
x_n=\sum_{j<n}a_jQ_j^{[n]},
\quad
y_n=\sum_{j<n}c_jQ_j^{[n]},
\quad
b_n=\sum_{j<n}a_j^2(Q_j^{[n]})^2,
$$

$$
h_n=h_\zeta(A^{[n]}),\qquad
s_n=x_n+h_n,\qquad
z_n=y_n-b_n+h_n^2.
\tag{2.4}
$$

$s_n,z_n$ 属于同一个 $\mathbb C[A^{[n]}]$，且字符为零。

存在只依赖原固定两行和固定相位的常数 $C_0,M\ge1$，使所有充分大的 $n$ 满足

$$
\|\widehat S_n-s_n\|,
\ \|\widehat Z_n-z_n\|
 \le\varepsilon_n:=C_0\eta_{n-1},
\tag{2.5}
$$

且 (2.2)–(2.4) 中每个算子的范数均不超过 $M$。

### 2.1 (2.5) 的完整 carry 核验

真实递归给

$$
N_j=E_j+\eta_j E_j^*N_{j+1}.
$$

把第 $n$ 位以后的部分置零后，对 $j<n$ 反复相减，得到

$$
\|N_j-N_j^{[n]}\|
 \le\prod_{\ell=j}^{n-1}\eta_\ell
 \le\eta_{n-1}.
\tag{2.6}
$$

由于 $N_j^2=\eta_jN_{j+1}$ 且原 $\eta_j$ 都极小，

$$
\|(I+N_j)^{-1}\|,
\ \|(I+N_j^{[n]})^{-1}\|\le3,
$$

$$
\|Q_j\|,\|Q_j^{[n]}\|\le6,
\qquad
\|Q_j-Q_j^{[n]}\|
 \le18\prod_{\ell=j}^{n-1}\eta_\ell.
\tag{2.7}
$$

因此 $x_n,y_n$ 的比较由 $a,c\in\ell^1$ 支付。对平方项，

$$
\|Q_j^2-(Q_j^{[n]})^2\|
 \le216\prod_{\ell=j}^{n-1}\eta_\ell,
\qquad
\|Q_j^2\|\le36\eta_j.
\tag{2.8}
$$

低位差加上真实高位尾，给

$$
\|B_0-b_n\|
 \le252\Bigl(\sum_j|a_j|^2\Bigr)\eta_{n-1}.
\tag{2.9}
$$

最后 $A=d_0N_0$，故

$$
\|A-A^{[n]}\|
 \le d_0\prod_{\ell=0}^{n-1}\eta_\ell
 \le d_0\eta_{n-1}.
$$

在 $h_\zeta$ 的某个固定解析圈上，$A$ 的预解有界；由 $A^{[n]}\to A$ 的算子范数收敛，充分大的 $n$ 的预解也在同圈上一致有界。Cauchy 积分的预解恒等式于是给

$$
\|h_\zeta(A)-h_\zeta(A^{[n]})\|
 \le C_{h_\zeta}\eta_{n-1}.
\tag{2.10}
$$

平方差再用两因子范数上界，即得到 (2.5)。这里未要求 $h_\zeta$ 的 Taylor 圆大于 $\|A\|$，也未把纯位算子当成实际交换子。

## 3. 真实联合理想中的完整差恒等式

对每个 $n$，由第 1 节为 $s_n,z_n$ 选取 $P_n$。置

$$
L_n=P_n(-A_n^{\rm tail},-C_n^{\rm tail}),
\qquad
E_n=P_n(\widehat S_n,\widehat Z_n).
\tag{3.1}
$$

$L_n$ 是真实尾代数 $\mathcal B_n$ 的算子，等距提升后仍记同一符号。$E_n$ 一般不是纯尾。

对每个单项式，先沿第一个变量、再沿第二个变量作差，得到真实有界右因子 $U_n,V_n\in\mathcal A$：

$$
\begin{aligned}
U_n
&=\sum_{i,j}p_{ij}
 \sum_{\ell=0}^{i-1}
 \widehat S_n^{\,i-1-\ell}
 (-A_n^{\rm tail})^\ell\widehat Z_n^{\,j},\\
V_n
&=\sum_{i,j}p_{ij}
 (-A_n^{\rm tail})^i
 \sum_{\ell=0}^{j-1}
 \widehat Z_n^{\,j-1-\ell}
 (-C_n^{\rm tail})^\ell.
\end{aligned}
\tag{3.2}
$$

空和为零。因为 $\widehat S_n+A_n^{\rm tail}=S$、
$\widehat Z_n+C_n^{\rm tail}=Z$，准确有

$$
\boxed{L_n=E_n-SU_n-ZV_n.}
\tag{3.3}
$$

全部系数归一化使

$$
\boxed{
\|U_n\|+\|V_n\|
 \le D M^{D-1}.
}
\tag{3.4}
$$

另一方面 $P_n(s_n,z_n)=0$，故有序幂差及 (2.5) 给

$$
\boxed{\|E_n\|\le D M^{D-1}\varepsilon_n.}
\tag{3.5}
$$

比较局部和实际幂时不需要跨这两组算子交换。例如
$\widehat S^i\widehat Z^j-s^iz^j
=(\widehat S^i-s^i)\widehat Z^j+s^i(\widehat Z^j-z^j)$，
再分别望远镜即可。

因此，对同一个 $\rho\ge0$、$\tau=\operatorname{Tr}\rho$，如果

$$
\phi_\rho(SR)=\phi_\rho(ZR)=0
\qquad(R\in A'),
$$

则 (3.3) 对全部 $R\in A'$ 给

$$
|\phi_\rho(L_nR)|
 \le\tau D M^{D-1}\varepsilon_n\|R\|.
\tag{3.6}
$$

没有改变 $\rho$，也没有把一个非酉相似后的密度当作原湮灭态。

## 4. 纯尾多项式映射的定量单射

为核实 $L_n$ 不会只是零算子，以下使用本轮实际伸缩族：

$$
a_j=e^{-\beta(j+1)^\alpha},\qquad
c_j=a_j^\kappa\quad(j>j_0),
\quad
\beta>0,\quad\alpha>1,\quad\kappa>1.
\tag{4.1}
$$

只取 $n>j_0$。设

$$
A_n^0=\sum_{j\ge n}a_jE_j,\qquad
C_n^0=\sum_{j\ge n}c_jE_j,
\qquad
L_n^0=P_n(2A_n^0,2C_n^0).
\tag{4.2}
$$

第 4 节的论证适用于任意 $P(0,0)=0$、总次数不超过 $D$、
系数 $\ell^1$ 范数为 $1$ 的标量多项式，不只用于头关系。

存在某个 $1\le k\le D$，其 $k$ 次齐次部分

$$
P_k(x,y)=\sum_{\ell=0}^k p_\ell x^{k-\ell}y^\ell
$$

满足

$$
\max_\ell|p_\ell|\ge N_D^{-1}.
\tag{4.3}
$$

### 4.1 齐次抽取不假设无限相位酉

在纯尾代数上，$E_j\mapsto e^{i\theta}E_j$ 定义等距自同构。可先对有限位作真实酉共轭，再对有限多项式及其算子范数闭包取极限；对 (4.2) 中的可和行，尾部也在范数中收敛。

于是 Bochner Fourier 系数投影是收缩，并给出

$$
\|P(2A_n^0,2C_n^0)\|
 \ge\|P_k(2A_n^0,2C_n^0)\|.
\tag{4.4}
$$

这里没有假设无限乘积相位酉在原参考真空表示中可实施。

### 4.2 全部齐次系数的有限插值

取 $k+1$ 个真实位 $J=\{n,n+1,\ldots,n+k\}$，置

$$
b_i=c_i/a_i=a_i^{\kappa-1}.
$$

对 $j\in J$ 令 $F_j=J\setminus\{j\}$。$E_{F_j}$ 的准确系数为

$$
2^k k!\left(\prod_{i\in F_j}a_i\right)Q_j,
\qquad
Q_j=\sum_{\ell=0}^k
 \frac{p_\ell}{\binom{k}{\ell}}\,
 e_\ell(b_{F_j}).
\tag{4.5}
$$

这保留了每个 $\ell$，没有把一个可能相消的齐次多项式替换成正系数和。

记 $q_\ell=p_\ell/\binom{k}{\ell}$。由

$$
e_\ell(b_{J\setminus\{j\}})
 =\sum_{t=0}^{\ell}(-b_j)^t e_{\ell-t}(b_J),
$$

存在次数不超过 $k$ 的一元多项式 $H$，使 $H(b_j)=Q_j$，且

$$
H(x)=\sum_{t=0}^k h_tx^t,\qquad
h_t=(-1)^t\sum_{\ell=t}^kq_\ell e_{\ell-t}(b_J).
\tag{4.6}
$$

充分大的 $n$ 下，$0<b_i\le1$ 且后继比 $b_{i+1}/b_i\le1/2$。故所有插值点间距至少

$$
d=\frac12 b_{n+k}.
\tag{4.7}
$$

逆三角变换的系数来自
$\prod_{i\in J}(1+b_ix)^{-1}$。其不超过 $k$ 次的系数绝对值至多
$\binom{2k}{k}\le4^k$，所以

$$
\max_\ell|p_\ell|
 \le(k+1)8^k\max_t|h_t|.
\tag{4.8}
$$

另一方面，Lagrange 公式中每个基多项式的系数 $\ell^1$ 范数不超过
$2^k d^{-k}$，因此

$$
\max_t|h_t|
 \le(k+1)2^k d^{-k}\max_{j\in J}|Q_j|.
\tag{4.9}
$$

合并 (4.7)–(4.9) 得

$$
\max_j|Q_j|
 \ge
\frac{b_{n+k}^k}{(k+1)^2\,32^k}
 \max_\ell|p_\ell|.
\tag{4.10}
$$

(4.5) 的某个系数因而至少为

$$
\frac{k!}{N_D(k+1)^2\,16^k}
 \exp[-\kappa\beta k(n+k+1)^\alpha].
\tag{4.11}
$$

为把该系数变成算子范数下界，在 $J$ 位取全零输入、$F_j$ 位为一而其余 $J$ 位为零的输出，外部仍取参考真空。由于当前齐次次数恰为 $k=|F_j|$，任何用到 $J$ 外的单项式都不能贡献该矩阵元。因此它准确等于上述系数。

由 (4.4)，统一得到

$$
\boxed{
\|L_n^0\|\ge m_{n,D}:=
\frac{\exp[-\kappa\beta D(n+D+1)^\alpha]}
 {(D+2)^4\,16^D}>0.
}
\tag{4.12}
$$

特别，两个纯尾行在所有有限次数的标量多项式中代数独立。这个结论依赖这里无限不同的真实比率；不适用于比例相同的两行。

## 5. 实际非零尾目标和归一源费

由 $N_j^2=\eta_jN_{j+1}$，

$$
\|Q_j+2E_j\|\le8\eta_j.
$$

所以在同一个原 Hilbert 空间中，

$$
\|-A_n^{\rm tail}-2A_n^0\|,
\ \|-C_n^{\rm tail}-2C_n^0\|
 \le C_1\eta_n.
\tag{5.1}
$$

增大固定 $M$ 后，对所有归一化的 $P_n$ 都有

$$
\|L_n-L_n^0\|
 \le C_1 D M^{D-1}\eta_n.
\tag{5.2}
$$

现在取 $H=2^n$、$D=\lceil\sqrt{2H}\rceil$。若

$$
1<\alpha<7,
\tag{5.3}
$$

则

$$
-\log m_{n,D}
 =O\!\left(H^{(\alpha+1)/2}+D\log(D+2)\right)
 =o(H^4).
\tag{5.4}
$$

而

$$
\eta_{n-1}\le
 \exp[-(770/16)H^4].
$$

因此 (5.2) 最终小于 $m_{n,D}/2$。实际尾算子也非零，而且

$$
\boxed{\|L_n\|\ge\frac12m_{n,D}.}
\tag{5.5}
$$

这里的 $\alpha<7$ 只是本辅助估计支付 carry 的范围；没有新增任何核排除范围。本轮关键的 $3/2<\alpha<3$ 完全处于其中。

令

$$
B_n=\frac{L_n}{\|L_n\|},
\quad
\widetilde U_n=\frac{U_n}{\|L_n\|},
\quad
\widetilde V_n=\frac{V_n}{\|L_n\|}.
$$

则 $B_n$ 是真实尾代数中的非零收缩，且

$$
\left\|
B_n+S\widetilde U_n+Z\widetilde V_n
\right\|
 \le
\frac{2D M^{D-1}\varepsilon_n}{m_{n,D}}
 \longrightarrow0,
\tag{5.6}
$$

$$
\boxed{
\|\widetilde U_n\|+\|\widetilde V_n\|
 \le
\frac{2D M^{D-1}}{m_{n,D}}
 =
\exp\!\left[O\!\left(H^{(\alpha+1)/2}\right)\right].
}
\tag{5.7}
$$

因此，本构造已经支付“非零实际收缩尾目标接近真实双行理想”及其完整源费用。后补 §8 证明这一受控次数关系族的归一目标无条件一致 WOT 趋零；它们不能提供非零弱锚。

## 6. 同一正常态迫使所有这些归一目标失去真空锚

设同一非零正正常 $\rho$ 满足第 3 节的两条湮灭式，故 $\tau=\operatorname{Tr}\rho>0$。由 (3.6)、(5.5)，

$$
|\phi_\rho(B_n)|
 \le
\tau\,\frac{2D M^{D-1}\varepsilon_n}{m_{n,D}}
 \longrightarrow0.
\tag{6.1}
$$

令 $\tau_n$ 为 $\rho$ 的真实尾部分迹。R253 已准确证明

$$
\|\tau_n-\tau|\Omega_n\rangle\langle\Omega_n|\|_1
 \le2\sqrt{\tau\delta_n},
\qquad
\delta_n\downarrow0.
$$

因为 $\|B_n\|=1$ 且 $B_n$ 是真实尾算子，(6.1) 给

$$
\boxed{
|\langle B_n\Omega_n,\Omega_n\rangle|
 \le
2\sqrt{\delta_n/\tau}
 +\frac{2D M^{D-1}\varepsilon_n}{m_{n,D}}
 \longrightarrow0.
}
\tag{6.2}
$$

该结论对每个头关系的选法一致成立；(4.12) 保证分母的统一下界，不需要给 $\delta_n$ 假设速度。

为准确记录先前的选择问题，定义下述有限维优化；后补 §8 已无条件证明其值趋零。令

$$
\mathcal K_n=
\{P\in\mathbb C[x,y]_{\le D}:P(s_n,z_n)=0\}.
$$

定义

$$
\kappa_n=
\sup_{\substack{P\in\mathcal K_n\\P\ne0}}
\frac{|\omega_n(P(-A_n^{\rm tail},-C_n^{\rm tail}))|}
{\|P(-A_n^{\rm tail},-C_n^{\rm tail})\|}.
\tag{6.3}
$$

在 (4.1)、(5.3) 下，分母对非零 $P$ 确实不为零，系数 $\ell^1$ 单位球面紧，所以此上确界可达到。现有结果给

$$
\kappa_n\le
2\sqrt{\delta_n/\tau}
+\frac{2D M^{D-1}\varepsilon_n}{m_{n,D}}
\longrightarrow0
\tag{6.4}
$$

作为假想联合见证的必要条件。

本稿没有证明 $\limsup\kappa_n>0$，甚至没有把某个单独关系的真空均值声明为非零。维数计数和算子范数下界都不控制这个均值；它们也不控制允许再乘任意右因子后的完整理想测试量。

后补 §8 已在本篇整个 $1<\alpha<7$ 范围内，无条件证明 (6.3) 的 $\kappa_n\to0$，并允许总次数仍受控的任意两模式多项式右因子。因此这一关系族的非零弱锚选择已被排除；任意尾代数或全交换子右因子的完整联合理想仍另待研究。


## 7. 关系目标的低齐次度部分一致消失

本节是前六节的补充。单独的低次数逃逸只说明关系空间不能靠固定低次主项免费得到弱锚；后补 §8 再利用真实伸缩系数支付物理池宽，完成整个受控关系族的统一弱零。

继续采用 (4.1)、$1<\alpha<7$、$H=2^n$ 和
$D=\lceil\sqrt{2H}\rceil$。所有结论对

$$
P\in\mathcal K_n,\qquad
\sum|p_{ij}|=1
$$

的选法一致。记 $P_k$ 为总次数 $k$ 的齐次部分，
$L^0=P(2A_n^0,2C_n^0)$，
$L=P(-A_n^{\rm tail},-C_n^{\rm tail})$。

### 7.1 在一个更短的头上再分离

取整数 $J<n$。在 $n$ 位局部头内定义

$$
s_{J,n}^0
 =s_J\otimes I-2\sum_{j=J}^{n-1}a_jE_j,
\qquad
z_{J,n}^0
 =z_J\otimes I-2\sum_{j=J}^{n-1}c_jE_j.
\tag{7.1}
$$

第 2 节同一组递归估计给

$$
\|s_n-s_{J,n}^0\|,
\ \|z_n-z_{J,n}^0\|
 \le C_2\eta_{J-1}.
\tag{7.2}
$$

具体地，$j<J$ 的截断差含全部
$\prod_{\ell=j}^{J-1}\eta_\ell$；
$J\le j<n$ 的 $Q_j^{[n]}$ 与 $-2E_j$ 之差至多
$8\eta_j$；
这些位上的平方项本身至多 $36\eta_j$；
$h_\zeta(A^{[n]})-h_\zeta(A^{[J]})$ 由原固定解析圈支付
$C\eta_{J-1}$。这些常数均独立于 $J,n$。

把固定常数 $M$ 增大一次后，由 $P(s_n,z_n)=0$ 得

$$
\|P(s_{J,n}^0,z_{J,n}^0)\|
 \le C_2D M^{D-1}\eta_{J-1}.
\tag{7.3}
$$

在低 $J$ 位的物理计算基向量 $e_0$ 上取同一输入和输出。对
$\mathbb C[A^{[J]}]$，这个矩阵元恰是常数字符：严格正幂的对角元为零。因此 (7.1) 的压缩准确给出

$$
P\!\left(
 -2\sum_{j=J}^{n-1}a_jE_j,
 -2\sum_{j=J}^{n-1}c_jE_j
\right).
$$

于是

$$
\left\|
P\!\left(
 -2\sum_{j=J}^{n-1}a_jE_j,
 -2\sum_{j=J}^{n-1}c_jE_j
\right)
\right\|
 \le C_2D M^{D-1}\eta_{J-1}.
\tag{7.4}
$$

这里使用的是低头物理计算基的字符，不是把 Haar 真空压缩误称为乘法同态。

### 7.2 从有限纯池恢复全部低次数系数

设 $1\le k<n-J$。在有限池 $[J,n)$ 上取同时相位的 Fourier 系数投影，保留次数 $k$。这次相位酉完全有限。再用第 4 节的 $k+1$ 位插值，但不对 $P_k$ 另行归一化，得到

$$
\max_{i+j=k}|p_{ij}|
 \le
\frac{(k+1)^2\,16^k}{k!}
 e^{\kappa\beta k(n+1)^\alpha}
 C_2D M^{D-1}\eta_{J-1}.
\tag{7.5}
$$

(7.5) 保留了全部复系数及其可能相消；插值点可以取
$J,\ldots,J+k$，其最小间距按第 4 节估计，且 $J+k+1\le n$。
指数中写 $n+1$ 是统一的放宽。

固定整数 $K$，取 $J=n-K-1$，则 (7.5) 同时适用于
$1\le k\le K$。它给出的不是某个最高次数系数估计，而是原关系的全部这些低次系数估计。

### 7.3 同尺度归一后仍消失

令

$$
L_{\le K}^0
 =\sum_{k=1}^K P_k(2A_n^0,2C_n^0).
$$

使用固定的尾行范数上界、(7.5)、单项式数以及
$\|L\|\ge m_{n,D}/2$，得到一个可取的统一粗界

$$
\frac{\|L_{\le K}^0\|}{\|L\|}
 \le
\frac{
 C_3D\,M^{D+K}(K+2)^4\,16^K
 e^{\kappa\beta K(n+1)^\alpha}
 \eta_{n-K-2}
}{m_{n,D}}.
\tag{7.6}
$$

这里只要求 $n-K-2\ge0$。$C_3,M$ 均固定，未把分母当成一个未知的正数；使用的是第 4–5 节对全部关系一致的准确下界。

若

$$
K=K_n=\lfloor\theta n\rfloor,\qquad
0<\theta<\frac{7-\alpha}{8},
\tag{7.7}
$$

则 (7.6) 的对数负主项来自

$$
-\log\eta_{n-K-2}
 \ge770\,16^{n-K-2}.
$$

其余项的对数至多

$$
O(D)+O(Kn^\alpha)+O(K\log(K+2))
+\kappa\beta D(n+D+1)^\alpha.
$$

最后一项为 $O(2^{(\alpha+1)n/2})$，而 (7.7) 正是

$$
4(1-\theta)>\frac{\alpha+1}{2}.
$$

所以

$$
\boxed{
\sup_{\substack{P\in\mathcal K_n\\\sum|p_{ij}|=1}}
\frac{\|L_{\le K_n}^0\|}{\|L\|}
 \longrightarrow0.
}
\tag{7.8}
$$

特别，任意固定 $K$ 的低齐次度部分也一致消失。

第 5 节已经给出 $\|L-L^0\|/\|L\|\to0$。因此每个归一真实尾目标
$B=L/\|L\|$ 都在算子范数中趋近一个纯尾多项式

$$
\frac{L^0-L_{\le K_n}^0}{\|L\|},
\tag{7.9}
$$

该纯多项式的最小齐次次数大于 $K_n$，范数为 $1+o(1)$。
这同样对关系的选择一致。

### 7.4 为什么 (7.8) 仍没有排除弱锚

最小产生次数趋于无穷，本身不能推出一个有界纯算子族弱趋于零。此前次数审计中的平顶例已经说明这一点：在 $N$ 个远位上取

$$
D_N=\frac2{N+1}\sum_{j=1}^N E_j.
$$

离散对称链范数给 $\|D_N\|\le1$，并且

$$
\langle D_N^k\Omega,\Omega\rangle
 =\frac{N(N-1)\cdots(N-k+1)}{(N+1)^k}
 \longrightarrow1
$$

只要 $k^2/N\to0$。这些例子的最小产生次数为 $k\to\infty$。

该平顶例不是当前两个固定伸缩尾行的关系目标，不能据此断言它们一定有锚；它只阻止从 (7.8) 免费推出它们没有锚。仍需利用真实两行、完整关系空间或合适右因子的额外结构。

本节支付的是选择问题中的一个明确限制：固定低次主项的策略不能绕过头关系。它不把增长次数、纯 Fourier 抽取或已付 carry 单独升级为普通正常湮灭者排除。

## 8. 完整受控次数关系族的统一弱零：次数逃逸之后的真空锚上界

日期：2026-11-13 UTC。状态：已证明的辅助加强。
本节继续同一实际两行、局部头与尾目标的记号，不假设正常湮灭态存在。

§7 的低齐次次数逃逸本身不够推出弱零，平顶长池例已经说明这一点。
下面利用本篇固定的真实系数
$$
a_j=e^{-\beta(j+1)^\alpha},\qquad c_j=a_j^\kappa
\quad(j\text{ 充分大}),\qquad
\beta>0,\quad\kappa>1,\quad\alpha>1,
\tag{8.1}
$$
给出缺少的物理池宽控制。所有标量多项式的系数允许任意复相位。

### 8.1 任意齐次复多项式的完整范数恢复

记两个纯比较尾行
$$
A_n^0=\sum_{j\ge n}a_jE_j,\qquad
C_n^0=\sum_{j\ge n}c_jE_j.
$$
对任意非零 $k$ 次齐次多项式
$$
P_k(x,y)=\sum_{\ell=0}^k p_\ell x^{k-\ell}y^\ell,
\qquad
\sigma_k=\sum_{\ell=0}^k|p_\ell|,
$$
式 (4.5)–(4.10) 的插值论证给
$$
\boxed{
\|P_k(2A_n^0,2C_n^0)\|
\ge
\frac{k!}{16^k(k+1)^3}
e^{-\kappa\beta k(n+k+1)^\alpha}\sigma_k.
}
\tag{8.2}
$$
这里 $n$ 足够大后，常数对所有 $k\ge1$ 一致。

核对该量词：取 $J=\{n,\ldots,n+k\}$，
$b_j=c_j/a_j$ 的后继比对所有 $j\ge n$ 都至多 $1/2$。
对 $J$ 中删除一个指标所得的 $k$ 位单项式，
完整插值保留全部 $k+1$ 个复系数，给出系数下界
$$
\frac{k!}{16^k(k+1)^2}
e^{-\kappa\beta k(n+k+1)^\alpha}
\max_\ell|p_\ell|.
$$
再用 $\max|p_\ell|\ge\sigma_k/(k+1)$ 得 (8.2)。
该系数由全零 $J$ 输入与所选 $k$ 位输出的矩阵元准确读出；
任何涉及 $J$ 外坐标的项都因总次数已经用尽而不能贡献。
因此没有把复系数和替换成正系数和，也没有漏掉完整 Hilbert 空间的外部向量。

### 8.2 按完整范数支付的有限物理池截断

固定 $\vartheta>0$，本小节只要求
$$
k\ge\vartheta n.
\tag{8.3}
$$
增大固定 $n_0$ 后，(8.1) 的尾几何比至多 $1/2$，并且
$$
\|2A_n^0\|,\ \|2C_n^0\|\le1
\qquad(n\ge n_0).
\tag{8.4}
$$
令
$$
E_{n,k}=k(n+k+1)^\alpha,
$$
选固定 $L\ge2$ 使
$$
\beta L^\alpha\ge\kappa\beta+12,
$$
并设
$$
N=N(n,k)=
\left\lceil Lk^{1/\alpha}(n+k+1)\right\rceil.
\tag{8.5}
$$
把两行截到有限物理池 $[n,N)$：
$$
A_{n,N}^0=\sum_{n\le j<N}a_jE_j,\qquad
C_{n,N}^0=\sum_{n\le j<N}c_jE_j.
$$
尾几何和给
$$
\|2A_n^0-2A_{n,N}^0\|,
\ \|2C_n^0-2C_{n,N}^0\|
\le4e^{-\beta(N+1)^\alpha}.
$$
由 (8.4)，对每个完整单项式逐因子望远镜，得到
$$
\|P_k(2A_n^0,2C_n^0)
-P_k(2A_{n,N}^0,2C_{n,N}^0)\|
\le4k\sigma_ke^{-\beta(N+1)^\alpha}.
\tag{8.6}
$$
特别，这一步没有额外的 $M^k$。

将 (8.6) 除以 (8.2)。
对全部 $k\ge1,n\ge n_0$，
$$
\log(4k)+k\log16+3\log(k+1)-\log(k!)
\le10E_{n,k}.
$$
由 (8.5)，得到完整相对误差
$$
\boxed{
\frac{\|P_k(2A_n^0,2C_n^0)
-P_k(2A_{n,N}^0,2C_{n,N}^0)\|}
{\|P_k(2A_n^0,2C_n^0)\|}
\le e^{-2E_{n,k}}.
}
\tag{8.7}
$$

池宽 $M_{n,k}=N-n$ 满足
$$
M_{n,k}
\le C_\vartheta k^{1+1/\alpha},
\qquad
C_\vartheta=L(\vartheta^{-1}+2)+1.
\tag{8.8}
$$
这里用的是 $n\le k/\vartheta$。
这正是平顶长池例没有的额外控制：
本篇两模式的任意复系数取消，都不能在完整范数归一后
把主要输出无代价地推到一个宽度远超过 (8.8) 的池。

### 8.3 数目中心窗给齐次真空比

在 $M$ 个物理位上，令 $\mathsf N$ 为取值 $0,\ldots,M$ 的数目算子。
任何 $k$ 次纯产生齐次算子 $Q$ 都把 $\mathsf N$ 恰增加 $k$。
定义中心窗投影
$$
P_{\rm win}=1_{\{|\mathsf N-M/2|<k/2\}}.
$$
两个窗内数目之差严格小于 $k$，故
$$
P_{\rm win}QP_{\rm win}=0.
\tag{8.9}
$$
参考向量 $\Omega_+^{\otimes M}$ 的数目分布为
$\operatorname{Bin}(M,1/2)$。
由
$$
\mathbb E e^{u(\mathsf N-M/2)}
=\cosh(u/2)^M\le e^{Mu^2/8}
$$
及正、负两个方向的指数 Markov 界，
$$
\|(I-P_{\rm win})\Omega_+^{\otimes M}\|^2
\le2e^{-k^2/(2M)}.
$$
把真空配对拆成至少一个向量在窗外的两项，(8.9) 给
$$
|\langle Q\Omega_+^{\otimes M},\Omega_+^{\otimes M}\rangle|
\le2\sqrt2\,\|Q\|e^{-k^2/(4M)}.
\tag{8.10}
$$
它适用于任意复矩阵系数；本节没有假设 $Q$ 正或增生。

把 (8.10) 用于
$Q=P_k(2A_{n,N}^0,2C_{n,N}^0)$，
再用 (8.7)–(8.8) 回到完整尾，得固定 $c_\vartheta>0$：
$$
\boxed{
\frac{
|\langle P_k(2A_n^0,2C_n^0)\Omega_n,\Omega_n\rangle|
}{
\|P_k(2A_n^0,2C_n^0)\|
}
\le
8e^{-c_\vartheta k^{\,1-1/\alpha}}
\quad(k\ge\vartheta n).
}
\tag{8.11}
$$
例如可取不超过 $1/(4C_\vartheta)$ 的正 $c_\vartheta$，
并按固定参数增大 $n_0$。
(8.11) 的适用范围只要求 $\alpha>1$；
下面把它转回实际关系族时才需要额外的次数/carry 条件。

### 8.4 不同齐次次数可逐项求和，且不损失最大次数因子

在纯尾算子的范数闭代数中存在等距圆作用
$$
\alpha_\theta(E_j)=e^{i\theta}E_j.
$$
这里仅先在任意有限坐标多项式上使用有限张量酉，
再作算子范数极限；没有在当前乘积表示中假设无限相位酉存在。
两条 $\ell^1$ 行及其有限多项式的轨道在范数中连续。
因此共同次数的 Bochner Fourier 投影收缩，并准确抽出
$$
\mathcal P_k\big(P(2A_n^0,2C_n^0)\big)
=P_k(2A_n^0,2C_n^0).
$$
特别，
$$
\|P_k(2A_n^0,2C_n^0)\|
\le\|P(2A_n^0,2C_n^0)\|.
\tag{8.12}
$$

令 $s=1-1/\alpha\in(0,1)$。
由 (8.11)–(8.12)，对任意有限多项式及任意 $K\ge\vartheta n-1$，
其高齐次部分满足
$$
\frac{\left|
\sum_{k>K}\langle P_k(2A_n^0,2C_n^0)\Omega_n,\Omega_n\rangle
\right|}
{\|P(2A_n^0,2C_n^0)\|}
\le8\sum_{k>K}e^{-c_\vartheta k^s}.
\tag{8.13}
$$
右边不含多项式的最大次数。
该尾和一致趋零，例如
$$
\sum_{k>K}e^{-c_\vartheta k^s}
\le
e^{-(c_\vartheta/2)K^s}
\sum_{k\ge1}e^{-(c_\vartheta/2)k^s}.
\tag{8.14}
$$
有限的第二因子只依赖固定参数。

### 8.5 实际关系族的统一真空上界及 WOT 零

现在回到本篇局部头 $s_n,z_n$ 及实际尾目标
$$
L_n(P)=P(-A_n^{\rm tail},-C_n^{\rm tail}).
$$
可以取比原平方根次数稍广的一组预算。
设固定 $d>0,C_D>0$，且
$$
D_n\le C_D2^{dn},
\qquad
d(\alpha+1)<4.
\tag{8.15}
$$
考虑所有非零复多项式 $P$，满足
$$
\deg P\le D_n,\qquad P(s_n,z_n)=0.
\tag{8.16}
$$
如果某个 $n$ 没有这样的非零关系，下述上确界约定为零。
否则，可先将系数 $\ell^1$ 归一为一。

完整 §4 的范数恢复、§5 的实际 carry 比较在任意有限次数 $D_n$
仍给
$$
\|P(2A_n^0,2C_n^0)\|\ge
m_{n,D_n}
=
\frac{e^{-\kappa\beta D_n(n+D_n+1)^\alpha}}
{(D_n+2)^4\,16^{D_n}},
\tag{8.17}
$$
$$
\|L_n(P)-P(2A_n^0,2C_n^0)\|
\le C D_n M^{D_n-1}\eta_n.
\tag{8.18}
$$
由 (8.15)，右侧除以 (8.17) 后一致趋零，
所以所有 (8.16) 的实际 $L_n(P)$ 在充分大 $n$ 时都非零。

选
$$
0<\vartheta<1-\frac{d(\alpha+1)}4,\qquad
K_n=\lfloor\vartheta n\rfloor.
\tag{8.19}
$$
为明确一般 $D_n$ 下的低次数量词，重述 §7 的同一估计。
取 $J=n-K_n-1$，把局部头两行与
低 $J$ 位实际头加上 $[J,n)$ 的纯产生行比较。
完整误差至多 $C D_nM^{D_n-1}\eta_{J-1}$。
低 $J$ 位的物理 $e_0$ 对头多项式给常数字符，
故压缩后得到有限纯池的多项式范数界。
两行的共同负号可由有限相位 $\pi$ 消去，不改变范数。
逐次数抽取后，仍用 §8.1 的 $k+1$ 点恢复，
对 $k\le K_n$ 得到 §7 的完整低次估计：
$$
\frac{
\|P_{\le K_n}(2A_n^0,2C_n^0)\|
}{
\|L_n(P)\|
}
\le
\frac{
C D_n M^{D_n+K_n}(K_n+2)^4\,16^{K_n}
e^{\kappa\beta K_n(n+1)^\alpha}
\eta_{n-K_n-2}
}{
m_{n,D_n}
}.
\tag{8.20}
$$
这一步只要求 $J+k+1\le n$，已经由上述选择保证。

(8.15)、(8.19) 给
$$
d(\alpha+1)<4(1-\vartheta).
$$
因此 (8.20) 的负主指数
$-770\cdot16^{n-K_n-2}$ 支付分母 (8.17) 与全部其余因子，
右侧一致为 $o(1)$，且衰减快于 $e^{-c n^s}$。
(8.18) 的相对误差也有同样的更快衰减。

把实际误差、(8.20) 的低次部分、
以及 (8.13)–(8.14) 的完整高次和相加，得到固定 $C,c>0$：
$$
\boxed{
\sup_{\substack{P\ne0,\ \deg P\le D_n\\P(s_n,z_n)=0}}
\frac{|\langle L_n(P)\Omega_n,\Omega_n\rangle|}
{\|L_n(P)\|}
\le C e^{-c n^{\,1-1/\alpha}}
\longrightarrow0.
}
\tag{8.21}
$$
常数只依赖固定参数及 (8.15) 的预算，不依赖复系数、具体关系或最大次数。

所有归一目标
$$
B_n(P)=\frac{L_n(P)}{\|L_n(P)\|}
$$
是作用在第 $n$ 位之后的**真实尾算子**，范数为一。
对任意固定有限柱 $f,g$，充分大 $n$ 下有准确因式
$$
\langle B_n(P)f,g\rangle
=\langle f,g\rangle
\langle B_n(P)\Omega_n,\Omega_n\rangle.
$$
再用有限柱稠密性与统一范数一，(8.21) 给
$$
\boxed{
\sup_{\substack{P\ne0,\ \deg P\le D_n\\P(s_n,z_n)=0}}
|\langle B_n(P)f,g\rangle|\longrightarrow0
\quad(f,g\in\mathscr H).
}
\tag{8.22}
$$
这是真实算子的统一 WOT 零，且完全不依赖正常湮灭假设。

原本篇的 $D_n=\lceil\sqrt{2\cdot2^n}\rceil$ 对应 $d=1/2$，
故 (8.15) 恰允许
$$
1<\alpha<7.
$$
因此先前 §6 由正常见证推出的该关系空间真空锚趋零，
在整个本篇范围内已由 (8.21) 无条件支付。
不能再用这一受控次数关系族本身争取一致非零正常锚。

### 8.6 已包含的两模式右因子与仍未覆盖的完整尾理想

若 $P_n(s_n,z_n)=0$，并取任意复多项式 $Q_n$，则
$$
(P_nQ_n)(s_n,z_n)=0,
$$
以及
$$
L_n(P_nQ_n)=L_n(P_n)L_n(Q_n).
$$
只要总次数满足 (8.15)，(8.21)–(8.22) 同样适用于
这个乘积的完整算子范数归一。
没有对 $Q_n$ 的系数大小、相位或单独算子范数另设上界。

这仍只覆盖同一两模式的受控次数多项式。
它没有覆盖任意实际尾 $\mathcal B_n$ 或完整交换子 $\mathcal C_n$
右因子，没有给全部最大子式尾理想的 $q_n^{\rm joint}$ 上界，
也没有声称任意高次数纯产生算子都弱零。
本节之所以能推出 (8.21)，正是因为完整系数恢复与相对截断
付出了 (8.8) 的池宽约束。
