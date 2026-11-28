# 只读来源审计：原 $S=0,h=k$ 排除不依赖错误 compact mean

日期：2026-11-28。会话：Astra-ISP-8542378f-20261127 / r150_open_geometry。

本记录只保存对三份既存成功源码及其原理想来源的静态阅读结论，没有重新运行旧消元、Bézout、Gröbner 基或原恒等式检查，也不作为一条新的数学排除结论。此前发现的 compact JS 错误是把双点 germ 的 $-2(d^2)_1=-4d_0d_1$ 错写为 $-2d_1^2$；下列三份源均未使用该错误定义。

## 1. 覆盖与三份精确源码

主结论是 [原 S0、相等 singleton 值的完整排除](../results/R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-equal-values-complete-exclusion.md)。原三个矩在 $S=0,h=k$ 上给
$$
(2\lambda-1)(2\lambda^2-1)=0.
$$
所需三份成功源如下。

| 作用 | 原成功源 / blob | SHA256 |
|---|---|---|
| 整个 $2\lambda^2=1$ 二次域及所有原参数纤维 | [2026-11-27-unit211-S0-equal-values-quadratic-field-return-8542.py](2026-11-27-unit211-S0-equal-values-quadratic-field-return-8542.py)，18,562 字节 | b7069f8779f512c3f50a3c889071bbd6712bf3227fdb9476dffc73ac100f494f |
| 该碰撞图上 $A_f=0$ 的完整先行排除 | [2026-11-26-unit211-U-value-S0-collision-347c.py](2026-11-26-unit211-U-value-S0-collision-347c.py)，blob 849653c3b99fa90d0f84f4d251cf2f917ac18b9b，4,629 字节 | 9e843f0cad6ae672258021d650ff68e72e914405fc1848ca41de5f6d1f3d5bab |
| 整个 $\lambda=1/2$ 原恒等式与原第五列秩矛盾 | 自含 JavaScript blob 0f6fbabe15135c7408a8649fad551eab9b80039a，5,345 字节 | f0d97e71d86fafa8a41822c84d7dd89bb5aa28cb2471d5a5165734d68aaea735 |

本次仅对实际取读字节核定这些 SHA，没有执行它们。后两项分别由 [S0 的 $A_f=0$ 值碰撞排除](../results/R150-appendix-essential-four-unit-two-plus-one-plus-one-U-value-S0-collision-exclusion.md) 和 [S0、$h=k,\lambda=1/2$ 排除](../results/R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-equal-values-lambda-half-exclusion.md) 保存原论证与旧执行身份。

主源用同一个原 Frobenius 代数
$$
v z=(v_0z_0,\ v_0z_1+v_1z_0,\ v_Bz_B,\ v_Cz_C).
$$
源码先算 $d^2=vm(d,d)$，原 $E_1$ 使用 $-2(d^2)_1$；其 $N_1,P_1$ 也是原双点极化/jet。主源没有 import compact mean，也没有依赖其错误 $R_2$。主源在整个二次数域内保两 $\lambda$ 共轭，再返回同一 $q$ 的原十一条件；从未把不同共轭的条件拼在一起。

$A_f=0$ 的所需先行依据可以限于上述 **碰撞交面** 定理：它从原 $N(V)$ 和矩得到 $b=c$、完整 $q$ 二次式，再在整个 $\mathbb Q(\sqrt2,\sqrt3)$ 上返回原九式单位。其 source 的 mean 使用真正 $mul(d,d)$，不依赖 compact $R_2$。所以为本次 $h=k$ 适用性不必额外借用一般三值互异 $A_f=0,L\ne0$ 图的后续消元。

$\lambda=1/2$ JavaScript 同样先用真实 dual 乘法计算 $d^2$，$-2(d^2)_1$ 没有替换为第二坐标平方。其非零 $t$ 原短证和 $t=0$ 原第五列论证必须保留各自性质：后者是原五列 Gram 秩二与同一物理六维空间中的秩至少四相矛盾，不能改记为已算出的抽象单位理想。

## 2. 当前 $p+q=2$ 图到旧 $p=1$ 图

当前规范为
$$
p=1+\rho,\quad q=1-\rho,\quad \rho^2=1-Q,
\qquad Q(1-Q)\ne0.
$$
于是 $p,q,\rho$ 都非零。用原共同 Gram 缩放使 $p$ 变为 $1$，旧参数是
$$
q_{\mathrm{old}}=\frac{1-\rho}{1+\rho},\quad
q_{\mathrm{old}}-1=-\frac{2\rho}{1+\rho},\quad
q_{\mathrm{old}}+1=\frac{2}{1+\rho}.
$$
因此旧三单位 $q_{\mathrm{old}}(q_{\mathrm{old}}-1)(q_{\mathrm{old}}+1)$ 全由当前原单位支付，没有在转换中引入一个待排除的零面。$b,c$ 及非零 $P_0,U_0$ 的物理条件同样保留；归一化值 $V=U/U_0$ 和 $\lambda$ 不改变。

在当前 $h=k\ne1$ 的原矩参数化
$$
A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1,\quad
h=k=1+B/A
$$
中，直接有
$$
S=h+k+1-2\lambda
 =\frac{(2\lambda-1)(2\lambda^2-1)}A.
$$
当前已付 $A$ 时，分子零恰落在上面完整三谱覆盖内，所以现有原结论允许在该碰撞图支付 $S$。这不是对错误 compact 来源的修补性重算。

## 3. 适用范围

上述链本身就是相等 singleton 值 $h=k$ 的原图，因而没有借用 distinct-singleton 图的 $D\ne0$。尤其没有从 W 的 $D\ne0$ 饱和、旧错误 compact $R_2$ 或其继承头条件外推一个单位。它只确认已刊 S0 碰撞定理及所需两个先行分支可以用于当前原碰撞图；不恢复任何另经错误 compact 来源产生的结论。
