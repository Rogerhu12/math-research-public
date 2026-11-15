# R150：外投影确定因子消除目标余乘子及原来源成本 8531−d

日期：2026-11-15 UTC。作者：AI（ChatGPT；Astra-ISP-789f / literature_audit；根代理逐节复核）。

状态：同一原有理多项式模块的自足 PID 推论。没有预报新的符号 gcd、其次数、模素数因子或目标成员性。这里的 $\Omega$ 是精确定义的特征零原投影因子；后续计算若确定它，才可将其实际次数代入结论。

## 1. 原模块与已经支付的支撑

令 $R_0=\mathbb Q[s]$，保持原十七式、全部 $m$ 次数至多三的 $6188$ 个来源，以及全部次数一至五的 $4367$ 个目标：
$$
A:R_0^{6188}\longrightarrow V=R_0^{4367},\qquad L=\operatorname{im}A.
$$
原二项式共动坐标是多项式单位变换。令 $W\subset V$ 为 normal 次数至少二的坐标子模；它是秩 $4212$ 的直和项。原九个目标为
$$
t_j=\left(\sum_{a=0}^j\binom ja(-s)^{j-a}m_a\right)^2,\qquad 2\le j\le10,
$$
且全部属于 $W$。令 $\overline L=(L+W)/W$，并置
$$
C=V/L,\qquad C_P=(V/W)/\overline L,\qquad
T=W/(L\cap W).
$$

原完整投影 $P\in R_0^{224\times155}$ 使用一百七十个纯切向来源和五十四个真实 $g$ 倍单坐标来源，其中
$$
g=-2s^2(s-2)(s+6).
$$
它满足 $C_P=\operatorname{coker}P^{\mathsf T}$。此身份是原来源级身份，不能在接触点将 $g$ 倍行换成裸单位行。参见[原局部投影与差长](R150-appendix-original-local-projection-length-gap-and-two-point-length-bound30.md)。

已证明的泛秩为
$$
\operatorname{rank}_{\mathbb Q(s)}A=4354,\qquad
\operatorname{rank}_{\mathbb Q(s)}P=142.
$$
因此 $W\subset L\otimes\mathbb Q(s)$，$T$ 是有限扭模，而 $C,C_P$ 的自由秩均为 $13$。

记已知临界多项式
$$
\Sigma_0=s(s-2)(s+6)F_+F_-E_8,
$$
以及
$$
h_*=s^3F_+^2F_-^2E_8.
$$
以下已付局部结论始终针对同一原来源模块：

- 在 $s=0$，$s^3t_j\in L_{(s)}$，其中 $t_2$ 恰需三次。
- 在 $s=2$ 和 $s=-6$，全部 $t_j$ 本身已在原局部像中。
- 在 $F_+$、$F_-$ 的各共轭点，$F_\pm^2W_{(F_\pm)}\subset L_{(F_\pm)}$。
- 在 $E_8$ 的各共轭点，$E_8W_{(E_8)}\subset L_{(E_8)}$。

所以 $h_*t_j$ 在 $\Sigma_0$ 的全部局部点属于原像。这不预设其他有限点没有来源扭子。

上述范围分别来自[零点完整桥](R150-appendix-original-generic-image-bridge-exact-cubic-zero-cost-and-thirteen-free-heads.md)、[二点完整长度十二](R150-appendix-two-complete-third-connection-smith12-and-all-original-square-local-membership.md)，以及[低投影双线性确定因子与 E8](R150-appendix-original-low-projection-double-linear-divisor-and-E8-local-target-membership.md)及其所引两三次域证明。

## 2. 精确序列的扭长恒等式

自然映射给出
$$
0\longrightarrow T\longrightarrow C\longrightarrow C_P\longrightarrow0.
\tag{2.1}
$$
固定任意首一不可约 $f\in R_0$，在 DVR $R_{0,(f)}$ 上局部化。记两个余核的扭子模分别为 $C_{\mathrm{tor}},(C_P)_{\mathrm{tor}}$。

这里扭子模也组成短正合列：
$$
0\longrightarrow T_{(f)}
\longrightarrow C_{\mathrm{tor},(f)}
\longrightarrow (C_P)_{\mathrm{tor},(f)}
\longrightarrow0.
\tag{2.2}
$$

证明不能只援引左右余核的自由秩相等。因为 (2.1) 满射，诱导的自由商映射
$$
C_{(f)}/C_{\mathrm{tor},(f)}
\longrightarrow
(C_P)_{(f)}/(C_P)_{\mathrm{tor},(f)}
$$
仍满射；两端均为同秩 $13$ 的自由 DVR 模，故该映射是同构。因此任意右侧扭元素的原像在左侧自由商中为零，已经属于左侧扭子模。这证明扭满射及 (2.2)。

