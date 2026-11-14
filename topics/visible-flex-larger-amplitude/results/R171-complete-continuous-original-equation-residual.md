# R171 — 原背景上完整连续候选的全方程残差

作者：/root（GPT-6 Astra Pro，AI-assisted），2026-11-13。

## 已完成的结论与范围

R170 的 216 段精确 binary-rational Hermite 候选，在原来的 3940 个真实背景叶上，按原 stage 边界细分为 3976 叶。R171 的 63 个批次均有独立 wait4 正式 exit 0；精确正项汇总覆盖每叶恰好一次，得到以下 **未乘传播核的 source-x 积分残差上界**。表中十进制仅为向上宽化的便读值，原证书保存严格 dyadic 端点。

| 原 cell | 低 46 模完整残差 L1 | 全部 m≥94 残差 L1 | 低频共用逆余项 L1 |
|---|---:|---:|---:|
| 9 | < 2.756e−9 | < 2.622e−37 | < 1.568e−297 |
| 8 | < 2.285e−5 | < 1.892e−29 | < 4.877e−160 |
| 7 | < 0.154753 | < 1.325e−21 | < 6.591e−26 |

这证明所定义候选的连续残差界；不证明实际 R143 解在 R170 管中，不是 Green 算子误差界、非线性自映射、外侧全部区间的存在性或闭曲面完成证书。cell7 当前低频界仍大，必须继续处理。第三列的共同余项已包含在第一列中，不能再把同一共同预算免费分配给每个模。

## 原方程与坐标

沿原 source 坐标 x，令 s=r_x/r、ell=(log w)_x、E=1+w²。候选非均值部分 P 为正弦系数、barK 为余弦系数，K=c+barK，其中 c 是 R170 已证明唯一的完整原均值根。这里的原状态 Π 不是 canonical Xi；R168/R169 的实际 root/split-RHS 坐标转换与导数身份全部继承。

对每个正偶模 m，残差为

    RP_m = P'_m + (s+ell) P_m + m s K_m,
    RK_m = K'_m + m ell P_m + 2 ell K_m − N_m,

其中完整非线性为

    N = Pi_perp { [E s (Ktheta−P)^2
                 + ell ((K+Ptheta)^2 + w²(2 K Ptheta+Ptheta²−P²))]
                 / (1+K+E Ptheta) }.

候选仅有 m=2,…,40 的显式非均值系数，但 N、均值根和角逆均未截断。Hermite 导数从 local stage t 转原 x 时明确乘 8。每段 Bernstein 系数以精确有理数保存，范围限制使用精确 de Casteljau；本结果仅需分段导数与 R170 已付的 C0 连接，不把端点数值当连续证书。

## 均值、角逆和真正正的无穷尾

在每叶上从 R170 的唯一根域出发，按原完整恒等式 c+c²/2+q0+R=0 连续交 4 次真实区间。每次保留完整 binomial/inverse 余项 R，使用稳定分支 c=−2q/(1+sqrt(1−2q))；不是有限角求积均值。

Laurent 索引 k 对应物理频率 2k。将 P=−i PI、Ktheta−P=i UI 写为实系数 Laurent 多项式，故两个平方的符号严格保留：BS=−E UI²，BL=(K+Ptheta)²+w²(2K Ptheta+Ptheta²+PI²)。设非恒定分母 L=barK+E Ptheta，a=1+c，a_min 为正下界，x=||L||_(sigma=1/2,0)/a_min，yd=||dtheta L||_(sigma=1/2,0)/a_min。

所有叶直接验证 x<1。逆多项式阶数 Q=32，完整 W1 逆尾显式界为

    rt0 = x^(Q+1)/(a_min(1−x)),
    rt1 = rt0 + [(Q+1)x^Q yd/(1−x)
                 + x^(Q+1)yd/(1−x)^2]/a_min.

完整逆 W1 范数不超过 1/(a_min−||L||0)+||dtheta L||0/(a_min−||L||0)^2。低 46 模逐项保有向有限残差区间，余项由 |s| ||BS||1 rt1+|ell| ||BL||1 rt1 **共同支付一次**。

输出范数为 sigma=1/64 的 sum (1+m)e^(m sigma)(|RP_m|+|RK_m|)。m≥94 的候选及导数为零，完整残差来自 N，故用在 sigma=1/2 的完整源 W1 乘 exp(−94(1/2−1/64))；这是所有高模的共同正上界。没有把尾端浮点下溢成零，没有把有限角格点或有限 Fourier 截断当完整方程。

## 背景与覆盖

原 SourceValues/PositiveKernels 的全部源身份由 R170 输入链固定。r、w、ell 复用已有真背景 whole-leaf 包。少数原 radius_x 的中点半径表示跨 0 时，用同一原式

    r_x = |w ell|/(8 E^(3/2)) + alpha ro_x/E

明确支付严格正端点下界 alpha ro_x/E，再与原包及原式上界相交。Arb 的圆球表示可能仍跨 0；证书分别记录真实严格正下端点，绝不把表示跨零解释成真实物理导数变负。s 的整个包用于残差，不调用 1/s。

每个 batch 只称其声明子集完成。组合程序核实际 owned0、源/输入/全部 profile SHA、范围无重无漏以及原 R170 每叶身份；然后以 Fraction 精确求正项和并向上转为 256-bit dyadic。3976 细叶恰好还原原 3940 叶。逐模 L1 的有限逆部分额外保存，但不把共同逆尾重复分配给各模。

## 实际资源、失败及重建

63 批 worker 墙时之和 786.731 秒，最大 RSS 69836 KiB；各批正式资源保存在完整小记录归档中。组合实际 exit0、15.369 秒、58436 KiB，12636 项身份/覆盖/正项组合检查。worker 源 SHA `86c1a7aab0df68b5b11054a7da22b1f015035309f2e8ebd8f0a845d1c79ce671`，组合主证书 SHA `50cf35f71ae4754e3850599c060e0e3eaf56b3bdca5115a50c61160caac48e6c`。

v1 的 arb_poly / arb API 错实际 exit1；v2 的旧严格 s>0 表示门实际 exit1；两者源、argv、完整日志和 owned 资源保留。v3 会话丢失前写下 9 个 chunk，却没有 final/owned 资源，不能称 exit0，也不称数学失败；其部分输出仅保 inventory，正式结果由原数学内容不变的 v4 独立完整批次重建。成功批次不重复计算。

`notes/2026-11-13-root-R171-complete-residual-manifest.json` 是稳定归档入口。125 个成功 profile 块完整保留；小记录归档保存每个原文件的 base64 原字节、SHA 和原路径，包括所有资源、主证书、plan、launch 与日志，恢复后 SHA 必须一致。输入沿 R170 已存身份链还原；先运行 owned batch driver，再运行本组合命令，原 argv 均在归档中。不新增独立审核、冻结或重复运行门。
