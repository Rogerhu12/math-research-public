# R137：受限真实head下当前正cut预算的有限代入障碍

作者：/root（GPT-6 Astra Pro，AI辅助），2026-11-13。状态：已证明一个指定正上界算法不足以支付R133细轴；这不是PDE解的下界，也不是不存在性结论。

## 实际输入与作用域

保持R130的原完整外场、原低频中心C、25来源块和原m92 cut核。内侧输入使用R134 expanded域（S半径3/4、T的l1半径1/32、每条T轴为R133投影像的4倍）下真实low46/13窗四轮交替的正式结果，主SHA8259ea4d96e66ec2b479f7c2dce959034c48ab29d1da01a54c0dc6fbf008c797。完整mean、inverse和独立far均保留。该输入与working域不同，不能把它的上界算法障碍说成working域真实残差的下界。

94已作为单独窗口。外侧使用R136实际真94核，不再借94..96共同窗的最坏模；旧共同窗、完整中频总质量帽仍同时保留。实际核对R134的全部T轴与头包域完全相等，R133原轴记录、原617规范和head条带全相同。新旧外核metadata的原叶输入hash、生产器SHA、固定条带及25块分割亦全部相等。

## 指定正迭代的下界

记第j块原有限中频总质量seed为r0_j，原94..96窗口seed为v0_j；新三带head帽为H_b，真正94头为H94。令

\[
 A_j=\sum_b G_{jb}H_b+c_j,\qquad
 r^*_j=\min(r0_j,A_j),\qquad
 v^*_j=\min(v0_j,r^*_j,h_{94,j}H94).
\]

其中c_j是原完整固定中心源贡献；所有项非负。保持这些常量不变的原迭代只会以min(旧帽, 常量+非负项)更新帽。归纳可见，每一步r帽至少r*，每一步94窗帽至少v*：从seed成立，取最小的每个候选项都不小于对应下界。这个论证针对所记录正上界的算术算法，与实际PDE场的相位或大小无关。

在原低×中源的m92←94位置保留真实正系数L_j和原V² cut核K_j。正预算中仅这一项即至少

\[
 B^*=\sum_{j=0}^{24}K_j L_j v^*_j.
\]

为证明此算法预算下界，可把其它非负源贡献置零；这不允许在完整自映证明中删除那些来源。94单独质量v*满足上述原共享帽，但不声称存在达到这个质量的真实PDE解。

## 实际数值与含义

准确有理算术加向下192bit记录给出

\[
 B^*>9.0571011589\times10^{-9},\qquad
 a_{92}=1.0761170616914837\times10^{-13},\qquad
 B^*/a_{92}>84164.64603.
\]

因此继续原样增加有限代入轮数不能让这套预算支付R133第92条细轴。它指明要改进真实head/源传播或有效算子，而不是再运行相同8轮大任务。

进一步把A_j中所有head带项删去，只保留固定中心c_j，得到较弱算法下界2.195031179435605e-14，小于a92。这项检查说明：仅由这里的固定中心，没有得出细轴永远失败的障碍。新的逐panel canonical源与更深入口传播仍可能改变结论；新头输入应使用新文件/新实际运行，不能覆盖本次失败预算。

## 实际运行、失败与复现

r1在读取R133的upper={mantissa,binary_exponent}记录时，用了只认识num/den或dyadic的旧helper，正式exit=1，1.133425s/70224KiB；没有输出证书。失败源及资源保留。r2仅显式按原mantissa和binary_exponent准确读取，保留原radius记录，不改输入域、核、预算或门槛。

r2正式exit=0，1.702321s/70060KiB，104门全部真；source f7d889455bcc7f6c3811ffe3505158d07f04197bf5222ce6842bc59cb2c04485，primary d3337f71241be7a1f4a1f4efe1854052d43152fd42dcbc0fe7f13a35259fa99f。归档主包、完整input pins、原失败source/resource及正式resource。真实四轮head耐久名为notes/2026-11-13-exact-resume-inner-restricted-alternate4-window13.json.gz及同前缀-resource.json，后者SHA18fdac70d25dd81bef2fcc0aa5ac9fa9a77e1c799153d28e40eabdeb94fa2984。

按资源命令在冻结输入路径运行computations/root_restricted_mode94_positive_budget_floor.py；同目录需原root_window_frequency_cut_bootstrap.py（SHAe854ddc93e01086922b85df02a4a6acecc1e29077b26d319b0af811d0adf5e79）。严格核验所有输入hash，换新out路径。报告为指定预算失败，不记为46cut成功、非线性自映或闭面完成。
