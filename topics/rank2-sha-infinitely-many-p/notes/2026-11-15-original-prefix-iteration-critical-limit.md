# 原前缀迭代在 9/8 临界窗中的准确计数界限

日期：2026-11-15。**状态：以下界限已证明；原指定 forcing 未解决。**

保 R738 及其零角增补的同一个原因子、原十九角面、
$K_{\rm mir}$、$d_0=-v_{0,(4,-1)}(F)$ 和
$h>\kappa,\ T-h>\kappa$。
本 note 只核定「独立 $Z$ 值产生更多核，再以更高前缀终止」这一具体推理，
不把它的不足认作原实际像已满。

## 1. 一个真实更高前缀的交数上界

记 $T_0$ 为十九角面上 $t=0$ 纤维的严格变换。
原零角四次吹起沿这条严格纤维进行。
若其相继曲线重数为 $\mu_{0,1},\ldots,\mu_{0,4}$，则
$$
C\cdot T_0=b-\sum_{j=1}^4\mu_{0,j}
=-v_{0,(4,-1)}(F)=d_0.
\tag{1}
$$
这也是原多项式在最后零角的准确平凡化计算。
$P=(0,1)$ 是 $C$ 与 $T_0$ 的光滑横截点。

设非零 $B\in K_{\rm mir}$ 的**来源**前缀至少为 $v\ge1$。
因为它在原多项式框中被 $t^v$ 整除，
其截面除子包含 $vT_0$。
同时
$$
B_1=(\mathcal EB)|_C\in t^v k[[t]],
$$
所以 R731 的 $\rho$ 至少为 $v$。

这里 $B_0=B|_C$ 不可能为零：
否则原镜轴及 $T-h>\kappa$ 迫 $B\in kF^2$，
而 $F^2$ 没有正的来源 $t$ 前缀。
于是 $B_0$ 是 $N^2$ 的非零截面，零除子次数为 $2\kappa$。
它在 $P$ 至少消到 $h+\rho\ge h+v$，
在 $v(T_0|_C)$ 的其余部分还有至少 $v(d_0-1)$ 份零。
因此
$$
\boxed{h+vd_0\le2\kappa.}
\tag{2}
$$
所有交数计重；无需假定其他交点光滑或约化。

令
$$
d_{\rm rem}=2\kappa-h.
$$
若 $d_{\rm rem}<0$，原镜轴本来只剩 $F^2$，无需下面的迭代。
若 $d_{\rm rem}\ge0$，则
$$
\boxed{
v_*=\left\lfloor\frac{d_{\rm rem}}{d_0}\right\rfloor+1
}
\tag{3}
$$
已使 $K_{\rm mir}\cap t^{v_*}k[[t]][Y]=0$。
由 $h>\kappa$，有 $v_*\le\kappa<T$，
故此处仍在 R738 前缀分次的合法长度内。

## 2. 这条终止门为何不能关闭当前临界窗

R738 零角增补对未决高 $\rho\ge r-k$ 子空间给出的前缀商上界为
$$
C_*(v)=2v(v+d_0-1)-\min(v,r-k).
\tag{4}
$$
想仅凭该上界与 (3) 排除所有指定输入被吸收，
必须有独立输入数 $N$ 满足
$$
N+1>C_*(v_*).
\tag{5}
$$
但 $v_*d_0\ge d_{\rm rem}+1$，
而对每个 $v\ge1$ 有
$2v(v-1)-\min(v,r-k)\ge-1$。
所以
$$
\boxed{C_*(v_*)\ge2d_{\rm rem}+1.}
\tag{6}
$$
另一方面所有真实 $Z$ 输入都在长度 $\kappa$ 的同一空间中，
故 $N\le\kappa$。
由 (5)、(6)，这种计数链若要产生矛盾，至少需要
$$
\kappa+1>2d_{\rm rem}+1,
\qquad\text{即}\qquad
\boxed{h>\frac32\kappa.}
\tag{7}
$$

原满主阶临界满足 $h/\kappa\to9/8$。
因此即便给这一计数法整个 $\kappa$ 维 $Z$ 空间，
(5) 也不能在该临界成立。
二维家族的实际较小独立数当然不能改变这项结论。
(7) 与 R555 已付的高接触范围相接，
没有产生一个新的临界非零定理。

本 note 不说实际 $K_{\rm mir}$ 一定达到上界 (4)，
也不说某条指定类在其像中。
更强的真实核限制、原完整 forcing、同一个 $R$ 或原中央条件
仍可能排除实际相容。
被排除的只是把现有「极点数—前缀维数—(2)」三步
直接当成 $9/8$ 窗终止证明。

依赖：
[R495](../results/R495-fixed-angular-surface-and-full-triple-source-joint-image.md)；
[R555](../results/R555-whole-original-linear-system-and-nonzero-high-contact-forcing.md)；
[R731](../results/R731-specified-mirror-normal-jet-and-two-actual-smith-p-factors.md)；
[R738](../results/R738-actual-balanced-families-and-original-kernel-prefix-alternative.md)；
[原零角增补](2026-11-15-r738-zero-angle-cap-and-high-rho-prefix.md)。
