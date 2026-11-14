# R239 附录：首源头的裸／完整右度量分裂与真实强制坐标的小量承载

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。
状态：以下首头正交分裂、同源能量配对、真实强制坐标趋零及远低 Schur 的中间带承载已证明。最后一节只完成右侧度量中的测试互补，不宣称完整左费用上界。

依赖：[原完整源坐标](R239-appendix-complete-source-schur-coordinates-and-growing-head-observation.md)、[原全部自由旗及顺次右链](R271-appendix-source-primitive-jets-and-sequential-right-chain.md)、[远低 Schur 局部化](R271-appendix-primitive-bandwidth-and-far-schur-localization.md)及[原首头完整最小链](../notes/2026-11-13-actual-high-hole-first-head-tests-and-transverse-observation-gap-1cf.md) §2。

## 1. 同一个原首源头的两种最小链

固定原 $m\ge5,d=2^m$、$4d\le q\le e^{d^3/4}$，写 $A=A_m,D=D_m$。
完整首源空间为
$$
\mathscr R_q=\bigoplus_{i=0}^{d-2}e_iE_{d-i-1,q},
\qquad E_{h,q}=\ker D^h\cap\mathcal H_q.
$$
令 $P$ 为源空间中第零头的原物理正交投影。
裸右最小链与完整右最小链分别记为 $\mathcal R_b$、$\mathcal R_f$，其范数为 $\alpha_q(r)$、$\lambda_q(r)$。前者在原低出生空间 $Z_q=\ker S_L$ 内取最小，后者在原完整右旗 $\ker S$ 内取最小。

取任意 $h\in E_{d-1,q}$，令 $R_1=D_{q+1}^{\dagger}$ 是固定层的真正单步 MP 逆。定义
$$
(k_h)_1=e_0R_1h,\qquad (k_h)_t=0\quad(t\ge2).
\tag{1.1}
$$
由于 $D^dR_1h=D^{d-1}h=0$，首段第零头的完整尾核旗满足；$Ae_0=0$ 使所有内部及最右输出为零，而首输出恰为 $e_0h$。第一段的整个允许尾旗属于原低出生空间：其相对出生为 $2-b\le1$，其中尾核高度 $b\ge1$。故 (1.1) 同时是裸和完整的合法链。

任意同首源链的首段第零头都必须解 $Dz=h$。固定层 MP 最小性给其范数至少 $\|R_1h\|$；(1.1) 达到下界。因此
$$
\boxed{\mathcal R_b(e_0h)=\mathcal R_f(e_0h)=k_h.}
\tag{1.2}
$$
这里涵盖全部 $E_{d-1,q}$，没有限制 $h$ 为 primitive。

若另一原源 $r$ 满足 $Pr=0$，则任何可行链的首段第零头 $c_{1,0}$ 满足 $Dc_{1,0}=0$。由于 $R_1h\perp\ker D$，
$$
\langle k_h,c\rangle=0.
\tag{1.3}
$$
(1.3) 对裸或完整可行链均成立，不依赖它是否最小。

## 2. 两个右源 Gram 的真正约化块

记
$$
J_{b,q}^{-1}=\mathcal R_b^*\mathcal R_b,
\qquad
G_q^{-1}=\mathcal R_f^*\mathcal R_f.
$$
全部算子都在同一个原 $\mathscr R_q$ 上。由 (1.2)–(1.3)，
$$
\boxed{[P,J_{b,q}^{-1}]=[P,G_q^{-1}]=0,}
\tag{2.1}
$$
且二者在 $P\mathscr R_q=e_0E_{d-1,q}$ 上相同，准确为
$$
\boxed{K_{0,q}:=(R_1|_{E_{d-1,q}})^*(R_1|_{E_{d-1,q}}).}
\tag{2.2}
$$
$K_{0,q}$ 是原短核输入空间上的实际压缩 Gram，不是未证可交换的 $DD^*$ 压缩逆。它有界严格正，因为 $DR_1h=h$ 给 $\|R_1h\|\ge\|h\|/\|D\|$。

