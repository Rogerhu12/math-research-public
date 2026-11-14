# R136：原几何下真正单模94、96的完整外传播核

作者：/root（GPT-6 Astra Pro，AI辅助），2026-11-13。状态：已证明下述线性正比较算子；不宣称新的完整非线性闭合。

## 原输入与真正单模

原185窗口中的首窗是94..96。重复使用这个共同窗不能给出两条独立锐化的单模核。本次用完全相同的原生产器、10793个原系数叶、18个原来源段和256bit Arb精度，实际指定94:94与96:96重放正比较代数。未重新求解ODE、未重新计算径向源积分、未更换g或条带。每窗保留25个原目标/来源块、1804个frame jump、两个独立初始分量以及V²、V、1三种来源材料。

原生产器SHA为79736efcc18d3a97f5db3e273b7914817142d3f9531969f736a276c14bb4f2ff。输入叶的SHA为dadf463497d12f85e5fb3046d46eb6d2d2b2fa26ca36d3c19fbd061c4ea1fad1，摘要SHA为7e9821bf97dc0ac6955cb1c010ba48039c13f01dc5598378b31317eaab113f87。R137的实际门另外逐项核对新旧metadata的原输入hash集合、生产器SHA与same_fixed_strip全部相同。因此这里没有把另一个几何问题的算子转入原场。

## 原共同strip与强范数转换

令Δ是原balanced-head包中严格正的头到输出条带差，Bcut为其正下界；ε_i为原共同条带第i块的extra_start。两个初始canonical分量必须分别保留。实际head系数使用

\[
 h_{m,i}=\max\left\{(c_{00}+c_{10})/B_{cut},\ c_{01}+c_{11}\right\}
             \exp[-m(\Delta+\varepsilon_i)].
\]

上述列和先在原包规范中转为强(P+κ)/V帽，再用原已证明的正指数上界付一次条带损失。对来源j<i，三材料分别再乘exp[-m max(0,extra_start_i-extra_end_j)]；同块来源不借用不存在的整块条带余量。每个系数与原94..96共同窗的同目标/同材料有效界取较小值。两者均独立覆盖同一算子，因此交取合法。

全部25个目标块的因果来源0..i和三种材料都保留。单模帽、旧共同94..96窗帽、185窗与共享中频总质量要同时使用；不能把共享质量重复分配给每个单模，亦不能把这些算子核称为已支付完整非线性源。

## 实际结论

原叶比较实际formal exit=0，9.592657s，30412KiB。共同strip转换714门全真，formal exit=0，0.550300s，39432KiB；正式核主SHA321b578cbffa909b4c95cb5879ef312b2535fa1bbeaa88fcae147d3785e799b7。

第23块真94、96的head系数与旧94..96父窗之比分别为0.7457190118622549、0.7736583994257443。改进真实但只有约25%和23%；没有数量级收益的主张。仍需真实各窗head输入、完整低中高反馈、均值/逆/far源及原46条cut。

## 复现及归档

归档原metadata、完整新两窗jsonl.gz、正式三材料核、两份资源与两份输入pins。先按原资源命令运行已归档hybrid-middle-windows-v2.py并指定两个singleton；再将其真实输出路径/SHA放入kernel输入manifest。第二步运行computations/root_outer_singleton94_96_kernels.py；同目录r127_window_helpers.py应是已归档notes/2026-11-13-exact-resume-r127-window-bootstrap-v1.py的逐bit副本，SHAf2f62cf05f729606f2e6fb510c4539519d86f1bc55e7a648844226e9487d0956。资源记录包含精确argv与正式退出码。复现使用新输出路径，不覆盖原产物。
