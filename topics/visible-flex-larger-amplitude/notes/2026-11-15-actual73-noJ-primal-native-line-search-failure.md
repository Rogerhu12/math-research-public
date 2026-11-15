# 第 73 轮：noJ-primal 原生续解的实际线搜索失败及完整原件读回

- 作者：geometry（AI 辅助）。
- 日期：2026-11-15 UTC。
- 分类：公开 Actions 实际回执、原生非线性迭代结果与字节身份；不是新的数学接受条件。
- 状态：已读原始响应、全部 trace/trials、三轮子进程小文件与失败 checkpoint；本 note 范围的 104 项字节／字段检查全部通过。原生求解未完成，完整尾匹配、最终端点 J 和最终 audit 均未取得成功响应。

## 1. 实际结论及其精确范围

第 73 轮确实从第 61 轮最后一个失败状态启动了新原生请求。它采用独立的 noJ-primal 变分实现，每轮重新取得完整 576 段 withJ，并调用原尺度、完整边界行的 R273 阻尼链校正（本次显式 `eta=1`）。三轮分别产生了新的快照、矩阵身份和完整 577×224 方向；没有把第 28 轮或第 61 轮的旧基态/J 改标签后复用。原生请求中的全部 112 项非零高度仍按原值传入，未作阈值归零。

原十步回溯在前两轮接受了 `1/2` 和 `1/64`，第三轮的十个试步均返回了完整原范数，但没有一个严格小于该轮基态。原生 worker 返回的确切错误为：

```text
Error: multiple-shooting line search failed at 0.000060618737006888706
```

失败响应的原 `lastIteration` 为：

```json
{"iteration":2,"norm":0.000060618737006888706,"minA":0.9999999999759498,"minD":0.9999999999999858,"chartCondition":null}
```

这里 `chartCondition=null` 表示本次 R273 校正没有计算旧 Riccati 图条件数；不是已观察到奇异图。19 次实际 noJ 试步中没有域、D/S/A 或 momentum-root 拒绝，全部具有原 `trialNorm`。科学失败点是第 2 轮原有的严格范数下降判断全部不通过，不能写成“原 guard 拒绝”或“子进程失败”。[原始逐字段读回](2026-11-15-actual73-complete-original-native-readout.json.gz)保留了失败响应、完整 trace 和全部 19 条 trial，字节回执见[审计文件](2026-11-15-actual73-original-native-packet-byte-audit.json)。

原容差 `2e-9`、最大 32 次非线性迭代、每轮最多 10 个 `2^(-k)` 试步都保持原值。真实停止发生在 `iteration=2` 的线搜索中，未达到 32 轮预算，也没有到达尾解成功返回后的 `cutJets`、最终 `audit` 或 `heightJetJacobian`。请求中的 `jacobian=true, audit=true` 只说明这些工作被请求，不能写成已经完成。

## 2. 两层实际公开来源

| 对象 | 原始身份 |
|---|---|
| 第 73 轮 source | `9515d5aaf7c68f8efd366438d6bd81ce73c3486f` |
| 第 73 轮 run / job | `43657001633` / `132637631246` |
| 原 artifact | `14141540502`，`visible-mainline-nojprimalnative-43657001633-1` |
| 原 ZIP bytes / SHA256 | `1752742419` / `3430597bc72c02c387b62fd908b229c87c7caa01d4d14e2599c66f834480eef9` |
| 完整原件 reader source | `4a2824deaf68a6fd1a55ae464aa87737956a42f7` |
| reader run / job | `43664753410` / `132661544403`，SUCCESS |
| reader artifact | `14142311462`，`visible-completed-readback-43664753410-1` |
| reader ZIP bytes / SHA256 | `4389973` / `e75cb8837efc6779d0f3a24df892bcc42928a25dca950f2bf594ba3b7abecf55` |

