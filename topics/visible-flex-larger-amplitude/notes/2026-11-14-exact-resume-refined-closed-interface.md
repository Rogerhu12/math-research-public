# 背景保留四级尾接入有限闭组装：实际接口与可移植执行链

作者：exact_closure，GPT-6 Astra Pro，AI 辅助。2026-11-14。

执行环境更新：06:15 UTC根README已停用旧公开代跑，本条不新增任何ci-queue；保留既有CLI文件名作为本地/迁移后仓库的可移植入口。以下完成状态是接口交付时的真实记录，后续本地全闭运行另行记录。

本条把已经测得较小误差的 2305 节点、同 g、RK12 背景保留尾场接入既有闭组装的参数化规则。新接口保留原真实物理 quintic 前缀，外端在尾半径坐标上作固定宽 `0.01` 的完整向量二 jet 修补；内端保留原有限 Hermite collar；帽上采用已推 [R14](../results/R14-arbitrarily-weak-gaussian-cap-markers.md) 的四个弱固定标记。

**已经实际完成的部分**是 plan、201 个原背景点的 native primitive/jet 取样、原前缀真实 cut 与新接口的完整二 jet 对照、以及三个既有误差见证子段的表示一致性读数。完整全局均值积分、闭网格和全相位法向弦样点检查已写成 CI 长链，尚未在本条执行；本条不报告它们已完成。

## 1. 可复用接口

新文件为：

- `computations/exact_20261114_refined_tail_adapter.py`：惰性读取完整 Cartesian 节点，保持共享非均匀水平 rr；提供 `RefinedTail`、`RefinedAssembly`、实际 prefix/collar/tail/cap jets 与任意实数相位的 `phase_jets`。
- `computations/exact_20261114_refined_closed_assembly.py`：`plan` / `render` 两个入口，沿用原 mesh 拓扑和材料角反演规则，但不使用旧 integrated-Fr 文件格式，也不在前缀上添加旧宽 `0.1` 的补丁。
- `computations/exact_20261114_closed_background.mjs`：沿用 `createStoredPhysical` 的全部 160 个保存校准和全局 warp alpha，评价原源背景和 native primitive，不重新校准或运行非线性尾 ODE。
- `computations/exact_20261114_ci_closed_assembly.py`：可在本地或迁移后仓库执行的长链封装，保存实际 argv、启动源哈希、退出码和终态。
- `computations/exact_20261114_refined_tail_interface_check.py`：本次轻量实际接口读数的复现入口。

节点导出仍保留源背景 $h_0'(r)=w(r)$、$h_0''(r)=w_r(r)$，只对小 Cartesian 扰动做 Hermite 插值。直接累计的 small mean 坐标包含在同一个扰动函数中。转换为 Fourier 系数后采用正频幅值表示

$$V(r,\theta)=\operatorname{Re}\sum_{k=0}^{256}c_k(r)e^{ik\theta},$$

其中偶数网格的 Nyquist 项按单个实余弦解释。这样任意相位的角导数和混合导数均来自同一个有限函数；没有在网格之间另外拟合角 jets。

## 2. cut 直接消费原 prefix Fourier 系数

原 cut 已处在材料角图为恒等且其前两阶径向角扰动为零的区域。因此可以直接将保存的 cylindrical Fourier 状态及其物理 quintic 一、二导数转换成 Cartesian Fourier 系数，再用真实 $r_s,r_{ss}$ 换成径向 jets。没有对 prefix 的 512 个位置样点再次做 FFT。

这消除了前次样点表示在纯角二阶上的约 `9e-12` 二义性。在同一个 cut mean 锚为零的框架下，本次 1024 角对照得到：

| 原 prefix 与新尾 cut 的差 | 最大向量范数 |
| --- | ---: |
| 位置 | `1.118863024879935e-16` |
| $F_s$ | `2.486410087150353e-16` |
| $F_{ss}$ | `4.450098274550997e-16` |
| $F_\theta$ | `1.1102230292780475e-16` |
| $F_{\theta\theta}$ | `1.1188630310358827e-16` |
| $F_{s\theta}$ | `2.482534390000168e-16` |

上表的尾侧使用相同 $r_s,r_{ss}$ 换回前缀 s 坐标。内端 cuff 的位置、一阶、二阶和两项角 jet 的扰动读数均为零。作为共享有限 Fourier 系数及 Hermite 多项式的定义，端点条件由构造给出；浮点评价的非零差仍按原样保留。

这次接口检查只使用 cut mean 公共锚，不假装已经计算全局 prefix mean 原函数。CI render 将用原保存五次曲面的 span-wise Gauss6 积分、完整 mean 角规则 `max(512,16*(3*M+1))=1552`、唯一的 `s=0` 锚计算绝对高度。只把原积分函数的 evaluation batch 从 128 改为 8，不改变积分式、正权重、原 knots 或 mean 定义。

## 3. 已测尾场的表示一致性

Fourier 变换与 Hermite 插值在精确线性运算下可交换；两种浮点求值顺序仍可能有差。因此实际消费此前的原 metric/curvature 见证子段，以及外端补带 metric 见证子段，各取原来的 17 个径向点和 1024 角进行对照。

