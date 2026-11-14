# R236 附录：二次共振后任意 ℓ² 主行的实际预解准则与长平台族

日期：2026-11-13。作者：Astra-ISP-0c017065 / central_next / central_review。
状态：主会话与 central_review 独立核验完整自然域、联合逆和实际 Laplace 预算。普通 Hilbert ISP 未完成。

[R270C](R270-appendix-closed-first-fast-polynomials-and-all-order-resonant-cyclicity.md) 已关闭准确二次消去；[R270E](R270-appendix-fast-auxiliary-modes-and-resonant-polynomial-modules.md) 已允许任意慢主行加独立超三次快辅助。本附录处理第一个有限非零偏离，新增条件涉及真实辅助算子的预解式；长平台例子的辅助不在该快类。

完整证明依次见[弱 ℓ¹ 稿](../notes/2026-11-13-next-nonzero-order-after-quadratic-resonance-central-next.md)、[有界行预算稿](../notes/2026-11-13-next-order-resonance-bounded-resolvent-criterion-central-next.md)、[任意 ℓ² 与实偏离阶稿](../notes/2026-11-13-general-ell2-near-resonance-resolvent-criterion-central-review.md)、[尾间隙和长平台稿](../notes/2026-11-13-tail-gap-resolvent-budget-and-nonweak-l1-plateau-near-resonance-central-review.md)。后两稿扩展前两稿的假设，不把真实排序变成物理重排。

## 1. 统一实际预解准则

令
$$
u=a_*+\sum_j a_j\chi_j,\qquad
w=b_*+\sum_j b_j\chi_j,\qquad a,b\in\ell^2(\mathbb C),
$$
主行有无限非零支撑，其非零幅度非增重排为 $\rho_n$。
固定任意实数 $\kappa>2$，要求
$$
|c_j|\le C_0|a_j|^\kappa\quad(\text{全部 }j),\qquad
|c_j|\ge c_0|a_j|^\kappa
\quad(\text{充分高物理位且 }a_j\ne0),\quad c_0>0.
\tag{1.1}
$$
只比较绝对值，不涉及复数幂分支。相位及物理排列任意；$a_j=0$ 时全局上界要求 $c_j=0$。有限低位无需下界，仍须满足上界。

记
$$
t_j=e^{-2b_j},\quad R_j=V(t_jN_j),\quad
Y=\sum_jc_j(R_j-I),\quad
B=\sum_ja_j^2(R_j-I)^2\in\mathcal G .
\tag{1.2}
$$
$c\in\ell^1$，两和均为真实范数收敛算子。$X_b$ 是 R176 的自然闭 first 算子；$a\notin\ell^1$ 时不把它改成有界级数。

**定理 A。** 固定 $0<\varepsilon<c_0^2/64$。若沿无穷整数子序列 $N$，
$$
L_N:=1+\log^+(\rho_N^{-1})=O(N^{3/2}),
\tag{1.3}
$$
$$
\boxed{
\sup_{|z|=\varepsilon\rho_N^{\,2\kappa-2}}
\log^+\|z(z-Y)^{-1}\|=O(N^2),
}
\tag{1.4}
$$
则
$$
\boxed{
\left[u^2+\sum_j(2a_j^2+c_j)(\chi_j-1)\right]e^w
\text{ 非零且对原实际 }A\text{ 循环}.
}
\tag{1.5}
$$
(1.4) 是实际双侧预解式的范数条件。该定理不要求主行属于 $\ell^1$、弱 $\ell^1$ 或 R268 的熵类。

## 2. 共同逆只在同一个自然核内使用

R176 和真实混合 Bell 公式给
$$
T=X_b^2+Y-B,\qquad
Te^w=\left[u^2+\sum_j(2a_j^2+c_j)(\chi_j-1)\right]e^w,
$$
$$
\operatorname{Dom}T=\operatorname{Dom}X_b^2,\qquad
T=\mathcal C T^*\mathcal C .
\tag{2.1}
$$
若 $M=\ker T$，则 $M\subset\bigcap_n\operatorname{Dom}X_b^n$，
$X_M=X_b|_M$ 全域有界，且
$$
X_M^2=(B-Y)|_M.
\tag{2.2}
$$
这里没有假设反射 $\mathcal C$ 保持 $M$。

