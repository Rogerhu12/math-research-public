# 正确 Phi 第二 NV t 头：两个原首一二次、完整二十同点列与三个固定四阶原 cofactor

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-29（Asia/Taipei）。

**状态：唯一新的首次输入，尚未执行。** 本输入只研究完整 NV 的第二 t 头
$$
B_2=\ell(3-2\lambda)+2T+2m\sigma=0.
$$
新目标是把原均值、N1、第三矩与完整 NV 放到同一个真正四元代数中，返回全部原二十列及三个事前固定的四阶 cofactor。第一 NV 头已冻结的三标量泛域 gcd 不在本输入内；本次也不计算第二头三标量的泛域 gcd。

源文件：[second-NV-t-head-original-four-generator-columns](2026-11-28-unit211-Phi-zero-corrected-second-NV-t-head-original-four-generator-columns-8542.py)。

- 零源码依赖；完整正确 dual Gram 在本源定义。
- 完整源码 SHA256：c7141ce12424d916ee415c0ac0121ea938ff206d20b5a8c12193bb3a1cdcdaa1。
- 唯一预算：120 秒、1 GiB；外层 135 秒。
- 无数值素数、权点选择、单根选择或头开图。
- 预算边界只保已经完成的原身份；不续轮、换列、重排、加限或改成同一目标的泛域 gcd。

## 1. 已付范围与同点原恢复

保持当前正确 Phi、distinct singleton、物理 $D_{\rm phys}\ne0$ 的原图。使用
$$
s=u-1,\quad \delta=1-Q,\quad
L=Q-2s(u-2),\quad \ell=L/Q,\quad m=u-\ell,
$$
$$
T_0=2u-\ell Q-2u^2,\quad J=2u(1-u)+\ell Q,\quad
P_{02}=2s\ell Q,
$$
$$
M=\ell(2u-\ell Q)-u^2=4bc\delta,\qquad
K_w=Q+4s,\quad M_n=QM.
$$
本源实际分母只按旧单位乘积
$$
U=Q\delta sK_wLM_n
\tag{1}
$$
审核。这里不需要倒 m、u、$2\ell-1$、$2u-3$、任何新谱头、sigma、t 或 D。旧物理图上它们中的一些可能另有支付，不被本次拿来隐藏新分母。

设 $a=\lambda-3/2$，直接在整个 $B_2=0$ 上代入
$$
T=\ell a-m\sigma.
\tag{2}
$$
同一点正确 $E_0,N_0,P_1$ 的恢复为
$$
E=\frac{P_{02}(T+\ell)}{T_0},\qquad
f=\frac{P_{02}\lambda-QE+sT_0}{J-Q},
$$
$$
V=f+bc\,t-E,\quad A_1=2E,\quad
W_1=T_0/2+2uf,\quad w=\lambda-1-T .
\tag{3}
$$
再由
$$
x=\frac{(u-\ell Q)V-mW_1}{M},\quad
y=\frac{\ell W_1-uV}{M},\quad
X=x+\rho y,\quad Y=x-\rho y,\quad \rho^2=\delta
$$
形成完整四行原 Gram。双点乘法始终为
$$
(vw)_0=v_0w_0,\qquad (vw)_1=v_0w_1+v_1w_0.
$$
没有借用撤回的 wrong-Rbar 链。

定义原矩算子与二次形式
$$
d=DK(1),\quad F_2=\tau(d),\qquad
N_4(v)=2\tau(dv^2)-F_2\tau(v^2)-4\tau(v)\tau(dv)
+2F_2\tau(v)^2+\tau(vDKv).
$$
完整三个原均值、$N_1$ 极化和完整 $NV=N_4(1,w,h,k)$ 都从该同一点真 Gram 构造。这里
$$
h=\lambda-\tfrac12-\rho\sigma,\qquad
k=\lambda-\tfrac12+\rho\sigma.
$$
其偏移量 $h-1=a-\rho\sigma$、$k-1=a+\rho\sigma$ 形成原第二、第三矩
$$
E_2=b(h-1)^2+c(k-1)^2-A_\lambda,\qquad
E_3=b(h-1)^3+c(k-1)^3-B_\lambda,
$$
$$
A_\lambda=2\lambda^2-2\lambda+1,\quad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1.
\tag{4}
$$
源实际返回 $E_0=N_0=P_1=0$ 的恢复身份、正确原均值差、完整 N1 极化、(4) 的全部系数及 $[t]NV=0$。最后一个身份属于本头的完整原式，不是把物理 t 设为零。

