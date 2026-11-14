# R236 附录：真实N慢正二次式的合并逆预算与全核排除

日期：2026-11-14 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。

状态：**完整证明；root 全文核验，另一代理独立核验原核导子、局部头与误差转移。** 本稿直接处理之前 first-flip 分支使用的同一个实际 N 二次式；不是从纯模型迁移一个未付的结论。全部原 carry、原 Haar 配对、高位平均及全域逆费用均列出。结论只排除这个明确二次式的核；不声称排除任意正常主理想湮灭态，普通 Hilbert ISP 仍开。

## 1. 指定的原实际算子

固定任意整数 k≥0，置 a_i=(i+1)^(-2) 对 i≥k，并令
$$
X=\sum_{i\ge k}a_iN_i,\qquad
B_0=\sum_{i\ge k}a_i^2N_i^2,\qquad
Y=\sum_{i>k}a_i^2N_i,
$$
$$
\boxed{T=X^2-B_0+Y.}
\tag{1.1}
$$
所有和按原 Haar 算子范数收敛。真实 N_i 属于原 A 的范数代数，满足
$$
N_i=E_i+\eta_iE_i^*N_{i+1},\quad
N_i^2=\eta_iN_{i+1},\quad
\|N_i\|\le1,\quad
\eta_i\le e^{-770\,16^i},
\tag{1.2}
$$
其中 E_i=e_(10)^(i) 为第 i 位物理平方零矩阵。T 对同一个原反射共轭 C 对称；记 B(f,g)=<f,Cg>。

式 (1.1) 也准确等于自然核图稿的
$$
T=2a_kN_kS+S^2+Z,
$$
$$
S=\sum_{i>k}a_iN_i,\qquad
Z=\sum_{i>k}a_i^2N_i-\sum_{i>k}a_i^2N_i^2.
\tag{1.3}
$$
因此没有换原核或忽略 Z 中的 carry。

**定理。** (1.1) 的 T 单射且值域稠密。因而本指定原核及由它提取的 first-flip 闭像缺陷均为零。若保留有限个不参与的前头或作有限放大，同样成立。

证明的输入是 [R215](R215-slow-semigroup-resolvent-and-normal-annihilator-tail.md) §§2–4 已付的统一实际半群界；对下述有限头/纯尾混合模型，同一界由逐项幂估计完全保留（也见 [R217](R217-slow-symbol-entire-order-and-directional-resolvent-growth.md) §2）。这不是将纯核结论直接当作实际核结论。

## 2. 保真低头、纯高尾以及实际误差

对整数 L>k，把低头截断定义为 N_i^[L]：第 L 位切断最后 carry，i<L。高尾则取 E_i。统一记
$$
\widehat N_i=\begin{cases}N_i^{[L]},&i<L,\\E_i,&i\ge L.\end{cases}
$$
整族仍彼此交换；低头只作用于前 L 位，高尾只作用于对应高位。原链展开给
$$
\|N_i-\widehat N_i\|\le\eta_{L-1}\quad\text{对所有 }i.
\tag{2.1}
$$
对 i<L，这是原乘积 carry 误差；对 i≥L，使用 ||N_i-E_i||≤eta_i≤eta_(L-1)。

以 hat N_i 代入 (1.1)，得到 hat X、hat B_0、hat Y、hat T。由 Σa_i<2、Σa_i²<2，
$$
\|X\|,\|\widehat X\|\le2,\qquad
\|T\|,\|\widehat T\|\le8,
$$
$$
\|X-\widehat X\|\le2\eta_{L-1},\quad
\|B_0-\widehat B_0\|\le4\eta_{L-1},\quad
\|Y-\widehat Y\|\le2\eta_{L-1},
$$
所以
$$
\boxed{\|T-\widehat T\|\le14\eta_{L-1}\le16\eta_{L-1}.}
\tag{2.2}
$$
特别作为 B(H) 上的有界导子，δ=ad_T、hat δ=ad_hatT 满足
$$
\|\delta\|,\|\widehat\delta\|\le16,
\qquad
\|\delta-\widehat\delta\|\le32\eta_{L-1}.
$$
非交换幂差望远镜给每个整数 m≥1
$$
\boxed{\|\delta^m-\widehat\delta^m\|
\le2m\,16^m\eta_{L-1}.}
\tag{2.3}
$$
这些是全 H 的真实误差。

