# R119 续篇：真实三径源、四径状态与1734阶 jet 逆

2026-11-15，visible-exact / tail_connector。

**状态：下述真实三径源到四径状态的有损逆已证明。** 本篇在原 fixed-$t$ 变量中逐次使用完整两行方程，支付 ordinary 源的三个径向导数到状态的四个径向导数。不把未知源拉到 mixed root 图，不要求第五个 profile 导数。全部导数是原真实有限分片上的单侧普通导数。原子、jump 和 weak 端荷仍是原有序 source 数据，不能从 ordinary norm 推断不存在的 bare trace。

主结论把 N 的1730角阶 source 损失变成 jet 窗的1734阶，背景最高相应是 $s+1796$，故最高 $s=6396$。本篇不消去真实 reduced derivative 的 residual 缺陷，也不把有限 jet 域自动称作已经完成的 smoothing 迭代。

## 1. 原单位和明确的 jet 空间

采用 [完整二层网络](R119-supplement-two-level-full-network-tame-inverse-and-complete-sources.md) N，及其原 I/T/C/O/M/G 依赖。内部胞元仍为
$$
 \ell_j=2^{-64}J_j^{-2}\delta_j^4,\qquad
 c_j=\frac{\mu_jp_*^2}{12r^{10}},\qquad
 C_j=2^{200}h_j^{-5}\frac{\zeta_j}{\mu_j\delta_j^2},
 \qquad r_t=r .
 \tag{J.1}
$$
$\mu_j$ 是胞元尺度，不是 physical density。当前背景完整 residual 写成 $\mathfrak r=N/c_j$，避免和物理 $r$ 混名。

对真实高度方向 $h$，置
$$
 p=\frac{h_\theta}{a_{\rm ph}w},\quad
 k=\frac{h_t}{a_{\rm ph}w},\quad
 Z_h=(p,k,p_\theta,k_\theta),\qquad a_{\rm ph}=\rho r .
$$
定义
$$
 \mathscr X_s(h)=\sup_j C_j^{-1}
   \max_{0\le a\le4}\ell_j^a
       \sup_{I_j}\|\partial_t^aZ_h\|_{H^s}.
 \tag{J.2}
$$
有限 connector 另加同一区间、$\ell_o=2^{-1024}$、四态单位 $2^{-440}$ 的项。$\mathscr X_s$ 不含任意重置的高度常数；height gauge 按原全局积分保留。

源使用 C 的完整定义
$$
 \mathscr N_s^{[3]}(g)=\sup_j(\zeta_j\delta_j^{16})^{-1}
   \max_{0\le a\le3}\ell_j^a
        \sup_{I_j}\|\partial_t^ag\|_{H^s}.
 \tag{J.3}
$$
mean 与非mean都在其中。有限 connector 先以它自己的准确 ordinary-to-two-row 转换得到 $e_o$，再计
$2^{440}\max_{a\le3}\ell_o^a\|\partial_t^ae_o\|_{H^s}$。
这保留原有限源单位，不用内部 (J.1) 的 $c_j$。

将这一有限普通源项及原完整端口、jump、weak source 合同记入 $\mathfrak B_q^{[3]}$。端口部分仍是原 $\mathfrak B_q$，不向离散端荷强行索取 $t$ 导数。令
$$
 \mathfrak d_q^{[3]}
   =\mathscr N_{q+2}^{[3]}(g)+\mathfrak B_q^{[3]}(d_{\rm ext}).
 \tag{J.4}
$$
测度/BV 源只对其实际一侧 ordinary 部分用 (J.3)，不将 jump 的分布导数塞进普通 supremum。

背景满足 N.1 的低球与高阶有限条件，本文需要至 $\mathscr R_{s+1796}$，不另要求它小。若要求四态及其一阶迹连续，源的一侧迹还须满足原方程的对应兼容；broken-jet bound 本身不会制造这项兼容。

## 2. 完整两行与准确递推

O 的真实非线性函数是
$$
 \mathcal F=
 \frac{Q(2K+U+K^2+KU+qP^2)+(1+q)(V-P)^2}
      {1+K+(1+q)U},
 \qquad q=w^2,\quad Q=-A .
 \tag{J.5}
