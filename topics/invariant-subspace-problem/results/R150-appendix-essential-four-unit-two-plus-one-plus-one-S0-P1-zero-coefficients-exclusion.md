# R150 附录：S=0 三值互异图中原 P1 两变量系数同时零的完整排除

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-347c-20261126 / unit31_general。日期：2026-11-26。

状态：本附录完整排除三值互异 $S=0$ 图内原 P1 的 f、t 两个系数同时为零的全部原解。先给出无遗漏的四次参数覆盖，再在保留所有值分配的 8 维 QQ 商代数中取得真正的原 mean 结果式单位身份。未假设 $A_f=0$；事实上最后的有限纤维上 $A_f$ 与 L 都是单位。本结论不宣称整个 S 层为空。

## 1. 原 P1 及已付范围

沿用[已经登记的原 P1 显式一次式](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-P1-S0-linear-cover.md)与原 $E_0=0,N_0=\lambda P_0$ 全局图。共同尺度取 $p+q=2$，保留

$$
bc\,pq(p-q)uP_0\lambda(u-1)\ne0.
$$

这里 [$u=1$ 的整个原分支已另行完整排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-nonzero-isolated-mean-unit-base-complete-exclusion.md)；使用 $u-1$ 为单位有该独立来源。记

$$
l=b+c,\quad u=bp+cq,\quad Q=pq,\quad
V_2=2u-lQ,\quad T_0=V_2-2u^2.
$$

原最高一阶 germ 方程 $P_1=3wP_0$ 等价于

$$
L_f f+L_t t+L_0=0,
$$

其中

$$
L_f=T_0\left(l-1+\frac{2u(1-u)}Q\right),\qquad
L_t=bc(T_0+4u-4+Q),
$$

$$
L_0=\frac{(1-u)T_0^2}Q
+2P_0\left(l+T-\frac{\lambda T_0}Q\right),
\qquad T=b(h-1)+c(k-1).
$$

这些系数是同一原双点 germ 的系数，不是另一个 Gram 必要系统的替代品。

## 2. 两个系数为零强制 T0=0

假设 $L_f=L_t=0$。由 $bc\ne0$，原 t 系数给出

$$
(1-l)Q=2(u-1)(u-2). \tag{1}
$$

在 (1) 上，不作新除法即可得到

$$
L_f=-\frac{4(u-1)^2T_0}{Q},
\qquad
2P_0=2lQ(u-1). \tag{2}
$$

因 $Q(u-1)\ne0$，$L_f=0$ 强制 $T_0=0$。于是

$$
Q=4(1-u),\qquad u=2l.
$$

原 P1 的常数项仍须为零；由 $P_0\ne0$ 得

$$
T=-l. \tag{3}
$$

这里没有先除 $L_f$，也没有在两个变量系数同时为零时遗失常数项。又因 $u=2l\ne0$，$l\ne0$。

## 3. S=0 的矩关系给出完整四次参数覆盖

令

$$
x=h-1,\quad y=k-1,\quad s=x+y=2\lambda-3,\quad z=xy,
$$

并处于三值互异图 $z(x-y)\ne0$。设

$$
A=2\lambda^2-2\lambda+1,\quad
C=-4\lambda^2+5\lambda-2,\quad D=A-C=6\lambda^2-7\lambda+3.
$$

原三个矩给出

$$
T=C/z,\qquad l=(sC-Az)/z^2.
$$

结合 (3)，得到

$$
C=-lz\ne0,\qquad Dz=sC. \tag{4}
$$

D 与 sC 的 QQ gcd 为 1；所以 (4) 与 $z\ne0$ 迫使 $D\ne0$。s 若为零，则 $\lambda=3/2$、$D=6$，也与 (4) 矛盾。因此

$$
z=\frac{sC}{D},\qquad l=-\frac Ds. \tag{5}
$$

为保留实际值分配，记 $\delta=x-y$，则 $\delta^2=s^2-4z$。由 $p+q=2$，可以写

$$
p=1+\theta\delta,\qquad q=1-\theta\delta,
$$

并且

$$
b-c=\frac{2T-ls}{\delta},\qquad
u=l+\theta(2T-ls).
$$

令 $j=s+2=2\lambda-1$。由 $T=-l,u=2l,l\ne0$，

