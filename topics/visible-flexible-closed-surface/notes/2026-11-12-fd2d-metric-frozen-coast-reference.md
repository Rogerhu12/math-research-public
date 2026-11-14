# 冻结 R139 coast 的真实一阶 jet 与逐点缓存

## 1. 函数身份

`scripts/fd2d_gc_frozen_coast_reference.py::FrozenCoastReference` 直接包装
已闭源 `SavedNativeCoast`，不另求 Gauss–Codazzi 主方程，也不对参考函数
作低阶 Fourier 拟合。完整函数定义仍是 [R139](../results/R139-native-gauss-codazzi-propagation-on-a-flat-coast.md)
的有限入口 Fourier 数据、固定材料图和显式 native 传播公式。

本实例的入口是
`notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz`，SHA256
`ed69b9a6599ef75f36f2d5bc094d152d993baeb078f4852a392648b85f6c9c3a`。
原 candidate SHA256 为
`7c3f31de4b230e8d98b99c3e3914d65ae69daa3cb5c54ae22f585a36a888bfd1`。
构造函数核对已经闭存的 R139 全角正性包及其入口、candidate、moments 身份。
当前存储代表值为

\[
 s_c=0.5919999999999992,\quad
 L=0.2755434451024161,\quad
 a_c=1.029181699754392,\quad v=0.2587478542495509.
\]

原有区间包同时涵盖准确 candidate 常数与保存代表值；本数值接口沿用
`SavedNativeCoast` 的保存代表值求值。缓存是这些显式函数的有限浮点评价，
其表项不被重新解释为定义参考函数的分片多项式。

参数全部冻结。参考 native 场的准确 GC 公式属于
`a(s)=a_c+v(s-s_c)` 的固定 `K=0` coast。主场改变物理 bump 参数后，
该函数作为显式参考 lifting 使用；主消费者仍需计算新目标的完整残差。
本接口不推断入口空间 monodromy、闭合位置或实际曲面度量已经兼容。

## 2. 最小调用接口与真导数

```python
from fd2d_gc_frozen_coast_reference import FrozenCoastReference

ref = FrozenCoastReference(inlet_path, cache_path=closed_cache_path)
jet = ref.jet_on_grid(x, coords, active_mask=active)
```

公开 `entry_s`、`length`、`exit_s`、`candidate_sha256`、`definition()`。
`x` 是一维物理 `s`；`coords` 包含 `(work,N)` 的 `u,u_s,u_xi`。
返回的 `values,x,xi` 都为 `(work,N,3)`，分量顺序统一为 **`n,m,l`**。
mask 是每个径向位置一个布尔值。默认只查询闭 coast；显式 mask 的活动
位置必须位于 coast。非活动槽置零，供调用者自己的支撑权及其导数组装。
这不宣称零槽构成参考函数的光滑外延。

`SavedNativeCoast` 已给保持材料角的 `n_s,m_s,n_u,m_u,l_u`。
因为这份冻结参考满足 `l=m²/n` 且其 `n` 在已证明区域严格正，补充的
物理径向导数为

\[
 l_s=\frac{2m m_s n-m^2n_s}{n^2}.
\]

分母仅是固定参考的正 `n`，没有除任何未知 raw 三场的 `n`。
对于调用者的 `u=U(s,xi)`，逐次使用实际坐标列作链式变换：

\[
 R_x=R_s+U_sR_u,\qquad R_\xi=U_\xi R_u,
 \qquad R=(n,m,l).
\]

这些是对明确参考函数的解析一阶导数，求值采用 R139 同一材料反解。
其数值反解容差 `2e-13` 及实际反解残差在缓存元数据中记录。
所有当前中央、尾和物理 bump 参数对参考函数本身的偏导为零；主 provider
拥有参考融合权、其径向导数、与旧 lifting 的合并，以及完整参数 jet。

## 3. 缓存键、共享与持久化

每个缓存条目只对应一个物理径向位置和一整列实际材料角。键包含
`s.hex()` 与这列 `u` 的规范化精确回读文本哈希。每次命中还逐元素核对
实际 `u` 列相等，因此不能因 `s` 相同而借用另一张计算角图。

缓存只保存物理 `values,physical_s,physical_u`。`U_s,U_xi` 不保存在条目
中，每次调用均重新用于链式变换。因此保持 `u` 列相同但改变坐标导数时，
不会误借旧的 computational jet。数值输入的 `longdouble` 使用可回读文本
做键，避免其未使用填充字节造成不稳定的缓存身份。

