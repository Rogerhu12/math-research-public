# 新输入：正确 Phi 第二 NV 头的真 E1/N1 同 t 范数与五条原值列

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-29（Asia/Taipei）。

**未执行。** 唯一新目标是从完整原 $E_1,N_1$ 的同一个 $t$ 变量取得一个至多四次的必要范数，再构造它的五条普通原值列。只有在预定点验证相应整矩阵非奇异，才登记新的非零纯权必要支持；完整新权零集保留。

源码 **2026-11-28-unit211-Phi-zero-corrected-second-NV-head-true-E1-N1-same-t-norm-five-original-weight-support-8542.py**，Git blob **5d1f200b19ef4ce2939d253470a5f77b0dde8091**，15598字节，SHA256：

**269b3925f9eb1ffb01fb36a1de16c41a2162564580f75d9732a003ce10e37860**。

零源码依赖；首次固定 **120 秒 / 1 GiB**、外135秒。唯一预定有限域点为
$$
p=1009,\qquad (u,Q)=(2,2).
\tag{1}
$$
不根据新列秩更换点、素数或预算。任何未返范围准确保留。

## 1. 与已成目标的区别及原范围

上一门 d2de、run 46182910418 已支付由五交换差 DAG 列定义的 $F_{\rm wt}\ne0$，次数上界 $(142,72)$。它只使用完整 $E_2,E_3,NV$。本次不重构该五列、它们的原标签、十个动作、交换子、DAG 秩选择、原整数矩阵、行列式或次数证明，也不重跑旧两个 sigma scalar、二十列、奇部八列或任何冻结 gcd。

本次首次加入的来源是完整真均值 $E_1$ 与完整第一 jet $N_1$。新显示纸稿

[R150-appendix-unit211-Phi-zero-true-E1-monic-t-quadratic-and-original-N1-linear-remainder.md](../results/R150-appendix-unit211-Phi-zero-true-E1-monic-t-quadratic-and-original-N1-linear-remainder.md)

（blob **eeae95f3a1e3126d004b6f3616cf58f1865eb0e3**）给真 $E_1$ 的纯权单位二次头，以及 $N_1-2(u-1)E_1$ 的完整一次式。本源实际输入这两个原式的完整系数，并将新范数及其五个基倍分别回原。

范围是正确 Phi、物理 $D\ne0$ 的第二 NV 头，已经独立排除其 $\ell=3/2$ 交集。基础权环
$$
A=\mathbb Q[u,Q,\mathcal U^{-1}],
$$
$$
\mathcal U=
Q(Q-1)(u-1)(Q+4u-4)L M_n(uQ-L)(3Q-2L),
$$
$$
L=Q-2(u-1)(u-2),\quad M_n=2uL-L^2-u^2Q
\tag{2}
$$
与已成五生成结构相同。所有实际约消后的分母必须逐项只含 (2)。不倒 $t,D,\lambda,\sigma$、新一次系数或新纯权支持。

## 2. 完整同点恢复

记
$$
s=u-1,\quad \delta=1-Q,\quad
\ell=L/Q,\quad m=u-\ell,\quad M=M_n/Q,\quad bc=M/(4\delta),
$$
$$
T_0=-Q-4s,\quad J=Q-4s^2,\quad P_{02}=2sL,\quad
\theta=u-\ell Q,\quad a_0=1-\ell.
$$
第二头给
$$
a=\lambda-\frac32,\quad
j=\ell\left(\lambda-\frac12\right)-m\sigma,\quad
T=j-\ell,\quad w=\lambda-1-T,
$$
$$
E=\frac{P_{02}j}{T_0},\qquad
f=\frac{P_{02}\lambda-QE+sT_0}{J-Q}.
\tag{3}
$$
置
$$
V_0=f-E,\quad W_1=T_0/2+2uf,\quad V_2=2u-\ell Q,
$$
$$
x_0=\frac{\theta V_0-mW_1}{M},\qquad
y_0=\frac{\ell W_1-uV_0}{M},
$$
$$
x=x_0+\frac{\theta}{4\delta}t,\qquad
y=y_0-\frac{u}{4\delta}t,\quad
A_1=2E,\quad d_1=f+E-a_0u-bc\,t .
\tag{4}
$$
这些式是同一点的真正原 Gram 恢复。源不以单个 $t$、$\lambda$、$\sigma$ 值代入，也不选择谱根。

