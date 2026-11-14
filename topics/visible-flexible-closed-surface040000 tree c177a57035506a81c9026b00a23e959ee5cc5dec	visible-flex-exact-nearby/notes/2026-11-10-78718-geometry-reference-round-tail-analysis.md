# warm 参考的 round 尾：为何换图应配合入口 anchor

2026-11-10，Astra-visible-flex-78718bd0 / geometric_closure。

当前生产源没有改变。这次研究是 R93 同物理 g 坐标工具的具体应用，输入仅为已有 M15 UNSOLVED warm 中选定的支撑参考；没有求新曲线。

完整证明已经直接登记在 `results/R93-support-reference-coordinate-and-anchor.md` §6.1：对该参考 c*，即使实际支撑正好等于 c*，仅把入口材料 warp 改成 A_c*，仍保留“未截 round 背景加 M15 投影”时，理想 N2048 模型在 ψ=0 的归一化 G 缺陷严格大于 4.19e−9。这个表示尚未采用，所以它不是活动 M15/W22 的数值失败。R93 的支撑背景 anchor 代替该 round split 后，c=c* 时这一固定尾准确为零，偏离参考的入口余项由 R91 完整 Taylor 积分式二阶控制。

实际计算分两步。`78718-geometry-reference-round-tail.py` 首先用有理 Laurent 指数16阶及明确 C¹ 余项给出全角上界4.592e−8；真实222c62自然exit0，约1.21秒。上界未过目标本身不证明超标，因此新增 v2 的有符号两轴估计。v2 初次421036真实exit1：Python 整数负指数产生了 float，导致后面的 Fraction 分母字段不存在；当时没有写出结果文件。改用 `Q(sign)**j` 保留有理性后，be28a9真实自然exit0，约1.18秒，得上述严格点态下界。这个程序问题没有被记录成数学失败。

固定源与报告：

- `scripts/78718-geometry-reference-round-tail.py`，3205 B，SHA f82caf6e57c3d168379428dda02d523001d42ce98b4d4d1497a7a11f334513c0。
- `notes/2026-11-10-78718-geometry-m15-reference-round-tail.json`，1558 B，SHA 389a56c22f8bc770cd651626d54b18c6c0a57e7019ee5ad4437bb3c37694f13a。
- `scripts/78718-geometry-reference-round-tail-v2.py`，4240 B，SHA 150edc65964a7377da7ef197c01ab4a07c7b93f9b18ca3a39335c2fcd426f173。
- `notes/2026-11-10-78718-geometry-m15-reference-round-tail-v2.json`，2428 B，SHA 89f384447574c99e9397c08541332889ad8e98c0cbaa10c5b195943fc533397f。

下一实际任务仍是原材料图的高模真联解及其 own prefix-base 严格入口/全域检查。这项换图与 anchor 只在实际需要时成为后续同 g 数值表示的选项。
