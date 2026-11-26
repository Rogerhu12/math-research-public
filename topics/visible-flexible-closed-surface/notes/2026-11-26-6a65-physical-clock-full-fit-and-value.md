# 更早入口与物理重参数后的完整拟合和真实值

2026-11-26，Astra-visible-flex-6a65e705-20261126。

本条消费[更早 .14 入口](2026-11-26-6a65-geometry-earlier-port-natural-metric.md)的完整
位置场，再按[角独立物理时钟](2026-11-26-6a65-geometry-exact-physical-clock.md)解除右段压缩。原完整位置集合与曲率在时钟变换中不变；
目标度量改成新物理坐标下的 `d sigma²+a(s(sigma))²du²`，所以明确是新 g。
随后对它重新完成全部 1788 参数的一阶 jet 拟合和真实完整 value，未沿用 raw 表的值。

## 1. 冻结新输入及有限拟合

时钟为 `sigma=s+Delta*S9((s-b)/.75)`，恒等/平移延到两侧，
`b=.1815625`、`Delta=.04567394987169149`。
新右长 `.7956739498716915`，实际 cut `.9772364498716914`，
完整平 cuff `1.4572364498716914`；保持真正 `A=.8746432018013935,Z=.51`。
完整零、一、二阶位置导数以及 a 的两阶导数使用同一逆时钟链式法则。

原 `short-cauchy-v1` 辅助工厂只改变声明的 rightLength；自动选择 S9 的相邻
7/8 次幂，未修改工厂源码，也不把辅助基说成原辅助基的时钟复合。
actual 周长与这个新辅助基的差仍由全部 rho 列拟合。

J38/K11/N128 和全部 theta/phi/height/rho/A/Z 通道保持，物理一阶导数拟合权 `.03`。
42 个准确有理 knots 由 `j/36` 及物理短前缀分点在新 `q=(sigma-c)/(S-c)` 下的
位置组成，完整配置原样登记在本条 `-config.json`。未遗留旧归一坐标下的分点。
实际 90 径点 ×128 角，矩阵秩 38；最大 rho 系数 `.08748553653390352`，
A/Z 与 cut 的定义保持。有限 `base+rho` 是此后真正求值的 g，不冒充原始周长的精确插值。

## 2. 三个实际成功进程

reference 实际 2.00418 秒，fit .16949 秒，完整 value 110.59571 秒，均自然 exit 0。
完整 value 使用 Node v24.22.3、heap 128 MiB、semi-space 4 MiB；每十秒读子进程真实
状态，采样 VmRSS/VmHWM 最大均为 86200 KiB。源文件在启动与退出时 SHA 相同。

| 真正完整有限值 | 数值 |
|---|---:|
| 总平方目标 | .21590705686187553 |
| metric 平方目标 | .19331494939474672 |
| 曲率平方目标 | .022571127096358317 |
| 几何平方目标 | .000020980370770502373 |
| 完整相对 metric 峰 | .3936856405881617 |
| 自己主曲率绝对值峰 | 18.630497499487163 |
| 最小归一面积平方 | .769744215101891 |
| 最大原点半径 | 1.4502134230075112 |
| 最大绝对 y | .8283679419627915 |
| 最小 held 见证距离 | .6263963331525163 |

与前条 `.18` 未解除时钟版本相比，实际完整值从 metric `.885019`、κ`28.74355`
降至本表；两者有不同 g、不同完整拟合场，不能当作固定 g 的加密。
原 raw 时钟表的 `.389776` 与 κ`17.40278` 没有被抄作本有限模型的值。

仍为 301210 行：metric 272 径点，曲率/几何 409 径点，65 半角节点。
metric 最坏点 `sigma=.2711470877806955,u=pi`，E 误差 `.3936856043`、F/a
误差 `.0001195284`；曲率峰在 `sigma=.2231838819266238,u=2.7979809571034093`。
held guide 违反 `.023603666847483717`，球包、width、高度 guide 在这些有限行中无违反。
还没有 normal 或 LM 接受，更没有全域 metric、全点对 reach 或全时族证书。

## 3. 前一输入首 normal 的真实退出补记

前条 `.18` 自然周长输入另做了完整 LM 尝试：实际 full normal 在 314.878 秒返回，
1788 列、301210 行，与其已公布 baseline 的 R²/metric/曲率逐值相同。
进程随后在 321.91403 秒被 SIGKILL（returncode -9）终止；无 trial、无末态、无接受。
最后一次监控为 VmRSS 245792 KiB、VmHWM 249036 KiB。原因尚未确定，
不能只由这个数值推定内存限额，也不能记成数学拒绝。

实际 stdout 只有那条 normal 返回；原件前缀为
`cauchy-perimeter-fit01-lm01-monitored`，入口源码始终为下表同一个 SHA。
后续检查完整矩阵的临时复制与线性求解生命周期，不删除参数、残差行或约束。

## 4. 原件和源码

大数组与完整状态均只在 scratch `geometry-work/`，保存真实退出回执。

| 原件 | SHA256 |
|---|---|
| r137-transplant11-physical-clock-samples.npz | 2ebaab53fd4c6517862fa12d3c5955be1b9e0f648f6f08e20d7a3cf7c31a6bf2 |
| cauchy-clock-fit02-config.json | c130403d727bd938093fccc5fecf713f94c8ea7f06763266cf86b2beed51b8b4 |
| cauchy-clock-fit02-reference.json | 538c87c739c42c709b9fada4cbfaaee07ae5d4ac1875edd5033a405824a507c7 |
| cauchy-clock-fit02-state.json | f597ce9c03cf6b113bc8847239e18abdfb1053b19867c2321fe33676b4c86810 |
| cauchy-clock-fit02-value-monitored-baseline.json | 01725d3b221e5d0f8d0580ac332f957e8183edc6bcacd3b664743197a4ee46e2 |
| 完整位置入口 | 25d0cd8db5444a0629aaa39b26e8287df68ef6f31956c27f10012a9095bffe3b |
| 完整 rho 拟合器 | 99d2bb06878e2efa89824b9bd1d1b3d9bba7343545e1e99d7af81a00f17c25d9 |
| 新输入成功 value stdout | 4ee26de94c0543fad2a3b25b5a821e6b2389befabca1028857a62e2f597469b8 |
| 旧输入被终止前的真实 normal stdout | 95d3a007b7b83b9c36038a39d04fb262b6e6e9a9eadf5e9ef1cae175d6d9ccdb |

复算顺序：实际短 Cauchy/coast、旧场 `.14` 扩域、完整自然周长、纯物理时钟导出，
以同一完整表的 `[0,trueCut]` 行生成 reference，运行 `--fit-radius`，最后真正 `value`。
本条所有求值都使用已声明的 metric tau `.05`、曲率另名 tau `1e6` 启动目标和 R219
全几何 guide；没有重定义一次失败尝试的成功含义。
