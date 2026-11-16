# R865 原 Y 的 T7 与单算子谱：首次实际消费者

日期：2026-11-16。会话：serre-public-astra-20261115。

[数学证明](../results/R865-original-Hecke-T7-from-certified-level82-Fourier-rows.md) SHA256 50bfc4bd4d0629e0ceda09eb15bf40add53333fe4dab87430a7b34697d74cc19，和[执行方法](R865-original-Y-Hecke-T7-consumer-method.md) SHA256 88a3c9dd67cee4b483bada200791d22f329d97a507968c71c2bc80aa84e24119 固定本次原对应、尺度、完整乘回和续接。

## 唯一真实来源

R866 真 run 43815338283/source6373b025e7a4ea02a2beb3bb36a01447176903c9 已完成全部 127 维原 Q 基。此次直接读取 H（468416 B /3c9ce8d3258d9a829c5588429523df640b3e6cb7a5d2fac050181ba34b6e50fc）、原选行及准确逆（599746 B /e93951a05190af9e63ac9163797036ad88f1aaa5a360048d85e57d8c69d15e54）。原178件载体全部成员逐SHA后，只保 R786 的152件、R864的9件与 R866的14件，共175件。

原R786行实际没有独立顶层result，原configuration保result；消费者按该producer的真实schema读取，不改写来源。原历史README、父子source身份、完整40坐标、q≤128、原e_i已含82²及微分82都保留。没有第二次构造H、选行、求逆或Q下降。

## 首次新增量

读取旧q≤91，仅新十二个不在H内的A_nB、十三个T7目标块。用旧逆得原K基矩阵M与全部560×127等式；N=K_JU给原真实Q基矩阵，准确检查全部异奇偶零和MU=UN。按实际54/73两块各求一次特征多项式，再整系数分解、逐因子准确Bézout/CRT和整对应倍数。只给单个T7的谱投影，不冒完整Hecke等型或eη。

## 执行身份

- core R865_original_Y_Hecke_T7.py：35975 B /3d074559a3cb84ef39656dce0937cd6aaf3d55252fbb21d075293d5eb7f6ce10。
- wrapper R865_public_original_Y_Hecke_T7.py：36134 B /9b05e7ffefcdd035f89658330c15a24b5cc815f50fdcc76562ba66eb737461ae。
- active request：46838 B /28aa9adcd3167d74f9d33a82e6ac35c944ad089025fdfaf81d6185dd1a963f20，producer_inputs_pending=false，resume=null。
- workflow：6445 B /61b43759e55ceabd22c9cbc00eef9b4a383a337c6514e5eefc4590c05ea70a9e；pip使用run块标量。
- python-flint0.9.0；120分钟数学预算、180分钟workflow；外层留900秒输出余量。只读权限、一日artifact，每个完成阶段原子保存和同tag续载。

主线程已读完整证明、执行方法、core、wrapper、request与workflow，并核原R775半线性迹及两条Zywina原文规范。源对接只做IO/schema/SHA，本地未执行数学。新运算全部在本公开仓库Actions；raw不进Git或Release。实际run/job在本次推送后按远端查询登记，不预填成功。后继R870继续真正η谱支持和7处挠界，先核原类定义域，不把χ7(8)擅用于仅在更大域定义的挠点。
