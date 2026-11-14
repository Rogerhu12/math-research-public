# R241：有限头四次进位成本与漂移 first 的全部点态多项式循环

日期：2026-11-12（UTC）。作者：kernel。状态：已证明；root 已完成新进位、分母成本与投影推导全文核验，域来源另与 R207/R176 对照。本稿不声称规范等振幅交替行或一般不变限制像稠密已解决。

## 1. 结论与准确范围

沿用本课题的 Haar 模型，令
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a\in\ell^2,\qquad X=X_u.
$$
记
$$
s_m=a_*+\sum_{j<m}a_j,\qquad
B_m=\sum_{j<m}|a_j|,\qquad
g_m=\left(\sum_{j\ge m}|a_j|^2\right)^{1/2}.
$$

**漂移判据。** 若
$$
|s_m|\longrightarrow\infty,\qquad
\frac{(1+B_m)\sqrt m\,g_m}{|s_m|^2}\longrightarrow0,
\tag{1.1}
$$
则不存在非零闭子空间 $M\subseteq H$ 同时满足
$$
M\subseteq\operatorname{Dom}X,\qquad XM\subseteq M.
\tag{1.2}
$$
这里甚至不另行要求 $AM\subseteq M$；由闭图定理，(1.2) 中的 $X|_M$ 自动有界。

因而：

1. 最高系数为 $\{A\}'$ 中实际有界单位的任意正次数自然多项式 $P(X)$ 都单射、像稠密。
2. 任意非零标量多项式 $q$，以及任意
   $$
   w=c_*+\sum_jb_j\chi_j,\qquad b\in\ell^2,
   $$
   均有 $q(u)e^w$ 对 $A$ 循环。
3. 这覆盖真正的全平面连续谱 first，例如
   $$
   a_{2k}=\frac1{2k+1},\qquad
   a_{2k+1}=-\frac{\kappa}{2k+2},
   \qquad \kappa>0,\quad\kappa\ne1.
   \tag{1.3}
   $$
   两个相位各自不可和，所以不是已知的可和相位缺陷空谱类。

本稿使用的旧结果是 R125/R128 的真实闭 first 与域交换、R207 附录 A–B 的指数次数尺度及自然幂界、R176 的自然多项式最大图与 Bell 核接口。下文把新幂估计和投影推论全部独立展开。

## 2. 实际有限头、全部有限柱投影及自然域

令
$$
N_j=A^{2^j}/d_j,\qquad
V_j=(I-N_j)(I+N_j)^{-1}.
$$
模型的实际算子恒等式与范数界为
$$
N_j^2=\eta_jN_{j+1},\qquad
0<\eta_j\le e^{-770\,16^j},\qquad
\|N_j\|=1,\qquad
\|(I+N_j)^{-1}\|\le3.
\tag{2.1}
$$
所有这些有界算子彼此交换；每个逆都是实际有界逆。

定义
$$
H_m=\sum_{j<m}a_j(V_j-I)
=-2\sum_{j<m}a_jN_j(I+N_j)^{-1},
\qquad
Z_m=X_{\sum_{j\ge m}a_j\chi_j}.
\tag{2.2}
$$
R125/R128 的有限头分解是在完整闭域上的等式：
$$
X-s_mI=H_m+Z_m,\qquad
\operatorname{Dom}Z_m=\operatorname{Dom}X.
\tag{2.3}
$$
$H_m$ 有界，属于 $\mathcal A\subseteq\{A\}'$，保持 $\operatorname{Dom}Z_m$，并与 $Z_m$ 域交换。归纳得到
$$
\operatorname{Dom}(X-s_mI)^p=\operatorname{Dom}Z_m^p,\qquad
(X-s_mI)^p=\sum_{k=0}^p\binom pk H_m^kZ_m^{p-k}
\tag{2.4}
$$
在这个真实自然域上成立。

为明确反向域包含，若 $f\in\operatorname{Dom}(Z_m+H_m)^{p+1}$，归纳已知 $f\in\operatorname{Dom}Z_m^p$，且 $(Z_m+H_m)^pf\in\operatorname{Dom}Z_m$。其二项式中全部低于 $p$ 的项本已在 $\operatorname{Dom}Z_m$ 中；相减得 $Z_m^pf\in\operatorname{Dom}Z_m$。所以没有只证明形式二项式而漏掉自然域。

