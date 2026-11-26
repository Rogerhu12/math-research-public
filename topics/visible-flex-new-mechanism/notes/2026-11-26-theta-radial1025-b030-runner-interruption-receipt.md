# B030 径向1025续接：原始关停和完整已刷回调

日期：2026-11-26。原run45814491221/job139890563243，source ee5dc7af68aacc4e508c0fc6607dc376cc20f815。作业终态后一次读取完整原stdout；没有新执行科学。

原stdout714677 B，SHA25601ec597812a268075c91987c9f30ac493bf5e9ca2fdf98b15b000b95f0f90720，仅scratch /tmp/runlogs/job-139890563243.log保存。实际wrapper7e05899998ff166808caf821091ab2db4abdbfcd3b4923f02b5907d057a35ad1，request154158 B/SHA25601b8a3704a07db2f170066dac02c230a5f284c91cc15cd2abb3570311313f23c，复用a879 checkpoint算子；这是从已识别上轮callback推进的一次新计算。

## 终态与实际改进

11:57:10.3800601 UTC原log明确runner收到shutdown，11:57:10.5362914操作被取消。没有FINAL、FINISHED或自然OptimizeResult，也没有科学clock或容量退出记录。

最近完整THETA_PEAK_CALLBACK_CHECKPOINT为outer0/callback1，UTC11:56:42.9973081；JSON153485 B，SHA2566988077d4e36321de786e80f814b6eddc954e6d3f2a06609d859d7ef04450f9f，与原IDENTITY逐字节核对一致。

本回调接受了一个完整fine+观察角峰均合格的metric候选，eta从输入.26032649730073404降至.25839888496076013，raw几何违约0。保留81q与该完整已接受trial逐项相同，binary64 SHA2567e708ba7a973e8505a81e94073707e8c39504d1f3285253f97e3564382992080。不能把关停后未知的后端位置当作更好末态。

| 状态 | 径向节点 | 显式峰orbit | trust |
|---|---:|---:|---:|
| 原输入/本轮实际 | 539 | 1218 | 1.20135498046875 |
| 完整已刷待采用proposal | 571 | 1276 | 原trust保留、未适配 |
| 新pending | 32个新增径向位置 | 58 | 未优化 |

571仍在已声明1025容量内；峰1276仍在2048内。没有新容量命中证据，不再改cap。1536实际全角/FFT与3072完整fine规则不变；fine为1080×3072。

## 完整回调的几何与角峰

ball最大1.0114938725138363，|y|最大.39260310843325497，主曲率最大16.451983793155406，E_min=.9975955022279087、E_max=3.31426803048484，det_min=.8645634647471048，z_min=.02。

raw归一ball最小.001000001822949792（s=.15,theta0），strip最小.0010022516326585462（s=.6802734375,theta=pi/2），curvature-plus最小.0010355440796038229（s=.75234375,theta=pi/2）；工作几何违约所有组均0。

均匀fine eta=.2583988545212921；完整定位后的metric-plus峰.25839888496076013位于s=.49687499999999996、theta1.310947482953855；metric-minus峰.2582464536748141位于s=.43242187499999996、theta1.3518435108642342。1072个候选均实际完成，3个512批，7289次点目标调用；无未完成括号。完整覆盖只限已观察到的括号，仍无连续角全覆盖证明。

当前后端epigraph=.25820230683842377，实际约束超差.00003774072354251201；uniform/extra已约束metric-minus峰.2582400475619663、metric-plus峰.25821756211701596。当前真实违规参与覆盖判定；本轮immediate exchange0，不能将这条callback臆为又一次重启。

同q嵌套FFT观察：metric分量差2.220446049250313e-15、meanE相对差7.263527952132361e-16、tau曲率差3.0470559408968254e-15；仍非连续Fourier尾证书。

## 实际成本与censored区间

本次完整callback elapsed217.92376114 s；加已记录旧链2635.3438845970004 s，新的科学耗时下界2853.2676457370003 s。其后至shutdown的27.382752 s墙钟单列为未刷工作；旧46.3705572 s未刷墙钟区间继续保留，二者均不并为精确科学elapsed，也不抹为零成本。

本次已完成1个Jac、6个方向块、1916894条硬约束、额外实际点4872，耗时129.229747337 s，数值重构差0。global计数此刻尚未fold当前rows，不能因其complete_jacobians=0就漏掉这次实付Jac。

实际完成2次全fine定位、总2126个候选、6批、14346次点目标调用；1次callback/1次metric接受，outer_started1、outer_completed0、natural_backend0。当前coarse/fine成本仍分开保：
coarse FFT8、point eval18、点参数方向394632、prepare93.966926445 s、point24.025982588999923 s；
fine FFT2、point eval14346、prepare7.016924763000006 s、point36.04061179699821 s。它们没有与已闭外层重复fold。

## 规则拉取与后继身份

public真实pull11:52:54.657389–11:52:54.918090 UTC，ee5dc7a→同SHA，根/题README差异均空。private真实pull11:52:57.771180–11:52:58.689916，9ade7417cdfda5281002286b45620de9595dc13c→同SHA，根规则匹配、本会话QUEUE进行中；私库正文未公开。

下一仅从本次真实81q、全部actual539/1218、全部proposal571/1276以及未适配原trust继续。新的薄恢复器可严格校验原run/job、实际执行wrapper文件hash、原a879算子和完整source-state摘要，避免每次改数学算子；新Jac和新全fine查询仍全部计费，不把原已完成outer或接口核再作为preflight重放。

本收据不授fixed-g加密、连续几何/角覆盖、全pair reach或README完成。
