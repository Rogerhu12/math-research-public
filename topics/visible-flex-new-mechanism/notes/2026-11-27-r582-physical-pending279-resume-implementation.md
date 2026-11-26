# R582：真实 a237 与原 pending279 的正常续算

日期：2026-11-26 UTC；会话 `Astra-new-mechanism-1f4a61a4-20261127`。

**状态：后继纯源码与必要输入；尚无本 scope 的科学结果。**
源的实际 18 次接受、每次完整 fine η、全部费用、两组 pending 近点及
raw/best 区分见[原自然终态收据](2026-11-27-r582-physical-paid-resume-original-terminal.md)。
本次只换已支付输入加载器，原科学 driver、所有物理与 metric 门不变。

## 1. 真正进入的新状态

唯一源 run45887805731/job140142780497，source
`0cce06dd57217f8b06af3a6eaf4018f445bda371`；其 FINAL JSON
364198 B/SHA-256
`e3371193ba4dcaa4df4d8298c856dce0663d2c4793d0cf205d625203af35ae47`。
真实97q SHA-256 为
`a2377220dacda9eefe63f25a2000441f0169a0db5de9bc23840f90e5037a895e`，
p=.181，完整11025×3072 η=`4.8302220914394944e-5`，
物理与工作几何违约均0，actual/next trust2。

已使用的 coarse 是243×1536；原38条 pending 径向坐标通过原
`append_nodes` 得到原 proposed279×1536。这里按源的明确提议采用279，
保留38个确切原坐标、无角升级，并不宣称279已经被源优化。
原全部11025个 fine 点保持精确不变，包括两对在 coarse 被原规则
近点合并的 binary64 坐标。加入279节点及其新中点后的坐标并集为11076，
这是纯坐标组织，不是已经获得新 fine 资格。
原 driver 对新实际 fine 照常重新完整扫描；同q/同p/同完整网格才复用旧扫描。

源最后 raw
`a14dedce9ecf12fb0337f4162e39b65bed931c816eaa1c19089c9f88585644c7`
当前行仍违约，另存为未合格 warm 点。它的独立半步才是完整接受的 a237。
后继需要在新的279行库与原 box 上重新判断 warm，不能由其旧行值或
已接受的独立半步给 raw 授资格。未输出的跨run BFGS 内部数组不假称恢复。

## 2. 加载器、物理门与费用

新加载器精确绑定原 FINAL 字节、q/hash、243/11025/279数组、38条pending、
源 raw/独立半步关系、完整20个fine、19个完整Jacobian及另2个已完成方向块。
旧完整源 request 按已发布路径与SHA读取，用它的原加载器恢复已支付材料
和祖先费用；不在新 request 中重复嵌入整个旧输入。
原 `r582_physical_epigraph_continuation_20261127.py` 保持逐字不动。

第一新网格为279×1536；全部原当前行、物理 box、完整 fine、原径向/角峰交换、
球/条带/高度/mean-E/det/曲率/mirror、工作 margin、实际 η 严格下降规则全保。
辅助 e 只属于独立候选的粗行 epigraph，完整 fine η 仍单列。
同 p=.181 的阶段门仍是 `2.5e-7`，未过门不提高 p；设计均值g仍可变化，
不冒固定g精化或 README 完成。

不重放源18次接受、19完整Jacobian、20完整fine、旧方向校验或七点诊断。
源科学2371.7857200480003秒、96backend值、249完成方向块、全部20×87 fine块
及未闭操作仍进入完整费用链。原更早未知费用项继续未知，不编造成零。
相同材料场的62878个端点没有作为数组保存，故必要重建仍完整计费，
原 mesh 必须保持 `0d222bd12ce8a61d0c88264c6fb5c82066f0ca058855b5bf7a670a53b483a991`。

科学上限2400秒、reserve30秒、job50分钟；其余参数与原scope完全相同，
唯一数值参数变化是 `initial_radial_nodes:243→279`，对应实际已记录待采用库。
限时只产生真实可继续 checkpoint，不表示课题完成。

## 3. 文件与绑定

| 文件 | 字节 | SHA-256 |
|---|---:|---|
| `scripts/r582_physical_pending279_resume_20261127.py` | 11630 | `6122c313082e96eb2826beface953d963e82bb517a16bb1d3e14423ab5c3a03b` |
| `computations/request-r582-physical-pending279-resume-20261127.json` | 380989 | `c7ba6dcdacbe6982f9f09414d3275f26b8ffc8dfba509e6c1f54a76595186b05` |
| `.github/workflows/visible-r582-physical-pending279-resume-20261127.yml` | 5259 | `ef878a85f5d109f09db66ca7e33d7a5139fe612b0690554317c99b40f462e11e` |

lane `actual-a237-pending279`；stdin367270 B/SHA-256
`1c6249edb3a98e28735869d63cbd629e313b0ef0673042484b72789b527395d0`。
30个源码/前驱request/workflow绑定以及稀疏依赖路径一致。
本地只有文本、AST、JSON/hash及原日志/坐标解析，没有导入或执行科学模块。
公开 Actions 先真实 pull 双仓、核对规则及本会话QUEUE，再删除认证环境。

## 4. 连续几何的后续输入

新q改变 mean controls 与末帽高；旧f1或旧R611参考的几何结论不会自动转移。
新同mean圆参考及当前/参考全域差仍须以这个a237和同一材料mesh支付。
本 request 中原完整 FINAL 的 `actual_retained_state.q` 是这条新场的唯一
q输入；科学材料seed仍使用原旧冻结参考半径商，不能随比较圆参考换场。
