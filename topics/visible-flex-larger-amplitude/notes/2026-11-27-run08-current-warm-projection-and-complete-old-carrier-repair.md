# 2026-11-27 run08：分开绑定当前 warm 与历史完整 observation carrier

## 1. 实际失败与修复范围

run08 的实际公开卷为 `2026-11-27-public-actions-45929088658-1-part-001.md`，完整 50,445 字节，SHA256：

`0f553795b9072d027c0b91832916d7daf91ebd61079fd0e76207cacf7cc2accc`。

真实 warm 已完成，真实 R690 reference preparation 也已完成。当前完整 warm 为
`4c34e0889a40e67a3a0a38abce030bb0358f74333fc1d8c95f669d5beefd9a0f`，
并不是历史 run05 的
`3df37dd362a1c700eaa86eece3d0b9a17524068c2a78fe0bebb1e96f1d09518c`。

当前完整 node report 为
`d7cac2c479defda89980c916f967353f5d1ac27f1c85cb93b37268972a4876d3`，
scalar gzip 为
`87bd2a4668638dbd49ec4523b33941c554b06471d1cf0ba522d3ea2a9a36ddb5`。
当前 preparation report 为
`4a3357f5daf16a08c267353d6c9064994c4de36b7d65e742ffde24f7ac8c8e10`，
reference bundle 为
`eeb55084744c60a5ed2e2bbb4343b01c73028a6ab61b1216142e4b3bf57dd6b4`，
observation carrier 为
`56b143f1ac7031b5cbeb12d02240fca28a67a57eba9938d5f134e4a1e7094d44`。

原 restorer `8c1e2d8f...` 的 `read_public_step` 对历史和当前两者都要求 whole warm 等于旧 `3df...`。实际第三步因此在原 reference-input 守卫处退出，报告明确为
`The public record is not the full actual reference input`。
原失败报告 SHA256：
`72363a45fd583ec8e7df1cb444e9e2a3a6219fbb6326d0a7cfdbe5db25b18348`。
随后两个入口没有取得所需 binding；没有返回新物理场或求解方向。

本修复不覆盖、删除或改写这五条实际记录。新的 reconstruction、science、reader 必须使用新 step ID 和输出目录。已生成的当前 warm/reference 继续使用自己的真实身份，无需重跑 warm/reference。

## 2. 为什么不能把 whole-warm 差异当成“只有 metadata”

历史 warm 的实际 H 为 1.9479520470229232，当前为 1.9479520470229237；这已经是工作字的差异。全部 qjets、DFT circle projection 或压缩内容是否还有其它差异，当前没有逐成员的历史数据对照，不能猜。

另一方面，完整历史 observation carrier 不消费全部 warm 自由场。原 bee5 producer 保存恰十个成员：

| warm 成员 | 原 4e/旧 carrier reconstruction 的作用 |
|---|---|
| `mesh` | 全部 923 个径向 carrier；原观察 plan、time error 和 symbolic-node recipe 的必要输入 |
| `qjets` | 检查完整 shape；提取 `qjets[0,0,1:161]` 作为固定 chart core |
| `width` | 原 literal lift width、唯一 exact breakpoint 与观察 plan |
| `radius` | 核对原 FullHold carrier；保存的 R690 radius 由 deep scalar 重新产生 |
| `fixed_core_first3` | 与完整 core 前三字交叉核；旧 carrier 保存前三字 |
| `Hcap` | 当前 4e preparation 另记原 warm 高度；不进入旧 carrier 的 plan、a、误差或保存内容 |
| `a_stages` | 不复用；完整旧 observation a 重新按准确 scalar 求值 |
| `circle_projection` | 不进入旧 carrier |
| `a_stage_absolute_error` | 不复用；完整新误差重新产生 |
| `stage_time_absolute_error` | 不复用；完整 observation time error 重新产生 |

