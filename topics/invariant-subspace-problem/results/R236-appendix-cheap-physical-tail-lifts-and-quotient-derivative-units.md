# R236 附录：删池真右逆的廉价物理尾提升与同商导子弱单位

日期：2026-11-14 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。

状态：下列实际构造、导子比较和完整源块身份已经逐项核验。上一稿的有限总度逆现在直接在原 Haar 空间构造一个便宜的实际尾代表，并列出它与原背景逆的准确主理想双向源。进一步使用 E_F 的实际解析近似，在同一个两行正常商上得到便宜输入的压缩导子弱单位。最终交叉块来源仍完整保留，未证明一般正常商为零。

依赖：[相对辅助系数及全域联合逆](R236-appendix-polynomial-relative-auxiliary-quadratic-exclusion.md)、[原解析右源及完整正常商余额](R236-appendix-actual-right-sources-and-normal-quotient-leakage.md)、[同商一次总度逆](R236-appendix-joint-right-inverse-on-the-same-normal-quotient.md)。

## 1. 所有量都在原 Haar 空间定义

沿相对辅助稿的原 Xi∈{Ni,Yi}、a_i、b_i、A、a_-、c。设
$$
X=\sum_i a_iX_i,\qquad Y=\sum_i b_iX_i,
\qquad T=X^2+Y.
$$
固定原有限放大闭旗 N⊂M、E=M orthogonal-minus N、L=M^perp，pi 为正常契约商表示。假设
$$
\pi(X)=\pi(Y)=0,\qquad\pi(T)=0.
$$
固定同一个非零正常密度 rho≥0 于 E，tau=Tr rho>0。

对充分高整数 P，取 F⊂{P,...,2P-1}、|F|=r≤P。记
$$
Z_F=\sum_{i\in F}a_iX_i,
\qquad X_F=X-Z_F,
\qquad
P_F(z)=\prod_{i\in F}(b_i+2a_i z)^2.
$$
原完整右源为 R_F=P_F(X_F)^(-1)。定义另一个完全实际的尾算子
$$
\boxed{\widetilde R_F=P_F(-Z_F)^{-1}.}
\tag{1.1}
$$
下节直接构造这个逆，避免只用 pi(R_F) 的范数推断一个未付提升。

## 2. 全原空间的有限总度逆和低范数界

真实 Xi 交换且 ||Xi||≤3、||Xi²||≤9eta_i。所以上一稿的重复位估计直接在完整原空间成立：令 w=3Σ_F|a_i|，则
$$
\|Z_F^n\|\le\eta_Pw^n\quad(n\ge r+1),
\qquad w\le3Ar/P^2.
$$
令 lambda_i=2a_i/b_i、p_F(z)=∏_F(1-lambda_i z)^2，H_r=max(1,24Ar/c)，并取 g_r=[1/p_F]_(degree≤r)。准确余式和实际预算为
$$
\|g_r(Z_F)\|\le G_r=(r+1)8^rH_r^r,
$$
$$
\|p_F(Z_F)g_r(Z_F)-I\|
\le e_{P,r}:=\eta_P(1+24Ar/c)^{2r}G_r.
$$
若 e_(P,r)≤1/2，则实际 Neumann 逆范数≤2，故
$$
\boxed{
\widetilde R_F
=\left(\prod_Fb_i^{-2}\right)
 g_r(Z_F)\bigl[p_F(Z_F)g_r(Z_F)\bigr]^{-1},
}
$$
$$
\boxed{
\|\widetilde R_F\|
\le\widetilde K_{P,r}:=
2(r+1)8^rH_r^r\frac{(2P)^{8r}}{(a_-c)^{2r}}.
}
\tag{2.1}
$$
一切都在原实际≥P尾代数内构造，且对有限放大不变。固定常数下 log tilde K=O(r log r+r log P)。

因此这一目标确有便宜物理尾代表；这次结论比仅有便宜商像严格多付了一个实际构造。

## 3. 同一主理想中的完整双向源

