# 实际全部同源分支的 Hecke 迹、微分倍数与周期坐标

日期：2026-11-12。状态：全部 $p+1$ 条分支的标签运输、微分权重、
Gauss–Manin 矩阵、实际两条半线的交换及原点归一 $H_i$ 的零迹
均已证明。这些关系尚未给出无穷多个 $p$ 的中央导数非零。

本篇取 $p\equiv3\pmod4$、$p\ge7$，使用原来的 $E_{17}$ 及
实际 $M_e=M_1=t^4+(7/2)t^6+\cdots$、$M_o=t+(1/2)t^3+\cdots$。
不是另选一条具有相似 Hecke 性质的曲线或模形式。

## 1. 全部 $p+1$ 条商同源的准确标签

设 $N=68$，$\Lambda_\tau=\mathbb Z+\tau\mathbb Z$，原轨道
$\mathcal S\subset(\mathbb Z/N)^2$ 及旋转轨道
$\mathcal S^{\rm rot}$ 如
[实际权一 Hecke 分解](2026-11-12-actual-weight-one-hecke-and-character-decomposition.md)。
标签 $(a,b)$ 代表 $(a+b\tau)/N$。
对任一这样的轨道 $\mathcal T$，记对应 completed-zeta 和为
$\mathcal G_{\mathcal T}$。其奇权重满足
$$
 \mathcal G_{u\mathcal T}=\chi_{-4}(u)\mathcal G_{\mathcal T}
 \qquad((u,N)=1).
 \tag{1}
$$
这来自原 $-3$ 轨道的精确标量协变，不要求 $17$ 角色平凡。

以下是全部循环 $p$ 次商同源，且每一条保留完整层结构：
$$
\begin{array}{c|c|c|c}
 &\tau_{\rm target}&z_{\rm target}&(a,b)_{\rm target}\\ \hline
 j=0,\ldots,p-1&(\tau+Nj)/p&z&(a,pb)\\
 \infty&p\tau&pz&(pa,b).
\end{array}
\tag{2}
$$
第一行有 $\Lambda_\tau\subset\Lambda_{(\tau+Nj)/p}$；
第二行有 $p\Lambda_\tau\subset\Lambda_{p\tau}$。
$Nj\equiv0\pmod N$ 使标签没有被隐去的平移。
$p$ 为奇数，且 $Nj$ 为偶数，所以有序的 $2$ 阶层结构也被保留。

对轨道 $\operatorname{diag}(1,p)\mathcal T$ 应用 R82 的式 (20)。
系数 Frobenius $\sigma_{p^2}$ 只把标签第一坐标乘以 $p^2$；
随后用
$$
 \operatorname{diag}(p^2,p)\mathcal T
      =p\operatorname{diag}(p,1)\mathcal T
$$
及 $\chi_{-4}(p)=-1$，准确得到
$$
\boxed{\quad
 \sum_{j=0}^{p-1}
 \mathcal G_{\operatorname{diag}(1,p)\mathcal T}
       \!\left(\frac{\tau+Nj}{p}\right)
 +p\,\mathcal G_{\operatorname{diag}(p,1)\mathcal T}(p\tau)=0.
\quad}
\tag{3}
$$
包括所有常数项。两个轨道 $\mathcal S,\mathcal S^{\rm rot}$
各自满足 (3)。

这里 $1,p$ 正是 (2) 对标准微分 $dz$ 的拉回倍数。
因此 (3) 是真实商同源上的权一截面拉回迹，不只是把 cusp
上的 $q$-系数移位算子重新命名。
特别是，所有目标上均使用原来的标签 $(a,b)$ 会给出错误的几何式子。

## 2. 从复周期权重到整 Legendre 微分

取本课题固定的 Legendre 家族
$$
 y^2=x(x-1)(x-\lambda),\qquad
 \lambda=\frac12+t,\qquad
 \omega=\frac{dx}{2y},\qquad s=1-4t^2.
 \tag{4}
$$
若其周期为 $\omega_1,\omega_2=\tau\omega_1$，则从
$\mathbb C/\Lambda_\tau$ 到 (4) 的解析参数是
$z_{\rm Leg}=\omega_1z$。因此 (2) 的拉回倍数，在 (4) 的
固定微分框架中准确为
$$
 d_j=\frac{\omega_1(\tau_j)}{\omega_1(\tau)}
       \quad(j<p),\qquad
 d_\infty=p\,\frac{\omega_1(p\tau)}{\omega_1(\tau)}.
 \tag{5}
$$
该比值是同源对应上的代数微分倍数；本篇不把复周期本身
任意嵌入 $\mathbb C_p$。在 $p$ 进侧使用的仍是同一个代数拉回
$\varphi_j^*\omega_j=d_j\omega$。

