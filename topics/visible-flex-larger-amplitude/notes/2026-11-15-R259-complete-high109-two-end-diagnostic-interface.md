# R259 / R277：完整高 109 自由 core 两端诊断接口

日期：2026-11-15。作者：ChatGPT / exact_refinement。

**分类：源码准备与已证明代数的实现合同；没有运行新数值。** 全部科学算术只准在公开 `Rogerhu12/math-research-public` 的 Actions 执行。本次只新增一个独立消费者，不改冻结 `geometry_20261114_small_core_resonance.py`，不改变实际 78 的搜索、任何原 BVP/native/full-DN 门或其他正在运行的分支。

## 1. 已有对象和这个消费者补哪一项

R259 的原入口已经保存原 112×112 真正完成的零高度尾 slope J，实际逐项非对角数为零；它只传播前三个单位 core 模式。已有“全部高行残差恰为零”仅表示试探向量的高分量为零时，高行也为零，不能排除高模齐次解。

新消费者逐一构造 **112 个模式、每模 699 个节点、698 个 2×2 原 collocation L/R 块**。对所有高模 4…112 检验完整两端系统，其左条件为 $H_j(0)=0$，径向入口 $U_j(0)=c_j$ 自由，右条件是原高度 RHS 的末端线性行减去完整尾 J 耦合。不会把高频长初值传播失败当成模式不存在。

完整行列式恒等式及奇异右块的多项式延拓证明见 [R277](../results/R277-complete-two-end-chain-determinant-and-high-core-elimination.md)。令

$$v_0=(1,0)^T,\quad v_{i+1}=-\operatorname{adj}(R_i)L_i v_i.$$

按固定原行列顺序，完整两端矩阵行列式是 $-\ell v_n$，不需要任何 $R_i^{-1}$。只有全部 $\det R_i\ne0$ 时，才另外给出单位入口到右行的 Schur 对角元

$$d_j=\frac{\ell_jv_n^{(j)}}{\prod_i\det R_i^{(j)}}.$$

输入 J 全部条目均读取并保存；只有实际非对角项全为零才用逐模分解。若输入变成非对角 J，消费者保留其身份并报告本分解不适用，不把条目截零继续。当前四个原数学输入全部硬锁，因此此处只使用实际已观察到的对角性质。

## 2. 新源码与冻结身份

新文件：

`computations/exact_20261115_r259_high_core_two_end.py`

- 字节数：49,546。
- SHA256：`f60db29ef0c235cc4d5d2fa2ffecd480dccc4d54b46aafe655a60ba88af7013f`。
- 输出 schema：`R259-complete-high109-two-end-diagnostic-v1`。
- 已做：本地 AST、来源文件 SHA 和原 JSON 字段/结构核对；独立回执为 `2026-11-15-R259-high109-static-source-check.json`，不覆盖 R276 的回执。
- 未做：import 新模块、RHS/J/ODE、矩阵/范数/有理递推/Arb 计算或试运行。

完整证明 R277：9,665 B，SHA256 `03d7498978f58b84f49c9995d09132fa0cd431c56c0c3960e6c65d6bbcbef9a7`。证明与接口没有生成任何未来运行身份。

## 3. 本次绑定实际 78；它仍不是共振根

实际父运行 `43662193286`，source `11b5d25c436d84d734a73d4609092bde749daea5`。下列 SHA 是原件字节读取，不是新数学计算：

| 父件 | 字节数 | SHA256 |
|---|---:|---|
| `request78-input-and-source-identity.json` | 28,516 | `57a5d443b0f13193a385a40a13c5dc038dae768e97095074e08a6edca5fc5b58` |
| `resonance/resonance-status.json` | 50,438 | `09031496410951afc018b223b921db111a43b3e0852592b87aafd5351b4f0c40` |
| `resonance/circle-reference.json.gz` | 139,996 | `6c56f190c6e07538582bc6271caa6abe9d8eb5c59362579b8f87ee6d13f8afb1` |
| `resonance/complete-scalar-domain.json.gz` | 79,207 | `8efa0be35549651bf8f8369cf7587c0b7cda240cebad67569686a9be9242be71` |

78 原保存最终参数为

```json
[0.09365081258727412, -0.13201200770909496, -0.12389206129693811]
```

其低三单位缺陷仍大；输入检查**不要求共振已找到**。程序逐位核最终参数与 circle 的完整 scalar 规范一致，保留父件的 `low_mode_candidate_has_small_full_recorded_right_residual` 原值，不将其改成接受标志。

当前参数化输入合同接受原冻结 3b9 入口生成的同 schema 原件。将来另一种 LM 搜索若更换 producer，应明确绑定它的真实来源后另作适配，不能把新 producer 贴为 3b9。

四个原数学输入仍是：

