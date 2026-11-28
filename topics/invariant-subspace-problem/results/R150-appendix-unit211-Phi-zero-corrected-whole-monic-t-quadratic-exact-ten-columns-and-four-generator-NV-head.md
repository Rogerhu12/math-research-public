# 正确 Phi：两个原均值的全权首一 t 二次、精确十列与 NV 第二头四生成环境

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-29（Asia/Taipei）。

**状态：完整显示的原多项式证明，无新执行。** 在当前正确 Phi 原恢复中，固定 $(\lambda,T)$ 后，两个真实均值的 t 二次头在旧已付系数环上生成 1。由此得到全权首一 $t^2$ 方程。三个原均值有精确二生成、四列呈示；整个原 I6 有精确二生成、十列呈示，不需斜率头开图。在完整 NV 第二 t 头上，它与原首一 sigma 二次给一个真正自由四生成的必要环境。

自由性仅指本文明确构造的两个首一多项式环境，不表示加入全部原条件后的商自由。本条没有排除原点，也没有降低既有全权纤维长度或公共权曲线界。

## 1. 原范围和固定谱参数的真实恢复

仍用当前正确 $\Phi=0$、distinct singleton、物理 $D_{\rm phys}\ne0$ 原图。设
$$
s=u-1,\quad \delta=1-Q,\quad
L=Q-2(u-1)(u-2),\quad \ell=L/Q,\quad m=u-\ell,
$$
$$
M=\ell(2u-\ell Q)-u^2=4bc\delta,\qquad
T_0=2u-\ell Q-2u^2,\qquad J=2u(1-u)+\ell Q .
$$
令 $\mathcal A$ 为当前已付纯权系数环；特别
$$
Q,\delta,s,\ell,bc,T_0,J-Q,P_{02}
$$
为旧单位，其中 $P_{02}=2s\ell Q$、$J-Q=-4s^2$。以下新组合没有 m 的逆，没有新几何头或 D 的逆，也不使用 W 的恢复或撤回的 wrong-Rbar 链。

按[正确全 t 原模型](R150-appendix-unit211-Phi-zero-corrected-whole-t-parameter-three-mean-generators-and-monic-lambda-cubic.md)，固定 $(\lambda,T)$ 后
$$
E=\frac{P_{02}(T+\ell)}{T_0},\qquad
f=\frac{P_{02}\lambda-QE+sT_0}{J-Q},
$$
$$
\mathcal V=f+bc\,t-E,\quad A_1=2E,\quad W_1=T_0/2+2uf .
\tag{1}
$$
因此
$$
[t]f=0,\qquad [t]\mathcal V=bc,\qquad
[t]A_1=[t]W_1=0.
\tag{2}
$$
这来自同一点原 $E_0,N_0,P_1$ 的双向恢复，没有施加物理 f 或 t 特化。

记 $\theta=u-\ell Q$，原 singleton 坐标为
$$
x=\frac{\theta\mathcal V-mW_1}{M},\qquad
y=\frac{\ell W_1-u\mathcal V}{M},\qquad
X=x+\rho y,\quad Y=x-\rho y,\quad \rho^2=\delta.
$$
由 (2)，
$$
\xi=[t]x=\frac{\theta}{4\delta},\qquad
\eta=[t]y=-\frac{u}{4\delta},
$$
$$
[t]X=\xi+\rho\eta,\qquad [t]Y=\xi-\rho\eta .
\tag{3}
$$
这里 xi、eta 仅表示 t 的系数，不是另一个无穷远或模点的坐标。

## 2. 两个真实均值的准确 t 二次头

用正确原式
$$
\mathcal R=4(f-u)(\mathcal V-f)+bc\,t^2
+t\left(4bcu-\ell\mathcal V+
 \frac{m(T_0+4uf-2\mathcal V)}{2\delta}\right).
\tag{4}
$$
它来自更正后双点乘法的完整原身份
$
2\mathcal R+E_1-bE_B-cE_C=0,\qquad
bE_B+cE_C=\ell E_{Be}+mE_{Bo}.
$
因此 $(E_1,E_B,E_C)$ 与 $(\mathcal R,E_{Be},E_{Bo})$ 给同一原均值理想。该身份先在 $E_0=0$ 的原 Gram 上成立；其自由权来源见[原 alpha/chi 坐标](R150-appendix-unit211-W-global-original-alpha-chi-polynomial-coordinates.md) §2，本文仅引用 W 权代入之前的完整身份。由 (2)，
$$
a_R=[t^2]\mathcal R
=bc\left(1-\ell-\frac m\delta\right)
=-\frac{bc\,s(2u-3)}{\delta}.
\tag{5}
$$
最后一步仅用正确 Phi 权式 $\ell Q=L$。没有单独反演 $2u-3$。

