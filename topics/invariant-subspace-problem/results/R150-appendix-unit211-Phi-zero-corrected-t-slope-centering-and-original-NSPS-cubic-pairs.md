# R150：正确 Phi 的 t 斜率中心化与原 NS/PS 三次两列

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-28（Asia/Taipei）。

**状态：完整纸面推论，无新执行。** 只在[正确原 t 参数 N1 模型](R150-appendix-unit211-Phi-zero-corrected-t-parameter-N1-two-slope-curves-and-six-by-two-model.md)的斜率补图上工作。通过一个不增加分母的仿射平移，首一二次式的两个系数均为 $t$ 的至多二次式；完整原 NS、PS 在两列中的系数均为至多三次式。两条未付斜率零曲线完整保留。这些是本次纸面推导，不改写 317928 首次执行的未中心化次数记录。

## 1. 同一个原 N1 与仿射中心

沿用已付权环 $\mathcal A$、原三个均值 $F_0,F_1,F_2$、真头 $H$ 和完整原余式
$$
n=n_0(t)+(a_ft+b_f)f+(a_Vt+b_V)V,\qquad
n_0(t)=At^2+Bt+C,
$$
$$
\Delta=a_fb_V-b_fa_V.
\tag{1}
$$
这里 $A,B,C,a_f,b_f,a_V,b_V$ 都是纯权系数。此次的 $A,B,C$ 只是 $n_0$ 的三个系数，不是旧权头的同名字母。令
$$
\mathcal A'=\mathcal A[\Delta^{-1}],\qquad
Z=a_ff+a_VV,\qquad \omega=Z+At+B.
\tag{2}
$$
在 $n=0$ 后，两条完整逆为
$$
f=\frac{(a_Vt+b_V)\omega-Ab_Vt-Bb_V+a_VC}{\Delta},
$$
$$
V=\frac{-(a_ft+b_f)\omega+Ab_ft+Bb_f-a_fC}{\Delta}.
\tag{3}
$$
这直接由已付的 $Z$ 逆公式代入 (2) 得到；其中原 $t^2$ 项相消。两式对固定 $\omega$ 都是 $t$ 的一次式，对固定 $t$ 都是 $\omega$ 的一次式。平移没有反演 $A,B,C,t$ 或任何新头。

## 2. 首一 qω 的两个系数均至多 t 二次

原三个 $F_i$ 在 $(t,f,V)$ 中的总次数至多二，其 $(f^2,fV,V^2)$ 头矩阵 $H$ 只含权。令
$$
\gamma=(a_f^2,2a_fa_V,a_V^2)H^{-1}.
\tag{4}
$$
把 (3) 代入后记为 $F_i^\omega$。由原三规则和
$a_ff+a_VV=\omega-At-B$，同一个原组合
$$
q_\omega=\sum_{i=0}^2\gamma_iF_i^\omega
$$
满足
$$
q_\omega=\omega^2+\widetilde q_1(t)\omega+\widetilde q_0(t).
\tag{5}
$$
首一性沿用原 $q_Z$ 的首一性，平移不改变二次头。

式 (3) 的每一项对 $t$ 至多一次；故每个 $F_i^\omega$ 对 $t$ 至多二次。$\gamma_i$ 是纯权量，所以直接从原组合得
$$
\deg_t\widetilde q_1\le2,\qquad
\deg_t\widetilde q_0\le2.
\tag{6}
$$
这个界不依赖把原 $q_Z$ 的三次常数系数再次展开、观察取消，也不需要任一原单式头为单位。

若 $A_i(t)$ 是 $F_i^\omega$ 的 $\omega^2$ 系数，则
$$
\ell_i=F_i^\omega-A_iq_\omega
$$
对 $\omega$ 一次，且
$$
(F_0^\omega,F_1^\omega,F_2^\omega)
=(q_\omega,\ell_0,\ell_1,\ell_2).
\tag{7}
$$
在 $S=\mathcal A'[t,\omega]/(q_\omega)$ 中，三条 $\ell_i$ 及其 $\omega$ 倍生成同一原四式的六行模。必要的 $\omega$ 倍规则是
$$
(a+b\omega)\omega\equiv
-\widetilde q_0b+(a-\widetilde q_1b)\omega.
\tag{8}
$$

