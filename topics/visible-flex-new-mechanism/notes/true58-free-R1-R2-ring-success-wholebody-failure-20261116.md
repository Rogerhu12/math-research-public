# 真正58自由R1/R2：目标环成功、完整曲面预测失败，范围闭账

日期：2026-11-16。**当前实际合格点仍为58；本任务没有59，也没有新的原十四门实际值。** 本文只解释已完成公开Actions的原输出；没有本地科学执行、重算、优化或附加检查。

本次确实解决了一个与此前射线不同的有限环问题：原172盒内自由34个R1/R2物理控制加K/h，完整实际G下的两网谱门均通过，环曲率降到目标附近。唯一准确共同合成、一次舍入的168候选随后在全曲面预测中严重违反metric和原曲率门。因此该环解不能提升为完整曲面合格点，也不证明连续reach。

## 1. 原任务及实际来源

范围与生成列定义沿用[原设计](true58-free-R1-R2-original-box-curvature-minimax-design-20261116.md)和[合同](true58-free-R1-R2-125-generator-model-contract-20261116.md)。输入真实58仍是[原两网接受](true57-nonlinear168-original-two-grid-accepted58-20261116.md)，永久55只作constructor，前三个已闭环范围未重开。

| 项 | 原身份 |
|---|---|
| workflow | `.github/workflows/visible-true58-free-r1-r2.yml` |
| run | [43884276617](https://github.com/Rogerhu12/math-research-public/actions/runs/43884276617) |
| research / report job | 133358065602 / 133359165070，均success |
| source | 7ac3c637ec9fb7d151e7b0f7f2ee314dd137533c |
| request | 75313B；498633426b4bc0928e9397379235ad390dade8b54be2febe87457a74e6cecc6f |
| request sources | 337，原326源hash未变 |
| research UTC | 14:18:08至14:19:53 |
| 原research日志 | 38467120B；64d1bd45673f9de4b533008b812acc4300024f34a976edeeb1886fd896076a80 |
| report读取文本 | 1809224 UTF8 B；e722490942c21e28f08b6b4a0b1e9b2521c22577850bde742c9c43bf4dd5fdfb |
| observer | 3.608391687000001秒，只读、不另加科学总账 |

报告完整解析11个原记录，parse/unparsed均0，projection0，semantic_read_is_incomplete=false。报告自身运行时workflow仍in_progress仅因report尚未结束，后续元数据已确认两个job成功；不是将中途日志当成最终返回。

固定g仍为fd5bc5fe2c114bdbe82c266a5e816ba22ed58f1f486f5bc3241ddaac95de88b6；固定b0为d61fb298989834c9eb2b4fe3bbff1fb5983d1bb3b3980cb6441f14e6c0299bb5。原58 physical为94950b2bd5d7b5241e14333a4315b073f64840f74849a7909d6de8cb3cc29f54，ind168为e2d52f849596a5e7bbf596b66d7805587acc944c1549c5648ee4e115548ed2bf。

## 2. 一次真实后端返回及环门

后端为SciPy1.17.0 SLSQP，原status=0、success=true，message为“Optimization terminated successfully”。nit11、nfev11、njev10；11个完整新值/解析Jac评价started=completed、failed0，13次cache命中。回调计数：initial_full1、objective11、objective_jacobian10、constraint_value12、constraint_jacobian10、iteration10、returned_vector1。没有重启、没有从中途callback提取另一个候选。

后端原耗时0.16559417500002382秒，完整local capture 0.2172797960000139秒；账中solver事件0.21288230300001487秒是在稍早位置结束的嵌套计时。它们不相加，solver overrun=0。

原结果：
- K=16.393442622950822，准确binary64分数为2307171940251279/140737488355328；
- h=3.0112159595549572，目标值16.39344563416678；
- raw36 SHA256为7d0fca6df79e1693e80478adea56aae72354779835e8957ab68457d7bce0f3d5；
- decoded floating36 SHA256为bfba8c376a541ca9874a9fd88e789c3ca712f5cafb3f00e76884996aa3b73d0a；
- model binding为5fb6c3a80738f6f38b08159a5102dc1d0a88448958816dcf9013902367a4aaf0。

K恰在原准确下界1000/61向区间内包的最小binary64端点；该binary64数准确地**略高于**1000/61，故原ring_K_above_reach_target=true保留。下面的实际有限节点谱值略低于目标的浮点值，但这不是准确连续上界证书。

全部7362约束由6912非线性行及450线性行组成，后者是344盒、102norm及4个K/h行。零增量/K58/h0初点的scaled violation和原线性violation均0；原返回二者也均0。原PSD和线性容差均1e−9，实际G未强制置1。

| 原有限环观察 | 粗网 | 细网 |
|---|---:|---:|
| 最大形算子谱范数 | 16.393442215426443 | 16.393396474844106 |
| metric辅助η | 0.1682900404968013 | 0.16829003337480608 |
| min Qcross | 0.8709237236547421 | 0.8709237303337387 |
| 原未平方PSD四行min | [12.205064775052591, 0.000004973861273214037, 38.709429196443594, 353.8399420358378] | [12.205110529385275, 0.000563240613537388, 38.682534794315124, 353.8425008133333] |
| 原PSD / metric / 冗余Q | 全真 | 全真 |
| 最大原PSD违约 | 0 | 0 |

两网最大abs(G−1)均6.661338147750939e−16。保真实G/Schur和直接cross两个计算的原差，不以G≈1取代模型。

完整OptimizeResult字段fun、jac、message、multipliers、nfev、nit、njev、status、success、x均已保存。multipliers为7362项/58896B，SHA256 80fb01304754742619f7196ce17a2990a25f0cfe9765fd367e40ae4c3cb9833d；它们是后端最后内部QP的乘子，不是准确全局最优证书，也没有捏造未返回的bound multipliers。

初解析Jac形状7362×36、2120256B，SHA256 333c5871f3a770a4dfdb04a2364e9379c520a35aa926c1748231665e5d6368ef；末Jac SHA256 fe5c27d6fe51734b2471e35c6b6c43ead472122c09c9b107dfef559a9469f69a。实际固定7362行尺度58896B，SHA256 f55dacd7d38abdce608d6dc7d974075c2c42ccc2908f2e2dc750438227e55a74。它们只按原stdout身份保存，不另复制入Git。

## 3. 准确合成与候选身份

原返回按原完整物理坐标一次共同合成168，再准确重嵌172并一次舍入；没有先接受中间R1态。原盒、准确epigraph以及原hmax均真。

- 完整候选physical为ab59622808faafbb1a1896a2edc670585c13373869665fb95c31b6ca8a1f2773；
- 外层candidate_array_sha256为b252055bf59dbdd9e4d22691b2fd1c8ae35f88b2795c7a38f894876cd50c5da7；
- array-binding schema的SHA256为5da50ccd367a7d1f5c9f621737c5b2bafcaba2db0eb39e3875adcb3fe6fffbf0；其schema不同，不与前一个hash混同；
- 实际norm准确为6765104810131585/2251799813685248；
- raw h减理想合成norm准确为15550726560313/2251799813685248，未事后修改h。

完整未舍入增量、准确168/172、舍入误差及全部候选元数据保原RING_SOLUTION/SOLVE_TRACE/COMPLETE。它是**未被全曲面接受的候选**；这些记录不等于一个可用于59的新accepted CACHE。

## 4. 全曲面原预测明确失败

在同一原配置、同一完整两网和原58基准上，只做了一个全body prediction。原要求η至少下降1e−7。结果如下。

| 项 | 粗网 | 细网 |
|---|---:|---:|
| 最大metric辅助η | 6.979414564932138 | 6.979414564941248 |
| metric峰s / 径向index | .585 /111 | .585 /111 |
| metric峰θ / θindex | π/2 /96 | 3π/2 /576 |
| 最大绝对主曲率 | 69803.90363033222 | 69803.90363577171 |
| 曲率峰s / 径向index | .7125 /131 | .7125 /131 |
| 曲率峰θ / θindex | 4π/3 /256 | 4π/3 /512 |
| 峰处两主曲率 | [−69803.90363033222, 11.960152144182246] | [−69803.90363577171, 11.960152143966809] |
| 最小法向面积 | .011574199804767248 | .011574199804408264 |
| 原曲率PSD / direct门 | false / false | false / false |

原基准η=.26600541463999305，原记录的predicted_eta_decrease=−6.7134091503012545，远未满足下降门。η仍是metric辅助量，不是握持位移δhold。

原曲率cap仍58，direct容差1e−8、PSD行容差1e−9；没有为了环目标另换全body配置。粗网plusdet/minusdet scaled行分别−.04017153529012362/−.03428319526948566；细网分别−.04022933694752245/−.034283195268745605。完整原行与direct主曲率同时失败。

metric prediction binding SHA256为83a908f6e54361aba97006a1ce5a4a98b6a3889b60260fb1e87d189413a2358d；curvature prediction binding为3c99cb93f6d450dbaf38c4197bcdab710360665f5eb1fd051201786ff8e0693d。

因此qualified_for_original_actual=false；actual_not_called_reason原文是一个完整舍入候选未过原预测资格。**没有调用原十四门actual pair。** 不编一张“14项失败”表，不以预测值冒实际值。accepted index、58物理态、原g/b0、永久reference及原pool顺序均未改变。

本次全body预测大数组没有保存为后继可免费输入，只保输出中的诊断/绑定元数据。下一任务若需要这些fields或jets，必须真实新付；不能从hash或少数峰值反构为已付数组。

## 5. 真正新付的模型和算子

环模型读取已付完整scalar/frame/Z17/PiZ17/V17及原二jets；此环构建本身没有新scalar frame、旧V17 Pi、ordinary或full168 J。每网真实增加142列完整周期原函数：17个L和125个二次生成列。uu45/uv44/vv36是生成列数，不作线性rank声明。

| 新完整Pi批 | 粗网384θ | 细网768θ |
|---|---|---|
| 输入bytes / SHA256 | 1308672 /4666be7f3eefab591b9db7bb8cb01862bfd4f81fd988dd2ec5ebe2efa26759d0 | 2617344 /7e729282bc939126605978a5fd21acc12d5e9601df5eb9cb165b2093510375bf |
| 输出bytes / SHA256 | 1308672 /b9d570e779de77dcb21fb93e0af949d021dc889156c450e5219aa46ccabe9149 | 2617344 /ae0b3b866337f7296ee5ef106c1b767b0aac0506611a267c48c6866bf1030eaf |
| L17 bytes / SHA256 | 156672 /7914e7a81cc1ea3b99e8c54d0a7d7d6879072c64d374435f860847af6beebc33 | 313344 /a4bb16fac7312de153b5bcff17bec7fe13a0ba187c8bd621a7efc8cfbc4d427f |
| H125 bytes / SHA256 | 1152000 /2a991849a6aa7522036457a18de301117d69001e56cb4ae02921df5a984be2a2 | 2304000 /53ffe7184db43fc853037eacf8e694245e9bfeee6b9bbe723c7701e3a276aaef |


粗phase/Pi嵌套耗时.006236919000002672/.002446801999951731秒；细.013152167000043846/.006149714000002859秒。两批真实Pi输出共490752个浮点数，原MODEL完整保留。

已付a=.3399084551031785，准确6123246366971023/18014398509481984；a_s=−.9915007990920229，准确−8930645258656767/9007199254740992。metric_a_s数组160项/1280B，SHA256 ce514e393ec20782b1b4a8ac0422cb44818b84c815d9b5e0c11b487910a882d7。它们来源原58 selected index141的合法身份，未用缺字段填零。

不能把“环模型0新frame”扩大成整个任务0frame。唯一wholebody预测实际另付：
- metric预测baseline scalar frames2、candidate scalar frames2、periodic4；
- 曲率预测scalar frames2、periodic6、heightjets1、position assembly2、curvature values2、独立principal spectra2；
- ordinary/full parameter J/actual14仍为0。

## 6. 完整费用与已关闭余额

最终FINAL_CLOCK在所有大输出及COMPLETE写出并flush之后采样，是科学账的权威值。其前的局部计时不另相加。

| 账项 | 原返回 |
|---|---:|
| 新科学总秒 | 72.22285305100002 |
| 原祖先科学秒 | 2902.366570826 |
| 相关累计科学秒 | 2974.589423877 |
| 新necessary full值 / actual full值 | 0 /0 |
| 累计原full值 | 147 |
| 原600秒范围未用余额 | 527.777146949，现关闭 |
| 总/solver overrun | 0 /0 |
| 新development / 旧检查复跑 | 0 /0 |

started计数：model build1、new complete Pi batch2、solver1、fixed metric1、paid first-jet binding2、nonlinear prediction1、actual pair0、actual grid values0。

源输入读取25.994011086秒；runtime imports1.238413883000021秒；model事件.09675649900003691秒；prediction事件28.27911009500002秒，其中metric27.401486371999965和curvature.8374428159999638秒是嵌套阶段，不重复累加。final process_seconds=72.222989273与科学账计时起点不同，也不另加。

COMPLETE之前科学stdout37992248B，peak RSS858548KiB。大矩阵/候选等只在原stdout，未入Git、artifact、Release或cache。没有用剩余527.777秒重开本会话。

## 7. 原11记录可追溯身份

下表bytes/hash均按原单行JSON加LF计算。

| tag（省略TRUE58_FREE_R1_R2_前缀） | bytes | SHA256 |
|---|---:|---|
| PUBLIC_PULL | 1485 | 127c7e33f9cbe310bf2d7bb9a9938a6d07faf810d4f7bb978aa9cd88e4e78d54 |
| PRIVATE_PULL | 584 | 3921605b66aaec5ad308b65d17430aecf477344a08acbe98d4ce7d046de31539 |
| REQUEST | 4514 | 40f00ceaca072ed1970a24fb598f729b5e88a1ae52d410cc38064e700d6b400d |
| INPUT | 232821 | 71aea06b3c9fa22e8a11b57edf5db717a731467ef706287d4b13a3bb4b6fe42f |
| MODEL | 25755139 | 89cc1b6ed0eedaaf18d454206f98831fb3decb8d401212493420bf80deb9ad31 |
| NONLINEAR_RESULT | 93220 | ac5848f5da3f72a3769717159c14e1a81bacd9ca20d1c7db9d50f1b8f91fd967 |
| SOLVE_TRACE | 11468459 | 578eb70cacea580eb2e069cbb44d0b49e4473c8cac0a253733f364feb5f090a5 |
| RING_SOLUTION | 148788 | 752025d1ef9dd9adb557aa7bf0f1c3899fb8a4cd417d00233289c0ff066ab3ae |
| PREDICTION | 289107 | 8832199e9b938983ef35448963a0163e4c24d577d40e57e51bc280edf889f9e3 |
| COMPLETE | 344760 | 396b50f3bfda35ec5131a3fdff61592a4c1dd27d2f69625da2e377965042f381 |
| FINAL_CLOCK | 7596 | 78152b9c0ea685146a3c34c1792660d42ea9f50b99b0dfb24f3d50feffcfa423 |

这些hash定位原记录，不替代其内容；新消费者须读取实际保存的字段，未保存字段仍需新付科学费用。

## 8. 两job的真实pull及后继问题

研究job的public实际pull为14:18:32.929224→14:18:33.406805，已读7ac3c637ec9fb7d151e7b0f7f2ee314dd137533c；private为14:18:36.099884→14:18:36.538012，已读2ec2f53e843d76f5b6227736b59a1b94195bac01。

report的public实际pull为14:20:08.240625→14:20:10.769425，已读4ef462296a239c5abf90ea3239f210cfc23be002；private为14:20:13.442969→14:20:14.331043，已读b589b1e9590411cc499b175994efe2a8b94294b3。

两次public根/题README及两次private根README均未变，private题README不存在，QUEUE本会话唯一进行中。这里只发表时间、提交和布尔状态，不发表私有正文。本地每小时真实pull义务另按HANDOFF执行。

新的具体问题是：能否保持已获环的完整二jets，用原前六径向样条的102个真实控制修复全body。R514已给该102纤维在s>.765零二jets的局域性；因此其固定后缀若在新必要输入中已违反门，整个该纤维就不能修复该后缀，必须立即换几何问题而非盲跑solver。若后缀通过，真正局部模型仍须保原盒、全body值与原14门。新值/frame/Pi/J按新范围支付，不能把此次未保存的预测大数组当作免费输入。

该后继并不重解已成功的自由36环问题。主README要求的同g等距精化、全时C²嵌入、宏观握持位移和连续全域reach均仍未完成，继续[open](../open.md)。
