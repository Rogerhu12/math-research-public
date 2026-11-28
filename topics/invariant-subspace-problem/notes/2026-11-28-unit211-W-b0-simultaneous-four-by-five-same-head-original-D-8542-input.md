# 首次新输入：整 b0 同步四乘五伴随、同 h 原恢复与直接 D 目标

- 会话：Astra-ISP-8542378f-20261127。
- 日期：2026-11-28（UTC）。
- 状态：未执行，不预记新头非零、纯权核非零、已付头、次数、点数或排空。
- 源：2026-11-28-unit211-W-b0-simultaneous-four-by-five-same-head-original-D-8542.py。
- Git blob：1898abba431faf62aca343cc2122e48b45d0599d。
- SHA256：313957129f4b54195253caf973ca1fdb93faaa59adb0027c1c9924c2d2faf3bd。
- 21087 字节；自含、零依赖；唯一首次 180 秒、4 GiB，外层可为 195 秒。

## 1. 原范围与和冻结门的严格分离

沿[整 b0 五原二次定义](../results/R150-appendix-unit211-W-b0-inverse-slope-five-original-quadrics-six-weight-conditions.md)的全部原域，保持 distinct-singleton、$D\ne0$ 和所有既有原单位。这里

$$
J_5=(E_1,E_{B,e},E_{B,o},N_1,q_2)
=(q_f,r_1,r_2,r_3,q_2).
\tag{1}
$$

新源仅从真 Gram、原 $q_2$、$q_f$ 和 $r_i$ 的必要定义进入，不执行旧六个 Sylvester 投影、旧 primitive PRS、旧 C74/C78 或其 gcd，也不重新计算全图 NS/PS 六核。

新原来源是[同 h 四乘五纸面定理](../results/R150-appendix-unit211-W-b0-simultaneous-four-by-five-same-head-original-recovery.md)中的同步系数矩阵，不是把旧投影延时或换序重放。原 $I_{11}$ 一直全部保留；(1) 仍只称物理必要子理想。

## 2. 全支权恢复及 q2 定义

使用

$$
\nu=\frac{(2u-1)(k+2)}{uk+2},\quad
d=u\nu-(2u-1),\quad r=2u-1-\nu,
$$

以及

$$
k=\frac{2r}{d},\quad
Q=\frac{2(u-1)r}{d},\quad
\ell=\frac{u(\nu^2-(u+1)\nu+2u-1)}r.
$$

源码完整核正反身份与已付分母，不删新的 $d=0$ 或 $r=0$ 原图。完整 b0 的 $A_*=uQ(\nu+2)$ 已由先前原值定理支付，所以仅在这个整分支中

$$
\kappa=\frac{\ell}{\nu+2},\qquad
T=-\kappa(3-2\lambda)
$$

合法。$\nu+2$ 不外推为整个 W 的单位。

原 $q_2=2a_d/\ell$ 与 $C_4=mD\ell q_2$ 完整保留。它的三系数组合 $a_2+3a_1+4a_0=-32uQ\delta\ell\kappa^2$ 为单位，但本源从未倒 $a_2$、$a_1$。所有实际次数下降留在原矩阵里。

另外只允许既有整 G36 原单位在新权坐标中的准确拉回；复制固定旧 36 项定义并核旧定义 SHA，直接返回 $d^8G_{36}(u-1,2r/d)$ 的完整多项式身份。没有复算旧 G36 排除或因式，也不改已冻结 10ab 源的支撑列表。

## 3. 真四行与新四乘五系数矩阵

原真 dual 乘法给独立 $E_1$，不使用错误 compact E1。$q_f$ 的 $E_{B,e}$ 系数是旧原单位，三个

$$
r_i=A_i(\lambda)+B_i(\lambda)f
$$

对 $(\lambda,f)$ 总次数至多二，且没有 $f^2$ 项。因此四行 $r_1,r_2,r_3,q_2$ 恰在

$$
(1,\lambda,f,\lambda^2,\lambda f)
$$

五个单项式上。源码逐项提取系数，核完整行回乘，并核每行相对于 (1) 左边五个原源的纯权组合。

各行仅乘其实际系数的已付权分母 LCM，得到纯权多项式矩阵

$$
F=L(1,\lambda,f,\lambda^2,\lambda f)^{\mathsf t},
\qquad L=[c_0\mid B],\quad B\in A_W^{4\times4}.
\tag{2}
$$

本次唯一矩阵目标就是这个固定 B 的 adjugate。程序逐条计算 16 个三阶子式，并核

$$
B\operatorname{adj}B=(\operatorname{adj}B)B=(\det B)I
$$

全部 32 个坐标。这里没有 Gaussian 主元或 determinant inverse。

## 4. 二十个乘子统一取消，同一个 h 不变

原四个伴随关系给

$$
\operatorname{adj}(B)F
=h_{\rm raw}(\lambda,f,\lambda^2,\lambda f)^{\mathsf t}
+v_{\rm raw}.
$$

