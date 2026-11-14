# R239 附录：一次有限对角压平给出的指数孔次数右逆

日期：2026-11-12（UTC）。独占作者：l2_moments。
有限尾压平引理与 literature、root、critical_kernel 共同核验；实际右逆及误差预算如下独立展开。

**结论。** 对 R239 中的两个实际慢边界符号，固定任意
$$
\kappa>\kappa_*:=2+2\log2,
\tag{A.1}
$$
存在有限常数 $C_\kappa$ 和实际右逆
$$
G_\kappa:
\mathscr X_\kappa=
\left\{v:\sum_{q\ge0}e^{\kappa q}\|\mathsf P_qv\|<\infty\right\}
\longrightarrow\mathcal H_-,
\qquad TG_\kappa=I,
$$
满足
$$
\|G_\kappa|_{\mathcal H_q}\|\le C_\kappa e^{\kappa q}.
\tag{A.2}
$$
因此 R239 的高位平均机制给出
$$
\boxed{
f\in N^\perp,\quad T^*h=f\ {\rm 逐行}
\quad\Longrightarrow\quad
\|\mathsf P_qh\|\le C'_\kappa e^{\kappa q}\|f\|.
}
\tag{A.3}
$$
同时，$T$ 和 $T^*$ 都真实有界作用于 $\mathscr X_\kappa$。
这使形式配对可以延至整个指数次数测试空间；不证明未知缺陷 $f$ 自身属于该空间。

本附录保留真实有限头，不需要先把它相似变换为 Jordan 块。
有限对角变换只压平纯尾中有限个较大系数，并且在右逆的输入端只支付最多 $q$ 个孔的代价。

## A.1 实际有限头加纯尾及需要的局部误差

沿用 R234 的记号。令
$$
H_m=T|_{\mathcal F_m},\qquad d=2^m,
\qquad
A_{\ge m}=\sum_{j\ge m}a_jE_j,\qquad a_j=(j+1)^{-2}.
$$
实际有限头满足
$$
H_m^d=0,\qquad \|H_m\|<6.
\tag{A.4}
$$
在有限头与尾的张量分解上，
$$
T^{[m]}=H_m\otimes I+I\otimes A_{\ge m}.
\tag{A.5}
$$
R234 已逐项证明
$$
T-T^{[m]}=\sum_{L\ge m}K_L,\qquad
\|K_L\|\le52e^{-770\,16^{L-1}},
\tag{A.6}
$$
其中 $K_L$ 只作用在前 $L+1$ 位，且级数在算子范数中收敛。
因此
$$
K_L\mathcal H_{\le b}\subset\mathcal H_{\le b+L+1}.
\tag{A.7}
$$
全空间 norm 估计与实际局部支撑都会使用，不能只保留前者。

## A.2 有限对角压平与所有相关层上的创建下界

固定 $q\ge0,m\ge1$，令 $d=2^m$。取
$$
N=2(q+d)+1,\qquad
F=\{m,m+1,\ldots,m+N-1\},\qquad
t=a_{m+N-1}=(m+N)^{-2}.
\tag{A.8}
$$
在纯尾孔基上定义正的有限坐标对角算子
$$
\Delta e_S=
\prod_{j\in S\cap F}\frac{a_j}{t}\ e_S.
\tag{A.9}
$$
所有因子至少为 $1$，所以 $\Delta$ 有界可逆，且
$$
\Delta\ge I,\qquad \|\Delta^{-1}\|\le1.
\tag{A.10}
$$
它只作用在有限位集 $F$，并保持每个尾次数层。
本节所有变换都是实际有界算子，不是无限张量相似的假设。

设
$$
C=A_{\ge m}^*=\sum_{j\ge m}a_jE_j^*,
\qquad C'=\Delta^{-1}C\Delta.
$$
直接作用于孔基可见
$$
C'=\sum_{j\ge m}b_jE_j^*,\qquad
b_j=
\begin{cases}
t,&j\in F,\\
a_j,&j\notin F.
\end{cases}
\tag{A.11}
$$
因此全部 $b_j\le t$，且恰有指定的 $N$ 个系数等于 $t$。

