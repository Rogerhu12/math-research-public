# 新 M28 当前基准的完整均值几何场

2026-11-13，geometry_audit，AI-assisted。**已实际完成的有限数值诊断；不是连续证书。**

新基准固定为 strong 已完成的 `2026-11-13-strong-m28-recovered-physical-r1`：实际主系数 $0.0959999590672073$、全部 28 模、2208 个原 raw 节点及其已记录数值图表；没有使用旧 q095 场来代替它。

从原 resident 几何 wrapper 新建 `root_actual_geometry_field_complete_mean.py`，原源不动。新版本将完整高度积分、$F_s$ 的均值项和 $F_{ss}$ 的均值项统一为物理后处理器的 $\max(512,16(3M+1))$ 角规则；本次为 1360。高度仍在每个原 raw 区间使用六阶 Gauss，独立 batch 为 8。几何取样角数为 384，两种角数的含义分开记录。

公共径向网格有 3383 点：包含全部 2208 个原 raw 节点、全部物理断点的锚、每段 33 点、物理均匀 241 点、数值均匀 257 点，以及先前已知峰的材料标签。保留旧标签只是避免丢掉已知位置，不宣称它还是当前最大值。

baseline 已正式 exit $0$、signal null，耗时 $113.83110881$ 秒，峰 RSS $157292$ KiB。全部 $3383\times384\times3$ 分量已保存，无 Node、无新 BVP、无新 nonlinear-tail 评价。当前场是穿过全部原 raw 数据的物理 $s$ 三次样条诊断，不是 accepted physical quintic 的替代证书。

关键结果与完整原 report 一并归档。两条主曲率的最大绝对样值为 $8.383679679468635$；与 accepted physical 报告的 $8.383682337531232$ 接近，二者仍是不同插值表示及取样网格，不能据此宣称连续误差为零。`twice_radius` 为共同原点的 $2\max\|X\|=3.908756832366815$，完整高度最大绝对样值为 $1.9261534018210071$，水平半径最大样值为 $1.3451921056598604$。

完整场由八个连续 gzip NPY 分块存放于 `geometry-work/m28-q096-r1/`，总计 $11578336$ 字节。每块完整 SHA 和位置见 `2026-11-13-geometry-m28-q096-r1-baseline-manifest.json`。按根 README 的可重建中间数据规则，本次只归档源、精确参数/输入身份、网格、原 report/resource 和分块 manifest，不再向仓库添加一套大数组；若 scratch 丢失，运行原 baseline plan 的完整命令重建，不把元数据当成已恢复数组。

`root_actual_geometry_fullmean_plan.py` 允许先完成此 baseline，再在新 M28 完整实际控制响应完成后补同一网格的十个正负方向场，baseline 不重跑。`root_geometry_minimax_from_plan.py` 已准备消费新十一场，仍待所有实际字段完成后执行；它只复用此前全行优化算法，不导入旧 q095 数值斜率。新几何方向继续为 strong 的真实增幅求解提供预测，未支付 closed/held/reach 或全频存在性义务。
