# 新输入：正确 Phi 的原 t 参数 N1 余式、首一 lambda 三次与斜率两生成图

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-28（Asia/Taipei）。

**状态：未执行。** 这是新 $t$ 参数坐标下的完整原值输入。已经纸证的三个真均值头用于构造必要系数；新的实际目标是原 $\lambda$ 乘法的首一三次、完整极化 $N_1$ 的一次余式、它的纯权斜率，以及只在该斜率补图上的精确六行二列模型。没有预报斜率的因子、单位性、两列次数或原图排空。

源：[2026-11-28-unit211-Phi-zero-corrected-t-parameter-original-N1-slope-model-8542.py](2026-11-28-unit211-Phi-zero-corrected-t-parameter-original-N1-slope-model-8542.py)。
Git blob 317928a236335a6d705499e6655f41a1749c4715，15033 字节；SHA256
c6346f72acd3fe94998ca4d8f4910af2ceb0e8afd5a67c5eb27df4696e480864。

自含、零依赖。最初绝对 120 秒 / 1 GiB，外层 135 秒。没有载荷文件、历史 JSON、旧原矩阵或失败门续段。

## 1. 原范围与真正不同的输入

只在当前正确 Phi、distinct singleton、物理 $D\ne0$ 原图。使用已经独立支付的
$$
u,\ Q,\ 1-Q,\ u-1,\ Q+4(u-1),\ L,\ M_n,\ 2\ell-1,
$$
其中
$$
L=Q-2(u-1)(u-2),\quad \ell=L/Q,\quad
M_n=2uL-L^2-u^2Q,\quad M=M_n/Q=4bc(1-Q).
$$
$2\ell-1$ 来自刚完成的整个正确 ell-half 原排除。这里不需要反演旧三头的 $A/B$，也不倒 $m$、$t$、$D$、$\lambda$、$f-u$、$\alpha$ 或它们的范数。

[整 t 参数三生成的纸面定理](../results/R150-appendix-unit211-Phi-zero-corrected-whole-t-parameter-three-mean-generators-and-monic-lambda-cubic.md)
已经给出
$$
\det H_{f,V}=32uQ(2\ell-1)/M^2.
\tag{1}
$$
本源只利用它构造新的实际三规则与后续原值系数，不重新执行旧 $\lambda$ 参数 f62/f73 头、十五列、两 C6、个别十次、NPV5 或 ell-half 证书。

## 2. 自由 f,V,t 的同一个真原 Gram

使用五变量 $u,Q,t,f,V$，权量
$$
T_0=2u-\ell Q-2u^2,\quad
J=2u(1-u)+\ell Q,\quad
P_{02}=2(u-1)\ell Q,\quad P_f=T_0(J-Q).
$$
同点恢复
$$
\lambda=\frac{Jf-QV+bcQt-(u-1)T_0}{P_{02}},\quad
T=-\ell+\frac{T_0}{P_{02}}(f-V+bct),\quad z=Qt.
\tag{2}
$$
源完整返回原 $N_0/P_1$ 恢复关系，(2) 与原 $(\lambda,T,z)$ 图的仿射行列式为 $-P_f/P_{02}^2$，是旧权单位。

取
$$
W_1=T_0/2+2uf,\quad
x=\frac{(u-\ell Q)V-mW_1}{M},\quad
y=\frac{\ell W_1-uV}{M},\quad A_1=2f-2V+2bct.
$$
用完整偶奇扩张 $\rho^2=1-Q$ 形成 $b,c,p,q,X,Y$ 和原 Gram 四行。真正双点乘法是
$$
(vw)_0=v_0w_0,\qquad (vw)_1=v_0w_1+v_1w_0;
$$
另两点按各自标量相乘。源从这个乘法直接计算 $d,DK(d),E_0,E_1,E_B,E_C$，不使用撤回的 compact germ square。

正确均值差
$$
\mathcal R=4(f-u)(V-f)+bct^2+
t\left(4bcu-\ell V+
 \frac{m}{2(1-Q)}(T_0+4uf-2V)\right)
$$
在同一自由图完整返回
$$
E_0=0,\qquad
2\mathcal R+E_1-bE_B-cE_C=0.
\tag{3}
$$
所以三式
$$
F=(\mathcal R,E_{Be},E_{Bo})
$$
与三真均值有原理想等价。所有系数均在原偶奇基环中，未选择单个复根。

## 3. 新实际三规则和原 lambda 乘法

按列 $(1,f,V,f^2,fV,V^2)$ 提取完整 $F$。用 (1) 构造 $H^{-1}$，完整返回
$$
q_{ff}=f^2-a\cdot e,\quad
q_{fV}=fV-b\cdot e,\quad
q_{VV}=V^2-c\cdot e,\qquad e=(1,f,V),
$$
$$
(q_{ff},q_{fV},q_{VV})^{\mathsf t}=H^{-1}F.
\tag{4}
$$
低三系数的 $t$ 次数分别至多 $2,1,1$。全部分母只在第 1 节旧权支持内。

