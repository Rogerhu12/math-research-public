# best4 完整物理角 M32 尾：实际 Gram、曲率与投影读出

2026-11-17，Astra-larger-parallel-16f63c8b / geometry_amplification。

**状态：实际数值证据。** 在同一 best4 固定背景上，真正接受的物理角 $M=32,\lambda=10^{-4}$ 场，经完整112项固定 $\rho$、实际 integral-K 高度及径向构造，N1024/G8 到 N2048/G12 的 Gram 采样为
$2.04539654\times10^{-6}\to2.04539712\times10^{-6}$；实际主曲率约5.997643。真实深端物理均高为1.13913067157。它是一个有限弱幅度尾场，尚未成为强前缀 $\lambda=1$ 的完整接合。

本条沿用 [R631 实际高度到几何](../results/R631-compatible-height-actual-geometry-and-C2-radial-map.md) 和已发表 [完整物理角高度读者](2026-11-17-parallel-geometry-weighted-actual-tail.md)；BVP 构造由 numerical_route 另行登记。这里不从 solver success 推断实际度量，而是重新读位置及其真实一、二阶 jets。

## 1. 输入、角规范与新读者

实际输入 `parallel-best4-weighted-m32-scale1e4.json.gz` SHA256：

```text
47c4f2838c24c319717d7493417ef1424fa49675bcce9ec720bef1f8d3a59bed
```

背景 `parallel-best4-background.json` SHA256：

```text
487373a8445674658cb36ddbd20445e774612269720f58c0e6db492f38c24e15
```

输入状态为物理角 $\widetilde P=h_\phi/(rw)=\rho P$ 的32个 sine 系数、K 的32个非均值 cosine 系数及普通物理角均值 $c_\phi$。全部112项 $\rho$ 保留，采样范围 $[.166020389935392,4.613861129346341]$。浅端高度锚为真正物理角均值 $.9703876955889461$；没有使用材料角均值 $.9196724$。

