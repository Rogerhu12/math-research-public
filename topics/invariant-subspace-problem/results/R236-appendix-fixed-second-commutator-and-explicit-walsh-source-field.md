# R236 附录：固定二阶的正常商强单位与同一正常态的显式单个位来源场

日期：2026-11-14 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。

状态：下列固定二阶构造、显式场分解和完整来源已逐项核验。沿上一廉价实际尾提升的原模型、同一有限放大物理旗和同一正常密度。这里不再令导子阶数随截断增长：固定二阶已经产生同商强单位，而且全部逆可在付清实际误差后化为两个明确的单个位矩阵。剩余来源只看固定的 T rho、T² rho；不把加权正常尾矩的 c0 性当作有速率估计，未证明一般正常商为零。

依赖：

- [原混合N/Y行与真实截断](R236-appendix-polynomial-relative-auxiliary-quadratic-exclusion.md)；
- [原物理旗及完整来源块](R236-appendix-actual-right-sources-and-normal-quotient-leakage.md)；
- [实际尾代表、准确差商来源和同商压缩](R236-appendix-cheap-physical-tail-lifts-and-quotient-derivative-units.md)。本文重付固定二阶所需的全部常数。

## 1. 固定的原对象与常数

令原 Haar Xi 逐位取 Ni 或 Yi=Ni(I+Ni)^(-1)。使用真实关系
$$
\|X_i\|\le3,\quad \|X_i^2\|\le9\eta_i,
\quad \|X_i-E_i\|\le4\eta_i,
\qquad \eta_i\le e^{-770\,16^i}.
$$
系数满足 |a_i|≤A(i+1)^(-2)，充分高位还满足 |a_i|≥a_-(i+1)^(-2)、|b_i/a_i|≥c(i+1)^(-2)，并令 B=Σ|b_i|<∞。A,a_-,c 均严格正。设
$$
X=\sum_i a_iX_i,\qquad Y=\sum_i b_iX_i,
\qquad T=X^2+Y.
$$
这里 T 是辅助两行零式的二次式，没有原排核稿中的减平方项。固定原有限放大闭旗 N⊂M，E=M orthogonal-minus N、L=M^perp，pi 为原解析代数的商表示、Phi 为全部算子的物理 E 压缩。假设
$$
\pi(X)=\pi(Y)=0.
$$
于是 pi(T)=0。固定同一个正常正密度 rho 支撑在 E，tau=Tr rho>0；以下不改 rho，不更换物理内积。若原 rho 有限秩，下文所有输运迹类算子也保持有限秩。

取安全常数
$$
M_T=54A^2+3B,\quad D_T=324A^2+9B,
\quad K=\max(1,2M_T),\quad V=\max(1,B+12A^2),
$$
$$
\kappa=6A/c,\quad d=36A^2/c^2,
\quad C_0=4(1+\kappa)^2,
\quad B_P=\frac{(2P)^8}{(a_-c)^2}.
\tag{1.1}
$$
实际 ||T||≤M_T。截断到第 P 位的保真低头/纯高尾辅助 T_hat 满足 ||T_hat||≤M_T、||T−T_hat||≤D_T eta_(P−1)。此处完全不需要任何低头 nilpotent 指数与导子阶数的比较。

## 2. 一个位的真实逆及准确二项近似

对 i∈I_P={P,...,2P−1}，记
$$
\lambda_i=\frac{2a_i^2}{b_i},\qquad
\beta_i=b_i^{-2},\qquad
\widetilde R_i=(b_i-2a_i^2X_i)^{-2}
=\beta_i(I-\lambda_iX_i)^{-2}.
\tag{2.1}
$$
有 |lambda_i|≤2A/c、||lambda_i Xi||≤kappa、||lambda_i²Xi²||≤d eta_i，且 |beta_i|≤B_P。取 P 足够高使 d eta_P≤1/2。实际因式
$$
(I-z)^{-1}=(I+z)(I-z^2)^{-1},\qquad z=\lambda_iX_i,
$$
由 Neumann 逆直接给
$$
\boxed{\|\widetilde R_i\|\le C_0|\beta_i|\le C_0B_P.}
\tag{2.2}
$$
这是原实际尾代数内的逆，不是由商像范数反推提升。

二项近似的准确恒等式为
$$
(I-z)^{-2}-(I+2z)=z^2(3I-2z)(I-z)^{-2}.
$$
从而
$$
\left\|\widetilde R_i-\beta_i(I+2\lambda_iX_i)\right\|
\le C_0d(3+2\kappa)|\beta_i|\eta_i.
\tag{2.3}
$$
记 P_(0,i)=E_i^*E_i 为原物理 e0 投影。由 (2.3) 和 ||Xi−Ei||≤4eta_i，
$$
\boxed{
\left\|E_i^*\widetilde R_i-
\beta_i(E_i^*+2\lambda_iP_{0,i})\right\|
\le C_{\rm loc}|\beta_i|\eta_i,
}
\tag{2.4}
$$
其中
$$
C_{\rm loc}=C_0d(3+2\kappa)+16A/c.
$$
所有近似都在全原空间的算子范数中成立，有限放大常数不变。

