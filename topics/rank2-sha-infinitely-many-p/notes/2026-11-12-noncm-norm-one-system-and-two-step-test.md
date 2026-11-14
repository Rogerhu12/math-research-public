# 非 CM 范数一 Euler 族、真实额外 delta 与两步充分条件

日期：2026-11-12。**已证明的定量与充分条件。**
无穷多个实际 $Q$ 的两步原始性尚未证明。

## 1. 明确输入及本篇结论

固定 R136 的
$$
 E:y^2+y=x^3+x^2-2x,\qquad F=\mathbb Q(\sqrt{-7}).
\tag{1}
$$
写 $r=\operatorname{rank}E(\mathbb Q)\ge2$；不预先假定 $r=2$。
R136 已证明 $N_E=389$、$w(E)=+1$、$E$ 非 CM、$h_F=1$，
负七扭曲秩一且整个 Sha 有限，基层实际 Heegner 点 $P_1=O$。

取 R138 给出的充分大的 $(p,\ell)$，保留
$$
 \ell\text{ 在 }F\text{ 惰性},\quad
 \ell+1=pu,\quad p\nmid u,\quad
 0<|a_\ell(E)|<p,
 \quad a_p(E)\not\equiv0,\pm1\pmod p.
\tag{2}
$$
再删去固定有限多个素数，包括负扭曲 Sha 的素因子及非 CM
Tate 表示的有限例外。Serre 开像定理及 $p\ge5$ 的标准提升
给 $G_F$ 在 $T_pE$ 上的像为 $\mathrm{GL}_2(\mathbb Z_p)$。
说明这里限制到 $F$ 不减小像：$F$ 与 $\mathbb Q(E[p^\infty])$
的交至多为二次，二次商来自行列式，而
$F\not\subset\mathbb Q(\mu_{p^\infty})$（$p\ne7$，分歧位不同）。

令 $H=F[\ell]$、$L/F$ 为其唯一次数 $p$ 子域，
$\Gamma=\langle\tau\rangle$，并使用原完整迹
$$
 Q=\operatorname{Tr}_{H/L}\pi(x_\ell),\qquad
 \pi(\infty)=O.
\tag{3}
$$
本篇对任何使 $Q$ 非扭的这样的输入成立；不把 R138 单独当作
$Q\ne0$ 的证明。Heegner 范数给
$$
                      N_\Gamma Q=a_\ell P_1=0.
\tag{4}
$$
设
$$
 B=\operatorname{Res}_{L/F}E,\quad A=\ker(N:B\to E),
 \quad \mathcal O=\mathbb Z_p[\zeta_p],
 \quad\delta=\tau^{(p-1)/2}(\tau-1).
\tag{5}
$$
这是平衡一致化元，$\bar\delta=-\delta$。
§2 证明 $A(F)\otimes\mathbb Z_p=\mathcal O w$ 以及
$S=\Sha(A/F)[p^\infty]$ 有限；定义实际整数
$$
                 Q=\delta^a\varepsilon w,
                 \quad a\ge0,\quad\varepsilon\in\mathcal O^\times.
\tag{6}
$$
本篇的主要定量结论是
$$
 \boxed{\quad
 S\simeq M\oplus M,\qquad
 \operatorname{length}_{\mathcal O}M\le a+1.
 \quad}
\tag{7}
$$
令 $d_p=\dim_{\mathbb F_p}\Sha(E/\mathbb Q)[p]$，允许未知可除部分。
完整符号比较进一步给
$$
 \operatorname{length}_{\mathcal O}S\ge
 \begin{cases}
   2r-2+2d_p,&a\text{ 偶},\\
   2r+2d_p,&a\text{ 奇}.
 \end{cases}
\tag{8}
$$
因而 **$a\le1$ 足以推出 $r=2$ 及 $\Sha(E/\mathbb Q)[p^\infty]=0$**。
§8 给只用实际共轭点的有限半局部充分检验。

## 2. 非零原迹给准确秩及整个范数一 Sha 有限