## 3. 一个局部矩阵的精确混合模型导子阶数

固定任意物理有限头矩阵 D，设它只作用于前 h 位。以后取 L≥h。
把 hat X 分成低头 H 和纯高尾 X_tail。同样分解 hat B_0、hat Y，得
$$
\widehat T=T_{\rm tail}+K_L,
$$
$$
K_L=H^2-B_{\rm head}+Y_{\rm head}+2H X_{\rm tail}.
\tag{3.1}
$$
T_tail 与 D 及 K_L 交换。准确地，令 A_L=N_0^[L]。有限 carry 给 A_L^(2^i)=c_i N_i^[L]，其中 c_i=prod_(s=0)^(i-1) eta_s^(2^(i-1-s))>0；并且 A_L^(2^L)=0。因此低头各 N_i^[L] 都是 A_L 的无常数项多项式。K_L 的每项都含正次 A_L，系数在尾代数中；所有系数交换，准确有
$$
K_L^{2^L}=0.
\tag{3.2}
$$
置 r=2^L。展开 ad_(K_L)^(2r)(D)，每项两侧幂次之和为 2r，至少一侧≥r，故
$$
\boxed{\widehat\delta^{2r}(D)=0.}
\tag{3.3}
$$
这里是这个混合模型的精确等式。下一各节用 (2.3) 支付把它放回原实际 T 的全部费用。

## 4. 删除整个所选集合后的共同背景逆

取
$$
r=2^L,\qquad q=r^2/4,
\qquad I_L=\{L,L+1,\ldots,L+q-1\},
\qquad M_L=L+q.
\tag{4.1}
$$
以后 L≥4，故 q≥r 且所有选中位高于 k。对任意 F⊂I_L、|F|=r，定义删除背景
$$
X_F=\sum_{\substack{i\ge k\\i\notin F}}a_i\widehat N_i.
$$
系数仍满足 |a_i|≤(i+1)^(-2)，故 R215 的实际逐因子证明给整个复平面的统一界
$$
\boxed{\|e^{zX_F}\|\le e^{16\sqrt{|z|}}.}
\tag{4.2}
$$
有限头保留原幂估计，高尾 E_i 的正二次幂为零，所以没有引入更大的常数。删除 F 后仍为真实范数收敛的交换和。

选中 E_j 的一次系数为
$$
V_{j,F}=a_j^2I+2a_jX_F=2a_j(X_F+c_jI),
\qquad c_j=a_j/2>0.
\tag{4.3}
$$
每个 X_F+c_jI 的实际有界逆由范数 Laplace 积分给出。更重要的是，把全部 2r 个逆一次相乘：
$$
\prod_{j\in F}(X_F+c_jI)^{-2}
=\int_{[0,\infty)^r}
\left(\prod_{j\in F}t_j\right)
 e^{-\sum c_jt_j}e^{-(\sum t_j)X_F}\,dt.
\tag{4.4}
$$
每个单因子来自 (X_F+cI)^(-2)=∫_0^∞ t e^(-ct)e^(-tX_F)dt；统一可积主控保证 Fubini 和乘法合法。它给真实左右逆乘积，不是形式模理想运算。

