# R270：一个熵受控主模式与无限重叠高阶小辅助模式

日期：2026-11-13（UTC）。作者：kernel；Astra-ISP-1cf8c51d 复核。
状态：已证明；原 Haar 模型的中间结论，普通 Hilbert ISP 未完成。

本文接 R268 的实际单尺度熵预算，处理真正无限支撑、与主模式在同一物理位重叠的辅助 first。辅助模式不是有限头，也没有被假设为 $A$ 的解析函数。关键是按系数幂次给全部混合累积量分配半径，并在准确的多模式有限平移差中保留辅助位移。

## 1. 主定理

取
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a\in\ell^2(\mathbb C),
$$
其非零幅度排序 $\rho_k$ 满足 R268 的单尺度熵条件：沿无穷尺度 $N$，
$$
\sup_{k\ge N}k\rho_k\le D N\rho_N,
$$
$$
E_N:=\sum_{k\le N}\log(\rho_k/\rho_N)=O(N^2),\qquad
L_N:=1+\log^+(\rho_N^{-1})=O(N^{3/2}).
\tag{1.1}
$$
特别，$\sup k\rho_k<\infty$ 加
$\liminf k^{-1}\log^+(\rho_k^{-1})<\infty$ 足够。
固定任意复指数权
$$
w=c_*+\sum_jb_j\chi_j,\qquad b\in\ell^2.
$$

设 $P(z,y_1,\ldots,y_d)$ 是关于 $z$ 首一的多项式，$z$ 次数为 $p\ge1$。
取辅助 first
$$
v_\ell=c_{\ell,*}+\sum_jc_{\ell j}\chi_j,\qquad 1\le\ell\le d,
$$
满足同物理位上的定量条件
$$
\boxed{
|c_{\ell j}|\le C_\ell |a_j|^{p+1}
\quad(j\ge0,\ 1\le\ell\le d).
}
\tag{1.2}
$$
相位任意，$a_j=0$ 时 (1.2) 要求 $c_{\ell j}=0$。

**定理。**
$$
\boxed{
P(u,v_1,\ldots,v_d)e^w
\text{ 对原实际 }A\text{ 循环}.
}
\tag{1.3}
$$
$P$ 在各变量中的根、重数和耦合任意，只保关于主变量的首一性。
它关于辅助变量的次数不受 $p$ 限制，但固定有限。

因为 $p+1\ge2$，
$$
\sum_j|c_{\ell j}|
\le C_\ell\sum_j|a_j|^{p+1}<\infty.
\tag{1.4}
$$
所以辅助 first 真正属于 $\ell^1$，其实际倾斜算子有界。
主 first 仍可无界。
辅助行可以在主行的每个非零位都非零，故这是无限重叠多模式结论。

例如取 $p=2$、$c_{1j}=a_j^3$，得到
$$
\left(u^2+\sum_ja_j^3\chi_j\right)e^w
\text{ 循环}.
\tag{1.5}
$$
§11 还把 $p\ge2$ 时的辅助条件加强到相对于 $|a_j|^p$ 的无速率小 $o$。

## 2. 全部实际混合参数及其权

置
$$
t_j=e^{-2b_j},\qquad R_j=V(t_jN_j),\qquad
X=X_b,\qquad
Y_\ell=c_{\ell,*}I+\sum_jc_{\ell j}R_j.
$$
$X$ 是 R176 的真实闭 first，$Y_\ell\in\mathcal A$ 按范数绝对收敛。
记
$$
s_\ell=c_{\ell,*}+\sum_jc_{\ell j},\qquad
Z_\ell=Y_\ell-s_\ell I
=\sum_jc_{\ell j}(R_j-I).
\tag{2.1}
$$
$Z_\ell$ 是零字符的有界 $\mathcal A$ 元素。

对多重指标 $\nu=(\nu_0,\ldots,\nu_d)$、$|\nu|\ge2$，
记
$$
a_j^{[\nu]}=a_j^{\nu_0}\prod_{\ell=1}^d c_{\ell j}^{\nu_\ell},
\qquad
K_\nu=\sum_j a_j^{[\nu]}L_{|\nu|}(R_j),
$$
$$
L_n(v)=
\left.\frac{d^n}{dt^n}\log(\cosh t+v\sinh t)\right|_{t=0}.
\tag{2.2}
$$
只保留对固定 $P$ 有贡献的有限多重指标集：
可取 $\nu_i$ 不超过 $P$ 在对应变量中的次数，且 $|\nu|\ge2$。
超出这个集合的微分恒为零。

