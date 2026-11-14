# 全部拉伸指数次数域与慢符号的无穷预解式分母障碍

日期：2026-11-13（UTC）。作者：normal_next；AI-assisted，GPT-6 Astra Pro。
状态：已证明。对 $S_N$、$S_Y$ 分别成立；不构造正常湮灭者，不关闭 R244 的见证专属配对域或普通 ISP。

本稿加强
[R253 第二附录](../results/R253-appendix-polynomial-degree-smooth-domain-and-finite-resolvent-denominators.md)
的多项式次数域障碍。
新增的高位孔链有显式阶乘分母，低位真实 carry 在所选物理子空间上按 $\eta_{q-1}$ 衰减。
它给出一个向量，具有所有严格次于线性指数的拉伸指数 Walsh 次数矩，却仍不属于 $\operatorname{Ran}S$。

结合
[无穷正预解式的完整逆测试](2026-11-13-positive-infinite-resolvent-inverse-tests-normal-next.md)，
所有非零规范无穷正 first 预解式积也不能写成 $SB$，其中 $B$ 甚至可以是任意有界算子。
这排除了此前尚未排除的无穷积主理想分母策略；配对域条件仍是另一个问题。

## 1. 原算子与待证域结论

仍用原 Haar 空间
$$
H=\bigotimes_{j\ge0}(\mathbb C^2,\Omega_+)
$$
及实际递归
$$
N_j=E_j+\eta_jE_j^*N_{j+1},\qquad
N_j^2=\eta_jN_{j+1},\qquad
\|N_j\|=1,\qquad
0<\eta_j\le e^{-770\,16^j},
$$
$$
E_j=e_{10}^{(j)},\qquad
Y_j=N_j(I+N_j)^{-1}.
\tag{1.1}
$$
置
$$
a_j=(j+1)^{-2},\qquad a_\Sigma=\sum_ja_j<2,
$$
$$
S_N=\sum_ja_jN_j,\qquad S_Y=\sum_ja_jY_j.
\tag{1.2}
$$
两者在原 $H$ 上都已证明单射。
下文分别对两者取 $S$，并用 $Z_j=N_j$ 或 $Y_j$ 统一记号。

令 $\mathcal N\chi_F=|F|\chi_F$。
对 $0<\beta<1$、$t>0$，定义 Hilbert 空间
$$
\mathcal G_{\beta,t}
=\operatorname{Dom}\exp\!\bigl(t(I+\mathcal N)^\beta\bigr),
\qquad
\|x\|_{\beta,t}
=\|\exp(t(I+\mathcal N)^\beta)x\|.
\tag{1.3}
$$
再令
$$
\mathcal G_{<1}
=\bigcap_{\substack{0<\beta<1\\t>0}}\mathcal G_{\beta,t}.
\tag{1.4}
$$
可以等价取可数族
$\beta_n=n/(n+1)$、$t_n=n$，$n\ge1$；
这些权对全部固定 $\beta,t$ 共尾。
以这可数范数族赋予 $\mathcal G_{<1}$ Fréchet 拓扑。

**定理 1。**
$$
\boxed{
\mathcal G_{<1}\not\subseteq\operatorname{Ran}S_N,\qquad
\mathcal G_{<1}\not\subseteq\operatorname{Ran}S_Y.
}
\tag{1.5}
$$
两式分别成立，没有额外声称同一个向量同时离开两个值域。

证明将构造同一个序列 $w_q$（对所选 $S$），使
$$
w_q\in\operatorname{Dom}e^{\mathcal N},\qquad
\|w_q\|=1,
$$
$$
\boxed{
Sw_q\longrightarrow0\quad\text{于每个固定 }\mathcal G_{\beta,t}.
}
\tag{1.6}
$$
所有实际域和随 $q$ 改变的指数权均在下文支付。

## 2. 统一于小指数权的真实算子与 Cayley 逆

