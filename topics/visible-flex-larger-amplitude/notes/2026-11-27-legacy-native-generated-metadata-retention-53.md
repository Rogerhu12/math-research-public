# 第 53 批：旧 native 身份副本与完整生成清单的可恢复退存

2026-11-27。本次只处理明确列出的 28 个旧文件：8 份完整身份文件的逐字副本、18 份完整 QR 输入绑定或输出数组清单，以及 actual39 的 2 份新系统生成元数据。毛退存为 **2,064,122 B**。所有原源码、请求、完整参数、原始数值数组、checkpoint、实际结果、失败说明和数学结论均保留。此文交付时仅保护了未引用 Git blobs，尚未改动 refs、队列或当前树；最终实施由 root 记录。

本批服务于当前实际返回和完整后处理包的容量需求，不产生新的数学值、接受步、导数误差界或完成结论。文件名中的 input-binding 不作为判断依据；选择来自下述真实 constructor、writer 和 reader 的完整源码。

## 1. 完整材料与固定恢复点

固定恢复提交：

**6fc35cce76db25916e359b8a0345620cb527857e**

该提交的课题树为 9c2d7b8295454aa325f14aaba6233dee8e916126，完整树元数据未截断。全部 28 个候选的 path、blob、size、mode 和 type 已从此树取得。root 实施时仍须与当下 fresh tree 逐项对应，只处理同一对象；有变化的条目保留并说明，不能借近似文件名扩大删除范围。

本批两个完整机器记录：

| 文件 | 字节 | SHA-256 | Git blob |
|---|---:|---|---|
| [完整源与参数登记](../computations/legacy-native-generated-metadata-retention-53-complete-source-parameters.json) | 94950 | e5ec76d2fa494b8bf59aac96b5cb46dfe883c8359e2aa82bf97cd0d4b4cece04 | 4e2f0f4e7b0c3aa5fa6a435319414f5088b6ba8c |
| [完整逐项 provenance 与删除表](../computations/legacy-native-generated-metadata-retention-53-provenance.json) | 94825 | ada078519ce0759aea56d21c413072c019f4bba76c8357bee7ecd85959640353 | 7c01d5c8af9da2f85e346f1f46412f737b05d62d |

provenance 使用紧凑 JSON 以保持单件小于 100,000 B，所有字段、记录和删除项完整保留。其 candidates 给出每件原对象、原 run、生成链、参数登记和固定恢复；delete_entries 是唯一拟实施删除表。源参数登记保留 24 份本次完整读取的源身份、原 6 组科学 workflow 命令、全部 11 个相关实际 run 的请求/资源/结果来源，并明确复用已刊完整台账。

这两份台账不是原文件的简化替代物。原完整文件在固定 Git 提交中逐字可恢复，完整源与参数仍在当前树及明确记录的历史版本中。

## 2. 两份完整身份文件仍在当前树

第一组共同 Git blob 是 1730e2713f0b8673a8144a9e747a498145a0c582，52,899 B，whole SHA-256：

**de9bbf01981f1605c0342817ea520005bf2d0a05f5a755986d50b718b16089a7**

保留 actual59 的完整文件：

notes/public-actions-43640772654-1-original576damped/native-original576-damped-chain-original-trial/restored-original-mathematical-identity-before-seed.json

它本身就是 actual61 完整原请求列出的输入。六份相同 blob 的旧路径副本进入本批；另外五份更早的相同身份文件也继续留树，没有顺手扩大删除。

第二组共同 Git blob 是 3138af87d499e8763258d40351c31578eae091e3，52,899 B，whole SHA-256：

**8a93c6845efe43cf570971569943eb56ddefca6cb1325596c33a00b3f6c24529**

保留 actual61 的完整文件：

notes/public-actions-43645948199-1-current576native/native-current576-damped/original-live-identity-before-selected-seed.json

actual73 和 actual95 各一份相同 blob 的副本进入本批。两个共同 blob 均已完整读取并计算 whole SHA，逐路径只核 Git 对象元数据，没有将两个不同 blob 当作一个文件。

