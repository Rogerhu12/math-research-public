# Actual73 → request83：实际 rounded 试步的完整精确分解接口

类型：计算接口与有限数组代数说明；尚无 request83 数值结论。  
作者：exact_refinement（与 geometry 的原 noJ 单次回放合同对接）。  
日期：2026-11-15 UTC。

## 1. 目的和已付输入

actual73 最后一轮的十个原步长均有严格的有限矩阵 affine 无穷范数下降预测，但原十次 noJ 试探全部拒绝；最后三个原标量等于基态值。这两个已经发生的事实由完整 actual73/R276 读回报告保存。本入口固定原最后一轮、原方向和原第九个试步索引，即 $\alpha=2^{-9}=1/512$。geometry 的独立 probe 只进行一次原 `evaluate(false)`，保存原 JavaScript 表达式实际形成的 577 个节点状态以及全部返回 residual。此消费者读取这些原件，不再次调用 noJ。

新消费者的唯一完整矩阵作用是保存的 $A$ 对实际状态差 $h$ 的作用。理想 $\alpha\delta$ 的作用沿用已保存的有符号 $e=r+A\delta$ 整数账，不重新计算 $A\delta$。不重求 $J$、ODE、root、RHS、QR，不更改 $\eta$、步长、约束、原 native 容差或任何接受条件。所有新精确算术仅在 `GITHUB_ACTIONS=true` 且 `GITHUB_REPOSITORY=Rogerhu12/math-research-public` 的公开 Actions 中执行。

源码：`computations/exact_20261115_native_realized_step_affine_decomposition.py`。

- 字节数：52,459。
- SHA256：`3570aa9f6bb3b24eb28678a57f88b145a8725a3a7bda05fe14a0860e136c917d`。
- 顶层结果 schema：`actual73-realized-step-complete-exact-affine-decomposition-v1`。
- 本地只做源码阅读、Python AST、原已有小报告字段和文件 SHA 核对；没有 import 此模块，没有执行数值、toy、norm 或 Fraction 测试。

## 2. 完整有限系统和精确分解

记 $x$ 为 actual73 最后 snapshot 的保存状态，$\delta$ 为该轮原返回完整方向。$\widetilde x$ 是本次 probe 用原表达式实际生成并送入原 noJ 的 binary64 状态。所有保存 binary64 数均按其原 IEEE 位解释为精确 dyadic 实数。定义

$$
h=\widetilde x-x,\qquad q=h-\alpha\delta.
$$

这里的减法在整数／二进制指数表示上精确完成，不先做 binary64 的 `trial-base`，也不把 $h$ 再舍入成一个浮点数组。负零与正零作为实数同为零，但原输入 raw bytes、各节点 slice SHA 和负零计数均保留。

原完整 residual 行数为 $112+576\cdot224+112=129248$，节点坐标数恰也为 $577\cdot224=129248$。线性作用按原 shooting 方向写为

$$
(Ah)_{\mathrm{cut},j}=h_{0,Q,j},
$$

$$
(Ah)_{n,i}=\sum_{j=0}^{223}J_{n,ij}h_{n+1,j}-h_{n,i},\qquad 0\le n<576,
$$

$$
(Ah)_{\mathrm{far},j}=h_{576,\Pi,j}-G_jh_{576,Q,j}.
$$

全部 $224\times224$ stage block、所有非零模式、完整 cut 和 far 都保留。$J$ 取该轮新 noJ-primal withJ 保存矩阵；不借用 actual28、1372 或其他轮的矩阵。$r$ 是该轮原保存 residual，$t$ 是新 probe 原返回 residual，包含保存的 cut 和 far。原正数尺度逐行沿用：cut 用 $\sigma_0$，stage $n$ 用 $\sigma_n$，far 用 $\sigma_{576}$。

定义理想和实际状态差对应的两个 affine 对象

$$
m=r+\alpha A\delta=(1-\alpha)r+\alpha e,
\qquad a=r+Ah,
\qquad e=r+A\delta.
$$

消费者逐行输出

$$
s=a-m=A(h-\alpha\delta),\qquad
f=t-a,\qquad
d=t-m=s+f.
$$

证明只用同一保存矩阵的线性性：从 $e-r=A\delta$ 得到 $m=r+\alpha A\delta$；随后 $a-m=Ah-\alpha A\delta=Aq$，而 $(a-m)+(t-a)=t-m$。每一个分量均作精确整数恒等式核，不只比较两个最大值。除以同一正 $\sigma_i$ 后恒等式仍成立。

