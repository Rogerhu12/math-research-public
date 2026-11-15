# 原第一 wild 层、同一个 Rubin 系数及中央消失阶

日期：2026-11-15。**状态：下述第一层特化、原 Hall 迹的准确赋值、真实 cyclotomic 因子及 Weierstrass 必要条件已证明。没有证明第一层非消失，也没有把原中央导数为零提升为第一层为零。**

本注沿用 [R716](../results/R716-original-wild-global-theta-period-and-exact-central-l-value.md) 的同一 $E:y^2=x^3+17$、原 $S_{34}$、完整 $2/3/17$ Schwartz 向量和原 Hall 提升。设
$$
p>101,\qquad p\equiv5\pmod6,\qquad e_p=p-1,\qquad
K=\mathbf Q(\omega),\quad \delta=1+2\omega.
$$
原反圆分参数、整模和实际参考基均取 [R303](../results/R303-jzero-inert-full-selmer-period-comparison-and-central-criterion.md)，不重新选一个与原来源无关的 $p$-adic $L$-函数。

## 1. 同一整 Rubin 系数

令
$$
F_\theta^*\xi_{17}=\mathcal A_p(T)\xi_1,\qquad
\mathcal A_p(T)\in\mathcal O_{K_p}[[T]],\qquad
\theta=17^{1/6}.
\tag{1}
$$
R303 已证明 $\xi_1$ 是完整 signed 整模的基，而不是只在分式域中的基。因而 $\mathcal A_p$ 与 $E_{17}$ 的标准 Rubin 函数相差一个 Iwasawa 整单位。BHKO 的 Theorem 1.5（亦见 Theorem 6.10）适用于本曲线：$K$ 类数一，$E$ 在当前惯性素数好约化，且 $p\nmid6h_K$。所以
$$
\mu(\mathcal A_p)=0.
\tag{2}
$$
定义
$$
\lambda_p=\min\{i:[T^i]\mathcal A_p\in\mathcal O_{K_p}^{\times}\}.
\tag{3}
$$
它有限，但本文没有给出关于 $p$ 的一致上界。

记原完整 Newton 函数为 $J_p(u)$，并置
$$
e=\operatorname{ord}_{u=0}J_p.
$$
R303 的实际同类特化给
$$
\operatorname{ord}_{T=0}\mathcal A_p=2e,\qquad
v_p([T^{2e}]\mathcal A_p)
 =2v_p([u^e]J_p)-2e.
\tag{4}
$$
特别地，原指定 $j_{34}=J_p'(0)=0$ 只先给 $e\ge2$ 及 $T^4\mid\mathcal A_p$。

## 2. 第一 wild 特化及共轭的实际相位

令 $\nu=\widetilde\eta_{p,r}$ 为 R716 的实际 Hecke 角色。它的局部角色是 $\chi_{p,r}^2$，是阶 $p$、导子 $p^2$ 的反圆分角色；平方不可删。令
$$
t_\nu=\nu(\gamma)-1
$$
使用 (1) 的同一个生成元 $\gamma$。若原 Artin 约定使用逆角色，则同时改为 $t_{\nu^{-1}}$；下列赋值和整因子不变。

BHKO 的有限字符插值式与 Theorem 4.15 在第一层给
$$
v_p(\delta_\nu(v_+))=-1.
\tag{5}
$$
实际参考 $\xi_1$ 对应的 Rubin 函数为整单位。$F_\theta$ 的微分、Tate 格与所有有限下降比较均是原 R303 的单位。因此，在非零时，
$$
v_p\mathcal A_p(t_\nu)
 =v_p\!\left(\frac{L(\psi_{17}\nu,1)}{\Omega_{\rm CM}}\right)+1.
\tag{6}
$$
若使用插值中的 $\overline{\psi_{17}\nu}$，同时作原复共轭；下面把这一点的相位付清。

写 R716 的原有限和为
$$
\mathscr S_p(r)
 =\sum_{\substack{v\in\mathcal O_K/p\\Nv=r}}
       \chi_{p,r}(v)\,\mathcal A(v/p),
\qquad
\mathcal A(v)=k(\Omega_{\rm CM}v)^{34}
             \phi_{34}(P(\Omega_{\rm CM}v)).
\tag{7}
$$
原实模型的系数实，且
$$
\frac{\overline{\Omega_{\rm CM}}}{\Omega_{\rm CM}}=-\omega,
\qquad
\overline{\mathcal A(v)}=\mathcal A(-\omega\bar v),
\qquad
\chi_{p,r}(-\omega\bar v)=\chi_{p,r}(v)^{-1}.
\tag{8}
$$
这里最后一式同时用了原角色在 $\mu_6$ 上平凡及反圆分性。换代表时，R703/R705 的真实 Heisenberg carry 相位与 $\chi_{p,r}$ 的相位互相抵消，故 (8) 可在整个求和中使用，得到
$$
\overline{\mathscr S_p(r)}=\mathscr S_p(r).
\tag{9}
$$
原 Hall 迹 $\mathcal T_{34,T_v}$ 与 $\mathscr S_p(r)$ 只差 R703 已完整确定的根单位。因此 R716 的
$$
\frac{L(\psi_{17}\nu,1)}{\Omega_R}
 =\frac{48940416}{p}\,|\mathscr S_p(r)|^2
\tag{10}
$$
在每个相容的 $p$-adic 嵌入下都给
$$
v_p\!\left(\frac{L(\psi_{17}\nu,1)}{\Omega_{\rm CM}}\right)
 =2v_p(\mathcal T_{34,T_v})-1.
