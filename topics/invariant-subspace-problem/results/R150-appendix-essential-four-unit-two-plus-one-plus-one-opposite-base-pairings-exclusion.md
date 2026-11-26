# R150 附录：单位 2+1+1 的相反基点配对分支全部为空

作者：Astra-ISP-347c-20261126 / unit31_general；AI-assisted GPT-6 Astra Pro。日期：2026-11-26 UTC。

**状态：本条精确范围已证明。** 在同一原单位 $2+1+1$ 与孤立零点分支中，归一 $p=1,q=-1$ 的整个分支为空。本条支付前稿尚余的一般图；连同已经独立完成的所有边界，得到相反基点配对的完整排除。其他 $q\ne0,\pm1$ 的一般分支及整个 ISP 没有由本条宣称解决。

## 1. 已付边界与本条唯一剩余图

继续保留原长度五除子 $2A+B+C+Z$、同一原六维非退化配对、同一 Frobenius 单位代数、原 mean、最高式和第二梯度的所有值与一阶 jet。参数、原 $P,N,E$、Cramer 图和所有原物理对象均与[一般图六条异常曲线专条](R150-appendix-essential-four-unit-two-plus-one-plus-one-opposite-base-pairings-regular-exceptional-curves-exclusion.md)第一节相同。

这里 $u=b-c$、$\ell=b+c$、$e=u^2$、$v=d_B-d_C-1$、$w=ut$、$T=u(d_B+d_C)/2$。以下边界均已独立完整排除：

- $u=0$：见[相反配对的零基点 mean 专条](R150-appendix-essential-four-unit-two-plus-one-plus-one-opposite-pairings-zero-base-mean-exclusion.md)。
- $\ell=0$ 与 $\ell=1/2$：分别见[零总单点权](R150-appendix-essential-four-unit-two-plus-one-plus-one-opposite-base-pairings-zero-total-weight-exclusion.md)和[半总单点权](R150-appendix-essential-four-unit-two-plus-one-plus-one-opposite-base-pairings-half-total-weight-exclusion.md)的完整排除。
- $D_1D_2=0$：见[两个奇异 mean 图](R150-appendix-essential-four-unit-two-plus-one-plus-one-opposite-base-pairings-singular-mean-charts-exclusion.md)。
- $vw(v+w)BG_-G_+=0$：见[六条异常曲线的完整原式排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-opposite-base-pairings-regular-exceptional-curves-exclusion.md)。

其中
$$
B=v^2+vw-w+1,\quad D_1=-2\ell+v-w+1,\quad D_2=-2\ell(v+1)+B,
$$
$$
G_-=v^3-vw^2-vw+v-w^2-w,\quad
G_+=v^3-vw^2+vw-v-w^2-w.
$$
原 mean 的 Cramer 公式是
$$
e_*=
\frac{\ell(\ell v^3-\ell v^2-\ell vw^2-\ell w^2+w^2)}{D_1D_2},
\qquad
T_*=e_*+\frac{\ell(v-1)(v+w)-w^2}{2D_1}.                       \tag{1.1}
$$
定义
$$
H=-2\ell^2(v+1)+\ell(2v^2+v-2w+1)-w^2.
$$
由原 $bc\ne0$ 和精确身份 $e_*-\ell^2=\ell(2\ell-1)H/(D_1D_2)$，本条唯一剩余图满足
$$
Q_0:=\ell(2\ell-1)D_1D_2\operatorname{num}(e_*)H\ne0,
\qquad Q_1:=vw(v+w)BG_-G_+\ne0.                              \tag{1.2}
$$
这些不等式每一个都有已登记的原方程来源或完整边界证明；没有用它们把未处理纤维划出讨论范围。

## 2. 原 trace 与单点共同范数的无除法必要式

记孤立零点配对列 $U=(u_0,u_1,u_B,u_C)$，$m=\tau(U)$，其中
$$
\tau(U)=a u_0+u_1+b u_B+c u_C,\qquad a=1-\ell.
$$
原最高值、原最高一阶 jet、第二梯度值和 jet 要求
$$
(P_0,P_1,P_B,P_C)=(-u_0^3,-3u_0^2u_1,-u_B^3,-u_C^3),
$$
$$
(N_0,N_1,N_B,N_C)=(-mu_0^2,-2mu_0u_1,-mu_B^2,-mu_C^2).         \tag{2.1}
$$
原零点自身的完整 mean 是 $\tau(U^2)=2m^2$，原最高式是 $P(U)=0$。故
$$
\overline N=aN_0+N_1+bN_B+cN_C=-2m^3,
\quad S=\overline P-2\overline N=0.                           \tag{2.2}
$$
此前保留的 jet 相容式为 $c_0=3P_0N_1-2N_0P_1=0$。

