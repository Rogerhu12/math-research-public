# R150：h=k 非 1 原碰撞的完整 Delta 因式与三均值必要 core

日期：2026-11-27（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

接续[完整原 Gram 与 Delta 首一四次](R150-appendix-unit211-equal-singleton-values-full-original-Gram-and-Delta-quartic.md)。本稿对同一个原输入的 Delta 和前三个均值分子作完整 QQ 因式返回，选出下一步真正原均值 core。没有以多变量 gcd 为 1 宣称原点不存在。

## 1. 原范围及实际清尺度

仍取旧矩图

$$\ell=A^3/B^2,\quad c=\ell-b,\quad h=k=1+B/A,\quad
u=(1+\rho)b+(1-\rho)c,$$

其中 A=2lambda²−2lambda+1，B=4lambda³−6lambda²+3lambda−1。原 Gram 使用已付的正确尺度

$$H=bc\Delta.$$

Delta 非零图保留全部八个原条件。本次只剥原 A,B,rho,p,q,lambda,b,c,P02 的非零因子，以及这个明确 Delta 非零图的 Delta 因子。没有使用 T0、Pf、S、ell−u 或物理 D 的逆。每次剥除实际 gcd 后立即乘回，最后把全部比例完整乘回原分子；原八行没有被替换成任意必要投影。

## 2. 整个 Delta 四次没有出现新的低次 QQ 分支

对原 Delta 分子去掉原物理单位后，准确必要分子的 (b,lambda,rho) 次数为

$$(4,24,4),$$

总次数 32，348 项，规范 SHA256

ace2f6cdfb7d020cbef435335c8e148b3f666f17d147ef3c2521222667411faf。

本次没有剥出任何非恒定原物理因子。QQ 完整因式返回只有一个一次幂因子，分量次数相同；其整系数规范 8351 字节，SHA256

64434431418e6550b36f39c2adb1053f63c3d9c2e318cbe0e5ba42fbdec003a2。

完整乘积回到原分子，非零有理内容为 1/2097152。故这一新因式输入没有把原首一四次分裂为更低次分支；后续仍保留完整四维环境，而非从若干模因子挑分支。

## 3. 三个原均值的全部 QQ 因子

对原 E1、EB、EC 分子仅剥已付物理部分，所得必要 core 的次数都是 (12,80,12)。它们分别有 7078、8033、7948 项。完整 QQ 因式返回为

$$C_1=a_1(2\lambda-1)^2F_1,\quad
C_B=a_B(2\lambda-1)^2F_B,\quad
C_C=a_C(2\lambda-1)^2F_C,$$

其中三个 a 都为明确非零有理数，三次完整因式乘积逐项回到各原 core。剩下三个单因子的实际信息是：

| 原均值来源 | 剩余 (b,lambda,rho) 次数 | 项数 | 规范系数 SHA256 |
|---|---:|---:|---|
| E1 | 12,78,12 | 6896 | fa60296a5aa6e939f2750dc3afc3d929b6973111b693d41aefedbc4062e79fdc |
| EB | 12,78,12 | 7827 | 2490b821e9a223d6d5efc26dfec96aca108512898fd7c1f05e515f75d7108b22 |
| EC | 12,78,12 | 7744 | 0ff8290ee4d4966d79d6fe5fcfe9d6181f87c811afd48a66fff29646b0353e20 |

三个 C 的 QQ gcd 恰为 (2lambda−1)² 的非零有理倍数。因而 F1、FB、FC 没有共同非恒定多项式因子。它们处于三个变量的多项式环中，**这不表示它们没有公共曲线或公共点，也不提供有限性或空性结论**。

## 4. lambda=1/2 已由旧完整物理返回支付

在这个 h=k 图上，lambda=1/2 使 h=k=0、w=0、S=0。该支早已由
[S0 等值 lambda-half 完整原物理排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-equal-values-lambda-half-exclusion.md)
支付。

旧证明完整区分 t 非零与 t=0：前者由原 E/P 四式矛盾，后者确有抽象必要族，必须补原第五列并使用同一六维物理 Gram 的秩下界才排除。本稿不重做该结论，也不将其改写为尚未构造的裸多项式单位理想。

因此对当前**实际物理原点**，2lambda−1 非零，三条新的必要条件确为

$$F_1=F_B=F_C=0.$$

这只是支付后的原必要系统，不把上述物理点排除提升成全局幂身份。原 Delta 零图与所有未付权面继续独立保留。

## 5. 实际执行

源：[原 Delta 与三均值完整 QQ 因式](../notes/2026-11-27-unit211-equal-singleton-values-primitive-original-mean-and-Delta-factors-8542.py)。

- Git blob：2794ac118f7927bec465941e6c0a7fcd80a3b646。
- SHA256：83ea9f06b6e45e8c743931cc811534c011920db8cb24f1bae310a76e6854e273。
- Actions run/job：46000054660 / 140509099684。
- 实际内层 exit0；源 2.257465187 秒，驱动 2.327275144 秒，RSS77896 KiB。
- stdout11551 字节，SHA256：d4403bf1e3c0bb60b5d246044e3e803a8c0fb0d822935853a41c4a7a0da58670。
- 源 main：38a775911837f5d05997c352941771996ebf67d4。
- 12:36:43.215861 UTC 实际 pull 后，两 README 无差异。
- 上限180秒/4GiB；未计算大的 b 消元投影，未重跑旧完整八行门。

完整源与小回执保存每个原比例、次数、大小和哈希；三十余万字节的各必要 core 不另存缓存。下一输入改用交换两个标签后不变的 u,Q 权坐标恢复原条件，保相同原 Gram 与全部例外。整个 h=k、R150 和 ordinary ISP 仍未排空。
