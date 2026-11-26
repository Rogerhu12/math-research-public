# 原606积分范数实际26–27：完整首方向与同父后继

本条登记 [Actions 45820592817/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45820592817) 的实际26、27；完整紧凑返回在[第6卷](2026-11-26-public-actions-45820592817-1-part-006.md)。root亲读两条完整公开结果，没有本地运行F、J、积分、因子或新的科学计算。

**原完整integral实现已实际构造带矩阵、平衡和Cholesky因子，并完成一个被真有限几何接受的完整方向。** 原因子路径没有失败。QP仍未驻，最终metric误差仍大；这不是终点或完成证书，也没有把该结果归给尚未执行的新QR实现。

## 1. 源码、完整输入及真正身份

原科学源码未改：launcher a94263f037dfa8535b11cf44fa93b6a4cd6df7dee1a6be35f2ea14f5abaa2690，driver 606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9。实际source checkout为 **4106d8fd47c60374493d0c9d498c4091fd467856**，控制器26状态completed，退出0。

参数与范数定义见[完整首方向说明](2026-11-26-direct-axisymmetric-integral-norm-full-direction.md)；采用same fixed g、原完整q.initial、明确的新integral坐标及mu=0.01，保全部四个已返回地点来源。没有用旧jet-sum checkpoint绕过原范数守卫，也没有把相同的阻尼数字冒作两范数下等价的正则化。

| 身份 | 实际完整SHA256 |
|---|---|
| reference | 0f0424cc7403d0ffbca22490fc9d0bc154c52c356278a800553528e77fc386c1 |
| scalar目标 | 6ffc1f7fc1e6196318dc27da22b6c9ffda3ee64e81223a4c815f6348cf5baebb |
| 原direct model | 9d4ccb16efe9a0c0f5b077c0e8919e76d1d04b06e669588b32e2de78c92f0258 |
| carrier | b0257d9e03da36a422eab4e424942d38ccf817ac40ceb3b42be4378b1260966f |
| 新integral norm | c06a7abc532243cc3faee0b123a4d5c7f6c109527e426dc764b1205af528c8d9 |
| 实际band | ba5017bbbf9e8b63a63541ca39ef6636e6f691064f5aff1b81d5e9519e00b10e |
| 实际factor | 9c04393e73929625c76514bb3b78572e949b78dddcfcfa504163484e23e22d2a |
| equilibration | 044bdec037398e505ae5a4d9626ee24ee06b8f3c8141e44405548684ddb57be3 |

norm schema为complete-SO3-radial-H2-positive-whitening-v1，kind=integral，完整Gauss order=6、bandwidth=5。实际维数M160、J923、N2048，全部1333370自由量、45324288完整metric行，未删core、H、旋转或mean/cross责任。

| runner完整输出 | 字节 | SHA256 |
|---|---:|---|
| axisymmetric-so3-integral-norm-first/report.json | 10073112 | cfe87f69a731e65abfddedfc6635ffb93af90b4fff44bee162d1f9774cd6621a |
| initial-new-field.npz | 10720288 | 81b3dd28c7c0398c1bf87a8d60e92b45d1c879e778bca96d617e4260a175bb83 |
| final.npz | 10720288 | 655d29f2734b00bce0097cbb16f64d3b0a33a1774ba463f285917679686427c0 |
| axisymmetric-so3-integral-norm-first-command.json | 10691 | ac33906ed3c8af7e9b35e78ba8b1cb8675125011c43107cf9da2f7a45a6d594c |
| 第27步完整pure readout | 40440 | 1ca66f2e65a5f0512d50aee0e83e5fab7f3c77fde7ca1e0ef93dba929b5741f0 |

这些大报告、字段文件和工作行都只在runner；本条只保必要标量和完整来源。新initial文件有自己的范数/身份记录，不能仅由其文件SHA不同推断原q.initial物理自由值发生改变，也不由此冒称两个完整文件逐字相同。

## 2. 真正首末读数

| 量 | 初始 | 最终 |
|---|---:|---:|
| max relative Gram | 0.5170375580125983 | 0.5063653325054447 |
| 完整同Phi | 213.89131075534186 | 197.58457993534574 |
| 全有限物理最大g | -0.024430047350427198 | -0.0246162690033348 |
| curvature永久位置 | 1709 | 1757 |
| radius永久位置 | 1709 | 1715 |

原pure reader实际返回同Phi改变 **-16.30673081999612**。实际1个metric方向接受，0个restoration方向；最终两mu仍0.01。所有永久位置和全部曲率分支均重读，final_feasible=true。stop_reason是declared_metric_direction_budget，metric_certified、geometry_certified与accepted_isometry均为false。

