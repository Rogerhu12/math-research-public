# 真 A 的四个同步 loop/bridge 响应已经算完

作者：strong_amplitude（GPT-6 Astra Pro，AI 辅助），2026-11-14。

修正后的 `strong_20261114_loop_control_response.py` 已实际完成，原
foreground supervisor 记录退出码 0，总时长 1505.47 秒、峰值 RSS
511896 KiB。计算保持真 A 的全部 2590 节点、97 状态、32 核心未知量、
1280 角前缀规则、原材料图和完整已存非线性尾高度 $H$ 及其导数。
没有运行新尾求解或接受新曲面。

新控制为 `loop_curvature`、`loop_radius`、`loop_speed`、
`terminal_peak_fraction`。每次扰动都同步改变 prefix 和有限终端桥，
真实 infinite-tail cut 的其它全部键和物理参数保持相同。实际复算
了前三原控制及 frontload 列作同一完整线性系统内的交换。

| 控制 | 全步/半步响应相对差 | 方程相对后向误差 |
| --- | ---: | ---: |
| loop curvature | $7.5991\times10^{-9}$ | $1.0907\times10^{-15}$ |
| loop radius | $6.9300\times10^{-9}$ | $1.1920\times10^{-15}$ |
| loop speed | $9.4177\times10^{-7}$ | $8.1447\times10^{-16}$ |
| terminal peak fraction | $1.53035\times10^{-4}$ | $2.3518\times10^{-16}$ |

最后一列接近原有 $2\times10^{-4}$ 门，但实际通过；不能把它描述为
与前三列一样稳定。所有原全半步及完整矩阵残差门均保留。这些浮点
后向误差不是区间逆矩阵证明，也不证明有限步的有效性。

新算的 delta、boost length、boost speed 全场响应与已归档同 A
对应方向的物理单位最大相对差分别为
$1.9302\times10^{-14}$、$6.4923\times10^{-14}$、
$2.0584\times10^{-14}$。因此将原九方向与四个新 core-held 方向组成
同点的十三方向初猜集合；没有把别的接受点的导数搬来混用。

新的回环曲率方向在保持前三核心系数时，需要的
$(\delta,L_B,v_p)$ 一阶变化约为
$(-3.7484\times10^{-4},7.5179\times10^{-4},1.4559\times10^{-4})$。
它对保留全部 32 模的核心轴差导数仅约
$-4.09\times10^{-7}$，因此可以接近独立地调节回环几何。这个局部
数值事实是继续真实增幅的输入，不是完成标准。

## 最小可运行归档

`2026-11-14-strong-resume-thirteen-control-response-r1.json` 只引用
实际 LP/非线性初猜需要的全部 13 个完整 $dy/dp$ 数组：原九方向
保留旧 notes 中的字节，新四个 core-held 方向复制到本次日期前缀。
另归档三件新 primary 数组用于上述同点比较。新增数组合计
13645620 字节，均为原 gzip 字节，单件小于 5 MB。

原始完整小摘要、运行退出记录和并行记录分别存为
`2026-11-14-strong-resume-loop-response-r3-full-summary.json`、
`...-resource.json`、`...-parallel.json`。
`...-archive.json` 明确列出 **33 个未归档的可生成派生数组**，包括
forcing、半步方向及未使用方向；J/QR 也未归档。这不是完整原始目录的
归档。完整源、原 argv、每件原 SHA 和重新生成规则均保留，必需的
十三个初猜方向已经逐件实际读回校验。

下一长非线性计算按根 README 新增规则 14 提交公开 runner；先用
本次十三方向的小网格 LP 选定有限初猜，再运行原全 H 耦合 BVP 和
最终物理审计。没有放松原 RMS、真实边界或尾审计要求。
