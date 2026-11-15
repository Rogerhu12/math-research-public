# R271 附录：原头的缩放齐次相似、完整源 Chebyshev 逼近与明确 moving-head 模型窗口

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 本文只研究原 N/Y 有限头模型 $\mathcal L_m=A_m+D_{\ge m}$ 及其真实 $V_{m,Q}/K_{m,Q}$。保留全部物理内积后，选择一个很小的齐次 Jordan 权，可以把相似条件数平方的主指数控制在 $(35/3)d^4$。再用自含的 Chebyshev 多项式直接近似同源完整能量，消去前稿带外估计的 $\chi_m^2$ 前因子，并把衰减长度从 $\chi_m$ 改为 $\sqrt{\chi_m}$。

结合[精确相容 Bernoulli 真空塔](R271-appendix-compatible-bernoulli-vacuum-towers-and-same-test-exact-kernel-approximation.md)，得到原模型在 $m\to\infty$ 的一个明确大窗口内，对全部原头 forcing 的统一收敛，见 (5.4)。另给支撑于原 $m$ 后总孔数 $\le L$ 的显式真核候选。原全局 $T$ 的母提升和实际 $W$ 运输**没有**由模型结论自动付清；第 6 节把原修复中仍在的两侧高头幂写出。

## 1. 原物理权、标量函数和真实解析半径

令 $m\ge10$、$d=2^m$。原有限后移满足
$$
B_me_n=\frac{W_n}{W_{n-1}}e_{n-1},\qquad
W_n=\prod_{i\in\operatorname{bits}(n)}d_i,\qquad
d_i=e^{-\Lambda_i},
$$
$$
\Lambda_i=100\,16^i-105\,8^i+(150i+25)2^i,\qquad d_0=e^{-20}.
\tag{1.1}
$$
两个实际头为
$$
A_m=F_m(B_m),
$$
$$
F_{N,m}(z)=\sum_{i<m}(i+1)^{-2}\frac{z^{2^i}}{d_i},\qquad
F_{Y,m}(z)=\sum_{i<m}(i+1)^{-2}\frac{z^{2^i}}{d_i+z^{2^i}}.
\tag{1.2}
$$
参见 [R239 真实头稿](R239-appendix-true-head-jordan-cost-and-pure-graded-formal-range.md) §1。所有有限头函数代入均为准确幂零截断。

使用[已付的十二半逆芽圆盘](../notes/2026-11-14-true-head-inverse-germ-twelve-half-radius-and-weighted-coefficients-789f-next.md)，置
$$
\tau_m=\frac{25}{2}d^3,\qquad \rho_m=e^{-\tau_m},\qquad
\Phi_m(z)=d_0F_m(z),\qquad
\varphi_m=\Phi_m^{-1}.
$$
为避免与后文谱比混淆，本节的 $\rho_m$ 始终是标量解析半径。原证明准确给
$$
|\Phi_m(z)|\le2\rho_m\quad(|z|\le\rho_m),\qquad
|\varphi_m(w)|\le\rho_m\quad(|w|\le\rho_m/2),
\tag{1.3}
$$
且 $\Phi_m'(0)=\varphi_m'(0)=1$。后一个式子来自
$\varphi_m(w)=\psi_m(w/d_0)$，没有改变逆芽变量。

## 2. 缩放齐次头与全部物理条件数

令 $J_de_n=e_{n-1}$。定义上三角矩阵
$$
(S_m)_{kn}=
\frac{\rho_m^n}{W_k}[z^n]\varphi_m(z)^k,
\qquad 0\le k,n<d.
\tag{2.1}
$$
$k>n$ 时为零，对角为 $\rho_m^n/W_n>0$，所以可逆。截断复合的准确逆给
$$
(S_m^{-1})_{kn}
=W_n\rho_m^{-k}[z^n]\Phi_m(z)^k.
\tag{2.2}
$$

为核对方向，令 $D_W=\operatorname{diag}W_n$、
$D_\rho=\operatorname{diag}\rho_m^n$，并记
$(M_\varphi)_{kn}=[z^n]\varphi_m(z)^k$。则
$$
B_m=D_W^{-1}J_dD_W,\qquad
S_m=D_W^{-1}M_\varphi D_\rho.
$$
由 $\Phi_m(\varphi_m(z))=z$，
$$
\Phi_m(J_d)M_\varphi=M_\varphi J_d.
$$
再用 $J_dD_\rho=\rho_mD_\rho J_d$，得到
$$
\boxed{
A_mS_m=S_mJ_m^{\rm sc},\qquad
J_m^{\rm sc}=\frac{\rho_m}{d_0}J_d.
}
\tag{2.3}
$$
这是原物理头的真实相似。齐次权虽很小，但后面的 grade 证明不要求它有统一正下界。

