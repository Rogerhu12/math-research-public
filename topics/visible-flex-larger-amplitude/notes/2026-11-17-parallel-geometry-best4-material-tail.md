# best4 实际尾几何：小 Gram 与深尾曲率峰并存

2026-11-17，Astra-larger-parallel-16f63c8b / geometry_amplification。

**状态：实际数值证据。** 对同一 best4 固定背景上两个真正接受的材料角有限尾场，积分实际 K，再用 [R631](../results/R631-compatible-height-actual-geometry-and-C2-radial-map.md) 的径向构造读取真实位置及导数。$\lambda=.001,.0014$ 的加密 Gram 算子采样分别为 $2.358\times10^{-7},1.421\times10^{-7}$，而实际主曲率峰分别为 $7.51359,8.47262$。后者来自实际高度二阶导数，不能用背景曲率上界6代替。

这两个场都不是 $\lambda=1$ 的完整前缀接合，未延伸到完整平 cuff，未闭合，也没有 reach 或完成标准证书。这里的极值是明确求积/角网上的证据，不是区间证明。BVP 接受与输入生成见 [best4 非线性延拓](2026-11-17-parallel-numerical-best4-tail-continuation.md)；本条不重复其求解结论。

## 1. 真正输入与几何定义

两个输入均为材料角 $\rho=1$、M8、BVP N256、source-index 坐标：

| 输入 | SHA256 |
|---|---|
| `parallel-best4-material-scale1e3.json.gz` | `a2d689c26cbe5309a61b9ab5de6fcb5b1e18ef703b28b160c01e7723ca35e210` |
| `parallel-best4-material-scale0014.json.gz` | `09d206be0c9c0a47df006920c99f33e8a95e915542f04b068b3899d767549cde` |

同一背景 `parallel-best4-background.json` 的 SHA 为
`487373a8445674658cb36ddbd20445e774612269720f58c0e6db492f38c24e15`。
物理区间为 $[1.167318285443017,1.6884392650708613]$，仅到 source depth4；设计中的完整 cuff 半径约1.767318，不能直接用有限端充当平接点。

高度锚在左端，材料均值为 $.9196724087226285$。非均值系数定义为

$$
C_j(r_a)=-\frac{r_aw(r_a)p_j(r_a)}{2j},\qquad
C_j'(r)=w(r)k_j(r).
$$

这里 $k_j$ 是接受字段的实际 cubic-Hermite 插值；$C_j''=w_rk_j+wk_{j,r}$ 使用其真实一阶导数。积分高度重新决定 P，再对字面均值 $Q_N B=0$ 求根；隐式导数决定均值高度的二阶导数。没有将 BVP 的 P 微分二次，也没有把方程 RHS 当作插值的真实导数。

随后按冻结 [径向读者](2026-11-17-parallel-geometry-radial-tail-readout.py) 积分 $\alpha_r=A_r$、$F^{xy}_r=bt+an$。径向 jets 由积分定义解析微分，角 jets 则对实际重构位置作 FFT。Gram 和主曲率来自这三组真实一、二阶导数；没有用 Darboux 预测替代它们。

## 2. 同一均值方程的浮点停止修正

冻结高度读者的旧规则要求每个 Newton 修正绝对值均小于 $2\times10^{-17}$。在本次 $.001$ 场的第4720批单元，它在同一个浮点均值附近循环：

$$
Q_NB=\pm2.15756232325\times10^{-17},\quad
\mu=.994763002915,\quad
\Delta c=\pm2.16892095597\times10^{-17}.
$$

因此原16步检查退出，未发生正分支失败。这是已实际复现的停止阈值问题。

新增 [稳定高度适配器](2026-11-17-parallel-geometry-stable-height-reader.py) 保持完全相同的 B、固定背景、K 插值和隐式导数，采用实际残差门

$$
|Q_NB|\le16\epsilon_{\rm mach}(1+Q_N|B|),
$$

并在 Newton 步上做正分支内残差下降回溯。实际均值与所用容差分别输出，不把残差写成零。适配器拒绝含物理 $\rho$ 的输入，避免把另一坐标图误当成材料角。最大实际残差均低于 $3.55\times10^{-15}$；最大容差分别约 $4.408\times10^{-15},4.670\times10^{-15}$。

## 3. 两个固定场的实际加密结果

每个原子单元都包含两端的一侧值与内部 Gauss 点。$.001$ 场4852单元，$.0014$ 场5094单元；N1024/G12 分别读出69,558,272和73,027,584个角—径向点。高度系数仍用Gauss8，独立Gauss12原函数节点差分别为 $1.085\times10^{-19},5.422\times10^{-20}$。