对 $0\le\sigma\le1$，令
$$
H_\sigma=\operatorname{Dom}e^{\sigma\mathcal N},\qquad
\|x\|_\sigma=\|e^{\sigma\mathcal N}x\|.
\tag{2.1}
$$
在单个位 Walsh 基中，$e^{\sigma\mathcal N}$ 为
$\operatorname{diag}(1,e^\sigma)$，
所以 $E_j,E_j^*$ 的加权相似范数均不超过 $e^\sigma\le e$。

令 $\eta_*=\sup_j\eta_j\le e^{-770}$。
真实递归的完整展开为
$$
N_j=\sum_{r=j}^{\infty}
\left(\prod_{\ell=j}^{r-1}\eta_\ell\right)
E_j^*\cdots E_{r-1}^*E_r.
\tag{2.2}
$$
它在每个 $B(H_\sigma)$ 中绝对收敛，且
$$
\|N_j:H_\sigma\to H_\sigma\|
\le\frac e{1-e\eta_*}<3.
\tag{2.3}
$$
由于 $H_\sigma\hookrightarrow H$ 连续，这个加权和就是原实际 $N_j$ 的限制。
所以已经证明了 $N_j$ 保持每个所用空间。

平方关系仍在这些实际限制上成立。
因此
$$
(I+N_j)^{-1}
=(I-N_j)(I-\eta_jN_{j+1})^{-1},
$$
其中右侧第二个逆在 $B(H_\sigma)$ 中有真正收敛的 Neumann 级数。
准确的左右逆恒等式及原 $H$ 上逆的唯一性给
$$
\boxed{
\|(I+N_j)^{-1}\|_{B(H_\sigma)}
\le\frac4{1-3\eta_*}<5,\qquad
\|Y_j\|_{B(H_\sigma)}<15.
}
\tag{2.4}
$$
这不是用形式 Taylor 逆替代实际域。

还需对纯单个位的差作统一估计：
$$
\|N_j-E_j\|_{B(H_\sigma)}
\le3e\,\eta_j.
$$
由 $Y(E_j)=E_j$ 及真实有界逆差恒等式，
$$
Y_j-E_j
=(I+N_j)^{-1}(N_j-E_j)(I+E_j)^{-1}.
$$
$\|(I+E_j)^{-1}\|_\sigma=\|I-E_j\|_\sigma\le1+e<4$。
故两个模型可共同取
$$
\boxed{
\|Z_j-E_j\|_{B(H_\sigma)}\le200\eta_j,
\qquad
\|Z_j\|_{B(H_\sigma)}\le15.
}
\tag{2.5}
$$
这些常数同时适用于全部 $j$ 和 $0\le\sigma\le1$。

## 3. 填充全 1 头后，低位 carry 仍有相对加权小界

固定整数 $q\ge2$，记
$$
J_q=\{q,q+1,\ldots,2q-1\}.
$$
再取整数 $m>2q$。
令 $\mathcal W_{q,m}$ 为下列物理张量子空间：

- 位 $0,\ldots,q-1$ 固定为 $e_1$；
- 位 $J_q$ 任意；
- 位 $2q,\ldots,m-1$ 固定为 $e_1$；
- 第 $m$ 位以后的原 Haar 尾任意。

定义只作用于中间 $q$ 位的纯下降算子
$$
D_q=\sum_{j\in J_q}a_jE_j
$$
和真正实际尾
$$
U_m=\sum_{j\ge m}a_jZ_j.
\tag{3.1}
$$
由 (2.5) 及 $\sum_{j\ge m}a_j\le1/m$，
$$
\boxed{
\|U_m\|_{B(H_{\ge m,\sigma})}\le\frac{15}{m}
\qquad(0\le\sigma\le1).
}
\tag{3.2}
$$

