# R38：二重腰圈、一般最低模核心与真实线性平尾

2026-11-12，constructive-route。

**状态：已证明的中间结论。** 第 1–3 节为完整代数结论，第 4 节给一个修改后的真实线性
二重平尾及其零二 jet。第 5 节列出尚未证明的完整非线性尾接口。
本文没有把 R72 的 $4\mathbb Z$ 定理授给 $2\mathbb Z$，
也没有从旧规范空间的无标签性推出一般 $C^2$ 不存在。

按用户新授权读取的正式源为 quantitative-newton-twist-flex：

- README，blob a5d4767b7289c0d8fb5c31ed91062eb62213110c；
- R72-large-width-inner-tail-to-cut128.md，
  blob a7c78793ba18724a4f0553b6ccd55259b8f4df92，尤其 §§2、7–9；
- R187-inner-high-window-green-full-tail-two-traces-and-fixed-collar.md，
  blob 7f21bd1797d2b2078c805e1a254e83594cd326af，尤其 §9。

下载内容的 Git blob SHA-1 与本仓库 HEAD 中的树逐一相同。
当前课题 R11 §7 已明确说明：第四模是为了使用已证明的
R72 全频非线性尾，不只是一个对称偏好。

## 1. 二重确实减小可见腰圈的曲率扰动

R33 的闭圈论证只需绕轴旋转 $\pi$ 和角反射，仍有
$\langle T\rangle=0$。取平面单位切向
$$
T_h=i e^{i\theta+i\beta\sin(2\theta)},\qquad
F_h=a\sum_{j\in\mathbb Z}
\frac{J_j(\beta)}{1+2j}e^{i(1+2j)\theta}.
$$
没有零分母，因 $1+2j$ 为奇数。由同一指数级数收集法，
$$
U_2=\frac{4a}{3}J_1(\beta),\qquad T_2=-U_2/2,\qquad
\kappa=(1+2\beta\cos2\theta)/a.
$$
$U_2/a=0.06$ 的唯一小根属于 $(.09,.091)$：
$J_1(.09)<.09/2$，而
$J_1(.091)>.091/2-.091^3/16>.045$，并用 R33 的严格单调性。
因此本腰圈有
$$
\kappa_{\min}>.818/a,\qquad \kappa_{\max}<1.182/a.
$$
与四重同幅下只保证 $\kappa_{\min}>.08/a$ 相比，这是实际的
二阶几何收益。但它只处理核心起点的幅度预算，没有解决两端。

## 2. Pöschl–Teller 核心的统一最低模公式

对整数 $n_0\ge2$、整数 $p\ge1$，令
$$
q=2n_0p+1,\qquad
\mu=\frac{n_0p^2}{q},\qquad
\nu=\frac{p(n_0p+1)}q.
$$
则
$$
\nu-\mu=p/q,\qquad \nu^2=\mu^2+\mu/n_0.
$$
因此
$$
L_n=-\partial_x^2-n^2(\nu^2\operatorname{sech}^2x-\mu^2)
$$
在 $n=n_0$ 有核
$y=\operatorname{sech}^{n_0\mu}x$。
令 $\ell_n=\sqrt{\nu^2n^2+1/4}-1/2$，
$c(n)=\sqrt{\nu^2n^2+1/4}-\nu n$；准确地
$$
\ell_{n_0}=n_0\mu,\qquad c(n_0)=1/(2q),
$$
并且
$$
\ell_n-\mu n-j=pn/q-j-1/2+c(n).
$$
$q$ 奇数，第一项到半整数至少相隔 $1/(2q)$。
$c$ 严格递减，所以 $n>n_0$ 无核；$n<n_0$ 则
$\ell_n<\mu n$，也无核。故唯一整数频率核为 $n_0$。
对 $n\in n_0\mathbb N$ 的非核谱，可逐项重复 R25 的谱因式分解，
得到线性谱隙
$$
|\lambda|>\mu n[c(n_0)-c(2n_0)].
$$
这里没有主张 R25 原来针对 $n_0=4$ 的具体逆常数原封不动。