[稳定物理角适配器](2026-11-17-parallel-geometry-stable-weighted-height-reader.py) 将冻结的完整 $\rho$ 链式导数与 [同一字面均值方程的残差停止](2026-11-17-parallel-geometry-best4-material-tail.md#2-同一均值方程的浮点停止修正) 组合。它不裁切 $\rho$，不改 B、K 插值或隐式微分。对原已发表物理 $\lambda=10^{-7}$ 场三个实际读点，hr、hrr、hphi、cr 与旧读者完全一致，c 差不超过 $2.27\times10^{-19}$。

本次每次根求解均报告字面 $Q_N(\rho B)$。加密运行最大残差 $3.551\times10^{-15}$，最大允许浮点残差约 $3.647\times10^{-15}$，未将其清零。积分高度相对原字段的最大变化为 $|\Delta\widetilde P|=4.153\times10^{-8}$、$|\Delta K|=3.681\times10^{-10}$。它仍是明确的新相容高度候选。

## 2. 同场实际加密

4593个原子单元，覆盖物理半径
$[1.167318285443017,1.6884392650708613]$ 的完整有限输入域，包括每个单元两端的一侧值。N1024/G8 与 N2048/G12 分别读47,032,320和131,690,496个角—径向点。

| 实际采样量 | N1024/G8 | N2048/G12 |
|---|---:|---:|
| 最大相对 Gram 算子 | $2.0453965359\times10^{-6}$ | $2.0453971183\times10^{-6}$ |
| 最大径向 Gram | $8.89\times10^{-16}$ | $1.12\times10^{-15}$ |
| 最大交叉 Gram | $2.145\times10^{-12}$ | $4.233\times10^{-12}$ |
| 最大主曲率 | 5.99764276661 | 5.99764287836 |
| 最小 Gram determinant | .0482490415964 | .0482490415633 |
| 最小 L | .939888863590 | .939782409280 |
| 最小 D | .999742442478 | .999742442478 |
| 最大接点 Fr 跳跃 | $1.111\times10^{-16}$ | $2.225\times10^{-16}$ |
| 最大接点 Frr 跳跃 | $5.701\times10^{-14}$ | $7.750\times10^{-14}$ |

高度系数 Gauss8/12 原函数节点比较差 $6.777\times10^{-21}$，单元积分差之和 $2.640\times10^{-20}$。初圈 literal 角相容误差分别 $2.10\times10^{-13},4.24\times10^{-13}$，随后的 Gram 来自实际位置角导数，未用兼容误差预测代替。

加密后的最大 Gram 在深端最后一个单元，主要为角向长度分量。曲率最大点在
$r=1.273694551916472,\phi=1.8315730607354554$，同点固定背景径向曲率5.99683153214。背景全域采样最大5.99684279446。与较大的材料角场不同，这个弱物理场没有产生显著额外深尾曲率峰。

两次读出固定原输入和 K 插值；角网加密也加密字面均值求积。这是实际几何求积/角网比较，不是又一次 BVP 接受，也不是连续误差上界证明。

## 3. 实际位置与固定见证点

两次深端均高完全一致：

$$
h_{0,\phi}(r_{\rm deep})=1.1391306715668115,
\quad\Delta h_{0,\phi}=.16874297597786536.
$$

加密实际高度范围为 $[.9703732836856053,1.1391443254852591]$。
沿用 [材料尾实际测量](2026-11-17-parallel-geometry-best4-material-tail.md#5-实际位置见证点和不付出的完整条件) 的 b677 真实 core 见证点
$p=(0,1.4141197181548968,0)$，得

$$
\min_{
\rm sampled\ tail}|F-p|=1.0012660482182896,
\qquad
\max_{
\rm sampled\ tail}|F|=2.0367810122299135.
$$

最小距离发生在浅端 $r=1.167318285443017,\phi=\pi/2$；最大原点范数发生在有限深端。关于 z=0 的镜像保留这两个量。该弱场尚未与完整强前缀同字段对齐，因此这里不给整个闭面的 held-distance 或 D 下界/上界；采样极值也不替代连续域证书。

本次真实高度低于旧宽 .05 bridge 物理弱场的1.2627，但不同背景/幅度的这项比较不支付真正 $\lambda=1$ 或未读的无限尾。有限深端不是设计中的完整平 cuff 半径1.767318。

## 4. 现有嵌入判据的实际投影输入

新增 [投影观察器](2026-11-17-parallel-geometry-radial-projection-reader.py) 只读取冻结径向重构的实际 $X=F^{xy}$、$X_r$、$X_\phi$。其中 $X_\phi$ 由存下的 **literal** 角误差加回 $qt$ 恢复，不使用 PDE 预测。

记 $R=|X|$、$\beta=\arg X$、$J_{xy}=\det(X_r,X_\phi)$，有实际恒等式

$$
\beta_\phi=\frac{\det(X,X_\phi)}{R^2},\qquad
\left.\partial_rR\right|_\beta
=\frac{R J_{xy}}{\det(X,X_\phi)}.
$$

[R9 §1](../results/R9-cylindrical-graph-global-embedding.md) 的固定方位角严格单调论证可在这里以平面半径作为排序坐标；[R27](../results/R27-explicit-star-shaped-graph-extension.md) 已有真实星形边界的图接口。本条只给该实场可直接读取的输入，不重复登记一般嵌入理论。

| 投影量的最小实际采样 | N1024/G8 | N2048/G12 |
|---|---:|---:|
| R | 1.167311035041 | 1.167311035041 |
| $\beta_\phi$ | .166018824862 | .166018824862 |
| $J_{xy}$ | .193773803013 | .193773803013 |
| $\partial_rR|_\beta$ | .999871212946 | .999871212946 |

初圈多边形的计算绕数为1和 $1+2.22\times10^{-16}$。若这些条件在连续域有证书，且初圈真正绕数为1，则各圈是按 R 严格嵌套的星形曲线，XY 投影全局单射，实际尾段成为平面环域上的高度图。本次只是对现有框架给出带明显余量的实际采样，未从采样正性宣称完成嵌入证明。

## 5. 复现、冻结源和未完成责任

本次新增两个源的 SHA256：

```text
2026-11-17-parallel-geometry-stable-weighted-height-reader.py
cd0702a1ea124e44938a87384ef8fa9ba09e8d3f2999ce6405d5f5086cc82612
2026-11-17-parallel-geometry-radial-projection-reader.py
d96d6fae6754173b190ac753ac3dcb98b98d6dc820d3e03c822f056bda46644c
```

复用的材料 stable reader、radial reader、radial-measure、angular helper 的 SHA 已在 [材料几何记录 §6](2026-11-17-parallel-geometry-best4-material-tail.md#6-冻结源与复现) 冻结；物理链式导数适配器 SHA 为
`edff3edcdbc135658d6ef22aff905ea48f59f7c25a27f607dca7a91c2f7ecc7a`。

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-geometry-radial-measure.py \
  --input /workspace/scratch/16f63c8bce6b/parallel-best4-weighted-m32-scale1e4.json.gz \
  --background /workspace/scratch/16f63c8bce6b/parallel-best4-background.json \
  --height-reader topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-geometry-stable-weighted-height-reader.py \
  --radial-reader topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-geometry-radial-projection-reader.py \
  --height-anchor left --anchor-mean-height .9703876955889461 \
  --witness-prefix /workspace/scratch/16f63c8bce6b/parallel-refine0992-m112-t8.json.gz \
  --angles 2048 --radial-gauss 12 \
  --out /workspace/scratch/16f63c8bce6b/parallel-best4-weighted-m32-scale1e4-radial-measure-n2048.json
```

粗读用 `--angles 1024 --radial-gauss 8` 并另存。两份历史报告的 SHA256 为

```text
N1024/G8
2f4ce799e780f92baf7685d74c09f73186ac7a978ee8cc0c55b117487c68ca0d
N2048/G12
99369245f1f51a3de81a16b7c1e8a23d26f845101ad2d063c5dc80dd7ab8f358
```

重新运行耗时不同，报告字节 SHA 可变；应核输入和源码身份及相应数学字段。raw 不入库。

未支付责任仍为强前缀的全部模式与 Cartesian 2-jet 接合、有限 depth4 之后的同一实际尾、平 cuff、固定闭盖、连续域极值、完整闭面的全体点对 reach 和全族条件。这里 $\lambda=10^{-4}$ 不能更名为本课题完成。
