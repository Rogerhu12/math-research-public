# R880 — 原三条 Artin 共轭、同次数 Hom 基与双轴 shadow 的整变换

日期：2026-11-16。

**状态：完整准 Hom 等式、双轴九项循环恒等式及在 5、7 处的整可逆性已证明。原候选 \(P=\Xi _0u\) 的次数二次型值为376；只有原坐标 producer 通过完整恒等式认证后，下面三条准 Hom 才作为次数376的实际曲线映射用于求交。本篇不以 q 前缀或次数整数替代该认证。尚未算出原 \(Z_{\rm orig}\) 的一个非零 shadow。**

本篇保持原 \(C=X_0(2601)\)、\(X=X_0(10404)\)、\(q_0,q_2\)、第一因子 \(F\)、两轴各自的新形式投影以及全部 Artin 系数。它把实际求交的三基由大次数的 Hecke 和映射改成同一 \(P\) 的三个共轭；没有更换原循环或引入 canonical 循环。

## 1. 同一个原候选和九次 Artin 作用

用 R862/R864/R874 的规范：
$$
K=\mathbf Q(\omega),\quad \delta=1+2\omega,\quad
\alpha=-1+2\omega,\quad c=-1-19\omega=\alpha^3\omega^2,
$$
$$
b^3=c,\quad \zeta=b/\alpha,\quad \zeta^3=\omega^2,\qquad
b_j=\omega^j b,\quad \zeta_j=\omega^j\zeta\quad(0\leq j\leq2).
\tag{1}
$$
全局系数嵌入和三个标签固定为
$$
(f_0,f_1,f_2)=(g_{10},g_{16},g_4).
\tag{2}
$$
改换原始九次根时必须同时置换这些标签，不能只换一个有限域根。

原十七挠点乘积 \(h\) 生成 \(H_9/K\)。记
$$
\widetilde\tau=\operatorname{Art}_{H_9/K}((\alpha)),\qquad
\tau=\widetilde\tau|_L,\quad L=K(\sqrt[3]{17}),\qquad
h^{\widetilde\tau}=\alpha h/\ell .
\tag{3}
$$
R864 的完整余循环给
$$
\widetilde\tau^3(h)=\omega h,\qquad
\operatorname{Norm}_{L/K}\ell=c.
\tag{4}
$$
系数域中的 \(\zeta_j\) 不随此 Artin 动作移动。这一延拓存在：原
\(H_9/K\) 在3处不分歧，而 \(K(\mu_9)/K\) 在3处全分歧，故两域交为 \(K\)。

设
$$
G_j=1+\frac{\tau^2\ell}{b_j}+\frac{c}{\ell b_j^2}.
\tag{5}
$$
由 \(b_j^3=c\) 及 \(\ell\,\tau\ell\,\tau^2\ell=c\)，逐项有
$$
\boxed{hG_j=h+\zeta_j h^{\widetilde\tau}
                   +\zeta_j^2h^{\widetilde\tau^2}.}
\tag{6}
$$
再用 (4) 和 \(\zeta_j^3=\omega^2\) 得
$$
\boxed{(hG_j)^{\widetilde\tau}=\zeta_j^{-1}hG_j.}
\tag{7}
$$
这保留原有限角色，而不只是三个不同的特征值。

令
$$
E=\mathbf Q(\vartheta),\quad \vartheta^3-3\vartheta+1=0,\quad
\epsilon_2=\vartheta^2-2,
$$
$$
u=\frac{915+1097\vartheta+2962\epsilon_2}{55569}.
\tag{8}
$$
按原三条形式的系数嵌入记 \(u_j\) 为 \(u\) 的三个像。R874/R875 给
$$
P=\Xi_0\circ u\in\operatorname{Hom}^{0}(J_0(2601),C_v),
\quad
\operatorname{Norm}_{E/\mathbf Q}(u)=-17/55569,
\quad q(P)=376.
\tag{9}
$$
这里 \(q\) 是原极化的次数二次型；(9)自身不声称 \(P\) 已为整 Hom。

固定
$$
C_v:Y^2+vY=X^3,\quad d=h/2048,\quad d^3=v/2,\qquad
\kappa(X,Y)=(X/d^2,\,2Y/v+1).
\tag{10}
$$
则 \(\kappa^*\omega_0=d\omega_v\)，原微分满足
$$
P^*\omega_v=H_u(q)\frac{dq}{q},\qquad
H_u=\frac13\sum_{j=0}^2u_jG_j f_j.
\tag{11}
$$

## 2. 三个同度共轭和完整矩阵

定义三个准 Hom
$$
\boxed{\mathcal A_r=(\kappa\circ P)^{\widetilde\tau^r},
\qquad r=0,1,2.}
\tag{12}
$$
若 \(P\) 已经由原坐标证书认证为实际映射，则 (12) 是同一个
\(C\to E_0\) 映射的三条 Artin 共轭，均把 \(\infty\) 送到 \(O\)，且
$$
\deg\mathcal A_0=\deg\mathcal A_1=\deg\mathcal A_2=376.
\tag{13}
$$
这是域自同构和目标同构保持映射次数的结论；没有形成 Hecke 邻点的和映射。

