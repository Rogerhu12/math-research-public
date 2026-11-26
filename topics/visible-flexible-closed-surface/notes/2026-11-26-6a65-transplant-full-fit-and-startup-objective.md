# 非退化后段融合场：完整拟合与明确的新启动目标

2026-11-26，Astra-visible-flex-6a65e705。新 baseline，不是接受步或等距核。

## 1. 实际换入的完整位置输入

消费[真实旧强后段融合场](2026-11-26-6a65-geometry-cauchy-strong-transplant.md)，
full sample SHA `8843c2e3909764ad254fe813ff210e48dd443d959bb9c6cb324136443420a3e5`。
其中央、Cauchy、coast、右连接和 R205 cut/cuff 都有具体函数及完整两jets。
本次保留同一 L=.75 Cauchy 标量 base、A=.8746432018013935、Z=.51，
重新用 s≤cut 的 90 个径向截面、128 个全周期角点拟合全部 J38/K11 通道。
维数 1788，物理导数权重仍 .03，拟合真秩 38，rho 初值为零。
没有沿用旧 Hermite warm 或其坏接受态的系数、目标值、normal。

## 2. 新目标完整声明及导数

[旧 warm 的首个真实 LM](2026-11-26-6a65-cauchy-first-lm-curvature-dominates.md)
已显示固定 tau=2 的曲率四次项约 8.3e9，metric 部分仅 76；总目标下降可容许 metric 急剧变坏。
这里为新输入选择明确的启动目标。令 r 为完整 R191 谱 hinge 的三个残差，q=r·r：

\[
r_{\tau}=r\sqrt{1+q/\tau^2},\quad
|r_\tau|^2=q+q^2/\tau^2,\quad \tau=10^6,
\]

\[
D r_\tau=hDr+r\frac{r\cdot Dr}{\tau^2h},\qquad h=\sqrt{1+q/\tau^2}.
\]

实现为 `../scripts/6a65-explicit-tau-curvature-hinge.cjs`，定义 schema 为
`6a65-explicit-tau-quartic-curvature-hinge-v1`。
完整真实 Gram、主曲率、谱分支、guide=9.5、外权 .01、全部点和全部参数列保留。
原四次 metric tau=.05、R219 几何 guide 及全部行保留。这个新目标主要是二次曲率启动，
它的零点仍为所有曲率 hinge 零点；有限加权目标下降不构成 reach 或等距证书。

原 R211 源码及其 tau=2 定义没有修改。最初仅传 tau=1e6 的调用被 R211 的准确
定义检查拒绝，真实 exit 1、无新场或接受步；随后才新增上述独立明确定义，并在
全局工厂中要求显式 `curvatureModel` 选择。没有绕过原 R211 检查或把新目标冒名为 R211。

本条同时改变位置初值和目标，两个总目标数值不可直接当作同一优化序列比较。

## 3. 实际完整 baseline

新 reference、全部通道拟合及完整 value 均自然 exit 0，实际耗时分别
1.255129337310791、.3011317253112793、36.19508671760559 秒。
完整 value 仍为 230490 行；没有少算坏的径向区间、角向点或几何项。

| 新拟合场自己的量 | 实际值 |
|---|---:|
| 新完整目标平方 | 38.269768167892316 |
| 四次 metric 部分 | 37.94011444889055 |
| 二次 metric 部分 | .11408316961144639 |
| 新曲率部分 | .3296535054670488 |
| metric 峰 | 2.4829784705399063 |
| 自身曲率峰 | 51.875549726426016 |
| 曲率格最小归一面积平方 | .2826856035201413 |
| 最大包球半径 | 1.481655397716746 |
| 最大绝对 y | .8145910303936289 |
| 最小 held 标记距离 | .6449455411272091 |
| 扣除允许高度后的最大超高 | −.004606811746291444 |

源场改善后的面积确实保留到实际拟合场；曲率峰在
s=.42822916666666666、u=π/2。metric 和曲率仍远未合格；held 只是有限样本。
当前从这个 baseline 启动完整 1788 列 LM，结果另记，不把启动记作完成。

## 4. 新链的一次实际参数方向核对

`../scripts/6a65-cauchy-real-curvature-jvp.cjs` 在该真实 1788 维态上，取一个
覆盖全部参数列的归一确定方向，比较完整曲率残差 JVP 与中心差分。
点为当前曲率最坏 knot、s=.4253125 的真实角节点和 s=.6 的另一角节点，
当前自身曲率分别为 51.87555、29.66675、13.73037，均在有效 hinge 分支。

| 点 | h=1e−5 相对误差 | h=5e−6 相对误差 |
|---|---:|---:|
| 当前曲率峰 | 1.08342e−9 | 1.45803e−10 |
| s=.4253125 | 4.35291e−10 | 1.59478e−10 |
| s=.6 | 1.49658e−9 | 3.30857e−10 |

进程自然 exit 0，科学秒 2.283。该有限方向核对检查新增目标的真实位置链，
不替代全空间误差界或完整 normal 的实际求解。

## 5. 复生身份

参数是本目录 `2026-11-26-6a65-transplant-fit02-parameters.json`，全部只是定义参数。
从源 NPZ 的 s≤1.0815625 和 u 生成 scratch grid 后，依次使用全局入口
`reference`、已有 `6a65-cauchy-global-warm-fit.py`、全局入口 `value`，
与[首版完整拟合](2026-11-26-6a65-cauchy-global-fit-and-real-baseline.md)的 argv 一致。

- 新全局入口 SHA：`3af74734af899d734477a6775e34ef0b64b20b85dc505e31ec8bffff3b825276`。
- 新曲率代数 SHA：`16c24dd07bbfea1129b4ad618afed16c19551f32b408ecebf63b24c8508050ae`。
- 新参数 SHA：`dc06654729944f614d9ea2ed8d26f81b86a8e78267fb26bc84dd86a830b27b61`。
- reference SHA：`1362dc06a3829d00b259f06b37326a694ea809babfc5af359d021273161e5885`。
- 实际 fitted state SHA：`97256cbc70a20c2d14775413a0d2af38a4af8f00d8d613598b944bc35f170167`。
- 实际 baseline SHA：`f19c0db9b62069e82a3fdbc66febfb3240168e4a1e6d94af39aac01c2270457e`。
- JVP 入口 SHA：`3651dcc1a689175d398ad263151288f9700a15a4a061570cde0f73f5307e1870`。

原件及逐进程外部退出回执在 scratch `geometry-work/cauchy-transplant-fit02-*`，不入 Git。
