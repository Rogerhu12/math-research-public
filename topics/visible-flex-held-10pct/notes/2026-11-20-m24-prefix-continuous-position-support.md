# 同一 M24 真核心前缀的连续位置与支撑函数证书

日期：2026-11-20。维护会话：Astra-held10-1b6d88ec-20261120。

**状态：已证明（实际执行的区间证书）。** 对下面固定的单张 $C^2$ 前缀，在整个径向区间和整个角周期上，

$$
 |F|<1.14,\qquad F\cdot n>0.504,
 \qquad |F_s\times(F_\theta/a)|>0.799.
\tag{1}
$$

这里 $F_s$ 按固定材料角求导，$n$ 取向外单位法线。这个结论支付本前缀的位置和支撑函数门；不重算曲率，不把带边前缀宣称为闭曲面，也不把当前材料圆化 $\lambda=.002$ 宣称为最终圆弧族。

## 1. 对象固定

使用 `newg-wide-lambda0p002-m24-linear` 的同一实际输入：

| 输入 | SHA-256 |
|---|---|
| `run.json` | `c44b6fd2fbb13cc9ce0451cc6ab1d3c06521de0622de27190bde94c4c550462a` |
| `physical.npz` | `f2e22fe19bb0b6fdeff79c4fa99363d9be6cbb1ef382fd882679a2b717a3030d` |
| 4672 个核心点／闭角盒 NPZ | `714de484be1cce998f74604b9d588f38084b4e4132dc3c4b84279235aaf34f35` |
| 该核心导出记录 | `b78d1e73dd058f5668706810ecde1383ca9ed0a696c2ff12e24ae55c51ab89eb` |
| 端点归一前缀高度记录 | `377b11526dec1d130985da5bf6d21e3db43db744fad57e1c09b8cc0d70e2e18e` |

本图使用 [真 R53 核心区间构造](2026-11-20-m24-r53-true-core-jet-certificate.md)、[端点归一前缀及固定均值](2026-11-20-m24-prefix-absolute-height-certificate.md) 和 `explicit_m24_prefix_pieces.py` 定义的共同右二 jet 五次 Hermite 场及角图。全部二进制输入被视作精确实常数；没有在本次计算中重新求 BVP 或改变物理参数。

令 $\psi$ 为计算角、$\theta=\psi-e(s)\sin(3\psi)/3$ 为材料角图，$G=q\mathcal B(Y)$ 为实际有限 Fourier 扰动，$H(\psi)$ 为同一真核心与冻结入口投影之差。前缀图为

$$
 F(s,\psi)=a(s)e_r(\theta)+G(s,\psi)
       +a(s)\chi(s)H(\psi)+Z(s)e_z,
 \quad Z(0)=0.
\tag{2}
$$

这里 $Z'=M_{1168}$，严格保持原来的固定 1168 点均值规则。使用的是该均值的真积分原函数，而不是另选 512 或 1536 点均值图，也不是把 GL6 的浮点高度值直接定义为原函数。

`PrefixPieces.field` 的输出已经含 $q$；证书只加一次 $G$。$H$ 始终按静态 Cartesian 分量加入，不能再随当前材料角旋转。

本次绑定的冻结入口投影二进制数组 SHA-256 为
`d8f0cb882c7f925df1b021cb278b5bfb379f63ce10f686edeef8a15d5d44c77a`。

## 2. 不再积分均值即可支付位置

已执行的端点归一前缀证书对同一 $M_{1168}$ 给出整个前缀的连续范围

$$
 .8057018470495728\le M_{1168}(s)
 \le1.0000000003290048.
$$

证书用精确有理数放宽为

$$
 \frac{161}{200}<M_{1168}(s)<\frac{1000001}{1000000}.
\tag{3}
$$

因为 $s\ge0$ 且入口高度锚为零，直接积分不等式得到

$$
 \frac{161}{200}s\le Z(s)
 \le\frac{1000001}{1000000}s.
\tag{4}
$$

因此每个径向片 $[l,r]$ 上，只需使用

$$
 Z([l,r])\subset
 \left[\frac{161}{200}l,
       \frac{1000001}{1000000}r\right].
\tag{5}
$$

这保持原来的高度锚和同一个均值函数，虽有意舍弃了 $M$ 与其他场的相关性，但不产生自由平移或新均值。证书没有再算任何 1168 点速度均值或核心积分。

## 3. 法线及完整矩形范围

令

$$
 \rho=\partial_\psi\theta>0,\qquad
 v=\frac{\partial_s\theta}{\partial_\psi\theta},\qquad
 U=F_s\big|_\theta,\qquad V=F_\theta/a.
$$

调用连续度量证书中的同一完整一阶 jet 公式，明确包含 $-vF_\psi$ 的对流项和完整 lift。对于本图的取向，参考圆柱的 $U=e_z$、$V=e_\theta$，所以

$$
 n=-\frac{U\times V}{|U\times V|}.
\tag{6}
$$

这个负号使法线朝外。$a>0$，因此归一化第二列不会改变法线方向。

在每个径向片与闭角盒的 Cartesian 积上，区间程序分别包围 (2)、$U$、$V$，再以外向舍入计算

