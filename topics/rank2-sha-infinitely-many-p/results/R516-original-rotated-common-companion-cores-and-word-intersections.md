# R516 — 原三阶旋转的六条共同伴随核与完整词交域

日期：2026-11-14。**状态：已证明。** R513 的两条隐藏单轴核心经原三阶几何变换，产生六条保留原 $Y,W,W',W_2$ 的真实核心。六行张成一个准确的三维共同伴随空间；本篇给它的完整原框架、三阶作用、四态核心和任意正词像格。它们与 R510 的 $Y/B_{15}$ 平面压深逐项交换，因而能支付两个词域的真实交集。

范数计算得到的第三条正交基轴尚没有单轴核心；本篇没有把六条已付轴的张成空间自动当成已付的全三轴共同压深。原 $B_0$ 仍含会移动的 $Z/T_c$ 条件。

## 1. 同一完整来源及基础核心

保 R493、R509、R513 的全部原 ray、周期、CM 覆盖和有限坏集。特别保
$\pi_0\equiv2\bmod49$；可同时保 R515 的 $\pi_0\equiv1\bmod263$。
记
$$
\chi=\chi_{65},\quad\chi^2=1,\qquad
\lambda=-\bar\pi_0^{-1},\quad\kappa=p\lambda^2,
$$
$$
\rho=-\nu_\sigma^{\otimes6}/84,\qquad
\xi=(\xi_1,\xi_2,\xi_3,x,c,d_0)^t.
\tag{1}
$$
所有变换仍在原六输入上进行。

令 $Q_0,Q_b$ 为 R513 的实际两行：
$$
Q_0=Q_1+\omega Q_2,\qquad
Q_b=\gamma(5Q_2-qQ_0),\quad
q=(-29-4\delta)/7,\quad\gamma=(5+\delta)/2.
\tag{2}
$$
它们正交，范数为 $5,515$。R513 已用真正 odd245/25235 覆盖及固定 CM 拉回，支付两条单轴的绝对核心 $\chi\lambda$。
它们在四个实际来源 $(u,v,z,h)$ 上都成立，且对 $\rho=u-h/2$ 也成立。