\tag{11}
$$
这里 $48940416$ 及 $\Omega_R/\Omega_{\rm CM}=1-\omega$ 都是当前位单位。

这一步没有声称原 Hilbert $p$ 扩张上只有一个 $p$ 地点；所需的是 (8)–(10) 中真实共轭仅留下根单位。结合 (6)，得到同一个原 Rubin 系数的准确第一层式
$$
\boxed{\quad
v_p\mathcal A_p(t_\nu)=2v_p(\mathcal T_{34,T_v}).
\quad}
\tag{12}
$$

## 3. 原边界零就是一个真实 cyclotomic 因子

$\Phi_p(1+T)$ 在 $\mathcal O_{K_p}[T]$ 上是 Eisenstein 多项式，且
$$
\ker\bigl(\mathcal O_{K_p}[[T]]
 \longrightarrow\mathcal O_{K_p}[\zeta_p],\
 T\longmapsto\zeta_p-1\bigr)
 =(\Phi_p(1+T)).
\tag{13}
$$
所以由原有限角色插值、R716 及 R663/R696 的同源迹公式，
$$
\boxed{\quad
\begin{aligned}
 B_{34}(v_T^{p+1})=0
&\iff \mathcal T_{34,T}=0\\
&\iff L(\psi_{17}\nu,1)=0\\
&\iff \Phi_p(1+T)\mid\mathcal A_p(T).
\end{aligned}
\quad}
\tag{14}
$$
任意非平凡阶 $p$ 角色都给同一个不可约因子；不是为每个 $r$ 添加独立假设。R716 的角色平方置换这些角色，故不改变 (14)。

由于 $T$ 与 $\Phi_p(1+T)$ 在分式域互素，若 (14) 成立，则
$$
T^{2e}\Phi_p(1+T)\mid\mathcal A_p(T).
$$
模 $p$ 后 $\Phi_p(1+T)\equiv T^{p-1}$，再由 (2) 得
$$
\boxed{\quad
 B_{34}(v_T^{p+1})=0
 \ \Longrightarrow\ \lambda_p\ge 2e+p-1.
\quad}
\tag{15}
$$
特别地，
$$
j_{34}=0,\quad B_{34}(v_T^{p+1})=0
\quad\Longrightarrow\quad
\lambda_p\ge p+3.
\tag{16}
$$
(16) 是两个真实条件的共同后果。本文没有从第一个条件单独推出第二个。

## 4. 小 Weierstrass 次数时的原迹值

若另有实际输入
$$
\lambda_p<p-1,
\tag{17}
$$
则在 $v_p(t_\nu)=1/(p-1)$ 处，$\mathcal A_p$ 的第 $\lambda_p$ 项严格支配：更低项的系数都被 $p$ 整除，更高项的幂次严格更大。因此
$$
v_p\mathcal A_p(t_\nu)=\frac{\lambda_p}{p-1},
\qquad
v_p(\mathcal T_{34,T})
 =\frac{\lambda_p}{2(p-1)}.
\tag{18}
$$
尤其原第一层不为零。

R663/R696 的原恒等式还给
$$
v_p(\mathcal T_{34,T})
 =\frac1{p-1}+v_pB_{34}(v_T^{p+1}),
\qquad
B_{34}(W)\in\mathcal O_{K_p}[[W]],
\quad v_p(v_T^{p+1})=\frac1{p-1}.
\tag{19}
$$
(18) 小于 $1/2$。所以 (19) 右侧只能由某个 $p$-单位系数 $b_iW^i$ 给出，且 $i<p-1$；带 $p$ 的较低系数估值至少一，不能参与最低项抵消。因而
$$
\lambda_p=2(i+1),\qquad
v_pB_{34}(v_T^{p+1})=\frac{i}{p-1}.
\tag{20}
$$
这证明 (17) 下的 $\lambda_p$ 必为偶数，并把它准确接回原 $B_{34}$ 的首个单位系数。没有证明 (17) 对所有或无穷多个 $p$ 成立。

## 5. 已发表非消失结果的精确范围

BHKO Theorems 1.1、1.3 对固定 $p$ 的足够高反圆分层给非消失和赋值式；Theorem 1.5 给 (2)。这些结论本身不排第一层因子 $\Phi_p(1+T)$。

在其惯性证明 §5.3.1 中，先使剩余值域包含 $\mu_p$，若其 $p$-Sylow 阶为 $p^s$，使用的深度条件是 $n>2s$；原导子 $p^2$ 层为 $n=2$，不能直接放入该步骤。之后的 Proposition 5.8 使用固定 $p$ 轨道的有限例外，未给出随 $p$ 一致的第一层界。以上只说明该证明的实际量词，未声称其他方法不可能支付 (17) 或第一层非消失。

原 $j_{34}$ 的未解步骤依然保留：从原完整中央条件联到足够强的第一层因子、原 $B$ 前缀或实际 $\lambda_p$ 界。一般 $\mu=0$ 不能替代这一步。

## 一手输入

- A. Burungale, W. He, S. Kobayashi, K. Ota, *Hecke L-values, definite Shimura sets and Mod $\ell$ non-vanishing*, arXiv:2408.13932v3，Theorems 1.3、1.5、4.14、4.15、6.10，§5.3.1、Proposition 5.8：[全文](https://arxiv.org/html/2408.13932v3)。
- 本课题 R303、R663、R696、R703、R705、R716 的实际整基、Hall 提升、有限角色、周期和完整原来源。这里没有换用一个可选但未识别的 toric test vector。