## 3. 先按原均值降次，再作一次中心化替换

原三规则形式为
$$
f^2,\ fV,\ V^2
\equiv r_0(t)+r_f(t)f+r_V(t)V,\qquad
\deg_t r_0\le2,\quad
\deg_t r_f,\deg_t r_V\le1.
\tag{9}
$$
赋予 $t,f,V$ 都为一次。每一次 (9) 替换不增加总次数，且严格降低 $f,V$ 的总次数。因此任意总次数至多 $d$ 的原多项式 $P$，经有限个这样的原式替换，得到某个完整身份
$$
P-\bigl(p_0(t)+p_f(t)f+p_V(t)V\bigr)
=\sum_{i=0}^2 a_i(t,f,V)F_i,
\tag{10}
$$
$$
\deg_t p_0\le d,\qquad
\deg_t p_f,\deg_t p_V\le d-1.
\tag{11}
$$
这只要求确定一个替换次序及其原组合；不要求规则合流，不假设三生成元自由，也不丢失 overlap 关系。

将 (3) 一次代入 (10) 的三列余式，得到
$$
P\equiv P_0(t)+P_1(t)\omega\pmod{I_4},
\qquad \deg_t P_0,\deg_t P_1\le d.
\tag{12}
$$
理由是 (3) 的两个仿射系数都至多 $t$ 一次，直接与 (11) 相加即可。这里不先把整个原 $P$ 换成 $\omega$ 多项式再反复使用 (5)；后一做法的中间次数并不能直接给出 (12)。

## 4. 完整原 NS、PS 与精确十行呈示

同一原 Gram 的行都对 $(t,f,V)$ 仿射，$\lambda,T$ 也仿射。完整 $N_4$ 与中心三次 $P_2$ 的每个原项在这些变量中次数至多三。记
$$
A_2=2\lambda^2-2\lambda+1,\qquad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
NS=bN_4(v_B)+cN_4(v_C)
   -2\lambda P_{02}(\ell+2T+A_2),
$$
$$
PS=bP_2(v_B)+cP_2(v_C)
   -P_{02}(\ell+3T+3A_2+B_3).
\tag{13}
$$
这是完整原加权值条件；尤其保留了 $(1+\xi)^2$、$(1+\xi)^3$ 的全部低项，没有用最高项或个别分量替代。

取 $d=3$，式 (10)–(12) 给
$$
NS\equiv N_0(t)+N_1(t)\omega,\qquad
PS\equiv P_0(t)+P_1(t)\omega\pmod{I_4},
$$
$$
\deg_t N_0,N_1,P_0,P_1\le3.
\tag{14}
$$
因 (10) 保留完整原三均值来源、(3) 是同一原 $N_1$ 的可逆消元，向原六行加入 (14) 两行及其 (8) 中的 $\omega$ 倍，恰得到完整 $I_6$ 商的十行二列呈示。不是仅有相同点值的必要行，也不要求原商自由或先作有限维假设。

两原行的固定二阶组合给必要式
$$
P_1(t)\,[N_0(t)+N_1(t)\omega]
-N_1(t)\,[P_0(t)+P_1(t)\omega]
=N_0P_1-N_1P_0,
\tag{15}
$$
其 $t$ 次数至多六。式 (15) 可能恒零；本条没有先验非零、首一、有限性或排空断言。若后续实际计算只取消两个真实乘子的共同因子，必须以取消后的乘子重新返回完整两坐标。所有未付权支持继续保留。

## 5. 范围

本推论只用已付真均值头与明确 $\Delta\ne0$；$\Delta=0$ 的 $H_6,H_8$ 两整曲线不适用 (3)，须另作真实原纤维分析。原 $\lambda,t,D$ 始终没有作为本推导的新分母；当前正确 Phi 的物理 $D\ne0$ 范围也没有外推至碰撞图。本篇没有新程序执行、没有重放 317928 的六行门，且不增加任何独立 $U_0$ 尺度计数。
