# R236 附录：逐位N/Y与任意复相位的原Haar二次排核

日期：2026-11-14 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。

状态：root 已全文核验的完整扩展。它只扩展[原N二次排核](R236-appendix-actual-slow-positive-quadratic-kernel-exclusion-by-joint-inverse.md)的算子族；仍是完整 Haar 空间排核，不是任意正常主理想或未知子商上的排核。

## 1. 原 Haar 的逐位 N/Y 二次族

逐位任取
$$
X_i\in\{N_i,Y_i\},\qquad Y_i=N_i(I+N_i)^{-1}.
$$
固定 k≥0，系数相位任意，仅要求
$$
|a_i|=(i+1)^{-2}\quad(i\ge k).
$$
令
$$
X=\sum_{i\ge k}a_iX_i,\quad
B_0=\sum_{i\ge k}a_i^2X_i^2,\quad
Y=\sum_{i>k}a_i^2X_i,
\qquad T=X^2-B_0+Y.
\tag{1.1}
$$
这里 a_i² 是原复数平方，并没有替换为 |a_i|²。全部算子在原 A 的范数代数内，且对同一个反射共轭 C 对称。

**定理。** (1.1) 的 T 单射、值域稠密。系数相位可以逐位任意，N/Y 可以逐位混用。对有限放大相同；不需要 first-flip 非零条件。

## 2. 混合模型与完整 carry 差

截断点 L>k 时，i<L 用原有限头 N_i^[L] 或 Y_i^[L]=N_i^[L](I+N_i^[L])^(-1)；i≥L 用纯 E_i。把所选项统一记作 hat X_i。低头与纯高尾组成同一个原 Haar 空间上的混合模型。

真实递推及逆差给
$$
\|X_i\|,\|\widehat X_i\|\le3,
\qquad
\|X_i-\widehat X_i\|\le9\eta_{L-1}
\quad\text{对全部 }i.
\tag{2.1}
$$
低头 Y 的差使用两个 (I+N) 逆范数<3。高尾 Y_i-E_i 的范数≤4eta_i，已包含在 (2.1)。

以 hat X_i 定义 hat T，有
$$
\|X\|,\|\widehat X\|\le6,\qquad
\|B_0\|,\|\widehat B_0\|\le18,\qquad
\|Y\|,\|\widehat Y\|\le6,
$$
$$
\|T\|,\|\widehat T\|\le60,
\qquad
\|T-\widehat T\|\le342\eta_{L-1}\le400\eta_{L-1}.
\tag{2.2}
$$
其中 X² 的差≤12·18eta=216eta，B_0 差≤108eta，Y 差≤18eta。故对 δ=ad_T、hatδ=ad_hatT，
$$
\boxed{\|\delta^m-\widehat\delta^m\|
\le7m\,120^m\eta_{L-1}\quad(m\ge1).}
\tag{2.3}
$$
因为两导子范数≤120、其差≤800eta，且 800/120<7。

## 3. 复移位的共同 Laplace 公式

仍取 r=2^L、q=r²/4、I_L=[L,L+q)、M_L=L+q，L≥4。对 |F|=r，令
$$
X_F=\sum_{i\ge k,\ i\notin F}a_i\widehat X_i.
$$
[R215 §§2–4](R215-slow-semigroup-resolvent-and-normal-annihilator-tail.md) 的逐位任意相位和 N/Y 混合量词给
$$
\|e^{zX_F}\|\le e^{16\sqrt{|z|}}\quad(z\in\mathbb C),
\tag{3.1}
$$
有限保真头/纯高尾版本使用同一幂估计，常数仍为16。

选中位的一次系数仍准确为
$$
V_{j,F}=a_j^2+2a_jX_F=2a_j(X_F+c_j),\qquad c_j=a_j/2.
$$
现在 c_j 可以有任意相位。写 c_j=|c_j|e^(i theta_j)，令 zeta_j=e^(-i theta_j)。实际逆的旋转 Laplace 公式为
$$
(X_F+c_j)^{-2}
=\zeta_j^2\int_0^\infty t\,e^{-|c_j|t}e^{-\zeta_jtX_F}\,dt.
\tag{3.2}
$$
该范数积分收敛，按算子指数微分给左右逆平方；没有假设所有移位都落在同一个实半平面。

乘起所有 (3.2) 后，公共算子指数的复时间是 Σzeta_j t_j，故
$$
\left\|e^{-(\sum\zeta_jt_j)X_F}\right\|
\le e^{16\sqrt{|\sum\zeta_jt_j|}}
\le e^{16\sqrt{\sum t_j}}.
$$
所以前稿的单纯形积分预算逐字保留：若 c=min|c_j|≥1/(2M_L²)，
$$
\left\|\prod_{j\in F}(X_F+c_j)^{-2}\right\|
\le(2/c)^{2r}e^{128/c}
\le(4M_L^2)^{2r}e^{256M_L^2},
$$
$$
\boxed{\left\|\prod_{j\in F}V_{j,F}^{-2}\right\|
\le4^rM_L^{8r}e^{256M_L^2}.}
\tag{3.3}
$$
相位绝对值为1，不产生额外费用。特别这里一次支付整个乘积，没有逐个相乘指数预算。

