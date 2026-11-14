# R259：多变量 Bell 分支、复指数倾斜与同幂慢尾的简单根多项式循环性

日期：2026-11-13（UTC）。作者：kernel。

状态：已证明。承接 R236 对称高位平均附录，把其排核机制扩到任意固定有限组高阶累积量、任意复 $\ell^2$ 指数倾斜，以及有任意复相位的双侧同幂慢尾。本文给完整的新增系数、轮廓、自然域和增长预算，不把矩阵伴随线性化的非交换误差当作已付。

规范交替调和行的有限多变量、全部指数权及简单根子类，亦已由 [R236 独立附录](R236-appendix-finite-cumulant-branches-and-squarefree-weighted-polynomials.md) 关闭。本稿完整支付的新增范围是双侧同幂衰减的任意复相位行，不把该规范子类重复登记为新发现。

## 1. 结论与准确量词

令
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a_*\in\mathbb C,\quad a\in\ell^2.
$$
假设存在固定 $p>1/2$、$c,C>0$ 和整数 $J$，使
$$
\boxed{
c(j+1)^{-p}\le |a_j|\le C(j+1)^{-p}
\qquad(j\ge J).
}
\tag{1.1}
$$
$a_j$ 的相位任意；有限个低位不受 (1.1) 限制。

另取任意
$$
w=c_*+\sum_jb_j\chi_j,\qquad b\in\ell^2,\quad c_*\in\mathbb C.
$$
记
$$
c_j=e^{-2b_j},\qquad
R_j=R_j(b)=\frac{I-c_jN_j}{I+c_jN_j},
$$
$$
X_b=X_u+H_{a,b}
=a_*I+\sum_j a_jR_j,\qquad
H_{a,b}=\sum_j a_j(R_j-V_j)\in\mathcal A.
\tag{1.2}
$$
等式使用 R176 §10 的真实闭实现：
$\operatorname{Dom}X_b=\operatorname{Dom}X_u$，有界差按范数绝对收敛。

定义固定标量多项式
$$
L_n(v)=
\left.\frac{d^n}{dt^n}\log(\cosh t+v\sinh t)\right|_{t=0},
$$
及实际累积量
$$
K_n(b)=\sum_j a_j^nL_n(R_j)\in\mathcal A,\qquad n\ge2.
\tag{1.3}
$$
这里 $L_n(1)=0$，所以所有 $K_n(b)$ 字符为零，均准幂零；级数按范数绝对收敛。

**定理1：多变量解析分支排核。** 对任意固定整数 $d\ge2$ 及任意原点邻域上的多变量全纯芽 $\Phi$，
$$
\boxed{
\ker\!\left(
X_b-\Phi(K_2(b),\ldots,K_d(b))
\right)=\{0\}.
}
\tag{1.4}
$$
$\Phi$ 的作用是同一个交换 Banach 代数中的多变量全纯演算。常数芽也包括在内。

**定理2：点态多项式的正向循环子类。** 若 $q$ 是非零且所有复根都简单的标量多项式，则
$$
\boxed{q(u)e^w\text{ 对原实际 }A\text{ 循环}.}
\tag{1.5}
$$
非零常数亦包括在内。结论对上述全部 $a_*,c_*,b$ 和任意复相位行 $a$ 成立。

特别，规范逐项交替调和 $a_j=(-1)^j/(j+1)$ 满足 (1.1)，所以它的任意简单根多项式乘任意复 $\ell^2$ first 指数权都循环。重复根的一般多项式不由本稿自动得到；单根极限也不能用循环向量的范数极限来代替证明。

## 2. 倾斜有理因子的统一预算

因 $b_j\to0$，
$$
0<c_-\le|c_j|\le c_+<\infty,\qquad c_j\to1.
\tag{2.1}
$$
以下固定 $a,b,d,\Phi$；所有常数允许依赖它们，但不依赖后面的 $r,m,q,F$。

