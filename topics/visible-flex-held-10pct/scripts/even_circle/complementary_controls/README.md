# C4 补弧控制：最小 provider、保守界与审计

这组文件替换精确圆弧核心的控制函数，保持原积分定义、材料弧长和参数 Jacobian。
没有运行新的前缀 BVP，也不提供新的闭曲面或完成证书。
主会话的独立 driver 使用这里冻结的三份核心文件；后续运行应另外登记物理参数和终态。

## 直接接口

```python
from plateau_core import PlateauSupportCore
from uniform_complement_core import make_core_class

Core = make_core_class(PlateauSupportCore)
core = Core(
    q=0.005,
    corrections=[0.0] * 5,       # M=6，五个高矩控制
    base_mode=4,
    halfwidth=0.145,
    transition=0.08,            # 原 primary 圆化过渡
    control_transition=0.08,    # 补弧控制自己的过渡
    homotopy=0.0,
    lock_fundamental=False,
    arc_nodes=512,
)
```

`make_core_class` 必须接收原始 `PlateauSupportCore`，不要传旧 `HomotopyPlateauCore`。
`_basis` 返回原接口 `(f,b,b',b'')`，其中 `b=f'`。
`rho_material_jets` 用新函数的真实导数计算 (\rho_\phi=b'+b'''\)、(\rho_{\phi\phi}=b''+b''''\) 的控制部分。
原 `normal_geometry`、`unit_geometry`、`arc`、`evaluate` 和固定材料参数 `parameter_derivatives` 均原样继承。

旧控制向量不能直接搬入新坐标。新控制向量的每个分量是相应高支持 Fourier 系数的单位坐标；
主频默认没有额外锁住，因而会具有固定的主频泄漏。
本题的 (q) 仍为圆弧半径参数，在圆化终点 (R=1-(n^2-1)q\)，并不是完整核心的主频支持 Fourier 系数。
每个新控制过渡宽度均需新鲜 (\lambda=0\) 初始化，或精确转换完整已表示低矩后重新求解。

构造后的 `ComplementaryMomentBasis` 只读：`support_jets`、`primitive`、`primitive_jets`、`homotopy_rho_bounds`、`summary` 都不改变持久状态。
可在独立 adapter 中缓存固定
`(base_mode,modes,halfwidth,transition,center,precision,quadrature_order,lock_fundamental)` 的对象，
但调用方不得就地修改公开数组。每个核心自己的 `_basis` 数组缓存仍属于该核心实例。
本包不包含主会话另行添加的构造缓存 adapter。

## 精确定义与保守界

令 (T=2\pi/n\)，补弧截断函数在 (|\phi|\le a\) 为零，在 (|\phi|\ge a+\epsilon\) 为一；中间使用

\[
 S(t)=126t^5-420t^6+540t^7-315t^8+70t^9.
\]

其端点前四阶导数均为零，因此控制支持函数 (b) 为 (C^4\)，原函数 (f) 为 (C^5\)。
以加权余弦 Gram 矩阵定义系数，均值恒为零；可选再把主频锁为零。
对高支持矩作可逆线性预处理，使模式 (2n,\ldots,Mn\) 的支持矩为单位阵。
未锁主频时的主频泄漏也保留在 (\lambda=0\) 投影中，所以整个控制同伦的全部已表示低矩严格不变。

在 (\lambda=1\) 的保护圆弧上 (b,f\) 及所需导数为零，圆弧的位置、圆心和半径不会被补弧控制改动。
均值为零使 (f) 周期，故原周长 (2\pi\) 保持。
这些是精确定义的性质；实现用 80 位计算系数后作 float64 函数求值，并不把有限 Fourier 多项式叫作精确圆弧。

`moment_interval_bounds.py` 独立使用有理数区间给出同一系数的包含界：

- Machin 公式与交错级数包围 (\pi\)。
- Taylor 余项包围加权余弦矩；(S'=630t^4(1-t)^4\) 的所有需要的矩均为有理数。
- 任意高精度逆矩阵候选转成有理矩阵后，以精确 (\|I-RG\|_\infty<1\) 验证逆界。
- 对截断多项式导数的 Bernstein 系数作 64 等分有理上界，再用三角不等式给出真实函数导数界。

最新窗口 (a=.145,\epsilon=.08,M=6\)、不锁主频时，Neumann 残差上界约 (8.14\times10^{-60}\)。
系数证书只认证系数和导数界，没有认证空间曲面。

核心正性先用真实函数的三角界，再用实际采样值减去导数 Lipschitz 余量。
保留原门槛 (10^{-5}\) 和默认最多 32768 点；若上界过粗导致不能认证，明确报错，不能仅凭采样为正接受。
除有理系数误差外还加了数值求值余量；这个浮点余量不是 libm 的区间定理。
因此本包的几何采样输出仍标为诊断。

## 比较结果及限制

下表固定 (a=.145\)、控制过渡 .08、不额外锁主频，范数在每周期 16384 点采样。
旧基结果由第一批已经发布的 80 位矩积分脚本重生。

| M | 旧原始支持矩条件数 | 新原始支持矩条件数 | 旧 canonical (\max\|\Delta\rho\|_\infty\) | 新同项 | 旧 canonical (\max\|\Delta\rho'\|_\infty\) | 新同项 |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 59.62 | 2.46 | 2477 | 2594 | 59122 | 274434 |
| 6 | 1042.20 | 5.72 | 21257 | 7763 | 683644 | 757099 |
| 8 | 11635.96 | 28.66 | 142438 | 25798 | 5949816 | 2589817 |

条件数是所列原始矩问题的坐标量，不是几何不变量。canonical 函数范数比较更直接反映控制的几何放大。
新基并非每个 (M\)、每种范数都改进：例如 (M=4\) 的导数峰值更大，(M=6\) 的导数峰值略大。
锁主频会付出额外代价；它不是本题保持圆弧所必需的限制，默认关闭。
较宽保护弧 (a=.28\) 仍明显病态，不能仅靠更换基消除这一点。

对旧窄窗 (q=.005,\lambda=.4,M=6\) 已完成解的一组实际控制，只匹配模式 (8,\ldots,24\) 的支持矩后：

| 控制选择 | 整体同伦未表示的 (\rho\) 余项采样最大值 | 新补弧控制 (\rho'\) 最大值 | 新原始支持矩条件数 |
|---|---:|---:|---:|
| 旧 compact 控制 | .230184 | 此表未重算 | 1042.20 |
| 新控制，过渡 .08 | .108445 | 27.3865 | 5.72 |
| 新控制，过渡 .12 | .0717463 | 12.3865 | 8.78 |
| 新控制，过渡 .16 | .0629872 | 7.90438 | 13.72 |

这里包含 primary 圆化带来的同伦余项，未把它从真实余项中删掉。
三组新函数的主频支持系数分别比旧值改变约 (5.53\times10^{-6}\)、(4.43\times10^{-6}\)、(3.65\times10^{-6}\)。
所以这些替换并没有解原 BVP；它们只是固定一组高矩下的控制形状比较。
过渡 .16 值得作为下一独立 BVP 比较，但不能代替正在运行的 .08 的真实终态。

## Jacobian 与函数接口审计

`audit_uniform_core.py` 检查 (\lambda=0,.4,1\) 的固定材料参数 Jacobian、曲率半径材料二 jet、基函数导数、
原函数求积，以及 (q=.06\) 的保护圆弧。
保护圆弧 65 点上 (b\) 的零至四阶导数及 (f\) 都精确返回零；与零控制核心的位置和材料弧长差均为零。
周期弧长误差约 (8.9\times10^{-16}\)，64→96 点 Gauss 原函数差约 (6.9\times10^{-17}\)。
这些是数值接口检查，精确圆弧和周期性来自上文定义。

最尖锐的第 5 个控制在 (\lambda=1\) 下，物理系数步长由

\[
 6.25\cdot10^{-7}\to3.125\cdot10^{-7}\to1.5625\cdot10^{-7}\to7.8125\cdot10^{-8}
\]

减小时，固定材料位置参数导数误差依次为

\[
 2.713\cdot10^{-6},\quad6.784\cdot10^{-7},\quad1.693\cdot10^{-7},\quad4.277\cdot10^{-8}.
\]

约四倍下降与中心差分的二阶截断误差一致；末项相对误差约 (2.20\times10^{-8}\)。
在 (\lambda=0,.4\) 最后进入约 (10^{-9}\) 的浮点噪声区。
审计使用原弧长逆之后的五次 Newton 修正来减少有限差分中求逆容差的干扰。

## 再生与源闭包

Python 依赖只有 `numpy` 和 `mpmath`。三个历史源文件从明确提交
`bf5e9f92c3befea1cc5173c33bf9130ccc3b320d` 定点恢复，并逐项核对 SHA-256。
不恢复或提交旧前缀网格、系数数组、端口数组或大 checkpoint。
实际方向诊断只需要 `actual_direction_input.json` 中五个控制参数及其来源 hash。

在本目录执行：

```bash
OPENBLAS_NUM_THREADS=1 python regenerate_all.py \
  --repo /path/to/math-research-public \
  --scratch /path/to/runtime-audit
```

这个入口先在空参考目录恢复源，再实际运行旧矩比较、新 core API、小步 Jacobian 和 24 组控制比较。
所有再生输出和日志写到指定 scratch。`completed.json` 保存命令、源恢复结果和输出 hashes。
运行时间、路径和浮点环境会改变整份 JSON 的 hash；比较标量应按合理数值容差。

`R20-exact-circle-primary-distance.md` 与 `verify_circle_primary_bound.py` 独立于以上数值实验。
其必要条件应与 `linear_circle_compatibility.md` 中的未验证谱信息、路线建议分开引用。
