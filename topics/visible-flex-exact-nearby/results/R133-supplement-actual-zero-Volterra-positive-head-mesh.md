# R133 supplement: actual zero-Volterra positive-head mesh conclusion

2026-11-16. **完整新目标已算并冻结；预设充分网格门为 false，未证明有限逆。**

公开仓库自身 [Actions run 43838214094/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43838214094) 成功。事件提交 `3e947078a90e8faa39a6578fa49df18e546c6033`；真实科学 checkout `475c2098242f869e97ba579e0206c5edce96c6a6`。一个科学子进程完成14门、24个依序目标：3个完整原行最大值、18个新标量球、完整候选选择、所需 N 诊断、严格比较。没有生成条件 resolvent，没有分配有限矩阵；旧成功数学调用为0。

此成功是完整计算及其保存成功。严格比较的 false 是已保存的科学结论，不能改写为通过，也不能解释为真实算子奇异或无逆。

## WHVA1. 完整原字输出与本次核验

| 文件 | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| [完整科学结论](../notes/zero_volterra_positive_head_ci/run-43838214094-1/actual-scientific-conclusion.json) | ebe7ae42c2482ce9b20e7af1d41e02f89b920010 | 12011 | ff5d6e5231e6be66107217d670133b18727dd5b24b81e7566fa884973b29df72 |
| [完整执行回执](../notes/zero_volterra_positive_head_ci/run-43838214094-1/execution.json) | 8eb5832f3383cb50f63ce5a09db0fcae9bb18e9f | 22191 | 65f008107d912a5243c135aa7446071428022154cd90b09e6ccf8aeee2422bb7 |
| [原运行报告](../notes/zero_volterra_positive_head_ci/run-43838214094-1/report.md) | 98e8bbb1a881a401810cdc7bbbf0f646c3fb5c8f | 428 | e6e2335164cb40de1d1906aaca346afab4153522a63693567ccf493abd239edb |

根完整读取三件 UTF8 原文并核字节数与 SHA，逐项核27字段、14门完整名称和全真值、24目标前缀、18球字段、全部参数/模块/实际 checkout/物理 scope、9个旧完整 literal、原 scope 与完整 false-branch progress。完整15 current receipts 与 manifest 的顺序及五键身份完全相等；6源只作 AST 核，其中3个原生产源没有 import/执行。

13份原历史分件的完整身份、offset、原压缩与展开 chunk hash 在执行回执逐项全保并标真。其去掉三核验布尔后的原列表与 manifest 完全相等；根从完整小回执原字重建 restoration receipt，得到原 `9047B/c7e9074d49558abcaf844ba94e423f3b1f85a4b715254e5e2fbb138a84cebf25`。真正原 native `25507783B/1f3e5fa630f39a667a96102f103ac8977d00e580f698a83904f361c5a05c6f3c` 只在公开 runner 临时恢复；根没有读取 binary/gzip，也没有独立重算 native 科学量。

两阶各4650完整行、inflated4650和3594接口均核完整；旧 progress4608及 parts-manifest 的原行计数0保持原字，未冒充覆盖计数。三旧成功 runs 43606747196/1、43615531666/1、43627228225/1 均只读。

4次真实 `git pull --rebase origin main` 完整回执的两 README actual diff 与相对已读规则 diff 均空；最后成功时间 `2026-11-16T09:16:50.206324+00:00`。根独核完整4步 hash chain `330a21db8443a688dbac289012b90f4c254d2609988826e6581b1ba2407a9728` 及 preflight 的 `1354B/66dc8c6aac5b385c2393ca8d853d4321a42f06a788698c125a386b1a206f3db6`。

原完整科学 stdout 是 `497130B/305935fa02e79e8096b79e8e1e8c2af4135eed7cf393bc0582029e2820fa737a`，这里只引用执行回执；根未通过 connector 取该大日志，也不宣称独立重建。运行 Python3.12.14、python-flint0.9.0、320bit，唯一 child returncode0、无timeout。科学输出原子保存并在每目标后打印完整前缀；本次无失败或遗失新量。

## WHVA2. 唯一新 whole maxima

这三个最大值是在原完整 order0 的4650已存行上首次完成的全覆盖比较，未重跑原系数、参考、图或行生产器。每个 winner 保留原完整三字符串 record、原行序号、区间、完整原行 canonical SHA；不是根据抽样端点或已有摘要替代全行。

