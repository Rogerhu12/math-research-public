# R270 第一附录：最大根重数与同阶无限辅助模式的非共振准则

日期：2026-11-13（UTC）。作者：kernel；Astra-ISP-1cf8c51d 复核。
状态：已证明。本文只加强 R270 的无限重叠多模式范围，不宣称普通 Hilbert ISP 完成。

## 1. 定理

保留 R270 的主行、任意复 first 指数权与首一多项式：
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad
w=b_*+\sum_{j\ge0}b_j\chi_j,\qquad a,b\in\ell^2,
$$
$$
P(z,y_1,\ldots,y_d)=z^p+\sum_{k<p}P_k(y)z^k,\qquad p\ge1.
$$
主幅度排序 $\rho_k$ 满足 R268 的实际熵条件：沿无穷尺度 $N$，
$$
\sup_{k\ge N}k\rho_k\le DN\rho_N,\qquad
E_N:=\sum_{k\le N}\log(\rho_k/\rho_N)=O(N^2),
$$
$$
L_N:=1+\log^+\rho_N^{-1}=O(N^{3/2}).
\tag{1.1}
$$

取辅助行
$$
v_\ell=c_{\ell,*}+\sum_j c_{\ell j}\chi_j.
$$
先给定其中心
$$
s_\ell=c_{\ell,*}+\sum_jc_{\ell j},
$$
并记
$$
q_0(z)=P(z,s),\qquad
\Lambda=\{\text{$q_0$ 的不同根}\},\qquad
\mu_\lambda=\operatorname{ord}_\lambda q_0.
$$
令
$$
\mu=\max_{\lambda\in\Lambda}\mu_\lambda,\qquad
m=\max(2,\mu).
\tag{1.2}
$$
这些量是同一组实际数据的条件；亦可先指定 $s$ 与系数行，再通过
$c_{\ell,*}=s_\ell-\sum_jc_{\ell j}$ 实现指定中心。

假设同一物理位上
$$
c_{\ell j}=0\quad(a_j=0),\qquad
|c_{\ell j}|\le C_\ell |a_j|^m.
\tag{1.3}
$$
因为 $m\ge2$，各辅助行确在 $\ell^1$，故中心和有意义。

若 $\mu\ge2$，对每个具有最大重数 $\mu$ 的根 $\lambda$，
再假设存在共同 $\eta>0$ 与 $j_0$，使
$$
\boxed{
\left|
(-2)^\mu\,\frac{q_0^{(\mu)}(\lambda)}{\mu!}
-
2\sum_{\ell=1}^d
P_{y_\ell}(\lambda,s)\frac{c_{\ell j}}{a_j^\mu}
\right|\ge\eta
}
\tag{1.4}
$$
对所有 $j\ge j_0$ 且 $a_j\ne0$ 成立。
若 $\mu=1$，不需条件 (1.4)。

**定理。**
$$
\boxed{P(u,v_1,\ldots,v_d)e^w\text{ 对原实际 }A\text{ 循环}.}
\tag{1.5}
$$

条件 (1.4) 是有限组明确的复数非共振条件，不要求辅助与主系数的相位相同。
它只涉及最大重根；较低重数的根自动分离。

特别：

1. 若 $q_0$ 的根全简单，则任意主次数 $p$ 都允许
   $|c_{\ell j}|\le C_\ell|a_j|^2$。
2. 若 $\mu\ge2$ 且 $c_{\ell j}=o(|a_j|^\mu)$，则 (1.4) 自动成立，
   且不需小 $o$ 的速率。
3. 若 $\mu\ge2$、$c_{\ell j}=\theta_\ell a_j^\mu$，
   只需固定向量 $\theta$ 避开有限个明确仿射超平面。
   辅助行可以与主行具有完全相同的无限支撑。

## 2. 实际混合参数与自然域

