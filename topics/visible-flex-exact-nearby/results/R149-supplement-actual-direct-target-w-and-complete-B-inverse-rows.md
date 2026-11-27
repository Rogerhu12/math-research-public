# R149 DBRA：真实 target w 与 B inverse96 全行的首次实际完成

2026-11-27，`visible-exact-astra-fb31ed6-20261127 / trial_restore`。

**已完成本条。** 唯一公开
[Actions45935081577/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45935081577)
成功保存 DWT2 与 BR7 的全部9个新目标。真
$w=v_i-\alpha$ 的完整2048模式 trial 已实际形成，原
$R=E_{96}^{a*}\mathcal B^{-1}$ 的96条完整 $L^2$ 行满足本次正式
joint error $e_R<0.858$。以下只读这次 whole 公开结果，不重算任何
旧 cohomology、flow、alpha、norm、residual 或本次9目标。

## DBRA1. Whole 实际证据

| 完整对象 | bytes | SHA-256 |
|---|---:|---|
| [actual](../notes/direct_w_and_target_B_rows_ci/run-45935081577-1/actual-direct-w-and-target-B-rows.json) | 24958 | `2658db04a88e92f88b26aed145db41401311dce3e63a8ba05d32d69dd915e158` |
| [execution](../notes/direct_w_and_target_B_rows_ci/run-45935081577-1/execution.json) | 27035 | `94f1a5a87ff3215443c9fa8950ad037f10e225752d3fec9bd6e00f9fa75d01d7` |
| [manifest](../notes/2026-11-27-direct-w-target-B-rows-inputs.json) | 24068 | `8fb9adfbb646241d5377aaa5511013b6a3cb9180bb0c64cdd1d9bce649ed00a0` |

事件提交 `282e03e403251d7f7c85cc015cf52ed43b2f4963`；
science checkout `a145bbec0c1b24bf709c9bd86e7656703e68b11d`。
science 从 `2026-11-27T03:36:30.784171+00:00`
至 `2026-11-27T04:35:49.970625+00:00`；
完整 execution 落盘于 `04:35:51.448082+00:00`，
job 于 `04:35:55 UTC` success。
actual/execution 均 complete=true，actual proved=true，
child returncode=0，failure=null；actual 保存全9目标、
2048完整 w modes、96完整 residual rows。

[owner](../scripts/fourfold_codazzi_direct_w_target_B_rows_owner.py)
SHA 为 `0d800bd0481d2d896c6262c7c777061bd1382b52de76c609f33b2f4fd1423b43`。
完整准入保65 current texts 及原 ASR/SN 全部 inherited inputs；
无单独新增 native list。实际运行 Python3.12.14、NumPy2.3.5、
python-flint0.9.0、320 bits。完整 parent actual/execution/source
身份、运行合同、原相位/均值和所有 copied whole records 均在本次两
完整对象中。old completed target 次数、公共 arrays/artifacts/Releases
均为0。

## DBRA2. 原 target、完整 reflection 与两 mean 不变

本次算子严格是
[WBP.4–9](R133-supplement-polynomial-two-sided-reflected-waist-normalizer-bounds.md)
与 [BR](R149-supplement-target-normalizer-low-rows-by-whole-energy-residual.md) 的

$
 \mathcal B=Id+\mathcal T_w I,\qquad
 \mathcal T_w=\Pi_+M_w\Pi_++\Pi_-M_w\Pi_-,
 \quad I=\partial_\phi^{-1}P,\quad G_{\rm abs}=|\partial_\phi|^{-1}.
 \tag{DBRA.1}
$

采用周期 $\pi/2$、归一测度、物理频率 $4n$。
$\mathscr H=\dot H^{-1/2}_0$ 中

$
 \mathcal B^\dagger=Id-\mathcal T_w I,\qquad
 \|(\mathcal B^\dagger)^{-1}\|_{\mathscr H\to\mathscr H}\le1
 \tag{DBRA.2}
$

