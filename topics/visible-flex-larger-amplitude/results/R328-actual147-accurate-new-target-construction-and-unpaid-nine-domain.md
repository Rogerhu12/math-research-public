# R328：actual147 准确新目标构造、完整基底域与原九参数未决范围

维护：ChatGPT /root（GPT-6 Astra Pro，AI-assisted），2026-11-15。

实际公开 run [43717814570](https://github.com/Rogerhu12/math-research-public/actions/runs/43717814570)，科学 source 为 3b2df31a555b9466911c9b0b3e9b45c7df576c41。compute 132823027880 与 report 132832524225 全部成功结束。这里的作业成功不表示原九参数合法、BVP 接受或固定闭面完成。

本次已经从真实 M96 core、同次原连续 C/cut 输入及实际146九参数，生成一份独立准确 v3 目标定义；R323 的十一项严格构造条件全部成立，未加九控制的完整基底域通过。原九参数的完整域检查在声明资源内未完成，数值 profile 的编译也不补这个缺口。全部原 C/切口/构造摘要及完整 width/seam 分段已经读回，随后 owned raw 清理；没有新增 artifact、Release 或 Git raw。

## 328.1 实际来源及读回身份

| 项目 | 原实际身份 |
| --- | --- |
| request | 17398 B；4b6f78bb25e0d87354e2ad786637fc9e4db5c7c34774d3cad4716638552ba707 |
| 独立构造 wrapper | 20377 B；738dd352cf62fbd47eb80e867ac441b7d0c179074cbee93fb8dd6528ba0d4cb0 |
| v3 accurate factory | 42270 B；0d89370df95c6063cb336182d87137705d5e4ddb87625a3fb1b58b35695a621e |
| numerical profile | 22469 B；7cfab12ebb8bf4a948336e7c605ea096a9597be43a4582f166f9067850ea4b60 |
| 原 shared-jet core kernel | 40466 B；a9a25d96eeb286d9f2214f997c992e50e42f6e6ec2bc59c136a183febe2a0703 |
| compute 解码日志 | 455002 B；dfda299cd8f5f18db562f497d8fb7f80cb760700b78768fc8ab22ca940cdc303 |
| report 解码日志 | 254278 B；19da9d4f63c4e924951e54c44f5baa4f8b65cbd36f7314b0b410e874ba4bc718 |
| 原 C 完整读回摘要，不含分隔 LF | 27508 B；91e375ab2e8fc749847b14114a231241327135819644755603a0cd88ff3415bc |
| cut 摘要，含原 LF | 5830 B；ef508448fd7f713cfd3ddcc526e6dfe5dfff38cd320ec7dbbde96959d7f07fe2 |
| 构造摘要，含原 LF | 27194 B；c581727c2097e723ead529013c33ef2b48c787d7ce8704ee075f57b1f950f5b9 |

三个正式摘要在 compute 与 report 的原 JSON 行逐字相同；构造摘要在 compute 的 always 读回中也逐字相同。两份解码 job 日志身份包含工具返回的初始 BOM 和全部换行，不冒原服务 ZIP 身份。

19 source pins、原 source-dependencies 所列恢复路径、公开历史 8bd267107cc8710d371f3b62c02986655ac965b0 的四原输入均实际检查。accepted 原压缩字节为 2614352 B/b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff，解码 8019880 B/4673d2f1c65b9f87e48dbc98c3978bc5296593673c85775b3f8d5e1089be5362。config 为 2161 B/01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5，另两 ready 输入保持原563a9997与c1c44f23全 SHA。原始输入没有重写或重新归档。

原始 E 科学 runner 从 13:13:23 到 13:43:24 UTC，construction runner 从 13:43:27 到 13:48:29 UTC。两者 science/wrapper returncode 均为0，periodic_sync_failures=[]、README_change=null，science checkout 未移动。实际规则同步分别读取3b2df31a555b9466911c9b0b3e9b45c7df576c41和1f26e63c05587c624ee53e77f1072fb11aea2701；不把 root 的集成 API 调用冒充这些 git pull。

## 328.2 同次完整 C 覆盖与 cut 输入

原 C 数学源仍 f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df；完整160 finite cells、1440 pieces、六 primitive A/B/sqrtE_A/sqrtE_B/w_A/w_B以及全部 n≥160 的准确深尾族保留。原全参数、精度256、integral绝对96/相对80、1800s、查询点+整个自然域没有缩减。

完整 finite head 和全 deep+head 的六 primitive 已付；1440 source pieces 完成。原查询两项均有合法闭域包含，原work-width只对cut点完整；whole查询仍未付部分宽度。没有 source/query 后缀被省略。

| 原返回项 | 实际原值 |
| --- | --- |
| E producer elapsed | 1800.9043813389999 s |
| cut 查询叶范围 | [0,1)，1个head叶；5次 refinement |
| cut E work-resolution | true |
| whole 查询叶范围 | [1,75014) |
| whole refined nodes | 60368 |
| whole unresolved-resolution fragments | 2887 |
| 完整 unpaid rows | 2888＝2887 query-resolution＋1 late integral-panel |
| source/query 未访问后缀 | 均 null |
| producer error | null |

晚期未付积分是 whole inverse-query 的原 piece1398/cell4/segment3/depth0，完整闭参数区间 [7903/32768,63225/262144]；实际停止分量 B，捕获 ResourceStop 后按原支持机制以 ValueError 传递。它发生在完整初始六 primitive 已完成之后，不冒缺失初始 source piece，也不写成数学域失败。原 A/sqrtE_A/w_A 完整端点包围与剩余原工作宽目标照原记录保留。

实际 result.json 为 23099 B/990f34cc51c124b1a4ca89ce094ed438dfa63520d521e64f19b20c8fd06168f5；query-results.json 为1922 B/d85a4a53004bf004210694b1599ec754ad1b12cee1e4ac5ae001f95d190080c5。完整 query-leaf ledger 75014行、136735915 B/cefb47580a12ee255b64e464c7fa65b0324048c99042962b79f69b566043cb2e；unpaid ledger 2888行、5837013 B/dc95dc2003086d710c3b0a09323e33a79752af5c6f4705949b285a3fdb2379d5。全部 raw 已清，不能由这些 hash 恢复给后继消费者。

cut reader仍1c39b242224824b361cbe5d28ea838b7e4824f5506a05302c662f045f735aeed，实际 cut-twojet-readout.json 为5684 B/952b5f6e01d4bc9361bde964f70bea11ad01ad118d43e0e5dd7b56068b99d8f6。原 cut binary64 字为333333333333d33f，准确值5404319552844595/18014398509481984，不改成3/10。

全部cut叶共同给出的准确 dyadic 端点如下；它们与 [R322](R322-actual144-original-cut-twojet-and-complete-domain.md) 的对应数值逐字一致，但本轮文件、运行和完整 whole 覆盖身份不同：

| 量 | lower mantissa | upper mantissa | 共同二幂指数 | 原 full-width mantissa |
| --- | ---: | ---: | ---: | ---: |
| E | 297036851754023534385 | 297036860731551973169 | −68 | 8977528438784 |
| E_r | −1377364570695686333 | −1377334639942752445 | −62 | 29930752933888 |
| E_rr | −18506607869532518095 | 3541147354781501745 | −57 | 22047755224314019840 |

原cut域/work完整，不把 E_rr 的宽盒改成额外接受门，也没有把中点认作准确叶值。自然外半径与 nominal binary cut 的差仍由原 display [7.1701834641e−15 +/-1.01e−26] 包含，未平移cut或warp。

## 328.3 R323 的实际选择及准确新定义

core来自accepted的/fixed_scalar_profile/geometry，几何 canonical SHA为bf7b3c997d12599d08e2415cb41392a9dc72ffd33993aa169f1c146796858706；core_end来自真实/mesh/-1：

$$
L_0=\frac{4458563631096791}{4503599627370496}.
$$

完整准确 core 有415个 piece。原 endpoint jet 原值为

$$
A=\frac{328370512257523}{281474976710656},\quad
V=\frac{6448229427256939}{18014398509481984},\quad
B_A=-\frac{4526389216721259}{2251799813685248}.
$$

按照已经证明的 R323 有限严格盒公式，实际选出：

$$
\kappa=\frac12,\qquad d=\frac1{524288},\qquad
e_A=e_B=\frac1{1024}.
$$

两个选择记录分别为 exponent19和10，strict_lower_than_input=true；没有 root 精化、参数扫描或假设一次有限盒可任意收窄。十一项原 construction_conditions 均为true，包括同cut的半径间隙、严格内向且subunit的切速、collar导数界、两transition的半径/导数条件和正coast长度。

第一支撑保持原 PrefixControls 的 left/stored_width：

$$
b_1=\frac{3566850904877433}{72057594037927936},\qquad
w_1=\frac{4458563631096791}{18014398509481984}.
$$

原 left/right/stored_width binary64 words 分别为f2d24d621058a93f、355eba490c02d33f、ae47e17a14aecf3f。准确支撑使用left+stored_width，不用独立right字替换这个准确和，也不换成CompleteProfile的另一默认支撑。

完整 width-selection 的14295 B/16e05d7564ed5cbb648e0ee07435827649ddc3047bd23594be6b6f51d1a4d66b已从原1段逐字重建；其中所有准确盒、core jet、margin、R323输入和十一项条件都保留。

原实际146九参数全部转录如下，来源为R320原final.parameters；没有沿用其状态、J、域证书或旧搜索半径：

~~~json
[0.3055213835477326,0.21645013203050154,0.34270051957744246,
 -0.06322334619266512,-0.01747451701873286,0.9376115689625685,
 1.0751306255033548,0.6886900390922872,0.9385431607625546]
~~~

recipe真实1835 B/3a63455d9812abca1ef4e5dac9fdc71db63ed53162fc59090350f74b843fed72，原root_choice明确R286-dovetailed-rational-middle-third。数学表达式仍用共同的E0/E1/E2语义叶；没有在准确目标中代入中点。

准确 definition 377788 B/d783cac154af8a4f89424fa7513a44b4f80cecae16fb1ae32c12a0f9aec6d16c。它含415 core pieces与first-transition/coast/last-transition/cubic-collar共4段，总419；它不是原有限Gauss目标g的重命名。

## 328.4 基底全域已付，原九参数全域未付

两个原prove_domain pass保相同最大65536节点、depth32和每pass300s；原源没有改变。结果如下：

| 责任 | 未加控制基底 | 实际原九参数 |
| --- | ---: | ---: |
| complete | true | false |
| all_parameter_values_retained | false | true |
| passed_leaves | 452 | 1735 |
| processed_nodes | 485 | 28596 |
| unresolved_terminal_leaves | 0 | 12766 |
| unvisited_stack_entries | 0 | 13 |
| elapsed_seconds | 0.14156015200001093 | 301.4390672699999 |

基底完整 ledger 为342064 B/6b1f1b4fa45e367da81285f7cc50fad1e02f3263f54e04b9952142623ad2b5d6。原九参数 ledger 为416060793 B/f3e8fe52ef2fe120b2ab650a23e27866c70cb7dcf55702b67fed390fed715411。前者只说明准确基底的整个所请求前缀满足原a>0、|a_s|<1；不能把它冒作给定非零九参数的域。

后者不通过不等于已证明真实a≤0或|a_s|≥1。程序只给充分区间检查；宽盒、深度和真实资源都能留下未决。原summary确实保全部九参数、closed_coverage_kept=true和未决数量；但这不把其中未付区间变成已证明合法的域。

本轮log未输出12766个terminal叶与13个未访问栈项各自的全部坐标，只保原ledger身份和计数；raw清理后不能再补抄这些范围。后续151必须重新形成实际数据，并在清理前逐项输出完整frontier/未决范围，不能从计数推断未付范围，也不能静默忽略后缀。这是明确的读回限制，不影响已支付的基底域或准确构造条件。

本次factory returncode为0、wrapper error=null、phase=complete-with-original-paid-and-unpaid-scopes。原source将“合法地产生一份含未付范围的报告”与full_current_nine_domain_certificate_complete区分，因此作业success与这里的false并不矛盾。

## 328.5 数值编译与全部接缝记录

数值编译成功，模式112、活跃scalar9、三个支撑。实际字面长度为2.723563252110879；公共坐标固定u∈[0,1]。准确目标长度仍是共同语义叶表达式L，不能用这个字面长度ℓ替代准确目标的L²du²。

数值编译所用叶中点及原word：

| 叶 | 原display值 | float64le |
| --- | ---: | --- |
| E0 | 1.0064000151459218 | 23eefbe6361af03f |
| E1 | −0.29866508687182997 | 9993242b541dd3bf |
| E2 | −51.92187136748508 | ce3b87e1fff549c0 |

这些三个字面数未证明由一个共同真实尾根选择实现。数值编译 SHA为4519328ceeaeda10894b73721501cf6fa9bc137505ae78eebfa361f34723bf50；完整specification为270229 B/8d7c8cbee15b8081703caf60f0a926acf6db4bd94d6ae02db7f64619fed8c035。

完整418个相邻分片接缝从8段、152147 B/4c6cfc68b571ccfbf21ea6a6a9f846469cba5ad3c87f873fc446ff76e743efba逐字重建。下标依次0..417，left/right分别j和j+1，无缺项。对原六个word串只做字节比较，核原numerical_jet_words_identical标志一致：

| 比较 | 完整418项中的原字结果 |
| --- | ---: |
| 三jet全部逐字相同 | 207 |
| 至少一个jet word不同 | 211 |
| a word不同 | 0 |
| a_s word不同 | 99 |
| a_ss word不同 | 146 |

这些数目允许交叠，不把99+146当作独立接缝数。相同的有限a字不能证明准确实多项式严格C0；不同的有限导数字也不单独证明准确实解释不C1，因为两侧计算的舍入序列不同。准确C²由准确表达式/接缝定理承担；数值函数相对准确目标仍需自己的包含证书。

靠近新四段的完整原记录如下。每个括号按a/a_s/a_ss，保原little-endian字串而不在本地作科学转换：

| left→right | 公共station字 | 左jet words | 右jet words |
| --- | --- | --- | --- |
| 414→415 | ae47e17a14aeef3f | 301fce7b6baaf23f / 6a1e7168a1e8d63f / 6bb9601dba1400c0 | 301fce7b6baaf23f / 6b1e7168a1e8d63f / 6bb9601dba1400c0 |
| 415→416 | ae47e17a14b6ef3f | 6b72f79522aaf23f / fbffffffffffdfbf / 0000000000546a3d | 6b72f79522aaf23f / 000000000000e0bf / 0000000000000000 |
| 416→417 | a13ac387dac70540 | d626b2b3343fd33f / 000000000000e0bf / 0000000000000000 | d626b2b3343fd33f / 000000000000e0bf / 0000000000000000 |
| 417→418 | a13ac387dac90540 | fd8ead2c3b33d33f / a6baa8bae9e5efbf / 0080647fe4e0c23f | fd8ead2c3b33d33f / a7baa8bae9e5efbf / e33c647fe4e0c23f |

完整source、width与seam语义值的重建没有执行profile、积分、ODE、QR或任何科学计算。实际科学都由本公开库Actions完成。

## 328.6 当前结论与紧接工作

已付的是同次原C完整cut输入、准确新v3定义、十一项严格构造条件、完整基底域和明确数值搜索编译；给定非零九参数的域仍未付。actual_tail_J_or_native_calls=0；actual_BVP_or_fullDN_success、actual_accepted_field_created、same_field_metric_or_C2_geometry_certificate均为false。

151按 [R326](R326-common-coordinate-target-enclosures-and-same-field-metric-transfer.md) 与 [R330](R330-centred-common-coordinate-difference-and-target-coefficient-bounds.md)继续同次重生、公共u准确目标闭包含及字面参考比较，保所有可能准确分片、全部九支撑、数值lookup两侧和完整未决frontier。它不会把宽盒未决直接写成真实域反证；只有实际严格包含支持时才能作相应域判断。

新C完整699/453物理绑定、真正非零尾producer、全部内部图或明确非除式初始化、全current-H/112列/338响应/mean和独立audit继续。旧cut线性商不供给全部内部stage图，旧同名client也不能改标签冒作新C非线性响应。尚无新闭合非零场，全部README最终标准继续承担。
