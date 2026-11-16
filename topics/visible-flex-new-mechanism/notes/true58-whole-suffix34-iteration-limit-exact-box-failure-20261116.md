# 真正58全后缀34控制：迭代上限返回、原精确盒失败与完整成本闭账

日期：2026-11-16。**这一范围已结束；没有接受59，当前仍是原完整两网接受点58。** 本文只读取原已完成公开Actions的实际输出，不执行新的科学、符号、优化或开发任务。失败返回不作全局几何不可行证书，也不以余额重启旧优化器。

## 1. 原问题及执行身份

原[设计](true58-R1-R2-whole-suffix-design-20261116.md)、[合同](true58-R1-R2-whole-suffix-model-contract-20261116.md)保持同一g/b0、真正58起点、原R0平面、准确172盒与34个R1/R2控制，加K/h共36变量；全部21径向行乘384/768完整角网。原145152非线性行加450线性行共145602。原13个可变径向行139…151，8个固定支持外行152…159；固定行仍按本次K重组谱门和K导数。

| 项 | 原值 |
|---|---|
| run | [43900273845](https://github.com/Rogerhu12/math-research-public/actions/runs/43900273845) |
| research job | 133414653234；15:47:48→15:53:06 UTC；success |
| completed-log report job | 133418227084；success |
| source commit | ffae5cb5f64004a4239f224e070aed320f7774fb |
| workflow | .github/workflows/visible-true58-whole-suffix.yml |
| request | computations/request-true58-whole-suffix.json |
| request bytes / SHA256 | 77451 / e460bef2af9ca39e855d34b874c1062fbd42ffffbd3110e951206a0190a33b68 |
| sources | 359，原348源字节hash未变 |
| model binding | 507caeb693a5aaaf5e80e522afdf42af7680624508d49b8ab7e552f921f69a96 |

原范围600科学秒、180solver秒、120迭代、240个不同backend36字节输入；同q不同K/h也计backend点。独立物理q几何、实际J和K无关导数另计。预算包含导入、四原日志、输入组装、临时IO、所有失败、序列化与输出。只允许一个solver session、一个真正58初点；原返回合格才至多一次完整body预测和一个原actualpair。

固定g为fd5bc5fe2c114bdbe82c266a5e816ba22ed58f1f486f5bc3241ddaac95de88b6；b0为d61fb298989834c9eb2b4fe3bbff1fb5983d1bb3b3980cb6441f14e6c0299bb5。原actual14、全部精确盒/容差/面积floor、连续metric/reach/嵌入和宏观幅度门从未修改。

## 2. 唯一原返回：未合格，不进入预测或actual

原SLSQP返回：

- status **9**，success **false**，message **Iteration limit reached**；
- nit **120**，nfev **142**，njev **120**；
- 原返回K **18.45692174062725**，原返回h **63.87343696103953**；
- qualified candidate **0**，完整body prediction **0**，actual pair/value **0/0**，new acceptance **0**。

raw36、一次舍入后的完整168及物理172坐标正文仍在可取得的BODY_SOLUTION中。其原身份分别为：

| 对象 | SHA256 |
|---|---|
| raw backend36 | 9e5d24bf3ed1b488101dbc00331b7fac6b06c738cdc43d9d06258accd547c1e2 |
| rounded independent168 | 9fb143ff99b0bbbb9d20ad8724d2f9132fbb03c672550a66dd60d5cd4daab63d |
| physical172 | 646e13185621ce59d52a862995e9651fc2d7aa52e9de6d3cdc106711459305f6 |

原返回舍入前、舍入后的准确盒均失败，物理索引 **58、61** 违反原门。返回对应坐标字面值为−8.000000000078638和−8.000000000535866。没有把它们夹回边界、以容差更换准确门、继续优化或晋升callback点。

K/h区间门和原充分hmax门为真；准确norm epigraph门为假，原收据的h−norm是 **−261270233/72057594037927936**。这里将准确门与后端浮点线性可行性分开记录。K下界所用binary64为16.393442622950822，准确表示2307171940251279/140737488355328；原hmax为18014398507545773/281474976710656。它们没有被返回失败改写。

**未取得与此原返回点配对的最终完整后缀η/κ总结正文。** 不把初始值、别的callback值、原环值或receipt当作这个点的η/κ。单凭SLSQP失败和原准确盒/范数失败，已经足以关闭本次候选；不需要补算一个拒绝点。

## 3. 实际可读记录和大输出的可用性缺口

生产者最终收据记录科学stdout在COMPLETE前已达 **250647593 bytes**。然而当前可取得的research job日志只有 **367277 bytes**，SHA256为 **64c07ee218476e577166aeca981e8d87ab1d4bd511af092ebef2c65394d4fd7a**。它以15:53:04.503附近的BODY_SOLUTION开头，共20行，只有下列3个带前缀JSON记录。

| 当前确实取得的记录 | JSON+LF bytes | SHA256 |
|---|---:|---|
| BODY_SOLUTION #1 | 98291 | e999c32bb49aad559aa6823c77cf1f728e58504d286f000e6aa33339816331ed |
| COMPLETE #1 | 260475 | 7e6445fc7f3dc9e8021a7f57cd4a14dc3f1b127675960b0620500eb93596d264 |
| FINAL_CLOCK #1 | 6027 | 6183fa46634b4f6bfd5059e2a269861a8542c726d54d359724ae1b7fbfbc0b80 |

独立再读job log得到相同bytes/hash。再通过CLI只读原完整run日志ZIP，ZIP为347260 bytes、SHA256 **1d3b117bf8b9c52f1a0b4741cfdbee26856c8efe31254f3e87faa6d003d711a2**；其中1_research.txt仍367277 bytes，对应research科学step文件364978 bytes，也没有此前的大记录正文。这里不推测缺失的服务端原因；没有为恢复输出而重跑科学工作、上传artifact/cache或把大payload存仓库。

后续记录引用了以下当前范围的producer收据，但**收据存在不等于正文已取得**：

| 只见producer收据、正文未取得 | receipt JSON+LF bytes | receipt SHA256 |
|---|---:|---|
| MODEL | 262726 | 923757ddc2af523c8405c029045b91660a3e51f948aef86452652d40d7384759 |
| NONLINEAR_RESULT | 1173031 | 850ea47708515df23e06e4c24e004f4949a9252e53a224d81c8851a4bcb18e05 |
| SOLVE_TRACE | 248887475 | 8355a231108352b0d638aa15440fc64f9f9d9221d49bc00672cedd33cfbf3bbc |

此前PUBLIC_PULL、PRIVATE_PULL、REQUEST、INPUT正文也未在所获尾日志中出现。尤其**当前模型数组、初末J、完整偏导/几何数组、原OptimizeResult的全部字段、multipliers及全部evaluation/iteration trace，不得被后继任务当成已保存的免费输入**。COMPLETE.model_summary的initial_summaries/last_summaries是solve前捕获的null，不能据此恢复模型终态。

原completed-log report日志412358 bytes / SHA256 **a205b9e063fc55c477fbbc0530e6e200bb5cef22652b569c54c5a87cab7d0bb9**，实际解析3条、0 parse error、0 projection。它的semantic_read_is_incomplete:false只说明**已取得尾日志的选择/解析**完整，不能说明生产者整条输出已完整取得；原literal_receipt_comparisons把缺失当前记录也容许作“可能祖先”收据，本文据真实标签纠正这一解释。下一个独立范围的报告器将明确列出缺失的当前记录，不能沿用该误读。

现有三条原记录足以支持第2节的拒绝、原返回完整向量以及第4节最终账。除此以外的缺失不能由hash反推出正文。

## 4. 最终时钟和全部新科学计数

FINAL_CLOCK是本范围的权威闭账：

| 项 | 原实际值 |
|---|---:|
| 本范围科学秒 | **184.71003744799998** |
| 进入祖先科学秒 | 3047.102915103 |
| 祖先加本范围科学秒 | **3231.8129525510003** |
| 原ordinary完整值累计 | **147** |
| 本范围原ordinary/actual值 | 0 / 0 |
| 新两网后缀物理q点值 | **142** |
| 不同backend36点 | **142** |
| 新物理点失败 | 0 |
| 完整J评估 / 失败 / hit | 120 / 0 / 1 |
| K无关物理导数block / 失败 / hit | 1920 / 0 / 0 |
| input preparation / model build / solver session | 1 / 1 / 1 |
| paid metric binding / paid first-jet binding | 0 / 0 |
| 完整body预测 / actualpair / new acceptance | 0 / 0 / 0 |
| 关闭余额秒 | 415.289962552 |
| observed overrun秒 | 0 |
| scope_exhausted | false |

“new_necessary_model_values=0”是旧ordinary计数器的原字段，**不表示没有新科学值**。本次142个新两网后缀几何点、120个J和1920个block在各自真实计数中完整保留，不混进原ordinary值定义，也不把它们写成零费用。

原callback计数：objective142、objective J120、constraint value143、constraint J120、initial value1、initial J1、iteration119、requested analytic J120、returned-vector evaluation0。所有120个J是初始缩放或后端实际请求；没有额外为了“验算”而运行新点。

包含在同一科学钟中的阶段秒：

| 阶段 | 原秒 |
|---|---:|
| scientific imports | 1.2328702009999972 |
| source input subphase，四原日志各一次 | 11.206693945000012 |
| model build | 0.13322999499999355 |
| ledger solver event | 139.69209619400002 |
| module-local solver elapsed | 139.60137213500002 |
| backend elapsed | 138.843244143 |
| raw solver emit | 0.20169655800000896 |
| temporary file IO | 7.075092483000077 |
| whole process elapsed | 184.71011732699998 |

model build原相对钟26.975524581→27.108755913；solver ledger27.130670627→166.822768649。上表互相嵌套，**不再次相加到最终钟**。求解器未触及180秒，先到120迭代上限。临时存储2182次写、**12063298236 bytes**、0次读；限同一进程，已计IO，没有未来免费复用承诺。峰值RSS **2317220 KiB**。

原内部分量计数/秒同样只作分解，不重加：

| 分量 | count | 秒 |
|---|---:|---:|
| PSD/J组装 | 1920 | 2.1622647990005817 |
| Π | 852 | .29402669599984677 |
| principal | 284 | .8125882399999824 |
| angle kernels | 1920 | 5.598543277000701 |
| curvature value | 284 | .2647638560000871 |
| position jets | 284 | .0806963260003215 |
| paid metric rows | 2 | .0002806680000162487 |
| scalar increment | 284 | .5707355670000709 |
| frame | 284 | .3587836590000393 |
| fixed new I/II | 2 | .0008397310000134439 |
| virtual jets | 1920 | 5.314149203000127 |

completed-log只读报告另用 **2.0928324900000064秒**，独立CLI读取已有run ZIP另用 **21.06371758399473秒**，二者均非新增几何/优化，不重加到上述科研scope；仍明确记录观察成本。

## 5. 真实58初始增量模型的已存在摘要

BODY_SOLUTION保有唯一初始value摘要。该模型使用已声明的paid scalar increment组装顺序，**不是原canonical几何的bitwise复现承诺**。本节仅抄原摘要，不新增计算。

| 原初始摘要 | coarse384 | fine768 |
|---|---:|---:|
| 全后缀门 | true | true |
| ηmax | .265998600016377 | .2659994610038927 |
| η峰径向/位置 | 144 / .8025 | 144 / .8025 |
| η峰角 | π/2，j96 | 3π/2，j576 |
| κabs max | 57.998792638483124 | 57.9997782607126 |
| κ峰径向/位置 | 141 / .78 | 141 / .78 |
| κ峰角 | π/2，j96 | 4.818744981678094，j589 |
| min normal area | .9605244288093617 | .9605244286809872 |
| minus PSD det | .20849802242908586 | .20815357980369506 |
| minus PSD trace | .934816103748031 | .9348161980746976 |
| plus PSD det | .000007580321956075768 | .0000013455321855423696 |
| plus PSD trace | .5714258237958818 | .5714256173520246 |

原metric预算.26600531463999305，初始scaled violation1.1102230246251565e−16。以上不作完整body的η下降，也不替代真正58原actual身份；真正58的原粗/细全bodyη仍.26600541430262403/.26600541463999305。

## 6. 规则读取回执及范围后继

发布前本地实际pull记录：

- 15:47:16.198708→15:47:35.118615 UTC，读e9326d071b578b09673e578393648a0960b75519；
- 15:49:15.738259→15:49:33.350546 UTC，读c3e91b762a6536a9820cf87e4dd1a9e898d88d62。

两次根/题README均空diff，NFF均立即实际rebase后续推。后续本地pull最新SHA见HANDOFF，不以API读代替actual pull。

本次research的PUBLIC_PULL/PRIVATE_PULL正文在第3节缺失范围内，因此**没有虚构其读过的SHA/时刻**。report实际public pull为15:53:30.842572→15:53:31.913622 UTC，读7af9e725e58983a740d3cb53c66b73166914e247，双README空diff；report实际private pull为15:53:34.717089→15:53:35.386209 UTC，读afa9c6cf31ba0b6f02955fdfd3158001d4b750ab，根不变、题README不存在、QUEUE会话唯一进行中。只发表私有核对元数据，不发表私有正文；CI pull不替代本地至少每小时pull。

**真正下一问题**释放原后缀另外17个R0方向，让原51个u/v系数共同变化；其51+K/h是另一个参数空间、另一个明示scope，唯一初点仍真正58。原失败36维scope不延长、不重启，不借失败返回补成新接受点。新模型的basis/几何/J只在确有旧字段时复用，缺失的whole34大输出不能免费恢复。后缀合格仍须原完整14实际门，连续metric/reach/嵌入、固定H和δhold主完成门全部继续。