令 $T$ 是 R512(2) 的实际三阶六维矩阵。
它保持 $Y$，并令
$$
WT=W',\quad W'T=W_2,\quad
W_2=-\omega^2W-\omega W'.
\tag{3}
$$
所以原三维观察空间
$$
\mathcal R=\operatorname{span}_K(Y,W,W')
\tag{4}
$$
在 $T$ 下不变。

## 2. 真正三维共同伴随的完整原框架

六条旋转行定义为
$$
\boxed{Q_{0,j}=Q_0T^j,\qquad Q_{b,j}=Q_bT^j,\qquad 0\le j<3.}
\tag{5}
$$
因 $T$ 是 Hermitian 等距，且原 $Q_0,Q_b$ 与 (4) 正交，
每条 (5) 都同时与 $Y,W,W',W_2$ 正交。
对每个固定 $j$，两行的 Gram 仍为 $\operatorname{diag}(5,515)$。

它们张成的空间准确为
$$
\boxed{\mathcal H=\mathcal R^\perp,\qquad\dim_K\mathcal H=3.}
\tag{6}
$$
一个完整可检验的第三基轴是
$$
\boxed{
E_*=Q_0T-\frac{7-\delta}{10}Q_0
              -\frac{-12-2\delta}{515}Q_b.
}
\tag{7}
$$
逐项原六输入系数为
$$
\begin{aligned}
E_*={}&\frac{-461+423\delta}{1442}\xi_1
+\frac{99+45\delta}{206}\xi_2
+\frac{-235-481\delta}{1442}\xi_3\\
&+\frac{-1+4\delta}{7}x
+\frac{9+13\delta}{1442}c
+\frac{-27+10\delta}{721}d_0.
\end{aligned}
\tag{8}
$$
准确有
$$
\boxed{
Q_0,Q_b,E_* \text{ 两两正交},\qquad
N(E_*)=216/103.
}
\tag{9}
$$
因此 (7) 确为非零第三方向，不是只从六行的数目推断维数。
$721E_*$ 是 CM 整行，范数为 $1090152$；此事实本身不支付它的核心。

保全原输入的六输出框架为
$$
\mathcal F_*=(Y,W,W',Q_0,Q_b,E_*).
\tag{10}
$$
它的 Gram 是两个完整三块
$$
G_{\mathcal R}=
\begin{pmatrix}
34&37-3\delta&37-3\delta\\
37+3\delta&72&51+7\delta\\
37+3\delta&51-7\delta&72
\end{pmatrix},
\qquad
G_{\mathcal H}=\operatorname{diag}(5,515,216/103).
\tag{11}
$$
交叉块严格为零，而且
$$
\det G_{\mathcal R}=24192,\qquad
\det G_{\mathcal H}=5400,\qquad
\boxed{\det\mathcal F_*=(43200+38880\delta)/7.}
\tag{12}
$$
其范数为 $130636800=24192\cdot5400$。
原固定坏集之外，这个框架和完整逆矩阵都在普通处整且可逆。
确切逆可直接取
$$
\mathcal F_*^{-1}=\bar{\mathcal F_*}^{\,t}
\operatorname{diag}(G_{\mathcal R}^{-1},G_{\mathcal H}^{-1}).
\tag{13}
$$
所以这里保留了原完整物理格，不是只有一个函数域层面的分解。

在 (10) 下，$T$ 是真正块对角的：
$$
\boxed{
\mathcal F_*T\mathcal F_*^{-1}
=\operatorname{diag}(T_{\mathcal R},T_{\mathcal H}),
\qquad
T_{\mathcal R}=
\begin{pmatrix}
1&0&0\\0&0&1\\0&-\omega^2&-\omega
\end{pmatrix},
}
\tag{14}
$$
$$
T_{\mathcal H}=
\begin{pmatrix}
(7-\delta)/10&(-12-2\delta)/515&1\\
(-9-5\delta)/5&(437-26\delta)/515&7+\delta\\
108(1+\delta)/515&216(5+3\delta)/53045&(-5-36\delta)/103
\end{pmatrix}.
\tag{15}
$$
(15) 三次为恒等并保持 (11) 的第二块，完整数据已在 R512 的 BigInt 证书中算出。它显示原三阶变换在隐藏空间中确实混合三个方向，不能只旋转原两条 $Q$ 后丢掉 (8)。

## 3. 从原来源身份支付六条单轴核心

对非零观察行 $L$，记实际单轴收缩
$$
D_{L,n}
=I+\frac{\kappa^n-1}{N(L)}\bar L^{\,t}L,\qquad n\ge0.
\tag{16}
$$
它令 $L$ 乘 $\kappa^n$，固定其正交五维伴随。

先对 $\rho,h$ 证明。R493 给
$$
T_*\rho=\omega h,\qquad
T_*h=-\omega(\rho+h).
\tag{17}
$$
所以 $\operatorname{span}(\rho,h)$ 在 $T_*$ 及其逆下稳定。
R513 的两条基础核心对这个整个来源空间成立。将其中一条对
$T_*^j\rho$ 使用，再用原六维 $T^{-j}$ 拉回，就得到
$$
\boxed{
\rho|_{\{Q_{\bullet,j}\in p^n\}}
=(\chi\lambda)^n(D_{Q_{\bullet,j},n})_*\rho,
\quad \bullet\in\{0,b\}.
}
\tag{18}
$$
这里准确用到
$$
D_{Q_{\bullet,j},n}=T^{-j}D_{Q_\bullet,n}T^j.
$$
它是原来源身份的真正共轭，不是从旋转后边际猜测新 odd 相位。
同理 (18) 对 $h$ 成立。

再看原四态。构造 $(u,v,z,h)$ 所需的原 $W$ canonical 平移、
$K_W$ 与 $W'/2$ 的实际核心操作，均只作用于 (4) 中的观察方向。
每条 (5) 都与这些方向正交；其收缩、深度事件和完整 canonical
操作逐项交换，连同原 quarter 中心。
从 $\rho$ 的 (18) 逐项传递，得到
$$
\boxed{
\nu_\mu|_{\{Q_{\bullet,j}\in p^n\}}
=(\chi\lambda)^n(D_{Q_{\bullet,j},n})_*\nu_\mu,
\qquad \mu\in\{u,v,z,h\}.
}
\tag{19}
$$
这没有假设 $T$ 保持整个四态空间。实际只先在 (17) 的稳定
二维空间中共轭，再沿正交的原来源构造传递；因此不会错误地将
$T_*v$ 认成未支付的四态线性组合。

固定 $j$ 时两轴正交，(19) 还给所有不等深矩形：
$$
\boxed{
\nu_\mu|_{\{Q_{0,j}\in p^r,Q_{b,j}\in p^s\}}
=(\chi\lambda)^{r+s}
(D_{Q_{0,j},r}D_{Q_{b,j},s})_*\nu_\mu.
}
\tag{20}
$$
不同 $j$ 的矩阵通常不交换，必须使用下一节的实际词域。

## 4. 任意正词都保三个原算术观察

任取由 (16) 的六种轴组成的正词
$$
N=D_{L_1,n_1}\cdots D_{L_m,n_m},\qquad
k=n_1+\cdots+n_m,\quad L_i\in\{Q_{0,j},Q_{b,j}\}.
$$
逐层使用 (19)，准确有
$$
\boxed{
\nu_\mu|_{N\mathscr L}=(\chi\lambda)^kN_*\nu_\mu,
\qquad\mathscr L=\mathcal O_p^6.
}
\tag{21}
$$
整个事件为 $N^{-1}\xi\in\mathscr L$，保每层的移动线性条件。
它不等同于将未移动的六轴深度条件逐个相交。

由 (6)、(16)，这些真实词还满足
$$
\boxed{YN=Y,\quad WN=W,\quad W'N=W',\quad W_2N=W_2.}
\tag{22}
$$
因此第一 $Y$ 和第一 $W/W_2$ 的 canonical CM 投影、完整角平均、
纤维和原算术条件行均与 (21) 交换。完整五伴随测试仍按同一个
$N$ 运输，而第一 Mellin 观察无需改变。
原参考行若测试依赖 Mellin 变量，其非零质量产生的求导项仍保留。

特别不能从 (22) 推出 $ZN=Z$ 或 $T_cN=T_c$：这些不属于
(4) 的三个观察。比如 (8) 的自由 $x$ 系数非零，已经显示这个区别。
所以 (21) 不自动控制 R503 的 $B_0$，也不删除它的原
$Z/Y/T_c$ 单位条件。

## 5. 与原 Y/B 平面词的真正交集

令 $B=B_{15}$ 为 R510 的原小轴。由
$$
B=(W_2+\omega^2Y)/2
$$
可知 $Y,B$ 均在 $\mathcal R$。
R510 的两种真实矩阵
$$
A_Y=I-\frac{\kappa+1}{34}\bar Y^{\,t}Y,\qquad
A_B=I+\frac{\kappa-1}{15}\bar B^{\,t}B
\tag{23}
$$
因而固定整个 $\mathcal H$。
与之相反，任意上述 $N$ 固定 $\mathcal R$、只在 $\mathcal H$
上变化。因此对任意 $A_Y/A_B$ 正词 $M$，
$$
\boxed{MN=NM.}
\tag{24}
$$

(11)–(13) 还保证原完整整格有真正直和
$$
\mathscr L=\mathscr L_{\mathcal R}\oplus\mathscr L_{\mathcal H}.
$$
$M$ 仅收缩前者，$N$ 仅收缩后者，所以
$$
\boxed{M\mathscr L\cap N\mathscr L=MN\mathscr L.}
\tag{25}
$$
这是实际像格交等式，不是以来源标量相等推断域相等。

设 $M$ 长度为 $\ell$，其中 $A_B$ 出现 $b$ 次；
$N$ 的总深度为 $k$。在 raw 原来源上，(21)、R510 逐层给
$$
\boxed{
\rho|_{M\mathscr L\cap N\mathscr L}
=\chi^{b+k}\lambda^{\ell+k}(MN)_*\rho.
}
\tag{26}
$$
因 (22)，两个原算术观察准确为
$$
Y(MN)^{-1}=YM^{-1},\qquad
W_2(MN)^{-1}=W_2M^{-1}.
\tag{27}
$$
于是原 (R510) 的 $S/T$ 中央行可以在这个真实交集上使用，
只乘 (26) 的显示标量；第一权仍取 (27)，不能改成原未移动权。
此处没有将 $M$ 的 raw 核用于未经 quarter 支付的 $\eta$。

## 6. 已付六轴与尚未付的第三正交核心

(6) 的线性张成、(9) 的范数和 (15) 的三阶矩阵，都不意味着
$E_*$ 有某个猜测标量核心。它的整化行 $721E_*$ 虽有明确范数，
其完整 theta 中心、半特征、绝对相位和原来源作用尚须另证。

同样，即使所有六条 (5) 都深 $n$ 等价于某个完整共同伴随
坐标深域，也不能把六个单轴限制机械相乘为该域的核心：
不同轴收缩改变其他条件。当前已付的精确对象是 (20) 的每个
正交二轴矩形与 (21) 的各个正词像格。

接续问题因此保持具体：计算这些像格与原 $Z/T_c$ 单位补域的
真实交叠，或支付第三正交核心和全部条件的进一步推前。
原固定曲线的跨素数中央非消失还没有由本篇推出。

## 依赖与精确数据

- [R512 的原六输入 BigInt 证书](../scripts/check-r512-original-geometric-group-and-observation-orbits.mjs)及
  [完整旋转行、三维矩阵、Gram 与六框架数据](../scripts/check-r512-original-geometric-group-and-observation-orbits.json)。
  这里使用已经实际执行的同一证书，不增加机械复跑门槛。
- [R513：两条基础 odd 核、原四态和真实隐藏输入](R513-original-hidden-odd-cores-and-b0-reflection-kernel.md)。
- [R493：原来源二维三阶身份](R493-original-half-torsion-six-sigma-factor-and-y-preserving-transport.md)。
- [R510：raw Y/B 两种核心及完整中央词域](R510-original-w2-companion-and-fifteen-axis-central-words.md)。
- [R496：原四态构造、完整偶核与实际平移](R496-original-new-axis-even-core-and-four-source-group.md)。

主目标未完成，继续原完整条件的联立。
