# 二位 Bézout 提升的全阶共振附录：固定多项式、任意可和偏离及全部标量位移

日期：2026-11-13（UTC）。作者：central_review。
状态：以下全阶扩展的实际自然域、导子与重复位预算已逐步证明，供独立核验。
本稿承接二位二次提升，但不把一般快系数多项式的反射差自动视为无一次项。

## 1. 全阶目标与双池条件

取任意复 $a,b\in\ell^2$、$a_*,b_*\in\mathbb C$、$c\in\ell^1$，
$$
u=a_*+\sum_j a_j\chi_j,\qquad
w=b_*+\sum_j b_j\chi_j.
$$
对 $n\ge2$ 定义
$$
v_n=\sum_j a_j^n(\chi_j-1),
$$
并沿用 R270C 的准确共振族
$$
F_k=
k![t^k]\exp\left(
tu+\sum_{n=2}^k\frac{2^{n-1}}n t^n v_n
\right),\qquad F_0=1,\quad F_1=u.
\tag{1.1}
$$
另记
$$
v_c=\sum_jc_j(\chi_j-1).
$$

假设沿无穷整数子序列 $N$，有两个不交物理位池
$I_N,J_N$，各含 $N$ 位，满足
$$
\min(I_N\cup J_N)\ge\mu N,\qquad
\max_{I_N\cup J_N}|a_j|\le C_aN^{-1/2}
\tag{1.2}
$$
对固定 $\mu,C_a>0$ 成立。
定义
$$
\Delta_{jk}=a_kc_j-a_jc_k,\qquad
d_N=\min_{j\in I_N,k\in J_N}|\Delta_{jk}|,
$$
并假设
$$
\boxed{
d_N>0,\qquad
\ell_N=1+\log^+d_N^{-1}=O(N^{3/2}).
}
\tag{1.3}
$$

**定理 1。**
对任意固定非恒定标量多项式
$$
q(z)=\sum_{k=0}^p q_kz^k,\qquad p\ge1,\quad q_p\ne0,
$$
以及任意 $\lambda\in\mathbb C$，
$$
\boxed{
\left[
\sum_{k=0}^p q_kF_k+v_c-\lambda
\right]e^w
\text{ 非零且对原 }A\text{ 循环}.
}
\tag{1.4}
$$

主、辅助相位及物理排列任意；
$c$ 在所选双池以外只须可和。
不存在首支撑顺序要求。
$p$ 固定，但可以任意大。
本结论不把 $F_k$ 改成未经共振修正的普通点态 $u^k$。

## 2. 实际全阶自然算子

置
$$
t_j=e^{-2b_j},\quad R_j=V(t_jN_j),\quad X=X_b,
$$
$$
G_n=(-1)^{n-1}(n-1)!
\sum_j a_j^n(R_j-I)^n\qquad(n\ge2),
$$
$$
Y=\sum_jc_j(R_j-I).
\tag{2.1}
$$
固定 $n$ 时，$G_n$ 的和按范数绝对收敛；
R270C 的真实局部消去还给 $G_n\in\mathcal G$。
以下只用其有界性、明确局部表达和已证明的有限 jets 恒等式。

定义有限系数多项式
$$
P_q(z)
=
\exp\left(
\sum_{n=2}^p\frac{G_n}{n!}\partial_z^n
\right)q(z).
\tag{2.2}
$$
右边为有限和，每个系数是有限个 $G_n$ 的多项式，
最高系数仍为非零标量 $q_p$。
R270C/R176 的真实自然 jets 给
$$
P_q(X)e^w=\left(\sum_{k=0}^p q_kF_k\right)e^w.
$$

取
$$
T_\lambda=P_q(X)+Y-\lambda I,\qquad
\operatorname{Dom}T_\lambda=\operatorname{Dom}X^p.
\tag{2.3}
$$
R176 给该准确自然域上的闭性、完整 $C$ 自伴性，
以及循环向量 $\xi=e^w$ 所生成的真实图核心。
因此只须排除 $\ker T_\lambda$。

反设
$$
M=\ker T_\lambda\ne0.
$$
同一个已证最大图机制给
$$
\boxed{
M\subset\mathcal D_\infty(X),\qquad
X_M=X|_M\in B(M).
}
\tag{2.4}
$$
全部 $\mathcal A$ 系数保持 $M$ 和全部自然幂域。
本稿不要求 $X_M$ 拟幂零；
它可能有多个非零的有限候选谱点。