有序 $2$ 阶标记确定目标 Legendre 方程，只剩
$y\mapsto-y$ 的可能。规定约化同源是实际
$(x,y)\mapsto(x^p,y^p)$，并运送完整的 prime-to-$p$ 层标记，
便固定这一符号。没有再用任意正式群同构乘一个单位、
从而改变 $\omega,K,L$ 的自由。

令
$$
 Y(t)=\begin{pmatrix}K(t)&L(t)\\K'(t)&L'(t)\end{pmatrix},
 \qquad
 (1-4t^2)y''-8ty'-y=0,
 \tag{6}
$$
初值 $K(0)=L'(0)=1$、$K'(0)=L(0)=0$。
于是
$$
 KL'-K'L=s^{-1},\qquad u=L/K,\qquad u'=(sK^2)^{-1}.
 \tag{7}
$$
使用[实际整 Frobenius](2026-11-12-integral-gm-frobenius-critical-row.md)
的同一行约定及常数
$$
 F_0=\begin{pmatrix}0&pa_p\\b_p&0\end{pmatrix},
 \qquad a_p,b_p\in\mathbb Z_p^\times,\quad a_pb_p=-1.
 \tag{8}
$$
这里 $a_p,b_p$ 不是 Frobenius trace，也不是半权 Taylor 系数。

[实际 canonical 邻点证明](2026-11-12-critical-gauss-period-map-and-canonical-neighbors.md)
§4–6 给出所需的晶体刚性接口：
所有循环商在共同特殊纤维标记下约化为同一个相对 Frobenius；
在 $h=Y^{-1}(\omega,\nabla_{\partial_t}\omega)^{\rm t}$ 的水平标记中，
其拉回恒为 (8)。
这一步使用实际商同源与晶体比较，不是从模 $p$ 矩阵相同就
推断特征零矩阵相同。
因而，对实际源、目标参数 $t,t_j$，
$$
\boxed{\qquad
 M_j=Y(t_j)F_0Y(t)^{-1}.
\qquad}
\tag{9}
$$
该公式保留目标的 Frobenius 层标记。系数上的 $\sigma$ 已包含在
这个标记中；$K,L,Y$ 的系数有理，所以没有额外系数扭转可删改。

## 3. 确切的 $p/u$、微分倍数和 Kodaira–Spencer

写 $K_j=K(t_j)$、$L_j=L(t_j)$。
(9) 第一行准确为
$$
 s(t)\bigl(
    b_pL_jL'-pa_pK_jK',\quad
    -b_pL_jL+pa_pK_jK
 \bigr).
 \tag{10}
$$
同源保 Hodge 子模，故第二个坐标为零。这给出
$$
\boxed{\quad
 pa_pK_jK=b_pL_jL,\qquad
 u(t_j)u(t)=\frac{pa_p}{b_p}.
\quad}
\tag{11}
$$
第二式在分母非零时成立，第一式是包括源 $t=0$ 的完整等式。
比例是 $pa_p/b_p$，不是 $b_p/(pa_p)$。

再用 Wronskian (7)，第一坐标化为
$$
\boxed{\quad
 d_j=b_p\frac{L_j}{K}
      =pa_p\frac{K_j}{L}.
\quad}
\tag{12}
$$
第二个表示仅在 $L\ne0$ 时使用。源 $t=0$ 时则准确为
$$
 K(t_j)=0,\qquad d_j=b_pL(t_j).
 \tag{13}
$$
引用上述 canonical 邻点证明，所有 $p+1$ 个 $t_j$ 两两不同，
恰是 $K$ 在
$$
 \rho=p^{-1/(p+1)}
 \tag{14}
$$
闭盘上的全部零点，且 $v_p(t_j)=1/(p+1)$。
在该盘上 $J=L/t$ 为单位，故
$$
 v_p(d_j)=1/(p+1).
 \tag{15}
$$
这与商同源的正式参数乘积所得微分估值一致。

对 (11) 求导，或直接对 $K_j-\xi L_j=0$ 求导，其中
$\xi=(b_p/(pa_p))u(t)$，得到
$$
\boxed{\quad
 \frac{dt_j}{dt}
   =\frac{s(t_j)}{s(t)}\,\frac{d_j^2}{p}.
\quad}
\tag{16}
$$
因此 $p$ 因子在微分倍数与基底变化之间也完全核对。
等价的、在每个邻点附近更方便的参数为
$$
 \xi=\frac{K(t_j)}{L(t_j)}
        =\frac{b_p}{pa_p}u(t),\qquad
 \frac{dt_j}{d\xi}=-s(t_j)L(t_j)^2.
 \tag{17}
