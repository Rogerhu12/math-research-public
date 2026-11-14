# M8 证明图的三个闭合可视网格

对象：R17/R18 已认证的同一 M8 公共接缝有限图。三件文件均已真实导出、重新读入，并通过闭合有向流形与径向 PL 嵌入检查。这里交付的是连续证明图的数值离散近似；G5 的固定背景收敛要求仍单独处理。

## 1. 文件、时刻与固定对象

| 时刻 $t$ | 活动角 $\alpha=2\pi t/3$ | 文件 | 存储字节数 |
| --- | --- | --- | ---: |
| $0$ | $0$ | `2026-11-09-db6f-visible-m8-t0.ply.gz` | 1257143 |
| $1/4$ | $\pi/6$ | `2026-11-09-db6f-visible-m8-t1of4.ply.gz` | 1218128 |
| $1/2$ | $\pi/3$ | `2026-11-09-db6f-visible-m8-t1of2.ply.gz` | 1257011 |

文件均在 `notes/`。每件解压后约 3.363 MB，满足单文件小于 5 MB；大于 1 MB 的输出使用 gzip。格式是 binary little-endian PLY，顶点为三项 binary64，面为三个有符号 32 位顶点索引。无需 PDF、图片或外部数据服务即可生成与核验。

每件有 67250 个顶点、134496 张三角面。三件共享完全相同的面索引及材料网格编号。实际文件中属于固定帽、圆 cuff 与极点的 4610 个顶点，其全部 binary64 位模式在三时刻完全相同。上帽保留三个固定凸起，下帽为固定平帽。

主 manifest 为
`notes/2026-11-09-db6f-visible-m8-manifest.json`，SHA256
`6a49b75c5a0c112fc798c4167356b9b8f57e0f489e33b6ed9aedcc2c1eff3282`。
该 manifest 保留生成时的状态，后续离散验证另由下面的绑定报告给出，没有改写原 manifest。

原闭图的 SHA256 为
`4f00d33a2add41b5711d805866228ff082786f597ab2362d6bd3a0c10a704524`，
原 whole certificate 的 SHA256 为
`265fe7d95f08895580ade27c4aa64b243736604f1a9a8fac55d65ade42521aaa`。
因此这些网格不能被重新标注为后来的 M12 图，也不从网格检查推断新的连续度量、曲率或 reach。

## 2. 材料角、公共接缝与镜像

导出器 `scripts/db6f-export-closed-mesh.py` 的 SHA256 为
`ee4a474ebdecf4462e41f19b8b22c591f0e532e0419f0d7b3e4f2677d43b1708`。
前缀采用原已审有理 clamped spline 与 cutoff 求 $e(u)$，再数值反解

$$
\theta=\Theta(u,\psi)=\psi-\frac{e(u)}3\sin(3\psi).
$$

固定材料角网格为 $\theta_j=2\pi j/144$。所选三时刻恰好使 $144t/3$ 为整数，故活动带的材料作用可由索引移位 0、12、24 精确表达：先取 $\theta_j-\alpha$ 对应的基础行，再施加平面旋转 $R_\alpha$。该操作在材料角网格上进行，未把图坐标 $\psi$ 错当材料角。固定帽行直接复制。

公共 cut 的前缀与尾部代表点分别求值作数值一致性检查，最终共享同一顶点环。R6 collar 使用同一有限图的五次多项式。上尾完整高度为

$$
H_c+\int_r^c w(s)\,ds-V_z(r,\theta),
$$

下活动带对完整高度作 $z\mapsto-z$，而非只反射旋转背景。core、cut、cuff 都使用单一共享索引。上下极点各只有一个顶点，没有把重合点作为未缝合边界。

实际独立接缝求值的最大差为 `2.498001805406602e-16`。这是网格数值诊断；连续图的精确两 jet 接合由原公共接缝证明承担。

## 3. 三件实际文件的严格离散验证

`scripts/db6f-audit-closed-mesh.py`，SHA256
`351c9828602a7ba38e918ed7ac46fb93699f8b92395a76fc1593cbde4114386e`，
从磁盘重新读取每件 PLY，不接受导出器内部的顶点或拓扑缓存。三次运行均实际退出 0，报告为

- `notes/2026-11-09-db6f-visible-m8-t0-audit.json`；
- `notes/2026-11-09-db6f-visible-m8-t1of4-audit.json`；
- `notes/2026-11-09-db6f-visible-m8-t1of2-audit.json`。

每次都验证无重复面、无边界边、每条边恰有两张反向邻面、所有面连通、每个顶点 link 只有一个闭环，以及 Euler 特征数为 2。随后把文件内 binary64 坐标视为精确输入，采用向外舍入区间核对全部面严格径向向外、相邻顶点内积为正、球面立体角和落入能隔离度数 1 的有理区间。

