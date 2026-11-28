# 正确 Phi：同一原 sigma 的两个 N/P—NV 五次交叉及一个原 t 十次式

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-29（Asia/Taipei）。

## 1. 实际结论与范围

在当前正确 $\Phi=0$、distinct singleton、物理 $D_{\rm phys}\ne0$ 原图，完整个别 N/P 的奇部、完整 $N_4$ 值和同一个原第二矩给出两个新的必要五次式。将这两个式子分别返到真正三个原均值，再与已刊的原 $N_1$ 余式作一个固定 cofactor，实际得到非零必要式
$$
C_{10}(u,Q,t)=0,
\qquad
(\deg_u,\deg_Q,\deg_t)C_{10}=(82,51,10).
\tag{1}
$$
其总次数为 $97$，共有 $26511$ 项。程序使用既定有理常数首一规范，准确 profile SHA256 为
$$
\texttt{d8ca679a943eb517247f5c77bca216fd51a98c44561b51cfa192a330fb6a92c0}.
$$
它的实际最高 $t$ 系数
$$
H_{87}(u,Q)=[t^{10}]C_{10}
\tag{2}
$$
满足双次 $(82,43)$、总次数 $87$、$2162$ 项，profile SHA256 为
$$
\texttt{6deba5686625349489ae386335d69f44c67bd69fa0a47a340cd56b144481b799}.
$$
本次没有对 $H_{87}$ 作因式、互素或单位判断，整 $H_{87}=0$ 纤维继续保留。这里没有得到原图排空、额外有限点界或既有公共权曲线界的降低。

