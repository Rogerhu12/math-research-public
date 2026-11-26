# R150：S=0、h=k 的全部原值碰撞完整排除

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / r150_open_geometry。日期：2026-11-27（Asia/Taipei）。

**状态：已证明。** 在单位 $2+1+1$ 补空间、非零孤立点 mean 的原图中，整个 $S=0,h=k$ 值碰撞不存在物理临界点。本条新证明两个 $2\lambda^2=1$ 谱的排除，与此前完整的 $\lambda=1/2$ 证明合并。这里只关闭这个碰撞；三值互异的 $S=0$、$L=0$ 补图、一般 $LS\ne0$ 及普通 Hilbert ISP 均不因此关闭。

## 1. 原矩的完整三谱覆盖

沿用 [原 U 值图](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md) 的同一 Frobenius 代数

$$
\mathcal A=\mathbb C[\epsilon]/(\epsilon^2)\times\mathbb C\times\mathbb C,
\qquad
\tau(v)=av_0+v_1+bv_B+cv_C,
\qquad a=1-b-c.
$$

共同规范 $p=1$；此前已闭边界允许

$$
bc q(q-1)(q+1)P_0\ne0.
\tag{1}
$$

记 $V=(1,w,h,k)$、$\lambda=\tau(V)$、$\ell=b+c$。$S=h+k+1-2\lambda=0$ 与 $h=k$ 给 $h=k=\lambda-1/2$。原三个 U 矩是

$$
a+w+\ell h=\lambda,\quad
 a+2w+\ell h^2=2\lambda^2,\quad
 a+3w+\ell h^3=4\lambda^3.
\tag{2}
$$

第一、二式消去 $a,w$ 得 $\ell(h-1)^2=2\lambda^2-2\lambda+1$；再以第三式消元，得到

$$
(2\lambda-1)(2\lambda^2-1)=0.
\tag{3}
$$

这是未除 $\lambda$ 的原多项式身份，且 (3) 与 $h-1$ 互素，所以没有 $h=1$ 遗漏。$\lambda=1/2$ 的全层已由 [原 mean 短证与完整第五列 Gram](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-equal-values-lambda-half-exclusion.md) 排除。余下两谱放在**同一个**代数

$$
\mathbb Q[\alpha]/(\alpha^2-2),\qquad
\lambda=\alpha/2,\quad
h=k=\lambda-\tfrac12,\quad
\ell=\frac{8(5+\lambda)}{49},\quad
w=\frac{3\lambda+1}{7}.
\tag{4}
$$

因此两共轭都保留；并未对每一个原式分别任取共轭。

## 2. 从同一原 Gram 重建九式

用原配对矩阵

$$
K=\begin{pmatrix}
0&0&1&q\\
0&A_1&r&s_1\\
1&r&0&t\\
q&s_1&t&0
\end{pmatrix},\qquad d=K1,\qquad \tau(d)=2f.
$$

矩阵作用为 $(Kv)_i=\tau(K_i v)$，乘法是 $\mathcal A$ 的乘法。设

$$
u=b+cq,\quad V_2=b+cq^2,\quad
P_{02}=b+cq^3-3\nu V_2+2\nu^3,\quad T_0=V_2-2\nu^2,
$$

$$
W_1=T_0/2+2\nu f,\quad
W_2=\nu T_0+\lambda P_{02}+(V_2+2\nu^2)f-bcq t.
$$

原 $E_0=0$、$N_0=P_0\lambda$ 等价地给

$$
X=\frac{qW_1-W_2}{b(q-1)},\qquad
Y=\frac{W_2-W_1}{cq(q-1)},
$$

$$
r=X-a-ct,\quad s_1=Y-aq-bt,\quad
A_1=2f-2bX-2cY+2bc t.
\tag{5}
$$

这些分母全是 (1) 已有单位。源码不使用有理函数化的浮点表达，而是取 $D=2bcq(q-1)$，在原多项式环上生成 $\widehat K=DK$，逐式核验 (5)、$E_0=0$、最高基值及 $N_0$。

具体用

$$
\mathsf P(v)=\tau\bigl((v-\tau(v)1)^3\bigr),
$$