把 (7)、(10)、(11) 合起来，得到
$$
\boxed{
\mathcal A_r^*\omega_0=
\frac{h}{3\cdot2048}
 \sum_{j=0}^2\zeta_j^{-r}u_jG_j f_j(q)\frac{dq}{q}.
}
\tag{14}
$$
因此相对于原有序 \((f_0,f_1,f_2)\)，完整矩阵是
$$
\boxed{
V\operatorname{diag}\!\left(
\frac{hu_0G_0}{3\cdot2048},
\frac{hu_1G_1}{3\cdot2048},
\frac{hu_2G_2}{3\cdot2048}\right),
\quad V_{rj}=\zeta_j^{-r}.
}
\tag{15}
$$
特别没有剩余的 \(h/h^{\widetilde\tau^r}\) 行因子：
该因子只出现在单独变换 \(P\) 的 Gauss 行时，随后被
\(\kappa^{\widetilde\tau^r}\) 的真实尺度消掉。

有限 Fourier 逆为
$$
\boxed{
\mathcal B_j=\frac13\sum_{r=0}^2\zeta_j^r\mathcal A_r,\qquad
\mathcal B_j^*\omega_0=
\frac{hu_jG_j}{3\cdot2048}f_j(q)\frac{dq}{q}.
}
\tag{16}
$$
(16) 在选定 CM 符号的 \(\operatorname{Hom}^{0}\otimes_{K,\iota}\mathbb E\) 中成立（见附录A）；另一符号逐项共轭。
证明只用
\(\sum_{r=0}^2(\zeta_j/\zeta_k)^r=3[j=k]\)
及该原 CM 线性 Hom 模上的特征零微分单射。不能将单一全纯微分的忠实性扩到未拆 CM 符号的 \(\operatorname{Hom}^{0}\otimes_{\mathbf Q}\overline{\mathbf Q}\)。

它也是完整九次 Artin projector，而不是把一个九次角色改成三次角色。
由 (4)、(14) 得
\(\mathcal A_0^{\widetilde\tau^3}=[\omega]\mathcal A_0\)；故
$$
\frac19\sum_{s=0}^8\zeta_j^s\mathcal A_0^{\widetilde\tau^s}
=\frac13\sum_{r=0}^2\zeta_j^r\mathcal A_r.
\tag{17}
$$
这里 \(\zeta_j^3\omega=1\)，正好支付三重分组的中心相位。

每个 \(\mathcal A_r\) 还满足原全 Hom 的
\(\mathcal A_rR_C=[\omega]\mathcal A_r\)。
因为 \(q_0R=R_Cq_0\)、\(q_2R=R_Cq_2\)，它们与原 \(F\)
组成的曲线继续满足 R841/R859 的完整中央三阶等变性。

## 3. 精确返回原 Hom，不放大实际求交映射

R862 的旧三基记为 \(\mathcal A_i^{\rm old}\)，以免与 (12) 混淆：
$$
(\mathcal A_i^{\rm old})^*\omega_0
=\frac h3\sum_{j=0}^2 b_j^iG_jf_j\frac{dq}{q}.
$$
所以整条等式是
$$
\boxed{
\mathcal A_i^{\rm old}
=2048\sum_{j=0}^2\frac{b_j^i}{u_j}\mathcal B_j
=\frac{2048}{3}\sum_{r=0}^2
 \left(\sum_{j=0}^2\frac{b_j^i\zeta_j^r}{u_j}\right)\mathcal A_r.
}
\tag{18}
$$
所有原 \(\Gamma_g,\Gamma_h\) 在旧三基中的固定系数直接乘 (18)；
没有重新选择原准同态或省略其整数清分母。

尤其对旧 \(i=0\) 的各单独新形式分量，
$$
\mathcal A_0^{\rm old}e_j=\frac{2048}{u_j}\mathcal B_j.
\tag{19}
$$
因此求交时可以始终使用 (12) 的次数376映射，再在循环群中作有限线性组合。
不必真的构造 \(17\Xi_0\)、\(51\Xi_i\) 或目标上的大倍点映射。
(18) 中出现 \(b_j^i\) 时保留它；证明在7处的整性时则用 (16)/(19)
的单独原形式，不通过可能带 \(\alpha^{-1}\) 的旧 \(b\)-基逆矩阵。

## 4. 原双轴九项循环恒等式

在原
$$
X=X_0(10404),\qquad q_0,q_2:X\longrightarrow C=X_0(2601)
$$
上，令
$$
Z_{rs}=\Pi_{\rm top}
  (F,\mathcal A_rq_0,\mathcal A_sq_2)_*[X].
\tag{20}
$$
基点项按 R831/R839 的原 modified diagonal 与 \(\pi_1^{\otimes3}\)
处理。对固定同一 \(F\)，该循环在后两个 Hom 变量分别线性；
这是 Chow 动机 \(h^1\) 的加法性质，不能先把曲线点当线性组合。
由 (16) 遂得
$$
\boxed{
Z_{jk}^{\rm eig}
=\Pi_{\rm top}(F,\mathcal B_jq_0,\mathcal B_kq_2)_*[X]
=\frac19\sum_{r,s=0}^2\zeta_j^r\zeta_k^s Z_{rs}.
}
\tag{21}
$$
例如用原旧 \(i=0\) 两线时，
$$
Z_{jk}^{\rm old}
=\frac{2048^2}{u_ju_k}Z_{jk}^{\rm eig}.
\tag{22}
$$
其它原 \(\Gamma\) 的系数逐项用 (18) 运输。