这些身份文件完整保存 parameters、rawNode、graphs/gains/far 的 whole raw hash、四个原函数身份和全部 576 stage 的 profile breakpoints。原 hook 在 seed 安装前比较完整原对象并写入它们。当前 state/checkpoint 字不在这种身份文件中。**相同 before-seed 身份不表示相同当前点、相同种子或相同收敛状态**；各 run 的独立来源和真实结果仍分别保留。

原 current576 hook 明确读取 actual59 的完整身份、完整 selected-state/checkpoint 与负零 sidecar，逐词恢复实际 577×224 状态，再将 liveIdentity 与原 whole 对象及完整 spec 比较。此次不减少这些检查，也不以一个身份摘要代替状态数组。

## 3. QR 生成文件的实际内容边界

实际共享 writer 是 geometry_20261114_native_captured_band_correction.py，完整 36,867 B，SHA-256 b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390，Git blob be5433942409739326e5d2acd8039ca1bc19ef4c。

其 write 保存完整 JSON、换行和原 gzip mtime=0 规则；OutputArrays.save 将实际数值 payload 写到独立 large-arrays 文件，再将 name、file、dtype、order、shape、byte count、SHA、role 及有限/NaN/无穷/负零计数加入 output.entries。输出 array manifest 保存这些完整描述器。它有真实来源与测量计数，不能说成“没有信息”；但它不序列化完整 J、状态或方向数值正文。

本批 QR 部分共 9 份 input-binding 和 9 份 output-array-manifest：

- actual57 的输出清单由完整 native_damped_chain_qr 写出。实际因子、纯常数行、完整方向和精确整数行账是独立 payload，均不在删除表中。
- actual59 的 Original576System 绑定原 actual28 全部 576 块、所有原非零模式/节点、完整原输入 raw hash、旧到新节点映射及完整有限矩阵定义。输入数组由 export_inputs 单独写出。原576方向和 actual57 对照各有独立完整结果，不能因名称相近而混同。
- actual61 的四轮 current576 和 actual73 的三轮 noJ-primal current576 分别绑定自己的完整 snapshot、state、context、manifest、全源、完整 J、所有输入数组描述器、参数和原 cut/far 残差。旧父只承担它原来声明的原始初值责任，没有将旧 J/范数冒作本轮值。
- actual95 的 word-candidate 写的是本轮系统的完整 binding。全 word delta 和 proposed unit states 在独立 large-arrays 中。该候选的实际模型选择、旧模型结果和非线性失败记录仍在原结果中。

特别保留 actual95 的 parent91/input-binding.json.gz（41,348 B，Git blob bfbd1c82136e7915335981017a3bc199e50082d9）。源码显示它含 old_complete_model_screen、完整原 15 输入、原 proposal 与已知不可用旧字段。它不属于本次 18 份 QR 生成清单，不能仅凭同一文件名类推退存。

## 4. actual39 的两个大文件为何可以分开退存

actual39 是 run 43620111146，原源提交 56e8912844b6d7fafa268a9da8f184d6d055756f。本批两件为 input-binding.json 256,056 B 和 new-system-array-identities.json 154,415 B；本次没有读取这两个大正文。

完整 SplitCapturedSystem 源显示：

- system.binding 保存原捕获来源、实际 split result/spec/summary/source、全部 578 cell 与 old_to_new、原及新增节点规则、每块来源/byte/SHA 和完整新矩阵身份；
- system.arrays 保存 shape、dtype、order、byte count、raw SHA 和 virtual-stream 标记；
- J_rows 保存全部 new/original stage、window、origin、byte count、raw SHA；
- export_inputs 使用原 OutputArrays.save 另存所有数值输入和四个实际短 J 块。

完整 correction 的写入顺序为 binding、独立数组导出、数组身份文件，然后原均衡、带状因子与精确读回。数组身份文件并不是 578 块 J 本文，也不是方向、状态或独立精确行账。

