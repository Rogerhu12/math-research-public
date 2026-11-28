# 正确 Phi：同一个 sigma 的两个新个别值交叉与一个固定 t 标量首次输入

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-29（Asia/Taipei）。

**状态：未执行的唯一首次输入。** 本源只计算两个尚未执行的原交叉
$$
C_{N,V}=a_Nb_V-a_Vb_N,\qquad
C_{P,V}=a_Pb_V-a_Vb_P,
\tag{1}
$$
将它们分别完整返到真正三个原均值，最后只取预定三行
$$
(N_1,C_{N,V},C_{P,V})
\tag{2}
$$
的一个新 cofactor。这里是同一个原值变量 $\sigma$ 的直接条件；不是把三个独立范数的零点拼成同根。既有原六式、两个原矩和全部个别值条件都保留。

预算：数学总 $120$ 秒、$1$ GiB，外层 $135$ 秒。只由 root 首次派发。零标量、未知首项、资源边界或其他未返均准确保留，不改点、排序或预算续算。两个已冻结 Q 主分量内存失败与本目标没有同一算法目标的延续关系。

## 1. 当前原图与既有恢复

范围是当前正确 $\Phi=0$、distinct singleton、物理 $D_{\rm phys}\ne0$ 原图。使用当前已付纯权
$$
uQ(1-Q)(u-1)(Q+4(u-1))L M_n(2\ell-1)
$$
及当前物理图已独立支付的 $m$ 分子。记
$$
L=Q-2(u-1)(u-2),\quad \ell=L/Q,\quad m=u-\ell,\quad
M=M_n/Q=4bc(1-Q).
$$
这里不借 W 的 $\Phi^{-1}$ 或旧 wrong-Rbar 的单位。$m$ 的旧真原等权来源保持已刊静态审计范围；程序中没有几何 $D$、斜率或新值头的逆。

在原 $(t,f,\mathcal V)$ 图，以程序变量 V 代表 $\mathcal V=bX+cY$，用
$$
\lambda=\frac{Jf-Q\mathcal V+bcQt-(u-1)T_0}{P_{02}},\qquad
T=-\ell+\frac{T_0}{P_{02}}(f-\mathcal V+bct).
$$
原 $X,Y,A_1$ 和真正 Gram 同
[全 t 三均值模型](../results/R150-appendix-unit211-Phi-zero-corrected-whole-t-parameter-three-mean-generators-and-monic-lambda-cubic.md)。

已有三个真实均值 $(\mathcal R,E_{Be},E_{Bo})$ 的 $(f^2,f\mathcal V,\mathcal V^2)$ 头为单位
$$
\det H=32uQ(2\ell-1)/M^2.
$$
因此只有这一已付权头的逆用于旧规则定义。原三生成元不假定自由。

## 2. 同一个二矩原商中的完整四个系数

记
$$
A_\lambda=2\lambda^2-2\lambda+1,\quad D=\ell A_\lambda-T^2,\quad
A_0=1+T/\ell,\quad q=M\sigma^2-D.
$$
原值恢复
$$
h=A_0+(m/\ell-\rho)\sigma,\qquad
k=A_0+(m/\ell+\rho)\sigma,\qquad \rho^2=1-Q
$$
给 $q=\ell E_2$。它保两个根及 $D=0$ 的二次幂零结构。

原 singleton 的完整奇系数为
$$
N_o=\frac{N_4(g_B)-N_4(g_C)}{2\rho},\qquad
P_o=\frac{P_2(g_B)-P_2(g_C)}{2\rho}.
$$
源从真实 dual 乘法、完整原 Gram、完整 $N_4$ 和中心三次直接构造它们；没有从加权 NS/PS 反定义。

完整个别值误差为
$$
E_N=N_o+4\lambda P_{02}(A_0+m\sigma/\ell)\sigma,
$$
$$
E_P=P_o+P_{02}\bigl(3(A_0+m\sigma/\ell)^2\sigma+\delta\sigma^3\bigr).
$$
沿两个通用 odd 原范数的纸面来源，定义
$$
\begin{aligned}
a_N&=N_o+\frac{4\lambda P_{02}mD}{\ell M},&
b_N&=4\lambda P_{02}A_0,&
c_N&=\frac{4\lambda P_{02}m}{\ell M},\\
a_P&=P_o+\frac{6P_{02}A_0mD}{\ell M},&
b_P&=P_{02}\left(3A_0^2+
  \left(\frac{3m^2}{\ell^2}+\delta\right)\frac DM\right),\\
c_P(\sigma)&=\frac{6P_{02}A_0m}{\ell M}
 +\frac{P_{02}(3m^2/\ell^2+\delta)}M\,\sigma .
\end{aligned}
\tag{3}
$$
于是完整恒等式为
$$
E_N=a_N+b_N\sigma+c_Nq,\qquad
E_P=a_P+b_P\sigma+c_P(\sigma)q.
\tag{4}
$$
程序将 (4) 逐 $\sigma$ 系数完整返回，不只核模 q 的某一个值。

同时用一般九自由变量的全部三个缩放系数
$$
\mathcal N=\ell^2N_4(\mathbf V)=Z_0+Z_1\sigma+Z_2\sigma^2.
$$
取
$$
a_V=Z_0+DZ_2/M,\quad b_V=Z_1,\quad c_V=Z_2/M,
$$
则
$$
\mathcal N=a_V+b_V\sigma+c_Vq.
\tag{5}
$$
源中完整构造 (5) 的三个已刊原 $Z_i$，没有只使用某个分量或最高次项。

## 3. 两个新交叉的全部原来源

