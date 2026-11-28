# R150：正确 Phi 整 alpha 零支的原范数、42 次投影及 378 权点界

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。

**已证明。** 当前修正后的 $\Phi=0,\ D_{\rm val}\ne0$ 原图中，整个 $\alpha=0$ 分支满足一条实际 42 次 QQ 多项式 $U_{42}(u)=0$。每个复 u 纤维的不同 Q 值至多 9 个，故不同权对至多 **378**。沿既有固定 $U/U_0$ 规范，完整不同原点至多 **1512**。这是必要有限覆盖，尚未排空 $\alpha=0$。

所有结论来自唯一首次精确原返回；没有使用模空性、单根嵌入或原范数逆，也不恢复旧错误 Rbar 的消元链。

## 1. 整支已成的真实首一 V 二次

记
$$
\delta=1-Q,\quad m=u-\ell,\quad \theta=u-\ell Q,\quad
M=4bc\delta,\quad \alpha=4\delta(f-u)-\theta t.
$$
沿 [整 alpha 零的原单首一环境](R150-appendix-unit211-Phi-zero-true-whole-alpha-zero-monic-V-two-and-weight-conditions.md)，原身份已在此整支支付 $m,\theta$，并给
$$
f=u-\frac{\ell\theta}{2m},\qquad
t=-\frac{2\ell\delta}{m}.
\tag{1}
$$
用原加权值 $V=bX+cY$，真实两个均值满足
$$
q(V)=V^2+q_1V+q_0=E_{Bo}/H,\qquad
H=\frac{4u\theta}{M^2}\ne0.
\tag{2}
$$
设
$$
E_{Be}=e_2q+a+bV,\qquad
r_0=a+bV.
$$
式中的系数 b 只表示该线性余式的系数；其出现不要求原权 b 等于它，也没有倒置此系数。

原 $N_1,N_S,P_S$ 的同 V 余式与 $r_0$ 已给三个必要纯权条件
$C_N,C_S,C_P$。本次只按这些既成对象的原行列式定义再生并核 SHA，不执行旧三个 pair 的证明门。

## 2. 新范数完整合成到两个原均值

定义
$$
n=a^2-q_1ab+q_0b^2.
$$
固定 $(2,1)$ 原结式身份给
$$
n=(a-q_1b-bV)r_0+b^2q.
$$
代回 (2) 和完整 $E_{Be}$ 得
$$
n=(m_0+m_1V)E_{Be}+(n_0+n_1V)E_{Bo},
\tag{3}
$$
其中
$$
m_0=a-q_1b,\quad m_1=-b,\quad
n_0=(b^2-e_2m_0)/H,\quad n_1=-e_2m_1/H.
$$
仅 H 是既有整支单位；没有倒置 b 或新首项。

源码实际返回 (3) 的 $V^0,V^1,V^2,V^3$ 全四坐标，再清四个真实乘子的已付权分母，取全部四乘子的共同内容。此次共同内容准确为 1。重新回乘并仅剥真实已付权支持后，得到必要多项式
$$
N(u,Q)=0.
\tag{4}
$$
其双次数为 $(20,9)$，总次数 20，118 项，规范原字典 SHA256 为

22cb8b5ccc91ee178afa4abbceeae38e27066de5dbe0e4459c1f861d9c808e04。

实际完整 QQ 因式乘回给一个不可约因子、重数 1；这里只指 QQ 不可约，不宣称绝对不可约。所有原二次和线性头零纤维均保留。

## 3. N 自身没有任何竖纤维

写
$$
N(u,Q)=\sum_{j=0}^9 n_j(u)Q^j.
$$
本次系数 Euclid 实际只使用了 N 自身的 $j=0,1,2,3,4$ 五项，即日志位置
$[(0,0),(0,1),(0,2),(0,3),(0,4)]$，便完整返回
$$
\sum_{j=0}^4 a_j(u)n_j(u)=1
\quad\text{于 }\mathbb Q[u].
\tag{5}
$$
这不是仅对四个原权条件的联合系数给单位，也没有在 (5) 中剥除 u 因子；实际首一 gcd 本身就是 1。

因此对每一个复 $u_0$，$N(u_0,Q)$ 都是非零的一元多项式。其次数可以降到 9 以下，但不可能恒零。故每个 $u_0$ 最多有 9 个不同 Q 根，包括所有最高系数退化纤维。

## 4. 两个完整固定 Q 结式与 42 次覆盖

本次首次计算
$$
R_N(u)=\operatorname{Res}_Q(N,C_N),\qquad
R_S(u)=\operatorname{Res}_Q(N,C_S).
\tag{6}
$$
原固定次数分别是 $(9,8)$ 和 $(9,11)$，因此对应固定 17 阶与 20 阶 Sylvester 行列式。任一有限共同 Q 根给非零 Vandermonde 核列，所以必要行列式为零；不在某个 u 点重新缩小矩阵，全部 Q 首项零纤维都包含。

实际 QQ 次数及身份为：

