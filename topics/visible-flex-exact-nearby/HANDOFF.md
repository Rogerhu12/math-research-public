# 交接：可见振幅的精确闭等距族

维护会话：`visible-exact-astra-ac637-20261120`；更新：2026-11-20 09:35 UTC。
**总任务未完成；继续研究，不等用户回复。**

## 规则读点与接续来源

部分克隆：`/workspace/scratch/ac637cfcc78d/math-research-public`。终端 git 已恢复，无 AGENTS。
2026-11-20 09:32 UTC 实际 `git pull --rebase --autostash origin main` 至 `96edc677044b6ad7c7fd3aa2f65bf77d9c0e27a1`；已读根/题 README，已读规则提交同上。相对前会话最后读点 `d86a3e8e`，根只新增 held-10pct 课题行，题 README 不变；本次拉取两文件 diff 空。每次 pull 后继续核两 README 差异，下一次实际 pull 不晚于 10:32 UTC。

接手前完整 H（含全部递归原页、成功/失败/恢复身份和未付义务）见 [2026-11-16 完整检查点](https://github.com/Rogerhu12/math-research-public/blob/882aa9b74efeaac682df43c197820e7280156357/topics/visible-flex-exact-nearby/HANDOFF.md)。本页只压缩索引；`open.md` 及所链接的原证明、适用域、均值、物理角、所有边界和误差费用继续有效。旧成功结论不重算。

新科学数值用本公开仓库 Actions；本机用于证明、编辑及静态检查。每条实质结论更新 H 并独立提交推送；推前实际 pull，非快进立刻 rebase 再推，不 force。规则15：只留脚本、参数、run、hash 和小结论，不入库新数组/可重算证书，topic≤200 MB。

前会话自设的全部活跃工作流静态白名单导致纯只读运行被他题阻断，非数学条件。根规12不要求这道行政门。本会话改为每次发布前在实际 rebase 后精确计算整个 topic 与输出字节数；竞争 push 后重算。数学输入、21个原件身份、mean/ports、50个新目标及 false 门一律不改。

## 完成标准与当前同一对象

须同一连通闭曲面上的固定度量、C² 连续的精确 C² 嵌入族；材料握持区 H 有内点并逐点固定，diam F0(H)≥.2D，held≥.05D，含反射的 δE>0，全族 reach≥.03D。不得把小振幅、有限截断、条件逆或障碍算完成。

继续原 candidate `ac1d5b98…`、连续 Qrepair `440866a3…`、Zdef `6a71cb81…`/native `87ed2f61…`；完整身份在原 H 和对应 proof。
α=6890507429876859/9007199254740992；ν0=−2572625729470897/72057594037927936；η0=−7789843107295549/4611686018427387904。真实物理角与独立 mean 不变。

geometry `43584188751/26` **仅条件性**：同η0真 wholecore（含帽）C0≤1e−4、|δν|≤1e−5以及全部 B/C/Cmean、腰 u0、第四 Robin、mean、phase、γ入口和 matching 后，held>.05075888242D、reach≥800D/25039、Hdiam≥360D/511，静态非共面 marker145..148。完整 core/全频逆尚未有，故不能据此宣布达标。最后只能全部匹配后一次冻结 ν*/Γ*/η/metric；不能把变ν的IFT当固定metric族，purephase只有刚体。

## 已有可复用的正侧链

- WIC：原 m160 真 tail 的全系统逆界 κ=3、N=24480 已证。完整 reference、ρ2、193 mean/head、97 root+96 outer、7 ports、两 RHS 资格保留。
- WPN：若同完整算子的 e+3dt<1，才得到双边 Neumann 逆、两 RHS 误差和指定 root-even I96。实际小门未过。
- WPS60、WVC56、WCTRA：完整既成数值分别给约635240.55、11066.29746、11976.30849 的充分门，均 false；不能反推算子奇异。已成目标不重算。WCTRA不替换本轮固定WVC参考。
- W2H/W2C：固定 WVC 上的双侧 collar-Volterra 候选，V=Vb+ψ(JB+JAJB)，W=Wb+ψ(−JC*+JA*JC*)。真 J* 积分上限 R；两 collar residual 二阶，transition、family Δ、true dual H1 和 mean 均完整。
- WJK：F=P+Q*−Q*LcP，body 的 χ′只在共同Gf下的完整 signed centre 核精确消；actual 两 residual 不删。必须同(r,s)合完整有符号核后再 abs；不能用旧171加正项冒小界。对应五 collar 项、两 Green 三角、193 atoms、7 ports 和两 RHS 全保。

相关 proof 是 `results/R133-supplement-{analytic-inherited-tail-and-weighted-impedance-circuit,complete-paired-Neumann-reconstruction-and-root96-normalization,complete-collar-Volterra-dual-feedback-candidate,joint-centre-Green-kernel-and-complete-collar-cross-terms}.md`。

## 接手时真实执行停点与当前分工

前会话最后自动 commit `56bb641c2` 保存 `43921663540/1`：23 AST 已过；native恢复前因他题 `serre-source-publication-recovery.yml` 未列白名单而停。readonly/science 均 false，science child0，目标0。原 execution/report 在 `notes/collar_volterra_dual_readonly_ci/run-43921663540-1/`。没有科学成功可冒认，也没有新目标需重跑。

当前模块：owner `fourfold_codazzi_collar_volterra_dual_candidate.py`；完整输入恢复/执行为同前缀 `public_worker.py`；reader 为 `readonly.py`、`readonly_core.py`；math 为 `true_collar_signed_packet_math.py`、`signed_semiseparable_kernel_math.py`、`collar_dual_feedback_math.py`、`W2C_signed_reference_math.py`（都在 scripts/）。完整 native 数据与29整球仅恢复旧字节，不调用旧 producer。

1. `joint_kernel` 补 `collar_dual_feedback_math.py` 的 graph4 稳定联合核压缩，保留所有 collar 项与真实 Gf atoms；此前递归高秩 generic 后端尚不适合科学 launch。
2. `positive_inverse` 研究把同 WJK 中心核直接并入参考边值系统：1217维一阶 ODE、609个自由初值/终端方阵；这是新推导中的候选，尚无实际可逆证书，不授全逆。
3. `global_route` 核查真正core/腰/ν/完整frame匹配与可替代结构，避免重复已证明的条件Schur。Ghomi等正亏格等距嵌入族不是已知连续弯曲；R520仅小振幅，均不替本题验收。
4. root 维护 main/H/open/results/log，修复无关工作流阻塞，准备新公共运行并追踪结果；代理不动git。

## 正侧以外仍未付的接口

完整列表和精确范围见 `open.md` 第2–7节，特别保留：
- 真实physical有限列、全部cross/pairing、square逆、Θ96、两physicalmean、ν Schur、负体/无限radial head；193角纤维不是整个radial head。
- WDH只给 selected homogeneous 右预条件高块（J=2^4608，χ<2^-44、逆<2）；finite补J−1及所有上述接口仍待，不是全物理逆或all-s估计。
- 同态两侧H1/fullmean/true residual0/wholeC0，以及 NG 迹门 385cL+min(145ZS+748ZL,489ZS+10ZL)≤9.5e−12 尚未actual通过。
- 真qν在负窗的控制、第四Robin/腰/mean/phase、D² tame与smoothing、增广非线性迭代；旧q*不是PDE响应。
- S/T只在原γ A0/H8193窗口给连续选解；loss1734/bg1796/E1856、94seed后Γ2及原极小种子等范围不扩。不得从局部帽/右collar估计推wholecore。
- 全部B/C/Cmean、height、holonomy、position周期、单一frame及腰镜像匹配后，才可应用几何比例结论。

任何新增界、源代码补全或路线排除均仅关闭其明确子问题；最终精确可见族尚未构造。