原三个不同形式对仍是
$$
(g_{10},g_{16}),\qquad(g_{16},g_4),\qquad(g_4,g_{10}).
\tag{23}
$$
不能只取总 \(\eta\) 投影替代两个轴的 (21)。例如
\(\beta_{10}\beta_{16}=\beta_4^2\)；
相应总角色也会收到另一个平方来源。(21) 同时保留两个准确 Hecke/Artin
角色，正是排除这一混入的实际九项公式。

若还需原 \(H_{34}/K\) 的 projector，保
$$
e_\chi=\frac1{18}\sum_{\sigma\in\operatorname{Gal}(H_{34}/K)}
 \chi(\sigma)^{-1}\sigma
\tag{24}
$$
及固定系数嵌入。它作用于循环或点因子，系数
\(\zeta_j^r\zeta_k^s\) 不随这个投影动作一起共轭。
将 (21) 代入 (24) 是有限的完整原 Artin 组合，不需要任何极限。

## 5. 5、7 处为何都是真整可逆变换

下述论证在每一个位于 \(\ell=5\) 或7之上的系数域素位成立。

第一，原 \(E_0\) 在5、7好约化，17与残余特征互素。
非零17挠点的约化仍为非零17挠点，故不落 \(O\)，也不落
\(X=0\) 的阶3点。因此每个 \(X([u]P_{17})\) 均为当地单位，
原16项乘积 \(h\) 及其全部共轭均为单位。式 (6) 立即给 \(G_j\) 整。

第二，使用两边的真正整基，而非带范数7的 \(\alpha\)-基。令
$$
a^3=17,\quad t=(a^2-a+1)/3,\qquad
\mathcal O_F=\mathbf Z[1,a,t],\quad
\mathcal O_E=\mathbf Z[1,\vartheta,\vartheta^2-2].
$$
R874 的原线性函数 \(\lambda:E\to F\) 在这些基中的矩阵为
$$
\boxed{
L_\lambda=
\begin{pmatrix}
1&-480&684\\
0&220&-119\\
0&-51&-225
\end{pmatrix},
\qquad \det L_\lambda=-55569.
}
\tag{25}
$$
两域判别式分别为 \(-867\)、81，而 \(55569\) 模5为4、模7为3。
所以两边整基的全部嵌入矩阵以及 (25) 在这些位均可逆。

具体地，若 \(e_i=(1,\vartheta,\vartheta^2-2)\)，则
$$
\lambda(e_i)=\frac13\sum_j G_j e_i^{(j)}.
$$
由 (7) 得其三条共轭行
$$
\bigl(\tau^r\lambda(e_i)\bigr)_{r,i}
=
\operatorname{diag}\!\left(\frac{h}{h^{\widetilde\tau^r}}\right)
\,V\,\operatorname{diag}(G_j/3)\,
\bigl(e_i^{(j)}\bigr)_{j,i}.
\tag{26}
$$
左边由 (25) 与 \(F\) 的嵌入矩阵可逆；右边的首矩阵、\(V\)
及末矩阵均为单位矩阵。故 \(\prod_jG_j\) 是单位。
由于各 \(G_j\) 已由 (6) 证明整，遂每一个 \(G_j\) 都是单位。
这里没有从一个任意可逆矩阵误推每个条目非零或为单位。

第三，(8) 的分母在5、7是单位，且
\(\operatorname{Norm}(u)=-17/55569\) 是单位，故三个 \(u_j\) 也各为单位。
于是 (15)、(16)、(19) 均给原三个单独形式之间的整可逆变换。

还保以下实际尺度：

- \(d=h/2048\)、目标缩放 \(\lambda(u)\) 的范数34，以及
  \(\theta_{17}\) 的六次扭曲尺度，在5、7均为单位；
- 双轴 Fourier 的 \(1/9\)、中央三阶 projector 和 Artin 的 \(1/18\)
  均为单位；
- 原 \(X_0\) 两条 degeneracy 的次数6、旧空间返回 \(6^{-2}\)，以及
  \(X_1\) 版本的12、1632、816，仅含2、3、17；
- (21) 不引入 \(1,\,T_7,\,T_{13}\) 基的 index5，也不引入旧
  \(b=\alpha\zeta\) 逆基中的范数7分母。

若另外选用原 \(\Gamma\) 的人为整数倍，仍按 R859 保那一个整数；
本篇只证明上面显示的原规范变换没有新增5或7成本。
原第一因子 \(F\) 的规范及其是否为真 Manin1映射由 R878 的完整坐标
证书独立认证，不由本篇假定。

## 6. 同一原 shadow 的具体有限求和

取一个固定好惰性素数 \(r\)，使原系数域可按 R859 在同一素位约化，
记 \(\varphi_r\) 为 \(E_0\) 的真正 \(r\) 次 Frobenius。
当原两份坐标证书均已通过，(20) 的每一项可直接读为
$$
\boxed{
S_r(Z_{rs})=
\operatorname{Alb}\,
(\overline{\mathcal A}_sq_2)_*
(\overline{\mathcal A}_rq_0-\varphi_r\overline F)^*[O].
}
\tag{27}
$$
这是 R859 在本篇原中央三阶等变映射上的完整公式。
所有闭点、交点重数及 \(\infty\) 的边界都在 pullback 除子中；
不只取仿射坐标等式的不同零点。
再用 (21)、(24) 及原 \(\Gamma\) 系数即可得到原指定 Artin 分量，
没有 canonical 来源替换。

