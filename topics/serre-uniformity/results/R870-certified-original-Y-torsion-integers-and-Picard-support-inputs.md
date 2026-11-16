# R870 — 原Y有理挠点整数与十六谱块的Picard判定输入已完成

日期：2026-11-16。状态：**真实公开Actions已完成新整数、全部乘回和80条原Picard输入计划；原η活跃支持仍未计算。**

[run43822039811](https://github.com/Rogerhu12/math-research-public/actions/runs/43822039811)、job133147178823、source `eb46ca019bfe2098799cd97a5b31dab27ad3c9a1` 成功。core receipt计时0.5794888300000025秒，最终证书在0.579031853999993秒写出，共20个完整数学阶段。

## 1. 实际有理挠点消去整数

沿[R870原有理Picard证明](R870-original-rational-Picard-torsion-and-T7-support-certificates.md)，原五个整点为ξ_j=[Z_j]∈J_Y(Q)，I_Z=O(−Z_j)，η_j=ξ_j/q_j。其原完整七项范数、Q下降、负Picard类号、两点帧与分母67/134不变。

本次直接读取[R865真实T7谱](R865-certified-original-Y-Hecke-T7-and-squarefree-spectrum.md)，没有重算矩阵、特征多项式、因式分解或CRT。实际16个因子重数均为1，故χ7=m7。新Actions逐系数验证

m7(X)=(X−8)Q0(X)+N0。

实际得到

```text
N0 = 11325784817368052420921175766200050035118266865985508210111548314027774542699191614334036812463309954663886110720
```

原7处好约化、diamond7=1、−3 twist在7处字符+1，以及全部有理挠点（含7主部分）的约化单射已由R870证明。因此这个实际正整数同时满足

- N0=χ7(8)=#J_Y(F7)；
- [N0]J_Y(Q)_tors=0；
- 对原R∈J_Y(Q)，R为挠点当且仅当(T7−8)R=0。

这里没有把Q以外的未指定扩域挠点纳入结论；也没有将局部log为零直接等同原主除子。

## 2. 十六个实际分块整数

以下编号沿原R865谱与CRT索引，未重新编号。对每个原不可约因子fi，本次保存并全系数乘回

fi(X)=(X−8)Qi(X)+ni，ni=fi(8)>0。

| 原因子索引 | 次数 | 实际ni |
|---|---:|---:|
| 0 | 2 | 56 |
| 1 | 3 | 985 |
| 2 | 3 | 659 |
| 3 | 3 | 962 |
| 4 | 4 | 4409 |
| 5 | 4 | 3401 |
| 6 | 4 | 3474 |
| 7 | 4 | 2518 |
| 8 | 8 | 8782681 |
| 9 | 8 | 6710644 |
| 10 | 8 | 7013556 |
| 11 | 12 | 32857550893 |
| 12 | 12 | 25272141677 |
| 13 | 16 | 115573682337296 |
| 14 | 18 | 2621246644246441 |
| 15 | 18 | 23745298769478007 |

新程序验证这16个ni的乘积为上述N0，按原重数的乘积也为χ7(8)。这些乘法与整数多项式除法均在本次公开Actions实际完成，本地只读取结果。

原整数投影为Pi=diEi。每一块还准确核了fiPi=m7Ri，并形成未约化的实际整数多项式Ai=(X−8)Pi。保留未约化Ai是为了固定有限对应和帧比较的真实表达式，不因Jacobian端同一个算子而悄悄替换对应代表。

## 3. 共同对应分母已经取得，原YP特定投影仍未选择

实际计算d*=lcm(di)，并完整验证所有d*Ei的多项式系数为整数。这个整数的十进制表示有1959个字符，完整字节及16个整数对应在 `R870-uniform-integer-correspondence-denominator.json.gz`，1899605字节，SHA256

`3ca6b9d41548bb782d399a3d15b2c7e6ace22d45406aa8fe9806ec611acb3e9f`。

不把大型整数及对应系数表复制进Git。d*是原已成16个di的公倍数，不声称最小，也不替换R862的d_A。只有真正识别原η活跃块以后，才能给YP指定e_η、其有限对应及所选d；本次相关旗标仍false。

原T7谱的每个重数均为1，结合R870§7的原模形式等型论证，实际16块已经相互分离。但“等型分离”不决定哪一块承载原ξ_j。

## 4. 八十个原Picard输入的准确出口

每个因子i与原五点j都已绑定GLOBAL中的原eta_degree_zero_fractional_ideal及FIBRES的原理想、ξ与Poincare纤维节点。没有用real_descent三倍对象替换原I_Z。

准确等价式为

Ei(T7)η_j=0于J_Y(Q)⊗Q
当且仅当Ai(T7)ξ_j=0
当且仅当[ni]Pi(T7)ξ_j=0。

真实循环7对应的迭代应按H(L)=Nm_target(source*L)计算，配tensor幂取得Picard类−Ai(T7)ξ_j的零度线丛。完整RR的h0=1才给零类，h0=0才给非零类。已成80条计划均保持实际RR维数、主生成元和活跃因子为null。

若后继得到A⊗B^−1=hO，原c0刚性化的A→B映射仍为乘c0/h，P1纤维比例为c0/c1；原RF例为κ_j/R_j(P1)。本次没有生成h、c0、c1或非p地方校正。

**可直接使用的正向有限证书。** 对一个原i,j，在同一完整对象合法好约化的素数处，若真实有限域Picard算术给[ni]Pi(T7)ξ_j的约化非零，则上述原有理类本身非零，故Eiη_j非零。若约化为零，不能据此宣布Eiη_j为零；仍需其他真实证据。若16块各有至少一个这样的原j非零证书，才可认定五点的联合活跃支持为全部块。本次没有计算这些约化，不预设其非零。

这一推论只是R870准确挠判与约化同态的直接组合，提供后继可用的较小非零出口，不替代原主函数、刚性化或完整height所需的校准。

## 5. 真实来源与输出身份

执行方法为[最小整数消费者](../notes/R870-original-Y-torsion-Hecke-inputs-consumer-method.md)，[激活记录](../notes/R870-original-Y-torsion-Hecke-inputs-activation.md)保首请求。实际core为32158字节，SHA256
`0e32a7f0cb75efb762b069de7b55217d94aaeb23f100594eaba4ecee18dd7006`；wrapper为35252字节，SHA256
`fc0fb7a76fd4515b959d424f10fa52052b792c73119478b419ab94dd1b3d94c0`。

方法SHA256为42799fe505ee573a3884a953dd3c836731c250e27234291de46cc081fd22c09e；数学configuration fingerprint为f4d082f109807b060f220023dd4bef3881b37128a38ec0d9fe287a1f148eebdb。实际首请求16503字节/9083cae5753cc2474083fe55b8b72eb3b0879e6fb3d5c273ea9dd1c7c1ecfb95。

| 已成对象 | Bytes | SHA256 |
|---|---:|---|
| 最终证书 | 10687 | be29c87289d41b7acf4ad32bce48fe68495e094a22823ef46327bfb01bb559ae |
| 普遍有理挠点整数与完整除法 | 9161 | 89cc393ea4ae5552d269f925a4fecb9af47c042c45ca616d5300f214e80eaa33 |
| 共同d*及16个整数对应 | 1899605 | 3ca6b9d41548bb782d399a3d15b2c7e6ace22d45406aa8fe9806ec611acb3e9f |
| 五点/80项Picard与校准计划 | 6932 | fe07d2ff9e375316b4517e1ab685bbb70662cbcef7d377185c813b782bad07c7 |
| 20完整stage索引 | 3262 | e5f23226d4c3ec48b25bb7177abbc51157429aab34aee8152e761d39f94cb4d4 |
| 全部30项输出manifest | 4517 | 0d7fa705ebd3ed56aaeb1ae07ed7bf5b9bfaf84271f2c7b958fb8a6a219c6dd1 |
| 42原件最小载体 | 1495243 | 6a9d22de285d81c69667b1d0ecf6026b244ec391c8bb5101726861917dadc327 |

最终证书文件名为p41-original-Y-rational-torsion-and-Hecke-support-inputs-certificate.json。16个逐因子stage的完整SHA保于该证书与stage索引，后继直接读取，不重新因式分解。

artifact14205027300，名serre-R870-original-Y-torsion-Hecke-inputs-43822039811-1，共4112038字节，ZIP SHA256
`723ec402304ae818683ed08d98078e55484b944b00bcd66e80b7474bffb5e94f`，到期2026-11-17 07:12:00 UTC。root确实下载并核了整个ZIP及全部30个输出成员。本次最小42原件为R865的26件、GLOBAL的8件、FIBRES的8件，实际旧source/core/tag与原文件SHA完整保留。

没有消费旧127矩阵、约395MB全局opaque载体，亦未重建Fourier、H、J或其逆。所有新算术由本公开Actions完成，机器输入、阶段及回执只保必要的一日artifact/carrier。原η支持、eη、主函数、非p地方高度、指定高度数值与非零均未被此次成功提前宣称。