源码将四行复合到五原源，共二十个实际纯权乘子。取它们共同的分母 LCM $\Delta$；只能是旧原单位。再取全部二十分子的共同因子 $c_{\rm com}$，所有二十个同时精确整除。四行统一使用同一个尺度，不能逐行改变头。

最终得到

$$
H_j=h\,m_j-K_j\in J_5,
\quad(m_1,m_2,m_3,m_4)=(\lambda,f,\lambda^2,\lambda f).
\tag{3}
$$

原组合本身保证 h 和各 K 的最终分母只有旧原单位；源逐个实际核这个支付。然后直接核

$$
BH=hF,\qquad L(h,K_\lambda,K_f,K_{\lambda^2},K_{\lambda f})^{\mathsf t}=0.
\tag{4}
$$

未知 $c_{\rm com}=0$ 完整保留，因为取消后的每行都有五原源的直接乘回；不借 $c_{\rm com}$ 的单位性。若全部二十个乘子为零，准确输出零伴随接口，保整原支，不继续猜恢复。

头 h 不预先付。源码只检查其实际分子能否被旧已付支持整除剥尽，输出真实布尔值及剩余支撑；不作新的头因式分解。若 h 整式为零，只有四条 $-K_j\in J_5$，没有 h 开图。

## 5. 先取真正原 D 目标

因本支 T 仿射于 lambda，

$$
D=d_2\lambda^2+d_1\lambda+d_0.
$$

首先返回全五原源身份

$$
hD-C_D=d_2H_{\lambda^2}+d_1H_\lambda,\qquad
C_D=d_2K_{\lambda^2}+d_1K_\lambda+d_0h.
\tag{5}
$$

这里 D 只正乘，未使用范数逆或模幂零。

如果实际 $C_D=0$ 且 h 确只含旧已付权支持，则 (5) 与原物理 $D\ne0$ 直接排除整 b0，源立即完成，不额外执行后续可选权目标。如果 $C_D\ne0$，或 h 仍有未付支撑，则只登记 (5) 的准确关系和所有 h 零纤维，不能预称排空。

## 6. 三个同时相容的纯权必要式

若尚未得到上述完整排空，并且 h 不是零式，设

$$
q_f=f^2+(a\lambda+b)f+c\lambda^2+d\lambda+e_0.
$$

源码按预定顺序构造三个新权式：

$$
\begin{aligned}
S_1&=hK_{\lambda^2}-K_\lambda^2,\\
S_2&=hK_{\lambda f}-K_\lambda K_f,\\
S_q&=K_f^2+(aK_\lambda+bh)K_f
 +cK_\lambda^2+dhK_\lambda+e_0h^2.
\end{aligned}
\tag{6}
$$

其来源逐项为

$$
\begin{aligned}
S_1&=(h\lambda+K_\lambda)H_\lambda-hH_{\lambda^2},\\
S_2&=h\lambda H_f+K_fH_\lambda-hH_{\lambda f},\\
S_q&=h^2q_f-(hf+K_f+ah\lambda+bh)H_f\\
&\quad-\{aK_f+c(h\lambda+K_\lambda)+dh\}H_\lambda.
\end{aligned}
\tag{7}
$$

每一项都完整复合五个原源，只约这五个真实乘子共同因子，再实际乘回；最后仅剥原已付权支持。任何未付共同因子、h 零面或几何头零都不被当单位。

若某新核为非零有理常数，必须完整五源返回后才宣布本物理整支为空，随后立即停止剩余目标。若只是零核，准确记零式并保其余原条件；不以多变量 gcd1 解释为空。本源不计算新的 resultant、factor、PRS 或 pure-u cover。

若 h 整式为零，则不执行 (6)，而先按固定顺序处理四个直接原权式 $-K_j=H_j$，同样只在实际原单位返回后才作排空结论。

## 7. h 开图的完整原意义及 h 零面

纸面定理已证明，明确局部化 h 后，

$$
J_5=(H_\lambda,H_f,S_1,S_2,S_q),
$$

并有

$$
A_W[h^{-1}][\lambda,f]/J_5
\cong A_W[h^{-1}]/(S_1,S_2,S_q),
\quad \lambda=K_\lambda/h,\quad f=K_f/h.
$$

这保整个原商的重数，但它只在 h 主开图成立。源码不额外计算这些比值，更不会把 h 主开图外推为整个 b0。

在整 h 零面，全部四个 K 必须为零，且仍保原五个方程和整个 I11。若尚未证明 h 全已付，所有这些纤维都继续开放。未执行之前，既不预记 h 为零或非零，也不预记三个 S 的任何次数、公共因子或点数改善。

## 8. 资源、输出及失败记录

总预算唯一首次 180 秒、4 GiB；所有定义和新目标共用同一次绝对 alarm。原定义重建只为提供新 4×5 的系数和真原来源；不接旧六个结式或 PRS 的尾段。

只输出源/参数定义、次数、字节数、SHA、完整回乘计数与小回执，不输出或保存可重算的大系数。触界时按实际最后 checkpoint 冻结，未返回的新 h、C_D、权核或原单位均不补称已成，不提高限额或重跑。
