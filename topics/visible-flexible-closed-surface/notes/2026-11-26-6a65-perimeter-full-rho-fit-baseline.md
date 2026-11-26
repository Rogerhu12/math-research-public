# 自然周长新 g 的完整 rho 拟合与真实 value

日期：2026-11-26。会话：Astra-visible-flex-6a65e705-20261126。

消费[自然周长完整初场](2026-11-26-6a65-geometry-transplant-natural-perimeter-metric.md)：
短前缀 `.06/.05/.02`、右长 `.75`、旧入口 `.18`，保留中央、完整连接和真实
R205 cut/cuff。这里完成的是实际有限全参数模型的初始化及第一次完整值，未完成
等距族，也没有把初始化拟合当作同 g 收敛。

## 完整参数及 g 的身份

`6a65-cauchy-global-position.cjs` 增加明确的 `baseModel=short-cauchy-v1`；
旧长支的默认工厂仍由独立文件定义。新短工厂支持声明的物理长度与斜率。
J=38、K=11、N=128，共 1788 参数，包含全部 theta/phi 正弦与余弦、theta 常数、
高度、rho、切口高度与幅度。配置原样保存在同名前缀的 `-config.json`。

`6a65-cauchy-global-warm-fit.py --fit-radius` 在原全角场拟合之外，以同一个
径向加权矩阵拟合 `a-base.a` 和 `a_s-base.a_s`，物理一阶导数权 `.03`。
rho 放在 `legacyDimension-J:legacyDimension` 的全部 38 列，明确检查系数域 `.4`；
未删除横向误差 F、未覆盖目标数组，未重用旧 normal。

实际 90 径点、128 角，拟合矩阵秩 38，rho 最大系数
`.08995033219836555`，A 和真实 Z 保持 `.8746432018013935/.51`。
最终有限度量是辅助 base 加拟合 rho；它与原始周长的连续定义不是逐点恒等，
必须由该有限模型独立计算残差。当前 g 仍是设计变量，未登记为最后固定 g。

完整目标保留 metric tau `.05` 与已明确另名的曲率 tau `1e6` 启动目标；
R219 全几何 guide、曲率 guide `9.5`、全部角度及全部参数仍在。
两种 slice cache 设为零，仅影响缓存，不改变残差或几何定义。

## 实际退出和数值

参考导出 2.05020 秒、拟合 .16718 秒，均自然 exit 0。
第一次完整 value 在 105.59757 秒收到 SIGKILL（returncode -9），无输出末态；
原因没有证据，不能记成数学拒绝、成功 value 或 LM 结果。

随后以完全相同的输入与源码重试，Node `v24.22.3`、old-space 128 MiB、semi-space
4 MiB；每十秒从真实子进程 `/proc/PID/status` 采集内存，不将 V8 heap 当作 RSS。
本次自然 exit 0，外部耗时 115.05477 秒，程序实际 value 耗时 114.813 秒；
采到最大 VmHWM 88072 KiB、VmRSS 87040 KiB，启动/退出入口源码 SHA 完全相同。

| 真正完整 value | 数值 |
|---|---:|
| 总平方目标 | .9023299957555637 |
| metric 平方目标 | .8547942347517179 |
| 曲率平方目标 | .04751188991286323 |
| 几何平方目标 | .00002387109098258348 |
| metric 行的相对误差峰 | .8850192898225859 |
| 曲率观察行中的相对误差峰 | .8875520451790433 |
| 自己主曲率绝对值峰 | 28.74354738113222 |
| 归一面积平方下界（有限行） | .7822946586284256 |
| 最大原点半径 | 1.4492984370220756 |
| 最大绝对 y | .8283698238320648 |
| 最小 held 见证距离 | .6256578231945371 |

301210 个实际残差行；metric 使用 272 径点，曲率/几何使用 409 径点，65 半角节点
对应 N=128。metric 主峰 `(s,u)=(.2728360367335329,0)` 几乎纯 E 误差；曲率峰
位于 `s=.21684027777777776,u=.44178646691106466`。held guide 违反
`.024342176805462912`。曲率、held 和 metric 均未达到主任务要求，非局部 reach
与连续域余项尚未支付。该过程没有做 normal、没有 LM 接受。

## 可复算原件身份

全部大数组、完整系数状态和实际 stdout 只留 scratch `geometry-work/`。

| 原件 | SHA256 |
|---|---|
| 输入 r137-transplant07-perimeter-samples.npz | 981f7ba60b44bffb27dfdcef8c1be421e29a52f70111cf29128dd5f94dec18fd |
| cauchy-perimeter-fit01-config.json | 967157d268e8465778deac672869ed01cdef90a42b0080401804893378218ad9 |
| cauchy-perimeter-fit01-reference.json | 63e019f4682440c5b00872189f2f5d00124f9b721deb19b3243148d442ab43dd |
| cauchy-perimeter-fit01-state.json | df691036ed80c8b6ca46f46cd41f296bd1bb4e77122f9ad1a419afb041d56998 |
| cauchy-perimeter-fit01-value-monitored-baseline.json | 089f8be803349b00d6caa3ee3450e4ee72fedd9a84bc279baad5fa8d46514f42 |
| 完整位置入口 | 25d0cd8db5444a0629aaa39b26e8287df68ef6f31956c27f10012a9095bffe3b |
| 完整 rho 拟合源码 | 99d2bb06878e2efa89824b9bd1d1b3d9bba7343545e1e99d7af81a00f17c25d9 |
| 独立短标量工厂 | e1029c35bfb820c71a797b16fa644b026e4750a1bfd84e450d5e5a8e3c3d4415 |
| 成功 value stdout | 2962aae1613b36467f0a1679df4bc4c992a6582e1488ed9ecd19c29d36bc9c11 |

复算顺序为短 Cauchy `collect/export`、真实周长导出、按表中物理 s/u 导出 reference、
`--fit-radius`，再对所得完整状态执行 `value`。外部退出回执和每次真实心跳保留在
同名前缀 `-exit.json`；下一完整 LM 必须从本次真实状态继续，不能借旧强分支的值。
