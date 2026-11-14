# R150 附录：谐和正主行的精确半条带预算及全部实剪切碰撞幂

日期：2026-11-13（UTC）。作者：kernel_resume_1cf / normal_resume_1cf / Astra-ISP-1cf8c51d。
状态：完整证明；根与 normal 独立核验全部条带常数及好时间序列。
此稿补[有限阶相伴图定理](R150-appendix-finite-order-positive-anchor-companion-graphs-and-all-shear-powers.md)未覆盖的谐和端点，进一步只要求原生计数的严格 limsup 阈值；不把无限阶整预解称为有限阶。实际正半群依据[计数半群证明](R134-appendix-positive-counting-semigroup-and-finite-order-entire-resolvent.md)，基本二次因式沿用[相反增生条带引理](R150-appendix-opposite-quadratic-accretivity-and-finite-order-resolvent-strip.md)。

## 1. 主结论与可核条件

沿用前一“有限阶正主行的相伴矩阵图排核”附录的真实对象：
$$
u=a_*+\sum a_j\chi_j,\qquad v=c_*+\sum c_j\chi_j,
$$
$a_*,c_*\in\mathbb R$，$a\in\ell^2\setminus\ell^1$、$a_j\ge0$，
$c_j\in\mathbb R$、$|c_j|\le C_0a_j$。

设正系数的下降重排满足：存在 $h>0,n_0$，使
$$
a_n^*\ge h/n\qquad(n\ge n_0),
\tag{1.1}
$$
并假设
$$
\boxed{C_0<2\pi h.}
\tag{1.2}
$$
这个严格充分界来自下文舍去有限物理头后可任意逼近1的局部衰减率；不称必要条件或最优阈值。

对
$$
G(x,s)=s^m+\sum_{\substack{i+j\le m\\j<m}}g_{ij}x^is^j,
\qquad m\ge1,\quad g_{ij}\in\mathbb C,
$$
仍有对任意 $\lambda\in\mathbb C$、整数 $r\ge1$、
任意复 $\ell^2$ 指数权 $w$，
$$
\boxed{[G(u,v-u^2)-\lambda]^r e^w\text{ 循环}.}
\tag{1.3}
$$
允许任意物理排列。

特别
$$
u=\sum_{j\ge0}\frac{\chi_j}{j+1},\qquad
v=\sum_{j\ge0}\frac{(-1)^j\chi_j}{j+1}
$$
有 $h=C_0=1$，严格满足 (1.2)。
因此对所有 $\beta,\lambda\in\mathbb C$、全部 $r\ge1,w$，
$$
\boxed{[(v-u^2)^2-\beta u^2-\lambda]^r e^w\text{ 循环},}
\tag{1.4}
$$
包括原来真实的 $\beta=4$ 碰撞。
本稿处理的是 $\sigma=1$，不重复前稿 $1/2<\sigma<1$ 的有限阶范围。

更一般，下文只需要正主行的实际半群给某个 $k>0$ 的预算
$$
\|(X-z)^{-1}\|\le C\exp[C e^{(\operatorname{Re}z)_+/k}],
\qquad C_0<2\pi k.
\tag{1.5}
$$
(1.1)—(1.2) 将通过所有 $k<h$ 的真实预算来验证它。

### 1.1 无须逐项谐和下界的原生计数判据

更一般，令
$$
\Lambda_a=\limsup_{t\to\infty}
\frac{\Theta_a(t)}{t\log t}\in[0,\infty].
$$
只要
$$
\boxed{\Lambda_a>C_0/(2\pi),}
\tag{1.6}
$$
同一个全部点态幂结论 (1.3) 成立。
它不要求下降重排逐项大于 $h/n$。
证明在 §§3.1、7.1 给出，只需一列远端矩形。

特别 $\Lambda_a=\infty$ 时允许任意有限辅助支配常数 $C_0$；
此前 $\Theta_a(t)\ge\gamma t^p,\ p>1$ 的有限阶范围自动满足它。
$\Lambda_a=0$ 不满足 (1.6)，不能据此称全部正非可和主行都已解决。

### 1.2 实斜率、有限物理头及可和余项

