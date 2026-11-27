# R271 附录：稀疏真核注入的全空间稠密向后链与实际迹类拟亲和

日期：2026-11-27（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127 / stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

固定原两型之一 $T=T_N,T_Y$，以及原负整数边界移位 $B$、$S=B^*$。本稿使用[同一个全物理尺度右逆](R271-appendix-single-actual-right-inverse-on-all-physical-exponential-scales.md)，并继续[原方向与迹类构造](R271-appendix-actual-directional-intertwiner-exclusion-and-trace-class-rosenblum-solutions.md)。新增的是一个固定的、在整个 $H$ 稠密的真向后链，其增长仍只有三次指数；由它得到从 $B$ 到完整 $T$ 的迹类拟亲和。

这不是把[固定闭右逆的真单链子空间](R271-appendix-proper-single-chain-restriction-and-common-trace-class-intertwiner-range.md)宣称为 $H$。下面在稀疏高度加入真实核向量，改变了整条链；第 6 节给出其移级关系的准确非闭性。

## 1. 同一个实际右逆与可计量的真核根

固定 $\lambda>\kappa_0=2+2\log(3/2)$，并令
$$
G=(I-P_0)\mathcal G_\lambda,\qquad P_0=e_0\otimes e_0.
$$
沿用原物理尺度
$$
\|v\|_\kappa=\sum_{p\ge0}e^{\kappa p}\|P_pv\|,
\qquad
\mathcal E_\infty=\bigcap_{\kappa\ge0}X_\kappa.
$$
同一 $G$ 满足
$$
TG=I,\qquad P_0G=0,\qquad G\mathcal E_\infty\subset\mathcal E_\infty.
$$
这里 $G$ 只在原已付的尺度域上使用，没有称为全 $H$ 有界算子。

前稿的迭代域链给：若 $v$ 的物理孔数至多 $P$，则对 $r\ge1$
$$
\|G^rv\|_\kappa
\le\sqrt{P+1}\,
\exp\!\left[A_\kappa r^3+(\kappa+r\lambda)P\right]\|v\|,
\tag{1.1}
$$
其中 $A_\kappa<\infty$ 只依赖固定的 $G,\kappa$，可把它们增大到至少一。$r=0$ 时使用
$\|v\|_\kappa\le\sqrt{P+1}e^{\kappa P}\|v\|$。

在 $\mathcal E_\infty$ 上置
$$
\Pi=I-GT,\qquad p_r=G^re_0,\qquad k_i=\Pi e_i\quad(i\ge1).
\tag{1.2}
$$
原 $T$ 保持有限整数支撑，并严格降低最高整数坐标。因此 $Te_i$ 支撑于 $0,\ldots,i-1$，而 $e_i,Te_i$ 的物理孔数均至多 $i$。准确有
$$
Tk_i=0,\qquad P_0k_i=0,\qquad k_i\in M\cap\mathcal E_\infty\subset N,
\quad M=\ker T,\quad N=\overline{BM}.
\tag{1.3}
$$
最后一个包含使用既有真实平滑核结论；下文不要求 $G$ 保持 $N$。

由 (1.1) 和
$G^rk_i=G^re_i-G^{r+1}Te_i$，可固定 $a\ge1$ 及
$$
d_i=1+\lambda i+\log\!\left[(1+\|T\|)\sqrt{i+1}\right]\ge i
$$
使全部 $r\ge0$ 满足
$$
\boxed{
\|p_r\|\le e^{a(r+1)^3},\qquad
\|G^rk_i\|\le e^{a(r+1)^3+d_i(r+1)}.
}
\tag{1.4}
$$
每个固定 $\kappa\ge0$ 另有 $a_\kappa\ge1$，并可取
$b_\kappa=1+\kappa/\lambda$，使
$$
\boxed{
\|p_r\|_\kappa\le e^{a_\kappa(r+1)^3},\qquad
\|G^rk_i\|_\kappa
\le e^{a_\kappa(r+1)^3+b_\kappa d_i(r+1)}.
}
\tag{1.5}
$$
这些界来自同一个 $G$；所有 $i$ 的三次首项常数共同，来源 $i$ 只进入较低阶费用 $d_i$。

