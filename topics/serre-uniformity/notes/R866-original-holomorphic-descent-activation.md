# R866 原全纯微分下降的首次公开计算

日期：2026-11-16。会话：serre-public-astra-20261115。

## 真实输入与新增范围

直接消费 [R864 的实际 127 维原全纯基](../results/R864-certified-original-canonical-holomorphic-basis.md)；其 producer 为 run 43813041008、source 3e31c9735b5ecf85948b4447782a5e0062e32167，artifact 14201401009，完整 ZIP SHA256 d83abe9541db2cd772fc3673d67783caf5038ef485b8abfe73cb787d6f7a6991。原 R786 的 152 件、R837 的 8 件从 R853 的真实 169 件载体取得；R853、R864 各直接 9 件，共保留 178 件原来源。载体每个成员仍核原字节/SHA，不改 producer 身份，不重算旧 Fourier、cusp kernel 或三条共轭。

[方法](R866-original-holomorphic-semilinear-action-and-Q-fixed-basis.md) SHA256 0ecc37602135f9605e52e667a9e180215213772192f09897dce33026030a96f9 已证明此次新运算：形成实际 H=AB，从原 146 个独立选行中取得 127 阶 Q 及其准确逆，求 C=Q^-1 S_J Q 和完整 Q-固定基 P。全部 560 行的 HC=SH、C²=I、C·bar(P)=P 及 S·bar(HP)=HP 都是本次结果的必要数学乘回。

原 e_i 已含 82²；H 就是原 F_j 的 Fourier 展开，微分的系数为 82H。原 c0 固定 ξ、共轭 s，normal 转换的 e73 负项只用一次。原有理 V1 坐标本身不冒充 Q-定义。

## 固定执行身份

- core：R866_original_holomorphic_descent.py，28830 B，SHA256 2b8aa7c10efcca6899df4de84abb3eb0b81e414aae931de9cca578dfffcc9fce。
- wrapper：R866_public_original_holomorphic_descent.py，41782 B，SHA256 7074905457e9299219fd8822b0272a034941cdb21fe07c94110fe5275b1b787c。
- request：R866-holomorphic-semilinear-descent-public-request.json，48270 B，SHA256 8ae7299c795268a93ad00bc744ae44979f90f68ab213f99e85778481f895cb3c。
- workflow：serre-R866-original-holomorphic-semilinear-descent.yml，6869 B，SHA256 b73a443e51f8cbee38e8d6b7bebd3ac2ef255c2b8ca3e8b0fd89f086c723e6da。
- python-flint 0.9.0；数学预算 60 分钟。每个已完成阶段有原配置和字节绑定，若需延续只恢复该阶段。
- 本地只完成源文件阅读、真实来源 IO、SHA/schema 和 AST；新数学全部交本公开仓库 Actions。主线程已读完整 core、wrapper、方法、请求与 workflow。

成功后 R865 直接读取同一 H、实际选行 J 和准确 Q^-1，不再形成 H 或求逆。此任务不计算 YP 的 128/634 维亚纯 Riemann–Roch 空间、连接、活跃 eη、非 p 高度或完整高度。激活时不预填新矩阵或成功证书；run/job/实际结果随后按远端真实输出登记。