## 2. 两个原首一二次和确切来源

按[第二头纸面原二次](../results/R150-appendix-unit211-Phi-zero-corrected-second-NV-t-head-original-monic-sigma-and-four-columns.md)，
$$
q_\sigma=\frac{E_2}{\ell\delta}
=\sigma^2-\frac{2ma}{\ell\delta}\sigma
-\frac{A_\lambda-\ell a^2}{\ell\delta}.
\tag{5}
$$
因此所有 sigma 重根和幂零结构保留。

另由[全权 t 首一二次与十列](../results/R150-appendix-unit211-Phi-zero-corrected-whole-monic-t-quadratic-exact-ten-columns-and-four-generator-NV-head.md)，取真原均值
$$
\mathcal R=4(f-u)(V-f)+bct^2+
t\left(4bcu-\ell V+
\frac{m(T_0+4uf-2V)}{2\delta}\right),
$$
其来源为
$$
2\mathcal R+E_1-bE_B-cE_C=0.
\tag{6}
$$
置 $E_{Be}=(E_B+E_C)/2$、$E_{Bo}=(E_B-E_C)/(2\rho)$。已显示计算的两个 t 二次头为
$$
a_R=-\frac{bcs(2u-3)}{\delta},\qquad
a_O=\frac{m(Q+2s^2)}{4\delta^2}.
$$
定义
$$
B_q=Q^2+(2u^2-3)Q+2s(2u-1)(u-2),\qquad
\gamma_R=-\frac{B_q}{\ell bcsQ},\quad
\gamma_O=-\frac{8\delta}{\ell}.
$$
完整原恒等式 $\gamma_Ra_R+\gamma_Oa_O=1$ 给
$$
q_t=\gamma_R\mathcal R+\gamma_OE_{Bo},
\qquad [t^2]q_t=1.
\tag{7}
$$
$\gamma_O$ 本身为旧单位；(7) 覆盖整个 $a_R=0$ 或 $a_O=0$，没有删除二者的交界。

仅按 (5) 作一次首一 sigma 除法
$$
q_t=\widetilde q_t+w_sq_\sigma .
\tag{8}
$$
$\widetilde q_t$ 对 t 仍首一二次，其每个系数对 sigma 次数至多一。于是
$$
\mathcal B=
\bigl(\mathcal A[\lambda,\sigma]/(q_\sigma)\bigr)[t]/(\widetilde q_t)
\tag{9}
$$
是 $\mathcal A[\lambda]$ 上真正自由四生成的环境，基为
$$
e=(1,\sigma,t,\sigma t).
\tag{10}
$$
两次首一除法是自由性的来源；不假定任何加入剩余关系后的商自由。

## 3. 七原式和完整二十列

本次原理想准确取为
$$
J_7=(E_2,\mathcal R,E_{Be},E_{Bo},N_1,E_3,NV).
\tag{11}
$$
它是完整物理系统的一个必要子理想。本输入不宣布这些七式已经是物理系统的充分条件；NS/PS、个别 N/P、其余同 sigma 条件与物理开图均继续保留。

在 (9) 中，仅需五个 seed：
$$
(\mathcal R,E_{Be},N_1,E_3,NV).
\tag{12}
$$
这是精确的商呈示，因为 $E_2=\ell\delta q_\sigma$，而 $\gamma_O$ 是单位，可由 (7) 消去原 $E_{Bo}$。

对每个 seed F，按固定顺序乘
$$
1,\ \sigma,\ t,\ \sigma t.
$$
每个 $m_0F$ 先对 $\widetilde q_t$ 首一除 t，再对 $q_\sigma$ 首一除 sigma：
$$
m_0F=r+Q_t\widetilde q_t+Q_sq_\sigma.
$$
利用 (5)、(7)、(8)，源完整返回普通多项式身份
$$
\boxed{
m_0F=r+
\frac{Q_s-Q_tw_s}{\ell\delta}E_2
+Q_t\gamma_R\mathcal R+Q_t\gamma_OE_{Bo}.
}
\tag{13}
$$
每条 r 又完整重构为 (10) 的四个坐标。所有分母逐一在 (1) 中支付；不经过泛型域逆或某个 Gram 头逆。

