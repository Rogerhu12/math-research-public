# Request95：把一个相邻输入词候选计入原 native 第一次 correction

类型：独立候选算法与公开 Actions 接口；尚无本入口的数值结果。  
作者：ChatGPT（`amplitude`）。  
日期：2026-11-15 UTC。

## 1. 具体改变及实际依据

本入口消费 actual91 完整 artifact，从 actual73 iteration2 的**完整失败基点**重新启动一次原 native 请求。它不是 actual83 已拒绝的 trial，也不是已收敛的尾锚。actual91 已确认 stage10/Pi76 的主要理想线性改善，在 node11/Q76 的输入 binary64 写回时丢失；该结论只支持尝试可表示候选，不保证新候选的全局或非线性下降。参见 [actual91 正式结论](2026-11-15-actual91-four-row-input-word-loss-and-native-candidate.md)。

唯一的新方向规则是：原 iteration0 已完成 fresh-withJ 后，尝试 node11/Q76 向下一个相邻正 binary64 词；其他数值方向坐标为零。先用完整旧模型，再用这次真实 fresh 模型筛选。两次筛选都保留原全部129248行，只有两次完整仿射无穷范数均严格下降，才把该方向交给原求解器。

**筛选不接受 native 步。** 原求解器仍运行原十档 noJ trial，使用原域判断和原 `test.norm < ev.norm`。该方向占原32次总迭代中的 iteration0，不在循环外先接受一个额外种子，不追加第十一个试探。若模型未选中候选，同一 fresh snapshot 直接交给完整 R273 QR，不再做一次 fresh-withJ。若候选已交回但原十档全部拒绝，则保留原 line-search failure。后续所有 correction 都使用完整 R273 current576 QR。

原配置仍为 modes112、shape224、576 stage、577状态节点、原32次迭代、原十档回溯、原容差 $2\times10^{-9}$。完整 cut/far、原 H、目标、scales、所有原参数、graphs/gains、576个 cell/profile、最终端点 J 与 fresh audit 保留。后续 QR 的显式正阻尼仍为 `--eta 1`；它没有变成最终方程或容差。

## 2. 原始证据与精确父身份

| 项目 | 固定实际值 |
|---|---|
| 仓库 | `Rogerhu12/math-research-public` |
| 原 actual91 | run43672150224 / source`b78f0dd1471a118d2ed21467602509d188c2ab67` |
| artifact | 14145200674；`visible-mainline-modelresponse-43672150224-1` |
| 完整 ZIP | 10267458 B；SHA`78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6` |
| actual91 主结果 | SHA`0b7200064336361ecb36b0627495fca298b7af758ed37d34d6ae6b1a1898db04` |
| actual91 input binding | SHA`0119e12bfc7f98732189b76b3fdfa23ae05229937a8ea998c9aa38890ff11d0a` |
| 原 actual73 | run43657001633 / source`9515d5aaf7c68f8efd366438d6bd81ce73c3486f`；call1/iteration2/snapshot2 |
| 完整原基点 | 577×224 binary64；SHA`f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6` |
| 候选坐标 | node11，列75，即 Q76；原 little-endian 词 `6e1cafdb47e9c93c` |
| 完整原 H | SHA`c35972d038321acf6db273248189b1e1d2527aa6eb2b323d37fcde4da448682f` |
| 完整原 target | SHA`e2ea4563e7afc7d993db2ebc29ef63a1d853355c9d1ceeaf10f296b84391a14d` |
| 完整原 scales | SHA`ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc` |
| 原 far graph | SHA`395804bb32582680dd544c6278862f51919c7598b3a1a526f1194f18deffda54` |
| 原全 J 的身份引用 | SHA`1f5e3cfd7d7fec8c127841c3c859b43ed4264e55c7bf7805e84f4dae73b453d4`；本轮不重新取完整旧 J |
| 原 stage8–11 完整 chunk | 1605632 B；SHA`fd117e2d3cfdd26ddfa584e5c75e521209f12ca16f098596ec61cab3e47f8677` |

