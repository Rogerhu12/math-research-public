# R223：任意真解析头下的慢 Bell 边界核及有控有限头延拓

日期：2026-11-13（Asia/Taipei）。作者：boundary。状态：已证明。

本稿扩展 R185/R188 的真实有限块纠错。新的允许项是任意真解析零常数芽，且慢系数允许复数并只要求双侧多项式尾界。芽的收敛半径可以小于算子范数；跨空白间隔的估计通过真实小圆预解式给出，不用失效的粗幂级数界。

## 1. 模型和定理

在实际负整数边界 $\mathcal H_-=\ell^2(\mathbb N_0)$ 上，沿用
$$
Be_0=0,\qquad Be_n=\alpha_{v_2(n)}e_{n-1},\qquad
\mathsf N_j=B^{2^j}/d_j,
$$
$$
\eta_j=\alpha_{j+1}/\alpha_j\le e^{-770\,16^j},\qquad
\mathsf N_j=\mathsf E_j+\eta_j\mathsf E_j^*\mathsf N_{j+1}.
$$
其中 $\|\mathsf N_j\|=1$、$\mathsf N_j^2=\eta_j\mathsf N_{j+1}$、
$\|(I+\mathsf N_j)^{-1}\|\le3$，$B$ 拟幂零。

定义 Bell 位符号
$$
\mathsf Z_j=\mathsf N_j(I+\mathsf N_j)^{-2}.
\tag{1.1}
$$
设复系数 $b_j$ 满足：存在 $p>1$、$0<c\le C<\infty$、$j_0$，使
$$
c(j+1)^{-p}\le|b_j|\le C(j+1)^{-p}\quad(j\ge j_0).
\tag{1.2}
$$
有限个早期系数任意，记 $M_b=\sum_j|b_j|<\infty$。

令 $r$ 为原点附近的任意复解析芽，且 $r(0)=0$。由于 $B$ 拟幂零，$r(B)$ 由任意足够小圆上的全纯演算良定义。置
$$
\boxed{S=\sum_{j\ge0}b_j\mathsf Z_j-r(B).}
\tag{1.3}
$$
级数按算子范数绝对收敛。

**定理 1.1。** $S$ 非零且有有限的形式首阶 $q\ge1$。存在由明确有限维右逆逐步构造的 $g\in\ker S$，其整数支持无限；特别
$$
\ker S\text{ 为真无限维闭 }B\text{ 不变子空间}.
\tag{1.4}
$$
有限头上的核只是标准 $q$ 维根旗；构造的 $g$ 不落在该旗。

规范危险平方的
$$
a_j=(-1)^j(j+1)^{-\sigma},\quad\tfrac12<\sigma\le1,
\qquad b_j=4a_j^2=4(j+1)^{-2\sigma}
$$
满足 (1.2)。又
$$
1-\left(\frac{1-N_j}{1+N_j}\right)^2
=4N_j(1+N_j)^{-2},
$$
所以其尾 Bell 和减任意真解析零常数头恰属本定理。删去有限多个低位、或从固定低位之后开始求和，不改变证明。

## 2. Bell 位与纯消灭的全部真实比较

由 $\|N_j\|\le1$ 和逆界，$\|Z_j\|\le9$。又
$$
Z_j-N_j
=-\bigl(2N_j^2+N_j^3\bigr)(I+N_j)^{-2},
$$
故
$$
\boxed{\|Z_j-E_j\|\le28\eta_j.}
\tag{2.1}
$$
这里及以下同一字体的实际符号在边界表示中解释。

设 $F=N_i^{[m]}$ 是作用低 $m$ 位的有限链，$N=N_i$。令 $R_N=(I+N)^{-1}$、$R_F=(I+F)^{-1}$。有
$$
Z(N)=R_N-R_N^2,
\qquad R_N-R_F=-R_N(N-F)R_F.
$$
将平方差按保持右端有限头因子的顺序写开，得到
$$
Z(N)-Z(F)
=-(I-R_N)R_N(N-F)R_F
+R_N(N-F)R_F^2.
\tag{2.2}
$$