令
$$
\omega=p+1,\qquad
m_\nu=\nu_0+\omega\sum_{\ell\ge1}\nu_\ell.
\tag{2.3}
$$
由 (1.2)，
$$
|a_j^{[\nu]}|\le C_\nu|a_j|^{m_\nu}.
\tag{2.4}
$$
纯主模式 $\nu=(n,0,\ldots,0)$ 的权为 $m_\nu=n\ge2$；
其余混合参数的权至少 $\omega>p$。
辅助中心变量 $Z_\ell$ 分配权 $\omega$。
所有这些系数行都在 $\ell^1$，故 (2.2) 是真实范数和。
它们的字符为零，因为 $L_{|\nu|}(1)=0$。

定义有限的标量参数多项式
$$
\mathcal P(z;\beta,\kappa)
=
\left[
\exp\left(\sum_\nu
\frac{\kappa_\nu}{\nu!}\partial_{z,y}^{\,\nu}\right)
P(z,y)
\right]_{y=s+\beta}.
\tag{2.5}
$$
它关于 $z$ 仍首一、次数 $p$：
主最高项 $z^p$ 不含辅助变量，任何非恒定微分都不能改变这个最高系数。

实际算子是
$$
T=\mathcal P(X;Z,K).
\tag{2.6}
$$
这是有界 $\mathcal A$ 系数的首一 $X$ 多项式。

## 3. 真实点态混合 Bell 恒等式和自然域

对有限参数 $\tau=(\tau_0,\ldots,\tau_d)$，每个位的线性组合为
$$
\ell_j(\tau)=a_j\tau_0+\sum_{\ell\ge1}c_{\ell j}\tau_\ell.
$$
有限截断中，准确的不同位倾斜恒等式给
$$
e^{\tau_0u+\sum_{\ell\ge1}\tau_\ell v_\ell+w}
=
\exp\left(
\sum_{|\nu|\ge2}\frac{K_\nu}{\nu!}\tau^\nu
\right)
e^{\tau_0X+\sum_{\ell\ge1}\tau_\ell Y_\ell}e^w
\tag{3.1}
$$
到所需的有限 Taylor 阶数。
这里的多重阶乘来自
$\ell_j(\tau)^n/n!=\sum_{|\nu|=n}a_j^{[\nu]}\tau^\nu/\nu!$。

R145/R176 的有限截断强极限、伴随图核心和倾斜幂域保证 (3.1) 的每个所需 jet 都是真实 $H$ 向量。
$Y_\ell$ 有界并与 $X$ 完整域交换，因此所有混合词需要的主变量域仅为对应的 $X$ 自然幂域。
不将全空间的无界指数解释为有界算子。

对 (3.1) 应用 $P(\partial_\tau)$ 后取零，得到
$$
\boxed{
T e^w=P(u,v_1,\ldots,v_d)e^w.
}
\tag{3.2}
$$
该等式包含全部重叠混合累积量，未把点态乘积换成算子乘积。

R176 §2、§4、§5、§8 以及倾斜 §10.1 明确允许任意有界交换系数和可逆最高系数。
故
$$
\operatorname{Dom}T=\operatorname{Dom}X^p,\qquad
T\text{ 闭且 }T=C_0T^*C_0.
\tag{3.3}
$$
若 $M=\ker T$，则
$$
\boxed{
M\subseteq\mathcal D_\infty
:=\bigcap_{k\ge0}\operatorname{Dom}X^k,\qquad
X_M\in B(M).
}
\tag{3.4}
$$
全部实际参数和 $X$ 保持同一个 $M$。
$e^w$ 还是 $T$ 的图循环基向量，最终
$[Te^w]_A=\overline{\operatorname{Ran}T}$。

## 4. 幂次主控的实际熵预解引理

需要 R268 熵引理的一个直接但重要的扩展。

