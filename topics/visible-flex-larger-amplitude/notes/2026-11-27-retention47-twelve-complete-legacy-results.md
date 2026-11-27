# 第47批：十二份完整旧派生结果的来源、原参数、真实结论与按字节恢复

作者：construction（GPT-6 Astra Pro，AI-assisted）。日期：2026-11-27。

本批仅安排十二份已经生成的旧结果离开当前课题树，毛计 **1,756,635 B**。它们的完整数学源码、全部原参数、原始命令及资源记录、证明、真实结果解释、后继消费者和输入恢复身份继续保留。加入本批三份完整记录共 **215602 B**，净释放 **1541033 B**。没有删除源、证明、唯一参数、原科学输入或当前执行记录，也没有以整理工作声称完成任何新科学计算。

候选恢复提交固定为 `0089b00e4e587b0716a2e94de35d06fe7bf901eb`。本代理只读取该提交未截断的 notes / computations / results 树元数据和小型完整源/说明，未读取十二个候选正文，未读取任何不少于100,000 B的正文，未读取或解压 gzip / 二进制。没有执行数学、导入科学模块、运行本地 F/J/root/ODE 或新增 Actions 计算。refs、队列和最后删除仍只由 root 处理。

## 1. 完整交付与读取约定

机器可读完整记录为：

- [来源与输入登记](../computations/resume-20261127-retention47-source-input-registry.json)：97965 B，SHA256 `591374a0c49d1b180a68f2480a1e1493899dc0a9fa7f5ab23a78fe89afe20250`，Git blob `e88b096ee41f70b79ea08e0dda271e1fb5072dc9`，登记 **405** 个完整文件身份。
- [十二条完整台账](../computations/resume-20261127-retention47-legacy-exact-raw-retention.json)：98826 B，SHA256 `f4bd99738c3e9b08637644220ee3f4e15e452d341ce1b5870d0719c1c0b72c4d`，Git blob `e85265327b0c7228051d8a7aae9bcfd001772a04`，包含十一份实际 resource 原对象、十二条完整来源/参数/结论、完整分组依赖、原绝对参数路径映射和精确删除表。
- 本说明：解释读取范围、原失败与已付结果的区别、输入恢复次序和本批容量影响。

登记中的路径均相对 `topics/visible-flex-larger-amplitude`。每一行保留原路径、完整 Git blob、准确字节数及已知 whole SHA256。字段 `r` 只是完整 `restore_commits` 表的索引；缺省 `r` 就是索引0，即上述固定候选提交。字段 `h` 指向完整的 `hash_evidence` 来源说明。这样避免反复抄同一长提交字串；没有缩减任何输入内容或改用浮动 HEAD。

早已不在当前树的输入有自己的固定恢复提交，主要为 `60321451c058c6a51da58c37ae5ec6f2d1145f74`。第46批两份完整 JSON 刚在 `22ce15dfcc41b76c5bd9e5fb007c88e07537e160` 发表，本批按它们自己的该提交登记，未假称它们已存在于较早候选快照。原第43—46批恢复目录仍完整保留。

没有在所读小记录找到 whole SHA256 的三份候选是 shared-Schur、two-cell reweight 和 two-cell attribution。其 SHA256 明确为 null；固定 Git blob、路径、大小与提交仍完整。没有通过读取大正文补造摘要，也没有把未知值称为已经计算。

## 2. 精确退存对象

下表中的全部文件均位于课题的 `notes/`。完整40字 Git blob、所有已知64字 SHA256 和固定恢复提交在台账 `delete_entries` 内逐项给出。没有采用通配符或目录级删除。

