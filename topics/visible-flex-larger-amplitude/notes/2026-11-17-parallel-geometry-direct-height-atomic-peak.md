# 新直接高度候选的全胞元读出：粗采样漏过的曲率峰

2026-11-17，Astra-larger-parallel-16f63c8b / geometry_amplification。

**实际数值证据；未完成。** 对 model 的 `acceptedbase-cut0-kappa` 新优化候选，独立使用全部5106个实际径向胞元读出。得到最大主曲率采样 $7.62716005$，高于优化器50个径向 panels 报告的 $6.79452998$；完整 Gram 误差 $1.32993171\times10^{-6}$，也仍超过当前 $10^{-6}$ 门。这里验证的是加入直接高度修正后的新候选，不是重复读原材料 $\lambda=.0014$ 尾场，也不是强 $\lambda=1$ 前缀或新的内向参考路线。

## 1. 同一个候选的身份与比较范围

原基底为[材料弱场实际积分 K 高度](2026-11-17-parallel-geometry-best4-material-tail.md)的 $\lambda=.0014$。新候选在该真实高度函数上加 C2 样条修正，延伸到平参考端点，并使用1552个高度变量与5个参考度量变量，共1557个已固定的实参数。`cut_fraction=0`，初圈取同一个弱基底的角原函数；内端并未接原强 b677 前缀。

候选 JSON 的 SHA256 为

```text
8fed32f53f5d839d10056c04645919e335034cf559be4e09b74efecff827eeae
```

读出全程保持这些系数不变。角点数同为512、径向 Gauss 阶同为8；主要差别是优化器只用50个径向 panels，独立读者用原接受 state、背景物理 r、全部新增样条 knots、接缝与补段端点的并集，共5106个胞元，并检查每个胞元的两个端点。总计26,142,720个角径点，累计积分使用 Kahan 补偿。

| 同一候选的量 | 优化器50 panels | 独立5106胞元 |
|---|---:|---:|
| 实际 Gram 算子误差 | $1.32877590864\times10^{-6}$ | $1.32993171242\times10^{-6}$ |
| 实际最大主曲率采样 | 6.79452997812 | **7.62716005176** |
| 参考最大子午曲率采样 | 5.99666636448 | 5.99684282157 |
| 平端高度 | 1.1392058303254877 | 1.1392058303254875 |

粗格的整体 Gram 与端点高度较稳定，不表示局部曲率极值也已被捕获。这是本次独立读出要解决的具体疑点；不将一次全胞元采样写成连续极值证书。

## 2. 字面实际几何及平端的稳定公式

[独立读者](2026-11-17-parallel-geometry-direct-height-reader.py)消费 model 的 `evaluate_height`、`atomic_radii`、初始 XY/alpha 和 Cartesian 接点修正接口。它不调用优化器的 `graph` 或已报 Gram/曲率作为答案，也不以原 P/K 方程或 curl 预测代替实际高度导数。

采用 [R631](../results/R631-compatible-height-actual-geometry-and-C2-radial-map.md) 径向构造的无 w 分母等价写法。若

$$
p=\frac{h_\phi}{r\rho},\quad E=1+w^2,\quad S=1-p^2,\quad D=ES-h_r^2,
$$

则

$$
a=\sqrt{D/S},\qquad b=-\frac{h_rp}{\sqrt S},\qquad
\alpha_r=\frac{h_r(h_{r\phi}/\rho-p)}{rS\sqrt D}.
$$

直接对这些式子求真实 r 导数，并径向积分
$F_{xy,r}=bt+an$。其中 $t=(\cos\alpha,\sin\alpha)$、$n=(\sin\alpha,-\cos\alpha)$。因此

$$
F_{xy,rr}=(b_r+a\alpha_r)t+(a_r-b\alpha_r)n.
$$

这些式子来自以 $p=wP$、$h_r=w(1+K)$ 消去 R631 的 w 商，在 w=0 的平端仍可直接评价。全程要求真实 $S,D>0$，未把负分支截断到人为下限。平面角导数由实际积分得到的 XY 求 FFT 导数，高度角导数使用同一高度函数的解析接口。最后加入同一个 Cartesian 修正的0/1/2阶导，才计算实际 Gram、法向和第二基本形式。

本次候选的初端 Cartesian Fr、Frr 两组修正系数均为0，因为它使用弱初圈；这个事实不被移用于强前缀。各实际胞元接点的 F、Fr、Frr 读出跳差均为0。