现在估计 $S-(D_q+U_m)$ 在 $\mathcal W_{q,m}$ 上的实际作用。
先令 $W_qx=e_1^{\otimes q}\otimes x$，其中尾 $x$ 任意。
当 $j<q$，完整递归准确给
$$
N_jW_qx=
\left(\prod_{\ell=j}^{q-1}\eta_\ell\right)
e_1^{\otimes j}\otimes e_0^{\otimes(q-j)}
\otimes N_qx.
\tag{3.3}
$$
关键是 $e_0,e_1$ 的单个位加权范数相同，
均为 $\sqrt{(1+e^{2\sigma})/2}$。
因此替换头中的这些物理 1 为 0 不改变该头的加权范数因子。
由 (2.3)、(2.4)，
$$
\|N_jW_qx\|_\sigma
\le3\left(\prod_{\ell=j}^{q-1}\eta_\ell\right)\|W_qx\|_\sigma,
$$
$$
\|Y_jW_qx\|_\sigma
\le15\left(\prod_{\ell=j}^{q-1}\eta_\ell\right)\|W_qx\|_\sigma.
\tag{3.4}
$$
这里没有多付或漏掉一个随头长增长的加权嵌入常数。

对于 $q\le j<m$，使用 (2.5) 控制 $Z_j-E_j$。
当 $j\notin J_q$ 时，$E_j$ 在所填物理位 $e_1$ 上为零。
所以对每个 $x\in\mathcal W_{q,m}\cap H_\sigma$，
$$
\begin{aligned}
\|(S-D_q-U_m)x\|_\sigma
&\le
\left(15a_\Sigma\eta_{q-1}
+200a_\Sigma\eta_q\right)\|x\|_\sigma\\
&\le500\eta_{q-1}\|x\|_\sigma.
\end{aligned}
$$
即
$$
\boxed{
\|(S-D_q-U_m)x\|_\sigma
\le500\eta_{q-1}\|x\|_\sigma,
\quad x\in\mathcal W_{q,m}\cap H_\sigma.
}
\tag{3.5}
$$
这是所选子空间上的实际加权算子界。
$D_q$ 只在中间有限块中替代了纯部分；所有低位、块内及跨块真实 carry 都已计入 (3.5)。
第 $m$ 位后的尾始终保持为实际 $U_m$。

## 4. 有显式阶乘分母的高位孔链

在 $J_q$ 的物理基中，令 $e_F$ 表示：
$F\subseteq J_q$ 中的位为 $e_0$，其余位为 $e_1$。
这些 $e_0$ 位称为孔，只用于本节有限矩阵记号。
$\{e_F\}$ 是正交单位基，且 $E_j$ 删除第 $j$ 个孔。

记下降阶乘
$$
(q)_r=q(q-1)\cdots(q-r+1),\qquad (q)_0=1.
$$
定义
$$
\boxed{
h_r=\frac1{(q)_r}
\sum_{\substack{F\subseteq J_q\\|F|=r}}
\left(\prod_{j\in F}a_j^{-1}\right)e_F,
\qquad 0\le r\le q.
}
\tag{4.1}
$$
于是 $h_0$ 为该块全 1 单位向量。
对于每个 $|G|=r-1$，
$D_qh_r$ 中 $e_G$ 的系数为
$$
\frac1{(q)_r}
\sum_{j\in J_q\setminus G}
a_j\left(\prod_{\ell\in G\cup\{j\}}a_\ell^{-1}\right)
=
\frac{q-r+1}{(q)_r}
\prod_{\ell\in G}a_\ell^{-1}.
$$
因此准确有
$$
\boxed{
D_qh_0=0,\qquad
D_qh_r=h_{r-1}\quad(1\le r\le q).
}
\tag{4.2}
$$