以下所有有限高次词只在 $\mathcal D_\infty(X)$ 上使用。
无需未经证明地识别整个 $\operatorname{Dom}T_\lambda^r$；
这个共同深域已经足以定义提升、全部中间词和逐次配对。

## 3. 全阶系数的实际反射壳与导子预算

固定有限高位集 $F$，
令 $J_F=\prod_{j\in F}M_{\chi_j}$、$\gamma_F=\operatorname{Ad}J_F$。
只在 $F$ 中把 $R_j$ 改成
$$
\widehat R_j=V(-t_jN_j)
$$
而在其余位保持原值；
由此定义 $\widehat X,\widehat Y,\widehat G_n$ 及 $\widehat P_q$。
带帽的有界系数仍属于 $\mathcal A$，与 $X$ 完整域交换。

下面说明 R260 的原壳估计确实适用于每个 $G_n$，
而不是仅凭“它属于 $\mathcal G$”推断。
在 R260 §3.1 的有限截断中，
将固定多项式 $L_n(R)$ 换成固定多项式 $(R-I)^n$。
全部真实与有限截断 $(I\pm t_jN_j)^{-1}$ 的范数一致有界，
所以有限幂差公式仍使最高位为 $\ell$ 的壳至多为
固定常数乘
$$
|a_j|^n\frac{\alpha_\ell}{\alpha_j}.
$$
非零壳必须越过一个被反射位，
故其最高物理位至少为 $\min F$。
按最高位收集后，用
$$
\left(\sum_j|a_j|^{2n}\right)^{1/2}<\infty
$$
代替一阶的 $\|a\|_2$，
得到局部壳
$$
\gamma_F(G_n)-\widehat G_n
=
\sum_{\ell\ge\min F}B_{n,\ell,F},
\qquad
\|B_{n,\ell,F}\|\le C_n\eta_{\ell-1}.
\tag{3.1}
$$
每个壳只作用于前 $\ell+1$ 位，
常数不依赖 $|F|$ 或最大选中位。

令 $\delta_XD=[X,D]$，采用 R260 的完整域导子代数
$$
\|D\|_{\delta_X}
=
\sum_{s\ge0}\frac{\|\delta_X^sD\|}{s!}.
$$
对最高位为 $\ell$ 的局部壳，
实际闭尾 first 与其交换，
低头范数至多为 $C+C\|a\|_2\sqrt{\ell+1}$。
于是
$$
\|B_{n,\ell,F}\|_{\delta_X}
\le e^{C+C\sqrt{\ell+1}}\|B_{n,\ell,F}\|.
$$
实际 $\eta_{\ell-1}$ 的双指数衰减可求和，
故对固定 $p$，
$$
\boxed{
\|\gamma_FX-\widehat X\|_{\delta_X}
+
\|\gamma_FY-\widehat Y\|_{\delta_X}
+
\sum_{n=2}^p\|\gamma_FG_n-\widehat G_n\|_{\delta_X}
\le\epsilon_m,
\quad
\epsilon_m\le C_pe^{-38516^{m-1}},
}
\tag{3.2}
$$
其中 $m=\min F$。
辅助 $Y$ 使用同一局部多项式差及 $c\in\ell^1\subset\ell^2$。
385 只作为真实 carry 的粗上界。

R260 的导子空间是实际幺 Banach 代数，
乘积完整满足域保持与 Leibniz 公式。
$P_q$ 的系数只有有限多个 $G_n$ 因子，
故有限乘积差分将 (3.2) 传给全部
$\gamma_F(P_q)$ 与 $\widehat P_q$ 的系数，
成本仅为固定 $p$ 的常数。
没有把一个一般有界逆自动当成保域算子；
本稿在这一步根本不需要新算子逆。

每个 $J_F$ 为实际有限局部矩阵。
其与足够高的闭尾 first 完整域交换，
所以双向保持 $\mathcal D_\infty(X)$。
该域事实先独立成立；
不依赖稍后的定量上界是否已经很小。

## 4. 共振系数没有隐藏的 Boolean 一次项