若输入空间由低头 $[0,m)$、空白间隔 $[m,L)$、新块 $[L,2L)$ 组成，记为 $\mathcal U_{m,L}$，则 $R_F,R_F^2$ 保持该空间。真实链给
$$
\|(N_i-N_i^{[m]})|_{\mathcal U_{m,L}}\|
\le\alpha_L/\alpha_i\quad(i<m).
$$
故 (2.2) 的两个项分别至多 $36\alpha_L/\alpha_i$、$27\alpha_L/\alpha_i$，即
$$
\|(Z_i-Z_i^{[m]})|_{\mathcal U_{m,L}}\|
\le63\alpha_L/\alpha_i.
\tag{2.3}
$$
对于 $m\le i<L$，将逆放在左边，得
$$
\|Z_i|_{\mathcal U_{m,L}}\|\le9\alpha_L/\alpha_i.
\tag{2.4}
$$
对 $L\le i<2L$ 使用 (2.1)；对 $i\ge2L$，实际位符号严格杀掉整个 $\mathcal F_{2L}$。

因此 Bell 和的实际模型误差至多
$$
91M_b\eta_{L-1}.
\tag{2.5}
$$
这对复系数一样成立，因为只取其绝对值。

## 3. 任意半径解析芽的真实空 gap 估计

取 $\rho>0$，使 $r$ 在闭圆盘 $|z|\le\rho$ 的邻域解析。允许 $\rho<\|B\|$。
由 $B$ 拟幂零，
$$
K_\rho:=\sum_{n\ge0}\|B^n\|\rho^{-n-1}<\infty.
\tag{3.1}
$$
有限头 $B_m=B|_{\mathcal F_m}$ 满足 $\|B_m^n\|\le\|B^n\|$，所以对每个 $m$、每个 $|\zeta|=\rho$，
$$
\|(\zeta-B)^{-1}\|\le K_\rho,
\qquad \|(\zeta-B_m\otimes I)^{-1}\|\le K_\rho.
\tag{3.2}
$$
第二个预解式只作用低头，因而保持 $\mathcal U_{m,L}$。

真实后移满足
$$
\|(B-B_m\otimes I)|_{\mathcal U_{m,L}}\|\le\alpha_L.
\tag{3.3}
$$
低头有孔时两者相等；低头真空时，真正借位只能从至少第 $L$ 位的孔开始。
使用准确预解式恒等式，且将有限头预解式放在右端，得到
$$
\|[(\zeta-B)^{-1}-(\zeta-B_m\otimes I)^{-1}]|_{\mathcal U_{m,L}}\|
\le K_\rho^2\alpha_L.
$$
Cauchy 全纯演算遂给
$$
\boxed{
\|[r(B)-r(B_m)\otimes I]|_{\mathcal U_{m,L}}\|
\le C_r\alpha_L,
\quad C_r=\rho\sup_{|\zeta|=\rho}|r(\zeta)|K_\rho^2.
}
\tag{3.4}
$$
$C_r$ 独立于 $m,L$。这里从未用 $\sum n|r_n|\|B\|^{n-1}$，该粗级数在小芽半径下可以发散。

将 (2.5) 和 (3.4) 合并，设
$$
C_0=91M_b+C_r.
$$
若 $S_m=S|_{\mathcal F_m}$，$D_L=\sum_{j=L}^{2L-1}b_jE_j$，则
$$
\boxed{
\|[S-(S_m\otimes I+I\otimes D_L)]|_{\mathcal U_{m,L}}\|
\le C_0\eta_{L-1}.
}
\tag{3.5}
$$
还使用了 $\alpha_L\le\eta_{L-1}$。

## 4. 多项式慢列的有限纯块右逆

置 $d=2^m$。固定一个整数 $K$，满足
$$
K\ge\max\{4,2^{2p+2}C^2/c^2\},
$$
并令 $L=Kd$。取 $m$ 足够大，使新块索引均超过 $j_0$。

令 $D_L=\sum_{j=L}^{2L-1}b_jE_j$，$C_L=D_L^*$，
$\sigma_L^2=\sum_{j=L}^{2L-1}|b_j|^2$。则
$$
\sigma_L^2\ge c^2 2^{-2p}L^{1-2p},
\qquad \max_{j\in[L,2L)}|b_j|^2\le C^2L^{-2p}.
$$
在块内 $q$ 孔空间，准确交换子给
$$
\|C_Lv\|^2-\|D_Lv\|^2
=\sigma_L^2\|v\|^2-2\sum_j|b_j|^2\|P_jv\|^2.
$$
对 $0\le q\le d$，$\sum_j\|P_jv\|^2=q\|v\|^2$，故由 $L\ge Kd$，
$$
\|C_Lv\|^2\ge
\frac{c^2}{2^{2p+1}}L^{1-2p}\|v\|^2.
$$
置
$$
\delta_L=c\,2^{-(p+1/2)}L^{1/2-p}.
\tag{4.1}
$$
于是 $D_L:\mathcal K_{q+1}\to\mathcal K_q$ 有明确右逆
$$
R_q=C_q(C_q^*C_q)^{-1},\qquad\|R_q\|\le\delta_L^{-1},
$$
其中 $C_q=C_L|_{\mathcal K_q}$。
由块真空 $h_0$ 递归 $h_k=R_{k-1}h_{k-1}$，有
$$
D_Lh_k=h_{k-1},\qquad
\|h_k\|\le\delta_L^{-k}\quad(0\le k<d).
\tag{4.2}
$$
不同 $k$ 的孔次数不同，因此彼此正交。

