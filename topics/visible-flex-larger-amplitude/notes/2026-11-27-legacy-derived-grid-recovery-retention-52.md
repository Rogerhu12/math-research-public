# 第 52 批：旧完整网格、恢复收据及条件预算的可逆退存

2026-11-27。来源整理；本说明不是新的科学计算、数值验收或连续几何证书。作者为 `/root/construction`（AI-assisted）。本稿仅保护完整未引用 Git blobs；是否以及何时实施，由根代理在最新树上决定。

## 1. 精确范围

本批只选择 **14 个已生成的旧记录，共 1,632,095 字节**：九张旧有限观察网格、一份五控制回归结果、两份工具会话中断恢复收据、一份硬链接维护报告，以及一份带明确假设的 carrier 曲率预算。全部原科学源码、原参数、完整计划、原 owned resource、主输入、证明和当前 Fejér 科学文件均保留。

开始时直接取得的当前提交为 `837c4fdea41e621264b3cd9dd658aca1abaf0847`。其课题树 `30aab0137711db07129c97c42b84d1b2ea4b4126` 有 12,005 条记录且未截断。历史提交 `60321451c058c6a51da58c37ae5ec6f2d1145f74` 的课题树 `22b07f5196012810bab15ff242ae83e227076420` 有 10,190 条记录且未截断。下列每项在两棵树中均有**相同完整路径、Git blob 和字节数**。完整 SHA-256 均来自原小 manifest 或原完整计划；没有为了补摘要读取候选正文。

| 序号 | 相对于 notes 的完整文件名 | 字节 | Git blob 前缀 |
|---:|---|---:|---|
| 1 | `2026-11-13-geometry-six-control-preparation-q096-identity-grid.json` | 80511 | `b4a4145046b4` |
| 2 | `2026-11-13-strong-current-stale-fine-geometry-preparation-r1-grid.json` | 92799 | `eca635fbddc8` |
| 3 | `2026-11-13-strong-initial-laws-geometry-q106-grid.json` | 81513 | `c0eb9e222131` |
| 4 | `2026-11-13-strong-native32-stale-fullmean-geometry-preparation-r1-grid.json` | 93798 | `0f4fb3534c3c` |
| 5 | `2026-11-13-strong-q106-secant-fullmean-geometry-grid.json` | 81238 | `5850a8ffa77a` |
| 6 | `2026-11-13-strong-q122-complete-mean-geometry-baseline-r1-grid.json` | 89815 | `d7d63c0dee17` |
| 7 | `2026-11-13-strong-q122-fine-coarse-warm-geometry-preparation-r1-grid.json` | 91808 | `982a9f4f65ef` |
| 8 | `2026-11-13-strong-q126-current-m32-geometry-baseline-r1-grid.json` | 90611 | `552832f3d1d4` |
| 9 | `2026-11-13-strong-secant-fullmean-geometry-prepare-baseline-grid.json` | 80779 | `2faad4aed414` |
| 10 | `2026-11-13-geometry-six-control-preparation-five-regression-r1.json` | 48329 | `621debb9cb0e` |
| 11 | `2026-11-13-strong-current-nine-geometry-session-recovery-r2-receipt.json` | 147007 | `a53d23da194b` |
| 12 | `2026-11-13-strong-current-nine-geometry-session-recovery-r3-receipt.json` | 216444 | `fbc09f453e43` |
| 13 | `2026-11-13-strong-old-frozen-notes-dedup-r1.json` | 228529 | `3825647f1f0e` |
| 14 | `2026-11-13-geometry-carrier-curvature-r1.json` | 208914 | `611c8da57e17` |

完整 40 位 Git blob、64 位 SHA-256、原证据身份、恢复提交和可实施删除项在 [完整 provenance](../computations/legacy-derived-grid-recovery-retention-52-provenance.json)；本表的短前缀只便于阅读，不是实施标识。

## 2. 完整材料在哪里