置
$$
F_m(n)=\tau_m n+\log W_n
=\sum_{i\in\operatorname{bits}(n)}
(\tau_m2^i-\Lambda_i).
$$
每个括号都严格为正，故 $F_m(n)\ge0$，且最大值在 $n=d-1$：
$$
F_m^{\max}
=\tau_m(d-1)-\sum_{i<m}\Lambda_i.
$$
由原权准确求和，
$$
\boxed{
F_m^{\max}
=\frac{35}{6}d^4+\frac52d^3
-(150m-275)d-\frac{850}{3}.
}
\tag{2.4}
$$

(1.3) 的两次 Cauchy 估计分别给
$$
|(S_m)_{kn}|
\le2^n\frac{\rho_m^k}{W_k}
=2^ne^{-F_m(k)}
\le2^{d-1},
$$
$$
|(S_m^{-1})_{kn}|
\le2^kW_n\rho_m^{-n}
=2^ke^{F_m(n)}
\le2^{d-1}e^{F_m^{\max}}.
$$
因此
$$
\|S_m\|\le d\,2^{d-1},\qquad
\|S_m^{-1}\|\le d\,2^{d-1}e^{F_m^{\max}}.
$$
把 $S_m$ 乘一个正标量，使其最小奇异值为 $1$。相似式不变，物理 Gram 满足
$$
I\preceq G_m=S_m^*S_m\preceq\chi_mI,\qquad
\chi_m=\operatorname{cond}(S_m)^2.
$$
得到明确上界
$$
\boxed{
\begin{aligned}
\log\chi_m
\le{}&\frac{35}{3}d^4+5d^3
-2(150m-275)d-\frac{1700}{3}\\
&+4\log d+4(d-1)\log2\\
\le{}&\frac{47}{4}d^4,\qquad m\ge10.
\end{aligned}
}
\tag{2.5}
$$
最后只用
$5d^3+4\log d+4(d-1)\log2\le d^4/12$。这没有删去物理条件数，而是选择不必拉平为单位权的齐次头，使它得到更小的已证上界。

## 3. 完整源能量中的 Chebyshev 逼近

设强前缀有 $R$ 位，$x=m+R$，
$$
C=A_m+D_<,\qquad
C_0=J_m^{\rm sc}+D_<,\qquad
\mathcal S=S_m\otimes I,
$$
其中 $D_<=\sum_{m\le i<x}(i+1)^{-2}E_i$。于是
$C\mathcal S=\mathcal SC_0$。$C_0$ 按“齐次头索引加强孔数”每次恰降一 grade。

对 $L<h=d+R$，沿用相容塔稿的
$$
R_La=\sum_{j=0}^L(-C)^ja\otimes\frac{\omega_j}{\sigma_j^2},
\qquad
H_L=R_L^*R_L,\qquad a_L=H_L^{-1}g_0,\qquad
f_L=R_La_L,
$$
其中 $g_0=g\otimes\Omega_<$。令
$$
H_L^0=\sum_{j=0}^L\frac{(C_0^*)^jC_0^j}{\sigma_j^2},
\qquad
K_L=(H_L^0)^{-1/2}\mathcal S^*H_L\mathcal S(H_L^0)^{-1/2},
$$
$$
z_L=(H_L^0)^{-1/2}\mathcal S^*g_0.
\tag{3.1}
$$
$H_L^0$ 保 grade；$K_L$ 的带宽至多 $w=d-1$，并有
$$
I\preceq K_L\preceq\chi_mI,\qquad
\mathcal S^{-1}a_L=(H_L^0)^{-1/2}K_L^{-1}z_L.
\tag{3.2}
$$
$z_L$ 支撑于 grade $\le w$，而准确物理能量为
$$
\|f_L\|^2=\langle K_L^{-1}z_L,z_L\rangle.
\tag{3.3}
$$

先设 $\chi_m>1$，置
$$
\vartheta_m=\frac{\sqrt{\chi_m}-1}{\sqrt{\chi_m}+1}\in(0,1).
$$
令 $\mathsf T_n$ 为满足 $\mathsf T_n(\cos t)=\cos(nt)$ 的 Chebyshev 多项式，并定义
$$
r_n(t)=
\frac{\mathsf T_n((\chi_m+1-2t)/(\chi_m-1))}
{\mathsf T_n((\chi_m+1)/(\chi_m-1))},
\qquad
p_{n-1}(t)=\frac{1-r_n(t)}t.
\tag{3.4}
$$
$r_n(0)=1$，所以 $p_{n-1}$ 确为次数至多 $n-1$ 的多项式。对于 $1\le t\le\chi_m$，分子绝对值不超过 $1$。又
$$
\mathsf T_n\!\left(\frac{\chi_m+1}{\chi_m-1}\right)
=\frac{\vartheta_m^{-n}+\vartheta_m^n}{2},
$$
所以
$$
\boxed{|r_n(t)|\le2\vartheta_m^n\quad(1\le t\le\chi_m).}
\tag{3.5}
$$