三件球面面积区间均落在
`[12.56637061435499, 12.56637066676993]` 内。这里使用报告的更紧区间作精确 Fraction 比较，不依赖打印小数。由正局部度与整体度数 1，径向投影是同胚，故每件实际 PL 网格无自交并嵌入三维空间。证明与顶点角扇步骤见
`notes/2026-11-09-db6f-closed-mesh-radial-validation-proof.md`。

该条件引理及区间实现已获 root 全文独审；root 又独立运行了三件完整 PLY 验证，所有数学字段与作者运行逐项一致，见
`notes/2026-11-09-db6f-root-review-visible-m8-replays.md`。

导出器全文另由 `/root/tail_theory` 独审，通过后独立完整 build 到新输出路径。三件 gzip 的 SHA256 与原件逐字节相同；20736 个材料角又由独立二分反解核对，所有整 Z 镜像、固定帽、相位与输入绑定检查通过。见
`notes/2026-11-09-db6f-tail-review-closed-mesh.md`。该审查没有让高度 helper 的作者自审自己的算法，而是依赖前述独立高度审稿。

实际文件之间的共同面索引、4610 个固定顶点的 uint64 位模式、所选时刻的材料索引移位另由
`scripts/db6f-audit-mesh-family.py` 检查，输出
`notes/2026-11-09-db6f-visible-m8-family-audit.json`，实际退出 0。
其中相位坐标比较是数值实现检查，严格离散嵌入仍由前述三个独立区间报告承担。

## 4. 数值高度的界限

76 个半径的相对背景高度来自冻结 helper
`scripts/db6f-tail-sample-background-height.mjs`。有限 160 个校准系数逐个与冻结表相同，本次完整 56 键参数字典也与紧 alpha 的 checkpoint 相同。实际查询的最大反解径向残差约为 $4.813\cdot10^{-15}$，拆分求积差约为 $1.735\cdot10^{-17}$，都仅为数值诊断。

独审见 `notes/2026-11-09-db6f-audit-height-sampler.md`。该稿另认证 alpha 代表值单独造成的精确源高度差小于 $4.56\cdot10^{-14}$，以及极深源的单独遗漏界；它没有把这两项冒充所有数值求积、反解、舍入和三角函数求值的总误差。网格未声称具有严格的连续图 Hausdorff 误差条。

## 5. 从冻结图复现

以下命令在本题目录运行；输出 stem 可换成新的审查 stem，避免覆盖已冻结报告。

```bash
python scripts/db6f-export-closed-mesh.py plan \
  --geometry notes/2026-11-09-db6f-root-flat17-common-cut-m8s32.json \
  --whole-certificate notes/2026-11-09-db6f-root-whole-metric-reach.json \
  --out-prefix notes/2026-11-09-db6f-visible-m8 \
  --angular 144 --prefix-intervals 128 --tail-intervals 64 \
  --collar-intervals 4 --cap-intervals 12

node scripts/db6f-tail-sample-background-height.mjs \
  --manifest notes/2026-11-09-db6f-tail-int2-flat17-m8-q10-n8-s32-manifest.json \
  --calibrations notes/2026-11-09-db6f-tail-finite-source-calibrations.json \
  --alpha notes/2026-11-09-db6f-tail-tight-alpha.json \
  --radii notes/2026-11-09-db6f-visible-m8-radii.json \
  --out notes/2026-11-09-db6f-visible-m8-heights.json \
  --source-root repro/source-root

python scripts/db6f-export-closed-mesh.py build \
  --plan notes/2026-11-09-db6f-visible-m8-plan.json \
  --height-samples notes/2026-11-09-db6f-visible-m8-heights.json \
  --out-prefix notes/2026-11-09-db6f-visible-m8

python scripts/db6f-audit-closed-mesh.py \
  --mesh notes/2026-11-09-db6f-visible-m8-t0.ply.gz \
  --out notes/2026-11-09-db6f-visible-m8-t0-audit.json
python scripts/db6f-audit-closed-mesh.py \
  --mesh notes/2026-11-09-db6f-visible-m8-t1of4.ply.gz \
  --out notes/2026-11-09-db6f-visible-m8-t1of4-audit.json
python scripts/db6f-audit-closed-mesh.py \
  --mesh notes/2026-11-09-db6f-visible-m8-t1of2.ply.gz \
  --out notes/2026-11-09-db6f-visible-m8-t1of2-audit.json

python scripts/db6f-audit-mesh-family.py \
  --manifest notes/2026-11-09-db6f-visible-m8-manifest.json \
  --out notes/2026-11-09-db6f-visible-m8-family-audit.json
```

原始 gzip PLY 的三项 SHA256 均列于 manifest；全部新交付与审查文件的字节数和 SHA256 列于独立 publication inventory。无需从对话恢复任何数据数组。
