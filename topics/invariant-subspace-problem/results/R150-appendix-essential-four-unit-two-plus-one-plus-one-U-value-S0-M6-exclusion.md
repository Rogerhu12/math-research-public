# R150 附录：unit 2+1+1 的 S=0、I=H=0 六次参数纤维完整排除

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-347c-20261126 / unit31_general。日期：2026-11-26。

状态：本附录的全部六次参数纤维已经完整排除，包括全部值分配与 q 根。证明使用原九式、原最高一阶 germ 的全局单位系数，以及一个真实 QQ 结果式单位身份；不宣称 S=0 一般层或整个非零均值层已关闭。

## 1. 范围及已付有限覆盖

沿用[原 U 值图](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md)与[已经登记的 S 线性退化有限覆盖引理](R150-appendix-essential-four-unit-two-plus-one-plus-one-U-value-S0-finite-parameter-cover.md)。保留

$$
p=1,\qquad
\lambda q(q-1)(q+1)bcP_0\ne0,\qquad
V=(1,w,h,k),
$$

并处于

$$
S=h+k+1-2\lambda=0,\qquad A_f=0,
$$

以及三值互异图 $(h-1)(k-1)(h-k)\ne0$。记

$$
x=h-1,\quad y=k-1,\quad s=x+y=2\lambda-3,\quad z=xy,
$$

$$
A=2\lambda^2-2\lambda+1,\quad C=-4\lambda^2+5\lambda-2,\quad R=3-4\lambda.
$$

前一有限覆盖引理已完整支付 $\mathcal I=\mathcal H=0$ 的所有非六次因子，并将剩余参数压到

$$
M_6(\lambda)=1280\lambda^6-1344\lambda^5-8496\lambda^4
+21020\lambda^3-17150\lambda^2+5810\lambda-693=0.
$$

其中 $M_6$ 在 QQ 上不可约；原 $I_2,H_3$ 关于 z 的 gcd 在此数域中为一次，唯一的 z 非零，$s^2-4z\ne0$，两权重亦非零。没有在本附录中重做已登记的结式覆盖或碰撞排除。

## 2. 保留全部参数点的 24 维 QQ 代数

先取

$$
K_6=\mathbb Q[\lambda]/(M_6).
$$

源码仍按前一引理的完整原 $I_2,H_3$ 定义在 $K_6[z]$ 中作 Euclidean 运算，实际检查 gcd 为一次并取其唯一 z 值。过程中每个除数都通过乘法矩阵求真实有理逆并回乘为 1。随后定义

$$
l=\frac{sC-Az}{z^2},\qquad T=\frac Cz,\qquad
w=\lambda-1-T.
$$

建立第一重二次商代数

$$
B_{12}=K_6[x]/(x^2-sx+z),\qquad y=s-x.
$$

这是一个 12 维 QQ 代数；不需要该二次式在 $K_6$ 上不可约，也不选择某个平方根。它同时保留两个值分配。由 $(2x-s)^2=s^2-4z$，

$$
b=\frac{T-ly}{x-y},\qquad c=l-b
$$

在 $B_{12}$ 中全局定义。

原 $A_f=0$ 的未除式是

$$
a_2q^2+a_1q+a_0=0,
$$

其中

$$
a_2=-zc(1-2c),\quad
a_1=R-z(2l-4bc),\quad
a_0=-zb(1-2b).
$$

这里不能先假定二次首项非零。源码先在整个 $B_{12}$ 中实际构造 $a_2^{-1}$，并逐项核对

$$
a_2a_2^{-1}=1.
$$

这证明所有六个 lambda 共轭与两个 x 分配上 $a_2$ 都非零，所以没有遗漏一次降次 q 纤维。再定义

$$
\mathcal B_{24}
=B_{12}[q]/\left(q^2+a_2^{-1}a_1q+a_2^{-1}a_0\right).
$$

该代数有 24 维 QQ 基

$$
\{\lambda^i x^j q^k:0\le i<6,\ 0\le j<2,\ 0\le k<2\}.
$$