对选中位 $|a_j|\ge\delta$，令
$$
\tau_j=\frac{c_j}{2a_j},\qquad L_j=8a_jX_b+4c_jI.
$$
(1.1) 给 $|\tau_j|^2\ge(c_0^2/4)\delta^{2\kappa-2}$。在共同双圆周
$|z_B|=|z_Y|=\varepsilon\delta^{2\kappa-2}$ 及稍大邻域上，
$z_B-z_Y-\tau_j^2$ 离零。
对 $r$ 元集合 $F$ 一次求值
$$
G_F(B,Y),\qquad
G_F(z_B,z_Y)=\prod_{j\in F}(z_B-z_Y-\tau_j^2)^{-1},
$$
然后定义
$$
\mathfrak R_F=
\left(\prod_F(8a_j)^{-1}\right)
\left(\prod_F(X_M-\tau_jI)\right)G_F(B,Y)|_M .
\tag{2.3}
$$
真实关系 (2.2) 给
$$
\boxed{\left(\prod_FL_j\right)\mathfrak R_F=I_M.}
\tag{2.4}
$$
没有全空间 $L_j^{-1}$ 声称。联合 Cauchy 公式只对完整乘积求值一次，故高额预解成本不再乘 $r$。由 (1.3)–(1.4) 及 $B$ 的快预算，
$$
\log^+\|\mathfrak R_F\|
\le K_0N^2+(2\kappa-1)rL_N+C_Mr+C.
\tag{2.5}
$$

## 3. 任意 ℓ² 行的完整域和弱平均

从前 $N$ 个幅度中去掉最前 $N/4$ 个排序秩以及最低 $N/4$ 个物理位，保留
$Q_N\sim N/2$ 位组成 $I_N$。所选幅度均在
$[\rho_N,2\|a\|_2/\sqrt N]$ 内，最小物理位趋无穷。
固定稍后取小的 $\theta>0$，令 $r=\lceil\sqrt{N/\theta}\rceil$。
对全部 $r$ 元子集 $F$，
$$
\sum_F|a_j|=O_\theta(1),\qquad
\sum_F|a_j|^2=O_\theta(N^{-1/2}),\qquad
\sum_F|c_j|\to0.
\tag{3.1}
$$
只需第一个和一致有界；不误用 $\sum_F|a_j|\to0$。

令 $J_F=\prod_FM_{\chi_j}$。R260 的最高位壳与完整导子代数把真实反射和符号反射之差支付为
$s!Ce^{-385\,16^{m_N-1}}$；处理非可和 first 时用 $\ell^2$ 壳预算，所有界不含 $\max F$。
准确身份
$$
(V(-z)-I)^2-(V(z)-I)^2=\frac{16z^3}{(1-z^2)^2}
$$
给
$$
\widehat B-B
=\sum_{j\in F}16a_j^2(t_jN_j)^3(I-t_j^2N_j^2)^{-2}.
\tag{3.2}
$$
所以快项不产生 Boolean 一次项；真实 $N_j^3=\eta_jN_jN_{j+1}$ 支付余项。慢差的一次系数为 $t_jL_j$。

对 $f_F=\mathfrak R_Ff\in M$，完整反射域预算给
$$
\|X_b^kJ_Ff_F\|\le2R_{M,\theta}^k\|f_F\|\qquad(k\le4r).
$$
先在 $M$ 内消去 $\prod L_j$，再施左反射。重复位用
$N_j^2=\eta_jN_{j+1}$ 支付，而不是忽略。
定义
$$
\mathcal V_N=(-1)^r(2/Q_N)^r
\sum_{\substack{F\subset I_N\\|F|=r}}t_F^{-1}J_F\mathfrak R_F .
$$
全部误差趋零，得
$$
T^r\mathcal V_Nf-C_{I_N}^rf\to0,\qquad
C_{I_N}=\frac2{Q_N}\sum_{j\in I_N}E_j.
$$
$\|C_{I_N}^r\|\le(1+1/Q_N)^r$，固定柱矩为
$(Q_N)_r/Q_N^r\to e^{-1/\theta}$，因此
$$
\boxed{T^r\mathcal V_Nf\rightharpoonup e^{-1/\theta}f.}
\tag{3.3}
$$
这是非零弱极限，不是一个高提升带的强单位。