## 5. 有限模型抵消及统一迭代预算

由于 $r(0)=0$，有限头 $S_m$ 是 $B_m$ 的无常数多项式，故
$$
S_m^d=0.
$$
记 $M_S=\max(1,\|S\|)$。对 $v\in\mathcal F_m$，定义
$$
V=\sum_{k=0}^{d-1}(-1)^kS_m^kv\otimes h_k.
\tag{5.1}
$$
则
$$
(S_m\otimes I+I\otimes D_L)V=0.
\tag{5.2}
$$
所有正阶修正都在新块有孔，严格保留低于 $2^L$ 的原坐标。

若 $\varepsilon=\|S_mv\|$，逐项估计给
$$
\|V-v\|\le A_m\varepsilon,
\qquad
A_m:=dM_S^{d-1}\max(1,\delta_L^{-1})^d.
\tag{5.3}
$$
因 $L=K2^m$ 且 $p,c,C,K,M_S$ 固定，存在一个固定常数 $C_1$，使对全部充分大 $m$，
$$
\log A_m\le C_1 m2^m.
\tag{5.4}
$$
这已经支付了所有右逆放大；不要求原稿中的数字 8 对新参数仍通用。

设
$$
\varepsilon_m=e^{-40\,4^m}.
$$
增大固定起始尺度 $m_*$，使对所有 $m\ge m_*$，
$$
A_m\varepsilon_m\le e^{-20\,4^m},
\tag{5.5}
$$
以及
$$
3C_0\eta_{L-1}\le e^{-40\,16^L}.
\tag{5.6}
$$
(5.5) 来自 $m2^m=o(4^m)$；(5.6) 来自
$\eta_{L-1}\le e^{-(770/16)16^L}$ 和 $770/16=48.125>40$。
所有固定参数和解析芽常数都吸收到 $m_*$，不随递归步骤变化。

