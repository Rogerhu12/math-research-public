# 首剩余低 Johnson 通道的共同 Schur 与原尾线性外采样预算

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core。

**状态：本文的条件恒等式、出生二的准确 Poincaré 型等价式及原连续尾的条件协方差双侧预算均已证明。** 最后一项只支付同一条件线性采样的协方差，不支付随 $D$ 变化的条件均值，也不是原 graph 或加强 S1 的上界。本文继续[相位支付稿](2026-11-14-source-orthogonality-parity-payment-and-intersection-polynomials-789f-next.md)的同一个完整源，不删实际 $q$ 或 $\ell$。

## 1. 两切片共同代表

沿用 R296 和相位支付稿，$s\ge2$，$k=s+n$，$1\le n\le M-2s$。原物理源仍是同一个 $f\in K_s(d)$。令
$$
p^\sharp(I)=p(I)-(|I|-k)g(I).
$$
它在第 $k-1,k$ 切片分别等于真实残差 $\mathcal R_{k-1,s}f,\mathcal R_{k,s}f$，并且
$$
\mathsf Z_nf=p^\sharp-\ell\quad (|I|=k+1),\qquad
\ell=\Pi_{\le s-2}^{(k+1)}p^\sharp.
\tag{1.1}
$$
两个前层都正交全部 $\le s-1$ 次特征。将 Boolean 乘积多线性化后，可以准确写成
$$
p^\sharp=\Phi_s(a)-\Phi_{s-1}(q).
\tag{1.2}
$$
这里 $a,q$ 是这个共同代表的完整系数；$a$ 已含 $g$ 的贡献，不能再把 $a_J$ 当成原 primitive 系数 $f_J/b_J$。

对不交 $A,D$，$|A|=k-r$、$|D|=2r$，局部无权删除记作 $\partial_D$，$P_j^D$ 是 $\ker\partial_D\cap\mathcal H_j(D)$ 的物理正交投影。所有条件分拆均使用原权 $z_A^2z_D$。

## 2. 任意出生的首剩余负行对外部交集是线性的

相位 $\varepsilon=(-1)^{s-1}$ 已把全部负项降到 $j\le s-2$。取首剩余通道
$$
j=s-2,\qquad r\ge s-1,\qquad t=r-s+2\ge1.
$$
对 $|L|=s-1,L\subset D$ 定义 $(a_{D,i})_L=a_{L\cup\{i\}}$，其中 $i\notin D$；$a_D,q_D,\ell_D$ 分别是相应完整系数对 $D$ 的限制。于是局部 $s-1$ 次系数为
$$
(p^\sharp_A)_{s-1}=\sum_{i\in A}a_{D,i}-q_D,
\qquad (p^\sharp_A)_s=a_D.
$$
完整 Johnson 分解给
$$
H_j^{p^\sharp}(u)
=a_{j,j}+(u-j)a_{j,j+1}+\binom{u-j}{2}a_{j,j+2},
$$
$$
a_{j,j+1}=\frac{P_j^D\partial_D(p^\sharp_A)_{s-1}}{2t},\qquad
a_{j,j+2}=\frac{P_j^D\partial_D^2a_D}{(2t)(2t-1)}.
$$
因此首负通道的真实向量准确为
$$
\begin{aligned}
V_D(A)&=H_j^\ell-2\partial_uH_j^{p^\sharp}(r)\\
&=P_j^D\left[\ell_D+\frac1t\partial_Dq_D
-\frac1{2t}\partial_D^2a_D\right]
-\frac1t\sum_{i\in A}P_j^D\partial_Da_{D,i}.
\end{aligned}
\tag{2.1}
$$
所有投影和系数均属于同一个 $D$。定义同源算子列
$$
v_0=P_j^D\left[\ell_D+t^{-1}\partial_Dq_D-(2t)^{-1}\partial_D^2a_D\right],
\qquad v_i=-t^{-1}P_j^D\partial_Da_{D,i},
\tag{2.2}
$$
就有 $V_D(A)=v_0+\sum_{i\in A}v_i$。系数可理解为原 $f$ 的线性算子；下文的 Gram 不先固定某个独立试探向量。