$$
2T-ls=-lj,\qquad \theta=-1/j.
$$

$j=0$ 不能在此步骤静默除去；直接在 $\lambda=1/2$ 代入 (5) 得 $s=-2,z=1$，使 $\delta^2=0$，与三值互异矛盾。故 j 非零。

原 Q 与值判别式现在满足

$$
Q=4(1-2l),\qquad
\delta^2=(8l-3)j^2.
$$

把 (5) 代入后一式，清除已付 $sD$，精确得到

$$
(-8D-3s)Dj^2-s^3D+4s^2C
=-4j^2M_4(\lambda)=0,
$$

其中

$$
M_4(\lambda)
=72\lambda^4-156\lambda^3+136\lambda^2-54\lambda+9. \tag{6}
$$

已支付 $j=0$，故所有剩余参数都落在 $M_4=0$。这是从原矩及完整 P1 推导的必要覆盖；没有把这个覆盖称为原方程的充分描述。

## 4. 保留全部根的 8 维 QQ 代数

取

$$
K_4=\mathbb Q[\lambda]/(M_4),\qquad
\Delta=s^2-4z,
$$

其中 l,z 由 (5) 定义。建立

$$
\mathcal B_8=K_4[\delta]/(\delta^2-\Delta).
$$

该代数有 QQ 基

$$
1,\lambda,\lambda^2,\lambda^3,\quad
\delta,\lambda\delta,\lambda^2\delta,\lambda^3\delta.
$$

不需要假定 $M_4$ 或第二个二次式不可约，也不选择数值嵌入。所有四次 lambda 根与两种值分配均由这个商代数同时保留。每个原参数候选给出 $\mathcal B_8$ 到 $\mathbb C$ 的求值同态。

在整个代数中定义

$$
p=1-\frac{\delta}{j},\quad q=1+\frac{\delta}{j},
$$

$$
b=\frac l2-\frac{lj\delta}{2\Delta},\quad c=l-b,\quad a=1-l,
$$

$$
h=1+\frac{s+\delta}{2},\quad
k=1+\frac{s-\delta}{2},\quad
w=\lambda-1+l.
$$

源码从 QQ 乘法矩阵构造每个所用单位的真实逆，并在原商代数乘回为 1，包括

$$
D,\ s,\ \Delta,\ j,\ \lambda,\ z,\ b,\ c,\ p,\ q,\ q-p,
$$

$$
u,\ u-1,\ P_0,\ h-1,\ k-1,\ h-k.
$$

全部参数阶段完成 41 次逆及下层范数逆检查，没有失败的全局逆试探。这些身份适用于整个代数，而非某个抽样根。

同时精确核对

$$
u=2l,\quad Q=4(1-2l),\quad V_2=2u^2,\quad
P_0=Ql(2l-1),
$$

以及原三个矩与 $S=0$。

## 5. 原 N(V) 全局确定 f，且本例外避开 L=0

原 $N(V)$ 的 f 系数满足

$$
A_f=3-4\lambda-z\left(l+\frac{2u(1-u)}Q\right)
=-(4\lambda-1)(2\lambda-1).
$$

(6) 与 $(4\lambda-1)(2\lambda-1)$ 的 gcd 为 1；源码还在整个 $\mathcal B_8$ 中构造并回乘 $A_f^{-1}$。

令

$$
W_\times=bp(k-1)+cq(h-1).
$$

在这份完整参数代数内，

$$
W_\times=2l(2lj-1).
$$

由于 $T_0=0$，原 $N(V)=0$ 等价于

$$
A_f f=wW_\times-\frac{z\lambda(2P_0)}Q.
$$

因此 f 在整个 $\mathcal B_8$ 中被全局唯一确定，没有新分母零面。

另有

$$
L=q(h-1)-p(k-1)=\frac{4\delta(\lambda-1)}j.
$$

$M_4$ 与 $\lambda-1$ 的 gcd 为 1，而且源码实际回乘 L 的逆。所以该有限例外自动处于 $L\ne0,A_f\ne0$，未与另行研究的 L=0 一般图混淆。

## 6. 原九式及一个真实结果式单位身份

使用上述 f 与完整参数代数，在同一原 Frobenius 数据上重建