令
$$
Q_m=I_{H_{<m}}\otimes|\Omega_{\ge m}\rangle\langle\Omega_{\ge m}|
\tag{2.5}
$$
是所有只依赖前 $m$ 位的函数的正交投影。它的秩为 $2^m$，满足 $Q_m\to I$ 强收敛。这里保留整个低头空间，绝不是一个全零或全一物理柱投影。

尾 $Z_m$ 在物理张量分解中只作用 $H_{\ge m}$。R207 附录的指数次数尺度估计给一个仅依赖固定模型的常数 $C<\infty$，使
$$
\operatorname{Ran}Q_m\subseteq\bigcap_{r\ge1}\operatorname{Dom}Z_m^r,
\qquad
\|Z_m^rQ_m\|\le(Cg_m\sqrt r)^r\quad(r\ge1).
\tag{2.6}
$$
其域理由是：尾真空属于每个正指数次数权空间；将尺度 $1\to0$ 分成 $r$ 个步长，每次作用真实闭 $Z_m$ 后仍在下一步的正权空间中。全部头分量正交，尾算子是头上的恒等张量，所以常数不随 $2^m$ 增长。

具体可取 R207 附录中的
$$
C=16+C_K,\qquad
C_K=\frac{18e^2\|\eta\|_2}{1-e\eta_*},
\qquad \eta_*=\sup_j\eta_j.
$$
后续只用 $C$ 固定有限。

固定 $p\ge1$，写
$$
D_{m,p}=Cg_m\sqrt p.
$$
则 (2.6) 对全部 $0\le r\le p$ 统一为
$$
\|Z_m^rQ_m\|\le D_{m,p}^r.
\tag{2.7}
$$
$r=0$ 时按恒等作用解释；若 $g_m=0$，正次尾幂为零。

## 3. 二进制进位总成本

**引理 3.1。** 对任意 $m\ge1$、非负整数 $k_0,\ldots,k_{m-1}$，若
$$
k=\sum_{j<m}k_j\ge\max(2m,16),
$$
则
$$
\left\|\prod_{j<m}N_j^{k_j}\right\|
\le \exp(-\gamma k^4),\qquad
\gamma=\frac{770}{16^4}.
\tag{3.1}
$$

**证明。** 置
$$
n=\sum_{j<m}k_j2^j.
$$
将所有重复因子依次向高位进位。准确的进位次数 $c_j$ 和最终二进制位 $r_j\in\{0,1\}$ 满足
$$
c_{-1}=0,\qquad
k_j+c_{j-1}=r_j+2c_j\quad(j\ge0),
\tag{3.2}
$$
其中 $k_j=0$ 对 $j\ge m$，且各列只有有限个非零值。由 (2.1)，实际算子乘积准确等于
$$
\prod_{j<m}N_j^{k_j}
=\left(\prod_{j\ge0}\eta_j^{c_j}\right)
 \prod_{j:r_j=1}N_j.
\tag{3.3}
$$
右端最后的乘积范数至多 1。令
$$
C_{\rm car}=\sum_jc_j,\qquad
E_{\rm car}=\sum_j16^jc_j.
$$
将 (3.2) 求和，得
$$
C_{\rm car}=k-\operatorname{popcount}(n).
\tag{3.4}
$$
又 $n\le k2^{m-1}$，从而
$$
\operatorname{popcount}(n)\le m+\lfloor\log_2 k\rfloor.
$$
当 $k\ge2m$、$k\ge16$ 时，$m\le k/2$、$\log_2 k\le k/4$，所以
$$
C_{\rm car}\ge k/4.
\tag{3.5}
$$

还需证明大量低位进位不能规避高位的真实成本。由 (3.2)，对每个 $\ell\ge0$，
$$
c_{j+\ell}\ge\left\lfloor\frac{c_j}{2^\ell}\right\rfloor.
\tag{3.6}
$$
若 $c_j\ge1$，取 $\ell=\lfloor\log_2 c_j\rfloor$。此时 $c_{j+\ell}\ge1$，故
$$
E_{\rm car}\ge16^{j+\ell}
\ge16^j(c_j/2)^4.
$$
因此对全部 $j$ 都有
$$
c_j\le 2E_{\rm car}^{1/4}2^{-j}.
$$
求和给
$$
C_{\rm car}\le4E_{\rm car}^{1/4},\qquad
E_{\rm car}\ge(C_{\rm car}/4)^4\ge(k/16)^4.
\tag{3.7}
$$
结合 (2.1)、(3.3)，即得
$$
\left\|\prod N_j^{k_j}\right\|
\le e^{-770E_{\rm car}}\le e^{-\gamma k^4}.
$$
证明完成。

