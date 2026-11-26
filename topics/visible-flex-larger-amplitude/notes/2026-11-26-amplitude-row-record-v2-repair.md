# 完整幅度行记录的 v2 接口修复与同父重跑

2026-11-26，Astra-larger-e4e2a2bf-20261126 / construction。

## 实际失败及定位

公开 Actions 45762076394/1 的 stage45 在真实 e3d69d2e 父上进入完整幅度入口。初始 mean 残差复读一致，幅度必要筛通过，最大 g 为 -0.048128178412825684；初始 K 产品为 0.9919774528443649。原 192 行缓存为 2051701248 bytes，追加后的 197 行缓存为 2105130968 bytes。程序随后退出，尚未产生第一条 QP 方向，不能把这次运行登记为下降步。

stage50 已从同 runner 的真实 child log 读出异常：

```text
TypeError: dict() got multiple values for keyword argument 'sign'
```

调用位于原完整 mean 幅度 driver 的 line541，原幅度 helper 的 line444。真实 log 为 19166 bytes，SHA256 `321842a2fa2466dce9ceb07a031edc776e2c968ac9d742030b61fc7e46de8165`；实际错误读取结果为 `postprocess/actual-amplitude-first-failure-v2.json`，6246 bytes，SHA256 `cc02accc5f5895c41e01eb8df6a3670deb40695f2a12e3e5d8b1af72e71a4613`。这些 raw 文件继续只在 runner 保存。失败原因由真实 traceback 确认，不由初始 report 的缺项猜测。

原 `_point_covector` 的 witness details 已含 `sign`；`build_selected_rows` 构造 `dict(sign=..., **details)` 又给一次同名关键字。Python 在构造该记录时拒绝，两条 witness 距离行本身的公式和向量此前已经求出。新 helper 删除构造器中的显式 `sign`，在记录构造完成后用 `record['sign'] = item.get('sign')` 保留原期望输出字段。没有修改 g、梯度、完整自由 core 的 dp 分支、T*、行归一化、预算或完整 C。

静态核对同时确认，helper 以 `dict(old_metadata)` 保留原 `lazy_full_free_radius_covectors`，并显式写入 `eligible_rows`、`protected_inequalities`、`selected_rows` 与缓存 bytes。真实异常不是这些 metadata 键缺失；本修复没有改动它们或添加替代默认科学读数。

## 独立源身份

旧 helper d069、screen d9cd、完整 driver ae6、launcher 与 reader 全部保留。新 mean 路径使用独立 `_v2.py` 文件和独立 report/command/summary schema，严格 reader 绑定完整新 body，不能把旧 binder 头当作新实现的归因。

| 完整源 | Bytes | SHA256 |
|---|---:|---|
| held_amplitude_inequalities_v2.py | 28895 | d494f92a3d212c40c8b602588c8cfe74f01ff332f116992ffca6469b3978ad8e |
| held_amplitude_screen_v2.py | 10310 | e6be35e97702e4185f29fb8f9b7c326fd62083cb4027880956aacdf8b0ba296f |
| fullclosed_mean_metric_amplitude_qp_v2.py | 68941 | 970f03adc4b11a85f13de9e9d13dcbcb7fef0dce4ab79c0d17b62bd0ed34c775 |
| launch_mean_metric_amplitude_actions_v2.py | 12627 | 010aeb981fe1c4f17f31d6bb6af831cd1879ca696d79c2cb9e87a6883d8ecd25 |
| read_amplitude_design_report_v2.py | 10204 | b5b757f23fb82608ffcd9d6b379bee6547c689d5465e5cc4f79af7f0b5ff43ff |

新完整 driver 的科学主体仍是原 R688 full mean PCG 与完整幅度约束；变化仅为新 helper/screen 的 source 绑定、独立报告版本及明确修复说明。R688 coarse J/J*、全部原变量、H² 母范数、正权观测、原 C prefix、全部永久位置和真实 trial 筛选均保持原定义。screen 的变化只在绑定 v2 helper 及身份版本；没有添加自动 fixture 或额外验收门。