本次保留原全 578 段 / 579 节点定义、574 个未改块和四个实际短块、旧节点与插入节点关系、原 cut/far/H/σ、原 3 次均衡与 3 次 refinement 的完整参数。原结论是新系统因子成功但原尺度线性缺陷巨大、修正后变坏；没有 nonlinear trial。它不是旧576系统求解成功，也不提供新的连续导数证书。

## 5. 原请求、完整参数和资源全部保留

既有完整来源直接复用：

| 原完整台账 | 字节 | SHA-256 | Git blob |
|---|---:|---|---|
| retention29 current576 provenance | 55,022 | 3c30ec4e8d3ad145c04767c7f1d42c11aea25fa25dcf45a9351702d3d1b2181f | 6b2b5593030151c184d692047f9837fd2e716601 |
| retention40 actual28/system metadata provenance | 98,273 | ed169ae6521d4beeb297f6e7bcb147cb7fcfd28e5e352de396e33c6e6a1bf855 | c834b974b297ed60177b70b97560ea84f9f76996 |

本批 full registry 对每个所用完整对象给出 whole record 与精确 JSON pointer，不用计数或简写代替原请求。actual61/73/95 的完整原请求还在本批 registry 中原样保存；三份原 saved request identity 和三份完整 current-solve-spec 文件在固定树上均已核得相同 blob/size，继续留树。

原请求原字 SHA 与保存后的 request-identity whole SHA 分开。实际原 source_commit、全部 source_sha256、artifact/ZIP、输入文件列表、原 scope 和 unknown 字段都保留。ret29 已记录的两个不同原 publisher 版本不能以当前 publisher 源替代；本批仍引用其原完整对象。

原 current576 资源为 Python 3.12.14、Node 24.22.1、NumPy 2.3.5、SciPy 1.17.0，BLAS/OMP/MKL 线程均 1，job 350 分钟、原科学步 320 分钟；eta 原字 1、node heap 6144 MiB、factor 上限 2147483648 B、exact workers 2、原 32 次迭代、10 次 trial、solve tolerance 2e-9 和最小空盘 34359738368 B。完整 workflow 和完整 argv 一起保留。

actual57/59 的原 job 120 分钟、QR 60 分钟、trial 30 分钟与完整调用参数保留。actual39 的原 45 分钟、均衡 3、refinement 3、exact workers 2 也保留。这些是历史配置，不是新执行命令，也没有因退存减少任何科学预算。

## 6. 原输入恢复责任保持原状

ret40 的 actual28 完整 PIN 仍为 run 43611175099、artifact 14120548264、235,561,097 B、ZIP SHA-256 0ff8e6f597af60f19243b5457c28e8638096c775551b6f3d044dc2d2f1fabeee；原 result SHA-256 ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7 与完整 J raw identity 同在原台账。actual41/54/57 的完整记录及恢复来源仍按 ret40 保存。

actual61 完整原请求明确保全部 13 个 actual59 选中输入、完整 577×224 raw state 与负零计数。actual73 仍将 actual61 failed point 仅用作 raw initial guess；actual95 保原 actual91 全 artifact、15 输入和初始状态责任。旧 base_stage_out、旧 ready-capacity payload 的既有不可用边界不补造、不写成空。

本次既没有读取这些大原数组，也没有重新下载 artifact；不凭仍有 artifact ID 推断今天一定可下载。**本批 28 个退存文件自身的完整字节恢复依赖固定 Git 对象，独立于外部 artifact 服务**。原科学输入的完整恢复合同、曾经的保存范围和既有不可用事项则继续如实保留。

## 7. 旧消费者仍然需要这些文件

原 original576 replay、damped replay 和三个 current hook 都实际读取完整 input-binding 与 output-array-manifest；它们检查 whole SHA、size、完整预期对象、checkpoint binding、完整形状与同一 current state。SplitCapturedSystem 也会读取原 before-seed identity。

因此此次不宣称“没有消费者”。要重用对应旧 reader，先把它实际读取的退存路径恢复为固定提交的完整字节；这些原守卫完全不改。不允许拿本批 ledger、计数、一个空 binding 或另一轮清单顶替。