以这些实际系数形成 $M_f,M_V$，再按 (2) 形成
$$
M_\lambda=\frac{bcQt-(u-1)T_0}{P_{02}}I
+\frac J{P_{02}}M_f-\frac Q{P_{02}}M_V.
\tag{5}
$$
三列原差 $\lambda e_j-e^{\mathsf t}(M_\lambda)_{\bullet j}$ 各有 (4) 的显式乘子，源逐个完整返回。随后新计算三个特征系数 $c_2,c_1,c_0$，实际核回
$$
M_\lambda^3+c_2M_\lambda^2+c_1M_\lambda+c_0I=0
\tag{6}
$$
的全部九坐标。相应 $\lambda^3+c_2(t)\lambda^2+c_1(t)\lambda+c_0(t)$ 的 $t$ 次数界为 $1,2,3$；首一及原来源不要求商自由。此式只有限于 $t$ 参数，不等于对权环有限或排空。

## 4. 完整原极化 N1 的新一次余式

源直接用同一个完整原
$$
N_4(v)=2\tau(dv^2)-F_2\tau(v^2)-4\tau(v)\tau(dv)
 +2F_2\tau(v)^2+\tau(vDKv)
$$
计算
$$
N_1=N_4(v_0+v_1)-N_4(v_0)-N_4(v_1)
        -4\lambda(\lambda-1-T)P_{02}.
\tag{7}
$$
原 $N_4(v_0)=2\lambda P_{02}$、完整 cubic jet 也在同点返回。没有用一部分 $N_4$ 或某个最高部代替 (7)。

按 (4) 降一次二次头，得到
$$
n=n_0(t)+n_f(t)f+n_V(t)V,\qquad
N_1-n=\sum_{j=1}^3 \eta_jF_j,
\tag{8}
$$
这个完整普通多项式身份实际乘回。这里
$$
\deg_t n_0\le2,\qquad \deg_t n_f,\deg_t n_V\le1.
$$
因此 $(F,N_1)=(F,n)$；所有后续行都仍来自完整原四式。

## 5. 新纯权斜率及所有零支

写
$$
n_f=a_ft+b_f,\qquad n_V=a_Vt+b_V,\qquad
\Delta_t=a_fb_V-b_fa_V.
\tag{9}
$$
四个系数和 $\Delta_t$ 均为纯权有理式，源核实 (9) 的完整重建。只对这条新的 $\Delta_t$ 分子剥旧已付因子，并做完整 QQ 因式乘回。

若 $\Delta_t=0$ 恒等，保整个原四式与已成三生成模型，不宣两生成。若其余支持非常数，整个余支持零集保留；后续仅在 $\Delta_t\ne0$ 开图。只有实际分子支持全部旧付时，才能将开图结果称为全当前 Phi。

在这个纯权开图定义
$$
Z_c=a_ff+a_VV.
$$
由 $n=0$ 精确解得
$$
f=\frac{(a_Vt+b_V)Z_c+a_Vn_0}{\Delta_t},\qquad
V=\frac{-(a_ft+b_f)Z_c-a_fn_0}{\Delta_t}.
\tag{10}
$$
源同时返回 $a_ff+a_VV=Z_c$ 与完整 $n=0$，没有反演任何关于 $t$ 的首项。

## 6. 全原四式的精确六行二列呈示

将 (10) 代入三个完整原 $F_j$，得到 $\widetilde F_j(t,Z_c)$。令
$$
\gamma_j=a_f^2(H^{-1})_{1j}
       +2a_fa_V(H^{-1})_{2j}
       +a_V^2(H^{-1})_{3j}.
$$
由 (4) 的完整原来源，
$$
q_Z=\sum_j\gamma_j\widetilde F_j
   =Z_c^2+q_1(t)Z_c+q_0(t).
\tag{11}
$$
源完整核回这个组合、二次系数一，以及 $\deg_t q_1\le2,\deg_t q_0\le3$。单独的三个原二次头不需要单位。

设 $\alpha_j=[Z_c^2]\widetilde F_j$，则
$$
\ell_j=\widetilde F_j-\alpha_jq_Z
$$
对 $Z_c$ 至多一次，且
$$
(\widetilde F_1,\widetilde F_2,\widetilde F_3)
=(q_Z,\ell_1,\ell_2,\ell_3).
\tag{12}
$$
在首一环境 $A[\Delta_t^{-1},t][Z_c]/(q_Z)$ 中，理想 $(\ell_j)$ 作为 $A[\Delta_t^{-1},t]$ 模精确由
$$
\ell_1,\ Z_c\ell_1,\ \ell_2,\ Z_c\ell_2,\ \ell_3,\ Z_c\ell_3
$$
生成。若 $\ell_j=c_j+d_jZ_c$，其第二行余式是
$$
(-q_0d_j,\ c_j-q_1d_j),
$$
并完整返回
$$
Z_c\ell_j-\operatorname{rem}(Z_c\ell_j)=d_jq_Z.
$$
这是完整原 $I_4$ 的六行二列呈示，不假定商本身自由或只取同点必要行。原完整 NS/PS 及个别 N/P/NV 尚未在本源中添加，不能借这个呈示冒称物理全系统已充分。

## 7. 首次执行边界

所有新未知纯权斜率零纤维、各 $\widetilde F_j$ 二次头零、$t=0$ 和 $D=0$ 的形式边界均通过上述全式保留；物理点的已付条件仍另行施加。源不反演 $D,t$ 或范数。整个过程只输出小 profile、次数、因子/SHA 和完整返回计数，不保存可重算系数载荷。

源失败或达到 120 秒 / 1 GiB 时按实际最后返回记录，不能增限、续旧段或把外层绿色代替内层数学。已刊纸面头与原定义无需另加复现审计门。