由 (4)，$\mathbb Q[\Gamma]Q$ 是
$\mathbb Q[\Gamma]/(N_\Gamma)=\mathbb Q(\zeta_p)$ 的非零商，
所以它恰为这个不可约有理表示。因此每个非平凡 $C_p$ 角色的
未除群阶 Heegner 和
$$
      \sum_{g\in\operatorname{Gal}(H/F)}\chi(g)^{-1}g\pi(x_\ell)
\tag{9}
$$
都非扭。这是特征零表示论，不使用对数的张量单射。

应用 Nekovář（2007）Theorem 3.2 的整角色结论，恰如 R119
§§3–5。其关于 CM 自同态域的例外在本非 CM 曲线上自动排除；
Heegner hypothesis、环类角色、模参数化和非扭性均已明确验证。
该定理不要求 $p\nmid\operatorname{ord}\chi$。故各非平凡本征
Mordell–Weil 空间秩一，对应整 Sha 本征群有限。

保留群阶 $p$ 的整论证如下。若
$S_L=\Sha(E/L)$、$S_L^0=\ker(N_\Gamma:S_L\to S_L)$，则
在整系数 $\mathbb Z[\zeta_p][\Gamma]$ 中，明确使用未除群阶的
$e_\chi=\sum_{g\in\Gamma}\chi(g)^{-1}g$，有
$$
                     \sum_{\chi\ne1}e_\chi=p-N_\Gamma.
$$
右边作用于 $S_L^0\otimes\mathbb Z[\zeta_p]$ 是乘 $p$；
左边的像在上述有限本征群中。此系数扩张是有限自由且忠实的，
再用 $S_L[p]$ 有限，得 $S_L^0$ 有限。
精确序列 $0\to A\to B\to E\to0$ 表明
$\Sha(A/F)$ 到 $S_L$ 的像在此有限群中，其核是
$E(F)/NE(L)$ 的子商；后者被 $p$ 杀掉且有限。因此
$$
             \operatorname{rank}A(F)=p-1,
             \qquad \Sha(A/F)\text{ 整个有限}.
\tag{10}
$$
没有在 $p$-整群环中使用 $1/p$ 投影。

还需 $p$ 挠点为零。$G_F$ 的像为全 $\mathrm{GL}_2$，其导出群
包含 $\mathrm{SL}_2$；任一 $F$ 的阿贝尔扩张的 Galois 子群
均包含该导出群，而它在 $E[p]$ 上没有不变量。于是
$$
                 E(F^{\rm ab})[p]=0.
\tag{11}
$$
特别地 $A(F)\otimes\mathbb Z_p$ 无 $\mathcal O$ 挠点，
(10) 使它是自由秩一，支付 (6)。

## 3. 原辅助位完全消失，包括全部 delta 精度

令 $K=F_\lambda$、$\lambda\mid\ell$。由 (2)，
$$
 \#E(\mathbb F_{\ell^2})
   =(\ell+1)^2-a_\ell^2\equiv-a_\ell^2\not\equiv0\pmod p.
\tag{12}
$$
所以 $\operatorname{Fr}_{\ell^2}-1$ 在 $E[p]$ 上可逆。
又 $\ell^2\equiv1\pmod p$，不分歧和 tame 部分分别为
$$
 E[p]/(\operatorname{Fr}_{\ell^2}-1)E[p]=0,
 \qquad E[p]^{\operatorname{Fr}_{\ell^2}=\ell^2}=0.
$$
这给 $H^1(K,E[p])=0$；$H^0$ 为零，局部 Tate 对偶给 $H^2=0$。
实际识别 $A[\delta]\simeq E[p]$ 后，沿每个短正合列
$0\to A[\delta^{j-1}]\to A[\delta^j]\to A[\delta]\to0$
归纳得到
$$
                    H^i(K,A[\delta^j])=0
       \quad(i=0,1,2;\ j\ge1).
\tag{13}
$$
所以本位没有隐藏的高精度局部修正。

