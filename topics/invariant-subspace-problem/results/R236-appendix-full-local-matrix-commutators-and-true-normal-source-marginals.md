# R236 附录：完整局部矩阵导子与同一正常来源的真实部分迹

日期：2026-11-14 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。

状态：完整辅助来源定理，已逐项核验。以下所有对象在原 Haar 空间及同一有限放大上。先把固定二阶的两个加权矩加强为逐个位精确渐近，再给任意有限选中位的整个局部矩阵代数以及全部允许原右测试的统一公式。结论是原正常见证必须满足的来源结构；没有把局部秩一、来源的三阶幂零或无速率正常性当成矛盾。

依赖：[原混合截断及全部 carry 常数](R236-appendix-polynomial-relative-auxiliary-quadratic-exclusion.md)、[固定二阶/Walsh 来源场](R236-appendix-fixed-second-commutator-and-explicit-walsh-source-field.md)、[实际原右源与完整物理块](R236-appendix-actual-right-sources-and-normal-quotient-leakage.md)、[廉价物理尾提升](R236-appendix-cheap-physical-tail-lifts-and-quotient-derivative-units.md)。

## 1. 原对象和准确全局常数

沿原逐位 Xi∈{Ni,Yi}、系数 a_i,b_i，以及
$$
X=\sum_i a_iX_i,\qquad Y=\sum_i b_iX_i,
\qquad T=X^2+Y.
$$
使用 |a_i|≤A(i+1)^(-2)、充分高位 |a_i|≥a_-(i+1)^(-2)、|b_i/a_i|≥c(i+1)^(-2)，以及 B=Σ|b_i|<∞。固定正数 A,a_-,c，并记
$$
M_T=54A^2+3B,\quad D_T=324A^2+9B,
\quad K=\max(1,2M_T),\quad V=\max(1,B+12A^2).
\tag{1.1}
$$
真实 ||Xi||≤3、||Xi²||≤9eta_i、||Xi−Ei||≤4eta_i，eta_i≤exp(−770·16^i)。第 P 位保真低头/纯高尾模型给
$$
\|T\|,\|\widehat T\|\le M_T,
\quad \|T-\widehat T\|\le D_T\eta_{P-1},
$$
$$
\|\operatorname{ad}_T^m-\operatorname{ad}_{\widehat T}^m\|_{\rm cb}
\le2mD_TK^m\eta_{P-1}.
\tag{1.2}
$$
原逐位截断还给 $\|X_i-\widehat X_i\|\le9\eta_{P-1}$；由 $\sum_i|a_i|\le2A$，删去任意选中集合的背景同样满足 $\|X_F-\widehat X_F\|\le18A\eta_{P-1}$。下文 $2r$ 个线性因子的乘积差因此至多 $2r\cdot36A^2V^{2r-1}\eta_{P-1}\le72rA^2V^{2r}\eta_{P-1}$。此 cb 界仅用左右乘法的范数及幂差，因此不依赖有限放大维数。

固定原物理旗 N⊂M，E=M orthogonal-minus N、L=M^perp，pi(X)=pi(Y)=0，Phi 为 E 压缩。固定同一个正正常 rho 支撑 E，tau=Tr rho>0。记 C_i=pi(Xi)。

## 2. 单个位：翻转矩为超小，minus 矩有逐点主项

记
$$
Q_i^-=\frac{I-E_i-E_i^*}{2},\qquad
Z_i=2E_i^*E_i-I,
\qquad X_i^{\rm bg}=X-a_iX_i,
\qquad V_i=b_i+2a_iX_i^{\rm bg}.
$$
这里 Vi 是新的临时线性因子，不是旧 Cayley Walsh 元。