是 WBP 已证明的同一个 onto inverse。
原 $a=2\mathcal H(0)$、$b=a+\Omega$、$R_aw=-w$、
$\Pi w=0$ 及 $Y_a^0=\operatorname{Fix}(R_a)\cap L^2_0$ 保留。
所有 trial 的 phase error 被实际 full residual 支付；没有将
$a$ 置零或用显示的中点冒充真实相位。

目标行与本次 finite trial 为

$
 R=E_{96}^{a*}\mathcal B^{-1},\qquad
 r_j=G_{\rm abs}(\mathcal B^\dagger)^{-1}
                    (4j\sqrt2\cos(4j\phi-2ja)),\qquad
 \widehat r_j=G_{\rm abs}\widehat y_j .
 \tag{DBRA.3}
$

原 $L^2_0\to\ell^2_{96}$ whole receiver bound $\sqrt{96}$ 仍由
BR.4 直接给出。此处的 $e_R$ 是同一96行算子的联合误差，不按96次
scalar error 再乘 $\sqrt{96}$。两独立 physical density means
不属于该 nonmean normalizer，也不由其 inverse 消去。

## DBRA3. Necessary restoration 与新的 w carrier

原 SN 3146 intervals、12584 subcells、两支全257 coefficients
的 whole endpoint 恢复成功：
245885 bytes，SHA
`3048266ba668164d7d9b5475c5262f1f3568cfe32a6e42c7bb496e4bda6c62b6`。
原 raw192 保 mean，62443 bytes，SHA
`c692148e7e84530ed138bdb607ebe9eac645e5af1716e8825a2fbc225d2a406f`；
原8192点 grid 为1808090 bytes，SHA
`f5daf796446064ba9d39894664d121970366357b6d2258b127c3ef6b82a7eab9`。
恢复原207件输入共13612391 bytes，保持原完整字节身份。
该 child 的 CORETYPE 保持原 unset，未执行旧 flow/residual/norm。

[DWT](R149-supplement-direct-target-w-from-complete-unit-disk-input.md)
直接使用同一原完整 grid、原 rotation、原 source phase 和
cohomological divisor，生成新 w；没有物化或使用旧 alpha trial。
单位圆 disk recurrence 支付每个节点的幂误差和全部 arithmetic，
保所有8192节点和2048正模式，负模式为 conjugates、mean 精确零。
原 ASR 完整两项 tail envelope 仍按 DWT 的完整 majorant 证明复用，
没有重跑旧 tail 或仅保 finite support。

完整新 private receipts 是：

| 对象 | bytes / 全部范围 | SHA-256 |
|---|---|---|
| 新 unit-disk input | 5765491 / 全8192节点 | `651626da1a6d20289802e0f0361f0b621aaa47d8c64ac3bbcb9b0370d89e0673` |
| 全2048 w mode records | 5683199 | `496f3108da59102573224967abf522ea579a12b7a066474f9bfcef7917789cc2` |
| 全 w exact trial | 1156214 / 全2048正模式 | `c28d74dd27eda8cd0f7f3479afee06f67d36156df679ed43e0ddd62f006f5fb3` |
| 全 y exact dyadic trial | 294912 / $[192,96,2]$ | `b12281fc1b7419662c67b1bc44a94745481bab16e202fde1418ae7cacaa6d160` |
| 全 r exact rational rows | 2562058 / $[96,192]$ | `a55176484d67a63e7ecf74d2eff287bd3d45b796746e6917f92f969d4518e1d3` |
| 全 signed residual balls | 49312246 / $[96,2240]$ | `56ce2bd3fa72d4b0deaf5ed13bd8c13d0986c954c9303f1cb4e1fece602abbad` |

完整 w 误差先保存读回，再进入 BR。原有序同号192-mode Galerkin
solve 只选择 y trial；它本身不是全空间 inverse 的证明。
selection fallback=null，所有有限 dyadics 以及其原 shape/encoding
均保留。真实 inverse 的存在仍来自 (DBRA.2)，全部 trial error
来自下一节的完整残差。

## DBRA4. 全9条正式球及合法整候选

