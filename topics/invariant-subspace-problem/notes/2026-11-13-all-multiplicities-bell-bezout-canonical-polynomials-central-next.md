# 高位 Bell 有限差、真 Bézout 输入与规范任意重数多项式核排除

日期：2026-11-13（UTC）。独占作者：central_next；AI-assisted，GPT-6 Astra Pro。
状态：已证明；根会话已独立全文核验，normal_next 另核真实进位、自然域与弱平均关键段。
分阶真实累积量预解预算由根会话独立稿
[分阶阶乘幂界与联合预解预算](../results/R236-appendix-factorial-cumulant-powers-and-joint-resolvent-budgets.md) 给出，本作者已全文逐式复核。
以下证明任意固定重数，不通过简单根逼近，不使用非交换 companion 的反射幂。

## 1. 定理及实际输入

固定原 Haar 模型及
$$
a_j=\frac{(-1)^j}{j+1},\qquad a_*=0,\qquad
u=\sum_{j\ge0}a_j\chi_j .
$$
令
$$
w=c_*+\sum_{j\ge0}b_j\chi_j,\quad b\in\ell^2(\mathbb C),\quad
t_j=e^{-2b_j},\quad R_j=V(t_jN_j).
$$
R176 的真实倾斜 first 为
$$
X=X_b=X_a+\sum_ja_j(R_j-V_j),\qquad
\operatorname{Dom}X=\operatorname{Dom}X_a.
$$
任意 Acal 元素保持其完整域，并与 X 域交换。
有限柱是其真实图核心。
定义固定有限个实际累积量
$$
G_n=\sum_{j\ge0}a_j^n L_n(R_j),\quad
L_n(v)=\left.\frac{d^n}{dt^n}\log(\cosh t+v\sinh t)\right|_{t=0},
\quad 2\le n\le p .
\tag{1.1}
$$
每个 G_n 在 Acal 中、字符为零，且是实际有界拟幂零元。

设 q 是任意非零标量多项式。除去非零首系数，可设 q 首一，次数为 p≥2。
常数、一次情形已由 R16/R147 覆盖。
引入有限 Bell 多项式
$$
\mathcal P(z;\kappa)
=\exp\left(\sum_{n=2}^p\frac{\kappa_n}{n!}\partial_z^n\right)q(z).
\tag{1.2}
$$
指数作用于次数 p 的多项式，故实际上是有限和。
它对 z 首一、次数 p，对各 kappa_n 是多项式，
且 $\mathcal P(z;0)=q(z)$。
R176 的实际闭实现为
$$
T=P(X):=\mathcal P(X;G_2,\ldots,G_p),
\qquad \operatorname{Dom}T=\operatorname{Dom}X^p.
\tag{1.3}
$$
它在该准确域闭且 C 自伴。若 M=kerT，则 R176 给
$$
M\subseteq\bigcap_{k\ge0}\operatorname{Dom}X^k,\qquad
X_M:=X|_M\in B(M).
\tag{1.4}
$$
所有 Acal 元素及 X 都保持 M。

**定理（已证明）。**
$$
\boxed{\ker T=0,\qquad q(u)e^w\text{ 对实际 }A\text{ 循环}.}
\tag{1.5}
$$
q 允许任意有限重数，特别包含
$(z-1)^2(z+1)$ 与 $(z^2-1)^2$。
证明完成的是这一规范单模式的全部点态多项式及任意 first 指数权；
一般普通 Hilbert ISP 仍未完成。

## 2. 独立实际预解预算及其使用方式

根会话分阶预解稿已证明：对每个固定 n≥2，有 K_n,D_n>0，
$$
\|G_n^k\|\le K_n\frac{D_n^k}{(k!)^{n-1}},\qquad
\|(z-G_n)^{-1}\|
\le\frac{K_n}{|z|}
 \exp\!\left((n-1)(D_n/|z|)^{1/(n-1)}\right).
\tag{2.1}
$$
该证明使用原 L² 函数非负锥的实际正主控，
保留所有低头与高尾 carry，并覆盖任意固定复 b。