令 c=min c_j≥1/(2M_L²)。按 T_0=Σt_j 的单纯形体积积分，(4.2) 给
$$
\left\|\prod_{j\in F}(X_F+c_jI)^{-2}\right\|
\le\frac1{(2r-1)!}
\int_0^\infty t^{2r-1}e^{-ct+16\sqrt t}\,dt.
$$
由于 16sqrt(t)≤ct/2+128/c，右侧至多
$$
(2/c)^{2r}e^{128/c}
\le(4M_L^2)^{2r}e^{256M_L^2}.
\tag{4.5}
$$
再乘 ∏(2a_j)^(-2)≤M_L^(4r)/4^r，得到
$$
\boxed{
\left\|\prod_{j\in F}V_{j,F}^{-2}\right\|
\le4^rM_L^{8r}e^{256M_L^2}.
}
\tag{4.6}
$$
关键是主要指数 256M_L² 没有再乘 r。每个 V_(j,F) 使用同一个删池背景 X_F；用逐因子范数相乘会丢失这个费用。

## 5. 全域高导子的精确最高项及一致弱单位

记 E_F=∏_(j∈F)E_j。对混合模型写
$$
\widehat T=T_F+W_F,
$$
其中 T_F 完全不作用于所选位 F，W_F 是选中 E_j 的无常数项多重仿射多项式，其一次系数正是 (4.3)。于是
$$
W_F^{r+1}=0,\qquad
W_F^r=r!E_F\prod_{j\in F}V_{j,F}.
$$
T_F 与 E_F^*、W_F 交换。展开 ad_hatT^(2r)(E_F^*)，只有中央项留下；由 E_F E_F^* E_F=E_F，准确得到
$$
\boxed{
\widehat\delta^{2r}(E_F^*)
=(-1)^r(2r)!E_F\prod_{j\in F}V_{j,F}^2.
}
\tag{5.1}
$$
全部 V_(j,F) 及其真逆与 hat T 交换。因此定义
$$
U_L=\frac{(-1)^r2^r}{(2r)!\binom qr}
\sum_{\substack{F\subset I_L\\|F|=r}}
E_F^*\prod_{j\in F}V_{j,F}^{-2}
$$
后，有
$$
\boxed{
\widehat\delta^{2r}(U_L)=
\frac{2^r}{\binom qr}\sum_{|F|=r}E_F=:R_L,
\qquad
\|U_L\|\le\frac{8^rM_L^{8r}}{(2r)!}e^{256M_L^2}.
}
\tag{5.2}
$$
不要求 U_L 属于右交换子；它是原 Haar 空间上真实有界的导子输入。

为支付 R_L 的全域范数，令 J_I=Σ_(j∈I_L) E_j。它把 q 位中第 d 层送到第 d+1 层，Cauchy–Schwarz 给该层范数≤sqrt((d+1)(q-d))，故
$$
\|J_I\|\le(q+1)/2.
$$
由 J_I^r=r!Σ E_F，
$$
\|R_L\|\le\frac{(q+1)^r}{q(q-1)\cdots(q-r+1)}.
$$
q=r²/4、r≥16 时 q≥2r，所以
$$
\log\|R_L\|
\le\frac rq+\frac{r(r-1)}{2(q-r+1)}\le5.
\tag{5.3}
$$
每个位的原 Haar 参考向量为 (e_0+e_1)/sqrt2，故 <E_F Ω,Ω>=2^(-r)。任意两个固定有限柱向量 f,g，当 L 足够高时，准确有 <R_Lf,g>=<f,g>。由 (5.3) 及有限柱稠密性，
$$
\boxed{R_L\longrightarrow I\quad\text{WOT},\qquad\sup_L\|R_L\|\le e^5.}
\tag{5.4}
$$
这里没有把增长阶数 r 的平均误称强极限；原核配对只需这个一致有界弱极限。

## 6. 全部 carry 误差真正压过合并逆

由 (2.3)、(5.2)，置
$$
\varepsilon_L=4r\,16^{2r}\eta_{L-1}
\frac{8^rM_L^{8r}}{(2r)!}e^{256M_L^2}.
$$
则
$$
\|\delta^{2r}(U_L)-R_L\|\le\varepsilon_L,
$$
$$
\|\delta^{2r}(D)\|\,\|U_L\|
\le\varepsilon_L\|D\|\quad(L\ge h).
\tag{6.1}
$$
第二式使用精确 (3.3) 后再用同一个真实幂差估计，没有删除任何局部导子余项。

