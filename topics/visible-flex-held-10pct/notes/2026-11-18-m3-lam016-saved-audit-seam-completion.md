# λ=.16：保留已保存的完整前缀审计，只补真实接缝

**类别：数值证据与已执行接口。** R45 的 $\lambda=.16$、M8 状态完成了原实际尾接缝。原内解、物理 quintic 和完整前缀审计保持；本次不再调用 prefix audit 或 mean-height 原函数积分。前缀有限 FFT metric 仍为原来保存的 $.00013837763095648974$，没有通过最终度量门。

## 1. 实际待完成的位置

原运行目录 `m3_work/trace-path-lam016-coupled-v1/` 已保存 494 节点的真实返回内解、实际 BC 检查、物理 quintic 以及完整 `summary`。原内解在两张自适应网格后成功，最大 RMS 为 $9.880114855350935\times10^{-7}$；outer 0 的真实 BC 为 $4.410472343803251\times10^{-11}$。完整返回文件和 sidecar 的 SHA-256 分别是

`62e1c1e1567bf8827fb4d21bd4a5ec11284920d172c14e853503db1dc5fd4ebf`、
`69ba65416c53b91e6e87ee6491ba63a9bc3ea01f65dd8ef93712799814f60a3b`。

节点高度的实际尾记录 `seed_tail_0001.json.gz` 已真正接受，SHA-256 为
`c807ab79ef1ca6d6a4b7954c9632d1defdee6e29bb1cf3380b737ffb7387c406`。
原程序随后在 physical quintic 的真实端点高度作新请求，该 `seed_tail_0002.json.gz` 真正失败于
$3.66786119636838\times10^{-9}$，SHA-256 为
`69e2d545dad75affedcde4872fcdf2fc86bb0e42234489c21887b58f81eed5bd`。

这次没有丢失前缀审计：待接缝的 `seed.json.gz` 已含完整 `summary`，SHA-256 为
`f60de678f4a99595e0caba4ecd8c9379fb8b607522956d7bb9769559282cb797`。其完整 audit JSON payload 哈希为
`0a673b3c455121d92ad5886efc2cf7c1837087960ee5a0d63f27b98edd015110`。

另一次已登记的显式新高度初值保留原接受尾的全部内部、深端和切口动量，只重新编码 node0 的两个实际 Dirichlet 差异。原 worker 在 `4232` 的真实运行中于 04:34:28 UTC 接受该新高度，迭代 0 残差 $1.83393059818419\times10^{-9}$，208 个有限 Jacobian 标量和完整 audit 返回。本次只复用这份真实响应：

`m3_work/trace-path-lam016-seam-preserved-v1/seed_tail_0001.json.gz`，SHA-256
`1470c291844bbc89cc9afe17d1a24a07aacad4728cf6fb92f8afb2da87961c57`。

## 2. 只补接缝的通用入口

新 `scripts/resume_closed/finish_m3_trace_path_saved_audit.py` 显式接收原待接缝 physical checkpoint、真实失败记录和同一新高度的真正接受记录/终态。源 SHA-256 为
`fff945cb062369b2f821bee39c76b2c4cb74ffcef9e1dd237dfe9315340b115c`。

它绑定完整物理定义、base 加 $p_0$ 一次、全部参数/控制、原窗口、原 native 来源和配置。需要的原 core/inlet constructor 在新进程中恢复一次，然后直接读取已保存 quintic 系数。未完成的 checkpoint 不插入假的 `tail_seam` 来通过完整 reader；只有真正的原 `seam_audit` 返回后，才对最终文件调用完整 reader 的元数据验收。

完整高度只允许逐位等于这次真实接受记录；未知高度拒绝，既不插值响应，也不替换为旧高度。没有 worker、DN、BVP、状态转移投影或新 C² 插值。旧完整 prefix audit 全 payload 保持，旧系数文件原字节复制。原 `seam_audit` 所需的切口速度及一、二阶 mean jets 确实重新求值；这不等于重算整个前缀的 mean-height 原函数积分。

准备 `a20ba4` 退出 0，.089646973 秒，仅绑定元数据与 121 个源。计划位于
`closed_work/m3-trace-path-lam016-seam-finish-v1/launch-plan.json`，SHA-256
`b02601dca34b75f69a968a1d231531a103055fa31f494a145dc0ab4c0d8a751a`。
唯一真实执行为 `81455`，启动 `eaa7e7`、终态 `99d8bc`：2026-11-18 04:35:45 UTC 退出 0，observer 2.0058231000002706 秒，实际后处理 1.2277773530004197 秒。