写 $u_j=t_jN_j$。
准确有
$$
\begin{aligned}
\widehat G_n-G_n
&=(-1)^{n-1}(n-1)!
\sum_{j\in F}a_j^n
\left[
(V(-u_j)-I)^n-(V(u_j)-I)^n
\right].
\end{aligned}
\tag{4.1}
$$
因为
$$
V(-u)-I=\frac{2u}{1-u},\qquad
V(u)-I=-\frac{2u}{1+u},
$$
(4.1) 的每一位都含实际 $u_j^n$ 因子。
$n\ge2$ 时至少含 $u_j^2$；
$n=2$ 的首项甚至是三次。
其余有理因子在所选高位上一致有界。
因此
$$
\widehat G_n-G_n
\equiv0\pmod{(N_j^2:j\in F)}.
\tag{4.2}
$$
这是一条带真实重复位余项的有限式，
不是把完整 $G_n$ 当成平方零多项式。

有限乘积差分使 $P_q$ 的每个系数变化同样落入上述重复位理想。
另一方面，
$$
\widehat X-X
\equiv4\sum_{j\in F}a_ju_j,
\qquad
\widehat Y-Y
\equiv4\sum_{j\in F}c_ju_j.
$$
故在记账的交换平方零商中，
$$
\widehat T_\lambda-T_\lambda
\equiv
A_F^{(p)},
$$
$$
\boxed{
A_F^{(p)}
=
\sum_{\ell=1}^p
\frac{P_q^{(\ell)}(X_M)}{\ell!}
\left(4\sum_{j\in F}a_ju_j\right)^\ell
+
4\sum_{j\in F}c_ju_j.
}
\tag{4.3}
$$
这里 $P_q^{(\ell)}$ 是对标量多项式变量的导数，
其 $G_n$ 系数冻结为实际有界系数。