令 $n_j=E_j^*E_j$。不同位交换，故
$$
(C')^*C'-C'(C')^*
=\sum_{j\ge m}b_j^2(I-2n_j).
\tag{A.12}
$$
在尾孔次数 $p\le q+d$ 的层上，
$$
\sum_jb_j^2\ge Nt^2,\qquad
\sum_jb_j^2n_j\le pt^2.
$$
结合 $C'(C')^*\ge0$ 得
$$
(C')^*C'\ge(N-2p)t^2I\ge t^2I.
\tag{A.13}
$$
所以 $C'$ 在每个所需次数层上有闭值域及有界左逆，范数不超过 $1/t$。
取伴随，得到纯删除
$$
A'=(C')^*
$$
的逐层右逆
$$
Q'_p:\mathcal H_{\ge m,p}\longrightarrow\mathcal H_{\ge m,p+1},
\qquad A'Q'_p=I,\qquad\|Q'_p\|\le t^{-1}
\quad(0\le p\le q+d).
\tag{A.14}
$$
例如可取 $Q'_p=C'_p((C'_p)^*C'_p)^{-1}$。
这里 $C'_p$ 是创建在第 $p$ 层上的限制。

把有限组所需层上的 $Q'_p$ 合为逐层算子 $Q'$。
它增加一个尾孔，且在头空间上张量恒等。
由于输出次数层互相正交，其在任意所需的有限次数直和上的范数仍不超过 $1/t$。

$Q'_p$ 的输出可以涉及无限多个尾位。
本证明只使用它的真实 Hilbert 有界性和次数增加一，不假定有限位支撑保持。

## A.3 保留真实头的有限 Neumann 右逆

由于 $\Delta$ 正且只作用在尾，对 (A.11) 取伴随给出准确方向
$$
A_{\ge m}=\Delta^{-1}A'\Delta.
\tag{A.15}
$$
因此
$$
T^{[m]}=\Delta^{-1}(H_m+A')\Delta.
\tag{A.16}
$$
头算子 $H_m$ 与 $Q'$、$\Delta$ 都交换。

在尾次数不超过 $q$ 的输入上定义
$$
R'_{m,q}
=\sum_{k=0}^{d-1}(-H_m)^k(Q')^{k+1}.
\tag{A.17}
$$
每个组合只经过尾次数 $0,\ldots,q+d$，所以 (A.14) 付清全部真域。
利用 $A'(Q')^{k+1}=(Q')^k$、头尾交换及 $H_m^d=0$，有限和直接望远镜相消：
$$
(H_m+A')R'_{m,q}=I.
\tag{A.18}
$$
不存在额外输出层残量；最后一项严格由 $H_m^d=0$ 消失。

由 $\|H_m\|<6$ 和 $t<1$，
$$
\|R'_{m,q}\|
\le\sum_{k=0}^{d-1}6^kt^{-(k+1)}
\le d\,6^d t^{-d}.
\tag{A.19}
$$
再定义
$$
R_{m,q}=\Delta^{-1}R'_{m,q}\Delta.
\tag{A.20}
$$
于是
$$
T^{[m]}R_{m,q}=I.
\tag{A.21}
$$
整个输入的孔次数若不超过 $q$，输出的尾次数不超过 $q+d$，头次数不超过 $m$，故
$$
R_{m,q}\mathcal H_{\le q}\subset\mathcal H_{\le q+d+m}.
\tag{A.22}
$$
$\Delta$ 与 $\Delta^{-1}$ 保次数，所以不会扩大这个范围。

相似代价只在输入端出现。尾次数不超过 $q$ 时，
$\Delta$ 的最大特征值是前 $q$ 个最大的因子的乘积：
$$
\|\Delta|_{\text{尾次数}\le q}\|
\le
\prod_{i=1}^q\left(\frac{m+N}{m+i}\right)^2
=
\left[\frac{(m+N)^q m!}{(m+q)!}\right]^2.
\tag{A.23}
$$
$q=0$ 时该积等于 $1$。
输出端 $\Delta^{-1}$ 的范数不超过 $1$，无需支付全空间 $\|\Delta\|$。

## A.4 保留指数增长常数的范数估计

当 $q\ge1$ 时，由单调函数的积分估计，
$$
\sum_{i=1}^q\log(m+i)
\ge\int_m^{m+q}\log u\,du
\ge q\log(m+q)-q.
$$
又因为 $N=2q+2d+1$ 且 $m+d\ge1$，
$$
m+N\le2(m+q)+3d.
$$
所以 (A.23) 给
$$
\begin{aligned}
\log\|\Delta|_{\text{尾次数}\le q}\|
&\le2q\left[1+\log\frac{m+N}{m+q}\right]\\
&\le2(1+\log2)q
+2q\log\left(1+\frac{3d}{2(m+q)}\right)\\
&\le\kappa_*q+3d.
\end{aligned}
\tag{A.24}
$$
$q=0$ 时最后上界也成立。

结合 (A.19)，令
$$
M_{m,q}
=
\exp(\kappa_*q+3d)\ d\,6^d(m+N)^{2d}.
$$
则
$$
\boxed{\|R_{m,q}\|\le M_{m,q},}
$$
$$
\log M_{m,q}
\le\kappa_*q+3d+\log d+d\log6+2d\log(m+N).
\tag{A.25}
$$
这里把同一个有限尾相似变换只支付一次，避免了在每次逐层右逆中重复支付其条件数。

## A.5 参数选择与全部长进位的加权估计

固定 $\kappa>\kappa_*$。
选常数 $Q\ge64$ 足够大，使
$$
\frac{20\log Q}{\sqrt Q}\le\kappa-\kappa_*,
\qquad
Q\ge\frac{4\kappa+1}{8}.
\tag{A.26}
$$
因 $(\log x)/\sqrt x$ 在 $x>e^2$ 上递减，第一式对所有 $x\ge Q$ 都成立。

对每个 $q\ge0$，置
$$
x=q+Q,\qquad
m=m(q)=\left\lceil\frac12\log_2x\right\rceil,\qquad
d=2^m,
\qquad R_q=R_{m,q}|_{\mathcal H_q}.
\tag{A.27}
$$
于是
$$
\sqrt x\le d<2\sqrt x,\qquad m\le\sqrt x,\qquad m+N\le4x.
\tag{A.28}
$$
由 (A.25)，对 $x\ge64$ 可粗取
$$
\log\|R_q\|
\le\kappa_*q+20\sqrt x\log x
\le\kappa x.
\tag{A.29}
$$
常数 $20$ 已包括 $3d+\log d+d\log6$ 及 $2d\log(m+N)$。
最后一步用 (A.26) 与 $q\le x$。

为统一小 $q$，使用等价的指数次数范数
$$
\|v\|_{\kappa,Q}
=\sum_{q\ge0}e^{\kappa(q+Q)}\|\mathsf P_qv\|.
\tag{A.30}
$$
它只是 $\mathscr X_\kappa$ 范数乘以固定常数 $e^{\kappa Q}$。

令 $L=m+\ell$，$\ell\ge0$。
由 (A.6)、(A.21)、(A.22)，
$$
(TR_q-I)v=\sum_{\ell\ge0}K_{m+\ell}R_qv,
\qquad v\in\mathcal H_q.
\tag{A.31}
$$
第 $\ell$ 项的次数不超过
$$
b=q+d+2m+\ell+1.
$$
因此
$$
\|K_{m+\ell}R_qv\|_{\kappa,Q}
\le
52\|R_q\|\sqrt{b+1}\,
\exp\!\left(\kappa(b+Q)-770\,16^{m+\ell-1}\right)\|v\|.
\tag{A.32}
$$

现在逐一支付全部 $\ell$。
因 $d+2m+1\le4\sqrt x+1\le x$，
$$
b+Q\le2x+\ell,\qquad b+1\le2x+\ell.
$$
并且
$$
770\,16^{m+\ell-1}=48.125\,d^4\,16^\ell.
$$
对 $x\ge64,\ell\ge0$，
$$
\log52+\frac12\log(2x+\ell)\le x\,16^\ell.
$$
例如先用 $\log(2x+\ell)\le\log(2x)+\ell$，
再用 $\log52+\frac12\log(2x)\le x/2$ 和 $\ell\le16^\ell$ 即可。
结合 (A.29)，(A.32) 的指数不超过
$$
-48.125d^4\,16^\ell
+3\kappa x+\kappa\ell
+x\,16^\ell
\le
-48.125d^4\,16^\ell+(4\kappa+1)x\,16^\ell.
$$
由 $d^4\ge x^2$ 和 (A.26)，最终得到
$$
\boxed{
\|K_{m+\ell}R_qv\|_{\kappa,Q}
\le e^{-40d^4\,16^\ell}\|v\|.
}
\tag{A.33}
$$
故级数在指数次数空间中绝对收敛，且
$$
\boxed{
\|(TR_q-I)v\|_{\kappa,Q}
\le2e^{-40d(q)^4}\|v\|.
}
\tag{A.34}
$$
这里没有遗漏大 $\ell$：其线性权增长由 $16^\ell$ 的实际误差衰减统一支付。
参数 $Q$ 同时处理所有小次数。

## A.6 实际 Neumann 修正与指数次数右逆

定义
$$
Rv=\sum_{q\ge0}R_q\mathsf P_qv.
$$
(A.29) 保证该级数在 $\mathcal H_-$ 中绝对收敛，且
$$
\|R\|_{\mathscr X_{\kappa,Q}\to\mathcal H_-}\le1.
\tag{A.35}
$$
再令
$$
Ev=\sum_{q\ge0}(TR_q-I)\mathsf P_qv.
$$
由 (A.34)，
$$
\|E\|_{\mathscr X_{\kappa,Q}\to\mathscr X_{\kappa,Q}}
\le\sup_{q\ge0}2e^{-40d(q)^4-\kappa(q+Q)}
<\frac14.
\tag{A.36}
$$
$T$ 在 Hilbert 空间上有界，所以真实恒等式
$$
TR=I+E
$$
由有限和取极限成立。于是
$$
\boxed{
G_\kappa=R(I+E)^{-1},\qquad
TG_\kappa=I,\qquad
\|G_\kappa\|_{\mathscr X_{\kappa,Q}\to\mathcal H_-}\le\frac43.
}
\tag{A.37}
$$
回到未移位的范数，可取
$$
C_\kappa=\frac43 e^{\kappa Q}
$$
得到 (A.2)。

本证明允许 $Q'_p$、$R_q$ 和 $G_\kappa$ 的输出在位指标上无限。
其所需的每次真实域与次数控制均已在 (A.14)、(A.22)、(A.33) 中说明。
不从有限位支撑或某种快速头逼近性质推断右逆。

## A.7 R239 的模稳定范围传递

把 R239 的 (3.4) 中 $G$ 换成 $G_\kappa$。
对于 $|F|=2(q+1)$，有
$$
\widetilde G_{F,q}^{(\kappa)}
=\sum_{j\in F}\mathsf N_jG_\kappa E_j^*Q_F^{-1},
\qquad
\|\widetilde G_{F,q}^{(\kappa)}\|
\le\frac83e^{\kappa(q+Q+1)}.
\tag{A.38}
$$
实际恒等式 $\mathsf N_jE_j^*=P_{j,0}$ 没有改变。
所有 $j$ 可任意远移，因而值域可要求落在任意指定的 $\operatorname{Ran}B^r$。

R239 第 4–5 节的有限旗与闭 $N$ 论证原样适用：
$$
(\widetilde G_{F,q}^{(\kappa)}-J_q)\mathcal H_q\subset N.
$$
因此对 $f\in N^\perp$ 的唯一形式原像，
$$
\boxed{
\|\mathsf P_qh\|
\le\frac83e^{\kappa(Q+1)}e^{\kappa q}\|f\|.
}
\tag{A.39}
$$
这个结论也仅是规范逆模 $N$ 的估计，不改变 $\|J_q\|$ 的真实巨大下界。

## A.8 $T$、$T^*$ 在整个指数测试空间中有界

这一点是指数权相对于原三次权的重要区别，单独证明。

在一个只作用前 $L+1$ 位的局部算子作用下，孔次数的变化不超过 $L+1$。
因此，对 $v\in\mathcal H_q$，
$$
\begin{aligned}
\|K_Lv\|_{\mathscr X_\kappa}
&\le e^{\kappa(q+L+1)}
\sum_{|p-q|\le L+1}\|\mathsf P_pK_Lv\|\\
&\le\sqrt{2L+3}\,e^{\kappa(q+L+1)}\|K_L\|\|v\|.
\end{aligned}
$$
求输入层的一次和，得
$$
\|K_L\|_{\mathscr X_\kappa\to\mathscr X_\kappa}
\le\sqrt{2L+3}\,e^{\kappa(L+1)}\|K_L\|.
\tag{A.40}
$$
同一估计适用于 $K_L^*$。

在 $m=1$ 时，两个模型的有限头都等于最低位纯删除，因此
$$
T^{[1]}=\sum_{j\ge0}a_jE_j.
$$
它只降低一个孔，通常伴随只增加一个孔，而且无权范数均小于 $2$。
所以它们在 $\mathscr X_\kappa$ 上的范数分别不超过
$2e^{-\kappa}$、$2e^\kappa$。

由 (A.6)、(A.40)，
$$
\sum_{L\ge1}
52\sqrt{2L+3}
\exp\!\left(\kappa(L+1)-770\,16^{L-1}\right)<\infty.
$$
故
$$
\boxed{
T,\ T^*:\mathscr X_\kappa\longrightarrow\mathscr X_\kappa
\text{ 都是真正有界算子。}
}
\tag{A.41}
$$
有限整数支撑向量在 $\mathscr X_\kappa$ 中稠密，故上述范数极限也确定了与原
Hilbert 算子一致的实际作用。

若 $f\in N^\perp$，(A.39) 使 $h$ 在 $\mathscr X_\kappa$ 上定义连续配对。
逐行关系因此合法延为
$$
\boxed{
\langle h,Tv\rangle=\langle f,v\rangle
\qquad(v\in\mathscr X_\kappa).
}
\tag{A.42}
$$
若还知道 $f\in M\cap\mathscr X_\kappa$，取 $v=f$ 即可推出 $f=0$。
当前没有证明任意 $f\in M\ominus N$ 具有这个指数次数矩，不能免费代入。

## A.9 后续双尺度可用的真实尾正则化

为准确记录 (A.39) 的域后果，固定 $\rho>\kappa$。
令 $\mathcal N_{\ge m}$ 数尾位 $j\ge m$ 的孔，并逐坐标定义
$$
h^{(m)}=e^{-\rho\mathcal N_{\ge m}}h,
\qquad
f^{(m)}=e^{-\rho\mathcal N_{\ge m}}f.
\tag{A.43}
$$
若尾孔数为 $p$，头孔数只能是 $0,\ldots,m$。
这些部分互相正交，所以 (A.39) 给
$$
\|\mathsf P_{\mathrm{tail},p}h\|^2
\le
(C'_\kappa)^2\|f\|^2
\sum_{r=0}^m e^{2\kappa(p+r)}
\le
\frac{(C'_\kappa)^2 e^{2\kappa(p+m)}}{1-e^{-2\kappa}}\|f\|^2.
$$
因此 $h^{(m)}$ 是真正的 Hilbert 向量，而且
$$
\boxed{
\|h^{(m)}\|
\le
\frac{C'_\kappa e^{\kappa m}}
{\sqrt{(1-e^{-2\kappa})(1-e^{-2(\rho-\kappa)})}}
\,\|f\|.
}
\tag{A.44}
$$
另一方面，对每个固定 $f\in\mathcal H_-$，
$$
f^{(m)}\longrightarrow f\quad(m\to\infty)
\tag{A.45}
$$
强收敛：先对有限整数头向量验证，再用这些收缩算子的一致范数界。

令 $C_{\ge m}=A_{\ge m}^*$。
对 (A.6) 中每个 $K_L^*$，尾正则化只需在其 $L+1-m$ 个尾位上共轭，
故相应局部共轭范数不超过
$e^{\rho(L+1-m)}\|K_L\|$。
于是存在有界算子 $\mathcal E_{m,\rho}$，满足
$$
\|\mathcal E_{m,\rho}\|
\le52\sum_{L\ge m}
e^{\rho(L+1-m)}e^{-770\,16^{L-1}}
\le C_\rho e^{-770\,16^{m-1}},
\tag{A.46}
$$
其中 $C_\rho$ 与 $m$ 无关。
最后一个常数有限，可直接提出首指数，并把剩余级数用 $m=1$ 的更慢衰减控制。

逐行方程 $T^*h=f$ 经上述有限局部共轭，成为实际 Hilbert 等式
$$
\boxed{
(H_m^*+e^{-\rho}C_{\ge m})h^{(m)}
=f^{(m)}-\mathcal E_{m,\rho}h^{(m)}.
}
\tag{A.47}
$$
识别 (A.47) 可以先逐有限整数行核对；实际 $T^*$ 的每行只有有限前驱，
局部差的这些行最终为零。再用 (A.44)、(A.46) 的实际 Hilbert 收敛，
不用给原形式 $h$ 赋予未证明的 Hilbert 域。

由 (A.44)–(A.46)，
$$
(H_m^*+e^{-\rho}C_{\ge m})h^{(m)}\longrightarrow f
\quad\text{于 }\mathcal H_-.
\tag{A.48}
$$
这是一个明确的真实有限头加缩放纯尾的像逼近。
它尚不是 $T^*$ 的像逼近：纯尾从系数 $1$ 改成 $e^{-\rho}$ 所产生的相邻孔次数项，
乘上 (A.44) 中可能增长的原像范数，仍需额外估计。
不能仅凭这些模型算子趋于 $T$ 就推出 $f\in\overline{\operatorname{Ran}T^*}$。

所以 (A.39)、(A.41)、(A.47) 提供了后续能量分析的实际域与可支付误差；
边界稳定范围等式 $N=M$ 仍保持未决。


## A.10 精确尾通量、稳定范围判据与统一缺陷尾下界

本节记录 (A.47) 的正能量后果。
其中关于单个缺陷向量最高位尾的指数下界，弱于 R214 已有的依赖首个非零整数坐标的多项式下界；
这里保留的是精确通量恒等式、对任意核向量的判据，以及整个缺陷单位球上统一的常数。
也不宣称本附录是指数次数右逆的首次构造：并发入库的 R234 附录已经有指数权 $24$ 版本，
本附录给出直接压平机制及 $\kappa>2+2\log2$ 的常数范围。

固定 $\kappa>\kappa_*$、$\rho>\kappa$，记
$$
r=e^{-\rho},\qquad
A_m^{\rm tail}=\sum_{j\ge m}a_j\le\frac1m\quad(m\ge1).
$$
将 (A.44) 中的固定常数记为 $L_{\kappa,\rho}$，即
$$
\|h_d^{(m)}\|\le L_{\kappa,\rho}e^{\kappa m}\|d\|
\qquad(d\in D).
\tag{A.49}
$$
这里 $h_d$ 是右侧为 $d$ 的唯一形式原像。

### A.10.1 对全部核向量的通量等式

取任意 $d\in D$、$f\in M$。
由 (A.47)–(A.48)，
$$
g_{d,m}:=(H_m^*+rC_{\ge m})h_d^{(m)}
\longrightarrow d.
$$
另一方面，令 $E_m=T-T^{[m]}$。
因为 $Tf=0$，
$$
(H_m+rA_{\ge m})f
=(r-1)A_{\ge m}f-E_mf.
$$
通常内积配对给
$$
\langle g_{d,m},f\rangle
=(r-1)\langle h_d^{(m)},A_{\ge m}f\rangle
-\langle h_d^{(m)},E_mf\rangle.
$$
(A.6)、(A.49) 保证最后一项趋于零。因此
$$
\boxed{
\langle d,f\rangle
=(r-1)\lim_{m\to\infty}
\langle h_d^{(m)},A_{\ge m}f\rangle.
}
\tag{A.50}
$$
右侧的极限存在，是由这个真实等式与左侧强极限得到的，
没有预设任何相邻次数通量消失。

令 $P_m$ 为前 $2^m$ 个整数坐标的投影，即尾真空投影。
纯尾删除满足
$$
A_{\ge m}P_m=0,\qquad
\|A_{\ge m}\|\le A_m^{\rm tail}.
$$
所以
$$
|\langle h_d^{(m)},A_{\ge m}f\rangle|
\le
L_{\kappa,\rho}e^{\kappa m}A_m^{\rm tail}
\|d\|\,\|(I-P_m)f\|.
\tag{A.51}
$$

**稳定范围判据。** 若 $f\in M$ 且
$$
e^{\kappa m}A_m^{\rm tail}\|(I-P_m)f\|\longrightarrow0,
\tag{A.52}
$$
则 $f\in N$。

证明是把 (A.51) 代入 (A.50)，得到 $f\perp D$，
再用 $M=N\oplus D$。相同证明也允许 (A.52) 只沿一条趋于无穷的子列成立。
这里没有要求正交缺陷分量 $P_Df$ 继承 $f$ 的尾正则性。

例如，如果 $\|(I-P_m)f\|=O(e^{-\beta m})$，且 $\beta>\kappa_*$，
可以选 $\kappa\in(\kappa_*,\beta]$，于是 (A.52) 成立。
这只是一个充分条件；一般 Hilbert 核向量没有这样的已知尾速率。

### A.10.2 缺陷单位球上的统一估计

现在令 $d\in D$、$\|d\|=1$，并置
$$
\delta_m(d)=\|(I-P_m)d\|.
$$
由于 $d^{(m)}=r^{\mathcal N_{\ge m}}d$ 是正收缩作用，
$$
\langle d^{(m)},d\rangle
=\sum_n r^{\nu_{\ge m}(n)}|d_n|^2
\ge\|P_md\|^2=1-\delta_m(d)^2.
\tag{A.53}
$$
这是实际正算子的配对；没有使用非正的 Jordan 级投影。

将 (A.47) 直接与 $d$ 配对，再用 $Td=0$，得到
$$
1-\delta_m(d)^2
\le
(1-r)L_{\kappa,\rho}e^{\kappa m}
A_m^{\rm tail}\delta_m(d)
+\varepsilon_m,
\tag{A.54}
$$
其中可以统一取
$$
\varepsilon_m
=
L_{\kappa,\rho}(26+C_\rho)
e^{\kappa m}e^{-770\,16^{m-1}}.
\tag{A.55}
$$
两个误差分别来自实际 $E_m$ 和共轭后的 $\mathcal E_{m,\rho}$。
它们的常数均与 $d$ 无关。

存在只依赖 $\kappa,\rho$ 的 $m_0$，使 $m\ge m_0$ 时 $\varepsilon_m\le1/2$。
令
$$
b_m=(1-r)L_{\kappa,\rho}e^{\kappa m}A_m^{\rm tail}.
$$
由 $0\le\delta_m\le1$，(A.54) 推出
$$
\frac12\le\delta_m^2+b_m\delta_m
\le(1+b_m)\delta_m.
$$
因此
$$
\boxed{
\inf_{\substack{d\in D\\\|d\|=1}}
\|(I-P_m)d\|
\ge\frac1{2(1+b_m)}
\ge c_{\kappa,\rho}\,m e^{-\kappa m}
\quad(m\ge m_0).
}
\tag{A.56}
$$
若 $D=\{0\}$，相关单位球断言按空集理解；这里没有用 (A.56) 假设其非零。
最后一步用 $A_m^{\rm tail}\le1/m$ 以及 $e^{\kappa m}/m\ge1$。
例如可取
$$
c_{\kappa,\rho}
=\frac1{2[1+(1-r)L_{\kappa,\rho}]}.
$$

等价地，若 $D\ne0$，则对每个 $m\ge m_0$，
$$
\boxed{
\|P_m|_D\|
\le
\sqrt{1-\frac1{4(1+b_m)^2}}<1.
}
\tag{A.57}
$$
这不排除未知缺陷空间，也不声称其单位球的尾一致趋于零。
恰恰相反，它给出每个有限整数头之外必须保留的统一质量。

(A.50) 把尚未解决的条件明确留在
$\langle h_d^{(m)},A_{\ge m}f\rangle$ 的相邻孔次数通量上。
单凭 $A_m^{\rm tail}=O(1/m)$ 与 (A.49) 的指数增长，不能令它自动消失。


## A.11 保留未压平尾的方差：阈值常数再降低

A.2 的交换子下界只使用了 $N$ 个压平位，丢掉了其后的正方差。
保留这一项可将以上全部结论中的阈值常数改进为
$$
\boxed{\kappa_{**}=2+2\log(3/2).}
\tag{A.58}
$$
也就是说，对每个 $\kappa>\kappa_{**}$，仍有 (A.2)、(A.3)、(A.39) 及 A.8–A.10 的全部结论，
但参数 $Q$ 和常数依新的 $\kappa$ 重新选择。
以下给出完整改动；前十节原有证明仍然成立，不被默改。

在 A.2 中令 $s=q+d$，改取
$$
N=\left\lceil\frac32(s+2)\right\rceil,\qquad
t=(m+N)^{-2},
\tag{A.59}
$$
其余有限对角算子 $\Delta$ 及 $C'$ 的定义不变。
所有新权重仍不超过 $t$，前 $N$ 个等于 $t$。
令 $x_0=m+N$。压平块之后的方差满足
$$
\sum_{j\ge m+N}a_j^2
\ge\frac1{3(x_0+1)^3},
$$
所以
$$
t^{-2}\sum_{j\ge m+N}a_j^2
\ge\frac{x_0^4}{3(x_0+1)^3}
\ge\frac{x_0-3}{3}.
\tag{A.60}
$$
最后一步由
$$
x_0^4-(x_0-3)(x_0+1)^3=6x_0^2+8x_0+3>0
$$
直接验证。

于尾次数 $p\le s$ 上，(A.12) 因而给
$$
(C')^*C'
\ge
\left[N-2p+\frac{m+N-3}{3}\right]t^2I
\ge
\left[\frac{4N+m-3}{3}-2s\right]t^2I.
$$
(A.59) 使最后括号至少为 $(m+9)/3\ge3$，特别仍至少为 $1$。
因此 A.2–A.3 的逐层 $Q'_p$ 及真实有限 Neumann 右逆完全不变，
仍可保守使用 $\|Q'_p\|\le t^{-1}$。

输入有限对角成本则改善如下。
对 $q\ge1$，由 $N<\frac32(q+d+2)+1$，
$$
m+N
\le\frac32(m+q)+\frac32d+4.
$$
沿用 A.4 的积分估计和 $\log(1+u)\le u$，得到
$$
\begin{aligned}
\log\|\Delta|_{\text{尾次数}\le q}\|
&\le
2q\left[1+\log\frac{m+N}{m+q}\right]\\
&\le
\kappa_{**}q+
2q\log\left(1+\frac{d+8/3}{m+q}\right)\\
&\le\kappa_{**}q+2d+\frac{16}{3}.
\end{aligned}
\tag{A.61}
$$
$q=0$ 时左侧为零，同一个上界仍成立。

在 A.5 的统一参数选择中 $Q\ge64$，从而 $d\ge8$、$s\ge8$。
故
$$
2d+\frac{16}{3}\le3d,\qquad
\left\lceil\frac32(s+2)\right\rceil\le2s+1.
$$
因此新 $N$ 不大于旧 $N$，且
$$
\log M_{m,q}
\le\kappa_{**}q+3d+\log d+d\log6+2d\log(m+N).
$$
A.28 的 $m+N\le4x$、A.29 的 $20\sqrt x\log x$ 余量全部保留。
只需把 A.26 改成
$$
\frac{20\log Q}{\sqrt Q}\le\kappa-\kappa_{**},
\qquad Q\ge64,\qquad Q\ge(4\kappa+1)/8.
\tag{A.62}
$$
之后 A.32–A.57 的每个实际误差、真域和正配对论证原样成立。

这一常数改进不声称任意小正指数权都有实际右逆。
它也不把一般右逆的可能下界转移到 $N^\perp$ 上的特殊模 $N$ 配对；
后者始终使用 R239 的独立高位平均论证。