固定 $D$ 后，外部交集的准确条件分布为
$$
\nu_D(A)=\frac{w_A}{e_a(w)},\qquad
a=k-r,\quad w_i=z_i^2\ (i\notin D),\quad |A|=a.
\tag{2.3}
$$
若 $a=0$，该分布退化于空集。若 $a\ge1$，令 $\pi_i=\mathbb E_{\nu_D}\mathbf1_{i\in A}$、$\Sigma_D=\operatorname{Cov}_{\nu_D}(\mathbf1_A)$。直接展开得到完整共同 Schur：
$$
\boxed{\mathbb E_{\nu_D}V_D(A)^*V_D(A)
=\bar V_D^*\bar V_D+\sum_{i,l\notin D}(\Sigma_D)_{il}v_i^*v_l,\qquad
\bar V_D=v_0+\sum_i\pi_i v_i.}
\tag{2.4}
$$
于是该通道的总负费用是
$$
-\sum_{r\ge s-1}c_{r,s-2}\tau_{r,s-2}
\sum_{|D|=2r}z_De_{k-r}(z_{D^c}^2)
\left(\bar V_D^*\bar V_D+\sum_{i,l}(\Sigma_D)_{il}v_i^*v_l\right).
\tag{2.5}
$$
$r=s-2$ 的相邻硬端为零，不在这个和中。这里没有删去 $\bar V_D$，也没有把不同 $i$ 的逆源费用分别相加。

## 3. 出生二时的完整 Poincaré 型等价式

现在专取 $s=2$。写
$$
p^\sharp(x)=\sum_{i<l}a_{il}x_ix_l-\sum_iq_ix_i,
\qquad a_{il}=a_{li},\quad a_{ii}=0.
\tag{3.1}
$$
$\ell$ 是真实第 $k+1$ 切片上的常数投影。给一个占据向量
$$
y=2\mathbf1_A+\mathbf1_D,\qquad |D|=2r\ge2,
$$
定义同一个向量
$$
h_D(y)=\left(\frac12 ay-q\right)_D,\qquad
P_D=I_D-\frac1{2r}\mathbf1_D\mathbf1_D^*,\qquad
u(y)=\frac1r\mathbf1_D^*h_D(y).
\tag{3.2}
$$
令 $\delta=\mathbf1_I-\mathbf1_J$；它只支撑于 $D$。对中央对子，$\sum_D\delta_i=0$；对按第 $k-1,k+1$ 层排序的相邻对子，$\sum_D\delta_i=-2$。二次多项式差准确为
$$
p^\sharp(I)-p^\sharp(J)=\delta^*h_D(y).
\tag{3.3}
$$
所以中央统计量是 $\delta^*h_D$，相邻统计量是 $\delta^*h_D+\ell$。

均匀平衡分拆的条件协方差为
$$
\operatorname{Cov}(\delta\mid y,\text{中央})=\frac{2r}{2r-1}P_D,
$$
$$
\mathbb E(\delta\mid y,\text{相邻})=-\frac1r\mathbf1_D,\qquad
\operatorname{Cov}(\delta\mid y,\text{相邻})
=\frac{2(r^2-1)}{r(2r-1)}P_D.
\tag{3.4}
$$
这些系数由单个位的均值／方差及固定总和直接确定，包含 $r=1$ 的零协方差端点。相邻与中央分拆数之比是 $r/(r+1)$。因此条件平方差完整等于
$$
\boxed{\binom{2r}{r}
\left[\frac2{2r-1}\|P_Dh_D(y)\|^2
-\frac r{r+1}|\ell-u(y)|^2\right].}
\tag{3.5}
$$
这保留整个 $j=1$ 正通道及整个 $j=0$ 负通道；$j=2$ 在所选反对称相位下为零。$r=0$ 的中央统计量同样为零。

