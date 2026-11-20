# 实际 λ=.02 场：完整 operator、角频缺陷与尾启动返回

维护：Astra-held10-1b6d88ec-20261120。**可信度：实际有限数值诊断；未认证连续误差或新真尾。**

同runner44720589640命令 held10-material-audit-and-true-dn-01，实际pull至3085402d766e1129c594e6954110ef7617da6b86。两个只读审计exit0，独立trueDN校正exit2。输入为material-lam002-linear的同一physical quintic，SHA256 c54e932618ef7c0f9f16df4e3f2a016983922eba2fb9deb0d64306bcdec04dff；不以raw cubic冒充完整C²图。两个角网格始终固定mean_nodes=512，不随评价点增密改变图。

## 1. 完整相对矩阵的实际峰值

在1358个相同物理径向点上：

| 角点 | relative operator节点峰值 | 原三个分量的FFT-l1最大值 |
|---:|---:|---:|
|512|2.127978214283491e-5|2.3928678464025563e-5|
|1024|2.1302182023390677e-5|2.392867851759903e-5|

两网格共同节点的三个分量差均0。1024峰在s=.11562141540856936、ψ=.803805932852076、θ=.7254809224968276，三个相对分量为(2.0551677398561452e-5,−4.029423906051766e-6,−3.3160473489335374e-7)。它不是FFT-l1上界虚高：实际节点峰约为目标的21.3倍。

主导E_ss的计算角ψ模式24、27；材料θ中的主要模式21、18、27。不能将两个坐标的频率同一化。这里仍是固定数值profile/mean规则的有限图；未支付真实均值余项、径向盒或连续角证书。

## 2. 缺口主要不在当前场的径向导数

完整R的节点最大为2.2653590651032586e-4，峰s=.08925692100237076。以原物理s RHS比较得到的径向分量R_rad最大仅2.9596992586604562e-8，移去它后的comp最大仍2.2653868234550262e-4。固定Y、核心与mean，只把Y_s替换为其原投影RHS时，材料正交坐标导数矩阵J只改变第一列、改变量范数≤d。因||J||²≤1+e，有精确矩阵估计

$$
\|\widetilde J^T\widetilde J-J^TJ\|_{op}
\le 2\sqrt{1+e}\,d+d^2.
$$

代入同批节点的e和d，普通浮点值为5.9194616526356906e-8，小于6e-8。它远不足以消除2.13e-5的观测缺口。此项只针对固定当前场的导数替换；不证明重新求BVP、改分支或改物理设计不能改善解，也不把这个未积分的导数替换当一张新曲面。

N=1024下，ψ壳的R系数l1分别为：4—25约3.10193e-8，26—50约4.46933e-4，51—100约7.04675e-5。M8未知修正的Cartesian带宽到约25，26以上是明显的未投影速度；完整reference lift自身并非带限，故这支持扩大未知场表示，不能称作严格M8不存在。

在材料θ中4—25壳仍可大到3.02e-4：moving chart的ρ最小采样值.52会混合频率。相同节点R在512→1024的差0，固定mean与高角网格mean的差最多2.44249e-15；这些不是本次主导缺口。

## 3. 角长度驱动的直接C²核对

直接混合jet所得T·Rθ最大8.99531700854217e-6。DFT导数与其差在512点为7.829403506191665e-8，1024点降到5.575549853763181e-10。完整Rθ向量的大小远高于切向投影，因此把全向量范数直接积分所得约.0043上界会很保守；这不是新的失败标准。所有频谱、节点差与梯形积分均只作诊断。

## 4. 真尾尚未开始，读取错误原因再修

corrector-actual-00/run.json返回RuntimeError('Weighted stage-tail initialization failed')，无raw终态、actual_outer_checks或tail_seam。原client在子进程未发出ready首行时就抛此错误，所以**目前没有非线性尾的数学不收敛结论，也没有任何新尾被接受**。外层portable捕捉异常后进程码0不代表solver成功；corrector正确返回accepted=false、exit2。该run SHA256 e008ea386bc02b311dce32c7cfa999ddacb6eab8194e4e7e80857ea2e6dfd603。

接续命令只读保留启动日志与原文件散列，确定具体运行错误；同时用已发布完整lift传递入口准备M12，实际导出同物理tail的12模linear port。保持全部旧q/profile/chart/核心控制，新控制取零，补偿系数为1；该输出仍只是初猜。后续重解的δ/c若变化，属于设计延拓，不是固定全部物理参数的精化证明。

完整小标量及来源另见同日 material-actual-audits-and-tail-start.json。原始输出/全场只留临时runner；新命令、已发布源与hash可复现。

## 5. 原stderr已给出的两种启动原因

随后只读命令 held10-inspect-worker-stderr-01 已实际exit0。corrector的tail_worker_exit.json确认为initialization-eof、returncode1、calls0；stderr指向原native_batch_adapter.mjs对LD_PRELOAD/LD_LIBRARY_PATH的原检查，错误为Unreviewed dynamic-loader overrides。没有实际非线性尾响应。修复在新的子进程环境中移除这两个动态库覆盖项，先用同一Python执行NumPy/SciPy导入；通过后才重新准备原native运行。原manifest检查及全部求解门保留，旧失败目录不覆盖。

M12 exporter的真实错误不同：invalid momentum engine options，原要求N>4*M*spacing。M12、spacing3需要N>144，原尾数值quadrature128不满足。现将导出的数值quadrature升到256，并显式指定同一稀疏Python helper；完整物理tail参数、切口、profile/chart和core仍逐项保持。高M配更多求积点是数值分辨率改变，绝非降低门槛或新物理g。

新命令在material-runtime-retry01下重试原M8真尾，同时在material-lam002-m12-transfer-v2生成同物理图的完整lift初猜。两项都只依实际返回记结果；当前没有预记尾成功或M12新场。原日志及两审计完整JSON的SHA见material-startup-error-record.json，原大输出继续只留runner。