结论还允许存在 $\gamma\in\mathbb R$、$d\in\ell^1(\mathbb R)$、$C\ge0$，使
$$
|c_j-\gamma a_j-d_j|\le Ca_j,\qquad C<2\pi\Lambda_a.
\tag{1.7}
$$
这里先保留原点态多项式的完整 Bell 最大实现。令 $b_j=c_j-\gamma a_j-d_j$，并取三个规范 first $X=X_{\sum a_j\chi_j}$、$Y=X_{\sum c_j\chi_j}$、$Y'=X_{\sum b_j\chi_j}$。在共同混合深域上有
$$
Y=Y'+\gamma X+X_d,\qquad X_d=\sum_jd_jV_j\in\mathcal A.
$$
$X_d$ 是按算子范数收敛的实际有界 first。把 $X,Y,Y'$ 同时纳入 R186 的有限共同正则器，足够深的固定正则幂是两组规范最大实现的共同图核心。下面的替换先在该深域成立，再由共同图核心识别完整最大闭图；不要求一阶自然和在原交域上已经闭。把 $Y=Y'+\gamma X+X_d$ 代入完整 Bell 式，只把剪切变量改为 $s+\gamma x+X_d$；总次数不增，$s^{mr}$ 仍首一，有界系数仍在原局部代数内。因此 §4 的相伴图改用 $X,Y'$，两个正 first 使用支配常数 $C$，其余证明不变。结论仍是原来指定的普通点态向量，不把 $X_d$ 误作点态乘法。

有限头误差是 $d$ 有限支撑的特例。尾实比值 $c_j/a_j$ 有有限上下极限时，可取其中点 $\gamma$ 和任意略大于半振幅的 $C$，只在严格阈值内使用；不假定下确界取到。$a_j=0$ 的尾位必须由 $d$ 支付，对应的 $c_j$ 须绝对可和，不能免费删去。

## 2. 时间100的逐位严格收缩

记 $K_j=V_j-I=-2N_j(I+N_j)^{-1}$。
实际恒等式 $N_j^2=\eta_jN_{j+1}$、$\|(I+N_j)^{-1}\|<3$ 给
$$
\|K_j\|\le6,\qquad \|K_j^2\|\le36\eta_j.
$$
置 $q_j=6\sqrt{\eta_j}$。对偶、奇幂分别求和，
$$
\begin{aligned}
\|e^{-sK_j}\|
&\le\cosh(sq_j)+(6/q_j)\sinh(sq_j)\\
&\le(1+6s)e^{sq_j}.
\end{aligned}
$$
所以
$$
\|e^{-sV_j}\|\le(1+6s)e^{-(1-q_j)s}.
\tag{2.1}
$$
原权 $\eta_j\le e^{-770\cdot16^j}$ 保证
$$
\|e^{-100V_j}\|
\le601e^{-100+600e^{-385}}<e^{-90}.
\tag{2.2}
$$
同时 $V_j$ 增生，任意正时间余数的半群仍收缩。
把 $s$ 写成 $100\lfloor s/100\rfloor$ 加余数，得到
$$
\boxed{\|e^{-sV_j}\|\le e^{-90\lfloor s/100\rfloor}.}
\tag{2.3}
$$

令 $X=X_{\sum a_j\chi_j}$。
与计数半群附录同样，对任意有限选位清出真实有界头，
剩余正尾最大增生且域交换，得到完整半群分解。
因此
$$
\boxed{
\|e^{-tX}\|\le
\exp[-90\Theta_a(t/100)],\qquad
\Theta_a(s)=\sum_j\lfloor sa_j\rfloor.
}
\tag{2.4}
$$
全部 carry 已在 (2.1)—(2.2) 支付；没有使用纯张量替换。

### 2.1 舍去有限头后把局部率任意逼近1

固定任意 $0<\kappa<1$。
先选固定有限 $T>0$ 使
$$
\frac{\log(1+6T)}{T}<\frac{1-\kappa}{2},
$$
再选固定物理头长 $J$，使
$$
6\sqrt{\eta_j}<\frac{1-\kappa}{2}\qquad(j\ge J).
$$
由 (2.1)，
$$
\|e^{-TV_j}\|\le e^{-\kappa T}\qquad(j\ge J).
$$
使用收缩余数及任意有限选位的真实半群分解，
$$
\boxed{
\|e^{-tX}\|
\le\exp\!\left[-\kappa T
\sum_{j\ge J}\lfloor ta_j/T\rfloor\right].
}
\tag{2.5}
$$
有限头保持为收缩因子，没有给出正指数范数损失。

删去的计数满足
$$
0\le\Theta_a(t/T)-\sum_{j\ge J}\lfloor ta_j/T\rfloor
=\sum_{j<J}\lfloor ta_j/T\rfloor
\le(t/T)\sum_{j<J}a_j=O(t).
\tag{2.6}
$$
因此即使物理排列任意，删去有限物理头也只改变线性 $t$ 项，
不改变谐和排序的 $h(t/T)\log t$ 主项。