数学源唯一实际运行是 [run 46164341750](https://github.com/Rogerhu12/math-research-public/actions/runs/46164341750)，job 141038441104。内层退出码为 $0$；本文依实际完整七条数学记录及驱动回执，不由外层工作流状态推论。

## 2. 原系数环与同点恢复

记
$$
s=u-1,\quad \delta=1-Q,\quad
L=Q-2(u-1)(u-2),\quad
\ell=L/Q,\quad m=u-\ell,
$$
$$
M_n=2uL-L^2-u^2Q,\qquad M=M_n/Q=4bc\delta .
$$
只使用当前已付纯权
$$
uQ\delta s\bigl(Q+4s\bigr)L M_n(2\ell-1)
$$
及当前物理图已独立支付的 $m$ 分子。$m$ 的使用限于已刊正确等权静态审计范围。没有借用 W 的 $\Phi^{-1}$，也没有沿撤回的 wrong-Rbar 链恢复任何单位。

以 $\mathcal V=bX+cY$ 表示源中的 V 变量。按[全 t 原三均值模型](R150-appendix-unit211-Phi-zero-corrected-whole-t-parameter-three-mean-generators-and-monic-lambda-cubic.md)，
$$
\lambda=\frac{Jf-Q\mathcal V+bcQt-sT_0}{P_{02}},
\qquad
T=-\ell+\frac{T_0}{P_{02}}(f-\mathcal V+bct).
\tag{3}
$$
这里 $T_0=-Q-4s$，$J-Q=-4s^2$，$P_{02}=2sL$。三个原均值
$$
\mathbf E=(\mathcal R,E_{Be},E_{Bo})
$$
的 $(f^2,f\mathcal V,\mathcal V^2)$ 头满足
$$
\det H=\frac{32uQ(2\ell-1)}{M^2}.
\tag{4}
$$
因此原三条二次规则只反演已付权。所有普通多项式身份都在这个已付系数环中解释；三生成元 $1,f,\mathcal V$ 不假定自由。

下面的二矩变量与完整原 singleton 值使用同一个 $\sigma$。设
$$
A_\lambda=2\lambda^2-2\lambda+1,\quad
D=\ell A_\lambda-T^2,\quad A_0=1+T/\ell,
\qquad q=M\sigma^2-D.
\tag{5}
$$
原值恢复为
$$
h=A_0+(m/\ell-\rho)\sigma,\qquad
k=A_0+(m/\ell+\rho)\sigma,\qquad \rho^2=\delta .
$$
由原第二矩，$q=\ell E_2$。这个二次式保两个根，并在 $D=0$ 保完整双根结构；下面的身份既不倒 $D$，也不要求先乘 $D$ 才取得原来源。

## 3. 两个完整 odd 原误差和完整 NV

从真实 dual 乘法、原 Gram 及完整原 $N_4,P_2$ 定义，记
$$
N_o=\frac{N_4(g_B)-N_4(g_C)}{2\rho},
\qquad
P_o=\frac{P_2(g_B)-P_2(g_C)}{2\rho}.
$$
完整 singleton 误差的奇部是
$$
E_N=N_o+4\lambda P_{02}(A_0+m\sigma/\ell)\sigma,
$$
$$
E_P=P_o+P_{02}\left(3(A_0+m\sigma/\ell)^2\sigma+\delta\sigma^3\right).
\tag{6}
$$
这些来自同一点的两个 singleton 原值，未以加权 NS/PS 代替。定义
$$
\begin{aligned}
a_N&=N_o+\frac{4\lambda P_{02}mD}{\ell M},&
b_N&=4\lambda P_{02}A_0,&
c_N&=\frac{4\lambda P_{02}m}{\ell M},\\
a_P&=P_o+\frac{6P_{02}A_0mD}{\ell M},&
b_P&=P_{02}\left(3A_0^2+
 \left(\frac{3m^2}{\ell^2}+\delta\right)\frac D M\right),\\
c_P(\sigma)&=\frac{6P_{02}A_0m}{\ell M}
 +\frac{P_{02}(3m^2/\ell^2+\delta)}M\,\sigma .
\end{aligned}
\tag{7}
$$
直接逐 $\sigma$ 系数展开即得
$$
E_i=a_i+b_i\sigma+c_i(\sigma)q,\qquad i=N,P.
\tag{8}
$$

同时，按[一般缩放完整 N4 三短式](R150-appendix-unit211-general-scaled-entire-N4-three-compact-identities.md)，
$$
\mathcal N=\ell^2N_4(\mathbf V)=Z_0+Z_1\sigma+Z_2\sigma^2.
$$
为明确全值而非分量来源，置 $c_\lambda=3-2\lambda$、
$w=\lambda-1-T$、$W_1=bpX+cqY$，三个系数为
$$
\begin{aligned}
Z_0={}&\ell^2A_1+4\ell^2(1-2\lambda)f+2\ell fD
 +2\ell uw(\ell c_\lambda+T)\\
&+2\mathcal V(\ell^2+\ell c_\lambda T+T^2)
 +2bc\,t(T^2-\ell^2),\\
Z_1={}&2(\ell c_\lambda+2T)(u\mathcal V-\ell W_1)
 -2\ell Mw+4bc\,mTt,\\
Z_2={}&2\left((u^2-\ell^2Q)\mathcal V
 -2m\ell W_1-\ell Mf-bcMt\right).
\end{aligned}
\tag{9}
$$
取
$$
a_V=Z_0+DZ_2/M,\qquad b_V=Z_1,\qquad c_V=Z_2/M;
$$
于是完整普通身份是
$$
\mathcal N=a_V+b_V\sigma+c_Vq.
\tag{10}
$$
本次实际源码完整返回 (8)–(10)，包括 P 支的 $\sigma$ 一次商项。没有选取二次式的一个根。

## 4. 新的两个同 sigma 交叉及原来源

定义
$$
C_{N,V}=a_NZ_1-a_Vb_N,\qquad
C_{P,V}=a_PZ_1-a_Vb_P.
\tag{11}
$$
由 (8)–(10)，它们有完全显示的原来源：
$$
\boxed{
C_{i,V}=Z_1E_i-b_i\mathcal N
 +\left(\frac{b_iZ_2}{M}-Z_1c_i(\sigma)\right)q,\qquad i=N,P.
}
\tag{12}
$$
源实际对整个 $\sigma$ 多项式返回这两个身份；所有正次 $\sigma$ 项在精确运算中消去。这里 $D=0$、$Z_1=0$、$b_i=0$ 均没有作为被删图面。它们是原同点必要条件，未把独立范数各自为零解释成同根。

以 $(t,f,\mathcal V)$ 总次数计，$a_N,a_P,a_V$ 至多三次，$b_N,b_P,Z_1$ 至多二次，所以 (11) 至多五次。实际两式都恰为五次：

| 新原式 | 分子 $(u,Q,t,f,\mathcal V)$ 次数 | 分子总次数 | 分子项数 |
| --- | --- | --- | --- |
| $C_{N,V}$ | $(29,17,5,5,5)$ | $36$ | $14513$ |
| $C_{P,V}$ | $(32,20,5,5,5)$ | $40$ | $18263$ |

两分子的 profile SHA256 依次为

    760e94ba0a18d3c5a72858ef0799c2f8fb4709dbc636ed79f599cc736a3f9592
    b92bdc406526270f6057f7599f014776c53de055e7bfd3039ab61a8a3e368dbd

所有分母仅含已付纯权，程序逐项确认。既有 $H=K-2mD\sigma$、两个原矩、原六式及其余完整个别值条件继续保留。以前由 H 与三个值条件得到的低 D 交叉不是本次重算目标。

## 5. 两条普通原均值迹和固定三行来源

对每个 (11)，只用 (4) 的三条原规则降低 $(f,\mathcal V)$ 次数，实际累积并返回
$$
C_{i,V}=r_i\cdot(1,f,\mathcal V)+\tau_i\cdot\mathbf E,
\qquad i=N,P.
\tag{13}
$$
实际两行 $r_i$ 的三个 $t$ 次数均为 $(5,4,4)$；每个 $\tau_i$ 的总几何次数至多三。两条完整普通多项式身份全部返回，未用未经证明的三维矩阵结合律。

令已刊正确原 N1 迹为
$$
N_1=r_0\cdot(1,f,\mathcal V)+\tau_0\cdot\mathbf E.
\tag{14}
$$
此次只用其唯一系数定义，完整三个分子 SHA 与原定义一致，不重做旧 N1、斜率或六行呈示的证明门。对固定三行 $(r_0,r_N,r_P)$ 的后两列取 cofactor。清真实纯权分母后，只约全部三个乘子的共同分子，再完整返三个坐标。本次共同内容实际为常数 $1$。

最后只剥原已付权支持，并将同一倍数运输到全部三个乘子，实际再返
$$
\mu_0r_0+\mu_Nr_N+\mu_Pr_P=(C_{10},0,0).
\tag{15}
$$
最终 $\mu_0,\mu_N,\mu_P$ 的分母均恰为 $1$，其 $t$ 次数分别是 $8,5,5$。固定行次数给
$$
\deg_t C_{10}\le 2+5+5-(0+1+1)=10;
$$
实际最高系数非零，所以次数恰为十。

将 (13)–(15) 合成，有
$$
\begin{aligned}
C_{10}={}&\mu_0N_1+\mu_NC_{N,V}+\mu_PC_{P,V}\\
&-(\mu_0\tau_0+\mu_N\tau_N+\mu_P\tau_P)\cdot\mathbf E.
\end{aligned}
\tag{16}
$$
再代 (12)，得到 $C_{10}$ 对真正三个原均值、原 N1、完整 odd N/P、完整 NV 及同一个第二矩的来源。因而 (1) 是当前整个原图的必要条件。所有共同内容和未知头零面由这些完整身份保留。

## 6. 唯一实际回执与可重现来源

[冻结源及输入](../notes/2026-11-28-unit211-Phi-zero-corrected-same-sigma-odd-NP-full-NV-crosses-8542.py)、
[首次输入说明](../notes/2026-11-28-unit211-Phi-zero-corrected-same-sigma-odd-NP-full-NV-crosses-8542-input.md)、
[实际小回执](../notes/2026-11-28-unit211-Phi-zero-corrected-same-sigma-odd-NP-full-NV-crosses-8542-execution.json)。

源 Git blob：

    b53edcc91babd2931dac68ef482744c6027f20f1

源完整 SHA256：

    fa1029b01d9438a54ff5fc21cc3fed0e0aebf553624e6743d84854b6b1ecf1c4

唯一依赖为已刊完整 Vlow 小源 dec77452e4631b4370e72d1b9491da01e35547b3。其完整 SHA 为

    0800a0f6ba0cad4cc4ddc7a592525c198bcc213bfa36df568ec0e9301b8f4335

只取必要前缀 $7689$ B，SHA 为

    607238e08c402392a599e84cf13764aac341c6b7f0fb34e29c0ea6667c647abe

前缀止于旧 N1 的三个系数 SHA 身份，未进入旧 NS/PS、Vlow 或两八次 cofactor。AST 只删除前缀 START、DEADLINE、resource.setrlimit、signal.setitimer 四条顶层时间/资源赋值，并断言恰为这四条。源最初的总截止一直有效，预算为 $120$ 秒、$1$ GiB、外层 $135$ 秒。

| 实际项目 | 返回 |
| --- | --- |
| run / job | 46164341750 / 141038441104 |
| 源提交 | 2da36c7d9613d54e967be16b713cbde6c9378748 |
| 实际 pull 后提交 | 2200aec6e52df774f005c9da30fffd97eeddf11c |
| 规则读取 UTC | 2026-11-28T16:17:33.527757+00:00，两份 README 未变 |
| 驱动耗时 / 峰值 RSS / 内层退出码 | $4.844514676$ 秒 / $84456$ KiB / $0$ |
| 最后数学记录耗时 | $4.802741693$ 秒 |
| 原普通均值身份 | 两条全式及六余式坐标 |
| 固定 cofactor 与最终规范返回 | 各三个坐标 |
| stdout | $12403$ B，七条数学记录 |

stdout SHA256：

    1049e4386ab5ec5cbaca5cfd8e2b8bfcc4f57051a3a8e5e5c5a236473b0e1ca5

本次保存源码、定义、profile 及小回执，不保存可重算系数载荷。两条旧 Q 主分量内存边界仍冻结；本次未运行其续段、旧轴比较、旧赋值归一或已成加权投影。

## 7. 保留范围

(12) 与 (16) 给新的同原值必要约束，但未给所有原值的充分条件。整 $H_{87}=0$、全部原二次重根与其余原条件继续保留。既有全权有限生成定理与其纤维长度界保持独立，本次不降低它们，也不降低旧公共权曲线总次数至多 $45$ 的界。整 Phi 及普通 ISP 仍未完成。
