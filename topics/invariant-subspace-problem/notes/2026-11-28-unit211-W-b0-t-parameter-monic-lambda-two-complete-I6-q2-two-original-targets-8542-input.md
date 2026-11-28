# 新输入：整个 W/b0 的 t 参数首一 lambda 二次、完整 I6 与两条原 t 标量

- 会话：Astra-ISP-8542378f-20261127。
- 日期：2026-11-28（Asia/Taipei）。
- 状态：未执行；只交冻结源码与完整新输入定义。
- 源：[2026-11-28-unit211-W-b0-t-parameter-monic-lambda-two-complete-I6-q2-two-original-targets-8542.py](2026-11-28-unit211-W-b0-t-parameter-monic-lambda-two-complete-I6-q2-two-original-targets-8542.py)。
- 源 blob：2f7fd85b7345f8c41747669526ffcf88d9b83acc。
- 源字节数：16151。
- 源 SHA256：4e6ac873561f4c65491899d2f5edac279e7e44b10057cd86cc9991cbec3bb402。
- 资源：唯一首次 180 秒 / 4 GiB，外层 195 秒；自含、零依赖。
- 新目标：在原 $t$ 参数下完整形成首一 $\lambda^2$、原 $I_6$ 十二行二列及其原 $q_2$ 加强，然后只取两条新的同 $\lambda$ 原标量。没有旧目标续算，没有预报新标量非零或整个 b0 排空。

## 1. 范围与此前尚未执行的新来源

只在当前正确 W、distinct-singleton、物理 $D\ne0$、$b_0=0$ 的已付原权图。完整理论见[整个 b0 的 t 参数首一 lambda 二次](../results/R150-appendix-unit211-W-entire-b0-original-t-parameter-monic-lambda-two-and-exact-I4.md)，本次把其必要定义直接用于真正新的完整原值输入。

这与旧 $(\lambda,f)$ 的 $q_f$ 两列、逆权 $\nu$ 投影、交叉头 G5、4×5 同 h 恢复、C2/Loww、冻结 PRS 都是不同输入。源不导入或执行这些旧算法，也不重新展开它们的证明乘子。新三均值头的理论已有显示原恒等式，本次不把重现它单独设为审计门；需要的系数直接服务于后面的完整 $N_1$/NS/PS 和新标量。

## 2. 全权图与一般 W 的 Phi 项

沿原逆权坐标定义

$$
e=u-1,\quad s=2u-1,\quad d=u\nu-s,\quad r=s-\nu,
$$

$$
k=2r/d,\quad Q=2er/d,\quad
\ell=u\{\nu^2-(u+1)\nu+s\}/r,\quad m=u-\ell,
$$

$$
\delta=1-Q,\quad M=\ell(2u-\ell Q)-u^2=4bc\delta.
$$

仍用原

$$
T_0=2u-\ell Q-2u^2,\quad
J=2u(1-u)+\ell Q,\quad P_f=T_0(J-Q),
$$

$$
\Phi=T_0+4u-4+Q,\quad
P_{02}=(2-3u)(2u-\ell Q)-Qu+2u^3.
$$

当前 b0 上 $A_*=4uQ-J=uQ(\nu+2)$ 已付，置

$$
\kappa=uQ\ell/A_*,\quad T=\kappa(2\lambda-3).
$$

新坐标的准确同点恢复为

$$
f=\frac{P_{02}(T_0-2\kappa Q)\lambda
+eT_0^2-QP_{02}(\ell-3\kappa)-bcQ\Phi t}{P_f},
$$

$$
V=\frac{Jf-\lambda P_{02}-eT_0+bcQt}{Q},\qquad
W_1=T_0/2+2uf.
\tag{1}
$$

源实际核完整原 $P_1$ 以及

$$
\lambda P_{02}=Jf-QV+bcQt-eT_0,\qquad
T=-\ell+\frac{T_0(f-V)+bc(T_0-\Phi)t}{P_{02}}.
\tag{2}
$$

没有把一般 W 的 $-\Phi$ 项换成 Phi 零支的公式。$f$ 的 $t$ 系数准确为 $-bcQ\Phi/P_f$，是旧单位，故与原 $(\lambda,f)$ 图双向。

