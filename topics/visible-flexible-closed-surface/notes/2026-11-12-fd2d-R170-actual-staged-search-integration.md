# R170 的实际分阶段求解接入

## 真实函数与新搜索域

本组使用既有同一 material-u 几何场、131 节点 P1 修正、31 个中央角模、16 个尾 Bernstein 参数、7 个物理 metric bump 参数。R149/R153/R155 和完整 R165 求积函数均不改变。新类 `DyadicTailRefinedDAE` 和真正的新 `DyadicBernsteinFlatDevelopableFamily` 接受严格的八段 degree-15 Bernstein 子盒；不是把旧类更名或绕过负全局系数 guard。

令全局尾控制为 $b\in\mathbb R^{16}$，准确二进制矩阵 $S\in\mathbb Q^{128\times16}$ 来自 R170 的八段细分，搜索域为 $0\le Sb\le6/5$。这充分保证真实曲率多项式 $0\le P(q)\le6/5$，原真实尾几何预算因此保留。旧逐系数 Bounds 已明确移除；QP 新增全部 128 条缩放增量行，中央上下界、39 个 profile 正值行、profile 盒及真实中央 gap 线性条件保持。

## 完整身份与投影

新 Context 源是旧 staged 初始化控制流仅换真实 factory，再接相同 R165 定义；完整 objective 和 diagnostics 继承冻结源。实际 request、source、域定义均进入独立 binding。`project` 不再 clip 全局尾系数；先作准确有理子盒检验，仅必要时调用 R170 显式向常数 3/5 收缩并记录完整修补。profile 盒与精确中央/cut 线性边界保持原投影。实际 checkpoint 保存独立 tail_search_domain_definition/kind/certificate，完整归档 native 使用 R170 专用 decoder，不让旧 K+1 或负系数 guard 读新场。

对 29 的真实 accepted 输入 `6668aa11…fe77c`，首次新域准备并没有改变任何实际向量或静态场定义数组，也没有重新求 F/J。只在新 provenance 下闭存已经求出的实际值包，并保存明确同函数 relation。原完整 unscaled normal、列缩放及 Schur 均原字节保留；输入 SHA、实际向量、mesh/atlas/lifting/窗口、目标、数学源逐项相同，只有已声明搜索域/context 实现发生变化。实际 direction 使用新域 binding，且 normal loader 用新 provider 重建并严格核对原完整消元映射。

## 真实两个方向和试步

同 29 完整 normal 下，原逐系数盒方向的预测范数为 3.420485168126175，新子盒方向为 3.412277190266488；改善很小，因此没有宣称原尾盒是主要瓶颈。新步端全局系数约在 [-2.90713,2.56984]，六个为负，但全部 128 个局部系数经准确有理检验仍在 [0,6/5]。该次没有尾修补，只有原边界投影 2.22e-16。

R170 全步实际 F 范数为 6.290524642917807，不满足 Armijo，已真实 exit0 并保存拒绝。随后同一方向半步实际通过：4.188531596931082 降为 3.6542929578185577。新 accepted 实体 SHA `3bceef937899fad65e512e56d3bd747a6d225b20301b64ed9d04582a4f6db981`，真实 gap=0.7987754625420107、A=1.3568209996741427、B=0.5580455371321319；node G 仍1.6492330583，形式节点曲率7.3873970053。强目标未完成。

两试步都消费 R176 `checkpointed_grouped_objective`，保持完整原 F 行序、domain 和 Armijo；131 个 node 包、65 个原 cell 块及完整 interior 包独立绑定当前全向量/源/实际 mesh。新引擎 source 明确记录；不是从未完成的残差估算接受。实际半步先写 accepted NPZ 再值包。31 随后从该真实实体复用完整实际 F，重新装配其自己的 normal，不借旧状态 Jacobian。

## 后续同域装配

另名 `fd2d_gc_dyadic_normal_tile_io.py` 和 `fd2d-gc-dyadic-stage-normal-*` 保留原 R165 行分片与全部链式 Jacobian，只把 Context 和实际执行源绑定为新 R170 接口。原 pure NumPy piecewise reducer 不需要修改，它核验真实共同 binding、逐行账本、原 tile 顺序和全覆盖。新 v2 selected-normal 接口明确区分初次域变化的原 normal 复用和新状态 freshly assembled normal，不能将二者暗中等同。