对 $j\in J_q$，$a_j^{-1}=(j+1)^2\le4q^2$。
又 $(q)_r=r!\binom qr$，所以
$$
\|h_r\|
\le
\frac{\sqrt{\binom qr}(4q^2)^r}{(q)_r}
=
\frac{(4q^2)^r}{r!\sqrt{\binom qr}}
\le\frac{(4q^2)^r}{r!}.
\tag{4.3}
$$
特别
$$
\|h_q\|\le\frac{(4q^2)^q}{q!}.
\tag{4.4}
$$
不同 $h_r$ 属于互相正交的物理孔次数层。
本节没有使用一个随 $q$ 未控制的 Jordan 相似或无限头形式右逆。

## 5. 真实尾校正、原像下界与完整残量

将 $h_r$ 填入第 3 节的头：
$$
\widetilde h_{r,q,m}
=e_1^{\otimes q}\otimes h_r\otimes e_1^{\otimes(m-2q)}.
$$
令 $\Omega_m$ 为第 $m$ 位后的原 Haar 真空，定义
$$
u_{q,m}=
\sum_{r=0}^q(-1)^r
\widetilde h_{r,q,m}\otimes U_m^r\Omega_m.
\tag{5.1}
$$
这是 $\mathcal W_{q,m}$ 中的真正向量。
由 (3.2)，每一项属于每个 $H_\sigma$，$0\le\sigma\le1$；
因为是有限和，$u_{q,m}\in H_1$。
没有对自然无界词作任何形式代入。

不同 $r$ 的头孔次数正交，因此
$$
\|u_{q,m}\|^2
=\sum_{r=0}^q\|h_r\|^2\|U_m^r\Omega_m\|^2
\ge1.
\tag{5.2}
$$
这就是后续原像的统一非零下界；不需要各修正项趋零。

任何前 $m$ 位的有限头向量 $v$ 都有
$\|v\|_\sigma\le e^{\sigma m}\|v\|$。
故由 (3.2)、(4.3)，
$$
\boxed{
\|u_{q,m}\|_\sigma
\le e^{\sigma m}
\sum_{r=0}^q\frac{(60q^2/m)^r}{r!}
\le\exp(\sigma m+60q^2/m).
}
\tag{5.3}
$$

由 (4.2)，有限和准确望远镜：
$$
(D_q+U_m)u_{q,m}
=(-1)^q\widetilde h_{q,q,m}\otimes U_m^{q+1}\Omega_m.
\tag{5.4}
$$
(4.4) 和 $q!\ge(q/e)^q$ 给
$$
\|(D_q+U_m)u_{q,m}\|_\sigma
\le
e^{\sigma m}\frac{15}{m}
\left(\frac{60e\,q}{m}\right)^q.
$$
再用真实 carry 界 (3.5) 及 (5.3)，得到本稿的统一核心估计：
$$
\boxed{
\|Su_{q,m}\|_\sigma
\le e^{\sigma m}
\left[
\frac{15}{m}\left(\frac{60e\,q}{m}\right)^q
+500\eta_{q-1}\exp(60q^2/m)
\right],
\quad 0\le\sigma\le1.
}
\tag{5.5}
$$
等式和不等式中 $U_m$、$S$ 始终为原实际算子；
纯块只出现在已单独支付 carry 的有限链中。

## 6. 从随 q 改变的 Hσ 到每个拉伸指数次数域

对固定 $0<\beta<1$、$t>0$，令
$$
\gamma=\frac{\beta}{1-\beta},\qquad
C_{\beta,t}=(1-\beta)t(\beta t)^{\beta/(1-\beta)}.
$$
对 $x\ge0$，在 $y=x+1$ 上优化
$t y^\beta-\sigma y$，得
$$
t(x+1)^\beta-\sigma x
\le \sigma+C_{\beta,t}\sigma^{-\gamma}.
$$
所以对每个 $0<\sigma\le1$，
$$
\boxed{
\|v\|_{\beta,t}
\le
\exp\!\left(\sigma+C_{\beta,t}\sigma^{-\gamma}\right)
\|v\|_\sigma.
}
\tag{6.1}
$$
该式由 Walsh 对角权逐项比较得到，常数完全显示；
它对下文随 $q$ 改变的 $\sigma$ 同样有效。