此处的 $k$ 是总因子数，而不是形式幂阶 $n$。阈值只线性依赖低头位数 $m$，没有支付 $2^m$ 的幂阈值。

## 4. Cayley 分母的完整成本

**引理 4.1。** 对全部 $k\ge0$，
$$
\|H_m^k\|\le(6B_m)^k.
\tag{4.1}
$$
进一步，当 $k\ge\max(2m,16)$ 时，
$$
\boxed{\|H_m^k\|\le(6B_m)^k e^{-\gamma k^4}.}
\tag{4.2}
$$

**证明。** 展开实际有限和 (2.2)：
$$
H_m^k=(-2)^k
\sum_{k_0+\cdots+k_{m-1}=k}
\frac{k!}{\prod_jk_j!}\,
\prod_{j<m}a_j^{k_j}N_j^{k_j}(I+N_j)^{-k_j}.
\tag{4.3}
$$
每个因子彼此交换，所以可以先把全部 $N_j$ 因子一起进位，再估计分母因子。分母的总次数恰为 $k$，故
$$
\left\|\prod_{j<m}(I+N_j)^{-k_j}\right\|\le3^k.
\tag{4.4}
$$
它不依赖各 $k_j$ 的分布，也不在进位后重新为高位分母付费。使用引理 3.1 后，对绝对值系数求和正好是
$$
\sum_{\sum k_j=k}\frac{k!}{\prod_jk_j!}\prod|a_j|^{k_j}
=B_m^k.
$$
这给 (4.2)；不使用进位衰减就得 (4.1)。所有分母都是 (2.1) 的实际逆，没有形式取消或无界商。证毕。

对 $m\ge8$，定义
$$
A_m=\max(1,6B_m),\qquad
\delta_m=A_m e^{-\gamma(2m)^3}.
\tag{4.5}
$$
由 (4.2)，当 $k\ge2m$ 时，
$$
\|H_m^k\|\le\delta_m^k.
\tag{4.6}
$$
此外 $B_m\le\|a\|_2\sqrt m$，因此 $\delta_m\to0$。

## 5. 四倍头长的全柱自然幂界

取
$$
p=4m,\qquad D_m=D_{m,4m}=2C\sqrt m\,g_m,\qquad m\ge8.
\tag{5.1}
$$
由真实二项式 (2.4) 和 (2.7)，
$$
\|(X-s_mI)^{4m}Q_m\|
\le\sum_{k=0}^{4m}\binom{4m}k\|H_m^k\|D_m^{4m-k}.
\tag{5.2}
$$

将和分成 $k<2m$ 与 $k\ge2m$。后半部分由 (4.6) 至多为
$$
(\delta_m+D_m)^{4m}.
\tag{5.3}
$$
前半部分用 (4.1)：

- 若 $A_m\ge D_m>0$，则对 $k<2m$，
  $A_m^kD_m^{4m-k}\le(A_mD_m)^{2m}$，因此前半部分至多
  $2^{4m}(A_mD_m)^{2m}$。
- 若 $D_m>A_m$，则每个 $A_m^kD_m^{4m-k}\le D_m^{4m}$，因此前半部分至多 $2^{4m}D_m^{4m}$。
- 若 $D_m=0$，前半部分为零。

所以对全部情况统一有
$$
\boxed{
\|(X-s_mI)^{4m}Q_m\|^{1/(4m)}
\le
2\sqrt{A_mD_m}+3D_m+\delta_m
=:\varepsilon_m.
}
\tag{5.4}
$$
使用了对非负数的 $(v+w)^{1/p}\le v^{1/p}+w^{1/p}$；无需把低头和尾当作正交像。

