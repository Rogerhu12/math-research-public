# R150：正确 Phi 的原 t 参数 N1、两条斜率曲线与精确六行二列模型

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-28（Asia/Taipei）。

**状态：完整证明，唯一首次实际成功。** 在当前正确 Phi 的原权范围上，三个真均值的 $t$ 参数规则、原 $\lambda$ 首一三次和完整极化 $N_1$ 均已返回。$N_1$ 的纯权斜率非零；剥去原已付单位后，其支持恰为两个 QQ 不可约因子 $H_6,H_8$，各重数一。在 $H_6H_8\ne0$ 上，原四式有一个首一二次加六行二列的精确呈示。**两条整零曲线均保留；本条没有排空或有限点结论。**

## 1. 原范围、系数环与真正的三个均值

只用当前正确 Phi、distinct singleton、物理 $D\ne0$ 原图。设
$$
s=u-1,\quad \delta=1-Q,\quad K_w=Q+4s,\quad
L=Q-2s(u-2),\quad \ell=L/Q,
$$
$$
m=u-\ell,\quad M_n=2uL-L^2-u^2Q,\quad
M=M_n/Q=4bc\delta,\quad g=2\ell-1.
$$
令 $\mathcal A$ 为 QQ 权多项式环局部化于本次实际使用的原单位
$$
u,\ Q,\ \delta,\ s,\ K_w,\ L,\ M_n,\ g.
\tag{1}
$$
$g$ 的支付来自[整个正确 ell-half 原排除](R150-appendix-unit211-Phi-zero-corrected-entire-ell-half-original-exclusion.md)。本次不反演 $m,t,D,\lambda,f-u,\alpha$，也不使用旧错误紧凑均值链的任何头单位。

保留原 $t$ 为参数、$f,V=bX+cY$ 为几何坐标。其他量由原式恢复：
$$
T_0=-K_w,\quad J=2u(1-u)+L,\quad P_{02}=2sL,\quad
W_1=T_0/2+2uf,
$$
$$
\lambda=\frac{Jf-QV+bcQt-sT_0}{P_{02}},\qquad
T=-\ell+\frac{T_0(f-V+bct)}{P_{02}},\qquad
A_1=2f-2V+2bct.
\tag{2}
$$
用 $\rho^2=\delta$ 及
$$
b=\ell/2+m\rho/(2\delta),\quad c=\overline b,\quad
p=1+\rho,\quad q=1-\rho,
$$
$$
x=\frac{(u-\ell Q)V-mW_1}{M},\qquad
y=\frac{\ell W_1-uV}{M},\qquad X=x+\rho y,\quad Y=\overline X
$$
恢复同一自由原 Gram；双点乘法始终为
$$
(vw)_0=v_0w_0,\qquad (vw)_1=v_0w_1+v_1w_0.
$$
因此原第一 germ 均值使用真正的 $(d^2)_1=2d_0d_1$。

记 $F_0=\mathcal R,F_1=E_{Be},F_2=E_{Bo}$，其中
$$
\mathcal R=
4(f-u)(V-f)+bc\,t^2+
t\left(4bc\,u-\ell V+
\frac{m(T_0+4uf-2V)}{2\delta}\right).
\tag{3}
$$
本次完整原式返回
$$
2\mathcal R+E_1-bE_B-cE_C=0.
\tag{4}
$$
故这三个二次式与原 $E_1,E_B,E_C$ 是同一均值理想，偶奇换基只使用已付 $\rho$。以下所有计算均以这三个实际 $F_i$ 为原来源。

## 2. 全图实际三规则与原 lambda 首一三次

按 $(f^2,fV,V^2)$ 排列二次头 $H$，按 $(1,f,V)$ 排列低项。已刊[整个 t 参数三生成定理](R150-appendix-unit211-Phi-zero-corrected-whole-t-parameter-three-mean-generators-and-monic-lambda-cubic.md)给出
$$
\det H=\frac{32uQ(2\ell-1)}{M^2}\in\mathcal A^\times.
\tag{5}
$$
本次从原 Gram 定义实际构造 $H^{-1}$ 和三规则 $r_0,r_1,r_2$，逐式返回
$$
\begin{pmatrix}f^2\\ fV\\ V^2\end{pmatrix}
-
\begin{pmatrix}r_0\\r_1\\r_2\end{pmatrix}
\begin{pmatrix}1\\f\\V\end{pmatrix}
=
H^{-1}\begin{pmatrix}F_0\\F_1\\F_2\end{pmatrix}.
\tag{6}
$$
每条规则的常数系数 $t$ 次数至多二，两个线性系数次数至多一。故未反演物理 $D$ 的均值商由 $1,f,V$ 作为 $\mathcal A[t]$ 模生成；这没有假设三者自由。

