# 原真 .995 切口后的向内参考度量与固定材料弦长预算

2026-11-17，Astra-larger-parallel-16f63c8b-20261117。

**参考函数的解析定义与数值必要条件；不是新的非线性曲面。** 这条设计从已接受的完整 Frenet `.995` 场出发，在原标量区间外重新定义 g。它允许 a′ 过零并转为负，末端达到可以向内接平盘的参考二阶 jet。完整 Frenet 方程不除以 a′，适合尝试这一方向；原正投影 r 图上的尾求解器不能直接跨过回头点。既有球面方向的尝试见 2026-11-14 sphere notes，本条的新内容是实际 `.995` 父、显式可退平的新曲率函数及固定材料对应的长度数值。

**坐标和精化约定。** 本note后文“同g”比较沿用[R240](../results/R240-canonical-material-metric-and-refinement.md)的共同材料规范：固定a(s)、区间及core常数项1，并在rho>0时用各自Theta(φ)拉回到ds²+a²dTheta²。计算φ下的rho由高阶未知core决定，并非逐点相同；相对Gram算子范数的连续上确界在这种变换下不变，但离散角样本不自动是同一材料网格。此处只报告真实求解及各自实际Gram，尚未支付R240要求的共同材料六jet收敛，也不把固定标量或更换有限BC当作README完整固定g精化完成。

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

## 6. 同 g M128 真解没有降低实际误差

以 M112 的新g `.997` 真接受场为暖父，duration=0、M128/N2048、K3、tol=1e−8、max_nodes=2000；`--boundary-input` 仍指定原`.995`真场，因此在新增角阶下重建同一实际父参照的主部边界，而不是从新暖父换一套参照。其余参数固定。M128完整386维，浅端261行、深端125行，未删任何行。66.548235365秒后510节点真接受，RMS9.32575229561e−9、边界3.46945e−18。

同一quintic读者 N2048/4细分给最大实际Gram **5.87897809846e−6**，最坏在s=.997、φ6.14819499785；κ最大6.30172524765，core gap .960001022623。比M112的2.754e−6更差，没有达到固定精化目标。未将两个字段平均、滤波或选择局部较好角点当作接受。

```text
parallel-inward0997-m128.json.gz
ca3871a8777d25df51372d7c0f7eb32945bfaed21ed379787cfe278d6426c8ec
parallel-inward0997-m128-readout.json
cb17ad8d11c8540b1e5bce13c658d374621a379f33f251c1b593ca2f1b7efc81
```

复现使用第5节同一入口，输入改为 M112 `.997`、`--duration 0 --modes 128 --boundary-input /workspace/scratch/16f63c8bce6b/parallel-continue0995-m112.json.gz --max-nodes 2000`，输出为上述M128路径；其余CLI固定。读者只改输入/输出路径。

### 6.1 截断投影与角求积的分离诊断

新增[真实节点投影读者](../scripts/parallel_20261117_prefix_projection_probe.py)保持接受场状态和保存的导数不动，在8192角点评价原Frenet的未投影速度 V，再与保存导数的三角表达 V_M 比较。未投影V的单位速度和对F_phi正交误差均约1e−15；这不修复已经积累的角向度量误差。设delta=V_M−V，则径向Gram误差为2 V·delta+|delta|²，混合误差为F_phi·delta；角向误差的局部增长缺陷为2 F_phi·(delta)_phi，均用真实移动frame连接项。

| 真实端点 | max|delta| | 将求积角数2048→8192后的速度差 | 相对角度量增长缺陷最大采样 |
|---|---:|---:|---:|
| 原g .995 M112 | 5.22427134e−5 | 1.59658e−12 | .0003287677 |
| 新g .997 M112 | .000411346898 | 1.35745e−8 | .0023599793 |
| 新g .997 M128 | .000414786811 | 1.38530e−8 | .0025767006 |

增求积角数只做同字段的评价/投影比较，不是重新求解高N BVP。两新场的有限角阶截尾在端点没有下降，其量级远大于本次N变化造成的低阶系数差；不能把当前问题仅归于角点求积不足。8192点的端点实际Gram读数分别约4.247e−7、2.859e−6、6.036e−6，略高于2048点采样；仍是样本而非连续上确界。

终端主部条件是否激励了有限谱端，是后续需检验的解释，不由这张局部表直接证明。也不能把delta的大小等同于累积的全部角Gram误差。继续检查实际误差沿径向的分布，并用更长的同g真场区分人工端部效应；不把辅助buffer或任何局部crop冒成闭尾。

```text
parallel_20261117_prefix_projection_probe.py source SHA
4d968fa0bbe2ea4975bbf244ae17e30c0c8317c6fb1d629cac33b70ae1f173c7
parallel-inward0997-projection-probe.json
e8f5667f5f6adac1b6e69ed21cc8d1ac6330f94e3c2063134a4ad9c1169c6f22
```

从仓库根目录，调用该源 `--inputs` 后依次给原`.995 M112`、新g`.997 M112`、新g`.997 M128`的完整scratch路径，`--angles 8192 --out /workspace/scratch/16f63c8bce6b/parallel-inward0997-projection-probe.json`。全部输入SHA在本note和输出中；原始字段与报告不入库。

## 7. 更长buffer的初始域失败

尝试以本新g `.997 M112` 真BVP场延伸到`.999`：duration=.002、step=.00025、同K3/M112/N2048、tol=1e−8、max_nodes=2000。518节点初猜进入 `invalid_current_iterate`，2.965620416秒返回status2、RMS NaN、jac计数0，未接受。

后端通用消息称 singular Jacobian，但本次尚未计算Jac，实际可确认的原因是初始残差含非有限值。不能把该消息解释成已证明某个实际Jac矩阵奇异，也不能拿初猜的巨大曲率/Gram作新几何数据。这个未接受状态不作父；仍从`.997`真父缩到duration=.001重新试。更长buffer在尚未真接受前不支付任何内部cut的误差控制。

```text
parallel-inward0999-m112.json.gz
c322970b4261896e1694b5d570f4179eb8be7a79569e6ee39f25d3ac70e6d77c
```

调用第5节同一冻结入口，只把输入设为新g `.997 M112`、duration=.002、max_nodes=2000、输出设为本`.999`路径；不另设curvature/ramp，准确继承新g身份。与第6节相比，这里恢复M112接受父，避免把未过几何门的M128变化冒作更优候选。

### 7.1 缩步 .997→.998 也未接受

仍从真`.997 M112`父出发，同一新g与完整原主符号边界，duration=.001、step=.000125、tol1e−8、max_nodes2000。该初猜通过域检查并进入完整QR，581.333128009秒、三轮网格后1202节点；RMS=.0005733200120566961、边界3.46945e−18，下一轮还需959节点（总2161）而超2000，status1，未接受。

```text
parallel-inward0998-m112.json.gz
abd2991424504412cfdca648e21d24e3ffb042acf9625b65938cb87443ae6387
```

这是不同于`.999`初猜域失败的一项完整求解失败。保留参数与最终身份，不从诊断曲率、gap或D提取新的几何结论。两次buffer都尚无接受场，未支付内部截口的误差改善；继续使用原`.997`接受态，对移动法切框架Schur行和遗漏速度谱两种明确新有限边界作真实比较。改边界属于设计另一有限问题，不能计作原边界的精化。