固定局部全矩阵 $D$，只从有限低头提出真实 $A$ 因子。
有限头分解保留余下 first 的全部自然 jets；R109 给两侧幂成本
$$
\|A^{r-s}\|\|A^s\|\le
\exp[-(5/6)r^4+105r^3].
$$
共同输入成本除以 $r^4$ 的上极限不超过
$K_0\theta^2+K_1C_L\theta^{3/2}$。选一个固定小 $\theta$ 即可支付全部固定局部测试；局部常数的 $r$ 次幂是低阶项。
完整自然域上的双线性配对
$$
\mathcal B(DT^r\mathcal V_Nf,g)
=(-1)^r\mathcal B((\operatorname{ad}_T^rD)\mathcal V_Nf,g)
$$
遂使 $\mathcal B(Df,g)=0$ 对所有局部矩阵和 $f,g\in M$ 成立。
局部全矩阵不可约，迫 $M=0$；(2.1) 及 R176 图核心给稠密像和 (1.5) 的循环性。

## 4. 三类直接计算的预解预算

**排序幂行。** 若固定 $\sigma\ge1$，
$$
0<\limsup n^\sigma\rho_n\le\sup n^\sigma\rho_n<\infty,
$$
实际正函数锥主控给
$$
\|Y^n\|\le KD^n/(n!)^{\kappa\sigma-1}.
$$
对所有实数 $s>0$ 的阶乘级数有
$\sum x^n/(n!)^s\le K_se^{C_sx^{1/s}}$，故沿所选下界子序列，
$$
\log^+\|z(z-Y)^{-1}\|
=O\!\left(N^{\,2\sigma(\kappa-1)/(\kappa\sigma-1)}\right).
$$
$\sigma=1$ 时是 $O(N^2)$，$\sigma>1$ 时严格低于 $N^2$。全物理头与 carry 已付。
弱 $\ell^1$ 的下界子序列也使主行实际非 $\ell^1$；$\sigma>1$ 则属于 $\ell^1$。

**排序指数行。** 若某个 $0<\alpha\le1$ 有全局
$\rho_n\le B_ae^{-\beta_-n^\alpha}$，并在无穷子序列有
$\rho_N\ge b_ae^{-\beta_+N^\alpha}$，$0<\beta_-\le\beta_+$，则
$$
\|Y^n\|\le Ke^{-dn^{1+\alpha}},\qquad
\log^+\|z(z-Y)^{-1}\|
\le C(1+\log^+|z|^{-1})^{1+1/\alpha}.
$$
共同半径上的成本为 $O(N^{1+\alpha})\le O(N^2)$。
因此这三类均满足定理 A，且都允许实 $\kappa>2$。

## 5. 尾间隙：真正全复方向的 Laplace 双侧逆

另一个不要求弱 $\ell^1$ 的充分条件是沿无穷 $N$，
$$
L_N=O(N),\qquad
\boxed{\sum_{n>N}\rho_n^\kappa=o(\rho_N^{\,2\kappa-2}).}
\tag{5.1}
$$
置 $L=\max(1,\sup|t_j|)$，
$$
W(N_j)=2LN_j(I-LN_j)^{-1},\qquad
M_c=\sum_j|c_j|W(N_j).
$$
这些是原函数锥中的保序算子，$\sup_j\|W(N_j)\|<\infty$，
$|Y^nf|\le M_c^n|f|$，不把保序误称为 Hilbert 自伴正性。

对任意有限物理集合 $H$，真实平方 carry、随 $s$ 选择的物理低头和有限 $A$ 除法给
$$
\|e^{sM_H}\|
\le K\exp[C(\log(2+s))^{4/3}]
\prod_{j\in H}(1+C_1s|c_j|).
\tag{5.2}
$$
常数不依赖 $H$ 的大小或最大位。准确 carry 为
$\eta_j=d_{j+1}/d_j^2$；证明只用其粗上界
$\eta_j\le e^{-385\,16^j}$。

