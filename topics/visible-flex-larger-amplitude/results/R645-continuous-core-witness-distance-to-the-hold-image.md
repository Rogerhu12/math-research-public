# R645：准确旋转核心点到完整 hold 规范化带边像的连续距离

**本条已证明的实际结论。** 对下述准确旋转核心点 $p$，以及 [R644](R644-certified-embedding-of-the-hold-prefix-and-mirror.md) 中同一规范化 hold 前缀的完整上下镜像带边像 $\mathcal A\cup J\mathcal A$，在 [R638](R638-global-positive-arclength-coordinates-for-two-prefixes.md) 相同的向外 binary64 算术模型下，

$$\boxed{\operatorname{dist}(p,\mathcal A\cup J\mathcal A)>\frac{2397}{2500}=0.9588>\frac{19}{20}.}$$

这是唯一一次预先固定的全 **2098 胞、4 径向子胞、4096 角点**连续覆盖的结果。它不修改已有场、构造角数、精确度量或缩放定义，不重新计算有限均值；不是对采样距离加一句连续性。当前对象仍有边界，本条不给闭面握持比例，也不把 $p$ 冒称为尚未构造的另一 flex phase 的点。

## 1. 固定点与固定像

对象是 [R644](R644-certified-embedding-of-the-hold-prefix-and-mirror.md) 的同一 hold 场及其上下镜像，输入 SHA256 为 `aa1cf41faf83a9e2b3e90167d0bc9e00e48c8d84cc2aec707c2da17c45f0ca15`。保留其准确共同 binary 五次定义、精确 HoldProfile、N4096 构造和

$$G(s,\phi)=c(s)+\lambda(s)(F(s,\phi)-c(s)),\quad c=(0,0,Z_0),\quad \lambda=a/b.$$

记 $S$ 为保存的 binary 1.02。上片像为 $\mathcal A=G([0,S]\times S^1)$，镜像完整带边像为 $\mathcal A\cup J\mathcal A$，$J(x,y,z)=(x,y,-z)$。R638 的角重参不改变这些像。

选定的原核心坐标为精确有理数

$$m=\sum_{j=0}^{320}R_j(0)=
\frac{14004764077009438831816268197}{9903520314283042199192993792}.$$

核心所有 Z 系数准确为零，而 $\phi=0$ 的 T 正弦项准确为零。因此定义

$$\boxed{p=\operatorname{Rot}_{\pi/2}G(0,0)=(0,m\lambda(0),0).}$$

这把点准确绑定到当前规范化核心，而不是把原始核心坐标当成已缩放坐标。特别地没有假定 $\lambda(0)=1$；准确含义是

$$\lambda(0)=\frac{a(0)}{4096^{-1}\sum_{j=0}^{4095}|F_\phi(0,2\pi j/4096)|},\qquad a(0)=1.$$

直接复用 R642 第0胞已证缩放盒

$$\lambda(0)\in[.9999999975596524,1.000000652293214],$$

以精确 Fraction 包围上述 $m$，再用向外乘法包围 $p_y$，报告中的 binary64 端点为

$$p_y\in[1.4141197875501916,\ 1.4141207134218798].$$

这里及以下机器端点按其报告中的准确 binary64 值解释。为不依赖这种小数显示约定，也可用更松的准确十进制有理区间 $[1.414119787550191,1.414120713421881]$。程序同时保存 $m$ 与两个原始缩放端点之积的准确有理数；没有假定点与各胞缩放区间独立，区间计算丢弃该相关性只会扩大包围。

所求只是 $p$ 到 $\mathcal A\cup J\mathcal A$ 的距离。该几何旋转点不被冒称为任何尚未构造的闭曲面 phase 的成员。

## 2. 复用已付缩放，覆盖真实位置