若为降低实际交点次数使用三循环 \((1\,2\,3)\)，它在
\(\Pi_{\rm top}\) 上为 \(+1\)：两个奇 \(h^1\) 的交换各给负号，
三循环为两次交换；同一等式在原 CM 可逆 Chow 线上成立。
故也可用完全等价的
$$
S_r(Z_{rs})=
\operatorname{Alb}\,\overline F_*
(\overline{\mathcal A}_sq_2-
       \varphi_r\overline{\mathcal A}_rq_0)^*[O].
\tag{28}
$$
这把两条求交映射都限制在次数376的原 \(P\) 共轭，
把 \(F\) 留到闭点 push/trace，未改变 source 或 Frobenius 方向。

最小可读的两种候选是 \(r=29,\ell=5\) 与 \(r=41,\ell=7\)。
因为
$$
E_0(\mathbf F_{r^2})=E_0[r+1],\qquad
r+1=30\ \hbox{或}\ 42,
$$
乘6后分别读真实5或7挠部分。
较小的惰性 \(r=5,11,23\) 的 \(r+1\) 只有2、3因子，
不能在 R859 倒置6的范围提供这种检测。
这里仅固定后续执行参数的可用范围，尚未声称任一 (27)/(28) 非零。

## 7. 与实际 producer 的接口及结论范围

输入必须是已严格认证的两份 sol：R878 的原 \(F\)，以及 R870/R874
同一 \(u\) 的 \(P\)。先撤回 producer 为改善目标系数所作的真实
\(X_{\rm new}=\lambda(u)^2X\)、\(Y_{\rm new}=\lambda(u)^3Y\)，
再按 (10)、(12) 同时共轭全部目标和原系数。
\(\widetilde\tau\) 的代数输入正是 R864 的 \(\ell\) 和
\(h^{\widetilde\tau}=\alpha h/\ell\)，不能另挑一个相容范数根。

这样只需三份同次数实际坐标、两个独立三项 Fourier 矩阵及九项闭点迹。
若其中一个原 Artin 组合的 \(\ell\)-挠 shadow 被准确算成非零，
R859 给的是同一 \(Z_{\rm orig}\) 的真实 \(\ell\)-adic Abel–Jacobi 非零。
本篇没有执行该求交，没有声称坐标证书已经通过，
也没有把原 R817 在7993的 canonical 检测移到这里。

## 来源

- R831：原 \(X_0/X_1\)、两条 degeneracy、完整 endpoint 与尺度。
- R839/R841：完整 Hom 展开、Chow 双线性及中央三阶等变。
- R859：原 Frobenius shadow、闭点迹、整比较与全部边界。
- R862/R864：实际17挠点乘积、完整有限角色及定向 \(\widetilde\tau,\ell\)。
- R874/R875：原候选 \(u\)、整 \(\lambda\) 矩阵、次数二次型及精确值376。
- R867：原 Hecke 返回；本篇不需要实际形成其大次数映射。
- R878：原第一因子的独立坐标认证门。

本篇各式为符号推导；没有新增数学数值执行或重算数据。


## 附录 A. 直接整循环检测、CM 符号及旧分母的准确作用

本附录仍以两份原特征零坐标证书成功为前提，固定原
\(F,\mathcal A_0,\mathcal A_1,\mathcal A_2\)，不提前断言这些坐标已认证。
它支付 \(r=29,\ell=5\) 的实际检测所用整表示；
不要求先对该表示乘原有理对应的一切人为清分母整数。

### A.1 先固定同一个 CM 符号

正文(16)、(17)中的 \([\omega]\) 只有在选定的
\(K\)-线性 Hom 模上才作为系数 \(\omega\) 使用。
在完整有理系数对应中，应先保留准确的 CM 幂等元
$$
e_\omega=\frac{[\omega]-\omega^2}{\omega-\omega^2},
\qquad
e_{\omega^2}=\frac{[\omega]-\omega}{\omega^2-\omega}.
\tag{A1}
$$
这里 \([\omega]\) 是实际 CM 对应，系数中的 \(\omega\) 使用已固定的嵌入；
二者在施(A1)之前不能相认。分母的范数为3，故在所有 \(\ell>3\) 处为单位。

在原最高块上可在任一因子施同一个 push 符号；
两条最高线的三个 CM 符号各自相同。
特别 R859 的 shadow 与第三因子的(A1)相容，准确为
$$
S_r\circ e_\omega^{(3)}=e_\omega\circ S_r.
\tag{A2}
$$
三循环到正文(28)后，同一投影由输出 \(F\) 的实际 CM 作用读取。
另一个符号必须将 \(\omega,\zeta_j\) 和全部原角色同时共轭。