几何组件仍须如实说明：$K'/K=L_\lambda/F_\lambda$ 全分歧，
$B$ 的 Néron 特殊纤维连通，而
$\Phi_A(\bar k)\simeq E[p](\bar k)$、$\delta\Phi_A=0$，
与 R125 §3 的实际核模型相同。但是本次 Frobenius 没有不变量，
所以 $\Phi_A(k)[p]=H^1(k,\Phi_A)[p]=0$。
这里没有把几何的 $p^2$ 个组件说成不存在；其局部有理贡献
准确由 (12)–(13) 消失。

## 4. 全部其余地方的局部比较与 Howard 假设

### 4.1 实际 Tate 格、残余和 Sah 条件

令 $R=\mathbb Z_p[\Gamma]$、$I=(\tau-1)R$。在几何坐标中
$$
 T_pB=T_pE\otimes R,\qquad
 T=T_pA=T_pE\otimes I,\qquad I\simeq R/(N_\Gamma)=\mathcal O.
\tag{14}
$$
最后的同构由乘 $\tau-1$ 给出；在阿贝尔簇上它就是
$B/E_{\rm diag}\simeq A$。故 $T$ 是自由秩二的
$\mathcal O$ 格，且
$$
                     T\simeq T_pE\otimes\mathcal O(\chi^{-1}).
\tag{15}
$$
角色逆向来自坐标的 Galois 置换，采用 R125 的同一约定。
$T/\delta T\simeq E[p]$ 绝对不可约。

$L/F$ 在 $\ell$ 分歧，而 $F(E[p^\infty])/F$ 在该好位
不分歧；由于 $[L:F]=p$，二者交为 $F$。因此复合表示像
包含中央 $(-I,1)$。它在 (15) 上作用为 $-1$，Sah 引理以
单位 $-2$ 消去 Howard H.2 所需的一次群上同调。
复合域在 $\mathbb Q$ 上 Galois，并由 Weil 配对包含全部
$p$ 次幂单位根。这验证 H.0–H.2，不假定一个任意 CM 表示
具有满像。

### 4.2 局部 Kummer、Cartesian 性及剩余比较

采用真实 $A$ 的通常 Kummer 条件。在任意有限地方，
对包含 $A[\delta^i]\hookrightarrow A[\delta^k]$ 比较完整
Kummer 正合列；右边是
$H^1(F_v,A)[\delta^i]\hookrightarrow H^1(F_v,A)[\delta^k]$
的真实包含。因此一个类的像属于高层 Kummer 条件，恰当
原类属于低层 Kummer 条件。这是全部有限商的 Cartesian
pullback；商映射的 Kummer 满射同样直接来自点商。
该证明保留局部 torsion，未假定局部 $H^1$ 包含单射。
与 R125 §4.2 相同的逆极限给从 $T$ 传播的条件就是这些
完整 Kummer 像。原 $\lambda$ 处更有 (13)。

现直接核其剩余条件等于 $E[p]$ 的通常条件。在 $v\ne\lambda$
处，$L/F$ 不分歧或分裂。若 $E$ 好约化，Lang 定理和不分歧
形式群的 trace 过滤给
$$
 H^1(\Gamma_v,E(L_w))=0,
 \qquad N:E(L_w)\longrightarrow E(F_v)\text{ 满射}.
\tag{16}
$$
形式群部分可逐层用不分歧整 normal basis 的加法群验证，
有限剩余部分则由 Lang 方程验证；分裂情形是诱导模。
唯一坏位 $389$ 是 split $I_1$。其 Tate 参数满足 $v(q_E)=1$，
在 $0\to q_E^{\mathbb Z}\to L_w^\times\to E(L_w)\to0$
中，Hilbert 90 后的映射
$H^2(\Gamma_v,q_E^{\mathbb Z})\to H^2(\Gamma_v,L_w^\times)$
是由 $v(q_E)=1$ 给出的同构；故 (16) 同样成立。单位的
不分歧范数满射及以 $q_E$ 调整赋值也直接给范数满射。