| ID | notes 下的原完整文件名 | 字节 | 原实际退出码 |
| --- | --- | ---: | --- |
| ret47-01 | 2026-11-12-closure-real-head-source-enclosure.json | 199673 | 原小记录未给 wait4 |
| ret47-02 | 2026-11-12-closure-r51-split-float-r2.json | 206817 | 0 |
| ret47-03 | 2026-11-12-closure-outer-shared-schur-cut-r1.json | 184137 | 0 |
| ret47-04 | 2026-11-12-closure-two-cell-refined-source-reweight-r1.json | 134967 | 0 |
| ret47-05 | 2026-11-12-closure-two-cell-m4-source-attribution-r1.json | 130706 | 0 |
| ret47-06 | 2026-11-12-closure-strong-two-material-low-pb-12to13-low46-r1.json | 168666 | 0 |
| ret47-07 | 2026-11-12-root-r82-complete-low-cut-r1.json | 161232 | 0 |
| ret47-08 | 2026-11-13-root-hybrid46-cut-r1.json | 107932 | 2 |
| ret47-09 | 2026-11-13-closure-r100-spectral-r1-wide.json | 106860 | 0 |
| ret47-10 | 2026-11-12-tail-outer-cell0-piecewise-general-r1.json | 103107 | 1 |
| ret47-11 | 2026-11-12-tail-outer-cell0-piecewise-general-r2.json | 128984 | 0 |
| ret47-12 | 2026-11-12-tail-outer-cell0-components-357-r1.json | 123554 | 0 |

这些文件的名称不能自行决定其科学角色。本批逐项以原 producer 的读取、写出和退出逻辑，以及完整资源记录/证明，确认它们是可按原对象恢复的派生记录。后继消费者真实需要它们时仍须恢复对应 whole 文件；并未因其离开当前树而删除那条数学依赖。

R82 的46份逐模式压缩源包早已退存，本批不再将它们计入释放量，也不重复删除。它们仍是完整聚合的实际输入，不会被一个 aggregate 或 summary 代替。

## 3. R26：完整实源及坐标费用，未改写成 ODE 证书

`closure_real_head_source_enclosure.py` 的完整原命令保留 ready、source-ledger、response 三个输入及输出路径；默认 start=12、far=96、exact-through=23、precision=192，源积分的 relative/absolute bits 为100/160。原 ready 的全部物理参数和160行源数据保留，不能从本结果的显示数字反推或重建一个较小问题。

[R26](../results/R26-real-head-source-interval-and-port-coordinates.md) §9 保存真实64次严格标量积分及约30 MiB的观察说明，报告第12半径宽度小于 $2^{-96}$、深尾小于 $2^{-99}$。本批没有找到独立原 wait4 对象，所以退出码、精确 wall 和峰值字段留 null，而不从证明状态虚构 resource。

这个结果支付的是同源实参数、半径/权重/动量及二进实数转换包围。它没有支付实际 ODE/Green 迹或整个外半径问题，更没有给出闭面结论。后续 Green/linear-head 源导入的是同一完整函数定义；“导入函数”与“读取这个结果 JSON”在台账中明确区分。原输出按 Git 字节恢复，数学重算产生新的 elapsed 字节并不等同原记录。

## 4. R51：全641行浮点提议与独立严格验证分开

原 `closure_split_joint_float_proposal.py` 读取完整 low、split、density，使用 metric-target `31/32`、physical-domain-log2 `-30`、96次原提议迭代。正因子有427坐标，原完整非线性及导数系统仍有641行；low / near / rest / infinite 四块分别保留2—92、94—184、186—8190及8192以上全部频率责任。

提议实际 exit0，9.235195636749268 s，68,508 KiB。它只是独立 Arb verifier 的输入，不能因其 positive/dyadic 而直接成为证书。完整执行说明记录随后 all641 验证通过，但得到的严格上界约为0.968750000000005655，小于0.969，仍未达到请求的严格 $31/32$。原 `actual_target_met=false` 保持。

较早 target3/4 的失败提议也未被本批删除。原完整 verifier、精确输出及全部实际 source/input/parameter 对象都保留。本批不把成功的较宽上界改写成原更强目标成功，也不从旧充分界失败推断数学不可达。

## 5. R67/R79：保留有符号中心、全部核与非零远端

