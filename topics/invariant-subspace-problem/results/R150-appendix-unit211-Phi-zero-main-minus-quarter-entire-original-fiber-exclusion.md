# Phi=0 主图 v=-1/4 整权纤维：原三均值返回物理 D 为零

日期：2026-11-28（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

## 1. 同一原纤维与结论

本稿接 [主图八权参数覆盖](R150-appendix-unit211-Phi-zero-main-rho-head-eight-weight-cover.md) 及 [v=-1/4 的真实原 lambda 约束](../notes/2026-11-27-unit211-Phi-zero-main-minus-quarter-lambda-half-return-8542.md)。范围仍是原 unit211、LS、$\Phi=0$、物理 $D\ne0$ 的主 rho 二次头零支
$$
u=1+v,\quad Q=1-v,\quad \ell=1+2v.
$$

已实际证明 $H_7(-1/4)=-169/512\ne0$，且同一原三多项式在 $v=-1/4$ 的完整 QQ gcd 为 $\lambda-1/2$。因此该权纤维若存在原解，必位于
$$
(u,Q,\ell,\lambda)=
\left(\frac34,\frac54,\frac12,\frac12\right).
$$
本稿给出这个点上完整原三均值的多项式恒等式，直接迫使 $D=0$，与原物理条件矛盾。故整个 $v=-1/4$ 原权纤维排空。

没有使用另一个特殊有序权图上的 $\lambda=1/2$ 结论；$H_7=0$ 的整纤维仍单独保留。

## 2. 从原关系代入，无额外分母

令 $z=Qt$，沿用原值坐标 $T$。直接代入原权定义有
$$
T_0=-\frac14,\quad J=1,\quad
P_{02}=-\frac5{16},\quad P_f=\frac1{16},
$$
$$
m=\frac14,\quad M=-\frac18,\quad bc=\frac18,\quad
A_2=\frac12,\quad G=-\frac3{32}.
$$
原 P1 在 $\Phi=0$ 上为 $P_f f+P_c=0$。由于 $P_f=1/16$，
$$
P_c=-\frac7{32}-\frac{25}{64}T,\qquad
f=\frac72+\frac{25}{4}T.
$$
因此原物理量准确为
$$
D=\ell A_2-T^2=\frac14-T^2.
$$

把这个同一 $f$ 代入已付紧凑原三均值 $R_{\rm bar},W_4,O_{\rm bar}$，只乘非零有理常数，得到
$$
P_R=256R_{\rm bar},\qquad
P_W=2048W_4,\qquad
P_O=512O_{\rm bar}.
$$
它们的完整多项式为
$$
P_R=10000T^2-1800Tz+52z^2+6250T-860z+625,
$$
$$
P_W=-42500T^2+9200Tz-272z^2-41000T+4720z-9875,
$$
$$
P_O=-11250T^2+1750Tz-44z^2-11125T+905z-2750.
$$
这些是原同一点三个均值方程的等价常数倍，故每个原解都使它们为零。所有原 $T,z$ 值都在此处保留；没有除去 $T$、$z$、$D$ 或新的值首项。

为说明实际新输入的完整范围，同一计算还构造了原 N1 的常数倍
$$
P_N=\frac{8192}{5}N_1
=-25500T^2-80Tz+16z^2-25100T-40z-6175.
$$
最终身份不需要该第四项，其乘子准确为零。

## 3. 完整原多项式证书

定义三个一次多项式
$$
L_R=-12556973810-19436127100T+1592724104z,
$$
$$
L_W=-3723252785-2989618775T+304579367z,
$$
$$
L_O=9707766245-5982442050T-543964z.
$$
完整有理多项式环 $\mathbb Q[T,z]$ 中有
$$
\boxed{\;
L_RP_R+L_WP_W+L_OP_O
=8890621787500\left(\frac14-T^2\right).
\;}
$$
这不是仅在某些候选点上的检验。新源使用 BigInt 有理数运算，逐项构造原三均值，再完整乘回上述全部多项式系数。右侧非零常数无需任何新的原单位假设。

原解使左侧三项都为零，因而 $D=0$，与当前原图的 $D\ne0$ 矛盾。结合上一条真实 QQ gcd 所付的 $\lambda=1/2$，整个 $v=-1/4$ 权纤维得到排除。

此前已实际核验 $R_{543}$ 恰含一次 $v+1/4$；本定理现在支付剥除该因子的原纤维理由。剥除后与其他完整原投影的下一次 Bézout 返回另用新输入，不能把尚未执行的余 gcd 写成本稿结论。特别地，本稿本身没有排空剩余的主图或整 $\Phi=0$ 面。

## 4. 实际执行与可重建原来源

新自含源：

[2026-11-27-unit211-Phi-zero-main-minus-quarter-lambda-half-complete-original-identity-8542.js](../notes/2026-11-27-unit211-Phi-zero-main-minus-quarter-lambda-half-complete-original-identity-8542.js)

Git blob：b2ebdf7798b74ad64b8add54cca55628db74a1e8。  
SHA256：b99785d69378591ab962143981dde1c99cba256055fbfd3499c82688aecf879b。  
源文件 8136 字节。

本源已在新的 V8 函数环境中实际执行，使用 BigInt 的分子、分母和 gcd，全部有理运算精确。实际数学返回 75 毫秒，无异常。它不是尚待运行的 Actions 源，也没有假报 Actions run/job。

实际构造四个完整原二次式乘所有次数不超过四的 $T,z$ 单项式，得到总次数六的 $60\times28$ QQ Macaulay 矩阵，秩为 27。每个保留的消元行均保原行组合并逐坐标乘回。常数一不在本次原行空间内；物理 $D$ 本身在原行空间内，最终又直接按完整多项式作一次乘回，得到第三节可独立检查的证书。没有把矩阵秩单独当作排空依据。

[完整小执行回执](../notes/2026-11-27-unit211-Phi-zero-main-minus-quarter-lambda-half-original-D-execution-8542.json) 保存四个原多项式、非零常数尺度、矩阵大小和实际秩、完整最终乘子及时间。本次没有重算旧结果式、旧六行 cofactor 或旧一般参数的长 Euclid 门。