共同共轭 $C$ 保持前 $m$ 位柱空间，因而 $CQ_m=Q_mC$。由 $X^*=CXC$，有
$$
\operatorname{Ran}Q_m\subseteq\operatorname{Dom}(X^*)^{4m},
\qquad
\boxed{
\|(X^*-\overline{s_m}I)^{4m}Q_m\|^{1/(4m)}
\le\varepsilon_m.
}
\tag{5.5}
$$
这里用共轭把已经证明的具体域搬过去，没有假设全部自然幂满足
$\operatorname{Dom}X^p=\operatorname{Dom}(X^*)^p$。

## 6. 在同一个未知闭空间上的投影恒等式

设 $M$ 是满足 (1.2) 的闭空间，令 $Y=X|_M$。$X$ 闭且 $M$ 闭，所以闭图定理给 $Y\in B(M)$。

对 $f\in\operatorname{Dom}X^*$、$y\in M$，通常伴随的定义给
$$
\langle P_MX^*f,y\rangle
=\langle f,Xy\rangle
=\langle P_Mf,Yy\rangle.
$$
故在完整通常伴随域上
$$
P_MX^*f=Y^*P_Mf.
\tag{6.1}
$$
对实际自然幂域逐次迭代，得到
$$
P_M(X^*-\overline{s_m}I)^pf
=(Y^*-\overline{s_m}I)^pP_Mf.
\tag{6.2}
$$

如果 $s_m\in\rho(Y)$，将 (6.2) 用于 $f\in\operatorname{Ran}Q_m$、$p=4m$，再用 (5.5)，得
$$
\boxed{
\|P_MQ_m\|
\le
\left(\|(Y-s_mI)^{-1}\|\varepsilon_m\right)^{4m}.
}
\tag{6.3}
$$
所有算子都属于同一个假设的未知空间 $M$ 或其到原 $H$ 的投影；没有运输 $M$、替换成规范共轭核或使用边界表示。

在 (1.1) 下，
$$
\frac{A_mD_m}{|s_m|^2}\longrightarrow0.
\tag{6.4}
$$
而 $|s_m|\le|a_*|+B_m\le C_*A_m$，所以
$$
\frac{D_m}{|s_m|}
=\frac{A_mD_m}{|s_m|^2}\,\frac{|s_m|}{A_m}
\longrightarrow0.
\tag{6.5}
$$
又 $\delta_m/|s_m|\to0$。因此
$$
\frac{\varepsilon_m}{|s_m|}\longrightarrow0.
\tag{6.6}
$$
当 $m$ 足够大时，$|s_m|>\|Y\|$，Neumann 级数给
$$
\|(Y-s_mI)^{-1}\|\le\frac1{|s_m|-\|Y\|}.
$$
所以 (6.3) 的右端趋零，甚至其 $4m$ 次根趋零：
$$
\|P_MQ_m\|\longrightarrow0.
\tag{6.7}
$$
另一方面 $Q_m\to I$ 强，故 $P_MQ_m\to P_M$ 强。只能有 $P_M=0$，即 $M=0$。这证明漂移判据。

## 7. 最高系数可逆的自然多项式全部无核

令
$$
P(X)=\sum_{k=0}^p E_kX^k,\qquad
E_k\in\{A\}',\qquad p\ge1,\qquad E_p\text{ 有界可逆}.
\tag{7.1}
$$
R176 §2 给其准确闭域 $\operatorname{Dom}X^p$。为把核内有界性接口完整说清，固定 R128/R140 的正则器 $R=R(t)$，置
$$
Z=R^p,\qquad Q=P(X)R^p\in\{A\}'.
$$
R176 §§3、8 的最大图等式给
$$
\ker Q=\ker P(X)=:M.
\tag{7.2}
$$
其反向包含的实质是：若 $Qf=0$，则用 $R(s)^pf\to f$ 和
$P(X)R(s)^pf=0$，由 $P(X)$ 的闭性把 $f$ 放回自然域。

由于 $Q$ 与 $X$ 域交换，对 $f\in M\subseteq\operatorname{Dom}X$，
$$
QXf=XQf=0.
$$
所以 $XM\subseteq M$。漂移判据给 $M=0$。R176 §4 的完整 $C$ 自伴性
$$
P(X)^*=CP(X)C
$$
随即给 $\ker P(X)^*=0$，即其像稠密。

这不是把标量算子多项式与点态多项式混同；下一节才使用真正的 Bell 系数。

## 8. 全部点态多项式及任意第一阶指数权