第二个二次式同样不需要不可约；其两个 q 根均保留。即使商代数分解为多个因子，或某个二次式出现重根，下面的代数身份仍同时适用于每一个复点。每个原参数候选都给出从 $\mathcal B_{24}$ 到 $\mathbb C$ 的求值同态，未被任取的数域嵌入代替。

## 3. 原单位与矩恒等式

源码在相关整个商代数中逐项求逆并回乘，支付 z、值判别式、b、c、q 二次首项及

$$
q,\ q-1,\ q+1,\ u=b+cq,\ P_0,\ h-1,\ k-1,\ h-k.
$$

这类单位身份是对整个代数的证明，不是只在某个数值根上检查非零。塔中所用逆的计算规则完全明确：若 $\xi^2=c_1\xi+c_0$，则

$$
(a+b\xi)^{-1}
=
\frac{a+bc_1-b\xi}{a^2+abc_1-b^2c_0},
$$

但分母只有在下层代数内实际求得真逆且乘回为 1 后才使用。最底层的逆由真实 $6\times6$ QQ 乘法矩阵求得，全部计算只用有理数。

参数阶段实际完成了 39 次成功逆检查（包含塔内范数的下层逆检查），并核对

$$
a+w+bh+ck=\lambda,
$$

$$
a+2w+bh^2+ck^2=2\lambda^2,\qquad
a+3w+bh^3+ck^3=4\lambda^3.
$$

原 $S=0,A_f=0$ 也在整个商代数中精确成立。

## 4. 同一原 Frobenius 图上的完整九式

仍用原代数

$$
\tau(v)=av_0+v_1+bv_B+cv_C,\qquad a=1-b-c,
$$

以及原活动 Gram 矩阵

$$
K=\begin{pmatrix}
0&0&1&q\\
0&A_1&r&s\\
1&r&0&t\\
q&s&t&0
\end{pmatrix}.
$$

令 $V_2=b+cq^2$。原 $E_0=0,N_0=\lambda P_0$ 全局图为

$$
W_1=V_2/2-u^2+2fu,
$$

$$
W_2=uV_2-2u^3+f(V_2+2u^2)-bcqt+2\lambda P_0,
$$

$$
X=\frac{qW_1-W_2}{b(q-1)},\qquad
Y=\frac{W_2-W_1}{cq(q-1)},
$$

$$
r=X-a-ct,\quad s=Y-aq-bt,\quad
A_1=2f-2bX-2cY+2bct.
$$

两个新显示的分母 $b(q-1),cq(q-1)$ 均在整个 $\mathcal B_{24}$ 中求得真逆并回乘。随后完全按原运算重建 $d,D_K,P,N$ 及双点 germ。实际逐项核为

$$
f=\tau(d)/2,\quad E_0=0,\quad P(k_0)=P_0,\quad
N(k_0)=\lambda P_0,\quad P(V)=N(V)=0.
$$

完整九式在 $\mathcal B_{24}[f,t]$ 中生成：

$$
E_1,\ E_B,\ E_C,\quad
P_1-3wP_0,\ P_B-h^3P_0,\ P_C-k^3P_0,
$$

$$
N_1-2\lambda wP_0,\ N_B-\lambda h^2P_0,\ N_C-\lambda k^2P_0.
$$

为了避免有理常数分母，源码分别对最高式乘 2、第二梯度式乘 4；这不改变零集。其真实总次数依次为

$$
2,2,2,1,3,3,2,3,3.
$$

其中最高一阶式的一次性来自真正的原双点导数，而非把第二行当作简单点。完整原九式生成结束时，已经完成 45 次真逆检查。

## 5. 原 P1 的全局单位系数与两条原 mean

写已生成的原最高一阶式为

$$
L_f f+L_t t+L_0=0
\quad\text{在 }\mathcal B_{24}[f,t]\text{ 中}.
$$

源码允许尝试可逆线性换元 $t=cf+T$，但实际第一次 $c=0$ 即成功：$L_f$ 本身在整个 $\mathcal B_{24}$ 中是单位，并且真实检查

$$
L_fL_f^{-1}=1.
$$

所以所有 24 个参数纤维同时满足

