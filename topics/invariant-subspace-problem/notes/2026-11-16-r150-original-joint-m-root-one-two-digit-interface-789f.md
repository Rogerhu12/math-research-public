# R150 原共同 M：根一剩余 socle 的完整两层入口

作者：ChatGPT（AI），literature_audit；2026-11-16。

## 1. 目标与严格停止条件

令 $D=\mathbf Z_{(31)}$、$p=31$、$M=\sum_{j=2}^{10}D[s][t_j]$。此前完整原商与 primitive 资格已付根一完整系数扭子 $T_1\simeq D/p\oplus D/p^2$，并且原九目标的剩余域像只是一条自由直线，由原 $f=[t_2]$ 生成，初始系数扭子坐标全部为零。因此

$$
S_1=M_1\cap T_1\subset pT_1\simeq D/p.
$$

本入口处理原 $t_3,\ldots,t_{10}$ 相对于 $f$ 的八个差；原 $t_2$ 保留为自由生成元。完整读数只有两个可能结果：八个实际二阶方向全零则 $S_1=0$，否则 $S_1\simeq D/p$。不以选定来源的受限零代替这条完整性结论。

## 2. 中心一必须真实生成

新 common、VQ、normal、transport、integer 源使用纯 Taylor 参数 $t=s-1$。原全局 G/V 来源 DAG 在这个中心重新求值至十阶；没有读取或重新标记根二 G/V。

普通整数 Taylor 幂为 $(1+t)^d$，系数是二项式系数。共用 CRT8 输出仍保根一的前三项和根二的后五项，但本次原剩余只放入前三项，后五项明确置零。原来源类型 kind=2 的物理含义不变；它不是 Taylor 中心。所有原 6188 来源行、4367 输出行、4433 原整数系数及普通平方对角/非对角约定保持。

整数乘回独立使用已经审核的模 $31^{12}$ 算术和 128 位累加界。这里只需要除 $p^2,p^3$，较高系数模数不扩大所声称的 Taylor 范围。

## 3. 两层充分性的原模证明

在根一的真正完成模内，$f$ 的自由像 primitive，故该有理自由直线中的整格为 $\mathbf Z_{31}f$。第零层对每个原目标 $W$ 核

$$
W\equiv a_0f\pmod{pC_1},
$$

且完整两个真实扭子方向的坐标均为零。实际求解全部 1034 原 G 行，运输到全部原来源，再在全部原输出核

$$
p^2(W-a_0f)-A(p^2q_0)=p^3r_1.
$$

十项有限解保留五项真正稳定前缀。完整原参数根一扭子由三项 Taylor 观测已完全检测；入口重新核这个原 315 作用事实，而不是直接假设。

第二层从完整 315 商读取

$$
r_1\equiv d_{11}g_1+d_{12}g_2+a_1f\pmod{pC_1}.
$$

这给真正完成模身份

$$
[W]=(a_0+pa_1)f+p d_{11}g_1+p d_{12}g_2+p^2[r_2].
$$

$p^2T_1=0$ 且自由直线 primitive，故最后一项只改变自由坐标的更高部分。$pg_1=0$，所以完整扭子坐标就是第二个方向上的 $p d_{12}$。这既解释了两层足够，也说明没有把自由尾补零。

根一的真实 $U_2$ 基仅从已付完整 $U_{16}$ 的根一投影选取。代码重新核完整 $J U_{16}=U_{16}J_{16}$、全部根一分量都落入这两个方向、指数为 $(1,2)$、总长三。第二层不需要新高阶除源：$p$ 乘一个指数二方向时，改变其 lift 的 $p$ 倍部分已被 $p^2$ 杀掉。

## 4. 全部必要核验

每个实际整数剩余保留全部原行和来源，完整 ordinary-square 字典与原方程缩放同时检查。两次原剩余及中间零类都通过 CRT8 到原 820 状态，再核 104 个局部自由条件、39 维局部重建、全部 315 坐标、505 个原自由条件及原参数作用。

第二层用原根一七维参数主分量的完整 basis 解重建，不套用根二的局部左逆。实际末类仍必须落在两个真实系数方向加自由 $f$ 的三维剩余域空间中。任何失败均如实保存，不升级为数学零。

已付 $x^2h_*M=0$ 且 $x=s-2$ 在根一为单位，故 $h_*M_1=0$。$h_*$ 在根一只有一个简单 Hensel 根，因而 $M_1$ 由九个未移位原目标作为 $\mathbf Z_{31}$ 模生成；没有遗漏参数作用闭包。有限 $S_1$ 若非零，被 $p$ 及 $s-1$ 杀掉。

## 5. 源、输入与运行

主源为 `2026-11-16-r150-original-joint-m-root-one-complete-two-digits-789f.py`，31388 字节，SHA256 `9a1188f53fa0a64185e0db3c163231f134d21f0fb5d66718a70f425fe79226d8`。

六个独立中心一 helper 的完整 SHA 在该主源的 `SOURCES` 字典中固定；其余 original dictionary、exact model、Schur、状态读出 helper 仍固定原 SHA。新源并不改写任何根二来源。

本地使用以下已经实际保存并完整核 SHA 的输入：原十个 G/V/NF/F/B/状态文件；原 primitive 整数方程；原 CRT8 quotient map 及回执；完整共同 M 资格回执和临时数学数据。资格回执为 20106 字节、SHA `9b8c104b8cbd9d7fbe17c7e6fbddd1067c66d6a6a17252ed9c8f854b7cd2a2a7`；对应数据为 2112889 字节、SHA `a7a21b4c00e306ee0278451217491aedf88c6bcb59c3ca23668198516a74a29d`。它们的旧父身份如实保留，不伪称本入口重跑了 full210 或 p9/50 来源链。

若在新环境运行，必须先重建同一实际资格数据或显式固定新的完整合格父，不能仅凭数据 hash 假定临时文件存活。本次直接在已核本地目录运行。

```sh
PY=/tmp/r150-normal-789f-20261116-1040/venv/bin/python
OLD=/workspace/scratch/789f3e887d7c/literature_root2_789f_work
$PY /tmp/literature_joint_m_789f/root1-source/2026-11-16-r150-original-joint-m-root-one-complete-two-digits-789f.py \
  --notes-root /tmp/literature_joint_m_789f/root1-source \
  --original-input-dir "$OLD/global197-original-inputs" \
  --exact-gzip "$OLD/original127-inputs/original-primitive-integer-equations.json.gz" \
  --jet-map-dir "$OLD/root2-fourth-jet-map" \
  --qualification-receipt /tmp/literature_joint_m_789f/qualification-paid-full210/original-joint-m-primitive-lattice-qualification.json \
  --qualification-data /tmp/literature_joint_m_789f/qualification-paid-full210/complete-original-joint-m-qualification-data.json \
  --out /tmp/literature_joint_m_789f/original-joint-m-root1-two-digits \
  --seconds 600 --memory-mib 2048
```

每阶段原子保存输入绑定和完整输出 SHA；预算退出 75 可以同绑定续接。主回执名为 `original-joint-m-root-one-complete-two-digits-receipt.json`，完整末坐标文件为 `root-one-complete-two-digit-coordinates.json`。数学数组只留临时目录，仓库只保存源、参数、执行身份和正式证明。本接口未预填 $S_1$ 的实际分支。