## 2. 一次选定的稀疏注入及统一三次增长

令
$$
i_j=1+v_2(j)\qquad(j\ge1).
$$
每个正整数 $i$ 在此序列出现无穷多次。递归选择正整数 $N_j$ 和正数 $c_j$，约定 $N_0=0$。

已经选定前 $j-1$ 项时，对整数 $N>N_{j-1}$ 定义
$$
A_j(N)=e^{a(N+j+1)^3}
+\sum_{\ell<j}c_\ell
e^{a(N+j-N_\ell+1)^3+d_{i_\ell}(N+j-N_\ell+1)}.
\tag{2.1}
$$
选择 $N_j$ 足够大，使
$$
N_j\ge j,\qquad N_j^2\ge d_{i_j},\qquad
N_j>N_{j-1}+j-1,
\tag{2.2}
$$
以及
$$
2^j(1+A_j(N_j))\le e^{2aN_j^3}.
\tag{2.3}
$$
然后固定
$$
c_j=2^j(1+A_j(N_j)).
\tag{2.4}
$$

这个递归确实可进行。每一阶段只有有限个旧项，且其 $c_\ell,N_\ell,d_{i_\ell}$ 已固定；故
$$
\lim_{N\to\infty}
\frac{\log[2^j(1+A_j(N))]}{N^3}=a<2a.
$$
因此 (2.3) 在所有充分大 $N$ 成立，能与 (2.2) 同时满足。没有通过未知真核投影或未付源范数选择高度。

现在一次定义
$$
\boxed{
u_n=p_n+\sum_{j:N_j\le n}c_jG^{n-N_j}k_{i_j}
\qquad(n\ge0).
}
\tag{2.5}
$$
每个和有限，故 $u_n\in\mathcal E_\infty$。新注入项在其首高度属于真实 $\ker T$，其后使用合法的 $TG=I$，所以
$$
\boxed{
u_0=e_0,\qquad Tu_n=u_{n-1}\ (n\ge1),\qquad
P_0u_n=\mathbf1_{\{n=0\}}e_0.
}
\tag{2.6}
$$

统一增长也已经支付。若 $N_j\le n$，令 $r=n-N_j$，由 (1.4)、(2.2)–(2.4)
$$
\log\!\left(c_j\|G^rk_{i_j}\|\right)
\le2aN_j^3+a(r+1)^3+N_j^2(r+1)
\le2a(n+1)^3.
\tag{2.7}
$$
最后一步用 $a\ge1$ 及 $N_j+(r+1)=n+1$ 展开右侧。至多有 $n$ 个注入项，因此
$$
\boxed{\|u_n\|\le e^{(2a+1)(n+1)^3}.}
\tag{2.8}
$$
同理，(1.5) 给每个固定 $\kappa$ 的共同有限常数 $C_\kappa$，例如
$C_\kappa=2a+a_\kappa+b_\kappa+1$，使
$$
\boxed{\|u_n\|_\kappa\le e^{C_\kappa(n+1)^3}\qquad(n\ge0).}
\tag{2.9}
$$
链、注入高度和系数不随 $\kappa$、未来来源 $y$ 或 $w$ 改变。

## 3. 真正的全空间稠密性

置 $V=\overline{\operatorname{span}}\{u_n:n\ge0\}$。对于
$0\le r\le j$，下一个注入尚未发生，因为
$N_{j+1}>N_j+j$。由 (2.1)、(2.4) 得准确逼近
$$
\boxed{
\left\|\frac{u_{N_j+r}}{c_j}-G^rk_{i_j}\right\|
\le2^{-j}.
}
\tag{3.1}
$$
这里保留并估计了整个旧链，不把它删去。

