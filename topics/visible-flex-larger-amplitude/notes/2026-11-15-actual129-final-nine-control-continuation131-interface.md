# Request131：actual129 第8批真实末九参数继续原八批

作者：ChatGPT /root（GPT-6 Astra Pro，AI-assisted）。日期：2026-11-15。

**类型：已明确来源的参数和执行接口，没有未来131结果。** 依据[R291实际129](../results/R291-actual129-eight-nine-control-batches.md)的原输出。所有科学运算继续仅在本公开仓库 Actions；本地只做原JSON字段选择、文本、字节/SHA和Git。

## 1. 真实末点与来源

原run `43701523658`，source `aba485afe160b63717b52f57d7f5c57a0a303173`；compute `132773497339`、report `132774328966`。原八批都完成，各批八方向均被原完整三残差 Armijo 接受；原新求的第一批初值为 `11.126800189953256`，第八批末值 `6.426170559507028`。前者与实际127最后保存的 `11.126800189953372` 最后几位不同，不能把旧值当本次fresh评价。

原停止为 `explicit_independent_batch_count_completed`，链 `174.200186809` 秒、exit0、resource partial=false。所有原unit、完整112、非零native和success标志仍false；原最后unit向量为：

```json
[-3.5850158845837177,-0.0014920654262581224,-6.102912416198981e-6]
```

本次只取实际第8批 `final.parameters`，顺序保持 `[p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3]`：

```json
[0.3069245569754433,0.20997429334070009,0.3763614846399783,-0.07501018427785207,-0.016829208312822436,0.9027966332362258,1.0753767742983957,0.6637557879927983,0.6316543431777241]
```

| 原件 | 字节数 | SHA256 |
|---|---:|---|
| 第8批status | 1683889 | f6a2076aee4227fe371c334abc341f8e326873fcfb479d1aa8657efb97939316 |
| 第8批primary | 62547 | c07e387c0cc5a6bb2ad84bd9b326f10a9bd4437d09d859b8bb271c350f985f9a |
| 第8批完整scalar view | 121112 | 234a134d7fcb9ea79dd158152769af86f291f427e454feb0c9ad1bc7c09526d5 |
| 原chain summary，无LF | 20087 | d2a6453113ce91436c9266da8f4e7bdd5a51eb83aa1651229c0f6debaecd9b6e |
| 原第8批compact restart recipe | 1839 | 1be8d732f119ef79a952e9d57d32228cd8560b4bcab6dfcece5e1ffcb6f1f609 |

原八primary、64完整方向组、八完整scalar view与各自stdout的身份已经按原数字文字重建核同，没有moved或omission。大status和内层raw仍已按原编排清理；其SHA只是来源，不能称本请求重新读了已删除的现场。

九参数是新搜索初猜，不是接受的非零完整场。第8批末半径 `0.003125` 不复用；原J、状态、merit、FD或域证书也不复用。完整九族和当前所有shape保留，不改变它的函数、有限求和顺序或控制支撑。

## 2. 本次文件和不变的科学来源

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| actual129-final-batch-nine-control-parameter-recipe.json | 2286 | 28acc474c6b5ccd6abaf6d6ebb16e9676e0e20820ef364ee53e6c894866065d4 |
| public-nine-control-batch-request.json | 41663 | 98d97b5aa564f3d96790c675a4ff298f174782ab1dcb82f07c360a165bfb9508 |
| visible-larger-public-nine-control-batches.yml | 18132 | 86551b1352a53b0360fbb5122482dadcd25d502d2f8c8e4562c6d087a65eb974 |

新pretty参数文件与原compact restart recipe的字节和SHA不同；只声称其来源和九个值对应。request只更换131身份、真实129来源和这些参数，完整输入、source table、runtime、direction model、batch contract及所有科学条件逐值保持。

| 冻结组件 | SHA256 |
|---|---|
| 原九family | 086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629 |
| 原九搜索producer | 824c0967e5de5cc9079a80018b66b1232c78ce406a6de4e0d7ab4cdee876bdaf |
| 原八批wrapper | b15a6571a1ebc5dc72f1037212fd86a10d7a5848957c2faca4ae9e7fd69f21bb |
| 原完整分段reader | f57a7dfae95f3e629aa412003e10ea4e32a9821b754c3d575318f97b09b7317d |

原84项source加2项workflow support及实际26项producer closure保持。四数学输入仍从公开历史 `8bd267107cc8710d371f3b62c02986655ac965b0` 恢复：accepted b4d2b98a、prepared0f94dd88、zero anchor e788a28d、T112-config01930f3b。完整SHA/路径原样保在request；原78源恢复、Python3.12.14、numpy2.3.5、scipy1.17.0、python-flint0.9.0和单线程设置保持。

## 3. 原完整过程、读回和停止

每批为独立child，初相对半径重置0.1，最多八方向、每方向20外回溯、完整两法向校正12×20内回溯。完整3×9响应、正则12×9 QR、七切向、原未加权三残差和0.2 Armijo保持。unit和内目标1e−8不改；内目标未达仍不是新增外接受门，过去和未来的原接受都按原条件解释。

新批次必须实际形成当前评价/J和全部初末九列三步长FD、新Arb完整标量域、原453完整圆参考、全节点/中点/两RMS/4096rho/BC及完整112一阶右残差。原圆参考中六shape固定、三active的两有限路径差异，以及zero-eta的25数组反事实比较，都保原职责；不把它们升级为新机器门或接受非零场证据。

每批原status经原完整reader消费后才生成下一短recipe。原停止条件均保持：child/reader或传输失败、原非预算停止、零接受、中断、批间3600秒或八批数上限。3600秒只在完整批间检查，科学step75分钟/compute90分钟/report10分钟原样。八个独立重置过程不冒一个保留radius的连续64方向求解。

compute保全部primary框、原reader stdout框和完整方向段。跨job仅传原compact chain index，框名为 `BEGIN_VISIBLE131_CHAIN_SUMMARY` 和 `END_VISIBLE131_CHAIN_SUMMARY`；其SHA不含分隔LF，各原stdout自己的末LF另按原协议绑定。失去原段时必须显式报告，不凭hash填回未知科学内容。

所有raw只在本请求RUNNER_TEMP消费，随后清理自己拥有的目录；不回写Git、Release或新artifact。wrapper与reader源码不变，workflow只改字面输入、来源核对及事件/框名，没有新的执行分支或额外试验门。

原规则runner代码保持，按2700秒真实pull/rebase核两README；当前已读根blob74c08a36f6c997d0bc1e64a7956b42276f5fa5d7、课题bff8aea253a9e6a7a4fac28d810ac454c5499fec。有变仍读diff按新规，科学checkout绑定实际GITHUB_SHA。

## 4. 独立非零场与最终责任

本请求由原batch-request路径的main push触发，没有未来run或结果预填。实际结束后完整读回并写正式结论，再继续未完成问题。

128已经独立以真实127末参数和明确正lambda=.001执行完整H(s)路径；它的run是43702058809、source3ee6c53840032444b2b88bb4ff98d69f038239d3。131继续标量设计搜索，不加载128的worker或场，不将另一个参数族的native状态混入当前模型。

低三条件仍不替代高109/完整112、真正当前H native J/FD/fullDN/finalaudit。只有真实接受的完整场才进入全九冻结450精化及同场闭面消费者；全t嵌入、held、reach、完整D、相对度量算子和README全部标准仍须实际完成。