新的 transport 复用 SHA`51224788…` 的冻结标准库内核，实际校验完整91 ZIP、所有成员的路径/类型/CRC/size/SHA，再只读发布。只有固定 pin、source commit 核对和本地 adapter 身份改变；网络重定向时 Authorization 的原处理、临时 ZIP 删除、receipt-last 发布保持。CLI 仍要求完整显式五元组。

Parent binder 把**本次完整91所有输入文件**逐字保存在自己的 `parent91/large-arrays/original91/`，并另写八份完整模型输入：base、576段 residual、cut residual、end residual、scales、far graph、H、target。原83的15数组全部仍在完整91副本中；新模型只用上述八份及原 J chunk。每份都与原15数组 manifest 和原73 context 的 SHA/shape/dtype/order 交叉绑定。

原83没有导出基点的 `stage-out`，所以入口不从 residual+state 重构它，也不拿被拒绝 trial 的 stage-out 替代。第一次真实 fresh-withJ 返回后，会按原73完整捕获规则保存全部十份数组，包括真实新的 stage-out 和所有576个 J 块。

实际91没有附旧 ready/capacity 的完整 payload。本入口不声称重新审计不存在的旧 payload：原 TrueTailClient 检查自己的真实 constructor/ready/capacity，新入口保存新完整记录，并核对原91保留的完整数学 source/config/parameters、原九个 physical rawNode 边界、576个 cell/profile、graphs/gains/far。旧失败状态不写入 `last` 或 `tangentPredictor`，不创建非零响应缓存。

## 3. 完整有限模型及一个词的作用域

令 $x$ 为固定实际基点，$h$ 为新候选方向，唯一非零数值坐标为 $h_{11,75}$。候选状态词取正数原词的 uint64 前一个值，方向增量取这两个有限数的精确差。Actions 实际检查这个差可被 binary64 精确表示，并检查原单位 trial 的 `x + h` 确实到达该邻词。

完整原模型为

$$
\begin{aligned}
q_{\mathrm{cut}}(h)&=r_{\mathrm{cut}}+h_{0,Q},\\
q_n(h)&=r_n+J_n h_{n+1}-h_n,\qquad 0\le n<576,\\
q_{\mathrm{far}}(h)&=r_{\mathrm{far}}+h_{576,\Pi}-G h_{576,Q}.
\end{aligned}
$$

本稀疏方向的非零线性改变量只可能位于 stage10 的全部224个输出行，以及 stage11 的第75行负单位项：

$$
\Delta q_{10,j}=J_{10,j,75}h_{11,75},\qquad
\Delta q_{11,75}=-h_{11,75}.
$$

其余行保留真实原 residual，不能删掉。所有129248行按原顺序与原正尺度比较：cut使用 $\sigma_0$；stage $n$ 使用 $\sigma_n$；far使用 $\sigma_{576}$。完整行账逐行保存精确有限二进制数据所定义的有理数仿射值及最大值位置。该精确算术仅针对保存的有限数组；不宣称 J 是 IEEE 程序的精确导数，也不宣称真实 native norm 等于这个有理数最大值的舍入。

这不是把旧完整 QR 方向截断、投影或清零。它是一个新的独立稀疏提案。后续 QR 仍保全所有129248未知、全部原方程、所有577节点的正则项、pure constants 和完整原精确线性读回。新 proposal result/checkpoint 使用独立 schema，绝不标成 R273 解。

对未改变坐标，普通 `+0` 可能改掉原 `-0` 的词身份。因此完整方向在原负零处保存 `-0`，其他未改变处保存 `+0`。完整577×224 delta、负零 sidecar、完整单位候选状态和所有 SHA 都保存。Hook 还用实际 JavaScript 的原单位 trial 表达式逐字核对全状态，确认只有 node11/Q76 一词变化。原后续 $1/2,\ldots,1/512$ trial 的实际舍入及接受结果由原十档程序真实执行，不从模型推断。

## 4. 首次 fresh 模型、原循环和后续完整 QR