现在原 \(\mathcal A_0^{\widetilde\tau^3}=[\omega]\mathcal A_0\)
及 \(\zeta_j^3\omega=1\) 才使完整九次 projector 化为三项。
这是 \(\operatorname{Hom}^0\otimes_{K,\iota}\mathbb E\)
或对应 CM 线上的恒等式；未拆符号的
\(\operatorname{Hom}^0\otimes_{\mathbf Q}\overline{\mathbf Q}\)
不能只用单一全纯微分判断为零。

### A.2 与原两个单独 Hecke 因子相同的整代表

取 \(\ell=5\) 或7以及系数完备整环 \(\mathcal O\)。
对正文(23)的一个固定有序对 \((j,k)\)，令
$$
\mathcal C_{jk,\chi}
=e_\omega^{(3)}e_\chi
\frac19\sum_{r,s=0}^2\zeta_j^r\zeta_k^s
\Pi_{\rm top}(F,\mathcal A_rq_0,\mathcal A_sq_2)_*[X].
\tag{A3}
$$
若原来源已作 point-factor 投影，则不重复施 \(e_\chi\)。
式(A3)是真实态射推前循环的有限组合。其全部显示分母只来自
\(3,9,18,\omega-\omega^2\)，在 \(\mathcal O\) 中均可逆；
所有根单位也整。椭圆 CK 投影用目标 \(O\)，不需要另引 cusp 的整数倍。

(A3)的两个独立 Fourier 矩阵同时选定两个原新形式；
它不是只取总 \(\eta\) 角色的循环。正文(14)中的每个
\(hu_jG_j/(3\cdot2048)\) 非零，原第一因子也已由其证书固定。
故(A3)有理化后正是 R831 对应端点类在原 CM 因子上的非零
\(h^1\) 同构的像。具体旧第零基仍保正文(22)的
\(2048^2/(u_ju_k)\)，其余旧基使用(18)；
\(X_0/X_1\) 和 old-space 的 \(6,12,1632,816\) 仍按 R831 返回。

若原归一还含非零代数标量或有理 \(h^1\) 对应，
它们在有理系数中保留并使用其逆。
这里没有令其数值为1，也没有把不同 cycle 认作相同；
只使用已经证明的同一原因子上的同构。
因此
$$
AJ_\ell(\mathcal C_{jk,\chi})\otimes\operatorname{Frac}\mathcal O\ne0
\quad\Longrightarrow\quad
AJ_\ell(Z_{jk,\chi}^{\rm orig})\ne0.
\tag{A4}
$$
在该原单独 CM 线上，此非零性也随同构双向保持。

### A.3 实际有限点式及无挠返回

将(A3)在原同一素位约化。保所有 point-factor Artin 动作，
直接由正文(28)得到
$$
\begin{aligned}
\mathscr S_{jk,\chi}
={}&\frac1{162}\,e_\omega
\sum_{\sigma\in\operatorname{Gal}(H/K)}
 \chi(\sigma)^{-1}
\sum_{a,b=0}^2\zeta_j^a\zeta_k^b\\
&\quad\cdot
\operatorname{Alb}\,
\overline F^{\,\sigma}_*
\left(
\overline{\mathcal A}_b^{\,\sigma}q_2
-\varphi_r\overline{\mathcal A}_a^{\,\sigma}q_0
\right)^*[O].
\end{aligned}
\tag{A5}
$$
在(A5)中，好素数为 \(r\)，内和的 \(a,b\) 是三条共轭的标签。
每个 \(\sigma\) 项都在同一所选几何素位取约化；
系数 \(\zeta_j,\chi(\sigma)\) 不跟着 point-factor 共轭。
全部闭点重数、剩余域迹和分母零点的延拓仍属于(A5)。

该式是 \(\mathcal O\)-整循环的真正 shadow。
若(A5)非零，R859 的整比较先给
\(AJ_\ell(\mathcal C_{jk,\chi})\ne0\) 于整全局 \(H^1(H,T_A)\)。
R859(20)证明这个模无挠，故其有理化仍非零，继而由(A4)返回原类。

这里也说明旧清分母的准确逻辑。若
\(\mathcal Z^{\rm old}=c\,\mathcal C_{jk,\chi}\) 于有理系数中，
其中 \(c\ne0\)，则有理 AJ 的非零性不要求 \(v_\ell(c)=0\)。
预先计算 \([\ell]\mathscr S_{jk,\chi}\) 却可能把非零的有限
\(\ell\)-挠点杀掉；因此它是更弱的检测，不能被当成必须的准备步骤。
原旧 \(D\) 或某个人为整倍数含 \(\ell\)，不阻止直接使用(A3)的检测。
这不是从一个有理非零有限域 Chow 类推结论；真正使用的是整 shadow
和无挠的特征零全局 \(H^1\)。

R814 的 \(1/30\) 出现在其 canonical 椭圆单位／regulator 比较，
不是 R831 端点循环定义的一项任意新增乘子。
本附录没有将两个来源相认，也不把该30机械乘入(A3)。

### A.4 两种有限域必须分别实现

(A3)所需最小角色系数域可取 \(\mathbf Q(\zeta_9)\)，
因为 \(\zeta_j,\omega,\chi\) 都在此域；
原 \(u_j\) 也在其全实子域，但(A3)甚至不需除 \(u_j\)。
这个系数域与几何定义域 \(H\) 的作用始终分开。

