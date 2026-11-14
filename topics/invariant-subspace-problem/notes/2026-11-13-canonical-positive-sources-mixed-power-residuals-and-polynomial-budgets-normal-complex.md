# 工作补充：同一规范正态源的混合高阶强残量与完整多项式预算

日期：2026-11-13 UTC。作者：normal_complex / Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。

本稿接
[规范有限头源补充](2026-11-13-canonical-head-positive-normal-sources-and-simultaneous-strong-annihilation-central-review.md)。
使用同一个固定正正常泛函、同一个完整有限头代表 $v_p$，将一阶强残量提高到混合幂的完整尾乘积。
实际头中的真解析修正保留为实际算子；它与局部头之间的差另付超指数 carry。
没有把一般尾函数当成局部算子，没有给不同幂重选见证。

## 1. 已付源及本文的准确分解条件

令 $\mathfrak C=A'$，$\rho\ge0$ 为固定正迹类，
$\tau=\operatorname{Tr}\rho>0$，$\varphi=\varphi_\rho$。
使用原完整规范头代表 $v_p=v_p^\rho\in\operatorname{Ran}\Pi_p$、
实际及局部有限 Walsh 乘子 $X_w,X_w^{[p]}$。
准确已有
$$
\|v_p\|\le\tau K_p,\qquad
K_p=10^{p/2},
$$
$$
B(v_p,R_p\Omega)=\varphi(R_p)\quad(R_p\in\mathcal A_p),
\qquad
\|X_w\|,\|X_w^{[p]}\|\le K_p\|w\|,
$$
$$
\|X_w-X_w^{[p]}\|\le D_p\|w\|,
\qquad
D_p\le6p\eta_{p-1}K_p.
\tag{1.1}
$$
$C$ 保持该有限头，$B(u,w)=\langle u,Cw\rangle$。
局部代数 $\mathcal A_p$ 交换且共同 $C$ 对称。
它只作用于前 $p$ 位，在头外张量恒等。

这个同一 $v_p$ 已满足
$$
\|\Phi_{v_p}-\varphi\|_{\mathfrak C_*}
\le\tau D_p+2\delta_p+2\sqrt{\tau\delta_p}\longrightarrow0,
\qquad
\langle v_p,\Omega\rangle=\tau,
\tag{1.2}
$$
其中 $\delta_p=\operatorname{Tr}(\rho(I-\Pi_p))$。
本稿不改变 (1.2) 的正常尾误差，也不为它附加衰减速度。

固定有限个实际交换元 $Z_1,\ldots,Z_d\in\mathcal A$，假设同一个泛函满足
$$
\varphi(Z_\nu R)=0
\quad(R\in\mathfrak C,\ 1\le\nu\le d).
\tag{1.3}
$$
对当前头长 $p$，要求有分解
$$
Z_\nu=\widehat L_{\nu,p}+R_{\nu,p},
\qquad
\widehat L_{\nu,p},R_{\nu,p}\in\mathcal A,
\tag{1.4}
$$
其中 $R_{\nu,p}$ 只作用于头外。
取同一个局部代数中的 $L_{\nu,p}\in\mathcal A_p$，令
$$
r_{\nu,p}=\|R_{\nu,p}\|,
\qquad
e_{\nu,p}=\|\widehat L_{\nu,p}-L_{\nu,p}\|.
\tag{1.5}
$$
于是局部头 $L_{\nu,p}$ 与全部实际尾 $R_{\mu,p}$ 交换。
实际尾之间亦交换，因为它们在 $\mathcal A$ 中。
但不需要、也不声称局部 $L_{\nu,p}$ 与实际头 $\widehat L_{\mu,p}$ 交换。

为简化常数，以下固定 $p$ 时省略下标 $p$。
取任意
$$
M\ge1,\qquad
\|\widehat L_\nu\|,\ \|L_\nu\|,\ r_\nu\le M
\quad(1\le\nu\le d),
\qquad B=2M.
\tag{1.6}
$$
当这些分解随 $p$ 按范数逼近时，可以对所有充分大的 $p$ 使用同一个 $M$。

