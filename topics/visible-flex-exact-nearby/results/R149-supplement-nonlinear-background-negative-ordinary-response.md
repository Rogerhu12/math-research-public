# 真非线性背景的全频负侧响应与普通径向误差

固定同一物理 $\eta_0$、选定的 $\nu=\nu_0+\delta_*$ 和 $Q=Q_{\delta_*}$。对实背景 $T=Q+p$，令 $\mathcal W$ 为物理频率 $k=4j$、权 $(1+|k|)^{1/3}$ 的 Fourier Wiener 空间，两行取和。置
$$
 t=\mathop{\rm ess\,sup}_{[0,r_+]}\max(\|p\|_{\mathcal W},\|p_\phi\|_{\mathcal W}).
$$
**已证明**下式对每个 $t\le10^{-7}$ 的背景成立，$p$ 可以有无限 Fourier 支集。对该背景实际 regular 方程的参数切向量 $q_\nu$，令 $e=q_\nu-Z$、$B=\|e(r_*^-)\|_{H^{1/3}\oplus L^2}$ 和 $V=\mathop{\rm ess\,sup}_{[r_*,r_+]}\|e\|_2$。$J_0,J_1$ 分别是在 $[0,c]$、$[c,r_*]$ 的真实独立跳之普通、mixed 范数之和，$c=r_+-1/200$。在 $c$ 的一枚跳只付一次，根处实际匹配差已进入左迹 $B$。在整段普通测度上有
$$
 \boxed{\|e\|_{L^2([0,r_+];L^2)}\le
 25.944(B+J_1)+3.973J_0+9.49\,10^{-7}V+1.755\,10^{-5}+5100t.} \tag{NBE.1}
$$
因此连续物理解若实际满足上述球及 $B\le.000170, V\le1$，右端小于 $.005$。这是对真实变化算子的 Cauchy 结论。此处尚未得到 nonlinear correction 的实际 $t$、完整边界匹配后的 $B,V$。能量估计不需要 $q_\nu$ 的角导上界。$[r_*,r_+]$ 宽至多 $9\,10^{-13}$，正侧用真态自身的普通 sup；若区间退化则该项为零。

## 四个真实径向系数

[D.5–6,19–20](R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md) 的逐行费用为明确非负项之和。[43713242980/1](R133-supplement-actual-selected-parameter-core-scalar-fees-and-collar-jets.md) 的 fixed-negative 最大 $M_0<6.051\,10^{-8},N_\nu<1.639\,10^{-6}$。记 $d=10^{-10}, E=19d,H=83d,U=14E+E^2,D=(7+E)^2$。令 $b=|\beta|\max(1,|K|)$、$g=|\gamma|\max(1,|K|)$、$b'=|\beta K_\nu|$、$g'=\|\partial_\nu(\gamma J(K))\|$，均取真物理系数。原正预算逐项支配
$$
 M_0\ge b[3U+(6E+(7+E)H)/2]+gH,\qquad
 N_\nu\ge b'[6U/4+DH/4+7U+DE]+g'[6E+(7+E)H].
$$
第二式在真实 compact bump 外两被界量均为零。因此完整 $[0,r_+]$ 有
$$
                  b<.53,\quad g<7.3,\quad b'<4,\quad g'<24.       \tag{NBE.2}
$$
这里使用原明定的正费用，不从算子真实范数的 upper 倒推某项。$Q,Z$ 的原始 $A^0$ 两行和及角导分别小于 $7,6,19,83$；对 $Q$ 使用原实际 $6.407,5.438$ 的余量。由于 $Q_0$ 仅到物理频率128，$Z$ 至384，分别转换 $Q=Q_0+\delta_*Z$ 的两项，$129^{1/3}<5.06,385^{1/3}<7.28$。因此可用
$$
 (\|Q\|_{\mathcal W},\|Q_\phi\|_{\mathcal W},
 \|Z\|_{\mathcal W},\|Z_\phi\|_{\mathcal W})<(33,28,139,606).       \tag{NBE.3}
$$
$J$ 和参数导每行每列各至多一个非零元，两行和算子范数与欧氏算子范数相同。$\mathcal W$ 次乘且支配完整 $H^{1/3}$；由 $\langle k+l\rangle\le(1+|l|)\langle k\rangle$ 和卷积不等式，$\|af\|_{H^{1/3}}\le\|a\|_{\mathcal W}\|f\|_{H^{1/3}}$。

## 同背景的真实参数源与 Newton 余项

令 $s(T)=F_\nu(T)+A(T)Z-Z_r$。真 $e$ 的方程是 $(\partial_r-A(T))e=s(T)$。写 $a=33,a_1=28,z=139,z_1=606$。在固定真实 metric 作 D.4 的逐项差；$I$ 的 $\mathcal W$ 范数为 $1/4$。当 $0\le t\le1$，principal、lower-order 两类带权系数的状态差至多 $m_1t,m_0t$，其中
$$
 m_1=.53(2a+1)/4+7.3,\quad m_0=3(.53)(2a+1)+.53(a_1+a+1)/2+7.3 .
$$
例如 primitive 项的两个因子差是 $p_\phi I(Q_K Z)+T_\phi I(p_K Z)$，$Q_K=(u,Kv)$。独立 mean 的 principal 与 rank 两项均保留。D.17 的 $F_\nu$ 差用 $\Delta(v^2)$ 乘未变的 $Q,Q_\phi$，再加 $v_T^2(p,p_\phi)$ 与完整 mean 的变化。因此
$$
 \|s(T)-s(Q)\|_{H^{1/3}}\le t\{m_1z_1+m_0z+
 4[(2a+1)(a_1/4+a)+(a+1)^2(1/4+1)]+24(a_1+a+1)\}\le46000t .       \tag{NBE.4}