$$
由于 $K$ 的零点简单，(17) 在 $\xi=0$ 附近给出全部 $p+1$
条解析分支。其单纯性也由
$-K'(t_j)L(t_j)=s(t_j)^{-1}$ 直接得出。

## 4. 实际 $M_e,M_o$ 的运输不能漏掉半线交换

沿用原除法单位模型的固定常数
$$
 c_e=\frac{\sqrt2\,17^{17/4}}{4800f},\qquad
 c_o=\frac{i\sqrt2\,17^{7/4}}{32f},\qquad f=34(1+i).
 \tag{18}
$$
在源水平标记中写
$$
 M_e=\frac{c_e}{2}(S-iS^{\rm rot}),\qquad
 M_o=\frac{c_o}{2}(S+iS^{\rm rot}).
 \tag{19}
$$
此处 $S,S^{\rm rot}$ 是已经除去周期的实际 completed-zeta
代数和，而不是 cusp 的标量 Fourier 系数。

所有目标的 prime-to-$p$ 标记，在共同形式盘中是源标记的
Frobenius 像。目标层的 $(S,S^{\rm rot})$ 因此是
$(S^\sigma,(S^{\rm rot})^\sigma)$。
惰性处 $\sigma(i)=-i$，但运输一个固定线性组合时，其系数
$-i$ 不另作一次 Galois 共轭。故源两条截面运输后准确是
$$
\boxed{\quad
 M_e^{\rm tr}=\frac{c_e}{c_o^\sigma}\,M_o^\sigma,\qquad
 M_o^{\rm tr}=\frac{c_o}{c_e^\sigma}\,M_e^\sigma.
\quad}
\tag{20}
$$
这正是
[实际 Kummer 半线比较](2026-11-12-kummer-frobenius-vertical-jets-and-gm-pairing.md)
中的交换。上述两个系数都是目标素数处的单位。
$M_e,M_o$ 的 Taylor 系数有理，故最后的 $\sigma$ 可在这些
级数上删去；不能把它连同 (20) 的交换和单位一起忽略。

把 (3) 变为 (4) 的微分框架，再代入 (20)，得到两条完整等式
$$
\boxed{\qquad
 \sum_{j\in\mathbb P^1(\mathbb F_p)}d_jM_e(t_j)=0,\qquad
 \sum_{j\in\mathbb P^1(\mathbb F_p)}d_jM_o(t_j)=0.
\qquad}
\tag{21}
$$
两个等式分别来自源的另一条半线。
在源 $t=0$，偶部那条是
$\sum L(t_j)M_e(t_j)=0$，它首先由 $\pm t_j$ 的配对抵消；
不可把它读成一个已知奇部首项对偶部中央行的非零证明。

## 5. 中央周期分支上的真实迹

在共同分支域取 $v=u(t_j)=1/\xi$。由 (12)，
$d_j=(b_pv/K(t))K_j$。
所以 (21) 等价于
$$
\boxed{\quad
 \sum_j K(t_j(v))M_e(t_j(v))=0,\qquad
 \sum_j K(t_j(v))M_o(t_j(v))=0.
\quad}
\tag{22}
$$
这里第一和确实是实际
$\mathcal B_1(v)=K(t(v))M_e(t(v))$ 的所有 $p+1$ 个邻点分支之迹。
这些分支在 $v=\infty$ 附近以 $\xi=1/v$ 展开。
它们并不是把同一个 $v=0$ 形式级数代入 $p+1$ 次。

还有一条独立的复解析全阶核对。设源 $\tau_0=i$，
邻点 $\tau_j^0=(i+Nj)/p$、$\tau_\infty^0=pi$。
源 Cayley 参数
$$
 w=\frac{\tau-i}{\tau+i}
$$
恰等于每个目标以自身 CM 点为中心的 Cayley 参数：
$$
 \frac{\tau_j-\tau_j^0}{\tau_j-\overline{\tau_j^0}}=w.
 \tag{23}
$$
对 (3) 除以 $1-w$，逐项展开即可得到全部中央 Taylor 迹。
若 $\partial_k=(2\pi i)^{-1}\partial_\tau-k/(4\pi\operatorname{Im}\tau)$
为 Maass–Shimura 算子，则
$$
 [w^m](1-w)^{-1}g(\tau(w))
 =\frac{(-4\pi\operatorname{Im}\tau_0)^m}{m!}\,
          \partial_1^m g(\tau_0).
$$
因此准确有
$$
 \sum_{j<p}\partial_1^m
       \mathcal G_{\operatorname{diag}(1,p)\mathcal T}(\tau_j^0)
 +p^{2m+1}\partial_1^m
       \mathcal G_{\operatorname{diag}(p,1)\mathcal T}(pi)=0.
 \tag{24}