因此一次系数准确为
$$
\boxed{u_jL_j,\qquad
L_j=4a_jP_q'(X_M)+4c_jI_M.}
\tag{4.4}
$$
所有其余项的选位总次数至少为2。
$p=2$ 时 (4.3) 恰还原二次稿的
$8X\sum a_ju_j+16(\sum a_ju_j)^2+4\sum c_ju_j$；
跨位项也包括在 (4.3) 中。

## 5. 同一二位标量输入消去全阶一次项

对跨池 $(j,k)$，沿用全空间有界输入
$$
P_{jk}=\frac{a_ku_k-a_ju_j}{4\Delta_{jk}}\in\mathcal A.
\tag{5.1}
$$
它保持 $M$，分母只为标量。
由 (4.4)，
$$
\boxed{
a_kL_j-a_jL_k=4\Delta_{jk}I_M.
}
\tag{5.2}
$$
未知有界算子 $P_q'(X_M)$ 完全消去，
不须给它求逆。

取 $r=\lceil\sqrt{N/\theta}\rceil$，
对每个 $r$ 元子集 $I\subset I_N$、$J\subset J_N$
固定一个双射配对，令
$$
F=I\cup J,\qquad
P_{I,J}=\prod_{(j,k)}P_{jk}.
$$
输入的选位总次数为 $r$。
在 $(A_F^{(p)})^rP_{I,J}$ 中，
如果任何一个差分因子选了次数至少为2的项，
总次数便超过 $2r=|F|$，所以出现重复位并在平方零商中消失。
只剩全部一次项。
每对的两种选择由 (5.2) 消为标量，
$r$ 个线性因子的排列数恰为 $r!$。
因此
$$
\boxed{
(A_F^{(p)})^rP_{I,J}
\equiv r!t_FN_FI_M
\pmod{(N_j^2:j\in F)}.
}
\tag{5.3}
$$
每个 $(I,J)$ 只用一个固定配对；
没有额外的 $r!$ 配对数。

## 6. 全阶真实 jets 与重复位误差

由双池条件，
$$
\sum_F|a_j|=O_\theta(1),\qquad
\sum_F|a_j|^2=O_\theta(N^{-1/2}),\qquad
\sum_F|c_j|\le\sum_{j\ge\mu N}|c_j|\to0.
\tag{6.1}
$$
这些上界使所有带帽有限增量和 (4.3) 的系数绝对范数和一致受控，
常数可依赖固定 $p,M,\theta$。

使用二次稿的实际绝对系数预算
$$
H_{I,J}
=
\prod_{(j,k)}
\frac{|a_k||t_k|+|a_j||t_j|}{4|\Delta_{jk}|}
\le H_N,
$$
$$
\boxed{\log H_N\le r\ell_N+C r,\qquad
\|P_{I,J}\|\le H_N.}
\tag{6.2}
$$
对 $f\in M$，$P_{I,J}f\in M$，
所以
$$
\|X^kP_{I,J}f\|
\le\|X_M\|^k\|P_{I,J}f\|.
$$

(3.2) 允许在
$$
X^kJ_FP_{I,J}f
=
J_F(\gamma_FX)^kP_{I,J}f
$$
中正规排序全部有限词。
零误差部分是 $X$ 加上有界交换增量，
其幂在当前输入上至多为固定几何增长。
含误差部分用 R260 的阶乘导数预算，
对 $k\le4pr$ 的全部词成本至多
$\epsilon_{\lfloor\mu N\rfloor}e^{C_p r\log(r+2)}$。
故充分大 $N$ 后，存在固定 $R_{p,M,\theta}$ 使
$$
\boxed{
\|X^kJ_FP_{I,J}f\|
\le2R_{p,M,\theta}^k\|P_{I,J}f\|
\qquad(0\le k\le4pr).
}
\tag{6.3}
$$
$p$ 固定；扩大到 $4pr$ 不改变双指数 carry 与四次提升预算之间的比较。

同一正常排序控制
$(\gamma_FT_\lambda)^r-\widehat T_\lambda^r$。
该有限词的 $X$ 总阶不超过 $pr$，
所有系数误差已经由 (3.2) 的 Banach 代数乘法支付，
所以误差不超过
$$
\epsilon_{\lfloor\mu N\rfloor}
e^{C_{p,\theta}r\log(r+2)}H_N\|f\|.
\tag{6.4}
$$

在 $M$ 上，$\widehat T_\lambda-T_\lambda$ 保持 $M$，
故 $\widehat T_\lambda^rP_{I,J}f$ 可按该有界差的 $r$ 次幂计算。
(4.1)–(4.3) 的全部余项均含某个真实选位平方。
以
$$
N_j^2=\eta_jN_{j+1},\qquad
\eta_j\le e^{-38516^j}
$$
支付，并使用 (4.3) 的系数绝对和与 (6.2)，
所有重复位项的总范数至多
$$
\eta_{\lfloor\mu N\rfloor}
C_{p,M,\theta}^rH_N\|f\|.
\tag{6.5}
$$
即使 (4.3) 有次数高达 $p$ 的项，
总系数预算仍是固定常数的 $r$ 次幂；
不能把单个词的总次数误当成额外未付的自由组合数。

正确次序为
$$
T_\lambda^rJ_FP_{I,J}f
=
J_F(\gamma_FT_\lambda)^rP_{I,J}f.
$$
先在 $M$ 中用 (5.3)，再施最左反射。
结合 $|F|=2r$ 的偶数符号及实际 $N_F$ 与纯 $E_F$ 的误差，
得到
$$
\boxed{
T_\lambda^rJ_FP_{I,J}f
=
r!t_FE_Ff+\mathcal E_{I,J}^{(p)}f,
}
\tag{6.6}
$$
$$
\|\mathcal E_{I,J}^{(p)}f\|
\le
\epsilon_{\lfloor\mu N\rfloor}
e^{C_{p,\theta}r\log(r+2)}H_N\|f\|
+
C r!|t_F|r\eta_{\lfloor\mu N\rfloor}\|f\|.
\tag{6.7}
$$
此处没有把任何核内算子移到 $J_F$ 的左侧。

## 7. 双池归一化完全保持

取
$$
\mathcal V_N
=
r!\left(\frac2N\right)^{2r}
\sum_{\substack{I\subset I_N,\ J\subset J_N\\|I|=|J|=r}}
t_F^{-1}J_FP_{I,J}.
\tag{7.1}
$$
总项数为 $\binom Nr^2$。
因此对 $L_b=\max(1,\sup_j|t_j|^{-1})$，
$$
\|\mathcal V_N\|\le A_N,\qquad
A_N=\max\left\{1,\frac{(4L_b^2)^r}{r!}H_N\right\},
$$
$$
\log A_N\le r\ell_N+C'r.
\tag{7.2}
$$

(6.6) 的 $r!$ 与 (7.1) 的 $r!$ 相乘，
恰好形成两个池各自 $r$ 次纯平均的系数。
若
$$
C_{I_N}=\frac2N\sum_{I_N}E_j,\qquad
C_{J_N}=\frac2N\sum_{J_N}E_j,
$$
则
$$
\|T_\lambda^r\mathcal V_Nf-C_{I_N}^rC_{J_N}^rf\|
\le
\left[
\epsilon_{\lfloor\mu N\rfloor}e^{C_{p,\theta}r\log(r+2)}A_N
+C4^r r\eta_{\lfloor\mu N\rfloor}
\right]\|f\|\to0.
\tag{7.3}
$$
纯平均范数不超过 $(1+1/N)^{2r}$。
在固定有限柱上的系数为 $[(N)_r/N^r]^2$，
所以
$$
\boxed{T_\lambda^r\mathcal V_Nf\rightharpoonup e^{-1/\theta}f.}
\tag{7.4}
$$
这个非零弱极限仍一致有界；
没有把高提升弱零转换成强近单位。

## 8. 全阶局部 A 因子及四次成本

固定前 $h$ 位的局部全矩阵 $D$。
令
$$
L_h=\sum_{j<h}a_j(R_j-I)=A V_h,
\qquad Z_h=X-L_h.
$$
$V_h$ 为实际真解析有限头。
$Z_h$ 为同一自然域上的闭尾 first 加标量，
与 $D$ 完整域交换。

把每个 $G_n$ 和 $Y$ 分为固定物理低头与高尾。
低头为真正解析有限和，且有零常数项，因此实际可提出一个 $A$。
高尾系数与 $D$ 交换。
用 $Z_h$ 及这些高尾系数构造
$T_{\lambda,\mathrm{tail},h}$，则它与 $D$ 完整域交换。
有限二项式和有限系数乘积差给实际深域分解
$$
\boxed{
T_\lambda
=
T_{\lambda,\mathrm{tail},h}+A U_h(X),
\qquad
U_h\in\mathcal A[z],\quad \deg U_h\le p-1.
}
\tag{8.1}
$$
只对固定有限头提出 $A$；
没有将完整 $G_n$ 或慢 $Y$ 有界除以 $A$。
两个加项在共同深域上交换，
因为它们都是 $X$ 的有界交换系数有限多项式。

因此
$$
\operatorname{ad}_{T_\lambda}^rD
=
\operatorname{ad}_{AU_h(X)}^rD
$$
在全部被测试的深域向量上成立。
其每项具有
$$
A^kU_h(X)^k\,D\,A^{r-k}U_h(X)^{r-k}
\tag{8.2}
$$
的形式。
$X$ 总阶至多为 $(p-1)r$。
固定局部 $D$ 的 $\delta_X$ 导数由固定低头有界 first 计算，
所以将有限 $X$ 字母移过 $D$ 只产生固定常数的几何成本。
(6.3) 的 $4pr$ jets 已覆盖所有这些词。

在 (8.2) 左右分别使用 $\|A^k\|$ 与 $\|A^{r-k}\|$，
R109 的原四次幂界及
$k^4+(r-k)^4\ge r^4/8$
给
$$
\boxed{
\|(\operatorname{ad}_{T_\lambda}^rD)\mathcal V_Nf\|
\le
2\|D\|A_N C_{p,D,M,\theta}^r
e^{-5r^4/6+105r^3}\|f\|.
}
\tag{8.3}
$$
多项式次数 $p$ 只进入固定几何常数；
四次负项没有被削减为低次。
这是一条具体输入向量上的估计，不是全空间有界交换子断言。

由 (1.3)、(7.2)，
$$
\limsup\frac{\log A_N}{r^4}
\le C_\ell\theta^{3/2}.
$$
固定足够小的 $\theta$ 使右边小于 $1/4$，
则 (8.3) 趋零。
$\theta$ 的选择不依赖局部 $D$。

## 9. 完整配对排核

对 $f,g\in M$，
所有有限词都在 $\mathcal D_\infty(X)$ 上合法。
完整 $C$ 自伴性允许逐个移动 $T_\lambda$，
而 $T_\lambda g=0$。
因此
$$
\mathcal B(DT_\lambda^r\mathcal V_Nf,g)
=
(-1)^r
\mathcal B((\operatorname{ad}_{T_\lambda}^rD)\mathcal V_Nf,g).
$$
结合 (7.4)、(8.3)，得到
$$
\mathcal B(Df,g)=0
$$
对所有局部全矩阵成立。
局部矩阵代数不可约，迫 $M=0$。
原完整 $C$ 自伴性给稠密像，
$\xi=e^w$ 的真实循环图核心遂给 (1.4)。
定理 1 得证。

## 10. 从二次双池构造直接得到的范围

二次稿的双池构造完全不依赖目标多项式的次数，
因此以下全部范围同时升为 (1.4) 的全阶结论。

### 10.1 任意物理排列的规则幂主行

若非零主幅度重排满足
$$
A_-n^{-\sigma}\le\rho_n\le A_+n^{-\sigma},
\qquad \sigma>\frac12,
$$
且对全部充分高的非零主物理位
$$
c_-|a_j|^\kappa\le|c_j|\le c_+|a_j|^\kappa,
\qquad \kappa>1,\quad c\in\ell^1,
$$
则固定大 $K$ 的两条秩带
$(N,3N]$ 与 $(KN,(K+2)N]$
在删除物理低位后各给 $N$ 项，
并满足
$$
|\Delta_{jk}|\ge C N^{-\sigma(\kappa+1)}.
$$
所以 (1.2)–(1.3) 成立。
有限物理头的偏离可以任意，包括全部低主位偏离为零。
所有复相位与物理重排都允许。

因此对于交替慢幂
$$
a_j=(-1)^j(j+1)^{-\sigma},\quad \frac12<\sigma<1,
$$
$$
c_0=0,\quad
c_j=\beta|a_j|^\kappa\omega_j\ (j\ge1),\quad
\kappa>2,\quad\beta\ne0,\quad|\omega_j|=1,
$$
每个固定非恒定 $q$、每个 $\lambda$、每个复 $\ell^2$ 指数权，
均满足 (1.4)。

### 10.2 两侧伸缩指数主行至 α=3/2

若
$$
A_-e^{-\beta_+n^\alpha}
\le\rho_n\le A_+e^{-\beta_-n^\alpha},
\qquad 0<\alpha\le3/2,
$$
仍有上述最终 $\kappa>1$ 比较，
则二次稿的同一双池给
$$
d_N\ge C e^{-C'N^\alpha}.
$$
因此 (1.4) 同样对全部固定 $q,\lambda$ 成立。
有限物理头例外不影响该构造。

$p=1$ 也由本稿定理允许；
严格线性抵消 $c=-q_1a$ 会使全部 $\Delta_{jk}=0$，
所以不会产生把零输出误称为循环的例外。

## 11. 没有自动外推的内容

本稿使用的是 R270C 明确设计的共振系数
$G_n=\text{常数}\sum a_j^n(R_j-I)^n$。
它们的反射差无 Boolean 一次项，由 (4.1) 逐项支付。
一般 $\mathcal G$ 系数未必有此性质；
不能只因一个系数属于 $\mathcal G$，
就把其反射差删去。

普通点态 $q(u)$、任意独立慢辅助的多变量多项式、
以及没有定量双池的任意不规则行，
仍需各自验证相应实际一次系数和预算。
本稿没有由两个形式独立方向直接推出所有混合多项式循环。

完整 Hilbert ISP 仍须继续推进其他开放项。

## 12. 来源

- [R176](../results/R176-natural-polynomial-maximal-graphs-and-bell-domains.md)：
  全部自然域、原完整 $C$ 自伴、核内有界 first 与图循环。
- [R270C](../results/R270-appendix-closed-first-fast-polynomials-and-all-order-resonant-cyclicity.md) §10：
  明确共振 $F_k$、实际 $G_n$ 与全阶有限 jets。
- [R260](../results/R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md)
  §§2–4、6：真实局部壳、完整导子 Banach 代数及阶乘导数正规排序。
- [二位二次完整源](2026-11-13-two-site-scalar-bezout-lifts-and-late-support-quadratic-cyclicity-central-review.md)：
  标量输入、双池精确归一化与实际秩带构造。
- [近共振统一准则](../results/R236-appendix-next-order-quadratic-resonance-and-resolvent-criterion.md)：
  原局部四次估计与完整双线性排核机制。

本稿新增的是 (3.1)–(4.4) 的全阶系数完整预算、
(5.3) 的高阶总次数消去、
以及 (8.1)–(8.3) 证明固定次数增长不破坏四次成本。