$N_j$ 准幂零，故 $I\pm c_jN_j$ 实际可逆。对充分大 $j$，
$|c_j|\le2$ 且 $N_j^2=\eta_jN_{j+1}$，所以
$$
(I\pm c_jN_j)^{-1}
=(I\mp c_jN_j)(I-c_j^2N_j^2)^{-1}
$$
有与 $j$ 无关的界。有限个低位单独取最大值，得到
$$
\boxed{
\sup_j\|(I\pm c_jN_j)^{-1}\|<\infty,\qquad
\sup_j\|V(\pm c_jN_j)\|<\infty,
}
\tag{2.2}
$$
其中 $V(z)=(I-z)(I+z)^{-1}$。

在由 (2.2) 覆盖的算子上，准确逆差式给
$$
\|V(c_jP)-V(c_jQ)\|\le C_b\|P-Q\|.
\tag{2.3}
$$
每个固定 $L_n$ 是多项式，幂差公式因而给同一集合上的 Lipschitz 常数。
这些估计保留实际进位，也允许 $c_j$ 为复数。

## 3. 多变量全纯演算的可用差估计

简记 $\mathbf K=(K_2,\ldots,K_d)$。
选取一个闭多圆周
$$
\Gamma=\{|\zeta_n|=\rho_n:2\le n\le d\}
$$
及其所围多圆盘，完全包含在 $\Phi$ 的全纯域内。
每个 $K_n$ 谱为零，故
$$
\Phi(\mathbf K)=\frac1{(2\pi i)^{d-1}}
\int_\Gamma
 \Phi(\boldsymbol\zeta)\prod_{n=2}^d
 (\zeta_n-K_n)^{-1}\,d\boldsymbol\zeta
\tag{3.1}
$$
是真正的有界算子。

若一个交换元组 $\widehat{\mathbf K}$ 在各坐标范数上充分接近 $\mathbf K$，
则 Neumann 逆差式在同一 $\Gamma$ 上给统一预解式界。
若另一个元组是 $\gamma(\mathbf K)$，其中 $\gamma$ 是固定酉共轭，
其各坐标预解式范数与原元组完全相同。
对 (3.1) 的有限预解式乘积逐因子相减，得到
$$
\boxed{
\|\Phi(\widehat{\mathbf K})-\Phi(\mathbf K)\|
 \le C_\Phi\sum_{n=2}^d\|\widehat K_n-K_n\|,
}
\tag{3.2}
$$
以及
$$
\boxed{
\|\Phi(\gamma\mathbf K)-\Phi(\widehat{\mathbf K})\|
 \le C_\Phi'\sum_{n=2}^d\|\gamma K_n-\widehat K_n\|.
}
\tag{3.3}
$$
混合元组之间不要求互相交换；对预解式乘积固定一个顺序作幂差即可。各元组内部交换，才用于定义各自的全纯演算。

## 4. 随幂次增长的高位输入

令
$$
Y=\Phi(\mathbf K),\qquad T=X_b-Y,\qquad M=\ker T.
$$
取
$$
m=m_r=\lceil e^{r^2}\rceil,\qquad q=q_r=r^4,\qquad
I_r=\{m,\ldots,m+q-1\}.
\tag{4.1}
$$
对 $F\subset I_r$、$|F|=r$，令
$$
J_F=\prod_{j\in F}M_{\chi_j},\qquad
p_F=\prod_{j\in F}a_jc_j,
$$
$$
\boxed{
\mathcal B_r=\frac1{(-2q)^r}
 \sum_{\substack{F\subset I_r\\|F|=r}}p_F^{-1}J_F.
}
\tag{4.2}
$$
$p_F$ 非零；复相位完整保留在系数中。

由 (1.1)、(2.1)，其绝对系数和满足
$$
S_r:=\frac1{(2q)^r}
 \sum_{|F|=r}|p_F|^{-1}
