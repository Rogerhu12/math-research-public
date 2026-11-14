# R148 后验域上的同一 R100 场：参数交域、全部 lift 与旧正核限制

作者：/root（GPT-6 Astra Pro，AI 辅助），2026-11-13。

## 结论及精确适用域

R143 已给原完整 cut 映射在复凸体 K 内的唯一固定点 a*。K 的六个 S 坐标半径为 3/8，40 个 T 坐标同时满足原各轴帽 2b_m 与总质量 1/64。R148 的完整坐标后验满足 |a*_m|≤B_m，其中 B_m 包括投影全非线性像及 R141 保留的完整非 low 修正。R148 只在 S≤1、T_l1≤1/32 上使用；K 是该域的子域。

定义新复域 P：保留 S 半径 3/8 与 T 总质量 1/64，逐 T 坐标帽取 min(2b_m, outward(B_m))。P 包含同一个 a*，又包含于 K 和原 expanded 域。这里没有重新定义参数轴、度量、复条带、Cs、Lambda 或 e=F−Cs−Lambda；只是限制已经存在的同一个全频场。S 的 Cs 帽仍保守使用原完整单位域帽。

## 已实际完成的计算

1. 全部 213 胞元、46 原 unit lift 列，按各坐标帽与一个共同 T 质量同时做精确贪心支持计算。每模帽为 unit_m min(cap_m,1/64)，共同帽使用按 unit 降序的同一质量预算，不逐模重复使用全部质量。正远端预算也按相同约束计算。
2. 全部 213×46 的 Cs+Lambda 输入重算，逐个与原完整帽相交。Cs 本身、原 V′=(257/256)V、共同连续 tau 和原46轴保持一致。没有进行 ODE、Green 核积分或新固定点求解。
3. 另以实际 Fraction 检查新域包含于旧 expanded 域、新 Cs/Lambda/总模帽及共同帽逐项不增，并绑定旧 DQ、alternate4 window、alternate4 low 以及该 low 真正使用的 alternate3 window 的原 SHA。旧窗口、低模、无限尾和 far 的数值及来源均未改写。

Lambda：828 门，owned exit 0，5.2546 秒，40088 KiB。新 m92 的 T 帽为 3.591159190141312e−14；cell12 Lambda92≤3.803096287431612e−46，共同 Lambda≤9.266188826422121e−34。

Modal：10450 门，owned exit 0，6.3992 秒，72064 KiB。主 SHA：0a76756d411a350836ab27ca274142df0306628293401763453842130fa6f77c。

Parent bridge：31397 门，owned exit 0，6.1034 秒，159096 KiB。主 SHA：97f3a6fd9c59c4d23dead6e83a961411bb0ca1d187343ce598f0b8d2abeefd24。

## 为何可以复用旧 DQ 与 e 帽

旧 DQ 系数由中心 Fourier 正帽的正线性表达式、最大值及共同质量支持给出，因而对全部中心帽单调。新域中仍是原 Cs(a)+Lambda(d)，且其每个模和共同帽均不大于旧帽；旧 DQ 表继续包住该限制域上的同一个导数。旧 e/low/window 界也因参数域包含关系继续有效。新消费者必须显式引用本 bridge，并保留旧输入身份；不能把旧核改名成在新模态上重新计算的核。

旧 DQ 全主包遵原 Rule11 仅在 scratch 保存；其已提交 manifest 保留 producer、完整 argv、原资源、独审、原主 SHA 与 canonical 数学行 SHA。durable-inputs 对这一个输入明确给出重建入口，不假装旧主包已被 Git 跟踪，也不在本次重复该成功计算。

这一步单独没有给出新的完整 true-beta 数值。新的完整源、641 分量、13 窗和 true-beta 后验由后续实际消费者继续支付。完整 mean、逆级数余项、所有无限频率和正 far 不得省略。它也不扩展外0..9，不构造闭面或全t族。
