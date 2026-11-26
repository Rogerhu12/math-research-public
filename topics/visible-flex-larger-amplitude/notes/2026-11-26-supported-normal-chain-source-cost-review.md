# 5297 normal-chain 实现的成本与等价省工位置：完整只读审查

2026-11-26。对象为 `so3_supported_unit_normal_lift_operator.py`，91,472 B，SHA256 `5297192216356970140585eb9e56c521d9f35453211fb5a76086b713350eaa67`；固定参考 base 为 e1bb、provider 为30ea。只读源码和已有 R703/R707，不执行科学计算，不改正在运行的入口，不将等待时间或源中操作计数当成实际时间归因。本条是实现审查，不新增数学定理或验收门。

## 1. 回答：已经逐 stage 递推，没有全局密集 6m/9m 矩阵

当前实现确实保留了全上游的块下三角依赖。它没有组装或求解一个维度为 `6*normal_stage_count` 或 `9*normal_stage_count` 的密集矩阵。

- `_run_chain` 每段实际求三个 increment 根；`_finish_stage_jets` 用该段同一3×3矩阵依次解一、二角 jet。
- `_get_roots(..., need_linearization=True)` 按实际角/段生成6×6或9×9的**单段**角 jet Jacobian，并存到 `stage['jacobian']`；`jacobian_order` 标明已付阶数。数值根、`eta`、`controls`、三套 `frame`、3×3矩阵和原逐段记录均存于同一当前完整自由点的 `_root_cache`。
- `_implicit_jet_value` 每段只调用一次局部6/9维 `torch.linalg.solve`。已选根、frame和control工作字作 forward anchor；`residual-residual.detach()` 提供完整同方程一阶外参数导数。
- active 的 `previous` 仍携带前段完整图；`_normal_frame_jets(previous,data,order)` 重新建立 $A(y,u_{i-1})$ 的完整参数和角导数图。原零控制目标也用 `zero_hat+(zero_computed-zero_computed.detach())` 保留参数链。这里并没有把前段 $A$、$u$ 或 $f(0)$ 冻成无导数常数。
- `vjp` 对这个相同递推图反传，所以其全链转置由反向依赖完成。它不需要在源码中显式构造全局块矩阵；也不能把单段矩阵的缓存误读为丢掉全局下三角项。

这些是 R703/R707 已有全链关系的实际接线，不重新证明它们。

## 2. 已经存在的缓存及其范围

`_select_point` 在完整自由向量改变时清掉当前 root/residual cache；因此不同 trial 不继承另一点的数值根。固定点处，literal angle hex 去重；相同角后续 field/J/J*可复用已选完整根和单段矩阵。`clear_base()` 只清 residual cache，没有误清同点根。

一阶到二阶的升级明确保留原 `eta[:2]`、`controls[:2]`、`frame[:2]`、原3×3矩阵，并在实际新数据上重读原端点方程。没有通过重跑零阶根改变原分支。二阶完整局部矩阵按需另建，不能拿一阶矩阵填充成二阶证据。

固定 supported 参考的均值根在 provider 内按 literal angle缓存；完整 radial plan和固定参考积分/grid四jet也分别缓存。因此它不是每次 J/J*重新求 R709 三均值根。base 的 `_parent_tensor` 仍会读取对应固定 `.npz` 并转换为tensor；这是固定工作数组读取，不是重新求根。其现策略故意不把所有角块的大数组驻留内存。

## 3. 当前每次 J/J*仍重复的具体工作

active 调用每段重新执行 `_normal_frame_jets`：对该段全部积分节点上的完整 closure jet做3个输出分量的反向产品，角阶1时6个、角阶2时9个。`create_graph=True` 使这个 partial frame能继续对外参数及全部上游求导。这部分不能以 cached frame的值替代，否则会删掉 $dA$。

