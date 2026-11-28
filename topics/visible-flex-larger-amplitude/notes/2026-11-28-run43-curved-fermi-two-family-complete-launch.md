# Run43 — 同一 R757 固定度量的双家族完整物理 Fermi 求解

会话 Astra-larger-e4e2a2bf-20261126。**这是新实际任务的完整交付与普通触发；实际 run、点、所有测量等待公开 Actions 原程序返回，课题未完成。** [R757](../results/R757-curved-section-and-nonflat-caps-on-a-fixed-closed-metric.md)规定真正弯曲剖面、非平两帽与同一个完整初始度量；[R759](../results/R759-elliptic-rim-sign-and-paired-curvature-tracks.md)规定另一种准确中央运动。与42、R758、R760的初始度量分别不同，不互借误差或精化。

## 完整原范围

保留原七个移相启动，另加三个真实成对轨道启动：角度 .78/.795、上升与下降区各2或3胞。两家族分别选有限评分最优者，分别完成4、8、16时间区间和全部独立空间/频率精化，共10粗+6细=16个完整阶段。原L-BFGS-B预算为52/64/76/92次迭代、maxls24、maxcor15、ftol2e−12、gtol2e−8，不加子进程时长截止。每个最终原点分别完成65个时间检查与七个指定相位整闭网；两组各有独立closed-geometry-index，原NPZ/PLY留原公开runner并保存完整身份。

物理域为一个九图闭曲面：全部中央、两整卷、两帽全部内部及完整公共缝。保留19个实际形状/刚移参数、两卷独立三个空间方向、钳制分数次幂与新的曲壁原子；成对族另有每个完整帽的三方向多项式系数。每次拟合后的两材料图以完整全部射线行重建；分块线性代数只减少工作内存，不删行、不删方向。损失包含实际全帽Gram，并独立返回重建后全部九图的相对Gram、曲率、support、缝二jet、材料Jacobian和全部射线guard/clip。

各阶段训练/独查的射线数为23/59、39/81、57/111、79/149，步数为72/143、104/207、144/287、200/399。独查使用RK4，训练使用原中点格式。包含真正弓胞所有符号/拼接断点，以及延迟径向角的16个内部位置；所有实际费用仍按固定初始g计算。

## 射线离散修正的准确含义

42的原独查已经返回零物理Gram而Jacobi误差约 .3273、导数误差约2.1034的情况；原完整结果保留，原任务继续。43用已知裸几何的真实法测地/Jacobi解作背景，直接积分真实物理几何系数与裸几何系数之差；每个RK子步直接计算真实径向d、d′、d″。背景曲率及其导数用32769加真实节点的一维表，实际非零场仍进入完整非线性Gram、Christoffel和Gauss曲率差。

这使裸几何的零扰动准确相消，并不等于所有非零射线已获严格误差界。旧移相族launch+advance未必恰在曲率表节点，非零射线仍有一维背景插值及扰动表插值误差。每阶段保留原双线性表历史校准，实际全域Gram独立从物理六jet量出；不把平衡后的零漂移当作原插值精度已证明，不把有限guard无触发当作全域非聚焦、单覆盖或嵌入证明。

## 已知数学限制与真正继续方向

R759的正Gauss曲率条边界第二基本形式同号结论，已经严格排除原七个移相中央在非零移相下的准确闭合极限。仍按承诺保留原完整预算，记录其实际有限行为。

成对族避开上述号障碍，但当前未加末圈自由度的平行卷在末圈具有
$g_{ss}(L)=(1-d_b\kappa_\varphi(s))^2$，目标为$(1-d_b\kappa_0(s))^2$。钳制的卷内部三方向、帽内部gate、刚性帽pose及其等距发展不能改变这一圈的材料角行；在所选非零轨道角保持时，负胞末圈还有真实未付费用。若优化把中央角降回零，必须同时如实检查强位移，不能以去掉形变换称完成。后继将释放两卷末圈与两帽整圈**同一个物理三向位移及横向二jet**，而不是继续只加内部模式。本次原科学过程不在运行中换点或改预算。