| 量 | 原字段 | winner行（原零基） | 原完整球 |
|---|---|---:|---|
| G_b | head_generator | 4620 | `[12722.684316728715418258096216140721504523191205748311655169417890885854877280981 +/- 4.92e-76]` |
| H_b | low_to_high_source | 2886 | `[689.47831262786371511581146628604961792015874481891755566841309631537600337563624 +/- 3.91e-78]` |
| L_b | high_to_low_raw | 2886 | `[66.213076660468572836117834294080928793116993848742675044021290138306386293322322 +/- 1.28e-79]` |

完整 winner 身份如下，全部为原字复制：

```json
{
  "G_b": {
    "winning_interval": [
      "3",
      "3383329220062085/1125899906842624"
    ],
    "winning_complete_row_sha256": "32670c077753a49989f62097c5d3504de48da06f323b6931ef69a9ba12a238ed",
    "rows_compared": 4650,
    "tie_break": "first original row"
  },
  "H_b": {
    "winning_interval": [
      "1452410879826985/2251799813685248",
      "2905447259602215/4503599627370496"
    ],
    "winning_complete_row_sha256": "0d23307d5657b331f7a2bec5fe0d0a980c94c94cbee169e2a870196972d3956b",
    "rows_compared": 4650,
    "tie_break": "first original row"
  },
  "L_b": {
    "winning_interval": [
      "1452410879826985/2251799813685248",
      "2905447259602215/4503599627370496"
    ],
    "winning_complete_row_sha256": "0d23307d5657b331f7a2bec5fe0d0a980c94c94cbee169e2a870196972d3956b",
    "rows_compared": 4650,
    "tie_break": "first original row"
  }
}
```

## WHVA3. 完整 typed 组合与已成球

使用 [WHV 精确解析合同](R133-supplement-zero-Volterra-preconditioning-and-readonly-positive-head-mesh-contract.md) e993f068 的 ordinary-dr/固定 raw fiber。旧 collar/body 源系数均是同真正侧完整 \(L^2_rH^{-1}\) 输出；源输入为 \(L^2_rH^{-2/3}\)。全高源、独立 mean、原 affine 及所有初值/外端/接口贡献仍按完整来源保留。

记 \(\Lambda_0=\langle388\rangle\)。\(A_c=\Lambda_0^{-2/3}(23/2)\)；两个完整 body 候选分别为 \(\Lambda_0^{-1}H_b\)、\(\Lambda_0^{-2/3}L_b\)，本次选后者。候选选择比较完整候选 upper，不减上界，不混不同输入范数。

\(C_P=\sqrt{(C_cA_c)^2+(C_bA_b)^2}\) 使用两段普通径向输入的正交分拆；\(L_* = \max(58/5,L_b)\)，\(C_K=1153L_*C_P\)，\(A_\infty=\max(62286/125,G_b)\)。1153只作用于真正 \(97\le|j|\le288\) 的耦合壳，不截未知解为有限频率。

以下完整18球逐字来自本次科学文件；本页没有计算任何新乘积、开方、指数、最大值或数值比较。

| 新量 | 完整 ball 字符串 |
|---|---|
| A_b_from_H | `[1.77700005846169470730602329282948234773900766545652145245701577225054798123 +/- 2.82e-75]` |
| A_b_from_L | `[1.24467220007668318858947923787273650680089905758001187198231194079055209595 +/- 3.40e-75]` |
| A_b_weight | `[0.00257731102765056173438620316059122199289981112014429110352686249126355210120 +/- 2.28e-78]` |
| A_c | `[0.216176788979021022547123318815010633904539663839870444207842182068403381225 +/- 1.43e-76]` |
| A_c_weight | `[0.0187979816503496541345324625056530986003947533773800386267688853972524679326 +/- 2.11e-77]` |
| A_infty | `[12722.6843167287154182580962161407215045231912057483116551694178908858548773 +/- 1.91e-71]` |
| C_D0 | `1.00000000000000000000000000000000000000000000000000000000000000000000000000` |
| C_K | `[145602.599136265490855944220510193339888473488076543892035984255609935159416 +/- 8.97e-71]` |
| C_P | `[1.90719918289202602488898585074719985828732117187163019143568535692730417227 +/- 5.23e-76]` |
| C_R0 | `[1.69900062557392838648031874832067759709942440208119279378291279789277565664 +/- 3.88e-75]` |
| C_T0 | `[290949.405913985987319393424892066603155319489122519424276716616199837528841 +/- 3.09e-70]` |
| C_V0 | `[1.83766862479906476613426408541016184469934453248854780674873071925390968540 +/- 4.47e-75]` |
| L_star | `[66.2130766604685728361178342940809287931169938487426750440212901383063862933 +/- 2.24e-74]` |
| Lambda0 | `[388.001288657653816303170954811205514921102065082122304180451513747271451074 +/- 2.71e-73]` |
| ell_upper | `[2.88660312570060000000000000000000000000000000000000000000000000000000000000 +/- 1e-79]` |
| epsilon | `[35.5162849016096175926993926870198490179833360745262969087788838134567295951 +/- 4.46e-74]` |
| mesh_numerator | `[145474.702956992993659696712446033301577659744561259712138358308099918764421 +/- 3.47e-70]` |
| pi | `[3.14159265358979323846264338327950288419716939937510582097494459230781640629 +/- 3.80e-75]` |