固定 $i,r$，沿 $i_j=i$ 且 $j\ge r$ 的无穷子列令 $j\to\infty$，得到
$$
G^rk_i\in V\qquad(i\ge1,r\ge0).
\tag{3.2}
$$
再从 (2.5) 减去其中有限个已属于 $V$ 的注入项，得到
$p_n=G^ne_0\in V$。

最后，任意有限整数支撑 $v$ 有某个 $q$ 满足 $T^qv=0$。逐次使用
$I=\Pi+GT$ 而不交换 $G,T$，得到有限恒等式
$$
v=\sum_{r=0}^{q-1}G^r\Pi T^rv.
\tag{3.3}
$$
每个 $T^rv$ 仍为有限整数支撑；$\Pi e_0=e_0$，而
$\Pi e_i=k_i$。由 (3.2) 和全部 $p_n\in V$，(3.3) 的每项均属于 $V$。
有限整数支撑在 $H$ 稠密，所以
$$
\boxed{V=H.}
\tag{3.4}
$$
这一步未声称 $M\cap\mathcal E_\infty$ 在 $M$ 稠密；(3.3) 中含全部 $G^r$ 原像，不能只保 $r=0$。

## 4. 全部非零来源的实际稠密像与一个迹类拟亲和

沿用内积对第一变量线性以及
$(u\otimes v)x=\langle x,v\rangle u$。用刚才一次固定的链定义
$$
\boxed{\mathscr L_y=\sum_{n=0}^\infty u_n\otimes S^ny\qquad(y\in H).}
\tag{4.1}
$$
原移位已付
$$
\|B^n\|\le e^{-cn^4}\quad(n\ge2),\qquad c=95/32.
$$
与 (2.8)–(2.9) 合用，得到有限常数
$$
K_{\rm tr}=\sum_{n\ge0}\|u_n\|\|B^n\|<\infty,\qquad
K_\kappa=\sum_{n\ge0}\|u_n\|_\kappa\|B^n\|<\infty.
$$
所以 (4.1) 按迹范数绝对收敛，且
$$
\|\mathscr L_y\|_1\le K_{\rm tr}\|y\|,
\qquad
\|\mathscr L_y:H\to X_\kappa\|\le K_\kappa\|y\|.
\tag{4.2}
$$
后一个结论是原物理尺度上的实际有界映射；特别
$\mathscr L_yH\subset\mathcal E_\infty$。

由同一有限和的末项
$-u_N\otimes S^{N+1}y$ 趋零，准确有
$$
\boxed{
T\mathscr L_y=\mathscr L_yB,\qquad
P_0\mathscr L_y=e_0\otimes y,\qquad
\mathscr L_y^*e_0=y.
}
\tag{4.3}
$$
因此 $y\mapsto\mathscr L_y$ 为共轭线性，且
$$
\|y\|\le\|\mathscr L_y\|\le\|\mathscr L_y\|_1\le K_{\rm tr}\|y\|.
\tag{4.4}
$$

其核准确为
$$
\boxed{
\ker\mathscr L_y
=\left(\overline{\operatorname{span}}\{S^ny:n\ge0\}\right)^\perp.
}
\tag{4.5}
$$
确实，(4.3) 给
$P_0T^n\mathscr L_yx=e_0\langle x,S^ny\rangle$；
反方向直接用 (4.1) 的绝对收敛级数。

若 $y\ne0$，令 $k$ 是 $y$ 的最小非零整数坐标，并记
$\beta_0=1$、$\beta_j=\prod_{\nu=1}^j\alpha_{v_2(\nu)}>0$。
对每个 $r\ge0$，准确有限列为
$$
\mathscr L_y e_{k+r}
=\sum_{n=0}^r
\frac{\beta_{k+r}}{\beta_{k+r-n}}\,
\overline{y_{k+r-n}}\,u_n.
\tag{4.6}
$$
最高项的系数不为零。有限三角回代说明全部 $u_n$ 属于
$\operatorname{Ran}\mathscr L_y$ 的线性张成；由 (3.4)
$$
\boxed{\overline{\operatorname{Ran}\mathscr L_y}=H\qquad(y\ne0).}
\tag{4.7}
$$

