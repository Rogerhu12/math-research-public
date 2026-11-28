# 新输入：正确 Phi 中心 t 坐标的完整 NS/PS、十行二列与新二阶原组合

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-28（Asia/Taipei）。

**状态：未执行。** 唯一首次目标是完整原 NS/PS 的三均值来源、中心首一二次及两条三次两列行，并构造它们的一个固定二阶原组合。没有预报这个组合的非零性、首项单位、有限性或空性。原斜率的两个整零曲线始终保留。

源：[2026-11-28-unit211-Phi-zero-corrected-centered-t-original-NSPS-ten-by-two-8542.py](2026-11-28-unit211-Phi-zero-corrected-centered-t-original-NSPS-ten-by-two-8542.py)。

Git blob 5ebffd4768a82d2244deda197ec501d5b67ea5ca；15867 字节；SHA256
dc945d90b88ff9388b561daf411304787a92cbc5c542fe32950e0e5739bc1a26。

自含、零依赖；最初绝对 120 秒 / 1 GiB，外层 135 秒。源首部一次设定绝对截止与硬内存限。没有历史载荷、旧日志系数、数据分块或输出缓存。

## 1. 已付接口与本次真正不同的输入

[原 t 参数 N1 结果](../results/R150-appendix-unit211-Phi-zero-corrected-t-parameter-N1-two-slope-curves-and-six-by-two-model.md)的唯一首次 317928 已完成真三均值规则、原 $\lambda$ 首一三次、完整 $N_1$ 余式和未中心化六行模型。其斜率
$$
n=n_0+(a_ft+b_f)f+(a_Vt+b_V)V,\qquad
\Delta=a_fb_V-b_fa_V
$$
只剥旧单位后留下 QQ 不可约 $H_6H_8$，各重数一。新源不再执行旧 CH、旧斜率因式、旧未中心化 $q_Z$、旧六行及其来源检查。

本次只再生必要的自由原 Gram、三个均值的系数定义、已付 $H^{-1}$ 与 $N_1$ 的三个余式系数。三个余式分子 SHA 分别钉为
84bdde216e7db3b309cee64f2b85445f07a38d1b76ecf2ef42af809e87101554、
eb53d324557d81df4535bdbbd89db877f1f09ff3c96cae2a889505336b35f4ca、
9d248069282c53e60dd5f33ae6afb26ff391988dfc306852a4bba261497743dd。
斜率分子、分母也按既成规范 SHA 锁定。它们是后续新输入的参数定义；本次不重新登记这些旧证明目标。

新目标依次为：

1. 同一完整原 Gram 的 NS、PS 两个三次式，以及它们在三个原均值下的完整普通多项式余式身份；
2. 新中心坐标 $\omega$ 的两条逆和首一 $q_\omega$ 的纯权原三均值来源；
3. NS/PS 两条系数 $t$ 次数至多三的二列行，及各自的 $\omega$ 倍；与已成六行经平移相接，得到原 $I_6$ 的精确十行呈示；
4. 仅两个实际乘子的共同内容约除后，完整两坐标返回的新二阶原组合，预定 $t$ 次数上界六。

没有重放旧 $f_{73}$ 十五列、旧 NSPS 两个 $\lambda$ 六次 cofactor、05c 个别 N/P/NV 门、NPV5 最高矩阵或任何冻结失败。

## 2. 原范围与明确分母

只在正确 Phi、distinct singleton、物理 $D\ne0$ 的已付权范围。原权单位为
$$
u,\ Q,\ \delta=1-Q,\ s=u-1,\ K_w=Q+4s,\ L=Q-2s(u-2),\
M_n=2uL-L^2-u^2Q,\ 2\ell-1,
$$
其中 $\ell=L/Q,\ M=M_n/Q$。$\ell=1/2$ 整支已经由正确原式关闭，故 $2\ell-1$ 在当前范围为单位。除此只在明确补图 $\Delta\ne0$ 中增加 $\Delta^{-1}$。

当前未付的 $H_6=0$ 与 $H_8=0$ 两曲线完整保留。程序没有反演 $t,D,\lambda$、任一个别均值的几何头或上述量的范数。此呈示也不需要旧 $\lambda$ 图的 $A/B$ 逆。

原恢复保持
$$
\lambda=(Jf-QV+bcQt-sT_0)/P_{02},\qquad
T=-\ell+T_0(f-V+bct)/P_{02}.
$$
真 dual 乘法的一阶分量为 $v_0w_1+v_1w_0$。原三式是
$\mathcal R,E_{Be},E_{Bo}$，满足原身份
$2\mathcal R+E_1-bE_B-cE_C=0$，其头
$32uQ(2\ell-1)/M^2$ 已在全当前图支付。新源以此已有头定义必要三规则，不再次运行旧头或 CH 检查门。