| 好素数与检测素数 | 几何点群 | 角色系数的剩余域 |
|---|---|---|
| \(r=29,\ell=5\) | \(E_0(\mathbf F_{29^2})=E_0[30]\) | \(\mathbf F_{5^6}\) |
| \(r=41,\ell=7\) | \(E_0(\mathbf F_{41^2})=E_0[42]\) | \(\mathbf F_{7^3}\)，保所选 \(K\) 嵌入 |

系数域结论由 \(\operatorname{ord}_9(5)=6\)、
\(\operatorname{ord}_9(7)=3\) 及 \(\Phi_9(T)=T^6+T^3+1\) 得到；
两处均不分歧。它们不是把九次根放进几何的
\(\mathbf F_{r^2}\)。

对各完整闭点迹先乘6，便只保留真正的5或7挠部分。
在该 \(\ell\)-挠部分，6为单位，不改变是否为零。
选定一个真实 \(E_0[\ell]\) 的 \(\mathbf F_\ell\) 基后，
各点成为两个 \(\mathbf F_\ell\) 坐标，再将(A5)的系数运算在表中的
角色剩余域进行。CM 矩阵 \([\omega]\) 和(A1)同样必须作用于这两个坐标；
不能把几何 \(r\) 次 Frobenius 当作角色系数域的 Frobenius。

这些式子给出可执行的同原类检测规范；本附录没有执行(A5)，
也没有宣称两份原坐标已认证或主 Sha 目标已经完成。


## 附录 B. 原 Frobenius 差映射的准确次数与完整极除子

本附录继续以两原特征零坐标证书成功为前提。
固定 \(r=29\) 或41、原几何素位及任意
\(\sigma\in\operatorname{Gal}(H/K)\)、\(a,b\in\{0,1,2\}\)。
在同一良好约化的原源 \(X=X_0(10404)\) 上置
$$
A=\overline{\mathcal A}_b^{\,\sigma}q_2,\qquad
B=\varphi_r\overline{\mathcal A}_a^{\,\sigma}q_0,\qquad
d_{ab,\sigma}=A-B.
\tag{B1}
$$
所有式子都是实际椭圆映射的群差，不是把曲线的坐标相减当群律。

### B.1 三阶作用严格消掉整个交叉项

原 \(q_0,q_2\) 的次数均为6，各实际
\(\mathcal A_a^\sigma\) 的次数为376。良好约化不改变这些次数：
源光滑、目标为好约化的阿贝尔概形，原态射由 Néron 映射性质延拓，
拉回 \(\mathcal O(O)\) 在光滑射影曲线族上的次数保持。
因此
$$
\deg A=2256,\qquad \deg B=2256r.
\tag{B2}
$$

原源三阶自同构 \(R\) 保 cusp \(\infty\)，且
$$
AR=[\omega]A,\qquad BR=[\omega^2]B.
\tag{B3}
$$
第一式来自原三条 Hom 的 R880(14)／R841 等变性；
第二式还使用真正的
\(\varphi_r[\omega]=[\omega^2]\varphi_r\)。
全部 \(\sigma\) 固定 \(K\)，故这些式子逐一保留。

对基点为 \(O\) 的椭圆映射写 \(q(C)=\deg C\)，并令
$$
b(C,D)=q(C+D)-q(C)-q(D).
$$
椭圆目标的对称线丛 \(\mathcal O(O)\) 的立方定理表明
\(b\) 是整数值的对称双加性形式。它在源自同构预合成及共同目标
自同构后合成下不变，且此结论在当前正特征也成立。
用(B3)及共同后合成 \([\omega^2]\)，得
$$
b(A,B)=b([\omega]A,[\omega^2]B)=b(A,[\omega]B).
$$
再重复一次，
$$
b(A,B)=b(A,[\omega]B)=b(A,[\omega^2]B).
$$
三式相加，右边由 \(1+[\omega]+[\omega^2]=0\) 为零。
左边是整数 \(3b(A,B)\)，所以
$$
\boxed{b(A,B)=0.}
\tag{B4}
$$
这里没有将 supersingular 目标的全部 endomorphism 环误当成交换环；
只用了实际三阶作用和整数次数的双加性。

由(B2)–(B4)，每一个原差映射的次数准确为
$$
\boxed{\deg d_{ab,\sigma}=2256(r+1).}
\tag{B5}
$$
特别它不恒定，也不可能因某个 Artin 共轭而恒等于 \(O\)。
其微分等于 \(A^*\omega_0\)，因为 \(\varphi_r^*\omega_0=0\)；
原实际单位首项保证此微分非零，故差映射可分。
这不说明每一个零纤维点都无分歧，重数仍必须保留。

### B.2 整个 pullback 除子由 x 坐标的极除子读取

在原正规化函数域中写 \(x_d=x(d_{ab,\sigma})\)。
由于目标 \(E_0\) 的 \(x\) 函数极除子恰为 \(2[O]\)，
得到精确的有效除子恒等式
$$
\boxed{
d_{ab,\sigma}^*[O]=\frac12\,\operatorname{div}_\infty(x_d).
}
\tag{B6}
$$
因此每一个极点重数均为偶数；
闭点 \(P\) 的贡献是
\(-v_P(x_d)/2\)，其几何次数还须乘 \([k(P):k]\)。
不是仅取 \(x_A=x_B,\ y_A=y_B\) 的不同仿射零点。

