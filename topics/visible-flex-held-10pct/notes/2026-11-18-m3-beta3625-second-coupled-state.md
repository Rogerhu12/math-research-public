# beta0=3.625：沿 accepted 分支到 q=.0225

维护：Astra-held10-7322d0de-20261118 / m3_true_coupling。
承接同日 `m3-beta3625-first-coupled-state`。q=.0225 已完成四次
实际尾响应、prefix 内解以及内解后实际尾的复核。所有原方程、
D/S/A 条件和 `2e-9` shooting 门槛保留。

## 新联合状态

tail 物理参数与第一个 beta0=3.625 锚点相同：M8、spacing3、
depth8、parts8、RK16、quadrature128、linearFar48/steps512。
prefix delta 再次求解，故两次整体设计尚不是固定同一个 g 的家族。

| 量 | q=.02 前驱 | q=.0225 新状态 |
|---|---:|---:|
| delta | .06105607495644815 | .061055703925903294 |
| prefix 径向节点 | 936 | 936 |
| prefix metric FFT l1 | 2.8847607452601175e-9 | 4.53176827623042e-8 |
| prefix Cartesian Darboux tensor FFT l1 | 5.602582255436866e-5 | 7.150288482236905e-5 |
| prefix sampled κmax | 8.050355296763517 | 8.132826053794343 |
| 最终 actual tail residual | 1.4651335661047553e-9 | 1.3788089599084824e-9 |
| 实际 tail min A | .6767415337239006 | .6181559744895361 |
| tail sampled actual metric | 3.2508129521602634e-10 | 2.031359969123514e-9 |
| tail sampled full Darboux defect | 2.821838319302809e-6 | 1.8191177051466616e-5 |

新状态最终实际物理 BC 为 1.2515907255864691e-10；mean 一阶、
二阶 jet 差分别为 2.008115895790752e-14、-4.2920555998193777e-11；
非 mean 二阶差为 2.754247318154835e-9。实际 outer check 在一次
prefix 内解后通过；第 3、4 次 tail residual 都是表中最终值。
cut metric 与 C1 metric FFT l1 分别为 3.714937531350926e-13、
5.5095053317913816e-12。

前缀 `solver_success` 与最终 `tail_converged` 均为 true。这是
有限离散的第二个联合锚点，仍不代表整个连续形变族的闭合、reach
或严格全角 C² 界。尤其 tail full Darboux defect 随幅值增大，必须
保留，不能只报较小的 metric 数值。

## 连续推进与复现

入口 `continue_valley_design.py --beta0 3.625 --amplitude .0225`，
以第一个新 g 锚点的 prefix、最终 tail 和实际 port 为输入；本次
tail 不需要新旧物理线性差修正。源副本只安装显式 design initializer，
接受的两份 beta0 均为 3.625，完整求解仍由原实际 DN 决定。

精确命令、参数、source/input/output SHA-256 和终态标量见
`scripts/resume_m3/beta3625_q0225_coupled_record.json`。
主要可再生输出：

- prefix：`c6c8112c831ac1fc5ed458a15615687bd391ea76d5b0e1f4679386135965de8b`；
- 最终 tail：`50375c8b0f82868d04b4fc769626b273a59527de88ccfe229065588772214171`。

一旦本次完整 accepted，依赖队列已启动 q=.025：prefix 用两个新
beta0 的 accepted 场作 secant，tail 使用 q=.0225 accepted 尾作
原同 g warm start，delta 再求解。不能把此运行与先前直接跨 beta0、
使用旧 q=.025 H 的失败启动混同。其终态另行登记；主任务继续。