本批有两个完整 JSON 文件，均低于 100,000 字节：

- [完整来源及输入恢复索引](../computations/legacy-derived-grid-recovery-retention-52-source-input-registry.json)：82906 字节，SHA-256 `266f12878e36b32948382bf8c978a0109f8680e0b8d74b839318ede4860215e6`，Git blob `ca297a892faf11d38bf1218426cd038ef401b0b8`。
- [完整 provenance 与删除项](../computations/legacy-derived-grid-recovery-retention-52-provenance.json)：58506 字节，SHA-256 `150e80909f4bdafd6c178930268adfe95ef5d47660f278e5b28f52fe97c3b237`，Git blob `10b3d93b66a11a4c67b5d87edc7761a68064b9c6`。

索引精确引用 52 份已保存的原计划、manifest、owned resource、执行账本和说明，并列出本批取回并核实整字身份的 43 份完整源码。142 组不同的原 source/input SHA 逐一对应原路径、证据记录和可用的固定 Git 恢复位置。重复引用以列名明确的表格表达；原文件的任何参数、命令、字段或结果没有被表格替换。

既刊 retention51 的完整四卷仍是共享上游：54 份原源码、71 份小记录、187 条原输入恢复记录、五份完整参数计划、18 个原 owned-resource/argv 对象，以及六个完整历史来源合同。这里按它们的完整路径、字节、SHA-256 和 Git blob 引用，不复制或重写那些原配置。retention44 的完整索引补充原 recovered-radius 身份。既刊退存项不在本次删除列表。

## 3. 九张网格是怎样产生和消费的

六控制和 initial-laws 规划器首先读取真正接受的主包、原 raw 节点、固定材料图及相应 audit。它们保留全部原 raw 节点，加入原图的所有锚、每个物理区间的细分点、完整原观察规则和按来源明确区分的曲率见证。新网格由原源码实际写出；不是本次为节省体积重新采样。其完整下游命令仍在对应计划中，包括所有模式、目标 core、profile、角向和径向规则、完整 mean、批大小及 RSS 参数。

原 current-stale 构造保留旧比较网格，同时加入实际当前 raw 和当前 quintic 见证。它没有把旧见证当成当前极值，也没有把不同的原材料图解释成同一个物理点。native32 后继进一步使用真正的完整 M32 增量构造，保全部 97 个状态通道与 32 个核心方向。fine/coarse 构造的旧网格嵌入关系、真实完整 fine point 和全部粗增量来源也继续严格保留。

这些网格随后是历史 full-field、minimax、secant 以及完整 reader 的**真实输入**。因此，本说明没有声称它们“从未被消费”或“没有用途”。旧消费者再次运行时，必须恢复表中精确原文件；同样的网格点数、新近重采样或近似相同的浮点值均不能替代原完整字。

q126 网格还进入真正 current-M32 的十九场计划。原 `archive_current_m32_nineteen_geometry_fields.py` 完整体明确保存原 grid、完整计划、全部 field resource/reader，并递归保留中断恢复链中的原 plan 和 receipt。对应 315,055 字节完整 gzip recipe 的身份是：

- 路径：`notes/2026-11-13-strong-q126-current-nine-complete19-geometry-r1-reconstruction.json.gz`；
- SHA-256：`4d291feb9296740b24402e164e949cf120ccc4993764128edb595a77cd7a5e47`；
- Git blob：`860d83ecd81997bb0e5ce97f9ed54e26f234f23f`；
- 固定恢复提交：`60321451c058c6a51da58c37ae5ec6f2d1145f74`。

本批读了原小 manifest 和完整 archive 源码，**没有打开或解压该 gzip**。恢复所选输出的首选路径仍是直接取得其独立 Git blob；无需先重做任何科学。

## 4. 原执行结论保留到哪一步

五控制回归确实以 exit 0 完成，消费了原完整十一场与全部 6,495,360 条有限不等式；原预测字典除控制数声明外与旧五控制计算完全一致。这不代表第六个方向已计算，也不代表新的非线性点已接受。其完整报告仍由固定 Git 恢复，原 combined-regression 计划确实会读取它。