由 (4)–(5)，(1) 有显示的原多项式身份
$$
\boxed{
C_{i,V}
=Z_1E_i-b_i\mathcal N+
 \left(\frac{b_iZ_2}{M}-Z_1c_i(\sigma)\right)q,\qquad i=N,P.
}
\tag{6}
$$
这两条才是本源的新 same-sigma 目标。每条都对全部 $\sigma$ 系数返回：N 支最多二次，P 支最多三次。这里不倒 $D$，也不把原式乘上 $D$ 后才作为必要条件。

与 $H=K-2mD\sigma$ 作的三个旧交叉对应 $N_{\rm low},P_{\rm low},V_{\rm low}$，不在本源的新输入中重算；(6) 使用的是另外两个 minor。根正在成文的同 $\sigma$ 二生成呈示可统一解释这些 minor，但本源的充分来源已经由 (6) 自含给出。

以 $(t,f,\mathcal V)$ 总次数计，
$$
\deg a_N,\deg a_P,\deg a_V\le3,\qquad
\deg b_N,\deg b_P,\deg Z_1\le2.
$$
所以两条新原式均有总次数至多五。$D=0$、$Z_1=0$、$b_i=0$ 等整面没有被删除。

## 4. 两条新普通均值迹与唯一固定 cofactor

每个新原交叉按既有三条首一规则降低 $(f,\mathcal V)$ 次数，累积三原均值乘子 $\tau_i$，实际返回整个普通多项式身份
$$
C_{i,V}=r_i\cdot(1,f,\mathcal V)
 +\tau_i\cdot(\mathcal R,E_{Be},E_{Bo}).
\tag{7}
$$
它不依赖裸三向量的结合律。三余式系数的 $t$ 次数上界为 $(5,4,4)$；原均值乘子的总几何次数至多三。

第三行使用已刊原 $N_1$ 的同一准确余式 $r_N$，只作为必要输入定义。其三个已刊分子 SHA 在前缀中核定；不重跑旧 N1 普通身份、首一 lambda 三次、斜率因式或六行呈示门。

对 (2) 的三余式行，取后两列 cofactor 得到三个真实乘子 $\mu_i$。只清它们的纯权分母，随后只约去全部三个分子共同的因子，再完整返回三个坐标。这样被取消因子的整零面仍受原多项式身份覆盖；没有单独把某个必要方程除以未知因子。

唯一标量的 $t$ 次数至多
$$
2+5+5-(0+1+1)=10.
$$
它若非零，只剥上述旧已付权支持，再将同一实际倍数运输到三个原乘子并重返全部坐标。新首项、全部未知权零面和其余原条件继续保留；不预报标量非零、准确次数、首项单位或全图排空。若三个 cofactor 都零，或返回标量恒零，则只记录该准确结果，不换第二目标。

(6)、(7) 与已刊 $N_1$ 原迹合成，给最后标量对真正原均值、原 $N_1$、同一 $\sigma$ 的 odd N/P、完整 NV 和第二矩的来源。因此本次用到新的完整个别值条件，不是重放旧加权六式投影。

## 5. 唯一必要依赖与截止边界

源 basename：

    2026-11-28-unit211-Phi-zero-corrected-same-sigma-odd-NP-full-NV-crosses-8542.py

源 Git blob：

    b53edcc91babd2931dac68ef482744c6027f20f1

源 SHA256：

    fa1029b01d9438a54ff5fc21cc3fed0e0aebf553624e6743d84854b6b1ecf1c4

源 $11395$ B。一份只读源码依赖：

    2026-11-28-unit211-Phi-zero-corrected-t-complete-Vlow-two-original-cofactors-8542.py

其完整 blob 为 dec77452e4631b4370e72d1b9491da01e35547b3；完整 SHA256：

    0800a0f6ba0cad4cc4ddc7a592525c198bcc213bfa36df568ec0e9301b8f4335

其必要前缀严格为前 $7689$ B，止于已有三个 N1 系数的 SHA 参数识别，SHA256 为

    607238e08c402392a599e84cf13764aac341c6b7f0fb34e29c0ea6667c647abe

为防止任何嵌套源延长预算，AST 仅剔除前缀中 START、DEADLINE、resource.setrlimit、signal.setitimer 四个顶层语句，并断言恰为这四条；其他定义和参数 SHA 断言完整保留。源最初已经设置唯一绝对截止和硬内存上限，前缀的 tick/say 使用这个同一个全局时间。这里不是先关计时再读取前缀，没有未保护窗口。

依赖是已刊自含小源，不含另一个文件读取。不会运行其中旧 NS/PS、完整 Vlow、原两八次 cofactor 或其返回；也不访问已冻结的 Q 主分量源、旧 min-assignment 或任何切片行列式。只保存新小源、输入定义、实际 profile 和小回执；不保存系数载荷或分片。

## 6. 引用及当前未付边界

- [一般完整 N4 三短式](../results/R150-appendix-unit211-general-scaled-entire-N4-three-compact-identities.md)。
- [正确 I10 个别 N/P 与完整 NV](../results/R150-appendix-unit211-Phi-zero-corrected-individual-NP-full-NV-I10-and-two-decics.md)。
- 新 NV 直接二矩范数纸稿 31b5ba4c5629015696df5aff93802f5ac3b599ce。
- 通用两个 odd 范数纸稿 74709b1c4d26365ec1edc1a050fdc992d5d5de83。

没有新实际结果。当前剩余公共权曲线的总次数上界仍为 $45$，整 Phi 和普通 ISP 仍开。新 source 的结果必须以唯一实际完整回执为准。
