# 原真 .995 切口后的向内参考度量与固定材料弦长预算

2026-11-17，Astra-larger-parallel-16f63c8b-20261117。

**参考函数的解析定义与数值必要条件；不是新的非线性曲面。** 这条设计从已接受的完整 Frenet `.995` 场出发，在原标量区间外重新定义 g。它允许 a′ 过零并转为负，末端达到可以向内接平盘的参考二阶 jet。完整 Frenet 方程不除以 a′，适合尝试这一方向；原正投影 r 图上的尾求解器不能直接跨过回头点。既有球面方向的尝试见 2026-11-14 sphere notes，本条的新内容是实际 `.995` 父、显式可退平的新曲率函数及固定材料对应的长度数值。

## 1. 一次固定的新参考函数

完整父数据 `parallel-continue0995-m112.json.gz` SHA：

```text
d6441e642b0bb0903915d42e0d4dd9fd564a2e0378e32070110fe6cc7922403f
```

父原 g、M112/N2048 全解及实际 C² 读出见[扩域记录](2026-11-17-parallel-numerical-0995-continuation.md)。令切口 s_c=.995，原真实标量值为 a_c、v_c、u_c，设

\[
\alpha_0=\arcsin v_c,\qquad \kappa_0=-u_c/\cos\alpha_0.
\]

新参考子午线由

\[
a'=\sin\alpha,\quad z'=\cos\alpha,\quad \alpha'=-\kappa(s)
\]

定义。用 S(u)=10u³−15u⁴+6u⁵，其原函数 J(u)=5u⁴/2−3u⁵+u⁶。起始宽度 δ_in=.02 的 ramp 为 κ=κ₀+(κ₁−κ₀)S；中段 κ=κ₁；终端宽度 δ_out=.02 的 ramp 为 κ=κ₁(1−S)。中段长度准确选为

\[
L_{mid}=\frac{\alpha_0+\pi/2-\delta_{in}(\kappa_0+\kappa_1)/2-\delta_{out}\kappa_1/2}{\kappa_1}.
\]

因此末端 α=−π/2、κ=0，参考 jets 为 a′=−1、a″=0、z′=z″=0。圆内侧可用同一高度的 Cartesian 平盘继续参考面；这只说明参考组件的接缝，未证明实际非轴场也到达它。切口处 κ₀ 的公式使 a,a′,a″ 与原标量相接；参考曲线由精确积分定义，32点 Gauss 只是两个短 ramp 的数值评价。端点使用同一保存的位置值，避免浮点相消造成伪接缝。

选择 κ₁=1.5 后，此 g 一次固定。后续改变 κ₁ 是另一设计，不能计作同 g 精化。

## 2. 用同一实际切口和固定材料对应检查长度

本条没有把外圆点自由配给最近的内端点。原 core 的系数 c_m 给定材料角

\[
\Theta(\phi)=\phi+\sum_{m=1}^{112}\frac{1-4m^2}{2m}c_m\sin(2m\phi).
\]

读取完整真实 `.995` Frenet 状态，并先把局部 polar frame 转回 Cartesian，得到 F_c(φ)=(X_c,z_c)。固定末点为 (R e_{Θ(φ)},H)，本次 H=1.8。按 [R633](../results/R633-finite-cuff-length-budget-and-actual-endpoint-obstruction.md) 检查

\[
|R e_{\Theta(\phi)}-X_c(\phi)|^2+(H-z_c(\phi))^2\le L^2,
\qquad L=s_{end}-s_c.
\]

在2048个角样本上，四个分别定义的新 g 的读数如下。两侧均用同一父场，不以弱初圈替代。

| κ₁ | s_end | R | L | 最大完整弦长，H=1.8 | L减最大弦长 |
|---:|---:|---:|---:|---:|---:|
| 1.25 | 2.5386599761 | .4059057735 | 1.5436599761 | 1.3141528981 | .2295070780 |
| **1.5** | **2.2847166467** | **.5318789142** | **1.2897166467** | **1.2170874598** | **.0726291869** |
| 1.75 | 2.1033285543 | .6218592500 | 1.1083285543 | 1.1511895044 | −.0428609500 |
| 2 | 1.9672874851 | .6893440831 | .9722874851 | 1.1040000247 | −.1317125396 |

κ₁=1.5 的采样必要高度区间为 [.0825513306,1.9060102390]；参考高度增量为 .8944982774511034。H=1.8 是目标平面高度，不是已解出的实际末高，也不强制等于切口物理角均值加参考高度增量。32→48点 ramp 求积的上述累计位移在本次双精度中相同，不代表区间认证。

## 3. 平盘的尺度与尚未支付的几何

只对位于 z=±1.8、半径 R=.5318789142041555 的两块参考平盘，有

\[
D_{disks}=2\sqrt{R^2+1.8^2}=3.75387542648,
\qquad \operatorname{diam}(\text{单盘})=2R=1.06375782841.
\]

单盘的直径大于 .2D_disks。此内向平盘方案不用再外加 R632 半圆回头盖的高度费用，但这两个数都不是尚不存在的完整闭面的 D 或握持区比例。实际活动体可能更大或靠近圆盘，需重新计算全部点对、曲率、嵌入及 reach。圆盘自身也没有提供打破旋转对称的固定标记；可沿既有 R625/627/629 方法设计标记，尚未在本候选装配。

