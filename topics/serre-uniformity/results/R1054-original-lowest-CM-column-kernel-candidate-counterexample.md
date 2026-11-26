# R1054：原 CM 最低列恒落 Q 核候选的 p=47 反例

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126；
root / o2_high_coefficient，原实际源使用 R1052。

**一个新的全称候选已经被实际有限反例排除。**
原 R1052 的最低 CM 列，在 $p=47$ 的 new 投影不属于
$\ker\overline{\mathsf Q}$。
因此不能将该列对所有 $p$ 都认作纯正 $\delta$ 的 Hodge 核方向。

这不证明实际行 $c=D\overline{\mathsf Q}(1-\overline{\mathsf Q})\lambda$
的最低值非零；也不排除某个仅限 $p>C_*$ 的不同渐近命题。
下文严格区分测试行、核向量和实际 MW 消去行。

## 1. 原最低列的实际代表

R1052 已在同一原模型上证明
$$
\mathcal C_{\rm CM}(T_c)=2B(c,L_{\rm CM}),\qquad
L_{\rm CM}=\operatorname{PP}_{b=1}(Z_b'/Z^\ell),
\tag{1054.1}
$$
其中最低 $w$ 列只再乘一个确定的非零原单位。
置
$$
p=47,\quad N=7,\quad \ell=16,\quad
r=1-b^3,\quad
j(r)={}_2F_1(1/2,1/2;2/3;r).
$$
R1052 的同源公式是
$$
\mathcal C_{\rm CM}(T)=
-\frac{3^{15}}{A(1)}
[r^{15}]
 \frac{T((1-r)^{1/3})}{(1-r)^{5/3}j(r)^3}.
\tag{1054.2}
$$
$A(1)$ 是已证明的单位，$j$ 只读到 15；
首个分母共振是 16，故这里没有零除。

取测试多项式 $T_*(b)=b^2$。
R1045 的 coefficient-fixed 插值是同一个实际向量空间的同构，
所以存在唯一的原测试行 $c_*$ 满足 $T_{c_*}=b^2$。
它属于负 $\delta$ 部分，并未被假设为 MW 消去行。
由 (1054.2)，
$$
\mathcal C_{\rm CM}(b^2)
=-\frac{3^{15}}{A(1)}[r^{15}]K(r),\qquad
K(r)=(1-r)^{-1}j(r)^{-3}.
\tag{1054.3}
$$

R1037 的实际 $\overline{\mathsf Q}$ 核在 $p=47$ 是一维纯正
$\delta$ 线。$D$ 对 $B$ 自伴，两个 new 特征空间的 $D$ 特征值
分别为 $+1,-1$，所以它们关于 $B$ 正交。
又 $D^2=e_{\rm new}$ 自伴，故对负行 $c_*$
$$
B(c_*,L_{\rm CM})=B(c_*,e_{\rm new}L_{\rm CM}).
$$
如果 $e_{\rm new}L_{\rm CM}$ 属于上述核，
就必须 $\mathcal C_{\rm CM}(b^2)=0$。
因此 (1054.3) 的一个非零值足以排除该候选。

更一般地，取 $T=b^{3t+2}$、$0\le t\le6$，所有这些负行读数
同时为零，当且仅当 $K_9,\ldots,K_{15}$ 同时为零：
它们是
$[r^{15}](1-r)^tK$，相应三角矩阵的对角元为 $(-1)^t$。
本反例只需要其中的 $t=0$ 一项。

## 2. 新输入的公开精确计算

这是此前没有执行过的原 CM inverse-period 输入；
它不重算 $p=47$ 的旧 $f_N,g_N$ 或固定盘窗口。

在公开
[run 45874715945](https://github.com/Rogerhu12/math-research-public/actions/runs/45874715945)，
job **140098765505**，源提交
[7e47699cd195f7fd70eca38a2f9f1011a636a090](https://github.com/Rogerhu12/math-research-public/commit/7e47699cd195f7fd70eca38a2f9f1011a636a090)
中，单独的 CM_KERNEL_DIAGNOSTIC 回执给
$$
\boxed{\qquad [r^{15}]K(r)=23\pmod{47}.\qquad}
\tag{1054.4}
$$
两种构造一致，且完整 $j^3K=1/(1-r)$ 恒等式已核到 15。

producer 只用如下安全递推：
$$
j_0=1,\qquad
j_n=j_{n-1}\frac{3(2n-1)^2}{4n(3n-1)}
\quad(1\le n\le15).
\tag{1054.5}
$$
第一种构造逐项反演 $j$，立方后乘 $1/(1-r)$。
第二种先形成 $j^3$，逐项解 $j^3K=1/(1-r)$；
最后又完整核每个所需次数的乘积系数等于一。
因此 (1054.4) 对应确切的同一有限级数，
不是不同截断或规范之间未经识别的数值。

完整 $j$ 和七项块只出现在公开 runner stdout；
此处只保存足以证明反例的单个值 23，不提交可重算数组。
源码为该源提交中的
[original_scalar_obstruction_new_window.py](../scripts/original_scalar_obstruction_new_window.py)，
SHA-256：
a99fe1212176daa4b0a9da5a7874ceb7ee1234bade567523e764d043ee5de312。
请求 SHA-256：
a1e4af4b4808d47588b3f748b5ab61a9b4cb51cc786c27ac090bf7df6b1c7abd。
方法 SHA-256：
d2d0644bcad18b2285a290ae506c4d6e6790f46ca2de22c15d0c04dc3307ed4c。

回执运行时将几何桥标为 conditional，避免提前宣称实际来源。
现在该桥已经由
[R1052](R1052-original-complete-CM-profile-and-actual-lowest-functional.md)
独立证明，故可以把这条纯代数回执用于 (1054.3)；
没有修改回执或声称运行时已使用当时尚未提交的证明。

## 3. 实际反例和准确剩余问题

由 $23\ne0$、$A(1)\ne0$ 和 $3\ne0$，
$$
\mathcal C_{\rm CM}(b^2)\ne0.
$$
§1 的原配对和真实核方向于是给
$$
\boxed{\quad
e_{\rm new}L_{\rm CM}\notin\ker\overline{\mathsf Q}
\qquad(p=47).
\quad}
\tag{1054.6}
$$
这也适用于 R1052 的原最低列本身，因为两者只差已付的单位。
所以“原最低列对所有 $p$ 都落在 $\overline{\mathsf Q}$ 核中”
不能作为后续捷径。

实际所需的标量仍是
$$
\mathcal C_{\rm CM}
(T_{D\overline{\mathsf Q}(1-\overline{\mathsf Q})\lambda})
=2B((1-\overline{\mathsf Q})\lambda,
               \overline{\mathsf Q}D L_{\rm CM}),
$$
其中原 $\lambda=-6(b+1)/(1-b^3)$，完整
$\overline{\mathsf Q}^{\,2}$ 保留。
一个负测试行的值非零，不迫这个指定实际行的值非零。
$p=47$ 也不被擅自说成超过 R1026 的巨大统一阈值 $C_*$。

本次诊断在同一公开 job 的 1200 秒总预算内执行；
完整 job 最终 895.294074836 秒，within_budget=true。
无本地数学执行。该候选到此停止；继续真实指定值、
完整多行深盘排除与 O0 全局覆盖。
Serre 主目标仍 OPEN。
