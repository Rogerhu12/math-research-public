# R236 附录：真正解析右源的导子弱单位与同一正常商完整泄漏余额

日期：2026-11-14 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。

状态：root 已全文核验的真实来源改进及正常商必要条件。所有右源改成原 Acal 中的实际单位逆；完整物理矩阵输入仍不属于 Acal。本文不将全 H 的核排除传到未知商，不用一般模型代替真实 Haar 方程。

## 1. 两行正常商和真实物理实现

设 N⊂M⊂H^(d) 是原 A^(d) 的闭不变旗，d 为固定有限整数；所有原 Acal 算子均保持该旗。记
$$
E=M\ominus N,\qquad L=M^\perp,\qquad
H^{(d)}=N\oplus E\oplus L,
$$
$$
\pi(R)=P_ER^{(d)}|_E,\qquad
\Phi(W)=P_EW|_E\quad(W\in B(H^{(d)})).
$$
π 是原 Acal 的正常契约表示；Φ 是固定物理压缩，但不在全部 B(H^(d)) 上保乘法。

保留一个固定非零正正常密度 rho≥0，作用于 E，tau=Tr rho>0。把 rho 按这个同一个实际嵌入视为原 H^(d) 上的密度；下文不会用新的独立状态替换它。

假设原两行 X、Y 满足
$$
\pi(X)=\pi(Y)=0,
\qquad X=\sum_i a_iX_i,\quad Y=\sum_i b_iX_i,
\quad X_i\in\{N_i,Y_i\}.
\tag{1.1}
$$
系数采用[相对辅助排核稿](R236-appendix-polynomial-relative-auxiliary-quadratic-exclusion.md)的条件：|a_i|≤A(i+1)^(-2)，充分高位 |a_i|≥a_-(i+1)^(-2)、|b_i/a_i|≥c(i+1)^(-2)，b∈ell1。特别包括未加 carry 修正的正两行 (sum a_i N_i,sum a_i²N_i)。

为了把两个准确零式同时使用，置
$$
\boxed{T=X^2+Y,\qquad\pi(T)=0.}
\tag{1.2}
$$
本节 T 与此前核稿的 X²-B_0+Y 有明确区别。下述混合模型的所有选中高位都平方零，所以删去 B_0 不改变一次系数及最高导子恒等式；低头仍是无常数幂零多项式。范数和误差仍可用相对辅助稿较大的安全常数
$$
M_T=54A^2+3\sum_i|b_i|,\quad
D_T=324A^2+9\sum_i|b_i|,\quad K=\max(1,2M_T).
\tag{1.3}
$$
因此该稿的全域导子预算也适用于这个辅助 T，但 π(T)=0 仍是商上的条件，不是说原 T 有核。

## 2. 把背景逆全部换成真实 Acal 右源

沿相对辅助稿取
$$
\sigma=\min(1/4,\sqrt{c/A}/16),\quad r=2^j,
\quad q=\lceil\sigma r^2\rceil,\quad
I_j=\{j,\ldots,j+q-1\},\quad M_j=j+q,
$$
且 j 足够高。对 |F|=r，分别定义
$$
X_F=\sum_{i\notin F}a_iX_i\in\mathcal A,
\qquad
\widehat X_F=\sum_{i\notin F}a_i\widehat X_i,
$$
其中 hat X_i 仍是第 j 位截断的保真低头/纯高尾混合模型。真实差有
$$
\|X_F-\widehat X_F\|\le18A\eta_{j-1}.
$$
令
$$
p_F(z)=\prod_{i\in F}(b_i+2a_i z)^2,
\qquad
\boxed{R_F=p_F(X_F)^{-1}=\prod_{i\in F}(b_i+2a_iX_F)^{-2}.}
\tag{2.1}
$$
每个 R_F 属于原 Acal：旋转 Laplace 积分直接在这个含幺范数闭代数内构造真正的左右逆。它与原 T 交换，并保留所有原右作用，不是混合模型里的替身。

同一个共同时间积分给
$$
\boxed{
\|R_F\|\le
4^r a_-^{-2r}c^{-2r}M_j^{8r}e^{256AM_j^2/c}=:K_j^{\rm src}.
}
\tag{2.2}
$$
定义带实际右源的输入
$$
\boxed{
U_j^{\rm act}=\frac{(-1)^r2^r}{(2r)!\binom qr}
\sum_{|F|=r}E_F^*R_F.
}
\tag{2.3}
$$
这些是物理矩阵乘原右源的完整实际算子。其范数不超过 C_j=2^r K_j^src/(2r)!。

## 3. 不付第二个巨大逆的精确比较

