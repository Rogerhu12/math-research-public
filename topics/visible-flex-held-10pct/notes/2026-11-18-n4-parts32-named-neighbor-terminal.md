# n4：parts32 唯一具名邻点后，原完整 DN 仍未通过

维护：Astra-held10-7322d0de-20261118 / n4_round_core；2026-11-18（UTC+8）。

状态：**已完成的原门失败终态**。本次只把预先指定的一个内部初值移到
相邻 binary64 数，再调用既有完整 DN 求解器。两条局部匹配行通过原门，
但全局仍有其他超门行；原 Newton 接受一次修正后，线搜索再次失败。
没有接受的 $0.5H$ 尾，没有发起完整 $H$ 或联立前缀求解。

## 唯一初值及保持的对象

输入是[parts32 原失败态](2026-11-18-n4-halfheight-parts32-terminal.md)，
SHA-256 `cb60dce0d09db2484e1914ba7149fc9495e6824d6dcc6d8441f68133663d24d3`。
[两原路径一致及具名单行诊断](2026-11-18-n4-parts32-map-consistency-and-one-ulp-peak.md)
已确定 node 175 / component 20，即 mode 4 动量的原 flow 值。

直接使用未修改的 `scripts/resume_m3/try_recorded_tail_neighbor.mjs`，
SHA-256 `8735d7b874975140bf92a9ec646420067f25f60c3acd0ecd72c2b2efc9336fa9`。
唯一初始化变化为

$$
-6.122429682261514\longmapsto-6.122429682261515,
$$

差为 $-8.881784197001252\times10^{-16}$。
对这一实际数值，`nextafter(old,new)==new`，确为负向一个相邻数；
没有把绝对 ULP 比例判据推广到二幂边界的非对称邻距。

两端边界节点在初始化时不变。完整 config 及 20 个物理 cut-height
分量按 binary64 身份保持；全部 height 的 little-endian Float64 SHA-256 为
`411ec0ff8775c34ce1106b1afa72ded610646a54384bb05dbb71afbbfd0ff70a`。
实际源仍为同一 shared/periodic 实现，M20、spacing 4、N512、depth 8、
parts32、RK16、audit RK32、maxIterations36，原停止门为 $2\times10^{-9}$。
没有另扫外部 $\alpha/\beta$ 候选，也没有改原 Newton 的线搜索。

## 局部检查与完整求解的区别

| 原匹配行 | 初始化前归一残差 | 初始化后归一残差 |
|---|---:|---:|
| stage 174 | $4.713435966625131\times10^{-10}$ | $2.3567179833125656\times10^{-10}$ |
| stage 175 | $1.5211857880292614\times10^{-8}$ | $9.507411175182884\times10^{-10}$ |

随后进入原完整残差与 Jacobian 路径，实际记录为：

| 原完整求解阶段 | 全局归一残差 |
|---|---:|
| iteration 0，唯一邻点初值的完整重放 | $9.783174511407431\times10^{-9}$ |
| iteration 1，原 Newton 已取一步 | $7.429289420154656\times10^{-9}$ |

原求解器在后一值报告 `multiple-shooting line search failed`。
最后完整求值的 `minA=.980752332821046`、
`minD=.9999448760732821`。正的这些数值不替代残差门。
局部两行均合格仍不足以得到全局接受；本次也没有返回收敛尾的
height-jet Jacobian 和完整 audit。

初值只改一个坐标，但最终失败态经过了原 Newton。
不把最终保存状态称为只有一个坐标变化，不把它当作接受态续接完整 $H$。

## 真实退出、保存与范围

执行句柄 65373，observer 于 `2026-11-18 00:23:22 UTC` 记录真实退出码 0，
耗时 $857.071196$ 秒。既有工具捕获原数学失败并保存记录，所以退出码 0
不是数学成功。采样 namespace RSS 峰为 961084 KiB，
`RUSAGE_CHILDREN` 的 `ru_maxrss` 为 960096 KiB；二者各按原语义记载，
不称为整机或全部进程树的峰值。

完整失败态 `one-ulp-tail.json.gz` 的 SHA-256 为
`b4356eabf97014127a364ef34b7951a930f4b184d8c6f4c4db83c161b2cbbb5e`，
保存在 `n4_work/raw-primaryb016-lam002-actual-m20-parts32-v1/`。
新增 `record_named_tail_neighbor.py` 只读取已完成的状态、日志和来源，
核对真实邻数、两条受影响行、全参数/全 $H$ 身份及原返回结果；不重跑数学。
紧凑记录为
[`raw_primaryb016_lam002_m20_parts32_neighbor_terminal.json`](../scripts/resume_n4_tail/raw_primaryb016_lam002_m20_parts32_neighbor_terminal.json)。

后续只读定位针对这个新失败态的主导行，再决定有依据的单一变化。
此前两个初值 screen 和这次原 DN 终态均不重复运行。
本条不证明数学不存在性、幅值上限、精确圆弧、闭合族或握持比例。