## 3. 完整真 E1/N1 及新同 t 范数

令
$$
W_r=W_1-a_0V_2-2bc\,t,
$$
$$
S_1=\ell(x^2+\delta y^2)+2mxy-a_0W_1-2bc\,tx,
$$
$$
S_2-S_1=
m(x^2+\delta y^2)+2\ell\delta xy
-a_0(\theta x+u\delta y)-2bc\delta ty.
$$
真 dual-germ 普通原式为
$$
E_1=2W_r-2uA_1-2S_1+4(f-u)d_1,
\tag{5}
$$
$$
\begin{aligned}
N_1={}&4S_2-4fW_r-4u(uA_1+S_1)-4d_1W_1+8fu d_1\\
 &+2A_1V_2
 +2bc\,t(2x-2\delta y-2a_0Q-ut)-4\lambda wP_{02}.
\end{aligned}
\tag{6}
$$
来源中 $(d^2)_1=2ud_1$，没有沿旧错误 compact $R$。本源由 (5)–(6) 实际返回新纸稿的完整系数式
$$
E_1=a_Et^2+b_Et+c_E,\quad
a_E=-\frac{bc\ell Q}{2\delta},\quad
b_E=4bc(y_0-f+s),
$$
$$
\mathcal L_N=N_1-2sE_1=a_N+b_Nt,\qquad
b_N=4bc(W_1-x_0-\delta y_0-2s^2).
\tag{7}
$$
$c_E,a_N$ 按同一普通原式的 $t^0$ 系数显示构造并完整回乘；它们对 $(\lambda,\sigma)$ 次数至多二。$a_E$ 是旧权单位，不是新猜测的几何头。

写
$$
q_E=E_1/a_E=t^2+q_1t+q_0,\quad
q_1=b_E/a_E,\quad q_0=c_E/a_E.
$$
唯一新的同变量标量为
$$
\boxed{R_N=a_N^2-q_1a_Nb_N+q_0b_N^2.}
\tag{8}
$$
它不含 $t$，几何 $(\lambda,\sigma)$ 总次数至多四；没有预报其权次数或非零性。

固定两个真实原乘子
$$
\Omega_N=a_N-q_1b_N-b_Nt,\qquad
\Omega_E=\frac{b_N^2}{a_E}-2s\Omega_N .
$$
普通恒等式是
$$
\boxed{R_N=\Omega_EE_1+\Omega_NN_1.}
\tag{9}
$$
源码必须在完整 $A[\lambda,\sigma,t]$ 中返回 (9)，并核所有 $t$ 项真正相消。它没有倒 $b_N$；$b_N=0$ 的全部纤维与常数余式都保留。

(8) 是同一个首一二次与同一个原一次余式的必要 norm。没有把若干独立 norm 零拼成全系统同根充分性，也没有把 (9) 解释成全部原均值和 singleton N/P 的充分条件。

## 4. 五生成规则只作必要参数定义

使用已付
[R150-appendix-unit211-Phi-zero-corrected-second-NV-head-global-four-head-unit-and-five-generator-algebra.md](../results/R150-appendix-unit211-Phi-zero-corrected-second-NV-head-global-four-head-unit-and-five-generator-algebra.md)
的完整三个原式
$$
\begin{aligned}
E_2&=\ell a^2-2ma\sigma+\ell\delta\sigma^2-A_\lambda,\\
E_3&=\ell a^3-3ma^2\sigma+3\ell\delta a\sigma^2
                        -m\delta\sigma^3-B_\lambda,\\
NV&=2[-(\lambda^2+\lambda-\tfrac34-\delta\sigma^2)f
 +(a^2-\delta\sigma^2)E-w(ua+\theta\sigma)]-2fE_2 .
\end{aligned}
\tag{10}
$$
其中 $A_\lambda=2\lambda^2-2\lambda+1$、
$B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1$。