| 量 | $.001$, N512/G8 | $.001$, N1024/G12 | $.0014$, N512/G8 | $.0014$, N1024/G12 |
|---|---:|---:|---:|---:|
| 最大实际 Gram 算子 | $2.34581648\times10^{-7}$ | $2.35770797\times10^{-7}$ | $1.41766074\times10^{-7}$ | $1.42005075\times10^{-7}$ |
| 最大实际主曲率 | 7.513585697 | 7.513586403 | 8.472618229 | 8.472618218 |
| 最大交叉 Gram | $1.568\times10^{-12}$ | $1.641\times10^{-12}$ | $9.042\times10^{-13}$ | $1.032\times10^{-12}$ |
| 最小 L | .3729729973 | .3729729973 | .1676982005 | .1676982005 |
| 最小 Gram determinant | 1.750515287 | 1.750515286 | 1.750515285 | 1.750515286 |
| 深端高度均值 | 1.088406686371 | 1.088406686371 | 1.088386025706 | 1.088386025706 |

径向 Gram 分量不超过 $1.12\times10^{-15}$。加密后接点 $F_r$ 跳跃不超过 $2.50\times10^{-16}$，$F_{rr}$ 不超过 $5.72\times10^{-14}$。两个场的背景实际主曲率采样最大值均约5.996843。

同场非均值高度积分及均值回缩造成的变化很小：$.001$ 场 $\max|\Delta P|\le1.363\times10^{-8}$、$\max|\Delta K|\le4.277\times10^{-9}$；$.0014$ 场分别为 $1.060\times10^{-8},5.703\times10^{-9}$。它们仍是明确的新高度候选，不将这些数写成原接受字段恰好满足全部几何相容条件。

角网加密也加密字面均值求积，参数、K 字段和高度积分定义保持固定；不是新的 BVP 精化接受。最大 Gram 不要求随加密单调下降。

## 4. 曲率峰的实际来源

[峰值高度检查器](2026-11-17-parallel-geometry-peak-height.py) 验证输入、背景、适配器与几何报告 SHA 后，在报告的同一原子单元、同一位置重新读实际高度 jets。它不重新定义或替换报告的曲率。

记 $y=1+K$、$E=1+w^2$、$T=P_\vartheta$、$U=K_\vartheta-P$、

$$
S=1-w^2P^2,\quad L=y+ET,\quad
N=1+\frac{w^2yT}{S}.
$$

对参考度量 $E\,dr^2+r^2d\vartheta^2$，Darboux 方程的完整高度预测为

$$
h_{rr}^{\rm Darboux}
=\frac{w_rSN+(Ew/r)U^2}{L}.
$$

这个等式来自 $\det\nabla_g^2h=K_g(1-|\nabla_gh|_g^2)$：其 Hessian 分量为
$h_{rr}-w^2w_ry/E$、$wU$、$rwL/E$，且 $K_g=ww_r/(rE^2)$；直接整理得到上式。该式只在真正满足完整方程时等于实际 $h_{rr}$，本次误差明确保留。

在两次加密的对称角峰，P 和 U 数值为零，S=1：

| 量 | $.001$ | $.0014$ |
|---|---:|---:|
| 峰半径 r | 1.688333671457 | 1.688340741539 |
| 峰处背景径向曲率 | 5.220993341 | 5.022821859 |
| w | .001309934499 | .001273671502 |
| K | −.3885793600 | −.5218370960 |
| $K_r$ | −3298.921480 | −4766.457715 |
| L | .6948503999 | .5927668177 |
| N | 1.00000008753 | 1.00000008890 |
| $w_r(1+K)$ | −3.192231306 | −2.401732930 |
| $wK_r$ | −4.321371057 | −6.070901357 |
| 实际 $h_{rr}$ | −7.513602364 | −8.472634287 |
| 完整 Darboux 预测 | −7.513858000 | −8.473542002 |
| 实际减预测 | $2.55637\times10^{-4}$ | $9.07715\times10^{-4}$ |

因此实际二阶高度中的 $wK_r$ 已超过背景贡献。这些点 $h_r$ 很小，主曲率数值接近 $|h_{rr}|$。$N\simeq1$ 时，$w_r/L$ 的增强解释了为什么只限制背景曲率或只看最大 K 不足以控制实际曲率。该诊断支持后续真实高度优化约束 $h_{rr}$ 或实际主曲率；它不声称其他背景已改善，也不将 $.0014$ 的较小 Gram 解释为较好的 reach。

## 5. 实际位置、见证点和不付出的完整条件