由 (16)，任意 $P\in A(F_v)$ 可写成
$P=(\tau-1)Y$，$Y\in B(F_v)$。选 $pS=NY$，则
$Y-E_{\rm diag}(S)$ 为该点的 $(\tau-1)$-除点。
其 Kummer cocycle 在对角 $E[p]$ 下为
$-\operatorname{Kum}_E(NY)$。因为 $N$ 满射，两个 Kummer
局部像恰相同；平衡 $\delta$ 只改变一个群环单位。
在 $\lambda$ 处两个全局部群都为零。这证明准确的全局同构
$$
                 \boxed{\operatorname{Sel}_\delta(A/F)
                     =\operatorname{Sel}_p(E/F).}
\tag{17}
$$
所有 $p$ 上地方都已包括，未要求 $p$ 在 $F$ 分裂。

用 R125 §4.2 的配对
$\langle x\otimes a,y\otimes b\rangle=ab\,e(x,cy)$，
得完美共轭自对偶 $\mathcal O$ 格；通常 Bloch–Kato 条件及
上述传播互为正交补。残余表示延拓到 $G_{\mathbb Q}$，
$c$ 有各一维的 $\pm$ 空间，(17) 的条件对 $c$ 稳定。
因此 Howard H.3–H.5 也逐项满足。$p$ 处的
$a_p\not\equiv\pm1$ 另外排除了 $F_v$ 剩余次数 $1,2$ 中的
局部 $p$ 挠点，但并未把通常条件替换成不同的 ordinary 条件。

## 5. 原族、真正的范数零族及逐标签有限—奇异比较

固定目标精度 $k$，先取足够大的 $m$，使
$m(p-1)\ge2k$。通过 Chebotarev 选辅助素数 $q$，其在
$F(E[p^m],L)/\mathbb Q$ 的 Frobenius 类为复共轭。
于是 $q$ 在 $F$ 惰性、在 $L/F$ 分裂，并有
$$
                    a_q\equiv q+1\equiv0\pmod {p^m}.
\tag{18}
$$
此处 **$a_q$ 未必在整数中等于零**。
令 $n$ 为这些素数的平方自由乘积，定义实际点
$$
 Y_n=\operatorname{Tr}_{F[\ell n]/LF[n]}P[\ell n]\in B(F[n]),
 \qquad Z_n=(\tau-1)Y_n\in A(F[n]).
\tag{19}
$$
导子互素及 $h_F=1$ 保证所用域交与直积辅助 Galois 群是
这些实际环类域的域交，而非形式变量。原 Heegner 关系准确给
$$
 N_\Gamma Y_n=a_\ell P[n],\qquad
 \operatorname{Tr}_{F[nq]/F[n]}Y_{nq}=a_qY_n.
\tag{20}
$$
因此 $N_\Gamma Z_n=0$，且 $Z_n$ 仍满足全部 Euler 范数关系。
它的 leading 是
$$
                 Z_1=(\tau-1)Q=(\text{单位})\,\delta Q,
\tag{21}
$$
在真实 Mordell–Weil 自由格中指数准确为 $a+1$。

用 $D_q=\sum_{j=1}^{q}j\sigma_q^j$、$D_n=\prod_{q\mid n}D_q$
构造未作全局 correction 的原始有限类。$h_F=1$，类数 coset
和只有一个代表；一般书写为
$\widetilde\kappa_n=\sum_s sD_nY_n$ 时此处就是 $D_nY_n$。
恒等式 $(\sigma_q-1)D_q=q+1-N_q$、(18)、(20) 使 Kummer
类模 $p^m$ 不变；(11) 使 inflation–restriction 的下降唯一。
先在 $B$ 中下降，再经实际 $B\xrightarrow{\tau-1}A$ 取像，
得到 (19) 的真实 $T/\delta^k$ 类族。

在非辅助地方，原类成为 Kummer 类后的误差属于不分歧
$H^1(F_v,B)$。$B$ 在原 $\ell$ 的组件为零，在坏位 $389$
也是组件阶一，在其余位为好约化的不分歧 restriction；故
这个误差的 $p$ 部分为零。辅助 $q$ 处的导数计算给真正的
transverse 条件。所有这些条件经 $B\to A$ 保留。