## 整文件身份与执行

21个科学输入、19个既有科学/控制父件的精确路径和全SHA见[完整请求](../computations/run43-curved-fermi-phase-request.json)与[完整交付](../computations/run43-complete-curved-fermi-source-and-launch-delivery.json)。全部新件如下；最后两个元数据互相不递归嵌入自己的哈希。

| 文件 | 字节 | SHA256 | Git blob |
|---|---:|---|---|
| scripts/resume_20261128/bent_curved_fermi_phase.py | 16130 | `2635ab9b36002b353e1f0aaf5c5936452aed5bcfa75a150fc06a495c41d2dfc1` | `bb8c676562bb3afca63d61fc9a16875228d2c7d3` |
| scripts/resume_20261128/bent_curved_hard_end_fields.py | 15892 | `28493b189b67a12393a8aa0c1cd1fa67a1c6f6e8a298a531766395a74766f94b` | `ae676490bc188e5b7f9307ef2d8efcb5b508c525` |
| scripts/resume_20261128/bent_curved_fermi_shoot.py | 20349 | `a7c83d0e426ebb9e74f02afc110790bdd59bad68ab2ffb9bbc4d23f44a12870a` | `18f9fc8529caa96acbacb90214fd1f7aae88a6ee` |
| scripts/resume_20261128/bent_curved_fermi_reconstruct.py | 5369 | `7b02529d61b0dade2eae09704384d15fb115de293290700cf52ee813d30e07a9` | `da5b63356e49eefe5ed2510b39f3751efe9a5eb7` |
| computations/bent-curved-fermi-phase-design-v1.json | 8065 | `ab92d14cc2a0c7991092b139053a13c728496e9a4501b1506b380b45966611dd` | `e237691ee9ee9dfb9ee67bae0c38456a61820a44` |
| scripts/resume_20261128/observe_bent_curved_fermi_search.py | 17205 | `72838930500b11881e35748120073152e7109972a2643afe2f3459944166263c` | `277b9f77d4c7661eb7e7cd0a6421289fd65f821f` |
| .github/workflows/visible-larger-run43-curved-fermi-phase.yml | 4663 | `a74e8d037bdf76b236acd62ff21bac4341b5aaab76013dbf19f2829736c3b962` | `0dd187843b753b5b51c697e57af0e32d1f3402f6` |
| computations/run43-curved-fermi-phase-request.json | 26058 | `24fcf4fc813c095918bb4f08b92b1a8948ee6be549b04758f3e45ab5d0693c07` | `88afb87793b72259893257c46c1e6fc68375bcbc` |
| computations/run43-complete-curved-fermi-source-and-launch-delivery.json | 25990 | `69711ee1b2f53d682b39b10de1b9ca1a01694d48a3fb3ab6808946d2bfbe9e89` | `76d8b8ec677a67a220edab700c0fcd59a49bccd4` |

公开Actions固定Python3.12.14、NumPy2.3.5、SciPy1.17.0、JAX/JAXlib0.7.1、CPU float64、每数值库单线程；原360分钟平台job预算，不加入额外截止。trigger SHA上的科学输入保持不可变，发布分支另做普通pull/rebase；2700秒真实pull后检查根与本题README，仅读差异并立刻执行。NFF立即拉取整合再推，禁止force。每个真实阶段与两个终端索引均原文小件发布；可重算完整raw按根§15只留runner并给全身份。未运行的actual字段明确为null。

完成仍须全域相对度量算子≤1e−6、同g/参数/全t真实精化收敛、闭连通C²强连续嵌入、全t reach≥.03D、固定有内点握径≥.2D、整初像距离≥.2D及含反射刚体商距正。此交付和任一有限校准均未替代这些条件。