随后 `_stage_constraints` 还在同实际 anchor形成完整段残差图，再通过单段 implicit solve连接至下一段。`jvp`使用 `torch.autograd.functional.jvp` 包住每个完整角块；`vjp`每角块重新构造同一完整图并反传。此源没有缓存整棵 active AD 图，也没有显式的手写 tangent/adjoint逐段 kernel。不能把“局部矩阵已缓存”理解为“后续 J/J*不再积分/微分完整场”。

局部矩阵的**值**缓存了，但 `torch.linalg.solve` 每次调用仍接收其完整tensor；源码没有保存对应 LU/其他 factor。矩阵仅6或9维，不应未经真实分项数据就把这点称为主要耗时。

现有 `actual_normal_counts` 可以分辨 attempted closure jets、frame reverse products、stage矩阵行和各类 solve；未见这些子步骤各自的 wall time。它们足以说明执行次数，不能直接证明占时比例。

## 4. 最小独立后继：只避免 no-grad 路径建立随后丢弃的高阶图

`_normal_frame_jets` 已在进入时保存 `enabled=torch.is_grad_enabled()`。它为求 partial $f_u$ 必须临时 `torch.enable_grad()`；但内部每次 `autograd.grad` 当前仍无条件 `create_graph=True`，最后在原入口 `enabled=False` 时才 `detach()`。

在 `_run_chain` 的真实数值根和角jet构造阶段，外层 `torch.no_grad()`，返回的 frame只作为数值值/缓存使用。此时可以在**独立新源**中把该参数改成 `create_graph=enabled`。完整角阶1/2公式已经显式在 `_closure_jets` 中；这里不是靠继续自动微分该 partial梯度来获得下一个角阶。保留必要的 `retain_graph` 直到所有分量梯度读完即可。

active `_implicit_jet_value` 的入口 `enabled=True`，仍全量建图；所有 $dA$、前段control和零目标导数照保。绝不能把全函数改成 unconditional detach，也不能把 active 部分改成 False。本建议不改模型自由量、支撑、共同partition、根验收、域、几何行或物理目标。

是否改变实际浮点归约字必须由新源自己的实际运行如实记录；不以数学公式相同承诺旧缓存可跨source继承。若实施，应有独立source/schema绑定与新实际baseline；本审查没有改动5297。

## 5. 同分支二阶升级：只求新 A2，保既有 A0/A1

现 `_run_chain(..., existing=...)` 先调用 `_normal_frame_jets(previous,data,2)` 算全三套frame，再把前两套覆盖成旧缓存字。对这条**no-grad升级路径**，可以另设显式输出阶选择，只算第2套 frame；原0、1阶原字直接复制。计算第2套仍必须消费完整 previous 三jet和完整 `T/Tp/Tpp`，不能把其中一阶、二阶上游清零。

同样，升级前原 `zero[:2]` 先重算再覆盖；可以只补二阶，但保留末尾实际原方程重读，不能为省工删掉该确认。

active路径仍须三套frame完整导数图，不复用无导数的A0/A1。二阶新段矩阵以及全部失败/upgrade来源记录仍须完整。这个优化只是避免计算马上被原缓存字覆盖的值。

## 6. 较大后继的正确接口，而非当前源替换

若真实返回后来表明 active AD图成本突出，可将已有 R703/R707 下三角结构变成显式 tangent/adjoint接口：每段固定原实际 anchor，完整计算前段control/frame与外参数方向对该段方程的贡献，解同一个局部6/9维方程得到 increment方向，再传播完整control jet；转置按段倒序解同局部转置方程并累计对前段及全部外参数的pullback。

这必须保留 $A(y,u_{i-1})$ 的全部变化、相同 $f(y,0)$ 的变化、全部一二角jet和 core/H支路。不能只做每段独立 `-J_i^-1 f_y`，也不能把每段结果对前段求导设零。cached numeric roots只决定forward anchor，Newton迭代轨道本身仍不求导。固定共同partition不能为每角自适应替换后仍冒同一场。

这类重写应独立完整源并先接真实新baseline，不能直接丢进正在运行的入口。没有实际候选返回或分项耗时之前，优先的小改仅是前两项明确重复工；本条不声称它们已解决首场收敛或性能问题。
