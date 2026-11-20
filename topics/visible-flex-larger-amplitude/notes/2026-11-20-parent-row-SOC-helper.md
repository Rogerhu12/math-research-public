# 真实几何拒步的固定父行二阶修正 helper

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / recover_evidence。

[完整源 full_phi_parent_row_soc.py](../scripts/resume_20261120/full_phi_parent_row_soc.py)，
30,947字节，SHA256
`5bc50d6b18223685da8ea355d179191234ad83b5e92fd6313f4070b7e02127c7`。
已逐段静态核对和AST解析，未import/科学执行、未建fixture、未改变运行中的方向。
这是R680的数值候选生成接口，driver接线仍在准备；没有实际SOC接受、性能或收敛结论。

## 实际动因和保留的目标

[已返回六方向与R671归因](2026-11-20-actual-original-six-and-geometric-rejections.md)
明确显示较大步真Phi下降而真实几何门拒绝。这里仍保原.992/.025数值参数、
原完整自由空间、原QP母范数、全部旧行与所有永久点，不以放宽门限得到接受。
它与R677线性继续求解、R681预条件准备分开；修正的存在不证明内层已收敛。

本源只在原始alpha=1试步有限、原域可行且真Phi已降，但实际完整几何screen失败时
尝试一次。几何读数不完整或奇异时不提出修正。其它情况保持原回溯。
当前对象一次尝试后不得重用为第二次；新父和新方向须重新绑定实际输入。

## 固定父行身份，不用全局最大值替代每行

`ParentRowsSOC`接收本轮同一个problem、父x、完整mmap行矩阵C、bounds、
v2行metadata、原几何/点/observed/inequality模块，以及实际source/model身份。
只消费冻结e783c8a3 v2行语义；逐条核行索引、norm、margin与literal bound，
矩阵必须是该metadata所指实际mmap。原模型与R671分别核完整六jet和点适配源；
R671同时核canonical definition、实际M/carrier、同context及factory2e0219c5。
身份/接口错误明确抛出，不伪装成一次普通不接受。

对每条父行，保存原曲率位置及principal branch、原radius partner和原norm $n_i$。
在试场$x+Td$只重新读取该固定二元组合的真值：

$$c_i(d)=\frac{.03D_i(x+Td)|\kappa_i(x+Td)|-.992}{n_i(x)}.$$

grid点仍走其实际grid六jet合成，arbitrary点走原模型绑定的point reader；
不把两种浮点约定只因物理坐标接近就混换。radius伙伴可以是固定core直径2、
实际帽高$2|H|$、指定grid半径或指定arbitrary半径。
不重选trial全局最大radius、不重新归一化、不把整个screen的单个product当每行残差。

同时记录实际非线性余项$c_i(d)-(C_id-b_i)$、signed curvature、principal gap及符号变化。
端点gap为正只是数值读数，不是整个路径上分支光滑或Lipschitz常数的严格证书。
若全部固定父行均未正越界而总screen失败，不臆断一定出现新峰；
未选二元组合、其它绝对门或不同读点数值约定都仍可能负责。

## 原范数QR修正与完整旧行检查

令$I=\{i:c_i(d)>0\}$，对显式数值参数$\tau\ge0$，取

$$h_i=c_i(d)+\tau\|d\|^3\quad(i\in I),\qquad C_I=RQ,$$

其中$R$是下三角、$Q$按行正交。本实现用两遍modified row Gram–Schmidt，
大Q仅存Actions raw mmap，按列分块读写；不形成$C_IC_I^T$的逆。
原范数最小等式修正的声明公式为

$$e=-Q^T R^{-1}h.$$

这里不能把下三角R误转置。若数值秩不足，整次proposal退出，不丢掉从属约束继续冒称成功。
三角解后记录R奇异值、Q的数值正交误差、实际等式残差、修正范数和右逆norm诊断；
这些是实际浮点诊断，不是严格奇异值包围。

随后直接重读**全部原行**$C_j(d+e)-b_j$，并保存其literal slack、真实父行单位下
的线性product以及数值可行容差对应的物理余量。只验证$I$不够。
若任一旧行超声明容差，保原射线回退。即使全旧线性行通过，返回值仍只是proposal，
不能由线性行或固定父行读数代替全grid/所有永久点的非线性screen。
raw Q、向量、逐行数据只留runner；不写Git/Release/artifacts。

## 与R680定理的准确边界

[R680](../results/R680-true-geometric-step-second-order-correction.md)给定光滑约束、
满行秩、Lipschitz控制及充分三阶内移时，证明原范数$O(\|d\|^2)$修正和局部真可行。
本源没有求出该严格$L,\gamma,\tau$邻域，也不声称实际I的秩诊断付了这些条件。
tau是必须由调用者显式给定并记录的算法参数；tau=0明确是无内移版本，
不能引用严格内移定理。实际成败交给完整真场读取。

由于C由同一原完整T拉回，准确算术中$\ker T\subseteq\ker C$，而最小范数e在
$\operatorname{ran}(C_I^T)$，没有人为注入零物理场的方向。这里不删任何原变量、
不改变母范数、无新Phase-I、无额外线性人为余量。

## 最小调用与尚未完成的driver接线

以下仅是后继公开Actions内调用约定，尚未运行：

```python
soc = module.ParentRowsSOC(
    problem, x, active_rows, active_bounds, active_metadata,
    geometry_module=geometry_module,
    point_module=point_module,
    observed_module=implementation,
    inequality_module=inequality_module,
    source_sha256_by_role=report['source_sha256_by_role'],
    observation_carrier_sha256=actual_carrier_sha256,
    model_definition=None if context is None else context.definition(),
    parent_bundle_sha256=actual_parent_bundle_sha256,
)
proposal = soc.propose(
    coordinate_step, lift, full_trial_point, full_trial,
    tau=explicit_tau, workdir=runner_soc_directory,
    rank_tolerance=actual_rank_tolerance,
    feasibility_tolerance=actual_linear_tolerance,
)
```

返回`Proposal(candidate, augmented_step, correction, report)`；没有候选时三个数组为空。
helper不改变x、不接受试场、不更新mu、不执行主QP或Phi。
driver须保留A/model residual/原d/完整行到尝试结束，支付修正方向自身的模型读数，
用修正后的真斜率与预测下降计算接受/阻尼，并实际读取修正场完整Phi、域可行性和所有真实点。
修正及原试步发现的新位置都永久保存，修正失败后仍沿原$x+\alpha Td$继续回溯。
这段接线尚未完成，因此本条不排入实际科学队列或宣称已有修正结果。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