## 3. 被漏过的深端峰与未闭合的平端

最大曲率样本位于

$$
r=1.6883406815921667,\qquad \phi=\pi/2.
$$

同一点的数据是

$$
\begin{aligned}
\kappa_{\rm actual}&=7.6271600517618765,\\
\kappa_{\rm ref}&=5.025000547430837,\\
w&=.001273972669173722,\\
w_r&=-5.025012780847586,\\
h_{rr}&=-7.627175115147394,\\
S&=1,\qquad D=1.0000009576110303.
\end{aligned}
$$

这里的额外曲率不是把参考 $w_r$ 当成实际曲率产生的误读；实际高度二阶导已显著放大。该样本已否定“本候选在粗格达到6.8就已控制实际最大曲率”的数值判断，无须对同一弱候选反复运行更多网格后才登记这项问题。

全域 Gram 最大点位于真正外端 $r=1.767318285443017$、$\phi\simeq2.24574787346$，几乎全由角向相对误差 $-1.32993171220\times10^{-6}$ 主导。rr 误差最大 $8.88\times10^{-16}$，rphi 最大 $5.17\times10^{-11}$；径向构造的 rr 恒等式没有自动消去角向误差。

外端高度一、二阶径向导数最大绝对值分别约 $4.99\times10^{-18}$、$1.56\times10^{-16}$，高度散布为0。尽管高度平化，端圈仍与 $R n(\alpha)$ 有最大欧氏位移 $9.64318814\times10^{-7}$，因此尚未给出精确圆 cuff。这里使用向量欧氏范数；原优化器的 `endpoint_circle` 使用分量最大值，二者不能当作同一种量直接比较。

其他实际样本：最小 $S=.99999939394$、最小 $D=.99644841766$、最小 Gram determinant $.04824905876$；最大原点范数2.10266598005；对既有 b677 见证点 $(0,1.4141197181548968,0)$ 的最小距离1.00107561761。因为本场未与强前缀对齐，这两个位置量不被解释成完整 D 或 held 下界。

## 4. 长度筛选与本结论的边界

这一个弱初圈到外端的参考总长度约 $.6691298193056361$，其初圈最小水平半径约1.16721949816。应用 [R633](../results/R633-finite-cuff-length-budget-and-actual-endpoint-obstruction.md) 的径向必要条件不产生正的误差下限。深端到平端的参考长度约 $.07887926723349092$，最大径向需求约 $.07887928546654033$，对应采样必要误差下限约 $4.62303\times10^{-7}$。这些量属于本次新候选，不能替代 R633 对原强 cut 的严格排除。

本次实际 Gram 仍大于 $10^{-6}$，粗格曲率约束亦未得到真实全域支持，端圈未精确闭合，没有全 t、reach 或闭曲面结论。读者覆盖全部函数断点，但没有区间运算的连续极值包围。后续工作转向新的可行参考设计；本旧弱候选只完成一次必要的独立全域核对。

## 5. 冻结源、数据与复现

独立读者 SHA256：

```text
2026-11-17-parallel-geometry-direct-height-reader.py
b2cb7e04a15396e483fcbf72d5a7707c0c88312da07bc194609e121f85040faa
```

model 已确认下列三个实际读取版本冻结。候选生成时记录的入口源是 `27bbc3d68c5be12b00d800c99cc912badea66c3479e557bafbd3b8672517c3e7`。后来不仅增加了实际高度 API，还改变了优化器默认算法、加入二阶导数缩放与末端高度可行初始化，并增加了度量和绝对高度独立变化的选项。因此不能声称当前默认入口仍会执行原生成算法。读者直接加载下述冻结定义与旧候选系数；旧 JSON 没有新增的独立度量选项，冻结定义将其解释为原来的 `metric_height_coupling=True`，保持实际高度函数不变。下文的显式 replay 源恢复原生成流程，并已逐字再生全部1557个 double 系数。

```text
2026-11-17-parallel-model-direct-height-accepted-base.py
33d3a80dfaa7be55aac7afbadba57048f2623ddbbcd83a11c8d5fb3b79c7c0c1
2026-11-17-parallel-model-direct-height-autodiff.py
4501a2c65ed63974616f500dfa353b0d1294a80ed96a53e0933ad6303a227661
2026-11-17-parallel-model-direct-height-gram.py
f4c93366bb05f4379f9e2121f414f8edc3659b788b2921943d4df5b6ed1c9f6f
2026-11-17-parallel-geometry-height-mode-api.py
dc3be256fd0566d4c2dd21b2bb362d81b04e8481167e35027a73a061237775f8
```

