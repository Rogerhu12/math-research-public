# 冻结几何的有界精确键缓存：22 只读定位与 24 接口

## 1. 范围与实际证据

本项先只读 22 的已有 progress 及 R152／R149／R139 求值源码，随后按
root 与 numerical 的明确分工实现另名薄缓存。numerical 独占 23 的
current residual/data 包复用及 24 driver；geometry 独占四个纯角
operator 投影缓存。本模块不改上述活动源、物理场、目标方程、求积规则、
normal 系统或原数学定义。

只读记录为
`notes/2026-11-12-fd2d-metric-frozen-cache-path-audit22-01.json`，
SHA256 `936f07a0d61346736671612e6f10f00e05db6dce9252342cb544307216107945`。
它绑定 22 b1 progress **直到首个 iteration 0 accepted 事件的前缀**
字节长度及 SHA；不把该前缀当后来链的最终状态。另保存已读源码身份、
原节点数组身份、各 cell-block 时间差和工作集下界。读取没有调用
profile、field、BVP 或任何 Jacobian。

已有阶段事件给出的直接量为：

| 事件区间 | 时间差 |
|---|---:|
| 已记录 node 0 完成到 node 128 完成 | `11.418340792999516 s` |
| node 128 完成到最后 cell-chunk 完成 | `96.04711044899886 s` |
| 覆盖 coast cell 63–74 的七个两格 chunk，即 cell 62–75 | `28.474559447997308 s` |
| 最后 cell-chunk 到附加 interior 行及 assembled 事件 | `1.447755919998599 s` |
| direction 自报时间 | `6.997336125001311 s` |

coast 七块事件间耗时的中位数为 `3.5362090279995755 s`；其余 57 块
为 `0.8937299659992277 s`。这些是完整阶段事件之差，包含该阶段的
所有运算和日志开销，不是函数级排他计时。没有据此将 `28.47 s` 归因于
某一个缓存 miss，也没有进行新的整跑性能 profile。

## 2. 已存在的缓存与真正缺口

原 `fd2d_gc_gauss_cell_codazzi_chunked.py::_chunks` 保存同 mesh／chunk
的 view；`fd2d_gc_gauss_cell_codazzi.py::_view` 保存同 mesh／order
的 G2 points 和 view；R149 `FrozenRulingAtlas.label_data` 已保存最近
8 个实际 label 列。并非所有几何工作都没有缓存。

真正可确认的重复路径是：

1. R152 `known_pde_average` 对每个 coarse／fine 点批重新调用
   `point_view`，后者重新做 `chart.coordinates(points)`。
   `known_lifting_correction` 虽保存最近完整参数的差值，但新参数会使
   这一动态缓存失效；其临时点批的纯几何数据没有持久保存。
2. `FrozenRulingAtlas.coordinates` 总将实际 `xi` 显式传给原 chart，
   原 `BlendedIntrinsicGC.coordinates` 因而再次调用固定
   `reference.reference_coordinate(xi)`。ruling 的 `label_data`
   缓存不覆盖这个原 seed-coordinate 调用。
3. 原 `DirectLabelCoastReference` 只保存最近 64 个 `(s,label)` 的
   物理参考 jet。这个实际 129-node mesh 的 active coast 有 12 格
   （索引 63–74），仅每格一个不再切片的 G8 规则就有至少 96 个不同
   径向点，尚未加 G2、节点及实际 piece 分片点。最小 coast 格宽仍为
   `0.002772524841526458`，不是无二进制内点的极小格。因此 64 点
   容量不能容纳整个 fine 工作集；这只证明容量不足，不量化时间损失。
4. `RawBumpDAE.operators(delta)` 在 delta 变化时还会重做四个纯角
   PE/PO 投影。这些对象属于 geometry 的另名缓存，不在本实现中改写。

原 R152 动态 cache key 包含整个 `p`，而 affine lifting 实际只依赖
tail 和 delta，central 参数由 raw boundary 映射进入。因此仅变 central
时可以避免不必要的动态失效。但完整 PDE average 仍依赖 tail/delta，
不能因 reference 冻结就将它移入本模块的静态缓存。

## 3. 哪些东西真正冻结

当前图为固定物理 `s`，atlas `u=U(s,xi)` 在优化参数间保持不变。
reference 的入口、`a_c,v`、全部 Fourier 数据、材料图、保存精度及
原始求值源码同样冻结。故以下对象可按精确输入重复使用：

