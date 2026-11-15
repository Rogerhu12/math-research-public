# R150：18 右端原常数单位块、补齐低阶来源与完整第四连接

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。

## 1. 状态与冻结文件

本入口沿同一自然参数 $u=1/s$、同一原行列集 $I,J$ 和同一所选方阵 $B(u)$。原 4318 常数单位块及 18 右端准备已实际完成。Python 新入口真实 AST 已通过；此处尚不报告原生求解或新来源的数学结果。

| 文件 | Git blob | 字节数 | SHA256 |
| --- | --- | ---: | --- |
| notes/2026-11-15-r150-third-missing-four-constant-unit-pipeline-789f.py | 088ce8a4a478b87184e3e4b01203ecfdc49a28d5 | 56964 | 15b4fcae4f8e251971d1eb9d79ba9802cea75c7f16e0484cce63ebf073a3c538 |
| notes/2026-11-15-r150-constant-unit-multiple-rhs-dixon-checkpoint-789f.cpp | 60d874f2b77932609289cdeaac69392de1ccc997 | 19136 | d592f2086e81be2206adb67c7553de15ce36d49a9d1e62721a47a469d8afece2 |
| notes/2026-11-15-r150-third-missing-four-eighteen-unit-preparation-789f.py | dfe99d639d2b66ca41a6e82ead1707078a134f9a | 11587 | 8e2b059af823dd8fc089470f5d20c930649ae1fd8e4ae695626ba6b88048d2a7 |

实际 18 右端准备数学时间 1.072890655 秒。原回执 2628 字节，SHA256 a692c7c920346fc5473fd8ee662b08d91c709682a1cca7dfb8a7efe8342cf36b；binding 为 25c4d03014a3754e6b5b22d1ae1d7d8835708a53092b7d2e5b923d151ecebab8。

实际输入 constant-unit-eighteen-right-hand-sides.json.gz 为 9305373 字节，SHA256 c2d645d0d59aa565c5aea537f66a3e3ba671dd0088f7dd9f3dfde65846405819。完整原 Mstar 模型 5245792 字节，SHA256 cbd7329c2447a6f44a5b8f93a9ba7906c702e5193212cfd4a12137c1b98ce658。

所选旧 HF/T 列零基索引为

$$
(0,1,2,13,14,18,20,25,26,28,29,30,31,32).
$$

它们来自已成 166 列有理残差 RREF 的前 36 列主元，模旧 $M_0$ 独立并张满旧 36 列的像。再商完整常数像后，仍张满完整 12 维来像。实际 primitive 模 31 秩只有 4，源码明确保留该事实，不预设某 12 列模 31 独立。四个目标对应已付 21 头坐标 $(15,18,19,20)$。

原单位块有 172861 个非零项、原系数最大 132 bit；四个目标右端最大 3824 bit。没有重新计算旧 4318 选元、旧 1736 高块、旧 786 个 pivot 或 906 个高来源。

## 2. 范围和常数单位

原式核验在这里指 $B(u)$ 的全部 4354 个原来源方程。左 cochain 每层保留 4367 个原输出坐标，并核其在 $I$ 外为零。不得将此写成全部 6188 个原来源方程的左恒等式。

已付 $B_0$ 的 $\mathbb Q/\mathbb F_{31}$ 秩均为 4318，完整前三连接秩为 $(3,9,3)$。第二、第三头空间维数分别为 24、21；此前真实 cochain 只有 22 条、17 条。

令

$$
M_*=B_0^T[E_{\rm new},E_4,E_5],
\qquad1546+1485+1287=4318.
$$

这是完整常像的来源基。已付原模 31 来源核 $\overline K$ 在自由原来源坐标 $F$ 上为单位阵。取 $R=J\setminus F$：若 $\overline M_{*,R}x=0$，则 $\overline M_*x$ 仅支撑 $F$；配 $\overline K$ 后该分量也为零，所以 $x=0$。因此同一原方块在模 31 和 $\mathbb Q$ 上均可逆，不需要先恢复七条未知的有理常核。

准备文件中的正行、列 content 满足

$$
A'_{ij}=(M_{*,R})_{ij}/(g_i h_j).
$$

原生程序解

$$
\operatorname{diag}(g)A'Z=-W_R,\qquad x=\operatorname{diag}(h)^{-1}Z.
$$