| CLI | 原相对路径 | SHA256 |
|---|---|---|
| `--accepted` | `notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz` | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| `--prepared` | `notes/public-actions-43588155190-1-prepare112/preparation112/prepared.json.gz` | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| `--tail-anchor` | `notes/public-actions-43592195185-1-coupling112banded/full-DN112/outer-00-anchor-tail.json.gz` | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| `--tail-config` | `notes/public-actions-43588155190-1-prepare112/T112-config.json` | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

这些路径相对于 `topics/visible-flex-larger-amplitude`。父件可由已公开同目录的小原件或完整原 artifact 的已核提取提供；本消费者不联网、不使用 token、不自行下载。run/source 由上游真实 artifact 绑定，消费者另保存该绑定范围，不冒独立 API 核验。

## 4. 最小 Actions 调用

沿实际 78 的环境：Python 3.12.14、NumPy 2.3.5、SciPy 1.17.0、python-flint 0.9.0，BLAS 三个线程环境均为 1。继续使用原 `prepare_public_source` 恢复公开 78 源及 source-origin，设置同一 `VISIBLE_SOURCE_TOPIC`。程序调用原 `setup` 创建原 profile 和边界常数，但不调用已创建 flow 的 RHS/J，也不启动 Node/native。

源闭包保留实际 78 的 68 项来源清单，加本消费者。父清单的全部科学来源逐项核当前 SHA；仅 publisher 是明确未被数学导入的出版工具，其历史收据完整保留，新出版版本可另记，不因该无关版本变化阻止诊断。消费者另硬锁原 3b9、profile、boundary、ScalarExpression、Arb primitive 等 10 个关键源。完整旧四输入及真正零 J 的成功来源继续由原 `setup` 校验。

设 `PARENT78` 为真实父件根（其中有 `request78-input-and-source-identity.json` 和 `resonance/`）：

```bash
python computations/exact_20261115_r259_high_core_two_end.py \
  --accepted "$ACCEPTED96" \
  --prepared "$PREPARED112" \
  --tail-anchor "$TRUE_ZERO112" \
  --tail-config "$CONFIG112" \
  --resonance-directory "$PARENT78/resonance" \
  --parent-identity "$PARENT78/request78-input-and-source-identity.json" \
  --parent-identity-sha256 57a5d443b0f13193a385a40a13c5dc038dae768e97095074e08a6edca5fc5b58 \
  --status-sha256 09031496410951afc018b223b921db111a43b3e0852592b87aafd5351b4f0c40 \
  --circle-sha256 6c56f190c6e07538582bc6271caa6abe9d8eb5c59362579b8f87ee6d13f8afb1 \
  --scalar-domain-sha256 8efa0be35549651bf8f8369cf7587c0b7cda240cebad67569686a9be9242be71 \
  --producer-run-id 43662193286 \
  --producer-source-commit 11b5d25c436d84d734a73d4609092bde749daea5 \
  --arb-bits 160 --arb-max-bits 640 \
  --budget-seconds 1800 --maximum-integer-bits 4000000 \
  --out "$VISIBLE_OUT/high-core-two-end"
```

必须使用新输出目录。精度、时间和整数存储上限只是这个诊断的显式计算预算，不是候选/非线性科学门。预算届满或区间未排零保留已完成证据；不会宣布高模真的奇异，更不会改父运行状态。

## 5. 第一个对象：保存有限系数的精确代数

父 circle 的全部 699×453 状态读入，699 个真实保存半径和完整均值高度不替换成 `a`。使用原 profile 在原 node/mid 返回的 a/ap，与原计算顺序形成所有 112 模的 B/Bmid/L/R；全数组按 `<f8` C-order 原始字节 gzip 保存。前三模额外按原独立三模宽度重放相同表达式，记录这些块是否逐字相同，不把 SIMD/批次产生的末位差默认抹掉。

整数核把上述有限 L/R 和末端 B、gamma、epsilon_h、J 常数当成精确二进数。末端 $B_{22}-\gamma\epsilon_hJ_{jj}$ **直接由有限操作数作精确代数**，不先悄悄增加一次 binary64 差的舍入。每模保存：

- 698 个精确 `det(R_i)`、其乘积和全部零块坐标；
- 完整两端行列式的精确有符号二进见证，以及两个最终 projective 分量；
- 单位入口 chart 存在时的 U、H、Hprime、右端缺陷和逆 Schur 对角元精确商；
- 所用完整数组身份及固定行列顺序。

大整数用“奇整数十六进制 + 二的幂”存储，避免十进制转换限制和浮点溢出。显示的 24 位科学记数法只是近似显示，不是外包；符号和等于零判断只看精确整数。若右块奇异，单位入口 chart 明确未定义，但完整两端行列式仍计算，不能把 $0/\text{非零}$ 冒该不存在 chart 的逆。

全部高模两端矩阵非奇异时，完整高齐次响应唯一为零。若高模的所有右块也非奇异，则高 core Schur 对角块存在且可逆；低/高耦合严格零来自已核对的完整对角 J 和 R259 圆 Fourier 分解，不是丢弃小非零项。完整 112 行 map 以全部 112 个对角见证及显式零交叉块表示，没有截成低 3。