在第 i 位截断的纯选中位模型中，T_hat=T_bg+Ei Vhat_i；背景与该位完整矩阵代数交换。直接乘 2×2 矩阵给
$$
\operatorname{ad}_{E_i}^2(Z_i)=0,
\qquad \operatorname{ad}_{E_i}^2(Q_i^-)=E_i.
$$
因此
$$
\operatorname{ad}_{\widehat T}^2(Z_i)=0,
\qquad \operatorname{ad}_{\widehat T}^2(Q_i^-)=E_i\widehat V_i^2.
\tag{2.1}
$$
(1.2) 和两个线性因子的差给
$$
\|\operatorname{ad}_T^2(Z_i)\|
\le4D_TK^2\eta_{i-1},
\tag{2.2}
$$
$$
\|\operatorname{ad}_T^2(Q_i^-)-E_iV_i^2\|
\le(4D_TK^2+72A^2V^2)\eta_{i-1}.
\tag{2.3}
$$
原低位 carry 在这里是 eta_(i−1)，不能误写为 eta_i。

利用 pi(X)=0，有 pi(X_i^bg)=−a_i C_i，因此
$$
\pi(X_iV_i^2)
=C_i(b_i-2a_i^2C_i)^2
=b_i^2C_i-4b_i a_i^2C_i^2+4a_i^4C_i^3.
$$
真实平方 ||C_i²||≤9eta_i 及 ||C_i||≤3 给
$$
\|\pi(X_iV_i^2)-b_i^2C_i\|
\le(36|b_i||a_i|^2+108|a_i|^4)\eta_i.
$$
替换 Ei 为 Xi 再付 4V²eta_i，于是
$$
\boxed{\|\Phi(\operatorname{ad}_T^2Q_i^-)-b_i^2C_i\|
\le h_i,}
\tag{2.4}
$$
$$
h_i=(4D_TK^2+72A^2V^2)\eta_{i-1}
+(4V^2+36BA^2+108A^4)\eta_i.
$$
因为 |b_i|≥a_-c(i+1)^(-4)，h_i/|b_i|²→0。

令原固定输运迹类 K_rho=ρT²−2TρT+T²ρ，定义
$$
q_i=\operatorname{Tr}(K_\rho Q_i^-),\qquad
z_i=\operatorname{Tr}(K_\rho Z_i).
$$
循环迹以及 (2.2)、(2.4) 给
$$
\boxed{|z_i|\le4\tau D_TK^2\eta_{i-1},\qquad
|q_i-b_i^2\operatorname{Tr}(\rho C_i)|\le\tau h_i.}
\tag{2.5}
$$
原正常性保 C_i→I_E/2 于 WOT，故
$$
\boxed{\frac{q_i}{b_i^2}\longrightarrow\frac\tau2,
\qquad \frac{z_i}{b_i^2}\longrightarrow0.}
\tag{2.6}
$$
复数 b_i 也适用，除法是对准确复平方 b_i²；并不需要先假 b_i 为正。

## 3. 所有选中位矩阵的纯最高导子

固定整数 P≥r≥1，F⊂{P,...,2P−1}，|F|=r。D 为该 r 位的任意矩阵，恒等扩张到其余物理位。令
$$
d_F(D)=\langle e_0^{\otimes F},D e_1^{\otimes F}\rangle,
\qquad E_F=\prod_{i\in F}E_i,
$$
$$
X_F=X-\sum_{i\in F}a_iX_i,
\qquad P_F(z)=\prod_{i\in F}(b_i+2a_i z)^2,
\qquad c_r=(-1)^r(2r)!.
$$
在第 P 位截断后，T_hat=T_bg+S_F，其中 T_bg 与整个 F 位矩阵代数交换，且
$$
S_F=\sum_{i\in F}E_i(b_i+2a_i\widehat X_F)
+2\sum_{i<j\in F}a_i a_jE_iE_j.
$$
S_F 每项都有至少一个选中位，因此 S_F^(r+1)=0；在 S_F^r 中每项必须恰取 r 个不同的一次位，准确有
$$
S_F^r=r! E_F\prod_{i\in F}(b_i+2a_i\widehat X_F).
$$
完整 2r 次导子展开中只剩左右各 r 次的一项。因为 E_F D E_F=d_F(D)E_F，得到
$$
\boxed{
\operatorname{ad}_{\widehat T}^{2r}(D)
=c_r d_F(D)E_F P_F(\widehat X_F).
}
\tag{3.1}
$$
这覆盖整个 M_(2^r)，不只 E_F* 或 Q_F^-。对任意额外矩阵放大，d_F 是同一个角映射，完全收缩；证明及以下误差不增加维数因子。