字段名 `state_addition_term` 指 $s$。这个名称包括原 `v + alpha * delta` 的整个状态形成效应：乘法、加法和存入 `Float64Array`。本入口没有分别保存每个中间浮点结果，因此不把 $s$ 解释成单独一次加法的误差。即使 $\alpha$ 为二的幂，也不假定任意 subnormal 乘法都精确。

字段名 `remaining_flow_tangent_model_term` 指 $f$。它合并实际 noJ residual 和保存 affine 模型之间余下的全部差异；仅凭它不能唯一分辨真实非线性余项、原 root 返回误差、保存 $J$ 的导数误差、传播和 residual 形成舍入等来源。$A$ 未被宣称为原数学 flow 的精确导数。

`trial-mean-height-increments` 的 576 个实际原值作为完整 probe 输入保存／核字节，不作为额外 native residual 方程加入上述 129248 行。

## 3. 整数表示与完整作用规模

复用冻结 `exact_20261114_native_allrows_dyadic_residual.py` 的 `stage_job`、`boundary_job`、`decoded_array`，不调用其 actual28 入口或历史 binder。所有当前数据显式作为参数传入；该复用只复用整数核，不复用其历史 matrix identity。

任意有限 binary64 是 $2^{-1074}$ 的整数倍。两个有限 binary64 的精确差 $h$ 也是该格点的整数倍，尽管通常不能用单个 binary64 精确表示。于是每个 $J_{ij}h_j$ 都是 $2^{-2148}$ 的整数倍。核中相乘、对齐二次幂和求和均是整数操作。

用核单位 $u=2^{-2148}$，记 $r=Ru,e=Eu,a=Hu,t=Tu$。统一比较单位取 $u/512=2^{-2157}$，八个完整输出向量的整数系数是：

| 输出字段 | 公共单位 $2^{-2157}$ 下的系数 |
|---|---|
| `stored_base_residual` | $512R$ |
| `saved_direction_endpoint` | $512E$ |
| `ideal_affine_residual` | $511R+E$ |
| `realized_affine_residual` | $512H$ |
| `stored_trial_residual` | $512T$ |
| `state_addition_term` | $512H-(511R+E)$ |
| `remaining_flow_tangent_model_term` | $512T-512H$ |
| `total_trial_minus_ideal` | $512T-(511R+E)$ |

若实际保存尺度 $\sigma=S u$，则归一值为上述系数除以 $512S$。整数比较没有先形成舍入后的 $J/\sigma$ 或 $r/\sigma$，也没有以普通 float dot 替代原行和。

`stage_job` 接受一般整数／指数对，故 $h$ 不受 53-bit mantissa 的限制。核返回值的解码使用一个独立的 4205-bit 表示上界：$|h|<2^{1025}$、$|J|<2^{1024}$，224 个乘积以及两个加法项之和的幅度小于 $2^{2057}$；以 $2^{-2148}$ 为单位，其整数绝对值小于 $2^{4205}$。这只是由有限 IEEE 输入推导的格式上界，不是残差大小阈值。旧 $e$ ledger 仍由冻结 R276 的原 4204-bit 解码器读取，因为它原本对应有限 binary64 $\delta$。

新作用遍历全部 576 个完整 stage block 和 far 的 112 个对角乘积，共沿原报告口径 28,901,488 个 product positions。零系数可以在冻结核内省略整数乘法，但所有原 J words 都经过解码／遍历，完整 J raw SHA 和逐 block SHA 均核对。

## 4. 固定 actual73 和已完成 R276 身份

原公开 run `43657001633`，source commit `9515d5aaf7c68f8efd366438d6bd81ce73c3486f`。