右端不要求被 $g_i$ 整除。Dixon 递推在内部单位素数下计算 $N_i/g_i$，实际逐行核整数整除；内部素数不是新的数学秩证书。$g,h$ 不得在源恢复中重复相乘。

协议 R15CUM01/version1，实际 $n=4318,m=18$。原生解只核单位行的 77724 个产品；外层还保留全部 78372 个原残量坐标。

系统独立 libflint-dev/libflint22 3.4.0-1 已实际安装。编译默认 g++ -std=c++17 -O2、链接 -lflint -lgmp；运行另记实际 header/runtime 版本，不用 Python wheel 代头文件。编译独立限 30 秒，数学共享 600 秒、每进程 4096 MiB。

## 3. 18 列原残量

前 14 个右端为 $W_j=F_{p_j}/c_j$，其中 $F=[HF,T]$，$c_j>0$ 是原列 content。最后四列为已实际保存的 $q_t=(R_3Z_t)/g_t$；不能再次除 $g_t$。

将恢复原来源尺度的单位解写成 $x_j=N_j/D_j$，$D_j>0$。逐 4354 原行保存

$$
S_j=M_*N_j+D_jW_j.
$$

全部单位行残量必须为零，其余 36 行不删。实际 $36\times18$ 残差必须满足：前 14 列秩为 12，全部 18 列仍为 12。其两条齐次关系和四个目标关系还逐 4354 原行乘回。

### 3.1 两条缺失第二 cochain

对前 14 残量的一条核关系 $\eta$，令

$$
u=\sum_j\eta_jN_j,\qquad z_{p_j}=\eta_jD_j/c_j.
$$

于是 $M_*u+HFz_H+Tz_T=0$。用已付第一族 $(\Lambda C,E_{\rm old}X)$ 和第一补空间 $\Lambda F$，构造

$$
\lambda_0=\Lambda Cz_T,\qquad
\lambda_1=E_{\rm old}Xz_T+\Lambda Fz_H,\qquad
\lambda_2=E_{\rm full}u.
$$

整条共同清分母，先保存候选，再核每条 13062 个原三层产品；两条共 26124 个。与旧 22 条的原 33 头坐标合并后，必须实际 rank 24。

理论上，这两头模旧 22 独立：若某新 $z_T$ 已有旧 $M_0$ 支持的 lift，比较后完整常商中 HF 的独立性迫相应 $z_H$ 相同，从而这个 14 列组合已经落旧 $M_0$ 像，与旧 14 独立矛盾。源码仍实际核 joint rank。

### 3.2 四条缺失第三 cochain

对目标关系 $S_t+\sum_j\eta_jS_j=0$，令

$$
u=\frac{N_t+\sum_j\eta_jN_j}{D_t},
\qquad
z_{p_j}=\frac{\eta_jD_j}{D_tc_j}.
$$

于是 $M_*u+q_t+HFz_H+Tz_T=0$。先按实际 $Z_t/g_t$ 和旧 primitive common divisor 恢复整条第二 cochain，再加

$$
\lambda_1\mathrel{+}=\Lambda Cz_T,\qquad
\lambda_2\mathrel{+}=\Lambda Fz_H+E_{\rm old}Xz_T,\qquad
\lambda_3=E_{\rm full}u.
$$

$E_{\rm old}$ 与 $E_{\rm new}$ 保持各自原坐标。整体清分母后，每条核 17416 个原四层产品，四条共 69664 个。先存候选、再写 verified；与旧 17 条实际合并头秩必须为 21。旧 17 产品仅按完整 SHA 复用，不重算。

## 4. 完整第四连接

真实 29 原来源定义 $\pi:E\to K_{29}^{*}$，$\dim E=36$、$\dim\ker\pi=7$ 且 $\ker\pi\subset W_2$。完整 $W_2$ 维 12、像维 5。旧 22 个第三 forcing 仅付 $W_{13}$，像维 6；完整 $W_3$ 维 15、像维 8。

只有实际两新第二来源和四新第三来源通过后，才增加两条 $R_3$、四条 $R_4$。最终按同一整数来源代表排列

$$
K_{29}^{T}[HF_3,T_{33},R_{3,\rm old22},R_{3,\rm new2},
R_{4,\rm old17},R_{4,\rm new4}],
$$

即 $29\times81$。旧 75 列以及其前 58 列原字节直接复用，新配对只增加六列。旧秩 $(5,6,7)$ 必须保持，前 60 列实际秩必须恰为 8。