$$
\mathsf N(v)=2\tau(dv^2)-2f\tau(v^2)-4\tau(v)\tau(dv)
 +4f\tau(v)^2+\tau(vKv).
\tag{6}
$$

从同一 $K$ 生成三个原 mean $E_1,E_B,E_C$、三个原最高值/jet $P_1,P_B,P_C$、三个原第二梯度值/jet $N_1,N_B,N_C$；并生成原孤立点式 $\mathsf N(V)=0$。所有 $D$ 次数分别按式的齐次次数保留，未对不同方程独立改配对。

在 (4) 中，$\mathsf N(V)=A_f f+C_f$，无 $t$ 项。这里 $L=(q-1)(h-1)\ne0$；[整个 $S=0,A_f=0,L\ne0$ 层](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Af0-L-nonzero-complete-exclusion.md) 已完整排除。因此只在已付的 $A_f\ne0$ 补图置 $f=-C_f/A_f$。若原式的 $f$ 次数为 $m$，以 $A_f^m$ 清分母；随后仅除去 (1) 和 $A_f$ 的实际公共因子。每次除法都回乘到原式，二次范数只用于实现精确多项式除法，从不另加“范数非零”的点假设。

记这些 $t$ 多项式为 $\widetilde E_1,\widetilde E_B,\widetilde E_C,\widetilde P_1,\ldots$。其系数在 $\mathbb Q[\alpha]/(\alpha^2-2)[b,q]$。$\widetilde P_1$ 至多一次；**不除它的首项**。

## 3. 先在同一二次域消元，再取有限参数覆盖

依次定义十一条必要投影 $F_0,\ldots,F_{10}$：

$$
\operatorname{Res}_t(\widetilde P_1,\widetilde E_1),\quad
\operatorname{Res}_t(\widetilde P_1,\widetilde E_B),\quad
\operatorname{Res}_t(\widetilde P_1,\widetilde E_C),\quad
\operatorname{Res}_t(\widetilde P_1,\widetilde N_1),
$$

接着是 $\widetilde P_1$ 与 $\widetilde P_B,\widetilde P_C,\widetilde N_B,\widetilde N_C$ 的四个结果式，最后是三个原 mean 两两的结果式。每个投影只去掉已经支付的公共单位。

在任何原点，十一式同时为零。特别是 $\widetilde P_1$ 的两个系数同时为零时，前八式也不会丢掉该点；后面三个原 mean 结果式继续约束这个例外面。

现在**先保持同一 $\alpha$**，计算

$$
R_j(b,\alpha)=\operatorname{Res}_q(F_0,F_j),\qquad j=1,2,3.
\tag{7}
$$

每条 $R_j$ 在 $b$ 上都是 156 次。实现是二次系数环上的 subresultant PRS；每次伪除法和精确商均回乘验证。其标量最后 subresultant 就是 Sylvester 行列式（至多非零常数符号）。因此原解必为三条 $R_j$ 的零点；这一步未要求任何专门化首项非零。

**只在 (7) 完成之后**取范数，再取三范数的平方自由公共因子。所得 16 次完整必要覆盖（相差非零有理常数）为

$$
b(2b-1)\Phi_1(b)\Phi_2(b)\Phi_3(b)\Phi_8(b),
\tag{8}
$$

其中

$$
\Phi_1=49b^2-40b+8,\quad
\Phi_2=49b^2-80b+32,\quad
\Phi_3=196b^2-124b+17,
$$

以及

$$
\begin{aligned}
\Phi_8={}&621651170018641b^8-2029881371489440b^7\\
 &+2603121970495552b^6-1616747953596928b^5\\
 &+445916973585408b^4+1336424316928b^3\\
 &-30846579507200b^2+6895787573248b-480559235072.
\end{aligned}
\tag{9}
$$

平方自由化和分解的乘积身份均实际验证。这里 (8) 只作有限覆盖，绝不把范数根本身认定为原解。

## 4. 返回全部原 q 纤维