八份身份副本也可以从对应保留 canonical 文件逐字复制回它们各自原路径；仍保各路径原 run 的记录。两个 canonical blob 不同，不能跨组拷贝。QR 与 split 清单按固定 Git blob 原样恢复，不能以重新计算的数值结果猜原文件字节。

## 8. 真实结果与未完成事项不升级

| 原实际分支 | 保留的真实结论 |
|---|---|
| actual38 split probe | 四个短 J 和四个独立 noJ 半窗已实际完成，旧 exit/mean 字保持；计划 probe 停止不等于 native 接受。 |
| actual39 split system | 全因子与完整精确读回完成，原尺度缺陷仍巨大，refinement 更坏；没有 nonlinear trial。 |
| actual41 raw steps | 全 868 原步局部 J 已捕获；不等于新全局系统已解。 |
| actual47 stage probe | 指定 stage43/step11 的局部矩阵及 same-run short J 已保存；字节审计与之后独立精确动作结论分开。 |
| actual54 direct-LD | 完整方向/读回后仍有巨大缺陷；随后原 trial launcher 的路径错误发生在全部非线性调用之前。 |
| actual55 direct-LD trial | 十次原调用均在原评估内拒绝，九次 momentum branch、一次 Newton line search；没有完整 trial norm 或 accepted state。 |
| actual57 damped | 十次 finite noJ norm 等于同一 recorded base norm，无下降、无 accepted state。 |
| actual59 original576 | alpha=1 第一步接受，只是一次下降；未完成原 native 求解、最终 height J 或 fresh audit。 |
| actual61 current576 | 四个完整 current QR 模型；前三次接受，第四次原 line search 失败，非超时完成。 |
| actual73 noJ-primal | 前两步接受，第三轮十次 trial 失败；完整有限 affine 预测下降不能代替非线性接受。 |
| actual95 word-first | 单词有限模型预测未带来原非线性 strict decrease；无 accepted native response。 |

完整原 notes 的字节、SHA 和 blob 均在 registry 中；原 ret40 中其他相应结论也完整保留。这里没有重做线性动作、范数、整数行账、J 或 nonlinear evaluation。有限数组精确读回仍只承担它原来的有限对象责任，不升级成完整曲面的 reach、活动幅度或误差付款。

## 9. 28 个精确删除对象

以下路径均相对于课题目录。每项还在 provenance 中保有原 run、完整恢复 tuple、known/unknown SHA-256 来源、producer 和全部参数来源。

