# R74. 一阶模数、向量扩张及真实 Witt 临界投影

日期：2026-11-12。**状态：固定几何接收器、高模数余项与准确临界投影均已证明；目标非零仍未证明。**

## 1. 真实一阶信息和 Frobenius 的不同格

实际 68 阶单位满足 $r_P(O)=1$，
$c_P=\partial_Z\log r_P(O)=-68^2U_P$。
它的主除子在带 $2O$ 刚性化的 Jacobian
$\mathcal J_2=\operatorname{Pic}^0(E_\lambda,2O)$ 中，准确落在加法核 $1+c_PZ$。
Coleman 1990 的 Prop.1.2、Thm.3.1 的假设在此逐项满足，故
$\mathcal J_2$ 确为整个家族的普遍向量扩张。
实际偶组合 $M_e=M_1$ 对应连接 $(\mathcal O,d-M_e\omega)$。

特征 $p$ 的相对 Frobenius 把模数 $2O$ 拉成 $2pO$；
$1+cZ'$ 先变成 $1+cZ^p$，忘到 $2O$ 后才变成 1。
$2pO$ 的主单位群不是向量群，且对数的第 $p$ 项含分母 $p$。
所以一阶的群同构不能代替高模数的整比较。

直接用 Picard-连接的一阶 cocycle 得
$\operatorname{Lie}\mathcal J_2=H^1_{\rm dR}$，加法核是 $\operatorname{Fil}^1$。
任意特征零代数群同态必须保这条线；真实惰性 crystalline Frobenius
却有 $\Phi(\omega^\sigma)=pa\eta$。它不是这样的群同态的微分。
原格像的商长度为一、determinant ideal 为 $(p)$；除 $p$ 使用的是扩大的源格。

## 2. 第一垂直 Witt 余项

令 $z=\int\omega$、$b_p=p[Z^p]z$，$\mathcal H_p$ 为不变向量场的 Hasse 系数。
对任意实际归一单位，直接的有限对数展开给
$$
p[Z^p](\log r-cz)\equiv c^p-\mathcal H_pc\pmod p,
\qquad b_p\equiv\mathcal H_p\pmod p.
$$
这是连接 $d-c\omega$ 的 $p$-curvature 的相反数。

使用 R71 的同一偶对数 $h_e$，置
$\Lambda_{e,p}=p[Z^p]h_e$、$W_{e,p}=\Lambda_{e,p}-b_pM_e$。
它们全整。惰性时准确有
$$
W_{e,p}\equiv\eta_pM_o(t^p)-\mathcal H_pM_e\pmod p,
\qquad \eta_p=c_e/c_o^\sigma.
\tag{1}
$$
普通时将 $M_o$ 换成 $M_e$，$\eta_p=c_e/c_e^\sigma$。

## 3. 原 GM 行给出的完全精度单位项

取惰性 $p\ge7$，定义实际整投影
$$
F_i=U^{p+1}/(s(V/t)^{p+2}),\qquad
\mathcal P_p(F)=[t^{p+1}]F F_i/V.
$$
令 $n=(p-1)/2$、$H_p=P_n(2t)$、$h_p=H_p'(0)\in\mathbb Z_p^\times$。
Legendre 方程在所需次数 $\le p-2$ 给 $H_p\equiv h_pV\pmod{p^2}$，于是
$$
\mathcal P_p(H_pM_e)\equiv h_pC_{p+1}\pmod{p^2}.
$$
另一个项可完全准确计算：
$$
\boxed{\mathcal P_p(M_o(t^p))
=[t^2]U^{p+1}/(s(V/t)^{p+3})=-p.}
\tag{2}
$$
所以它模 $p$ 消失，但除 $p$ 后留下单位 $-1$。

保留实际第二余项
$$
E_{e,p}=\frac{\Lambda_{e,p}-(b_p-H_p)M_e-\eta_pM_o(t^p)}p
\in\mathcal O[[t]].
$$
由恒等式 $W_{e,p}+H_pM_e=\eta_pM_o(t^p)+pE_{e,p}$ 得
$$
\boxed{h_pC_{p+1}/p\equiv
-\eta_p-\mathcal P_p(W_{e,p})/p+\mathcal P_p(E_{e,p})\pmod p.}
\tag{3}
$$
$\mathcal P_p(W_{e,p})$ 确被 $p$ 除。式 (3) 的最后两项尚可能抵消已知单位；
定义它们并不提供独立的非零关系。
完整证明及 Coleman 原文范围见
[一阶模数与实际临界投影](../notes/2026-11-12-first-modulus-vectorial-extension-and-critical-projection.md)。