在每个辅助 $q$ 上，选择一处完成并以 $\Gamma$ 标记所有
$L$ 上方素位。先在相应素位应用原 Heegner Frobenius 同余，
再用标签搬回所选完成，所得局部算子是
$\varphi_q\otimes1_R$，不是附加标签反演的全局复共轭。
Howard Proposition 1.7.4 的直接计算因此逐坐标给
$$
 \begin{aligned}
 c_n^B(\operatorname{Fr}_{q^2})
   &=\frac{\varphi_q^2-1}{p^m}
                         \overline{\widetilde\kappa_n},\\
 c_{nq}^B(\sigma_q)
   &=\frac{a_q-(q+1)\varphi_q}{p^m}
                         \overline{\widetilde\kappa_n}.
 \end{aligned}
\tag{22}
$$
这里使用的是**导出整点**的约化，非原始 $Y_n$。
局部除点按该命题定义，并不声称导出点全局可除。
特征多项式恒等式准确给
$$
 a_q-(q+1)\varphi_q
       =-q\varphi_q^{-1}(\varphi_q^2-1).
\tag{23}
$$
所以有限—奇异值由同一局部整自同构
$-q\varphi_q^{-1}\otimes1_R$ 相连，且它与 $R\to\mathcal O$
和所有精度商相容。非 CM 情形不能将它简化成 $\varphi_q$。

## 6. 弱 stub 下降给 a+1，不能再删一个 delta

R125 §5.3 已逐 case 审核 Howard Lemma 1.6.4（出版 pp.1454–1455）：
证明只需要边的局部消失等价、Cartesian 性、低精度归纳及
$2k-1$ 到 $k$ 的提升；不需要把局部同构提升成全局 correction。
完整量化的 stub 深度由低精度归纳给出，不只是剩余类非零。
(23) 是所有精度来自同一个 Tate 模自同构，故本题实际类族
满足其全部弱版本输入。H.0–H.5 已在 §4 核实，辅助素数可
在任何所需的更高同余精度选取。

因此 Howard Theorem 1.6.1 的有限下降将 leading 放入
$\delta^{\operatorname{length}M}$ 倍的自由 Selmer 格。
(10) 使余下 Sha 有限；取精度超过其指数与 $a+1$，由
(21) 的真实指数得
$$
                    \operatorname{length}M\le a+1,
                    \quad S\simeq M\oplus M.
\tag{24}
$$
这证明 (7)。

为何不再照 R125 §6 除 $\delta$：本次原始 $B$ 类的
augmentation 是 $a_\ell$ 乘 $E$ 的原导出 Heegner 类，
而不是零。具体在实际对角 $A[\delta]\simeq E[p]$ 的规范下，
(19) 特化类的剩余值等于该 augmentation 的负号；该反号
与 §4.2 的 Kummer 图一致。$a_\ell$ 是单位，而高层 $P[n]$
没有被证明全部为零。因此不能断言整族剩余值为零、不能
用高精度唯一前像把全族除以 $\delta$。只看首项 (4)
不足以做这一步。

## 7. Cassels–Tate 原始层及尖锐的两步结论

由标准 Heegner 共轭公式及 $w(E)=+1$，
$cQ=-\tau^bQ$。可能的有理 cusp 平移为零，因为
$E(\mathbb Q)_{\rm tors}=0$。R122 §§1–2 的整平衡同构与
有限 Cassels–Tate 层证明只使用 norm-one augmentation 格
及 $E$ 的主极化，**不使用 CM**，故在 (5) 同样成立。
它给一个完美对称配对 $B_S$，满足
$$
 B_S(\delta x,y)=-B_S(x,\delta y),
 \qquad B_S(cx,cy)=-B_S(x,y).
\tag{25}
$$
精确长度 $n$ 的原始商
$$
 P_n=S[\delta^n]/\bigl(S[\delta^{n-1}]+\delta S[\delta^{n+1}]\bigr)
