# R1197：原最高 primitive packet 的完整 CM 系数旗标

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；root / global_route / o2_high_coefficient。

**已证明。** 在 R1193 的同一个最高整 packet 中，原 CM 圆盘上全部非恒定模 $p$ 系数构成一个完整旗标：从高到低的第 $k$ 列，在此前各列同时消失时，准确是首中心多项式 $T_L$ 在 $b=1$ 的第 $k-1$ 阶导数乘一个显示的原单位。整个轮廓的秩为 $2g-1$，核准确为 $T_L=c(b^3-1)^{2g-1}$ 的一维空间。

证明在每个所需 normal 层使用完整的原有限角，而不只计算最高极部。较低极部、全纯自由项、中心自身变形及其它尾的返回全部保留，直到完整一维投影处理它们。

该核尚未被识别为一个特定 CM 算术因子；本篇也不将整个 packet 的秩传给指定非 CM 半秩商，或把它替成同一 $\beta$ 的首列单位。Serre 主目标仍 OPEN。

## 1. 同一原对象及结论

沿用 R1193 的
$$
p=12g-1>37,\quad m=6g-1=(p-1)/2,\quad
e_0=m(p+1),\quad \pi_0^{e_0}=p,\quad\varepsilon=\pi_0^m.
\tag{1197.1}
$$
原曲线为 $X_1$，原点为 $c_1$，整角为
$$
E_m=(e_{\tau_m}+e_{\mathrm{PS}_{m-1}})e_N
 \in e_N\mathbf Z_p[\operatorname{PGL}_2(\mathbf F_p)]e_N.
$$
这是同一个尖点型与主系列的整 packet。R1193/R1195 已给其完整整性，不使用单独尖点型的非整投影。

令 $L$ 是 generic 尾上惯性权 $m^2$、deck 角色 $\zeta^2$ 的特殊 Hodge 向量，$\Omega_L$ 是同角色且被 $E_m$ 固定的实际整提升。R1193 的原首中心层是
$$
\overline{\pi_0^{-1}\Omega_L}|_I
 =\frac{T_L(b)}{uA_p(b)}\,db,\qquad
u^m=(1-b^3)^{2g}A_p(b),\quad A_p(b)=bQ_p(b^3),
$$
$$
T_L\in k[b^3],\qquad \deg_bT_L<m-1=6g-2,
$$
$$
T_L(b)=\frac2m\sum_{s\in S}\lambda_s\rho_sL_s
                       \frac{A_p(b)}{b-s},