对多重指标 $\alpha\in\mathbb N_0^d$，写
$$
q=|\alpha|,\qquad
r^\alpha=\prod_\nu r_\nu^{\alpha_\nu},\qquad
E_\alpha=\sum_\nu\alpha_\nu e_\nu.
\tag{1.7}
$$
约定 $0^0=1$；$q=0$ 仅使用 $\|v_p\|\le\tau K_p$。

## 2. 实际头的混合矩准确转移到实际尾

由 $\widehat L_\nu=Z_\nu-R_\nu$、全部实际元交换以及 (1.3)，
逐项展开有限乘积即给
$$
\boxed{
\varphi(\widehat L^\beta R)
=(-1)^{|\beta|}\varphi(R_{\rm tail}^{\beta}R)
\quad(R\in\mathfrak C).
}
\tag{2.1}
$$
这里 $R_{\rm tail}^{\beta}=\prod_\nu R_\nu^{\beta_\nu}$；
右侧最后的 $R$ 仍是任意实际右测试。
所有含至少一个 $Z_\nu$ 的项都属于被同一个 $\varphi$ 湮灭的实际主理想。
这一步不用局部头，不混用不同见证。

取 $w\in\operatorname{Ran}\Pi_p$、$\|w\|=1$。
局部 $C$ 对称性和 (1.1) 给
$$
B(L^\beta v_p,w)
=B(v_p,L^\beta X_w^{[p]}\Omega)
=\varphi(L^\beta X_w^{[p]}).
\tag{2.2}
$$
若 $b=|\beta|\ge1$，有限有序望远镜式给
$$
\|L^\beta-\widehat L^\beta\|
\le E_\beta M^{b-1}.
\tag{2.3}
$$
此式逐个替换乘积中的因子，故不要求两种头彼此交换。

从 (2.2) 减去实际项
$\varphi(\widehat L^\beta X_w)$，
再用 (2.1)，得到
$$
|B(L^\beta v_p,w)|
\le
\tau K_p r^\beta
+\tau K_p E_\beta M^{b-1}
+\tau D_pM^b.
$$
$L^\beta v_p$ 留在有限头内，且 $C$ 保持该头，
对全部单位 $w$ 取上确界可得
$$
\boxed{
\|L^\beta v_p\|
\le
\tau\left(K_pr^\beta+
K_pE_\beta M^{b-1}+D_pM^b\right)
\quad(b\ge1).
}
\tag{2.4}
$$
对 $\beta=0$ 使用准确预算 $\|v_p\|\le\tau K_p$，
不引入额外 $D_p$ 项。

(2.4) 的首项含完整尾乘积 $r^\beta$。
它来自所有混合正常湮灭式，而不是把一阶向量残量作幂。

## 3. 同一个源的实际混合幂

令
$$
B_\nu=L_\nu+R_\nu.
$$
这组算子两两交换，因为局部头之间、实际尾之间、头与尾之间均交换。
所以
$$
B^\alpha v_p=
\sum_{\beta\le\alpha}
\binom{\alpha}{\beta}
R_{\rm tail}^{\alpha-\beta}L^\beta v_p.
\tag{3.1}
$$

将 (2.4) 及 $\beta=0$ 的单独预算代入。
主项准确求和为
$$
\tau K_p
\sum_{\beta\le\alpha}
\binom{\alpha}{\beta}
r^{\alpha-\beta}r^\beta
=\tau K_p\,2^q r^\alpha.
\tag{3.2}
$$
第一种误差满足
$$
\begin{aligned}
&\sum_{\beta\le\alpha}
\binom{\alpha}{\beta}
r^{\alpha-\beta}E_\beta M^{|\beta|-1}\\
&\quad=
\sum_{\nu=1}^d
\alpha_\nu e_\nu
(M+r_\nu)^{\alpha_\nu-1}
\prod_{\mu\ne\nu}(M+r_\mu)^{\alpha_\mu}
\le E_\alpha B^{q-1}.
\end{aligned}
\tag{3.3}
$$
和式中 $|\beta|=0$ 的项按零处理。
第二种误差的和为
$$
D_p\left(\prod_\nu(M+r_\nu)^{\alpha_\nu}-r^\alpha\right)
\le D_pB^q.
\tag{3.4}
$$