程序的已付支持按名字逐一记录：$u,e,s,d,r,\nu,\nu-1,Q,\delta,bc,M,\ell,m,P_{02},P_f,\Phi,A_*,2\ell-1$ 的原分子。每个出现的实际系数分母都必须完全由这些支持整除；未付分母会直接使该新输入停止，不会静默倒置。$2\ell-1$ 准确引用[整个 W/Lhalf 完整原排除](../results/R150-appendix-unit211-W-entire-Lhalf-complete-original-exclusion.md)，而非早期 F101 cover。

## 3. 真 Gram 与完整三均值头

使用

$$
x=\frac{(u-\ell Q)V-mW_1}{M},\quad
y=\frac{\ell W_1-uV}{M},\quad
A_1=2f-2V+2bct.
$$

在完整偶奇扩张 $\rho^2=\delta$ 中取

$$
b=\ell/2+m\rho/(2\delta),\quad c=\bar b,\quad
p=1+\rho,\quad q=1-\rho,\quad X=x+\rho y,\quad Y=\bar X.
$$

四行原 Gram 与 dual 乘法直接构造；一阶分量为 $(vw)_1=v_0w_1+v_1w_0$。源完整计算 $d,DK(d),E_0,E_1,E_B,E_C$，核原 $E_0=0$ 与

$$
2\mathcal R+E_1-bE_B-cE_C=0,
$$

$$
\mathcal R=4(f-u)(V-f)+bct^2+
t\left(4bcu-\ell V+\frac{m}{2\delta}(T_0+4uf-2V)\right).
\tag{3}
$$

$E_1$ 独立保留，不用 $E_1=E_W$ 替换。

固定原 $t$、只看 $f,V$ 的二次头。源由真正 $X$ 的线性系数

$$
X_f=-2mu/M+\rho(2\ell u/M),\qquad
X_V=(u-\ell Q)/M-\rho(u/M)
$$

构造 $(-2X_f^2+4X_f,\,-4X_fX_V+4X_V,\,-2X_V^2)$ 的偶奇行，与 $\mathcal R$ 的 $(-4,4,0)$ 合成 $H$。这同时核四个原 $V,W_1$ 导数系数的准确身份，不调用旧三规则。

同点头为

$$
\det H=32uQ(2\ell-1)/M^2,
$$

其逆的九个矩阵坐标实际乘回。令

$$
C=\begin{pmatrix}-1/2&\ell/2&m/2\\0&1&0\\0&0&1\end{pmatrix},
\quad
\gamma=\frac{(J^2,-2JQ,Q^2)}{P_{02}^2}H^{-1}C.
$$

程序只用这些纯权乘子直接形成

$$
q_\lambda=\gamma(E_1,E_{B,e},E_{B,o})^t
=\lambda^2+q_1(t)\lambda+q_0(t),
\tag{4}
$$

完整核 $\lambda^2$ 系数为 1、$\deg_tq_1\le1$、$\deg_tq_0\le2$。没有反演新的单式头或 $t$ 首项。

## 4. 完整原 I6 与 b0 必要 q2

源从同一真 Gram 直接计算

$$
N_4(v)=2\tau(dv^2)-F_2\tau(v^2)-4\tau(v)\tau(dv)
+2F_2\tau(v)^2+\tau(vDKv),
$$

以及完整中心三次 $P_2$。原 $N_0=2\lambda P_{02}$、三次 jet $3wP_{02}$ 实际核回；极化式

$$
N_1=N_4(v_0+v_1)-N_4(v_0)-N_4(v_1)-4\lambda wP_{02}
$$

完整保留。两个 singleton 的 $N/P$ 都直接从原行算出并核共轭，形成完整加权 NS、PS。它们未被最高部或旧 compact 量替代。

原输入七式按固定顺序为

$$
F=(E_1,E_{B,e},E_{B,o},N_1,NS,PS,q_2).
\tag{5}
$$

最后一个仅为当前 b0 的完整原值必要式。记

$$
D=\ell(2\lambda^2-2\lambda+1)-T^2,\quad
C_*=A_*m^2+J\delta\ell^2,
$$