沿用 R270 的真实记号
$$
t_j=e^{-2b_j},\quad R_j=V(t_jN_j),\quad X=X_b,
$$
$$
Y_\ell=c_{\ell,*}I+\sum_jc_{\ell j}R_j,\qquad
Z_\ell=Y_\ell-s_\ell I,
$$
$$
K_\nu=\sum_j a_j^{\nu_0}\prod_{\ell\ge1}c_{\ell j}^{\nu_\ell}
L_{|\nu|}(R_j),\qquad |\nu|\ge2.
$$
只取固定 $P$ 所需的有限多重指标。
现在分配权
$$
w(Z_\ell)=m,\qquad
m_\nu=\nu_0+m\sum_{\ell\ge1}\nu_\ell.
\tag{2.1}
$$
纯主参数的权为 $n\ge2$，其余混合参数的权至少 $m+1$；
全部权至少为 2。
真实系数界为
$$
\left|a_j^{\nu_0}\prod_\ell c_{\ell j}^{\nu_\ell}\right|
\le C_\nu |a_j|^{m_\nu}.
$$

设
$$
\mathcal P(z;\beta,\kappa)=
\left[
\exp\left(\sum_\nu \frac{\kappa_\nu}{\nu!}
\partial_{z,y}^{\,\nu}\right)P(z,y)
\right]_{y=s+\beta}.
\tag{2.2}
$$
R270 的实际混合 jet 恒等式仍准确给
$$
T:=\mathcal P(X;Z,K),\qquad
Te^w=P(u,v)e^w.
\tag{2.3}
$$
这是关于 $X$ 的首一 $p$ 次自然多项式。
R176 任意有界交换系数定理给
$$
\operatorname{Dom}T=\operatorname{Dom}X^p,\qquad
T=C_0T^*C_0,
$$
以及对 $M=\ker T$
$$
M\subset\mathcal D_\infty,\qquad X_M\in B(M).
\tag{2.4}
$$
这些结论不依赖新非共振条件。全部混合参数均有界并保同一个 $M$。

R270 的幂次主控熵引理对 (2.1) 的每个权适用。
在 $\delta=\rho_N$ 及固定小 $\varepsilon>0$ 下，共同圆周为
$$
|\beta_\ell|=\varepsilon\delta^m,\qquad
|\kappa_\nu|=\varepsilon\delta^{m_\nu}.
\tag{2.5}
$$
全部系数函数的一次实际共同求值成本仍为
$$
K\exp[C(E_N+L_N^{4/3}+N^2)].
\tag{2.6}
$$
没有权 1 的参数，也没有逐位重复支付这个成本。

## 3. 加权根团估计

下面的标量引理是本附录的新步骤。

记
$$
d_\lambda=\frac{q_0^{(\mu_\lambda)}(\lambda)}{\mu_\lambda!}\ne0.
$$
取足够小的固定 $\theta\in(0,1/8)$；
随后取足够小的固定 $\varepsilon>0$。
对于小 $\delta>0$，在扩大一倍的 (2.5) 多圆盘上，
$\mathcal P$ 在每个原根 $\lambda$ 的
$$
|z-\lambda|<\frac{\theta\delta}{2}
\tag{3.1}
$$
内恰有 $\mu_\lambda$ 个根，按重数计，且其全部根都在这些小盘中。

证明：先仅保纯主参数，得到
$$
\mathcal P_0(z;\kappa_{\rm pure})
=
\exp\left(\sum_{n=2}^p\frac{\kappa_n}{n!}\partial_z^n\right)q_0(z).
$$
每个非恒定 Taylor 项的总主微分阶为 $k$，参数乘积的绝对值
不超过 $C\varepsilon\delta^k$。
在 $|z-\lambda|=\theta\delta/2$ 上，
$$
|q_0^{(k)}(z)|\le C_\theta\delta^{\max(\mu_\lambda-k,0)}.
$$
所以纯参数扰动 $\le C_\theta\varepsilon\delta^{\mu_\lambda}$。

其余项至少包含一个辅助中心参数，权至少 $m$，
或一个含辅助的混合参数，权至少 $m+1$。
固定邻域中所有多项式导数有界，因此这些项总和
$\le C\varepsilon\delta^m
\le C\varepsilon\delta^{\mu_\lambda}$。
这里 $m\ge\mu_\lambda$。
而原 $q_0$ 在该圆周上的模长
$\ge c_\theta\delta^{\mu_\lambda}$。
先固定 $\theta$，再选 $\varepsilon$，Rouché 定理即证明 (3.1)。