$$
 R=\sqrt{\sum_{j=1}^3F_j^2},\quad
 L=\sqrt{\sum_{j=1}^3(U\times V)_j^2},\quad
 S=-\sum_{j=1}^3F_j\frac{(U\times V)_j}{L}.
\tag{7}
$$

只有 $L$ 的下端严格为正才进行除法。这里 $S$ 是完整位置对完整单位法线的支撑函数，不是对背景法线的投影，也没有只取 Fourier 系数范数代替实际图。

为复用已有 API，均值范围在二阶自动微分容器的零阶槽中传入；最后只读零阶槽。辅助一／二阶槽置零仅为这次**值范围**运算服务，不声明真实均值导数为零，也未以此计算曲率。

395 个径向片包含共同 Hermite 节点、归一 profile 节点和 lift 接点。4672 个相邻闭角盒连续覆盖 $[0,2\pi]$；末盒上端外向超过真 $2\pi$，由同一周期核心覆盖。真核心导出已经在核心 sector、窗和内部积分片接点分裂取包围。径向片两侧 jet 由共同 Hermite／归一 profile 定义吻合，因此对各闭片的证明覆盖所有接点。

所有初始 395 片直接通过，无需额外径向分裂。结果为

| 全域量 | 实际区间端点 | 可引用的有理放宽 |
|---|---:|---:|
| $\sup|F|$ | $\le1.1393302427229397$ | $<57/50=1.14$ |
| $\inf F\cdot n$ | $\ge0.5041830823211103$ | $>63/125=.504$ |
| $\inf|U\times V|$ | $\ge0.7993504186030218$ | $>799/1000$ |

逐片外向范围包含整个矩形；矩形覆盖完整参数域，所以取这些端点的最大／最小值即得 (1)。这不是把有限采样提升为连续结论。

## 4. 实际执行与复现

脚本 `scripts/resume_m3/certify_prefix_position_support.py`，SHA-256
`b592095918cde75952b5104e153ac0cfe6f86eb032c10a744bbf8a13bea42f12`。

本次终态 `continuous_prefix_position_and_support_certified`，395 个接受片、395 次尝试、0 次分裂；运行 186.5947 秒。输入 NPZ、完整 JSON 输出留在 scratch，不入仓库或 Release。输出 SHA-256 见本文末的记录行。

复现时先按前述真核心和高度证书的脚本／参数重建同一输入，再运行：

```bash
python scripts/resume_m3/certify_prefix_position_support.py \
  --source-run "$WORK/m3-work/newg-wide-lambda0p002-m24-linear/run.json" \
  --physical "$WORK/m3-work/newg-wide-lambda0p002-m24-linear/physical.npz" \
  --core-angle-intervals "$WORK/geometry-work/newg-m24-r53-core4672-angles.npz" \
  --core-angle-certificate "$WORK/geometry-work/newg-m24-r53-core4672-angles.json" \
  --mean-range-certificate "$WORK/n4-work/prefix-z0-normalized-certificate.json" \
  --interval-kernel scripts/finite_closure/m3_m8_closed_map/interval_geometry_kernel.py \
  --support-dir scripts/resume_m3 \
  --out "$WORK/geometry-work/newg-m24-prefix-position-support.json"
```

`$WORK` 为运行数据的父目录；命令在本课题目录执行。关键依赖源码 SHA-256：

| 源码 | SHA-256 |
|---|---|
| `certify_prefix_metric_interval_taylor.py` | `6b36ccd6bab54fa35c6fe62a433f417faf7a51b80c35b798b17567eb22714986` |
| `explicit_m24_prefix_pieces.py` | `1a0a45db78a9aa62884459a6542d20f6995ea152962030919fbbb74d8aee573e` |
| `certify_bridge_metric_fourier_taylor.py` | `fe99f0afc6ed90dac1b9b3616c857421fa621901958dfbafdbb26191c5766bb2` |
| `certify_r59_fixed_mean_ranges.py` | `ab08dc1dc7f24f6e92e3d64fcc530767cb66f5ae5a2940f953460a3274b6a1a5` |
| `interval_geometry_kernel.py` | `6234c458d303dfd2e47dcf1e1a6ee54a3d466118a8aea4d76f66013154c034e7` |

## 5. 与闭面目标的关系

这使当前同一前缀的半径和支撑函数进入 R59/R60 组合预算，并留有很大的余量。本结论本身没有重新计算 $K$，没有改变正在进行的连续度量／曲率证书，也不替代真非线性尾端条件。

当前数据给出明确的 $C^2$ 前缀对象；“exact lift”标签不自动支付保存的入口场／角图与期望圆柱材料锚的严格相等。若最终构造要在入口接入圆柱，仍须按实际入口定义支付该接缝，不能由本次支撑函数范围推断其精确匹配。整个闭曲面、全族固定 $g$ 的加密收敛、最终 $\lambda=1$、reach 和握持比例均仍另付。

完整执行输出 SHA-256：
`50aaab772da4a0815cf48c2c4844c57c5b9292e455fff28d9b697e3c403cbd4b`。


机器可读的小记录见[执行 JSON](2026-11-20-m24-prefix-position-support-execution.json)。