两个较大 κ₁ 在所选 H=1.8 下连必要长度门都未过，不再沿该固定组合求完整闭合。κ₁=1.5 仅值得进入实际 Frenet 求解；其长度余量不保证局部解延拓、平端退休、非轴高度消失、同 g 全 t 族或 README 完成标准。

## 4. 冻结源码与复现

```text
parallel_20261117_inward_profile.py
1816ba9f5c9d1c207ba5e502ed5fa37a2f28807c54067cde766ae313df40e3e0
parallel_20261117_inward_preflight.py
ae39332bc5175cd627195c02165192cfea153915dad9f379c703165fc706ba39
parallel-inward0995-fixed-material-budget.json
3ad4973a2b1046ef403647e34eb20e9d989a1582d341ef52d7f2debd7cafceaf
```

[source profile](../scripts/parallel_20261117_inward_profile.py) 与 [实际切口检查源](../scripts/parallel_20261117_inward_preflight.py) 依赖已登记的原 Profile、Frenet。实际运行：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python \
 topics/visible-flex-larger-amplitude/scripts/parallel_20261117_inward_preflight.py \
 --input /workspace/scratch/16f63c8bce6b/parallel-continue0995-m112.json.gz \
 --angles 2048 --height 1.8 --ramp .02 --curvatures 1.25 1.5 1.75 2 \
 --out /workspace/scratch/16f63c8bce6b/parallel-inward0995-fixed-material-budget.json
```

所有 raw 留在 scratch。非线性入口另记实际终态，不能用本条参考预检预填成功。

## 5. 新 g 的第一次完整实际延拓：s=.997

用[新g入口](../scripts/parallel_20261117_continue_inward.py)调用原完整 Frenet BVP，只替换标量评价函数，所有338个方程、解析Jac、229个浅端行和109个深端行均保留。深端行由真实 `.995` 场计算，目标为该场的二阶位置外推。这是显式有限边界设计，不是整个内向尾的非线性 DN。

新 g 从 `.995` 到 `.997`，duration=.002、step=.00025、M112/N2048、K3、tol=1e−8、max_nodes=1800，100.264572240秒后510节点、两轮网格，BVP真接受：RMS9.32556475754e−9、边界8.67362e−19。

随后[新g实际quintic读者](../scripts/parallel_20261117_prefix_inward_readout.py)绑定输出中 mandatory 的 `inward_scalar_profile` 与源SHA。旧原 Profile 只描述其未改前缀，不能直接拿来读整个新场。与原读者相同，从共同节点F/Fs/Fss的唯一五次式计算实际0/1/2jet；N2048、每胞元4细分、509胞元，共5,212,160点。

| 新 g 同一接受场的实际读数 | 值 |
|---|---:|
| 最大相对 Gram 算子误差 | **2.753578662839614e−6** |
| 最坏位置 | s=.997，φ=2.705942109830271 |
| 最大主曲率采样 | 6.301720635756675 |
| core gap | .9600010353771838 |
| 对既有点见证的最小距离 | .960001035377184 |
| core rho最小采样 | .16601063267919747 |
| 镜像开前缀D代理 | 3.5090195830980546 |

虽然离散BVP接受，实际Gram已超过1e−6，不能据此宣称几何目标通过。区间末a′=.34384039496，尚未回头，前述终端参考盘还远未到达。D代理和gap仍不代表闭面比例；正在以同一新g、同一原`.995`边界参照提高角阶，处理这个具体误差，不沿失败或未接受状态计闭合。

```text
parallel_20261117_continue_inward.py
86fd79df32938a5437bece1b1f7807e53976de4cfd8edf6e99ef1cca9bd88bfb
parallel_20261117_prefix_inward_readout.py
75218531458ed3c5a91c215b8d57282fe9f547bb598adaee59da647855a5d76a
parallel-inward0997-m112.json.gz
11960350cb15cc43334d039e161184a8f7b7caa0650311c96ae8b33eac69e327
parallel-inward0997-m112-readout.json
1dd74000ac836ebcd3302dcbce1a71b00be6611ca55fe35a1c00007d34f6c474
```

实际调用：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
 topics/visible-flex-larger-amplitude/scripts/parallel_20261117_continue_inward.py \
 --input /workspace/scratch/16f63c8bce6b/parallel-continue0995-m112.json.gz \
 --duration .002 --step .00025 --modes 112 --angles 2048 --fixed-modes 3 \
 --curvature 1.5 --ramp .02 --tol 1e-8 --max-nodes 1800 \
 --out /workspace/scratch/16f63c8bce6b/parallel-inward0997-m112.json.gz

PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
 topics/visible-flex-larger-amplitude/scripts/parallel_20261117_prefix_inward_readout.py \
 --input /workspace/scratch/16f63c8bce6b/parallel-inward0997-m112.json.gz \
 --angles 2048 --radial-subdivisions 4 \
 --out /workspace/scratch/16f63c8bce6b/parallel-inward0997-m112-readout.json
```

wrapper补入新g身份后最终raw的SHA如上；旧完整solver在补身份前打印的中间gzip SHA不冒最终文件SHA。所有源明确冻结，后续同g使用该参数与来源定义。
