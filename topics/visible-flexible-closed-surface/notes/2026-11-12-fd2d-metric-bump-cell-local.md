# 保存网格上的局部 Gauss 两点查询

## 1. 对象与接口

`scripts/fd2d_gc_bump_cell_probe.py` 直接消费已经闭存的
`RawBumpSeedNativeField`。其 `select_cells` 与 `probe_cell` 不调用
BVP provider 的网格工厂：实际 P1 网格、节点修正、独立的 `l`、全部参数、
物理 bump 支撑和显式 seed weight，均由输入 NPZ 和原生 reader 决定。

```python
from fd2d_gc_bump_seed_native_field import RawBumpSeedNativeField
from fd2d_gc_bump_cell_probe import select_cells, probe_cell

field = RawBumpSeedNativeField(actual_npz, actual_candidate)
cells, requests = select_cells(field,
    segment_labels=['early_shallow_return'])
for cell in cells:
    sample = probe_cell(field, int(cell), angles=256, endpoints=True)
    mean = sample['gauss2_mean']  # (angles, 3)，顺序 G, Rn, Rm
```

调用者可以使用 `cells=[...]`、`intervals=[(left,right),...]`、
`segment_labels=[...]` 的并集。物理区间选取与其内部有正长度交叠的整个
保存单元；仅接触区间端点的相邻单元不会被加入。查询不裁剪或细分 P1 单元。
物理段名来自输入目标的真实 base profile，因而从 99 节点改为 122 节点后
仍可定位同一短回转段。

命令行入口是 `scripts/fd2d-metric-bump-cell-local.py`：

```bash
python3 scripts/fd2d-metric-bump-cell-local.py \
  --field notes/ACTUAL_FIELD.npz \
  --candidate notes/ACTUAL_CANDIDATE.json \
  --out-prefix notes/FRESH_OUTPUT_STEM \
  --segment early_shallow_return \
  --segment redeepen_after_partial_return \
  --angles 256 --endpoints
```

也可使用可重复的 `--cell ID`、`--interval LEFT RIGHT`；全域查询必须明确
加 `--all-cells`。每个单元独立消费并立即写进度，不积存全域大数组。
函数返回完整点值数组，命令行报告保存各单元点值极值、完整 Gauss 均值、
保留部分和遗漏部分，及峰值的物理和计算坐标。输入本身仍能由定义和源文件
准确重算全部有限点值。

## 2. 实际导数与平均的含义

设保存单元为 `[s_i,s_{i+1}]`，长度为 `h`。其 P1 修正的一阶导数使用
该单元的准确差商，而 seed、tail lifting、物理目标和计算角变换的导数
使用原生 reader 的实际函数。两个查询位置为

\[
 s_\pm=s_i+h\left(\frac12\pm\frac1{2\sqrt3}\right).
\]

当请求端点时，左端使用右单侧差商，右端使用左单侧差商；两者都属于本单元。
接口核对 `J=1`，适用于明确声明 `physical_bumps` 的物理坐标 `x=s`。
材料角是 `u=U(s,\xi)`，完整残差为

\[
\begin{aligned}
 G&=ln-m^2+a_{ss}/a,\\
 R_n&=n_s-m_u/a-(a_s/a)(l-n),\\
 R_m&=m_s-l_u/a+2(a_s/a)m,\\
 n_s&=n_x-(U_x/U_\xi)n_\xi,
 \qquad m_s=m_x-(U_x/U_\xi)m_\xi.
\end{aligned}
\]

这些量由 `fd2d_gc_three_field_residual.py` 统一求值。没有以方程 RHS
替换插值场的真导数，也没有通过 `n` 消元独立的 `l`。

输出 `gauss2_mean` 为

\[
 \frac12\big(R(s_-,\xi)+R(s_+,\xi)\big).
\]

它保持计算角 `\xi` 固定，所对应的两个材料角通常不同。这是两个有限点的
算术平均；乘 `h` 得到报告中的有限求积值。它本身没有给出真实单元积分的
余项界，也没有给出固定材料角的 primitive。全径向、全角的后验仍须另外
消费实际场及相应连续余项。

在均匀 `\xi_j=2\pi j/N` 上，用实际保留的 `cos(2k\xi)`、
`sin(2k\xi)` 基作离散投影：`G,Rn` 使用带均值的余弦基，`Rm` 使用正弦基。
完整采样残差始终保存；遗漏部分逐点定义为完整值减投影值。所有均值也分别
输出完整、保留和遗漏部分。此离散分解没有声称无限 Fourier 展开已经收敛。

## 3. 真实 122 节点接口运行

输入为已闭存的
`notes/2026-11-12-fd2d-raw-bump-turnmesh01-warm.npz`，SHA256
`6edb4f22059f365c6351a32ea86fcc1f5b7c3460902dc1ca075c67432c7fb122`。
它声明 `targeted_turn_mesh_exact_central_cylinder_v1`，保存 122 个真实节点，
目标 candidate SHA256 为
`7c3f31de4b230e8d98b99c3e3914d65ae69daa3cb5c54ae22f585a36a888bfd1`。

实际命令：

```bash
python3 scripts/fd2d-metric-bump-cell-local.py \
  --field notes/2026-11-12-fd2d-raw-bump-turnmesh01-warm.npz \
  --candidate notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json \
  --out-prefix notes/2026-11-12-fd2d-metric-bump-turnmesh-cell-local-smoke-01 \
  --interval 1.001 1.002 --angles 128 --endpoints
```

会话 `47541`、完成块 `3753e7` 实际返回 0，耗时 1.584 秒，进程最大 RSS
69,380 KiB。物理区间选择唯一的保存 cell 86，端点为
`1.000419888139713` 和 `1.0031442329625426`。网格、源文件和输入场字节均未改动。

该 warm 场仍有显著有限残差：所查询四个径向点的采样最大值分别为
`G=3.2153506727`、`Rn=.5063660357`、`Rm=.4058782471`；两 Gauss 点均值
采样最大值分别为 `3.2024752894`、`.2514677489`、`.1894433613`。
这次运行完成的是新保存网格的局部查询路径，没有求解或认证该 warm 场。

闭存产物包含 source、实际 field definition、报告、逐格进度和真实退出记录，
统一身份见同前缀的 `cell-local-closed-manifest-01.json`。