令 $L\ge d-1$，并取准确整数
$$
\nu=\left\lfloor\frac{L}{d-1}\right\rfloor
=\left\lceil\frac{L-d+2}{d-1}\right\rceil\ge1.
\tag{3.6}
$$
定义真正候选
$$
a_{\rm pol}
=\mathcal S(H_L^0)^{-1/2}p_{\nu-1}(K_L)z_L.
\tag{3.7}
$$
因 $z_L$ 的 grade 至多 $w$，多项式次数至多 $\nu-1$，故中间向量的 grade 至多 $\nu w\le L$。$(H_L^0)^{-1/2}$ 保 grade，因此
$$
a_{\rm pol}\in\ker C^{L+1}.
\tag{3.8}
$$

这一步直接在完整能量中估计，而非先取逆的环境范数：
$$
\begin{aligned}
\|R_L(a_L-a_{\rm pol})\|^2
&=\|K_L^{-1/2}r_\nu(K_L)z_L\|^2\\
&\le4\vartheta_m^{2\nu}
\|K_L^{-1/2}z_L\|^2\\
&=4\vartheta_m^{2\nu}\|f_L\|^2.
\end{aligned}
\tag{3.9}
$$
因此，若 $p_L$ 是前稿在 $W_L=\ker C^{L+1}$ 上使用完整压缩 Gram 得到的真正最小者，则
$$
\boxed{
\delta_L^2:=\|f_L-p_L\|^2
\le\min\{1,4\vartheta_m^{2\nu}\}\|f_L\|^2.
}
\tag{3.10}
$$
完整源最小化保留了所有 nuisance，并消除了 $\chi_m^2$ 前因子。若 $\chi_m=1$，则 $K_L=I$，对 $L\ge d-1$ 有 $\delta_L=0$。

## 4. 同实际测试的界，以及较小原孔支持的显式真核

使用相容塔稿的 $v_j$、$T_L$ 和
$$
A_{x,L}
=\mathbb P(N\ge L)^{-1}
\left(\frac{S_x}{S_{x+L}}\right)^L.
$$
在准确 $W_L$ 上，两个完整压缩 Gram 满足
$$
H_{L,W}\preceq\widehat H_{L,W}
\preceq A_{x,L}^2H_{L,W}.
$$
于是，若原 cut 满足 $Q\ge R+L$，同一个实际
$$
u_g=(P_{V_{m,Q}}-P_{K_{m,Q}})
(g\otimes\Omega_{\ge m})
$$
满足
$$
\boxed{
\|u_g\|^2
\le
\left[
1-A_{x,L}^{-2}
+A_{x,L}^{-2}\min\{1,4\vartheta_m^{2\nu}\}
\right]\|g\|^2.
}
\tag{4.1}
$$
这是前稿同一个 $u_g$、同一个物理源及同一个 $W_L$ 最小化；没有重新定义投影来源。

另有一个可用于后继原 carry 的具体候选：
$$
k_{\rm pol}=T_La_{\rm pol}.
\tag{4.2}
$$
它是真核，因为 (3.8)。而且它在第 $m$ 位以后的**原总孔数至多为 $L$**。证明如下：$\mathcal S^{-1}a_{\rm pol}$ 的 total grade 至多 $L$；$C_0^j$ 将它降到 grade $\le L-j$，所以对应强孔数至多 $L-j$；$\mathcal S$ 只作用旧 $m$ 位头，不改强孔数；张量 $v_j$ 后增加恰好 $j$ 个远孔。因此
$$
\boxed{k_{\rm pol}\in K_{m,L}.}
\tag{4.3}
$$
原 cut $Q\ge R+L$ 仍是保持 $f_L$ 与 forcing 的全部 $V/K$ 投影所需条件，不能因 (4.3) 而从这一来源恒等式中删除 $R$。

相容塔误差逐层垂直于相干列，故有准确正交拆分
$$
\begin{aligned}
\|f_L-k_{\rm pol}\|^2
={}&\|R_L(a_L-a_{\rm pol})\|^2\\
&+\|(T_L-R_L)a_{\rm pol}\|^2.
\end{aligned}
$$
从而
$$
\boxed{
\|f_L-k_{\rm pol}\|^2
\le
\left[
4\vartheta_m^{2\nu}
+(A_{x,L}^2-1)(1+2\vartheta_m^\nu)^2
\right]\|g\|^2.
}
\tag{4.4}
$$
这是真核候选的原范数误差，不依赖把小方程残量换成核距离。

## 5. 一个明确的 moving-$m$ 模型窗口