在外圈
$$
\Gamma_\lambda=\{|z-\lambda|=\theta\delta\}
$$
上同理有
$$
|\mathcal P(z;\beta,\kappa)|
\ge c_\theta\delta^{\mu_\lambda}.
\tag{3.2}
$$
全部结论在扩大一倍多圆盘及其一个邻域内一致。

## 4. 完整辅助平移的主项

设 $\delta\le|a|\le a_0$，以及辅助向量 $c=(c_1,\ldots,c_d)$ 满足
$|c_\ell|\le C_\ell|a|^m$。
对闭盘内全部点
$$
|\zeta-\lambda|\le\theta\delta
$$
考虑完整平移
$$
\mathcal P(\zeta-2a;\beta-2c,\kappa).
$$

在 $\lambda$ 邻域的有限 Taylor 展开给
$$
q_0(\zeta-2a)
=
d_\lambda(-2a)^{\mu_\lambda}
+
O\big((\theta+|a|)|a|^{\mu_\lambda}\big).
\tag{4.1}
$$
辅助中心平移的未扰动贡献为
$$
P(\zeta-2a,s-2c)-q_0(\zeta-2a)
=
-2\sum_\ell P_{y_\ell}(\lambda,s)c_\ell
+O(|a|^{m+1}+|a|^{2m}).
\tag{4.2}
$$
这里把 $P_{y_\ell}(\zeta-2a,s)$ 替换为
$P_{y_\ell}(\lambda,s)$ 的误差是 $O(|a|^{m+1})$。

所有 $\beta$ 与 $\kappa$ 参数的额外贡献为
$$
O(\varepsilon |a|^{\mu_\lambda}).
\tag{4.3}
$$
具体地，纯主参数乘积的权等于其主微分阶 $k$：
作用于 $q_0$ 时成本
$\delta^k|a|^{\max(\mu_\lambda-k,0)}
\le |a|^{\mu_\lambda}$；
作用于辅助平移差时另有因子 $O(|a|^m)$。
含辅助的参数权至少 $m$，故也至少 $\mu_\lambda$。
固定有限多项式使所有常数一致，且任意非恒定参数项都含固定小因子 $\varepsilon$。

因此：

- 若 $\mu_\lambda<m$，则辅助主项也是
  $O(|a|^{\mu_\lambda+1})$，从而
  $$
  \mathcal P(\zeta-2a;\beta-2c,\kappa)
  =
  a^{\mu_\lambda}
  \left[
  (-2)^{\mu_\lambda}d_\lambda
  +O(\theta+\varepsilon+|a|)
  \right].
  \tag{4.4}
  $$
- 若 $\mu_\lambda=m$，则
  $$
  \mathcal P(\zeta-2a;\beta-2c,\kappa)
  =
  a^m\left[
  (-2)^m d_\lambda
  -2\sum_\ell P_{y_\ell}(\lambda,s)\frac{c_\ell}{a^m}
  +O(\theta+\varepsilon+|a|)
  \right].
  \tag{4.5}
  $$

复系数的除法是 $c_\ell/a^m$，不是除以 $|a|^m$；
全部误差界按模长给出，所以无实相位假设。

当 $\mu=1$，有 $m=2$，所有根都属 (4.4)。
当 $\mu\ge2$，(4.5) 恰好只发生在最大重根。
先由非零 $d_\lambda$ 及 (1.4) 选择固定小 $\theta$，
再选固定小 $\varepsilon$，最后选固定小 $a_0$。
于是对所有高物理位、全部实际所选参数，有
$$
\boxed{
|\mathcal P(\zeta-2a_j;\beta-2\mathbf c_j,\kappa)|
\ge c|a_j|^{\mu_\lambda}
\quad
(|\zeta-\lambda|\le\theta\delta).
}
\tag{4.6}
$$
这是整个闭盘上的估计，故 shifted polynomial 在内盘确实无根；
不是只从边界非零推内盘无根。

## 5. Hermite 逆及实际预算

