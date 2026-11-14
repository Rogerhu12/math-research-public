# 同一准确材料图册的512模区间包及完整C4余项

2026-11-12，Astra-visible-flex-fd2d / root。

**已证明的计算界。** 本记录只扩充原固定 balanced seed 的材料角图册表示，
不增加中央形状参数、不改变物理 g，也不把当前粗 BVP 的残差当成已达精度。
原95模均值包、中央 provider、accepted6 的准确曲线定义和轴区间均保持不变。

## 1. 准确目标与已经支付的解析带

沿用 `2026-11-12-fd2d-balanced-exact-moment-intervals.md` 的准确 seed

$$
\rho(\phi)=\rho_{raw}(\phi)+u_0+u_2\cos2\phi+u_4\cos4\phi,
\qquad U(\phi)=a_0^{-1}\int_0^\phi\rho(v)\,dv.
$$

准确矩给其平均值为 $a_0$。原均值定义是

$$
\mu_j=\frac1{2\pi a_0}\int_0^{2\pi}\rho(\phi)\cos(2j\phi)\,d\phi.
$$

由偶性、$\pi$ 周期性及 $U(0)=0$，准确 Fourier 展开为

$$
U(\phi)=\phi+\sum_{j\ge1}\frac{\mu_j}{j}\sin(2j\phi),
\qquad U'=1+2\sum_{j\ge1}\mu_j\cos(2j\phi).
\tag{1}
$$

原证明在 $|\operatorname{Im}\phi|\le\delta=1/20$ 上给
$|\rho_{raw}|\le r+D$：logistic 指数的虚部绝对值小于 $\pi/2$，
分母实部至少1。对复 Fourier 积分平移上下轮廓即得

$$
|\mu_j|\le M e^{-2j\delta},\qquad M=(r+D)/a_0,\quad j>2.
\tag{2}
$$

这里只对 j>2 使用 (2)，因为矩修正的两个非恒定项准确只占 j=1,2。
指数衰减同时支付 (1) 的逐项微分到任意固定阶。

## 2. 真实的512模求值与第一次区间膨胀

两次都使用同一2048点梯形公式，四重对称化后实际评价513个节点，
以及已经证明的 Fourier 混叠界

$$
E_m\le\frac{2(r+D)e^{-(2048-m)\delta}}{1-e^{-2048\delta}}.
\tag{3}
$$

第一次直接把原脚本的70位区间 Chebyshev 递推延长到 j=512。
session38883 自然 exit0，36.60秒，但最高区间宽达到约 $8.795\times10^{123}$，
报告的 `all_mean_widths_below_1e_16=false` 原样保留。
这些包含式没有因宽而变成错误区间，但它们不能支付所需图册精度。
原因是长区间递推的依赖膨胀；(3) 在最高 m=1024 处仅约 $3.677\times10^{-22}$。
该失败是求值表示问题，不是 seed、解析带或几何解失败。

第二次另名脚本 `scripts/fd2d-balanced-weighted-means-blocks.py` 每32项用
直接区间 $\cos(2(j-1)\phi)$、$\cos(2j\phi)$ 重启递推，再应用准确恒等式

$$
\cos(2(j+1)\phi)=2\cos(2\phi)\cos(2j\phi)-\cos(2(j-1)\phi).
$$

每个重启值和每步运算都包住准确三角值；归纳说明整个加权和仍是同一梯形和的区间。
所以原 (3) 的混叠证明及矩区间传播完全不变，而依赖膨胀只在32项内传播。
session35010 自然 exit0，23.04秒；全部512均值的最大区间宽

$$
\max_j\operatorname{width}(\mu_j)<4.390\times10^{-18}.
$$

最大宽仍来自既有 $u_4$ 矩区间，未为更窄的额外精度偏好重算原矩。

两份原始输出超过1MB，按根规矩提交其无损gzip，原始JSON本地保留：

| 记录 | 解压后SHA-256 | gzip SHA-256 |
|---|---|---|
| `2026-11-12-fd2d-balanced-weighted-means-512-01.json.gz`（宽度失败） | `35af5e20d30622196b85f322318c3adc5fdfe140d82ce6a8dd8fef4c8a523f6f` | `100acfea9997ad1e820433a91a93bc757cada8eb764ad6b00fe34696b94b52e0` |
| `2026-11-12-fd2d-balanced-weighted-means-512-02.json.gz`（可用） | `e4826072c89271dcd91a618721654b4527ab0b3036896d1603b948057d53a1c7` | `41bb9029e103d2a4d93ea635e77fbab5d1a42d9764eeeac6052c91d08b33b4e3` |