因此合法修复是严格核真正消费的投影，再真实重建并核整个旧 carrier，而不是声明两个 warm 相同。新 source 会记录全部十个当前成员的 dtype、shape 和完整 array SHA，但不从这些当前摘要虚构旧成员差异清单。

## 3. 同一个准确标量、域与固定 chart 的条件

新源码保留完整历史输入定义：

- 准确 scalar 参数投影 SHA256：
  `e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa`；
- 全部 mesh array SHA256：
  `eff967897039ec740c9aca49620253f27fb46d93cd8c59f4ed4759781ef88262`；
- 全部 160 项固定 chart core array SHA256：
  `90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e`；
- 原 literal `float(.05)` width；
- 原完整 923-node affine-in-S 配方：保留全部 819 个 prefix literal nodes，然后依 bee5 的五段 4/8/64/12/16 分割构造其余节点。

这些原值来自完整 c79 material-envelope 源
`c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152`。
新 restorer 在运行时读取这份完整来源、核 whole SHA，再用 stdlib AST 只提取原六个 origin constants 作相等核；不执行或改写该旧 consumer。

准确 scalar 的相等要求当前完整 scalar 文件真读得到的
`analytic_extension_origin` 与 `fixed_scalar_profile.geometry`
整个投影相等，并且 scalar/integer/hold/deep 各完整源码仍为原固定身份。不是只比较一个自报参数 SHA。

全 mesh 的逐字摘要固定前 819 个 literal nodes；准确 scalar 固定 S 及五段参数；完整 Fraction recipe 与当前 node report 的全部 923 项 `true_scalar_nodes` 逐项相等。因此准确 symbolic domain 也保持。全 160 项 chart core 的摘要同时保留固定材料角映射。前三项、width、FullHold endpoint carriers 另核，不能用 shape 代替身份。

上述均为新入口必须实际通过的输入条件。本说明没有提前宣布 run08 已通过新 guards，也没有继承任何旧场、根、Gram、曲率、reach 或存在性证书。

## 4. 当前完整来源链

新 `bind_actual_warm_return` 从同一实际 run/attempt 的完整公开卷提取唯一 warm return。它核：

1. 真实 warm completed/returncode0 与 M160/J923/922 cells；
2. 实际 wrapper source 是 `reproduce_and_solve.py` 的 `067b3f2e...`；
3. 完整 `input_files` 中 recipe 是 `561308ca...`、hold-warm producer 是 `bee5ae58...`；
4. warm、node、scalar 三输出的路径、字节数和整文件 SHA 与当前 preparation 的 `original_warm/node/scalar_input` 逐一相同；
5. 三文件均处于本次实际 `RUNNER_TEMP/visible-larger-research-RUN-ATTEMPT/research/fullclosed_solver/data`。

这里明确区分顶层 wrapper source 与被执行 recipe source，不把 recipe SHA 误当公开 warm 记录的顶层 source。

当前 preparation、reference bundle 和 carrier 仍逐文件绑定本次真实返回。旧 WARM SHA 只保留在历史来源记录与历史 public-step 检查中。

## 5. 历史完整 carrier 仍以原 SHA 验收

历史输入仍是：

- 原 actual public volume SHA：
  `6eca69a388330b3e539aac4e2c793ce8256c724d52abf11adc8c8e85d49d08b3`；
- 原 live leaves：2397；
- 原完整 scalar 参数、tail cutoff `1/8`、integral tolerance `1e-18`、panels128、原 observation order6；
- 原 whole carrier SHA：
  `dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0`；
- 原 whole carrier 大小：227,202 字节。

2397-leaf 构造保留原 integer/Fraction leaf arithmetic、heap priority、tie order、完整无限尾和已记录 accuracy 状态。当前 scalar 文件只提供已证明相同的准确参数；旧 `input_identity` 是显式的历史被重建定义，绝不把当前 scalar 文件改标旧 SHA。