准确有限差仍是
$$
\mathscr L_j(z;\beta,\kappa)
=
-2[
\mathcal P(z-2a_j;\beta-2\mathbf c_j,\kappa)
-\mathcal P(z;\beta,\kappa)].
$$
对任意所选 $r$ 元位集 $F$，令
$$
H_F(z;\beta,\kappa)
=
\prod_{j\in F}
[-2\mathcal P(z-2a_j;\beta-2\mathbf c_j,\kappa)].
$$
(4.6) 保证 $H_F^{-1}$ 在每个原根团闭盘邻域内全纯。
对同一个 $\mathcal P$ 作保全部重数的 Hermite 余式：
$$
\mathcal R_F(z;\beta,\kappa)=
\frac{1}{2\pi i}\sum_{\lambda\in\Lambda}
\int_{\Gamma_\lambda}
H_F(\zeta;\beta,\kappa)^{-1}
\frac{\mathcal P(\zeta;\beta,\kappa)
-\mathcal P(z;\beta,\kappa)}
{(\zeta-z)\mathcal P(\zeta;\beta,\kappa)}
\,d\zeta.
$$
它是次数小于 $p$ 的多项式，全纯依赖同一个参数元组，且
$$
\mathcal R_F\prod_{j\in F}\mathscr L_j
=1+\mathcal P\mathcal S_F.
\tag{5.1}
$$
由 (3.2)、(4.6) 和圆周长度 $O(\delta)$，
$$
|[z^k]\mathcal R_F|
\le C^{r+1}\delta^{-\mu r-\mu+1}.
\tag{5.2}
$$
安全地以 $p$ 代替 $\mu$ 也足够。
一次使用 (2.6)，再代入同一有界 $X_M$，得真正的核内逆
$$
\mathfrak R_F=\mathcal R_F(X_M;Z|_M,K|_M),\qquad
\left(\prod_{j\in F}\mathscr L_j(X;Z,K)\right)
\mathfrak R_F=I_M,
$$
$$
\log^+\|\mathfrak R_F\|
\le K(E_N+L_N^{4/3}+N^2)+K_PrL_N+K_M.
\tag{5.3}
$$
非共振仅改变固定常数；没有 $(\max|a_j|/\min|a_j|)^r$ 成本。

## 6. 原 Haar 域与平均闭合

为明确新参数权没有绕过原域约束，列出后半段实际接口。

取 R268/R270 的位集：幅度前 $N$ 项删除幅度前 $N/4$ 项及物理前 $N/4$ 位，
留下 $Q_N=\lfloor N/2\rfloor$ 个实际位；令
$r=\lceil\sqrt{N/c}\rceil$。
则
$$
\min I_N\ge\lfloor N/4\rfloor,\quad
\delta\le|a_j|\le 2\|a\|_2/\sqrt N,\quad
\sup_{F\subset I_N,\ |F|=r}\sum_F|a_j|<\infty.
$$
由 $m\ge2$，
$$
\sum_F|c_{\ell j}|
\le C_\ell(\max_{I_N}|a_j|)^{m-1}\sum_F|a_j|\longrightarrow0.
$$
所有混合行的总增量也一致有界。
(1.4) 及固定小 $a_0$ 最终同时成立。

基本实际 gauge 误差依旧由 R260 的任意跨度局部壳给
$$
\|\delta_X^s(\gamma_F B-\widehat B_F)\|
\le s!\epsilon_N,\qquad
\epsilon_N\le C e^{-385\,16^{\lfloor N/4\rfloor-1}},
$$
其中 $B$ 遍历 $X$、全部 $Z_\ell,K_\nu$。
每个有界误差保 $\mathcal D_\infty$；
主变量自然词仍至多 $pr$ 阶，辅助字母都是有界字母。
因此原 R270 的实际正规排序和反射 jets 预算逐项不变。

