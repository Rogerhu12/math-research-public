# R141 补篇：真实高频逆的五项源费用实际完成

2026-11-20，visible-exact-astra-ac637-20261120。

公开运行 [44736533396/1](https://github.com/Rogerhu12/math-research-public/actions/runs/44736533396)
完成[五源合同](R141-supplement-actual-GH-source-window-and-return-contract.md)
(H.3) 的全部五个新 whole-domain 标量。它们是同一完整真实族的源费用，
不是重新求解已证明的高逆，也不是有限 WJK 试算子 $F$ 的范数。
全部五项成功冻结；低逆和实际反馈门还应消费它们的保存球另行验证。

## 1. 五项实际保存结果

记 $B_c=B_{HL,c}S^{-1}$、$\Delta B=(B_{HL}-B_{HL,c})S^{-1}$、
$\Delta C_0=B_{LH}-B_{LH,c}$。每个 $S^{-1}$ 只出现一次；第五项是 raw
输出源，不额外左乘 $S$。下表逐字复制 actual 的完整记录。

| 准确目标 | 保存的有向上界球 |
|---|---|
| centre collar：$b_{c,c}$ | `[9.52957241293211601716976817484763879448592609218030144905615389702622450396 +/- 4.68e-75]` |
| centre body：$b_{c,b}$ | `[240.474633106142799008255515420425285692964001590159727074099378749644077553 +/- 3.27e-73]` |
| full-family 差 collar：$b_{\Delta,c}$ | `[2.72995666633970526291518984177045350899719416567256821937034459758010288809e-5 +/- 4.86e-80]` |
| full-family 差 body：$b_{\Delta,b}$ | `[0.000464792301711853820595121012113889174246952883211034042481503687363664428196 +/- 4.32e-79]` |
| 完整 $\Delta C_0$ raw：$d_C$ | `[1.84954461253332636302949722929447815050823893188311575779908919972184642146e-5 +/- 4.71e-80]` |

前四项的源单位是普通 $L^2_rH^{1/3}_\phi$，Fourier 频率仍为 $4j$，其
逐行权准确为 $(1+16j^2)^{1/6}$。centre 输出至 $j=160$；完整族差输出
至 $j=288$。第五项的高输入有效至 $288$，但实际高未知解始终无限维。

原153父片、4650闭行、4801交集和全部3594接口均保留；实际比较为155
完整panel，collar由原parent0辨认，没有从body上界外推到真根。
中心pure-mean到high列在全部155panel准确为零；这个支持恒等式没有
用于删除 full-family 差的 mean。所有 signed 矩阵先相加，之后才取
Schur范数和完整窗口sup。

## 2. 准确的下一消费位置

原 base-order public43617150971/1 的完整
`entire_positive_raw_L2` 行给两个已成源常数 $C_c^{(0)},C_b^{(0)}$。
由于两个径向源窗口的输入掩码正交，实际高响应满足已证公式
$$
 \|G_H(B_c+\Delta B)\|
 \le \sqrt{[C_c^{(0)}(b_{c,c}+b_{\Delta,c})]^2
              +[C_b^{(0)}(b_{c,b}+b_{\Delta,b})]^2}.
 \tag{GHA.1}
$$
这是原合同 (H.4)，本次不把它的未执行新组合数伪装为已保存的第六个标量。
后继可只读本五球及旧完整行，取得 $H_B,H_Z,H_{\rm root}$ 和实际外迹。

R141低Green随后提供完整body/193atoms的 $g_C,g_0,c_B,c_A$，原 $L_0$
保持已有连续whole-kernel资格。完整内部反馈由 (H.8)--(H.14) 消费；
只对body环要求小于一，atom输出费用保留。真正physical外端97+96方块、
所有七类独立粗端口及两physical mean也继续保留。不能将内部收缩自动
叫作完整外端逆，不能将 coarse external source 一律升级成 raw $L^2$。

## 3. 完整运行与只读来源

事件提交 `c0d0bfce76eee48791e7f2be720f0d01a75942e3`；实际科学checkout
`ba5592a346b9d61a0dea7173ab329a5259b09519`。
固定Python `3.12.14`、python-flint `0.9.0`、320 bits、单BLAS线程。
实际数学时间 `97.32827455099999` 秒、child wall `108.07822201699999` 秒，
返回码0。五完整target、五保存球；37顶层字段、25门及全部原资格保持。

| 文件 | 字节 | SHA256 |
|---|---:|---|
| [actual](../notes/actual_GH_source_fees_ci/run-44736533396-1/actual-scientific-conclusion.json) | 49719 | `e7766bc9e1a714456fa224b9dc69171ba119626bf62ffce2437d43dcd80924d6` |
| [execution](../notes/actual_GH_source_fees_ci/run-44736533396-1/execution.json) | 54316 | `2feec091d753aa856bbcbd6140f41c693972cf88b43d07232efea6c03f44629e` |
| [report](../notes/actual_GH_source_fees_ci/run-44736533396-1/report.md) | 527 | `04fe921580b1c25bab07fcd0f9e6eadeb16f5ec2737ffdaf784e52da6e5ee0ee` |
| [完整首次清单](../notes/2026-11-20-actual-GH-source-fees-inputs.json) | 63939 | `69449ea01bbdfc202d6a6c763661a13f42efdcb08303fd356b1b32dc2f09887f` |

root 逐件核71当前文件的bytes/SHA/blob，科学、执行、manifest三份完整列表
相等，21历史原件的完整恢复对象与冻结身份相等；whole旧 $L$、centre排除
和两份base0/negative-one高图均原字保留。四次pull的双README差异均为空。
保存每球后先验证它包含原有向upper，再从实际文件读回；后继只能使用保存
区间的upper，不能读取一个没有登记的更窄中点。

原base0科学summary27047B/SHA
`410e8f07545c862425673a2c0cc37eebfc6f950217167f2b72c44d5a7b5676e7`，
process7437B/SHA
`d35bb44e4cd7d933778d3234b6b0fe6c271fa9a8e744466a3fa9fd40f0e1f454`；
原negative-one完整summary41797B/SHA
`0a3fb8e1be19b9ad82655099da8d5446ac49d92f073e7f6626d08a0626ec4fef`。
这些whole对象连全部7列、exterior mean/affine资格一起由actual引用，
没有只抄两个有利常数而舍弃原域。

没有调用 $G_H,G_f,G_L$ 的新action，没有重算旧 $L$、旧centre、endpoint、
atom、原50配方或旧producer，也没有附加未声明的 $\Delta A_L$ raw目标。
新数组、artifacts、Releases均零。

## 4. 未付范围

五源完成不授actual低高逆、完整$CFB$、true97+96物理行、原finite $\rho$
桥或任一真实RHS。完整负侧径向head、$\nu$、两physical mean、非线性
求解及全matching继续待付。最终精确可见固定度量闭族尚未构造。