$$
原 $F$ 的完整 Newton 二阶及三阶余项 $\|F(Q+p)-F(Q)-A(Q)p\|_{H^{1/3}}$ 逐点至多
$$
 t^2\{.53[a_1/4+a/2+3a+1/4+1]+7.3\}\le74t^2 .                    \tag{NBE.5}
$$
二次项含 $I(p_Kp)Q_\phi,2I(Q_Kp)p_\phi$、三个局部项及 $\langle p_2\rangle\gamma Jp_\phi$；三次项含 $I(p_Kp)p_\phi,(p_Kp)p$。在 $[c,r_*]$，compact bump 及其参数导准确为零，所以 (NBE.4) 只需前两项，小于 $28000t$。在严格段 $[0,c]$ 的普通源，仅需 $A^0$ 乘法，把同式中的 $(a,a_1,z,z_1)$ 换成 $(7,6,19,83)$ 得 $2600t$。两式接收变化产生的所有新频率。同一真实体方程的 state jumps 另计。

## 严格负段保留真实主部

用 [NRO.1](R149-supplement-ordinary-negative-response-from-the-strong-positive-root.md) 的 $q=\sqrt{-K}$ 和 $(h_1/q,h_2)$。$T$ 的两类主导输运仍分别是标量漂移与角常实对称系数，后者即使 mean 改变也不给实能量费用。局部反应两个交叉项仍逐点反对称。标量漂移对角的增加与局部反应之和至多 $3.5(.53)(2\cdot7+1)t$。这是因为 $\partial I=P_{\ne0}$ 在 $A^0$ 收缩，两条局部对角各按自身 supremum 比较。primitive 的两个实际乘法因子变化增加至多 $.53(1.03)^2(7+6+1)t/2$；真 mean-rank 的新导数同常输入向量正交，费用至多 $7.3(1.03)t/2$。三者合计小于 $36t$。任意严格反向子段的普通传播范数至多 $8.22e^{36ct}<8.22001=:U'$。

## 真实根能量容纳无限频背景差

用 [E.2–9](R133-supplement-full-real-large-root-Cauchy-two-source-windows.md) 的原 $M=(\theta/w,\theta)$ 与 $a_*=13/10$。原 $R=1/200$ 行给 $|\eta|<1.254,q<1.03,W<1.44$。新 $|\eta_T|\le|\eta|+7.3t<13/10$，所以 E.5 的全部反对称主部、耗散与真 $K_r$ 费用均用原界。当 $k,l$ 为物理输入频率与频移，E.4 给
$$
 |M_i(k+l)/M_i(k)|\le(1+|l|)^{1/3},\quad
 |k|\,|M_i(k+l)/M_i(k)-1|\le(1+|l|)^{1/3}|l|.
$$
这是原乘子导数逐对频率的推论，适用所有 $l$。保留旧实际 $G_0$ 全额，仅给背景差增加下列增长率，每项的表值须再乘 $t$。

|项|逐径向增量上界（除去 $t$）|
|---|---:|
|输运实能量与换序|$1.5(.53)(2\cdot33+1)$|
|两个局部对角|$4(.53)(2\cdot33+1)$|
|两个交叉局部|$4(1.03+1.44)2(.53)(7+1)$|
|完整 primitive|$2(4\cdot1.44)(.41)(.53)(7+28+1)$|
|独立 mean rank|$4(7.3)$|

前两行用 $\mathcal W$ 差以及上述无截断乘子。第三行在原次序用 $q^2/w\le q,w\le W,\theta^{-1}<4$ 与 $\Delta(uv)$ 的 $A^0$ 差。第四行用 $\|M^{-1}\|\le4W$、$L^2\overset{I}{\longrightarrow}H^{1/3}$ 的 $.41$，两外乘子再用 $\mathcal W$。第五行 $|\langle h_2\rangle|\le4\|Mh\|$。合计小于 $600t$。因此原 [43621934843/1](R133-supplement-actual-full-real-large-root-Cauchy-energies.md) 真根到任一点的完整混合数据增益至多 $6.531704e^{600t/200}<6.53171=:C'$。用原 Fourier 截断的统一估计、弱极限与零初值唯一性给全频能量解；无限支集系数按绝对加权卷积收敛。

## 全固定窗

对真根迹与根段每一原子，普通径向增益是 $C'\sqrt{1/200+c(U')^2}<25.944=:A'$；严格段每个原子小于 $\sqrt cU'<3.973$。对旧已知 $s(Q)$，其 low/root 和全部高源及大小完全没有改变。只把 [NHT.7](R149-supplement-selected-complete-high-Newton-and-nu-from-the-Z-tail.md) 的 $8.22,25.943$ 两个增益换为 $U',A'$，其右边相对原式小于 $1.00004$ 倍，故仍小于 $1.755\,10^{-5}$。对新增的 $s(T)-s(Q)$，使用 (NBE.4) 的逐点强上界。根段付 $28000tA'/200$；严格段从 $r$ 的真正积分长度为 $c-r$，平方积分给 $2600tU'\sqrt{c^3/3}$。两项合计小于 $5100t$。最后从 $r_*$ 到 $r_+$ 加 $\sqrt{9\,10^{-13}}V$ 即得 (NBE.1)。这项正侧观测须在 $T$ 处联立真实 root-even/outgoing、height、Robin、mean、holonomy 与外边界；$Q$ 处原强图不自动适用于 $T$。