| 对象 | SHA256 |
|---|---|
| 原完整73 ZIP（1,752,742,419 B；artifact14141540502） | `3430597bc72c02c387b62fd908b229c87c7caa01d4d14e2599c66f834480eef9` |
| native 根 `result.json` | `ade4fdac3adce104cb4e216e9d2f40b219bfca47d2c027ac548e6c65f65ab394` |
| iteration002 snapshot `result.json` | `2f9bf170c0366e9d5adaf003a9d0746f28a536171a32339e8a5f502313495e92` |
| iteration002 QR `result.json.gz` | `9d464f8239c375a2e95f207a3cfbad33e1f36037cd450cfefa2e3b165d86e3ff` |
| 完整577基态 raw | `f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6` |
| 完整577原方向 raw | `4b4b1aaacd96910635a03f97d45957ae995c724997a0e18b66ac1d06408e294a` |
| 完整576当前 J raw 流 | `1f5e3cfd7d7fec8c127841c3c859b43ed4264e55c7bf7805e84f4dae73b453d4` |
| 当前完整矩阵 canonical identity | `6ea4b16fa7e41ae1099a3e792b67c19cf6c9d4ae41f5c3209fa84d43c5f8fbd8` |
| 原 exact full report | `36a0a1fde40e95ce7e33f18bc55d68d0fa16c30f6132429aa6feb39a71111a97` |
| 原129248行 signed-$e$ gzip ledger | `2d3f377c0126562375420bb174ced9d5d6b8201beae8fd3efda8d9a4a8fa94c4` |
| 已完成R276 iteration002 原gzip（12,153 B） | `b7812e06716bb1d22d4d32ff6ca12c62cb926dd9df12f41c199988f933ccd029` |

最后一件已经逐原压缩 bytes 另存为本课题公开输入 `notes/2026-11-15-actual73-r276-iteration002-original.json.gz`。它不是重算的 R276 报告。新消费者核 baseline、选择的 $1/512$ 全局预测及 cut/stage/far 三类最大值与该原报告的精确有理数和坐标完全一致。此检查用于保证同一输入对象与索引，没有用数值大小决定原 native 是否接受。

selected fetch 沿原 tree 提取 root metadata／原 trials／correction journal、最后 snapshot 的十个完整数组、最后 QR result/binding/manifest/checkpoint/delta、九个 QR `original_arrays` 副本、原 exact full report 和 signed ledger。不会取回 QR factors 或纯常数 payload。完整 ZIP 的固定大小和 SHA、GitHub run/artifact metadata 以及安全路径／CRC，由 geometry 的独立固定 transport 负责。

## 5. 新 probe 输入合同

新 producer 运行结果必须由同一 Actions 中实际生成的 `result.json` SHA 显式传入。没有未来 run、artifact 或输出 SHA 占位身份。