令 $M_f,M_V$ 的第 $j$ 列为原变量乘第 $j$ 个生成元后按 (6) 的余式，取
$$
M_\lambda=\frac{bcQt-sT_0}{P_{02}}I+
\frac{J}{P_{02}}M_f-\frac{Q}{P_{02}}M_V.
\tag{7}
$$
本次三条完整原 $\lambda$ 乘法身份、九个 Cayley–Hamilton 坐标均返回。特征多项式给原均值理想中的
$$
\lambda^3+c_2(t)\lambda^2+c_1(t)\lambda+c_0(t)=0,
\qquad \deg_t(c_2,c_1,c_0)=(1,2,3).
\tag{8}
$$
这是一个首一三次关系；不声称它是最小多项式。其来源是自由三列矩阵到原生成模的满射，不要求原商自由或矩阵之间在自由模上交换。

## 3. 完整原 N1 的一次余式与新斜率

令 $N_4$ 为完整原四倍值式，$v_0,v_1$ 为同一 Gram 的前两行。实际输入是
$$
N_1=N_4(v_0+v_1)-N_4(v_0)-N_4(v_1)
       -4\lambda wP_{02},\qquad w=\lambda-1-T.
\tag{9}
$$
同时完整返回原 $N_0=2\lambda P_{02}$ 和 $P_{\rm jet}=3wP_{02}$。将 (9) 仅按 (6) 约化，实际得到
$$
N_1-\sum_{i=0}^2\eta_iF_i
=n_0(t)+(a_ft+b_f)f+(a_Vt+b_V)V=:n,
\tag{10}
$$
其中 $a_f,b_f,a_V,b_V\in\mathcal A$，$\deg_t n_0=2$；三个余式系数的真实 $t$ 次数为 $(2,1,1)$。式 (10) 是完整原多项式身份，不是必要值的替代。

新纯权量
$$
\Delta=a_fb_V-b_fa_V
\tag{11}
$$
实际非零。其约分后的分子总次数十五、双次数 $(15,8)$；分母只含 (1) 的支持。只剥原已付支持并首一化后，保留量 $H_\Delta$ 满足
$$
H_\Delta=\frac1{1024}H_6H_8,
\tag{12}
$$
完整 QQ 因式乘回已返回。准确参数为：

| 量 | 总次数 | $(u,Q)$ 次数 | 项数 | 重数 |
| --- | ---: | ---: | ---: | ---: |
| $H_\Delta$ | 14 | $(14,7)$ | 63 | — |
| $H_6$ | 6 | $(6,3)$ | 16 | 1 |
| $H_8$ | 8 | $(8,4)$ | 25 | 1 |

规范 profile SHA256 依次为：

- $H_\Delta$：1a40cae82d6752cacad4033ed12c07ae06731abd9ff7db0c976812d86d1b68dc；
- $H_6$：2b93b7f418f47c46493b2b1edbd717ef8f1c4a027fe312c8717805e8e11d0e77；
- $H_8$：ddaac32405c19d23886f545ac141f33b83b3bddb1f87a647317ec682d82a5945。

两因子的不可约性限于 QQ；没有绝对不可约主张。它们的系数由所附原定义与唯一因式规范确定，不另保存可重算载荷。

## 4. 斜率补图上的精确六行二列原呈示