| 对象 | 精确键所需信息 | 不依赖的当前参数 |
|---|---|---|
| 全 atlas 坐标和其空间 jets | 冻结 chart binding、实际径向数组、实际 label 列、radial side | central、tail、delta、raw y |
| 独立调用的 ruling chart jets | 同 binding、精确 `s`、实际 label 列 | 同上 |
| 冻结 reference 的物理 `(n,m,l)`、`∂s`、`∂u` | reference binding、精确 `s`、实际 label；并核对实际 material-u 组合 | 同上 |
| 原固定 seed 的材料坐标和两角导 | 原 seed/reference binding、实际 label 列 | 同上 |

以下仍按当前参数计算，**没有缓存进静态层**：

- `a_delta,a_delta',a_delta'',c_delta,K_delta` 及它们的参数导数；
- 当前 tail 在 `a_delta(s) sin U(s,xi)` 上的角函数和参数列；
- 完整 lifting、`F_p L_p`、Codazzi forcing、实际 Jacobian；
- raw P1 correction、R153 的商式和 R155 的正 trace 非线性字段；
- 随 central `c` 变化的真实中央曲线。

特别是固定 reference 只在原 `delta=0` 的 K0 coast 上准确解 GC。
当前 delta 非零时它是固定参照函数，当前 target 的残差和参数链式都
必须保留。本缓存不把其原 GC 恒等式推广到改变后的目标。

例如固定 reference 的 PDE 值仍有

\[
\frac{m_{*,u}}{a_\delta}+c_\delta(l_*-n_*)+U_s n_{*,u},
\]

即使星号项和 `U_s` 都可缓存，`1/a_delta` 和 `c_delta` 仍必须实时
重组。把整个表达式只按 `(s,xi)` 记忆将是错误实现。

## 4. 新接口与对象生命周期

冻结实际源：

`scripts/fd2d_gc_prepared_geometry_cache.py`，`13991` bytes，SHA256
`c2c54ba42ab50200a05c68c85bc0cdba5b25ea07838a302bd61449fc72bbad03`。

```python
from fd2d_gc_prepared_geometry_cache import install_prepared_geometry_cache

# 只在新建的 24 problem 上安装，不改正在运行的 22/23。
geometry_cache = install_prepared_geometry_cache(
    problem, byte_limit=16 * 1024 * 1024)
report["prepared_geometry_cache_definition"] = geometry_cache.definition()

# 原消费者与 copy views 继续使用相同 chart/ref API。
# 结束或保存 report 时记录真实计数。
report["prepared_geometry_cache_statistics"] = geometry_cache.statistics()
```

安装仅给该新 problem 的共享 chart、DirectLabel reference 和固定 seed
reference 实例加薄方法；不改类方法、旧源码或 `problem.operators`。
原对象的 `__copy__`／`__deepcopy__` 保持共享语义，因此现有小 view
自然使用同一缓存。重复以同字节预算安装返回同一 handle；若试图用
不同预算或不同 reference 暗中替换既有缓存则拒绝。

原 mathematical field packets 保留原样，新增缓存定义属于运行求值的
来源记录。24 report 应同时记录新 source SHA、`definition()` 和实际
`statistics()`；原 field 的可移植 native reader 不依赖此缓存才可
重建同一函数。

## 5. 精确键、侧迹与容量

静态 binding 包含完整 chart definition、reference binding 和原
evaluation definition，以及 NumPy／longdouble 精度信息。
实际 key 进一步区分：

- 径向数组的 shape 与原 binary64 字节，或单点 `float.hex()`；
- 注册的实际 longdouble label 列，命中逐列用 `array_equal` 核对；
- `coast/left/right` 三种真实径向侧约定。

不用 rounded 坐标、最近点或近似相等命中。longdouble 的未使用 padding
字节不作为 key；比较的是原求值函数消费的实际数值列。最近 8 个 label
列的注册表受限，淘汰 label 时连带清除该 label 的缓存结果。

reference 命中后仍以原 `2e-13` 容差核对请求的完整 material-u 与保存
组合值；不能因为 `(s,label)` 命中就给另一个物理角返回旧结果。原
`jet_on_grid` 继续用 caller 的 `U_s,U_xi` 重组计算图导数，所以不会
把一侧的径向导数静默借给另一侧。