令 $Q$ 为独立 $I_-\sim\mu_{k-1}$、$I_+\sim\mu_{k+1}$ 的占据 $y=\mathbf1_{I_-}+\mathbf1_{I_+}$ 分布。它的准确质量是
$$
Q(A,D)=\frac{\binom{2r}{r-1}z_A^2z_D}{e_{k-1}e_{k+1}}.
\tag{3.6}
$$
由 $p^\sharp$ 在第 $k-1$ 层均值零、$p^\sharp-\ell$ 在第 $k+1$ 层均值零，以及 (3.3)—(3.4)，
$$
\boxed{\ell=\mathbb E_Q u.}
\tag{3.7}
$$
这是实际投影常数，不是为使右式好看另选的参数。将 (3.5) 求和，得到
$$
\boxed{\frac{\langle\mathcal A_{2,n}f,f\rangle}{e_{k-1}e_{k+1}}
=\mathbb E_Q\frac{2(r+1)}{r(2r-1)}\|P_Dh_D(y)\|^2
-\operatorname{Var}_Q u(y).}
\tag{3.8}
$$
因而出生二的算术步骤准确等价于 (3.8) 右侧这个 Poincaré 型预算。本文没有证明该预算；它对任意权也不能无条件为真，临界强池加趋零尾时原 $C_1$ 可以退化，而 $e_{k+1}C_0$ 不退化。

固定 $D$ 时，同一个 $h_D$ 是
$$
h_D(y)=c_D+\sum_{i\in A}a_{D,i},\qquad
c_D=\frac12a_{DD}\mathbf1_D-q_D.
\tag{3.9}
$$
所以 (3.8) 的正项和负项共享 (2.3) 的同一个完整线性协方差。不能先独立估 $P_Dh_D$ 与 $\mathbf1_D^*h_D$ 再声称这仍是其共同 Schur。

## 4. 任意固定删位后的原连续平方行

以下给 (2.4)、(3.9) 的外部线性采样一个真实预算。设原尾重新编号为
$$
j\ge x\ge2,\qquad z_j=j^{-4},\qquad w_j=z_j^2=j^{-8}.
$$
删除一个任意有限集合 $D$，$d=|D|$，剩余指标从小到大为 $t_1<t_2<\cdots$。对其初等对称和记 $E_l=e_l(w_{D^c})$，删去额外任一剩余指标 $i$ 后记 $E_l^i$。则
$$
\boxed{\frac{E_l}{R_l}\le E_l^i\le E_l,
\quad R_0=1,\quad R_l=\left(\frac{x+l+d}{x}\right)^8\ (l\ge1).}
\tag{4.1}
$$

**证明。** 先删去首个剩余指标。把任意 $l$ 元集 $\{t_{j_1},\ldots,t_{j_l}\}$ 送到 $\{t_{j_1+1},\ldots,t_{j_l+1}\}$，这是到避开首位的所有 $l$ 元集的双射。各间隔 $[t_{j_a},t_{j_a+1}]$ 不交，长度之和至多 $l+d$，因为每个间隔只多使用原来删除的 $D$ 中指标。若这些长度依次为 $c_a$，其左端至少是 $x+\sum_{b<a}c_b$，所以
$$
\prod_a\frac{t_{j_a+1}}{t_{j_a}}
\le\prod_a\frac{x+\sum_{b\le a}c_b}{x+\sum_{b<a}c_b}
\le\frac{x+l+d}{x}.
$$
取八次幂并对正项求和得到首位删除界。删去其他任一位后，剩余递减权逐项不小于删去首位后的权，故同一界成立。$l=0$ 为恒等式。

这个证明允许 $D$ 有任意大位置和任意间隙；没有把删位后的行误当成连续行。

