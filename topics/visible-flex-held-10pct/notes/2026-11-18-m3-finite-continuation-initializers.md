# m3 原物理尾：两种幅值初值、局部根延拓与原门槛终态

维护：Astra-held10-7322d0de-20261118 / m3_true_coupling。计算日志的 UTC
时间为 2026-11-17；文件日期沿用本批接手记录。以下全部是原物理
`beta[0]=3.125`、mode spacing 3、M8、8 个物理 cell、每段 8 个 shooting
parts 的有限离散计算。没有改变原局部 D/S/A 条件或全局 `2e-9` 门槛。

## 新结论及边界

从已恢复并登记的 q=.021、.025 真联合场出发，尚未得到新的合格
q=.026 或 .0275 联合态。改良初值确实跨过了原来立即拒绝的局部根，
但完整尾部 Newton 的终态仍在原门槛之外；不能登记成幅值提高。

| 目标 q | 初始化或数值变化 | 终态 | 最后实际 min A |
|---|---|---|---:|
| .0275 | 原两联合场的 prefix secant；尾部原幅值缩放 | 首个局部根 D/S/A 拒绝；无 shooting 残差 | 未形成 |
| .0275 | 再用两 accepted tail 的全部 normalized state secant | 同样局部 D/S/A 拒绝 | 未形成 |
| .0275 | 原幅值缩放，加可选局部 root continuation | 局部 momentum Newton line search 失败 | 未形成 |
| .0275 | 几何 Q/L 幅值初值，加同一可选局部 root continuation | shooting 残差 `3.3753297793399703e-9` 后原线搜索失败 | .09175732928850125 |
| .026 | 原幅值初值，RK steps 16 | 第 1、2 次实际尾响应通过；第 3 次 `2.9567125289867316e-9` 后失败 | .21113473865912677 |
| .026 | RK steps 32，以前一运行第 1 次 accepted tail 为初值 | 第 1 次响应 `2.612966868725094e-9` 后失败 | .20996164393814443 |

`.026 / steps16` 的首个真实尾响应残差为
`1.7851946811285395e-9`，但它只对应前缀校正之前的 H。因此不能把这一
单独尾响应替代最终联立检查。`.0275` 几何初值运行从 shooting 残差
`4421.812979...` 依次降到约 `8.36`、`.00111593`、`1.4197e-8`，最后
停在表中数值。该运行证明初始化障碍可以被跨过，并未证明原完整
离散问题不存在解或其可接受误差已经满足要求。

## 局部失败点的实际诊断

旧 q=.025 到 q=.0275 的第一处原局部根拒绝位于 raw cell 0、raw
segment 4、segment 参数区间 [.875,1] 内：RK 子步 10 的 d 阶段，
局部 x=.6875，r=.27610311766803547，w=.0011548820524321874。
保持这个失败状态及原方程不变，从零态沿同一个状态方向递增，且把
前一步已求得的 L 作为下一步猜测，原局部求解器达到 lambda=1；该
根 min A=.7509954014614849、min D=.9999961936114845，局部相对
残差约 `4e-16`。因此这次立即拒绝不构成该点无 admissible 根的证据。

复用的原诊断脚本 `audit_m3_warm_initializer.mjs` SHA-256 为
`68e608d7697da5b601e428a8b3e3766ea36136533afc79de4f625957471ee839`。
原 accepted q=.025 的全尾 min A 位于 cell 0 的 segment 3/4 交界附近，
r 约 [.23506865,.23535194]，与上述第一次数值拒绝点不同。
R25 给出的是固定有限 Q/g、正 A 可行域内根的唯一性，不赋予这个
continuation 算法全局收敛保证。

## 两种可选初值的精确定义

`install_tail_secant_initializer.py` 只在明确给出第二个 accepted
checkpoint 时使用两份完整 normalized state 的 secant。之后仍执行
原来的 Dirichlet height 线性边界修正和真非线性 shooting。

`install_geometric_tail_initializer.py` 在节点上恢复 Q/L 原变量，把
非恒定 height 与径向 height 系数按目标幅值同比缩放，再用原 mean
equation 重新标定 mean。它没有强行线性缩放 mean。q=.0275 运行的
非恒定径向系数缩放误差小于 `6.7e-19`，初值节点 min A 约
.17143586，局部根最大相对残差约 `1.12e-14`。这些都是初值性质；
实际积分路径的 min A 及最终残差由完整求解另外决定。

`install_local_root_continuation.py` 生成独立的可选 engine 模块。
直接调用原 root 失败时，才尝试从 lambda=0 到 1 的局部状态延拓；
每一步调用同一个原 root，使用上一步 L 作为猜测，并保留其全部
条件。步长起始 .1，失败减半，下限 `1e-6`，总尝试至多 200。可选
factory 重定向到新模块；canonical `repro/source-root` 未修改。

在建立这个可选模块前，曾错误地直接修改**本会话 scratch 副本**的
canonical root，startup Git blob hash 守卫正确拒绝加载。这是独立的
工程失败，未进行数学求解，也未改动旧会话或仓库源。副本随后恢复
原字节，再采用上述独立模块。该失败也保留在机器记录里，避免把它
计作一次数学失败或悄悄删除。

## 复现与保留内容

入口位于 `scripts/resume_m3/`：

- `continue_true_coupled.py` 读取两份已 accepted prefix，生成 secant，
  接原实际 DN。可选 `--low-tail`、`--geometric-tail-initializer`、
  `--tail-steps` 和 `--tail-parts` 均写入命令记录。
- 上述三个 `install_*` 只对调用者明确给出的独立 source 副本安装。
  每个 installer 输出安装前后源码 SHA-256。
- `summarize_coupled_runs.py` 从终态输出提取标量、参数、源和输出
  SHA-256；`initial_continuation_failures.json` 保留这 7 个运行（包含
  那个 startup 工程失败）的精确命令与输入散列，不含场或网格数组。

`initial_continuation_failures.json` 中的 `solver_success=false` 为终态
依据。外层 driver 在原 coupler 捕获失败后可以返回进程退出码 0，
退出码不能代替数学收敛标志。所有场、checkpoint、逐步 trace 均只
留在本会话 scratch，可由所记参数、源码及已登记前驱重建。

这批计算关闭了原物理尾的若干初值分支。后续正向路线是按
`2026-11-18-m3-first-valley-design-screen.md` 改首谷 beta，重新求解
完整新物理前缀及尾部；这属于设计变化，不能累计成原 g 的 refinement。
