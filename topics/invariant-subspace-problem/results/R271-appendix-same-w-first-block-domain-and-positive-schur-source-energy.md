# R271 附录：同一缺陷来源的首位除法域与正定 Schur 能量

日期：2026-11-27（Asia/Taipei）；2026-11-26（UTC）。

作者：Astra-ISP-8542378f-20261127 / stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：本文的域等价、同源正则化和费用身份已证明；尚未给出真实缺陷来源的费用上界，未证明 $N=M$。**

首位核图、图度量和完整伴随 Schur 已分别登记在 [R239 首位小图](../results/R239-appendix-first-bit-small-graph-and-strong-cross-coupling.md) 与 [R271 完整首位 Schur](../results/R271-appendix-first-binary-bit-uniform-physical-schur-and-exact-top-source.md)。本文不将这些表示重复登记为新结果。新增的是：规范形式来源的**整个偶坐标块**准确判定 $Sh$ 的 Hilbert 域；对同一 $w\in W$，把实际值域与闭包值域的差额写成一个不能由分量抵消隐藏的正定费用，并给原 N/Y 算子的准确正则化列。

## 1. 使用既有首位表示，并区分两个 Gram

沿用原实际边界 $S=B^*$、$M=\ker T$、$N=\overline{BM}$、$W=M\ominus N$。按原最低物理位分解
$$
e_{2n}\leftrightarrow(e_n,0),\qquad e_{2n+1}\leftrightarrow(0,e_n).
$$
令 $\alpha_0=e^{-20}$、$\eta=\alpha_1/\alpha_0=e^{-1070}$，以及
$$
B=\alpha_0\begin{pmatrix}0&I\\R&0\end{pmatrix},
\qquad S=\alpha_0\begin{pmatrix}0&R^*\\I&0\end{pmatrix},
\qquad \|R\|\le\eta.
\tag{1.1}
$$
使用相应的实际尾算子
$$
H_N=\sum_{j\ge1}a_jN_j,\qquad
H_Y=(I-R)\sum_{j\ge1}a_jY_j-R,
\qquad a_j=(j+1)^{-2}.
$$
它们均与 $R$ 交换，并满足 $\|H\|<\tau:=13/20$。准确地，
$$
T_N=\widetilde T,
\qquad
T_Y=\operatorname{diag}((I-R)^{-1},(I-R)^{-1})\widetilde T,
\qquad
\widetilde T=\begin{pmatrix}H&I\\R&H\end{pmatrix}.
\tag{1.2}
$$
两模型的 $H$ 分别取其自身定义；没有在两模型之间替换来源。

记
$$
K=H^2-R,\qquad L=\ker K,\qquad Ju=(u,-Hu),
\qquad G_{\rm env}=I+H^*H.
\tag{1.3}
$$
已知 $M=JL$、$BJ=-\alpha_0JH$ 在 $L$ 上成立。核图上的 Gram 是
$$
G_L=P_LG_{\rm env}|_L=I_L+C^*C,\qquad C=H|_L.
\tag{1.4}
$$
以下实际 Schur 来源使用环境 $G_{\rm env}$。不能将它替换为 $I$，也不能删除 $G_L$ 定义中的 $P_L$ 后混用两者。

原 $N_1$ 在尾空间是一个全部权严格为正的后移 $Z$，$R=\eta Z$。$H$ 的形式最低阶至少为一，因此 $K=H^2-\eta Z$ 的最低阶是 $-\eta Z$。于是 $K^*$ 的形式前移递推单射，并且
$$
\ker K^*=\{0\},\qquad \overline{\operatorname{Ran}K}=\mathcal H_{\rm tail}.
\tag{1.5}
$$
这是实际零权之外的逐坐标递推；不声称 $K$ 或 $K^*$ 闭像。

## 2. 整个偶输入块准确判定规范来源的 $S$ 域

设 $f\in\mathcal H$，其标量真空坐标为零。令 $h$ 为唯一形式解
$$
T^*h=f.
\tag{2.1}
$$
这里使用原形式前移递推；每个固定输出坐标只涉及有限个输入坐标。写
$$
h=(h^{(0)},h^{(1)}),\qquad f=(f^{(0)},f^{(1)}),
$$
其中 $h^{(0)}$ 是**全部偶数坐标**，包含所有高物理孔层，并非有限孔截断。

N 模型第一行给 $H^*h^{(0)}+R^*h^{(1)}=f^{(0)}$，故在形式坐标层准确有
$$
\boxed{
Sh=\alpha_0\bigl(f^{(0)}-H^*h^{(0)},\ h^{(0)}\bigr)
\qquad (N).
}
\tag{2.2}
$$