这些源 Gram 均有有界逆，故 (2.1) 也给
$$
[P,J_{b,q}]=[P,G_q]=0,\qquad
G_q|_{P\mathscr R_q}=J_{b,q}|_{P\mathscr R_q}=K_{0,q}^{-1}.
\tag{2.3}
$$
特别，对每个原源 $r$，准确有
$$
\boxed{
\begin{aligned}
\alpha_q(r)^2&=\alpha_q(Pr)^2+\alpha_q((I-P)r)^2,\\
\lambda_q(r)^2&=\lambda_q(Pr)^2+\lambda_q((I-P)r)^2,\\
\alpha_q(Pr)&=\lambda_q(Pr).
\end{aligned}}
\tag{2.4}
$$
本节没有证明左源 Gram $J_q$ 与 $P$ 交换。

## 3. 同一个真实左源的首头能量配对

对任意原源，置
$$
y=J_q^{-1}r,\qquad r^\flat=G_qy,
\qquad \lambda_{\rm flat}(r)=\lambda_q(r^\flat)=\|G_q^{1/2}y\|.
$$
令 $r_0=Pr$、$y_0=Py$。由 (2.3)，在同一个第零源头的 Hilbert 空间中作加权 Cauchy，得
$$
\begin{aligned}
|\langle r_0,y_0\rangle|
&\le\|K_{0,q}^{1/2}r_0\|\,
      \|K_{0,q}^{-1/2}y_0\|\\
&=\alpha_q(r_0)\,\|G_q^{1/2}y_0\|.
\end{aligned}
$$
由 (2.4) 和 $G_q$ 的约化性，得到
$$
\boxed{
|\langle Pr,PJ_q^{-1}r\rangle|
\le\alpha_q(r)\lambda_{\rm flat}(r)
\le\tfrac12\bigl(\alpha_q(r)^2+\lambda_{\rm flat}(r)^2\bigr).
}
\tag{3.1}
$$
两个泛函始终来自同一个 $r$ 和同一个 $y$，没有用 $J_q^{-1}Pr$ 替换 $PJ_q^{-1}r$。

若 $r$ 或 $J_q^{-1}r$ 支持在第零源头，则整个左能量 $\mu_q(r)^2=\langle r,J_q^{-1}r\rangle$ 正好是 (3.1) 的配对。因此这两个准确源锥均满足
$$
\boxed{\mu_q(r)^2\le\alpha_q(r)\lambda_{\rm flat}(r).}
\tag{3.2}
$$
一般来源仍保留其余源头的配对，不将它们丢弃。对任何已经支付 $\alpha_q(r_m)\to0$、$\lambda_{\rm flat}(r_m)\to0$ 的同源序列，首头配对趋零；若左费有正极限，剩余源头必须承载该能量。这里未声称各剩余头的单项配对均为非负。

## 4. 强制三角坐标中的整条最小头对角

沿完整源坐标稿写
$$
a=\Gamma_qr\in\mathscr U_q
=\bigoplus_{t=0}^{d-2}H_{\ge t+1}\otimes K_{q-t},
\quad B_U=\Gamma_q^{-1},
$$
$$
\mathcal G_q\succeq I,\qquad
\mu_q(r)^2=\langle\mathcal G_qa,a\rangle,
\quad
\mathcal F_q=B_U^*J_{b,q}^{-1}B_U,
\quad
\mathcal H_q=\Gamma_qG_q\Gamma_q^*.
$$
定义源首头在这些坐标中的实际投影
$$
\boxed{\Pi_q=\Gamma_qPB_U.}
\tag{4.1}
$$
它一般不是原无权坐标内积中的正交投影，不能把它换成删除若干坐标。

记原非零权积
$$
\gamma_t=(A^{t+1})_{0,t+1}>0.
$$
源 jet 公式给
$$
\boxed{
(\Pi_qa)_t
=\gamma_t^{-1}e_{t+1}\otimes
(e_0^*A^{t+1}\otimes I)a_t.
}
\tag{4.2}
$$
其范围恰为
$$
\boxed{\mathscr D_q
=\bigoplus_{t=0}^{d-2}\mathbb Ce_{t+1}\otimes K_{q-t}.}
\tag{4.3}
$$
满射性可直接由 $B_U$ 核验：任意 (4.3) 的坐标经 $B_U$ 作用都只落在第零源头；反之 (3.4) 的实际头逆把第零源头 jet 送到 $e_{t+1}/\gamma_t$。

