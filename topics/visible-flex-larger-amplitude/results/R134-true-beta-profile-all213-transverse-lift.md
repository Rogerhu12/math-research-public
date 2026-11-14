# R134：R133逐轴域上的全部213-cell真实横向提升

作者：/root（GPT-6 Astra Pro，AI 辅助），2026-11-13。状态：已证明参数输入界；尚不构成完整 head 或 cut 闭合。

使用原213×46真实 Λ 列，保持 R100 轴、连续strip、V-prime单位及所有原列不变。只对参数域取子集。working域取 S l∞半径1/2、T l1准确半径1/36及各轴cap=2b_m；expanded域取3/4、1/32及cap=4b_m，其中 b_m 为R133完整投影映射界。第一批六个 S 参数由原 C_S 处理，不重复放进 Λ。

若 U_jm 是原cell j的单位列，则逐轴上界 U_jm min(cap_m,r_T)。共同质量不是把每个单轴的最坏值直接相加，而是在0≤x_m≤cap_m、Σx_m≤r_T上精确最大化 ΣU_jm x_m；按 U_jm 降序填充的 greedy support 给该线性规划准确值，再向上序列化。两域每个cell逐模/共同上界均核小于原1/32域。准确1/36用 numerator/denominator输入，没有将显示向上数误作半径。

实际863门全真，formal exit=0，3.455213s，37672KiB。cell12的第92模working Λ≤1.139625559734559e-45，expanded≤2.279251119469117e-45；working共同Λ≤1.731367830442242e-33。共同量没有随第92轴同倍下降，所以不能把细轴改善率乘到完整共同源上。

原 far 单位列同样在该同时受限域上做独立support；不乘 S 收缩率。C_S可保留原unit S的界，真实 e 和完整辅助 far仍另外付。这个包只是下一完整source/e/head计算的实际输入，未宣称新受限域完整固定点、非低cut自映、闭面或新g结论。

源41a7d7e596ffb158e0884f7262eed7be5a8e9771e42aa66186dfeea5c28bb32a；主087a68ddc9932825ec0a56e765095e507249374db7e7ce482a4bdf890055c5c7。复现：computations/root_true_beta_profile_transverse_lift.py --inputs <恢复manifest> --out <新json.gz>，使用原helper及strong_resource_run.py。manifest记录原提升、R133主与正式资源的完整SHA。

首次准备遇ENOSPC，未创建科学源/输入或启动数值子任务；在逐对象证明旧Git临时包被正式包覆盖后清除四份冗余临时包，释放2,627,161,634字节。随后才执行本formal0任务。科学原件、正式Git包及活动Newton矩阵均未删除。