shared-Schur 的 producer 保留两输出模式2/4和全部46输入模式，原256位、40,960 KiB观察门与 cells11/10 不变。原 flow、signed-cut、true-cut、完整 ready 和 candidate11 都是独立 whole 输入。候选中心变化及补偿线性源仍在准确同一方程内。

该次真实 exit0、0.5306105613708496 s、29,896 KiB。它将 cut 部分收至证明中所列界，并保留完整 $2\times46$ DN 控制；范围仍只是 cut 贡献。不能把它当完整两胞残差、整个外逆/Schur 或闭面已通过。后续 linear-cancellation 源共享 flow/signed-cut/candidate 输入，所读 argv 并不读取这份 shared-Schur JSON；本批明确记录这条区别。

two-cell reweight 与 source attribution 都读取完整 adjoint functional。其全18核组与18原源组由 preserved22721 B functional 的 `kernel_groups` 一一绑定；cell10 的9份细化源由完整27426 B summary 绑定；原10,793源面板、两端输出和全部原20模式不删。节点/候选、源单位和 physical two-jets不变。完整 R63 非零 far 费用继续保留。

reweight 实际 exit0、34.597071170806885 s、17,588 KiB；attribution 实际 exit0、21.549806356430054 s、15,572 KiB。完整 R74 轴下比值改善不等于旧 R72 的 m4 轴通过；其旧比值约4.74590仍未付。归因记录的宽度是区间包围宽度，不是候选实际误差的下界。本批保留两种结论，并保留全部精确有符号源及原参数路径。

较大的完整 `config`、`source_identity`、`parent_constraints` 没有在新台账里反复展开成第二份科学输入，而是指向登记了 whole Git/SHA 的原完整小 manifest 的准确字段。原 manifest 全文保持，全部原参数仍在那里；新定位字段不是其替代品。

## 6. 完整46模 PB 边：保留真实源位置，未冒完整 strong 门

该包实际覆盖 cell12→13 的全部46正偶模式，原192位精度、1873真实源面板、5839个 PB 子片及 $AB\le2^{-20}$ 保持；没有给 `--only-mode`，也没有拿较早 m92 单模探测代替全窗口。全部原 q/strong、source/target panel、material 和 ready 的完整身份可恢复。

原执行 exit0、93.92280411720276 s、65,820 KiB。它保留逐面板真实浅列，径向 corr 上界的最坏模式仍为92，near 列相对旧界约0.109431134845。原数学分别使用径向材料系数 $5/2$，以及另一个材料的 $2/285$ 或 $2/9$，没有按总积分比例随意拆分旧核。

该源没有新做背景半径积分，但确实重新严格积分流的标量核，因此不能写成“没有新积分”。完整后继浮点诊断的全矩阵谱半径仍约61.0368852303；单边改善不等于 strong 全频联合收缩。完整 full641 proposal/verifier 和各自独立门继续保留。

本批另外读取原7539 B provider summary，取得12个完整浅胞 provider 和6个完整 linear-column 组的原 whole SHA。它们均逐项进入登记，不读取任何压缩体。两份实际PB输入 cell012/cell013也使用这些真实原摘要，未凭文件名推定相等。

## 7. R82：全部9798源行和真实46个子执行继续可恢复

R82 的完整 producer、串行 replay、实际 batch state、194项 stable manifest 记录和 proof 均保留。46正偶模式乘213真实源胞元，共9798行，六个完整 real-column 组和12个浅源 provider都必须按原 whole 文件恢复。每个模式的原完整计划、原资源和 gzip 主包身份均已在登记中保存；46模式集合不是抽样。

最初双模式尝试在原40 MiB观察条件下 exit1，峰41,100 KiB；它的失败记录未改变。之后同源逐模式真实成功，46个子任务累计76.0825343132019 s，最大子任务峰38,192 KiB。最终 Fraction aggregate 真实 exit0，1.8443641662597656 s，24,584 KiB，十一门全真。