统一选择
$$
\ell_q=\lceil\log(q+1)\rceil,\qquad
m_q=q\ell_q^2,\qquad
u_q=u_{q,m_q}.
\tag{6.2}
$$
对 $q\ge2$，$m_q>2q$。
记 (5.5) 方括号中的两个量为
$$
\Theta_q=\frac{15}{q\ell_q^2}
\left(\frac{60e}{\ell_q^2}\right)^q,\qquad
K_q=500\eta_{q-1}\exp(60q/\ell_q^2).
$$
准确的渐近预算为
$$
\log\Theta_q=-2q\log\log q+O(q),
$$
$$
\log K_q\le\log500-770\,16^{q-1}+60q/\ell_q^2.
\tag{6.3}
$$

现在只为估计某个固定 $\beta,t$ 选择
$$
\sigma_q=m_q^{-(1-\beta)}.
\tag{6.4}
$$
它处于 $(0,1]$，并有
$$
\sigma_qm_q=m_q^\beta,\qquad
\sigma_q^{-\gamma}=m_q^\beta.
$$
将 (6.4) 同时代入已经统一于全部 $\sigma$ 的 (5.5) 和 (6.1)，得到
$$
\|Su_q\|_{\beta,t}
\le
\exp\!\left(1+(1+C_{\beta,t})m_q^\beta\right)
(\Theta_q+K_q).
\tag{6.5}
$$
对每个固定 $\beta<1$，
$$
m_q^\beta=q^\beta\ell_q^{2\beta}=o(q).
$$
因此 (6.3) 的第一项仍保有负主项 $-2q\log\log q$，
第二项仍保有双指数负主项。
故
$$
\boxed{
\|Su_q\|_{\beta,t}\longrightarrow0
\quad\text{对每个固定 }0<\beta<1,\ t>0.
}
\tag{6.6}
$$
参数 $\beta,t$ 只是验证同一向量序列的不同范数；
没有按未知向量尾速率移动这两个参数。

最后令
$$
w_q=u_q/\|u_q\|.
$$
由 (5.2)，归一化只会减小 (6.6) 的残量，且 $\|w_q\|=1$。
每个 $w_q\in H_1\subset\mathcal G_{<1}$。
这证明 (1.6)。

## 7. Fréchet 闭图给同一个全部拉伸指数域见证

每个 $\mathcal G_{\beta,t}$ 是闭对角权的定义域，配其图等价范数为 Hilbert 空间。
取第 1 节的可数共尾权，
其交 $\mathcal G_{<1}$ 完备：
在全部范数中 Cauchy 的序列具有相同 $H$ 极限，
再逐权使用闭性确定各个加权极限。
所以它确实是 Fréchet 空间，且连续嵌入 $H$。

反设对所选 $S$ 有
$\mathcal G_{<1}\subseteq\operatorname{Ran}S$。
$S$ 单射，因此
$$
S^{-1}:\mathcal G_{<1}\longrightarrow H
$$
全域定义。
其图闭：输入的 Fréchet 收敛蕴含 $H$ 收敛，
而 $S$ 在 $H$ 上有界。
Fréchet 到 Banach 的闭图定理迫这个逆连续。
但 (1.6) 给
$$
Sw_q\to0\quad\text{于 }\mathcal G_{<1},\qquad
S^{-1}(Sw_q)=w_q,\qquad \|w_q\|=1,
$$
矛盾，证明 (1.5)。

因此，对每个所选 $S$，存在一个
$$
v_S\in\mathcal G_{<1}\setminus\operatorname{Ran}S.
\tag{7.1}
$$
它同时具有所有 $t>0$、$\beta<1$ 的上述次数矩。
这也立即给每个单独 $\mathcal G_{\beta,t}\not\subseteq\operatorname{Ran}S$。
这里是存在性结果，不给 $v_S$ 的闭式表达，也不由此保证它具有任何正线性指数次数矩。