若 $v\in\mathcal F_m$、$\|v\|\le2$、$\|Sv\|\le\varepsilon_m$，则 (5.3)—(5.5) 先给
$$
\|V-v\|\le e^{-20\,4^m},\qquad\|V\|\le3.
$$
再由 (3.5)、(5.2)、(5.6)，令 $m'=2L=2K2^m$，得到
$$
\|SV\|\le C_0\eta_{L-1}\|V\|
\le e^{-40\,4^{m'}}=\varepsilon_{m'}.
\tag{5.7}
$$
每一步都重新得到对应新真实头尺度的同一预算。

## 6. 一个非零的高位初值

对充分大 $j$，取 $k=j+1$，并令
$$
v_0=
\frac{b_ke_{2^j}-b_je_{2^k}}
{\sqrt{|b_j|^2+|b_k|^2}},
\qquad m_0=j+2.
\tag{6.1}
$$
复系数也严格抵消纯真空项；$\|v_0\|=1$，两个高位坐标都非零。

对单孔向量，若 $i<j$，实际链给
$\|N_ie_{2^j}\|=\alpha_j/\alpha_i$，于是
$\|Z_ie_{2^j}\|\le9\alpha_j/\alpha_i$；若 $i=j$，则
$Z_je_{2^j}=e_0$ 精确成立；若 $i>j$，输出为零。

另写 $r(z)=zh(z)$。$h$ 仍为真解析芽，且
$$
\|r(B)e_{2^j}\|
=\|h(B)Be_{2^j}\|
\le\|h(B)\|\alpha_j.
\tag{6.2}
$$
所以存在固定 $C_2<\infty$，使
$$
\|Se_{2^j}-b_je_0\|\le C_2\eta_{j-1}.
$$
(6.1) 的两个标量系数模长都不超过 1，故
$$
\|Sv_0\|\le C_2(\eta_{j-1}+\eta_j)
\le2C_2e^{-770\,16^{j-1}}.
\tag{6.3}
$$
当 $j$ 足够大时，右边小于
$e^{-40\,4^{j+2}}=\varepsilon_{m_0}$，并且 $m_0\ge m_*$。

## 7. 收敛到实际核及保留高位系数

递归 $m_{n+1}=2K2^{m_n}$，使用 (5.1) 将 $v_n$ 变为 $v_{n+1}$。所有有限维右逆按 (4.2) 固定，故序列明确。
由 (5.5)，
$$
\|v_{n+1}-v_n\|\le e^{-20\,4^{m_n}}.
$$
增大初始 $m_0$ 后，修正和小于 $1/4$。因此所有 $\|v_n\|<5/4<2$，归纳预算合法；同时 $\|Sv_n\|\le\varepsilon_{m_n}\to0$。

向量 $v_n$ 强收敛到某个 $g$，$S$ 有界，所以 $Sg=0$。所有后续修正都在新块有孔，严格保留最初 $e_{2^j}$ 和 $e_{2^{j+1}}$ 两个非零坐标。因此 $g\ne0$。

## 8. 非零形式首阶与无限支持

还须排除解析芽恰好消去整个符号，并保证构造超出所有有限核。
对固定 $j$，在 $e_{2^j}$ 到 $e_0$ 的矩阵元上，Bell 位的有限三角展开给
$$
\left\langle\sum_i b_iZ_i e_{2^j},e_0\right\rangle
=b_j-\sum_{i<j}b_i\,2^{j-i}\frac{d_j}{d_i^{2^{j-i}}}.
\tag{8.1}
$$
如前述真实 dyadic 幂递推，
$$
\frac{d_j}{d_i^{2^{j-i}}}\le\eta_{j-1}.
$$
所以 (8.1) 中的低位总误差至多 $2^jM_b\eta_{j-1}$。

若 $r(z)=\sum_{n\ge1}r_nz^n$，Cauchy 系数界给
$|r_n|\le C_\rho\rho^{-n}$。在所考察矩阵元中，解析项恰为 $r_{2^j}d_j$。而
$$
d_j=W_{2^j}\le\alpha_j\le\eta_{j-1}
$$
（其余权均不超过 1）。故
$$
\left|\langle Se_{2^j},e_0\rangle-b_j\right|
\le\left(2^jM_b+C_\rho\rho^{-2^j}\right)\eta_{j-1}
=o((j+1)^{-p}).
\tag{8.2}
$$
由 (1.2)，这些矩阵元在全部充分大的 $j$ 非零。

因此 $S$ 的形式系数不全为零；常数项为零，其最早非零阶记为 $q\ge1$。在每个足够大有限头上，
$$
S_m=B_m^qU_m(B_m),\qquad U_m(0)\ne0,
$$
其中 $U_m(B_m)$ 为可逆有限三角多项式，故
$$
\ker(S|_{\mathcal F_m})
=\operatorname{span}\{e_0,\ldots,e_{q-1}\}.
\tag{8.3}
$$

在第 6 节选取初始 $j$ 时，再要求 $2^j>q$。所构造的 $g$ 保留该位置的非零系数，因此不可能有有限支持，否则会违反 (8.3)。
由 $SB=BS$，$\ker S$ 是闭 $B$ 不变空间；它包含无限支持向量，因而不能有限维。$S\ne0$ 又使该核为真子空间。定理 1.1 得证。

## 8A. 任意有限头的线性延拓

上述实际核还满足完整有限头满射性，并有足以接入 R195 的增长预算。

**命题 8A.1。** 存在只依固定 $b,r$ 的常数 $C_3,C_4$，使每个 $m\ge1$ 都存在有界线性映射
$$
J_m:\mathcal F_m\longrightarrow\ker S,
\qquad P_mJ_m=I_{\mathcal F_m},
\qquad \|J_m\|\le C_3\exp(C_4m2^m).
\tag{8A.1}
$$
对全部充分大的 $m$，可具体取 $\|J_m\|\le2\Gamma_m$，其中
$$
\Gamma_m=1+\|S\|A_m,
\tag{8A.2}
$$
$A_m$ 如 (5.3)。

证明：先令 $m\ge m_*$，对任意 $v\in\mathcal F_m$ 直接用 (5.1) 构造 $V$，不要求 $Sv$ 小。式 (5.3) 给
$$
P_mV=v,
\qquad \|V\|\le\Gamma_m\|v\|.
$$
由实际空 gap 误差 (3.5)，
$$
\|SV\|\le C_0\eta_{L-1}\Gamma_m\|v\|,
\qquad L=K2^m.
$$
当 $v\ne0$，把 $V$ 除以 $\Gamma_m\|v\|$；所得向量在新头 $m'=2L$ 内，范数不超过 1，由 (5.6) 有残量不超过 $\varepsilon_{m'}$。因此从第 5 节的后继尺度开始，原收敛预算完全适用。乘回后得到 $J_mv\in\ker S$，范数不超过 $2\Gamma_m\|v\|$。每个后续修正至少在第 $L'>m'$ 位有孔，故不会改动 $P_mV=v$。

