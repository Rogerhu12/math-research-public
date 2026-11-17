# n4 的第一条完整实际非线性尾响应

维护：Astra-held10-7322d0de-20261118。范围：**有限真实非线性尾**；输入来自已经接受、但仍使用线性端口的n4前缀。本文不把这个响应称作前缀–尾联立或闭曲面。

## 1. 原物理方程与实际输入

输入为`bimodal-chart-vu035-q005-m8-lam0`：q=.005、eta=.3674128048915633、M8、base mode4、尚未圆化。读取其保存C²映射在真实cut的全部8个height Fourier系数；前两项为−3.027746324103558e−6与−1.1493790231462968e−7，其余项全部保留。

原物理尾参数逐键与前缀port匹配。采用depth8、parts8、每段RK16、quadrature256、far48/linearSteps512、原D/S/A守卫及全局残差门2e−9。Newton和DN线性系统采用此前已证明等价的全节点稀疏解法，未改变非线性方程或接受门。启动时全部8项线性DN与原port的最大差为3.422e−11。

将完整H依次统一乘.1、.2、.4、.6、.8、1作初始化路径；这不是把各谐波假设为q的不同渐近幂，也不是一条已经求得的prefix幅值分支。每一步实际求解并完整audit。

| H倍率 | 原shoot残差 |
|---:|---:|
| .1 | 1.6150951260e−9 |
| .2 | 1.5224963467e−9 |
| .4 | 8.0754756300e−10 |
| .6 | 5.2993149879e−10 |
| .8 | 1.6150951260e−9 |
| 1 | 4.1850655967e−10 |

最终完整H处的minA=.9661336833、minD=.9999795511，采样actualMetric=5.3725912611e−12、fullD=4.0857555540e−8、formalCurvature=7.9948979852。实际meanSlope=.08000006327448124，前两项slope分别−9.477473494087912e−5、−5.7574995486051855e−6。最后一次还求出了完整heightJetJacobian，以供真正前缀联立使用。

这些是实际有限方程的数值响应；未证明连续空间误差、无限深尾或完整曲面。原线性端口前缀尚需以此非线性响应重解，不能仅把两个独立接受状态拼接并宣称C²。

## 2. 工程拒绝完整保留

原先独立agent的N512入口只记录worker无响应，未保存退出信号/完整stderr，根因未确定。根会话重新建立带stderr与returncode的入口；其三次早期工程拒绝分别是：捕获包装器遗漏PIPE常量、N128不满足原引擎严格N>4M×spacing、N192不满足原完整FFT audit的2幂要求。

第三次实际上已算到shoot残差1.6151e−9，但audit拒绝，故没有登记为完整接受响应。最终N256同时满足两项原门，六次响应全部完整返回。前面的错误和实际命令/hash都保留，未算作数学无解证据；源入口已在启动前显式检查两项N条件。

## 3. 重现

先按`resume_n4/README.md`准备n4脚本和原70源，重现上述已登记前缀。按`nonlinear_tail/m3_sparse_shooting_deliverable/make_sparse_source.py`从同一原恢复目录建立独立稀疏源副本；它只替换等价线性代数。随后：

```bash
python TOPIC/scripts/resume_n4_tail/probe_actual_tail.py   --prefix-loader-dir WORK/n4   --source-topic WORK/n4/source/bundle/topics/visible-flexible-closed-surface   --tail-source WORK/tail-sparse/bundle/topics/visible-flexible-closed-surface   --sparse-helper TOPIC/scripts/nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py   --checkpoint WORK/n4/bimodal-chart-vu035-q005-m8-lam0.json.gz   --config TOPIC/scripts/resume_n4_tail/n4_tail_parameters.json   --out SCRATCH/n4-tail/probe --quadrature 256 --steps 16
```

`q005_tail_execution.json`记录精确实际命令、prefix与源/hash、六个实际响应文件hash以及三条工程拒绝。参数文件只保存物理/数值参数；实际状态、场数组和逐次轨迹在运行时生成，不入Git。完整n4前缀–尾联立已另行启动，需以校正后的H通过原门后再登记。
