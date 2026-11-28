# Phi 的整个 D2=0 无穷方向：原四二次式压缩到五个候选权值

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

**后续状态：** 五个候选的全部纤维已由[整个 D2 最高方向的原 Bézout 排除](R150-appendix-unit211-Phi-zero-whole-D2-highest-direction-original-exclusion.md)关闭。以下保留此前候选压缩的完整推导与唯一执行身份。

## 1. 此前已成范围

在当前 $\Phi=0$、物理 $D\ne0$ 的原权图，整 H1 已排除，因此第一原二次头可付。给 $\lambda,T,z$ 同赋次数一，令 $t=T/\lambda,s=z/\lambda$。本文处理原最高部分 $D_2=2\ell-t^2$ 的整个零方向，保留物理 $D$ 与其最高部分的区别。

**结论。** 任何满足全部原最高必要式且 $D_2=0$ 的非零无穷方向，都必须有
$$
\ell=\frac12,\qquad t=1,\qquad Q=4(u-1)(u-2).
\tag{1}
$$
在这条完整权曲线上，四个原二次式实际给出一个清分母身份；只剥已付权单位后，剩余六次一元支持完整分为一个不可约四次因子与一个不同的一次因子的平方。因此这样的方向最多涉及 **五个不同的 $u$ 值**，亦即五个有限权对 $(u,Q)$。

在本稿原执行时，这五个整纤维尚未排除；现已由上列后续完整论证排除。本文没有给出原仿射解数界，也未关闭整个 Phi。真实最高零方向本身已经限制到上述有限权集；原权参数的无穷处不在这个陈述内。

## 2. 规范最高方向与整几何缩约

[整 H1 原排除](R150-appendix-unit211-Phi-zero-whole-H1-complete-original-exclusion.md)支付原三均值的 T²,Tz,z² 头矩阵。在一个非零最高共同方向中，若 $\lambda$ 方向坐标为零，则这三个平方单项式全零，迫 $T=z=0$，与方向非零矛盾。所以可以在最高齐次式中规范 $\lambda=1$。这个步骤未在原仿射方程中倒置物理 $\lambda$。

沿[完整 NV/F6 最高式及原提升](R150-appendix-unit211-Phi-zero-whole-first-head-highest-original-NV-F6-filtered-lift-and-twenty-one-generators.md)，有
$$
D_2=2\ell-t^2,\quad
K_3=4\ell^2-6\ell t+2t^3,\quad
\overline F_6=MK_3^2-4m^2D_2^3.
\tag{2}
$$
当前 $M,\ell$ 均为已付原权单位。若 $D_2=0$，由 $F_6$ 得 $K_3=0$。用 $t^2=2\ell$，
$$
K_3=2\ell(2\ell-t),
$$
所以 $t=2\ell$，再代入 $t^2=2\ell$ 得 $\ell=1/2,t=1$。原 Phi 恒等式
$$
\ell=1-\frac{2(u-1)(u-2)}Q
$$
给出 (1)。

在整曲线上，
$$
M=-2(u-1)^2,\qquad
\delta=1-Q=1-4(u-1)(u-2).
\tag{3}
$$
$u-2$ 在此曲线上已付，因为 $Q$ 和 $u-1$ 已付。原最高 NV 在此方向为零，因此本文直接保留其它四个原二次式，未从这个零值虚构约束。

## 3. 四条真正原最高式

令 $F_i$ 为同一原定义中的 Rbar、W4、Obar、N1，定义
$$
h_i(u,s)=[\lambda^2]\,
F_i\bigl(u,4(u-1)(u-2),\lambda,\lambda,\lambda s\bigr).
\tag{4}
$$
源码从原式按总次数精确提取，完整保留 0、1、2 次分解并乘回。每条分母只含 u、u−1、u−2、delta 中已付因素。没有求逆旧二次头，没有构造旧三列规则或重新执行最高 Gaussian。

四个最高式的实际规模为：

| 原式 | 分子 u 次数 | s 次数 | 分子项数 | 分母 u 次数 |
|---|---:|---:|---:|---:|
| Rbar | 10 | 2 | 24 | 4 |
| W4 | 12 | 2 | 30 | 4 |
| Obar | 13 | 2 | 32 | 6 |
| N1 | 13 | 2 | 32 | 4 |

规范 h_i 由 (4) 和原源唯一定义，不另保存可重算系数表。

