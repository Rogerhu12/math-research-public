# RET100P：已闭原Actions源码的完整原字恢复

本记录只整理已行政结束的历史计算源码。每个原请求、参数、报告、失败、当时贡献与未解决数学问题原样保留，不把官方success充科学收敛。

## 完整保存与精确恢复

固定原态 `092d4d9834744ad0e853df76a7ac30656876f71b`。220份完整历史源码共6099115B，全部来自2026-11-14至16的原公开任务。它们由86份独立、仍保留的完整父源码及16份语义完整的逐行文字差异精确恢复。21件新manifest/恢复器/来源与保护记录/差异共1381546B，源码族净释放4717569B；本note和导航的开销另计。没有退唯一计算状态、真实系数、原任务报告、参数请求、活输入或既有恢复父文件。

通常恢复：在课题目录运行 `node computations/reproduce_ret100p_closed_public_sources.mjs --out EMPTY_DIRECTORY`；从别处可另给 `--topic TOPIC_DIRECTORY`。恢复器只读本地已刊完整文本，对所有父/差异先核字节、SHA256和Git blob，按原行号插入原字，恢复220份全部源码并再次核完整三身份，全部验证后才写新目的目录；任何不同的已有输出都会报错。原固定提交与原官方trigger同时保留原完整件，未改写git历史。

ROOT已独立完整读取86个父和16个差异，用正式restoreWhole函数重建220/220，累计6099115B；再完整读取220个原blob逐字比较并重新核对三身份，全部一致。这里只进行文本恢复/身份核验，没有运行任何新科学计算。

## 原运行与触发来源

ROOT重新访问27个原官方run和45个job，逐一核对run/attempt/head/workflow、每个job id/name/status/conclusion，全部确为completed，包含原failed状态。再从每个真实trigger的题目/工作流目录metadata及单层树验证：原完整请求、原workflow、原源码文件都在该head、字节/Git身份吻合。27个原完整请求和27个原workflow全文核三身份，workflow含实际原请求名；220源的SHA256均在各自请求给定JSON路径，206条以文件名为SHA map键，另14条是同object下明确filename sibling。不能把仅同名later source或同号request充原科学。

|原run/attempt|真实trigger|官方conclusion|完整jobs|
|---|---|---|---:|
|[43684544925/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43684544925)|34691ac1052c0d86950f864835534fed52515565|success|2|
|[43685348016/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43685348016)|8d4a3af1d553cd85cfa9694ec8cfaf1c0b66ce3f|success|1|
|[43685696741/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43685696741)|a7ea42924dbdaf8dab9377ace446690e0ce922c5|success|2|
|[43687426018/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43687426018)|dc032461bbd2f3f7515ea30e5495b50870a06f65|success|2|
|[43690052251/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43690052251)|4f4dbf700ee0732f6e7bd245f35808592ac82607|success|2|
|[43693006085/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43693006085)|bb1d75675dc639f3f1ab74749798a5c11b2ac3a5|success|1|
|[43693462669/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43693462669)|6fffce1f36e876f3b08a1c73198a7fde259d94d6|success|2|
|[43694950669/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43694950669)|da16069e10e11d4541992fa66c6f03ee7165baf7|failure|2|
|[43702578242/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43702578242)|690ca0f924f069c6b8c2134ca83bc856918c2e89|failure|1|
|[43712613111/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43712613111)|a7ce55798404fec8fb3638c0fbf083250c5363b2|success|1|
|[43732286420/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43732286420)|4241fb33b951ee3b0bad9b1579ec7efb7e0de62e|failure|2|
|[43729456722/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43729456722)|ce2b12c0f391a008343866ed9fe649f44d91ed28|success|2|
|[43743904448/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43743904448)|257b227a49034faaf1979bfe093122e7d06e1785|success|2|
|[43741519736/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43741519736)|de9a730a8f9cf8ea1f3e31fa6f6dd9cfb64e1d80|failure|2|
|[43739787509/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43739787509)|298c7dbebc28b5fa94bea030b4efe1426b21bf67|success|1|
|[43745317876/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43745317876)|3975e583fcdb54e3b87a50bcb0fda8c964ba13bc|failure|2|
|[43745211514/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43745211514)|411c6ed30e304c681c5ced2f672f4518d138020f|success|2|
|[43748206814/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43748206814)|48e55d2e0f6f07405c216b5417ef97844654124e|success|1|
|[43747934170/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43747934170)|d7540200dcf5e10378471620915aa29a39389862|failure|2|
|[43761083360/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43761083360)|068805ae3009884cbbcd200ba4c9f9be474f5bd7|failure|1|
|[43784544723/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43784544723)|1a757004b7ebff1f43563bd57b5d13961648d681|success|2|
|[43790929300/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43790929300)|557b1d47cd637d268cf292c86f77218ccc3b5458|failure|2|
|[43812359001/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43812359001)|fe0a0d737440bcad59d5af9cb9d08b24131204f4|failure|1|
|[43830433500/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43830433500)|0f101b697beb04db9bf6c225a488755e191f3a54|failure|2|
|[43839064900/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43839064900)|035d28663109b4d94a48c4223c29f06d88796978|failure|1|
|[43872121853/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43872121853)|cec9d8c877fa92bd5edf70f950ff7e0dcd77e2c3|failure|2|
|[43897098674/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43897098674)|f70acbf1886f0f363c3c1d6b60760438f59e545c|failure|2|