\le\frac{D^r(m+q+1)^{pr}}{r!}
\tag{4.3}
$$
对某个固定 $D>0$ 成立。因此
$$
\boxed{
\|\mathcal B_r\|\le S_r
\le\frac{\exp(pr^3+O(r))}{r!}.
}
\tag{4.4}
$$
这里使用
$r\log((m+q+1)/m)=O(rq/m)=o(1)$。
主项将精确消去 $p_F$，不是把倾斜或相位当成小的标量扰动。

## 5. 完整 gauge 误差与主项

令 $\gamma_F(Q)=J_FQJ_F$，并令 $s_k=-1$ 当 $k\in F$、否则为 $1$；
置 $\ell=m+q-1$。
真实递归给，对全部这样的 $F$ 一致，
$$
\|\gamma_F(N_k)-s_kN_k\|\le
\begin{cases}
2\alpha_m/\alpha_k,&k<m,\\
2\eta_k,&m\le k\le\ell,\\
0,&k>\ell.
\end{cases}
\tag{5.1}
$$
窗口允许有孔，不要求 $F$ 相邻。

置 $R_j^-=V(-c_jN_j)$。定义
$$
\widehat X_F=X_b+\sum_{j\in F}a_j(R_j^--R_j),
$$
$$
\widehat K_{n,F}
=K_n+\sum_{j\in F}a_j^n
 \big(L_n(R_j^-)-L_n(R_j)\big),
\qquad
\widehat Y_F=\Phi(\widehat{\mathbf K}_F),
$$
$$
A_F=(\widehat X_F-\widehat Y_F)-T,\qquad
E_F=\gamma_F(T)-(\widehat X_F-\widehat Y_F).
\tag{5.2}
$$
每个 $\widehat K_{n,F}$ 仍在 $\mathcal A$ 中且字符为零，所以同一全纯芽有定义。
$A_F\in\mathcal A$，与 $T$ 在完整域交换。

固定 $n\le d$，由 (2.2) 及 (1.1)，
$$
\|\widehat K_{n,F}-K_n\|
\le C_n\sum_{j\in F}|a_j|^n
\le C_n' r m^{-2p}.
\tag{5.3}
$$
所以充分大 $r$ 时，§3 的轮廓预算对全部 $F$ 一致适用。

低位和可用 Cauchy–Schwarz 与真实权比估计为
$$
\sum_{k<m}|a_k|^n\frac{\alpha_m}{\alpha_k}
\le C_n''\bar\eta_{m-1},\qquad n\ge1,
$$
其中 $\bar\eta_j=e^{-770\,16^j}$；
窗口内则用 $\sum_{k\ge m}\bar\eta_k\le2\bar\eta_m$。
结合 (2.3)、固定多项式的幂差及 (3.3)，得到
$$
\boxed{\|E_F\|\le C_E\bar\eta_{m-1}.}
\tag{5.4}
$$
常数独立于窗口大小和所选集合。

准确有理式是
$$
V(-cN)-V(cN)=4cN(I-c^2N^2)^{-1}.
\tag{5.5}
$$
因此令
$$
P_F=4\sum_{j\in F}a_jc_jN_j,
$$
便有
$$
\boxed{
\|A_F-P_F\|\le C_A r m^{-2p},\qquad
\|P_F\|\le C_P r m^{-p},\qquad
\|A_F\|\le C_0 r m^{-p}
}
\tag{5.6}
$$
对充分大 $r$ 成立。
第一式中的真实有理余项至多 $C r m^{-p}\bar\eta_m$，已由超快进位吸收到右侧。
$\widehat Y_F-Y$ 用的是 (3.2) 和 (5.3)。

## 6. 全部自然幂域与对称求和后的误差

