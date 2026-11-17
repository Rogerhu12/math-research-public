# R638：两条实际前缀的全域正弧长坐标与 C² 映射

**已证明的范围：** 对下面固定的精确 binary 共同节点映射，在标准 IEEE binary64 四则/平方根运算模型下，向外区间计算严格封闭全部径向位置和全部角度上的 q_N、ρ 正性。因此此前两条弧长规范化候选的隐式坐标在整个开放前缀上有定义，且是 C² 映射。这里没有把采样 Gram、曲率、嵌入、reach、闭合或全 t 族升级为严格证书。

## 1. 固定对象和实际结论

第一条是[β=.75 的规范化前缀](../notes/2026-11-17-parallel-numerical-arclength-normalized-prefix.md)，原接受数据 SHA256 `852a673f4464090f003fd44c3247a819cf9bae0418d07caf97f8edb0e3d39471`。M112，509个共同 quintic 胞元，固定构造 N2048。

第二条是[原前缀与 pulse 桥的完整拼接](../notes/2026-11-17-parallel-numerical-pulse-arclength-prefix.md)，拼接数据 SHA256 `26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72`。M320，818胞，固定构造 N4096。旧498胞的原 M112 二jet与新320胞的保存二jet逐位相接；本证书直接使用完整保存 d2，未用 M320 RHS 重生旧二jet。

节点和0/1/2jet均视为精确实数的 binary64 数据，每胞为其唯一 Hermite 五次式。第一条二jet由原冻结 M112/N2048 JVP 再生后固定为 binary 数据，证书不声称它是精确 ODE 解。按 x,Y,D,DD 顺序、行优先 little-endian float64 拼接的 SHA256 分别为

- β=.75：`64632a0425e29fbcb6d08503032381b409e4f121bbbc249a631e73892b05e336`；
- pulse：`840193a1cdb37f79d04f5f36f5a0c485c4eb50f3fd2a103af8c4c267d5232793`。

| 固定场 | 整个前缀的 q_N 下界 | 固定ρ的全角下界 | 最差径向胞 |
|---|---:|---:|---|
| β=.75 | ≥.11521439717031048 | ≥.1521176778215779 | [.9275,.93] |
| pulse 至1.0 | ≥.09866635452557888 | ≥.15909568175875186 | [.9475,.95] |

保守的十进制陈述可直接取 q_N>.1152、ρ>.1521，以及 q_N>.0986、ρ>.1590。它们不是径向采样最小值；下面的径向与角向余项已全部扣除。

## 2. 不循环假定 q>0 的全域准则

令 q=|Fφ|，I_N 为含单 cos Nyquist 项的实三角插值，q_N=I_N q。其基函数为

\[
 l_j(\phi)=N^{-1}\left[1+2\sum_{k=1}^{N/2-1}\cos k(\phi-\phi_j)
 +\cos\frac N2(\phi-\phi_j)\right].
\]

离散正交关系给

\[
 \sum_jl_j(\phi)^2=\frac{N-1+\cos^2(N\phi/2)}N\le1,
 \qquad \|I_N\|_{\infty\to\infty}\le\sqrt N.
\]

在一胞上若 |F_sφ|≤B，则范数的反三角不等式直接给

\[
 \|q_N(s,\cdot)-q_N(t,\cdot)\|_\infty\le\sqrt N B|s-t|.
\]

这一步不除 q。F_sφ 的径向次数为4，将其转成五个 Bernstein 控制向量后，用凸包性质。对每个向量，旋转坐标 R/T/Z 的角分量 l1 界是

\[
 \sum_{j\ge1}|\nu_jR_j+T_j|,\quad
 |R_0|+\sum_{j\ge1}|R_j+\nu_jT_j|,\quad
 \sum_{j\ge1}|\nu_jZ_j|,\qquad \nu_j=2j.
\]

三者平方和开方，再对五个控制向量取最大，即为 B。

每胞用4个等分区间。对每个分点的 q_N，区间变换在 Q=2N 角网得到向下的最小值，再扣 π/Q 乘全角导数上界。后者由正频率给出

\[
 2\sum_{k=1}^{N/2-1}k|\widehat q_k|+(N/2)|\widehat q_{N/2}|.
\]

任意径向点距最近分点至多 h/8，故整胞下界还扣 h√N B/8。β最差胞的分点全角下界为.17368866952108447，径向扣量≤.05847427235077397；pulse最差胞对应为.18293274560262746与.08426639107704856。ρ是固定有限余弦多项式，直接使用同一角向区间/导数覆盖，不需要径向扣量。

