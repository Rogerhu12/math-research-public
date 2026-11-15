# R738 增补 — 原零角 Gauss 帽与高 rho 的更高前缀替代

日期：2026-11-15。**状态：已证明。**

保 [R738](../results/R738-actual-balanced-families-and-original-kernel-prefix-alternative.md)
的同一 $F,Q,\mathcal H_2$、原矩阵和已付家族。
本增补直接使用原因子在 $t=0$ 最后一条角上的 Gauss 值，
收紧前缀容量，并把 R731 未决高 $\rho$ 条件接入同一个真实首核。

## 1. 同一原因子的准确零角整数

记原 Gauss 赋值
$$
v_0\!\left(\sum f_i(t)Y^i\right)
=\min_i\{4\operatorname{ord}_t f_i-i\},
\qquad
\boxed{d_0=-v_0(F).}
\tag{1}
$$
这里 $d_0$ 是整数，不是角函数 $d(t)=1+8t$。
由 $F(0,1)=0$、$F_Y(0,1)\ne0$，
$F(0,Y)$ 为非恒定多项式，故
$$
d_0\ge\deg_YF(0,Y)\ge1.
$$
$Q(P)$ 为单位使 $v_0(Q)\le0$。
原 $\mathcal W_D$ 每一列的 $v_0$ 均至少为 $-2$，
Gauss 赋值对同一个非零乘积可加，所以
$$
-2\le v_0(P^{\rm fact})
=4r-3d_0+v_0(Q).
$$
因此准确有
$$
\boxed{1\le d_0\le\left\lfloor\frac{4r+2}{3}\right\rfloor.}
\tag{2}
$$
没有用一个自由平面次数替代原角帽。

同一 $\mathcal H_2$ 的最后零角条件是
$v_0(B)\ge2v_0(F)=-2d_0$。
所以逐个普通 $t$ 系数有
$$
\boxed{\deg_Y[t^i]B\le4i+2d_0.}
\tag{3}
$$
这是 R495 的原倍数线性系条件；
不是把整个 $\mathcal W_D$ 都换成此较小帽。

## 2. 镜轴核的真实前缀容量

仍令
$$
K_{\rm mir}=\ker\bigl(
\mathcal H_2\to k[t]/t^T,\ 
B\mapsto B(t,\psi e^{2\eta_0})
\bigr),
\quad T=s-r-\delta_0,
$$
$\delta_0=0$ 或 $13$，取对应的 $J$ 或完整 $M$。

若 $B=t^iB_i(Y)+O(t^{i+1})\in K_{\rm mir}$，
且 $i<T$，
原轴常数为一，因而 $B_i(1)=0$。
结合 (3)，每个前缀分次的维数至多 $4i+2d_0$。
故对于 $1\le v\le T$，
$$
\boxed{
\dim\frac{K_{\rm mir}}{K_{\rm mir}\cap t^v k[[t]][Y]}
\le2v(v+d_0-1).
}
\tag{4}
$$

现在令 $m=r-k\ge1$，并考虑真实线性子空间
$$
K_{\rm mir}^{[m]}
=\{B\in K_{\rm mir}:(\mathcal EB)|_C\in t^m k[[t]]\}.
\tag{5}
$$
它包含 $F^2$，也包含 R731 中所有满足未决高 $\rho\ge r-k$
的指定镜轴代表。
若在某个分次 $i<m$，则同时有
$$
B_i(1)=0,\qquad(\mathcal EB_i)(1)=0.
$$
这两行在次数至多 $4i+2d_0$ 的多项式上独立，
所以该分次再少一维。
于是
$$
\boxed{
\dim\frac{K_{\rm mir}^{[m]}}
{K_{\rm mir}^{[m]}\cap t^v k[[t]][Y]}
\le2v(v+d_0-1)-\min(v,m),
\quad1\le v\le T.
}
\tag{6}
$$
所有分次只给上界；没有声称任意合格首项都能延成原镜轴核。
$T$ 的十三行缩短仍准确保留。

## 3. 同一实际家族的有限三择