最后比较实际 $Z^\alpha$ 与 $B^\alpha$。
每个因子 $Z_\nu-B_\nu=\widehat L_\nu-L_\nu$ 的范数为 $e_\nu$，
且 $\|Z_\nu\|,\|B_\nu\|\le B$。
再次作有序望远镜，不假设不同两组算子交叉交换，得到
$$
\|Z^\alpha-B^\alpha\|\le E_\alpha B^{q-1}.
$$
乘上 $\|v_p\|\le\tau K_p$，
并与 (3.2)--(3.4) 合并即得完整结论：
$$
\boxed{
\|Z^\alpha v_p\|
\le
\tau K_p\,2^q r^\alpha
+2\tau K_pE_\alpha B^{q-1}
+\tau D_pB^q
\qquad(q\ge1).
}
\tag{3.5}
$$
特别，若 $e=\max_\nu e_\nu$，则
$$
\|Z^\alpha v_p\|
\le
\tau K_p\,2^q r^\alpha
+2\tau K_pq eB^{q-1}
+\tau D_pB^q.
\tag{3.6}
$$
这是实际混合幂的强向量界，阶数 $q$ 不必固定。
所有增长费用都保留在公式中。

### 3.1 任意多项式必须保留其真实系数费用

对无常数项多项式
$$
P(z)=\sum_{\alpha\ne0}c_\alpha z^\alpha
$$
定义非负系数主控
$$
P^\#(t_1,\ldots,t_d)=
\sum_{\alpha\ne0}|c_\alpha|
\prod_\nu t_\nu^{\alpha_\nu},
\qquad
A_P(t)=\sum_{\alpha\ne0}|c_\alpha|t^{|\alpha|}.
$$
由 (3.6) 逐项求和，
$$
\boxed{
\|P(Z_1,\ldots,Z_d)v_p\|
\le
\tau K_pP^\#(2r_1,\ldots,2r_d)
+2\tau K_p eA_P'(B)
+\tau D_pA_P(B).
}
\tag{3.7}
$$
允许 $P$ 随 $p$ 改变，只要右侧全部实际系数费用均被支付。
本稿没有用单一算子范数 $\|P(Z)\|$ 替代这些系数费用，
也不把任意右因子的预算免费并入本式。

## 4. 同一个迟首联合见证的两条慢行

沿用已固定的 $H=H_\zeta$、$\rho$，写
$$
X=\sum_ja_jQ_j,\quad
Y=\sum_jc_jQ_j,\quad
B_0=\sum_ja_j^2Q_j^2,
$$
$$
S=X+H,\quad
G=B_0-H^2,\quad
Z=Y-G,\quad
T=X^2-B_0+Y.
\tag{4.1}
$$
同一个 $\varphi$ 湮灭 $S\mathfrak C$、$Z\mathfrak C$、$T\mathfrak C$。
定义真正作用于头外的实际尾
$$
A_p^{\rm tail}=\sum_{j\ge p}a_jQ_j,\qquad
C_p^{\rm tail}=\sum_{j\ge p}c_jQ_j,
$$
$$
r_{a,p}=\|A_p^{\rm tail}\|
\le4\sum_{j\ge p}|a_j|,\qquad
r_{c,p}=\|C_p^{\rm tail}\|
\le4\sum_{j\ge p}|c_j|.
\tag{4.2}
$$
实际头选择为
$$
\widehat S_p=S-A_p^{\rm tail},\qquad
\widehat Z_p=Z-C_p^{\rm tail}.
\tag{4.3}
$$
其中完整的实际 $H$、$G$ 都保留在实际头里。
$\widehat S_p,\widehat Z_p$ 本身不被当成只作用于前 $p$ 位。

采用规范源补充中的同一个局部 $S_p,Z_p\in\mathcal A_p$。
它们由 $Q_j^{[p]}$、$H(A^{[p]})$ 及 $B_p$ 构成。
该稿 §5 的固定解析圈与二阶真实 carry 预算给
$$
e_p=
\max\{\|\widehat S_p-S_p\|,
       \|\widehat Z_p-Z_p\|\}