## 3. 数值封闭方式

[区间源](../scripts/parallel_20261117_arclength_interval_positive.py) SHA256 `f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d`。所有数组加减乘除/平方根均将下端 nextafter 到−∞、上端到+∞；上界求和逐项向上，不依赖库 reduction 的舍入顺序。假设基础运算遵守标准 IEEE binary64；溢出、无效运算和除零立即报错。

没有把库 FFT 的输出当精确 Fourier 系数：源实现有方向区间 radix-two 变换。π来自 Machin 的16atan(1/5)−4atan(1/239)，各80项交错级数及下一项给有理包围。角因子用10^80整数区间及40项 Taylor 递推；22/7 上界核验尾项小于10^−75。每个有理数转 binary 的包围端点再用 Fraction.from_float 精确核对，因此转换误差也被封闭。实 q 的偶性使其精确正弦系数为0；Nyquist 按正负各半放入 Q>N 网格，未遗漏该项。

Hermite 系数、四次 Bernstein 转换、角系数 l1、径向 h、√N 和两个覆盖扣量同样向外计算。两对象的 q_N 角网格区间最大宽度分别小于6.363e−10和2.178e−9，远小于正性余量。程序检查有限完整数组、严格递增节点、字段维数、dyadic 网格，并拒绝非有限证书；入口冻结源码身份，出口核验没有中途修改。两份输入在运行中保持冻结。

独立审阅核对了插值范数、Nyquist、旋转导数和 Bernstein 链；另以精确 Nyquist、三个有理速度平方、二次 Hermite 例检验了实现接口。这些检查不替代上述全509/818胞的实际区间运行。

## 4. 坐标和 C² 结论

因为 q_N 在构造节点准确等于 q，严格正性先保证这些节点的速度范数非零。有限角谱及共享径向二jet使 F_ssφ 连续，故每个构造节点的 q、所有 q_N 系数以及 b=mean(q_N) 均为 C²；这里不需要未经证明的“任意 joint C² 映射都有 F_ssφ”。

ρ>0 且 meanρ=1，b>0。方程

\[
 \int_0^{\psi(s,\phi)}q_N(s,u)\,du
 =b(s)\int_0^\phi\rho(u)\,du
\]

在每条圆周上唯一确定严格单调的周期提升，ψ(φ+2π)=ψ(φ)+2π。对左端变量的导数 q_N>0，隐函数定理给 ψ 为 C²。取已声明的精确 C² 标量 a(s)，则

\[
 \widetilde F(s,\phi)=c(s)+\frac{a(s)}{b(s)}
       (F(s,\psi(s,\phi))-c(s))
\]

为整个前缀上的 C² 映射，原径向共享二jet经同一个算子仍共享。这结清原记录留下的坐标正性条件。

此结论仅保证该映射有定义且 C²；它没有单独证明 F 的 immersion/全局单射，更没有形成闭面或全 t 族。已有 Gram/主曲率仍是有限采样读数，标量精确积分与其 Gauss 求值误差也没有在本证书中重封闭。共同材料精化、完整闭尾、held、含反射 E3 与 reach 保持未付。

## 5. 复现和实际输出

S为本题scripts目录，单线程并设置PYTHONDONTWRITEBYTECODE=1。所有raw保持仓库外。

```sh
PYTHONPATH="$S" python "$S/parallel_20261117_arclength_interval_positive.py" --input parallel-model-inward-svd-b075.json.gz --construction-angles 2048 --angles 4096 --radial-subdivisions 4 --out parallel-model-inward-b075-arclength-interval-positive-final.json
PYTHONPATH="$S" python "$S/parallel_20261117_arclength_interval_positive.py" --input parallel-pulse-a5-complete-base.json.gz --construction-angles 4096 --angles 8192 --radial-subdivisions 4 --out parallel-pulse-a5-arclength-interval-positive-final.json
```

最终报告 SHA256 分别为 `17be30d89d4b53553311ddc7d55d83038a494590b9760cb54f3898b6a7e719dd` 与 `a70aa9a2bb6b38e5bf17fdd9a14aa67309124e3f794972267599082cef4c6337`。原浮点准则/评估保留在[前置记录](../notes/2026-11-17-parallel-numerical-arclength-positive-bound.md)，其未定向舍入的数值不被追溯改标为严格证书。
