# R147 WBN：同一完整 Θν 列的新实际联合误差

2026-11-28。**唯一公开 run46125286420/1 的全部1项实际成功，后置全件准入与原 validator 通过。**

对原 BFP 的同一个真正全空间参数响应 $x_\nu=\mathcal B^{-1}F_\nu$，
保持全部原96个 exact rational signed centres $d$，现有

$$
\|\Theta x_\nu-d\|_{\ell^2_{96}}
\le 0.001118590706097307792053294204707889143507034563782908055046<.001118591.                       \tag{WBN.1}
$$

它替换原完整 `.0316537342916386695…` 误差候选的一个已付槽；
没有改动列、相位、mean、model、trial 或其他误差项。

## 1. 同一完整正公式

沿 [ABFP.2](R147-supplement-actual-full-target-nu-forward-and-Theta-column.md)
与 [WMT.19](R149-supplement-complete-weighted-model-Theta-receiver.md)，
新的完整误差仍为

$$
(B_{\widehat\Theta}+E_{\Theta,*})\delta_X
 +E_VB_{\rm model}+E_MB_x+E_{\rm pair},
\qquad
E_{\Theta,*}=\min(E_{\Theta,\rm UACT},E_{\Theta,\rm WMT}).
\tag{WBN.2}
$$

两个 whole global 候选都保存；实际选中 `new_WMT_global`，即
WMA 的完整 `6.957961777218554…` 球。完整原 UACT global850候选
也保留。有限96专用的约 `.31698` 从未放入全空间槽。
$\delta_X$ 是 ABFP 已付的整个 $L^2$ 列误差，其余三项逐字沿用
同一个 BFP19 全对象。没有对旧 total upper 做相减，也没有重算
一个旧范数、积分、forward residual 或 pairing。

`all_complete_original_BFP_scalar_and_signed_records` 完整保存全部
19项父记录。原96 exact centres 仅保存一次，新结论以整个中心数组
的 SHA 绑定；它是完整联合球，不能把原显示为对称区间的坐标当零。
两条 physical density mean 槽逐字保持原 NP 证书及原反射关系。

## 2. 完整实际身份与校验

| 原实际文件 | bytes | SHA256 |
|---|---:|---|
| [actual](../notes/saved_WBN_column_ci/run-46125286420-1/actual-saved-column-consequence.json) | 30152 | `1f972ee941633f7052454035596536aee9fc843452fe2b4395fe2c183e3bbb52` |
| [execution](../notes/saved_WBN_column_ci/run-46125286420-1/execution.json) | 10579 | `1cd75afa628a42e2a069d96e649e34a358792b12057888cf3c37b5eefeaf32d9` |

原 [完整manifest](../notes/2026-11-28-saved-WBN-column-inputs.json) SHA256 `696a280cc634b2ecf94cb1a3d2af90fc676024e9327dfc245f89e15fff4f9ab2`，全部17件 current inputs 已逐件核 whole bytes/SHA；两个父件的完整manifest/actual/execution及原validator全文准入，实际父件全成功后才开始本目标。后置又通过同一完整 metadata admission和公开worker的整个validator，没有导入数值包。

事件提交 `3808849512c21299b2d4a9f10e7a12bfb65f01ee`；科学checkout `6f82901ea89603f2a16635522d035d7f2a6fb662`；owner SHA256 `f75bc9e2428c91cfa960c8f17c351d57ab989657b6e712df808855f4a62033e9`。完整中心数组 SHA256 为 `4a3a4ad2a25bc7e2f952b18ff6d6e963dfc5ce0df28c128bb530a7996d3bec1e`。

所有声明目标 complete/proved，child returncode0，failure null，timeout false；原科学目标重复数为0，旧大数组恢复数为0。实际运行使用 Python3.12.14 的 exact Fraction；所有原球均读取完整center和radius后取正确有向端点。新 exact rational 以及60位向上小数同时保存在 actual 中，小数转换由精确整数除法完成。

## 3. 使用范围

这是完整 Θ 对真全空间参数列的联合读出。DCP 对同一512-mode trial的直接密度逆与全异号tail是另一个已启动目标；本证明不预报其结果，也不代替它。

真实 homogeneous finite96、全部 high/cross 和普通 finite complement、physical mean/phase/height 与完整 regular 参数缺陷仍需同一方程接入。所有原 full-Schur 和最终闭族 false flags 保留；本结果不证明整个物理逆或最终非线性族。
