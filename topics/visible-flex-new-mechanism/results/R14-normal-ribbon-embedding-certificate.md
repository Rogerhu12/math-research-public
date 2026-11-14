# R14：法弦近远点对分解与有限宽准确核心嵌入

日期：2026-11-14。

**已证明：**下列近弧长法弦界、全参数片覆盖及法向条带嵌入准则。**当前数值状态：**只运行了合成单位圆与双覆盖圆的廉价实现检查；真实 ψ-warp 候选仍交公开 Actions。此证书不包含圆领、握持区或完整闭曲面的 reach 下界。

## 1. 核心中心曲线的准确曲率

沿用 [R12](R12-warped-ruled-core.md)：$|d|=1$，$k=|d_\phi|>0$，$c_\phi=b\,d\times d_\phi$。令

$$
T=\frac{d_\phi}{k},\qquad B=d\times T,
\qquad \kappa=\frac{\det(d,d_\phi,d_{\phi\phi})}{k^3}.
$$

则 $T_\phi=k(-d+\kappa B)$、$B_\phi=-k\kappa T$，从而

$$
c_\phi=bkB,\qquad
c_{\phi\phi}=bk_\phi B-bk^2\kappa T.
$$

因此中心曲线速度为 $bk$，曲率绝对值准确为

$$
K_c=|\kappa|/b.
\tag{1}
$$

同时 $d\perp c_\phi$、$|d|=1$，所以 $X(s,\phi)=c(\phi)+s d(\phi)$ 是中心曲线的一个单位法向条带。这个论证允许 $\kappa$ 变号和等于零，不需要 Frenet 标架在那些点有定义。

## 2. 近点对的法弦界

设 $\gamma:[0,\ell]\to\mathbb R^3$ 是单位速 $C^2$ 曲线，$|\gamma''|\le K$，其中 $K>0$，并且

$$
0<\ell\le\frac{\pi}{2K}.
$$

记 $\Delta=\gamma(\ell)-\gamma(0)$，$N_0$ 为起点切线的正交补。则

$$
\boxed{\frac{|\Delta|^2}{2|P_{N_0}\Delta|}\ge\frac1K,}
\tag{2}
$$

分母为零时约定左侧为无穷大。

**证明。** 单位切向在球面上的长度不超过 $K$ 倍弧长，因而

$$
|P_{N_0}\Delta|
\le\int_0^\ell\sin(Kr)\,dr
=\frac{1-\cos(K\ell)}K.
$$

这里 $Kr\le\pi/2$ 保证正弦单调。另一方面，把位移投影到中点切向，

$$
|\Delta|\ge
\int_0^\ell \cos\big(K|r-\ell/2|\big)\,dr
=\frac{2\sin(K\ell/2)}K>0.
$$

两式相除并使用 $1-\cos t=2\sin^2(t/2)$，得到 (2)。反向走同一弧时起点法平面不变，所以可选任一方向的较短已控制弧。

## 3. 全参数片覆盖给中心曲线 reach 下界

将构造角圆周分为 $N$ 片，已知每片的完整位置 box 与导数 box。令 $a_j$ 为第 $j$ 片弧长的定向上界。对两片 $I_i,I_j$，如果从 $I_i$ 的左端走到 $I_j$ 的右端，或反向绕圆周走的完整覆盖弧长上界，不超过 $\pi/(2K)$，那么其中任意两点都由 (2) 覆盖。

对其余片对，用三维位置 boxes 计算两片之间的距离下界。设所有这些剩余片对的共同下界为 $d_{\rm far}$；若没有剩余片对，忽略这一项。定义

$$
r_* = \min\{1/K,\ d_{\rm far}/2\}.
\tag{3}
$$

如果 $r_*>0$，曲线首先是嵌入：同一个或近片对中的不同参数由上述正弦弦长下界分开，远片对由 $d_{\rm far}>0$ 分开。所有不同像点都满足

$$
|q-p|^2\ge 2r_*|P_{N_p}(q-p)|.
\tag{4}
$$

近片对由 (2)，远片对由 $|P_{N_p}(q-p)|\le|q-p|$ 给出。只要某点 $z$ 到曲线的距离小于 $r_*$，它就不能有两个不同的最近点 $p,q$：最近点条件给 $z-p\in N_p$，等距条件给

$$
|q-p|^2=2(z-p)\cdot(q-p)
\le2|z-p|\,|P_{N_p}(q-p)|,
$$

与 (4) 矛盾。因此

$$
\operatorname{reach}(c)\ge r_*.
\tag{5}
$$

这里不把网格样本当成全参数片。整个对角附近由弧长引理处理，其余完整片对全部枚举；若区间太宽导致下界为零，程序只报告未证明。

## 4. 准确有限宽鞍带的嵌入

假设 $r_*>w\ge0$。对 $z=p+s d_p$、$|s|\le w$，由 (4) 有

$$
\begin{aligned}
|z-q|^2-|z-p|^2
&=|q-p|^2-2s\,d_p\cdot(q-p)\\
&\ge |q-p|^2\left(1-\frac{w}{r_*}\right)>0
\end{aligned}
$$

对每个 $q\ne p$ 都成立。故 $p$ 是 $z$ 唯一的最近中心点，不同中心点的法向 ruling 不相交；同一中心点上 $s$ 也唯一。结合准确度量的正则性，紧参数带 $[-w,w]\times S^1$ 的映射 $X=c+s d$ 是光滑嵌入。

该结论只证明核心本身无自交。曲面的主曲率仍由核心说明中的形算子计算；远端连接可能产生新的自接近，不能从 (5) 推出完整闭曲面的 reach。

## 5. 定向实现与公开 Actions

独立脚本 `scripts/warped_ruled_tube.py` 消费已冻结的 `certified_centerline` API，不修改原核心或连接器。弧长上界来自完整 $c_\phi$ boxes；前缀和用十进制定向区间，减法保留两端包围，避免把两个上界相减误当成差的上界。每个位置 box 转为 binary64 区间时再向外一步，全部三维片对运算也逐步向外舍入。

合成检查存于 `notes/warped-ruled-tube-check-20261114.json`：

- 准确单位圆分 48 片时，证明中心曲线 reach 至少约 $0.6010$，足以证明半宽 $0.1$ 的法向条带嵌入。该下界保守，不声称得到圆的准确 reach $1$。
- 同一圆的二重参数覆盖有远片重合，程序得到下界 $0$ 并拒绝参数嵌入证明。
- 全部无序片对数量核对为 $N(N+1)/2$，没有漏掉对角片、跨零角片或远片。

真实候选命令：

```bash
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/warped_ruled_tube.py \
  --warp-u .6,.8,1,1.2 --warp-v 0 --scale 1 --half-width .05 \
  --nodes 1536 --out "$RUN_DIR/warped-ruled-tube.json"
```

更省重复区间求积的方法是在已有 Actions 主循环中，对同一 `certificate` 调用 `tube_audit(certificate, half_width_text)`。它会报告中心曲线与核心的证明标志，同时始终保留 `whole_closed_surface_reach_proved=false` 和 `task_complete=false`。