所有实际变量交换。定义有限多项式差商
$$
D_F(u,v)=\frac{P_F(u)-P_F(v)}{u-v}.
$$
右边指唯一有限多项式，不是对 u-v 取算子逆。由 u=X_F、v=-Z_F、u-v=X，得到
$$
\boxed{
R_F-\widetilde R_F
=-X R_FD_F(X_F,-Z_F)\widetilde R_F.
}
\tag{3.1}
$$
反向差即同一右源的相反号。所有因子均在原 Acal，不是模理想的形式逆。

令 V=max(1,Σ|b_i|+12A²)。因为 ||X_F||≤6A、||Z_F||≤3A，逐个替换2r个线性因子给
$$
\|D_F(X_F,-Z_F)\|\le4rA V^{2r}.
$$
记
$$
H_F=R_FD_F(X_F,-Z_F)\widetilde R_F.
$$
原背景右源的已付全域界为
$$
\|R_F\|\le K_{P,r}^{\rm src}
:=4^r a_-^{-2r}c^{-2r}(2P)^{8r}e^{1024AP^2/c}.
$$
故
$$
\boxed{\|H_F\|\le4rA V^{2r}K_{P,r}^{\rm src}\widetilde K_{P,r}.}
\tag{3.2}
$$
目标提升便宜，但其原双向理想来源仍保这项费用。

(3.1) 给 pi(R_F)=pi(tilde R_F)。若原同一 rho 湮灭 X 的全部允许右倍数，则对每个允许右测试 G，且 H_FG 仍在原测试代数内时，准确有
$$
\operatorname{Tr}\rho R_FG=\operatorname{Tr}\rho\widetilde R_FG.
\tag{3.3}
$$
这特别对全部原 Acal 右测试成立；若原见证给完整 A' 测试，则也保留该完整测试族。已有非零配对在此精确保留，没有另选 rho。

## 4. 便宜输入在同一正常商上产生压缩导子弱单位

令 j→∞、r=2^j，并取
$$
\sigma=\min(1/4,\sqrt{c/A}/32),\qquad
P=\lceil\sigma r^2\rceil,\qquad I_j=\{P,...,2P-1\}.
$$
第 j 位仍作为保真低头/纯高尾的辅助截断。固定物理压缩记Phi。定义完全原源输入
$$
\boxed{
\widetilde U_j=\frac{(-1)^r2^r}{(2r)!\binom Pr}
\sum_{|F|=r}E_F^*\widetilde R_F.
}
\tag{4.1}
$$
于是
$$
\|\widetilde U_j\|
\le\frac{2^r}{(2r)!}\widetilde K_{P,r},
\qquad \log^+\|\widetilde U_j\|=O(r\log r).
\tag{4.2}
$$
这里已避免原背景逆的 exp(CP²) 输入费用。

所有 tilde R_F 与原 T 交换，所以 ad_T^m(E_F*tilde R_F)=ad_T^m(E_F*)tilde R_F。相对辅助稿的原幂差以及混合最高项给，m=2r 时
$$
\operatorname{ad}_T^m\widetilde U_j
\quad\text{与}\quad
\frac{2^r}{\binom Pr}\sum_{|F|=r}
E_FP_F(X_F)\widetilde R_F
$$
之间的全域算子范数差不超过
$$
\eta_{j-1}2^r\widetilde K_{P,r}
\left[\frac{4rD_TK^{2r}}{(2r)!}+72rA^2V^{2r}\right].
\tag{4.3}
$$
(4.3) 只乘便宜 tilde K；其中第二项是比较 P_F(hat X_F) 和 P_F(X_F) 的有限多项式差，不比较逆。

准确多项式身份又给
$$
P_F(X_F)\widetilde R_F
=I+X D_F(X_F,-Z_F)\widetilde R_F.
\tag{4.4}
$$
右侧额外项属于原 X 主理想，但左乘 E_F 不是自动合法消去。为此使用真实解析近似
$$
A_F:=\prod_{i\in F}X_i\in\mathcal A,
\qquad
\|E_F-A_F\|\le4r3^{r-1}\eta_P.
\tag{4.5}
$$
因为每个高位 ||Xi-Ei||≤4eta_i，且 ||Xi||≤3。(4.5) 是全原空间范数估计。