$$
f=-L_f^{-1}(L_t t+L_0).
$$

没有按某个纤维的非零数值选根，也没有遗留 $L_f=0$ 的例外：单位身份已在整个代数中支付。此次计算无失败的全局逆试探，最终真逆检查总数为 48。

代回原九式后，原最高一阶式恒为零，其他式对 t 的次数依次保持

$$
2,2,2,-1,3,3,2,3,3.
$$

只需其中两条真正的原 mean，记代回后的 $E_1,E_B$ 为 $F(t),G(t)$，二者均为二次式。完整 Sylvester 结果式

$$
\mathcal R=\operatorname{Res}_t(F,G)\in\mathcal B_{24}
$$

由无除法行列式直接计算。这里不需要、也没有除以 F、G 的 t 二次首项；若它们在某个复参数点降次，原共同有限 t 根仍使这个完整 Sylvester 行列式为零。因此没有把均值最高系数的零纤维丢掉。

## 6. 真实 QQ 单位身份及矛盾

在上述 24 维 QQ 基中，计算乘法算子

$$
M_{\mathcal R}:\mathcal B_{24}\longrightarrow\mathcal B_{24},
\qquad v\longmapsto \mathcal Rv.
$$

实际有理矩阵为 $24\times24$，精确秩为 24。源码求出有理向量代表的 $g\in\mathcal B_{24}$，随后在原商代数乘法中重新核验

$$
g\mathcal R=1. \tag{1}
$$

这是真正的多项式商代数单位身份，非模素数满秩探测。乘子向量的 SHA256 为

abc9b92937b4388afd1388e57064d20e93e571ffbef6ab105efc419e1e41f7eb。

若存在本层原解，其参数求值同态将 $F(t)=G(t)=0$ 送到 $\mathcal R=0$；但 (1) 同时被送到 $g\mathcal R=1$，矛盾。因此整个六次参数族排除。结合已登记的有限覆盖引理，三值互异 $S=0,A_f=0,\mathcal I=\mathcal H=0$ 的整个退化例外亦关闭。

完整原九式在同一个输入中保留并验证；矛盾最终由原 P1 加两条原 mean 给出。这里不需要宣称抽象必要条件充分，且没有修改固定的原 Frobenius 或物理几何。

## 7. 实际执行身份与旧超时的区别

[成功源](../notes/2026-11-26-unit211-U-value-S0-M6-native-algebra-347c.py)与[实际小回执](../notes/2026-11-26-unit211-U-value-S0-M6-native-execution-347c.json)均保留；可重新生成的商代数矩阵和乘子数组不入库。

冻结 blob：1df7d6359b8d52a60f0c41276e86a626d6eddd8b。源码 SHA256：f81d5d2f276c68c020985fdcbbf34f4172ea878dbc4f9d83e44bda0c917082b5；13376 bytes。依赖 Python 3.12.14、python-flint 0.9.0。

公开 Actions run 45808427743 / job 139869664343。冻结源提交 116a91ca3c94f7c9836ee322839910c20948e4c1。实际源内计时 2.914484 秒、源内峰值 RSS 37628 KiB；驱动计时 2.970073224 秒、驱动记录峰值 RSS 38296 KiB，退出码 0。

原九式输入 SHA256：

ea5947aff096a17e3cb544441fb188030194e6f28b23dc72e187368ce76da0d7。

stdout SHA256：

6c72df0deedc0a135821a864f0249a3c670112857d7f5c94104d07a371b724b6。

最终状态 exact_original_finite_fiber_excluded；实际只使用结果式对 E1/EB 即得到单位身份。最终输出明确 claimLambdaLayerEmpty=false、ordinaryISPClaim=false。

旧 SymPy/RootOf 版本 run 45802044010 / job 139847488577 在 630.777373 秒输出有限参数 ideal 的次数 [2,2] 与零维性；随后在 900.000124 秒源内闹钟停止，退出码 124，完整原九式尚未输出。它不是本排除的依据。新成功源直接构造整个 QQ 商代数，未重复旧的 630 秒参数饱和，也未把旧超时阶段伪记为已完成计算。
