# R862 首次公开消费者：同一 Rosati 投影的准确整数倍

日期：2026-11-16。状态：执行入口已具备真实来源；本文件不预称新 Norm 多项式及整数分母已经计算。

## 数学范围

[完整证明](../results/R862-original-Rosati-projector-from-certified-Hom-correspondences.md) SHA256 afa1e0d08d0a0bd65374fee1996f0d644588840dee35fec7d766cc2f4e5707d0 已证明：原七个实映射的 pull–push 之和为整对应 D_A=q_R†q_R。既有 R791 原六次实域元素 a_A=κM_v 给 P_A(X)=Norm_F/Q(X−a_A)，d_A=P_A(0)>0，以及整个 J_X 上同一投影 E_A=1−P_A(D_A)/d_A=q†κ⁻¹q。F_A=d_A E_A 是实际整有限对应。

此次只做新的六阶整数乘法矩阵和准确 Faddeev–LeVerrier 运算，验证原域中的 Cayley–Hamilton 和 a_A 逆元分子；随后在已认证的十二阶 Hom 矩阵上完整计算 P_A(E)=0、F_A(E)=d_A I，并检查 F_A²−d_A F_A 在 X P_A 商中为零。全部分量使用原次序，常数 3870 乘 1，不误作 s₀=2。整体 J_X 恒等式依赖上述证明，不能仅从十二行检查外推。

新对应表达还保留七个原 f_R 共轭和五个原 g_R,j 方向；没有重求 Hom、Gram、Galois、κ 或原周期。E_Aφ*=0，所以该投影不能替代原 Y 的活跃 Hecke 投影 eη，d_A 也不能代 YP 的 d 或挠阶 N。没有宣称完整非 p 支撑、原高度或全 p 排除。

## 固定实施

| 项目 | 字节 | SHA256 |
|---|---:|---|
| core R862_original_Rosati_projector.py | 24146 | 4656250c7fcd86c9e6d36a4c94925979b27cc4ab54e0cb1299e6972319598a86 |
| wrapper R862_public_original_Rosati_projector.py | 27169 | 8c7c82be5e208dd5c7e82e3f07b8d3d4d1936504dbc249409a866bea38b2b7b9 |
| request R862-original-Rosati-projector-public-request.json | 8561 | 0b928df90e16cec9a5174b1ba7639723c2cc71ab5553644ef582bc8f32010e67 |
| workflow serre-R862-original-Rosati-projector.yml | 6132 | 8aa8e52c3b768230749cf7ef8429f7b4079fc39804db69c9e16c9ab513530e71 |

首 scope 为 20 分钟，只有标准库新数学，无本地执行。四个新数学 stage 原子保存；预算和纯运输参数不改变数学身份，同 tag 完成阶段只读复用。所有结果与必要原源仅保存在一日 Actions artifact，不进入 Git 或 Release。

## 空 runner 的实际来源

由 R852 成功 run43801628875/source d0023643ba47099947b6753010d8e7c8120a214c 的 artifact14196442913（2743138 bytes，SHA256 01ae4657b56387080bc44b9f10b841e0c29499ffce02e2046b1a3794c26cd45d）取九个直接原件及其中 270 个原叶；完整逐件 bytes/SHA 和父子来源关系确认后，选出 R791 的八个原件。原 R791 run43686308194/source f945ef5d5aee4d8222dc791e39a0709b661cebbc、core11068eb0、configuration eb3d0714 和旧 README 身份 c6db597c 均保留。没有向已到期的 R791 或 R847 artifact 发出请求。

原输入 Galois 矩阵为 15617 bytes/f3793ddc7680b718a4448d45587661182986a3558db346ad0a2c9031c8952183；实下降/η 输入为 5573 bytes/24a894163f136a4e8c71b117e373f8fafb66a6e0c94b4efe3f141f78bb39b968。来源封装复用已经登记的 R858/R852/R850/R824 纯 IO 代码，不导入其数学核心。

主线程已完整读取 core、wrapper、请求及 workflow；本地只作字节、schema、AST 和源码阅读。实际 run/job/artifact 与 d_A 必须待公开运行结束后补入正式结果。