冻结 producer：

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261115_native_realized_trial_probe.py` | 30,617 | `305f5db2c6bc0fef85bd3115045531b1b366334b33300852634692a537f7d9cb` |
| `geometry_20261115_native_realized_trial_probe_hook.mjs` | 37,135 | `c03f59e4c3b6555a7a47187f1905a70f1e5a92dafacc222c327f4913c3ccdce0` |
| `geometry_20261115_fetch_actual73_realized_selected.py` | 17,288 | `51f865285ab348792842a3d1419135fd1c9ae8ece5c853d13776f252e43d4056` |

probe 顶层 schema 为 `actual73-iteration2-realized-noJ-trial-probe-result-v1`。`summary`、`input_binding`、`array_manifest`、`specification` 都是真实 `{file,bytes,sha256}` 描述符。消费者先保原 result/summary 的原 bytes 和失败事实，再要求完整数学操作数。若原 noJ 没有完整返回，精确分解不伪造缺失 residual；保存真实错误和已存在的原结果。

完成路径核原 noJ 计数为 1、native solve/new J/new withJ/new correction 为 0，全部576 flow 返回，原输入不被观察器改动，原 cut/far 未投影。新 noJ norm 与旧 actual73 第九试步 norm 的 bit 相等性只作为输出字段；不要求相等，不要求新 norm 下降。

`array-manifest.json` 的 schema 是 `actual73-iteration2-realized-noJ-trial-output-arrays-v1`，`arrays` 为完整单文件 `<f8`、C-order 描述符列表。数学消费这15项：

| 数组名 | 完整 shape | 用途 |
|---|---|---|
| `base-states`, `native-delta`, `trial-states` | `[577,224]` | 精确 $h$、理想增量和原方向身份 |
| `original-scales` | `[1,577]` | 全部原 $\sigma$ |
| `cut-target`, `physical-height`, `original-far-graph` | `[1,112]` | 原边界与输入身份 |
| `saved-stage-residuals` | `[576,224]` | 原 $r$ |
| `saved-cut-residual`, `saved-end-residual` | `[1,112]` | 原边界 residual |
| `trial-stage-out`, `trial-stage-residuals` | `[576,224]` | 原返回 out 的字节身份及实际 $t$ |
| `trial-cut-residual`, `trial-end-residual` | `[1,112]` | 实际边界 residual |
| `trial-mean-height-increments` | `[1,576]` | 完整原返回旁证，不增 native 方程 |

所有数学操作数要求保存的有限 IEEE 数；这个实数定义要求与完整输入身份检查不是新增 native 接受条件。原 norm numberRecord 可忠实保留 nonfinite 分类，其与精确有理 norm 的比较仅在该原标量有限时形成。root 返回观察包、误差／尺度等旁证由 probe 保存，本消费者不再次读取大 root packet 或推断唯一误差来源。

## 6. 科学源码闭包和复用边界

除本新 consumer 和上一节两个 producer 源外，同目录必须有如下9个冻结源。只有两个带“import”标记的纯标准库模块被本消费者动态导入；其余用于原 profile 的完整 source receipt 核对，不调用其 scientific main 或构造器。

| 文件 | SHA256 | 范围 |
|---|---|---|
| `exact_20261115_native_affine_infinity_prediction.py` | `bd4ff360cb27750a98bb9966981949f89d6b6dcf607fd820c34bb71adee9cde4` | import：身份 binder、文件 I/O、精确比值展示；不调用 main/predict |
| `exact_20261114_native_allrows_dyadic_residual.py` | `0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f` | import：完整整数 stage/boundary 核；不调用 historical main |
| `exact_20261114_native_damped_chain_qr.py` | `9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33` | 只 source receipt |
| `geometry_20261114_native_captured_band_correction.py` | `b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390` | 只 source receipt |
| `geometry_20261114_noj_primal_current576_damped_solve.py` | `938fbec22f0733fff6ceb22e6e9b7a9e12942c12d1eae31c608d8f517702df8c` | 原73 producer receipt |
| `geometry_20261114_noj_primal_current576_damped_solve_hook.mjs` | `099798e9c57f09b82f7532ea184d124446aeeb2cdbafe452390cb794b8db405d` | 原73 hook receipt |
| `exact_20261114_noj_primal_current576_damped_system.py` | `48297483617c56179fdd4d6b80e9aeeb1151bf89c90fd816ca41d2e3ccc0bcb3` | 原73 binder receipt |
| `exact_20261114_noj_primal_current576_damped_chain_qr.py` | `70bc10dfb31717b662265485d10a15028365dbba5db85ccf9c8f592226e33955` | 原73 direction receipt |
| `geometry_20261114_noj_matched_variational_engine.mjs` | `f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9` | 原73新 flow receipt |

只运行本 consumer 不需要 NumPy/SciPy，不需要新的78源恢复，不调用 native worker。整个83 job的原 probe仍依赖其已经声明的原78恢复、client/runtime和source环境。它们由 probe/workflow的完整 closure核对；本表不冒充整个job仅需这些文件。

## 7. 最小 Actions 命令

先运行固定 selected transport 和 geometry 的单次 probe。随后从该 probe 的实际 `result.json` 原 bytes 得出 SHA，并作为此命令参数。`ACTUAL_PROBE_RESULT_SHA256` 是运行时值，不是预写的科学结果。

```bash
python "$TOPIC/computations/exact_20261115_native_realized_step_affine_decomposition.py" \
  --native-directory "$SELECTED73/native-noj-primal-current576-damped" \
  --native-result-sha256 ade4fdac3adce104cb4e216e9d2f40b219bfca47d2c027ac548e6c65f65ab394 \
  --probe-directory "$VISIBLE_OUT/actual73-realized-trial" \
  --probe-result-sha256 "$ACTUAL_PROBE_RESULT_SHA256" \
  --r276-reference "$TOPIC/notes/2026-11-15-actual73-r276-iteration002-original.json.gz" \
  --r276-reference-sha256 b7812e06716bb1d22d4d32ff6ca12c62cb926dd9df12f41c199988f933ccd029 \
  --workers 2 \
  --budget-seconds 1800 \
  --out "$VISIBLE_OUT/actual73-exact-realized-step"