## 3. 固定二阶已经足够：同商强单位

定义真实输入和等权目标
$$
U_P=-\frac1P\sum_{i\in I_P}E_i^*\widetilde R_i,
\qquad R_P=\frac2P\sum_{i\in I_P}E_i.
\tag{3.1}
$$
||U_P||≤C_0B_P=O(P^8)。这个输入在原 ≥P 尾上。

在第 P 位保真截断后，选中位是纯 Ei，且删去 i 的背景
$$
X_i^{\rm bg}=X-a_iX_i
$$
与 Ei 的纯辅助版本完全交换。固定二阶的准确纯身份是
$$
\operatorname{ad}_{\widehat T}^2(E_i^*)
=-2E_i(b_i+2a_i\widehat X_i^{\rm bg})^2.
\tag{3.2}
$$
无需 2^P 次的低头幂消失。原 tilde R_i 与实际 T 交换，所以先对 E_i* 比较实际导子，之后右乘同一个实际 tilde R_i。由两次幂差及最高多项式差，
$$
\left\|\operatorname{ad}_T^2U_P-
\frac2P\sum_i E_i(b_i+2a_iX_i^{\rm bg})^2\widetilde R_i\right\|
\le C_0B_P(4D_TK^2+144A^2V^2)\eta_{P-1}.
\tag{3.3}
$$
例如幂差界为 4D_T K² eta_(P−1)；两个线性因子的差给 72A²V² eta_(P−1)，再乘 (3.2) 的 2，得到第二项。

令 p_i(z)=(b_i+2a_i z)^2，并取真正有限多项式差商
$$
D_i(u,v)=\frac{p_i(u)-p_i(v)}{u-v}
=2a_i\bigl[(b_i+2a_i u)+(b_i+2a_i v)\bigr].
$$
在 u=X_i^bg、v=−a_iXi 处，u−v=X，且 ||D_i(u,v)||≤4AV。因此
$$
p_i(X_i^{\rm bg})\widetilde R_i
=I+X D_i(X_i^{\rm bg},-a_iX_i)\widetilde R_i.
\tag{3.4}
$$
Xi X D_i tilde R_i 在原解析代数内且商像为零。Ei 与 Xi 的实际范数差付清后，(3.3)–(3.4) 给
$$
\boxed{
\|\Phi(\operatorname{ad}_T^2U_P)-\Phi(R_P)\|
\le\varepsilon_P,
}
\tag{3.5}
$$
$$
\varepsilon_P=C_0B_P\left[
(4D_TK^2+144A^2V^2)\eta_{P-1}
+192A^2V\eta_P\right]\longrightarrow0.
\tag{3.6}
$$
这里第二项是 2×4eta_P×6A×4AV×C_0B_P。没有用 pi(Ei) 的乘法性。

Boolean 单层和满足 ||Σ_(I_P)Ei||≤(P+1)/2，所以 ||R_P||≤1+1/P。对任意固定有限柱 x，P 高于它的全部物理支撑时，各个单高位波动正交，准确有
$$
\|(R_P-I)x\|=P^{-1/2}\|x\|.
$$
由有限柱稠密性得 R_P→I 强。结合 (3.5)，
$$
\boxed{\Phi(\operatorname{ad}_T^2U_P)\longrightarrow I_E
\quad\text{强收敛，且压缩输出一致有界。}}
\tag{3.7}
$$
所以同一个正常 rho 满足
$$
\operatorname{Tr}\rho\,\Phi(\operatorname{ad}_T^2U_P)\longrightarrow\tau.
\tag{3.8}
$$
这一步先对有限秩迹类近似用强收敛，再用输出的一致界，适用于原任意迹类 rho。

## 4. 把全部实际逆换成显式单个位场

在原物理位定义
$$
Q_i^-=\frac{I-E_i-E_i^*}{2},\qquad
Z_i=P_{0,i}-(I-P_{0,i})=2P_{0,i}-I.
$$
Q_i^- 是 Walsh minus 投影，Z_i 交换该位的 Walsh plus/minus。定义完全显式的局部场
$$
\boxed{
W_P=\frac1P\sum_{i\in I_P}\beta_i
(2Q_i^--\lambda_i Z_i).
}
\tag{4.1}
$$
同时令原解析项
$$
G_P=\frac1P\sum_{i\in I_P}\beta_i(X_i-I-\lambda_i I).
$$
因为 −Ei*=Xi−I+2Q_i^-+(Ei−Xi)，式 (2.4) 给准确已付分解
$$
\boxed{\|U_P-G_P-W_P\|
\le(C_{\rm loc}+4)B_P\eta_P.}
\tag{4.2}
$$
G_P 与 T 交换，所以 ad_T²G_P=0。故 (3.7) 直接加强为
$$
\boxed{\Phi(\operatorname{ad}_T^2W_P)\longrightarrow I_E
\quad\text{强，且一致有界。}}
\tag{4.3}
$$
与 (3.5) 对同一 R_P 的范数误差至多
$$
\varepsilon_P+4M_T^2(C_{\rm loc}+4)B_P\eta_P.
\tag{4.4}
$$
因此此同商强单位已不含任何隐含右逆或高阶输入：W_P 只由两个原单个位矩阵组成。其范数仍可增长，||W_P||≤(2+2A/c)B_P。

