# actual121：五批原计算完成，因摘要传输上限停止

作者：ChatGPT /root（GPT-6 Astra Pro，AI-assisted）。本条读取公开Actions已有输出，没有本地科学算术。课题未完成。

## 1. 实际停止的是读回编排

公开 run [43694950669](https://github.com/Rogerhu12/math-research-public/actions/runs/43694950669)，source `da16069e10e11d4541992fa66c6f03ee7165baf7`，compute `132753318793` failure、report `132754032982` success。run于2026-11-15 08:32:04 UTC创建，原rules监测08:32:41启动、08:34:59结束。链原计时 `137.48953699100002` 秒，实际启动5批，五个原science child和五个原reader进程均exit0。

每批科学status均为 `diagnostic-completed`、原8方向8接受/0拒绝方向，按原8方向预算停止；各批unit/full112/nonzero/success仍false，native未调用。链exit70的原原因是 `original_reader_did_not_return_complete_scalar_summary`，不是native或原三式的数学拒绝，也不是墙钟截止。`resource_limited_partial_chain=false`、无wrapper异常或signal，未启动第6至8批。

前四份为正常原reader schema。第5份在原可选省略后仍为93000B，超过原90000B界；原reader实际输出 `request117-readout-metadata-over-budget-v1` fallback16702B。其被省下的正常候选摘要原SHA为 `d170c8b33010b6579837fbd7a6d8106f1fefba6d7dffc4711fe349cea5b6a478`。这个大摘要没有在log中保留，不能由SHA恢复。

源码执行顺序已直接核对：wrapper打印真正reader输出，然后 `read_status` 完整读status/trace及24源闭包，之后才检查summary schema并决定停止。因此原 `completed_original_readbacks=5` 表示五份回执及原status均已读取，**不表示有五份正常完整scalar summary**。第5原 `complete_status_read=true`，原source闭包计24、相等；全部五批 `raw_cleanup_completed=true`。没有仍可下载的第5大status/trace或未印trial表。

## 2. 原逐批数值

全部数值逐项抄原字段，不重新计算跨批差值。每批仍显式radius=.1重置、原3×6/两normal+四tangent、原8×20外试探及12×20校正、完整未加权三式Armijo、全部final职责。原源码见[121接口](2026-11-15-actual119-to-six-control-batches121-interface.md)，未改e154/79464/3e2c。

|批|原W before → after|末unit第一式|末3×6最小数值奇异|末前三列最小数值奇异|末radius|
|---|---|---|---|---|---|
|1|739.9479122853971 → 738.1963167066945|−38.42385385732618|.9222996234865298|.8720685348851764|.000390625|
|2|738.1963167066945 → 738.1784546897181|−38.42338901610876|.2671049582719033|.22708730327596494|.000390625|
|3|738.1784546897181 → 738.1772981178082|−38.42335892281797|.21922719232464968|.1958105783256598|.000390625|
|4|738.1772981178082 → 738.1754896790695|−38.42331186586826|.044031566468692364|.0065780756303784|.000390625|
|5|738.1754896790695 → 738.1754024784359|−38.42330959663998|.0068574945219558045|.005436493341118373|.000390625|

第5末完整unit为 `[-38.42330959663998,-0.009196866645244496,-0.00012357057226189492]`，完整112右残差前三项 `[-17.74800909155234,0.0005490024705623676,-1.9437720987857e-6]`。3×6奇异值 `[170043600.09878358,165159.37881482596,0.0068574945219558045]`；前三列 `[168636066.07225206,121499.8406509716,0.005436493341118373]`，原四列 `[168704463.02573216,123690.23343942428,0.005707288855395433]`。

响应显著变弱、原接受仍有下降、残差远未达原1e−8。这些观测不证明rank丢失、局部极小或无根；FD的整列归一误差也不是最小奇异值相对误差界。

## 3. 实际试探和可读范围

前四批全部外trial行的alpha/接受/原W与bound/内层tol/域异常计数已逐行读取。其正常摘要也保留原返回参数、三残差和约束误差；本条不复制可重算整表。原normal corrector调用次数为38、54、68、69，第5的原计数为100，但第五完整trial行不在fallback中，不能假称亲读或编造其接受alpha序列。

前四批仍有正常有限候选不达Armijo，而非全为域失败。第4批方向3的alpha=.00390625，原W `738.1769363164194`，bound `738.1769357414771`，被拒；alpha=.001953125随后以W `738.1768947541321`、bound `738.1769769120374`通过。第4批方向4的alpha=.125在 `normal_target_tolerance_met=false` 时原门接受，W `738.1755619628464`；内层tol不是新增外门。

前四批observer错误均空；evaluation attempts/returns/exceptions依次为1613/1606/7、2272/2222/50、2757/2719/38、2966/2915/51，J190/251/301/312均返回。外trial exception文本均空，不能把内层失败计数称为外抛错。

第5chain在完整status中读到evaluation3525、returns3525、exceptions0，complex2358/real1167，J393全部返回，observer错误空。其trace4800696B/SHA `9f5cf193e9f49686188b2fd0e640f95d96df90025e96ebbe5628b908f2891413`。这项原计数进一步区分了第5摘要上限与内层域拒绝；未印的trial具体序列仍未读。

## 4. FD、scalar域与零circle

前四批初末六列FD的原三个步长 `2e-5,1e-5,5e-6` 都独立尝试、完整六列有效。第5fallback保留完整final FD，三档最大归一误差原值为 `3.971789619780593e-9,3.467783583198889e-9,1.5399047639288349e-9`，每档all six attempted/checked和valid均true。

前四批原Arb160/depth14的叶数1042、1042、1043、1043，unresolved均0；原a/ap有限Gauss表达域通过，但ap=Da、C²接口、binary64舍入包围和完整Frenet域仍没有由此证明。第4scalar身份 `3483b64aaa3280ec81141a5d7b348f56f0a7e7d401182ee24cbd602314503cc6`。

前四批三odd冻结的原3active/453态circle，原节点、中点、2×698 RMS查询无无效项，4096rho guard通过且rho=1，BC/常数残差0。physical collocation原值依次 `4.410534437671032e-16,4.507028431022242e-16,4.524917766868253e-16,4.445771008276811e-16`。这仍是零core参考检查，不是非零场接受。

第5fallback保留source-circle节点/中点最小beta² `0.005153128322737621`、最小radius `0.2999999979751078`，scalar最小radius `.30000000000000027`；其完整Arb及circle诊断细项未出现在fallback，不把前四批或119的数据替给它。原phase完成只说明原程序走完自己的诊断，并不等于本条已亲读每项第五批数值。

## 5. 原输出身份与可重现范围

原summary身份排除打印分隔LF：

|批|bytes|SHA256|形式|
|---|---:|---|---|
|1|81079|`c25c81a3e34a51a9173fc5c8ec711fd364eeefc54d7b1cd588af411b4bb39f27`|正常原schema|
|2|86847|`d63275776782d4d7430499fae451afbdf7129ca2ab61877a41717d6e15691fe5`|正常原schema|
|3|81220|`169feb64bf1f1d79b32480f02201ddeb3f971f161959fec33b2764d934d141d1`|正常原schema|
|4|81766|`f02114288281ed3afaf50d2ebaafc8bc8c0a949a166ba8a3f9533df6da073968`|正常原schema|
|5|16702|`24c3b370b23840ddaf93c52caa36a4b434ff3018e31a65ccb0f4d574a6d5b30e`|明确over-budget fallback|

五个原status身份为：

|批|bytes|SHA256|
|---|---:|---|
|1|2163178|`bbc3d076496a6461bd9e3b5ba92005672d681701896344c9928c24f224831988`|
|2|2980369|`9685032321b39d56ed439b406186bb639a4d839c687235869af4c9ca3f22ccd0`|
|3|3598504|`e4d907b25ee02bed6d536e64aa3bdfc426d177c1c35d1d82b76dddc4ef0b20a1`|
|4|3838165|`24cfa463b1a540506925636cc6b55890486954a8120f43c3e18591367213d3f9`|
|5|4646850|`cfe09440cd7d89bb9a1b79513ff17695c16f683cc745dd73fb4412c87742241d`|

链打印摘要42458B/SHA `6e8a62827c26fa69688ab9a2e23903d09ebed0ca838a7844002e67449613d36a`，原chain文件40917B/SHA `6f50d10de7dbb2aabb39708f1efd238baa0d5e2f7bd3d411227374894f81ea4b`。compute log400434B/SHA `302d06547428a0d12e8f0072d666a47fe5df65ccaa1a34ceb4fbb7391dea4ed6`；report log89700B/SHA `f1d269a08ca8d7b6305a0f1cc765d022f3dbcd77e9e9d4d17e147403f8674d85`。

只有正常schema才生成新的短recipe，所以 `last_restart_recipe`及误导性名称 `last_fully_read_parameters`仍指第4批：recipe1570B/SHA `c130d445d53b3b50665906aa6f10dbe01107a4f328201617f533770090baa0ac`。它不否定第5原status确已读全。若需要重得第5未印全部试探，应从该第4批真实recipe按公开原源重做，不从SHA制造旧raw。

原规则08:32:40 UTC读origin/main `ad90f969282811ed8d4499606cb577186e07ec39`，两README未变，08:32:41推送 `4f907970586563e6e1fe0fc9d16aa3d3696380fe`。原rules runner保science_returncode70、无规则变更或同步失败。没有artifact/Release或Git raw上传。

## 6. 下一实际参数与工程改进

第5真实末参数来自原fallback的 `final.parameters`，同时与chain的完整status读回一致：

```
[0.4091209275836485,0.2513669199841148,0.4996145196964636,
 -0.006902208058565607,-0.035813559588767495,0.5645740576397902]
```

123准备一个明确的新九控制族，在三个原支撑分别添加 $b_i(x)(2x-1)^2$，旧六参数顺序保留，新三个eta初值均0。完整3×9、12×9正则QR、两normal/七tangent和九列FD/新scalar域全部重付，原8方向/20档/12×20/完整三式Armijo及final不变。最终circle仍冻结全部六个shape设计，只以原前三p作453态方阵；不能把新九active塞入旧方阵或让120六参数入口静默消费九参数。函数独立不保证响应变强或补秩。

新reader将明确分段：每个方向的全部原trial行单独输出有SHA的≤90KB块，primary摘要仅放原source/初末/FD/scalar/circle与分段身份，再通过GitHub output传送。需要进一步分块时保完整字段与顺序，不静默截行、不新增数学接受门；旧3e2c不改。选择第五批参数不冒完整trial摘要可用，也不把摘要工程stop解释成此六维族不存在解。

独立120仍用119第3批及λ=.001尝试完整非零112，113/118/122及同场连续几何责任照常推进。没有因为121传输错误改换120初猜或原门。