新增 [位置测量钩子](2026-11-17-parallel-geometry-radial-measure.py) 只观察冻结读者的实际 F，不更换积分或 jets。实际接受前缀 `parallel-refine0992-m112-t8.json.gz` 的 SHA 为
`b677632099a08a33f94792a06dcc37d4e0f029131069b6ff94b1cb586ebaff25`。
以其 core 的 $\phi=0$ 点作四分之一转，得固定测试点

$$
p=(0,1.4141197181548968,0).
$$

| 加密实际位置量 | $.001$ | $.0014$ |
|---|---:|---:|
| 所读尾段最小 $|F-p|$ | .952114424689923 | .952075886406782 |
| 所读尾段最大 $|F|$ | 2.008872268578663 | 2.008868166400438 |
| 最小距离位置 r | 1.167318285443017 | 1.167318285443017 |
| 最小距离位置角 | $\pi/2$ | $\pi/2$ |
| 高度最小采样 | .919578994804466 | .919541629237202 |
| 高度最大采样 | 1.088458121895173 | 1.088450589386828 |

关于 z=0 的反射保持这两类距离，所以同一数值也描述镜像尾段。当前弱幅度初圈与完整强前缀不是同一个实际字段，故这些距离只是测量器验证，**不**是完整 held-distance 的下界。采样最小距离本身也不支付连续极小值的严格下界。

同理，表中最大原点范数是开放尾段的采样量，不能单独给完整闭面的 D。真实 $\lambda=1$ 场还须支付所有模式/高度/Cartesian 2-jet 接合、有限深端之后的尾、平 cuff、回头盖、全体点对 reach 和全时段检查。现有 [R632 回头盖组件](../results/R632-c2-return-cap-parallel-body-and-diameter.md) 不替代这些活动体条件。

## 6. 冻结源与复现

| 源码 | SHA256 |
|---|---|
| radial-tail-readout.py | `adc0a3e27032d966f4e193414b9646288ef0c7b191eb4e45611d5ff8134a7531` |
| stable-height-reader.py | `6730a4f9d1cc39125143c01f8d256a0b5e3b14e4466f3a7e37da820b89ed9893` |
| radial-measure.py | `1d9431e1c4837346de538cd84ed3a454cf14d4c300622b3a917915d49dd3a6e6` |
| peak-height.py | `5884d4186707203867716cd8fb864ec154508b8bc9693366fc7446e5d681293b` |
| 旧 tail-readout.py，适配器依赖 | `9606511eab76ce9a4d268af11eb62010f555753358b7f1f1ca38af6b8df44815` |
| model-angular-reconstruct.py | `63844e36ba779f8847ad72464745b334394ae2a89c720b51497d5e2029a5522f` |

均在本 notes 目录，文件名前缀为 `2026-11-17-parallel-geometry-`；最后一项前缀为 `2026-11-17-parallel-`。在仓库根目录运行：

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-geometry-radial-measure.py \
  --input /workspace/scratch/16f63c8bce6b/parallel-best4-material-scale1e3.json.gz \
  --background /workspace/scratch/16f63c8bce6b/parallel-best4-background.json \
  --height-anchor left --anchor-mean-height .9196724087226285 \
  --witness-prefix /workspace/scratch/16f63c8bce6b/parallel-refine0992-m112-t8.json.gz \
  --angles 1024 --radial-gauss 12 \
  --out /workspace/scratch/16f63c8bce6b/parallel-best4-material-scale1e3-radial-measure-n1024.json
```

另一场只把输入/输出 basename 中的 `scale1e3` 换成 `scale0014`；粗读取把 `--angles 512 --radial-gauss 8` 写入并另存报告。局部峰分解：

```sh
OPENBLAS_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-geometry-peak-height.py \
  --report /workspace/scratch/16f63c8bce6b/parallel-best4-material-scale0014-radial-measure-n1024.json \
  --input /workspace/scratch/16f63c8bce6b/parallel-best4-material-scale0014.json.gz \
  --background /workspace/scratch/16f63c8bce6b/parallel-best4-background.json
```

四份历史实际报告 SHA 依次为：

```text
lambda .001, N512/G8
c0035edc05424fb5e3730fb5e12b97ca924e7d6d387ad513e0c19f81aac8bf20
lambda .001, N1024/G12
d4fd7747eef4b1e8e34d49a0ee83bcd0a4d2aebd13fa0c8e839cede5c17b7e77
lambda .0014, N512/G8
8be8a6baf83675f9913bc906dc7fca75d3020895a18db09f95c6fe92b53c2990
lambda .0014, N1024/G12
b13955d4cfc8b103536ca4376f29d1c460a6cad16f7cd80560d6a177a74ff587
```

重新运行的耗时字段会改变报告字节 SHA；关键输入、源 SHA 与数学读出应按字段比较。raw/网格均留在临时计算区，不入库。
