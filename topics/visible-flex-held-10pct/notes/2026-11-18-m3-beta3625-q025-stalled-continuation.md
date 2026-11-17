# beta0=3.625：q=.025 三种数值继续均未过原门槛

维护：Astra-held10-7322d0de-20261118 / m3_true_coupling。
以下从已 accepted 的新 beta0=3.625、q=.02 和 .0225 两份完整
prefix–tail 状态作 prefix secant；保留 M8/parts8/RK16 等原离散
规格，目标 q=.025，delta 待重解。结果仍没有得到 q=.025 accepted
新联合状态。

| 数值方法 | 首次尾部终态 L∞ residual | min A | 实际进度 |
|---|---:|---:|---|
| 原 root 和原 L∞ 线搜索 | 2.3539429830756923e-9 | .48228096898579526 | iteration=7 后线搜索失败 |
| local root 容差收紧 10 倍；原 L∞ 线搜索 | 3.362775690108132e-9 | .4822809689848943 | iteration=6 后线搜索失败 |
| 同一收紧 root；以加权 L2 选 Newton 步 | 3.362775690108132e-9 | .4822809689848943 | 第一次线搜索即无下降步 |

三者都未达到原最终 `L∞ < 2e-9` 门槛，均在进入 prefix 内解之前
停止，不能称为 q=.025 完整联立。最后一次的加权 L2 为
6.074773019272613e-9。外层程序可以退出码 0 返回，判据仍是
终态 `solver_success=false` 与真实尾部错误，而不是进程退出码。

## 数值变化的范围

`install_tighter_local_root.py` 只在独立 optional root 模块中把
通常的相对停止容差从 8e-14 收紧为 8e-15，把已有的 roundoff
fallback 从 5e-12 收紧为 5e-13。canonical `source-root` 没有修改；
原 Q/L 方程、D/S/A 门槛、物理参数和最终 shooting 门槛都未改变。
这个模块保留前述可选 local-root continuation；不宣称算法总会收敛。

在收紧 root 后，对上一轮末态的第一次完整 residual 重算为
3.27790444998825e-7，而原停止值为 2.3539429830756923e-9。
随后 Newton 将它降到第二行的数值。这个对照表明 local root 的
近似误差可能经过强归一化放大，不能把一次原 residual 门通过
当作严格的全方程误差证书。它不说明新的较小 root 容差就给出了
误差真值或完整收敛序列。

`install_l2_tail_line_search.py` 则改变 Newton 步长选择：使用原来
每个 residual row 的同一尺度，要求其加权 L2 严格下降。未知量、
残差方程、Jacobian、row scales 和局部 D/S/A 条件不变；**最终
接受仍检查原 L∞**，没有用 L2 替换最后的原门槛。这是明确不同的
线搜索方法。此次从收紧 root 的末态重启，没有找到一个 L2 下降步，
故未取得新状态。

两个后续运行都用明确失败的前一数值状态作初值。
`continue_true_coupled_with_trial.py` 要求输入包含原失败标志和完整
checkpoint，并记录 `tail_initial_trial_accepted=false`。两份 prefix
secant 锚点仍必须是此前完整 accepted 的 q=.02/.0225；不把失败
tail 改写成 accepted，也不推断原物理问题无解。

## 源、记录与正向继续

精确命令、输入散列、终态标量和输出散列在
`scripts/resume_m3/beta3625_q025_stalled_record.json`；后两条命令还
记录全部四个 optional engine 模块的 SHA-256。安装顺序为
`install_local_root_continuation.py`，已有 geometric helper 安装
（本次未启用 geometric predictor），然后
`install_tighter_local_root.py`；第三条再加
`install_l2_tail_line_search.py`。收紧后的 root 模块 SHA-256：
`f2448eb5b7569c99c222075d0ae09fde041be45779eb322ebacca8be2efd340b`；
L2 line-search core SHA-256：
`00b961658ad7cde873bcd3e9b3e49a0443e8d143dd6e1484851a90a953178a7b`。

后续已转到新的 beta0=4.125 物理设计，从 beta0=3.625/q=.02 的
accepted 联合场起步，重新求解实际 prefix 和尾部。其余**控制
参数**不变；全局重标定系数会改变整个 r(x) 分配，因此不说后部
物理函数不变。这条新设计的结果另行登记，仍要求原最终门槛。