`copy.copy` 和 `copy.deepcopy` 都共享同一冻结对象，适用于原生 problem
的节点视图和 Gauss-cell chunk 视图。缓存是操作状态；定义参数和入口
数组保持冻结。

`save_cache(path)` 写一个新的不可变 NPZ（超过仓库压缩阈值时按既有
存储规则使用 `.gz`），返回其真实路径、字节数与 SHA。`load_cache(path)`
核对入口、candidate、源、moments/means、既有正性包、数值精度、全部
实际角列，以及保存 jet 字节的哈希。通过后可直接复用条目。

静态 `binding_sha256` 是这些依赖的规范指纹。`cache_statistics`、已加载
缓存的路径、命中次数只记录运行情况；它们不属于数学函数身份。可迁移
消费者应比较静态指纹和自己的支撑/权定义，同时保留完整原始说明。

## 4. 真实 122 节点预填

生成器为 `scripts/fd2d-metric-frozen-coast-cache-prepare.py`。输入实际保存
网格是 `2026-11-12-fd2d-raw-bump-turnmesh01-warm.npz`。生成器只读取
其网格、角阶、blend 与 candidate 身份，不消费其未收敛修正作为参考场。

使用与原 provider 相同的 `BlendedIntrinsicGC` 和准确固定 seed 材料图，
逐点生成原 `U(s,xi)` 列。Gauss2 位置使用与原 helper 相同的
`numpy.polynomial.legendre.leggauss(2)` 算法和物理节点运算顺序。
在参考 coast 内部共有 8 个保存节点、18 个 Gauss2 点，合计 26 个不同
径向位置。预填使用 `rim_fraction=.12` 的支撑约定：coast 两端权及一阶
导数都为零，可以跳过；具体权值与导数仍由根侧 provider 实施。

实际命令：

```bash
python3 scripts/fd2d-metric-frozen-coast-cache-prepare.py \
  --inlet notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz \
  --field notes/2026-11-12-fd2d-raw-bump-turnmesh01-warm.npz \
  --candidate notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json \
  --out-prefix notes/2026-11-12-fd2d-metric-frozen-coast-reference-01 \
  --rim-fraction .12
```

会话 `96475`，最终退出块 `cd4421`，实际自然退出 0；耗时 67.979 秒，
进程峰 RSS 72,976 KiB。逐径向点求值，每四点保存一次可恢复缓存。
没有组装大矩阵或另解 BVP/位置 ODE。

最终缓存
`notes/2026-11-12-fd2d-metric-frozen-coast-reference-01-cache.npz`
共 401,936 字节，SHA256
`a300860b15e993f4272dff55d9068723664d84240d643a195b2c955ab15fd6c8`。
静态绑定指纹为
`5a0fbc11024e0b73e2956e29520334418c4da357bfc854fa9969deb7cd15cfce`。
重新加载后 26 个实际查询全部命中，新增公式求值次数为 0，`values,x,xi`
与首次结果逐位一致。材料反解残差最大约 `1.954e-13`，原生 GC 公式的
实际求值残差最大约 `1.276e-14`；它们是数值观察，连续包仍来自原证明。

完整实际报告、逐点进度、部分缓存、最终缓存、源与真实退出记录统一列在
`2026-11-12-fd2d-metric-frozen-coast-reference-closed-manifest-01.json`。

## 5. 与 D2 行压缩的相容性

冻结入口具有 `n_c` 偶、`m_c` 奇与 `pi` 周期，所以 `k=m_c/n_c` 为奇函数，
`k_t` 为偶函数。R139 的 `w,Q,D` 都是偶的 `pi` 周期函数。
材料图

\[
 U(\sigma,t)=t-\frac1v\arctan\frac{w k}{\rho_c+w}
\]

满足 `U(sigma,-t)=-U(sigma,t)` 和 `U(sigma,t+pi)=U(sigma,t)+pi`。
严格 `D>0` 保证的唯一逆保留同样对称性。故 R139 的材料 `n,l` 为偶函数、
`m` 为奇函数，均为 `pi` 周期；复合当前旧计算角 `U(s,xi)` 后仍如此。
任何径向支撑权和固定参考融合都保留该性质。因此新增这个参考函数后，
[R142](../results/R142-D2-isometric-high-angular-row-compression.md) 的解析
D2 前提仍成立；该结论来自公式而非有限采样拟合。