令
$$
X_{b,>\ell}=X_b-a_*I-\sum_{k\le\ell}a_kR_k.
$$
它与 $X_b$ 相差有界项，故完整域仍为 $\mathcal D=\operatorname{Dom}X_u$。
有限柱是这个尾 first 的图核心：R125 的核心收敛加上 R176 的范数有界倾斜差即可。
任何支撑于前 $\ell+1$ 位的局部矩阵保持有限柱，并与尾部有限截断交换；
以图核心逼近和尾 first 闭性延拓，得到完整尾域交换。

各 $\mathcal A$ 元素也保持 $\mathcal D$，并与 $X_b$ 及该尾完整交换。
由 (5.2) 的具体构造，$E_F$ 保持 $\mathcal D$，与同一个 $X_{b,>\ell}$ 完整交换。
于是若
$$
D_\ell^{\rm bd}=a_*I+\sum_{k\le\ell}a_kR_k-Y,\qquad
d_r=2\|D_\ell^{\rm bd}\|,
$$
则
$$
\operatorname{ad}_T^sE_F
=\operatorname{ad}_{D_\ell^{\rm bd}}^sE_F,\qquad
\|\operatorname{ad}_T^sE_F\|\le d_r^sC_E\bar\eta_{m-1}.
\tag{6.1}
$$
所有右侧算子保持完整域。
粗界 $\sum_{k\le\ell}|a_k|\le\sqrt{\ell+1}\|a\|_2$ 已足给
$$
\log(1+d_r)=O(r^2).
\tag{6.2}
$$

对 $f\in M$、$v=J_Ff$，
$Tv=-(A_F+E_F)v$。
递归
$$
Q_0=I,\qquad
Q_{n+1}=\operatorname{ad}_TQ_n-Q_n(A_F+E_F)
$$
同时证明 $v\in\operatorname{Dom}T^n$ 与 $T^nv=Q_nv$。
给 $A_F$ 权1，给 $\operatorname{ad}_T^sE_F$ 权 $s+1$；
每个权 $n$ 多项式的系数绝对值总和至多 $(n+1)!$。
唯一不含误差的项是 $(-A_F)^n$。因此
$$
\boxed{
\|T^rJ_Ff-(-A_F)^rJ_Ff\|
\le(r+1)!C_E\bar\eta_{m-1}
 (1+\|A_F\|+d_r)^r\|f\|.
}
\tag{6.3}
$$

### 6.1 非交换误差

将 (6.3) 乘完整绝对系数和 $S_r$，得到上界
$$
\bar\eta_{m-1}\exp(O(r^3))\|f\|\longrightarrow0.
\tag{6.4}
$$
这是因为 (4.4) 的 $pr^3$、(6.2) 的 $r\log(1+d_r)$ 及阶乘都已计入，
而负对数为 $-770\,16^{m-1}$。

### 6.2 Bell 主项替换

由 (5.6) 的真实幂差，
$$
\|A_F^r-P_F^r\|
\le C_A r^2(C_0r)^{r-1}m^{-p(r+1)}.
$$
乘 (4.3)，利用 $r!\ge(r/e)^r$，完整误差至多
$$
\boxed{
C_1 r\,m^{-p}C_2^r e^{O(rq/m)}\|f\|
\longrightarrow0.
}
\tag{6.5}
$$
这正是双侧同幂尾的用途：分母损失 $m^{pr}$ 与主幂 $m^{-pr}$ 抵消，
留下 $m^{-p}=e^{-pr^2+o(1)}$ 吸收全部固定底数的指数。
不能对不同幂次的上下界无证套用这个抵消。

### 6.3 重复位与纯主项

所有实际 $N_j$ 交换且 $N_j^2=\eta_jN_{j+1}$，所以
$$
P_F^r=4^r r!p_F\prod_{j\in F}N_j+\mathcal E_F,
$$
$$
\|\mathcal E_F\|
\le\bar\eta_m(C_Pr m^{-p})^r.
$$
经 (4.3) 求和后，误差至多
$\bar\eta_m C_3^r e^{O(rq/m)}\|f\|\to0$。
又因物理位 $E_jJ_j=E_j$，
$$
\left\|\left(\prod_{j\in F}N_j\right)J_F-\prod_{j\in F}E_j\right\|
\le r\bar\eta_m.
$$
主项总系数绝对值不超过 $2^r$，故最后误差不超过
$2^rr\bar\eta_m\|f\|\to0$。