令 $\Delta_A,\Delta_P\in\mathbb Q[s]$ 分别为原 $A$ 和 $P$ 的全部非零最大子式 gcd，取首一代表。Smith 标准形将它们识别为相应有限扭子的确定因子。由 (2.2)，
$$
\boxed{
\operatorname{length}_{R_{0,(f)}}T_{(f)}
=v_f(\Delta_A)-v_f(\Delta_P).
}
\tag{2.3}
$$
特别是右端非负，而且任何 $t_j$ 在 $T_{(f)}$ 中的类都被
$$
f^{\,v_f(\Delta_A)-v_f(\Delta_P)}
$$
消去。这里使用“扭模长度支配每个正 Smith 指数”，不假设 $T$ 是循环模。

## 3. 外投影因子的定义与真实全局消除

已付完整公共因子为
$$
K=K_{158}
=s^{66}(s-2)^{12}(s+6)^{12}F_+^6F_-^6E_8^4,
\qquad K\mid\Delta_A.
$$
置 $R=\Delta_A/K$，忽略无关非零有理常数。令 $R_{\mathrm{out}}$ 是 $R$ 的全部 $\Sigma_0$ 外因子，即
$$
R_{\mathrm{out}}
=\prod_{f\nmid\Sigma_0}f^{v_f(\Delta_A)}.
$$
最新[完整无穷远第七连接及下界 $63$](R150-appendix-infinity-complete-seventh-connection-one-sixteen-heads-and-length63.md)与[射影 gcd 次数上界 $381$](R150-appendix-full-projective-divisor-degree381-and-residual-multiplier170.md)共同给
$$
\deg\Delta_A\le318,\qquad
\deg R_{\mathrm{out}}\le\deg R\le160.
\tag{3.1}
$$

定义
$$
\boxed{
\Omega=\prod_{f\nmid\Sigma_0} f^{v_f(\Delta_P)},\qquad d=\deg\Omega.
}
\tag{3.2}
$$
这是原完整投影在已知支撑之外的精确确定因子；不是某一个选定子式，也不是有限域 $Q_{60}$ 的未经提升猜测。由 (2.3)，
$$
\Omega\mid R_{\mathrm{out}},\qquad
0\le d\le\deg R_{\mathrm{out}}\le160.
\tag{3.3}
$$
因此
$$
M:=R_{\mathrm{out}}/\Omega\in\mathbb Q[s]\setminus\{0\},
\qquad \deg M\le160-d.
$$

对每个 $f\nmid\Sigma_0$，$v_f(M)$ 准确等于 (2.3) 的差长，故 $M[t_j]=0$ 于 $C_{(f)}$。对每个 $f\mid\Sigma_0$，$M$ 是局部单位，而第 1 节已知 $h_*[t_j]=0$。于是 $Mh_*[t_j]$ 在所有有限不可约局部化中为零。

有限生成 $R_0$ 模的元素若在所有极大理想局部化中为零，则该元素为零。因此
$$
\boxed{
Mh_*t_j\in L\quad(2\le j\le10),\qquad
\deg M\le160-d,\qquad
\deg(Mh_*)\le183-d.
}
\tag{3.4}
$$
同一个 $M$ 同时适用于九个目标。

更精确地，若 $U$ 是九目标联合最小消去多项式在 $\Sigma_0$ 外的部分，则逐不可约因子的同一论证给
$$
\boxed{U\mid R_{\mathrm{out}}/\Omega.}
\tag{3.5}
$$
故消除 $\Omega$ 直接减少未知目标乘子，并非仅仅发现两个余核共有某种扭子。

## 4. 与真实 56×22 原矩阵的联系

[原投影的 56×22 符号 Schur](R150-appendix-original-projection-away-from-critical-support-56-by-22-schur.md)在
$$
S=\mathbb Q[s,\Sigma_0^{-1}]
$$
中给出原来源级等价
$$
C_P\otimes S\simeq S^{13}\oplus\operatorname{coker}_S G^{\mathsf T}.
$$
该归约分离十三个真实归一自由核、五十四个真 $g$ 单位、三个纯列以及七份同一 $H_9$ 单位，保留全部余行。四层分母只含 $D_{\mathrm{lin}}$，其支撑包含于 $\Sigma_0$。

所以对真实多项式清分母矩阵 $\widetilde G$ 求全部二十二阶子式 gcd，再只剥 $\Sigma_0$ 因子，正好得到 (3.2) 的 $\Omega$。本篇不预填此 gcd 的实际值。

若后续只证明某个首一 $\Omega_0\mid\Omega$，则 $R_{\mathrm{out}}/\Omega_0$ 仍是合法较弱的九目标额外乘子；同下文只须以 $\deg\Omega_0$ 代 $d$。单个子式的因子或单素数上的因子并不自动满足该前提。