为独立核另一个头，取原 $a=1-\ell$、
$p=1+\rho$、$q=1-\rho$、
$b=\ell/2+m\rho/(2\delta)$、c 为共轭。
真 Gram 行 $g_B=(p,r,0,t)$ 给完整均值
$$
E_B=ap^2+2pr+ct^2
-2(apu+pd_1+ru+ctY)-2X^2+4fX,
$$
$$
r=X-ap-ct,\qquad d_1=2f-\mathcal V-au.
\tag{6}
$$
(6) 使用真实 double-germ 乘法，没有以 $d_1^2$ 代替其第二坐标。由 (2)，其 t 二次头严格是
$$
[t^2]E_B=c-2c(\xi-\rho\eta)-2(\xi+\rho\eta)^2 .
\tag{7}
$$
令 $E_{Bo}=(E_B-E_C)/(2\rho)$。取 (7) 的完整奇系数，得到
$$
\begin{aligned}
a_O=[t^2]E_{Bo}
&=\frac{m(2\xi-1)}{2\delta}+\ell\eta-4\xi\eta\\
&=\frac{\theta(2u-\ell)-\delta(2m+\ell u)}{4\delta^2}\\
&=\frac{m\{2s+Q(2-\ell)\}}{4\delta^2}
=\boxed{\frac{m(Q+2s^2)}{4\delta^2}}.
\end{aligned}
\tag{8}
$$
其中最后一步再次只用 $\ell Q=Q-2s(u-2)$。整个 m 零面未被此计算当作新物理单位。

## 3. 显示 Bézout1 与全权首一 t 二次

定义一个仅用于本条公式的纯权多项式
$$
B_q=Q^2+(2u^2-3)Q+2s(2u-1)(u-2).
\tag{9}
$$
这个符号不是此前旧 B 权曲线。利用 $mQ=uQ-L$，直接展开有
$$
Q\{2m(Q+2s^2)+\ell\delta\}=(2u-3)B_q.
\tag{10}
$$
等价地，由 (8)，
$$
8\delta a_O+\ell=\frac{(2u-3)B_q}{Q\delta}.
\tag{11}
$$
例如将 $u=s+1$ 代入 (10)，三个 Q 系数依次都是 $2s-1$ 的倍数，商为
$Q^2+(2s^2+4s-1)Q+4s^3-2s^2-2s$，即 (9)。

代 (5) 入 (11)，得到旧已付环上的完整恒等式
$$
\boxed{
\gamma_R a_R+\gamma_O a_O=1,\qquad
\gamma_R=-\frac{B_q}{\ell bc\,sQ},\qquad
\gamma_O=-\frac{8\delta}{\ell}.
}
\tag{12}
$$
两个系数只含旧单位分母。特别 $\gamma_O$ 本身也是旧单位；(12) 同时覆盖 $2u-3=0$ 和 $a_O=0$，并没有用两个开图来删除交界。

于是
$$
\boxed{
q_t=\gamma_R\mathcal R+\gamma_OE_{Bo}
=t^2+\alpha(\lambda,T)t+\beta(\lambda,T)
}
\tag{13}
$$
是整个当前正确 Phi 权图的真正原首一二次。所有原均值在 (1) 后对 $(\lambda,T,t)$ 总次数至多二，所以
$$
\deg_{\lambda,T}\alpha\le1,\qquad
\deg_{\lambda,T}\beta\le2 .
\tag{14}
$$
这里不需要 t 为单位，也不倒 D 或任何新值头。(13) 是显示原多项式组合，不以泛型头非零、点集空性或抽象存在性代替来源。

## 4. 三个原均值的精确四列呈示

取 $R=\mathcal A[\lambda,T]$。依次令
$$
F_R=\mathcal R,\quad F_B=E_{Be},\quad F_O=E_{Bo},
\qquad a_i=[t^2]F_i,
$$
$$
r_i=F_i-a_iq_t,\qquad \deg_t r_i\le1.
\tag{15}
$$
由 (12)–(13)，完整身份为
$$
\gamma_Rr_R+\gamma_Or_O=0.
$$
因 $\gamma_O$ 是旧单位，原三个均值的理想准确等于
$$
\boxed{
(F_R,F_B,F_O)=(q_t,r_R,r_B)
\quad\text{于 }R[t].
}
\tag{16}
$$
两向包含都由 (13)、(15) 给出，不需要三个原式的某个新头为单位。