例如在群律的通用开集上可以计算
$$
x_d=\frac{(y_A+y_B)^2}{(x_A-x_B)^2}-x_A-x_B.
\tag{B7}
$$
(B2)的不同次数保证 \(x_A-x_B\) 不恒为零。
(B7)只是函数域表达；其所有零分母点及 \(O\) 的值，
均由同一正规化函数的赋值读取。
一切取消必须在函数域中完成后才取(B6)，否则会增删实际交重。

准确的总次数如下：

| \(r\) | \(\deg d^*[O]\) | \(\deg\operatorname{div}_\infty(x_d)\) |
|---:|---:|---:|
| 29 | 67680 | 135360 |
| 41 | 94752 | 189504 |

对每一条 \(a,b,\sigma\) 都是同一数值。
此次数包括 cusp、其余有限闭点及任何分母零点的正规化贡献。
推前到原 \(F\) 后，零循环的总次数仍等于中列；
取 Albanese 时减去这个次数倍的 \(O\)，并按 R859 保全部剩余域迹。

该表提供真实求交的完整次数条件，不能单凭总数正确就认证了全部点值。
需要将(B6)中的实际每个地方与原 \(F\) 的值逐一相接。
本附录没有运行该除子分解，没有声称其 shadow 已非零。


## 附录 C. 原十八项 Artin 动作的九个实际除子实现

本附录仍以原 \(P\) 与 \(F\) 的两份完整特征零坐标证书成功为前提。它减少的是同一个原 Artin 组合中需要分解的实际除子数；既不改变原 \(\chi\)，也不省去任一闭点、交重或系数。

### C.1 全部定义域和实际方向

令 \(H=H_{34}\)，其 \(K\) 上 Galois 群为循环十八阶；\(H_9\) 是九次子域。令 \(\sigma\) 为正文 \(\widetilde\tau\) 在 \(H\) 中的唯一九阶提升，\(\epsilon\) 为二阶元。二者交换，且
$
 \operatorname{Gal}(H/K)
 =\{\sigma^l\epsilon^e:0\le l<9,\ 0\le e<2\}.
 \tag{C1}
$
这里 \(\epsilon\) 固定 \(H_9\)。仍固定 \(\theta_{17}^6=17\)、\(a=\theta_{17}^2\) 和原实嵌入；故 \(\epsilon(\theta_{17})=-\theta_{17}\)。

实际余循环的方向为
$
 \boxed{\sigma(a)=\omega^2a,\qquad
        \sigma(\theta_{17})=\omega\theta_{17}.}
 \tag{C2}
$
第一式可直接在 R864 的 \(\ell\) 与 \(a^3=17\) 中检验。方向也由本题公开 local-input 运行 43850679589/job 133242082519 完整固定：原三个 \(a\) 的余值按 \(12,12\omega,17+17\omega\) 排列时，真实余循环给置换 \((2,0,1)\)。这不是凭另选一个有限域根替换 Artin 方向：全局 \(\sigma(a)/a\) 先已属于 \(\{1,\omega,\omega^2\}\)，三者在这个好位约化互不相同，因此一次准确余值便辨别了原全局等式。第二式由第一式先给 \(\pm\omega\)；负号会使 \(\sigma^9(\theta_{17})=-\theta_{17}\)，与 \(\sigma\) 阶九矛盾，故只能为正号。

原第一因子是在 \(\mathbf Q\) 上的 \(X\to E_{17}\) 映射后接
\((x,y)\mapsto(x/\theta_{17}^2,y/\theta_{17}^3)\)。所以
$
 \boxed{F^\sigma=[\omega]F,\qquad F^\epsilon=-F.}
 \tag{C3}
$
这些是实际映射等式，基点仍为 \(O\)，没有额外平移。

三条原共轭映射则全部在 \(H_9\) 上，且由正文(4)、(12)、(14)有
$
 \boxed{
 \mathcal A_r^{\sigma^l}
  =[\omega]^{\lfloor(r+l)/3\rfloor}
    \mathcal A_{(r+l)\bmod3},\qquad
 \mathcal A_r^\epsilon=\mathcal A_r.
 }
 \tag{C4}
$
系数中的 \(\zeta,\omega\) 不随 (C1) 的点因子作用改变；此约定与附录A一致。

### C.2 一个源自同构准确支付所有相位

在固定同一个几何约化处，定义
$
 D_j(a,b)=
 \bigl(\overline{\mathcal A}_bq_2
       -[\omega]^j\varphi_r\overline{\mathcal A}_aq_0\bigr)^*[O],
 \qquad
 P_{ab}=\operatorname{Alb}\overline F_*D_0(a,b).
 \tag{C5}
$
原 \(R\) 作用满足
\(\mathcal A_bq_2R=[\omega]\mathcal A_bq_2\)、
\(\varphi_r\mathcal A_aq_0R=[\omega^2]\varphi_r\mathcal A_aq_0\)。
因而作为完整 Cartier 除子，
$
 R^*D_j(a,b)=D_{j+1}(a,b),\qquad
 \operatorname{Alb}\overline F_*D_j(a,b)
       =[\omega]^{-j}P_{ab}.
 \tag{C6}