这个整数证书没有把已舍入圆半径、B/L/R 或理想 Fourier 分解冒成完整普通 FFT 程序的精确 Jacobian；源和输出对此有独立 false 标志。

## 6. 第二个对象：声明实数离散圆的 Arb 包络

原 `complete-scalar-domain.json.gz` 的完整 descriptor 与 circle 的全 scalar 规范交给已冻结 `ScalarExpression`。使用原 `returned_ap` 表达式，不把 app 当有限 Gauss 半径的导数。保留原实际 binary64 节点、`np.diff` 形成的宽度和原舍入 midpoint 位置，并把这三个离散采样常数组解释为精确常数。

每个精度层重新用 Arb 评价这些位置的 a/ap；按原 scalar collocation 递推真实数意义的 R；严格包住所有 node/mid 的 R>0 与 $1-(qR)^2>0$。然后生成全部指定模式的 B/L/R，并用同一 R277 行列式递推包络。这里不会把父 binary64 R 直接塞进 Arb，故它是**另一个明确声明的实数离散模型**，不是第一个模型的浮点误差证书。

首次成功建立圆包络后至少计算全部 112 模。默认在 160 位开始，最多 320、640 位；后续精度只重算尚未排零或尚未确认初值 chart 的高模。若某层圆包络本身未解决，尚未评价的低三也不会遗漏。所有层的完整圆包络和各模见证都保留。

`all_high109_two_end_blocks_proved_nonsingular_in_declared_model=true` 仅在实际 109 个完整行列式包络都排除 0 时成立。Schur 字段还要求全部右块的行列式也排零。它没有证明：

- 实际零尾 J 与真正数学尾导数之间的误差；
- 连续 ODE 的高模非共振或普通 FFT 实现导数的误差界；
- 整个 s 区间的圆 Frenet 域、低三共振存在或参数横截；
- 一个非零幅度完整 BVP、原 native/full-DN 接受或闭曲面。

因此成功高块诊断可以填入 R259 的一个明确条件；不能以该条件替代其余存在假设。

## 7. 输出与中止保全

小输出为 `summary.json`、`input-binding.json`、`finite-model.json`、`array-manifest.json`。完整状态是 gzip 的 `result.json.gz`。所有原矩阵、整数见证、完整 Schur 表和 Arb 包络放在 `large-arrays/`，按当前 publisher 规则仅在 artifact 保存，不塞进 Git。

| 文件 | 内容 |
|---|---|
| `large-arrays/*-all112.f64.gz` | 完整 B/Bmid/L/R 原字节，含 112 个模式 |
| 其他 `*.f64.gz` | 全 J、mesh、h、mid、原半径/均值高度及 scalar/q/W 数据 |
| `exact-mode-001.json.gz` … `112` | 每模完整精确有限系数行列式见证 |
| `finite-full-mode-schur.json.gz` | 全 112 模单位 map、全部高 109 core 及零交叉耦合的范围 |
| `arb-circle-BITS.json.gz` | 每层真实数离散圆完整包络 |
| `arb-mode-JJJ-bits-BITS.json.gz` | 每层每模包络、排零和 chart 状态 |

每个已经完成的 mode 都先写完整文件并记录 SHA；精确阶段的已完成收据列表、Arb 阶段的已完成精度/模式收据和 latest 字段保存在 result 中。触发计算预算时，输出 `resource-budget-exhausted-with-partial-evidence`；没有完成的模态不取得非奇异资格。有限精度到上限仍未排零时，输出明确的 unresolved 高模列表。I/O、身份不符或实际程序异常保存 traceback 并非零退出。

完整原件不会因为区间失败而被删除。输出 `success=false` 始终表示没有宣称原非线性 BVP 成功；不要把这个标志与独立诊断执行完成混淆。

## 8. 资源结构与尚未实测的成本

这是有限结构账，不是运行时间预报：

- 每模方程维数为 1,398，全部 112 模共有 78,176 个 cell。程序不形成 1,398² 稠密矩阵，也不形成/分解 109² 稠密高块。
- 全部 L/R 原矩阵字节为 5,003,264 B；全部 B/Bmid 为 5,006,848 B，合计 **10,010,112 B**，另有小规模原 scalar/J/mesh 数据。程序把这些完整矩阵 gzip 保存。
- 精确递推每 cell 只有固定次数的二进整数乘加；但整数位数随长度增长，不能把大整数操作当常数成本。默认每整数 4,000,000 bit 资源上限和总 1,800 s 限额明确记录，实际最大整数位数、运行秒数、RSS 在 Actions 输出。
- Arb 先共享一份该精度的完整圆轨道，然后逐模处理；最多三个默认精度层，后两层只重复 unresolved 高模。端点巨大分子和区间见证的压缩大小未预报，全部放 artifact。

没有新 J、RHS、ODE、全 Fourier 方向调用、native 进程或低三参数优化。已有的低三搜索、native73、prefix 路径均不等待此诊断作为前置门。