## 8. 一般的有限幂型指数逆成本都不足以成为 S 的分母

下述准则把第 5–6 节变成一个可复用的有界分母障碍。

设 $R\in B(H)$，并且存在常数
$A_0>0$、$B_0\ge0$、$0<\gamma_0<\infty$，
使每个 $0<\sigma\le1$ 都有一个线性映射
$$
T_\sigma:H_\sigma\to H
$$
满足
$$
RT_\sigma x=x\quad(x\in H_\sigma),\qquad
\|T_\sigma\|\le A_0\exp(B_0\sigma^{-\gamma_0}).
\tag{8.1}
$$
不要求这些右逆在全 $H$ 有定义，也不额外要求 $R$ 单射。

**定理 2。**
$$
\boxed{
R\notin S B(H),\qquad
\operatorname{Ran}R\not\subseteq\operatorname{Ran}S.
}
\tag{8.2}
$$

证明中对同一 $u_q$ 选
$$
\sigma_q=m_q^{-1/(\gamma_0+1)},\qquad
z_q=T_{\sigma_q}Su_q.
$$
由 (5.5)、(6.3)、(8.1)，
$$
\|z_q\|
\le A_0
\exp\!\left((1+B_0)m_q^{\gamma_0/(\gamma_0+1)}\right)
(\Theta_q+K_q)\longrightarrow0.
\tag{8.3}
$$
因为固定指数 $\gamma_0/(\gamma_0+1)<1$，前面的正指数仍为 $o(q)$。
而实际右逆恒等式给 $Rz_q=Su_q$。

若 $R=SB$，$B\in B(H)$，取消单射的 $S$ 得 $Bz_q=u_q$。
这与 $z_q\to0$ 和 $\|u_q\|\ge1$ 矛盾。
若只假定 $\operatorname{Ran}R\subseteq\operatorname{Ran}S$，
则 $S^{-1}R:H\to H$ 全域且图闭，故有界；
这又给一个被排除的因子 $R=SB$。定理得证。

### 8.1 共同的平滑向量属于所有这类 R 的像

事实上，
$$
\boxed{\mathcal G_{<1}\subseteq\operatorname{Ran}R}
\tag{8.4}
$$
对每个满足 (8.1) 的 $R$ 都成立。

令 $P_n$ 在本小节专指 Walsh 次数等于 $n$ 的正交投影，
$f_n=P_nf$。
选择
$\sigma_n=(n+1)^{-1/(\gamma_0+1)}$，
并置 $\beta_0=\gamma_0/(\gamma_0+1)<1$。
则
$$
\|T_{\sigma_n}f_n\|
\le A_0
\exp\!\left((B_0+1)(n+1)^{\beta_0}\right)\|f_n\|.
$$
对 $f\in\mathcal G_{<1}$，任选 $\beta_0<\beta<1$。
Cauchy–Schwarz 和
$$
\sum_{n\ge0}
\exp\!\left(2(B_0+1)(n+1)^{\beta_0}-2(n+1)^\beta\right)<\infty
$$
表明
$\sum_nT_{\sigma_n}f_n$ 在 $H$ 中绝对收敛。
$R$ 有界且 $RT_{\sigma_n}f_n=f_n$，所以它的和为 $f$ 的一个原像。
这证明 (8.4)，不要求不同 $\sigma$ 的右逆相容。

因此第 7 节的同一个 $v_S$ 属于所有满足 (8.1) 的 $R$ 的像，
却不属于 $\operatorname{Ran}S$。
这一量词加强只在上述明确逆成本类内使用。

## 9. 非零无穷正 first 预解式积的实际应用