统一 LRU 的默认预算为 `16 MiB`。统计量区分数值 array payload 与
计入 key／容器 header 的保守 accounted bytes；这不是整个进程 RSS，
也不包含一次 miss 的临时求值数组。实际 packet 被深复制、数组标为
只读；返回时仅复制 mapping 容器，防止 caller 改键污染缓存。

大 `include_native=True` 诊断包不保存；DirectLabel 只保存所需的
物理 value/s/u 九个分量和实际材料列。原 `_point` 仍是 miss 求值器，
其旧内部缓存缩为 **一个 staging row**，该行占用在 statistics 另列。
这样不另叠加一个未计入预算的 256-point 大包。现有原始对象的固定
输入和原 label-data 小缓存不是本新增 LRU 的载荷；source 和 binding
仍保持原函数身份。

同一精确 key 的 miss 只调用绑定的原函数，缓存该次实际结果；hit 不再
求另一函数或插值。由于绑定、输入和 side 都保持，memoization 不改变
所声明的数学值。实际零差检查针对数值数组，不声称 longdouble padding
字节具有跨平台意义，也不把缓存当成区间证书。

## 6. 唯一少量真实点检查

新检查入口为 `scripts/fd2d-metric-prepared-geometry-cache-check.py`。
使用已闭 K31/tail16/129-node 暖态
`notes/2026-11-12-fd2d-refined-angular21-central-restore-field.npz`
（SHA `eac2a27ebecd31424bc5880a3870749cb10b8a130b2a61430d94fa83cf604d73`），
只构造原 problem，不计算原 `F/J`。

实际执行 session `50469`，`14da72 → 3c7b4b`，真实退出 `0`。
内部 `12.073596700000053 s`，wrapper `27.44888859099956 s`，
峰 RSS `92580 KiB`。没有借此测量整链速度；wrapper 包含解释器及依赖
启动，与缓存自身收益无关。

查询为三个全 512 角网格的径向点，其中两个在 coast 内、一个在出口
过渡图；另用三个 label `(.17,.53,1.12)` 支付不同 label、精确 entry
左侧/coast 侧、相邻二进制径向数及独立 ruling/seed 方法。

14 组与原函数或同点复用的实际数值差全为 `0`。两组不同 delta 下，
这三个点的当前 `a` 实际变化 `1.8167711766547967e-5`，`K` 实际变化
`0.006410631901930142`，而冻结 coords/reference 保持零差；这明确区分了
允许缓存与必须重算的对象。

exact entry、三个指定 label 的左/coast `U_s` 差为
`1.190846767018484`。这是相同径向点的真实两侧求值，且只是该三个角的
读数，不是全角侧跳最大值。两侧各自都与原函数零差。相邻 binary64 `s`
确实造成新的 miss；重复坐标与参考调用分别产生真实 hit。

只读数组的写入尝试被拒绝，返回 dict 删键没有污染后续 hit，copy view
仍共享原 chart/reference，重新安装返回同 handle。实际最终统计：

| 类别 | hits | misses | 保存条数 |
|---|---:|---:|---:|
| coordinates | 5 | 5 | 5 |
| 独立 ruling jet | 1 | 1 | 1 |
| reference physical point | 6 | 2 | 2 |
| seed coordinate | 5 | 2 | 2 |

最终数值 array payload `313312 B`，保守 accounted `340893 B`，原单
staging row `54416 B`，远低于默认预算。本小核没有为了制造 eviction
另跑大工作集；淘汰策略由实现的有限 LRU 与每次记录的字节计数控制。
未来真实 24 的缓存命中与耗时应由其实际 report 决定，本说明没有预报
速度改善倍数。

完整实际记录为
`notes/2026-11-12-fd2d-metric-prepared-geometry-cache-01-report.json`，
同 stem 的 exit receipt 和 process-observations console。它们与新源、
检查源、只读阶段记录、本说明统一列于
`notes/2026-11-12-fd2d-metric-prepared-geometry-cache-closed-manifest-01.json`。

## 7. 后续依赖边界

geometry 已独立冻结
`fd2d_gc_frozen_operator_projections.py::install_frozen_operator_projection_cache`，
其职责是纯角投影；它不改本模块的 chart/reference，两个接口可安装于
同一新 problem。numerical 在 24 接入并保存两份运行定义。本项没有
重复他们的实现、whole 对照或主求解，也不为这次求值缓存新增数学完成门。