由 (2.1)，$\Pi_q$ 同时是两种正度量中的正交投影：
$$
\boxed{
\Pi_q^*\mathcal F_q=\mathcal F_q\Pi_q,
\qquad
\Pi_q^*\mathcal H_q^{-1}=\mathcal H_q^{-1}\Pi_q.
}
\tag{4.4}
$$
而二者在该范围上相同：
$$
\boxed{\Pi_q^*\mathcal F_q\Pi_q
=\Pi_q^*\mathcal H_q^{-1}\Pi_q.}
\tag{4.5}
$$
因此首头结论对应整个强制三角坐标的最小头对角 $i=t+1$，横跨全部 $t$；它不只处理顶层 $a_0$。同时，$\Pi_q$ 的无权范数和它与左度量 $\mathcal G_q$ 的关系仍须保留。

## 5. 真实来源的全部强制坐标趋零

现在固定一个原 $w\in W$，令 $m\to\infty$，在原合法窗选 $q=q_m$，并采用已有实际低投影来源
$$
\bar v_m=P_{\mathscr V_{q_m}}w,\qquad
r_m=E_{q_m}\bar v_m,\qquad
v_m=E_{q_m}^{\dagger}r_m.
$$
原低投影和有限 $L_m$ 核提升估计已经给 $v_m\to w$。这里不重新更换其来源。令
$$
p_m=P_0^{(m)}v_m,\qquad a_m=P_{\mathscr U_{q_m}}p_m=\Gamma_{q_m}r_m.
$$
$P_0^{(m)}$ 保孔层，且强制空间只位于
$[q_m-d+2,q_m]$，故
$$
\boxed{
\|a_m\|
\le\|P_{[q_m-d+2,q_m]}^{(m)}w\|+\|v_m-w\|
\longrightarrow0.
}
\tag{5.1}
$$
为核对最后的极限，尾真空投影随 $m\to\infty$ 强趋于单位，且该孔带至少为一孔，所以第一项趋零。原窗亦有 $q_m-d\to\infty$。

尾真空子空间包含在 $\ker D_m$ 中，因此 $P_0^{(m)}\to I$ 强成立。结合 $v_m\to w$，还有
$$
\boxed{p_m\to w,\qquad
\|(I-P_0^{(m)})v_m\|\to0.}
\tag{5.2}
$$
因此“大 Schur 费用”不等于说真实 $v_m$ 的物理非primitive部分占大质量；它可以由全部自由坐标的消元和相消承载。

若 $w\ne0$，则 $\mu_{q_m}(r_m)=\|v_m\|\to\|w\|>0$，$a_m$ 最终非零，且
$$
\boxed{
\frac{\langle\mathcal G_{q_m}a_m,a_m\rangle}{\|a_m\|^2}
\longrightarrow\infty.
}
\tag{5.3}
$$
这是在非零真实缺陷假设下的必要放大，不是反证；此前并无相反的一致上界。

## 6. 远低 Schur 将这一必要重建定位到中间边界带

沿 R271 的第一层 Schur，按 primitive 孔数写
$$
p_m=(u_m,b_m),\qquad
u_m\in\mathscr P_{\rm lo}:=\mathbb C^d\otimes\!\bigoplus_{n\le q-d+1}K_n,
\quad
b_m\in\mathscr P_{\rm bd}:=\mathbb C^d\otimes\!\bigoplus_{q-d+2\le n\le q}K_n.
$$
此节 $u_m$ 是坐标向量，不是尾算子范数。
真实最小性给
$$
u_m=-D_{00}^{-1}D_{01}b_m.
\tag{6.1}
$$
由 (5.2) 和同一孔带估计，$b_m\to0$、$u_m\to w$。

先取原已付的最后 $d/8$ 层 $\mathscr P_{\rm top}$，令
$b_m=b_m^{\rm top}+b_m^{\rm mid}$。远低 Schur 稿证明
$$
\|D_{00}^{-1}D_{01}b_m^{\rm top}\|
\le e^{-d^4/5}\|b_m^{\rm top}\|.
$$
因此
$$
\boxed{
-D_{00}^{-1}D_{01}b_m^{\rm mid}\longrightarrow w,
\qquad b_m^{\rm mid}\longrightarrow0.
}
\tag{6.2}
$$
对非零 $w$，这给实际中间带方向上的放大比趋于无穷。中间带包含全部头坐标，尚未被替换成只含强制坐标的子带；其自由头分量也由真实 Schur 耦合决定。