$$
$U=P_\theta,V=K_\theta$，$K$ 含真正 holonomy mean。仍置
$$
 \alpha=J^{-1}+3q(1+K)/D,\qquad
 \beta=(1+q)/J,\qquad
 \gamma=3q(1+K)d/D .
$$
固定 metric 的 proxy 方程 $c_j\mathcal J_Wh=g$ 精确等于
$$
 \begin{aligned}
 p_t&=k_\theta-(A+1)p,\\
 k_t&=\mathcal F_Up_\theta+\mathcal F_Vk_\theta
 +(\mathcal F_P+\beta\mathfrak r_\theta+\gamma\mathfrak r)p
 +(\mathcal F_K-\alpha\mathfrak r)k+g/c_j .
 \end{aligned}
 \tag{J.6}
$$
三个 residual 号直接来自
$\mathcal J=\mathcal L+\alpha\mathfrak r k-\beta\mathfrak r_\theta p-\gamma\mathfrak r p$。首行没有新源，不暂用 $K_t=\mathcal F$。

记 $u=(p,k)^T$，
$$
 M=\begin{pmatrix}0&1\\\mathcal F_U&\mathcal F_V\end{pmatrix},
 \quad
 B=\begin{pmatrix}
 -(A+1)&0\\
 \mathcal F_P+\beta\mathfrak r_\theta+\gamma\mathfrak r&
                              \mathcal F_K-\alpha\mathfrak r
 \end{pmatrix},
 \quad e=(0,g/c_j)^T .
$$
每一片内 $\ell_j$ 是常数。令 $u_a=\ell_j^a\partial_t^au$，则
$$
 \boxed{\quad
 u_{a+1}=\sum_{b=0}^a{a\choose b}
 \left[(\ell_j^{b+1}\partial_t^bM)\partial_\theta u_{a-b}
       +(\ell_j^{b+1}\partial_t^bB)u_{a-b}\right]
       +\ell_j^{a+1}\partial_t^ae,\qquad0\le a\le3 .
 \quad}
 \tag{J.7}
$$
再取一次 $\theta$ 导就是四态递推。source 最高只有 $\partial_t^3(g/c_j)$，背景 residual 最高是 $\partial_t^3\mathfrak r_\theta$。没有第四个 source 径向导，没有微分 $\sqrt Q$，也没有在根 $Q=0$ 除以 $Q$。

先对局部光滑解证明。只要递推右端范数有限，逐阶在分布中定义导数，就得到相应普通一侧代表；不先假设 $\mathscr X_s$ 有限再循环估计。

## 3. scalar 和系数的全部 scaled 费用

C.4–C.7 从同一个 $w=\mu_jp_*/r^7$ 给
$$
 (\log c_j)_t=2A+4,\qquad
 \max_{a\le3}\ell_j^a
     \|\partial_t^a(g/c_j)\|_{H^s}
 <2^{-170}h_j^5C_j\delta_j^{16}\mathscr N_s^{[3]}(g).
 \tag{J.8}
$$
这是对任意 ordinary $g$ 的完整 Leibniz 恒等式，不要求 $g$ 是背景 residual。$c_j^{-1}$ 前三阶 Bell 导数及二项式总费小于4；完整 mean 也使用同一个 scalar。

原 B.4 输入为
$$
 |Q|\le2^{12}J\delta^{-3/2},\quad
 |Q_t|\le2^{18}J\delta^{-3},\quad
 |Q_{tt}|\le2^{26}J\delta^{-9/2},\quad
 |Q_{ttt}|\le2^{40}J\delta^{-6}.
 \tag{J.9}
$$
故 $\ell_j^{a+1}Q^{(a)}$、$a\le3$ 均统一有界且很小。$q_t=2Aq$ 的重复导数同理。有限 connector 使用 B.31 的同一参考 coefficients 与 $\ell_o$，有限 scalar 费用可宽取 $2^{4096}$；这只用已知 radial profile，不把未知场解析延拓到旧条带。