聚合保留 R74 同一个20复参数盒、$257/256$ 包络、$4225/4096$ 源乘数、Cauchy半径 $3/4$ 及一二阶乘数4/64。整个低块的辅助 far 和 full-head-minus-auxiliary质量各加一次。完整低块上界小于 $6.884236844\times10^{-49}$，一阶上界小于 $2.753694738\times10^{-48}$；原全部高频与完整 mean 高度规范继续保留。

这些是实际内头 cut/DN 接口。完整外 Green/Schur、真正未知外场和闭面问题没有因此完成。R83 后继仍可读取恢复后的完整 aggregate；本批没有删除该后继任何参数。

## 8. R100 projected cut 的 exit2 与 R101 wide-tail 的 exit0并列保存

hybrid46 consumer 使用完整 geometry、budget、R94/R100 ledger、其准确 source 和完整 head/spectral primary。原混合范数是六个选定 $\ell^\infty$ 坐标加40个加权 $\ell^1$ 坐标；后40个要作和，不能换成最大值。十个原 $T$ 半径1/64、1/32、3/64、1/16、3/32、1/8、3/16、1/4、3/8、1/2全部保留。完整 mean、逆分母、非零 far 和原 Cauchy 域不减。

该次真实退出 **2**，1.69808030128479 s，16,148 KiB。源先写出完整结果，然后因 `all_gates=false` 返回2。新台账不会将其列为成功收缩，也不会凭退出码猜哪个未读的具体 scenario/子门失败。整个原结果按字节可恢复，原 head bottleneck 后继仍独立保存。

wide-tail supplement 是另一份真实 exit0 结果，2.9102556705474854 s、47,196 KiB；原 Node 48 MiB old-space与4 MiB semi-space参数全保。它严格消费同一个原完整 spectral primary，保留全部230个94—552模式及57个554—5758块，所有正尾和完整 mean域仍在。原 R101 saved-summary consumer 已准确核其14个门、两个来源和 whole primary关系。

该额外解析宽只适用于已经知道的有限46中心及其相位轨道，不能据此给真正未知的 middle/high 场换目标或免费扩大解域。primary已经在第46批按 whole 保存，head在第45批；本批明确它们的恢复先后与原绝对路径别名，不将新生成字节冒旧主包。

## 9. R66的两份部分结果与后续完整候选不能混淆

第一次 segment-domain 执行实际 exit1，15.048738241195679 s，31,848 KiB，已经支付前七段、1732连续面板，但原端点分支尚未闭合。这个失败包是后续 `--resume` 的真实输入，不能以较晚完整结果改写它。

endpoint-union 后继完整钉住原 source SHA `836074abfdc5758822633a591d5ed4eb0cdf1aae6d018f486308f20c2330f32f`，只实行原四处明确替换。真实 exit0，3.5941967964172363 s、30,744 KiB；前八段2164面板支付，但原第九段的 coarse mean 仍未付。随后单独的 physical-$r$ 最后一段以16面板完成，形成 R66 的2180面板覆盖。后继成功不使前两个包自动变成完整候选证书。

原完整 shared-node 文件虽然早已移出当前树，仍按真实406599 B Git对象恢复，SHA为 `1ac05db87c40fe4421eb6067d81448a466548060c58a2dfc0c4ea51bd7ed7582`。原 node producer 的全部 argv、$\tau=1/64$、inverse-degree=8、原 whole strong-M20 response、radius ledger和ready在完整10305 B执行 manifest 内保存。没有从显示坐标重造十个节点，也没有将原完整865行场缩成节点表。

本批保留原9份正矩源包、全部20模式、物理两 jet及 complete mean公式。之后的 `tail_outer_last_piece_physical_radius.py` 仍真正读取 restored r2 前缀，再在自己的输入/源责任下完成最后一段。

## 10. 九段components357：7378连续面板是候选证据

组合器只用 stdlib 精确 dyadic 比较，完整读取原 base、shared nodes、physical last-piece，以及 segments3/5/7 的全部压缩主包。它选择每一原段的一份完整组件，不把区间中点、不同 bubble 或不同源坐标字段拼为新候选。