R176 §7 给每个非零标量多项式 $q$ 一个最高系数为非零标量的实际 $\mathcal A$ 系数多项式 $P_q$，使
$$
P_q(X)1=q(u),\qquad
\operatorname{Dom}P_q(X)=\operatorname{Dom}X^{\deg q}.
\tag{8.1}
$$
常向量 $1$ 循环并属于该域；R176 §5 的真实图核心等式为
$$
[q(u)]_A=\overline{\operatorname{Ran}P_q(X)}.
\tag{8.2}
$$
第 7 节已给右端为 $H$，所以全部非零 $q(u)$ 循环。

再取任意 $w=c_*+\sum b_j\chi_j$、$b\in\ell^2$，置 $\xi_w=e^w$。R176 §10 已证明：

- $\xi_w$ 循环，且属于所需全部真实自然幂域；
- 倾斜 first 为 $X_b=X+H_{a,b}$，其中 $H_{a,b}\in\mathcal A$ 有界并与 $X$ 域交换；
- 存在最高系数为 $q_pI\ne0$ 的 $\mathcal A$ 系数多项式 $P_{q,b}$，使
  $$
  q(u)e^w=P_{q,b}(X_b)\xi_w,
  $$
  且该向量的循环空间恰为对应闭自然多项式的像闭包。

因为 $H_{a,b}$ 有界且域交换，将 $P_{q,b}(X+H_{a,b})$ 作真实二项式展开，仍是最高系数 $q_pI$ 的 $X$ 自然多项式，全部系数属于 $\{A\}'$，准确域保持为 $\operatorname{Dom}X^{\deg q}$。第 7 节遂给其单射稠密。因此
$$
\boxed{q(u)e^w\text{ 对 }A\text{ 循环}}
\tag{8.3}
$$
对全部上述 $q,w$ 成立。非零常数 $q$ 则直接归于 $\xi_w$ 的循环性。

## 9. 真正的全平面谱实例

对 (1.3)，任意固定 $a_*\in\mathbb C$ 都有
$$
s_m=\frac{1-\kappa}{2}\log m+O(1),\qquad
B_m=\frac{1+\kappa}{2}\log m+O(1),\qquad
g_m=O(m^{-1/2}).
\tag{9.1}
$$
其中奇偶截断只改变 $O(m^{-1})$；例如
$$
\sum_{k<n}\frac1{2k+1}=H_{2n}-\tfrac12H_n,\qquad
\sum_{k<n}\frac1{2k+2}=\tfrac12H_n.
$$
因此
$$
\frac{(1+B_m)\sqrt m\,g_m}{|s_m|^2}
=O((\log m)^{-1})\longrightarrow0.
$$
判据完全覆盖这些行。

正系数子列、负系数子列的绝对和均为无穷。对任意旋转角 $\theta$，正负两类的相位缺陷系数分别为 $1-\cos\theta$、$1+\cos\theta$；不可能同时为零。因此不存在可和相位缺陷方向，R138 的完整谱分类给
$$
\sigma(X)=\mathbb C
$$
且每点都是连续谱。这与本稿排除有界限制及 Bell 多项式核完全相容：全空间谱集本身没有排除这些核，本稿使用了全柱高次投影恒等式。

更一般地，周期复系数
$$
a_j=\frac{\omega_{j\bmod d}}{j+1},\qquad
\frac1d\sum_{r=0}^{d-1}\omega_r\ne0
$$
也满足 (1.1)。若非零的 $\omega_r$ 不全在同一正射线上，则仍无可和相位缺陷方向，因而也给全平面谱的新例。

## 10. 保留的核心缺口

本稿没有证明：

- 等振幅规范交替 $a_j=(-1)^j/(j+1)$，或一般 $a_j=(-1)^j(j+1)^{-\sigma}$、$1/2<\sigma\le1$ 的危险平方核为零；其 $s_m$ 不发散，不能套 (1.1)；
- 一般复 $\ell^2$ first 在每个闭 $A$ 不变限制中像稠密；
- 从原 $H$ 中不存在有界 $X$-不变空间，直接推到任意商空间具有同一结论；
- 整个 Hilbert 不变子空间问题已经完成。

新的正结果是一个原先属于全平面谱分支的明确慢尾类，其全部单模式点态多项式和第一阶指数加权碰撞均已通过同一未知空间上的真实高次恒等式关闭。