### 6.1 可把已排顶带扩大到最后 d/4 层

当 $m\ge7$，令 $r=d/4$、$\mathscr P_{\rm top}^{(1/4)}$ 为最后 $r$ 个 primitive 孔层。沿用 R271 的准确系数
$$
w_t=\exp[t\Theta-\gamma(t-m)_+^4],\qquad
\gamma=770/256,\quad\Theta<d^3/2+11.
$$
其同一个交叉块证明给
$$
\|P_{\rm lo}\mathcal D P_{\rm top}^{(1/4)}\|
\le d^2\exp[(d+r)\Theta-\gamma(d-r-m)^4].
$$
$m/d\le7/128$，故 $d-r-m\ge(89/128)d$。准确常数是
$$
\gamma(89/128)^4-5/8
=\frac{2680926305}{34359738368}>\frac3{40}.
$$
而 $2\log d+(55/4)d\le d^4/80$ 对 $d\ge128$ 成立，因而
$$
\boxed{\|P_{\rm lo}\mathcal D P_{\rm top}^{(1/4)}\|
\le e^{-d^4/16}.}
\tag{6.3}
$$
同一个 $D_{00}\succeq I$ 给该顶带的 Schur 修正不超过 $e^{-d^4/8}I$，最小远低补全范数不超过 $e^{-d^4/16}\|b\|$。

所以 (6.2) 也可把中间带准确缩到
$$
\boxed{q-d+2\le n\le q-d/4.}
\tag{6.4}
$$
它仍不是完整源 Schur 的带支撑定理：继续消去边界自由头旗时，可能产生新的间接耦合，不能把 (6.4) 直接解释为 $a_m$ 只在此带内承载全部能量。

## 7. 首头与增长头测试在右度量中的稳定分裂

取增长头稿的一条实际右测试链映射 $c=\mathcal C_R:\mathscr Z\to\ker S$，满足 $\|c\|\le\varepsilon$。其源为 $r_{m test}=F_{\rm flag}c$，坐标映射为
$$
S=\Gamma_qF_{\rm flag}c.
$$
对每个输入，令 $c_0$ 是 (1.1) 对首头源 $Pr_{m test}$ 的链，置 $c_1=c-c_0$。

首段第零头上的单步 MP 分解说明 $c_0$ 是 $c$ 到闭零返回子空间
$$
\mathscr K_0=\{k_h:h\in E_{d-1,q}\}
$$
的物理正交投影：$D^{\dagger}D c_{1,0}=P_{(\ker D)^\perp}c_{1,0}$，且 $c_{1,0}\in\ker D^d$。因此
$$
\boxed{c_0\perp c_1,\qquad
\|c_0z\|^2+\|c_1z\|^2=\|cz\|^2.}
\tag{7.1}
$$
两者均在原完整右旗；其源分别为 $Pr_{m test}$ 和 $(I-P)r_{m test}$。

定义
$$
S_0=\Gamma_qF_{\rm flag}c_0=\Pi_qS,
\qquad
S_1=\Gamma_qF_{\rm flag}c_1=(I-\Pi_q)S.
$$
由 (4.4)，两源测试在 $\mathcal F_q$ 和 $\mathcal H_q^{-1}$ 度量中正交。对同一个任意实际源 $r$，完整配对还给
$$
S_j^*\mathcal G_q\Gamma_qr=c_j^*c^\flat\qquad(j=0,1).
$$
$c_0,c_1$ 的值域正交且各自范数至多 $\varepsilon$，所以
$$
\boxed{
\|S_0^*\mathcal G_q\Gamma_qr\|^2+
\|S_1^*\mathcal G_q\Gamma_qr\|^2
\le\varepsilon^2\lambda_{\rm flat}(r)^2.
}
\tag{7.2}
$$
这将增长头测试正交化到最小头对角及其共同右度量补空间，未增加右侧源费用。

仍须保留左侧限制：原 $S^*\mathcal G_qS\preceq(1+\varepsilon)^2I$ 不自动给 $S_0$、$S_1$ 各自的同阶左度量上界。$J_q$ 未被证明与物理首头投影 $P$ 交换，故左费中二者可以有交叉相消。控制这一实际交叉块、一般补方向的裸费用，以及 (6.4) 中间带的完整源 Schur，仍是尚未支付的输入。
