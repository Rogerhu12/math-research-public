# 新平切口 g 的真实 balanced 前段初猜

本次按 root 的实际 raw 三场初始化需求执行，不运行新的 BVP 或尾 DN。完整候选为
`2026-11-12-fd2d-flat-cut-prefix-v1-coast-compatible-candidate.json`，SHA256
`a92b552f70bcc26c97f16261fbc78fac10c1daad6d72eafc8063dcb093cdd147`。
整个计算中物理 \(T=.02\) 固定，中央圆柱长度为 `.5`。

## 实际执行与已保存范围

独立运行目录为 `/workspace/scratch/fd2dbfd2c83e/visible-flex-flat-prefix-initializer-01`。
该目录在启动前复制实际源码、准确中央 moment/mean 包及候选，原 Git 工作树后续变动不影响运行。
源码闭包已保存为 `2026-11-12-fd2d-flat-prefix-balanced-ivp-01-source-closure.tar.gz`。

真实工具 session **80564**，启动 chunk `7065a6`，完成 chunk `7cd1b3`，自然退出 **0**。
运行 42.962 秒，调用 4424 次 RHS，保存 **355** 个节点。前 `.5` 的准确恒定圆柱直接用
\(X(s,u)=X(0,u)+s e_z\) 生成，形状保持 \(l=m=0,n=n_*(u)\)；之后的每个保存节点都是
真正接受的 DOP853 状态，没有用插值冒充径向推进。

最后保存的可用节点为
\[
s=.8090484941089444.
\]
其点值位置导数计算给出的有限诊断为：metric 误差约 \(3.0224\times10^{-10}\)，
\(n_{\min}\approx .2649312\)，实际最大主曲率约 \(7.15643\)。这些是此有限 IVP 的节点诊断，
不是全域后验证书或完整前缀求解。

下一接受试点 \(s=.8095571388168331\) 的未保留角向 RHS 约 `.011582`，超过本次初始化
采用的 `.01` 污染保护值。其 metric 仍仅约 \(4.0874\times10^{-10}\)，正 \(n\) 也未失效。
该点保存在单独的 `-guard-state.npz`；供初猜的主轨迹明确止于前一个可用节点。
没有继续用被污染的高频 IVP 推到平尾零曲率端，也没有由该事件推断新的 g 或强目标不存在。

## 方程与坐标身份

中央使用当前准确 moment-defined `BalancedCurvatureCore((),base_kind='balanced_seed')`，
不是旧有限均值种子或某个有自由修正的旧 accepted 核。

角坐标是**固定种子法向角** \(\phi\)，物理材料角始终
\[
u=U_*(\phi)=\operatorname{arc}_*(\phi)/a_0.
\]
独立 \(n,m\) 使用最大频率 190 的实偶/奇 Fourier 场（参数 `modes=191`），
非线性右端在 768 个角点计算并按原有限方程投影；\(l=(K+m^2)/n\) 是完整实际函数，
不另作 \(l\) Fourier 截断。位置和标架在该细角网格逐点推进，旋转乘积不截模。
metric 由实际位置角导数计算，没有把辅助 frame 正交性当作实际等距证明。

径向坐标为物理经线 \(s\)。在当前 \(T=T_{\rm ref}=.02\) 时，它正好等于 root 的参考 \(x\)。
root 使用的图册为
\[
U(x,\xi)=\xi+(1-\beta(x))(U_*(\xi)-\xi),
\]
其中 quintic \(\beta\) 的区间是
\([.58,\ 1.263603200988874]\)。消费时必须先求材料 \(u=U(x,\xi)\)，再反求对应 \(\phi\)；
不能直接把保存的 \(\phi\) 当 \(u\) 或 \(\xi\)。形状 \(l,m,n\) 是正交标架的标量值，不乘图册速度。

## 保存实体与 reader

完整压缩轨迹为 `2026-11-12-fd2d-flat-prefix-balanced-ivp-01-trajectory.npz.gz`，1,374,989 B，SHA256
`db7614138c5f55b77e23f04849af02c75db36a277064b64f684a8da574c68c51`。
它保存实际 \(s\) 节点、96 个 \(n\) 实余弦系数、95 个 \(m\) 实正弦系数、各自实际有限 ODE RHS、
独立 `l_m_n_sample` 点表、固定角/材料角映射以及最后完整 pointwise-frame 状态。
真实曲率 \(l\) 没有因为旧 14 列 `gc_values` 的布局而丢失。

薄 reader 为 `scripts/fd2d_flat_prefix_initializer.py`，SHA256
`6300cd5e5134480da94914362c0704627c11d89405123703710fe9e596ffefa9`。

```python
from fd2d_flat_prefix_initializer import ActualFlatPrefixInitializer
guess = ActualFlatPrefixInitializer(trajectory_path, candidate_path)
field = guess.evaluate_material(s, u)  # 或 evaluate_phi(s, phi)
# field: l,m,n,n_s,m_s,l_u,m_u,n_u,phi,u
```

reader 在径向定义了一个**仅供初始化**的共享节点 cubic Hermite 插值，节点一导使用源中真实有限 RHS。
它不是原 DOP853 dense polynomial 的导数，也不是新的认证场。所有请求必须落在
\([0,.8090484941089444]\)；域外不会静默补点或外推。root 可以显式与真实尾 lifting 混合，
但该混合本身仍是待求解的初猜。

reader 的一次实际消费检查 session **77785**，`a5df01` 到 `500173`，自然退出 0。
25 径向节点、19 角上的 \(l,m,n\) 与原点表差至多 \(7.11\times10^{-15}\)；
同一材料点经 \(u\to\phi\) 反解后的形状差至多 \(8.89\times10^{-15}\)。
还保存了 root 上述真实 \(\xi\) 图在 5 个径向截面的预览；它没有另算任何 PDE。

当前已交给 root 的对象是强 balanced 核出发的真实局部非线性轨迹。
尚未支付完整冻结 feedback 段、后续过渡段、平尾匹配、闭合或强目标最终几何。
