# R401 — actual189 完整十维全三校正的 69 次真实接受与资源部分终态

作者：AI（ChatGPT，geometry）。日期：2026-11-15。本文只读取已经完成的公开 Actions 原日志及原单份必要摘要，核对原字段、字词、来源和 SHA；没有本地导入模型、运行科学、重算残差、FD、矩阵范数或新接受判定。root 已收到同一份必要摘要和两份原日志，不需重复获取。

## 401.1 本次实际结论

Request189 在 actual185 真正末十参数上、同一个 persistent Decimal50 owner 内启动最多 16 个原 8 方向块。它实际完成 **69 次原全三 Armijo 接受、158 个原 $\alpha$ 档**，最后接受点的原未加权全三 merit 为

$$
W=1.7920048197146154915389967007746182829336465880156,
$$

原起点为

$$
W_0=4.3468672471711859976481753001800879050274704518442.
$$

这些是原记录的两个字词，不是本文重新算出的 merit。前 69 个 owner 方向均取得原门接受。第 70 个方向已经开始，但尚无原 $\alpha$ 试探记录时，whole-child 2400 秒资源限制向科学子程发出 SIGTERM。科学源捕获 signal 15，留下资源部分状态和完整必要读回。**它没有执行完 128 方向，也不是原 20 档全部拒绝的数学停滞。**

计算 job 为 failure，真实 child exit 为 75；必要读回、原错误读回、条件清理及独立 report job 均 success。原摘要为 87897 B，成功进入单份 90000 B 合同，没有摘要超限或分包恢复。科学原字段为：

| 原字段 | 原值 / 原存在范围 |
|---|---|
| phase | resource-partial |
| resource_partial | true |
| diagnostic_completed | false |
| success | false |
| stop_reason | null |
| exception | ResourceStopped('Received signal 15; do not infer a mathematical failure') |
| final | {present: false} |
| final_binary64_projection | {present: false} |
| accepted_point_count | 69 |
| attempted_outer_directions | 70 |
| original_trial_records | 158 |
| elapsed_wall_seconds（producer） | 2400.158791314 |
| temporary_wrapper.wrapper_wall_seconds | 2402.325367978 |

**最后接受的完整十个 Decimal 字词确已返回，并与 current owner 字词逐字相同。** 它们可以明确作为后续新实验的真实数值初猜；资源部分终态不能改称 completed 末态、accepted fullDN checkpoint、非零 native 场或连续 C 十族接受场。全局末 FD、末 scalar/Arb/圆及原终消费者没有返回，后续必须真实重求。

## 401.2 官方运行与唯一原件身份

