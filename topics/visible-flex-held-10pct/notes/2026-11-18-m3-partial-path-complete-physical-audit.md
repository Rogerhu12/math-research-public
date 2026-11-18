# 部分圆化路径：原物理多项式与两个真实高度响应的完整后处理

## 1. 完整有限终态

在前条已保存物理 quintic 上，原完整前缀 audit 与原实际接缝 audit
均已真实返回。本次不重新求解 inner、不重新生成 C² 插值、不启动尾
worker；原493点内层解、全部参数、七个物理控制及保存的物理系数块
保持不变。

原前缀有限 FFT metric 为
$1.9786688260610694\times10^{-6}$，Darboux 指标为
$0.0016485800156731678$。真实物理端点尾残差为
$1.833931450579216\times10^{-9}$，通过原 $2\times10^{-9}$ 门。
这补齐了一个**完整记录的有限 $\lambda=0.02$ 终态**；metric 仍大于
$10^{-6}$，不将原 solver/BC/尾的接受改称更严格完整 metric 门已过。

本条属于同伦中的新物理设计结果，未声称固定 $g$ 精化、连续角误差、
完整闭面、精确圆弧或 10% 持握。中间 $\lambda$ 的定义本来就不将
有限 inlet 宣称为精确核心曲线；不能从本条数值领取 $\lambda=1$ 的
几何预算。

## 2. 两个真实响应的准确分派

前条物理端点求值改变了四个 binary64 高度末位。m3 的独立原生执行
`84464` 已对这个**实际物理端点高度**取得完整原门接受，原生记录为
`24dd350f7f0ec440122b369841d2c03cf75e968f3e89a04de1ed44f95d389ffe`。
其初值保留旧接受态的全部内部/深端状态与切口动量，仅按原
JavaScript $H/r^4$ 更新切口 Dirichlet 值；此接受来源另条登记。

原 `adaptive.audit` 的末尾 `physical_bc_max` 用原节点 `physical.y`，
因此查询的是原节点高度；原 `seam_audit` 则用保存的物理 quintic
在终点求值。新后处理保留这两个不同查询：

|原调用|实际输入高度来源|真实接受响应|本次查询数|
|---|---|---|---:|
|前缀 `physical_bc_max`|原 raw inner 的末节点|`d65514e…`|1|
|完整 `seam_audit`|原物理 quintic 的末点求值|`24dd350…`|1|

只在全部八个 binary64 高度字节匹配时返回对应的真实完整
Jacobian/audit 响应；未知高度立即报错。没有高度钳制、近邻替代、
affine 延拓或额外原生求解。两份响应分别原字节复制到新输出目录，
接缝引用 `seed_tail_0000.json.gz`，尾调用数0明确表示本次没有新调用。
实际 `tail_config` 保留真实响应的执行配置；原恢复进程的 active IO
元数据移动到 `prior_resume_worker_metadata`，不伪称本次有 worker。

## 3. 原有限图及原后处理没有改变

`finish_m3_trace_path_physical.py` 用原 source reader 恢复同一模型，
用原 `load_checkpoint` 解码保存的完整物理 quintic；不再调用
`c2_interpolant`。物理节点值来自真正保存的 raw `y`，不是把多项式
节点求值重新标成原 solver 状态。原 normalized cubic、物理 quintic
和原 node tuple 的身份保持区分。

物理系数块在新目录的压缩字节 SHA 仍为
`fe0fb7a590023c62fc7d65c3247ad0adfd4bc3a3b249c973a0291c70659ec189`。
原全部参数保持，其中 $p_0=-1.3637752370752413\times10^{-10}$，
只从 base profile 的 $\delta$ 加一次。

- 数值 gauge / 原 warp：`0.06` / `0.06`。
- 定义主核支撑幅值：`0.059818741459951905`。
- $\lambda$ / partial lift：`0.02` / `0.02`，窗口 $(0.5,0.9)$。
- 主保护半宽 / 主过渡 / 控制过渡：`0.21` / `0.32` / `0.4`。
- base $\delta$：`0.06104275721220832`；物理
  $\delta$：`0.0610427570758308`。