## 4. 全实际 cb 误差与重复位消去

定义实际 A_F=∏_(F)Xi、Z_F=Σ_(F)aiXi，及其商像 C_F=∏_(F)C_i、Zbar_F=Σ_(F)ai C_i。真实逐因子差给
$$
\|A_F-E_F\|\le4r3^{r-1}\eta_P,
\qquad \|A_F\|\le1+4r3^{r-1}\eta_P.
\tag{4.1}
$$
最高多项式差为
$$
\|P_F(\widehat X_F)-P_F(X_F)\|
\le72rA^2V^{2r}\eta_{P-1}.
$$
结合 (1.2)、(3.1)、(4.1)，有一个完整全空间近似：
$$
\begin{aligned}
\|\operatorname{ad}_T^{2r}(D)-c_rd_F(D)A_FP_F(X_F)\|
\le\|D\|\big[&4rD_TK^{2r}\eta_{P-1}\\
&+(2r)!72rA^2V^{2r}\eta_{P-1}\\
&+(2r)!4r3^{r-1}V^{2r}\eta_P\big].
\end{aligned}
\tag{4.2}
$$
它也在每个额外矩阵放大成立。

现在才使用原 pi(X)=0。于是 pi(X_F)=−Zbar_F，且
$$
\pi(A_FP_F(X_F))
=C_F\prod_{i\in F}(b_i-2a_i\overline Z_F)^2.
$$
记 gamma_F=∏_(F)b_i²。每个非恒项都有 C_F Zbar_F 因子，并且每个求和项含一个真实重复位。由平方关系得到
$$
\|C_F\overline Z_F\|
\le9\eta_P3^{r-1}\frac{Ar}{P^2}.
\tag{4.3}
$$
逐个替换 2r 个线性因子，||b_i−2ai Zbar_F||≤V；因此
$$
\boxed{
\|\pi(A_FP_F(X_F))-\gamma_F C_F\|
\le\frac{36A^2r^2 3^{r-1}V^{2r-1}}{P^4}\eta_P.
}
\tag{4.4}
$$
这里没有对 Zbar_F 或任何尾算子取形式逆。

定义唯一标量归一化费用
$$
J_{P,r}=\frac{(2P)^{8r}}{(a_-c)^{2r}},
\qquad |\gamma_F|^{-1}\le J_{P,r},
$$
以及
$$
\begin{aligned}
e_{P,r}=J_{P,r}\bigg[&
\left(\frac{4rD_TK^{2r}}{(2r)!}+72rA^2V^{2r}\right)\eta_{P-1}\\
&+\left(4r3^{r-1}V^{2r}
+\frac{36A^2r^2 3^{r-1}V^{2r-1}}{P^4}\right)\eta_P
\bigg].
\end{aligned}
\tag{4.5}
$$
全部系数固定时，e_(P,r)→0 对每个固定 r 成立；实际上
$$
\sup_{1\le r\le P}e_{P,r}\longrightarrow0,
\tag{4.6}
$$
因为除 eta_(P−1) 外全部正因子的对数至多 O(P log(P+1))，而 −log eta_(P−1)≥770·16^(P−1)。

(4.2)–(4.5) 得完整局部矩阵映射的实际 cb 估计：
$$
\boxed{
\left\|\frac{\Phi(\operatorname{ad}_T^{2r}D)}{c_r\gamma_F}
-d_F(D)C_F\right\|\le e_{P,r}\|D\|.
}
\tag{4.7}
$$
此式完全有界范数的误差同样≤e_(P,r)。归一后的整个局部输入映射距离角映射 D↦d_F(D)C_F 趋零；目标 cb 范数≤1+4r3^(r−1)eta_P，故对 r≤P 一致有界。