q106 原 complete-mean baseline 真正完成，其场形状是 `[3404,768,3]`，sampled max curvature 为 8.25715453947172，twice max norm 为 3.9106138120984015。原 archive 另明确 scale-2 已执行而 scale-1 仅准备。不同的 initial-laws baseline 计划仍保持 `prepared_only=true`、`executed=false`；本批没有借另一份 baseline 的 exit 0 给它补成功。

q122 baseline 的原退出码为 0，保全部 28 模式、2,587 个原节点、3,764 × 768 网格和完整 1,360 点 mean。原记录给出 S=3.9043958298236814、quintic sampled curvature 8.409022709039338 及 gap/S=0.06216423007951198。原 metric/flow 缺口仍未付。

q126 baseline 原退出码也为 0，保全部 32 模式、2,590 个原节点、3,767 × 768 网格和完整 1,552 点 mean。原记录给出 S=3.9779596080918149、quintic sampled curvature 8.345514341083943、gap/S=0.063006701324432049。原实际残差和完整有限域结论没有提升为连续 reach、闭面直径或全相位振幅证书。

current-stale、native32-stale 与 fine/coarse 的记录明确是实际准备调用；其退出 0 不能改写为生成了新完整场或通过了新的 BVP。fine/coarse 原无效 control-name 调用 exit 1 的完整 resource 保留。secant 准备原先使用错误 plan 文件名而 exit 1 的 resource 同样保留，随后真正正确的 prepare-only exit 0 也单列。没有把先前缺失的方向、未保存的 half-vector 或未知后续场填成零。

## 5. 两份中断恢复收据

原恢复程序先核原完整 M32 十九场计划和全部 source/input SHA，再对每个已有真正 owned exit-0 结果调用 `inspect_complete`，重读其完整 field manifest 和每个 chunk。只有未完成且已有部分文件的情况才更换输出前缀，并逐 token 证明反向替换恢复原命令。已完成的完整场不重算，尚未启动的命令不改。

r2 记录的不可用工具会话是 24782 和 93724；八个完整场复用，十一场未完成。r3 是 56849 和 31479；十四场复用，五场未完成。原 heartbeat 没有最终 owned wait4 resource 的状态继续如实保留。`Unknown process id` **不是子进程退出码、终止信号或科学失败原因**。

两份完整 recovery plan 仍在当前树，分别有 83,837 和 84,089 字节，保全部十九个原命令和每个数学参数。receipt 中逐项旧部分文件身份、全部输出 token 编辑和当时观测时间仍由精确原 Git blob 全字恢复；不通过现在的文件系统状态再“生成”一份冒原字的收据。后来完整十九场归档属于有独立来源的后续事实，不能倒填中断时尚未完成的结果。

## 6. 维护报告与条件曲率报告

硬链接维护程序只处理原明确允许的旧 q096/q098/q106/q122 成功 gzip 副本，原 q126/A、当前九控制数据、源码、非 gzip 和未完成 producer 文件均排除。原 owned exit 0、106 个文件、227,292,609 字节及完整命令/时间/RSS 都保留。这是原维护行为的记录，不是当前 scratch 状态或数学结论。本批只退它的生成报告，**不删除它曾处理的任何科学副本**。

carrier 曲率 consumer 的完整 15,114 字节源码和原 relocated 路径合同均保。它读取全部 111 个 part-0 叶、完整 41 个 J 模式（0 到 80）、mean/Hrr、真实 background 和原 R102 其余七部分，保全部原公式与来源检查。原 5,118 字节 `950f-tail-subdivision.mjs` 已从固定 603214 提交取回，整字 SHA-256 为 `e44317579d483147aa7fe73b086aba059695aa0f675b831c178902a2c0cb62e6`，不是用别的同名版本代替。