因此若
$$
C_{m,q}=\frac2q\sum_{j=m}^{m+q-1}E_j,
$$
则
$$
\boxed{
\mathcal B_rM\subseteq\operatorname{Dom}T^r,\qquad
\|T^r\mathcal B_rf-C_{m,q}^rf\|\le\varepsilon_r\|f\|,
\quad\varepsilon_r\to0.
}
\tag{6.6}
$$
由于 $p_F$ 含全部 $a_jc_j$，这里的主项没有留下倾斜因子或相位。

## 7. 同一个全 Haar 强近单位

在 $q$ 位计算基的 $s$ 孔层上，
$\sum E_j$ 的范数平方至多 $(s+1)(q-s)\le(q+1)^2/4$，各层像正交。
所以
$$
\|C_{m,q}\|\le1+1/q,\qquad \|C_{m,q}^r\|\le e^{r/q}.
$$
若 $f$ 是低于第 $m$ 位的有限柱，则
$2E_jf=(1-\chi_j)f$，故
$$
\|(C_{m,q}-I)f\|=q^{-1/2}\|f\|,
$$
$$
\|(C_{m,q}^r-I)f\|
\le r q^{-1/2}(1+1/q)^{r-1}\|f\|\longrightarrow0
$$
因为 $q=r^4$。
有限柱稠密与一致算子界遂给全空间强收敛 $C_{m_r,q_r}^r\to I$。
由 (6.6)，
$$
\boxed{T^r\mathcal B_rf\longrightarrow f\qquad(f\in M).}
\tag{7.1}
$$
未知核向量不需要预设任何尾速率。

## 8. 多变量低头差的真实 A 因子与四次交换子界

固定局部矩阵 $D$，支撑在前 $h$ 位。置
$$
K_{n,\ge h}=\sum_{j\ge h}a_j^nL_n(R_j),\qquad
Y_{\ge h}=\Phi(K_{2,\ge h},\ldots,K_{d,\ge h}).
$$
所有尾累积量仍字符为零。
定义
$$
Z_h=a_*I+\sum_{j\ge h}a_jR_j+
  \left(\sum_{j<h}a_j\right)I-Y_{\ge h},
$$
$$
G_h=\sum_{j<h}a_j(R_j-I)-(Y-Y_{\ge h}),
\qquad T=Z_h+G_h.
\tag{8.1}
$$
$D$ 与 $Z_h$ 在完整域交换；$G_h\in\mathcal A$ 有界，也与 $Z_h$ 完整交换。

对有限个低位，
$$
R_j-I=-2c_jN_j(I+c_jN_j)^{-1}
=A\left(-\frac{2c_j}{d_j}A^{2^j-1}(I+c_jN_j)^{-1}\right).
\tag{8.2}
$$
又因为 $L_n(1)=0$，存在固定多项式 $\widetilde L_n$ 使
$L_n(v)=(v-1)\widetilde L_n(v)$。因此每个
$$
K_n-K_{n,\ge h}=A\,U_{n,h}
\tag{8.3}
$$
都有由有限和给出的明确有界 $\mathcal A$ 因子。

对 $\Phi$ 的多变量 Cauchy 式逐坐标作预解式差，
并使用全部坐标和尾坐标互相交换，得到
$$
Y-Y_{\ge h}
=\sum_{n=2}^d(K_n-K_{n,\ge h})L_{n,h}
=A\sum_{n=2}^dU_{n,h}L_{n,h},
\tag{8.4}
$$
其中 $L_{n,h}\in\mathcal A$ 是固定多圆周上的有界预解式积分。
$h$ 固定，所用范数不必对 $h$ 一致。
故
$$
\boxed{G_h=A U_h,\qquad U_h\in\mathcal A\subset B(H).}
\tag{8.5}
$$
这不是“零字符即可除以 $A$”；(8.2)—(8.4) 给出了准确有限低头因子。