最终实际K乘积为0.9167359977955157。五幅度家族的实际g为body -0.0246162690033348、plus -0.13778012759893254、minus -3.3090316747700292、cap -0.06755212470427197、height -1.040667674857096。

这些是有限工作screen的真返回，不是全连续reach或完成几何认证。积分范数的解析稳定性也只在其明确条件下给估计，不能把实际普通因子hash当成精确等距白化或误差包围。

## 3. 完整QP与五个实际ray

原QP仍是 **iteration_limit**，真实advances=64，Pg=992.9490656427213，对比tolerance=0.0023323146347878506。末活动面有5行；实际原几何行36、幅度行6，共42条完整C，工作行448012320字节。末线性违约为7.030373462210693e-20。不能把工作线性近可行或一个ray接受称作驻点。

QP耗时1522.7005101089999秒，QP区间J=67、Jtranspose=68。实际回溯仅5次：

| alpha | 同Phi下降 | 全几何已读 | 实际positive g | 接受 |
|---:|---|---|---:|---|
| 1.0 | false | false | null | false |
| 0.5 | false | false | null | false |
| 0.25 | true | true | 1.5516891584872368 | false |
| 0.125 | true | true | 0.2485949195432704 | false |
| 0.0625 | true | true | 0.0 | true |

各trial的actual_read_error均为null。前两次在Phi门被拒绝，没有实际全几何值；不能填造其K或将null补零。中间两次虽下降仍被实际物理g拒绝；当前紧凑返回没有分别列其全部家族或最坏地址，本条不猜某一个家族。最后positive g为0只是非负违反量；完整末最大g确为前节所列负数。

这条数据没有证明单换范数已经解决所有曲率问题，也不支持把旧jet-sum/R696不同场、不同维数和不同初始预算作受控因果比较。它确实证明当前原完整integral入口可执行并产生了上述下降。

## 4. 实际成本、pure归因和缺项

原完整setup为142.48204393099877秒，driver总计1829.4684319909993秒；控制器子进程为1832.3353395530012秒，peak RSS为2173196 KiB。完整原科学区间residual=8、J=68、Jtranspose=69、point_covectors=41。

第27步原完整6d54cbba7ff998bc98b0f39c6a26ae33c16957fb0b9dc0fffced1037212455eb纯reader在source checkout **44ec743e9548f6723f6ff66d617670d57a7e30ae** 运行，completed/0，6.025577441996575秒；自身J/Jtranspose均0。它没有再跑方向。

26的summary_errors与missing_outputs均为空。27有92个摘要缺项：60个来自不存在的trial5–14，32个来自没有发生的restoration0–3。实际只有5个ray和0次restoration，没有省略实际存在的相应科学结果；缺项保持原错误，未补为0或成功。27的完整输出存在，missing_outputs为空。

## 5. 同一真实末场的后继责任

已经排过的固定Q残差延拓真实消费本次完整报告作为第五个地点输入；其后来实际28初场根失败是独立事件，不把本次655d场改写成零闭合场。

当前可继续的integral父是这个 **真实655d/cfe87**，必须保持同一606完整source、c06a范数、同一完整g/model以及全部原自由量，以原restart检查实际读取两件文件；不能回退到旧jet-sum父或冒继旧阻尼单位。后继还保留已返28完整报告的地点责任，全部位置在自己的新候选上重读。

README的完整metric、闭面嵌入、全t的握持/非全等/reach和固定g精化尚未达到。此处直接接续实际方向，同时推进新增形状的独立完整端点构造，不在首轮预算结果处结束。

## 6. 实际后继参数与全参数归档

2026-11-26 17:23:05 UTC：原a942/606/6d54来源不改，真实655d/cfe87按原restart完整守卫接1×64/rest4×64，两mu按真实末值.01。完整参数 computations/resume-20261126-direct-integral-norm-655d-next64-ready.json，23252B、SHA256 0da880099a4397e79cfa7146f6373750a5036f8aff1d5f8f0c6ab08d1e2da435；六份manifest保原四份以及本次完整cfe87和实际28的a244失败报告，只消费同材料位置、不继别场证书。没有执行本地科学，尚无该后继结果。

活动队列原9条21–29均已真实返回，其中28科学失败、29纯读取失败，保持原状态。完整92518B原队列逐字归档到computations/resume-20261126-followups-03b-completed-archive-003.json，SHA256 cabb82d4917838c6aecfc47dbddb56331f383332e3c1e92da61afdafb6b1aabf，原archive002指针及其全历史链同存。新活动仅两个完整后继对象，23955B；没有缩写argv、截断schema或删除待执行步骤。原29纯读取失败另按真实报告/traceback修复，未把它混作26科学失败。