L≥4 时 r=2^L、M_L=L+r²/4≤r²/3，且
$$
770\,16^{L-1}=(770/16)r^4.
$$
舍弃有利的 factorial 分母，得到
$$
\log\varepsilon_L
\le-\left(\frac{770}{16}-\frac{256}{9}\right)r^4
+r\log8+16r\log r+\log(4r)+2r\log16.
\tag{6.2}
$$
对 r≥16，最后四项至多 r^4/8：可用 log r≤r/4、log8<3、log16<3、log(4r)≤r，从而其和≤4r²+10r≤r^4/8。故
$$
\boxed{\varepsilon_L\le e^{-19r^4}\longrightarrow0.}
\tag{6.3}
$$
因为 770/16−256/9−1/8=19.555...>19。常数仅使用原实际 carry 下界及 R215 的半群常数16。

## 7. 同一个原核中的局部完整配对排除

令 f,g∈ker T。T 全域有界且对原 B 对称，所以对任意有界 D,U 和整数 m≥0，逐次使用完整导子乘法恒等式可得
$$
\boxed{B(D\delta^m(U)f,g)=(-1)^mB(\delta^m(D)Uf,g).}
\tag{7.1}
$$
这是原 T、原核与原配对的等式：先用 B(δ(V)f,g)=0，再把导子逐次从 U 移到 D。没有把 f,g 当成混合模型的核向量。

对任意固定有限头 D，取 m=2r、U=U_L。由 (6.1)，
$$
|B(DR_Lf,g)|
\le2\varepsilon_L\|D\|\,\|f\|\,\|g\|\longrightarrow0.
$$
再用 (5.4)，得到
$$
\boxed{B(Df,g)=0\quad\text{对所有有限头矩阵 }D.}
\tag{7.2}
$$

最后排核不需要 C 保持 ker T。反设非零 f∈ker T，取 g=f。令 P_h 为前 h 位柱空间投影，P_h→I 强，且它与原反射共轭 C 交换。取范数1的前 h 位矩阵 D_h，使 D_hP_hf 与 P_hCf 同方向且有相同范数。它与 P_h 交换，于是
$$
B(D_hf,f)=\|P_hf\|^2
+\langle D_h(I-P_h)f,(I-P_h)Cf\rangle.
$$
尾项模≤||(I-P_h)f||²→0，第一项趋||f||²>0，与 (7.2) 矛盾。故 ker T=0。

T*=CTC 随即给 ker T*=0，因此 T 值域稠密。定理证明完毕。

## 8. 准确范围及没有解决的正常态问题

本稿关闭的是 (1.1) 这个真实二次式的全核，故之前从这个原核进入的指定 first-flip 正常见证条件现在没有非零实例。它不依靠先证明特定首位 gauge 配对必非零，也不把一个新的正密度替换旧 rho。

以下结论没有由本稿证明：任意正常 rho 满足 phi_rho(S_N R)=0 的不存在性；S_N 在任意未知不变限制或有限放大子商上稠密；不同辅助尺度、不同尾系数或全部普通多项式的排核；普通 Hilbert ISP 完成。

证明中的纯尾仅用于构造一个有精确代数的辅助混合模型，每个回到实际 T 的步骤都带 (6.1)–(6.3) 的全域预算。特别不会把纯核等向性或未付的局部强密度移到原模型。

## 与负边界线性符号的区别

本文T是原Haar空间上的指定二次式。[R200 §1](R200-boundary-right-shift-domains-and-forward-division-saturation.md)的同名T_N/T_Y是在负边界ℓ²(N0)上构造的线性慢和，核至少含e0，N=M仍开。本文的排核不适用于该不同表示/不同算子；两类路线必须区分。
