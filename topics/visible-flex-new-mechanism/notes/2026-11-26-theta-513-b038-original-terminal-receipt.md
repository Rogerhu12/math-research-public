# 2026-11-26：513 径向续接 B038 原始终态收据

## 身份、成本和真实规则读取

公开 run **45790610433**，job **139808369258**，lane rounded-core-B038，source **48e3048105f2e4e83c537beddb4bdefb99ae6e21**。自然 GitHub success、child returncode=0；child从09:18:02.405145至09:27:31.526800 UTC。本段实际科学 **568.432517953秒**；此前链 **2099.765385366秒**，累计 **2668.197903319秒**。它是局部定位容量终态，没有完成课题。

请求86776 bytes，SHA256 **ceac3f5de0069939e687900d5142fa8a0a6539113a26d8b40799c884e7a3e844**。wrapper **0093d8ce3b80600a6b4eb0d921208423ca390cbc957497b026d8ef230355aaa1**，原driver **6094c15ff2696d6b64e9eac09ce60b54a59a64c545cb88fb7734df8bb185f757**，角oracle **46eea6c6da4a94c82106e8a57ff98e70bf8f85bd2d0ef35c26cb649a0ee2f0a7**，完整传递依赖见已绑定请求。

job实际pull公开main，source前后不变；private实际pull到 **2e29dddc702b392dd01307cfc6745c87ad55fff3**。根/题/私根README blob分别282e86b03385d3b6245ce7100ae2e2af7b103c2d、d0432faff569c8e9af7ed4809847e12880976c11、5ba164843b1f5802184178a82d786264404873a3，全部匹配且差异空，QUEUE确认本会话进行中。Python3.12.14/numpy2.3.5/scipy1.17.0，科学前凭据已移除。只在自然终态后读取完整原stdout。

## 原q与全部pending真实采用

起始取前次真实保留81q，保留actual250径向/213峰及pending303径向/268总峰，实际采用全部303/268，FFT/均匀角1536不变，trust=.2669677734375。不取前次被几何门拒绝的eta约.5993 trial。径向cap257→513；同一算子原parity/方向核已付，本次新检查数 **0**，没有复跑旧joint/接口核。

新起始细格607×3072，eta真峰 **.6505886794002231**、细格 **.6505883052193007**、几何V=0。原保留q没有变，新增pending径向重建及全细扫均在本段计费。

| outer | 实际 radial/峰 | callbacks / 接受 | 已接受真峰eta | 下一 radial/峰 |
|---|---:|---:|---:|---:|
| 0 | 303 / 268 | 3 / 1 | .5993461338962852 | 387 / 357 |
| 1 | 387 / 357 | 1 / 1 | .5615689639460253 | 460 / 498 |
| 2 | 460 / 498 | 1 / 1 | .5194593774637183 | 464 / 502 |
| 3 | 464 / 502 | 1 / 0 | .5194593774637183 | 470 / 508 |

共4个完成outer、5个开始outer、6次完整callback细扫、3次metric接受、0次restoration接受；4次真实未覆盖几何峰交换。自然SLSQP OptimizeResult次数为0。

## 被拒trial与518候选容量必须分开

最后实际backend trial来自outer3：backend epigraph=.49249364505591753，实际约束组metric_minus=.49235199337029506、metric_plus=.49393586249442323。全细网给eta=.49636784079583696，但 raw几何V=**.016097949768784092**（负曲率分支，s=.38437499999999997、theta=pi/2，绝对曲率16.73415595798393），所以未接受。实际工作曲率正分支缺口.000602245909446796；不能把这个trial当终态q。

之后outer4成功构造 **470径向×1536+508峰**及其细格。对保留q的初始localizer枚举出 **518 candidates**，超过 **512** 上限，返回 candidate_capacity_not_angular_coverage、unresolved=518、目标求值0。故该轮没有构造新的SLSQP行或开始backend；终止为 unresolved_initial_angular_localization_checkpoint。最终重扫仍为同样518 candidates、0局部求值、518未解决。

这不是优化器backend错误、2400秒时钟、513径向cap或1024峰库cap。本段实际最后一次SLSQP使用的是outer3的464径向/502峰；FINAL的470/508是已经构造的actual oracle网格，但尚未在其上运行优化。两种身份不得合并。

## 终态有限扫描与接受边界

保留q来自outer2的真实接受：该时500候选全部定位，eta **.5194593774637183**、几何V=0。它保持到FINAL。但扩大到最终941×3072细格后，localizer无法解决518候选，所以FINAL准确分类为 **unqualified_finite_scan_or_restoration_input**。旧已接受记录仍成立于其原扫描范围，不能代替新范围未完成的定位。

FINAL raw细网eta **.5194591704351894**、几何V=0；这里 accepted_eta_max 字段同值只是未定位时的细网回退值，不是新的真实角完整上界。eta细格点s=.212786865234375、theta=.366110081375373。

| 最终941×3072细网量 | 值 |
|---|---:|
| ball半径最大 | 1.0099021213909583 |
| abs(y)最大 | .3925880515017075 |
| 最大绝对曲率 | 16.46154827985457 |
| mean E 最小 / 最大 | .3202459811689092 / 8.99745065895974 |
| normalized det 最小 | .21559353826560615 |
| z最小 | .02 |

曲率峰s=.6878906249999999、theta=pi/2。raw曲率正分支余量 **.0004547884472306807**，仍欠.001工作余量中的 **.0005452115527693193**。raw球/条带余量分别.004141707816520235、.0010788763559544945。以上只说明有限点；最终角定位未完成。

FINAL actual470径向/508峰、actual trust **.9010162353515625**；最终proposal也列470/508及同值next trust，未给额外待加入坐标。不能据相同数目把最后网格说成已经过backend。后继应取完整保留q及这些实际坐标，首先完成518候选观察，不取被拒的.49637 trial。

## 运算与原收据摘要

14个value keys、6次完整Jacobian、36个16方向块，重构值差最大0。9个完成localization返回、2490个已处理bracket、19185次对应目标求值；容量拒绝的518候选没有被计成完成定位。底层58个FFT状态、522个primitive Fourier字段、134158个非均匀求和点、16090个均匀准确gather点；全部工作记入568.432517953秒。

已观察的嵌套FFT差最大：metric e/f 1.9984014443252818e-15，relative Ebar 9.31963231779471e-16，tau*curvature 1.0837272412800302e-13。它们是离散比较，不是连续尾界。

完整job stdout UTF8 **863530 bytes**、SHA256 **5a2224e4dcd01c4bd9c4ca976ddaf74e04b298e160f0aa7397f32ebbba79f1ca**。FINAL JSON **125971 bytes**、SHA256 **488a6a2c92216e5cbc0e2dfb6aa78ba192b9c45340c0cac8e2aded09e646e89b**，与producer identity完全一致。原日志仅scratch和原Actions，不进Git/blob/artifact。

下一实现的实证缺口是“518>512则整批不做”，应在有限候选完整保留的前提下分批处理并收费。不能省略峰、放松几何/接受门或将本次有限raw scan升级。metric仍随设计变化；固定g精化、连续度量/曲率/全pair reach、非圆闭面和README全门继续欠账。