原 make_plan、全部 7377 个观察点、a/ae/time error、radius、keyword 顺序、dtype 与 `np.savez_compressed` 均保留。只有保存候选 whole SHA 和字节数同时等于原 dc5/227202，才建立历史 carrier 身份并输出供后继使用的 binding。若任何投影核或完整 SHA 核失败，输出真实 failure；没有丢弃字段、近似接受、偷偷改用地址 packet 或猜测压缩等价的 fallback。

新、旧全部 plan arrays 仍逐字比较；如果 material addresses 不同，后继仍消费原完整 old/current 并集，不从“同准确 g”推断工作地址相等。

## 6. 完整 consumer API

新文件使用独立 basename，保留旧 8c1e 文件不变：

`restore_actual_run05_carrier_for_compatible_current_run08.py`。

`binding['current_input_compatibility']` 含六个完整当前 file records：

- `current_warm_bundle`
- `current_node_report`
- `current_scalar_input`
- `current_carrier`
- `current_preparation_report`
- `current_reference_bundle`

另含 whole historical carrier、历史/当前完整 public return、原 envelope source record、完整准确 scalar 参数投影、当前 model/scalar identity、固定 mesh/chart 摘要、完整 symbolic-node 摘要、literal width 与来源范围字段。binding 同时保存
`current_input_compatibility_identity_sha256 = canonical(value)`。

纯 stdlib validator 的固定签名：

~~~python
validate_current_input_compatibility(
    value, *,
    actual_model,
    current_carrier,
    current_preparation_report,
    current_reference_bundle,
    current_node_report,
    current_scalar_input,
)
~~~

所有文件参数均为真实 `file_record` 字典。validator 重新核六个当前文件整 SHA/bytes；warm 由 value 中的完整真实 record 重新核。它真读完整 preparation、node、scalar 及 public evidence，将完整 source/model/输入关系相互核对，并再次核历史 whole carrier。调用方不能用 shape、count、某个 True flag 或别的模型摘要代替实际文件。

此 validator 不 import NumPy/Torch/SciPy，不构造或评估物理场；它对 scalar JSON 只提取并核完整准确参数，不跑科学积分。后继 memory consumer 必须整源 pin 此 producer 后才调用，并核 binding 内 canonical compatibility identity。旧 consumer 的 e640、全 mesh、全 chart、P0、old whole carrier 与 typed 策略守卫继续保留；只将错误的“当前 warm 必等旧 whole warm”一项改为此完整受检 current compatibility。

root 已实际读取 controller 源确认：旧 followup source worktree 在本 job 内保留，清理只针对显式 rows cache。因此这些被绑定小来源路径对后继 consumer 可读；本版没有新增复制或依赖一个未持久化本地临时文件。

## 7. 完整来源与已做的验证

完整新源：53,529 字节，SHA256：

`6cc95526e5305fa0265b96f66d322bbba612b8702d5ebcc5ec48a9fb29639d19`。

远端未引用完整 Git blob：

`69c09e991ac162db64761a6f176c749932996eff`。

它从真实 GitHub 取回的完整 31,102 字节旧 8c1e 源纯文本派生，并已再次从远端 blob 取回、核同新 SHA。不是仅有本地 hash-object 的未上传对象。

以下完整数学片段与 8c1e 逐字相同：

| 片段 | 字节 | SHA256 |
|---|---:|---|
| exact symbolic-node recipe | 1220 | `f07d88dad55057c01e6bde1db4552299c3ec9f23e6a6ff8ac4417947b404c004` |
| counted-tail class 的全部 exact leaf body | 3159 | `9d160a25523b17f46fea1a4096ca43572eca5dfa0c1b396c93f4979b8a502dae` |
| deep 构造至 radius/plan/7377 observations/save/full-SHA/array comparison | 5563 | `59474b1661e43b596090af8eec1a3a7d17c1490cf3f54ad9fc0249e70bd72e04` |
| member comparison/array records | 367 | `5a1ef1b963e3d8f46369d35ba2787bb28c03edfb0cf94a8ca2a3b2df89cf862d` |