## 3. 全部未保留模的明确和式

令 $J=512$、$N=J+1$、$t=e^{-2\delta}$，以第2包每个 dyadic 区间的
**准确有理中点** $\widehat\mu_j$ 定义 $U_J$。记该区间半宽为准确有理数 $e_j$。
这些中点在本段不再舍入成 binary64；若消费者另行舍入，必须计入该舍入误差。

对无穷尾，(2) 给

$$
\|U-U_{\le J}\|_\infty
\le\frac{M t^N}{N(1-t)},
\tag{4}
$$

而对 k=1,2,3,4，

$$
\|(U-U_{\le J})^{(k)}\|_\infty
\le 2^k M t^N
\sum_{q=0}^{k-1}\binom{k-1}{q}N^{k-1-q}S_q(t),
\tag{5}
$$

其中几何级数及其三次求导准确给

$$
S_0=\frac1{1-t},\quad S_1=\frac t{(1-t)^2},\quad
S_2=\frac{t(1+t)}{(1-t)^3},\quad
S_3=\frac{t(1+4t+t^2)}{(1-t)^4}.
$$

证明 (5)：令 j=N+h，展开 $(N+h)^{k-1}$ 并用
$S_q=\sum_{h\ge0}h^qt^h$，再用 (1) 每次微分产生的因子2j。
对 k=0，只须使用 $1/j\le1/N$，得到 (4)。

有限系数区间的不确定度分别贡献

$$
E_{0,finite}=\sum_{j=1}^J e_j/j,
\qquad E_{k,finite}=2^k\sum_{j=1}^J j^{k-1}e_j\quad(k\ge1).
\tag{6}
$$

因为每个 $e_j$ 已来自包含梯形混叠和矩区间的最终均值区间，(6) 没有遗漏它们。
将 (4)/(5) 与 (6) 相加，就包住准确 U 与实际有理多项式 $U_J$ 的完整差。

## 4. 实算严格预算与消费范围

`scripts/fd2d-balanced-chart-fourier-tail.py` 用80位区间算术及输入完整 dyadic 端点，
准确有理求和 (6)，区间评价 (4)–(5)。真实工具 chunk d27a14 自然 exit0，约.723秒。
输出 `2026-11-12-fd2d-balanced-chart-fourier-tail-01.json`，SHA
`314240aeaf1bf354ad4e6e1d86c300695cdca2a3fc9eef049879013bec985057`。
向外取短小数的上界为：

| 导数阶 k | 仅无限尾 | 含有限区间中点误差的总界 |
|---:|---:|---:|
| 0 | 3.394e−24 | 1.331e−18 |
| 1 | 3.482e−21 | 4.868e−18 |
| 2 | 3.639e−18 | 2.987e−17 |
| 3 | 3.804e−15 | 1.166e−14 |
| 4 | 3.978e−12 | 1.180e−11 |

可复现命令：

```sh
python scripts/fd2d-balanced-weighted-means-blocks.py \
  --moments notes/2026-11-12-fd2d-balanced-moments-taylor-01.json \
  --out notes/weighted-means-512-reproduction.json --count 512 --angular 2048 --restart-every 32
python scripts/fd2d-balanced-chart-fourier-tail.py \
  --means notes/2026-11-12-fd2d-balanced-weighted-means-512-02.json.gz \
  --moments notes/2026-11-12-fd2d-balanced-moments-taylor-01.json \
  --out notes/chart-tail-reproduction.json
```

这使移动图册 $u=(1-\beta(x))U(\xi)+\beta(x)\xi$ 的真实物理角与导数可连续包围。
其 BVP native η/ζ 场仍是原保存的共享C1 cubic，指数 n=nref·expη 不能截断成另一张有限场。
当前 small01 粗插值在非配点处的残差仍约 $10^{-5}$；本图册证书不降低该残差，
不会把配点精度、图册精度、连续 metric 或强闭核混成一个已完成结论。
