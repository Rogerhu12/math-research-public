# R149 UACT：原 finite Θ96 方阵的首个完整实际逆

2026-11-27，`visible-exact-astra-fb31ed6-20261127 / trial_restore`。

**本条已完成。** 唯一公开 Actions
[run45933303391/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45933303391)
完整成功，21/21 个新自然目标及所有整候选已经保存。原
$T=\Theta E_{96}^{a}$ 的完整误差为下述正式球，实际
$\rho<1$，因此同一个真实96维坐标方阵可逆，并有
$\|T^{-1}\|_2<12.588$。这解除 TQ.7 的条件并使 TQ.8–12 的坐标表示实际适用。

本证明只读本次已公开 whole actual/execution；未重新计算旧 ASR、IR、
OT、GY Hilbert–Schmidt 或本次21个目标。全 physical/PDE/Schur inverse
仍是原另一个问题，完整结果明确保留其 false flags。

## UACT1. 全对象、来源和实际终态

[whole actual](../notes/unit_disk_operator_Theta_low_square_ci/run-45933303391-1/actual-unit-disk-operator-Theta-low-square.json)
与 [whole execution](../notes/unit_disk_operator_Theta_low_square_ci/run-45933303391-1/execution.json)
提供以下完整字节身份；不是只取21条中的有利字段。

| 对象 | bytes | SHA-256 |
|---|---:|---|
| actual | 42477 | `17c721993bb6488ec48918c50caf70c84785ca54cb004fbc51d11de1c6eb14bc` |
| execution | 52265 | `de2b9e0f2a1f424cd4c644ab23839bf715590e4153058517e66706a3d79b768c` |
| manifest | 48987 | `80dbfdf33a39c180159f930a288813ef16fabe04e61c81f175154f012b99dcee` |

事件提交为 `6ecc22139cdb367421d9b93afa16e6a8c2031704`，
实际 science checkout 为 `67b7534477a199f32ff183c2b9e1a199cf6436c0`。
science 于 `2026-11-27T03:18:39.534163+00:00` 开始，
于 `2026-11-27T04:18:32.815907+00:00` 完成；
execution 完整落盘于 `04:18:35.616023+00:00`，
job success 结束于 `04:18:42 UTC`。
实际 child returncode 为0，actual/execution 的 complete 均为 true，
actual proved=true，saved_record_count=21，failure=null。

入口是
[fourfold_codazzi_unit_disk_operator_Theta_low_square_owner.py](../scripts/fourfold_codazzi_unit_disk_operator_Theta_low_square_owner.py)，
owner SHA 为 `94f9164cbfcb5d9859aa2ecd7467849cdf441031b267d5546af62b5e217a3f1c`。
完整准入含130份 current inputs、6份完整历史 native，以及 inherited
AS 的207份完整旧输入；actual 的 entire whole_completed_inputs 与
execution 的全部 receipts 保留它们的字节身份。
科学算术为320 bits，Python3.12.14、NumPy2.3.5、python-flint0.9.0。
原 IR carrier/proposal 保持 Haswell 单线程；原 AS/SN 恢复不强制
CORETYPE。只有1个新科学 child；2个必要原载体 child 不执行旧科学目标。

真实 selected member 仍是原 `43588332723/1`、
loss `1/250`、physical strip `1/128`，
原参考和隐式选取区间完整保留：

\[
 \alpha_{\rm raw}={6890507429876859\over9007199254740992},\qquad
 \nu_0={-2572625729470897\over72057594037927936},
\]
\[
 \nu_*\in\left[
 {-1004932207049545851281\over28147497671065600000000},
 {-1004931644099592429969\over28147497671065600000000}\right].
 \tag{UACT.1}
\]

这里的 $\alpha_{\rm raw}$ 是原 scalar candidate 参数；
下面的 $\alpha(x)$ 是 WBN/DT 的 mean-zero source coefficient，
两者按原定义区分。没有把 $\nu_*$ 换成区间中心。

## UACT2. 本次真正使用的方阵及 Hilbert 单位

沿 [TQ.1–7](R149-supplement-original-Theta-restriction-and-joint-Schur-row-consumer.md)
和 [TQL.1–8](R149-supplement-exact-low-model-isometry-and-Theta-square-error.md)，
在物理周期 $\pi/2$、归一测度 $dx/(\pi/2)$ 上令