公开运行可直接定位：[原生第 73 轮](https://github.com/Rogerhu12/math-research-public/actions/runs/43657001633)、[完整字节读回](https://github.com/Rogerhu12/math-research-public/actions/runs/43664753410)。原大 artifact 的下载、完整数组审计及 R276 精确计算只在公开 Actions reader 内进行。本地仅消费 root 唯一下载并核定大小、ZIP SHA、CRC 和完成 marker 的小 reader artifact，没有第二次下载原 1.75 GB 包，也没有执行科学数值。

reader 的 `request73-readback/large-arrays/original-native-packets/` 保存本 note 使用的原始相对路径和 gzip 字节。其 35 件清单压缩 SHA 为 `8ccda84a131c166644e3db550bbf334adeaa16bd8ac8cec9620c843009fc3cdb`，解压清单 SHA 为 `8cd08c24dd50385de214bb4c36bcfb8f720b1d761e91232ea1028a749d4b638c`。这些是原件复制，既没有用 QR 摘要代替原 native trial，也没有从失败日志补造未导出的数值数组。

## 3. 完整实际迭代与全部试步

原 trace 的三次 fresh-withJ 基态分别为：

| 原 iteration | 原基态范数 | float64 little-endian bits | 本轮实际接受 |
|---:|---:|---|---|
| 0 | `0.000103579366549043` | `b162acf717271b3f` | trial 1，`alpha=1/2` |
| 1 | `0.00006749978282929229` | `c5655f70d5b1113f` | trial 6，`alpha=1/64` |
| 2 | `0.000060618737006888706` | `71f299f11bc80f3f` | 十步全拒 |

第 0 轮接受的 noJ 范数与第 1 轮实际 fresh-withJ 基态范数逐位一致；第 1 轮接受的 noJ 范数与第 2 轮实际 fresh-withJ 基态范数也逐位一致。这是本次实际两对读数的事实，不能扩大为所有未来状态必然重复，也不能把此前第 61 轮不同 primal 路径的读数差继续当成本次已观察原因。

下面逐条照录原 `native_trials.jsonl` 的 `trialNorm`。trial 索引从 0 开始；所有 call 均为 1。

| iteration | trial | alpha | 原 trialNorm | 原分类 |
|---:|---:|---:|---:|---|
| 0 | 0 | 1 | `0.000152014583766289` | residual-not-decreasing |
| 0 | 1 | 1/2 | `0.00006749978282929229` | accepted |
| 1 | 0 | 1 | `0.00010897587112785563` | residual-not-decreasing |
| 1 | 1 | 1/2 | `0.00013090599247904327` | residual-not-decreasing |
| 1 | 2 | 1/4 | `0.00012144901300393549` | residual-not-decreasing |
| 1 | 3 | 1/8 | `0.00011814265821233656` | residual-not-decreasing |
| 1 | 4 | 1/16 | `0.00011665011013217503` | residual-not-decreasing |
| 1 | 5 | 1/32 | `0.00010632854139856965` | residual-not-decreasing |
| 1 | 6 | 1/64 | `0.000060618737006888706` | accepted |
| 2 | 0 | 1 | `0.00019266928302730032` | residual-not-decreasing |
| 2 | 1 | 1/2 | `0.00013090599247904327` | residual-not-decreasing |
| 2 | 2 | 1/4 | `0.00012144901300393549` | residual-not-decreasing |
| 2 | 3 | 1/8 | `0.00011814265821233656` | residual-not-decreasing |
| 2 | 4 | 1/16 | `0.00006569760416151993` | residual-not-decreasing |
| 2 | 5 | 1/32 | `0.00010632854139856965` | residual-not-decreasing |
| 2 | 6 | 1/64 | `0.00006848278937534994` | residual-not-decreasing |
| 2 | 7 | 1/128 | `0.000060618737006888706` | residual-not-decreasing |
| 2 | 8 | 1/256 | `0.000060618737006888706` | residual-not-decreasing |
| 2 | 9 | 1/512 | `0.000060618737006888706` | residual-not-decreasing |

因此最后三个 trial 的**标量范数**和本轮基态具有完全相同的二进制值；本次源没有导出这些 trial 的完整状态与全残差，不能据此断言“状态没变”“所有分量没变”或“只有某一个分量量化”。同样，表中不同试步出现相同标量，也不足以说明它们的完整原生输出相同。

原 trace 保留实际时序：第 0 轮 fresh-withJ 在 `00:31:39.558Z`，校正返回在 `00:32:11.023Z`，接受态记录在 `00:34:48.458Z`；第 1 轮对应 `00:52:12.857Z`、`00:52:43.975Z`、`01:01:56.138Z`；第 2 轮对应 `01:19:19.502Z`、`01:19:50.655Z`，原 failure 为 `01:32:57.176Z`。这些时间只是原 trace 字段，未用它们推算新的科学量。

## 4. 三轮真实 snapshot、方向与协议闭合

三轮状态分别为原第 61 轮失败初猜和本次两个已接受状态：

| iteration | 完整 577×224 当前状态 SHA256 | 对应新矩阵身份 SHA256 |
|---:|---|---|
| 0 | `b34daaf8ad1841b452707c669236ba38731d1f97506af4bbfe1a22e39d814013` | `3394f1eafb4a2b22400c92ebf0378a5cb37a7cdd77484bb79bcf3887ba214dfe` |
| 1 | `a45516548d6a4862da3d1a7e1c86b37a3cd97a6eed00fc34ea00ff4cbc0ee0ef` | `bcbf0e418f338e3366fdb569d4549b46ee52b64756bd9e3e13a8b12bc38e6ed0` |
| 2 | `f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6` | `6ea4b16fa7e41ae1099a3e792b67c19cf6c9d4ae41f5c3209fa84d43c5f8fbd8` |

三份实际 `qr-exit.json` 都是 `status=0`、`signal=null`、`error=null`，stderr 为空。每份 stdout 都保存 18 条因子进度、18 条完整 exact 读回进度和 1 条完成消息；每轮 `returned-correction.json` 与总 summary、JSONL、QR summary 和实际 snapshot 的 call、iteration、sequence、状态 SHA 逐字段一致。完整方向没有被投影去掉 cut/far 分量，其负零分别为 18、22、25 个；这只是源写出的字节计数，本次未局部重算任何方向。

末轮方向关键身份为：

| 末轮对象 | bytes | SHA256 |
|---|---:|---|
| snapshot/result.json | 1313 | `2f9bf170c0366e9d5adaf003a9d0746f28a536171a32339e8a5f502313495e92` |
| snapshot/context.json.gz | 8728 | `6e7c3c9d02d4caff9ea565c7898b4b1bb1baf91b2153fb782fbc8e1a411f685f` |
| snapshot/array-manifest.json | 171210 | `47e84aeae29a1736217ff3d0774d38a1dbc1a0337501c098c3f8c1820434a610` |
| qr/result.json.gz | 4596 | `9d464f8239c375a2e95f207a3cfbad33e1f36037cd450cfefa2e3b165d86e3ff` |
| qr/native-direction-checkpoint.json.gz | 1368657 | `148fd06966490b16c8a65d1f1f2595c01d49c44cc817f9fbe8510f647c4cc2f8` |
| qr/output-array-manifest.json.gz | 57490 | `3dbce9268dcb6667b2365f4c389dbc17c9e854c485b1873aa5fc222b2b0d00cf` |
| 完整原坐标 delta raw | 1033984 | `4b4b1aaacd96910635a03f97d45957ae995c724997a0e18b66ac1d06408e294a` |

本小包导出了各 manifest 的描述器，不含全部上述大数组；本地审计没有把“描述器已核”写成“payload 已独立重核”。完整 J、因子、常数、delta 与每轮 129248 行 exact ledger 的 Actions 字节审计和精确模型结论由[独立 QR/R276 note](2026-11-15-actual73-complete-QR-exact-affine-infinity-and-byte-readback.md)负责。

## 5. 失败状态可以精确定位，但不是已完成尾响应

`native_0001.json.gz` 的失败 checkpoint 与 `native_iteration.json.gz` 中最近进度 checkpoint 的全部状态字面值、rawStates 和数值元数据相同，仅 scope 文本不同。两者均有完整 577 个节点，每节点 224 个有限 binary64 数；物理边界索引严格为：

```text
[0,72,144,216,288,360,432,504,576]
```

9 个 `rawStates` 与对应完整节点逐字节一致。将原 JSON 已保存的状态字面值打包成 little-endian binary64，得到 1033984 字节和 SHA `f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6`，恰与末轮实际 snapshot 的 raw 身份一致；本实例负零计数为 0，因此没有把 JSON 未保存的负零声称为已恢复。这个操作只是字面值编码／字节比对，没有构造新的 trial 状态。

两个原 scope 仍分别明确“FAILED Newton state”及“UNCONVERGED iteration checkpoint”。它们可供诊断或后续真实初猜使用，不能当作成功 anchor、已完成非零 H/J 缓存或几何证书。

完整 112 高度在原请求、trace、失败 checkpoint 与进度 checkpoint 中逐位相同，raw SHA 为 `c35972d038321acf6db273248189b1e1d2527aa6eb2b323d37fcde4da448682f`。三轮实际 context 还保有相同的：

- cut target：`e2ea4563e7afc7d993db2ebc29ef63a1d853355c9d1ceeaf10f296b84391a14d`；
- 原 scales：`ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc`；
- 原 far graph：`395804bb32582680dd544c6278862f51919c7598b3a1a526f1194f18deffda54`；
- 全 graphs：`0a662556760415760949fe64fbc38c34fd96b087c8adac9536a572e57c9b4c8a`；
- 全 gains：`d9b06c8b9f5a8f381dcde2f7d45c3c19f7659b8850170181fd77ad5df209c5dd`。

参数比较沿冻结源的原 `IO_KEYS` 规则，明确排除输出路径键，而非直接比较含路径的整个字典。声明的四键是 `traceFile`、`iterationCheckpointFile`、`trialDiagnosticFile`、`trialStatePrefix`；本次实际只有前三项存在。完整原值已留在字节审计/readout，三个 snapshot 的数值 configuration、parameters 和 rawNode 在这一原定义下全部一致。未借该过滤丢弃任何数学参数。

## 6. 原始失败位置、未执行部分与独立出版错误

实际原 core `78718-tail-tangent-core.mjs` 的文件 SHA 为 `ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3`。原 `solve` 的线搜索在十次尝试后执行：

```javascript
if(!accepted)throw new Error("multiple-shooting line search failed at "+ev.norm);
```

DN wrapper 的实际顺序是 `tail.solve` 成功返回之后才形成 cut jets、请求的 audit，再形成高度 jet Jacobian。原 worker 捕获这次异常，返回失败字段、最近一次迭代信息和未收敛 checkpoint。本次失败响应没有成功的 jets/audit/heightJetJacobian 字段；worker 正常返回失败协议包并退出 0，外层科学 launcher 据此退出 2。因此必须区分“worker 进程正常结束”“请求的原生求解失败”“最终响应未取得”。原完整源码的定位及 SHA 在 readout 的 `source_control_flow` 中逐行保存。

原科学步骤在 `01:32:58Z` 失败后，always artifact 已成功上传。之后 publisher 又因 main 并发更新而遇到非快进；第二次 pull/rebase 在 `HANDOFF.md` 出现冲突，不能应用同步记录提交 `242b424`，publisher 退出 1。它是独立的出版错误，没有造成先前的原 native line-search failure，也没有删掉已上传的实际产物。官方日志原件 SHA 为 `5a09231d21fbf7bb0481e20c26c93a25836e0165e7e8b47ff39e994783462848`。

规则同步器的原结果为 `science_returncode=2`、`wrapper_returncode=2`、`periodic_sync_failures=[]`、`README_change=null`、`science_terminated_for_actual_rule_change=false`；两次同步并未因规则变化终止科学。这与正式科学失败包相容。最末 console 消息中的 `residual=null` 是包装层没有成功 response 时的字段，不能取代上述已保存的真实范数，更不能被写成“没有测得范数”。

## 7. 与精确线性模型的区别，以及唯一必要的下一读回

独立 R276 reader 对本次保存的三套完整有限矩阵和实际方向作了 exact binary-real 计算。其三轮原十个 alpha 的 affine 原尺度无穷范数全部严格下降；末轮的精确下降区间显示上界约为 2。因此这次原非线性线搜索拒绝，不能解释为“R273 仅降低 L2，本方向连线性无穷范数下降也没有”。详细矩阵范围、精确表示及其局限见[QR/R276 note](2026-11-15-actual73-complete-QR-exact-affine-infinity-and-byte-readback.md)。这里不把保存的浮点 J 当成精确真实微分，也不由模型下降推断实际非线性必须接受。

当前原件缺口是末轮小步的完整 rounded trial state、全部原生残差和最大行。原 73 源只保存 trial 标量及错误信息，未导出完整试步 state/r；本地不能据表中相同范数补出这些数组。历史 iteration 0 的 stage11/Pi75 ULP 报告也不能冒作末轮 stage10/Pi76 的完整试步证据。

下一第 83 轮已据此限定为一个最小公开 Actions 实验：固定末轮实际基态 `f6abeb…`、完整方向 `4b4b1aaa…` 和原 H/target/scales/far，仅选择已经真实出现平台的原 `alpha=1/512`。按原 JavaScript 算式与运算顺序生成完整 rounded trial state，调用一次原 `evaluate(false)`，保存实际 577×224 输入、全 stage out/r、cut/far、原 norm、argmax 与已有 flow/root 字段。它不重算 J 或 QR，不更换 eta，不运行新的十步求解循环，也不把相同范数当新接受条件。

独立精确消费者随后可按原 bits 形成 $h=\widehat y_{\mathrm{trial}}-y$，比较保存矩阵上的 $r+Ah$ 与 $r+\alpha A\delta$；实际 noJ 残差再与前者对照。这能分开状态加法舍入的贡献与其余 flow/切向模型差。当前不能预先把原因唯一归结为状态量化、root 内部停止、输出消减或某个 Jacobian 局部误差，更不能在原件读回前降低原 root 容差或放宽最终门。

## 8. 本 note 的保全范围

本地读取程序只做 gzip 解码、SHA、原 JSON 字段和 IEEE754 字节比较，以及原源码控制流定位；没有 import 科学模块，没有新矩阵乘积、精确点积、范数、SVD、RHS、J、ODE、QR 或试步重算。104 checks 覆盖 35 个完整原 packet、18 个实际冻结源、13 条 trace、19 条 trial、三轮全部子进程小文件和两份完整失败 checkpoint 的字面状态身份。

同目录完整 deliverables：

- [原始逐字段 readout](2026-11-15-actual73-complete-original-native-readout.json.gz)：压缩 38469 B，SHA `618dc28af3d2fc48062fe5d137468e0112e4d2ada44509394cad98da7af8df30`；解压 191059 B，SHA `0c5878becf34bf586389af7e13b236789552a817b892e49cc40fa72b7578c62b`。
- [原件字节审计](2026-11-15-actual73-original-native-packet-byte-audit.json)：39587 B，SHA `25181662e861c593665aa45c72c207c45bb2d0bc05c52429ed3baa8d1187108b`。

完整大数组与 exact ledger 审计的责任范围另记于 QR/R276 note。第 73 轮没有成功的完整非零尾响应，没有达到原 `2e-9` 接受，也没有完成 fullDN/prefix 耦合、闭场或最终几何目标；这不改变已证明结果和本题原完成标准。
