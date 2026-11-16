# true53 完整多峰投影首次实际：没有合格方向，原接受点 53 保留

日期：2026-11-16。**唯一公共运行的首次实际结果；主课题未完成。** 原始研究与同run只读报告均正常结束；“作业成功”仅表示约定的有界观察完整记录。投影未完成一个合格的原始可行方向，未开启生产scalar session，未产生实际新候选；没有证明不可行、驻点、数值改善或主目标通过。

直接来源：[公开Actions 43811870681](https://github.com/Rogerhu12/math-research-public/actions/runs/43811870681)，源码提交[42f95905deec3024dfee7a687bdc806d38c79baf](https://github.com/Rogerhu12/math-research-public/commit/42f95905deec3024dfee7a687bdc806d38c79baf)，[原请求](../computations/request-true53-projected-direction.json)及[方法合同](true53-complete-grid-maximin-projection-direction-design-20261116.md)。本稿只读已付原输出，未重跑solver、模型、开发或几何。

## 1. 准确决定与真正可继续的末态

完整科学状态为 `complete-current53-projected-direction-and-original-gate-audit`，其中投影session终态准确为 `search-separation-allocation-ended-one-final-slot-reserved`，首个prox状态为 `finite-projection-work-incomplete`，最终方向null。

方法给搜索最多23次完整分离，另留1次复核合格方向的实际rounded步。本次23次均未得到合格方向，预留槽未用。**这不是600秒或100万坐标额度耗尽**；未用槽、prox或剩余秒数也不能移作这个已完有界任务的重试。

真实physical仍为此前p32完整线唯一接受的53：

| 项目 | 本次最终记录 |
|---|---|
| accepted index / 新接受 | 53 / 0 |
| physical SHA256 | 9ffba0f1400c504343f9b0b8847be7f14745144f66b3cd89dfe698f45d81548e |
| 粗网真实η | 0.2660148711293937 |
| 细网真实η | 0.26601514422985384 |
| 本次真实η下降 | 0 |
| 细网最大绝对主曲率 | 57.9992694544513 |
| 新metric目标13/50 | false |
| 原两网各14门及163精确盒 | true，终态使用已付点53的收据 |
| 实际pool / 版本 | 4448/4549 / 13/14 |
| bank / learning事件、commit、pending | 512 / 62、61、0 |
| trust / 两条streak | 0.00025 / 0、0 |

fixed g、b0、永久enriched reference c0和159→163坐标未变。η是metric epigraph辅助量，**不是δhold**；约58曲率与全域/非局部reach要求的缺口仍在。未独立重复初点或终点几何；两个ordinary value是新53硬模型必要缓存，全部按新费用记录。

新objective评价身份为 `c98db48657cfe706675db5873439cf7b8d731c663784d81f0fbe0b45f0b14807`，完整一阶模型绑定为 `e095e93d1455302af6904e703e762adad05d9cdef7220761c468e3ea0efca9a1`。它们绑定真实53和当前池；不是旧52/p32线缓存的身份。

## 2. 三组首次新开发与旧来源只读

三组新人工均在同一600秒科学钟内，且只执行一次：

1. 原域不含零的加权投影与同dual新中心重绑，两个实际向量为(0.25,0,0.5)、(0.75,0,0.2)，完整原行诊断均通过。
2. 保留current gap 0.1，错误方向的遗漏行残差0.2200000000000002；追加原metric行，不删hard。literal零行/负RHS的严格矛盾与数值容差内通过分开。999999个模拟继承debit不算执行，真实再访问1个坐标后预算退出，保有限向量。
3. 合法区间[0.25,0.75]仍以真实物理α=0为基准，重复查询照计；目标常数0.26保留；空区间不启动scalar session。

人工实际2个投影session、3个prox、3次sweep、13次coordinate访问、1个scalar协议session、5次完整小查询。内部开发用时0.0061183429999971395秒，入口含导入/包装的开发段0.010381925999993769秒。两者包含而非相加，都在新科学总钟内。

旧6/12/11/9开发收据及paid p32三组结果只读。98个原参数、24输入与原200来源逐项相同；旧geometry/J/JVP/scalar/LP/SOC/cone和旧developer suite均未重跑。新闭包212项：184 Python、14 workflow、10 Markdown、4历史JSON。八新Python来源顺序、请求47564字节/SHA256 `85b076f483a41385888468aeb2ac51e56c1cf5253d738af1a73d40fb439d4fe4`由run/report核对。

直接祖先是p32 run43804573954/job133092260804/sourceab1ba331a1d376d61e6e9f9b7f29f2bb9221a1e2。只读一次其原研究日志中的REQUEST、PRIOR_WORK_REUSED、COMPLETE、FINAL_CLOCK，不解码旧52线cache。祖先权威最终成本1406.2512530919998秒/126次原完整value，旧32cone/64HiGHS永久关闭。

## 3. 完整当前模型与原硬域

保160个原径向点，粗/细角384/768，即61440/122880个metric点，每点两个原分支；目标常数0.26另保。完整φ0=0.26601514422985395，原真实η末位浮点差未强行覆盖。

两次必要ordinary geometry各一次；coarse/fine原池4448/4549行各一次原selected factorization，保原hard J与selected metric observable，计两个新hard-J-grid build。旧objective的selected159-J批次/refresh为0。两个完整first-jet-grid缓存的原frame复现误差均为0，内部没有额外ordinary geometry。

冻结curvature guard仍用既有系数57.187653029922444、67.42701956990882及B=0.00025。coarse无修改，fine只提高group8原四行1091507、1091533、1091891、1091917目标，最大增量0.0000020981583979125305；原A/J/values、物理盒和norm行全保。guard模型身份 `579032816cef3c9f10f804652e823d19d1630bd6399785116ecd29e93133e93d`。未调用radius-mapped witness，未用旧SOC RHS冒新guard。

物理度量用原163维归一映射K，非平凡分解只有五高度块，用时0.0008787350000147853秒，未加jitter或改height范数。K SHA `774641f606e78af541e6aff1a3313e637af3fdd0ee1b2b20d55a18cce849eb27`，G SHA `83d144f9a39a201eca5fb2297ee4df420ef3fa49cfe6d618d6e8a6f72923d01f`。

## 4. 23次完整分离为何不能形成方向

生产只有一个prox中心、184次完整sweep、724792次真实coordinate访问。每八次sweep作一次完整粗/细分离，共23次。每次保全部gap、常数目标和两网所有分支；23个不同方向各有两次完整JVP，不从selected池最大值推全网最大值。

23个经完整扫描并修复物理norm的候选，其 `qualified_positive_ideal_primal` 全false。关键原记录：

| 分离序号 | 完整一阶最大值 | 修复后完整收益d | 已安装master全原容差通过 |
|---:|---:|---:|---|
| 1 | 0.2660157410381146 | −5.968156312826824e−7 | true |
| 3 | 0.26601873841390067 | −3.5942005890107947e−6 | false |
| 16 | 0.2660156716174386 | −5.274396644129722e−7 | false |
| 23 | 0.26601573294896613 | −5.887796501991287e−7 | false |

第一行已说明：有限master通过自己的容差，完整网格仍可发现实际一阶收益为负。所有负收益原样保留，没有拿raw gain约1e−6代替完整gain。

末模型安装40条metric梯度行，大多数直接取已付当前selected-gradient缓存，另有5条原池外gradient真算。不能把40说成40次新导数，也不能把5说成仅保5条metric约束。五次新增：

| 网格/group | 原flat row | 原t | 原θ/π | gradient SHA256 |
|---|---:|---|---|---|
| coarse/0 | 28429 | 27/80 | 13/192 | 054a3d4639712b842939621de5916a99ba9a99850009e3ae1ed4a6a0c3a11d5d |
| fine/1 | 181837 | 141/400 | 589/384 | a4eef0b7091d6ec7018b54c7136f434486c59baf37a8b8525773ea9505c2541b |
| fine/0 | 67364 | 171/400 | 137/96 | 94013b83b7107980a84316edd5c39e5d53762d9da34c459f981c5cd5902531d2 |
| fine/1 | 181159 | 69/200 | 679/384 | 5ebc2cb5b40a61c3afd375074dcc5973bbb8c433941757f4dd15b936cb83e562 |
| fine/1 | 191151 | 87/200 | 229/128 | c0791f321b9db83e2febdc4e18d28e3f2ffb0890ae42ae67ad918d1ab02bc8d1 |

这些只是模型信息，不是假造actual新增pool行。池仍4448/4549 v13/14；没有actual trial，所以没有更新bank/gamma/controller。五次single-row derivative全完成，观察段合计0.2678789039999856秒，包含在科学总钟。

最终master3950行：

| 原诊断 | 数值 |
|---|---:|
| 最大metric残差 | 1.588778857197029e−6 |
| 最大norm残差 | 5.118940978312495e−7 |
| 最大hard残差 | −1.1589002468807874e−9 |
| 最大physical残差 | −0.000381837336661872 |
| 超原容差最大量 | 1.5877788571970289e−6 |
| 已安装行全部通过 | false |
| dual负乘子个数 | 0 |
| dual stationarity最大浮点误差 | 3.3306690738754696e−16 |
| 投影dual下值诊断 | 1.055062501326466e−7 |
| 仅primal完整可行时才可用的primal值 | 2.3375915566325418e−8 |
| 原gap差 | −8.213033456632119e−8 |

负gap来自未满足原约束的primal迭代值，不能当弱对偶反例、收敛或精确证书。修复h为物理norm后，末候选的hard/physical/norm/bound域检查通过，但完整收益仍负，尚未通过方向门或新rounded actual/163精确盒检查。

最后maximin上值仅是未外向舍入的binary64诊断0.0016659578028829455；metric乘子和0.2811328206465306、原外域线性最小诊断−0.0004682031655476318。它没有证明最大收益≤0，不能据此宣布驻点或不可行。

真实有限161向量及其精确binary64表示在原PROJECTION_RESULT，SHA `013df3ee21ac44005fb56249ea9d624eddd7ca2208f504a7d1db67b7c8bd6e8d`。真实λ、原row-order、RHS、row-scale、中心和迭代均保留；A SHA `7e53a0bbaaa426c9e54e4fb23f6543fe3c8728cb00fbbbc513df2ea24a2eea87`，b SHA `3f3498e82fb3e7adaed76e7194937e0684a64c0da3d7d2535105880a375c3c9c`，dual SHA `1369526f2cc96c2a204ea41ef5026d710ef3bca7cbd91089c840e471a3d54f67`。哈希只定来源。

## 5. 费用和操作全账

权威FINAL_CLOCK在全部大MODEL/COMPLETE序列化和stdout之后取样。**新科学188.188974004秒，祖先合计1594.440227096秒、128次原完整value**。入口process为188.188997335秒，另保。旧cone968.6757049859999秒已在祖先里，不重复加。

| 新生产操作 | 实际启动 | 原本次上限 |
|---|---:|---:|
| 当前必要完整value | 2 | 2 |
| hard-J-grid build | 2 | 2 |
| first-jet-grid build | 2 | 2 |
| projection session | 1 | 1 |
| prox | 1 | 12 |
| sweep | 184 | 256 |
| coordinate访问（包括零变化/零行） | 724792 | 1000000 |
| 全网分离 | 23 | 24，末1预留 |
| 原池外metric-gradient | 5 | 96 |
| scalar session / query | 0 / 0 | 1 / 64 |
| actual pair / actual完整value | 0 / 0 | 3 / 6 |
| 旧LP/SOC/cone/legacy-selected-J | 0 | 不重开 |

人工操作另分类，但时间在新188.188974004秒内。220个生产ledger事件正常结束，没有吞掉失败费用。主要段：

| 段 | 秒 |
|---|---:|
| paid53日志只读 | 1.97749211 |
| 必要24输入prepare | 14.469766058000005 |
| 新objective构造 | 0.12909917300000018 |
| 两个必要当前geometry | 126.93052477399999 |
| 新完整模型build | 36.624100779 |
| 投影session | 5.23513079899999 |
| MODEL序列化/stdout | 0.707028514000001 |

阶段与内部事件含嵌套，不能再次累加。两geometry内部107.86421906299998、18.845151869999995秒；首个固定height primitive prefix-miss为98.908515444秒，只是本次观察，不外推旧进程因果加速。

research UTC05:41:27—05:46:32为305秒；含pull和程序的step05:41:48—05:46:29为281秒，与monotonic科学时间分列，不猜差额。只读report自身2.529812888000002秒单列，不记为新科学评价。

## 6. 原始记录、来源与保存范围

research job133115100791，report job133116787814，同source42f95905deec3024dfee7a687bdc806d38c79baf。report只读一次原research log：35,105,831字节/SHA `fa7edaf1419325ce31e6926de44f8c9ebbddf1ea554d140fafef61aecbc9ceb9`。

唯一完整MODEL保原hard J、soft gradients、159/163当前点、40安装metric行和5新gradient；没有复制进Git/artifact/Release/跨run cache。下表以原JSON加LF为指纹规范：

| 原tag | 字节 | SHA256 |
|---|---:|---|
| REQUEST | 35217 | ec7ed753aeb2e79bf557dee969380da7c7430c68afa89853824f2f06ffc412c0 |
| DEVELOPMENT | 24377 | a43d32a83a35fe77364cd372f38fce231d573eb49564caf47046fbad0b286587 |
| PRIOR_WORK_REUSED | 4514 | 6091bc5437d74943df8e72a3a75be6af17e380148a5ccef9032c2298b8e6119b |
| BASE_VALUES | 6101 | e9dac180ce8c6d667d499850d9571ad8bdfcc0e9b921b4d795fbf8c29058b814 |
| PROJECTION_EVENT | 600724 | 94185f8ed8b6b50872003b4954f000e80b8201524da52d6dc8b558abedff5564 |
| PROJECTION_RESULT | 1531224 | 1750945efef7fed6f85b31205fd3ea8504c2f7411d03bedf1b11d6a0832beae7 |
| MODEL | 27365833 | 926681688d09311883c64dfa1dc40599a62d1904d7f6dbcaf478893fe14bd539 |
| COMPLETE | 5316472 | f2638d46b440afdb7336334cdc2ffe1c31b1ced18a5493e5fe39100a6daf03ba |
| FINAL_CLOCK | 127108 | b513907be93a9220bfd61487b6d07e885fd6c1547554dacfa15a10079372dc53 |

未生成生产CACHE/QUERY/SCALAR_RESULT/TRIAL，因为对应阶段没有启动。MODEL回执与原记录字节/哈希相等。后续费用继承取FINAL_CLOCK，不能取较早COMPLETE的时刻。

只读report日志2,345,650字节/SHA `5fe55b868476e0bc91ea1d58f058d0fc3bad70592d441446ad8c1d4914630643`；REPORT_COMPLETE原JSON+LF2,260,858字节/SHA `ecacb3eaafd22bad58ba9a42927b5dca48af2f706b26465b5550e57d6df998de`。

报告未转发dense arrays，但多个阶段与ledger语义仍超过800000字节软目标，如实记录 `semantic_cap_exceeded_after_secondary_omissions=true`。没有修改限制、编码或分块；root直接消费原完整报告。后续若减少报告重复元数据，不应为此重跑科学。

## 7. 四次实际pull与已读规则

research公开实际pull为05:41:48.307107—05:41:48.638904 UTC，before=after42f95905deec3024dfee7a687bdc806d38c79baf，rc0。其私有pull为05:41:51.073561—05:41:51.526785，before=after26811132f0f77f361fec6a464f93d2ee19ec1a24。

report公开实际pull为05:46:51.539801—05:46:51.955126 UTC，从42f95905deec3024dfee7a687bdc806d38c79baf到已读 **8184486663a0480a9805ed8efa5c6b4739cc08d8**，rc0。私有05:46:54.007619—05:46:55.187011，从8d9caf92c263faeea363e822af26effbff7b73f4到b3a11fe6e1797a6f91d299091a5bfa52573f0a5c。

每次公开pull的根/题README与已读基准相同，diff为空：根blob21bd547f56590b7f2dd279d0297efb289a9b2783、题blobd0432faff569c8e9af7ed4809847e12880976c11。私有根blob5ba164843b1f5802184178a82d786264404873a3未变、该题README无、QUEUE本会话唯一进行中；私有内容不发表。

root已消费四个原pull记录及空差异，HANDOFF同步。下一实际pull最迟 **06:46:51 UTC**；如发生推送非快进，立即实际rebase，不等时限。

## 8. 已完观察与后续仍欠的任务

已完的是这个唯一有界观察：新完整模型建立、新人工通过、原行/guard/gap保全、23分离无合格方向，末态与费用完整可回原stdout。连续最优投影、真正下降方向与主课题均未完成。

现有输出把下一数值问题定位到原有限master的可行性、坐标度量与完整下降资格：raw gain不能冒完整修复gain，dual stationarity小不能冒primal可行，有限master容差通过不能冒全网通过。下一新数学或方法必须直接使用已付模型/失败方向/最终dual，说明真正新目标和有限范围，不改名延长旧184sweep/23分离，不重开32cone/64LP；没有新几何改善可先行继承。

理论R459—R462分别已付同宽signed全partial、真实光滑period range、原九行同规范与完整权零五核。actual正锥/完整基准、同一九行兼容、其它路径段、高阶收敛、C²嵌入/reach、固定g精化及幅度门继续。主课题不在本次失败、预算或阶段处结束。