原重新定位 consumer 实际 exit 0；九个 structural gates 与 111 个 conditional gates 通过。原形式 carrier 曲率 8.143011140160913403、defect 上界低于 0.000117729748874029，最终报告的 seg7 上界 8.165888306896059 < 33/4，仍然以**同一候选的准确 Darboux 场和全频误差不超过 1/512**为条件。准确误差、存在性、全域 reach、握持及时间问题没有因此付清。旧 pending 文件未被找回这一事实也保留，不能把本次路径恢复解释为原 pending 执行成功。

## 7. 输入恢复与已知缺口

每份大输入只检查 Git 树元数据和已有小来源，不读 raw 或二进制正文。原完整计划中的 source/input map、完整 accepted/raw/tail/config/port 记录与所有参数保持原字。对于已退的依赖，索引给出固定历史提交、完整路径、Git blob、字节数以及已知 whole SHA。

九个旧 runner-only numpy gzip payload 的**原路径和 SHA-256**仍在原计划和本索引，当前没有为它们找到独立 Git blob，故明确写未重新取回；没有猜它们存在、为空，或可以由计数恢复。这些原科学 payload 不在删除列表。所选十四个生成输出的完整 Git 字节恢复不依赖这些 payload 的重新计算。

原 4,752 字节 `78718-prefix-tail-geometric-client.py` 缺失边界仍完整沿 retention51 保留。8,274 字节同名 mirror 不是它。原 11,445 字节 core-tail-proxy 的源码版本区别也原样保留。因而本文不宣称“任意旧科学都已能无条件逐字重算”，只提供可验证的旧输出恢复和原已知输入/源的完整身份。

## 8. 当前 Fejér 分支与历史消费者

本批直接全文读回当前完整科学 source registry `fixed-fejer-meridian-producer-binding-repair-complete-delivery.json`，52,830 字节、SHA-256 `970b8f8bbb141fc7f1c4e5e42d6048497f0de58731e65918f3c4e4cf6aff008a`。其中没有十四个候选的完整路径或 basename。此结论只限该真实完整 registry，不冒称搜索了所有未来或未知消费者。

另取回当前 39,375 字节 `fixed_fejer_r690_reference_inputs.py`，整字 SHA-256 `89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60`。它的固定输入依赖是原 accepted099 的准确 scalar projection、全固定数学源和确定性 Fejér recipe，而不是本批旧有限网格；这十四个路径及 basename 均未出现在该完整 source 中。当前新目标、标量、节点、参考、全部自由变量、137 个来源角色、typed/history、运行 18/19 的命令和实际返回均不在本批变更范围。

历史消费者仍可能需要这些旧文件；这已逐族写入 provenance，而没有因它们不在当前 registry 就把旧消费责任删除。

## 9. 实施与恢复

根代理实施前只需对最新 HEAD 中每个拟删路径作其正常的 blob/size 相等检查；不符的一项保留，不删除其他路径作为替代。实施授权不包含删除 source、proof、参数、输入、port、Nelder 或当前材料。

每项可直接恢复，例如：

```bash
git show 837c4fdea41e621264b3cd9dd658aca1abaf0847:topics/visible-flex-larger-amplitude/notes/2026-11-13-strong-q126-current-m32-geometry-baseline-r1-grid.json > recovered-original-grid.json
```

然后使用完整 ledger 的字节、SHA-256 与 Git blob 核对。所有十四项还在 603214 历史提交有相同完整 blob。原绝对 runner 路径可在获准的隔离 runner 中重建，但不能把更换数学输入或近似重采样称为路径恢复。

本批没有读取十四个候选正文，没有解压大 gzip，没有本地执行科学、AST、编译、测试算例或数值重放。这里也不增加一个必须先重新计算旧科学才能开展当前工作的门槛。未来如需科学重算，须在获准 runner 使用其真正完整原输入与源码；新返回不自动获得旧报告的字节身份。本批提供的立即可用恢复机制是固定 Git 对象。