\qquad S=\{A_p=0\}.
\tag{1197.2}
$$
全部节点单位沿用原文。映射 $L\mapsto T_L$ 是该负角色底空间与
$k[B]_{\le2g-1}$（$B=b^3$）的同构：逆式是
$$
L_s=\frac{mT_L(s)}{2\lambda_s\rho_sA_p'(s)}.
\tag{1197.3}
$$
其分母全为单位，真实 deck 等变性正是 $T_L\in k[b^3]$。

原 CM 尾及同一节点参数为
$$
D:\ y^2=x(x^{2g}+A_{\rm tail}),\qquad Q=(0,0),\quad t=\sqrt x,
$$
$$
z_Dw=\rho_1\pi_0^3,\qquad
b-1=\kappa_1w^m+\cdots,\qquad
u=\lambda_1w^{2g}+\cdots .
\tag{1197.4}
$$
这里的 $\kappa_1$ 是显示的节点首系数，与 R1193 完全相同。原有理圆盘参数仍为
$$
w_{\rm rat}=(a-1)/p^3,\qquad
z_{\rm CM}=\varepsilon^3w_{\rm rat},\qquad
\lambda_0=(d\bar z_{\rm CM}/dt)(Q)\ne0.
\tag{1197.5}
$$
$a$ 是原 coarse 参数，$b$ 是 Igusa 参数，两者不互换。

R1193 的完整尾界已经证明
$$
H_L(w_{\rm rat})
 =\varepsilon^{-m}\int_{c_1}^{x(w_{\rm rat})}\Omega_L
 \in W(k)\langle w_{\rm rat}\rangle,\qquad
\deg\overline H_L\le2g-1,\qquad H_L(0)=0.
\tag{1197.6}
$$
有限未分歧底时按原文使用该底的整数环。此界包括所有 $p$ 倍积分次数。

定义
$$
\mathcal F_j=\{L:T_L(1)=T_L'(1)=\cdots=T_L^{(j-1)}(1)=0\},
\qquad \mathcal F_0=\text{整个负角色底空间}.
\tag{1197.7}
$$
对 $1\le k\le2g-1$，记
$$
n_k=3k-3,\qquad d_k=km-2g,\qquad N_k=(3k-1)m,
$$
$$
b_k=\frac{6\,2^{n_k}(5/2)_{n_k}
                 (\sqrt{A_{\rm tail}})^{n_k+1}}{(n_k+3)!},
$$
$$
v_k=
\frac{m\kappa_1^k\rho_1^{d_k}}
 {\lambda_1A_p(1)d_k(k-1)!}\,
 b_k\,\lambda_0^{-(2g-k)}\in k^\times.
\tag{1197.8}
$$
$(5/2)_n$ 表示上升阶乘。本文证明
$$
\boxed{\quad
L\in\mathcal F_{k-1}
\Longrightarrow
[w_{\rm rat}^{\,2g-k}]\overline H_L
   =v_kT_L^{(k-1)}(1).
\quad}
\tag{1197.9}
$$
此前更高的 $w_{\rm rat}$ 次数在这个子空间上全为零。因此在整个底空间上，各系数泛函与
$T_L(1),T_L'(1),\ldots,T_L^{(2g-2)}(1)$ 构成同一个完整旗标；没有将此前各列的未知倍数设成零。

## 2. 所需全部次数上的完整有限角图像

这一节独立核准最高 packet 的 determinant twist，不能直接使用 R1044 最低型的次数结论。

置
$$
D_k=3k(p-1)-2,\qquad
M_k=\operatorname{Sym}^{D_k}(k^2)\otimes\det^{\,1-m}.
\tag{1197.10}
$$
其中心角色为零，因为
$D_k+2(1-m)=(3k-1)(p-1)$。令
$C=X^pY-XY^p$；它的次数为 $p+1$，换基角色为 determinant。

按 $C$ 的幂过滤 $M_k$。第 $j$ 个商的 ambient polynomial 次数为
$D_k-j(p+1)$，determinant twist 为 $1-m+j$。在当前范围，
$$
0\le j\le\left\lfloor\frac{D_k}{p+1}\right\rfloor\le m-3,
$$
$$
r_j\equiv D_k-j(p+1)\pmod{p-1},
\qquad r_j=p-3-2j,\qquad 4\le r_j\le p-3.
\tag{1197.11}
$$
最后一个界可直接在 $k=2g-1$ 核准：
$D_k=(m-3)(p+1)+4$。

对非终端的 evaluation quotient，R1042 的同一齐次评价正合列给两个组成因子
$$
S_j=\operatorname{Sym}^{p-3-2j}(k^2)
               \otimes\det^{\,1-m+j},
$$
$$
T_j=\operatorname{Sym}^{2+2j}(k^2)
               \otimes\det^{\,m-1-j}.
\tag{1197.12}
$$
这个公式也可由 evaluation quotient 的两个标准因子
$\operatorname{Sym}^{r_j}\det^{t_j}$ 和
$\operatorname{Sym}^{p-1-r_j}\det^{r_j+t_j}$、$t_j=1-m+j$ 直接得到；没有略掉 determinant twist。

写
$W_b=\operatorname{Sym}^{2b}(k^2)\otimes\det^{-b}$。
第一因子为 $S_j=W_{m-1-j}$。其 $N$-固定线存在当且仅当 $m-1-j$ 为偶数；存在时，R1195 的整角将它分配到指标
$r=(m-1-j)+1=m-j$。所以 $E_m$ 只在 $j=0$ 的这个因子上有一维图像，在 $j>0$ 的第一因子上为零。

第二因子写为
$$
T_j=W_{j+1}\otimes\eta,\qquad
\eta=\det^m.
$$
设 $a=j+1\le m-2$。Cartan 固定单项式的下标必须为
$a+(m+1)$ 或 $a-(m+1)$ 模 $p+1$；二者都不在 $0,\ldots,2a$ 中。因此 $T_j^N=0$，实际 $E_m$ 在它上面为零。

过滤的终端次数位于 $[0,p]$，又同余于 (1197.11) 的 $r_j\ge4$；所以终端次数就是 $r_j$，而非 $r_j+p-1$。它是简单模 $S_j$。由于 $D_k>p$，终端的 $j>0$，也不贡献 $E_m$ 图像。

对任意实际幂等元，取其像是 exact 函子。因此逐个组成因子计数合法，不要求剩余表示半单：
$$
\boxed{\quad \dim_k\overline E_m M_k=1
       \qquad(1\le k\le2g-1).\quad}
\tag{1197.13}
$$

## 3. 同一 full 分支上的准确参考 primitive

沿 R1193 的原 full-$p$ 坐标写
$$
c=A_0^{p+1}-B_0^{p+1},\qquad
U=(A_0^{p+1}+B_0^{p+1})/2,\qquad V=A_0B_0,
$$
$$
U^2=V^{p+1}+A_{\rm tail},\qquad A_{\rm tail}=c^2/4,
\qquad x=V^6,\quad y=UV^3,\quad z_D=V^{-3}.
\tag{1197.14}
$$
所有实际非零 Weil 配对分支一起保留。令
$$
F=UV^{m-2}=x^{g-1}y,\qquad
\Theta=X^p\partial_X+Y^p\partial_Y.
$$
R1030/R1042 给
$$
\Theta V=2U,\qquad \Theta U=V^p,\qquad \Theta c=0;
\tag{1197.15}
$$
$\Theta$ 与完整 $\operatorname{GL}_2(\mathbf F_p)$ 换基交换。R1193 已在全部分支证明
$E_m(c^{1-m}F)=c^{1-m}F$。

定义
$$
a_n=(-1)^n(n+3)!/6,\qquad
H_k=a_{n_k}^{-1}\Theta^{n_k}F.
\tag{1197.16}
$$
于是 $E_m(c^{1-m}H_k)=c^{1-m}H_k$。

在原无穷支 $U\sim V^{m+1}$，$F$ 的最高 $V$ 次数是 $2m-1$。第 $j$ 次作用 $\Theta$ 时最高系数乘
$$
2(2m-1+jm)=-(j+4)\quad\text{于 }k.
$$
所以准确的总乘数就是 $a_{n_k}$，而最高 $z_D$ 极阶是
$(2m-1+n_km)/3=km-2g=d_k$。因此
$$
\boxed{\quad H_k=z_D^{-d_k}+\text{较低极阶项}.\quad}
\tag{1197.17}
$$

在 $Q$，$t=V^3$、$U(Q)=\sqrt{A_{\rm tail}}$。最低项只来自每次使用
$2U\partial_V$；凡使用 $\Theta U=V^p$ 的项次数更高。
这里 $m-2=-5/2$ 于 $k$，故下降阶乘
$(m-2)(m-3)\cdots(m-1-n)=(-1)^n(5/2)_n$。由此
$$
\boxed{\quad H_k(t)=b_k t^{2g-k}
                         +\text{更高 }t\text{ 次项}.\quad}
\tag{1197.18}
$$
所有归一因子确为单位：
$n_k\le m-5$，$n_k+3\le m-2<p$；
$(5/2)_{n_k}$ 中最大的奇分子为 $2n_k+3\le p-8$；
且
$$
d_k\equiv-(3k+1)/6\pmod p,\qquad 3k+1\le m-1<p.
$$
另外 $2g-k\ge1$。这也逐项证明 (1197.8) 的 $v_k\ne0$。

须区分 primitive 和微分系数的次数：
$$
\deg H_k=(3k-1)(p-1)-2,\qquad
\deg(\Theta H_k)=D_k.
\tag{1197.19}
$$
(1197.13) 的生成元是 $c^{1-m}\Theta H_k$ 所代表的微分系数，而不是次数较低的 $H_k$。

## 4. 每一条实际 normal 微分都进入这个一维图像

固定一个原 full 分支 $C=c_0\ne0$。其真实无零仿射微分为
$$
\eta=\frac{dX}{X^p}=\frac{dY}{Y^p},\qquad
dG=(\Theta G)\eta.
\tag{1197.20}
$$
它在完整 level 换基下不变。R1044 §3 的平面闭包
$X^pY-XY^p=c_0Z^{p+1}$ 光滑，且
$$
\operatorname{div}(\eta)=(p-2)\sum_\infty[\infty].
$$
同一 full 分支到 $D$ 的无穷分歧指数为六。

设实际第 $N_k$ 层在 $D$ 上仿射正则，唯一可能极点为无穷远，极阶至多 $d_k+1$。写其 full 拉回为 $\Omega_k=f_k\eta$。拉回微分的极阶至多 $6d_k+1$，所以 $f_k$ 的极阶至多
$$
6d_k+p-1=3k(p-1)-2=D_k
\tag{1197.21}
$$
在每个 full 无穷点成立。超平面截面就是这些无穷点；平面 hypersurface 正合列和
$H^1(\mathbf P^2,O(a))=0$ 给一个总次数不超过 $D_k$ 的真实 polynomial representative。这里从完整极点界得代表，不是假设原微分已 exact。

原 framing 以
$\varpi^{p^2-1}=p$、$\pi_0=\varpi^2$、$\sigma\varpi=\upsilon\varpi$
表示时，$X,Y$ 的权为 $\upsilon^{-1}$。原 $\Omega_L$ 的权为
$\upsilon^{2m^2}$，而 $\eta$ 的权为 $\upsilon^{p-1}$。故当前 $f_k$ 的权为
$$
\upsilon^{2m^2-6km}.
$$
乘上在固定分支为常数的 $c^{m-1}$ 后，其准确权变成
$$
\upsilon^{2m^2-6km-(m-1)(p+1)}
 =\upsilon^{-D_k}.
\tag{1197.22}
$$

固定分支的惯性稳定子为 $\mu_{p+1}$。对 polynomial representative 平均，只留下次数
$D_k-j(p+1)$ 的项；用 $c_0^{-j}C^j$ 将各项齐次化而不改变其在该分支上的值。因此 $c^{m-1}f_k$ 有准确次数 $D_k$ 的齐次代表。完整
$\mu_{p^2-1}$ 在实际非零 pairing 分支上传递，(1197.22) 使同一个代表在全部分支上成立。乘回 $c^{1-m}$，准确得到 (1197.10) 的 determinant twist。

现在对代表施真实 $E_m$。原微分已经被这个整幂等元固定，$\eta$ 又对 level 换基不变，故仍代表同一实际微分。(1197.13) 迫它是
$$
c^{1-m}dH_k
\tag{1197.23}
$$
的标量倍数。该生成元非零，因为其最高项为
$-d_kc^{1-m}z_D^{-d_k-1}dz_D$，$d_k$ 为单位。

在固定原分支上，$c^{1-m}$ 是指定非零常数，可在比较最高项时一并吸入标量；在其它分支仍保留其 determinant 运输。特别地，若实际微分的最高极部为零，整个当前层都为零，包含全部低极部和全纯自由项。

R1021 的 full 换基在整个 $R/(p)$ 仿射模型上为常线性作用，故整 $E_m$ 逐 normal 层相容。当前最大层
$$
N_{2g-1}=(m-3)m<m^2<e_0
\tag{1197.24}
$$
确在该已证明精度内。

## 5. 全部 global normal 层的归纳

我们证明更强的实际断言：若 $L\in\mathcal F_{k-1}$，所有小于 $N_k$ 的 CM 层都为零，且
$$
\boxed{\quad
\overline{\pi_0^{-N_k}\Omega_L}|_D
=\frac{m\kappa_1^k\rho_1^{d_k}}
 {\lambda_1A_p(1)d_k(k-1)!}\,
 T_L^{(k-1)}(1)\,dH_k .
\quad}
\tag{1197.25}
$$
$k=1$ 正是 R1193 的完整首层，包含其低层消失及全纯修正处理。本节不重做该已登记结论。

相邻的可能 CM 层相差 $3m$：原仿射 CM 微分的角色都为 $3m$ 的倍数，故权 $m^2$ 的提升只有
$n\equiv2m\pmod{3m}$。因此当前归纳假设确实给此前全部 CM 层为零，不只是此前最高极部为零。

中心的可能层是
$$
n=1+j(p+1),\qquad j\ge0.
\tag{1197.26}
$$
在当前 $b=1$ 标记，此前 CM 层全零，故没有该尾返回的 polar input。其它两个 CM 尾和 generic 尾的已规定主部仍完整保留；它们在当前标记正则。中心自身的 smooth deformation 也按 R1032/R1044 的原方法处理：在支撑全部已规定极点、避开当前标记的充分大有效除子 $D_{\rm aux}$ 下，
$H^1(I,\Omega_I^1(D_{\rm aux}))=0$，逐阶提升非齐次部分。这个操作保留实际节点主部和 holomorphic 自由项；节点 residue 另由 compact-type 树的逐叶 residue 定理核准。

第 (1197.26) 层的中心 character 写为
$$
u^{-1-2j}r_j(b)\,db .
$$
在 $b=1$ 正则迫 $r_j$ 无基极点。确切地，未乘 $r_j$ 时的 $w$ 阶为
$m-1-2g-4gj$，严格小于 $m$；额外一个 $b-1$ 的负幂便不正则。$j\ge1$ 时还须有相应零点，但不需要把这些未知零点的系数先设为零。

乘 regular Taylor 项 $(b-1)^\ell$ 后，$w$ 指数加一为
$$
(\ell+1)m-2g-4gj.
$$
厚度三的节点将它送入
$$
1+j(p+1)+3((\ell+1)m-2g-4gj)
  =(3\ell+2)m
\tag{1197.27}
$$
层。当前 $N_k$ 对应 $\ell=k-1$，其极阶至多
$d_k+1-4gj$。故 $j\ge1$ 的所有中心返回严格低于最高极阶 $d_k+1$；最高项只能来自已知的第 $1$ 中心层 (1197.2)。

在 $\mathcal F_{k-1}$ 上，该首中心层于当前标记的首项准确为
$$
\pi_0
 \frac{m\kappa_1^k}{\lambda_1A_p(1)(k-1)!}
 T_L^{(k-1)}(1)\,w^{d_k-1}dw.
$$
由原节点 $z_Dw=\rho_1\pi_0^3$，它给
$$
-\frac{m\kappa_1^k\rho_1^{d_k}}
 {\lambda_1A_p(1)(k-1)!}
 T_L^{(k-1)}(1)\,
 \pi_0^{N_k}z_D^{-d_k-1}dz_D.
\tag{1197.28}
$$
原节点单位及坐标的更高项，要么乘此前已为零的 $T_L$ 导数，要么提高 normal 次数、降低当前极阶；因此不改 (1197.28)。

当前整个实际层仍在仿射尾正则，其所有低极部及可能全纯自由项都满足 §4 的完整极阶和角色条件。故它必须是 $dH_k$ 的倍数。比较 (1197.17) 的最高微分系数 $-d_k$，得到 (1197.25)。

若 $L$ 进一步属于 $\mathcal F_k$，该最高项为零，§4 迫当前整个层为零，从而完成归纳。这里没有把高中心层、其它 CM 尾返回或 holomorphic 自由项当作独立消失条件。

## 6. 回到同一个有理圆盘及完整核

在 $\mathcal F_{k-1}$ 上此前 CM 层全零，故把
$\bar z_{\rm CM}=\lambda_0t+O(t^2)$ 代入 (1197.18)、(1197.25) 时，更高坐标项不能降低最低 primitive 次数 $2g-k$。其准确系数乘
$\lambda_0^{-(2g-k)}$。混合特征的更高 normal 修正只乘此前的零层，或提高当前层。

同一尺度恒等式为
$$
N_k+3m(2g-k)=m^2.
\tag{1197.29}
$$
因此该项除以 $\varepsilon^m=\pi_0^{m^2}$ 后，恰位于单位尺度。积分次数 $1\le2g-k<p$，分母为单位。固定这个 Taylor 次数的后续 normal 项由精确惯性相差整 $e_0$，不再改变模 $p$ 系数；其它次数、包括全部 $p$ 倍次数，已经受 (1197.6) 的完整尾界控制。于是准确得到 (1197.9)。

写 $T_L(b)=R(b^3)$，$\deg R\le2g-1$。映射 $b\mapsto b^3$ 在 $b=1$ 的导数为 $3$，而所有所需阶乘小于 $p$；所以前 $2g-1$ 个 $b$-jets 与前 $2g-1$ 个 $B$-jets 等价。其共同核准确为
$$
R(B)=c(B-1)^{2g-1}.
$$
结合每个 $v_k$ 为单位及 (1197.6)，得到
$$
\boxed{\quad
\operatorname{rank}(L\mapsto\overline H_L)=2g-1,\qquad
\ker(L\mapsto\overline H_L)
=\{\,T_L=c(b^3-1)^{2g-1}:c\in k\,\}.
\quad}
\tag{1197.30}
$$
这也说明该模 $p$ 轮廓只依赖底向量 $L$：同底向量的提升之差在所有上述层都为零，完整尾界又控制剩余项。

## 7. 与原半秩问题的准确接口

R1196 已把同一个 $P=(p-1)D_0$ 的最高 packet 首对数列写成原相对 Picard 的有限 Čech log，并在该首层排除了 formal-log 的 $p$ 次返回。本文给同一原盘的完整 CM 轮廓及其精确一维核；二者可在同一个原整格中继续作 Serre 配对。

仍须支付：同一 $\beta$ 在该底空间中的实际全图列、该列与上述 CM 旗标的关系、指定 $C$ 的整拉回及单尖点型拼接。R1195 的一个 $p$ 拼接模不能直接删除。本文不证明 (1197.30) 的核是 CM 算术线，不证明其与指定非 CM 空间的交为零，也不从高系数单位推整个深盘唯一零点。

全篇为原几何、有限表示和纸面代数，没有执行数学程序，没有重跑任何登记窗口。

## 来源

- [R1193](R1193-original-highest-primitive-packet-and-simple-Cauchy-CM-jet.md) §§1–7：原最高整 packet、负角色首中心、实际节点单位、$F=UV^{m-2}$ 的整投影、CM 首层及原有理盘完整尾界。
- [R1195](R1195-original-full-integral-normalizer-corner-and-one-p-gluing.md) §§1–4：完整有限角、各 $W_a$ 的真实 packet 分配及单型整拼接范围。
- [R1042](R1042-original-CM-disc-second-column-and-finite-corner.md) §4：同一个 Dickson 过滤与 evaluation quotient；本文重新计算全部最高型次数及 determinant twist。
- [R1044](R1044-original-CM-disc-complete-coefficient-flag.md) §§2–6：同一 full 分支的 $\Theta,\eta$、光滑平面闭包、齐次代表、全部分支及 global normal 递推方法；本文不把其最低型参数代入为最高型结论。
- [R1032](R1032-original-lowest-type-complete-CM-normal-jet-functional.md) §3、[R1021](R1021-actual-full-p-affine-tail-rigidity-and-quotient-parameter.md) §§2–3：实际非齐次中心提升、全部节点 residue 及整个模 $p$ 仿射范围的真实常线性作用。
- [R1196](R1196-original-highest-packet-Picard-log-and-finite-Cech-source.md)：同一 $P,\beta,C$ 的有限 Picard log 来源及保留的全图配对。

root 逐式核准次数、角色、完整 normal 归纳及原尺度；o2_high_coefficient 独立核 §2 的全部终端因子和一维整角图像。核对只用于落实显示证明，不构成额外发布审批。