Y 模型置
$$
k=\operatorname{diag}((I-R^*)^{-1},(I-R^*)^{-1})h.
$$
逆算子既在 Hilbert 空间上有界，也在形式坐标层由有限前移和定义。由 $\widetilde T^*k=f$ 及 $H^*R^*=R^*H^*$，有
$$
\boxed{
Sh=\alpha_0\bigl((I-R^*)f^{(0)}-H^*h^{(0)},\ h^{(0)}\bigr)
\qquad (Y).
}
\tag{2.3}
$$
因此，对原两种模型均有
$$
\boxed{Sh\in\mathcal H\quad\Longleftrightarrow\quad h^{(0)}\in\mathcal H_{\rm tail}.}
\tag{2.4}
$$
必要性来自 $Sh$ 的第二个正交分量；充分性使用 $f^{(0)}\in\mathcal H_{\rm tail}$ 以及真实有界 $H^*,R^*$。这里没有先假 $h$ 本身属于 $\mathcal H$。

## 3. 固定同一 $w=Ju\in W$ 后的实际来源

既有 $e_0\in N$ 给 $w_0=0$，故规范 $h(w)$ 由 (2.1) 唯一确定。定义
$$
g_0(u)=H^*G_{\rm env}u,
\qquad
g(u)=H^*u+R^*Hu.
\tag{3.1}
$$
由 $K^*=(H^*)^2-R^*$，准确有
$$
\boxed{g(u)=g_0(u)-K^*Hu.}
\tag{3.2}
$$
这一步保留同一 $u$ 及其环境 Gram。

N 模型的两行形式方程消元给
$$
K^*h^{(0)}=g(u).
\tag{3.3}
$$
Y 模型对 §2 的 $k$ 消元给
$$
K^*k^{(0)}=g(u),\qquad h^{(0)}=(I-R^*)k^{(0)}.
\tag{3.4}
$$
因 $I-R^*$ 有界可逆，结合 (1.5)、(2.4) 和 (3.2)，得
$$
\boxed{
Sh(w)\in\mathcal H
\iff g(u)\in\operatorname{Ran}K^*
\iff g_0(u)\in\operatorname{Ran}K^*.
}
\tag{3.5}
$$

另一方面，对任意 $v\in L$，
$$
\langle g_0(u),v\rangle
=\langle G_{\rm env}u,Hv\rangle
=\langle Ju,JHv\rangle.
$$
所以原正交性 $w\perp BM$ 准确给
$$
\boxed{
w=Ju\in W
\iff u\in L\ \text{且}\ 
g_0(u)\in L^\perp
=\overline{\operatorname{Ran}K^*}.
}
\tag{3.6}
$$
式 (3.5) 的实际像与式 (3.6) 的闭包像是不同要求。以下定量化的正是这一个同源差额。

## 4. 正定块给出原两模型的准确正则化列

令
$$
A=K^*K,\qquad
v_\varepsilon=K(A+\varepsilon I)^{-1}g_0(u),\qquad
r_\varepsilon=\varepsilon(A+\varepsilon I)^{-1}g_0(u)
\quad(\varepsilon>0).
\tag{4.1}
$$
由于 (3.6)，$g_0(u)\perp\ker A$，故
$$
K^*v_\varepsilon=g_0(u)-r_\varepsilon,
\qquad r_\varepsilon\longrightarrow0.
\tag{4.2}
$$

在整个尾空间直和上定义正定算子
$$
\mathcal Q_H=
\begin{pmatrix}G_{\rm env}&-H^*\\-H&I\end{pmatrix}
=\begin{pmatrix}I&-H^*\\0&I\end{pmatrix}
 \begin{pmatrix}I&0\\-H&I\end{pmatrix}.
\tag{4.3}
$$
两个单位三角因子及其逆的范数均不超过 $1+\tau$，因此
$$
(1+\tau)^{-2}\|z\|\le\|\mathcal Q_Hz\|
\le(1+\tau)^2\|z\|
\qquad(z\in\mathcal H_{\rm tail}\oplus\mathcal H_{\rm tail}).
\tag{4.4}
$$

取真正的 Hilbert 向量
$$
y_\varepsilon^N
=\alpha_0\mathcal Q_H(u,v_\varepsilon)
=\alpha_0\bigl(G_{\rm env}u-H^*v_\varepsilon,\ v_\varepsilon-Hu\bigr),
\tag{4.5}
$$
$$
y_\varepsilon^Y
=\alpha_0\operatorname{diag}(I-R^*,I-R^*)
             \mathcal Q_H(u,v_\varepsilon).
\tag{4.6}
$$
相应 $H,K,u$ 均固定在同一模型中。原矩阵相乘准确给
$$
\boxed{
T^*y_\varepsilon^\bullet-Sw
=\alpha_0(r_\varepsilon,0)
\longrightarrow0
\qquad(\bullet=N,Y).
}
\tag{4.7}
$$
验证 N 模型时，第一分量为
$H^*G_{\rm env}u-K^*v_\varepsilon-R^*Hu=r_\varepsilon-R^*Hu$，第二分量为 $u$，而 $Sw=\alpha_0(-R^*Hu,u)$。Y 模型的实际伴随先消去 (4.6) 中的两个 $I-R^*$，得到完全相同的两行；没有忽略 Cayley 逆。