- 实际物理 meridian 长度：`1.36025241231913`。
- M8，25状态；原尾 parts16/RK16/N128/depth8 与原门全部保留。

仍调用原 `adaptive.audit(obj,physical,512)` 和原
`obj.seam_audit(physical)`。平均高度由这份真实 partial-lift flow 的
原 `height_integral` 计算，512角、每段六点求积，没有拷贝旧均值。
每项完整 audit 一返回立即按原 CP 格式保存；只有完整保存后才进入
下一项，因此接缝失败不会再遮蔽已经返回的 metric 数值。

## 4. 原 audit 的完整标量

前缀本次使用1134个径向取样点和512角。表中均为原有限读数，
不扩大为全域严格上/下界。

|量|实际值|
|---|---:|
|metric FFT $\ell^1$|$1.9786688260610694\times10^{-6}$|
|Darboux 指标|0.0016485800156731678|
|flow defect|$8.894983978207411\times10^{-6}$|
|物理 BC|$6.850787654316204\times10^{-16}$|
|原 inner 最大 RMS|$9.873637694422844\times10^{-7}$|
|原 outer0 实际 BC|$3.425393827158102\times10^{-14}$|
|样本 Frenet 最小余量|0.002484955971123859|
|样本曲率峰|9.410697476835391|
|最大水平半径 / 高度绝对值|1.090189053663974 / 0.7826775541518115|
|真实物理端点尾残差|$1.833931450579216\times10^{-9}$|
|mean 一阶接缝差|$2.9879146379307997\times10^{-10}$|
|mean 二阶接缝差|$-6.978953415170963\times10^{-9}$|
|非均值一阶 / 二阶接缝差|$7.160071147094271\times10^{-16}$ / $1.29164515619927\times10^{-7}$|
|cut metric / cut C¹ metric|$8.444548190606823\times10^{-8}$ / $1.7903532378011616\times10^{-6}$|

保存的原 audit **没有 metric 的主导 E/F/G 分量、径向 argmax 或主导
角频率**：原函数仅将最大有限 $\ell^1$ 标量累计到 `metric_l1`。
本条不从该标量推断位置，也不为补位置重算整图。
另存的 inlet `unlifted_projection.metric_l1=7.20796651244889e-8`
仅是未 lift 的有限投影诊断，不能改称当前实际 partial inlet 的
metric 或全域主峰来源。

## 5. 执行、可复现来源与后续入口

冻结执行源 SHA：
`53222150e078a94ea0ff01a36db1e52f95d949777d15f775c04cb04b8449db3e`。
launch plan SHA：
`58e5587799ba3314402a445411748ad05e74cb825c02dd26b5a990d591fac932`。
元数据准备 `01e648` 真 exit0，绑定113个定义/执行源；没有方程评估。

唯一 observer `17021`，入口 chunk `130b6a`；2026-11-18
03:49:42 UTC 观察到真实 child exit0。实际后处理3.905091秒，
observer6.014423秒。新 inner 数、新原生尾数、新 C² 插值数均为0。
原完整 audit 的两次真实查询及三个及时保存阶段全部记录。

最终 CP：
`closed_work/m3-trace-path-physical-finish-v1/seed.json.gz`，SHA
`fd93d3f088038830f9291356acbd4ef997cb912cd345570a0f18c1b5fe574596`。
原物理块、两真实响应、全参数/尺度/控制/profile/chart/port 定义及
执行来源在
`scripts/resume_closed/m3_trace_path_physical_finish_terminal.json`
绑定，完整大数组不加入 Git。

只读收集器执行 `6919cd` 真 exit0、0.106359秒；复核113源、原物理
图/原节点/全参数未改、全部系数块、两响应及原门完整来源，并实际
通过原 `m3_trace_path_prefix.bind_checkpoint` 的完整终态身份检查。
该步骤没有构造模型或重算任何 metric、mean、Jacobian 或尾。

后续改变 $\lambda$ 是新的同伦设计。继续时应继承完整原状态和
`path_base_profile+p_0`，明确旧场来自 raw 节点还是物理 quintic；
两者在 cut 的实际 binary64 高度不同，必须选对应真实尾锚。
不得使用旧 `ratio**j` 幅值缩放或将新增模式的控制槽静默改序。