线性性也必须保留：初始的有限模型算子以及每一步用固定 $R_q$ 定义的修正算子均为线性。上述除以范数仅用于证明统一估计，没有进入构造公式。对 $\|v\|\le1$，后续增量范数由 $\Gamma_m\sum_n e^{-20\,4^{m_n}}$ 一致控制，故线性构造在算子范数下收敛，极限 $J_m$ 仍线性。

由 (5.4)，$\log\Gamma_m\le C_4m2^m$ 在充分大 $m$ 成立。有限多个较小 $m$ 可先嵌入某个固定合格头 $\mathcal F_{m_*}$，再用 $J_{m_*}$，最后增大固定 $C_3$。这给出 (8A.1)。

因此 $\ker S$ 对任意有限坐标集合的限制都是满射。这个结论来自范数有控的真实纠错，不能仅由第 7 节两个保留坐标的单一初值推得。它本身仍不推出任意核向量的有限头延拓近似，亦不推出 $\overline{B\ker S}=\ker S$。

## 9. 解析因子在芽曲线上的必要消失

回到同一个 UHF 代数的忠实 Haar 表示，令
$$
Z=\sum_j b_jN_j(1+N_j)^{-2},\qquad S=Z-r(A),
$$
其中 $b_j,r$ 满足上文条件。记负整数边界的连续 $*$ 表示为 $\pi_-$。
设 $F(z,u)$ 是 $(0,0)$ 附近的真双变量解析芽，令
$R=F(A,Z)$。若存在有界 $C\in\{A\}'$，使
$$
R=SC,
\tag{9.1}
$$
则
$$
\boxed{F(z,r(z))\equiv0\quad\text{作为解析芽}.}
\tag{9.2}
$$
此处不要求 $C$ 属于 UHF。

证明：$C$ 与 $S$ 交换，所以 $R=CS$，从而在 Haar Hilbert 空间上有
$$
R^*R\le\|C\|^2S^*S.
$$
$R,S$ 属于 UHF；忠实 $*$ 表示反映正性，故此正序不等式传到边界：
$$
\pi_-(R)^*\pi_-(R)\le\|C\|^2\pi_-(S)^*\pi_-(S).
$$
因此 $\pi_-(R)$ 杀掉定理 1.1 的无限支持 $g\in\ker\pi_-(S)$。

解析差商
$$
G(z,u)=\frac{F(z,u)-F(z,r(z))}{u-r(z)}
$$
在原点附近解析。对两个交换的拟幂零元作全纯演算，有
$$
R-F(A,r(A))=SG(A,Z).
$$
边界作用到 $g$ 后，得到 $F(B,r(B))g=0$。

若单变量芽 $h(z)=F(z,r(z))$ 非零，写 $h(z)=z^\nu u(z)$、$u(0)\ne0$。$u(B)$ 有界可逆且保持有限根旗，所以
$$
\ker h(B)=\ker B^\nu
=\operatorname{span}\{e_0,\ldots,e_{\nu-1}\}.
$$
这与 $g$ 无限支持矛盾，故 (9.2) 成立。

范数闭主理想中的 $R$ 也有相同结论：若 $R\in\overline{S\mathcal A}$，连续边界表示直接给 $\pi_-(R)g=0$，后半段证明不变。这里的有界交换因子版本更强，不能通过把 $C$ 擅自送入边界表示来证明。

## 10. 范围

已覆盖规范 $\sigma\in(1/2,1]$ 的 Bell 慢和、任意真解析零常数芽及任意有限低位删改。没有声明覆盖完全任意、可能极稀疏或超快趋零的 $\ell^2$ 系数行；那些行可能不满足 (1.2)，有限块右逆预算须另行检验。

定理构造的是实际负整数边界核。它不构造原 Haar 的不变子空间，不判断此新核或原两核的 $\overline{B\ker S}=\ker S$，也不把解析公共因子排除升级为全部有界/可闭共同像的排除。