$$
上，$B_S(x,\delta^{n-1}y)$ 非退化：
奇数 $n$ 的两个符号维数相等；偶数 $n$ 的每个符号维数
各为偶数。这些是完整层条件，而非只用 $\#S$ 为平方。

实际 Mordell–Weil Kummer 线的符号为 $(-1)^a$。
理由是 $c\delta c=-\delta$ 先使点商的符号为 $(-1)^{a+1}$，
而 $\kappa_\delta(cP)=-c\kappa_\delta(P)$ 再引入一次反号。
由 (17)、负扭曲秩一及有限 Sha，固定例外集外
$$
 s_+=r+d_p,\qquad s_-=1,
$$
从而
$$
 (t_+,t_-):=
 (\dim S[\delta]^+,\dim S[\delta]^-)
 =\begin{cases}
 (r+d_p-1,1),&a\text{ 偶},\\
 (r+d_p,0),&a\text{ 奇}.
 \end{cases}
\tag{26}
$$
这里已保留 Kummer 反号，没有沿用旧 CM 辅助位的
$+1-2r_\pm$ 修正；本次该整个位的 $H^1$ 是零。

若 $a$ 偶，唯一一个负 socle 强迫恰有一对奇长度块，
各一正一负；没有偶长度负块（其重数须偶）。
这对块最短总长度 $2$，其余 $r+d_p-2$ 个正 socle
必须来自长度至少 $2$ 的偶块，给
$\operatorname{length}S\ge2r+2d_p-2$。
若 $a$ 奇，所有块都是偶长度，故
$\operatorname{length}S\ge2(r+d_p)$。
同时 $r+d_p$ 必为偶数。这完整证明 (8)。

结合 (24)：

- $a=0$ 时，$2r+2d_p-2\le2$，迫 $r=2,d_p=0$。
  并且所有界取等，$S\simeq(\mathcal O/\delta)^2$，
  两个 socle 符号各一维。
- $a=1$ 时，$2r+2d_p\le4$，同样迫 $r=2,d_p=0$。
  此时 $S\simeq(\mathcal O/\delta^2)^2$，两个 socle 都为正号。

$d_p=0$ 蕴含整个 $p$ 初级 Sha 为零，因为任意非零 $p$ 初级
元素均有非零的阶 $p$ 多重。于是
$$
 \boxed{\quad Q\notin\delta^2(A(F)\otimes\mathbb Z_p)
       \ \Longrightarrow\
       r=2,\quad\Sha(E/\mathbb Q)[p^\infty]=0.\quad}
\tag{27}
$$
这还说明额外的 $+1$ 并非可以任意删除的记号成本：
即使 $a=0$，本次实际范数一簇仍有非零的有限 Sha。

## 8. 一个适用于实际 Q 的有限半局部充分检验

本节直接推广 R130 的具体有限行，而不重复 Bernardi 高度。
置
$$
 \mathcal P=\mathcal O_L\otimes\mathbb Z_p,
 \quad I_p=\ker N_\Gamma=(\tau-1)\mathcal P.
$$
若 $p$ 在 $F$ 分裂，令 $s=\operatorname{Art}_{L/F}(\mathfrak p)$，
$$
 D_p=(s^2-a_ps+p)(s^{-2}-a_ps^{-1}+p).
$$
若 $p$ 在 $F$ 惰性，$(p)$ 在环类群中为主理想，故它在
$L/F$ 完全分裂；此时置
$$
                   D_p=(p+1)^2-a_p^2.
\tag{28}
$$
这些是实际 Frobenius 多项式，杀掉 $E(L)$ 的全部 $p$ 处约化。
由 (2)，augmentation 分别为 $(p+1-a_p)^2$ 及
$(p+1)^2-a_p^2$，都是 $p$ 单位。令 $R=D_pQ$，则
$R$ 在全部 $p$ 处 formal，$\log_E R/p\in I_p$。
整最小模型的 $\omega/dt\in\mathbb Z_p[[t]]$，所以对
$t\in p\mathcal P$ 有
$$
                      \log_E(t)/p\equiv t/p\pmod p.