1. Parent binder 验全部原件，保存原完整模型筛选，不启动 native 请求。
2. 创建一个原 TrueTailClient 和空响应缓存。新 hook 在原 worker 的首次 initial 赋值处恢复完整 BASE；没有 checkpoint 重采样、入口 Q0 替换、cut/far 清零或 H 阈值化。
3. 原迭代0首先完整调用原 evaluate(withJ)。冻结的 `f9b292c4…` noJ-primal variational implementation 与 actual73相同，原 root/RHS/rk4 和 noJ map不改。
4. 原 correction 调用处捕获真实10数组；candidate 子进程使用新 snapshot/source/context/manifest 和 full J 身份，检查全部当前数组。旧 J只用于旧模型的候选筛选，不能充当新 J。
5. 如旧、新两完整模型均预测严格下降，返回新一词 direction。若未选中，则在**同一个 snapshot**调用原完整 R273 QR。若子进程或身份核对出工程错误，则保留 partial报告/原输入并如实失败，不伪装成数值拒绝。
6. 原十档 noJ trial、原域与原 norm 判断执行。第一词占原 iteration0。若接受，迭代1及以后均fresh-withJ→完整R273 QR；若原十档拒绝，则原异常直接返回。没有额外试探或自动新方向重试。
7. 原循环可能在任意实际满足容差处正常停止；也可能达到原32上限或原失败出口。最终原 endpoint sensitivity、full Jacobian 和 audit 保留。

所有 child stdout/stderr落独立 iteration文件，不进入 worker JSON协议。返回 `maxChartCondition:null` 如实表示新方向没有计算原消元图条件数，不能填0或冒原 chart。第一 proposal 和后续 R273 返回数分别记录，最终 `native_accepted` 仍以原 TrueTailClient 完整成功响应为依据。

## 5. 源码职责与 schema

| 新文件 | 职责 |
|---|---|
| `root_20261115_fetch_native_word_parent91.py` | 完整实际91固定取件，复用冻结512247 transport |
| `exact_20261115_native_word_first_parent.py` | 完整父来源、八输入、原整模型一词筛选及全部原件保全 |
| `exact_20261115_native_word_first_current576_system.py` | 新来源身份下的完整fresh576数学数组接口；原组装算法保留 |
| `exact_20261115_native_word_first_current576_chain_qr.py` | 后续或首步fallback的完整原R273；仅身份包装改变 |
| `exact_20261115_native_word_first_candidate.py` | 真实首次snapshot上的完整一词筛选与完整delta/checkpoint |
| `geometry_20261115_native_word_first_current576_solve_hook.mjs` | 原initial赋值、唯一correction调用桥、原源码可逆核、候选/QR接续 |
| `geometry_20261115_native_word_first_current576_solve.py` | 一次live原client所有权、父核、配置、完整响应/失败和finally关闭 |

新的顶层结果为 `native-word-first-current576-damped-solve-result-v1`。新的首候选结果为 `native-word-first-complete-current576-proposal-v1`；新的父为 `actual73-failed-current-base-via-complete-actual91-v1`。每个current snapshot和adapter/QR都有 `word-first` 身份，包含这次实际 source、fresh snapshot、全矩阵及状态 SHA；不会重标签旧73 output。

七份完整冻结SHA/大小位于同目录 `frozen-files.json`。四份相对冻结73的完整diff也在同目录，文件名为对应新source basename加 `.diff`。旧四source没有修改。

## 6. CLI 与唯一 Actions 草稿

取件：

```bash
python -u computations/root_20261115_fetch_native_word_parent91.py \
  --run-id 43672150224 \
  --artifact-id 14145200674 \
  --artifact-name visible-mainline-modelresponse-43672150224-1 \
  --expected-size 10267458 \
  --expected-sha256 78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6 \
  --out "$RUNNER_TEMP/actual91-word-first-parent"
```

原32循环由既有规则 runner包住：

```bash
python -u computations/root_20261114_current576_rules_runner.py \
  --out "$VISIBLE_OUT/rule-sync" --command \
  python -u computations/geometry_20261115_native_word_first_current576_solve.py \
  --original91-directory "$RUNNER_TEMP/actual91-word-first-parent" \
  --source-topic "$VISIBLE_SOURCE_TOPIC" \
  --eta 1 --node-heap 6144 --exact-workers 2 \
  --max-factor-bytes 2147483648 \
  --out "$VISIBLE_OUT/native-word-first-current576"
```