若 $|H|=N$、$0<r\le1$、$\|M_{H^c}\|\le r/4$，则对每个 $|z|=r$，
$$
Z_z=\int_0^\infty e^{-t}e^{tY/z}\,dt
$$
在真实算子范数中绝对收敛，积分求导准确给
$(I-Y/z)Z_z=Z_z(I-Y/z)=I$。所以
$$
Z_z=z(z-Y)^{-1}.
$$
由 (5.2) 和 $\int_0^\infty e^{-t/2}(1+t)^Ndt\le
2^{N+1}e^{1/2}N!$，
$$
\log^+\|z(z-Y)^{-1}\|
\le C[1+N\log(N+1)+N\ell_r+\ell_r^{4/3}],
\quad \ell_r=1+\log r^{-1}.
\tag{5.3}
$$
取 $H$ 为前 $N$ 个主幅度的实际物理位，
$r=\varepsilon\rho_N^{2\kappa-2}$，(5.1) 保证尾范数条件且 (5.3) 为 $O(N^2)$。
这证明尾间隙足以推出定理 A；不是只在某个半平面使用形式 Laplace 公式。

## 6. 非弱 ℓ¹ 长平台的明确新增族

任取 $1/2<\sigma<1$ 和整数
$$
p>\frac{\sigma(2\kappa-2)}{\kappa\sigma-1}.
$$
令 $N_0=0$、$N_k=2^{p^k}$（$k\ge1$），并定义
$$
\rho_n=N_k^{-\sigma}\qquad(N_{k-1}<n\le N_k).
\tag{6.1}
$$
有
$$
\sum_n\rho_n^2<\infty,\qquad
\sum_n\rho_n=\infty,\qquad
\sup_n n\rho_n=\infty.
$$
而沿 $N_k$，
$$
L_{N_k}=O(\log N_k),\qquad
\frac{\sum_{n>N_k}\rho_n^\kappa}
{\rho_{N_k}^{2\kappa-2}}
\le2N_k^{\,\sigma(2\kappa-2)-p(\kappa\sigma-1)}\to0.
$$
故任意物理排列、相位、$\ell^2$ 指数权及满足 (1.1) 的偏离行都给循环向量 (1.5)。

例如 $\kappa=3,\sigma=3/4,p=3$，尾比至多 $2N_k^{-3/4}$；
可取 $c_j=\gamma a_j^3$，$\gamma\ne0$，或独立相位的
$c_j=\gamma|a_j|^3\omega_j$。
该主行无弱 $\ell^1$ 上界，也无任意固定正指数全局上界。
$c_j=\gamma a_j^3$ 的辅助在平台末端满足
$-\log c_{N_k}^*=O(\log N_k)$，因此不满足 R270E 的超三次排序快条件。

## 7. 已有范围与剩余问题

此外，[R134/R138/R155 的既有空谱范围](../notes/2026-11-13-existing-empty-spectrum-anchor-scope-for-near-resonance-central-review.md)已经覆盖非ℓ¹且可和相位缺陷主行的任意ℓ¹辅助与任意复指数权；同射线例不重计为本次新增。长平台或规则慢幂要展示旧空谱类之外的范围，可取正负交替相位；完整支撑版仍须本稿的实际预算。可和主行若a*+Σa≠0，目标本来是范数代数单位。

若辅助为 $a_j^2h(a_j)$、$h(0)=2$、$h\not\equiv2$ 且 $h$ 为解析芽，
其首个非零 Taylor 项给整数 $\kappa\ge3$；上述各类均适用。
有限零主系数位的辅助例外须先把有限真解析 $Y_{\rm exc}$ 吸到
$B'=B-Y_{\rm exc}$，并保留有限头反射壳；不能直接抹去。

$c=0$ 与超三次排序快辅助已属 R270C/E，不重计。
快辅助的准确 $\mathcal G$ 依据是
[R151 §6.1](R151-quartic-analytic-approximation-gauge-stability.md)、
[R154 引理2.1](R154-supercubic-modes-all-polynomials-exponential-weights.md)
和 R115 的实际占据界；允许任意物理排列，要求非零幅度排序超三次。
单个四次幂界不是 $\mathcal G$ 的定义。

这里尚未证明每个 $\ell^2$ 行满足 (1.3)–(1.4) 或尾间隙；
无间隙慢主行、独立慢辅助、一般有限 chaos、普通 Haar 不变格、
边界无权核心及一般正常湮灭者仍开放。指数带也不笼统写成全部
$\alpha>1$：$\alpha>3$ 的旧快类和已有临界特例必须保留。