## 5. 同一正常态的完整部分迹，不丢矩阵维数

令 m=2r，并在同一原全空间上定义
$$
\boxed{
K_{\rho,m}=
\sum_{s=0}^{m}(-1)^s\binom ms T^s\rho T^{m-s}.
}
\tag{5.1}
$$
所有幂有界，K_rho,m 迹类；有限秩 rho 时 rank K_rho,m≤(m+1)rank rho。循环迹给
$$
\operatorname{Tr}(K_{\rho,m}D)
=\operatorname{Tr}(\rho\operatorname{ad}_T^mD).
$$
取 F 位的真正部分迹 denoted R_F(K)，也将有限放大因子并入被迹去的部分。由 (4.7) 对全部 ||D||≤1 的统一界，迹范数对偶直接给
$$
\boxed{
\left\|\frac{\mathcal R_F(K_{\rho,2r})}{c_r\gamma_F}
-\operatorname{Tr}(\rho C_F)E_F\right\|_1
\le\tau e_{P,r}.
}
\tag{5.2}
$$
没有逐个矩阵元求和，故不出现 2^r 或 4^r 的额外维数费用。

对固定 r，原正常性与 (4.1) 给
$$
\sup_{F\subset[P,2P),\ |F|=r}
\left|\operatorname{Tr}(\rho C_F)-2^{-r}\tau\right|
\longrightarrow0.
$$
证明先用有限柱支撑的迹类近似 rho；在所有充分高 F 上 E_F 的柱压缩准确是 2^(-r)I，再用统一 ||A_F||≤1+o(1) 付余量。整个正常误差不乘 gamma_F^(-1)。所以
$$
\boxed{
\sup_{F\subset[P,2P),\ |F|=r}
\left\|\frac{\mathcal R_F(K_{\rho,2r})}{\gamma_F}
-(-1)^r\frac{(2r)!}{2^r}\tau E_F\right\|_1
\longrightarrow0.
}
\tag{5.3}
$$
这是完整局部来源矩阵的迹范数结论，不仅是一条 q_F 配对。

对于增长 r，可保留未乘 (2r)! 的 (5.2) 和完全有界式 (4.7)。其正常锚 2^(-r)tau 会变小；不由此声称增长 r 仍有统一非零锚。全部正常近似误差始终须按实际归一化处理。

令 Q_F^-=∏_(F)Q_i^-，则 Tr(E_F Q_F^-)=(-1/2)^r，故固定 r 时
$$
\boxed{
\frac{\operatorname{Tr}(K_{\rho,2r}Q_F^-)}{\prod_{i\in F}b_i^2}
\longrightarrow\frac{(2r)!}{4^r}\tau
}
\tag{5.4}
$$
在上述 F 上一致。若局部测试 D 的唯一角 d_F(D)=0，则其同归一化来源矩趋零，且由 (4.7) 有明确 e_(P,r) 级误差。

## 6. 全部原右测试：保留同 rho 和其原湮灭授权范围

以下给两种准确适用方式，不能互换未给出的假设。

第一种，H 属原旗保持的测试代数且与 T、Xi 交换。将 (4.2) 的全空间近似右乘同一 H，再压缩，并使用实际同态 pi，而不是把一般 Phi(O H) 写成 Phi(O)pi(H)，即可得到 (4.7) 的右测试版本，误差乘 ||H||。