现在只在 $\mathcal A'=\mathcal A[\Delta^{-1}]$ 上设
$$
Z=a_ff+a_VV.
$$
$(f,V)\mapsto(Z,n-n_0)$ 的行列式为 $\Delta$。消去 $n=0$ 后的完整逆为
$$
\widehat f=\frac{(a_Vt+b_V)Z+a_Vn_0}{\Delta},\qquad
\widehat V=\frac{-(a_ft+b_f)Z-a_fn_0}{\Delta}.
\tag{13}
$$
本次两个原反代身份均返回。因此
$$
\mathcal A'[t,f,V]/(F_0,F_1,F_2,N_1)
\simeq\mathcal A'[t,Z]/(F_0^*,F_1^*,F_2^*),
\tag{14}
$$
其中星号仅表示 (13) 的同点代入。

置
$$
\gamma=(a_f^2,2a_fa_V,a_V^2)H^{-1},\qquad
q_Z=\sum_{i=0}^2\gamma_iF_i^*.
\tag{15}
$$
由 (6) 与 $a_f\widehat f+a_V\widehat V=Z$，
$$
q_Z=Z^2+q_1(t)Z+q_0(t)
$$
真正首一。实际返回 $\deg_t(q_0,q_1,1)=(3,2,0)$。

若 $A_i(t)$ 是 $F_i^*$ 的 $Z^2$ 系数，令
$$
\ell_i=F_i^*-A_iq_Z=a_i(t)+b_i(t)Z.
$$
则
$$
(F_0^*,F_1^*,F_2^*)=(q_Z,\ell_0,\ell_1,\ell_2)
\tag{16}
$$
是双向理想相等，所有来源均已完整返回。在首一二次代数
$S=\mathcal A'[t,Z]/(q_Z)$ 中，理想 $(\ell_0,\ell_1,\ell_2)$ 作为 $\mathcal A'[t]$ 模恰由六行
$$
(a_i,b_i),\qquad (-q_0b_i,\ a_i-q_1b_i),\qquad i=0,1,2
\tag{17}
$$
生成；第二行是同一 $\ell_i$ 的 $Z$ 倍。这里只用所定义首一二次代数 $S$ 的基 $1,Z$，没有把原商假定为自由二列代数。

本次六行的真实 $t$ 次数依次为
$$
(5,4),(7,6),(5,4),(7,6),(5,4),(7,6).
\tag{18}
$$
这些是未中心化原执行的准确返回，不将后续纸面中心化降次混写为本次实际输出。

## 5. 唯一实际凭据与保留边界

源：[原 t 参数 N1 输入](../notes/2026-11-28-unit211-Phi-zero-corrected-t-parameter-original-N1-slope-model-8542.py)；
[输入说明](../notes/2026-11-28-unit211-Phi-zero-corrected-t-parameter-original-N1-slope-model-8542-input.md)；
[完整小回执](../notes/2026-11-28-unit211-Phi-zero-corrected-t-parameter-original-N1-slope-model-8542-execution.json)。

源 blob 317928a236335a6d705499e6655f41a1749c4715，15033 字节，SHA256
c6346f72acd3fe94998ca4d8f4910af2ceb0e8afd5a67c5eb27df4696e480864。
自含、零依赖；最初绝对 120 秒 / 1 GiB，外层 135 秒。

唯一实际 run 46147554675 / job 140986824614。源提交
be479a0ebd3762207e459ae38deed08d6f15cf32；执行前真实 pull 到
21e3710300d405488d5b328c263116569f28c321，2026-11-28T13:02:01.663292+00:00，两规则未变。
内层数学 28.151746173 秒，driver 28.214213199 秒，峰值 166752 KiB，exit 0。
stdout 12621 字节，SHA256
bc5bb4118fa5868bba518f34048e21a153c8f24fce0cc3ddee15da459818a3d9。

累计 227 次精确除法回乘；11 个原恢复坐标、3 条真均值规则、3 条原 $\lambda$ action、9 个 CH 坐标、1 条完整 $N_1$ 余式、2 条斜率逆坐标、7 条首一/六行身份均已返回。

全图保留两个整权零面 $H_6=0$、$H_8=0$。在其上仍有前面的正确三生成和首一 $\lambda$ 三次，但不套用 (13)–(18)。斜率补图的两生成结论只在未反演物理 $D,t$ 的必要代数上陈述；随后取物理单位开集不能自动声称仍为同一基环上的有限模。本条不证明全 Phi、任何整斜率曲线或 ordinary ISP 排空，也不把必要生成元数当成包含独立 $U_0$ 尺度的规范点数。