- 仓库：Rogerhu12/math-research-public。
- request：189。
- source commit：598951293035cb2e2fa705bc13e24cc1a5f59b8a。
- [公开 run 43762371885](https://github.com/Rogerhu12/math-research-public/actions/runs/43762371885)。
- compute job：132959791013，官方 terminal failure。
- report job：132971537272，官方 terminal success。
- 运行创建时间：2026-11-15 21:12:17 UTC；report 完成于 21:53:07 UTC。

以下身份来自本次真正取得的完整原文本。日志身份含原 UTF-8 BOM，不先剥掉 BOM 再冒原文件 SHA。

| 原件 | B | SHA-256 |
|---|---:|---|
| compute 官方日志的实际返回文本 | 199967 | 19a0dd6e41afa2b9ac7c175ec6f35dcbb249ededb285a578ce640feffc9d9b4e |
| report 官方日志的实际返回文本 | 180496 | f54270b4e8da0a241efbd03174c018fcee7e4520b77921ed45722d17fbd4cee8 |
| 最终单份 necessary summary，JSON 字符串不含日志分隔 LF | 87897 | 8549fc6e2bb1ca4514b789e0995083aa2a07425b37c37e7434140472757c0c15 |
| wrapper 首次 compact reader 输出，尚未加 post-step 注记 | 86562 | 250276e28655bb7001748d6971107c5751b148bfef4788fd1eb39c7d2be86cb4 |
| Actions 临时完整 status | 29251870 | 979e391ba22e13d3a4e8ca259f414391f3ac5f513395d9e33dfc73a13af5fdaf |
| Actions 临时完整 event JSONL，1237 events | 3226182 | 96077dd773768ff40b632321dbc2d19aa0b00e6688b0c1144df63573c20787d3 |

原 status/event 大正文没有通过工具搬回，没有在 Git、Release 或 artifact 留存。本文核读的是上述单份必要摘要与两份实际日志；大原件 SHA 是原 reader 在 Actions 内完整读取后给出的身份，不称为本文逐数值复核。

计算 steps 1–7（checkout、runtime、完整来源和四输入、原 78 源恢复）均 success；step 8 科学 failure；step 9 必要读回、step 10 原错误与 stdout 身份、step 11 条件清理均 success。report 不运行、不重启、不续算科学。

## 401.3 真父点、同一有限模型及固定尺度

本次真父为 [R395](R395-actual185-complete-ten-full-three-normal-eight-directions.md) 的 actual185：

| 父身份 | 原值 |
|---|---|
| run / source | 43759673057 / fe5f7cc2bc612d009d25e859a877bf3f9e766ecd |
| compute / report | 132951426792 / 132952034624 |
| producer schema | R259-completed-ten-full-three-predictor-normal-v1 |
| producer SHA | 5eb4d38dbee0291dbfd0246baf94c904c735e546c82edb176b86f20744bfa89f |
| status | 2270732 B / 8d337203c06d4b7bb113d89394374064b4de6dbdc05c8f6dcd52d419a2ed2236 |
| necessary summary | 76157 B / acc93f034be193eba0c763ecd3c69688f023fe72faedc02e89379cd240d2f810 |
| 真实参数路径 | final.parameters |
| 原停止词 | Explicit eight full-ten direction budget completed |

189 的初次 fresh model 真正重算了原十点的方程、merit、完整响应及初始 FD。原 fresh_initial_parent_word_comparison 返回 same_equation_words=true、same_merit_word=true；这只是已返回字词比较，不是接受门。没有读取父状态、J、merit 或 FD 作为当前求值。

这里保持的是有限 literal/原 Gauss 表模型：10 个参数，699 nodes，112 field/tail modes，Decimal50、ROUND_HALF_EVEN。新增 shape 固定 catalogue index 3，即 support 1 / power 4；全部十坐标可以变化。shape family SHA 为 09240b33b82be3f595e82df05d93b309baefd6eeb74f1c34ba3a095cb2548016，ten literal model 为 geometry_20261115_adjoint_selected_ten_decimal_model.py，10479 B / 8cb8352b76be0770ab565de3b24907faa302a86a75660b9f5ffaa9a23cc6a9b7。

原 binding 明确：新控制表为源 binary64 样本的准确 lift；不是重新在 Decimal 中生成全部几何表；完整原 112×112 zero-tail-J 已消费，但它不是新 g 的非线性尾响应。本文不把该模型改名为 R400/current-C 连续十族，亦不由 literal 导数诊断证明准确连续 metric、C² atlas 或非共振。

固定尺度原字词为：

```json
[
  "0.01",
  "0.01",
  "0.01",
  "0.01",
  "0.01",
  "0.01",
  "0.010751309729055790270477681013298138652831191583353",
  "0.01",
  "0.01",
  "0.01"
]
```

它们只由 actual157 的原九参数字词形成，xi 尺度固定 .01。固定来源仍是 run43729310294/source c71cbeac7fd13c65cf50c7eb39842e9949737b25，producer54167dff0ce67e9f8fe0fa5d2899c35f0f99534077f2530d90b296eee7537100；原 summary89063B/7411fd01db054215e5d22293f6a4c239aa482302bf75b4da123f35d500d0cad2、status51842612B/931b013b6cfaba4215065e0734c129ba2089662273427f7ebecc5df4f35ee2b0。189 不从自己的末 p 重新计算 S，也不从父小半径替换 xi 尺度；scaled_trust_radius 原为1。

原 Armijo 系数仍准确 lift 的
0.200000000000000011102230246251565404236316680908203125。
每个原 $\alpha$ 固定同一 base p/F/W、formed full3 slope 与原 Armijo bound；法向临时点只在通过原全三门后才成为 owner。其条件数学范围见 [R392](R392-complete-three-residual-normal-correction-on-ten-parameter-predictors.md)，本运行不把条件满秩、有效导数或小步结论直接当实际已证。

## 401.4 所有计划块、已开始方向与未访地址

全程没有重置 Decimal owner、S、radius 或总时钟。每完成一个真正原 8 方向块，仅其原停止词明确为预算完成时，才在同一个当前 owner 上 fresh 取得完整十列响应并开始下一块。

| block（0-based） | 真开始 | 原8方向返回 | 接受 / 尝试方向 | 原 $\alpha$ 条数 | 实际后继 |
|---:|---|---|---|---:|---|
| 0 | true | true | 8 / 8 | 16 | 继续 block1 |
| 1 | true | true | 8 / 8 | 16 | 继续 block2 |
| 2 | true | true | 8 / 8 | 16 | 继续 block3 |
| 3 | true | true | 8 / 8 | 17 | 继续 block4 |
| 4 | true | true | 8 / 8 | 20 | 继续 block5 |
| 5 | true | true | 8 / 8 | 20 | 继续 block6 |
| 6 | true | true | 8 / 8 | 20 | 继续 block7 |
| 7 | true | true | 8 / 8 | 20 | 继续 block8 |
| 8 | true | false | 5 / 6 | 13 | 资源中断，不续 |
| 9–15 | false | 原 key 未形成 | 未开始 | 未形成 | 原完整后缀 |

blocks0–7 的原停止词均为 Explicit eight full-ten direction budget completed。blocks1–8 块首均是 fresh-complete-ten-response-at-owned-current-point，原 first_forward_equation_words_equal_owned_primal=true。块0使用 global-initial-description-complete-ten-forward。

全局 directions0–68 各 accepted=true。direction69 为 started=true、accepted=false、alpha_trial_count=0、原 stop=null；它的全部原 $\alpha$ indices0–19 尚未访问，不能称20档全拒。directions70–127 started=false，各原完整 $\alpha$ suffix0–19保留。block8 的原 local directions6、7未访；blocks9–15每个local0–7未访。原必要摘要含全部128计划行和全部158实际 $\alpha$ 行，没有用最后几个事件猜缺失后缀。

接受档的完整索引规律由原158行逐行读出：

- directions0–29：先试1未接，再在1/2接受；其余 $\alpha$ indices2–19未访。
- directions30–68中偶数方向：1和1/2未接，在1/4接受；indices3–19未访。
- directions31–67中奇数方向：先试1未接，再在1/2接受；indices2–19未访。
- 没有追加第21接受档，没有对原全拒方向重启；此次也没有实际发生原20档全拒。

以下表保全部69个原 accepted after merit 字词。原 reader 对每一字词确实相同的 before/前一 after 采用显式引用；全部 alias mismatch 列表为空，缺 key 与显式 null 另有 presence 表，不以缺失填零。

| 全局 direction | 原接受 $\alpha$ | 原 accepted after merit |
|---:|---:|---|
| 0 | 0.5 | 4.2974718870912152394995028073581364968418836547657 |
| 1 | 0.5 | 4.2375632864208903130644127507024691025986130527299 |
| 2 | 0.5 | 4.1886427059335324810241383630184668660105186190919 |
| 3 | 0.5 | 4.1299251214406249152206275294408930738069168582678 |
| 4 | 0.5 | 4.0819508668995514495847137933709250796460050963754 |
| 5 | 0.5 | 4.0244809196757684360761580410188582801321484657438 |
| 6 | 0.5 | 3.9777433629556317446710374240407014630385518408486 |
| 7 | 0.5 | 3.9215420725038412287839893826128302825864347362830 |
| 8 | 0.5 | 3.8762564284715582826668297383228865461151348480329 |
| 9 | 0.5 | 3.8213261555239672253875124795933321518718482259560 |
| 10 | 0.5 | 3.7776787882548070701308744615137388383123475641134 |
| 11 | 0.5 | 3.7240098462137769868216789287672128139577987252365 |
| 12 | 0.5 | 3.6821842106252135121037661819214366331663482487740 |
| 13 | 0.5 | 3.6297569640466974991808850485231457467757277238594 |
| 14 | 0.5 | 3.5899524579086110599014757713141799977314619389318 |
| 15 | 0.5 | 3.5387368749331637479938777681753557894956755776700 |
| 16 | 0.5 | 3.5011866230315359515554988980227767928100305717592 |
| 17 | 0.5 | 3.4511399728776841829683466587058876567982757316056 |
| 18 | 0.5 | 3.4161314614241788172052214652418392518426564059716 |
| 19 | 0.5 | 3.3671943331618809109856917759237373782410196015295 |
| 20 | 0.5 | 3.3350966754067739096819468928220663879580145015916 |
| 21 | 0.5 | 3.2871872905063904818154259056949744872926055374165 |
| 22 | 0.5 | 3.2584899328331105159442780590954762041572173331338 |
| 23 | 0.5 | 3.2114967415492432822381706573488368623869593347628 |
| 24 | 0.5 | 3.1868665240280399779088860907581743855598121858549 |
| 25 | 0.5 | 3.1406393820142215257289049475522701247139271142866 |
| 26 | 0.5 | 3.1210061375527678539208378277379703843196005498072 |
| 27 | 0.5 | 3.0753471304898740759895579605144637555332574454278 |
| 28 | 0.5 | 3.0620321375640347247160727156320055300175789190262 |
| 29 | 0.5 | 3.0166885622228407017291701674105636644793239599446 |
| 30 | 0.25 | 2.9910344239138334459159211205100480053921569676343 |
| 31 | 0.5 | 2.9434006309635043702926660311307504120230743748802 |
| 32 | 0.25 | 2.9176200080319398161077832050946304750077312651755 |
| 33 | 0.5 | 2.8708672517215377621563905887126245021903958106773 |
| 34 | 0.25 | 2.8454651847109341775070375698231022964702706727498 |
| 35 | 0.5 | 2.7994941796067547047608222883415012802468051753979 |
| 36 | 0.25 | 2.7744997625172049349256792892179312376411979524616 |
| 37 | 0.5 | 2.7292953226379109650860396712885576687378514566034 |
| 38 | 0.25 | 2.7047066715801762718197312343821500692447792134918 |
| 39 | 0.5 | 2.6602622095332221500968423519402265180171161447064 |
| 40 | 0.25 | 2.6360759652794349660714375950962167624690500108809 |
| 41 | 0.5 | 2.5923853423376320484658057077749108950039190302337 |
| 42 | 0.25 | 2.5685980752204070588607712757850100907485304235664 |
| 43 | 0.5 | 2.5256552132570509209368220505724542394926482940468 |
| 44 | 0.25 | 2.5022634922705438855640586667454262176352790728404 |
| 45 | 0.5 | 2.4600623510918861143159177301491888970679905330458 |
| 46 | 0.25 | 2.4370627463494124905960478226495916765850675294228 |
| 47 | 0.5 | 2.3955973189637342996729276430331890240335777931115 |
| 48 | 0.25 | 2.3729864007237210431130960536851518486471648961962 |
| 49 | 0.5 | 2.3322507098620091717861761595967222529664964924124 |
| 50 | 0.25 | 2.3100250475420199330311966072323536851322460604099 |
| 51 | 0.5 | 2.2700131424830812412588760935171795010870533899882 |
| 52 | 0.25 | 2.2481693038369203631501875151425361047135250725390 |
| 53 | 0.5 | 2.2088752574134988484106801236460223348416466877065 |
| 54 | 0.25 | 2.1874098078588110422840719416978899994584607371702 |
| 55 | 0.5 | 2.1488277135772835882205394239975519399225419811748 |
| 56 | 0.25 | 2.1277372156531902831497273565453864186134524594591 |
| 57 | 0.5 | 2.0898611848712195205671612397966701713513146402946 |
| 58 | 0.25 | 2.0691421978085647211458130787852357111126227877684 |
| 59 | 0.5 | 2.0319663569229484903279970417851087886560385483694 |
| 60 | 0.25 | 2.0116154363130021881062362747022456075429044951920 |
| 61 | 0.5 | 1.9751339239165083834231372567563861321786600897048 |
| 62 | 0.25 | 1.9551476214668419825107364129725387387576347903871 |
| 63 | 0.5 | 1.9193545854384192052943154963568037381813803133542 |
| 64 | 0.25 | 1.8997294488071458825120755320484970709471950329478 |
| 65 | 0.5 | 1.8646190433047425873097507937701273611114214049801 |
| 66 | 0.25 | 1.8453516160064659705508950878554670870029722224574 |
| 67 | 0.5 | 1.8109179983359243201661532674495544281825526370624 |
| 68 | 0.25 | 1.7920048197146154915389967007746182829336465880156 |

## 401.5 完整全三校正实际工作量与责任

所有158个实际 $\alpha$ 档都真实返回了1个 predictor primal及3个校正 primal，并完成3次 fresh complete3×10 normal response。全部69个owner采用点都来自 normal update2/trial0，beta=1，实际采用点没有激活径向投影。该事实只描述已记录有限运行，不保证别的点或预算同样成功。

| 原计数 | 实际 |
|---|---:|
| 原 $\alpha$ attempts | 158 |
| nested actual primal attempts / returns | 632 / 632 |
| fresh complete ten normal response attempts / returns | 474 / 474 |
| normal updates started | 474 |
| normal trial records | 474 |
| temporary normal working updates | 405 |
| 从 corrected point 选出的 outer candidates | 69 |
| projected normal proposals | 172 |
| 所有已记录 normal direction models | 474 |

原 normal stop 计数：89档为 Explicit three full3 normal updates exhausted; no owner acceptance inferred，69档为 Original full3 Armijo returned an actual domain-valid point。原 normal trial reason 计数：69次原 complete3 merit Armijo accepted，405次原 full3 Armijo rejected; full3 target-deviation decrease advances only this alpha working point。后405次只更新相应 $\alpha$ 的临时点，没有污染全局owner；也没有被计成接受。

全部632个 nested primal 的原 domain flag 都 true；实际 all_original_trial_failures_and_exceptions 和 additional_named_normal_exceptions 为空。normal incomplete_current_records、actual_counter_differences、normal_response_return_presence异常列表亦为空。这里只支付原已返回有限节点/中点测试，不从632个true推出全域连续正则性。

完整模型调用器还包括初始描述/FD与外层方向响应，原总计为：

- primal693 attempts /693 returns；
- forward544 attempts /544 returns，5440 forward columns；
- exceptions0。

因此不能把 nested632或normal474冒作全部科学调用。原 fresh_original_nine_model_call_counts 为零是对应旧九包装器的计数，不是新十模型没有运算。

## 401.6 predictor 偏离、实际采用点及其原全三量

原 normal_readback.all_actual_primal_merit_extrema 保的是全部 nested primal 的原标量极值，不只已选 owner：

- 最大原 merit 位于 direction68、alpha_index0、predictor=true：
  141870870.75325300038013778807792346746885600577260。
- 该 predictor 原全三方程：
  -1.7444958616970933131520120804026252100673435381723；
  -0.69648957254664279866110050929389133364737000202030；
  -16844.635287774635122742215356463468249816793936131。
- 原 Armijo bound：
  1.7957465515349058416367144580003560666470870337853；
  accepted=false，reason为 Original complete3 merit Armijo rejected。
- 原 full3 target-deviation merit：
  141859373.99120685455198486674608286213752039370976。

同一direction68的alpha1/2 predictor merit原为
8847738.5294868163999313503318324988259414991310715，最终该档仍未接；alpha1/4 predictor merit原为
552865.23972515837293886940908419521931418265752935，其后完整全三校正才得到真正接受点。不能把 alpha 行里的 predictor_merit 当作最后所选 normal 点的 merit，更不能说1/4原线性预测点已经通过。

最后接受点的原 affine_three_target 为：

```text
-1.7615943523132360531394708454581302332922823866120
-0.0012850011693509926748033374465622294371242607048367
-0.69339048552992503336082728548915276103214712873323
```

其实际 full3 target deviation 原词为：

```text
-1.3091900049899645928770466455319963541E-12
-6.25955748152999177487335597483029295605822E-11
-0.00000213492010739346027576411861431240705988183779
```

原 deviation merit 为
2.2789419344364119610754745908802654046935244172249E-12。
原 projected/unprojected scaled L2均为
0.28893618815128217609839758686035138945365685107713，
projection_active=false，radial_projection_factor=1。完整原点参数身份两者均为
6cde2c5de1c286bcf423422a4b4f0f34bb6eb61f40660a1ff87e8e76c9f69205。

这说明此次有限 full3 correction 能把所选档的真实非线性偏离大幅修正，并实际通过原 merit 门；它不等同于三方程为零，也不把原 derivative、SVD、拟合或normal remainder作为新接受标准。

## 401.7 最后真正接受的十词与原门见证

原路径一：
current_accepted_ten_parameter_words。

原路径二：
trial_conclusion.first_and_last_selected_original_points[1].original.actual_parameters。

两路径逐字符串完全相同；路径二含 direction68、alpha_index2、original_owner_direction_accepted=true、normal.update2、normal.trial0、beta1。原 complete_original_alpha_identity 为164225 canonical B / c9aae5b83cc4089afaef86d8bf75f12b2cd2df35103841a36d994ed6561a4c33；实际原 normal candidate identity 为6565 canonical B /64cbd12197a89f9493541e426cef6cecff4821934d1c82658c1a23cdaa0d3155。

| 参数（原顺序） | 最后原 owner 十进制字词 |
|---|---|
| p1 | 0.30349714070335898202049490814191077205575467864259 |
| p2 | 0.22320768974262297170414986995579884450841998149419 |
| p3 | 0.34081705005491527094864297864650612156455583844009 |
| theta1 | -0.069175246714031320186776691087337749389739707375868 |
| theta2 | -0.015506713450726331055293869372957681520904387286358 |
| theta3 | 0.93421350081504509386680316080616227348253782114646 |
| eta1 | 1.0695276807467625106931097655550841166478724545351 |
| eta2 | 0.62656309587554530255529775529366865178791645293775 |
| eta3 | 0.94772070126252395783272186025386560172248319686079 |
| xi | 0.38289088706268504028829015458735618531240133888561 |

原全三残差为：

```text
-1.7615943523145452431444608100510072799378143829661
-0.0012850012319465674901032551952957891854271902654189
-0.69339262045003242682110304960776707343920701057102
```

原 actual_merit=1.7920048197146154915389967007746182829336465880156；
原 original_Armijo_bound=1.8071251366356697005337935650872548377986862362431；
该 direction 的 formed_full3_slope=
-0.075857234005092388436271658404394364385849096750166。

该点原 circle node_and_mid minimum beta² 为
0.00515312939275526298554361089024385841844669560980；
原 scalar node_and_mid minimum radius 为
0.30000000000000026645352591003756970167160034179688。
这些是当次原 finite primal 返回的节点/中点量，不是最后 Arb 全区间结果，也不是新连续 C 的全域证书。

这里恢复的是**真实原门已采用的数值参数**。没有恢复不存在的 final 描述，没有由 status SHA 反造场，没有把该参数点称为 accepted native 或物理450 checkpoint。

## 401.8 已付初始完整 FD 与未付终态 FD

初始完整十轴、三档 Decimal FD 与 binary64投影FD共60 checks全部valid，实际异常列表为空。计划的全局末60检查因资源停止没有返回，故本次不能写成120都完成。

| 原视图 | step 的原显示名称 | checks | valid | 原 maximum_relative_error |
|---|---:|---:|---|---|
| Decimal50 | 2e-5 | 10 | true | 3.7244566343333405080331643002032340844064632496699E-9 |
| Decimal50 | 1e-5 | 10 | true | 9.3111415836128214864776422034404421460621751134868E-10 |
| Decimal50 | 5e-6 | 10 | true | 2.3277853957644222602114178437585008150934215595893E-10 |
| 原 binary64 投影视图 | 2e-5 | 10 | true | 3.731853030712753e-9 |
| 原 binary64 投影视图 | 1e-5 | 10 | true | 9.49165711744071e-10 |
| 原 binary64 投影视图 | 5e-6 | 10 | true | 1.2225140512269572e-9 |

Decimal的step实际为原binary64数的完整准确lift，不擅改成短十进制实数。原三step字词依次为：

```text
0.00002000000000000000163606107828062619091724627651274204254150390625
0.000010000000000000000818030539140313095458623138256371021270751953125
0.0000050000000000000004090152695701565477293115691281855106353759765625
```

初始 complete3×10 forward response 原canonical identity：
1639 B /12cf709cad490c08a7ceaa9591dcf523fee702ccbefc55002b21d137d4c780b1。
初始完整112×10 forward payload：
11673 B /e0a0c8e420b56700f204ae2b53b0f85e442218ed4b4bd9119eedfdfe33af484b。
forward primal 方程词与真实 state 相同。

初始 binary64投影3×10 singular_values 原为
[161551158.35077256,296536.2613134227,4.254524076020001]；
first3为[151913063.72057417,218622.46473443075,0.728064301444352]；
old9为[161540400.99378246,296535.4972342274,1.9640230395763958]。
原 numerical_parameter_condition=37971616.91041588。
这些仅为初始投影视图的原数值，不是末点值、严格秩、横截性或非共振证书。

初始原 radius cell denominator minimum absolute为
0.99915678962362412732576597396409374528145589252263；
初始原节点/中点minimum scalar radius为
0.30000000000000026645352591003756970167160034179688；
初始 source circle minimum beta²为
0.00515312955692829884499761715757417270478859413623。
投影视图的 radius/有限圆统计及原 low collocation residual均保原scope，不传给未返回的末描述。

原 projected zero_tail_slope_J 记录 shape112×112、all_entries_consumed=true、exactly_diagonal_as_recorded=true、offdiagonal0、ready_linear_graph_used=false。该原固定zero响应不替代当前非线性native；high_free_core_Schur_elimination_computed=false、high_mode_nonresonance_proved=false原责任不变。

## 401.9 资源中断的确切位置与不可外推的原因

原 wrapper 在 whole_child_wall_seconds=2400 打印 request189-explicit-resource-stop，child_receives_original_checkpoint_signal=true。wrapper received_signal=null；它自身没有收到外部SIGTERM，而是到既定whole-child资源时间后停止自己的子程。

原 traceback 的关键链如下，省略重复的递归clean帧，不省首因：

```text
completed_ten_predictor_normal_resume.py:438  continue_original_blocks(...)
completed_ten_predictor_normal_resume.py:231  search_module.search(...)
fixed_power_ten_predictor_normal.py:401  checkpoint()
completed_ten_predictor_normal_resume.py:229  synchronized_checkpoint -> checkpoint()
completed_ten_predictor_normal_resume.py:353  raw=k.encoded(status)+b'\n'
nine_control_decimal_literal_model.py:91  json.dumps(clean(value), ...)
completed_ten_predictor_normal_resume.py:367  stop_signal
ResourceStopped: Received signal 15; do not infer a mathematical failure
```

信号恰在完整status编码路径被抛出，这是实际观测。现有日志没有分项科学/编码耗时，不据此断言2400秒主要耗在序列化，更不把checkpoint成本推为唯一失败原因。可以研究语义相同的必要状态写出方式，但不能以未实测的性能猜测替代此次资源事实或偷偷增预算。

已经执行的完整nested primal/normal记录均有返回，direction69还没有实际alpha记录；原资源中断不证不存在下一接受步，不证存在解，也不证原方法收敛。405次normal临时更新与69次owner接受已经由原记录分责，不因后续signal撤销其历史数值事实。

## 401.10 原来源闭包、四输入与规则同步

六运行件保持已发布字节；路径默认相对topic，workflow相对repo：

| 文件 | B | SHA-256 |
|---|---:|---|
| computations/geometry_20261115_completed_ten_predictor_normal_resume.py | 47259 | 295c375b016a16bbdd7bffe68db7ffcdd3f715c33eee7a20147e9b5c379d0f8a |
| computations/root_20261115_completed_ten_predictor_normal_resume_readout.py | 46481 | cfebee555d55d6937541b360c189d0f6e0e89219f045e0f53d3d929a88287b1f |
| computations/geometry_20261115_completed_ten_predictor_normal_resume_temporary.py | 22789 | 527926ca8b51d1196d4762dc46602574962725c0cfc87a58cdeb285c3293d831 |
| computations/completed-ten-predictor-normal-resume-actual185-parameters.json | 14570 | e3c28f12454c654a828ad35c2c118eba2f63db98904e2341f502b7cf62f7902e |
| computations/public-completed-ten-predictor-normal-resume-request.json | 62318 | 252dfa6c4cf60a17377ab24ec9c1be67a91851b2baf94638a3b826b64e913a19 |
| .github/workflows/visible-larger-public-completed-ten-predictor-normal-resume.yml | 31215 | 2c2ef4d4fc143b636d248e8e54853c4f9983e9390f4e292b47254dfe8fbf7a38 |

原workflow实际打印 source_count119、workflow_support_source_count13、origin_child_source_count48、current_child_source_count49。当前完整49源canonical closure为6088 B /8bd39ccfc7c6852baab3f97167cceedb752351997ed4c6f0de2f79c1bd9e9157。原normal helper/search源数学没有因续算改写；新producer仅显式同owner多块与完整资源/来源编排。

四数学输入原SHA不变：

| 原角色 | SHA-256 |
|---|---|
| accepted | b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff |
| prepared | 0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714 |
| tail anchor | e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51 |
| tail config | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |

四输入及原78公共源仅恢复一次到runner自有临时目录。本地本文没有下载这些科学payload。

原规则runner SHA仍3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde；周期2700秒，真正pull/rebase及发现规则变化停止的实现保留。实际日志 request189_explicit_rules_baseline_update 明示root README从原runner内旧pin更新到已读21bd547f56590b7f2dd279d0297efb289a9b2783，topic保持bff8aea253a9e6a7a4fac28d810ac454c5499fec。不是仅改文字冒实际同步。

本次 actual_rules_sync_completed 的原记录为round0，2026-11-15 21:12:58 UTC，origin_main_read=ca1fe0d562497055f9e5441edc17ac588a25229c，published_commit=c136747a87f8483b7d6841bed98d02d32264e7e1。sync-0000-completed.json原700 B /d3a964b0acce83f1ce4234bfd97eadee700ae9bfa6f1b68d1a8562a151abe7eb。本文不把本地文件读取或GitHub API查询改称本地pull。

## 401.11 读回、raw清理与未独立支付范围

必要reader在Actions内读完整原status、原方向/全部alpha/normal记录和eventledger，再只选择必要标量、原极值、地址、原来源与SHA。读取时metadata_errors=[]、required_available_recorded_fields_complete=true；没有重新运行模型、计算FD或残差范数。

原完整方向记录canonical identity为28823797 B /86408bfc14593fbc13591e99560fcdc7ca2409522d9e405d1459339e258756e1；完整trial列表canonical identity为25846259 B /c30313ba942ec29bd19ad5f80941db9fa81f9900b5557b78e55b23ae5beb77c9；normal candidate列表为3721452 B /961b36b26029ae81d4feb507b3351e0d5e9f2139c68bcc9b778d422e890714a0。它们不是本文额外获取的大文件。

单摘要保全部128计划方向、全部158实际alpha、69个normal选择地址、所有已录失败与异常、当前后缀、最坏/最后见证及初始FD。完整每点参数、所有d/J/QR、中间大full112向量与所有非选normal向量没有逐值传回；摘要明示 first/last selected详细点之外的这些范围只保身份。本文不能据完整hash声称已独立逐值复核。

原 producer stdout445 B /ffdb281ed5364903f71fe66dfa0c5ef60b5c73b855b1b89fbf924113fb18fefe；reader stdout90958 B /1b066b73825d96f65dbdc7a27fb2b1c2271b83a8c68b69c9b05802cd37dfe403，仅stdout整体身份，不能把该带marker/说明的长度当作87897 B单JSON超限。producer/reader stderr实际均0B，SHA均为e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855；原完整traceback来自status，前文已保具体首因。

step11真正执行的 request189_temporary_scientific_payloads_removed 记录明确：单份必要摘要、原错误与子程quiescence在前；随后只删除本请求自有science目录、四输入目录和恢复原源目录。没有原artifact或Release上传。读回成功不由清理成功倒推，反过来也不因raw清除撤销已返回必要原件的身份。

## 401.12 可恢复边界与最小下一实验

R401 的可恢复输入是第68号方向、第三个原alpha档、normal update2/trial0通过原owner门后留下的十个参数字词及固定S。第401.7节给了全部原词与直接路径、原选点身份；不是从SHA还原未知数组。

因此下一独立请求可以：

1. 将这十个原词明确写入新的数值参数recipe，parent origin绑定本run/source、status29251870/979e391b、summary87897/8549fc6e、两原job和明确原路径；同时保parent phase=resource-partial、diagnostic_completed=false、final_present=false、accepted_point_count69及真正selected地址。
2. 维持actual157原固定尺度、support1/power4、Decimal50、原全三merit/Armijo、每方向20alpha、每alpha3×20normal与全局2400秒。不得把原partial父改写为已完成parent分支。
3. 对该新初猜重新建立当前state、完整J、初始FD；新的末FD/Arb/scalar/453消费者及所有原终门仍须本次真实执行。历史F/W可作来源说明与fresh读回比较，不作为当前状态。
4. 若原末字段仍未返回，继续逐实际后缀报告；不以本条参数恢复付native、fullDN、非零场、continuous-C十族、闭面/metric/held/有限t等最终责任。

本文没有派发或完成该后继。R401已支付的是实际69次原门下降、完整必要来源/读取和资源部分终态；课题原终门仍未完成。