$$
a_d=M\ell^2Q(3-4\lambda)+MA_*T^2
+2MuQ(3-2\lambda)\ell T+DC_*,
\qquad q_2=2a_d/\ell.
\tag{6}
$$

其原来源已刊：$b_0=0$ 时 $C_4=mD\ell q_2$，当前物理 $mD\ell\ne0$，故全部原物理解必须满足 $q_2=0$。本次不重新跑旧值投影，不把 $q_2$ 的头当单位；$q_2$ 的全部 $\lambda$ 降次纤维保留。

$(F_1,\ldots,F_6)=I_6$ 是完整六原式；$J_7=I_6+(q_2)$ 只是对当前全物理原系统的必要加强，未宣称它包含所有个别 N/P 与 NV 条件。

## 5. 完整十二/十四行二列及其原乘子

对 (5) 每一式只用首一 (4) 作普通除法：

$$
F_i=Q_iq_\lambda+r_i,\qquad
r_i=A_i(t)+B_i(t)\lambda.
\tag{7}
$$

原乘子为

$$
\tau_i=e_i-Q_i(\gamma_1,\gamma_2,\gamma_3,0,0,0,0).
$$

源每次完整核 $\tau_iF=r_i$。另完整核

$$
\lambda r_i-
\{-q_0B_i+(A_i-q_1B_i)\lambda\}=B_iq_\lambda
\tag{8}
$$

及对应七原乘子 $\lambda\tau_i-B_i\gamma$。

前四式给八行精确 $I_4$；前六式给十二行精确 $I_6$；全部七式给十四行 $J_7$，均在首一环境

$$
A_W[t][\lambda]/(q_\lambda)
$$

的两个自由坐标 $(1,\lambda)$ 中。自由性只指这个首一环境，不指原方程商。

四原二次及 $q_2$ 的余式次数分别满足 $(\deg_t A_i,\deg_t B_i)\le(2,1)$；完整 NS/PS 余式满足 $(3,2)$。程序将逐行核验这些新界，而不先假设某个余式非零。

## 6. 只取两个新原同 lambda 标量

预先固定两对 $(q_2,N_1)$、$(q_2,NS)$，取

$$
H_{ij}=A_iB_j-A_jB_i
=B_jr_i-B_ir_j
=\sum_{\ell=1}^7
(B_j\tau_{i\ell}-B_i\tau_{j\ell})F_\ell .
\tag{9}
$$

新 $t$ 次数先验上界分别为 $3$、$4$。这些是同一个 $\lambda$ 的必要标量，没有把不同根的投影拼在一起。若其中一式恒零，则准确登记零式和原组合，不借此生成新权条件。

对非零式，只取消**全部七个实际原乘子**的共同因子：

1. 只清乘子的已付纯权分母，得到七个普通多项式乘子；
2. 取它们的真共同因子 $h$，每个乘子都精确除以 $h$ 并乘回；
3. 直接重新计算七个新乘子作用于完整原七式所得的标量，核其与旧标量的 $h$ 倍关系；
4. 核该新标量没有 $\lambda$、实际分母仍只含旧已付权支持；
5. 最后只清该原分母和剥旧已付支持，重新返回完整七原组合。

取消 $h$ 不是把一个原方程除以未付因子：最后的新七原乘子本身在原环内，完整普通多项式身份直接成立。因此 $h=0$ 的所有纤维仍满足新必要标量。未知纯 $u,\nu$ 内容、新 $t$ 首项及它们的整个零面全部保留。

源不执行任何新的多变量 gcd 判空、纯权投影、t-resultant、全因式分解或旧失败算法。两条标量只登记实际次数、项数、SHA 和原返回计数。

## 7. 唯一首次的边界

源码从开始设置绝对 180 秒和 4 GiB 硬界，没有嵌套脚本或重置 deadline。只有 self SHA 读取，不写系数载荷、矩阵缓存或参数片。

若执行只完成首一式、完整原值或一条新标量，就仅按最后真实标记登记；不增加预算、不重播同源、不把外层 success 当成内层全成功。任何尚未实际形成的十二/十四行或标量不会预记为完成。

本源不宣称整个 b0 或 W 为空，也不提出新的权点数或未规范化算子计数。后继方向只由此次真实原目标决定。