由完整尾域交换，
$$
\operatorname{ad}_T^rD=\operatorname{ad}_{G_h}^rD.
$$
每个嵌套交换子有界、保持完整一阶域，并递归保持所有自然幂域；
相应 Leibniz 公式由逐次完整域交换得到。

原实际权的 R109 估计为
$$
W_n=\|A^n\|\le
\exp\left[-\frac{100}{15}n^4+105n^3\right],\qquad W_0=1.
$$
$A,U_h$ 交换，故 $\|G_h^n\|\le W_n\|U_h\|^n$。
展开有界交换子，并用
$s^4+(r-s)^4\ge r^4/8$、$s^3+(r-s)^3\le r^3$，得到
$$
\boxed{
\|\operatorname{ad}_T^rD\|
\le\|D\|(2\|U_h\|)^r
 \exp\left[-\frac56r^4+105r^3\right].
}
\tag{8.6}
$$
复相位、倾斜及有限多变量只改变固定 $U_h$，不改变四次主阶。

## 9. 完整配对闭合排核

$X_b$ 与 $Y\in\mathcal A$ 都在真实完整域上 $C$ 自伴，故 $T$ 同样如此。
记 $\mathcal B(f,g)=\langle f,Cg\rangle$。
对 $f,g\in M$，置 $v_r=\mathcal B_rf\in\operatorname{Dom}T^r$。

第8节已支付自然幂域的 Leibniz 公式，故
$$
DT^rv_r
=\sum_{k=0}^r(-1)^k\binom rk
 T^{r-k}(\operatorname{ad}_T^kD)v_r.
$$
与 $g\in\ker T$ 作 $C$ 双线性配对，除最高项外均由真实域对称性消失：
$$
\mathcal B(DT^r\mathcal B_rf,g)
=(-1)^r\mathcal B((\operatorname{ad}_T^rD)\mathcal B_rf,g).
\tag{9.1}
$$
由 (4.4)、(8.6)，右端绝对值至多固定常数乘
$$
\frac1{r!}
\exp\left[-\frac56r^4+(105+p)r^3+O(r)\right]\|f\|\,\|g\|
\longrightarrow0.
$$
左端由 (7.1) 趋于 $\mathcal B(Df,g)$。
因此
$$
\mathcal B(Df,g)=0
\quad(f,g\in M,\ D\text{ 任意有限局部矩阵}).
\tag{9.2}
$$

原 Haar 无限张量表示中局部全矩阵代数不可约：
与所有局部矩阵交换的投影也与前 $h$ 位真空投影交换；
这些投影强趋于真空秩一投影，且局部矩阵作用真空张成稠密空间，
故该投影只能为 $0$ 或 $I$。
从而每个非零 $f$ 的局部矩阵轨道线性张成稠密。
若 $f\ne0$ 在 $M$ 中，(9.2) 取 $g=f$ 迫 $Cf$ 正交于这个稠密轨道，矛盾。
这证明定理1。

## 10. 简单根多项式的实际 Bell 分支分解

令 $q(z)=\sum_{n=0}^d q_nz^n$，$q_d\ne0$，并假设其 $d$ 个根都简单。
对变量 $\mathbf x=(x_2,\ldots,x_d)$，定义有限 Bell 多项式
$$
\beta_\ell(\mathbf x)
=\left.\frac{d^\ell}{dt^\ell}
 \exp\left(\sum_{n=2}^d x_n\frac{t^n}{n!}\right)\right|_{t=0},