$
后一式使用 \(FR=[\omega]F\) 及自同构拉回在所有闭点上的准确重数与剩余域迹。它不是只对仿射相交点成立。

对 \(a,b\in\{0,1,2\}\) 和 \(0\le l<9\)，唯一写成
$
 a+l=3u+a',\quad b+l=3v+b',\qquad 0\le a',b'<3.
$
由真正 Frobenius 关系
\(\varphi_r[\omega]^u=[\omega]^{2u}\varphi_r\)，
(C3)、(C4) 及 (C6) 遂给
$
 \boxed{
 P_{\sigma^l\epsilon^e,a,b}
 =(-1)^e[\omega]^{\,l-2u+v}P_{a'b'}.
 }
 \tag{C7}
$
左边恰为附录A(A5)中的该 \(\sigma^l\epsilon^e,a,b\) 项，含其第一输出因子。式(C7)亦可在两边同时乘6后使用。它以九个完整除子 \(D_0(a,b)\) 产生全部 \(18\times9\) 个真实输入；不把 Artin 动作换成几何的 \(r\) 次 Frobenius，也不令其作用于角色系数域。

例如 \(l=3\) 时 \(u=v=1,a'=a,b'=b\)，输出为
\([\omega]^2P_{ab}\)，与两个后轴各乘 \([\omega]\) 的整个最高 Chow 块相符。\(l=9\) 时输出回到原值，故循环端的相位也准确封闭。

### C.3 原三个角色和系数消费者

在正文已固定的 CM 符号中，
\(\mathcal B_j^\sigma=\zeta_j^{-1}\mathcal B_j\)，
而 \(F^\sigma=[\omega]F\)。因此原有序对 \((j,k)\) 的点因子角色准确为
$
 \boxed{\chi_{jk}(\sigma)=\omega/(\zeta_j\zeta_k),
        \qquad\chi_{jk}(\epsilon)=-1.}
 \tag{C8}
$
这是原 \((g_{10},g_{16})\)、\((g_{16},g_4)\)、\((g_4,g_{10})\) 三对来源的完整总角色，不是只据阶数选择的角色。仍须保正文(21)的两个独立 Fourier 投影。

用 \(\zeta^3=\omega^2\)、\(\omega=\zeta^6\)，表为
$
\begin{array}{c|c|c}
(j,k)&\chi_{jk}(\sigma)&\chi_{jk}(\epsilon)\\ \hline
(0,1)&\zeta^7&-1\\
(1,2)&\zeta^4&-1\\
(2,0)&\zeta&-1
\end{array}.
\tag{C9}
$
消费者因此在固定系数域中按
\(\chi_{jk}(\sigma^l\epsilon^e)=\chi_{jk}(\sigma)^l(-1)^e\)
逐项填入原 \(1/162\) 式；几何输入则按 (C7) 使用实际 CM 矩阵。
最后仍施同一个显式 \(e_\omega\)，另一符号用全部共轭。不能在未施符号前把几何 \([\omega]\) 当成系数 \(\omega\)。

(C7)只降低求交工作量。每个 \(P_{ab}\) 仍须由 R883 的完整有效除子、共同交重、唯一额外提升及全部闭点迹算出，并核其原次数 \(2256(r+1)\)。本附录没有运行该除子计算，没有预报任一原 shadow 非零。

实际方向核验的公开 provenance：
source `de42a2c8c4850202a184b1b88e42a92c981db1ef`，
run `43850679589`，job `133242082519`，
result SHA256 `eeb45e36cad8a34e3382350f065fe1ca2ca4d51dd52182368dec1a9142136643`。
该运行只支付原 local input/方向/精度，未支付特征零坐标映射的认证门。


### C.4 先施 CM 符号后的九项最终读数

令 \(p_{ab}=[6]P_{ab}\)，并把它们在同一真实 \(E_0[\ell]\) 基中读取。
只有在先施显式 \(e_\omega\) 后，(C7)的几何 \([\omega]\) 才等于系数 \(\omega\)。
这时以 \(a=a'-l+3u,\ b=b'-l+3v\) 和 \(\zeta_j^3=\zeta_k^3=\omega^2\) 计算，
$$
 \zeta_j^a\zeta_k^b\,
 \omega^{l-2u+v}
 =
 \left(\frac{\omega}{\zeta_j\zeta_k}\right)^l
 \zeta_j^{a'}\zeta_k^{b'}.
$$
\(\epsilon\) 在 (C7) 和 \(\chi^{-1}\) 中的两个负号也相消。
因此附录A(A5)的整个十八项和，准确化为
$$
 \boxed{
 [6]\mathscr S_{jk,\chi_{jk}}
   =\frac19\,e_\omega
      \sum_{a,b=0}^2\zeta_j^a\zeta_k^b\,p_{ab}.
 }
 \tag{C10}
$$
原 \(18/162=1/9\) 的倍率完整保留。
式(C10)是在固定系数域中的两个坐标向量恒等式，不能在未拆符号的
\(E_0[\ell]\) 上先把 \([\omega]\) 替成某个系数九次根。
实现可以用 (C7) 填回既有18×9消费者，并以(C10)独立核对有限系数运算；两者使用同一九个实际完整除子，而非新增九个任意向量。