\[
 Y=Y_a^0=P\operatorname{Fix}(R_a)\cap L^2(\mathbb T;\mathbb R),
 \quad v_n^a=\sqrt2\cos(4nx-2na),\quad
 a=2\mathcal H(0),\quad b=a+\Omega,
\]
\[
 \Theta=E_{96}^*D_+^{-1}\mathcal C^{-1}\mathcal A\overline G,
 \qquad \mathcal A=Id-\mathcal T_\alpha I,\qquad
 \mathcal T_\alpha=\Pi_+M_\alpha\Pi_++\Pi_-M_\alpha\Pi_-,
\]
\[
 T=\Theta E_{96}^a:\mathbb R^{96}\longrightarrow\mathbb R^{96}.
 \tag{UACT.2}
\]

输入是原 target 的前96条真实 $v_n^a$ 正交坐标，输出是原 root/source
96坐标；物理频率为 $4n$。原 $\overline G E_{96}^a=E_{96}^b$ 的
low reference 是精确等距。因而同一真实 $T$ 的误差可直接使用整个
$V_Q$ joint $L^2$ 误差，再加所有9216个 low model balls 的误差。
没有把 high 的512费用放进这一限制，也没有删任何无限残差、模型、
cohomological divisor 或 true-phase 费用。

本次原载体恢复均完成整个 SHA，而非只核96×96前块：

| 完整 private 载体 | bytes / shape | SHA-256 |
|---|---|---|
| 原 IR trial | 294912 / $[192,96,2]$ | `02ee6051166f1f23139b39984dbd309592c415405620f99982a3972d8dd49db1` |
| 原 AS alpha trial | 95675 / 全2048正模式 | `df6ed2ab4f3b12ecb6f3510401995291bcc989fa89f92f3712496845962d2e85` |
| 原 full raw source | 62443 / 全192正模式及 mean | `c692148e7e84530ed138bdb607ebe9eac645e5af1716e8825a2fbc225d2a406f` |
| 原8192点 grid | 1808090 | `f5daf796446064ba9d39894664d121970366357b6d2258b127c3ef6b82a7eab9` |
| 原 OT exact dyadic Θ trial | 1720320 / $[96,2240]$ | `3b5bff1ccffa74600cc6cb56b8521fb32830ae0697733617eb0042bb1a8f9143` |
| 原 OT full model balls | 1648623 / 全96行2240模式 | `a25b68d98866bba6ce163a94587753773342988df1b9dabbe1a73ba42b43a722` |
| 本次 exact dyadic low square | 73728 / $[96,96]$ | `59407fb83861bdedd4694fef870012eba106944376fcca2d8add4f0a5bedd323` |
| 本次 exact dyadic trial inverse | 73728 / $[96,96]$ | `982b6c5fe1d92dd9f42c8866963455c6d7a526353bf87605f70295f7565cae90` |
| 本次 whole signed residual | 1055504 / $[96,96]$ | `3ba3723a3031f0232c6a6283f441d41757674be351fa4b15fba30fc973ccf2ec` |

这些大载体保持 private；公共 actual 保存全文件身份、全行/模式合同、
所有完整 bound 和整门。没有新增公共数组、artifact 或 Release。

## UACT3. 21个正式新目标全部结果

下表逐条复制 actual 的全部 new_records，依其完整 target order；
所有 bound 类型为 upper。显示的整 ball 是正式 enclosure，
不是 midpoint upper。

