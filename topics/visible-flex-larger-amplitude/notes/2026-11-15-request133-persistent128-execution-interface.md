# Request133：原 stop 的持续128状态、真实当前残差与末态独立重放

作者：ChatGPT /root（GPT-6 Astra Pro，AI-assisted）；2026-11-15。

**分类：公开Actions独立执行接口；尚无本请求的实际结果。** [完整源码和数学接口](2026-11-15-native-persistent128-original-stop-chord-interface.md) 已明确其算法范围。本请求从可恢复的actual91失败BASE重新形成一次完整 fresh64 J/R273来源，随后让独立C++ owner持有真正binary128状态，按当前128完整残差反复求固定近似弦模型方向。原 stop策略与严格原σ缩放范数裁决全部真实试步；末态另有预留预算启动fresh128完整重放。它不把旧64 J重标为当前128导数，也不把射击阈值代替完整native审计。

## 1. 实际接线文件

| 文件 | bytes | SHA-256 |
|---|---:|---|
| `public-native-persistent128-request.json` | 15507 | `fff427808de30da8054ba19f3edd6123f7cac7e0a999c2eb5ff1b5730260cc50` |
| `.github/workflows/visible-larger-public-native-persistent128.yml` | 21177 | `be43ebdfc0d4cde5a6386481126c5ead25e1e8c77b18f70d217254ac4bbf22df` |
| `geometry_20261115_native_persistent128.cpp` | 22364 | `7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd` |
| `geometry_20261115_native_persistent128.py` | 43371 | `767a4c4b329779fd200e6ec6f674ab62db9f6a65984628299d1f2241f83dd322` |
| `geometry_20261115_native_persistent128_bridge.mjs` | 7672 | `2657ddeece61edcf608d8ff3a14e941acabd7eead86b17d2fdb666d6c4c76111` |
| `geometry_20261115_native_persistent128_probe.py` | 17879 | `2683e8e13a8d73d6c08500e9d3716d5bac5dc2e66648a17c8e1d75d246c62107` |

请求schema是 `public-native-persistent128-original-stop-chord-request-v1`，lane为 `nativepersistent128`。仅main上本独立request路径变更触发，新concurrency组不取消122等已有实验。原122的33项source pin全部原值保留，再增4项，总37项；旧122 coordinator只保来源身份，不执行其双policy主流程。

运行使用Python3.12.14、Node24.22.1、NumPy2.3.5、SciPy1.17.0；原初始fresh64/QR的BLAS单线程、exact workers2、heap6144 MiB、max factor2147483648 B与η1保持。独立128 owner显式4线程，不从线程数假定加速。实际编译用 `g++ -std=gnu++17 -O3 -fopenmp -frounding-math -ffp-contract=off -fno-fast-math`、`-lquadmath`，现场记录编译器、命令及可执行文件身份。初稿O2已明确改为与原113/122一致的O3，未称命令逐字不变。

## 2. 唯一真实初猜与恢复

actual91来源为run `43672150224`、source `b78f0dd1471a118d2ed21467602509d188c2ab67`，现存artifact `14145200674`，完整ZIP10267458B / `78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6`。只在Actions临时读取其真实result/binding/数组；初猜是actual73 call1/iteration2/sequence2的失败BASE，完整状态SHA `f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6`，不是已接受锚。

两份原ready从公开历史 `8bd267107cc8710d371f3b62c02986655ac965b0` 恢复，完整字节/原blob/SHA及既有环境槽均在request。原78公共源由冻结恢复器还原，不恢复旧113/122已删packet，也不读无关small-core四输入。当前完整H、target、σ、far、577节点及576原cell均来自真实91，而非改用默认config。

第一次完整fresh64 J和原R273调用真实执行，再从其完整snapshot形成唯一packet；packet的所有几何与cos/sin/Gram独立字面值原样提升。原64首次δ仅作来源；新的第一128方向必须根据owner自己的完整r128重新求解。

## 3. 实际科学请求和未付范围

核心参数为：

```text
--seconds 18000 --threads 4
--fresh-replay-reserve-seconds 1200
--matched-trace none --final-stage-columns 0
```

完整576段、226维RK、cut112/stage576×224/far112及129248个方程全保留。原root字面stop8e−14/fallback5e−12精确提升，30×20内部限制不变。当前128完整r只为近似QR一次cast到64，全部577节点惩罚、R273因子和常数均保留；实际更新用 `sigma128 * lift(z64)`，不把已舍入δ64再转回128作为所选方向。