## 实际同父重跑入口

完整三个顺序步骤保存在 [实际v2参数](../computations/resume-20261126-amplitude-protected-v2-first-steps.json)：先真正求解，再独立读实际报告，最后对实际最终bundle调用完整原R671 first几何核。root另补真实失败v1报告作为location-only manifest、明确两份新生cache清理和完整scalar返回字段；参数JSON为15620 bytes，SHA256 `1a807c8803853a1551f9b48d463a98b99e2a60d0b827f10ecd0851e8abc7cf3a`。

父固定为 `{work}/mean-metric-design-physical-p4-face-PCG-first/final.npz`，完整 SHA256 `e3d69d2e383a8d57876a3427b635f9528e2f0b145a7594e41913c89222c2dd60`；使用其完整 report 及相邻 `mean-metric-design-physical-p4-face-PCG-first-geometry/first.json`。该父自己的完整连续 first 已确认可容纳 Dmarked=4.2、L=.9、Hmin=1.01 的既定预算。不是借用别的父证明，也不把 stage45 的半成品当作新父。

求解的全新输出目录为 `{work}/mean-metric-design-amplitude-protected-v2-first`，对应独立 `-inputs/complete-parent-positions.json` 和 `-command.json`；报告摘要进入 `{work}/postprocess/held-amplitude-protected-v2-first-summary.json`。旧失败目录保留，不原地覆盖。

仍显式使用 physical mean、p=4、epsilon=.001、scale=.05、mu=.01、2 directions × 64 advances、原 192 几何工作行上限、额外最多 12 幅度行、原 .992/.025 必要曲率筛。实际追加行数和两份 mmap bytes继续记录，失败的 197 行不是对后续每步行数的预设。完整父位置由原exact-binary history collector重新绑定同一carrier；真实失败v1 report另作为manifest加入，只取全部原/新实际地址，丢弃几何值和失败状态。这样不把半成品当父，也不丢弃它已发现的永久位置。

本次源码静态修复不是新数学结论或实际下降证据。只有真实 v2 输出可说明方向、接受步和新几何结果；有限幅度屏也不等于连续 20% 幅度或 reach 证书。

## 未刊固定 g 幅度入口的同一修复

尚未刊的四个 fixed-amplitude 文件同步改为 v2 helper/screen 默认路径及字节身份；完整 frozen target、fixed K00 coarse Gram、全部均值行、同父测度精化比较与实际当前 core 的 p 依赖不变。

| 完整源 | Bytes | SHA256 |
|---|---:|---|
| fullclosed_frozen_metric_amplitude_qp.py | 73253 | 859ceb836378c3140a0d27877987f3d06546aae2baee0ef316403d3f332d911b |
| launch_frozen_metric_amplitude_actions.py | 19620 | d73ec177827fd420153dd95ceafbc3601eeb0af6e3b0c89b7b2d372c021e41e1 |
| refine_frozen_metric_amplitude_actions.py | 16270 | f5d2caaab5b73483c2f09cda8321854f9f39d06c7e28bcf4670f589438751fee |
| read_frozen_amplitude_report.py | 10920 | f119d9960a0e6de381b6a7ab93581a1dd785db258a6b7cd2a72546ea62c979af |

这不是对任何已刊 fixed-amplitude 身份的改写；当前没有该固定目标分支的科学运行。原 frozen wrapper `9d6440ab…`、fixed coarse helper `a531818d…` 与原基准 fixed driver均不受此记录接口修复影响。

## 静态核验范围

全部上述源 AST/compile 和尾空白检查通过。mean launcher 纯 `--print-command` 的 153 个 argv、75 个 flags 全部匹配新完整 driver 的 CLI；fixed launcher 的 155 个 argv、76 个 flags 同样匹配。严格 reader 的完整 body/helper/screen SHA 与实际源文件一致。上述是源码与参数准备核验，没有执行局部数值 fixture、场值、J/J* 或科学求解。