## WHVA4. 预设网格的真实结果与严格限制

N=4096是预先冻结的资源上限；所测试的输出维数原回执为790528，角纤维193，径向仍无限维。球 `epsilon` 是该完整充分估计的 \(\ell_{upper}(A_\infty+C_K)/(\pi N)\)，其保存 upper 与1比较结果为 **false**。

完整 required-N 诊断保持如下原字：

```json
{
  "diagnostic_is_not_a_finite_inverse": true,
  "exceeds_256_digits": false,
  "formula": "floor(saved numerator upper)+1",
  "required_N_decimal": "145475",
  "resource_cap_N": 4096,
  "tested_N": 4096,
  "tested_output_dimension": 790528,
  "within_declared_cap": false
}
```

诊断中的145475是同一个已得 numerator 上界按已声明公式给出的足够网格数。它不证明真实算子必须使用这么多网格，不证明其他估计或投影无效，也不证明 Fredholm 核非零。未以此分配大矩阵，未暗改资源 cap 或重试原已完成数学。

因此没有 \(R_N^{-1}\) 数值准入、没有有限 signed inverse、没有实际 kernel/cokernel 基底或 prescribed-root 96 normalization。WHR 的固定算子 Fredholm index0、未知 \(m_H\)、全余核/H¹补列/真正端点行及全交叉块仍完整保留。WHV 的 \(F_0=(Id-V_0A)F\) 精确左预处理、右端/初值/impulse 一致变换、余核逆伴随和直接端点项仍成立；本次数值充分门不改变这些解析事实。

负侧 head、真实 physical96 的数值基底/waist Gram/\(\Theta\)、\(\nu\) 与两物理 mean 的完整有限 Schur、全背景/非线性 matching，以及 README 的同一闭嵌入 fixed-metric 族验收均未因此完成。

## WHVA5. 冻结与先前失败

首次 run43837109596/1 仍为 failure：完整只读 preflight 通过后，marker push 非FF触发立即真实 rebase，但该 Git 调用缺 bot identity。唯一科学 Popen 尚未到达，new0/old0/lost0。完整 [科学前失败证据](../notes/2026-11-16-R133-WHV-pre-science-failed-attempt-evidence.json) `ba9f172a/6946/e6b6f079f9ff476a98829a3090f662d3335c56c3a8c5ba77ed3072f48c510a71` 已于8dfc6d8c先推，明确全部原新目标仍未计算。

修复只给每一个 Git 调用统一添加原 bot 的 command-local name/email，两数学源原字不变。成功 run 的已消费 marker 在 `notes/zero_volterra_positive_head_ci/WHV_zero_volterra_positive_head_mesh_v1-consumed.json`，首次推送475c2098；之后不得再次运行这24个已成目标。后续任何新细化必须另定义完整新目标并只读本次结果。

| 本次冻结件 | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| science | 437a9f2841dc5b4cdb3a3f55bf9938a2d049f98f | 9632 | e82c51805d04b28117d38dc60b9ac7fe64d1eb3a867e828b114ab259ef063031 |
| readonly | f1e2a255863413438cc4985cbad66124514bc4be | 15718 | 7cb5c84b09aa51e451103db9a718d0766a748f5be26256e4b61c0041e0dd81f5 |
| actual worker | 9d1967739aebf24756708014426ab91932c06903 | 25559 | a51725c25881464971d5598ba3f639e9dad049068cd8516d6b7954ccccb00cda |
| manifest | f45ca10bc1021261ec9bcb89b335bd801c540fa3 | 21813 | 791e8f2ecfa8ebe23473d8d2e7548eaa25466149f54ead7a124dc1a0eda7d70a |
| workflow | 20bba959252c64a0ede7d7625cd6d020788c11a4 | 2914 | f4ef2a3347007a543ca75e7d47042577ff36bed832349128174934155cedce18 |

新运行前及立即启动前均留完整70000B输出预算+120000B；启动前topic199751373B。保存已完成输出只按实际200MB上限，不另用预留阻止保存。本次没有新数组/data/Release/artifact。根仅文本/模式/字节与hash核验；所有新数学均由本公开仓库 Actions 完成。未达总验收，继续下一完整子问题。