设 R738 已给 $N$ 个线性独立的真实 $Z$ 输入
$\mathsf S_\lambda|_Z$，对应
$z_\lambda=\pi_{\rm v}\overline{\mathsf M}_0(qt^rF\mathsf S_\lambda)$。
若所有 $z_\lambda=0$，镜轴类 $[B_\lambda]$ 唯一，
并且 $F^2,B_\lambda$ 在同一个 $K_{\rm mir}$ 中线性独立。

若某个指定 $\rho_\lambda<r-k$，
R731 已给显示原格的准确两条 $p$。
若 R731 高 $\rho$ 增补中的第三块条件不成立，
同样已由原实际两行得到两条 $p$。
现在假定所有输入都落在剩余高 $\rho$ 分支；
于是 $F^2,B_\lambda$ 全部属于 (5)。

**命题 1。** 若对某个 $1\le v\le T$ 有
$$
\boxed{N+1>2v(v+d_0-1)-\min(v,r-k),}
\tag{7}
$$
则以下三者至少有一个成立：

1. 某个指定 $z_\lambda$ 在同一整单位商中为单位列；
2. 某个指定镜轴核与原 cube 的首 Bockstein
   被 R731 的实际低行严格区分，显示原格准确有两条 $p$；
3. 同一个原 $\ker\overline{\mathsf M}_0$ 中有非零来源，
   其 $t$ 前缀至少为 $r+v$。

**证明。** 若前两项均不成立，
$F^2,B_\lambda$ 张成 (5) 中一个 $N+1$ 维空间。
(6)、(7) 迫其包含一个非零的 $B_*\in t^v k[[t]][Y]$。
因此
$$
\boxed{P_*=qt^rFB_*\in\mathcal W_D}
\tag{8}
$$
是实际原首核，且 $v_t(P_*)\ge r+v$。
乘 $qF$ 不会令这个非零多项式变成零。
所有来源均来自同一个原 $\mathcal H_2$，预算不增加。证毕。

(8) 一般不是 cube。
其整原来源提升可按 R738 的真实前缀格选取；
若与原线性组合的整提升相差 $p\mathcal W_D$，
该差必须带进同一个 $R$。
本命题不自动给 (8) 的下一位提升。

在 $v=1$ 时，(7) 只需
$$
\boxed{N\ge2d_0-1.}
\tag{9}
$$
对连续 $c$ 家族，可明确取 $L=2d_0-2$。
所以 R738 的完全实际充分条件为
$$
\boxed{
c_1-c_0\ge2d_0-2,\qquad
\Delta_F>4b(d_0-1).
}
\tag{10}
$$
当 $d_0=1$ 时，只需原单个非零 $Z$ 输入：
若它既未给单位，也未给 R731 的两条 $p$，
就必有严格更高前缀的真实核。

## 4. 原 r=ell=1 的准确低门及极值范围

若 $r=\ell=1$，则 $k=0$，
(2) 给 $d_0=1$ 或 $2$。
在后一种情形，
原 Gauss 等式还迫 $v_0(Q)=0$、$v_0(P^{\rm fact})=-2$；
这是准确的饱和角边界，不额外假定 $F(0,Y)$ 的第二根。

因此只要
$$
c_1-c_0\ge2,\qquad \Delta_F>4b,
$$
最多三个连续平衡整数就足以应用命题1：
得到一个真实单位列、一个已付的两条 $p$ 显示块，
或者得到至少 $t^2$ 前缀的真实非零原首核。

只有当所用 cube 本来就达到**全原首核空间**
的最大 $t$ 前缀时，第三项才被排除。
在 cube 子类中最大化前缀不够；
新来源 (8) 不必属于该子类。

最后，单位列或显示的两条 $p$ 都没有判定整个
$\mathcal W_D$ 的指定 forcing。
原其他低列、同一个 $R$、两条十三行 carry、
完整 $U_0/\xi/V_1$ 和第三精度继续保留。

依赖：
[R491](../results/R491-valuated-source-factor-lifts-and-homogeneous-joint-obstruction.md) 的原 Gauss 因子格；
[R727](../results/R727-original-balanced-sections-and-single-residual-column-in-vertical-unit-quotient.md)；
[R731](../results/R731-specified-mirror-normal-jet-and-two-actual-smith-p-factors.md) 及
[完整第三块增补](2026-11-15-r731-complete-third-carry-and-high-rho.md)；
[R738](../results/R738-actual-balanced-families-and-original-kernel-prefix-alternative.md)。