设
$$
Q_\nu=(I+X_{b^{(\nu)}})^{-1},\qquad
b^{(\nu)}\ge0,\quad b^{(\nu)}\in\ell^2,
\qquad c=\sum_\nu b^{(\nu)}.
$$
R230 无穷积附录给：若 $c\notin\ell^2$，则有限乘积弱趋零；
若 $c\in\ell^2$，则有限乘积强趋非零收缩 $P$。

本稿的
[前一完整逆测试稿](2026-11-13-positive-infinite-resolvent-inverse-tests-normal-next.md)
已经证明，对于 $c\in\ell^2$，
存在相容的实际逆测试 $F_\infty$，且
$$
PF_\infty x=x\quad(x\in H_\sigma,\ \sigma>0),
$$
$$
\|F_\infty:H_\sigma\to H\|
\le\sqrt2\exp(D_c/\sigma),
\qquad D_c=eC_+^2\|c\|_2^2<\infty.
\tag{9.1}
$$
该恒等式来自实际有限自然词消去及一致有界强极限，
不来自形式无穷约分；该稿也给真正 $\mathcal A$ 中的有界截断。
取 $T_\sigma=F_\infty|_{H_\sigma}$，
(9.1) 正好满足 (8.1)，其中 $\gamma_0=1$。

所以
$$
\boxed{
P\notin S_NB(H),\quad
\operatorname{Ran}P\not\subseteq\operatorname{Ran}S_N;
}
$$
$$
\boxed{
P\notin S_YB(H),\quad
\operatorname{Ran}P\not\subseteq\operatorname{Ran}S_Y.
}
\tag{9.2}
$$
这包括行的任意重叠和 $\sum_\nu\|b^{(\nu)}\|_2=\infty$ 的情况。

有限个正 first 半群及有界复杂 first 预解式的附加乘积，
在上述逆测试稿中也具有
$A\sigma^{-k/2}e^{B/\sigma}$ 的完整自然逆成本。
将有限幂因子吸收到较大的 $A'e^{B'/\sigma}$ 后，
同一个定理 2 也覆盖它们。
不据此声称一般复杂行的无穷乘积存在或满足此成本。

### 9.1 R253 尾理想分母策略的直接限制

R253 的有限 dyadic 相位乘积给
$$
I_{\mathrm{head},m}\otimes Q_m=S C_m,
\qquad C_m\in\mathcal A.
\tag{9.3}
$$
若某个非零尾空间正无穷预解式积 $P^{\mathrm{tail}}$
可以写成 $Q_mG$，其中 $G$ 在该尾空间上有界，
则
$$
I_{\mathrm{head},m}\otimes P^{\mathrm{tail}}
=S C_m(I_{\mathrm{head},m}\otimes G)\in S B(H).
$$
但左侧仍是原 Haar 模型的正无穷预解式积：
只需将各个尾系数行在前 $m$ 位补零。
这与 (9.2) 矛盾。

因此，不能把任何这类非零尾无穷积直接放进 $Q_mB(H_{\mathrm{tail}})$，
再利用其收缩强单位来给 $q_m$ 一个下界。
本结论不排其他理想测试，也不否定 $q_m$ 可能通过别的方法一致离开零。

## 10. 与 R244 的边界

本稿的全部结论针对实际值域和有界因子等式 $R=SB$。
未知因子 $B$ 从未被要求交换；
因此不能靠把右因子从 $\mathcal A$ 扩到 $\mathfrak C$ 来绕过这些障碍。

R244 的指定输入条件
$$
Rf_i\in\operatorname{Dom}X_{Cf_i}
$$
并不要求 $R\in SB(H)$。
所以 (9.2) 没有排除某个无穷预解式积对某个假想正常正湮灭见证恰好满足配对域；
也没有证明存在这样的选择。

前一逆测试稿的 R240 反例排除普遍配对正则化，
本稿排除这一整类正则器作为慢主理想的有界分母。
两者都没有构造正常湮灭者，也没有完成一般正常见证的排除或普通 ISP。
