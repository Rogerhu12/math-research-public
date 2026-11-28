# R790 / Run53：原完整物理流的逆坐标传输及第44组全部预算

Astra-larger-e4e2a2bf-20261126（AI）。ROOT全文读[R790完整证明](../results/R790-twelve-physical-jets-and-transported-inverse-collar-coordinates.md)、两物理源、新主求解/适配层、全参数及workflow；数学研究者独立逐读对照原R761/R763/R44给出同方程和全预算复核。新运行尚未返回，不预填run/PID、耗时、点或加速比；原44/45继续自己的原历史和预算。

## 同一连续物理问题

原R761在每次速度求值反复从同一世界点X反解两组坐标b=Bθ⁻¹(X)、c=Cθ⁻¹(X)，再计算V=Vb+ω(Vc−Vb)。R790保完整X的两坐标×六材料jet=12行，只追加b、c共4个标量，沿真实轨迹解b′=DB⁻¹(V−Vb)、c′=DC⁻¹(V−Vc)。在原正则分支上，Bθ(b)−X与Cθ(c)−X导数为零且初值为零，故与原物理ODE等价。

实际一阶/二阶逆材料jet仍从原2×2系统求得；Hessian中两个混合项和所有ss/sa/aa都代入真实速度。没有用辅助变量代替物理jet，也不引入第三几何导数。两镜帽的原X/Z材料jet完全相同时共享一条平面轨迹，但各自完整有符号轴向冠保留；其余真实材料输入不同则独立。原32768站近邻预取、.00035真flow band、.00050外预取幅、原32物料块、原近rim≤1e−8覆盖、全域直接补区以及全部九图均保持。

给定所需真实角集合，对每个原材料块从零按实际binary64角排序连续积分，每个角都是积分端点。没有用时间插表代替原相位；完整时相自然立方系数场仍由原44的实际time sampler/Objective/shape adjoint/pair list构成。不同浮点步会产生不同点字节和不同择优结果，不能称原44逐字复演。

## 原精度、正则检查和真实恢复