第二种，若原见证另给完整 A′ 右零式
$$
\operatorname{Tr}(\rho XG)=0\qquad(G\in\mathcal A'),
\tag{6.1}
$$
则可对每个固定 H∈A′ 作同样的标量结论，即使没有另外证明 H 保持这面具体的物理旗。理由如下。

先在 (4.2) 中真正右乘 H。H 与 T 交换，故 ad_T^m(DH)=(ad_T^mD)H。唯一需要删除的原项来自有限多项式差
$$
P_F(X_F)-P_F(-Z_F)=X D_F(X_F,-Z_F).
$$
其右因子 A_F D_F H 属原 A′，所以由 (6.1) 精确消去。余下 A_F P_F(−Z_F)−gamma_F A_F 的全空间范数仍由 (4.3)–(4.4) 的实际重复位证明控制；这里完全不使用 pi(H)。

因此对所有局部 D，
$$
\left|\frac{\operatorname{Tr}(\rho\operatorname{ad}_T^{2r}(DH))}{c_r\gamma_F}
-d_F(D)\operatorname{Tr}(\rho A_FH)\right|
\le\tau\|H\|e_{P,r}\|D\|.
\tag{6.2}
$$
由于 H 与 T 交换，左侧首项准确等于 Tr(H K_rho,2r D)/(c_r gamma_F)。再次取完整迹范数对偶，得到
$$
\boxed{
\left\|\frac{\mathcal R_F(HK_{\rho,2r})}{c_r\gamma_F}
-\operatorname{Tr}(\rho A_FH)E_F\right\|_1
\le\tau\|H\|e_{P,r}.
}
\tag{6.3}
$$
对固定 r 和固定允许 H，正常性使 Tr rho A_FH→2^(-r)Tr rho H，故
$$
\boxed{
\frac{\mathcal R_F(HK_{\rho,2r})}{\gamma_F}
\longrightarrow(-1)^r\frac{(2r)!}{2^r}
\operatorname{Tr}(\rho H)E_F
\quad\text{于迹范数，统一于上述 }F.
}
\tag{6.4}
$$
所用泛函一直是原 rho；没有把 HK_rho,2r 当作新正态。H 随 P 增长时，仍须保 (6.3) 中 ||H||e_(P,r) 及原正常配对的实际预算，不能借固定 H 的结论免费通过。

### 6.1 一个有界原移动右测试，说明固定 H 不能省略

取 r=1、F={i}，令 H_i=I−X_i。它属于原 Acal，范数≤4，且真实平方给
$$
\operatorname{Tr}(\rho X_iH_i)
=\operatorname{Tr}(\rho X_i)-\operatorname{Tr}(\rho X_i^2)
\longrightarrow\tau/2.
$$
另一方面
$$
\tfrac12\operatorname{Tr}(\rho H_i)\longrightarrow\tau/4.
$$
所以即使 H_i 是一致有界的实际解析右测试，也不能在 (6.3) 中统一把 Tr rho A_F H_i 改成 2^(-r)Tr rho H_i。这个例子保同一个原 rho、同一 Xi 及全部真实 carry；它只反对该不合法的统一因式化，不反对 (6.3) 的完整式。

## 7. 这些部分迹来自完整的三个物理块

由于 pi(T)=0，在原 N⊕E⊕L 上写
$$
T=\begin{pmatrix}A&B&D\\0&0&F\\0&0&G\end{pmatrix}.
$$
对 m=2r，(5.1) 的所有项给准确原块
$$
\boxed{
K_{\rho,m}=
\begin{pmatrix}
0&A^{m-1}B\rho&\displaystyle\sum_{s=1}^{m-1}(-1)^s\binom ms
 A^{s-1}B\rho FG^{m-s-1}\\
0&0&\rho FG^{m-1}\\
0&0&0
\end{pmatrix}.
}
\tag{7.1}
$$
中段全部二项权和均保留。由真实三角位置 K_rho,m³=0；这只是来源结构，不能与 (5.3) 的局部 rank-one 极限合起来当作矛盾，部分迹不保乘法。

本稿付出了逐点超小 z 矩、非零 q_i/b_i² 渐近、整个局部矩阵代数的 cb 归约、实际完整部分迹的迹范数渐近，以及全部原允许右测试的同 rho 版本。仍须利用 (7.1) 的来源与原正 rho 的额外关系，证明这些已确定的局部剖面不能同时实现；本文没有省掉这一步。