在 $\mathbb Q(u)[s]$ 中按上述顺序作 Euclid，每次除法都返回完整乘积，四原来源持续保留。实际 gcd 次数链为 0、0、0；最终实际给
$$
1=\sum_{i=1}^4 a_i(u,s)h_i(u,s).
\tag{5}
$$
原来源允许某个最终乘子为零，不要求四个都非零，也不把泛型 gcd 为 1 当作整权曲线排空。

## 4. 最终分母的完整支持

取所有 $a_i$ 的系数分母最小公倍式 $C(u)$，令 $\beta_i=C a_i$。实际逐系数返回
$$
\boxed{C(u)=\sum_{i=1}^4\beta_i(u,s)h_i(u,s).}
\tag{6}
$$
C 的准确次数是 16、17 项，定义 SHA256 为
ef6bf7eaf584bd6cf4c3c5ad98ba2720e2909b170e54eb725559f22d751a44d1。

原中间主元的零点全部包含在 (6) 的多项式身份中。随后实际仅剥 u−1 两次、u−2 六次及 delta 一次，故
$$
C(u)=c\,(u-1)^2(u-2)^6
       \bigl(1-4(u-1)(u-2)\bigr)\,C_6(u),
\qquad c\in\mathbb Q^\times.
\tag{7}
$$
$C_6$ 为首项归一的准确六次多项式，7 项，定义 SHA256 为
4c0fbc2110711d6466f801b1b18dac4a19dc98dd67d9e19f281d7036cfd976f1。

完整 QQ 因式及乘回实际给
$$
C_6=\eta\,F_4 F_1^2,\qquad\eta\in\mathbb Q^\times,
\tag{8}
$$
其中 F4、F1 分别是唯一的四次和一次不可约因子，规范定义如下：

| 因子 | 次数 | 项数 | 在 C6 中的幂 | 原定义 SHA256 |
|---|---:|---:|---:|---|
| F4 | 4 | 5 | 1 | 99c6aea629beae631b0b9f1b113022eb548b33b1e162403e3e80565c88b0919e |
| F1 | 1 | 2 | 2 | e9280b10191f0bd264db452dfc19bff862a1464f70c181519b8710bfba5a4adc |

(6)–(7) 表明每个允许的最高共同零方向必须满足 $C_6(u)=0$。特征零下两个不同不可约因子均可分，所以不同候选 $u$ 值数至多 $4+1=5$；$Q$ 由 (1) 唯一确定。平方因子的完整重数仍保留，没有将有限候选点误称为已排除点。

这里尚未对五个整 s 纤维完成原返回，也未加入原 P6 的最高头。因此不从这个支持界推出任一原 lambda 首一性或原仿射点数界。下一项新输入是这些方向与已经成立的原 P6 头的同点返回。

## 5. 唯一实际执行

[唯一源](../notes/2026-11-28-unit211-Phi-zero-whole-D2-zero-infinity-original-four-quadratics-8542.py)及[执行前输入](../notes/2026-11-28-unit211-Phi-zero-whole-D2-zero-infinity-original-four-quadratics-8542-input.md)：

- 最终 blob：321647e9cd06500e769bb0b6b8119659e4bd95fd。
- 源 SHA256：baf684e40df5e447c6dfcb9f5eb3eef8173d28d6ae1a37e152c4475ff342b03c。
- [run 46088131910](https://github.com/Rogerhu12/math-research-public/actions/runs/46088131910)，job 140802461762，attempt 1。
- 实际 driver：0.120667964 秒，最大子进程 RSS 39880 KiB，真实内层 exit 0。
- 源最终数学阶段：0.082009484 秒，源报告峰值 39488 KiB；不混同 driver 峰值。
- stdout：3855 字节，SHA256 7c57c07c2c1d6d18e2b5d611d3e59071acd46db66261daee284b626187d54888。
- 源提交及实际 pull 后提交均为 9a9868c5e67083a3bd07563d0d8d2853a8bff52a；实际 pull 时间 2026-11-28 00:29:33.979111 UTC，两份 README 未变。

仅执行原四式定义前缀 4452 字节，其 SHA256 为
ea859ab09cc447cd05f30b02d8baa4280c08cdbd40bfa45d5b42034b0cf9356e。
未重放旧原头、旧三列模块、最高 Gaussian、P6/P9 或范数；未输出或保存系数载荷、编码或分片。ordinary ISP 尚未完成，继续上述原五权支及其它开放输入。