## 4. 所选位最高项和局部导子仍精确

hat T 在所选平方零变量上的无常数项 W_F，满足
$$
W_F^{r+1}=0,\qquad W_F^r=r!E_F\prod_FV_{j,F}.
$$
因此
$$
\widehat\delta^{2r}(E_F^*)
=(-1)^r(2r)!E_F\prod_FV_{j,F}^2.
\tag{4.1}
$$
不同 N/Y 选择只影响删去所选位后的背景；所有所选高位在混合模型中都是 E_j，故没有更改 (4.1) 的线性系数。

另一方面，低头每个 Y_i^[L] 都是同一个头幂零 A_L=N_0^[L] 的无常数项多项式：其逆是有限几何多项式。对任意固定 h 头矩阵 D、L≥h，hat T 的所有含头项组成 K_L，仍有 K_L^(2^L)=0。因此
$$
\widehat\delta^{2r}(D)=0.
\tag{4.2}
$$
这两个恒等式都不把原核当成混合核。

## 5. 一致弱单位与所有实际误差

定义
$$
U_L=\frac{(-1)^r2^r}{(2r)!\binom qr}
\sum_{|F|=r}E_F^*\prod_FV_{j,F}^{-2},
\qquad
R_L=\frac{2^r}{\binom qr}\sum_{|F|=r}E_F.
$$
由 (3.3)–(4.1)，
$$
\widehat\delta^{2r}(U_L)=R_L,
\qquad
\|U_L\|\le\frac{8^rM_L^{8r}}{(2r)!}e^{256M_L^2}.
$$
纯高位平均与系数相位和 N/Y 选择完全无关。其范数由 Boolean 层入射界给 ||R_L||≤e^5，且对固定有限柱的矩阵元准确为恒等矩阵元，故 R_L→I WOT。

由 (2.3)，把前稿误差换为
$$
\varepsilon_L=14r\,120^{2r}\eta_{L-1}
\frac{8^rM_L^{8r}}{(2r)!}e^{256M_L^2}.
$$
则
$$
\|\delta^{2r}(U_L)-R_L\|\le\varepsilon_L,
\qquad
\|\delta^{2r}(D)\|\,\|U_L\|\le\varepsilon_L\|D\|.
\tag{5.1}
$$
L≥4 时 M_L≤r²/3，舍弃 factorial 后，
$$
\log\varepsilon_L
\le-\left(\frac{770}{16}-\frac{256}{9}\right)r^4
+r\log8+16r\log r+\log(14r)+2r\log120.
$$
r≥16 时后四项≤4r²+14r≤r^4/8。因此仍有
$$
\boxed{\varepsilon_L\le e^{-19r^4}.}
\tag{5.2}
$$

## 6. 排除同一个真实核

对原 f,g∈ker T，原 C 对称性给
$$
B(D\delta^{2r}(U_L)f,g)=B(\delta^{2r}(D)U_Lf,g).
$$
由 (5.1)–(5.2) 及一致有界 R_L→I WOT，得到 B(Df,g)=0 对每个有限头矩阵 D 成立。以 P_h 与 C 交换及头矩阵 D_hP_hf=P_hCf 的原 Haar 检验，得到 f=0。故 ker T=0；T*=CTC 再给像稠密。

不需要正系数。正性只在前稿简化了 Laplace 时间，本稿用 (3.2) 付完整复方向。

## 7. 正常接口仍保留的限制

这个结论同时排除相应的 N、Y 及逐位混合二次核，因此从这些原核提取的正正常闭像缺陷没有非零实例。它并不排除一个没有这些原核来源的正常两行湮灭者；也不把全 H 上的 T 单射稠密传给未知半不变商。

若直接在未知商 E 上把 E_F^* 替成 π(N_F)^*，则压缩不保留这里的最高导子等式；高位强近似没有付合并逆增长后的误差。对此本稿不作外推。

## 符号与负边界线性算子的区分

本文的T始终是原Haar空间上的二次式(1.1)。[R200 §1](R200-boundary-right-shift-domains-and-forward-division-saturation.md)中的T_N、T_Y则是在负边界空间ℓ²(N0)上，以边界移位B构成的线性慢和；它们至少以e0为核向量。二者只是历史符号重名，本文不排除这些边界线性核，也不解决其M=kerT、N=closure(BM)的N=M。
