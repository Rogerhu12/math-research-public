# actual61：四个当前 576 段 QR 模型及原方程精确残差读回

类型：启发式 / 数值证据；不声称 native 已收敛。
作者：ChatGPT / exact_refinement。日期：2026-11-14（UTC）。

## 1. 实际结果与本记录范围

第 61 次请求完成了四次真实当前状态的 `withJ` 求值、四份独立当前 576 段快照、四次 $\eta=1$ 的 R273 完整平方根阻尼方向，以及各方向对本轮保存原方程的全部行精确读回。同步桥没有失败；前三轮分别有原 `noJ` 试步被接受，第四轮原线搜索失败。最终 `success=false`、`native_accepted=false`、`complete_tail_matching=false`；不能把四个线性方向已返回写成完整 native 求解完成。

实际运行：[43645948199](https://github.com/Rogerhu12/math-research-public/actions/runs/43645948199)，来源提交 `cf6b51193255dfc713610d2919598451ccdd49e2`。原错误为 `Error: multiple-shooting line search failed at 0.00007952539043101878`。原容差仍为 `2e-09`，原最多 32 次迭代未改变，只有一次 protocol 请求；请求的最终完整 DN Jacobian 和 finite audit 没有获得成功返回。出处：[native result](public-actions-43645948199-1-current576native/native-current576-damped/result.json)、[同步桥汇总](public-actions-43645948199-1-current576native/native-current576-damped/current-correction-summary.json)。

本记录逐字读取四个完整小 QR summary、同步桥 summary、native result 和原 trace，核其 SHA256 及桥到四个 summary 的状态、矩阵、方向、结果收据对应关系。没有在本地重做矩阵动作、范数、有理运算、RHS、Jacobian 或 QR。完整 2,335,870,174 字节 artifact 的逐数组 / 因子 / 整数 ledger 字节核由另一个公开 Actions reader 承担，本记录不预先宣称该核已经完成。原标量、精确分子分母和所有小报告文件身份保存在 [伴随 JSON](actual61-four-QR-original-scalars.json)。

Artifact 元数据：ID `14136633570`，名 `visible-mainline-current576native-43645948199-1`，ZIP SHA256 `7b17d1b0c11bfe14329a1d8715c8451498d0dedb6821859deb8485e5b1c1b469`。这些是根协调端提供的实际 artifact 身份，不是本次小文件读取对整个 ZIP 的独立验证。

## 2. 四个不同的当前线性模型

每轮以本轮真实 `states`、`flows[n].J/out`、`residuals/end`、cut、far、target 和原 $\sigma$ 形成独立快照；没有以 actual28 或上一轮缓存替换本轮基态。第 0 轮状态 SHA 为 actual59 真正接受状态的 `384de298d6274ef7a6f5bdbc4e6cf6ef9dee5fb9bffd020b7b60001463940e03`，之后三轮分别绑定新的状态。下面全部数值直接抄录原 Actions 报告。

| 轮次 | 本轮原 fresh `withJ` norm | 本轮状态 SHA256 | 本轮原有限矩阵 identity SHA256 |
|---:|---:|---|---|
| 0 | `0.00018359565445185818` | `384de298d6274ef7a6f5bdbc4e6cf6ef9dee5fb9bffd020b7b60001463940e03` | `3a5bcab4442e5539bcd6d52fe809078531a5181c643999a3628ea15b4968864c` |
| 1 | `0.00016781299431962708` | `78bd3880951910c473fa42b03bd87165b123e0339d4ced343f11e3ffb153caee` | `fa74c276297f39b1ec601dcc522e5859cd7cd809c95f99771d1573b45fe8f41b` |
| 2 | `0.00010439752900203701` | `ad7963646d2d3351690b9c9945ef26caf0baf4cf12c92ac12c8bd716dc9a6fec` | `a311f83bb856a45cee3ec969be08ffcf985c889d5ee5848d54e42ceb21da44ee` |
| 3 | `0.00007952539043101878` | `b34daaf8ad1841b452707c669236ba38731d1f97506af4bbfe1a22e39d814013` | `20a6c30233dc870fc1048b6091f05ba9eaca0f3d47c33a491d48d549af5bb240` |

出处：[iteration-000](public-actions-43645948199-1-current576native/native-current576-damped/iteration-000/qr/summary.json)；[iteration-001](public-actions-43645948199-1-current576native/native-current576-damped/iteration-001/qr/summary.json)；[iteration-002](public-actions-43645948199-1-current576native/native-current576-damped/iteration-002/qr/summary.json)；[iteration-003](public-actions-43645948199-1-current576native/native-current576-damped/iteration-003/qr/summary.json)。全部方向保持完整 `577 × 224` 原坐标，不清零或投影 cut/far 分量。四份报告各自记录 129248 个有限方向分量；负零数依次为 21、20、20、17。此处引用报告计数，方向 raw payload 的独立字节核尚不在本小报告范围内。

## 3. 原方程全部行的 exact 读回

每轮 exact oracle 对当轮保存的有限 binary64 数组计算完整 cut / stage / far 行。在 stage 行使用 $e_n=J_n\delta_{n+1}-\delta_n+r_n$，先按实际保存数的精确二进制值形成未缩放残差，再精确除以实际 $\sigma_n$。这与先把 $J_n/\sigma_n$ 等系数舍入后求点积不同；该读回不包含阻尼罚项，也不包含新科学接受条件。完整 129248 行、576 段及 28901488 个原 product positions 均由 Actions 报告完成。

四轮最坏行均为 `stage 9 / row 0 / Q1 / global equation row 2128`；其保存原尺度 bits 均为 `14b8f8fa483ef73c`。原 64 位有效十进制展示字符串如下，真正比较依据仍是报告所保存的整数分子 / 分母。

| 轮次 | 原 exact $\max |e|/\sigma$ 的完整展示字符串 |
|---:|---|
| 0 | `9.685625012058062404290715378074972870371298997949219946410926342E-11` |
| 1 | `9.685623139675829559868110986169517446209818527497778758253948554E-11` |
| 2 | `9.685623141492648871729266017278251425127578322813875579535512578E-11` |
| 3 | `9.685623141564525654024788745526925689480898069418253457984007082E-11` |

这些值证明的是各自已保存线性系统及各自已恢复 binary64 方向的缺陷很小。它们不证明数学 flow 的导数被精确表示，不控制新的非线性试步余项，也不等于原 `noJ` 流程实际重新求值的 norm。小 summary 已完整保存最坏行的精确分子分母；每轮全行 ledger 收据及 full report 收据也已纳入伴随 JSON。

## 4. 平方根模型的数值读数与精度边界

每轮完整平方根问题报告 129248 个未知量、258496 个增广行、577 个节点罚块、1153 次局部 QR、1152 次形成操作，以及 129248 个纯常数行。每轮因子与常数共 `464891392` 字节，形成时舍入为 binary64 零的计数为 0。没有删除节点罚项、丢弃纯常数或增加局部 ridge；这仍是原完整链上的 $\eta=1$ 方向问题。出处同四份 `factor_summary`。

下表是已经形成的 binary64 加权系数上、由 longdouble 运算读取的模型结果；不是区间包络或精确实数目标的认证。该平台报告 dtype `float128`、storage 16 bytes，但实际 significand 为 64 bits，不能把这个 dtype 名称写成 IEEE 四倍精度。

| 轮次 | 原 formed base objective | 原 formed objective | 原 formed residual $\ell^2$ | 完整未预条件模型梯度 $\ell^2$ |
|---:|---:|---:|---:|---:|
| 0 | `5.8964241258891773136e-08` | `6.5510046315094011616e-21` | `1.1440448194968094127e-10` | `405733.65259936885695` |
| 1 | `3.990538805649319283e-08` | `6.638479341421796542e-21` | `1.1514427842547540496e-10` | `1354093.549866969254` |
| 2 | `2.4359516108152003926e-08` | `6.545847387395797259e-21` | `1.1434609171873255444e-10` | `628039.57135626521915` |
| 3 | `1.490582767237037018e-08` | `6.540365634198721016e-21` | `1.1429906034631574624e-10` | `478231.02473180188738` |

完整未预条件梯度仍为表中数值，不能因为三角回代残差或目标值很小就称模型最优性已认证。报告明确没有从这些普通浮点范数推出 R273 后验误差证书。第 0 轮三角残差为 `2.0792011877132903636e-20`，形成能量减因子能量为 `-1.0103146193287089313e-33`；这些也仅是相应浮点读数。其余三轮同类完整值直接保留在伴随 JSON，不另在本地计算差值或比率。

| 轮次 | factor 时间（秒） | QR 加原诊断总时间（秒） | 最大 RSS（KiB） |
|---:|---:|---:|---:|
| 0 | `22.40335964199994` | `23.170818268999938` | `725212` |
| 1 | `22.64713808900001` | `23.397928358999934` | `928004` |
| 2 | `22.461917857000117` | `23.218483733000085` | `965388` |
| 3 | `22.400164291999317` | `23.15283448000082` | `954064` |

## 5. 原非线性接受与 fresh `withJ` 读数必须分开

原 trace 保存了三个实际被接受的 `noJ` 试步；第四轮原线搜索报错。下面只转录 `accepted-trial-recovery-only` 与下一轮 fresh `withJ` 事件，不把两种求值路径合并成一条单调序列。出处：[原 native trace](public-actions-43645948199-1-current576native/native-current576-damped/native_trace.jsonl)。

| 方向来自轮次 | 原接受 trial / step | 被接受 `noJ` norm | 下一轮 fresh `withJ` norm |
|---:|---|---:|---:|
| 0 | `0 / 1` | `0.00016781299431962708` | `0.00016781299431962708` |
| 1 | `0 / 1` | `0.00008541616009257574` | `0.00010439752900203701` |
| 2 | `4 / 0.0625` | `0.000103579366549043` | `0.00007952539043101878` |
| 3 | 无接受；原线搜索失败 | 未返回被接受 norm | 不存在下一轮快照 |

这给出一个已发生的区别：同一被接受状态在下一轮 fresh `withJ` 路径中，可以出现不同于接受时 `noJ` 的 norm。当前公开小报告还不足以把差异归因于唯一的几何公式、某个 RK 操作或某个最坏分量。四个当前线性缺陷小，并不能消除这项原求值路径差异。后继最小诊断先固定最后一个已保存状态，只补一次原 `noJ` 输出，与该状态已有 `withJ` 的完整 residual / 出口逐项对照；只有留下具体未解释差异时再扩大到其余状态。不必为这个问题重跑四次 QR，也不应先改原验收规则。

## 6. 精确身份与尚未付款范围

| 组件 | 已执行来源 SHA256 |
|---|---|
| current576 launcher | `06b8c44c115fcf754e963aeeb3adc04a26500cade3817018bae50e2e50aebc3b` |
| current576 hook | `0933ee819ce56be648f17e2e876372e943059f19c79fed701bda60ec11cf66dc` |
| current576 QR CLI | `ac04842bb9c42b9f29c8209d0d5f523c83744aa548e5615267521d8bf2c3141f` |
| current576 system adapter | `695c2a564ada2bfc3cac251dfb5bd46bf99f6d16b696c64b75d9f90703a6ed90` |
| R273 动态 factor engine | `9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33` |
| 原 exact 整数 kernel | `0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f` |

上述来源身份、每轮 snapshot / state / matrix / delta / checkpoint / factor-index / 全行 ledger 收据均来自原报告，并保留在伴随 JSON。已经实际完成的是小报告原 bytes、桥与 summary 共享身份的交叉检查及原标量阅读。整个 artifact 的四份完整快照、全部 QR 因子/常数、四份方向 payload 和四份全行整数 ledger 的独立 byte 审计仍须以已安排的 Actions reader 实际结果为准。本记录不给任何未读大阵补写 PASS。

这次计算推进了当前原 576 模型的同步求解，但尚没有完整 native 接受对象，不能作为后续 full DN、闭场或完成标准的已接受父场。