## 3. 完整原加权三次和原三均值返回

记
$$
A_2=2\lambda^2-2\lambda+1,\qquad B_3=4\lambda^3-6\lambda^2+3\lambda-1.
$$
新源使用完整
$$
NS=bN_4(v_B)+cN_4(v_C)-2\lambda P_{02}(\ell+2T+A_2),
$$
$$
PS=bP_2(v_B)+cP_2(v_C)-P_{02}(\ell+3T+3A_2+B_3).
\tag{1}
$$
$N_4$ 保留全部五项、$P_2$ 使用完整中心三次。$\rho$ 共轭同时交换 $b/c,p/q,X/Y,v_B/v_C$，并与真 trace、DK、中心化交换；因此从完整 B 行取共轭得到完整 C 行，不选择 $\rho$ 的单根，也不只用偶部替代某个别值。

每条原式总 $(t,f,V)$ 次数至多三。程序固定选择最高 $(f,V)$ 单项式，用三条已付原均值规则降次，逐步保留同三个原均值的普通多项式乘子，最终实际返回
$$
F-\{r_0(t)+r_f(t)f+r_V(t)V\}=\sum_{i=0}^2\tau_i(t,f,V)F_i,
\quad F=NS,PS.
\tag{2}
$$
全部差式在原五变量有理系数多项式中返回；不是用一个未经证明的三维结合代数乘法。每次严格降低 $(f,V)$ 次数并不增加总次数，故余式的 $t$ 次数至多 $(3,2,2)$。

## 4. 中心化仅一次代入；不展开大的 omega 三次幂

令 $n_0=At^2+Bt+C$，置
$$
\omega=a_ff+a_VV+At+B.
$$
本次的 $A,B,C$ 仅是 $n_0$ 系数。新逆为
$$
\widehat f=\frac{(a_Vt+b_V)\omega-Ab_Vt-Bb_V+a_VC}{\Delta},
$$
$$
\widehat V=\frac{-(a_ft+b_f)\omega+Ab_ft+Bb_f-a_fC}{\Delta}.
\tag{3}
$$
两条原逆身份真实返回。每式固定 $\omega$ 后对 $t$ 一次。

若原均值头逆为 $H^{-1}$，令
$$
\gamma=(a_f^2,2a_fa_V,a_V^2)H^{-1}.
$$
源构造并完整返回
$$
q_\omega=\sum_i\gamma_iF_i(\widehat f,\widehat V)
=\omega^2+q_1(t)\omega+q_0(t).
\tag{4}
$$
各 $F_i$ 原总次数二，$\gamma$ 纯权，由 (3) 得
$\deg_tq_0,\deg_tq_1\le2$。这只是新首一系数与原来源的必要定义；不重建已成未中心化六行。

将 (3) 一次代入 (2) 的三列余式，得到
$$
F\equiv a_F(t)+b_F(t)\omega\pmod{I_4},
\qquad \deg_ta_F,\deg_tb_F\le3.
\tag{5}
$$
它的来源由已完整返回的 (2) 和可逆原 $N_1$ 消元 (3) 相接。不先展开整个三次 $F(\widehat f,\widehat V)$，也不反复对大 $\omega^3$ 做短除。

新两个倍数实际返回
$$
\omega(a_F+b_F\omega)
-\{-q_0b_F+(a_F-q_1b_F)\omega\}=b_Fq_\omega.
\tag{6}
$$
与旧六行在可逆平移中的像一起，(5)–(6) 给完整十行二列原 $I_6$；原商不假定自由。六条旧行只作为已刊接口保留，不重新执行其证明段。

## 5. 真原两乘子 cofactor 和全部零面

两条新线性行的固定乘子为 $(b_{PS},-b_{NS})$。先清它们实际纯权分母，再仅取消两个实际多项式乘子的全部共同因子。使用取消后的乘子重新返回两个完整坐标，得到纯 $(u,Q,t)$ 的必要式；没有除原方程或从旧标量上盲目约去公共因子。

若该标量非零，则其 $t$ 次数至多六。程序只剥本图已付的原权支持和明确 $\Delta\ne0$ 的支持，保留所有新的纯权内容、$t$ 首项零面与 $t=0$。输出 profile、精确除法计数和来源状态，不输出系数载荷。标量若恒零，照实保留完整十行呈示，不称得到非零支持。若超时或资源失败，按最后实际已返回阶段冻结，不延长或重放。

[中心化纸面推论](../results/R150-appendix-unit211-Phi-zero-corrected-t-slope-centering-and-original-NSPS-cubic-pairs.md)已给以上分级证明。本次只支付真正新的实际原 NS/PS 系数和组合，不设置旧结果复现门。物理 $D$ 局部化不自动保留基环有限模性质；本输入没有任何全 Phi 排空或独立 $U_0$ 尺度点数主张。