## 3. 谐和排序下的双指数型实际预解

固定 §2.1 的 $T,J,\kappa$，令 $s=ht/T$、$N=\lfloor s\rfloor$。
由 (1.1)，对充分大的 $t$，
$$
\begin{aligned}
\Theta_a(t/T)
&\ge\sum_{n=n_0}^{N}\lfloor s/n\rfloor\\
&\ge s\sum_{n=n_0}^{N}n^{-1}-(N-n_0+1)\\
&\ge s\log s-C s.
\end{aligned}
$$
结合 (2.5)—(2.6)，存在有限 $C_1,C_2$，使
$$
\boxed{
\|e^{-tX}\|
\le C_1\exp[-k_0t\log t+C_2t]\qquad(t\ge1),
\quad k_0=\kappa h.
}
\tag{3.1}
$$
短时间仍用收缩界。

给任意 $0<k<h$，先选择 $k/h<\kappa<1$，于是 $k<k_0=\kappa h$。标量最大值计算给
$$
(r+C_2)t-k t\log t
\le k\exp((r+C_2)/k-1)\qquad(r,t\ge0).
$$
把 (3.1) 的 $k_0t\log t$ 分为 $kt\log t$ 和
$(k_0-k)t\log t$，剩余一项在 $t\ge1$ 可积。
实际全平面 Laplace 预解于是满足
$$
\boxed{
\|(X-z)^{-1}\|
\le C_k\exp[C_k e^{(\operatorname{Re}z)_+/k}].
}
\tag{3.2}
$$
这里增长只依赖 $\operatorname{Re}z$。
特别对每个固定 $b\in\mathbb R$，存在有限
$$
M(b)=\int_0^\infty e^{bt}\|e^{-tX}\|\,dt
$$
使
$$
\sup_{\operatorname{Re}z\le b}\|(X-z)^{-1}\|\le M(b).
\tag{3.3}
$$
(3.2) 不是有限阶；后文明确使用它的指数型速率 $1/k$。

所有这些预算直接传到有限对角放大及保持原正预解的闭限制。
下面的等价范数步骤还会保持原半群范数上界，不重新放大它的衰减常数。

### 3.1 原生 limsup 计数判据：只在一列竖半面付预算

若 (1.6) 成立，选固定参数
$$
C_0/(2\pi)<k'<k<\kappa h<h<\Lambda_a,\qquad 0<\kappa<1.
\tag{3.4}
$$
$\Lambda_a=\infty$ 时仍只取有限 $h$。
再按 §2.1 固定 $T,J$。
由 limsup，有 $s_n\to\infty$ 使
$$
\Theta_a(s_n)\ge h s_n\log s_n.
$$
令 $\tau_n=T s_n$。
有限物理头的删除只扣 $O(\tau_n)$，故充分大 $n$ 有
$$
q_n:=\|e^{-\tau_nX}\|
\le \exp[-k\,\tau_n\log\tau_n].
\tag{3.5}
$$
这里没有推断所有时间都满足同一 $t\log t$ 预算。

置 $r_n=k'\log\tau_n>0$。
使用半群性和短时间收缩，将真正 Laplace 积分按长度 $\tau_n$ 分块：
对 $\operatorname{Re}z\le r_n$，
$$
\begin{aligned}
\|(X-z)^{-1}\|
&\le\sum_{\ell\ge0}q_n^\ell e^{r_n\ell\tau_n}
 \int_0^{\tau_n}e^{r_nt}\,dt\\
&=\frac{e^{r_n\tau_n}-1}
 {r_n(1-q_ne^{r_n\tau_n})}