| 对象 | QQ 次数 | SHA256 |
|---|---:|---|
| $R_N$ | 164 | 23099a933d8d407ae57955ae33070df3b95b31109e030411efd3e433dd5be882 |
| $R_S$ | 241 | 8d071a969df2bc89b66ebd2b0bc2d5866292d6ac07d1d1760688ab8ebc369c75 |
| 首一 $\gcd(R_N,R_S)$ | 142 | f1f15250b5c4d792bf6ab317714dda10de7952643f8aa6306b9fd79002123e79 |

两次完整 QQ Bézout 均乘回。最后只剥当前整 alpha 零图上已经支付的权支持，全部除法乘回，得到
$$
U_{42}(u)=0,\qquad \deg U_{42}=42.
\tag{7}
$$
该多项式 43 项，SHA256：

a2ad5fc1085bdb07f18030adf2aba55be3165c43aa773f31f71df30ffae03a65。

本篇没有对它的所有零纤维返回原值，也没有把必要结式根当作充分原点。

由 (7) 和 (5)，不同权对数至多
$$
42\cdot9=378.
\tag{8}
$$
源末通用统计使用四个条件的最大 Q 次数 11，照实输出宽界 462。本篇的 378 直接来自同一次实际已返的 (5)：N 自身已经排竖纤维，因此可以使用 N 的 Q 次数 9。没有新增计算或修改执行回执。

## 5. 同规范完整不同点至多 1512

对每个权对，(2) 是同 V 的首一二次，所以不同 $(u,Q,V)$ 点至多 $2\cdot378=756$。由 (1)，f、t 唯一；原 E0/N0/P1 同点恢复给
$$
W_1=(T_0+4uf)/2,\quad A_1=2f-2V+2bc\,t,
$$
$$
\lambda=\frac{Jf+bcQt-QV-(u-1)T_0}{P_{02}},\qquad
T=\frac{T_0A_1}{2P_{02}}-\ell.
\tag{9}
$$
因此 $\lambda,T$ 也唯一，没有另乘 lambda 次数。

保 $\rho^2=1-Q$ 的两个可能值。对每个 $\rho$，
$$
b=\frac{\ell+m/\rho}{2},\qquad c=\frac{\ell-m/\rho}{2},\qquad
p=1+\rho,\quad q=1-\rho,
$$
$$
x=\frac{\theta V-mW_1}{M},\qquad
y=\frac{\ell W_1-uV}{M},\qquad
X=x+\rho y,\quad Y=x-\rho y
$$
唯一；原四列 Gram 的
$$
r=X-(1-\ell)p-ct,\qquad s=Y-(1-\ell)q-bt
$$
与 $A_1,t$ 全部唯一。这使用的 M、rho 分母均是原单位。

最后核固定 $U/U_0$ 孤立列的恢复，而非只数基础四列。沿
[原 U 值图](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md)，该列写作
$(1,w,h,k)$，$w=\lambda-1-T$。记
$$
X_U=h-1,\qquad Y_U=k-1,\quad
A_2=2\lambda^2-2\lambda+1,\quad
B_3=4\lambda^3-6\lambda^2+3\lambda-1.
$$
原同点矩给
$$
bX_U+cY_U=T,\quad
bX_U^2+cY_U^2=A_2,\quad
bX_U^3+cY_U^3=B_3.
$$
若 $S=X_U+Y_U,\ P=X_UY_U$，则
$A_2=TS-\ell P$、$B_3=A_2S-TP$，所以在当前
$D_{\rm val}=\ell A_2-T^2\ne0$ 图上
$$
S=\frac{\ell B_3-TA_2}{D_{\rm val}},\qquad
X_U=\frac{T-cS}{b-c},\qquad
Y_U=\frac{bS-T}{b-c}.
\tag{10}
$$
此整支已付 $m=(b-c)\rho\ne0$，故 (10) 的分母合法，孤立列也唯一。

每个 $(u,Q,V)$ 最多对应两个 $\rho$，从而同一固定规范的完整不同原点数至多
$$
756\cdot2=1512.
$$
这是不同点数界，不宣称整个必要方案的长度、商模自由秩或最后 42 次支持已经排空。

## 6. 唯一实际回执

源：[整 alpha 零新原范数与 Q 投影](../notes/2026-11-28-unit211-Phi-zero-true-alpha-zero-original-norm-and-Q-projections-8542.py)，blob 61066a5a18105081e38d919170e0bd4b3f2c09ac，SHA256：

385ce1a1c0c70e404dcf08ed84ea22db4e9350624721d480ef86265853715ee0。

run **46129066446**，job **140930042380**；source commit
e97b242fe9715bf8f38ceab2924b3cb347514542，真实 pull 到
7d9df60a56d62cb30c7edf3c3eabe42c5a282e7b，2026-11-28 09:08:59.266624 UTC，两 README 无变。

数学末阶段 0.329488159 秒，驱动 **0.381504878 秒**，RSS **41636 KiB**，exit **0**。原预算 120 秒/1 GiB，外 135 秒。stdout **3724** 字节，SHA256：

11492b3ce25c255e99d14ea88764d2fbb8294ff7b897cdeb5d195df63d1f7922。

[小回执](../notes/2026-11-28-unit211-Phi-zero-alpha-zero-norm-Q42-execution-8542.json)保存源的原宽界和上述已成身份。系数载荷没有输出、分片或入库；只保必要定义、准确 SHA 与实际小回执。