全部原请求/源对应路径、每job身份和已保原报告见完整 [来源册](../computations/ret100p-original-action-source-bindings.json)。未执行的后续阶段和原失败不会因源码恢复而变成已完成。

## 当前与既有恢复保护

ROOT独立全文读取两保护册所列811条、810个不同路径，均小于100000B。789个全文没有任何一个被退源码basename；其余21个为RET100K/L/M/O中用于恢复历史完整JSON/源码的literal差异记录，出现位置只在rows或members的原字内容。所有既有恢复器、manifest及完整输入父本身不读取这些待退路径；重建旧任务需要时由本恢复器先生成全部旧源码。两册列出的当前/已声明后继输入（含R77721源、R78023源、47实际17861B请求及R783–786）全部保护。另到达的52八完整新件也逐字查220名为零；R788不依赖这些旧快照。

14条在保护快照尚未推main的准备件均有独立原blob、字节与路径身份，不能误称当时已刊。本提交只退明确220个旧computations源码路径，完全不触及这些准备件和当前工作流。原活动运行在冻结源上继续所有原预算。

## 全21件完整交付身份

|路径|UTF-8字节|SHA-256|Git blob|
|---|---:|---|---|
|computations/ret100p-closed-public-source-recovery.json|63739|3bb99bade4c3c98858c1e8f080b0763f4297706ccc74dd2d801d1d769b6b349e|7a50bdee1a25b0451a6b676d003cffed2f8778b5|
|computations/reproduce_ret100p_closed_public_sources.mjs|3952|1bbac1c9fe50e2f2727424f0c78fba6abd78b3f282d88f23842e66f905683000|c51be798d672a190a145fea4fa065b15a242875c|
|computations/ret100p-original-action-source-bindings.json|50319|472e930ebc7766882690602ebf1c2d18d27d718e7886f06e2c6ab9b56e82fa2e|83b89942552f6c02acbc177f2200b871bcba5eb6|
|computations/ret100p-existing-recovery-dependencies.json|54615|2e02236ac287ab4c8fe42e27bb3550e7bd56249b2a204349e0a046fc5734332b|a3d74520674413c2e4d26156d764965dbe430691|
|computations/ret100p-current-scientific-dependencies.json|45632|f0360167527107a981922c63db6d08ac80b6f7b74e900773a90827741a89dde3|dcf09c5c1abed7c2cdf58beda93af535b7b787b4|
|computations/ret100p-complete-source-replacements-01.json|44646|779838820c1b3a397f2bdb6b66e09e6761698998f72f50ff01daf98d8a6134f0|4ee6adc608c545ad1ddbea252ab06941617973f8|
|computations/ret100p-complete-source-replacements-02.json|79741|0c0b0c990a300ce8a69a28bd50f19d50a6fb0e8c0dd6fc2adffab274fbf13a00|caf7338b1b48e87573bfb6288679c90dbd030d7c|
|computations/ret100p-complete-source-replacements-03.json|80508|936a422145e25286ecf548ec75b90f13fa0142756f81235bf02ef8395796fffc|deb813be2eac26827a356acd616e2a7c2ad67c4a|
|computations/ret100p-complete-source-replacements-04.json|63411|f688be6ba4199c06c2580cfd265a9ded010a8f9bac274baa9000d2a55f900412|503b40f7dea264e7dc13c6aff54f7a7e426d74dd|
|computations/ret100p-complete-source-replacements-05.json|71687|821e27687c93b8752efc352a08784d98d10c01d95d940ffb86557f5e7176495b|6554543554b62df0850133d246dc1b65bf522054|
|computations/ret100p-complete-source-replacements-06.json|79691|f59147011a46e9649ef8e2b90445c0548293c466a18becb7a9d930c26211c1f5|20ace88b38b3da91571f29079cbb14a6138ba7a4|
|computations/ret100p-complete-source-replacements-07.json|80876|edf38f2021b60366c360b2574719091d4540d10fbb53ec12bc2fe0bec23962a9|52a50cac1df157aeb10ca9e70301e92ad79bed2e|
|computations/ret100p-complete-source-replacements-08.json|76148|f164783180a450725431de84301edae1d6afd330d887169bf108345eaccdae26|5f74fab9253153a08a831856cbba082e165068b8|
|computations/ret100p-complete-source-replacements-09.json|77813|3380bd99f9bb6086e57dde6d93f583a0df9e7405221e9645e0eeec180ffe48fe|0c70f42c3f173416790558d47ea354d69a595332|
|computations/ret100p-complete-source-replacements-10.json|75778|2bfe8f6791d86a296ceebf4b1b7e6d18184dcd2b9bbffb3a84fd34fc23f63a25|332585d1843f559705b7d2299323e5d4fba6c42b|
|computations/ret100p-complete-source-replacements-11.json|73350|e7f9ed01a167133318c394f496145514b5348e61c881a6911e0a6f0b7dfb07d2|c3dd34f272de94cfdd35337515dc56275c0a33a1|
|computations/ret100p-complete-source-replacements-12.json|81118|d32d99c361aac80fc23556c440ee50a048dddfcc9af9d0bd3a43b699cf795726|ecc2c6f26caa3e3de7e412cbec8ae14072ae0174|
|computations/ret100p-complete-source-replacements-13.json|78000|de7e9686eb27fc1273cbe0f874e6b6fbf78825cd7836d7ca8fd6bd9d20a642d1|0f896a0b571afec2a926a29ad15d7f5b4f309051|
|computations/ret100p-complete-source-replacements-14.json|79737|b33aa944cbad6e1bd6153a3e9459d6f6b7d7c46a19238bb702ccfad72389a428|2970e9826136464e4a7d1eb3412623c94d5ab888|
|computations/ret100p-complete-source-replacements-15.json|74836|34bb2d3caaf6430694c2c5f232684598285a105691db4f1a3daa6870f60a9176|8f5bbad2db9dfa32ab4da0424537e510c186124d|
|computations/ret100p-complete-source-replacements-16.json|45949|577bc9fc5523a601b9164fa830637ad30bec3bf89da45239b6a3048af6e526d5|f40d3ca5406cfc167e456c8bab9c56a0820c8dce|

[完整manifest](../computations/ret100p-closed-public-source-recovery.json)包含全部220原件、86父、逐件父映射、16差异与其他保护来源身份。继续真正求解；这次可恢复整理本身不支付任何剩余几何或等距条件。