| 子段 | 新旧未补 $F_r$ 差 | 新旧未补 $F_{rr}$ 差 | 新补丁后 metric 算子范数最大值 |
| --- | ---: | ---: | ---: |
| 43，外端补带见证 | `1.697e-16` | `3.588e-12` | `6.217889746901072e-8` |
| 111，原全尾 metric 见证 | `1.021e-16` | `1.370e-12` | `7.292281634097009e-8` |
| 1625，原全尾曲率见证 | `7.202e-21` | `5.686e-16` | `4.504e-16` |

三段上最大角一阶表示差不超过 `1.82e-18`，纯角二阶差不超过 `3.72e-16`，混合差不超过 `2.31e-14`。表中的 rr 差是有限运算顺序差的实际量级，没有被写成严格全域误差界。三个子段的检查不能替代新接口上的完整全域最大值。

原源背景 201 点取样用时 `12.20252` 秒，实际退出 0；最大反演半径残差 `2.7755575615628914e-16`。160-cell native primitive 总高度为 `0.022684311165528714`，只是 rotational background 的数值原函数代表。cuff 的未计深部 rotational primitive 另存原 R28 的条件量级，非轴无限尾仍未构造。

完整接口读数用时 `37.67023` 秒，实际退出 0。结果见本 note 同名前缀的 `-check.json`；plan 为 `-plan.json`；原背景样本为 `-background.json.gz`；实际结束记录为 `-terminal.json`。保存的 plan 来自接口开发期间的同一算术版本，其源哈希保留原启动身份；最终 CLI 后续只补上实际 tail-response 身份检查和 metric 算子范数报告，CI 会从最终源重新生成自己的 plan。

## 4. 全 phase、上下半片、固定帽与 mean 规则

对活动区保持

$$F_\alpha(s,\theta)=R_\alpha F_0(s,\theta-\alpha),\qquad
\alpha=\pi t/2,\quad 0\le t\le1.$$

前缀材料角总经 `SavedPrefix.inverse` 反演，未直接平移数值 eta 图。完整下半片是完整上半片的 z 反射；有限 tail 的 source background 和 small mean 一起反射。所有帽和公共 cuff 对全部相位保持固定，输出网格直接复制相同的固定顶点。任意实数相位有明确求值接口；选定 mesh 角网和 9 个 phase 采样又使对应材料移位恰落在角网中。

固定帽采用 R14 的原式：$k=1/160$，第 i 个支撑半径为 $r_c/(8i)$、主曲率上界为 $i^2k$；三个上帽中心为 $(r_c/2,0),(0,r_c/2),(-r_c/2,0)$，下帽中心为原点。四个凸起高度均为 $kr_c^2/512$。当前 cuff 约 `0.05`，所以最大 marker 曲率为 `0.1`、公共高度约 `3.0517578125e-8`。

R14 对旋转内蕴 g 的 Gaussian 曲率纬圈性质给出**精确极限的条件工具**，不要求 marker 主曲率超过活动主体。本接口没有宣称当前尚有等距误差的有限图已经恰有四个严格 Gaussian 极大点。两固定帽的并集可作不连通的 H；实际直径仍由组装结果计算。

## 5. 可移植执行与预期产物

根统一 prepare 恢复 91 个 pinned source 文件后，安装 NumPy、SciPy 即可执行：

```sh
python -u topics/visible-flex-larger-amplitude/computations/exact_20261114_ci_closed_assembly.py \
  --source-topic "$SOURCE_TOPIC" --out "$OUT_DIR"
```

默认链只绑定当前原 A：原 577 节点 readout → RK12 真正内部加密到 2305 节点 → plan → 原 source background → 全 mean 与有限闭网格/phase/pairs。大的节点侧件保留在 `RUNNER_TEMP`，`OUT_DIR` 只接收网格、normal 样本包、报告、输入哈希和实际退出记录。没有使用未提交的 prefix 原始 pickle；原已提交物理 PPoly 及其系数块足够。

当前显示 plan 有 `73634` 个顶点、`147264` 个面；单个未压缩 mesh 大小上界 `3759378` bytes，小于 5 MB。将保存 $t=0,1/2,1$ 三个 mesh，并读出 9 个 phase 的像距离样本。法向弦检查分为 moving/moving、fixed/fixed 和 moving/fixed：前两者在共同刚体转动下不变，后者调用 R11 的连续相位消元。全部输出仍是选定空间样点的有限筛查。

未来实际候选已有自己的相同格式完整 readout 时，可以显式传入 `--complete --config --checkpoint --port`。CLI 不允许把自动恢复的原 A 尾移植给另一候选；它还检查完整 readout 绑定的是该接受 prefix 的 actual tail response。对新 provider/非零 frontload，调用方仍须按现有专用 loader 恢复正确 flow；公共 `RefinedAssembly(saved,...)` 可直接消费该正确 saved 对象。

## 6. 尚未支付的事项

当前原 A 幅度未达本题要求。内端 finite collar 具有非零 metric 缺陷，既有无限非轴尾与准确共同 g 极限缺口保持显式。本次没有靠缩 collar 或增加深度把它称为准确解逼近。完整 phase 公式、闭网格拓扑和有限法向弦样本也不能单独证明连续嵌入或完整 reach；这些内容应由 CI 的真实结果继续推进。