多模式 Boolean 恒等式也逐字不变：
$$
4a_j\partial_z\mathcal P+
4\sum_\ell c_{\ell j}\partial_{\beta_\ell}\mathcal P+
\sum_\nu4L_{|\nu|}'(1)
a_j^{\nu_0}\prod_\ell c_{\ell j}^{\nu_\ell}
\partial_{\kappa_\nu}\mathcal P
=\mathscr L_j.
$$
先在同一个 $M$ 内用 (5.1) 消去完整有限差乘积，随后才作用左反射，
于是 R270 的实际 $T^r$ 公式和平方窗口 WOT 极限成立。

逆像平均 $\mathcal V_N$ 满足
$$
T^r\mathcal V_N f\rightharpoonup e^{-1/c}f,
$$
$$
\log A_N\le
K(E_N+L_N^{4/3}+N^2)+K_PrL_N+O(r)+K_M.
$$
有限低头删除仍给 $T-T_{\rm tail}=A W_h(X_{\ge h})$、
$\deg W_h\le p-1$；
含辅助的尾参数只是有界交换系数，不是有限头替代物。
故固定局部测试 $D_0$ 的实际交换子上界仍为
$$
\|(\operatorname{ad}_T^rD_0)\mathcal V_N f\|
\le
2\|D_0\|A_N C_{h,M,c}^r
e^{-(5/6)r^4+105r^3}\|f\|.
$$
一次选固定小 $c$，由 (1.1) 支付
$K_0c^2+K_1c^{3/2}<1/4$。
最高交换子配对与局部不可约性迫 $M=0$。
R176 的 $C_0$ 自伴及图循环随后给 (1.5)。

## 7. 显式边界例子

### 7.1 二次主模式与同阶辅助

取任何满足 (1.1) 的主行，固定 $\vartheta\in\mathbb C$，
定义
$$
v_\vartheta
=
-\vartheta\sum_j a_j^2
+
\vartheta\sum_j a_j^2\chi_j.
$$
因为 $a\in\ell^2$，两个和都绝对收敛，
辅助中心准确为 $s=0$。

对
$$
P(z,y)=z^2+y
$$
有 $q_0(z)=z^2$、$\mu=m=2$、$d_0=1$、$P_y=1$。
非共振式恰为
$$
4-2\vartheta\ne0.
$$
故
$$
\boxed{
\left[
u^2+\vartheta\sum_ja_j^2(\chi_j-1)
\right]e^w
\text{ 循环，若 }\vartheta\ne2.
}
\tag{7.1}
$$
这覆盖与主模式完全重叠的同阶平方辅助；
$\vartheta$ 无需小。

当 $\vartheta=2$ 时，零参数处的准确有限平移满足
$$
P(-2a_j,-2c_j)=4a_j^2-4a_j^2=0.
$$
所以该附录的 Hermite 逆机制在这个值确实失去根团分离。
这里只记录机制边界，不声称实际向量不循环。

### 7.2 高次数但简单中心根

设 $q$ 为任意具有简单根的首一多项式，
$$
P(z,y)=q(z)+y.
$$
令 $v$ 的系数满足 $|c_j|\le C|a_j|^2$，
并调整 $c_*=-\sum_jc_j$，使 $s=0$。
此时 $q_0=q$，$\mu=1$、$m=2$，
不需要任何额外非共振条件。
所以
$$
(q(u)+v)e^w
$$
循环，即使 $q$ 的次数远大于 2。

### 7.3 任意同阶常比向量

若 $\mu\ge2$ 且 $c_{\ell j}=\vartheta_\ell a_j^\mu$，
通过辅助常数保持指定 $s$，
则需排除的只是
$$
2\sum_\ell P_{y_\ell}(\lambda,s)\vartheta_\ell
=
(-2)^\mu\,q_0^{(\mu)}(\lambda)/\mu!
\quad(\mu_\lambda=\mu).
$$
若某个根的全部 $P_{y_\ell}(\lambda,s)=0$，
对应方程根本无解，因为右端非零；
该根自动满足非共振。

## 8. 范围

本附录降低的是辅助幅度要求并关闭明确的同阶非共振族。
它仍使用同一熵受控主模式，有限个辅助模式以及主变量首一性。
它没有从部分小参数核排除推出任意参数核排除，
没有假定未知 $M$ 对点乘保持不变，
也没有把 $\vartheta=2$ 的机制失效误称为反例。