写 delta=ad_T、hat delta=ad_hatT、m=2r。因为 R_F 与原 T 交换，准确有
$$
\delta^m(E_F^*R_F)=\delta^m(E_F^*)R_F.
\tag{3.1}
$$
混合模型最高项给
$$
\widehat\delta^m(E_F^*)=(-1)^r m!E_Fp_F(\widehat X_F).
$$
而 p_F(X_F)R_F=I。故比较误差可直接写成
$$
(\delta^m-\widehat\delta^m)(E_F^*)R_F
+(-1)^r m!E_F\bigl[p_F(\widehat X_F)-p_F(X_F)\bigr]R_F.
\tag{3.2}
$$
这里没有比较两组逆，也没有乘第二个 e^(256AM_j²/c) 费用。

令
$$
V=\max\left(1,\sum_i|b_i|+12A^2\right).
$$
在 ||X_F||、||hat X_F||≤6A 上，每个线性因子的范数≤V；两因子之差≤36A²eta_(j-1)。逐个替换全部2r个因子，得到
$$
\boxed{
\|p_F(\widehat X_F)-p_F(X_F)\|
\le72rA^2V^{2r}\eta_{j-1}.
}
\tag{3.3}
$$
不同背景之间不必交换；这个有序积差估计本来就是非交换的。

把 (3.2) 求平均，令
$$
R_j^{\rm av}=\frac{2^r}{\binom qr}\sum_{|F|=r}E_F,
$$
得到
$$
\boxed{
\|\delta^{2r}(U_j^{\rm act})-R_j^{\rm av}\|
\le\eta_{j-1}2^rK_j^{\rm src}
\left[\frac{4rD_TK^{2r}}{(2r)!}+72rA^2V^{2r}\right]
=:\epsilon_j^{\rm act}.
}
\tag{3.4}
$$
平方括号只有 exp(O(r)) 费用。沿 M_j≤2σr² 的高位，(2.2) 的主要指数≤4r⁴，原 carry 至少 (770/16)r⁴；其余都是 O(r log r)。所以可以显式检查右边，并对足够高 j 保证 epsilon_j^act≤exp(-43r⁴)。

此外，对任意固定有限头 D，hat delta^(2r)(D)=0，原幂差仍给
$$
\|\delta^{2r}(D)\|\,\|U_j^{\rm act}\|
\le4rD_TK^{2r}\eta_{j-1}C_j\|D\|\longrightarrow0.
\tag{3.5}
$$
同一 Boolean 平均满足 ||R_j^av||≤exp(1/σ)、R_j^av→I WOT。故
$$
\boxed{\delta^{2r}(U_j^{\rm act})\longrightarrow I\quad\text{WOT},
\qquad\sup_j\|\delta^{2r}(U_j^{\rm act})\|<\infty.}
\tag{3.6}
$$
这是原全空间的实际导子弱单位，其输入已具有完整真实右源。

## 4. 真正常商的高位双向泄漏

本节仍使用固定旗 N⊂M、固定 E。对实际 N_l^(d)，写块矩阵
$$
N_l^{(d)}=
\begin{pmatrix}
A_l&B_l&D_l\\0&C_l&F_l\\0&0&G_l
\end{pmatrix},\qquad C_l=\pi(N_l).
$$
令 H_l=N_l^(d)+(N_l^(d))^*-I。由旗不变性，准确有
$$
\boxed{B_l=P_NH_l|_E,\qquad F_l^*=P_LH_l|_E.}
\tag{4.1}
$$
原 Haar 物理式给
$$
H_l=-2Q_l^-+K_l,
\qquad Q_l^-=(I-E_l-E_l^*)/2,
\qquad\|K_l\|\le2\eta_l.
\tag{4.2}
$$
Q_l^- 是第 l 位 Walsh minus 投影；对每个固定有限柱向量，充分高 l 时它为零。因此 H_l→0 强。

对同一个 rho，记 p_l=Tr(rho Q_l^-)、tau=Tr rho，则
$$
\boxed{
\|B_l\rho^{1/2}\|_{\rm HS}^2+
\|F_l^*\rho^{1/2}\|_{\rm HS}^2
\le4(\sqrt{p_l}+\eta_l\sqrt\tau)^2.
}
\tag{4.3}
$$
这里 p_l 直接按同一物理 rho 计算，没有换成新密度。它趋于0，故两种高位泄漏确实趋于0。

两种 Schwarz 缺陷准确为
$$
\boxed{
\Phi(N_l^*N_l)-C_l^*C_l=B_l^*B_l,\qquad
\Phi(N_lN_l^*)-C_lC_l^*=F_lF_l^*.
}
\tag{4.4}
$$
所以它们都是正的，并趋强0。其和也是固定压缩对 H_l 的方差
$$
B_l^*B_l+F_lF_l^*=\Phi(H_l^2)-\Phi(H_l)^2.
\tag{4.5}
$$
(4.5) 使用 π(N_l²)=π(N_l)² 的真实解析乘法，不在含伴随的全算子代数上假设乘法。