本轮执行环境在修复期间失联。此新源已完成完整文字、自身来源和逐字不变片段检查；**尚未实际 AST/compile，也没有本机 scientific import、数值 fixture 或科学运行**。不能把这些未运行项写成通过。真正 reconstruction 是否成功以随后公开 Actions 的完整返回为准。


## 8. 完整可再生脚本

纯 stdlib 再生器为
`derive_run08_consumed_projection_carrier_repair.py`，
29,815 字节，SHA256：

`0f05ea9e1dca4d0b0ffbc2f7c42037756870010577198fbe76a3bbacde6eac73`。

远端完整 blob：
`c86bfb1248304f1c0023cd7dc72c68db87c19ff6`。

它核整个原 8c1e SHA，应用完整 17 个精确行段变更，核整个新 6cc SHA 与上述四段原数学体，随后仅作 AST/compile。可用 `--verify-existing` 对完整已写文件逐字复核；不会 import 或运行新 scientific source。例：

~~~text
python derive_run08_consumed_projection_carrier_repair.py \
  --parent restore_actual_run05_carrier_for_current_run08.py \
  --out restore_actual_run05_carrier_for_compatible_current_run08.py
~~~

本次已在 functions 的 JavaScript 内存中实际按同 17 个变更重组完整文本，并核 6cc 整字节身份；Python 再生器本身尚未执行，其未来输出中的 AST/compile 状态不能预填为本次已通过。

solver 已独立逐字段核 `bind_actual_warm_return` 和完整 compatibility validator 对应实际 08 warm/preparation 小卷、4e 与 bee5 字段，未见所读接口阻断；geometry 已独立核 execute 的投影守卫，并对 ef674/8c1e 逐字核原 exact-node、2397-leaf、radius、全部 7377 observations、save 和 whole-SHA 拒绝段，未见所读范围阻断。两项均为源码/真实小卷静态审查，没有本机科学运行，不替代新 Actions 的实际 reconstruction 返回。

## 9. 完整六份后继源码与原科学体保留

root 将完整 5f22 memory、c253 geometry、eb22 transfer、91c driver、904 launcher、c0cc reader 逐字派生为独立新 basename。旧文件均保留。新 memory 只将当前 whole warm 必须等历史 whole warm 的错误要求，替换为第 6 节完整实际文件 compatibility；原历史直接载体路径仍要求原 whole warm，原 c79 strict terminal 路径不放宽。

新 memory 在首次载入当前材料包络和完整报告读回时，重新核 compatibility 的 canonical identity、实际五个调用输入记录、真实 preparation/model 和整份 6cc 源，才调用其固定纯 stdlib validator。完整旧载体、全部 grid/角、P0、原十一来源和全部 typed history 守卫不变。此验证不放入每个候选的热筛循环，不重新构造 F/J/root。

新 driver 增加直接角色 `independent_input_projection_producer`，整源 pin 6cc；直接角色由 39 变为 40。其余改动仅为完整新 memory/geometry/transfer 路径及全 SHA。launcher/reader 跟随完整新 driver，原全部统计、normal/C1/stage/adjacent 计数、原科学输出后缀均保留。driver 从 `save_report` 至 EOF 的整个原科学后缀 SHA256 仍为：

`3a34eeb13a52579aacafb1598c52a94a42f8db2cfab03a3fef0d64c2b88937d5`。

所有六个新文件均已在云端 JavaScript 内存中用登记的完整精确文本替换重新生成，整 UTF-8 字节及 SHA 相同。完整再生器 `derive_compatible_current_input_adjacent_entry.py` 包含全部 parent pins、完整替换文本、完整新源 hashes 和上述科学后缀核；它的 Python AST/compile 尚未执行，不写成已通过。construction 对完整新 memory 的真实 API、首次载入和纯报告读回作独立文字审查；没有本机科学 import、数值 fixture 或额外科学验证门。

