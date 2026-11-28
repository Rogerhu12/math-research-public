# 新输入：正确 Phi 整 alpha 零图的原 V 首一二次与完整值两列

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

**尚未执行。** 首次总预算 $120$ 秒 / $1$ GiB，外层 $135$ 秒。
源自含、零文件依赖，不调用旧 B、C76、Phi 首头或已冻结 GB。
源 SHA-256：58cab31654894e8b4a4309f1c6b69619f5ee19591f74256f3128dd2026a4f025。
建议 basename：
2026-11-28-unit211-Phi-zero-true-whole-alpha-zero-monic-V-two-8542.py。

## 1. 当前准确范围与没有借用的单位

仅当前正确原 $\Phi=0$、$D_{\rm val}\ne0$ 图。
原 intrinsic 条件支付 $Q,\delta=1-Q,u-1,L,K,M_n$，其中

$$
L=Q-2(u-1)(u-2),\quad K=Q+4(u-1),\quad
\ell=L/Q,\quad M_n=2uL-L^2-u^2Q.
$$

独立真实原零基点 mean 排除支付 $u$。
[整个正确 t 零支](../results/R150-appendix-unit211-Phi-zero-true-entire-tzero-original-exclusion.md)
支付 $t$；[整个正确 f=u 支](../results/R150-appendix-unit211-Phi-zero-true-entire-fu-original-exclusion.md)
支付 $\eta=f-u$；
[整个正确 A 零曲线](../results/R150-appendix-unit211-Phi-zero-true-Azero-second-linear-and-whole-curve-exclusion.md)
支付 $A=4(u-1)^2-Q$。

本次尚未假定 $m=u-\ell$ 或 $\theta=u-\ell Q$ 在一般 Phi 图非零。
下面在新 $\alpha=0$ 整支内，从同一点原恒等式支付它们。
不使用旧错误 Rbar 的首头，不借用 W 的等权或 $H_{\rm old}$ 支。

## 2. 自由权原 R 身份给全 alpha 零图

记
$$
M=\ell(2u-\ell Q)-u^2=4bc\delta,\quad
T_0=2u-\ell Q-2u^2,\quad V=bX+cY,
$$
$$
R_w=2u(1-u)-uQ+(2u-1)\ell Q,\qquad
\alpha=4\delta(f-u)-\theta t.
$$

[已刊 alpha/chi 原坐标稿](../results/R150-appendix-unit211-W-global-original-alpha-chi-polynomial-coordinates.md)
的 §1(2)、§2(4)–(7) 是 W 代入之前的自由权恒等式。
只引用这些已成完整原身份，不重新运行其通用小源。
其正确
$\mathcal R=\overline R_{\rm true}/Q^2$
满足，在原 $E_0=0$ 时，
$2\mathcal R+E_1-EW=0$。
置 $R_4=4\delta\mathcal R$，由这些自由身份直接得

$$
\theta R_4
=\alpha\{4\theta(V-f)-Mt\}
-2tR_w\{2m(f-u)+\ell\theta\}.
\tag{1}
$$

Phi 的新权公式准确给

$$
R_w=-(u-1)A,
\tag{2}
$$

故本图 $R_w$ 为真原权单位，来源是上节整个正确 A0 排除，
不是 W 中 $R_w=-ue^2H_{\rm old}/\overline V$ 的支付。

在整个 $\alpha=0$ 原支上，(1) 和 $tR_w\ne0$ 迫

$$
2m\eta+\ell\theta=0.
\tag{3}
$$

又纯多项式身份

$$
t(2m\eta+\ell\theta)+\ell\alpha
=2\eta(mt+2\ell\delta)
\tag{4}
$$

与 $\eta\ne0$ 给 $mt=-2\ell\delta$。
所以 $m$ 在此支为单位；$\theta t=4\delta\eta$ 也支付 $\theta$。
整个原支唯一满足

$$
\boxed{\quad t=-\frac{2\ell\delta}{m},\qquad
f=u-\frac{\ell\theta}{2m}.\quad}
\tag{5}
$$

这些新分母的零面已经由 (1)–(4) 完整排除，不是只取泛型开图。
未外推 $m,\theta$ 到 $\alpha\ne0$。

## 3. 原 V 坐标恢复和实际均值头

令
$$
W_1=(T_0+4uf)/2,\quad
x=\frac{\theta V-mW_1}{M},\quad
y=\frac{\ell W_1-uV}{M},
$$
$$
\rho^2=\delta,\quad X=x+\rho y,\quad Y=x-\rho y,
\quad p=1+\rho,\quad q=1-\rho.
$$