**引理。** 设 $H$ 为固定多项式、$H(1)=0$，且
$$
S=\sum_jd_jH(R_j),\qquad
|d_j|\le C|a_j|^m,\quad m\ge2.
\tag{4.1}
$$
这里 $d_j$ 是本引理的标量系数，与原归一化常数无关。
在 R268 的尺度 $N$、$\delta=\rho_N$ 上，
对 $|\lambda|=\varepsilon\delta^m$，
$$
\boxed{
\|\lambda(\lambda-S)^{-1}\|
\le K\exp[C'(E_N+L_N^{4/3}+N^2)].
}
\tag{4.2}
$$

证明：对固定 $H$ 构造与 R268 相同的非负 Taylor 有理主控
$W(N_j)$，使 $|H(R_j)f|\le W(N_j)|f|$。
用 $C|a_j|^m$ 代替 $|d_j|$ 得到真实函数正锥主控。
实际局部平方关系及物理低头 $AU_h$ 给
$$
\|e^{zS}\|
\le K\exp[C(1+\log(2+|z|))^{4/3}]
\prod_k(1+c|z|\rho_k^m).
\tag{4.3}
$$
所有 carry、有限低位逆和原四次幂成本照 R268 §3 支付；
只改变固定多项式与标量幂次。

在真实 Laplace 左右逆中令 $|z|=s/(\varepsilon\delta^m)$。
前 $N$ 个标量因子不超过
$e^{mE_N}(1+Cs)^N$；
尾部由 $k\rho_k\le DN\delta$ 不超过
$\exp(CN s^{1/m})$。
物理低头另付
$\exp[C L_N^{4/3}+C(\log(2+s))^{4/3}]$。
积分的 $e^{-s}$ 吸收后，仅余
$O(N\log N)+O(N^{m/(m-1)})$。
$m\ge2$ 保证不超过 $O(N^2)$。
这证明 (4.2)，且覆盖所有复方向。
它没有将函数锥正性误作 Hilbert 自伴正性。

将本引理用于 $Z_\ell$ 的 $H(v)=v-1$、权 $\omega$，
以及每个 $K_\nu$ 的 $H=L_{|\nu|}$、权 $m_\nu$。
这些有限个参数在同一个交换代数内。
所以在共同圆周
$$
|\beta_\ell|=\varepsilon\delta^\omega,\qquad
|\kappa_\nu|=\varepsilon\delta^{m_\nu},
\tag{4.4}
$$
上，任意在闭多圆盘邻域全纯、边界模长 $\le M_F$ 的系数函数满足
$$
\boxed{
\|F(Z,K)\|
\le K M_F
\exp[C(E_N+L_N^{4/3}+N^2)].
}
\tag{4.5}
$$
有限多个坐标只改变固定常数，所有圆周一次共同求值。

## 5. 原根团与辅助位移的严格分离

令
$$
q_0(z)=P(z,s_1,\ldots,s_d),
$$
它首一、次数 $p$。
将纯主模式参数记为
$\kappa_n=\kappa_{(n,0,\ldots,0)}$，并定义基准
$$
\mathcal P_0(z;\kappa_{\rm pure})
=\exp\left(\sum_{n=2}^p
\kappa_n\partial_z^n/n!\right)q_0(z).
$$
当所有含辅助的参数及 $\beta$ 为零，(2.5) 就是这个基准。

固定足够小的 $\varepsilon$。
在扩大一倍的 (4.4) 多圆盘内，纯参数给 R266 的根团位移 $O(\delta)$；
每个额外项至少含一个权 $\ge\omega=p+1$ 的参数，
故在固定根邻域中有
$$
|\mathcal P-\mathcal P_0|
\le C\varepsilon\delta^{p+1}.
\tag{5.1}
$$
因此 $\mathcal P$ 的各根团仍位于
$|z-\lambda_\mu|<\delta/8$，并保持原重数 $\mu\le p$。
在 $\Gamma_\mu=\{|z-\lambda_\mu|=\delta/4\}$ 上，
$|\mathcal P|\ge c\delta^p$。

对一个选中位 $j$，记
$\mathbf c_j=(c_{1j},\ldots,c_{dj})$。
需要的准确有限差是
$$
\mathscr L_j(z;\beta,\kappa)
=-2[
\mathcal P(z-2a_j;\beta-2\mathbf c_j,\kappa)
-\mathcal P(z;\beta,\kappa)].
\tag{5.2}
$$
辅助位移不能省略。

设 $\delta\le|a_j|\le a_0$。
对 $\zeta\in\Gamma_\mu$，纯基准的根团分离给
$$
|\mathcal P_0(\zeta-2a_j;\kappa_{\rm pure})|
\ge c_\mu|a_j|^\mu.
\tag{5.3}
$$
不同原根团由固定根距隔开，同一团距 $2|a_j|$。
另一方面，(1.2) 与固定有限多项式给
$$
|\mathcal P(\zeta-2a_j;\beta-2\mathbf c_j,\kappa)
-\mathcal P_0(\zeta-2a_j;\kappa_{\rm pure})|
\le C(\varepsilon\delta^{p+1}+|a_j|^{p+1})
\le C'|a_j|^{p+1}.
$$
由于 $\mu\le p$，选择固定小 $a_0$ 后，该误差小于 (5.3) 的一半。
所以
$$
\boxed{
|\mathcal P(\zeta-2a_j;\beta-2\mathbf c_j,\kappa)|
\ge c|a_j|^\mu\ge c'\delta^p.
}
\tag{5.4}
$$
全部复相位允许；没有使用最大/最小幅度比。

## 6. 保全部重数的混合有限差逆

设 $F$ 有 $r$ 个选中位，置
$$
H_F(z;\beta,\kappa)
=\prod_{j\in F}
[-2\mathcal P(z-2a_j;\beta-2\mathbf c_j,\kappa)].
$$
(5.3)--(5.4) 的同一几何距离下界对整个闭盘 $|\zeta-\lambda_\mu|\le\delta/4$ 都成立：原团内根位移小于 $\delta/8$，而 $2|a_j|\ge2\delta$；跨团根距保持固定正值。辅助扰动在该闭盘仍小于主下界的一半。因此每个平移因子在闭盘及稍大邻域都无零点，$H_F^{-1}$ 在原根团圈内部及邻域全纯。
用真正 Hermite 余式
$$
\mathcal R_F(z;\beta,\kappa)
=\frac1{2\pi i}\sum_\mu\int_{\Gamma_\mu}
H_F(\zeta;\beta,\kappa)^{-1}
\frac{\mathcal P(\zeta;\beta,\kappa)
-\mathcal P(z;\beta,\kappa)}
{(\zeta-z)\mathcal P(\zeta;\beta,\kappa)}\,d\zeta
$$
得到次数小于 $p$ 的多项式，保留全部根重数，满足
$$
\mathcal R_F\prod_{j\in F}\mathscr L_j
=1+\mathcal P\mathcal S_F,
$$
$$
|[z^k]\mathcal R_F|
\le C^{r+1}\delta^{-pr-p+1}.
\tag{6.1}
$$
这是在原参数 $(\beta,\kappa)$ 上的全纯恒等式；
各 $j$ 的辅助位移只是已知标量，并未产生不同的求值元组。

对各系数一次使用 (4.5)，在同一 $M$ 上令
$$
\mathfrak R_F
=\mathcal R_F(X_M;Z|_M,K|_M).
$$
有
$$
\boxed{
\left(\prod_{j\in F}\mathscr L_j(X;Z,K)\right)
\mathfrak R_Ff=f,\quad f\in M,
}
\tag{6.2}
$$
$$
\boxed{
\log^+\|\mathfrak R_F\|
\le K(E_N+L_N^{4/3}+N^2)+K_PrL_N+K_M.
}
\tag{6.3}
$$
最高系数首一及次数小于 $p$ 的代入，使 $B_M$ 只进入固定 $K_M$。

## 7. 任意跨度的真实域误差

采用 R268 的实际位集：前 $N$ 幅度删除前 $N/4$ 排名和前 $N/4$ 物理位，
取 $Q_N=\lfloor N/2\rfloor$ 个剩余位组成 $I_N$，
$r=\lceil\sqrt{N/c}\rceil$。
于是
$$
\min I_N\ge m_N:=\lfloor N/4\rfloor,\qquad
\rho_N\le|a_j|\le2\|a\|_2/\sqrt N,
$$
所有 $r$ 元 $F$ 的 $\sum_F|a_j|$ 一致有界。
因此
$$
\sum_{j\in F}|c_{\ell j}|
\le C_\ell(\max_{I_N}|a_j|)^p\sum_{j\in F}|a_j|\to0,
$$
混合参数的选中增量也一致有界并趋零。
§5 的固定小 $a_0$ 条件最终满足。

令 $\gamma_F=\operatorname{Ad}J_F$。
用反转 $N_j\mapsto-N_j$ 定义所有带帽变量：
主 $X$、每个 $Y_\ell$ 和每个 $K_\nu$ 都只在 $j\in F$ 的局部函数中改用 $V(-t_jN_j)$。
中心 $s_\ell$ 保持原固定值，故
$\widehat Z_\ell=\widehat Y_\ell-s_\ell I$。

R260 的局部壳证明对任意固定多项式 $H(R_j)$ 和任意 $\ell^2$ 系数行适用。
这里所有混合系数行都由 (2.4) 属于 $\ell^2$。
按真实 $\delta_X=[X,\cdot]$ 定义，对全部阶数 $s$ 有
$$
\boxed{
\|\delta_X^s(\gamma_FX-\widehat X)\|
+\sum_\ell\|\delta_X^s(\gamma_FZ_\ell-\widehat Z_\ell)\|
+\sum_\nu\|\delta_X^s(\gamma_FK_\nu-\widehat K_\nu)\|
\le s!\epsilon_N,
}
$$
$$
\epsilon_N\le C e^{-385\,16^{m_N-1}}.
\tag{7.1}
$$
每个基本误差及全部导数保 $\mathcal D_\infty$，没有最大物理位成本。

R268 的实际正规排序引理再次适用：
含至多 $pr$ 个 $X$ 字母和 $O_P(r)$ 个有界字母、
且含一个基本误差的词，在核内输入 $f_F\in M$ 上的总成本
$\le\epsilon_N e^{C r\log(r+2)}\|f_F\|$。
高阶辅助次数只增加固定数量的有界字母，不增加主 first 的最高次数 $p$。

反射输入的 jets 仍由主变量一式
$X^kJ_Ff_F=J_F(\gamma_FX)^kf_F$ 支付。
对每个固定物理头 $h$，存在固定 $R_{h,M,c}$ 使
$$
\|X_{\ge h}^kJ_Ff_F\|
\le2R_{h,M,c}^k\|f_F\|,
\qquad k\le2pr.
\tag{7.2}
$$
辅助变量有界且完整交换，不需要给它们另立无界域。

## 8. 多模式 Boolean 线性项的精确恒等式

令 $\widehat T_F$ 为所有带帽变量代入 (2.5)，
$A_F=\widehat T_F-T$。
在同一 $M$ 上，$A_F$ 有界并保持 $M$，
虽然在全 $H$ 上通常是低于 $p$ 阶的无界多项式。

用实际 $N_j^2=\eta_jN_{j+1}$，
其 Boolean 替身的增量为
$$
\Delta X=4\sum_{j\in F}a_jt_jN_j,\qquad
\Delta Z_\ell=4\sum_{j\in F}c_{\ell j}t_jN_j,
$$
$$
\Delta K_\nu
=4L_{|\nu|}'(1)\sum_{j\in F}a_j^{[\nu]}t_jN_j.
\tag{8.1}
$$
所有有理余项真含 $N_j^2$，限制到 $M$ 后总范数为
$O(\eta_{m_N})$；原始系数绝对和由 §7 的选中总量控制。

(2.5) 的微分满足
$$
\partial_{\kappa_\nu}\mathcal P
=\frac1{\nu!}\partial_{z,\beta}^{\,\nu}\mathcal P.
$$
对每个总阶 $n\ge2$，
$4L_n'(1)=-2(-2)^n$。
加入主 first 和辅助 first 的一次项 $4a_j\partial_z$、
$4c_{\ell j}\partial_{\beta_\ell}$，有限多变量 Taylor 公式准确给
$$
4a_j\partial_z\mathcal P+
4\sum_\ell c_{\ell j}\partial_{\beta_\ell}\mathcal P+
\sum_\nu4L_{|\nu|}'(1)a_j^{[\nu]}
\partial_{\kappa_\nu}\mathcal P
=\mathscr L_j.
\tag{8.2}
$$
因此每个位的 Boolean 一次项为
$t_jN_j\mathscr L_j(X;Z,K)$。
这里正是 (5.2) 的完整辅助位移，未忽略它。

$r$ 个正次因子且只有 $r$ 个选中变量，所以
$$
A_F^r
=r!t_FN_F\prod_{j\in F}\mathscr L_j(X;Z,K)
+\text{实际重复位余项}
\quad\text{于 }M,
\tag{8.3}
$$
重复位余项及有理替换成本 $\le C^r\eta_{m_N}$。
所有系数在 $M$ 上交换，保留完整真实 carry。

定义 $f_F=\mathfrak R_Ff\in M$。
在原共同深域上
$$
T^rJ_Ff_F=J_F(\gamma_FT)^rf_F.
$$
(7.1) 的正规排序成本允许换成 $J_F\widehat T_F^rf_F$；
$Tf_F=0$ 和交换性使其等于 $J_FA_F^rf_F$。
先在 $M$ 内用 (6.2) 消去整个有限差乘积，
再以 $J_jE_j=-E_j$ 得
$$
\boxed{
T^rJ_F\mathfrak R_Ff
=(-1)^rr!t_F\prod_{j\in F}E_jf+\mathcal E_Ff,
}
\tag{8.4}
$$
其中第一部分误差
$\le\epsilon_N e^{Cr\log(r+2)}
\|\mathfrak R_F\|\|f\|$，
另有 $r!|t_F|r\eta_{m_N}\|f\|$。
这是真正的自然幂恒等式与界，不是形式多项式计算。

## 9. 弱平均及局部四次交换子

设
$$
\mathcal V_N=(-1)^r(2/Q_N)^r
\sum_{\substack{F\subset I_N\\|F|=r}}
t_F^{-1}J_F\mathfrak R_F:M\to H.
$$
如 R268，绝对系数上界 $A_N$ 满足
$$
\log A_N\le
K(E_N+L_N^{4/3}+N^2)+K_PrL_N+O(r)+K_M.
\tag{9.1}
$$
(8.4) 的总 carry 误差趋零，
而平方窗口纯平均给
$$
\boxed{
T^r\mathcal V_Nf\rightharpoonup e^{-1/c}f
\quad(f\in M).
}
\tag{9.2}
$$
这是全 $H$ 一致有界纯平均导出的固定弱极限；
没有使用未知核向量的尾速率。

固定前 $h$ 位的局部矩阵 $D_0$。
对主 first、辅助中心变量和全部混合累积量，
删除有限低头后的差都含明确有界 $A$ 因子：
$$
R_j-I=A\left[-2t_jd_j^{-1}A^{2^j-1}(I+t_jN_j)^{-1}\right],
$$
且 $L_n(1)=0$ 给每个混合项同类因子。
这里 $d_j$ 恢复为原归一化常数。
所有实际尾与 $D_0$ 完整交换。定义尾表达式时保留被删除低头的全部标量字符；只有有限低头的零字符余项被提取为 $A$ 因子。

因为 $P$ 关于主变量首一，有限多项式相减给
$$
T=T_{\rm tail}+A W_h(X_{\ge h}),\qquad
\deg W_h\le p-1,
\tag{9.3}
$$
其系数有界、属于 $\mathcal A$。
辅助尾虽无限，但只是这些有界系数的一部分；
没有被删除或视为有限头。

原 $A$ 的四次幂界及 (7.2) 的真实主变量 jets 给
$$
\|(\operatorname{ad}_T^rD_0)\mathcal V_Nf\|
\le2\|D_0\|A_N C_{h,M,c}^r
e^{-(5/6)r^4+105r^3}\|f\|.
$$
(1.1)、$N/r^2\to c$ 使
$r^{-4}\log A_N$ 的上极限至多
$K_0c^2+K_1c^{3/2}$。
选择固定小 $c$ 使此和小于 $1/4$，该选择独立于所有固定局部测试。
于是上式趋零。

对 $f,g\in M$，
真实自然域及完整 $C_0$ 自伴性给最高交换子配对
$$
\mathcal B(D_0T^r\mathcal V_Nf,g)
=(-1)^r\mathcal B((\operatorname{ad}_T^rD_0)\mathcal V_Nf,g).
$$
由 (9.2)，得到
$\mathcal B(D_0f,g)=0$
对所有固定局部全矩阵成立。
其不可约性迫 $M=0$。

$C_0$ 自伴性给 $T$ 像稠密；
(3.2) 和 R176 图循环判据遂证明 (1.3)。

## 10. 正确的适用范围与一个具体新族

主行可以是任意相位、任意物理重排的
$$
|a_j|=\frac1{j+1},
\quad
|a_j|\asymp\frac1{(j+1)(\log(j+2))^\beta},
\quad
|a_j|\asymp e^{-\gamma(j+1)^\alpha},\quad0<\alpha\le1,
$$
以及 R268 的更一般熵行和超指数阶梯行。
在重排时 (1.2) 始终是对应实际位上的关系，不将辅助系数独立重排后仍假设它成立。

例如给任何一个满足 (1.1) 的 $a$，取
$$
v=a_*'+\sum_j\theta_j a_j^3\chi_j,\qquad
\sup_j|\theta_j|<\infty.
$$
则任意关于 $z$ 首一的二次式
$$
P(z,y)=z^2+F(y)z+G(y)
$$
（$F,G$ 任意固定标量多项式）满足 $P(u,v)e^w$ 循环。
$\theta_j$ 可任意复相位，辅助支持可以与主支持完全相同。
这不是有限头多模式，也不要求 $v$ 对应一个解析 $A$ 系数。

该论证不能免费用于辅助量仅与主量同阶的情形。
在一个 $p$ 重根旁，主有限平移大小为 $|a_j|^p$，
同阶辅助平移可能准确取消它。
下一节给出的可放宽范围明确保留这个非取消条件。

## 11. $p\ge2$ 时的临界小 $o$ 加强

当 $p\ge2$ 时，可把 (1.2) 换成
$$
c_{\ell j}=0\quad(a_j=0),\qquad
\sup_{a_j\ne0}\frac{|c_{\ell j}|}{|a_j|^p}<\infty,
$$
$$
\boxed{
\max_{1\le\ell\le d}
\frac{|c_{\ell j}|}{|a_j|^p}\longrightarrow0
\quad(j\to\infty,\ a_j\ne0).
}
\tag{11.1}
$$
不要求这个小 $o$ 有定量速率。

证明只需在 §2、§4 把辅助权 $\omega$ 改为 $p$。
仍有 $m_\nu\ge2$，所以每个实际熵预解仍只付 $O(N^2)$。
原多圆盘的辅助扰动为 $O(\varepsilon\delta^p)$，
选择固定小 $\varepsilon$ 仍保持全部根团。

在选中位上，令
$\epsilon_N'=\max_{\ell,j\in I_N}|c_{\ell j}|/|a_j|^p$。
因为 $\min I_N\to\infty$，$\epsilon_N'\to0$。
§5 的辅助位移误差现在为
$$
C(\varepsilon+\epsilon_N')|a_j|^p
\le C(\varepsilon+\epsilon_N')|a_j|^\mu,\qquad \mu\le p,
$$
其中充分大 $N$ 已有 $|a_j|\le1$。
先取 $\varepsilon$ 小，再令 $N$ 大，便小于 (5.3) 的一半。
所有 Hermite、Boolean 和 carry 步骤保持原准确恒等式；
小 $o$ 只用于这个固定比例的根团分离，不乘 $C^r$，
所以不需要额外速率。

辅助 $\ell^1$ 性由
$|c_{\ell j}|\le C|a_j|^p$、$p\ge2$ 得到。
其余自然域和预算完全不变，故 (1.3) 在 (11.1) 下成立。
例如二次主模式允许
$c_j=a_j^2/\log(j+2)$，
即使不存在统一 $\varepsilon>0$ 使
$|c_j|=O(|a_j|^{2+\varepsilon})$。

$p=1$ 不采用 (11.1)：其一般小 $o$ 不自动保证辅助 $\ell^1$，
也不能把权1参数放进 §4 的 $m\ge2$ 预解引理。
该情形仍按主定理的 $|c_j|\le C|a_j|^2$ 处理。

## 12. 尚未覆盖之处

本稿关闭的是一个熵受控主模式加若干逐位高阶小的无限辅助模式。
没有声称一般同阶独立慢模式都满足根团分离，
没有删除混合累积量，
没有把主 first 的全部自然幂域替换为有限 chaos 域，
也没有将全空间预解界外推成未知限制的下界。

规则 $1<\alpha\le3/2$ 主行的全部重数、一般无界弱 $\ell^1$ 常数、
正常湮灭者、实际边界 $N=M$ 与完整普通 ISP 仍开放。

## 依赖

R145 的混合 Bell jets；R176 任意有界交换系数的首一自然域和图循环；
R260 任意物理跨度的完整导子壳；
R266 非同幅 Hermite；
R268 实际正锥熵预算、自然词、反射 jets 与平方弱平均；
R109 原四次幂界。