| ID | 相对路径 | 字节 | 固定 Git blob |
|---|---|---:|---|
| ret53-01 | `notes/public-actions-43619564953-1-nativesplitprobe/native-same-schedule-split-probe/original-live-identity-before-seed.json` | 52,899 | `1730e2713f0b8673a8144a9e747a498145a0c582` |
| ret53-02 | `notes/public-actions-43622149326-1-rawcell0steps/native-rawcell0-step-capture/original-live-identity-before-seed.json` | 52,899 | `1730e2713f0b8673a8144a9e747a498145a0c582` |
| ret53-03 | `notes/public-actions-43630351235-1-stage43probe/native-stage43-local-j-probe/original-live-identity-before-seed.json` | 52,899 | `1730e2713f0b8673a8144a9e747a498145a0c582` |
| ret53-04 | `notes/public-actions-43634889730-1-directld/native-rawcell0-direct-ld/original-live-identity-before-seed.json` | 52,899 | `1730e2713f0b8673a8144a9e747a498145a0c582` |
| ret53-05 | `notes/public-actions-43636504089-1-directldtrial/native-direct-ld-trial/original-live-identity-before-seed.json` | 52,899 | `1730e2713f0b8673a8144a9e747a498145a0c582` |
| ret53-06 | `notes/public-actions-43637356027-1-dampedchain/native-damped-chain-original-trial/original-live-identity-before-seed.json` | 52,899 | `1730e2713f0b8673a8144a9e747a498145a0c582` |
| ret53-07 | `notes/public-actions-43657001633-1-current576native/native-noj-primal-current576-damped/original-live-identity-before-failed61-seed.json` | 52,899 | `3138af87d499e8763258d40351c31578eae091e3` |
| ret53-08 | `notes/public-actions-43675377211-1-current576native/native-word-first-current576/original-live-identity-before-failed73-seed.json` | 52,899 | `3138af87d499e8763258d40351c31578eae091e3` |
| ret53-09 | `notes/public-actions-43637356027-1-dampedchain/native-damped-chain-qr/output-array-manifest.json.gz` | 133,187 | `dbb0dd15e150ca78cfdd68dc5a2893f362545567` |
| ret53-10 | `notes/public-actions-43640772654-1-original576damped/native-original576-damped-chain-qr/input-binding.json.gz` | 61,380 | `55a09b22568098451a695a79363313d3dc55a49c` |
| ret53-11 | `notes/public-actions-43640772654-1-original576damped/native-original576-damped-chain-qr/output-array-manifest.json.gz` | 57,270 | `6d21e3d2e26979895b4f6e874c6553973436e83d` |
| ret53-12 | `notes/public-actions-43645948199-1-current576native/native-current576-damped/iteration-000/qr/input-binding.json.gz` | 72,206 | `c00b7abc7e1b03e085fbebe777c9c4a83eae2c45` |
| ret53-13 | `notes/public-actions-43645948199-1-current576native/native-current576-damped/iteration-000/qr/output-array-manifest.json.gz` | 57,370 | `cea818068e8c0998ce305788f310737bc7681ca0` |
| ret53-14 | `notes/public-actions-43645948199-1-current576native/native-current576-damped/iteration-001/qr/input-binding.json.gz` | 72,310 | `3787404793a1655162489488ff0773756b567d37` |
| ret53-15 | `notes/public-actions-43645948199-1-current576native/native-current576-damped/iteration-001/qr/output-array-manifest.json.gz` | 57,368 | `5299bebfaa6aa5ed152629e47bbd87293b973c5a` |
| ret53-16 | `notes/public-actions-43645948199-1-current576native/native-current576-damped/iteration-002/qr/input-binding.json.gz` | 72,310 | `527a7e6b49d4cea45072c98c809e095fa764afe7` |
| ret53-17 | `notes/public-actions-43645948199-1-current576native/native-current576-damped/iteration-002/qr/output-array-manifest.json.gz` | 57,374 | `5da3036c7feeb715595c304e32b81193f09667ff` |
| ret53-18 | `notes/public-actions-43645948199-1-current576native/native-current576-damped/iteration-003/qr/input-binding.json.gz` | 72,324 | `2e486bccd9b21b75f1ff8f43bfd702a0136e5e9d` |
| ret53-19 | `notes/public-actions-43645948199-1-current576native/native-current576-damped/iteration-003/qr/output-array-manifest.json.gz` | 57,340 | `12688dccaf1ea38326a82f4f08f4f1c2534a0059` |
| ret53-20 | `notes/public-actions-43657001633-1-current576native/native-noj-primal-current576-damped/iteration-000/qr/input-binding.json.gz` | 73,277 | `75f2aad7d764d2d83063d9479735639b22624d65` |
| ret53-21 | `notes/public-actions-43657001633-1-current576native/native-noj-primal-current576-damped/iteration-000/qr/output-array-manifest.json.gz` | 57,452 | `dda9438749d399aab3ba1df065b7b3837f7b5aae` |
| ret53-22 | `notes/public-actions-43657001633-1-current576native/native-noj-primal-current576-damped/iteration-001/qr/input-binding.json.gz` | 73,286 | `a07b5a5edfbdfe8a9caa5104fb76af24b46b1305` |
| ret53-23 | `notes/public-actions-43657001633-1-current576native/native-noj-primal-current576-damped/iteration-001/qr/output-array-manifest.json.gz` | 57,448 | `3c79b2c6b52c2faa8550e0b215f5bfc935cf2f28` |
| ret53-24 | `notes/public-actions-43657001633-1-current576native/native-noj-primal-current576-damped/iteration-002/qr/input-binding.json.gz` | 73,266 | `34bb59ed8b5af1108d97d8a1b01dadff1c4467fa` |
| ret53-25 | `notes/public-actions-43657001633-1-current576native/native-noj-primal-current576-damped/iteration-002/qr/output-array-manifest.json.gz` | 57,490 | `637dd9155c1fe73967eccef18f53801b7910fcb6` |
| ret53-26 | `notes/public-actions-43675377211-1-current576native/native-word-first-current576/iteration-000/word-candidate/input-binding.json.gz` | 67,801 | `81a7feabac09767566e2cf4fc07b7d7a0d9b9404` |
| ret53-27 | `notes/public-actions-43620111146-1-nativesplitband/native-split-equilibrated-correction/input-binding.json` | 256,056 | `efd0151e0fa176d0f27d90f23e0e0bc8f8455ca4` |
| ret53-28 | `notes/public-actions-43620111146-1-nativesplitband/native-split-equilibrated-correction/new-system-array-identities.json` | 154,415 | `69c678dfcfc6fc8f59b64a776e833f68e2a01aca` |