\le C_e\bar\eta_{p-1},
\qquad
\bar\eta_j=e^{-770\,16^j}.
\tag{4.4}
$$
这里 $B_0-B_p$ 的尾是
$36\sum_{j\ge p}|a_j|^2\bar\eta_j$，
不是一个慢 $\sum|a_j|^2$ 尾。
故 (4.4) 对辅助行同样是纯 carry 费用。

这些头和尾的算子范数有与 $p$ 无关的上界。
将 (3.5) 用于 $(S,Z)$，得到
$$
\boxed{
\|S^kZ^\ell v_p\|
\le
\tau K_p(2r_{a,p})^k(2r_{c,p})^\ell
+C\tau K_p(p+q)B^q\bar\eta_{p-1},
\qquad q=k+\ell\ge1.
}
\tag{4.5}
$$
$C,B\ge1$ 只依赖当前固定两行及其解析修正，
不依赖 $p,k,\ell$ 或 $\rho$；$\rho$ 的总体尺度是外面的 $\tau$。

### 4.1 真实二次行及其混合幂

不把 $T-T_p$ 全部称为纯尾算子。
它含有交叉头系数。
准确使用恒等式
$$
\boxed{T=(X-H)S+Z.}
\tag{4.6}
$$
全部为实际交换元。
令 $M_0=\|X-H\|$，对 $n,k,\ell\ge0$、
$q=n+k+\ell\ge1$，展开 $T^n$ 后应用 (4.5)：
$$
\boxed{
\begin{aligned}
\|T^nS^kZ^\ell v_p\|
\le{}&
\tau K_p(2r_{a,p})^k(2r_{c,p})^\ell
\bigl(2M_0r_{a,p}+2r_{c,p}\bigr)^n\\
&+C\tau K_p(p+q)
\bigl(B(1+M_0)\bigr)^q\bar\eta_{p-1}.
\end{aligned}
}
\tag{4.7}
$$
在展开中每项的 $S,Z$ 总次数恰为 $q$；
其误差系数之和是 $(1+M_0)^n$，已包含于上界。
这不使用 $\rho$ 的真实核支持；真实核支持对另一交叉源 $h_p$ 的
$\sqrt{\delta_p}$ 加强仍按原稿单独保留。

## 5. 伸缩指数尾与允许增长的次数

在当前固定余族，取
$$
a_j=e^{-\beta j^\alpha},\qquad
c_j=a_j^\kappa\mathbf1_{j>j_0},
\qquad
\alpha>1,\quad\beta>0,\quad\kappa>1.
\tag{5.1}
$$
充分大的 $p$ 上，凸性给
$$
r_{a,p}\le C_a e^{-\beta p^\alpha},
\qquad
r_{c,p}\le C_c e^{-\kappa\beta p^\alpha}.
$$
所以 (4.5) 具体成为
$$
\boxed{
\|S^kZ^\ell v_p\|
\le
\tau10^{p/2}
\left[
C_0^q e^{-\beta(k+\kappa\ell)p^\alpha}
+C_1(p+q)C_2^q
 e^{-770\,16^{p-1}}
\right],
\quad q=k+\ell\ge1.
}
\tag{5.2}
$$
常数与所有这些次数统一。

例如，对任何随 $p$ 变化的非负整数 $k_p,\ell_p$，若
$$
q_p=k_p+\ell_p\ge1,\qquad
q_pp^\alpha=o(16^p),
\tag{5.3}
$$
则对任意固定 $\epsilon>0$，充分大 $p$ 时
$$
\boxed{
\|S^{k_p}Z^{\ell_p}v_p\|
\le
\tau\exp\!\left[-(\beta-\epsilon)
       (k_p+\kappa\ell_p)p^\alpha\right].
}
\tag{5.4}
$$
若 $\epsilon\ge\beta$，结论仍由小正 $\epsilon$ 的版本推出；
有内容的情形是 $0<\epsilon<\beta$。

确实，
$\log K_p+q_p\log C_0=O(p+q_p)
=o((k_p+\kappa\ell_p)p^\alpha)$。
由 (5.3)，carry 项的对数
$$
-770\,16^{p-1}+O(p+q_p+\log(p+q_p))
$$
比 $-\beta(k_p+\kappa\ell_p)p^\alpha$ 更负，
故也可吸收到 (5.4)。
任意固定幂增长 $q_p=O(p^L)$ 都满足 (5.3)。
这给出可供真实高阶证书使用的已付向量残量，
而非只给固定次数结论。