本次计数为：**0 新 inner、0 新 native、0 新 prefix audit、0 新 mean 原函数积分、0 新 C² 插值；1 次原 seam audit、1 次真实响应查询。**

## 3. 保持的原结果与新完成的接缝

当前原 gauge/warp 仍为 `.06`，定义核幅度 `.05857996100242497`，原 base 加完整 $p_0$ 后 $\delta=.061042681029028364$，经线长 `1.3602518771749645`。全部八参数、七物理控制、原尺度、profile、chart/port 和真实尾身份在紧凑记录中，没有从别的 $\lambda$ 或旧 raw 圆化核替换。

| 审计量 | 保存值 | 本次来源 |
|---|---:|---|
| prefix metric，有限 FFT $\ell^1$ | $.00013837763095648974$ | 原保存 audit，未重算 |
| Cartesian Darboux 张量有限值 | $.11186743320536596$ | 原保存 audit，未重算 |
| flow defect | $.0006715911078039435$ | 原保存 audit，未重算 |
| physical BC | $8.820944687606502\times10^{-13}$ | 原保存 audit，未重算 |
| mean 一阶接缝差 | $3.332213902029757\times10^{-8}$ | 本次原 seam audit |
| mean 二阶接缝差 | $-7.795056617965201\times10^{-7}$ | 本次原 seam audit |
| nonmean 一阶接缝最大差 | $8.820938771081366\times10^{-13}$ | 本次原 seam audit |
| nonmean 二阶接缝最大差 | $1.4977331737121337\times10^{-6}$ | 本次原 seam audit |
| cut metric，有限 FFT $\ell^1$ | $4.763323669994485\times10^{-6}$ | 本次原 seam audit |
| cut metric 一阶差，有限 FFT $\ell^1$ | $9.977384758489137\times10^{-5}$ | 本次原 seam audit |

原 prefix audit 使用 1136 个径向样本及 512 个角样本。它仍没有保存最坏 metric 分量/径向位置，不从总量猜测峰的位置。有限 FFT 数值和原求解容差不代替全角、全径向或全相位误差证明。

## 4. 输出与复现

新执行目录中的完整结果是：

- `seed.json.gz`：`770a54c6a1016f57e723091443a49c25bf9ebc9c7b81bca88b94600490fad8ec`。
- `seed_coeff_00.npy.gz`：`f844311c5a24ac651b3a1b85e4814260bbd14f5b785d51983ed4304aea2d2a7a`，与原 physical 系数原字节相同。
- `seed-summary.json`：`7d0d7e958ea6332bddd3e4948a9183b87bab4ef3919008ee97d26cfc4ef63b44`。
- `seed_tail_0000.json.gz` 是真实 `1470c291…` 接受记录的原字节别名，明确标记复用，未虚构新 native 调用。

准备命令使用新脚本的 `--prepare NEW_DIRECTORY --checkpoint ORIGINAL_CP --failed-seam FAILED_RECORD --accepted-seam ACCEPTED_RECORD --accepted-summary ACCEPTED_SUMMARY`；这里的四输入分别是第 1 节的真实文件。准备产生 observer 命令，实际入口为 `--run-plan NEW_DIRECTORY/launch-plan.json`。不可覆盖原运行目录。

`record_m3_trace_path_saved_audit.py` 只读 collector 在 `93a6d4` 退出 0，.032463268 秒，核实完整审计 payload 未变、物理参数和系数未变以及真正的接缝来源。它没有构造模型或评估方程。紧凑记录为 `scripts/resume_closed/m3_trace_path_lam016_seam_terminal.json`，SHA-256
`f3574eaa83d54459f2c9981982ab2e62d6bdaef095b13e20ae6af6171bf5996f`。

这个完整 finite checkpoint 可继续下一设计同伦。它仍不是 $\lambda=1$ 圆弧，也未满足最终度量门、固定完整 $g$ 收敛、闭合、reach 或 10% 握持要求。R47 的精确控制嵌套是后续升阶接口，不改变本次 M8 运行或使这些数值误差自动消失。