\tag{29}
$$
这是每个次数 $n\ge2$ 的估值 $n-v_p(n)\ge2$，不要求 CM。

定义实际半局部向量
$$
 \mathcal T_{2,p}(Q)=
 \sum_{j=0}^{p-1}\binom j2\,
                   \frac{t_E(\tau^jR)}p
          \pmod {p\mathcal P}.
\tag{30}
$$
不分歧 normal basis（及分裂处的置换基）使 $I_p$ 是
$\mathcal O\otimes(\mathcal O_F\otimes\mathbb Z_p)$ 的自由秩一格。
在 $\mathbb F_p[\Gamma]$ 中
$$
 \sum_j\binom j2\tau^j=\tau^2(\tau-1)^{p-3},
$$
其在 $I_p/pI_p$ 上的核提升后准确为 $\delta^2I_p$，
如 R130 的整 normal-basis 证明；其中 $pI_p\subset\delta^2I_p$
及 augmentation 核的饱和性都保留。
若 $a\ge2$，实际 $Q=\delta^2S_0$ 可在点群的 $p$ 进完成中
实现；同一 $D_p$ 与对数给 $\log R/p\in\delta^2I_p$，
于是 (30) 为零。因此
$$
 \boxed{\quad \mathcal T_{2,p}(Q)\ne0
       \ \Longrightarrow\ a\le1
       \ \Longrightarrow\ \Sha(E/\mathbb Q)[p^\infty]=0.\quad}
\tag{31}
$$
该行保留所有 $p$ 上素位；若 $L/F$ 在 $p$ 完全分裂，
$\Gamma$ 作用在完成的整个置换模上，不能只取一个完成
并将它的作用设为平凡。若 (30) 非零，则 $Q$ 自动非扭，
所以应用本篇前述条件不需另验证非扭性。

R138 已提供无穷多合法的普通、非异常 $p$；它本身没有证明
(30) 对无穷多输入非零。这个指定实际行仍是剩余全局任务。

## 来源和核查范围

- J.-P. Serre（1972），*Propriétés galoisiennes des points
  d'ordre fini des courbes elliptiques*，Invent. Math. **15**，
  259–331，Introduction 的开像定理及 §4；
  [作者页面全文](https://www.college-de-france.fr/media/jean-pierre-serre/UPL5874918517843398173_Serre_proprie_te_s_galoisiennes_des_courbes_elliptiques.pdf)。
  本文只在固定非 CM 曲线上删除固定有限例外，不用一致性猜想。
- R136：全部固定曲线、负扭曲、Heegner 域和原点。
- R138 §4：原辅助位的完整 $H^1=0$；§3 给实际大因子输入。
- R119 的整角色证明；J. Nekovář（2007），*The Euler system
  method for CM points on Shimura curves*，Theorem 3.2、§3.5.1，
  [作者全文](https://webusers.imj-prg.fr/~jan.nekovar/pu/euler.pdf)。
  本文不除 $p$，非 CM 条件使该定理的 CM 例外自动不发生。
- B. Howard（2004），*The Heegner point Kolyvagin system*，
  Compositio **140**，1439–1472，H.0–H.5、Lemmas 1.6.2–1.6.4、
  Theorem 1.6.1、Proposition 1.7.4；
  [出版全文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1BF8414258216C1575963BBDA814CB2F/S0010437X04000569a.pdf/the-heegner-point-kolyvagin-system.pdf)。
  R125 §5.3 已逐 case 证明实际局部可逆关系足以支付完整 weak-stub
  深度；本文补齐非 CM 族、全部局部条件和不可再除的 $\delta$。
- R113、R122 的整平衡同构和原始 CT 层论证；本文明确核其
  norm-one 格证明不使用 CM，并重新计算新的两个符号维数。
- R130 的半局部整核计算；本文 (28)–(30) 支付新曲线的全部输入。