九段原面板数依次为1、292、16、4211、16、1124、16、1686、16，共7378。真实 exit0、1.262916088104248 s、17,720 KiB，原六个共同身份/覆盖/物理单位门全真。完整物理 Darboux 上界4.023376336位于segment5，非均值二阶源与实际高度二导上界分别33.905255681与33.772181675，位于segment7。不同单位的最大值不能混用。

这是同一真实度量下的兼容高度候选。Darboux缺陷未为零；高度二导不是已证精确曲面的主曲率，完整 outer inverse/Schur、谱/图形/reach仍未因此支付。

后续 centered-interval/finite-$J$ 说明也保留其实施纠正：旧 `delta**j` 在该绑定下会返回非有限区间，原 intersection 回落旧包围；既有有限界仍有效，但最初并未支付所声称的更紧 centered-polynomial 界。本批不删除该纠正、不把原旧组件换成修后数据，也不把较晚0.760858上界倒填为当前候选包的原结果。

## 11. 精确恢复与已知消费者

默认恢复从仓库根执行如下形式；这些是原对象恢复说明，本次未执行：

```sh
git fetch --filter=blob:none --depth=1 origin 0089b00e4e587b0716a2e94de35d06fe7bf901eb
git show FIXED_COMMIT:topics/visible-flex-larger-amplitude/RELATIVE_PATH > RESTORE_DESTINATION
```

对每个输入应先从登记的 `r` 解析真实固定提交。不要把全部输入强套候选提交，亦不要拿当前 HEAD 代替历史来源。恢复目录及父目录由实际使用方准备；原 gzip按压缩字节保存，不解码后重压。任何原绝对 source/data 路径必须对应登记的相同 whole 文件，台账已保存完整 argv 与其路径映射。

恢复分支如下：

1. R51先恢复三输入与完整提议，再运行其原完整 verifier；不能跳过 verifier。
2. Two-cell先恢复 truecut、flow/signed-cut/candidate、全部18核及18源、9细化源，才有完整 functional consumer。
3. R82恢复六列组、12 provider及全46 source primary/plan/resource，再恢复聚合，供 R83读取；aggregate不代替模式源。
4. R100恢复原 head与spectral primary，随后恢复 wide或failed-cut；保留原成功与失败语义。
5. 外胞先恢复正矩组/完整node，再恢复原 r1→r2→独立physical last-piece、三个完整substage与nine-segment composition，原同场身份和单位必须保持。

这里没有新增审核、扫描或重跑前门。若只需恢复旧字节，Git whole对象即可；若未来主动执行旧科学 consumer，其原程序本就要求完整source/输入 SHA与数学门，责任没有被台账删掉。重执行可能改变 elapsed、资源与输出序列化字节，不能称为原结果逐字再现。

当前 warm依赖的既有067b/561308/bee5来源闭合保存在第34批完整记录。本批直接保留那份全文，不以“文件名像输出”断言全仓库无消费者，也没有做新的全局依赖扫描。所有现行 Fejér inputs、参考、科学源、完整checkpoint/typed history、连续费用、N/M/J各完整族及运行队列不在删除范围。

## 12. 实施边界与容量

root只需对十二项做当前树的准确 path/blob/bytes匹配，然后按普通提交保留本三完整件并退存这十二个对象。若某一对象已变，保留那一对象并如实调整实际容量；不要读其大正文来让它勉强符合旧表。除精确列出的十二项以外，不删除任一源或其他raw。

本批三件共 215602 B，净释放 1541033 B。ret43—46已退项、46份R82 gzip，以及未闭 source mismatch 的 ports/Nelder都未加入本批。R167/binary-C2跨topic源根关系也没有用近似名义纳入。课题得到的空间可留给真实自然返回及已经完整准备的费用包，容量整理本身不计作数学完成。

本说明与两个完整JSON均由纯文本和元数据构造，远端未引用 blob保护后交root。没有修改refs、队列、任何数学source或已有数值参数。