唯一新workflow草稿为 `/tmp/visible-larger-request95/visible-larger-public-native-word-first.yml`，拟入 `.github/workflows/`。唯一request为同目录 `public-native-word-first-request.json`，拟入题目录 `computations/`。只有该request路径的main push触发，没有第二个dispatch。沿现有 `current576native` publisher route，artifact名为 `visible-mainline-nativewordfirst-<actual-run>-<attempt>`；此处没有虚填未来run或结果。

环境沿原73：Python3.12.14、NumPy2.3.5、SciPy1.17.0、Node24.22.1、数值库单线程、原公共78源恢复。24源pin包括七新源、四冻结73基线源、原91producer证据、原QR/精确kernel、真实client、transport、规则runner和publisher。前置编译是源完整性检查，不执行科学。

原运行资源合同沿350分钟job、320分钟native步骤、32 GiB可用空间、Node6144 MiB、单次factor上限2147483648 B、精确读回2workers。新输入只需完整91的约10MB ZIP，避免为同一原chunk重新下载旧73约1.75GB ZIP。空间不足/工程timeout只按真实工程失败保全，不缩减原32预算或修改数学容差。

## 7. 输出保全与读回次序

主结果先读 `native-word-first-current576/result.json`、`current-correction-summary.json`、原 `native_0001.json.gz`、`native_trace.jsonl`、`native_trials.jsonl` 和当前iteration。它们分别回答原请求是否实际成功、首词是否入选、哪一档真实接受、后续QR是否运行、当前真实残差和实际失败位置。不能仅凭 `selected_for_original_trials=true` 或exact模型下降报告声称native进展。

`parent91/`保完整旧证据及旧整模型；`iteration-000/snapshot/`保存首次完整真实10输入；`word-candidate/`保存新提案、full delta/checkpoint、单位state和fresh整模型；`qr/`只在真的执行QR时存在。后续每轮都保存真实snapshot/QR输出，所有原J、factor、pure constants和exact行账留完整artifact。旧、新完整129248模型JSONL行账放各自`large-arrays/`，由publisher按原artifact-only规则处理，不为Git大小截断科学对象。

代码未伪造旧完整factor已导出、旧完整J重新核过、旧ready/capacity逐字重新核过，或旧base-stage-out存在。所有这些范围必须在后续实际读回中继续保持。完整原source配置不等于浮点映射导数的认证；一词模型下降也不等于原noJ域/范数下降。

## 8. 已完成的静态检查与未支付部分

本地只做源码/原JSON/原字节操作，未导入任何本数学模块、未运行Fraction科学算术、NumPy/SciPy、RHS/J/ODE、native或QR。检查包括七source AST/Node语法、69条源码与实际父字节合同；adapter完整数组访问和组装AST、QR全部函数AST在声明的身份元数据改名后与冻结73一致。

纯源字符串往返还核过原engine/worker变换：完整evaluate与十档trial原文字节一致，唯一core变化是原correction调用；原initial附近只插入一次恢复来源，不改其它request逻辑。结果保存为 `source-and-byte-static-check.json`、`pure-source-roundtrip.json`。唯一workflow的24源、9个shell和4段inline Python亦只做字节/语法检查。

以上检查没有支付一次新的科学执行。新候选、fresh模型筛选、实际原trial、后续QR及最终audit必须由拟发布的公开Actions真实输出回答。

## 9. 公开库保存名

源交付清单在公开库保存为 [2026-11-15-native-word-first-source-files.json](2026-11-15-native-word-first-source-files.json)。源合同、纯源往返、工作流合同分别保存为 [request95源码字节核](2026-11-15-request95-source-and-byte-static-check.json)、[request95纯源往返](2026-11-15-request95-pure-source-roundtrip.json)、[request95接线核](2026-11-15-request95-workflow-static-check.json)。[主控完整静态读回](2026-11-15-request95-root-static-readback.json)另核24实际sourcepins、四diff字节、69源合同、47接线项及原evaluate/十trial逐字保留。此段仅说明保存名，七个冻结科学/运输源均未改写。
