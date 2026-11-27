# R150：一般等权图的 singleton 均值 y=1/2 支为空

**已证明。** 在原一般 LS、unit 2+1+1 非零孤立均值图中，b=c 时不能有 y=1/2。这里 y 是两个原 singleton 均值 X=x+yr、Y=x−yr 的奇部系数。一般等权图与普通 Hilbert ISP 仍未完成。

会话 Astra-ISP-8542378f-20261127；2026-11-27（台北）；AI-assisted GPT-6 Astra Pro。

## 1. 已付原坐标与分支

沿用[原均值差首项零支排除](R150-appendix-unit211-equal-weights-original-mean-leading-zero-exclusion.md)。写
$$
m=b+c=u,\quad d=1-Q,\quad v=2y-1,\quad
x=m+(y-1)z,
$$
$$
t=2(1-z)+[2(z-d)y-Q]/m,
$$
$$
F=zdv^2+(m-1)(d+z^2)v-z(2m-1)=0.
$$
此前完整原返回已经支付
$$
A_m=(d+z^2)v-2z\ne0,\quad z\ne0.
$$
这些单位由各自整个零分支排除而来，不是本稿新增假设；仍保原 m、m−1、Q、d、P02 及原值判别 D_val 非零。

若 y=1/2，即 v=0，F=0 和 z≠0 准确给 m=1/2。原恢复式随即成为
$$
x=(1-z)/2,\quad t=0,\quad f=(1-z)/4,
$$
$$
A_G=0,\qquad r_G=s_G=-z/2.
\tag{1}
$$
这里 Q、d 没有特殊化。

## 2. 同一个原 N1 恰为物理单位的倍数

直接在 (1) 的原 Frobenius 代数与 Gram 中计算
$$
P_{02}=3d/4,\quad
N_4(k_0)=d(3-z)/4,\quad
J_0=\tau((k_0-\tau(k_0)1)^2(k_1-\tau(k_1)1))=-zd/8.
$$
由原 L=lambda P02、J0=wP02，
$$
\lambda=(3-z)/6,\qquad w=-z/6,\qquad T=-1/2.
\tag{2}
$$
所以原值矩的物理单位为
$$
D_{\rm val}
=m(2\lambda^2-2\lambda+1)-T^2=z^2/36.
\tag{3}
$$
原双点 N 极化准确为
$$
N_H=-dz^2/12=-3dD_{\rm val}.
\tag{4}
$$
(4) 的两因子 d、D_val 都是原已付单位，矛盾。故整个 y=1/2 支为空，不需要把 Q 或 z 再投影到任何抽象根。

## 3. 原执行返回及后续范围

实际计算使用已提交的完整原图源
[regular-original-chart](../notes/2026-11-27-unit211-equal-weight-regular-original-chart-8542.js)生成原 E1、EBe、N1、Ns、Ps，再把同一个 m=y=1/2、Q=1−d、z 返回。其 N1 行定义为
$$
\frac{P_{02}N_H}{m^2(m-1)^2}.
$$
返回准确为单项式 −d²z²，故结合 m=1/2 和 P02=3d/4 即为 (4)。没有把已清分母行误当原 N_H，也未换原 h、k、lambda、T。

两个原 mean 同时恒零；加权 N/P 返回只是额外必要信息，未用于最后矛盾。原 (2)—(3) 的低次身份亦可直接按显示 Gram 手算。

[实际新返回函数体](../notes/2026-11-27-unit211-equal-weight-half-mean-original-return-8542.js)，SHA-256：0d11eb266b841da217640b85425c33519a1b83bba5491e7e7bdf0ae9d7741150。
纯 V8 BigInt 有理运算实际0.032秒，正常返回；没有 OS 子进程退出码或 RSS 可报告。[小回执](../notes/2026-11-27-unit211-equal-weight-half-mean-execution-8542.json)保规范输出 SHA。

该函数体以已提交原图源的返回对象为唯一参数，不读缓存或外部 JSON。原图本身的构造不是本稿新增结论；新输入是整个 v=0、m=1/2 原纤维的准确返回。

因此一般等权余图现在同时可用 v≠0、v≠1、z≠0、A_m≠0、dv²≠1。剩余原 mean/N/P 和原值条件仍须继续，没有证明一般等权分支全空。