```

`--out` 必须全新且与三个输入根互不包含。`--workers` 支持1–4，默认2；进程使用 `spawn`，最多预提交 `2*workers` 个完整stage。资源截止在节点／stage块边界检查。已经启动的有限块和 gzip/receipt 收尾可能越过该软截止；不声称是硬秒级杀进程。父进程和子进程实际 RSS 分开记录，不能把两者简单相加当同时峰值。

默认1800秒是诊断资源预算，不是科学容差。没有提前试算来选择预算，也没有预造运行时长或内存读数。J 流按原4-stage chunk读取，约1.6MB单chunk；$h$ 保完整129248整数／指数对，队列有限。输出大小由实际整数长度和gzip压缩决定。完整有理 ledger不作为小JSON塞入Git；各原件可流式写入 `large-arrays`。此入口不需要重新取1.75GBZIP，直接复用同一次已经验证的selected提取根。

## 8. 完整输出与 partial 事实

| 路径 | 内容 |
|---|---|
| `summary.json` | 完整/partial状态、计数、原身份、主要精确最大值及原noJ scalar对照；大整数必要时缩成坐标和原精确比值的十进制展示，完整比值仍在fullreport |
| `original-native-outcome.json` | 诊断开始前的原73失败及原最后十trial，不改变原结果 |
| `original-probe-result.json`, `original-probe-summary.json` | 新probe对应原文件的逐原bytes副本（summary存在才复制） |
| `original-probe-outcome.json` | 新probe真实结果与summary的明确语义记录，先于新精确算术保全 |
| `increment-status.json`, `decomposition-status.json`, `progress.json` | 全部完成范围／实际partial计数／资源错误 |
| `large-arrays/complete-exact-realized-increments.jsonl.gz` | 577有序节点、全129248坐标的精确 $h$、$\alpha\delta$、$q$，各原node raw SHA及负零／字节变化计数 |
| `large-arrays/complete-original-row-decomposition.jsonl.gz` | cut+576stage+far共578块、每一原行全部八个精确dyadic对象、原sigma bits、旧e源行hash和新J块hash |
| `large-arrays/complete-original-block-maxima.jsonl.gz` | 全578块各八向量的精确原sigma最大值 |
| `large-arrays/input-binding.json.gz` | 全原矩阵／provenance、原R276文件、新probe完整输入binding／manifest |
| `large-arrays/complete-input-file-receipts.json.gz` | 实际读取的所有原文件大小和SHA；未读factor明确记录 |
| `large-arrays/result.json.gz` | 完整结果、全部global/family精确比值、最坏行的八分量、watched行、原科学outcome、partial范围和运行资源 |

所有八向量都有完整全局及 cut/stage/far 最大值、原坐标、精确有理数、tie count；tie按最小原global equation row取。原 noJ 的扫描顺序或 binary64 除法可能产生不同的等值／近等值坐标，原probe最坏行仍另保，不静默改标签。

watched全局行2539是actual73末轮原最大 residual 行；2762是较早同state noJ/withJ比较中的历史行；2128是该方向原 exact endpoint 最大缺陷行。全部行同时输出，不把这三个点代替全系统。

`norm_readback` 区分精确 $\|m/\sigma\|_\infty$、$\|a/\sigma\|_\infty$、$\|t/\sigma\|_\infty$，给出相对原精确baseline和原binary64baseline的比较。标量norm差和分量向量 $s,f,d$ 分别命名；norm差不被冒充余项向量。十进制64位展示不是区间包围，只用于阅读，全部比较用整数交叉乘法。

每个gzip ledger在正常或异常退出时关闭并记录压缩／解压hash及已写块数。资源耗尽或身份错误产生非零诊断退出码、`diagnostic_completed=false`及真实partial；不把partial最大值标为全系统最大。若原probe未返回完整residual，保其原结果和错误，不补造新noJ或缺失行。后续workflow可始终上传这些原件；诊断状态不改任何已有native接受／失败状态。

## 9. 可支持和不能支持的结论

只有实际运行返回以后，才能据精确八向量判读该固定试步的状态形成项与剩余项各自在原sigma口径中的大小、符号和所在行，及实际状态差的affine预测是否仍下降。若二者在某些行互相抵消，完整分量账会直接保留这种抵消，不能通过两个独立最大值的差去猜。

本入口不会直接证明哪个root误差、哪个连续导数或哪个非线性项是唯一原因；也不从一条行的ULP间距推出原2e−9不可达。没有新方向、新步长、新η、新优化或新增科学验收。后续变更若有必要，由这次真实输出支持，不能把其尚未运行的输出当成既成结果。

主控全文读源/接口；发布版只对齐实际合并workflow的CLI输出名。原接口19263B/b7f3e3a52d17d6e3026b345f93b9349504bd4ee09a6261d663dfd9289a7b46aa；源码3570aa9f不变。