\le\frac{2e^{r_n\tau_n}}{r_n}
\end{aligned}
\tag{3.6}
$$
当 $n$ 足够大，因
$q_ne^{r_n\tau_n}\le
\exp[-(k-k')\tau_n\log\tau_n]\to0$。
所以 (3.6) 是一列完整竖半面上的统一算子预算，
不要求各列之间的增长控制。

另外，所有正非可和主行早已满足
$\Theta_a(t)/t\to\infty$；
其真实半群比每个固定指数更快衰减。
因此 (3.3) 的每个固定 $M(b)$ 仍有限。
§6 第二因子所需的固定竖半面界可照用，
无需由 (3.6) 冒充全平面双指数界。

对原生判据，§6 取 $C_0<c<2\pi k'$，
再按相同次序取小 $\varepsilon,b$ 及
$c/(2\sqrt2)+b/2<a<\pi k'/\sqrt2$。
最后改用 §7.1 的序列最大模论证。
所有参数先固定，再令 $n\to\infty$。

## 4. 相伴矩阵的有限谱在原闭图上确实成立

前一相伴矩阵附录已完整证明：
若指定普通 Bell 最大实现有非零核，
存在非零闭空间 $\mathcal M\subset H^d$、$d=mr$，满足：

1. $\mathcal M$ 保持所有对角 $A'$；
2. 正 first 的真实部分 $\mathbb X_{\mathcal M}$ 最大增生、空谱，
   预解为原对角预解的限制；
3. 有界相伴矩阵 $\mathcal C$ 保持 $\mathcal M$，且
$$
\operatorname{Dom}\mathbb Y_{\mathcal M}
=\operatorname{Dom}\mathbb X_{\mathcal M}^2,\qquad
\mathbb Y_{\mathcal M}
=\mathbb X_{\mathcal M}^2+J\mathbb X_{\mathcal M},
\quad J=\mathcal C|_{\mathcal M};
\tag{4.1}
$$
4. 对任意 $c>C_0$，两个真实正 first 部分
$$
\pm\mathbb X_{\mathcal M}^2+(cI\pm J)\mathbb X_{\mathcal M}
\tag{4.2}
$$
在准确平方域上均最大增生。

还须验证 $J$ 只有有限谱，不能从相伴矩阵的形式形状直接赠送。
前稿的有界归一化多项式
$$
Q(z)=z^d+\sum_{j<d}A_jz^j
$$
全部系数实际属于局部闭交换代数
$$
\mathfrak B=\overline{\operatorname{alg}}(I,\mathcal A,L),
\quad L=X^{-1}.
$$
倾斜项属于 $\mathcal A$，字符只保留相应常数；
$L$ 拟幂零，所以 $\mathfrak B$ 的唯一字符 $\phi$ 满足 $\phi(L)=0$。
故
$$
H(z)=z^d+\sum_{j<d}\phi(A_j)z^j
$$
是一个非零首一标量多项式。

若 $H(\zeta)\ne0$，则 $Q(\zeta)\in\mathfrak B$ 为单位。
相伴矩阵的有限 Cayley–Hamilton 余式或有限矩阵消元公式给
$(\mathcal C-\zeta I)^{-1}$；
更具体，它是 $\mathcal C$ 的有限多项式，
系数由对角 $A_j$ 和对角 $Q(\zeta)^{-1}$ 组成。
这些系数和 $\mathcal C$ 都保持 $\mathcal M$，
所以逆也保持 $\mathcal M$。
因此
$$
\boxed{\sigma(J)\subseteq H^{-1}(0).}
\tag{4.3}
$$
这是实际限制上的完整逆结论，不是从全空间谱免费传给限制。

在非零 $\mathcal M$ 上至少有一个非零 Riesz 谱子空间
$\mathcal K$，其上
$$
J=\omega I+N,\qquad \sigma(N)=\{0\}.
\tag{4.4}
$$
所有对角 first 预解都与 $J$ 交换，因而与这些 Riesz 投影交换；
故 $\mathcal K$ 保持它们。
§4 的正性、真实域、全部空谱预解以及 (3.2)—(3.3) 因而在
$\mathcal K$ 上仍成立。
以下把 $\mathbb X_{\mathcal K}$ 简写为 $Z$。

## 5. 只缩小拟幂零部分的等价 Hilbert 范数

给定 $\varepsilon>0$，定义
$$
\|f\|_\varepsilon^2
=\sum_{n=0}^\infty\varepsilon^{-2n}\|N^nf\|^2.
\tag{5.1}
$$
$N$ 拟幂零，故级数在算子范数中收敛；
零项给下界 $\|f\|_\varepsilon\ge\|f\|$，
所以它是等价 Hilbert 范数。
并且
$$
\|Nf\|_\varepsilon^2
=\varepsilon^2(\|f\|_\varepsilon^2-\|f\|^2)
\le\varepsilon^2\|f\|_\varepsilon^2.
\tag{5.2}
$$

若有界 $S$ 与 $N$ 交换，则逐项有
$$
\boxed{\|S\|_\varepsilon\le\|S\|_{\rm old}.}
\tag{5.3}
$$
因此全部与 $N$ 交换的正 first 收缩半群仍收缩；
$Z$ 的原半群范数预算 (3.1) 也保持相同上界。
等价范数不改变闭域、空谱或真实因式。
正 first 部分仍最大增生，(3.2)—(3.3) 的界也不增大。

这一点使下面选择 $\varepsilon$ 不存在循环：
用于控制第二因子的 $M(b)$ 可以先由原半群固定，
然后任意缩小 $\varepsilon$。

## 6. 精确的小宽半条带

由 (1.2) 选
$$
C_0<c<2\pi k,\qquad 0<k<h.
\tag{6.1}
$$
在 $\mathcal K$ 的范数 (5.1) 下，两个真正最大增生算子为
$$
T_+=Z^2+(c+\omega+N)Z,\qquad
T_-=-Z^2+(c-\omega-N)Z
\tag{6.2}
$$
域均为 $\operatorname{Dom}Z^2$。

写 $z=x+iy$、$R=|z|$，
$$
q_+(z)=z^2+(c+\omega)z,\qquad
q_-(z)=-z^2+(c-\omega)z.
$$
准确二次因式是
$$
\begin{aligned}
F_+(z)&:=T_+-q_+(z)I-Nz
=(Z-z)(Z+z+c+\omega+N),\\
F_-(z)&:=T_--q_-(z)I+Nz
=-(Z-z)(Z+z-c+\omega+N).
\end{aligned}
\tag{6.3}
$$

对 $x\ge-1$，第二因子未加 $N$ 时的标量预解参数
$-z\mp c-\omega$ 的实部不超过
$$
b_0=1+c+|\operatorname{Re}\omega|.
$$
由 (3.3)、(5.3)，这两预解的范数至多同一个固定 $M(b_0)$。
先取
$$
\varepsilon<\frac1{2M(b_0)}.
\tag{6.4}
$$
Neumann 公式遂使两个实际第二因子都有逆，范数至多 $2M(b_0)$。
这里不需要取 $c>\|J\|$，也不把第二因子的实部粗估成 $c-\|J\|$。

再取任意 $b>\varepsilon$。
若 $-\operatorname{Re}q_\pm(z)\ge b(R+1)$，
最大增生预解及扰动 $\pm Nz$ 的准确 Neumann 界给
$$
\|F_\pm(z)^{-1}\|
\le[(b-\varepsilon)R+b]^{-1}.
\tag{6.5}
$$
同前一条带引理的有界预解恒等式，
$$
\begin{aligned}
(Z-z)^{-1}
&=(Z+z+c+\omega+N)^{-1}
 +(2z+c+\omega+N)F_+(z)^{-1},\\
(Z-z)^{-1}
&=(Z+z-c+\omega+N)^{-1}
 -(2z-c+\omega+N)F_-(z)^{-1}.
\end{aligned}
\tag{6.6}
$$
因此 $(Z-z)^{-1}$ 在这些区域统一有界。
$x\le-1$ 由 $Z$ 增生直接控制。

未控制的大点只可能满足 $x\ge-1$ 和
$$
|\operatorname{Re}(z^2+\omega z)|
\le c x+b(R+1).
\tag{6.7}
$$
若右边为负，则该点根本不在此集合。
(6.7) 首先给 $|x-|y||=O(1)$；
因为 $x\ge-1$，大点只能靠近两条向右的对角射线。
置
$$
z=e^{i\theta}(t+is)-\omega/2,\qquad
\theta=\pi/4\ \hbox{或}\ -\pi/4.
$$
先用 $t\ge R/\sqrt2-O(1)$ 与 (6.7) 得 $s=O(1)$，
再有 $R/t\to1$、$x/t\to1/\sqrt2$。
而
$$
\operatorname{Re}(z^2+\omega z)
=\mp2ts-\operatorname{Re}(\omega^2)/4.
$$
除以 $2t$，得到所有未控制大点满足
$$
|s|\le\frac{c}{2\sqrt2}+\frac b2+o(1).
\tag{6.8}
$$
这些 $O(1)$、$o(1)$ 对该集合统一。

由于 $c<2\pi k$，可以先把 $\varepsilon$ 再缩小、再选 $b>\varepsilon$，
最后选择固定半宽 $a$ 使
$$
\boxed{
\frac{c}{2\sqrt2}+\frac b2<a<\frac{\pi k}{\sqrt2}.
}
\tag{6.9}
$$
于是除固定圆盘外，全部未控制点落在两条平移半条带
$$
z=e^{i\theta}(t+is)-\omega/2,\quad t\ge t_0,\quad |s|\le a.
\tag{6.10}
$$
两长边 $s=\pm a$ 的主项给
$-\operatorname{Re}q_\pm=(2a-c/\sqrt2)t+O(1)>b(R+1)$，
所以它们由 (6.5)—(6.6) 控制；短边紧致。
因此这些半条带的三条边及其外部均有统一预解界。

## 7. 双指数型预算仍被该半条带障碍压住

由 (3.2)，在 (6.10) 中
$$
\log\|(Z-z)^{-1}\|
\le C_{\omega,a}\exp[t/(k\sqrt2)].
\tag{7.1}
$$
(6.9) 允许选择
$$
\frac1{k\sqrt2}<\beta<\frac{\pi}{2a}.
$$
对任意单位 $f,g$，
$$
\psi(w)=
\langle (Z-e^{i\theta}w+\omega/2)^{-1}f,g\rangle
$$
在半条带上解析，三边有统一界。
乘上
$$
\exp[-\delta\cosh(\beta(w-t_0))],\qquad \delta>0.
$$
在闭条带内，其实部障碍至少为
$\cos(\beta a)\cosh(\beta(\operatorname{Re}w-t_0))$，
而 $\cos(\beta a)>0$。
远端竖边上，这个障碍按 $e^{\beta t}$ 增长，
严格压过 (7.1) 的 $e^{t/(k\sqrt2)}$。
在有限矩形应用最大模原理，先送远端到无穷，再令 $\delta\downarrow0$，
得到整条半条带上的相同界。

两条半条带均如此处理。
故所有预解矩阵元在全平面有界。
负实轴上的增生预解界使它们趋零，
Liouville 遂给 $(Z-z)^{-1}=0$，
与非零 $\mathcal K$ 上真实逆矛盾。

所以前稿的放大核图不能非零，原 Bell 最大核也为零。
原 $H$ 上完整 $C$ 自伴和指定指数向量的混合图核心，
将它准确转回 (1.3)—(1.4) 的循环性。

### 7.1 limsup 版本的远端矩形序列

继续 §3.1 的记号。固定一个平移斜半条带
$$
z=e^{i\theta}(w)-\omega/2,\qquad
\operatorname{Re}w\ge t_0,\quad |\operatorname{Im}w|\le a.
$$
选择
$$
\frac1{\sqrt2\,k'}<\beta<\frac{\pi}{2a}.
$$
令远端实部
$$
L_n=\sqrt2\,r_n-a-|\operatorname{Re}\omega|-1.
$$
它趋于无穷，且在 $\operatorname{Re}w=L_n$、
$|\operatorname{Im}w|\le a$ 上，实际 $z$ 的实部均不超过 $r_n$。
(3.6) 因而给
$$
\log\|(Z-z)^{-1}\|\le r_n\tau_n+O(1).
\tag{7.2}
$$
这个预算经 Riesz 限制及 (5.3) 的等价范数仍不增加。

对 §7 同一个障碍函数，
$$
\cosh(\beta(L_n-t_0))
\ge c_\beta\,\tau_n^{\beta\sqrt2\,k'}
$$
当 $n$ 大时成立。
因为 $\beta\sqrt2\,k'>1$，
$$
r_n\tau_n-\delta c_\beta\cos(\beta a)
 \tau_n^{\beta\sqrt2\,k'}\longrightarrow-\infty
$$
对每个固定 $\delta>0$ 成立。
所以乘障碍后的矩阵元在这一列远端竖边上一致趋零。
每个有限矩形的其余三边照旧有统一界，
最大模原理沿 $L_n\to\infty$ 给整个半条带的同界。
再令 $\delta\downarrow0$，得到 §7 相同的全平面有界性和 Liouville 矛盾。

因此 (1.6) 的 $\limsup$ 已足够；
没有把一次选到的好时间扩张成全尾同阶半群衰减，
也没有要求未知核向量的任何收敛速度。

## 8. 界线

本稿实际新增谐和下界与 (1.2)、以及原生计数条件 (1.6) 的范围，
不把一般非可和主行都称为双指数型预算。
尤其 $a_n\asymp1/(n\log n)$ 不由本稿证明的 (3.1) 覆盖。

任意复指数权与所有固定点态幂均保留：
倾斜和 Bell 只改变局部代数内有界系数，
有限谱分支及等价范数步骤明确支付这些系数。
没有把普通点态幂换成自然幂，也没有把整个放大交换子不变性赠给未知图。
严格界 $C_0<2\pi h$ 为本证明的明确充分条件，不称必要条件或最优阈值。