非径向背景按 C.10–13 的真实递推，每个 $t$ 导只添一个角导或 $\mathfrak r,\mathfrak r_t,\mathfrak r_{tt},\mathfrak r_{ttt}$，并先乘相同 $\ell_j$。$J,D,1-qP^2$ 的低正下界不变。用 N.5/L.18 的 one-high 完整几何与二项式级数，而非高范数小门，可得 $b\le3$ 时
$$
 \begin{split}
 \|\ell_j^{b+1}\partial_t^bM\|_{H^{s+1}}
 +\|\ell_j^{b+1}\partial_t^bB\|_{H^{s+1}}
 \le C_{\rm rad,b}+2^{262144}C_j^\#(1+\mathscr R_{s+b+5}),
 \quad C_{\rm rad,b}\le2^{4096}.
 \end{split}
 \tag{J.10}
$$
相乘时最高方向只收低 coefficient norm；高 $\mathscr R$ 只乘低方向。radial/reference 常数与角权交换，不反复乘高代数常数。

角阶可逐项核：$b=3$ 的 $\mathfrak r_\theta$ 只需 $\mathscr N_{s+2}^{[3]}$；其余 state 三次径向导最多添三角导，再付一次 coefficient 导和 envelope 余量，$s+b+5\le s+8$ 足够。四次有限 Leibniz/商法则至多八个 jet 因子。总导数的一高分配及 $s\le6404$ 的角系数费被262144覆盖，不调用第五 profile 导数。

## 4. 零阶状态到四个径向 jets

依次用 (J.7) 的 $a=0,1,2,3$，每步至多多取一角导。近/远乘法将高系数项放到低方向，不能产生 $\mathscr R_{\rm high}\mathscr Y_{\rm high}$。低系数每步可宽取 $2^{4100}$。高角乘法因子不超过 $4(2(s+8)+2)^{s+9}$，其 logarithm 小于 $16(s+10)<103000$；加262144、四个4100、二项式和邻胞费小于400000。故统一取
$$
 \boxed{\quad
 \begin{split}
 \mathscr X_s(h)\le2^{1048576}\{&
 \mathscr Y_{s+4}(h)+\mathscr N_{s+4}^{[3]}(g)
                     +\mathfrak B_{s+2}^{[3]}\\
 &+(1+\mathscr R_{s+8})
      [\mathscr Y_{16}(h)+\mathscr N_{16}^{[3]}(g)
                                  +\mathfrak B_{16}^{[3]}]\}.
 \end{split}
 \quad}
 \tag{J.11}
$$
应用取 $s\ge64$；低整数阶直接用同一递推。有限 connector 使用已声明的 $e_o$ 单位；内部 $C_j^\#/C_j<2^{256}$ 和相邻 $\ell_j$ 比的有限次幂均在余量内。129–8192前缀未删去。

该式对独立原子只估实际片内解及一侧普通源；跨片的真跳仍由原端荷处理。若需全局 $C_t^k$，必须另外核相应一侧 jets 相等。

## 5. 两个 mean 与真实高度

第一行平均给 $(\langle p\rangle)_t=-(A+1)\langle p\rangle$；真实周期高度本来有 $\langle p\rangle=0$。第二行的 $\langle k\rangle$ 保留并照 (J.7) 估计，不使用 $1/(im)$ 或高频极限。

proxy 的真通量 mean 为
$$
 \chi_t=12\mu_jr^{-4}\langle A_0g\rangle .
 \tag{J.12}
$$
$\chi$ 到四径导只需 $g,A_0$ 到三阶，与两行 mean 是同一恒等式。本篇通过准确两行恢复 $k$ 的 jets，不从裸 $\chi/q$ 再引入 $w^{-2}$ 层损。body 的 flat-end $\chi=0$ 与外部非零 affine flux 分别保留。

height gauge 只指定一次。准确物理读出为
$$
 h_\theta=a_{\rm ph}wp,\quad h_t=a_{\rm ph}wk,\quad
 h_{\theta\theta}=a_{\rm ph}w\,p_\theta,\quad
 h_{t\theta}=a_{\rm ph}w\,k_\theta,\quad
 h_{tt}=a_{\rm ph}w\{k_t+(A+1)k\}.
 \tag{J.13}