## 6. 预算的用途与未给出的逆步骤

(3.7)、(4.5)、(5.2) 可以与另行构造的实际多项式或右因子预算相乘。
其中所有局部比较、源的 $10^{p/2}$ 因子及次数系数均已列明。
原正常泛函近似仍是 (1.2)，其 $\delta_p$ 没有额外速度。

这些强混合残量不推出 $v_p$ 到有限或无限联合核的距离小，
不提供相应正交投影、伪逆或解方程的费用。
同样不把任意高次数输入的性质升级为保持原正交代表的有限窗论证。
当前 $S$ 在全空间单射时，原规范源仍满足
$\|v_p\|\to\infty$、$v_p/\|v_p\|\rightharpoonup0$，
而真空锚始终为 $\tau$。

需要下一步单独支付的，是一个与上述实际费用相容的源范数上界、
或含非零快元的真实理想证书。
本稿只提供供该步骤使用的更高阶强残量，不把该逆步骤视为已经完成。

## 7. 真正二次核给重置正密度的全部 Hilbert--Schmidt 幂残量

本节使用 root 提出的实际头分解，并完整核验其算子域、部分迹和费用。
额外假设同一个原正密度确有核支持
$$
T\rho^{1/2}=0.
\tag{7.1}
$$
该条件对原迟首核的秩一见证成立；
不能只从 $\varphi(T\mathfrak C)=0$ 推出它。

### 7.1 实际二次头及非纯尾余项

定义全部实际的有限和
$$
X_{<p}=\sum_{j<p}a_jQ_j,\qquad
Y_{<p}=\sum_{j<p}c_jQ_j,\qquad
B_{<p}=\sum_{j<p}a_j^2Q_j^2,
$$
$$
\widehat T_p=X_{<p}^{\,2}-B_{<p}+Y_{<p}.
\tag{7.2}
$$
其差准确为
$$
\boxed{
R_p=T-\widehat T_p
=2X_{<p}A_p^{\rm tail}
 +(A_p^{\rm tail})^2-B_p^{\rm tail}+C_p^{\rm tail},
\quad
B_p^{\rm tail}=\sum_{j\ge p}a_j^2Q_j^2.
}
\tag{7.3}
$$
这些都是实际 $\mathcal A$ 元素，因而彼此交换。
$R_p$ 含实际头系数 $2X_{<p}$，本节不把它当成只作用于尾的算子。

令
$$
r_{T,p}=\|R_p\|.
$$
原真实二阶 carry 给
$$
\boxed{
r_{T,p}\le
(2\|X_{<p}\|+r_{a,p})r_{a,p}
 +36\sum_{j\ge p}|a_j|^2\eta_j+r_{c,p}.
}
\tag{7.4}
$$
设 $T_p\in\mathcal A_p$ 为同一局部头中
$X_p^2-B_p+Y_p$ 的准确定义。
逐位低头差和平方望远镜给
$$
\epsilon_p=\|\widehat T_p-T_p\|
\le C_T\bar\eta_{p-1}.
\tag{7.5}
$$
这里只比较同一有限和的实际与局部算子；
没有将 (7.3) 的慢余项并入 (7.5)。
取与 $p$ 无关的
$$
M_T\ge1,\qquad
\|\widehat T_p\|,\|T_p\|\le M_T
$$
对所有充分大的 $p$ 成立。

### 7.2 真核、局部幂和部分迹的准确次序

由 (7.1) 及 $\widehat T_p=T-R_p$ 的实际交换性，
对每个整数 $n\ge1$ 有准确算子等式
$$
\boxed{
\widehat T_p^{\,n}\rho^{1/2}
=(-R_p)^n\rho^{1/2}.
}
\tag{7.6}
$$
这是先在整个实际空间上使用真核关系，再比较局部头。
因此
$$
\|\widehat T_p^{\,n}\rho^{1/2}\|_{\mathrm{HS}}
\le r_{T,p}^{\,n}\sqrt\tau.
$$
有序幂望远镜给
$$
\|T_p^n-\widehat T_p^{\,n}\|
\le nM_T^{n-1}\epsilon_p,
$$
无需局部 $T_p$ 与实际 $\widehat T_p$ 交换。
故
$$
\boxed{
\|T_p^n\rho^{1/2}\|_{\mathrm{HS}}
\le
\sqrt\tau\,
\left(r_{T,p}^{\,n}+nM_T^{n-1}\epsilon_p\right).
}
\tag{7.7}
$$

