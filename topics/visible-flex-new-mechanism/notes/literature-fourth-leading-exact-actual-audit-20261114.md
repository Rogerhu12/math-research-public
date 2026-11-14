# R49 准确代数公开运行审计：43611065115

2026-11-14，root。实际运行：[public Actions 43611065115](https://github.com/Rogerhu12/math-research-public/actions/runs/43611065115)，job 132496020911；源码提交 `bc0768a3c14e5de84a27124b9391d9ebcbacf20c`。本项只检查精确符号恒等式及多项式最高系数，没有几何 ODE、候选评价或优化。

原回执为 [receipt.json](actions-43611065115-1-fourth_order_exact/receipt.json)。按回执逐件读取来源提交的 **70 个来源文件**，全部字节数与 SHA256 一致；唯一输出的原字节数与 SHA256 亦一致。runner 实际 pull 到 `975bb85afd4f24c5ce01c48bf626d70f214a527a`，两份 README 无变化。

- 脚本 `literature_fourth_constant_leading_certificate.py` SHA256：`64690bc72441abe2f3e3ffc39482dd6f611c54e30b84b35abf9e859d386dd772`。
- 输出 `fourth-constant-leading-exact.json`：754 字节，SHA256 `d9d1ef018d8ac588bed9caa2436a7b1d9d66d6d678b7e16997147e7d0f3bec79`。
- 输出与已提交的纯代数开发证书原字节完全相同。

五个符号差逐项准确为零：单平方 characteristic 的二导数、交叉极化的二导数、能量分部积分的完整通量，以及 F 和 Qa 的两条导数恒等式。准确展开同时得到平移密度次数 8、最高系数 `-f2^2*f3^2/128`，及窄化密度 lambda^-10 系数 `-c^2*(1+c^2)^3*f2^2*f3^2/128`；乘 dx 后是积分 lambda^-9。单 packet 的四次幅度和准确为 `241/225`。

这些结果复核 [R49](../results/R49-fourth-ruling-leading-coefficient-and-narrow-packets.md) 的代数步骤。真实常段、支撑分离、最高次数与二/三阶自由校正不变、非零紧支撑函数的正积分，仍由该文完整证明承担。此回执不声称所有 profile 的 T 都为负，不构造有限等距族，也不满足主课题完成门。

本项已成，不重复相同短运行。继续尚未排除的 profile/几何与完整闭面连接。