三组分别为 423,192 B、1,230,459 B、410,471 B，合计 2,064,122 B。只删除这 28 个精确对象。原 source/config/request/spec、数值数组、checkpoint、完整结果与证明、当前 science 材料、ports 与 Nelder 均不在此表。

## 10. 已知 whole SHA 与未知项

8 份身份副本的 whole SHA 来自两个完整小 blob；另有三件的原 whole SHA 在已刊小源/记录中明确给出：

| 旧对象 | 原 whole SHA-256 | 真实来源 |
|---|---|---|
| actual57 output-array-manifest.json.gz | 8a77b6b6365562ae3d41b3ff4832576f0bd880f41f2b5ed0a8fdefa86a650401 | original576 QR 源的 REFERENCE57_MANIFEST_SHA，按 reference57 result 的 array_manifest 角色读取 |
| actual59 input-binding.json.gz，61,380 B | b722d1c8cfd5a7a26b565f3392b1da505a47578c5b424f3db37838b30830566e | actual59 完整原 note 第 8 节 |
| actual73 iteration-002 output-array-manifest.json.gz，57,490 B | 3dbce9268dcb6667b2365f4c389dbc17c9e854c485b1873aa5fc222b2b0d00cf | actual73 原 failure note 的末轮方向身份 |

其余 17 件 whole SHA-256 在本次读取的小记录中没有找到，明确记 null。每件仍有固定 commit、完整 Git blob 和字节数，不能将 Git SHA-1、矩阵 identity、数组 raw SHA 或解压内容 SHA 冒作该文件 whole SHA。没有为补这些未知值读取任何大正文或 gzip。

## 11. 恢复方法与字节语义

在指定的历史恢复目录中，以固定提交及原完整路径取得原文件，或者按记录的 Git blob 直接恢复对象。输出重定向到原相对路径，保留原 .gz 字节和文件名；不要把大内容送入对话。

对恢复对象核原 byte count 与 Git blob；已知 whole SHA-256 继续作为原额外身份。原 JSON 不重新排键，原 gzip 不重新压缩，文件 hash 不以解压 hash 或内容语义相等替代。原消费者随后执行它已有的完整 source/input/binding 检查。

固定 commit 与每条原路径是完整恢复来源。数值重跑可能受实际状态、浮点环境、runtime 路径或时间影响，不被声称能逐字重建历史文件，也不是本批恢复路径。

## 12. 实施边界

本批只读 source/小参数/小原 note 与树元数据，生成完整文本台账及哈希；没有本地科学、AST/fixture、benchmark、raw 解压、队列操作或 ref 写入。旧实际结果未经改变。实施无需新增独立科学重跑、扫描或验收门；root 只按已授权范围对精确 fresh 对象做一次普通提交，保留原 source/参数与恢复合同，并在提交记录中报告实际净容量。

后续任何 active run 的实际值、trial 接受、完整 field、误差或新证书仍只能由其自己的完整真实返回决定，与此存储操作无关。