本条还使用原 trace 定义本身的完全无除法后果
$$
\begin{aligned}
\mathcal T={}&3N_0N_BN_C-(3aP_0+P_1)N_BN_C\\
             &-3bP_BN_0N_C-3cP_CN_0N_B=0.                    \tag{2.3}
\end{aligned}
$$
把 (2.1) 代入，右侧精确成为
$$
3m^2u_0^2u_B^2u_C^2
(-m+a u_0+u_1+b u_B+c u_C)=0.
$$
因此 (2.3) 同时覆盖 $m=0$ 和任一配对分量为零的情形，不除以某个 $N_i$。

由 (2.1)、(2.2)，每个单点都必须满足
$$
\Lambda_i=2N_i^3-\overline N P_i^2=0\qquad(i=B,C).
$$
下文保留它们的差
$$
\mathcal L=\Lambda_B-\Lambda_C=0.                             \tag{2.4}
$$
这是原最高式、第二梯度和原零点 mean 的共同范数约束，不是另加的标定。它没有把必要范数相容式当作充分性；整个论证只从原完整临界性出发推出矛盾。

## 3. 从原乘法生成的五个有理数多项式

由 (1.1) 完整恢复原 Gram 后，在有理函数域 $\mathbb Q(\ell,v,w)$ 上使用形式关系 $u^2=e_*$。原单位代数仍为
$$
\mathbb C[\epsilon]/(\epsilon^2)\oplus\mathbb C\oplus\mathbb C,
\qquad \tau(X)=aX_0+X_1+bX_B+cX_C.
$$
原 $P,N$、原 mean 由这一乘法直接生成。配套源码把每个表达式写成 $A+uB$，其中 $A,B\in\mathbb Q(\ell,v,w)$，完全精确进行约分；所需的 $u^{-1}=u/e_*$ 已由 (1.2) 支付。这个形式二次代数保留了 $u$ 的所有平方根，不作数值选根。

原 $M=u^2E_1$、$c_0$、$\mathcal L$ 为偶式，原 $S,\mathcal T$ 为奇式。因此使用
$$
M,\quad S/u,\quad c_0,\quad \mathcal T/u,\quad \mathcal L.
$$
取各化简分子后，仅按前稿的精确 Strip 定义反复除去与 $Q_0$ 的 gcd，再乘非零有理常数作统一首一化。这里首一化的系数是整个多变量 $\mathbb Q$ 多项式的数值系数，不是某个依赖参数的单变量首项系数。记五个所得多项式为 $M_*,S_*,C_*,\Theta_*,L_*$，其中 $\Theta_*$ 是 trace 多项式。

| 原必要式 | 多项式 | 关于 $(\ell,v,w)$ 的次数 |
|---|---|---|
| 剩余 mean $u^2E_1$ | $M_*$ | $(4,6,5)$ |
| 零点 mean 和最高式 $S/u$ | $S_*$ | $(4,7,5)$ |
| 原 jet 相容式 $c_0$ | $C_*$ | $(9,14,10)$ |
| 原 trace $\mathcal T/u$ | $\Theta_*$ | $(19,27,22)$ |
| 原单点范数差 $\mathcal L$ | $L_*$ | $(22,33,25)$ |

每个原解都必须使五个多项式同时为零。原已解的 $E_0,E_B,E_C$ 在源码中亦被逐项验证为零，原 $E_1$ 保留在 $M_*$ 中。未放松 mean 的任一分量。

## 4. 三个完整二轮结式只留下两个未付 $w$ 纤维

先对 $\ell$ 计算四个完整结式，再仅除去与已经完整排除的 $Q_1$ 的 gcd 因子，记为
$$
R_{MS}=\operatorname{Strip}(\operatorname{Res}_{\ell}(M_*,S_*),Q_1),
$$
$$
R_{MC},\ R_{MT},\ R_{ML}
$$
及相应定义。各自的 $(v,w)$ 次数精确为
$$
(15,8),\quad(32,23),\quad(73,53),\quad(96,63).                \tag{4.1}
$$
没有删除 $Q_1$ 以外的因子。由于 (1.2)，每个原解仍使这四个二变量多项式全为零。