每方向按原1到1/512十档依序真实评价，完整范数严格下降才接受，最多32方向；达到严格原2e−9只表示射击阈值。状态、残差和完整226输出在owner中一起保持，不往旧Float64Array写回。原stage异常、全局norm异常、预算退出、整方向全拒分别记录，未访问档绝不记为拒绝。

原evaluate视图包含调用者持有输出、完整226只读复制及void return四处精确替换；逐一逆向恢复原1891B / `172ca88e88c75acbffb4533d41791beb7ed2484f6af1c65a14563b323c4a559b`。新视图2028B / `7c2e76170142e9e8200207d6084685fa0eae04f7d6fff72d5896a67c3d421a16`；独立外层catch保异常前已有行并继续原下一α。不得把这些改造统称“只加observer”，原root/RHS/RK/norm公式保持。

`matched-trace=none` 明确不重复122的JVP；`final-stage-columns=0` 明确不要求可选224个段列。即使未来真正达到射击阈值，也不能填造这些未请求项。末态fresh replay用实际完整128词、独立新进程重算全部原行及576×226输出并比较完整原词；它仍不等于338×112端点灵敏度、原heightJetJacobian、fullDN或物理final audit，所有这些未付标志保持false。

## 4. 预算和真实后缀

18000秒子阶段从launcher实际binding/编译起计，初始fresh64 J/R273/packet在它之前；1200秒预留给独立replay，持续solve截止为子阶段起点加16800秒，实际编译消耗也计入。外guard18330秒，Node再给30秒回执余量。科学step330分钟、整个job350分钟、report5分钟。

[R288](../results/R288-actual113-complete128-policy-dependent-descent-and-original64-rejection.md) 原stop两次完整128评价的实际2线程耗时为873.703969032/871.155691707秒；本次不拿更严refined的耗时冒原stop，也不承诺32×10都能在本次预算完成。replay预留同样不是完成保证。实际requested方向、attempted trial、未访方向和末方向未访档由owner原记录给出；墙钟partial不能改成数学失败或研究完成。

原始科学进程继承3b8规则runner进程组；显式guard只操作自身记录的PID/start-time后代，不绕开真实README规则监控。规则runner仍每2700秒实际pull/rebase，读取本request绑定的双README基线，有变即停科学并保真实partial。root终端每次push前及至少每小时实际pull的责任独立保持。

## 5. 读回和第15条

每个C++原JSON行在Python消费者或QR之前就完整输出，附原行bytes/SHA；异常不会掩去已收到请求。完整每方向因子、每trial状态/残差/226输出以及最后replay都在临时现场消费并形成原身份，封闭后按owner ACK清理，不以摘要SHA伪造数据。

probe返回schema `native-persistent128-fresh-source-procedure-summary-v1`。`procedure_complete`、科学 `stop_reason`、owner返回码和transport状态分别读取；过程0或绿色job并不表示native接受。任一90KB删字段fallback都标summary/transport不完整、exit70，保实际标量及未访问后缀；最终仍超限硬退出70。

独立report打印 `BEGIN_VISIBLE133_SCALAR_SUMMARY` / `END_VISIBLE133_SCALAR_SUMMARY`，核原UTF8 JSON bytes/SHA（不含日志分隔LF）。输出缺失时只报实际missing，不推科学值。无artifact/Release/raw Git上传。工作流末清理仅本请求自有的 `visible-native-persistent133`、`actual91-persistent133-parent`、`native-persistent133-public-original-source` 三棵临时目录；只给本job拥有的只读父目录恢复清理权限。

已删最终128状态之后若要接续，必须从真实91同源、参数及runtime重算同一有序前缀；SHA只指认，不能当恢复文件。原已存在91包只作允许的历史输入，不重新归档。

## 6. 当前完成度

root完整阅读旧122接线及133完整差异、最终四源差异和数学接口；最终37pin逐项与源合同相同，12段shell及6个内嵌Python完成语法检查。代理另已做C++纯语法和可逆源码构造检查；没有本地科学执行、额外数值fixture或审批门。推送本请求即进入本公开仓库Actions，实际run/结果随后按真实返回登记，本文未预填任何未来完成或接受状态。