二重具体选择 $n_0=2,p=11$ 给
$$
\mu=242/45,\quad \nu=253/45,\quad q=45.
$$
整个径向连续族 $\nu^2=\mu^2+\mu/n_0$ 保持最低核，并且正势作用量
$I=\pi(\nu-\mu)$ 满足
$$
\frac{dI}{d\mu}
=\pi\left(\frac{\mu+1/(2n_0)}{\nu}-1\right)
=\frac{\pi}{4n_0^2\nu(\mu+1/(2n_0)+\nu)}>0.
$$
这只是径向背景的真实计算，不能替代当前非径向返回图的参数导数。

## 3. 旧 R72 尾确实没有自由的二重线性标签

沿用 R72 的真实参数
$$
\delta_n=\frac2{25}2^{-n},\quad
\eta_n=\frac{\delta_n^{3/2}}{4\sqrt2},\quad
\epsilon\delta_n^6,\quad
p_*:1,\ 64/\delta,\ \delta/(65/64),\ 1/\delta,\ 64,
$$
三主平台各长 $\delta$，六个短段各长 $\eta$，
$r_y=r/\sqrt{12}$。共同状态和矩阵为
$$
W=(\nu_mQ,\pi),\quad Q=C/r^4,\quad
\pi=p_*\frac{C'/r^3-m^2Q}{\sqrt{12}},
$$
$$
\nu_m=m^2(m^2-1)/12,\quad k_m=(m^2-4)/\sqrt{12},\qquad
W_y=\begin{pmatrix}k_m&\nu_m/p_*\\-p_*&-k_m\end{pmatrix}W.
$$
末端除以 $64$ 的第二分量，得到端口矩阵 $B_{m,n}$。

在 $m=2$，$\nu_2=1,k_2=0$。三个理想剪切为
$$
P_-=\begin{pmatrix}1&0\\-64&1\end{pmatrix},\quad
C_*=\begin{pmatrix}1&65/64\\0&1\end{pmatrix},\quad
P_+=\begin{pmatrix}1&0\\-1&1\end{pmatrix}.
$$
所以准确的极限端口矩阵为
$$
\boxed{
B_{2,\infty}=
\begin{pmatrix}1&0\\0&1/64\end{pmatrix}P_+C_*P_-
=\begin{pmatrix}-64&65/64\\0&-1/4096\end{pmatrix}.
}                                                        \tag{3.1}
$$
两个特征值绝对值为 $64$ 和 $1/4096$。
R72 的规范指数是 $\zeta_n=\epsilon\delta_n^{39/4}$，
故其大分量因子变为
$$2^{-39/4}\,64\,e^{-2h_n}=2^{-15/4}e^{-2h_n}<1.$$
此模永远没有 R72 §8 所需的第一次越过 1 的标签层。

以下直接估计真矩阵，避免把 R72 只写给 $m\ge4$ 的界不加证明外推。
在 $m=2$ 的恒定平台，生成元平方为 $-I$，所以流的准确矩阵是
$$
\begin{pmatrix}
\cos\delta&p_*^{-1}\sin\delta\\
-p_*\sin\delta&\cos\delta
\end{pmatrix}.
$$
由 $|\cos\delta-1|\le\delta^2/2$、
$|\sin\delta-\delta|\le\delta^3/6$，三平台距上述三个剪切的
无穷矩阵范数分别不超过 $12\delta^2,2\delta^2,2\delta^2$；
实际平台范数分别小于 $66,3,3$。
六个短段满足
$$
\int\|A_2\|_\infty\,dy
\le6\eta(64/\delta)<68\sqrt\delta.
$$
当 $\delta\le2^{-56}$ 时，后者小于 $1/2$。逐段 Duhamel 或
乘积伸缩估计给短段的总差至多
$594(e^{68\sqrt\delta}-1)\le80784\sqrt\delta$；
三平台差的总费至多 $732\delta^2$。所以
$$
\|B_{2,n}-B_{2,\infty}\|_\infty<2^{17}\sqrt{\delta_n}<1.
$$
于是 $\|B_{2,n}\|_\infty<67$。由于 $2^{39/4}>768$，
真实规范矩阵满足
$$
\boxed{\|A_{2,n}\|_\infty
 =\|{-2^{-39/4}e^{-2h_n}B_{2,n}}\|_\infty<1/8.}          \tag{3.2}
$$
若 $X_{2,n}$ 在全部深层有界且满足齐次递推
$X_{2,n-1}=A_{2,n}X_{2,n}$，则对任意 $j$
$$
|X_{2,n}|\le8^{-j}\sup_{k\ge n}|X_{2,k}|,
$$
令 $j\to\infty$ 得 $X_{2,n}=0$。
因此在原 R72 规范球内，不能以一个非零二重一阶核接入这条尾。

这不证明所有 $C^2$ 二重尾都不存在。未规范的理想大分量
向深约以 $64^{-1}$ 衰减，即 $\delta^6$ 量级，绝对二阶
平坦与 R72 要求的相对于极小背景的小性是两个不同条件。
上面的无解范围准确是原 $\delta^{39/4}$ 强空间的齐次二重分量。
在完整 $2\mathbb Z$ 方程中，二重模也可由其它频率的非线性耦合
产生；这不产生一个自由的二重一阶标签。

## 4. 修改第一剪切后，确有真实线性二重平尾

保持 $\delta_n,\eta_n$、背景幅度 $\epsilon\delta_n^6$、
末端 profile 值 $64$ 和全部实际段长不变。仅取
$$
K=2048,\quad \alpha=(K+1)/K,\qquad
p_*:1,\ K/\delta,\ \delta/\alpha,\ 1/\delta,\ 64.
                                                               \tag{4.1}
$$
四次过渡仍使用原 log-quintic，故这是一个明确的真实背景。
末端值仍是 $64=2^6$，相邻胞的 $w=\epsilon\delta_n^6p_*/r^7$
继续准确匹配；不能把这个端因子也任意改成 $K$。

同一矩阵乘法给
$$
B_{2,\infty}^{(K)}
=\begin{pmatrix}-K&\alpha\\0&-1/(64K)\end{pmatrix}.       \tag{4.2}
$$
大规范因子为 $2^{5/4}e^{-2h_n}$。保留 R72 的
$h_n\le9/100$，则
$$
2^{5/4}e^{-2h_n}>
\frac94(1-9/50)=369/200>9/5,                            \tag{4.3}
$$
而小因子小于 $2^{-26}$。

真矩阵误差也可直接支付。六短段的积分至多
$2K\sqrt\delta$，三实际主平台范数分别小于 $K+2,3,3$。
重复 §3 的准确指数估计，粗取
$$
\|B_{2,n}^{(K)}-B_{2,\infty}^{(K)}\|_\infty
 \le64(K+2)^2\sqrt{\delta_n}<2^{30}\sqrt{\delta_n}.       \tag{4.4}
$$
该界在 $\delta\le2^{-56}$ 成立，且全部实际深尾层 $n\ge128$
有 $\delta_n<2^{-131}$。令
$$
E=\begin{pmatrix}1&t\\0&1\end{pmatrix},\qquad
t=\frac{\alpha}{K-1/(64K)}.
$$
则 $0<t<2/K$，$\|E\|,\|E^{-1}\|<2$，并精确对角化 (4.2)。
结合 (4.4)，规范实际矩阵在此基中距 (4.3) 的对角参考块
小于 $2^{-43}$。

对于参考递推，在 cut128 指定第一分量标签，向深取大分量的
收缩递推；小分量取未来收敛和。由 (4.3)，强 $\ell^\infty$
源的 Green 范数至多
$$
\max\{1/(9/5-1),\,1/(1-2^{-26})\}<2.
$$
真实矩阵差因而由 Neumann 级数吸收，因为 $2\cdot2^{-43}<1$。
这给一个非零标签对应的真实齐次二重线性解及有界规范序列 $X$，
而非只给理想剪切解。

它的物理二阶平坦可以直接证明。设 $\|X\|_\infty\le M$。
胞内真实流范数小于 $2^{16}$，$r\in[1,2]$、
$p_*\ge\delta/2$。于是
$$
|C|\le2^{20}\epsilon M\delta^{39/4},\qquad
|C'|\le2^{23}\epsilon M\delta^{35/4}.                     \tag{4.5}
$$
固定频率与有限绝对角宽给 $e^{-2\tau_n}\le1$，故上界已包含角权。
令 $b=(\log p_*)_y$。在本深区，
log-quintic 的最大导数 $15/8$ 给
$|b|\le64(1+|\log\delta|)\delta^{-3/2}$。
由 $Q_y=\xi$、$\xi_y=-Q-b\xi$，
$$
C''=r^2(7\sqrt{12}-12b)\xi,
$$
从而可取
$$
|C''|\le2^{29}\epsilon M(1+|\log\delta|)
                           \delta^{29/4}\longrightarrow0.       \tag{4.6}
$$
固定频率的角导数不损失这些衰减。选择镜像背景 $z_r=-w$
（不改诱导度量和高度线性方程），径向场由当前课题 R11 的
一般 $N$ 公式在 $N=2$ 处恢复：
$$
U=\frac{w}{3}(4C-rC'),\qquad T=-U/2,\qquad U_r=wC_r.
$$
其中 $w=O(\epsilon\delta^5)$、
$w_r=O(\epsilon(1+|\log\delta|)\delta^{7/2})$。
所以 $U,T$ 及其前两阶物理导数也趋零。将此真实线性等距场在
平领圈上延为零，得到 $C^2$ 零二 jet。

本节只证明修改背景上的**真实线性**二重平尾；没有证明它的
非线性全频标签 map、完整 mean 或与核心的两迹接线。

## 5. 完整非线性二重尾必须新增的支付

修改 (4.1) 不改变任何径向段长，因而 R187 §9 的几何无穷和
$$
r_{\rm flat}=r_{\rm cut0}
\exp\left[-\frac1{\sqrt{12}}
\left\{\frac6{25}+\frac3{125(2\sqrt2-1)}\right\}\right]
$$
不变。只要完整新尾构造完成，原 $[99/100,203/200)$ 固定常数
开领圈的半径余量仍可使用。这只是几何位置事实，不能先借它宣称
新非线性尾已经有零 residual。

尚须重新证明的接口具体为：

1. 将含 mean 的全角局部方程及 holonomy-one 小根放到
   $2\mathbb Z$ Wiener 代数。该空间是乘法代数，$m=1$ 仍被排除，
   $\nu_2=1\ne0$；但旧估计中的 $m^2/\nu_m<1$、
   $\sqrt8|m|/\nu_m<1$ 在 $m=2$ 不成立，须付真实有限常数。
2. 按新 $K$、$\alpha$ 重算胞内真流、低窗误差、全频高窗、
   实际强制修正、压缩逆和全部 log-jump 材料费。原端因子仍为64，
   不可把第一剪切与端因子误认为同一参数。
3. 对所有 $m\in2\mathbb Z$ 证明强 $\sum\sup$ Green 和标签 map；
   新二重参考线虽已由 §4 给出，$m=6,10,\ldots$ 也须进入同一
   全频证明，并处理常宽段的临界模。
4. 重付完整非线性递推的小球、二次常数、所有频率相互作用、
   唯一 mean 和全角两迹。§4 的一个线性标签不代替这些。
5. 重新匹配核心二重核的物理高度和径向迹，并重付 connector 的
   全频普通源逆、核外方向、有限幅几何和全局 reach/可见性。

因此目前的准确判断是：二重的可见腰圈确有更好的曲率余量，
旧 R72 尾不可直接使用；最低模障碍在旧归一化谱结构中，
并非一般 $C^2$ 或固定开帽的逻辑禁止。改变第一剪切提供了一个
可证明的线性修复，完整非线性代价尚未支付。