$$
$a_{\rm ph}w$、$\rho$ 和真实高度常数均不设为1；原 D/R 的端点权继续使用。

## 6. 1734阶 jet 逆及最大范围

在 N.23 使用输出 $s+4$，网络角阶 $q=s+1732$，ordinary 源最高 $s+1734$，背景最高 $s+1796$。因此
$$
                       64\le s\le6396,\qquad s+1796\le8192 .
 \tag{J.14}
$$
不能从 $s=6400$ 的网络结果再免费多加四个背景导数。保 N.3 的
$\mathfrak H_q=1+\mathscr R_{q+64}+\mathcal A_{q+16}+\epsilon_L\mathcal D_{q+16}$、
同一真实外行与 N.2 独立外门，得到
$$
 \boxed{\quad
 \mathscr X_s(h)\le
 2^{10485760}\mathfrak d_{s+1732}^{[3]}
 +2^{37748736}\mathfrak H_{s+1732}\mathfrak d_{1792}^{[3]},
 \qquad64\le s\le6396 .
 \quad}
 \tag{J.15}
$$
第一数覆盖 $8388609+1048576<10485760$，第二数覆盖
$33554433+1048576<37748736$。其余高背景只乘已得的 low $\mathscr Y_{16}$，无两个 high 因子。low source 仍是1794/1792完整窗。

N.26 的 projected 第一参数反馈可用同一式，但其 metric source 三径 jets 还须如下收费；一般 charged 数据仍保 G 的 projected-feedback识别范围。

## 7. 第一 metric 列的三个 source jets

两 bump 为 $64z^3(1-z)^3$，真实 scale仍为 $dt=(\eta_j/\sqrt{12})dx$。对其 degree6 多项式逐导并乘 $\ell_j^a$，可宽取
$$
 \ell_j^a|\partial_t^a\psi|\le2^{64}g_j,\qquad
 \ell_j^a|\partial_t^{a+1}\psi|
       \le2^{64}\delta_j^{-3/2}g_j,\qquad0\le a\le3 .
 \tag{J.16}
$$
$g_j$ 是原实际参数变化及邻胞和。第四导只在各 piece 内取。bump 的0、1、2阶端 jets 为0，第三阶可以跳；因此这里不声称 source 的第三分布导没有原子，也不制造新的0阶物理 jump。

沿 G 的准确式
$$
 B_pv=\Pi_{A_0}\{c_j e_{\psi,\rm rem}
       +c_j(\mathcal F_K-2Q)\ell-\psi N\}
 \tag{J.17}
$$
取三个 broken $t$ 导。scalar $\ell$ 是 M 的 mean/metric 导数，不是 $\ell_j$。它到三阶只需背景四态三 jet、$N$ 三 jet、$q_t=2Aq$ 与 $\psi$ 三导；$e_{\psi,\rm rem}$ 的 $\psi_t$ 用 (J.16) 至第四导。

每项把 $\ell_j$ 分配到实际因子，原 G 三个 profile、$C_j^\#$、physical $D\gamma$、$\delta^{-49/2}$ 及完整 finite 外段不变。相对原一导门，(J.16) 最多多51 bits。高 Moser、三径 chain rule 及原200000 profile bits后可取
$$
 \mathscr N_q^{[3]}(B_pv)
 \le2^{1572864}\mathscr R_{1856}
        (1+\mathscr R_{q+12})\|v\|_{\mathscr D_8},
 \qquad q+12\le8192 .
 \tag{J.18}
$$
low版保两个小因子 $2^{1572864}\mathscr R_{1856}^2\|v\|_{\mathscr D_8}$。
它用于已经解出的参数 source 的 jet读出，不代 N 更尖的 low Schur 门。

将其和同一 low D8 解代回 (J.11)，high项仍在 (J.15) 第二常数余量内。真实 metric lift 单独恢复
$$
 (H_p)_t=a_{\rm ph}w\{\psi(1+K_0)+\dot K_0\}.
 \tag{J.19}