对每个 $m\ge10$，选择整数
$$
x_m=\left\lceil e^{12d^4}\right\rceil,\qquad
R_m=x_m-m,\qquad
L_m=\left\lceil e^{(71/12)d^4}\right\rceil,
\qquad d=2^m,
\tag{5.1}
$$
并取任意 $Q_m\ge R_m+L_m$。这里 $d-1\le L_m<d+R_m$。

由 (2.5)，
$$
\sqrt{\chi_m}\le e^{(47/8)d^4},
\qquad
\frac{L_m}{\sqrt{\chi_m}}\ge e^{d^4/24}.
$$
又 $\nu\ge L_m/(2d)$，并且
$$
-\log\vartheta_m
=\log\frac{\sqrt{\chi_m}+1}{\sqrt{\chi_m}-1}
\ge\frac2{\sqrt{\chi_m}},
$$
所以
$$
\vartheta_m^{2\nu}
\le
\exp\left[-\frac2d e^{d^4/24}\right].
\tag{5.2}
$$
$\chi_m=1$ 时该项直接取零。

相容塔稿给
$$
\varepsilon_{x,L}
=\exp((L-1)\log2-(x+1)/6),
\qquad
1-A_{x,L}^{-2}
\le4\varepsilon_{x,L}+\frac{6L(L+1)}x.
$$
对 (5.1)，
$$
\varepsilon_{x_m,L_m}\le e^{-x_m/12},\qquad
\frac{6L_m(L_m+1)}{x_m}\le36e^{-d^4/6}.
\tag{5.3}
$$
结合 (4.1)，得到显式结论
$$
\boxed{
\sup_{\|g\|\le1}\|u_g\|^2
\le
36e^{-d^4/6}
+4e^{-x_m/12}
+4\exp\left[-\frac2d e^{d^4/24}\right]
\longrightarrow0.
}
\tag{5.4}
$$
(4.4) 同时给原 $K_{m,L_m}$ 中的精确候选 $k_{\rm pol}$，它与相同 $f_{L_m}$ 的距离趋零、范数一致有界。所有 forcing 均为原 $d$ 维物理头任意向量张量其后真空，结论在这些向量上统一。

## 6. 原母提升仍不是“一次 $Q^2$”的费用

本节只定位下一步必须证明的原模型运输，不作新的普遍反例。

[已付 c26 原联合 carry 稿](../notes/2026-11-14-joint-positive-carry-budget-and-twenty-six-window-actual-sources-789f-next.md) §4 的实际一步为
$$
c_p=\sum_{j<z}(-A_{p+1})^jR'_{j+1}K_pk_p,\qquad z=2^p.
$$
其原相容右逆参数确实满足
$$
\mathcal R_0\le512(Q+5z)^2.
$$
但实际范数估计是
$$
\boxed{
\|c_p\|
\le
\mathcal R_0
\sum_{j,\ell<z}
\frac{\mathcal R_0^{j+\ell}}{(j+1)!\,\ell!}
\|A_p^jK_pA_p^\ell\|\,\|k_p\|.
}
\tag{6.1}
$$
所以二次参数仍被放入全部两侧头幂，不能只支付一次 $Q^2\|K_p\|$。原正系数共同估计保留跨块次数 $2z-1$；其 Cauchy 界的真实权指数为该稿 (3.7)
$$
-\sum_{i=0}^{p}\Lambda_i+(2z-1)t_p.
\tag{6.2}
$$
当估计参数取 $\log\mathcal R_0$ 为 $O(d^4)$ 而 $p=m$ 时，(6.2) 的正成本可到 $O(d^5)$。因此，直接把 (5.1) 代入旧 c26 证明，不能仅凭原
$\|T-\mathcal L_m\|\le104e^{-770\,16^{m-1}}$
宣布修复仍小。旧合法母窗是 $Q\le e^{26d^3}$，本稿没有扩大它。

新候选 (4.2) 的真实原孔数只有 $L_m$，比 $Q_m$ 小；它还保留同一随机池和精确源多项式。后继可以专门估计
$A_p^jK_pA_p^\ell k_{\rm pol}$，而不先取 (6.1) 的全源环境范数。但 $K_p$ 会改变旧头 grade，(4.3) 本身没有把这些高头幂全部杀掉。

同样，实际 $P_{V_{m,Q}}w$ 的误差还需 c26 §§5–6 的完整 $D$ 交换子和同一 $w$ 的导数展开，不由真核候选的存在自动推出。故 (5.4) 是明确而完整的 moving-head **模型**结论，不等于原全局 $W=0$ 或 $N=M$。

原全局算子仍严格按 [R200](R200-boundary-right-shift-domains-and-forward-division-saturation.md) §1 (1.1) 的 $T_N,T_Y$ 定义。新缩放、完整物理 Gram 和精确塔都没有将其替换成纯分级模型。
