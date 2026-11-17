# q=.22 small-cut 原端口：固定度量 M32 精化完成

会话 `literature_mechanisms`。这是原 `r=.30, curvature=4, peak_fraction=.2` small-cut 分支的精化，使用原 tail port；与新 `hybrid_outer_cell_v1 / beta8` 物理尾端口分开。此前 q21/q22 几何交接快照保持不变，本补遗将其中 q22 fixed 的 pending 状态更新为 completed。

## 已完成结果

固定 profile 的 `delta=.17141686211304713`，与 q22 M28 设计种子字面相同。数值求解只把物理支持主幅度由 `.22` 调整为 `.22000090750374524`；目标旋转度量保持该冻结 profile。

|量|M28 设计种子|M32 固定度量精化|
|---|---:|---:|
|实际 q|.22|.22000090750374524|
|delta|.17141686211304713|.17141686211304713|
|采样 metric_l1|1.13275037e-6|1.1188476139153463e-8|
|采样主曲率最大值|7.18514343|7.189775178903014|
|前缀高度|1.272213830|1.2722136378107283|
|Frenet 根最小采样值|.0004227642869|.0004227469739011003|
|末端第一高度模绝对值|.002693297377|.002693308738200825|

M32 求解 `solver_success=true`，最终 1675 个节点，审计 3457 个径向点、2048 个角点；计时约 2241 秒。`flow_defect=3.768593651399721e-8`，`darboux_l1=1.350852663073902e-5`，实际末端线性 BC 残差最大值 `1.8403654251583636e-18`。

这是已完成的固定同一目标 g 数值精化；采样度量残差尚未给出严格连续等距性，线性有限 DN 尚未支付真实非线性尾、均值和 Cartesian 二 jet 接合，故不是闭合候选。q20 的显式 C² 连续区间几何证书也不能自动移用到这个 q22 对象。

## 恢复与运行

依赖已有 `recover_prefix.py` 的完整 source 恢复闭包，使用 `smallcut_highq_work/recovered` 作为恢复根。精化命令为：

```sh
python -u fixed_refine_smallcut.py \
  --recovery smallcut_highq_work/recovered \
  --checkpoint smallcut_highq_work/secant-r30-p20/q220-m28.json.gz \
  --port smallcut_highq_work/config/port30-m32.json \
  --output smallcut_highq_work/fixed-r30-p20-q22-m32 \
  --modes 32 --tol 2e-8 --nodes 701 --max-nodes 7000
```

当前临时 checkpoint 是 `fixed-r30-p20-q22-m32/fixed.json.gz`，SHA256：

`94235c5031911d77272f3cd501391ace81d4f922b0a583f142eec0a822162e31`。

该目录的 `refinement_manifest.json` 保存实际命令、source 和依赖信息；`fixed-H.json` 导出实际 upper-prefix z 的完整 32 个高度 Fourier 模及 Hs/Hr。orientation=+1 的真实尾若在自身正斜率背景解，需要输入 -H、匹配 -Hr，再反射整个尾的 z 和均值。这里不改变该符号约定。

checkpoint、系数与 endpoint 数组为可重算临时数据，只供当前真实接尾任务读取，不作为持久仓库 artifact。

512 角完整实际 Cartesian endpoint 已另行导出为 `fixed-r30-p20-q22-m32/endpoint.npz`，包括 X、Xs、Xss、Xtheta、Xthetatheta、Xs theta 及非线性均值。数组 SHA256 为 `21c5b22d5fb2f3877d0cff40adbd2b4b3876da2fe304e30be455afd809ed3f12`。末端 mean z、mean zs、mean zss 分别为 `1.2696422293870728,.0827912437638402,1.7299931823766053`；末端采样 E/F/G 归一化误差分别为 `1.52645e-11,4.95539e-12,5.33068e-10`。这些是接口恢复值，不是圆领条件。

## q22 有限 core 的二阶矩：直接有理数证书

q22 的次级支持系数范数已经约为 `.00473597,.02092794,.09973465`，超出此前 R7 使用的 q<=.21、`.004,.018,.08` 统一误差假设。因此不能套用该统一估计。可以直接对当前有限 core 作精确 Fourier 积分。

令 `h(phi)=sum h_k exp(i k phi)`，`h_0=1`，对正偶频 m 取 `h_m=h_-m=c_m/2`，c_m 是存储 binary64 常数。core 的复二阶矩为

`AC = integral_C (x+i y)^2 dA = (pi/2) S`，

`S = sum_(k1+k2+k3+k4=-2) (1-k1)(1-k2)(1-k4²) h_k1 h_k2 h_k3 h_k4`。

这是 `gamma=(h+i h') exp(i phi)` 与平面通量公式的有限 Fourier 系数恒等式。所有 c_m 都是精确有理数，因此 S 可只用整数和有理数卷积计算。`finite_core_moment_exact.py` 先以有理三角界验证 `rho=1+sum (1-m²)c_m cos(m phi)>0`，再分别卷积两对多项式，保留目标 -2 系数，最后用 pi>3 给出严格有理下界。当前结果为

`Re AC > .580914626611`。

该下界属于显式有限 core，不声称其已经位于一条严格同 g 闭族。它支付条件标记帽论证中需要的 core 矩非零性，并避免错误延伸 q<=.21 的统一估计。完整分子、分母和输入/source 哈希在小型标量文件 `core-moment-exact.json` 中。

运行命令：

```sh
python finite_core_moment_exact.py \
  smallcut_highq_work/fixed-r30-p20-q22-m32/fixed-summary.json \
  --out smallcut_highq_work/fixed-r30-p20-q22-m32/core-moment-exact.json
```