对任意原解析右算子 R，写其相应块 B_R、F_R，则
$$
\boxed{
\Phi([R,N_l^*])-[\pi(R),C_l^*]
=F_RF_l^*-B_l^*B_R.
}
\tag{4.6}
$$
若 π(R)=0，右侧就是商内把原交换子搬运过去时留下的完整两项；(4.3) 不能在 R 的范数随 l 增长时自动把它们压过逆费用。

## 5. 原零式 π(T)=0 下的全部导子交叉块

现在把原辅助 T 的块写作
$$
T^{(d)}=
\begin{pmatrix}
A&B&D\\0&0&F\\0&0&G
\end{pmatrix},
\tag{5.1}
$$
中间0正是两行 (1.1) 给的同一个 π(T)=0。对任意有界 U，记 U_LE=P_LU|_E 等。直接按 T 的三角幂展开得到每个 m≥1 的准确身份
$$
\boxed{\begin{aligned}
\Phi(\operatorname{ad}_T^mU)
={}&FG^{m-1}U_{LE}+(-1)^mU_{EN}A^{m-1}B\\
&+\sum_{s=1}^{m-1}(-1)^s\binom ms
FG^{m-s-1}U_{LN}A^{s-1}B.
\end{aligned}}
\tag{5.2}
$$
因为 T^sE⊂N 对 s≥1，而 P_ET^p 只从 L 进入 E；端点及所有中段都在 (5.2) 中，没有删除一个 π(T)=0 后仍存在的物理耦合。

取 m=2r、U=U_j^act；有限放大时将这些原算子同步张量 I_d。由 (3.6) 的一致算子范数界，先对 rho 的有限秩近似使用 WOT 极限，再以迹范数误差乘该一致界取极限；这准确支付了同一正常 rho 的迹极限，而不是把一般 WOT 当作 ultraweak。固定压缩 Φ 后因此有
$$
\boxed{\operatorname{Tr}\rho\,\Phi(\operatorname{ad}_T^{2r}U_j^{\rm act})
\longrightarrow\tau>0.}
\tag{5.3}
$$
因此 (5.2) 右侧的完整源余额必须保留同一个非零锚 tau，不能在商内把整个高导子当作0。

一个完全保原 rho 的必要费用可写为
$$
\begin{aligned}
\Gamma_j(\rho)={}&M_T^m\sqrt\tau
\left(\|U_{LE}\rho^{1/2}\|_{\rm HS}
+\|U_{EN}^*\rho^{1/2}\|_{\rm HS}\right)\\
&+\sqrt\tau\sum_{s=1}^{m-1}\binom ms M_T^{m-s}
\|U_{LN}A^{s-1}B\rho^{1/2}\|_{\rm HS}.
\end{aligned}
\tag{5.4}
$$
由 Hilbert–Schmidt Cauchy–Schwarz，(5.2) 每一项的迹绝对值之和不超过 Γ_j，因此
$$
\boxed{\liminf_j\Gamma_j(\rho)\ge\tau.}
\tag{5.5}
$$
这里所有输运列都是明确的实际算子乘原 rho^(1/2)，不是任意换一个满足相同尾界的状态。

## 6. 每一列中完整保留真右源

按 (2.3)，以其系数逐项展开 U 块。对一个 F 项 E_F^*R_F，(5.4) 需要的中段源准确是
$$
P_LE_F^*R_F\,T^s\rho^{1/2}\qquad(s\ge1),
\tag{6.1}
$$
因为 T^sE⊂N 且 A^(s-1)B=T^s|_E。首段为 P_LE_F^*R_F rho^(1/2)，反向端点为 P_NR_F^*E_F rho^(1/2)。全部 R_F 是 (2.1) 的原代数真逆，原两行和同一 rho 都保留。

(4.3) 只控制固定原 rho 下单个高位的泄漏。它不直接控制 (6.1) 的增长阶数、全部 F、真实右源 R_F 和全部 T^s 输运列。把 R_F 在商中的像界当作原 (6.1) 的源范数会丢掉 N 向耦合；把正常性 p_l→0 乘以未付增长费用也没有根据。

本文的新接口是：全域导子弱单位已经可以使用完整实际右源，其在任意两行正常商中的障碍被准确限定为 (5.2)、(6.1) 的原交叉块和同一 rho 输运列。若这些实际列能使 Γ_j→0，便与 (5.5) 矛盾而排除此正常商；当前未证明这一控制，也没有构造原 Haar 中满足该正常商条件的反例。

原半群及真实高位物理来源参见[R215](R215-slow-semigroup-resolvent-and-normal-annihilator-tail.md)和[原N二次局部导子证明](R236-appendix-actual-slow-positive-quadratic-kernel-exclusion-by-joint-inverse.md)。本文保原Acal右源、同一个不变旗和同一ρ；不把R200的负边界线性核与这里的正常商混同。