$$
这里的邻点是导子增加 $p$ 的 CM 点，且层结构如 (2)。
公式 (24) 不把这些值改成原固定曲线在同一原点的
$C_m$，也不把 (22) 误写成 $v^n\mapsto v^{n/p}$。

## 6. 原点归一 $H_i$ 的邻点迹确实为零

取
[固定周期 torsor 原函数](2026-11-12-fixed-period-torsor-primitives-and-residues.md)
中实际惰性原函数的 $t$ 表示
$$
 \mathscr I(t)=H_i(u(t))
       =\int_0^t\frac{M_eK}{sL^2}\,dt.
 \tag{25}
$$
这个表达在 $t=0$ 正则，因为 $M_e$ 从 $t^4$ 开始。
由
[准确周期分母](2026-11-12-gauss-manin-period-denominators.md)，
$J=L/t$ 的最近零点半径是
$$
 R_J=p^{-1/(p^2+p)}>\rho.
 \tag{26}
$$
$M_e$ 在开单位盘整，$K$ 在开单位盘解析。
因此 (25) 的微分在 $|t|<R_J$ 解析。
逐项积分所除的整数增长是次指数的，不缩小开盘收敛半径；
故 $\mathscr I(t)$ 的原点级数可合法到达全部 $K$ 邻点。
这一步与把 $H_i(v)$ 的原点级数直接代入 $v=\infty$ 不同。

在 (17) 的共同域中，
$$
 \frac d{d\xi}\mathscr I(t_j(\xi))
       =-K(t_j(\xi))M_e(t_j(\xi)).
 \tag{27}
$$
由 (22)，所有分支之和为常数。
又 $K,s,M_e$ 为偶函数、$L$ 为奇函数，所以 (25) 的被积系数
为偶函数，$\mathscr I$ 为原点归一的奇函数。
$K$ 的全部邻点根以 $\pm r$ 成对。因此这个常数准确为零：
$$
\boxed{\qquad
 \sum_{j=0}^{p}\mathscr I(t_j(\xi))=0.
\qquad}
\tag{28}
$$
没有待定的单位、周期或选择各支原函数常数的自由。
这条归一化零迹对每个目标惰性 $p$ 成立，故它本身不等价于
完整中央 $J'_p(0)=0$；例如本课题已严格证明的 $p=7$ 非零证书
与 (28) 同时成立。

相反，普通辅助原函数
$$
 \mathscr E'(t)=\frac{M_e}{sK}
 \tag{29}
$$
在每个邻点 $r$ 有真正的简单极点。准确留数为
$$
\boxed{\qquad
 \operatorname{res}_{t=r}\mathscr E'(t)\,dt
     =-L(r)M_e(r)\ne0,\qquad
 v_p(L(r)M_e(r))=\frac5{p+1}.
\qquad}
\tag{30}
$$
这里使用 $-s(r)K'(r)L(r)=1$，以及
$M_e=t^4(1+t^2\mathbb Z_p[[t]])$、$J(r)$ 为单位。
若 $\mathscr H_o'= \mathscr E/(sKL)$，则任取一个一致的局部
对数规范，其在 $r$ 的最高对数项为
$$
 \mathscr H_o(t)
   =\frac{L(r)M_e(r)}2\bigl(\log(t-r)\bigr)^2
       +\text{较低对数阶的项}.
 \tag{31}
$$
所以 $\mathscr E,\mathscr H_o$ 的值或迹常数，需保留真实
对数或 Coleman 规范；不能照搬 (25) 的原点解析值论证。

## 7. 与真正第二 Witt 层的接口

[全部邻点的 Kummer 范数](2026-11-12-all-isogeny-neighbors-kummer-norms.md)
保留了各同源的常数 $\kappa_{\varphi,P}$ 与完整源参数 germ。
本篇 (12)、(16)、(20) 给出将那个全 germ 恒等式放入
同一 Legendre/GM 框架时必须使用的微分倍数、基底导数与半线交换。
其一阶项正好产生 (21)，而高阶项包含各分支的全部正式群
Taylor 系数，不能只用 $d_j^k$ 代替同源的高 jet。

本篇没有把全邻点 Hecke 迹替换为一个 crystalline $\phi^2$
分支，也没有把已知零迹 (28) 当成中央除 $p$ 行的额外消失。
下一项真正需要比较的对象，是保留这些权重及对数规范之后，
完整邻点 germ 对实际第二 Witt 行和完整中央 Stokes 常数的作用。

外部规范的原始依据已分别列在 R82、实际整 Frobenius 以及
canonical 邻点证明中；本篇 (2)–(5)、(10)–(24)、(27)–(31)
是对本题实际对象给出的直接计算。