旧498胞的缩放区间来自 R642 报告 `b9813c624e47c05d6ad8cfb21ee026f9e12c83755e4e88f968748eba9a6784a6`；新1600胞来自 R644 报告 `80377514272e4d68ba8f8d9e5fefdc273c0b74ee221331bfea9a9a8df2c4e59b`。R644 已证明旧节点及旧精确标量逐点同一，故这些是当前整个 $G$ 的区间。新程序核两个报告身份、全部2098个胞元编号/端点及正缩放盒；没有重复均值、嵌入或曲率计算。

每个唯一 quintic 胞元作4个闭 dyadic 子胞，用有向 Bernstein 凸包包围 $R,T,Z-Z_0,Z_0$ 及其真实一、二阶角导数。$\lambda(s)$ 虽不必是径向多项式，但每点值均在本胞既证盒内，直接作区间组合仍覆盖全子胞；没有把它当成常数求径向导数，本项也不需要径向导数。

在随角旋转的正交坐标中，点 $p$ 的分量是 $(p_y\sin\phi,p_y\cos\phi,0)$。故令

$$u=\bigl(\lambda R-p_y\sin\phi,\lambda T-p_y\cos\phi,
Z_0+\lambda(Z-Z_0)\bigr),\qquad f=|u|^2.$$

正交旋转保持距离，$f(s,\phi)=|G(s,\phi)-p|^2$。角导数直接使用物理向量公式

$$f_\phi=2(G-p)\cdot G_\phi,\qquad
f_{\phi\phi}=2|G_\phi|^2+2(G-p)\cdot G_{\phi\phi},$$

其中 $G_\phi=\lambda F_\phi$、$G_{\phi\phi}=\lambda F_{\phi\phi}$。旋转坐标的连接项已包含在原物理角导数中，没有漏掉点在该坐标下随角变化的贡献。

## 3. 全角 Taylor 封闭

对固定 $s$，$\lambda,Z_0,p_y$ 均为常数，距离平方可写为

$$f=\lambda^2(R^2+T^2)+[Z_0+\lambda(Z-Z_0)]^2+p_y^2
-2p_y\lambda(R\sin\phi+T\cos\phi).$$

$R,T,Z$ 的最高角频为 $2M=640$。平方项频率至多 $4M=1280$，与点的交叉项频率至多 $2M+1=641$，故 $f$ 及 $f_{\phi\phi}$ 的真实三角次数不超过 $K=1280$。这里没有把位置的最高 Cartesian 频率误作 $M$，也没有对非线性乘积作 Fourier 截断。

采用 [R641 §2.1](R641-continuous-Gram-certificate-for-one-pulse-cell.md) 已证明的二导三角 Bernstein 覆盖，不重新登记该一般引理。设 $h=\pi/4096$。在 $|f_{\phi\phi}|$ 的极大点，一阶导数为零，且

$$\|f_{\phi\phi\phi\phi}\|_\infty\le K^2\|f_{\phi\phi}\|_\infty.$$

因此对一个径向子胞，若构造角网格上二导绝对值的区间上界为 $B_{2,\mathrm{grid}}$，则全角统一界为

$$B_2=\frac{B_{2,\mathrm{grid}}}{1-K^2h^2/2},$$

分母用向下包围且严格正。每个角距最近网格点至多 $h$，故对所有径向位置和角度，

$$f(s,\phi)\ge \underline f(s,\phi_j)
-h\,\overline{|f_\phi(s,\phi_j)|}-\tfrac12h^2B_2.$$

右端各量由全径向子胞凸包给出。程序对全部2098胞、4子胞和4096角点取最小，并最终向下开平方。全部角线性变换、$\sin\phi,\cos\phi$、区间四则、平方根和两个角余项均用 R638 的同一向外算术。

## 4. 实际输出与范围

固定计划全部通过，总运行时间为 855.931329 秒；没有失败后另加角数或另扫点云。准确机器输出为：