DOP853原rtol=2e−9、atol=2e−11保持，误差分别在12物理行和4辅助行上计算再取较大值，避免因加行而稀释物理估计。ROOT另从[官方SciPy v1.17.0源码](https://github.com/scipy/scipy/blob/v1.17.0/scipy/integrate/_ivp/rk.py)读22800B完整文件、SHA256 fa5d6300917f4f949e699b116f59ae147159d5c6147d55d940dc9d3303891056，核其实际DOP853误差表达式分母使用所传scale的长度，所以这里独立切片确保持原12行归一。

每次真实坐标图保持原残差≤3e−10、|det DH|≥1e−11检查；合格预测可做原Newton抛光，不合格预测按原分支seed调用原完整逆求解。每个请求角结束又在不改物理12行的情况下恢复实际标签。增广积分数值失败时，原完整R761 move按同一个原32点块、每个剩余实际角分别重算；原恢复若失败仍是真失败。原失败/恢复次数、RHS、真实残差/行列式、物料点和角区间计数公开，不把计数当作速度或科学成功。

最多四个公开CPU独立处理原块，临时表按完整material word、阶、ramp和角集合精确key复用；768MiB临时文件预算超限只驱逐重算，不删材料点或相位。原角/两镜完整冠与两族物理对象不截断。

## 原44全部11阶段

27实际冻结输入=22份原44完整输入加五份新科学件；原44入口本身直接提供Objective、pair_list、times，原5795B参数文件也实际读入。ROOT将designs、physics、mesh_times、coarse、refinements、runtime和两export SHA逐项与原文件比较，完全一致。五粗起点（三released、二tube）分别做两个原L-BFGS块；两个族各自选后都执行4/8/16时间区间三层，共11阶段。

原训练mesh25/9/8/7，独立51/15/12/12、两区间；三个细层训练35/13/10/10、49/17/13/12、65/21/16/15，独立67/21/16/15、91/29/20/18、121/39/26/22。每块原maxiter30/35/42/50，原pair_count1536/2048/3072/4096，全部原线搜索、同点方向导数观测、全时间联合目标、重新扫描有序弦和独立九图/全部接缝/normal–cap重叠实际检查保留。没有新增准入测试。

同一runner上为两最终独立点分别做原全部验证相与七个整闭mesh时相的并集，保点/NPZ/PLY/几何index完整身份；所有raw留定义runner。参考未修正R761的理论管不能转借新优化场；有限Gram/曲率/法弦/整像样本不当连续证明。两真正全末网和同g加密结果自然返回前不填成功。

公开四核16GB runner，Python3.12.14、numpy2.3.5、scipy1.17.0、jax/jaxlib0.7.1及FP64，数值BLAS线程均1。原360min job，无子进程新增墙钟截断。共享原完整Run48主管每2700秒真实pull/rebase并读双README差异，无新科学值也即写note/HANDOFF；普通拒推即时合并再推。

## 完整身份与恢复入口

[完整请求](../computations/run53-shared-rim-transport-request.json)与[全部交付](../computations/run53-complete-shared-rim-transport-source-and-launch-delivery.json)保27科学/4控制的全路径、长度、SHA256/Git身份、所有原参数与未返字段。ROOT重算下列九件三身份，22父/4控制与当前主线tree核同；原44参数完整Git c20ee9f91ea0f1eb664a1be4ab53aa71037c819c、SHA256 2bc4c956d286d273928e298c58bd0799974d751ae93d022a5d730170dfa8c6e2。

| 完整文件 | 字节 | SHA256 | Git blob |
|---|---:|---|---|
| results/R790-twelve-physical-jets-and-transported-inverse-collar-coordinates.md | 8843 | 3768f73e8ef55b95e5ac1161e0916cc3bf548de315e7491e323356ebf7d9704e | 7d38c9f20e128e5ef80c3d272f94c4f76bda022c |
| scripts/resume_20261126/r790_augmented_collar_flow.py | 7942 | 16bc272fc3bd6cb4bc362788fe7cb5912f15bd58ea639686dac2c4e2e7315b9e | 3223a00e118ff8af42253997abf62326fd0c573d |
| scripts/resume_20261126/r790_multiphase_tube_transport.py | 9532 | d8b728901a5c26af4f85322757581a4eddfb4c8923ceacb60612e819b3fd737f | abfbab28773982bd08a4d9cf3363a72ea791cedc |
| scripts/resume_20261128/bent_shared_rim_transport_phase.py | 14032 | 0a760e955661f2ca2cab74c551907757561433701830d9f889c6a268a7b87ff8 | 53dfa22e3f7dce0a5df2657f0ee178b015ec07dd |
| scripts/resume_20261128/bent_shared_rim_transport_fields.py | 1516 | dae6e2f74d0f2c4db36650339d1eb99a6020e5d33a51ae2331e84669f74c0d33 | 7007bddae4572fbfe7a2bd75d799c299394f5dbf |
| computations/bent-shared-rim-transport-design-v1.json | 7267 | 54eca00464bd0fe03109338fde69a597490e50c3abafe001b7c6784644295cdf | a2ca33beaab5f0342eb2a8bce34629bf2f5ffd14 |
| .github/workflows/visible-larger-run53-shared-rim-transport.yml | 5328 | 517d1a072572395477fdd3a70ed9fe8105267942de4847eefa7d1d8f151affef | 4bf597edbe39599ff08a4167026e530dcaa1e9b5 |
| computations/run53-shared-rim-transport-request.json | 26162 | f271b7031c8c0ad694bb14d479d36e7fb17227feda74ce4f8bcabdfef803328d | e114a6c6bb2c095eefc74a0a4a9e702c8eb7c034 |
| computations/run53-complete-shared-rim-transport-source-and-launch-delivery.json | 37638 | 6830c1bba772870e99922d911162f22c7b5cab136c441fb816726922656e0dc8 | 9207a4418248b24d687d988ba6b0f46b47f0e256 |

ROOT本次云端小文本发布非pull。完整新科学须靠自身实际返回判断，所有原预算与README完成标准继续。

## 新输运实现自身的实际启动（2026-11-28）

source 8b7e069ba67b38cbad5454a391f18a9bebb5d4f5，public run46183731999/1、job141098858624。ROOT独立读取官方jobs，finite_amplitude原完整科学步骤in_progress。科学PID2552在19:56:35Z真实启动；27个actual_frozen_inputs逐一与请求的原路径、完整长度、SHA256及Git blob核同，actual里的scientific_inputs也全同。原44/45继续独立运行，本53没有删其预算或覆盖其历史。

固定30d2ccbf3d44c60c822e4671726800572abcff06的实际原记录为27459B/Git fc5d2c3232d70efb8f2dbb3c2744193238a1cc37/SHA256 499f546e19d48297f0fe4741c458e3c040454789dd48e836267cfa2396d822ad；20:00:57Z已有3个完整stage进入summary。这些早先released分支没有管道积分，不能由它们的零transport计数或耗时判断R790改进效果。后续原两个tube粗起点、两族4/8/16和两次原完整末网继续；真正物理解、全域误差和实际加速仍待其自己的完整返回。

最新原真实pull为20:00:58Z至78e4083c67efc0e647375e88db2c4992a6db200f，双README核同，root此次为云读非pull。上述完整本run记录保全部实参/环境/科学点引用，未用别run的较好或较坏数值代填。