若 a_i>0、b_i=a_i²，则 lambda_i=2、beta_i=a_i^(-4)，W_P 自伴。
特别 a_i=(i+1)^(-2) 时
$$
W_P=\frac2P\sum_{i=P}^{2P-1}(i+1)^8(Q_i^--Z_i).
\tag{4.5}
$$
没有把这些物理矩阵假定为原旗的保持算子。

对任何位于第 P 位之前的有限柱 x，Q_i^-x=0，Z_i x 两两正交，所以还有准确物理列公式
$$
\boxed{\|W_Px\|^2
=\frac1{P^2}\sum_{i\in I_P}|\beta_i\lambda_i|^2\,\|x\|^2.}
\tag{4.6}
$$
它保留实际单个位结构，比把每一项独立乘总范数少一个平方根的池计数；它本身并不支付未知正常向量的相应加权尾。

## 5. 完整同 rho 来源只剩固定三个块

把原 T 写成
$$
T=\begin{pmatrix}A&B&D\\0&0&F\\0&0&G\end{pmatrix}
\quad\text{于 }N\oplus E\oplus L.
$$
对 U_P 或 W_P，完整二阶公式都是
$$
\boxed{\Phi(\operatorname{ad}_T^2 W_P)
=FG(W_P)_{LE}+(W_P)_{EN}AB-2F(W_P)_{LN}B.}
\tag{5.1}
$$
没有增长的 T^s rho 族，也没有省去两个端点或中段。由 (4.3)，这三个固定来源的同 rho 迹和趋于 tau。

更精确地，把 rho 视作全原空间上仅 E 支撑的迹类算子，定义同一个固定迹类
$$
\mathcal K_\rho=\rho T^2-2T\rho T+T^2\rho.
\tag{5.2}
$$
循环迹给 Tr rho ad_T²W=Tr K_rho W。其完整块为
$$
\boxed{
\mathcal K_\rho=
\begin{pmatrix}
0&AB\rho&-2B\rho F\\
0&0&\rho FG\\
0&0&0
\end{pmatrix}.}
\tag{5.3}
$$
因此 K_rho³=0、Tr K_rho=0；若 rho 有限秩，rank K_rho≤3 rank rho。对每个与 T 交换的有界 H，还准确有 Tr K_rho H=0。

令
$$
q_i=\operatorname{Tr}(\mathcal K_\rho Q_i^-),\qquad
z_i=\operatorname{Tr}(\mathcal K_\rho Z_i).
$$
这些是同一原 rho 经固定两次 T 输运产生的确切复矩。由 (4.1)、(4.3)，得到新的有限矩余额
$$
\boxed{
\frac1P\sum_{i=P}^{2P-1}b_i^{-2}
\left(2q_i-\frac{2a_i^2}{b_i}z_i\right)
\longrightarrow\tau>0.}
\tag{5.4}
$$
q_i→0，因为 Q_i^-→0 强；z_i→0，因为 Z_i→0 WOT，且 Z_i 一致有界，K_rho 迹类。上述极限由正常性提供，但没有速率。式 (5.4) 保留全部加权和，不能由这两个 c0 结论判为零。

在 a_i=(i+1)^(-2)、b_i=a_i² 的指定正系数情形，(5.4) 是
$$
\boxed{\frac2P\sum_{i=P}^{2P-1}(i+1)^8(q_i-z_i)
\longrightarrow\tau.}
\tag{5.5}
$$
尤其对所有充分大 P，
$$
\max_{P\le i<2P}|q_i-z_i|
\ge\frac{\tau}{4(2P)^8}.
\tag{5.6}
$$
这只是实际输运矩的必要下界，不是原 rho 的正概率尾下界；K_rho 通常非正，不能把它当另一个正常状态。

## 6. 准确收获及剩余处

本稿把上一稿中 r=2^j 的高阶同商单位，降到固定二阶的原实际单位；同 rho 的全部输入可换成显式单个位数算子/翻转算子场，原逆和其 carry 全部付清。完整来源现在只涉及固定的 AB rho、rho FG、B rho F 三块；非零锚为同一个 tau。

尚须利用这三块的真实原旗来源与 X、Y 全右倍数零式，控制 (5.4) 的加权矩。一般迹类矩的 c0 性、有限秩、(4.6) 的有限柱式或 W_P 的自伴性，单独均没有付出该控制。本文不作不存在一般正常湮灭者、未知不变子商稠密像或普通 ISP 完成的结论。