以 seed 为外循环、基元为内循环，固定得到二十列：
$$
[0,1,2,3]=\mathcal R\cdot(1,\sigma,t,\sigma t),
$$
$$
[4,5,6,7]=E_{Be}\cdot(1,\sigma,t,\sigma t),
$$
$$
[8,9,10,11]=N_1\cdot(1,\sigma,t,\sigma t),
$$
$$
[12,13,14,15]=E_3\cdot(1,\sigma,t,\sigma t),
$$
$$
[16,17,18,19]=NV\cdot(1,\sigma,t,\sigma t),
\tag{14}
$$
右侧均指完整普通来源 (13) 的余式列。其 $4\times20$ 矩阵 cokernel 精确呈示 (11) 在 (9) 中的商：因为 (10) 真的是一个自由结合代数的基，每个原 seed 的理想就是其四个基倍数所生成的基环模。

## 4. 唯一预定的三个四阶 cofactor

本次只计算以下三个固定列组：
$$
(0,1,4,8),\qquad
(0,1,4,12),\qquad
(0,1,4,16).
\tag{15}
$$
分别对应
$$
(\mathcal R,\sigma\mathcal R,E_{Be},N_1),\quad
(\mathcal R,\sigma\mathcal R,E_{Be},E_3),\quad
(\mathcal R,\sigma\mathcal R,E_{Be},NV).
$$
没有按实际秩、行列式或返回头更换列组。

对每个四阶列矩阵 B，取
$$
\omega_j=(-1)^j\det B[\{1,2,3\},\{0,1,2,3\}\setminus\{j\}].
$$
这是 $\operatorname{adj}(B)e_0$ 的完整列。源逐坐标返回
$$
B\omega=F e_0,\qquad
F=\sum_{j=0}^3B_{0j}\omega_j=\det B .
\tag{16}
$$
因此 F 是同一点七原式的必要标量，不倒 $\det B$ 或任何主元。

把 (13) 的全部来源代入 (16)，首先得到
$$
F=\sum_{i=0}^6\Omega_i\,F_i
\tag{17}
$$
于普通多项式环，其中 $F_i$ 按 (11) 的七原式顺序。随后把每个 $F_i=N_i/d_i$ 改为原分子 $N_i$，统一清除实际七乘子及 F 的分母；再仅同时约掉**全部七个真实原乘子**的共同多项式因子，每步实际普通多项式乘回。

最后只移除 (1) 的旧单位支持，七个最终乘子再次完整返回同一个原标量。这样共同因子、某个矩阵主元或某个新 lambda 头为零的整个纤维都保留。裸行列式自身的内容不能代替这一步。

若某个固定 F 为零，实际只记录该零身份并保全部纤维；不换列重试。若最终真实原组合返回旧单位，才可据该原单位身份排除此头；单凭次数、非零性、某个数值秩或外层工作流绿色不能作此结论。

## 5. 先验几何次数与实际返回的区别

给基元 (10) 的几何权
$$
d=(0,1,1,2).
$$
两个首一二次的系数满足分级上界；(13) 保持总 $(\lambda,\sigma,t)$ 次数。前三个 seed 总次数至多二，E3 和完整 NV 至多三。因此若输入列的原几何次数为 g，
$$
\deg_\lambda B_{ij}\le g-d_i .
$$
对 (15) 的三组列，列几何次数分别为
$$
(2,3,2,2),\qquad(2,3,2,3),\qquad(2,3,2,3).
$$
在行列式各项中减去 $\sum_i d_i=4$，得到三个**证明过的上界**
$$
\deg_\lambda F\le5,\quad6,\quad6.
\tag{18}
$$
这些不是预报的实际次数或非零性。全部七原乘子公共取消及旧纯权单位约除也不会增加 lambda 次数；最终只报告真实得到的 profile 和头。

所有新 lambda 头、全部未付纯权零纤维以及第一 NV t 头继续保留。这里没有新的 gcd、因式、完整原点数或整个 Phi 排空结论。

## 6. 保存、预算和已有边界

源只输出来源定义、逐阶段布尔/计数、次数、项数和 SHA 小回执，不输出多项式系数载荷。原普通身份和确定性函数留在可读源中。

本输入与第一头的三 scalar 泛域 gcd 是不同原目标：新真实均值首一 t 二次把同一个物理 t 留在四元代数里，固定 cofactor 明确含原均值；不重算第一头的 sigma gcd，也不重做任何 Q 估值、旧轴比较或旧三生成模型的执行门。到达唯一 120 秒或 1 GiB 边界即停止并保准确最后阶段。