因此，固定 epsilon>0 后，对于 0<delta≤1，
若 F 在多圆盘
$$
|\kappa_n|\le\varepsilon\delta^n,\qquad 2\le n\le p
\tag{2.2}
$$
的邻域全纯，边界上 |F|≤M_F，则
$$
\boxed{
\|F(G_2,\ldots,G_p)\|
\le K M_F\exp(C_\varepsilon\delta^{-2}).
}
\tag{2.3}
$$
常数与 delta、F 无关。
这来自各坐标真实 Cauchy 积分，因
n/(n−1)≤2。
后面将一次求值整个位集合的逆，而不将各个位的预解成本相乘。

## 3. Bell 线性反射系数是准确的有限平移差

由定义，
$$
\left.\frac{\partial}{\partial v}
\log(\cosh t+v\sinh t)\right|_{v=1}
=\frac{1-e^{-2t}}2.
$$
所以对 n≥1，
$$
\boxed{4L_n'(1)=-2(-2)^n.}
\tag{3.1}
$$
同时 (1.2) 给
$$
\partial_{\kappa_n}\mathcal P
=\frac1{n!}\partial_z^n\mathcal P .
\tag{3.2}
$$

给定一个非零系数 a，若把某个平方为零的形式变量 x 所对应的位反射，
则真实有理式模 x² 给
$$
V(-tx)-V(tx)=4tx,
$$
$$
L_n(V(-tx))-L_n(V(tx))=4tL_n'(1)x.
$$
因此 Bell 多项式在该位的一次项恰为 tx 乘
$$
\begin{aligned}
\mathscr L_a(z;\kappa)
&=4a\,\partial_z\mathcal P
 +\sum_{n=2}^p4L_n'(1)a^n\partial_{\kappa_n}\mathcal P\\
&=-2\,[\mathcal P(z-2a;\kappa)-\mathcal P(z;\kappa)].
\end{aligned}
\tag{3.3}
$$
这是完整有限 Taylor 恒等式，没有略去高阶累积量。
在模 mathcal P 的商中，
$$
\mathscr L_a(z;\kappa)\equiv-2\mathcal P(z-2a;\kappa).
\tag{3.4}
$$
这条准确式子允许在未知重根核上对线性主项作真正的 Bézout 逆。

## 4. 小 Bell 多圆盘上的根团与真实逆余式

设 q 的不同根为 lambda_1,...,lambda_s，
重数为 mu_1,...,mu_s，总和为 p。
固定 theta=1/4。
存在 delta_0>0、epsilon>0 及只依赖 q 的正常数，使以下对
0<delta≤delta_0 与
$$
|\kappa_n|\le2\varepsilon\delta^n
\tag{4.1}
$$
成立。

### 4.1 根团保持各自重数

mathcal P−q 的每个 Bell 系数 beta_k 对变量 kappa_n 的权重为 n，
故在 (4.1) 上，k≥2 时
$$
|\beta_k(\kappa)|\le C_p\varepsilon\delta^k
\tag{4.2}
$$
（减小 epsilon≤1 后）。在
$|z-\lambda_\nu|=\theta\delta$ 上，
$q^{(k)}(z)=O(\delta^{\max(\mu_\nu-k,0)})$。
因此
$$
|\mathcal P(z;\kappa)-q(z)|
\le C_q\varepsilon\delta^{\mu_\nu},
$$
而 $|q(z)|\ge c_q\delta^{\mu_\nu}$。
固定足够小的 epsilon，Rouché 给每个圆
$$
\Gamma_\nu(\delta)=
\{|z-\lambda_\nu|=\theta\delta\}
$$
内恰有 mu_nu 个根，并在圆上有
$$
|\mathcal P(z;\kappa)|\ge c_q\delta^{\mu_\nu}.
\tag{4.3}
$$
圆互不相交且总重数已是 p，所以没有遗漏其它根。
不要求根能逐个全纯选取。

### 4.2 所有小非零平移都避开这些根团

取任意有限 F 及系数 a_j 满足
$$
\delta\le|a_j|\le2\delta\qquad(j\in F).
\tag{4.4}
$$
将 delta_0 再减小。
若 z 在第 nu 个闭圆盘内，mathcal P(z−2a_j;kappa) 的同团根
与 z 的距离至少
$$
2|a_j|-2\theta\delta\ge\frac32|a_j|.
$$
不同团则由 q 的固定最小根距控制。
于是
$$
|\mathcal P(z-2a_j;\kappa)|
\ge c_q|a_j|^{\mu_\nu}
\ge c_q\delta^{\mu_\nu}
\tag{4.5}
$$
于这些闭圆盘上成立。
这允许 a_j 取正、负或任意复相位；只用了明确的幅度范围。

设 |F|=r，定义
$$
H_F(z;\kappa)=
\prod_{j\in F}[-2\mathcal P(z-2a_j;\kappa)],
\qquad h_F=H_F^{-1}.
\tag{4.6}
$$
h_F 在所有根团圆盘的共同邻域全纯，并在各圆上满足
$$
|h_F|\le C_q^r\delta^{-pr}.
\tag{4.7}
$$

### 4.3 不丢失重数的 Hermite 余式

定义次数小于 p 的多项式
$$
\boxed{
\mathcal R_F(z;\kappa)=
\frac1{2\pi i}\sum_{\nu=1}^s
\int_{\Gamma_\nu(\delta)}
h_F(\zeta;\kappa)
\frac{\mathcal P(\zeta;\kappa)-\mathcal P(z;\kappa)}
 {(\zeta-z)\mathcal P(\zeta;\kappa)}\,d\zeta .
}
\tag{4.8}
$$
分子除以 zeta−z 是真正的次数 p−1 多项式。
它的系数在所用圆与多圆盘上由固定 C_q 控制。
(4.3)、(4.7) 及圆长 O(delta) 给每个系数
$$
\boxed{
|[\!z^k\!]\mathcal R_F|
\le C_q^{r+1}\delta^{-pr-p+1},
\qquad 0\le k<p.
}
\tag{4.9}
$$
这些系数在 (4.1) 的邻域联合全纯。

为核对重根处的逆，不只检查根值：
对某个根团盘内的 z，Cauchy 公式把 (4.8) 写成
$$
h_F(z;\kappa)-\mathcal R_F(z;\kappa)
=\mathcal P(z;\kappa)\,J_F(z;\kappa),
$$
其中右侧 J_F 在盘内全纯。
所以 mathcal R_F 在每个根处与 h_F 的全部所需导数相同。
因此多项式 mathcal R_F H_F−1 被 mathcal P 整除。
首一多项式长除法又说明商的系数联合全纯。
由 (3.4)，最终得到真正的多项式 Bézout 恒等式
$$
\boxed{
\mathcal R_F(z;\kappa)
\prod_{j\in F}\mathscr L_{a_j}(z;\kappa)
=1+\mathcal P(z;\kappa)\mathcal S_F(z;\kappa).
}
\tag{4.10}
$$
它在全纯系数代数中成立，允许 q 和 mathcal P 均有重根。

## 5. 逆积的一次实际求值及核内输入

在 (4.8) 的系数上使用 (2.3)，取圆周
$|\kappa_n|=\varepsilon\delta^n$，
由 (4.9) 得
$$
\|[\!z^k\!]\mathcal R_F(z;G)\|
\le K C_q^{r+1}\delta^{-pr-p+1}e^{C_\varepsilon\delta^{-2}} .
\tag{5.1}
$$
这一步只付一次联合预解式，不乘 r 个 $e^{C/\delta^2}$。

以下反证假设 M=kerT 非零；由 (1.4)，令 B_M=||X_M||。
在 M 上定义有界算子
$$
\mathfrak R_F
=\mathcal R_F(X_M;G|_M):M\longrightarrow M .
\tag{5.2}
$$
它是次数小于 p 的真实 X 多项式限制。
(5.1) 给
$$
\|\mathfrak R_F\|
\le K_M C_q^{r+1}\delta^{-pr-p+1}e^{C_\varepsilon\delta^{-2}}.
\tag{5.3}
$$
因 M 在全部自然 X 幂域中，(4.10) 可以真正代入 X 并作用于 M；
系数与 X 完整交换。因此
$$
\boxed{
\left(\prod_{j\in F}\mathscr L_{a_j}(X;G)\right)
\mathfrak R_F f=f,\qquad f\in M.
}
\tag{5.4}
$$
本稿只需要核内这个有界输入；没有声称 mathfrak R_F 是全 H 上的有界算子，
也没有任意取一个闭算子的全空间逆。

## 6. 窗口、有限局部域与带权系数范数

取一个稍后固定的常数 c>0，令
$$
m=m_r=\lceil c r^2\rceil,\qquad q_r=m,\qquad
I_r=\{m,\ldots,2m-1\},\qquad \ell=2m-1,\qquad
\delta=\frac1{2m}.
\tag{6.1}
$$
充分大 r 时 m≥r、delta≤delta_0，
且对 j∈I_r，delta≤|a_j|≤2delta，故 §4 适用。

为避免与 §4 的积分余项同名，记物理反射为
$$
\mathsf J_F=\prod_{j\in F}M_{\chi_j},\quad
\gamma_F(Q)=\mathsf J_FQ\mathsf J_F,\quad
t_F=\prod_{j\in F}t_j .
$$
L=max(1,sup|t_j|,sup|t_j|⁻¹)<∞。
记真实闭尾 first
$$
Z_\ell=X-\sum_{j\le\ell}a_jR_j,\qquad
H_\ell=\sum_{j\le\ell}a_jR_j .
\tag{6.2}
$$
X 与 Z_ell 只差有界、完整交换的 Acal 元素，故
$$
\operatorname{Dom}Z_\ell^k=\operatorname{Dom}X^k
\quad(k\text{ 固定}),
$$
由有限有界交换扰动的逐域二项式归纳得到。
有限柱仍是真实图核心。

任意前 ell+1 位局部矩阵完整交换 Z_ell：
在有限柱上与尾有限截断交换，取真实核心极限，再用闭性延拓。
所以 mathsf J_F 保持全部 Z_ell 自然幂域并与之交换。
Acal 元素也完整交换 Z_ell。
后文全部反射系数都由这些元素及其有限乘积组成。

对于形式算子多项式 Q(z)=ΣQ_kz^k，
当全部 Q_k 有界且完整交换 Z_ell 时，定义
$$
\|Q\|_R=\sum_k\|Q_k\|R^k .
\tag{6.3}
$$
这是允许系数不互相交换的次乘法范数。
令
$$
R_r=1+B_M+\|H_\ell\| .
$$
因为 ||R_j|| 一致有界，
$R_r\le C_{b,M}(1+\log(m+2))$。
若 f_F=mathfrak R_F f∈M、v_F=mathsf J_F f_F，
则全部 k≥0 都有
$$
\|Z_\ell^k v_F\|
=\|Z_\ell^k f_F\|
\le R_r^k\|f_F\|.
\tag{6.4}
$$
所以任意此类多项式 Q 的实际作用满足
||Q(Z_ell)v_F||≤||Q||_(R_r)||f_F||。
这是真实深域输入，不是仅形式系数估计。

## 7. 全部 carry 后的 Boolean 主项

本节所有算子等式先取在
mathcal D_infty=cap_k DomX^k=cap_k DomZ_ell^k 上。
所有涉及的有界系数、mathsf J_F 均保持该域。

### 7.1 真实 gauge 与交换替身

令 s_j=-1 对 j∈F，其余为 1。
实际递归给
$$
\|\gamma_F(N_k)-s_kN_k\|\le
\begin{cases}
2\alpha_m/\alpha_k,&k<m,\\
2\eta_k,&m\le k\le\ell,\\
0,&k>\ell.
\end{cases}
\tag{7.1}
$$
窗口未选位也已包括。
统一真实的 (I±t_jN_j) 逆，加上固定多项式 L_n 的有限差商，给
$$
\|\gamma_F(X)-\widehat X_F\|
+\sum_{n=2}^p\|\gamma_F(G_n)-\widehat G_{n,F}\|
\le C_{p,b}\bar\eta_{m-1},
\tag{7.2}
$$
其中
$$
\widehat X_F=X+\sum_{j\in F}a_j
 [V(-t_jN_j)-V(t_jN_j)],
$$
$$
\widehat G_{n,F}=G_n+\sum_{j\in F}a_j^n
 [L_n(V(-t_jN_j))-L_n(V(t_jN_j))].
\tag{7.3}
$$
所有替身系数属于 Acal，故
$$
\widehat T_F=\mathcal P(\widehat X_F;\widehat G_F),\qquad
A_F=\widehat T_F-T
$$
作为 Z_ell 的多项式与 T 交换。
令 E_F=gamma_F(T)−widehat T_F。
各自都是同一个闭尾 Z_ell 的有界系数多项式；
其最高阶 p 系数相同，故 A_F、E_F 的次数至多 p−1。

固定 p，有限多项式相减及 (7.2) 给某个 C（可依赖 q,b,M）
$$
\|T\|_{R_r}+\|A_F\|_{R_r}
\le C(1+R_r)^p,\qquad
\|E_F\|_{R_r}\le C(1+R_r)^p\bar\eta_{m-1}.
\tag{7.4}
$$
全部系数保持 mathcal D_infty。
E_F 可能不在 Acal，但真实公共尾域已付清。

因为 gamma_F(T)v_F=0，Tv_F=−(A_F+E_F)v_F。
在有中心变量 Z_ell 的非交换系数多项式代数中，
$$
Q_0=I,\qquad Q_{k+1}=[T,Q_k]-Q_k(A_F+E_F)
$$
逐次同时给自然幂 T^kv_F=Q_kv_F。
权计数与前稿相同：系数总和≤(k+1)!，且唯一不含 E_F 的项是 (−A_F)^k。
由 (7.4) 的完整范数预算，
$$
\|T^r v_F-(-A_F)^rv_F\|
\le\bar\eta_{m-1}
 \exp(Cr\log(r+m+2))\,\|f_F\|.
\tag{7.5}
$$
这里所有固定有限阶自然幂都作用在真实 mathcal D_infty 中。

### 7.2 精确平方为零商与实际重复位误差

令 d_n=4L_n'(1)，取交换多项式
$$
\widetilde A_F=
\mathcal P\left(X+4\sum_{j\in F}a_jt_jN_j;\
 G_n+d_n\sum_{j\in F}a_j^nt_jN_j\right)
-\mathcal P(X;G).
\tag{7.6}
$$
由真实 N_j²=η_jN_(j+1) 和有理式差商，
A_F−tilde A_F 的系数范数不超过
C barη_m(1+R_r)^p。
对 r 次幂逐因子替换，这只在 (7.5) 右侧增加同型误差。

为计算 tilde A_F，先将选中 N_j 换成独立交换形式变量 x_j；
系数留在 Acal[X]，随后再真正代入。
这个多项式没有零次项，总 x 次数至多 p。
由 §3，它的一次部分准确为
$$
\sum_{j\in F}t_jx_j\mathscr L_{a_j}(X;G).
\tag{7.7}
$$
在商 x_j²=0 中，r 个正次多项式相乘、可用的变量只有 r 个：
凡有一个因子取次数≥2，或者选中某变量两次，所得单项式都为零。
因此
$$
\boxed{
\widetilde A_F^r\equiv
r!t_F\left(\prod_{j\in F}x_j\right)
 \prod_{j\in F}\mathscr L_{a_j}(X;G)
\pmod{(x_j^2:j\in F)}.
}
\tag{7.8}
$$
没有略去一个未归一化的 O(m⁻²) 项；
所有二次及更高 Boolean 项被实际重复位关系控制。

真实代入的每个弃项含某个 N_j²，
范数至多 barη_m 乘余下系数预算。
固定 p 的有限展开，其系数绝对值和在 (6.3) 的权范数下
至多 exp(Cr log(r+m+2))：
可先把每个 x_j 的绝对值置 1，使用
Σ_{j∈F}|a_j|≤r/m≤1 及 R_r=O(logm)，再对 r 次乘积取次乘法范数。
故 (7.8) 的实际误差仍被 (7.5) 的同型右侧控制。

### 7.3 把线性系数移过反射，再准确消去

记
$$
L_F(X;G)=\prod_{j\in F}\mathscr L_{a_j}(X;G),\qquad
N_F=\prod_{j\in F}N_j .
$$
用同一替身计算 gamma_F(L_F)−L_F。
除已付的 carry 外，每项含至少一个选中 N_j。
因此左乘 N_F 后都含重复位。
系数次数至多 pr、绝对系数预算仍是 exp(Cr log(r+m+2))，
由 (6.4) 可得
$$
\|N_FL_Fv_F-N_F\mathsf J_F L_F f_F\|
\le\bar\eta_{m-1}\exp(Cr\log(r+m+2))\,\|f_F\|.
\tag{7.9}
$$
使用的是
$L_F\mathsf J_F-\mathsf J_FL_F=(L_F-\gamma_F(L_F))\mathsf J_F$，
并非假定反射与 L_F 交换。

最后 (5.4) 给 L_F f_F=f。
合并 (7.5)--(7.9)，得到
$$
\boxed{
\left\|T^r\mathsf J_F\mathfrak R_Ff
-(-1)^rr!t_F N_F\mathsf J_F f\right\|
\le\bar\eta_{m-1}
e^{Cr\log(r+m+2)}\|\mathfrak R_F\|\|f\|.
}
\tag{7.10}
$$
这是真实 T 自然幂的像公式。

## 8. q≈c r² 的平均给非零弱极限

在 M 上定义有限和输入
$$
\boxed{
\mathcal V_r=
(-1)^r\left(\frac2m\right)^r
\sum_{\substack{F\subset I_r\\|F|=r}}
t_F^{-1}\mathsf J_F\mathfrak R_F.
}
\tag{8.1}
$$
它是 M→H 的有界算子，且 mathcal V_r M⊂mathcal D_infty。
由 (5.3)、binom(m,r)≤m^r/r!，
存在与 c、r、F 无关的 K>0 及固定 K_M，使
$$
\boxed{
\|\mathcal V_r\|
\le \frac{(2L)^r}{r!}\sup_F\|\mathfrak R_F\|
\le \exp\!\left(Km^2+Kr\log(m+2)+K_M\right).
}
\tag{8.2}
$$
K 可以增大到正数且仅依赖 q,b、原模型；
X_M 的范数只出现在固定 K_M 中。

原物理位满足 E_j mathsf J_j=E_j，以及
$$
\|N_F\mathsf J_F-\prod_{j\in F}E_j\|\le r\bar\eta_m.
$$
把 (7.10) 按 (8.1) 求和，得到
$$
\boxed{
\|T^r\mathcal V_rf-C_{m,m}^rf\|
\le\epsilon_r\|f\|,\qquad \epsilon_r\longrightarrow0,
}
\tag{8.3}
$$
其中
$$
C_{m,m}=\frac2m\sum_{j=m}^{2m-1}E_j .
$$
具体 carry 预算可取固定常数乘
$$
\bar\eta_{m-1}
\exp\!\left(Km^2+Cr\log(r+m+2)+K_M\right)
+2^rr\bar\eta_m.
\tag{8.4}
$$
m≈c r² 时它趋零；输入的 e^(Km²) 已包含在内。

有限提升矩阵的占据层估计给
$$
\|C_{m,m}\|\le1+1/m,\qquad
\|C_{m,m}^r\|\le(1+1/m)^r\longrightarrow1.
\tag{8.5}
$$
若 v,z 是只使用低于 m 位的有限柱向量，则
$$
\langle C_{m,m}^r v,z\rangle
=\frac{(m)_r}{m^r}\langle v,z\rangle,
$$
其中 (m)_r=m(m−1)...(m−r+1)。
因为 m=ceil(c r²)，
$$
\log\frac{(m)_r}{m^r}
=-\frac{r(r-1)}{2m}+O(r^3/m^2)
\longrightarrow-\frac1{2c}.
$$
有限柱稠密及 (8.5) 的一致界，遂给全 H 上
$$
\boxed{
C_{m,m}^r\rightharpoonup\alpha_c I,\qquad
\alpha_c=e^{-1/(2c)}>0.
}
\tag{8.6}
$$
结合 (8.3)，T^r mathcal V_r f 弱趋 alpha_c f。
这里没有误称强趋 I；为了使用小 c，恰须保留这个非零弱系数。
它对未知核向量不需要任何尾速率。

## 9. 每个固定局部矩阵的 p 阶真实交换子

固定局部矩阵 D，支撑在第 h 位以前。
令
$$
Z_h=X-\sum_{j<h}a_jR_j,\qquad
s_h=\sum_{j<h}a_j,
$$
$$
G_{n,\ge h}=\sum_{j\ge h}a_j^nL_n(R_j),\qquad
T_{\rm tail}=\mathcal P(Z_h+s_h;G_{2,\ge h},\ldots,G_{p,\ge h}).
\tag{9.1}
$$
真实闭尾 Z_h 与 D 完整交换，D 保持全部 Z_h 幂域；
尾 G 的有界系数也与 D 交换。

有限低头差有明确有界因子：
$$
X-(Z_h+s_h)=A U_{1,h},\qquad
U_{1,h}=-2\sum_{j<h}\frac{a_jt_j}{d_j}
 A^{2^j-1}(I+t_jN_j)^{-1},
$$
$$
G_n-G_{n,\ge h}=A U_{n,h},
$$
$$
U_{n,h}=-2\sum_{j<h}\frac{a_j^nt_j}{d_j}
 A^{2^j-1}(I+t_jN_j)^{-1}\widetilde L_n(R_j),
\quad L_n(v)=(v-1)\widetilde L_n(v).
\tag{9.2}
$$
所有 U 都是有限的实际 Acal 和。

把 (9.2) 代入有限多项式 mathcal P。
每个差项至少含一个 A；首一最高 z 项只产生低于 p 次的差。
所以存在次数至多 p−1 的有界 Acal 系数多项式 W_h，使
$$
\boxed{
T=T_{\rm tail}+K_h,\qquad
K_h=A W_h(Z_h),\qquad
W_h(z)=\sum_{k=0}^{p-1}B_{h,k}z^k .
}
\tag{9.3}
$$
这里 K_h 本身通常无界；只称其系数 B_(h,k) 有界。

在共同深域 mathcal D_infty 上，
D 与 T_tail 交换，K_h 与 T_tail 也交换，
因为全部 Acal 系数相互交换且完整交换 Z_h。
故逐次准确得到
$$
\operatorname{ad}_T^rD=\operatorname{ad}_{K_h}^rD
=\sum_{s=0}^r(-1)^s\binom rsK_h^{r-s}DK_h^s .
\tag{9.4}
$$
这不是在非交换 companion 中假设每若干步又出现 A；
本式的每个项明确有总共 r 个 A 因子。

确实，Z_h 完整交换 D，所以展开 W_h 幂后，
每项的真实形式为
$$
A^{r-s}B_{\rm left}\,D\,A^sB_{\rm right}\,Z_h^k,
\qquad 0\le k\le(p-1)r.
\tag{9.5}
$$
A 可与 B 系数、Z_h 交换，但未移过 D。
R109 的全幂界给
$$
\|A^{r-s}\|\,\|A^s\|
\le\exp\!\left(-\frac56r^4+105r^3\right)
\quad(0\le s\le r).
\tag{9.6}
$$

### 9.1 平均输入的真实尾 jet

对固定 h，Z_h=Z_ell+Σ_{h≤j≤ell}a_jR_j，两个加数完整交换。
由 (6.4)、mathsf J_F 与 Z_ell 交换及有限二项式，
对 f_F=mathfrak R_F f，
$$
\|Z_h^k\mathsf J_F f_F\|
\le \big(C_{h,b,M}(1+\log(m+2))\big)^k\|f_F\|.
\tag{9.7}
$$
这对所有固定整数 k 成立；后面只用 k≤(p−1)r。
取 rho_r=C_(h,b,M)(1+log(m+2))≥1，定义
$$
A_r=\frac{(2L)^r}{r!}\sup_F\|\mathfrak R_F\|.
$$
由 (8.1)，
$$
\|Z_h^k\mathcal V_rf\|\le A_r\rho_r^k\|f\|.
\tag{9.8}
$$

把 (9.5)--(9.8) 与
$B_h(\rho)=\sum_k\|B_{h,k}\|\rho^k
 \le C_h(1+\rho)^{p-1}$
合并，得到完整实际估计
$$
\boxed{
\|(\operatorname{ad}_T^rD)\mathcal V_rf\|
\le
\|D\|\,A_r[2B_h(\rho_r)]^r
\exp\!\left(-\frac56r^4+105r^3\right)\|f\|.
}
\tag{9.9}
$$
所有项都作用在 mathcal D_infty 中。
没有声称 ad_T^rD 是全 H 上有界算子，也没有混淆全域与这些已付清的深域输入。

## 10. 选定同一个小 c，完整配对并排除核

(8.2) 的 K 独立于固定局部 D,h。
现在固定
$$
0<c<\min\left(1,\sqrt{\frac5{48K}}\right).
\tag{10.1}
$$
于是 m/r²→c，(9.9) 右侧的对数为
$$
-\frac56r^4+Km^2+O_{q,b,M,h,D}(r^3+r\log(m+2)),
$$
故趋于负无穷。
从而对每个固定有限局部 D，
$$
\boxed{
(\operatorname{ad}_T^rD)\mathcal V_rf\longrightarrow0
\quad(f\in M).
}
\tag{10.2}
$$

记真实双线性型 B(x,y)=<x,Cy>。
固定 f,g∈M。
mathcal V_r f 在 mathcal D_infty 中；D、T 及其全部所用嵌套交换子
都保持这个共同深域。
因此通常 Leibniz 公式在真实自然域上成立：
$$
DT^r\mathcal V_rf
=\sum_{k=0}^r(-1)^k\binom rk
 T^{r-k}(\operatorname{ad}_T^kD)\mathcal V_rf.
$$
逐次用 T 的完整 C 自伴及 Tg=0，所有 k<r 项配对为零。
所以
$$
B(DT^r\mathcal V_rf,g)
=(-1)^rB((\operatorname{ad}_T^rD)\mathcal V_rf,g).
\tag{10.3}
$$
右边由 (10.2) 趋零；
左边由 (8.3)、(8.6) 趋于 alpha_c B(Df,g)。
alpha_c>0，故
$$
\boxed{B(Df,g)=0
\quad(f,g\in M,\ D\text{ 任意有限局部矩阵}).}
\tag{10.4}
$$

原 Haar 的有限局部 *-代数不可约：
前 h 位参考向量投影强趋于常向量 1 的秩一投影；
任意与全部局部矩阵交换的正交投影因此在 1 上是 0 或 I，
局部矩阵作用于 1 又稠密，所以该投影只能是 0 或 I。
因此任何非零 f 的局部矩阵轨道线性张成稠密。
若 0≠f∈M，令 g=f，(10.4) 迫 Cf 正交于这个稠密轨道，
与 Cf≠0 矛盾。
所以 M=0，核排除完成。

## 11. 真正循环性及准确范围

R176 已付清
$$
\xi_w=e^w\in\bigcap_k\operatorname{Dom}X^k,\qquad
T\xi_w=q(u)e^w,
$$
xi_w 对 A 循环，且
$$
[q(u)e^w]_A=\overline{\operatorname{Ran}T}.
$$
T 在准确自然域 C 自伴，kerT=0 使其像稠密。
所以任意非零标量 q（允许重根）均满足 (1.5)。

本稿没有从简单根 q 的循环性取极限。
重数通过 §4 的真实 Hermite 余式及 Bézout 恒等式完整保留；
增长通过 §2 的按累积量阶数缩小的真实多圆周一次求值支付；
非交换 carry 通过 §6--7 的同一个闭尾多项式代数支付；
局部高阶配对通过 §9 的明确 A^(r−s)·D·A^s 支付。

仍未解决任意复 ell² 系数行的全部单模式多项式、
多个独立慢模式、一般有限 chaos、任意 L² 向量循环性、
一般正常湮灭者或两个边界 N=M。
完整普通 Hilbert ISP 的 README 完成标准保持不变。