| 完整源 | 字节 | SHA256 |
|---|---:|---|
| [so3_reference_centred_compatible_frame_material_envelope_geometry.py](../scripts/resume_20261126/so3_reference_centred_compatible_frame_material_envelope_geometry.py) | 68275 | `ba98027d88f2949e902af90bc9fe19cb0e18c0e758512c18382798e1a050425b` |
| [transfer_material_envelope_memory_to_compatible_frames.py](../scripts/resume_20261126/transfer_material_envelope_memory_to_compatible_frames.py) | 55758 | `f3264400100cabbf717c4e07cae70d7cabca8403bc6c8b4c46c726da3eb6f10a` |
| [fullclosed_reference_centred_compatible_frame_material_envelope_so3_qp.py](../scripts/resume_20261126/fullclosed_reference_centred_compatible_frame_material_envelope_so3_qp.py) | 74542 | `5c5c2c944c030682bc85470089590a4d3f1536049942d6a3de6cf79e38ed2191` |
| [launch_reference_centred_compatible_frame_material_envelope_so3_actions.py](../scripts/resume_20261126/launch_reference_centred_compatible_frame_material_envelope_so3_actions.py) | 20745 | `a52e4b54d7785b226a255c5d938892198164858907795e93337c529a8b2c625e` |
| [read_reference_centred_compatible_frame_material_envelope_so3_report.py](../scripts/resume_20261126/read_reference_centred_compatible_frame_material_envelope_so3_report.py) | 95632 | `475fa6d8505611d8198debc97f5bb4101fb18c10312835178d486e3c366a927e` |
| [complete_material_envelope_memory_compatible_current.py](../scripts/resume_20261126/complete_material_envelope_memory_compatible_current.py) | 45188 | `1e2ca9ec89d407d6d187ed60fe94406820f098dfca7c2b70c4f0645ea9bcdfa9` |
| [restore_actual_run05_carrier_for_compatible_current_run08.py](../scripts/resume_20261126/restore_actual_run05_carrier_for_compatible_current_run08.py) | 53529 | `6cc95526e5305fa0265b96f66d322bbba612b8702d5ebcc5ec48a9fb29639d19` |
| [derive_run08_consumed_projection_carrier_repair.py](../scripts/resume_20261126/derive_run08_consumed_projection_carrier_repair.py) | 29815 | `0f05ea9e1dca4d0b0ffbc2f7c42037756870010577198fbe76a3bbacde6eac73` |
| [derive_compatible_current_input_adjacent_entry.py](../scripts/resume_20261126/derive_compatible_current_input_adjacent_entry.py) | 16368 | `918eadbf0f35f0bb359ab9f0dd6f683ed5a28d26175ae8871650089cb11b7259` |

## 10. 全参数三步续接与真实旧四步归档

本次在同一个实际 run **45929088658/1** 的 followup 队列提交以下三步；只有实际控制器返回才算已执行或通过：

1. `restore-actual-run05-complete-carrier-compatible-current-run08-20261127-v2`，使用新 6cc 完整重建；
2. `complete-independent-compatible-frame-full-envelope-20261127-08-v2`，新 a52e launcher/5c5c driver 的完整独立分支；
3. `actual-independent-compatible-frame-full-envelope-20261127-08-v2`，新 475f 完整纯读回。

旧四个 followup 对象只有在逐个核真实 step_id 已返回后才从活动队列移出。第 2 步 reference 成功、原第 3 步 restorer 失败、原第 4/5 步失败全部原状归档：完整原 script、parent、每个 argv、全部 summary 路径、outputs、scope、cleanup、原头字段与实际完整 compact return 均保留；失败 summary_errors、missing_outputs 和退出码不删除。warm 的原完整公开记录仍保同卷。没有删除未返步骤，也未将失败科学入口称为已算首场。

