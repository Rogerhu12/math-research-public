# 正确 Phi：完整 NV 的第一个 t 首项零支，原二矩、三矩与全值的首次输入

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-29（Asia/Taipei）。

**状态：未执行的唯一首次输入。** 固定新目标是完整 NV 的第一个 t 首项因子
$$
B_1=T+u\sigma=0
\tag{1}
$$
上的同点原二矩、三矩和完整 $N_4$ 值。下面先构造一个原首一 lambda 二次，再只对另两原式短除，取预定三个同 lambda 标量，最后作一次固定顺序的 $\mathbb Q(u,Q)[\sigma]$ gcd。若得到常数，必须把三个标量来源完整合回三个原式，再只清最终实际乘子分母，才登记纯权支持。

预算：数学总 $120$ 秒、$1$ GiB，外层 $135$ 秒。零依赖、只由 root 首派；资源边界、非恒定 gcd、未知纯权支持全部保留，不换顺序、不增预算、不续轮。第二首项因子与整个 Phi 均不在本次排空声明内。

## 1. 新几何入口及原系数环

按已成 [完整 NV 二矩范数与 t 头](../results/R150-appendix-unit211-Phi-zero-corrected-whole-NV-two-moment-norm-and-quadratic-t-head.md)，在同一个原 sigma 上
$$
[t]\bigl(\ell^2N_4(\mathbf V)\bigr)
=2bc(T+u\sigma)\bigl(\ell(3-2\lambda)+2T+2m\sigma\bigr).
\tag{2}
$$
本次只处理第一个完整因子 (1)，不反演第二个因子，不把范数首项的两个根当同一个原根。

范围仍为当前正确 $\Phi=0$、distinct singleton、物理 $D_{\rm phys}\ne0$ 图。取
$$
s=u-1,\quad \delta=1-Q,\quad
L=Q-2(u-1)(u-2),\quad
\ell=L/Q,\quad m=u-\ell,
$$
$$
M=\ell(2u-\ell Q)-u^2=4bc\delta,\quad M_n=QM,
$$
$$
T_0=2u-\ell Q-2u^2=-Q-4s,\quad
J=2u(1-u)+\ell Q,\quad J-Q=-4s^2,\quad P_{02}=2s\ell Q.
$$
只使用当前旧已付纯权
$$
uQ\delta s(Q+4s)L M_n(2\ell-1)
$$
及正确原等权审计所支付的 m 分子。没有引用撤回的 wrong-Rbar 单位或 W 的 $\Phi^{-1}$。不倒 $\sigma,D,V_2,V_3$ 或任何本次新头。

## 2. 原恢复、两个矩与完整 NV 的小式

令 $T=-u\sigma$。保完整原 $E_0,N_0,P_1$ 仿射恢复：
$$
E=\frac{P_{02}(T+\ell)}{T_0},\qquad
f=\frac{P_{02}\lambda-QE+sT_0}{J-Q},
$$
$$
\mathcal V=f+bc\,t-E,\qquad
A_1=2f-2\mathcal V+2bc\,t=2E,\qquad
W_1=T_0/2+2uf.
\tag{3}
$$
所以 f 对 $(\lambda,\sigma)$ 仿射且不依赖 t。原
$$
x=\frac{(u-\ell Q)\mathcal V-mW_1}{M},\qquad
y=\frac{\ell W_1-u\mathcal V}{M}
$$
及真正四阶 dual Gram 均照原定义恢复。源逐个核分母仅含已付权，保真乘法
$$
(vz)_1=v_0z_1+v_1z_0.
$$
这里 lambda 和 sigma 都是自由几何变量，没有选单个复嵌入。

设 $\rho^2=\delta$、$p=1+\rho$、$q=1-\rho$，
$b=\ell/2+m\rho/(2\delta)$、c 为共轭。原 singleton 比值在 (1) 上严格变成
$$
h=1-p\sigma,\qquad k=1-q\sigma,
\qquad w=\lambda-1+u\sigma.
\tag{4}
$$
因此原值向量 $\mathbf V=(1,w,h,k)$ 有完整等式
$$
\mathbf V=\mathbf 1-\sigma g_0+w e_1,\qquad
g_0=(0,0,p,q),\quad e_1=(0,1,0,0).
\tag{5}
$$
取
$$
A_\lambda=2\lambda^2-2\lambda+1,\quad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1,\quad
V_2=2u-\ell Q,\quad V_3=2V_2-uQ.
$$
原第二、第三移位矩完整等于
$$
E_2=b(h-1)^2+c(k-1)^2-A_\lambda
    =V_2\sigma^2-A_\lambda,
$$
$$
E_3=b(h-1)^3+c(k-1)^3-B_\lambda
    =-V_3\sigma^3-B_\lambda.
\tag{6}
$$
于是有真正原首一二次
$$
q_\lambda=\lambda^2-\lambda+\frac{1-V_2\sigma^2}{2}
          =-\frac12E_2.
\tag{7}
$$
(7) 的首项是常数 1；没有倒 $V_2$，其整个零面仍在图内。