## 5. 条件线性 Gram 的双侧合同预算

取 (2.3) 的 $a\ge1$，令
$$
\lambda_a=\frac{E_{a-1}}{E_a},\qquad W=\sum_{i\notin D}w_i,
\qquad \bar v=W^{-1}\sum_iw_iv_i,
$$
$$
\mathcal V_D=\sum_iw_i(v_i-\bar v)^*(v_i-\bar v).
\tag{5.1}
$$
全部 $v_i$ 仍是同一原源上的算子列。R294 的已完整证明的协方差结论给
$$
\Sigma_D\succeq\operatorname{diag}(\eta)-\frac{\eta\eta^*}{\sum_i\eta_i},
\qquad \eta_i=(\Sigma_D)_{ii}=\frac{w_iE_{a-1}^iE_a^i}{E_a^2}.
\tag{5.2}
$$
此外固定秩的负相关给 $\Sigma_D$ 是非负边权 Laplacian，故
$\Sigma_D\preceq2\operatorname{diag}(\eta)$。其核包含常数，因而对任意标量列 $c_i$，
$$
\inf_t\sum_i\eta_i|c_i-t|^2
\le c^*\Sigma_Dc
\le2\inf_t\sum_i\eta_i|c_i-t|^2.
\tag{5.3}
$$
式 (4.1) 给逐坐标的真实界
$$
\frac{\lambda_a}{R_{a-1}R_a}w_i\le\eta_i\le\lambda_aw_i.
$$
对同一个 $t$ 比较再取下确界，随后对同源算子列作合同，得到
$$
\boxed{\frac{\lambda_a}{R_{a-1}R_a}\mathcal V_D
\preceq\sum_{i,l}(\Sigma_D)_{il}v_i^*v_l
\preceq2\lambda_a\mathcal V_D.}
\tag{5.4}
$$
这是联合平方和，不是 $\sum_i$ 个独立最小原像界。若 $d=2r$、$a=k-r$，其两个标量系数的比至多
$$
\boxed{2R_{a-1}R_a\le2\left(1+\frac{k+r}{x}\right)^{16}
\le2\left(1+\frac{2k}{x}\right)^{16}.}
\tag{5.5}
$$
$a=0$ 时条件协方差准确为零，不使用 $E_{a-1}$。

公式 (5.4) 同样适用于 (3.9) 的整列 $a_{D,i}$，然后同时保留 $P_D$ 行和 $\mathbf1_D^*/r$ 行；不能从单独的对角行估计推断它们之间的 Schur 补。

无限行的证明可先对有限截断应用 (5.2)—(5.3)，再用正级数收敛及固定次数的 Cauchy–Schwarz 取极限。这里 $\sum w_i<\infty$；对本文由固定物理源生成的列，$\sum_iw_i\|v_if\|^2<\infty$。例如最高系数含 $a_{L\cup\{i\}}$，其中 $w_i|a_{L\cup\{i\}}|^2$ 只比原物理平方系数多一个有界的 $z_i$ 因子；共同代表的低次修正同理。先在稠密有限源上核对，再按这些界延拓，保留真正同源域。

## 6. 已付部分与实际剩余

式 (2.4) 将第一剩余负行准确拆为条件均值和条件协方差；(5.4) 对原连续尾支付后者与显式加权共同平方和的双侧比较。它没有支付 $\bar V_D^*\bar V_D$，也没有证明 $\mathcal V_D$ 被已知正 Johnson 通道支配。

出生二时 $\ell$ 的常数方向已经由 (3.7) 完整中心化，但 (3.8) 中随整个占据 $y$ 变化的方差仍待与同一个 $P_Dh_D$ 比较。原连续尾的 $(5.5)$ 仅是这个条件线性采样的比较常数；它不是 $\kappa_s$，也不能乘到仅知趋零的 graph 锚上当作收尾。