## 5. 同一原 I、J、B 上的完整来源降度

保持[原来源成本证明](R150-appendix-global-residual-multiplier-nine-sources-cost8531.md)中的同一 $I,J$、
$$
B=A_{I,J},\quad D=\det B,\quad H=8770,
$$
以及已付界
$$
8527\le\deg D\le8640,
$$
$$
v_\infty D\ge130,\qquad
v_\infty(\text{全部原来源换列子式})\ge125,\qquad
v_\infty(\text{全部 cofactor})\ge125.
$$
来源权仍为
$$
a_{m^\alpha N_i}=20+10|\alpha|,\qquad
a_{m^\alpha\Gamma_i}=25+10|\alpha|,\qquad
\delta_\ell=a_\ell-10,\qquad |\alpha|\le3.
$$

因为 $\Omega$ 与 $K$ 互素，而 $\Omega\mid\Delta_A$，新的真正完整公共因子是
$$
K'=K\Omega,\qquad\deg K'=158+d.
$$
令
$$
d_*=D/K',\qquad q=\deg d_*.
$$
这仍是同一原 $D$ 的多项式商，且
$$
8369-d\le q\le8482-d.
\tag{5.1}
$$
由 $d\le160$，特别有 $q\ge8209>0$，所以以下余式整理不出现零次除数或非法负度支路。

对每个原来源列定义
$$
P_\ell=\operatorname{adj}(B)(A_\ell)_I/K'.
$$
每个坐标都是一个原最大换列子式除以 $K'$，因此均为多项式。并且
$$
A_JP_\ell=d_*A_\ell
\tag{5.2}
$$
在全部 $4367$ 个输出上成立：原输出限制在函数域像上单射，不能只保所选四千余行。

固定目标 $b=Mh_*t_j$。式 (3.4) 已给真实多项式来源 $Ax=b$，因此
$$
T_b=\operatorname{adj}(B)b_I/K'
=\sum_\ell P_\ell x_\ell
\in\mathbb Q[s]^{4354}.
\tag{5.3}
$$
没有从未付的原 $h_0$ 成员性推断这个整除。

对每个非基来源 $\ell\notin J$ 作
$$
x_\ell=d_*v_\ell+r_\ell,\qquad\deg r_\ell<q.
$$
置
$$
y_\ell=r_\ell\quad(\ell\notin J),\qquad
y_J=x_J+\sum_{\ell\notin J}P_\ell v_\ell.
$$
由 (5.2)，$Ay=b$，且准确基来源等式为
$$
d_*y_j=(T_b)_j-\sum_{\ell\notin J}(P_\ell)_j r_\ell.
\tag{5.4}
$$
这与原余式证明完全同一 $J,B$；没有重选一个未核的较优子式。

## 6. 三个成本支路及其范围

因为 $b$ 仍仅含二次 $m$ 输出，原输出权为 $20$，所以
$$
\tau(b):=\max_i\bigl(\deg b_i+b_i^{\mathrm{wt}}\bigr)
\le (160-d)+23+20+20=223-d.
\tag{6.1}
$$
此处原目标 $t_j$ 的参数次数至多 $2j\le20$，而 $h_*$ 的次数准确为 $23$。

以新的完整因子 $K'$ 代入同一换列及 cofactor 上界：
$$
\deg(P_\ell)_j\le H-a_j+a_\ell-125-(158+d),
$$
$$
\deg(T_b)_j\le H-a_j+\tau(b)-125-(158+d).
$$
由 (5.1)、(5.4) 及 $\delta_j=a_j-10$，三个真实成本支路为
$$
\begin{aligned}
\text{非基来源}
&\le (8482-d)-1+45=8526-d,\\
\text{原来源转移}
&\le8770+55-125-(158+d)-11=8531-d,\\
\text{目标伴随}
&\le8770+(223-d)-125-(158+d)-10-(8369-d)\\
&=331-d.
\end{aligned}
\tag{6.2}
$$
在已经证明的 $0\le d\le160$ 范围内，第三支仍介于 $171$ 和 $331$ 之间，三个支路均非负。故
$$
\boxed{
\exists\,y^{(2)},\ldots,y^{(10)}:
\quad Ay^{(j)}=Mh_*t_j,\quad
\operatorname{cost}(y^{(j)})\le8531-d.
}
\tag{6.3}
$$

这是同一原次数至多三来源模块内的存在与次数界，不提供 $M$ 或来源的展开系数，不界定系数高度，也不提供固定 $31$ 分母。若实际证明 $d=\deg R_{\mathrm{out}}$，才可进一步断 $M$ 为常数并关闭原 $h_*$、等价地原 $h_0$ 的九列全局成员性。当前没有预设这一等号。