A_F X D_F tilde R_F 保持原旗，并且商像准确为0。故
$$
\|\Phi(E_FX D_F\widetilde R_F)\|
\le(4r3^{r-1}\eta_P)(6A)(4rA V^{2r})\widetilde K_{P,r}.
\tag{4.6}
$$
此处真的支付了 E_F 的物理-to-解析替换，未把 pi(E_F) 当作一个代数同态输入。

记 R_j^av=(2^r/binom(P,r))Σ E_F。由 (4.3)、(4.6)，
$$
\boxed{
\|\Phi(\operatorname{ad}_T^{2r}\widetilde U_j)-\Phi(R_j^{\rm av})\|
\le\epsilon_j^{\rm cheap}\longrightarrow0,
}
\tag{4.7}
$$
其中一个完整显式上界为
$$
\begin{aligned}
\epsilon_j^{\rm cheap}={}&
\eta_{j-1}2^r\widetilde K_{P,r}
\left[\frac{4rD_TK^{2r}}{(2r)!}+72rA^2V^{2r}\right]\\
&+2^r(4r3^{r-1}\eta_P)(24rA^2V^{2r})\widetilde K_{P,r}.
\end{aligned}
\tag{4.8}
$$
log tilde K=O(r log r)、eta_(j-1)≤exp(-(770/16)r⁴)，而 eta_P 更小，所以 (4.8) 趋零。

Boolean 平均的 ||R_j^av||≤exp(1/σ)、R_j^av→I WOT 仍成立。因此
$$
\boxed{
\Phi(\operatorname{ad}_T^{2r}\widetilde U_j)\longrightarrow I_E
\quad\text{WOT，且商上输出一致有界。}
}
\tag{4.9}
$$
对固定原正常 rho，用有限秩迹类近似和该一致界，得到
$$
\boxed{
\operatorname{Tr}\rho\,\Phi(\operatorname{ad}_T^{2r}\widetilde U_j)
\longrightarrow\tau>0.
}
\tag{4.10}
$$
只声明商上输出一致有界；(4.4) 中未压缩的 X 项可以很大，本文未声称这个 cheap 输入产生一个全空间一致有界弱单位。

## 5. 低输入费用没有删掉原交叉块

把 T 在原 N⊕E⊕L 上写成
$$
T=\begin{pmatrix}A&B&D\\0&0&F\\0&0&G\end{pmatrix}.
$$
上一稿的完整恒等式仍逐项适用于 U=tilde U_j：
$$
\begin{aligned}
\Phi(\operatorname{ad}_T^mU)
={}&FG^{m-1}U_{LE}+(-1)^mU_{EN}A^{m-1}B\\
&+\sum_{s=1}^{m-1}(-1)^s\binom ms
FG^{m-s-1}U_{LN}A^{s-1}B.
\end{aligned}
\tag{5.1}
$$
它与 (4.10) 给同一个 rho 的非零源余额。所有中段来源现在是便宜实际尾右源
$$
P_LE_F^*\widetilde R_FT^s\rho^{1/2},\quad s\ge1,
$$
但 T^s rho^(1/2) 仍落在 N。便宜源范数本身并没有令这列趋零，E_F* 也不保持原旗。

更精确地，原与尾替换输入的差为 -E_F*XH_F。由于 XH_F 把 E 送入 N，
$$
\boxed{\Phi(E_F^*XH_F)
=(E_F^*)_{EN}(H_F)_N B_X.}
\tag{5.2}
$$
在任何导子阶 m 也有
$$
\boxed{\Phi(\operatorname{ad}_T^m(E_F^*XH_F))
=(\operatorname{ad}_T^mE_F^*)_{EN}(H_F)_NB_X.}
\tag{5.3}
$$
这是完整实际的 N 向源项，不能由 pi(X)=0 宣称为零。

若把 E_F*X 写成 X E_F*+[E_F*,X]，两个项都必须保留；第一项的右因子不属于原解析代数，不能用原正常湮灭式免费删除。式 (5.2)–(5.3) 避免了这个容易遗漏的来源问题。

本文由原零式构造了低范数实际尾提升，并进一步付了同一商上的低输入导子弱单位。一般正常商的余目标现在是对 (5.1) 的完整原 rho 输运列作真正估计；没有把有限头/正常性或低像费用当作这个估计。