$$
W_1=V_2/2-u^2+2fu,\qquad
W_2=uV_2-2u^3+f(V_2+2u^2)-bcpqt+2\lambda P_0,
$$

$$
X=\frac{qW_1-W_2}{bp(q-p)},\qquad
Y=\frac{W_2-pW_1}{cq(q-p)},
$$

$$
r=X-ap-ct,\quad s_1=Y-aq-bt,\quad
A_1=2f-2bX-2cY+2bct.
$$

两个显示的 Cramer 分母均求真实逆并乘回。随后按原定义生成

$$
E_1,E_B,E_C,\quad
P_1-3wP_0,\quad P_B-h^3P_0,\quad P_C-k^3P_0,
$$

$$
N_1-2\lambda wP_0,\quad
N_B-\lambda h^2P_0,\quad N_C-\lambda k^2P_0.
$$

源码逐项检查同一 $E_0,N_0,f$ 恒等式与 $P(V)=N(V)=0$。对 t 的真实次数依次为

$$
2,2,2,-1,3,3,2,3,3.
$$

第四个次数 -1 表示原 P1 在全部 8 维参数代数中确实恒为零；它不是被除去，也不是由于忘记了原常数项。全部原九式生成后，共计 45 次真实单位检查。

取两条原 mean 在 $\mathcal B_8[t]$ 中的完整 Sylvester 结果式

$$
\mathcal R=\operatorname{Res}_t(E_1,E_B).
$$

没有除以这两条二次式的最高系数；任意原共同有限 t 根，包括发生降次的参数纤维，仍必使完整结果式为零。

源码在上述 QQ 基中建立 $\mathcal R$ 的 $8\times8$ 乘法矩阵，实际 QQ 秩为 8，求得 $g\in\mathcal B_8$ 并回到原代数乘法核验

$$
g\mathcal R=1. \tag{7}
$$

乘子向量 SHA256：

9d90b34a44e8fed5651f57c13eaad8235bed5aa66180a852d551ee1d70ea2e35。

任何本层原解的求值同态会令 $\mathcal R=0$，而 (7) 同时给出 1=0，矛盾。因而 (6) 覆盖的全部有限纤维排除；结合第 2、3 节，三值互异 S=0 图内原 P1 两变量系数同时零的整个分支关闭。

所以在剩余三值互异 S=0 原解上，$(L_f,L_t)\ne(0,0)$。可按 $L_f\ne0$ 解 f，或在 $L_f=0$ 时由 $L_t\ne0$ 解 t；这个覆盖不再限于 $A_f=0$。其他原最高式、第二梯度式和同一物理几何继续保留，本附录不声称剩余图已排空。

## 7. 实际执行身份

[自含源](../notes/2026-11-26-unit211-S0-P1-zero-eight-algebra-347c.py)及[实际小回执](../notes/2026-11-26-S0-P1-zero-eight-execution-347c.json)已保留。

冻结 blob：336ca629d862cd4ee18d2e6fd4e5f38af240ac8b；11653 bytes。

源码 SHA256：

c723b14b198bfe1673697c8bb535f85ee00f704ed321834a3c644f9e8cf7aea1。

公开 Actions run 45813236876 / job 139886236638。冻结源提交 e94bd75f9e5a6f6c3369af418b9456c2896728ad；执行前实际 pull 至 9f13b3910c1b795c2dfde6a4bd3447033100d774，根 README 与课题 README 未变。依赖 Python 3.12.14、python-flint 0.9.0。

参数与单位核验 0.006709 秒；完整原九式核验 0.067356 秒；最终真实 QQ 单位身份完成于 0.070704 秒。源内峰值 RSS 34840 KiB；驱动计时 0.148037494 秒、峰值 RSS 35596 KiB，退出码 0。

原九式输入 SHA256：

42c1c8b3855363669be669db8a6558a2e687acc7b37d56c7a56f1e1c214a5b38。

stdout SHA256：

0a6e2fa4838999e38cce47fd626b9f5d89828278621eee754c149e4e723a8268。

实际只用 E1/EB 这一个结果式即得到 (7)。最终状态 exact_original_eight_fibers_excluded；P1IdenticallyZero=true、failedGlobalInverseTrials=0、claimS0LayerEmpty=false、claimLambdaLayerEmpty=false、ordinaryISPClaim=false。