原四对象的完整来源是提交 `291adcd2b2f4de1dac4c7118dbce69b471dc5813` 的旧队列，57,618 字节/SHA256 `52d277dbac947142f511adafc452976f112ebd9da25b0a857af3e5c06b50c778`。实际记录使用提交 `e553b6fb567f73b58b128fd263d4211d4cb5d5d5`、blob `734ec6541c064e102273126d7481d41dd408707c` 的完整 50,445 字节公开卷；它不是正在增长卷的未固定快照。

| 全参数文件 | 字节 | SHA256 |
|---|---:|---|
| [resume-20261127-followups-08-returned-002-003-archive.json](../computations/resume-20261127-followups-08-returned-002-003-archive.json) | 39332 | `3aad3de97322dfaf45fc37f83563679da9e9d038c1934d8b9abd475bfc6e75b5` |
| [resume-20261127-followups-08-returned-004-005-archive.json](../computations/resume-20261127-followups-08-returned-004-005-archive.json) | 72479 | `1e5f435b77b6494c29c8d4b3a615ce92002c7ec5b80f71d24d9b5a45268da623` |
| [resume-20261127-followups-08.json](../computations/resume-20261127-followups-08.json) | 62973 | `4c38a226f9fe05f290bf868de781c88572723d80b08c6644944f4af3f76f5217` |
| [reference-centred-compatible-frame-independent-envelope-run08-ready-v2.json](../computations/reference-centred-compatible-frame-independent-envelope-run08-ready-v2.json) | 80571 | `21450415dfa0ffc91f99237f3d4e90dbb4aa2f8a599f89d4d4c567b0483b7e18` |

新三个步骤的 argv 分别仍为 **16、139、7** 个词。逐词与各原步骤比较，变化只有新源码/输出目录/对应 binding 路径；原数字及开关完全不改。仍为 M160/J923/P7377/N2048、32 normal stages、全自由量/全 Gram/Phi/C/J/J*、原 endpoint/Q18/bubbles/gamma、十二片/192 正权 seed、1 个 metric direction ×16、4 个 restoration directions ×64、15 rays、192 原前缀及全部 amplitude/typed rows、near-active32 但不截永久 typed。原所有精确 fractions、tolerances、thread/块参数和完整配置以全 argv 为准，不以本段摘要代替。

旧输入只使用真实 run08 warm/reference 已返回的整文件；新输出路径是 `run05-actual-observation-carrier-compatible-restored` 与 `reference-centred-compatible-frame-envelope-normal-lift-v2`，不会覆盖原失败产物。未返回的新 binding、载体/科学报告 hash 和数值结果均为空或未声明。未知 07 terminal 和适用的未来 typed history 仍须完整绑定合入，不能因独立起点豁免。

## 11. 环境、规则与持久记录边界

最后一次 root 真实 CLI pull/rebase 为 2026-11-27 02:43:10 UTC、提交 `5ddd1f551e6df201c5a92693f842be05945bb310`，随后真实推送 48bf。执行环境约 02:50 失联后，本修复使用连接的 GitHub API 读取固定提交并作普通 fast-forward 提交；**云端读取不冒称真实 git pull/rebase**。恢复终端后仍须立刻真实 pull/rebase 并核双 README 差异。PAT 没有进入文件、提交或连接器参数。

本次发表前实际读取 main `37c083b9539cea50cb76b752e940355eba63c1da` 的根 README 和本课题 README，分别仍为完整 SHA256 `581402c2148ee8c4ee2af741198ab54a56d71de2b5a7b0d0edf65359121cb102`、`3c1c03b358792b6c9937b95fcfea05b80a572a4da2cce615c4c9832fe929057d`，相对上次无变化。若普通更新被 CI 抢先推进拒绝，将读取新 main、仅读规则差异、保留新 CI 槽后重建普通父提交，绝不 force。

本提交只保存完整小源码、完整原参数/来源、实际小卷结论和完整失败对象；新大 raw、载体与生成证书仍仅在 runner，未存 Git、Release 或 artifact。这里没有新的 metric/reach/嵌入或严格存在证书，当前题目仍未完成，后续继续实际求解、根费用和真实同问题精化。