对每个因子，在完整有限 $\mathbb Q$ 代数中保留所有根。除了有理根 $b=1/2$（在完整 $\mathbb Q[\alpha]/(\alpha^2-2)$ 内处理）以外，从原 $R_1=R_{1,0}+\alpha R_{1,1}$ 的同一纤维得到

$$
\alpha=-R_{1,0}R_{1,1}^{-1}.
\tag{10}
$$

逆由扩展 gcd 给出，并实际乘回 1；又核验 $\alpha^2=2$ 及全部三个 $R_j=0$。所以 (10) 恢复**同一个**原 $\lambda$，不会将两种共轭的不同方程混配。三个二次因子上的 (10) 分别为

$$
\Phi_1:\ \alpha=(49b-20)/2,\qquad
\Phi_2:\ \alpha=(49b-40)/4,\qquad
\Phi_3:\ \alpha=(98b-31)/8.
\tag{11}
$$

$\Phi_8$ 上同样用 (10)，无需把较大的七次有理表达式抄入正文；自含源码从 (7) 重新生成它并核验全部身份。这个步骤不依赖一个未经证明的二次塔不可约性：下列每个使用的逆均在完整有限商代数中通过乘回检查。

将十一条原 $F_j$ 逐条专门化到同一个代数，按其原次序做 $q$ 的扩展 gcd。每次除法与 Bézout 身份都在该完整代数中回乘。结果如下。

| 完整 b 因子 | 同一原纤维的结果 | 排除理由 |
|---|---|---|
| $b$ | $b=0$ | 原单位 (1) |
| $2b-1$ | 原 $q$-gcd 次数 $12\to7$，最后只含 $q^7$ | $q\ne0$ |
| $\Phi_1$ | 原 $q$-gcd 次数 $12\to4$；全部因子被 $A_f$ 的两个二次 gcd 去掉 | $A_f=0$ 整层已有完整排除 |
| $\Phi_2$ | (4)、(11) 直接给 $b=\ell$，故 $c=0$ | 原单位 (1) |
| $\Phi_3$ | 原 $q$-gcd 次数 $5\to0$ | Bézout 等于 1 |
| $\Phi_8$ | 前八个投影给二次 $q$-gcd；加第九条原 $\operatorname{Res}_t(\widetilde E_1,\widetilde E_B)$ 后为 1 | 保留并排除 $P_1$ 双零面 |

每个因子都排除，故 $2\lambda^2=1$ 的两个原谱全部排除。与第 1 节的 $\lambda=1/2$ 完整证明合并，即得到整个 $S=0,h=k$ 碰撞为空。

## 5. 自含源码与实际执行

- 源码：[2026-11-27-unit211-S0-equal-values-quadratic-field-return-8542.py](../notes/2026-11-27-unit211-S0-equal-values-quadratic-field-return-8542.py)，18,562 字节。
- SHA-256：`b7069f8779f512c3f50a3c889071bbd6712bf3227fdb9476dffc73ac100f494f`。
- 依赖：Python、python-flint 0.9.0；输入仅为源码中显示的原公式，不读取外部计算数组。
- 参数：`--seconds 120`。本次实际 exit 0，12.271560 秒，峰值 RSS 60,284 KiB。
- 原完整九式输入 SHA-256 为 `1ca70ab4b1840756d7251d43cddd1b0d4607b3ea9e4de35cd3aff611215d1469`，与此前未完成门的原输入一致；本次改变的是消元次序。
- 353 条原多项式精确除法、198 条 PRS 精确商、全部伪余式身份实际回乘；有限返回实际核验 161 个代数逆、112 个多项式除法和 45 条 Bézout 身份。
- 小回执：[2026-11-27-unit211-S0-equal-values-quadratic-field-execution-8542.json](../notes/2026-11-27-unit211-S0-equal-values-quadratic-field-execution-8542.json)，保参数、结果、各结果式哈希、stdout 哈希及实际运行身份，不保存可重算的大数组。

此前 run45831444045/job139948952215 的 1270.862 秒 driver 终止、六个 QQ 结果式和 238 次必要覆盖仍保留其原状态。本次没有把那次超时改记成功，也没有继续重跑其后十八条大 QQ 结果式，而是从同一原九式完成了 (7)–(11) 的新返回。