| 量 | 向外预算或身份 |
|---|---:|
| 全域距离平方下界 | 0.9193492518686062 |
| 全域距离下界（向下开平方） | 0.9588270187414443 |
| 最坏胞／子胞／角网索引 | 388／3／1023 |
| 最坏胞端点 | binary 0.9450000000000001，0.9475 |
| 最坏处径向凸包的网格距离平方下界 | 0.9195066525554785 |
| 一阶角余量 | 0.00010615696665418993 |
| 二阶角余量 | 0.000051243720218046006 |
| 此子胞的全角 $|f_{\phi\phi}|$ 上界 | 174.21710694844694 |
| 全运行最大的二导上界 | 185.82046646633952 |
| 角覆盖分母的向下界 | 0.5180857226030579 |
| 最大线性变换区间宽度 | $7.51398943066306\times10^{-13}$ |

最坏胞的既证缩放盒为 $[0.9988957035052125,1.0011126905481929]$。最终严格有理下界 $2397/2500$ 由准确 Fraction 比较验证：它的平方严格小于报告中的准确 binary 距离平方下界，而向下平方根也严格大于它。因此定理不依赖把浮点显示值误当准确十进制结论。

因为 $Jp=p$ 且 $J$ 为欧氏等距，$\operatorname{dist}(p,J\mathcal A)=\operatorname{dist}(p,\mathcal A)$，所以上片的连续距离下界同时覆盖上下镜像。R638 的角坐标微分同胚保持像，也给同一 $\widetilde F$ 下界。

此条没有完整闭面、握持区、$D$ 或某实际非全等 phase 的定义，因此不给闭面 $\delta_{\rm hold}/D$。它只支付上述明确点到当前完整带边像的距离。

## 5. 冻结来源

新源为 [2026-11-17-parallel-geometry-hold-witness-interval.py](../notes/2026-11-17-parallel-geometry-hold-witness-interval.py)，SHA256
`d83ab6bb8748f519eceb00970b8b50dc6c622889f3c6811545b2f59f826eeb9a`。
唯一算术／控制值依赖是：

- [R638 向外算术源](../scripts/parallel_20261117_arclength_interval_positive.py)：`f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d`；
- [R642 共同控制值 helper](../notes/2026-11-17-parallel-geometry-normalization-interval-tools.py)：`a685b93e888e55e8b2dc4e0505e977a6ac0f2db88c18f2db2b5889d6a7dd02d8`。

完整报告 `parallel-negative-hold-witness-interval.json.gz` 的 SHA256 为
`638ca6d7972a7caca2bd24e0ee1ff7d89e3ac76a13540a70a09520c268ab3fd4`。
它保存所有 2098 个胞的距离平方下界、准确见证坐标定义、最坏余量、全部依赖和声明范围。两个缩放报告只作已证区间数据输入；其完整身份列在 §2，入口在前后均检查，不静默接受被改动的证书。

本轮 `numerical_route` 对新源逐字只读复核了：真实次数 $4M$、物理一／二阶角导数、旋转坐标中的点、二导极值覆盖的方向、四个闭 dyadic 子胞及参数区间的合法性；未发现上述新部分的代数或覆盖缺口。该复核没有重跑数值或重新审计旧 FFT 基础，不能描述成第二次独立运行。

令 `WORK` 指向保存上述原始输入和两份已认证缩放报告的仓库外工作目录；在仓库根运行：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-geometry-hold-witness-interval.py \
  --topic topics/visible-flex-larger-amplitude \
  --input "$WORK/parallel-negative-hold-complete-base.json.gz" \
  --old-scaling "$WORK/parallel-pulse-a5-normalized-graph-interval.json" \
  --new-scaling "$WORK/parallel-negative-hold-new-graph-interval.json.gz" \
  --out "$WORK/parallel-negative-hold-witness-interval.json.gz"
```

输入场及两份缩放证书的生成配方分别在 R644／R642；此入口绑定本轮已保存的具体身份。报告含计时，重跑整份报告 SHA 未承诺相同。替换任一外部证书应先核其数学对象、完整胞端点和向外缩放界，并登记新身份，不能略过现有校验。所有可重算 raw／报告均保仓库外。
