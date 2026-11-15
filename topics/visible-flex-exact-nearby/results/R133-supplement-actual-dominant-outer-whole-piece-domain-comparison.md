# R133：实际五片整域检查与下一相关源扩展的合法范围

2026-11-15。**实际公开 Actions 结论：run 43680556665/1，子进程退出码 0，15 项门全部通过。**

本结论只比较原完整物理片与已经支付的径向域。没有计算新目标、FFT、旧 cubic value、源包络或径向积分；原78成功数学阶段没有重算。新域比较实际用时 0.03972491499996522 秒，包含启动与退出等待的父进程 wall 为 0.2642209229999253 秒。

## 1. 实际输入与同一对象

脚本是 scripts/fourfold_codazzi_dominant_outer_piece_domain_comparison.py，18008 bytes，SHA256 43abdfca9fdb16ebaae6a50349e3faaab87b8def87e1a233e7e44aca18ad6017。参数清单是 notes/2026-11-15-R133-dominant-outer-piece-domain-comparison-CI-inputs.json，4594 bytes，SHA256 9c5aac3369fa328284d08f1daf5a40f1230cdbb3fd1d70afcde5b9ef21d4cdf3。

原四输入均从不可变公开提交 a3d84d905ce72e3a854874bbe98d119623f3f8de 恢复到临时 science 目录，并通过完整文件字节和 SHA 检查：

| 原输入 | bytes | SHA256 |
| --- | ---: | --- |
| full65 candidate index | 6750 | ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413 |
| candidate natural shard001 | 2738003 | 3aeb38bf0577207cafcad3a59e43ed5a04a4c9cf9a703c4c3c4088c963a09106 |
| full193 direction index | 11295 | ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6 |
| direction natural shard005 | 2698707 | ce29c19c81e77cb2f2ea9b70edc59af96a869116fa96e2e5375ffa4d61927917 |

只解读原 NPY 头和 radial_nodes 的准确 binary64 有理数。full65/full193 的五个整片节点完全一致；原 root piece2549 和原根区间不变，独立 mean 未删。五片连续、没有间隙、重叠或新造 seam。

## 2. 两个目标整片的实际门

固定 eta0，保原 real/complex delta 半径 1/100000000。原 Rg=3/8000、RHO=1/6000、intrinsic RC=1/2000，原 scalar germ 不扩大。

| 目标片 | 实际完整物理区间 | 对所有原允许根的最大 absolute rho | 对 RHO 的严格余量 |
| ---: | --- | --- | --- |
| 2547 | [4292493394837505/18014398509481984, 8586863289519747/36028797018963968] | 2542605252665060199531/21990232555520000000000000 | 3367300519764819401407/65970697666560000000000000 |
| 2551 | [1074061598631745/4503599627370496, 8594369288898697/36028797018963968] | 6368035656917093122749/43980465111040000000000000 | 2886125584768720631753/131941395333120000000000000 |

两片各自全部位于同一原 germ、正确严格侧、Rg、RHO 和 RC 的内部。结论覆盖整个原 cubic piece，不是仅覆盖诊断中的一个 common-row。

五片的完整准确区间、全部15项实际门和下一入口条件见 [原实际小结论](../notes/dominant_outer_piece_domain_comparison_ci/run-43680556665-1/actual-result.md)。其4514 bytes 的 SHA256 为 8bd0ae3d892cb1a603bcebc3f150a95ff5ded2d7dd69ade2c63e947c68644182。

## 3. 允许继续的范围

按 [E1–16 非零入口合同](R133-supplement-nonzero-entry-continuation-to-the-next-physical-pieces.md)，piece2547 继承2548，piece2551 继承2550 的真实 phase difference、normalized first-correction difference 和 log(G/Gbar)−log(A/Abar)/6 的径向常数。三者不能在新 seam 重置。

下一消费者仍须实际检查旧入口 strip 与新 coefficient strip 的共同 ray 门，支付连接段、完整 ordered forcing difference、九个 old-circle 词、五个独立 mean 项和完整径向源积分。径向 jets 由新片单侧方程产生，原物理接口和修正 trial 的真实 jump 不消失。

这项结果不证明新完整源界、corrected-trial seam 算子、strong-return、cutoff97 全高频逆、参数 Schur 或精确 PDE 族。

## 4. 执行、同步和保存范围

实际脚本命令使用 --repo <immutable-science> --manifest <committed-manifest> --manifest-sha 9c5aac3369fa328284d08f1daf5a40f1230cdbb3fd1d70afcde5b9ef21d4cdf3 --out-dir <temporary-output>。

真实 pull 在 05:19:39.225985 UTC 和 05:19:46.281134 UTC 完成；后者到 d13e520839a5beda65c2e8d240d7432f31362abf。两次根及课题 README 差异均为空，继续已读137c5a877fb387a82cbde01f084d1fa67ee717aa规则。

临时完整 process11799 bytes/SHA581e0db497c363b577fede1a3b9b3e934e4c543972bdc97861a8797ff180aea8和stdout114 bytes/SHAf7d1d5e23bbf1c42360c245aa9be5bab6f98696d537448efa8a826d48258f3b3仅留下身份记录。没有新数据、Release或Actions artifact上传。完整实际命令、全部输入身份、门、pull记录和输出哈希见同目录 execution.json。