| 序号 | target | 完整正式 ball |
|---:|---|---|
| 1 | `complete_G_trial_real_matrix_infinity_upper` | `[2.34196249581376287071364983801386512261131639545440202208066 +/- 2.27e-60]` |
| 2 | `complete_G_trial_real_matrix_one_upper` | `[3.06121937264150853614943323071437650967363677589666086732215 +/- 4.08e-60]` |
| 3 | `complete_G_trial_real_matrix_Schur_two_upper` | `[2.67754756487815706859991314828884570870554612171032478773076 +/- 4.15e-60]` |
| 4 | `complete_unit_disk_alpha_finite_Linf_product_upper` | `[0.929367955420804305985347586349937373226710589956788002379103 +/- 3.19e-61]` |
| 5 | `complete_unit_disk_alpha_finite_L2_product_upper` | `[6.24812289442354207197408289204944660797346696050102349209354 +/- 4.74e-60]` |
| 6 | `complete_unit_disk_alpha_inverse_error_Linf_product_upper` | `[0.0247135743301449302896688075733299597090394078018272947296150 +/- 1.02e-63]` |
| 7 | `complete_unit_disk_alpha_inverse_error_L2_product_upper` | `[0.0130464035317555979742719748744664526185704216886743816723807 +/- 3.15e-62]` |
| 8 | `complete_unit_disk_original_VQ_joint_L2_error_upper` | `[0.315533578702214915533262962264242261446641009299472929853017 +/- 2.10e-61]` |
| 9 | `complete_unit_disk_original_VQ_joint_H1_error_upper` | `[1.66200079139834846966928076415920538695882314159093323715268 +/- 4.42e-60]` |
| 10 | `complete_unit_disk_original_Theta_joint_L2_error_upper` | `[850.945862005507648368456798920646200406576793767861642840771 +/- 1.57e-58]` |
| 11 | `complete_low_model_action_joint_radius_upper` | `[0.00144828127036764038220967680123311837677884700767087258261174 +/- 1.94e-63]` |
| 12 | `complete_low_Theta_square_error_upper` | `[0.316981859972582555915472639065475379823419856307143802435629 +/- 4.81e-62]` |
| 13 | `trial_inverse_complete_infinity_upper` | `[2.34010921916157288255539183183140752103909548241766609532325 +/- 1.66e-60]` |
| 14 | `trial_inverse_complete_one_upper` | `[2.71917975570910619495207674340279977609980663143431865689994 +/- 4.37e-60]` |
| 15 | `trial_inverse_complete_Schur_two_candidate` | `[2.52253396704432763132176042938065457067623939931505548040621 +/- 2.92e-60]` |
| 16 | `trial_inverse_complete_Frobenius_candidate` | `[9.85617371560356147925832886501886636061732445430627428722217 +/- 1.67e-60]` |
| 17 | `trial_residual_complete_infinity_upper` | `[6.34631170808790399206803901891697938455582587380383915026742e-16 +/- 4.26e-76]` |
| 18 | `trial_residual_complete_one_upper` | `[8.11571528335556616330051323739192155207575485336610309300324e-16 +/- 2.64e-76]` |
| 19 | `trial_residual_complete_Schur_two_candidate` | `[7.17668857637471760185214594761000249650594867609125051547208e-16 +/- 3.30e-76]` |
| 20 | `trial_residual_complete_Frobenius_candidate` | `[1.43938514246689370807642243393906870304734981583956186001068e-15 +/- 2.92e-75]` |
| 21 | `complete_low_Theta_preconditioned_residual_upper` | `[0.799597508717728958701864679399867591405786599390279444875771 +/- 4.20e-61]` |

前三条是同一个完整 $GY$ real matrix 的新 induced norm：
全部384×96=36864个 signed entries 先形成、保存读回，再取整行/列
absolute sums。该 private matrix 为4211884 bytes，
SHA `7167f4e4e1d24ef46d1f4962c303d5c48a274ef0f8e4354acd29be9f6062ca7d`。
原 OT 的完整 Hilbert–Schmidt upper $9.797954012892\ldots$ 原样保留，
没有重算。两 whole candidates 均正式存在后，选择新的
$2.677547564878157\ldots$ Schur two upper；
[GYN](R149-supplement-complete-trial-primitive-operator-norm.md)
证明它可替代 UDR finite-product 中的 HS upper。

第4–7条用 [UDR](R149-supplement-unit-disk-phase-errors-in-original-Theta-rows.md)
的单位圆 disk recurrence，从同一原8192点 grid、同一原 signed2048
alpha trial 认证全2048 mode residual，保全部负模式共轭、零 mean、
原 $b=a+\Omega$ 和每个 cohomological divisor。
新的全8192点输入为5765491 bytes，
SHA `651626da1a6d20289802e0f0361f0b621aaa47d8c64ac3bbcb9b0370d89e0673`；
全2048 mode records 为3150509 bytes，
SHA `f7dc89b821eb1cb38373183eef20fe062110804cb87460cffd8d69ba007ecbc8`。
全 mode records 保存读回后才形成产品，保原 ASR 完整两项 tail；
旧 ASR 巨大的完整 scalar error 仍是它原来的成功结果。

四个完整新产品先各自落盘后，finite trial 使用整 $L^\infty$ product
（第4条），**无限** inverse error 使用整 $L^2$ product（第7条）。
没有在一条产品内部抽取不同模式的有利局部，也没有遗漏
$(\alpha-\widehat\alpha)G(Z-Y)$。UDR.16–18 连同原 IR 全频残差给
第8–10条。原完整 global Θ error 为 $850.9458620055\ldots$，
它没有因为 finite low restriction 而被删掉。