四个三次头按 $(\lambda E_2,\sigma E_2,E_3,NV)$ 定义，已付行列式是
$2P_{02}m\delta(3-2\ell)$。本源只用固定三阶 cofactors 再生其逆和四条降次规则；不重新计算四阶 determinant 或返回旧32坐标作为目标。再定义 $E_2/(\ell\delta)$ 的 $\sigma^2$ 规则。

必要降次依旧是：先用四个三次规则严格降低总次数，再在总次数至多二处消 $\sigma^2$。对本次每个新输入 $P$ 都实际返回
$$
P=\mathcal B\,v(P)+\tau(P)\cdot(E_2,E_3,NV)^t,\qquad
\mathcal B=(1,\lambda,\sigma,\lambda^2,\lambda\sigma).
\tag{11}
$$
(11) 的普通原返回本身核定这次使用的规则；没有旧动作、交换子或旧点选验证的再执行。

## 5. 五条固定新原值列

只有在实际 $R_N\ne0$ 时继续。固定输入恰为
$$
R_N,\quad \lambda R_N,\quad \sigma R_N,\quad
\lambda^2R_N,\quad \lambda\sigma R_N,
\tag{12}
$$
不从旧交换子队列选列，也不在 rank 之后追加列。

对 $\mathcal B_jR_N$ 用 (11) 得 $v_j,\tau_j$。结合 (9)，完整新来源为
$$
\boxed{
\mathcal Bv_j
=-\tau_{j,1}E_2-\tau_{j,2}E_3-\tau_{j,3}NV
 +\mathcal B_j\Omega_EE_1+\mathcal B_j\Omega_NN_1.}
\tag{13}
$$
这五个等式全部在未取商的普通 $A[\lambda,\sigma,t]$ 中返回。它们来自五个完整原多项式，不要求五生成元自由，也不构造自由代数上的虚拟乘法。

每列的实际五系数只清旧权分母 LCM，再清有理常数分母、除正整数内容，得到整数列 $\mathsf C_j$。同一个列尺度乘到全部五个 (13) 乘子，最终再次完整原返回；五列零的情况直接停止，不能假装整矩阵非零。

令 $\mathsf C=(\mathsf C_1,\ldots,\mathsf C_5)$。它由 (12) 固定，没有列选择、重排或候选重试。普遍 adjugate 给
$$
\mathsf C\operatorname{adj}(\mathsf C)e_0=G_{\rm wt}e_0,
\qquad G_{\rm wt}=\det\mathsf C,
$$
进而把 $G_{\rm wt}$ 返回到
$$
(E_2,E_3,NV,E_1,N_1)
\quad\text{于原已付系数环。}
\tag{14}
$$
只定义 (14)；不展开巨大 QQ 行列式或重新计算已有 $F_{\rm wt}$。

## 6. 唯一固定点、次数上界与精确边界

在 (1) 核整数列尺度和所有实际分母；若不合格，停止并保留全部纤维。若合格，对唯一新整数 $\mathsf C(2,2)$ 作有限域 Gaussian：

- rank 小于五：只记录实际 rank 与全部原返回，不宣 $G_{\rm wt}\ne0$，不换点；
- rank 五：必须完整返回其双向50坐标，且实际 determinantModuloP 非零，才付 $G_{\rm wt}$ 为 QQ 非零多项式。

之后只按实际整条目，枚举固定五阶120个匹配取得 $u$、$Q$、总次数上界。不宣保度，也不按模结果删除 paid 或未付因子。

即使本次非零支持成功，完整 $G_{\rm wt}=0$ 零集仍保留。没有预报它与已成 $F_{\rm wt}$ 互素、没有有限权点界，也没有整个第二头或整个 Phi 空性。若只完成 (9) 或部分 (13)，就只登记那些真实身份。

本输入不触及第一 NV 头已冻结的三个 scalar 合并 gcd，不重原20/8列或旧全图 cofactor，不续 QQ[u] 幺模资源门，不保存可重算的系数 payload。任一实现异常或预算截止都按实际最后阶段准确冻结。