普遍代数 $R[t]/(q_t)$ 是自由二生成，以 $(1,t)$ 为基。若
$r_i=A_i+B_it$，则它及 t 倍的真实余式列为
$$
\binom{A_i}{B_i},\qquad
\binom{-\beta B_i}{A_i-\alpha B_i}.
\tag{17}
$$
取 $i=R,B$ 的四列，cokernel 就是 (16) 的原均值商。这里自由二生成只属于首一二次环境；原均值商不被假定自由。

## 5. 整个原 I6 的精确十列

沿正确原定义，I6 由三个均值以及完整 $N_1,NS,PS$ 生成。对后三式仅作 (13) 的首一 t 除法：
$$
F_i=r_i+Q_iq_t,\qquad r_i=A_i+B_it,\qquad i=N,S_N,S_P .
\tag{18}
$$
此处保持完整原 N1 与完整加权 NS/PS；未以最高项或某个分量替代它们。首一除法无需新权逆。

由 (16)、(18)，有准确原理想等式
$$
\boxed{
I_6=(q_t,r_R,r_B,r_N,r_{S_N},r_{S_P}).
}
\tag{19}
$$
因此将这五条一次余式各自按 (17) 加上 t 倍，得到 $R^2$ 中十条真实关系列，恰呈示整个原 I6 商。乘 t 的规则来自一个明确的结合二次代数，不是假定之前的三生成元呈示自由或结合。

由 (14)，首一除法保持总几何次数上界。均值和 N1 的 $A_i,B_i$ 总 $(\lambda,T)$ 次数至多 $(2,1)$；NS/PS 的上界至多 $(3,2)$。本条只给完整定义和纸面上界，没有执行这些实际系数、乘法表、cofactor、因式或原单位目标。

这个十列呈示的基环是 $\mathcal A[\lambda,T]$，生成元是 $(1,t)$。它不等同于此前在斜率补图上以 t 为基参数、以中心 omega 为二次变量的十列门；这里没有 H6/H8 或新斜率例外。本文也不重跑该旧门。

## 6. NV 第二 t 头的真正自由四生成必要环境

在
$$
\ell(3-2\lambda)+2T+2m\sigma=0
$$
整个支上，取 $a=\lambda-3/2$、$T=\ell a-m\sigma$。按[第二 NV 头的完整原二次与四列](R150-appendix-unit211-Phi-zero-corrected-second-NV-t-head-original-monic-sigma-and-four-columns.md)，原第二矩给
$$
q_\sigma=\sigma^2-\frac{2ma}{\ell\delta}\sigma
-\frac{A_\lambda-\ell a^2}{\ell\delta}.
\tag{20}
$$
它的首项为 1，分母只有旧 $\ell\delta$。将同一点的 T 代入 (13)，再把其系数按 (20) 首一短除，记所得 t 首一二次为 $\widetilde q_t$。两者之差只是 $q_\sigma$ 的原倍数，故没有丢掉来源。

于是
$$
\boxed{
\mathcal B=
\bigl(\mathcal A[\lambda,\sigma]/(q_\sigma)\bigr)
[t]/(\widetilde q_t)
}
\tag{21}
$$
是 $\mathcal A[\lambda]$ 上真正自由四生成的代数，可取
$$
1,\ \sigma,\ t,\ \sigma t
\tag{22}
$$
为基。理由是两次相继的首一二次除法；所有重根和幂零结构完整保留。

原剩余均值、N1、NS/PS、第三矩、完整 NV 和个别 odd N/P 都可在同一个 (21) 中作为原关系加入。它们的理想在基环上的准确关系可由各原余式乘 (22) 取得，无需先反演某个 lambda 头、D 或范数。完整 NV 在本支不含 t，不表示物理 t 被设为 0；t 由 (13) 保持为真正二次变量。

(21) 本身不是全部原条件的充分模型，也不表示最终商自由、有限于纯权或为空。下一新输入须逐式保留完整原值来源和所有实际纯权分母。第一 NV 头三标量 gcd 的资源边界已经冻结；本条不续接该算法，也不触及已冻结的 Q 主分量。