取原权
$b=(\ell+m\rho/\delta)/2$、$c=(\ell-m\rho/\delta)/2$，
并恢复原 Gram
$A_1=2f-2V+2bct$、
$r=X-(1-\ell)p-ct$、
$s_{\rm G}=Y-(1-\ell)q-bt$。
从原 $N_0/P_1$ 取

$$
\lambda=\frac{Jf+bcQt-QV-(u-1)T_0}{P_{02}},
\quad
T=\frac{T_0A_1}{2P_{02}}-\ell,\quad
P_{02}=2(u-1)L,\quad J=2u(1-u)+L.
\tag{6}
$$

全部恢复量对 $V$ 至多一次，权分母仅为已付单位。
源实际返回 $E_0=0$、$\mathcal R=0$、$P_1=0$ 和两条线性恢复；
原均值直接通过四行 Gram 和真正双点乘法构造，不引入旧紧凑公式。

具体原
$$
E_B=-(1-\ell)p^2+2(p+2f-u)X-2p d_1
+ct(t+2u-2p-2Y)-2X^2,\quad
d_1=2f-V-(1-\ell)u.
$$
其 $V^2$ 唯一来自 $-2X^2$。
因为 $[V]X=(\theta-u\rho)/M$，
对 $E_{\rm Bo}=(E_B-E_C)/(2\rho)$ 得

$$
\boxed{\quad [V^2]E_{\rm Bo}=\frac{4u\theta}{M^2}.\quad}
\tag{7}
$$

上节和原零基点 mean 支已付 (7) 的整个头。
源将从实际 raw Gram 计算该头并完整比较，再定义

$$
q_V=\frac{E_{\rm Bo}}{4u\theta/M^2}
=V^2+q_1(u,Q)V+q_0(u,Q).
\tag{8}
$$

因此整个当前 $\alpha=0$ 图有同一个原首一二次环境；
没有未处理的新 V 头零纤维。

## 4. 新完整原值在同一点两列环境

在
$$
B=A_{\rm weight}[V]/(q_V)
$$
中每次乘法都实际返回
$ab=\operatorname{rem}(ab)+c\,q_V$ 的两个低次坐标。
这里 $A_{\rm weight}$ 只倒前述纯权单位，
不倒几何 $D_{\rm val}$、其范数或任何新的原值首项。

重新用完整双点原 Gram 构造

$$
E_{\rm Be},\quad N_1,\quad NS,\quad PS.
\tag{9}
$$

$N_1$ 是完整 $N_4$ 对 $g_0,g_1$ 的双线性极化；
NS/PS 是完整两 singleton 行的加权 $N_4/P_2$ 差。
源实际核 $F_2=2f$、$N_4(g_0)=2\lambda P_{02}$、
完整原值的奇 $\rho$ 系数为零。
没有以 $\Phi$ 倍数或部分分量替代原 $N_4$。

(9) 每项的两列分母都必须通过上述纯权支持检查；
失败就如实保留，不扩大白名单。
$B$ 是首一多项式定义的实际必要代数；
不假定原理想商自由，取其它物理单位开集也不据此宣称仍有限自由。

## 5. 三个真正新的固定标量

分别取
$(E_{\rm Be},N_1)$、$(E_{\rm Be},NS)$、$(E_{\rm Be},PS)$。
若两行为 $a_0+a_1V$、$b_0+b_1V$，先用原已付权分母清
$(b_1,-a_1)$，只精除这**两个实际乘子**的完整公共多项式因子 $g$。
所得多项式 $\mu,\nu$ 全坐标返回

$$
\mu(a_0+a_1V)+\nu(b_0+b_1V)=C(u,Q).
\tag{10}
$$

因此 $g=0$ 的整权纤维也在 (10) 中；
没有将原方程除以未付 $g$。
最后 $C$ 只剥已经支付的权因子，其余完整纯权零集保留。
若两 V 系数均为零，保留两个完整原常数行，不除零。

首次结果仅按实际三个原标量报告。
非零必要曲线、泛域秩或函数域单位本身不等于整个 alpha0 排空；
只有实际常数单位返回才登记整支关闭。
所有其它原值方程在同一点继续保留。

## 6. 执行与归档

零文件依赖，Python 3.12.14 / python-flint 0.9.0。
总 $120$ 秒 / $1$ GiB；没有前缀重置计时。
仅输出各新原阶段的次数、项数、哈希和小回执；
不输出或存储大系数、矩阵、编码或分片。
本源不重跑已有 B34/40、四 fu、A0、旧 Phi scalar 或冻结 GB。
