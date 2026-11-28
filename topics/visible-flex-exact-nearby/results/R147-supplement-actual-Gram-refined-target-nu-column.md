# R147 GBN：同一完整 target 参数列的实际 Gram 改进

2026-11-28。**唯一公开 run46125342339/1 的全部2项实际成功，后置全件准入与原 validator 通过。**

对同一个真正参数响应及原 target 基，有

$$
\|E_{96}^{a*}\mathcal B^{-1}F_\nu-d\|_{\ell^2_{96}}
\le 0.000163011451549838818017373316209787850160266874851829255286<.000163012.                       \tag{GBN.1}
$$

$d$ 是完整 BNC7 的全部96个 exact rational centres，没有重新拟合或
改变任一坐标。这仍是 target 低96读出；它不是原 $\Theta$ 列。

## 1. 新 row 费用与其余四个完整旧费用

沿 [ABGR.3](R149-supplement-actual-complete-target-B-Gram-row-error.md)，
先保存并读回新完整记录

$$
e_{\rm row,new}=e_R^{\rm Gram}B_HN_0
\le 0.000155450611196815986458810704862830405500654342415203653281,                                          \tag{GBN.2}
$$

再计算整个正公式

$$
e_{\nu,\rm new}=e_{\rm row,new}+e_{\rm PDE}
                +e_{\rm compound}+e_{\rm alias}+e_{\rm disk}.
\tag{GBN.3}
$$

以下四个完整旧记录逐字复制，未重新归约，也未从原 total 中相减：

| 旧完整费用 | 原 outward ball |
|---|---|
| `complete_target_B_receiver_on_NP_PDE_error_upper` | `[4.42691707286214688809724563378906589324930856729603380729443e-6 +/- 4.03e-66]` |
| `complete_target_B_trial_compound_error_upper` | `[2.64742313733725706092659573511286930942474574101655267438180e-6 +/- 5.99e-67]` |
| `complete_target_B_trial_quadrature_alias_upper` | `[3.23325693469253014831113874609641562910688022504801340691467e-106 +/- 2.41e-168]` |
| `complete_target_B_trial_quadrature_rounding_upper` | `[4.86500142823427609538769978055509456938478128313015523238951e-7 +/- 2.96e-67]` |

完整原 BNC joint 候选
`[0.00138311054706412401812510339157497624842376937611060421686754 +/- 4.65e-63]`
仍独立保存。实际 whole choice 是 `new_complete_Gram_candidate`。
原 BGR 的全部三个完整新球及原 BNC 的全部七项记录也完整保留。

`all_complete_original_BNC_scalar_and_signed_records` 保存全部原96
exact centres一次；新联合球通过完整中心数组 SHA 与原字段路径绑定。
旧较宽的逐坐标显示球并未改写，新结论准确为同一 exact centre vector
加减一个联合半径。两条 physical density mean 槽及原完整反射关系保持。
完整第97模以上的真响应没有被设置为零。

## 2. 完整实际身份与校验

| 原实际文件 | bytes | SHA256 |
|---|---:|---|
| [actual](../notes/saved_GBN_column_ci/run-46125342339-1/actual-saved-column-consequence.json) | 67092 | `901e86d15d72a9e0bdeb70ce7d7766e7d663915cbe491107f91deb32ed3c9f6d` |
| [execution](../notes/saved_GBN_column_ci/run-46125342339-1/execution.json) | 10805 | `39378bf7b4c107e4bbd04c8260316467aa14d170065ee597164b3f585871151a` |

原 [完整manifest](../notes/2026-11-28-saved-GBN-column-inputs.json) SHA256 `06c14835582b28d4736b7f8eaf25b22dae79e4f7169cfc640c15f30663bf293b`，全部18件 current inputs 已逐件核 whole bytes/SHA；两个父件的完整manifest/actual/execution及原validator全文准入，实际父件全成功后才开始本目标。后置又通过同一完整 metadata admission和公开worker的整个validator，没有导入数值包。

事件提交 `f6b405ad489bd029ed6f8d602572d31d2f9b6507`；科学checkout `2e37c0d422bb10c7e462d60f2e3fc01bcd0f2a1f`；owner SHA256 `f75bc9e2428c91cfa960c8f17c351d57ab989657b6e712df808855f4a62033e9`。完整中心数组 SHA256 为 `5c75df0b67110c064ecbafe8f27ff4e65bc8a96dbf948724ac53e84ff7feb25f`。

所有声明目标 complete/proved，child returncode0，failure null，timeout false；原科学目标重复数为0，旧大数组恢复数为0。实际运行使用 Python3.12.14 的 exact Fraction；所有原球均读取完整center和radius后取正确有向端点。新 exact rational 以及60位向上小数同时保存在 actual 中，小数转换由精确整数除法完成。

## 3. 使用范围

本结果只改善原 target 观测列。原 BFP/WBN/DCP 的完整目标响应及 Θ 作用使用各自证书，不能与本矩阵按名称互换。

真实 homogeneous finite96、全部 high/cross 和普通 finite complement、physical mean/phase/height 与完整 regular 参数缺陷仍需同一方程接入。所有原 full-Schur 和最终闭族 false flags 保留；本结果不证明整个物理逆或最终非线性族。