其余冻结依赖仍为已登记的平化源、角原函数源、stable height reader 和径向读者；完整九项 SHA manifest 在输出 JSON 中。本轮运行前后再次核对这些文件，均与读入字节一致。实际输出报告 SHA 为

```text
f89a07c646097db03cb4a83bf7a78c4b786665c9f7cc706524e7c43dbfae3676
```

### 5.1 不依赖中间 template 的最小生成配方

已冻结 [replay-cut0-curvature.py](2026-11-17-parallel-model-replay-cut0-curvature.py)，其 SHA256 为

```text
d6cced1c7c605f9a9bbaee4e974ae83ad7635e658f6f0b7a88f08e7b87eea024
```

该源把原先 template 提供的全部参数直接写成可审阅的常量，不再依赖该中间 JSON。仅需以下三份已登记输入：

| 输入 | SHA256 |
|---|---|
| `parallel-model-trace0992-jets.json` | `5db66710248b645f455e1f156bc4dc6654dafd08b4387cefccbcfda1137979f8` |
| `parallel-best4-material-scale0014.json.gz` | `09d206be0c9c0a47df006920c99f33e8a95e915542f04b068b3899d767549cde` |
| `parallel-best4-background.json` | `487373a8445674658cb36ddbd20445e774612269720f58c0e6db492f38c24e15` |

生成从零系数出发；原来的线性可行初始化在本例确实返回零。采用物理角 M32/N512、50个径向面板、GL8、1552个高度变量及5个 logw 变量；高度与 logw 使用原耦合，`cut_fraction=0`、外补段 `A=.048856939517352364`、实际曲率罚权 `.1`、目标曲率 `6.8`。源中显式保留旧的 B1/m²B0 对角缩放，未使用后来的 B2 缩放；L-BFGS-B 参数为 `maxiter=300`、`maxfun=1200`、`maxls=30`、`maxcor=30`、`ftol=1e-14`、`gtol=1e-9`。不调用后来的末高可行初始化、Armijo 或长度罚项。为保持原浮点运算次序，外段参考 w 使用原多项式评价，未换成等价的因式分解评价。

从仓库根目录执行：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-model-replay-cut0-curvature.py \
  --trace /workspace/scratch/16f63c8bce6b/parallel-model-trace0992-jets.json \
  --state /workspace/scratch/16f63c8bce6b/parallel-best4-material-scale0014.json.gz \
  --background /workspace/scratch/16f63c8bce6b/parallel-best4-background.json \
  --out /workspace/scratch/16f63c8bce6b/parallel-model-cut0-curvature-replay.json
```

本次实际 replay 另传入可选的 `--compare /workspace/scratch/16f63c8bce6b/parallel-model-direct-acceptedbase-cut0-kappa.json`，只用于生成之后比较，不参与初值、目标函数或求解。21次函数调用、17次迭代后，得到相同的 cost `1.773255963294775e-12` 和粗格曲率 `6.7945299781218464`。新旧系数数组 `array_equal=True`，最大差为 **0**；按 little-endian float64 连续字节计算，两者系数 SHA256 均为

```text
46b9fa16550323411895dd9d72e159676f933e174e65309d1947b350999c6d78
```

本次含比较元数据的新输出报告 SHA256 为

```text
665a1dca4ed289016cf6d04c7eb3a267837683989686351642473e82c4d725b1
```

新报告加入 replay 入口、冻结依赖、比较结果和新的运行时间，因此其 JSON 字节不同于原 `8fed32...`；不把它冒称同一 raw 文件。实际几何参数已逐字相同，既有独立全胞元读数仍绑定原候选，且不需要为相同参数再次运行全域读者。

### 5.2 独立读者命令

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-geometry-direct-height-reader.py \
  --input /workspace/scratch/16f63c8bce6b/parallel-model-direct-acceptedbase-cut0-kappa.json \
  --angles 512 --radial-gauss 8 --mean-gauss 12 \
  --out /workspace/scratch/16f63c8bce6b/parallel-model-cut0-kappa-actual-n512-g8.json
```

原始输入、输出和系数均留在 scratch，不入库。该接口可用于另一组冻结候选的必要真实核对；它不自动把任何优化状态升级为已接受强场。