第11条保全部9216个 low model rounding/true-phase radii；
第12条是第8条与第11条的完整和。global/low 两候选全部先保存，
再按 TQL.9 选择第12条。第13–20条分别保存 exact trial inverse
和其完整 signed residual 的1、$\infty$、Schur two、Frobenius
候选；两个 whole two 候选均保存读回后才选 Schur bound。
所有矩阵乘法先完整保留符号，后取绝对值。

## UACT4. 完整严格门和已认证坐标逆

令 $\widehat T$ 为原 entire OT carrier 的前96×96块，$X$ 为上表
新 exact dyadic trial inverse（此字母不指 target normalizer
$\mathcal B$）。实际已保存

\[
 \|T-\widehat T\|_2\le\xi,\qquad
 \|X\|_2\le b_X,\qquad
 \|Id-X\widehat T\|_2\le r_0,
\]
\[
 \rho=r_0+b_X\xi
 \ \in\
 [0.799597508717728958701864679399867591405786599390279444875771
       \ \mathord{\pm}\ 4.20\,10^{-61}].
 \tag{UACT.3}
\]

该整球 upper 严格小于1，故 $\|Id-XT\|_2<1$。
由 Neumann 级数 $XT$ 可逆；在同一96维方空间内 $T$ 可逆，且

\[
 \boxed{\quad
 \|T^{-1}\|_2\le {b_X\over1-\rho}.
 \quad}
 \tag{UACT.4}
\]

这里右边取正式 saved upper 的有向算术结果，actual 的
`complete_coordinate_inverse.complete_coordinate_inverse_two_upper`
完整保存为

\[
 [12.5873383654262387573861417098853506361358752559755050755042
        \ \mathord{\pm}\ 2.70\,10^{-59}],
 \tag{UACT.5}
\]

从而确有 $\|T^{-1}\|_2<12.588$。
(UACT.5) 是同次已完成计算中的正式输出，不是本证明在本地重算
21目标或由打印中心倒推出的 bound。

actual 明确
`finite_coordinate_inverse_proved=true`，
`strict_whole_residual_upper_less_than_one=true`；
execution 同样记录完整 finite inverse proved。
所有旧 false loss outcomes 和原 parent whole flags 都保留。

## UACT5. 原高约束的已可用坐标同构及作用边界

现在令 $Q=E_{96}^a(E_{96}^a)^*$，$P=Id-Q$。TQ.8 的

\[
 R=P-E_{96}^a T^{-1}\Theta P,\qquad
 J(c,p)=E_{96}^aT^{-1}c+Rp
 \tag{UACT.6}
\]

在同一个真实 $Y$ 上已定义且有界，而非尚待有限门的形式写法。
由 $T=\Theta E_{96}^a$、$PE_{96}^a=0$，

\[
 \Theta R=0,\quad PR=P,\quad
 \Theta J(c,p)=c,\quad PJ(c,p)=p,\quad
 J(\Theta u,Pu)=u.
 \tag{UACT.7}
\]

因此 $\Theta u=0$ 等价于在这套坐标中 $c=0$，并且
$R:PY\to\ker\Theta$ 是以 $P|_{\ker\Theta}$ 为逆的同构。
对任一已认证 $\tau\ge\|\Theta P\|$，
TQ.10 的 whole bound 可实际使用本次 (UACT.5)：

\[
 \|Rp\|^2\le(1+\|T^{-1}\|_2^2\tau^2)\|p\|^2.
 \tag{UACT.8}
\]

本条不制造一个尚未计算的 sharper $\tau$，也不以原 trial 在
$n>2240$ 精确零推导真实 $\Theta$ 零尾。

对原已实现方程 $(Id+K)u+U\Theta u=f$，代回仍是
TQ.11–12 的完整表达式，尤其 high operator 保留

\[
 Id_P+PKP-PKE_{96}^aT^{-1}\Theta P .
 \tag{UACT.9}
\]

同一 $\mathcal B^{-1}$ 的完整物理列、两项独立 physical means、
true $\nu$/phase/height、真实 high feedback 和完整 PDE 接收均未由
本坐标逆产生。actual 的
`physical_PDE_column_inverse_proved=false`、
`full_physical_Schur_proved=false`、
`topic_completion_proved=false`
准确描述这个范围。后继可以直接消费这里完整已成的逆与 joint
error；无需再运行 ASR/IR/OT/GYN/UDR/TQC 的任何已成目标。
