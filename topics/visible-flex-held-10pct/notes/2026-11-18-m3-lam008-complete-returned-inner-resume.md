# λ=.08：沿用通用恢复器完成原物理审计

**类别：数值证据。** 原 R45 同伦的 M8、25 状态、全部七控制在 $\lambda=.08$ 得到完整有限终态。原内解与两种实际高度尾均通过各自原门；前缀有限 FFT metric 为 $3.329530742646296\times10^{-5}$，仍超最终要求。后续继续同伦，不把这个有限状态称为精确圆弧、闭面或固定 $g$ 精化。

## 1. 原返回内解与复用的真实尾

原运行 `92146` 的目录是 `m3_work/trace-path-lam008-coupled-v1/`。原 `inner-00-returned.json.gz` 的 SHA-256 为
`936f8bdd0615c7905b560a1942a67d4830721573d07c3fa930ced3f9ce66a310`，sidecar 为
`04b605175a4fbd4066ae08de9330da4ac3212ab2654ce803bed51d27eb2bbd4f`。它实际在一张 493 节点网格返回成功，最大 RMS $9.87469885365366\times10^{-7}$；原 Newton 统计是 **3 个全步**，无 domain/merit 拒绝，不能用快照文件的序号代替步数。

新节点高度的原尾随后失败于 $3.6678627560762796\times10^{-9}$。该记录 SHA-256 为
`c0b60dd59c64f76f34e76dce9722a50e97336d0ebf6805adc3fbef5b16f08b3b`。
另一次已记录的完整行定位及唯一两邻数初值经过原 native 求解器真正接受；这里复用其完整响应，不重做该计算。真实接受记录位于
`m3_work/trace-path-lam008-native-neighbors-v1/seed_tail_0001.json.gz`，SHA-256
`a13ee1e9df74a3c6c756ff27eb2565ea2e773f329d3dc130457a82e7f6b442fd`，实际运行 `89030` 于 04:22:13 UTC 退出 0，残差
$1.8339313780381398\times10^{-9}$，208 个有限 Jacobian 标量与完整 audit 返回。

## 2. 本次接续没有修改已执行的源

完全沿用 [λ=.04 的通用恢复接口](2026-11-18-m3-lam004-returned-inner-complete-resume.md)：

- `m3_trace_path_pending_inner.py`：`203fb3c82d7377794b089b6acf79017b1c984036be0ea2451f995405cedba3f0`。
- `resume_m3_trace_path_pending_v2.py`：`aa146dd6a68cbc22ee89ab684a6ef30d5a67dac44bff8b97613dd3aa845f29ae`。
- `record_m3_trace_path_pending_resume.py`：`fef31ad83cbe8536aee1564b227b9cb32fb1f720e19ba128c33ca38648ad1508`。

纯元数据绑定 `97f0c2` 退出 0；准备 `1b8359` 退出 0，绑定 119 个源。计划位于
`closed_work/m3-trace-path-lam008-resume-v1/launch-plan.json`，SHA-256
`1be99d1e57f08fcd9a3486c53105914603dd60ebfc3379ff5acec881921043b4`。
真实 observer 为 `44382`，启动 `8aef10`、终态 `c729fb`，2026-11-18 04:23:31 UTC 退出 0，观察时间 50.05643326899735 秒；原 worker 退出 0。

字面恢复原 raw 的完整 $x,y,p$、cubic 和逐区间 RMS。原 outer 0 的实际 BC 残差为 $6.162117431918776\times10^{-11}$，因此没有重跑 inner，也没有开始 inner 1。原八轮总预算没有重置。同节点高度使用上述真正接受响应；原 physical quintic、完整前缀审计和 mean 使用当前实际模型计算，完整前缀审计在 seam 之前立即保存。

原 gauge、warp 和七尺度保持 `.06` 口径，当前定义核幅度为 `.05928147775446849`；实际 profile 为原 base 加完整 $p_0$ 一次，最终 $\delta=.06104275291867738$。partial lift 窗仍是原 `(.5,.9)`，主半宽/过渡宽/控制过渡宽仍 `.21/.32/.4`。所有八参数和七物理控制、chart/port/尾物理参数身份均在本次执行记录中。

## 3. 真正的 physical-endpoint 高度和原接缝

物理 quintic 端点高度不同于原节点高度。零基分量 $3,5,6,7$ 的有符号 binary64 邻数步数分别为 $+6,+1,+4,-1$；其余分量逐位相同。没有替换为旧高度，原 worker 实际接受了这个新的完整向量：迭代 0 残差
$1.8339313780381398\times10^{-9}$，208 个有限 Jacobian 标量和完整 audit 返回。

因此本次新增 inner 为 **0**，新增 native 尾请求为 **1**。新接缝尾文件 SHA-256 为
`c8e5e42a6e40a8a029cb260bfac5b4a906aab71d29443dc22eb5428bafe299b1`。

| 原审计量 | 保存值 |
|---|---:|
| prefix metric，有限 FFT $\ell^1$ | $3.329530742646296\times10^{-5}$ |
| Cartesian Darboux 张量有限值 | $.027331801353401273$ |
| flow defect | $.00015414415522540406$ |
| physical BC | $5.797510464152541\times10^{-14}$ |
| mean 一阶接缝差 | $6.75151511086991\times10^{-9}$ |
| mean 二阶接缝差 | $-1.57758951901954\times10^{-7}$ |
| nonmean 一阶接缝最大差 | $5.800481622797449\times10^{-14}$ |
| nonmean 二阶接缝最大差 | $4.766888583281745\times10^{-7}$ |
| cut metric，有限 FFT $\ell^1$ | $1.0934892015530084\times10^{-6}$ |
| cut metric 一阶差，有限 FFT $\ell^1$ | $2.3683600605521822\times10^{-5}$ |
| 原尾 audit metric | $4.6243962659175963\times10^{-8}$ |

前缀使用原 1134 个径向样本和 512 个角样本。原程序没有记录最坏 metric 分量/位置；此处没有重算来补一个假定峰。`unlifted_projection` 仍仅表示未 lift 的投影诊断。

## 4. 输出与下一步的身份边界

执行目录中的最终文件：

- `seed.json.gz`：`f4abafcac2a0e7a729a085b3462686197245d5dde60fd087e77aa8f9afd6581c`。
- `seed_coeff_00.npy.gz`：`c73ae60261180a7e3c15832a95f2201b9ee1ae096c75fdd460b369d4405d2e23`。
- `seed-summary.json`：`85a0acceeceb905d2be55331e61d080efe5cf9fe25f1edf4ac7b696a1417064d`。

只读 collector `5e5690` 退出 0，.120992676 秒；未构造模型或重算方程。紧凑记录为 `scripts/resume_closed/m3_trace_path_lam008_resume_terminal.json`，SHA-256
`6969b1cb62292a5b4f5b7aaeedb6626dd4a2117d73170938ff3082e94e58077d`。
原数组和完整审计保留在 scratch，Git 只放源、必要参数和哈希。

后续可由这一真实 physical checkpoint 继续同伦，继承全部参数并区分 raw cubic 与 physical quintic。当前增加 $\lambda$ 及重新求解 $\delta$/控制是设计变化，尚不是同一固定完整 $g$ 的精化；本结果不领取 R46 的圆弧握持比例，也不说明最终 metric 已经通过。
