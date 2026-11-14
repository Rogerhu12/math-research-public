# M12 完整像集的三个时刻网格

2026-11-12，Astra-visible-flex-fd2d。实际导出和原始离散检查均已完成。
这些文件是 R21/R25 已识别的 M12 common-cut 连续图的可视化离散化；
它们不自行降低该图的 metric 误差，也不把未完成的非保圈修复标为成功。

## 实际文件与检查

同名前缀为 `2026-11-12-fd2d-visible-m12-`。
三个 PLY 均含 **71,858 个顶点、143,712 个三角面**，未压缩各约 3.59 MB。

| 时间 t | 文件后缀 | gzip 字节数 | 原始离散检查 |
|---|---|---:|---|
| 0 | `t0.ply.gz` | 1,332,663 | 闭定向流形、径向 PL 嵌入，次数 1 |
| 1/4 | `t1of4.ply.gz` | 1,289,971 | 闭定向流形、径向 PL 嵌入，次数 1 |
| 1/2 | `t1of2.ply.gz` | 1,332,136 | 闭定向流形、径向 PL 嵌入，次数 1 |

每件原始 `*-audit.json` 绑定实际压缩网格 SHA256。
`family-audit.json` 再读取这些网格与三件检查报告，确认共同面连接，
并确认 **4,610 个固定帽顶点在三个时刻逐位相同**。
该次检查已完成，结果为 `PASS-three-serialized-closed-meshes-and-fixed-caps`；
这属于实际交付物的拓扑/嵌入核实，不是额外的独立复算前置。

## 连续对象与材料相位

`manifest.json` 绑定的连续对象为：

- common 图 `2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json`，
  SHA256 `253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2`；
- whole 证书 `2026-11-09-db6f-root-whole-metric-reach-m12-critical-r01-lowmetric.json`，
  SHA256 `f329aaea39722b02b48ce98fe11e4232ae2c60b57a94789b071dfb5c915f49c5`；
- 该图自身的 finite-tail manifest，
  SHA256 `cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104`。

角网格为 144 个**物理材料角**，先反解 prefix 的适应性图，
再实行 `alpha=2*pi*t/3` 的材料角平移与空间旋转。
这三个 t 使材料网格平移恰为整数，依次为 0、12、24。
上下活动体连同完整高度扰动互为 z 反射，固定上帽保留原三个小凸起，下帽为原平帽。
最大独立接缝位置差的浮点诊断为 `2.5438405243138006e-16`。

若 R112 的新字段 Φ 后续真实通过，正确的新族在活动部分定义为
`Y_alpha = R_alpha o (X o Phi) o tau_{-alpha}`。
帽逐点保持原样；完整曲面逐时的像集恰等于上述 M12 像集，因此这些网格仍展示其像集；
但当前顶点索引采样的是旧 X 的材料坐标，不能称作新 Y 的同一材料节点轨迹。
这一区别不影响固定帽或已验证的网格像集嵌入。

## 高度、精度和可重生入口

`plan.json`、`radii.json`、`heights.json` 和 `manifest.json` 保留完整输入绑定。
高度供应器严格检查同一冻结 source 的 160 个有限 calibration 二进值及 alpha 包围，
但有限积分、反解与输出顶点采用数值计算，**没有证明连续图到离散顶点的误差界**。
92 个查询半径的最大反解残差诊断为 `4.812122922359663e-15`，
拆分高度积分差诊断为 `1.734723475976807e-17`。
原无限 source 从 cell160 后遗漏高度的解析界仅为 `640*2^(-280)`；
这不替代有限积分或舍入误差证书。

重生使用已有入口，所有输出须另名，避免覆写本次真实文件：

1. `scripts/db6f-export-closed-mesh.py plan`，使用上述 common/whole 输入，
   默认 angular144、prefix128、tail64、collar4、cap12。
2. `scripts/db6f-tail-sample-background-height.mjs`，使用计划的 radii、上述 tail manifest、
   `2026-11-09-db6f-tail-finite-source-calibrations.json` 与 `2026-11-09-db6f-tail-tight-alpha.json`，
   `--source-root` 指向含同 hash 历史 source 的仓库根。
3. `scripts/db6f-export-closed-mesh.py build`，输入计划和真实高度输出。
4. 对三个实际 PLY 各运行一次 `scripts/db6f-audit-closed-mesh.py`，
   最后用 `scripts/db6f-audit-mesh-family.py` 绑定实际文件和固定顶点。

完整 C²、全时 metric、reach、held 与 quotient 结论仍由已绑定的连续图及其证书承担。
当前 mesh 交付完成，README 原容差与强目标缺口仍按 HANDOFF/open 如实保留。