$$
该相对 mean 一般不属于 fixed-metric $\mathscr Y$，不能直接加进 (J.2) 后宣称同一 norm。参考 lift、两端 height/flux、$\nu$ 和第二参数继续保原合同；本文只给 lift 后 fixed-metric部分的 jet逆。

## 8. 真 mean 重建与 quadratic 三径源

设 $h$ 在 holonomy-one 切空间，metric暂固定，low $\mathscr X_{16}$ 足够小使更新仍有 $D,J>1/2$，high范数仅有限。用 M 的同一小根重建 mean，二阶 scalar差为 $\Delta\kappa_2$。必须先写
$$
 \begin{split}
 P_\perp\mathfrak r_{\rm retr}
 =P_\perp\mathfrak r_{\rm line}
 -P_\perp\{&
 \mathcal F(P+p,K+k+\Delta\kappa_2,U+p_\theta,V+k_\theta)\\
 &-\mathcal F(P+p,K+k,U+p_\theta,V+k_\theta)\}.
 \end{split}
 \tag{J.20}
$$
$\partial_t\Delta\kappa_2$ 先被 $P_\perp$ 准确消去，再取三个径向导只需 $\Delta\kappa_2$ 三阶。完整普通mean由
$$
                  N_{\rm retr}
                =\Pi_{A_{0,\rm retr}}(P_\perp N_{\rm retr})
 \tag{J.21}
$$
恢复，并非设为0。

$\Pi_Af=f-\langle Af\rangle/\langle A\rangle$ 的修正输出是常数。其三个 $t$ 导用 scalar 正下界和完整圆周配对；任意角阶都不对该常数再取高导。$A_{0,\rm retr}$ 的三径导由实际更新三 state jets给出。所有 mean/nonmean配对保留。

原二次分子、inverse denominator和(J.20)均用 one-high Hölder。$c_j$ 的 scaled 三导用(J.8)，$Q$用(J.9)，所以原 profile
$c_j(1+|Q|)(C_j^\#)^2/(\zeta_j\delta_j^{16})$ 不变，其有限前缀和深净 $103-10/256$ 仍由 R.33 全和支付。故完整 retracted quadratic 源满足
$$
 \boxed{\quad
 \mathscr N_s^{[3]}(g_{\rm quad})\le2^{1572864}
 \{\mathscr X_{16}(h)\mathscr X_s(h)
       +(1+\mathscr R_{s+8})\mathscr X_{16}(h)^2\},
 \qquad s\ge16 .
 \quad}
 \tag{J.22}
$$
所有输入须在所列角窗内。没有把未投影mean用裸 $c_j$ 粗估，也没对已消去的 scalar 再取未付径向导数。

## 9. 完整 residual 缺陷与尚未授予的迭代

准确差仍为 $\mathcal E_N[h]=\alpha Nk-\beta N_\theta p-\gamma Np$。取三个 broken $t$ 导及完整 $\Pi_{A_0}$ 后，
$$
 \begin{split}
 \mathscr N_s^{[3]}(\Pi_{A_0}\mathcal E_N[h])
 \le2^{1572864}\{&
 \mathscr N_{s+1}^{[3]}(N)\mathscr X_{16}(h)
 +\mathscr N_{17}^{[3]}(N)\mathscr X_s(h)\\
 &+(1+\mathscr R_{s+8})
          \mathscr N_{17}^{[3]}(N)\mathscr X_{16}(h)\}.
 \end{split}
 \tag{J.23}
$$
只有相容 body 校正才能用 C.25 的 flat-flux门识别切向；外荷、原子、metric列保准确补项。

(J.15)、(J.22)、(J.23) 是同一个真实源/状态的径向jet接口。它们不证明1734导损失能被一个只有64阶高低差的 smoothing序列吸收，也不把高 $\mathscr R_{s+1796}$ 当小。下一步仍须 actual smoothing、parameter/height重建、$\mathcal E_N$ 有损缺陷与初 residual 收敛余额，才能宣称完整 nonlinear matching 和最终physical $C^2$存在性。