由 $\ker\pi\subset W_2\subset W_3$，

$$
E/W_3\cong K_{29}^{*}/\pi W_3,
\qquad
\beta_4=\operatorname{rank}_{\mathbb Q}(29\times81)-8.
$$

此时完整 21 头域与完整 incoming 都已覆盖，没有旧两维来像缺口。不同第三 lift 的差进入完整 $W_3$；额外 33 个第一族平移的 forcing 也在 $T\subset W_2$。因此本页精确秩不要求先把所有规范零头核展开，但后续真实 $\lambda_4$ 恢复仍需原 cochain 参数。

源码不预填实际秩，只要求符合已证 $3\le\beta_4\le5$。原 81 列核恢复所有列比例后乘回，头投影维数应为 $h=21-\beta_4$。可据此得到

$$
v_\infty D\ge114+h,\qquad
v_\infty(\text{cofactor、原来源换列})\ge110+h-1.
$$

这些是阶数下界。没有构造 $\lambda_4$，没有证明原目标特征零成员性，没有证明最高系数为 31 单位。条件费用另与实际最新公共因子相接，本代码不固定旧 $K_{101}$ 或 $K_{104}$。

## 5. CLI

下面的 {work} 和 {scripts} 由现有会话请求展开。旧目录须沿实际步骤参数。

~~~sh
python3 {scripts}/2026-11-15-r150-third-missing-four-constant-unit-pipeline-789f.py \
 --constant-preparation-out {work}/third-missing-four-constant-unit-preparation \
 --unit-prepared-out {work}/third-missing-four-eighteen-unit-preparation \
 --second-out {work}/selected-natural-second-left-regauged \
 --first-out {work}/selected-natural-first-left-envelope \
 --prepared-out {work}/third21-forcing-support-preparation-v2 \
 --third-out {work}/same-source-koszul29-third-pairing \
 --consumer-out {work}/third21-normal-four-original-consumer \
 --pairing-out {work}/same-source-koszul29-second-pairing \
 --fourth-out {work}/same-source-koszul29-fourth-on17-pairing \
 --native-source {scripts}/2026-11-15-r150-constant-unit-multiple-rhs-dixon-checkpoint-789f.cpp \
 --out {work}/third-missing-four-constant-unit-pipeline \
 --seconds 600 --memory-mib 4096 --compile-seconds 30 --through unit
~~~

单位段之后，同源码、同 out，改为 --through final。两模式、预算和绝对路径不进入数学绑定。源码、原生源码、14 个实际输入身份、协议和原坐标进入绑定。模式切换不迁移 native binding。

## 6. 回执和恢复

主回执 missing-third-constant-unit-pipeline-receipt.json。

单位段完成为 exit0、status=completed-prefix、outcome=complete-original-unit-only、unitSolutionExactVerified=true；其他来源及第四秩字段保持 false。

全部完成为 exit0、status=completed、outcome=complete-second24-third21-and-fourth-rank，且以下字段全真：

- all18CompleteOriginalResidualsRetained；
- all24CompleteSecondHeadsExplicit；
- allNewOriginalThreeLayerProductsZero；
- all21CompleteThirdHeadsExplicit；
- allNewOriginalFourLayerProductsZero；
- completeFourthIncomingImageComputed；
- fullSelectedFourthRankExactlyKnown；
- allOriginal81PairingKernelProductsZero。

actualIncomingPairingRank=8；fullSelectedFourthRankOverQ、completeFourthHeadDimension 和三个阶数下界取实际值。

时间到时 exit75，status/outcome=checkpointed-time-budget；失败时 exit1，status/outcome=failed。输入失配、非零原产品或与已证维数矛盾不包装成数学否定。

原生每个完整 digit 保存双槽 $X,N,p^k$，重建前也保存。完整单位解先落盘再回填；若完成 receipt 与 solution SHA 匹配，后续直接消费，不再升一位。Python 各完整阶段、各原残量列和各已核 cochain 按实际绑定与 SHA 复用，未完成部分继续。临时原候选与 verified 标记严格分开。

编译回执有实际 executable SHA，已成编译复用。实际运行统计记录系统 FLINT header/runtime。所有大矩阵、来源、解、残量及 native 检查点仅在当前 job 临时目录，长期只留小文本源码、参数、摘要与 SHA，不新增 Release、二进制 Git 文件或大 artifact。