\qquad \beta_0=1,\quad\beta_1=0,
$$
$$
P_q(z;\mathbf x)
=\sum_{n=0}^d q_n\sum_{k=0}^n
 \binom nk\beta_{n-k}(\mathbf x)z^k.
\tag{10.1}
$$
R176 §10 的准确倾斜 Bell 实现就是
$$
P_q(X_b;\mathbf K)\,e^w=q(u)e^w.
\tag{10.2}
$$
这是 $\operatorname{Dom}X_u^d$ 上的闭、$C$ 自伴自然算子，并具有循环向量 $e^w$ 生成的真实图核心。

在 $\mathbf x=0$ 时，$P_q(z;0)=q(z)$。
对每个简单根 $\lambda_\nu$，全纯隐函数定理给原点附近的唯一解析根
$\Phi_\nu(\mathbf x)$，满足
$$
\Phi_\nu(0)=\lambda_\nu,\qquad
P_q(\Phi_\nu(\mathbf x);\mathbf x)=0.
$$
取共同足够小的多圆盘，这些根仍彼此不同；最高系数固定为 $q_d$，故有真正的解析多项式恒等式
$$
P_q(z;\mathbf x)=q_d\prod_{\nu=1}^d
 (z-\Phi_\nu(\mathbf x)).
\tag{10.3}
$$
对交换的零字符元组 $\mathbf K$ 作同一个多变量全纯演算，得到准确有界系数恒等式。每个
$Y_\nu=\Phi_\nu(\mathbf K)$ 都属于 $\mathcal A$，并与 $X_b$ 完整域交换。

R176 的有界交换扰动域归纳给
$$
\boxed{
P_q(X_b;\mathbf K)
=q_d\prod_{\nu=1}^d(X_b-Y_\nu),
\qquad
\operatorname{Dom}=\operatorname{Dom}X_b^d
=\operatorname{Dom}X_u^d.
}
\tag{10.4}
$$
这里可逐因子减去已在下一阶域内的低阶项，得到自然乘积域的反向包含；没有只用形式因式分解。

定理1使所有因子 $X_b-Y_\nu$ 单射。
因此其真实自然乘积单射，(10.4) 左侧无核。
由完整 $C$ 自伴性其像稠密，再用 R176 (10.15) 的图循环判据，
得到 $q(u)e^w$ 循环。

一次多项式用常数解析芽的定理1；
非零常数用 $e^w$ 已证的循环性。
由此证明定理2。

## 11. 尚未付清的重复根分支

若 $q$ 有重复根，(10.3) 的标量多变量解析分支不一定存在。
不能把伴随矩阵 $Y(\mathbf K)$ 的线性化直接代入本稿：
虽然 $X_bI$ 与矩阵系数交换，$\widehat Y_F-Y$ 一般不与 $Y$ 交换，
于是第5—6节使用的
$\operatorname{ad}_T A_F=0$ 可能失败。
把该差当作 $O(rm^{-2p})$ 小量而忽略其高阶交换子，
会在乘上输入成本 $m^{pr}$ 后丢失控制。

已知单个一次因子的点态幂循环性及新二次结论仍可独立使用；
本稿不通过它们推断任意多个重复根的点态乘积。
循环向量的集合也不对范数极限封闭，不能以简单根多项式逼近重复根多项式来补这个缺口。

本稿关闭的是 (1.1) 行下的全部有限多变量解析 Bell 分支，
并由此给出实际的简单根多项式及任意复 $\ell^2$ 指数权循环性。
普通 Hilbert 不变子空间问题仍未完成。

## 使用的完整接口

- R236 对称高位平均附录：原高位平均与最高局部交换子机制；
  本稿 §§2–9 重付扩展后的统一预算和自然域。
- R176 §§7、10：高阶累积量、倾斜 first 的有界交换扰动、
  准确自然多项式域与加权图循环判据。
- R125/R161：真实有限柱图核心、完整域交换和物理进位链。
- R109：原 $A^n$ 的准确四次范数界。