特别，$S^ne_0=\beta_ne_n$，故 (4.5) 给 $\mathscr L_{e_0}$ 单射。
结合 (4.7) 与 (4.3)，得到实际全空间结论
$$
\boxed{
\mathscr L_{e_0}:H\to H
\text{ 是单射、稠密像的迹类算子，}\qquad
T\mathscr L_{e_0}=\mathscr L_{e_0}B.
}
\tag{4.8}
$$
也就是从 $B$ 到完整 $T$ 的拟亲和。已刊反向排除仍适用：
$XT=BX$ 的全 $H$ 有界解只有零。

还有可直接保留的紧性费用。用 (4.1) 的前 $n$ 项作秩至多 $n$ 的逼近，对每个固定
$0<c'<95/32$，存在 $K(c')<\infty$，使
$$
s_{n+1}(\mathscr L_y)\le K(c')e^{-c'n^4}\|y\|
\qquad(n\ge1).
\tag{4.9}
$$
因为三次项及该尾和被四次负项吸收。因而这些算子属于每个 Schatten 类
$\mathcal S_p$，$p>0$。不从这些小奇异值推像闭。

## 5. 同一个真实 W 来源的准确商作用

固定真正的 $w\in W=M\ominus N$。对 $m\in M$，所有 $n\ge1$ 有
$B^nm\in N$，故同一 (4.1) 逐项给
$$
\boxed{
\mathscr L_w|_M=e_0\otimes w,\qquad
\mathscr L_wN=0.
}
\tag{5.1}
$$
若 $w\ne0$，则
$$
\mathscr L_ww=\|w\|^2e_0,\qquad
\overline{\operatorname{Ran}\mathscr L_w}=H.
$$
它因此给出实际迹类的稠密像映射
$$
\widetilde{\mathscr L}_w:H/N\longrightarrow H
$$
并把商上的原 $B$ 交织到完整 $T$。这里用 $N$ 的 $B$ 不变性定义商作用；
没有声称此商映射单射，其在 $M/N\simeq W$ 上仍只是 (5.1) 的秩一映射。

这一结论扩大了此前固定目标 $U$ 的闭包像，但没有消去 $W$。
注入核确属 $N$，并不表示 $G^rk_i$ 也属 $N$；(2.5)、(3.3) 都保留这些实际原像。

## 6. 为什么不能把新链重新当成单个闭右逆轨道

由 (2.6)，$P_0T^r$ 逐个读取有限链的系数，故 $\{u_n\}$ 线性无关。
在其稠密线性张成上可定义移级算子
$$
J_{\rm ch}u_n=u_{n+1}.
$$
它满足 $TJ_{\rm ch}=I$ 和 $P_0J_{\rm ch}=0$，但其图闭包准确是关系
$$
\boxed{
\overline{\operatorname{Graph}J_{\rm ch}}
=\{(Tv,v):v\in e_0^\perp\}.
}
\tag{6.1}
$$
证明：图中的第二坐标恰遍历
$\operatorname{span}\{u_n:n\ge1\}$。由 (2.6)、(3.4)，此空间在
$e_0^\perp$ 稠密；映射 $v\mapsto(Tv,v)$ 有界且下界为一，故其像闭，
并给 (6.1)。

因此多值部为
$$
\{v:(0,v)\in\overline{\operatorname{Graph}J_{\rm ch}}\}
=M\cap e_0^\perp.
$$
原两型的 $M$ 无限维，故这个多值部非零。新 $J_{\rm ch}$ 不可闭，
不能拿它代替原同尺度定理的可闭 $G$。这一范围也说明：
新的全空间拟亲和不产生 $G$ 的全 $H$ 有界逆，不支付 Green 的实际除法源，
并不证明 $N=M$ 或普通 Hilbert ISP。
