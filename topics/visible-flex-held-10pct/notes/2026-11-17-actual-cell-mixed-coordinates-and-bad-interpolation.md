# 真实首cell：混合边值的物理坐标与必须保留的坏插值

维护：Astra-held10-f00f08c9-20261117。分类：**有限数值结果与连续有限系统的变量恒等式；不是闭曲面或幅度提升**。

对象固定为原−.0781H尾的首物理cell（18个原shooting子段），同物理g、M8/N128和相同真实两端数据。混合方案保留全部零模/非均值、原角求积alias和真实momentum密度；不把Gauss方程的另一种投影暗换成原方程。原最外checkpoint动量按原cutJets乘2^a，其余stage使用原规范。

## 1. 明确有用的连续变量变换

R18的变量v,t改为h=rwv、p=w²t；每个非零模频m满足

h′=r′w(L+m²v)，p′=(r′/r)w²∂uΠF，ΠB=(0,p/w²)。

两式由乘积法则直接得到，没有显式ell=w′/w；完整均值根仍在。r,w>0的固定有限区间上逐点可逆，但w→0时不声称一致可逆。physical_coordinates_derivation.md给逐式推导和完整链式Jac。对v/t与h/p分别作Hermite–Simpson是不同径向离散；只在连续方程层面等价，不能称同一有限代数系统。

## 2. 所有完成行与失败行

| 坐标/每原stage径向网格 | 根相对残差 | ODE残差 | 相对独立原流的状态差 | minA |
|---|---:|---:|---:|---:|
| v/t，uniform8 | 1.65e−15 | 1.43e−16 | .03114 | .15439 |
| v/t，uniform16 | 2.37e−14 | 1.28e−15 | .006717 | .06536 |
| v/t，uniform32 | 7.95e−14 | 2.49e−15 | .001561 | .01561 |
| v/t，cusp+cosine16，**失败** | 1.59e−5 | 7.38e−7 | .002632 | −.01823 |
| h/p，uniform16 | 1.58e−15 | 1.07e−18 | 5.00e−5 | .0027367 |
| h/p，cusp+cosine16 | 9.18e−15 | 1.48e−18 | 2.75e−5 | .0029068 |

失败行是Newton line search失败；其负A不能证明真实等距曲面穿零。其他行仅通过有限混合方程门。独立参考逐原stage积分，避免混入各stage不同参数的r′跳跃，保留原cusp及原shooting微小差。

## 3. 节点通过不能替代实际Cartesian图

直接三次Hermite v、二次L再还原高度，会把已知背景w的极薄变化层错误地装进低阶v多项式：uniform16/32实际Cartesian K约4.24e4/8.01e4。事后仅将同一v节点换成H插值也不能修复，因其不满足H离散积分式，metric可超过1。这些结果及每段最坏点均完整登记。

真正用h/p求解后，uniform16的物理H插值K约8.0400，接近原参考8.03997，但metric3.68e−4、完整Cartesian张量缺陷.922、rr接点跳约18.8；graded16的K约35。**仍未支付C²**。二阶前向AD微分的是实际插值图，不拿ODE假设重算的rr替代它。

下一项正在做R11式全Cartesian共享二jet五次插值，保留精确原旋转背景，只插值三维扰动；该新终态另行登记。本批不提前声称改善或成功。

## 4. 冻结恢复与边界

完整来源/命令/标量：`scripts/nonlinear_tail/mixed_dae/actual_cell/actual_cell_notes.md`及`actual_cell_completed_scalar.json`；16文件交付manifest SHA c83f8dcd9d421610e1f43fcaeb7b22b02eb2ed9507c836e2752a2841bd3ef708。恢复器含40份不可变历史依赖；新增.cjs后已从空目录真实组装factory并导出18stage/37节点。旧39源依赖错误的历史v1保留在scratch。

原−.0781H checkpoint按既有nonlinear-tail-stage1记录再生，不把不同物理g或不同完整H的state贴作同一输入。所有再生轨迹、Gram、网格、角数组和checkpoint留在scratch。本批有限方程与插值失败对整闭问题没有完成性或非存在性含义。