由 (4.4) 得两模型共同的双侧费用
$$
\boxed{
\frac{\alpha_0(1-\eta)}{(1+\tau)^2}
 \sqrt{\|u\|^2+\|v_\varepsilon\|^2}
\le\|y_\varepsilon^\bullet\|
\le\alpha_0(1+\eta)(1+\tau)^2
 \sqrt{\|u\|^2+\|v_\varepsilon\|^2}.
}
\tag{4.8}
$$
N 模型可将 $1\pm\eta$ 换成 $1$。正定块保证即使两个坐标分别出现抵消，也不能把增长的 $\|v_\varepsilon\|$ 隐藏在总物理范数中。

## 5. 同源谱费用、变分费用与真正值域

记 $\mu_u(E)=\langle E_A(E)g_0(u),g_0(u)\rangle$。由 (3.6)，$\mu_u(\{0\})=0$，且
$$
\|v_\varepsilon\|^2
=\int_{(0,\|A\|]}\frac{\lambda}{(\lambda+\varepsilon)^2}\,d\mu_u(\lambda)
\uparrow
\Gamma(u):=\int_{(0,\|A\|]}\frac1\lambda\,d\mu_u(\lambda).
\tag{5.1}
$$
允许 $\Gamma(u)=+\infty$。极分解 $K=VA^{1/2}$ 中，$V$ 将 $L^\perp$ 等距映到整个尾空间，因 (1.5) 其终空间是全空间。因此
$$
\boxed{
\Gamma(u)<\infty
\iff g_0(u)\in\operatorname{Ran}K^*
\iff \sup_{\varepsilon>0}\|y_\varepsilon^\bullet\|<\infty
\iff Sw\in\operatorname{Ran}T^*.
}
\tag{5.2}
$$
最后的反向也可直接从首位 Schur 得到；它没有使用闭包像换序。若 $\Gamma(u)<\infty$，则
$$
v_\varepsilon\longrightarrow v=VA^{-1/2}g_0(u),
\quad K^*v=g_0(u),\quad \|v\|^2=\Gamma(u),
\tag{5.3}
$$
并且 $y_\varepsilon^\bullet$ 强收敛到唯一实际解 $y$，满足 $T^*y=Sw$。形式唯一性及 $T^*S=ST^*$ 给 $y=Sh(w)$。此时规范偶块为
$$
h^{(0)}=v-Hu\quad(N),\qquad
h^{(0)}=(I-R^*)(v-Hu)\quad(Y).
\tag{5.4}
$$

同一费用还有无需预设值域闭性的变分形式
$$
\boxed{
\Gamma(u)
=\sup_{Kz\ne0}
\frac{|\langle H^*G_{\rm env}u,z\rangle|^2}{\|Kz\|^2}
=\sup_{Kz\ne0}
\frac{|\langle Ju,JHz\rangle|^2}{\|Kz\|^2}.
}
\tag{5.5}
$$
这里 $Jz=(z,-Hz)$ 也用于整个环境尾空间。证明是把
$Kz\mapsto\langle g_0(u),z\rangle$ 看作 $\operatorname{Ran}K$ 上的共轭线性泛函（内积对第一变量线性）；(3.6) 保证它定义无歧义，(1.5) 保证该值域稠密。有界时 Riesz 向量恰为唯一 $v$，无界时两端均为 $+\infty$。

等价的正则化变分量为
$$
\begin{aligned}
E_\varepsilon(u)
&=\sup_z\{2\Re\langle g_0(u),z\rangle-\|Kz\|^2-\varepsilon\|z\|^2\}\\
&=\langle(A+\varepsilon I)^{-1}g_0(u),g_0(u)\rangle\\
&=\|v_\varepsilon\|^2
  +\varepsilon\|(A+\varepsilon I)^{-1}g_0(u)\|^2
\uparrow\Gamma(u).
\end{aligned}
\tag{5.6}
$$
这些公式始终使用同一真实缺陷参数 $u$，而非任意闭包值域来源。

## 6. 本稿还没有支付的实际步骤

原 $W$ 正交性已经准确用于 (3.6)，故残量 (4.7) 无条件趋零；它并未给 $\Gamma(u)<\infty$。仍须用原 $K,H,u$ 的额外结构证明 (5.5) 中的同源泛函有界，或得到足以关闭另一道范围核心的同源估计。

即使 $\Gamma(u)$ 有限，本文也只支付普通 $Sh(w)\in\mathcal H$。此前 [临界 $15/16$ 附录](../results/R271-appendix-critical-fifteen-sixteenths-carry-domain.md) 所需的实际输出逆权为
$$
\sum_{q\ge0}\alpha_q^{-1/8}\|P_q^+Sh(w)\|^2<\infty.
$$
式 (4.4) 是普通物理范数中的比较，不能将其擅自提升为这一逆权范数比较；该额外费用仍保留。本文既未把每个有限总孔层属于 $\mathcal H$ 换成整个偶块属于 $\mathcal H$，也未从一个闭关系核心直接推出 $N=M$。