为给完整 NV 的独立小原来源，记这里
$$
N=N_4(\mathbf V)
$$
是未乘 $\ell^2$ 的完整原二次型。令
$$
\mathcal E_0=2W_1-T_0-4uf,\qquad
n_0=N_4(g_0)-2\lambda P_{02}.
$$
真 dual 乘法直接给
$$
\begin{aligned}
N_4(e_1)&=4(f-u),\\
\operatorname{Pol}_{N_4}(\mathbf1,e_1)&=2(u-2f),\\
\operatorname{Pol}_{N_4}(\mathbf1,g_0)&=T_0+\mathcal E_0,\\
\operatorname{Pol}_{N_4}(g_0,e_1)&=-2\mathcal E_0 .
\end{aligned}
\tag{8}
$$
展开 (5)，得到完整原恒等式
$$
\begin{aligned}
N={}&2\lambda P_{02}\sigma^2+4(f-u)w^2-T_0\sigma+2(u-2f)w\\
&+\sigma^2n_0+(2\sigma w-\sigma)\mathcal E_0 .
\end{aligned}
\tag{9}
$$
(3) 的原恢复使 $\mathcal E_0=n_0=0$。源直接从完整 Gram 返回这两式及原 P1 jet，并独立返回 (8) 和完整 $N_4(\mathbf V)$ 对 (9) 的相等。故在本支，
$$
\boxed{
N=2\lambda P_{02}\sigma^2+4(f-u)w^2-T_0\sigma+2(u-2f)w.
}
\tag{10}
$$
这确实不含 t，且 $(\lambda,\sigma)$ 总次数至多三。没有把 NV 的一个分量或最高项代替完整 N，也没有使用新几何头的逆。

## 3. 新的同 lambda 三个标量与完整原乘子

只将 (6) 的第三矩和 (10) 各除以首一 (7)，完整普通返回
$$
E_3=a_H(\sigma)+b_H(\sigma)\lambda+Q_Hq_\lambda,
$$
$$
N=a_V(\sigma)+b_V(\sigma)\lambda+Q_Vq_\lambda.
\tag{11}
$$
系数为旧已付权环上的 sigma 多项式，$Q_H,Q_V$ 也保为完整原商。源逐项返回 (11)，不把某个 lambda 一次系数当单位。

写 $q_\lambda=\lambda^2+q_1\lambda+q_0$。固定三个新必要标量为
$$
n_H=a_H^2-q_1a_Hb_H+q_0b_H^2,\qquad
c=a_Hb_V-a_Vb_H,\qquad
n_V=a_V^2-q_1a_Vb_V+q_0b_V^2.
\tag{12}
$$
例如取 $p_H=a_H-q_1b_H-b_H\lambda$、$p_V$ 同理，就有
$$
\begin{aligned}
n_H&=p_HE_3+(b_H^2-p_HQ_H)q_\lambda,\\
c&=b_VE_3-b_HN+(b_HQ_V-b_VQ_H)q_\lambda,\\
n_V&=p_VN+(b_V^2-p_VQ_V)q_\lambda.
\end{aligned}
\tag{13}
$$
三个式子都对全部原 $(\lambda,\sigma)$ 坐标返回；$b_H=0,b_V=0$ 等降头面全部保留。这里仅取必要条件，未把独立范数为零宣布为原同根充分性。

## 4. 唯一固定 gcd 与最终三个原式返回

固定顺序为
$$
(n_H,\ c,\ n_V).
$$
仅在计算域 $\mathbb Q(u,Q)[\sigma]$ 作一次 Euclid 链。每次完整短除相乘返回，每次扩展 gcd 都返回原标量 Bézout；规范化的逆只属于这个计算域，不宣其纯权分子在物理图为单位。得到常数时立即停止，不接另一个目标。

设最终 gcd 为 $g(\sigma)$。将完整三个标量 Bézout 与 (13) 真正合并，并代 $q_\lambda=-E_2/2$，得到
$$
g=\Omega_2 E_2+\Omega_3 E_3+\Omega_N N.
\tag{14}
$$
进一步将三个原式各自已付分母运输到 $\Omega_i$，对其三个原分子得到完整普通身份。**只在完成这一步后**才取三个最终乘子与 g 的实际纯权分母 LCM。清分母后再约全部三个真实原乘子的共同多项式，同时对右端作精确除法并完整乘回。最后只剥已经支付的物理纯权因子，并再次返整个原多项式身份。

因此：

- 若最后是常数 1，才排整个 (1) 原支。
- 若最后是非恒定纯权 C，得到 $C(u,Q)=0$ 的必要支持；整 $C=0$ 保留。
- 若仍含 sigma，得到该完整必要多项式；其头零和全部剩余原纤维都保留。
- 若三个标量全零，准确登记这一结果，不接别的矩阵或正幂目标。

这不是从泛域 gcd 为 1 直接宣整原图空。中间所有未付纯权极点都由实际原终端身份保留，允许其最终合法约消；不靠小分母、泛型维数或模点推空。D、sigma、lambda 和其他原条件均未被除去；完整原 N1、三个均值、NS/PS、个别值、另一 t 头仍在原系统中。

## 5. 来源与去重边界

这是一个新原首项零支的同点输入。它不调用：

- 两个冻结 Q 主分量的旧矩阵、后续轮或轴比较；
- 旧加权六式及 Vlow 的投影；
- 已成两个 odd N/P—NV 交叉或其 t 十次 cofactor；
- 任何旧首项/参数 proof gate。

必要原恢复采用显示式 (3)；完整 Gram 和 N4 均在本源重新定义，用于这个新头支的真正原值返回。没有源码依赖、历史 JSON、载荷或片段恢复。

源 basename：

    2026-11-28-unit211-Phi-zero-corrected-first-NV-t-head-original-moments-and-value-8542.py

源 Git blob：

    e362142779557f1aba8f349ac6c39b7135ab9acd

源 SHA256：

    05f9b72e900b1176ae1dc765786841fa01da8b6dc474ba407d52c3df7f3b4d89

源 $14478$ B。纯 profile 小输出，不输出大系数。本文不预报任何 gcd、纯权 cover、不可约性、排空或点界；必须以唯一实际完整回执为准。