接着计算完整 $v$ 结式
$$
A_C(w)=\operatorname{Res}_v(R_{MS},R_{MC}),\quad
A_T(w)=\operatorname{Res}_v(R_{MS},R_{MT}),\quad
A_L(w)=\operatorname{Res}_v(R_{MS},R_{ML}).                     \tag{4.2}
$$
它们的次数分别为 $359,838,1011$。三个特征零有理数多项式的精确首一 gcd 为
$$
\boxed{w^{90}(w+1)^4(w^2+2w-1)^2.}                           \tag{4.3}
$$
仅用前两个结式时还留下 $3w+4$ 和一个十二次因子；原单点范数差 (2.4) 的第三个结式完整消掉这两个候选，没有把它们未经检验就宣布为空。

共同有限根必使结式为零，故每个原解必须满足 (4.3)。$w=0$ 已由完整物理排除支付，剩下
$$
w=-1\quad\text{或}\quad w^2+2w-1=0.                         \tag{4.4}
$$
整个论证只使用结式的必要方向。任何由首项下降引入的额外根都继续保留到下一节，没有因某次结式降次而丢掉例外。

## 5. 最后两个纤维回到原多项式后均矛盾

### 5.1 $w=-1$

将 $w=-1$ 直接代入四个一轮结式 $R_{MS},R_{MC},R_{MT},R_{ML}$。它们在 $\mathbb Q[v]$ 中的精确首一 gcd 为
$$
v.
$$
因此原解必有 $v=0$，与已完整排除的异常曲线矛盾。

### 5.2 $w^2+2w-1=0$

令 $Q_w=w^2+2w-1$。将四个一轮结式分别对 $Q_w$ 关于 $w$ 取余，再加入 $Q_w$，它们在 $\mathbb Q[v,w]$ 中的精确约化 lex Gröbner 基是
$$
\{v-1,\ Q_w\}.                                               \tag{5.1}
$$
$Q_w$ 首一，取余不引入参数分母；两个共轭根都保留在同一个有理数理想中。故原解必须 $v=1$。

此时返回第三节由原 $M,S,c_0$ 得到的三个多项式 $M_*,S_*,C_*$，不再只依赖结式。代入 $v=1$，分别对 $Q_w$ 取余并加入 $Q_w$，在 $\mathbb Q[\ell,w]$ 中得到精确约化基
$$
\{\ell-1/2,\ Q_w\}.                                         \tag{5.2}
$$
因此最后纤维强迫 $\ell=1/2$，与已经完整支付的半总权分支矛盾。至此 (4.4) 的全部根均已排除。

## 6. 自含原式复算及完整结论

配套[自含 QQ 源](../notes/2026-11-26-unit211-opposite-regular-main-exclusion-347c.py)直接实现原 Frobenius 乘法和原 $K_B$，保留全部原 $P,N$ 值与一阶 jet，在形式二次代数 $u^2=e_*$ 中精确生成各式。它核验已解的三个 mean、剩余 mean、多项式奇偶身份、原 trace 和单点范数身份、全部结式次数、(4.3) 的真正 QQ gcd，以及 (5.1)、(5.2) 的两个完整末纤维。依赖 Python 3.12.14、SymPy 1.14.0、python-flint 0.9.0；所有计算数组仅在内存中。

实际执行命令为 `PYTHONPATH=/tmp/isp-347c05929dd3/deps python 2026-11-26-unit211-opposite-regular-main-exclusion-347c.py`，exit 0，程序计时 49.017732 秒，峰值 RSS 101092 KiB；源码 SHA256 为 `8d35129c88d20fe7476b82b309e1858a38d78a93f0a14aab51c2a2e338c54657`。源码引用前稿已经完成的边界，不重跑这些完整结论。

从第一节列出的穷尽分拆出发，所有 $p=1,q=-1$ 的单位 $2+1+1$ 原分支均已排除。这是同一原物理模型下的空性结果，包含该模型允许的无穷远支撑；没有用抽象范数解冒充物理临界点，也没有将此排除当作全局幂恒等式或普通 ISP 的证明。下一未付范围是非相等、非相反的两个非零基点配对。