现在令
$$
\widehat\rho_p=
(\operatorname{Tr}_{\ge p}\rho)
 \otimes|\Omega_{\ge p}\rangle\langle\Omega_{\ge p}|
$$
为规范源补充中的正重置密度。
由于 $(T_p^n)^*T_p^n$ 是同一个头上的有界局部算子，
部分迹准确保留它的期望：
$$
\begin{aligned}
\|T_p^n\widehat\rho_p^{\,1/2}\|_{\mathrm{HS}}^2
&=\operatorname{Tr}
 \left(\widehat\rho_p (T_p^n)^*T_p^n\right)\\
&=\operatorname{Tr}
 \left(\rho (T_p^n)^*T_p^n\right)
=\|T_p^n\rho^{1/2}\|_{\mathrm{HS}}^2.
\end{aligned}
$$
因而有完整的正密度结论
$$
\boxed{
\|T_p^n\widehat\rho_p^{\,1/2}\|_{\mathrm{HS}}
=
\|T_p^n\rho^{1/2}\|_{\mathrm{HS}}
\le
\sqrt\tau\,
\left(r_{T,p}^{\,n}+nM_T^{n-1}\epsilon_p\right).
}
\tag{7.8}
$$
相等的是 Hilbert--Schmidt 范数，未把两个算子值本身写成相等。
这里的部分迹可以测试整个头矩阵代数，
不要求 $(T_p^n)^*T_p^n\in\mathcal A_p$ 或实际 $\mathfrak C$。

在 (5.1) 的指数包络下，
$r_{T,p}\le C e^{-\beta p^\alpha}$、$\epsilon_p\le C\bar\eta_{p-1}$。
因此若 $n_pp^\alpha=o(16^p)$、$n_p\ge1$，
对任意 $0<\epsilon<\beta$，充分大 $p$ 时
$$
\|T_p^{n_p}\widehat\rho_p^{\,1/2}\|_{\mathrm{HS}}
\le
\sqrt\tau\,
 e^{-(\beta-\epsilon)n_pp^\alpha}.
\tag{7.9}
$$
这保留正密度的实际近核信息，不需要规范源的 $K_p$ 放大。

### 7.3 一个带明确阈值的有限矩阵条件接口

为准确标出仍需证明的步骤，取任意整数 $n_p\ge1$ 和数 $s_p>0$，记
$$
b_p=r_{T,p}^{\,n_p}
+n_pM_T^{n_p-1}\epsilon_p,
$$
$$
P_p=\mathbf1_{[0,s_p]}(|T_p^{n_p}|),
\qquad
|T_p^{n_p}|=((T_p^{n_p})^*T_p^{n_p})^{1/2}.
\tag{7.10}
$$
$P_p$ 是有限头谱投影，头外张量恒等。
谱定理与 (7.8) 给
$$
\boxed{
\operatorname{Tr}\bigl(\widehat\rho_p(I-P_p)\bigr)
=
\operatorname{Tr}\bigl(\rho(I-P_p)\bigr)
\le\tau(b_p/s_p)^2.
}
\tag{7.11}
$$
中间等号仍是准确部分迹，不需要先取重置密度的极限。

所以，若另行证明
$$
b_p=o(s_p),\qquad P_p\longrightarrow0\ \text{强收敛},
\tag{7.12}
$$
则 (7.11) 迫 $\operatorname{Tr}(\rho P_p)\to\tau$，
而正常性与强收敛迫该迹趋于零，矛盾。
条件 (7.12) 因而足以排除该真实正核见证。

本节未证明 (7.12) 的第二项。
$P_p$ 是一个有准确阈值的低奇异值区间投影，不是未经付费的核投影；
仅有它的维数比例、抽象相似变换或一般次数计数，
不能替代原表示中的强收敛。
这是可继续分析的具体有限矩阵门槛，未宣称其已经被支付。