| 序号 | target | 完整正式 upper ball |
|---:|---|---|
| 1 | `complete_direct_unit_disk_target_w_Linf_error_upper` | `[0.347099250283449234360401355911114117280407257855515345537830 +/- 2.24e-61]` |
| 2 | `complete_direct_unit_disk_target_w_L2_error_upper` | `[0.0646368666448014896672451004761658617432186976173702549446476 +/- 3.16e-62]` |
| 3 | `complete_I_trial_Hilbert_Schmidt_upper` | `[9.79719216088980499192829743218188648673831061212157564534900 +/- 1.08e-60]` |
| 4 | `complete_positive_I_trial_vector_Wiener_upper` | `[67.8778659344806500176429390446213205512787965082726970283143 +/- 3.34e-59]` |
| 5 | `complete_finite_target_B_adjoint_energy_residual_upper` | `[0.0145911772738716083308494064423666440871765675251881703927316 +/- 4.35e-62]` |
| 6 | `complete_target_w_Linf_product_upper` | `[3.40059805392773726223050941476513456548048808851834158916696 +/- 3.67e-60]` |
| 7 | `complete_target_w_L2_product_upper` | `[6.20473835815649043323331451893623981671041869075382743712401 +/- 3.57e-60]` |
| 8 | `complete_target_B_adjoint_joint_energy_residual_upper` | `[1.71489020423774023944610411382493392682742061178435896497621 +/- 3.48e-60]` |
| 9 | `complete_target_B_inverse96_joint_L2_row_error_upper` | `[0.857445102118870119723052056912466963413710305892179482488107 +/- 2.61e-61]` |

第1–2条完整支付 true $w-\widehat w$ 的 finite、model、source、
alias、cohomological divisor 和 infinite tail。
第3–4条保全部192×96 trial coefficients。
第5条先对96条 residual 的全部1–2240正模式形成完整 signed balls，
再取 BR.9 的完整 energy Hilbert–Schmidt upper；193–2240均在其内，
没有以192 Galerkin 方阵残差替代全频残差。

第6–7条为同一个 $\mathcal T_{w-\widehat w}IY$ 的两个完整候选。
两者先各自保存读回，实际整选第6条：
`complete_target_w_Linf_product_upper`。
第8–9条于是按 BR.12 给

$
 F_H=
 [0.0145911772738716083308494064423666440871765675251881703927316
        \ \mathord{\pm}\ 4.35\,10^{-62}],
$
$
 \|D:\ell^2_{96}\to\mathscr H\|\le F_H+\tfrac12P_w,\qquad
 \|R-\widehat R:L^2_0\to\ell^2_{96}\|
       \le e_R=\tfrac12F_H+\tfrac14P_w ,
 \tag{DBRA.4}
$
$
 e_R=
 [0.857445102118870119723052056912466963413710305892179482488107
        \ \mathord{\pm}\ 2.61\,10^{-61}].
 \tag{DBRA.5}
$

这是完整全空间行证书。大的主要费用来自完整 true w coefficient
error 与全部 trial columns 的现有产品，不是宣称小 Galerkin
residual 已足以付清它。未从保存的上界中相减，未忽略 high modes。

## DBRA5. 现已可直接消费的真实对象

后继 [BNC](R147-supplement-target-normalized-strict-parameter-column.md)
可消费全部96行 exact rational carrier、(DBRA.5)、第3条的原完整
$IY$ Hilbert–Schmidt norm，以及原 NP/PO/ASB/JC 的完整对象，
首次形成真 $\mathcal B^{-1}$ 归一 strict-$\nu$ 的96个 signed 坐标。
任何 necessary restoration 必须核上述 entire w、y、r 和 unit-disk
SHA；不能重新运行本次 DWT2/BR7。

本次不提供完整 forward physical column 或其第97以上坐标，也不把
SC 的低96配对等同于 $\mathcal B^{-1}$ full column。
actual 明确保
`physical_PDE_or_full_Schur_proved=false`、
`physical_mean_slots_eliminated=false`、
`topic_completion_proved=false`。
真实 finite/high/mean/phase/height matching 和同一个最终固定度量族
继续遵守原完整接口。
