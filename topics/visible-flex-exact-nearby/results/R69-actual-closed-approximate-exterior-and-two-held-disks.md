# R69：同一实际对象的完整闭近似外尾、正域源与两平盘尺寸

2026-11-12，independent_audit。

**状态：已证明，含同一准确参数族的连续有向证书。** 两段原始 body
在本次恢复后的运行中从头完成，分别411与893个闭 cell，均无失败或
待处理单元；没有拼接丢失运行的 partial 数据。

本篇把 [R66](R66-actual-family-positive-collar-and-natural-exterior-graft.md)
的实际 \(r=25/8\) 径向入口接到真正 R72 无限平尾，并在另一端准确镜像。
它构造同一准确参数族的闭 \(C^2\) 星形近似背景；两个平子盘的并集
具有题目要求的握持尺寸。这里的“近似”指主体与给定径向目标度量的
缺陷仍须修正，并不是将一个数值封口宣称为精确等距封口。

另将真实移动根至 \(r=25/8\) 的全部正 cell 放进一个实际角流，支付
这一完整有限正域的 Dirichlet、Poisson、DN 和普通源 contact。
无穷尾自身使用 R72 的实际全层结构，不被误称为简单正帽。
本篇未证明两个平区已在某个公共度量的有限幅精确族中同时固定。

## 1. 对象、真实有限覆盖与口径

沿用 R66 的准确参数盒

\[
 \delta_c=-7789866024620307/4611686018427387904,\qquad
 |\delta-\delta_c|\le1/2000000.
 \tag{69.1}
\]

所有 core、根领口、正 body、外接段报告必须具有同一个 origin、
direction 和准确参数区间。core 的已证较大区间按 Fraction 严格包含
(69.1)。各点仍使用自己的真实根 \(t(\delta)\)，不能将一个固定根
端点改称全族的根。

实际核心证书
[affine core](../data/phase_ring_continuation/type_fixed_step02_d5_affine_core_interval.json)
及其[完整证明](../notes/2026-11-12-exact-affine-core-support-and-log-gate.md)
给整个较大参数区间、\(|r|\le\operatorname{binary64}(.24)\)、全部实角：
\[
 F\cdot(F_\theta\times F_r)>1.13806491,\qquad |F|<1.17505412.
 \tag{69.2}
\]
其 origin/direction 是 R66 的同一对准确输入。根上包络严格小于
\(\operatorname{binary64}(.24)\)，所以它与 R66 的领口有非空重叠。

原始有限 body 的两个连续报告是
[quarter-to-one](../notes/2026-11-12-positive-family-outer-quarter-to-one.json.gz)
与 [one-to-three](../notes/2026-11-12-positive-family-outer-one-to-three.json.gz)。
每个报告使用真实仿射物理 germ、全部反射 knots、无限 primitive 的
tail 与 alias、全部实角间隙及物理复角带 \(1/512\)。其稳定曲率公式
和无限均值误差逐项证明见
[stable curvature](../notes/2026-11-12-positive-family-stable-curvature.md)。
从准确圆周切向量先减去恒定圆背景后再作区间 DFT，使大圆背景的
舍入误差不会盖住真实极小的非径向差；这个改写不改变实际对象。

合并源从原始 cell 重新以 Fraction 检查
\([1/4,1]\)、\([1,3]\) 和 \([3,25/8]\) 的无缝覆盖，检查全部
源/依赖 SHA 及 completed 标记。任何 partial、失败 cell、不同参数盒、
已改依赖或径向缺口都会拒绝输出 whole-domain 结论。每个原始正 cell
的 \(K_0>0\) 与真实支持分子 \(F\cdot(F_\theta\times F_r)>0\)
都保留；没有只从 endpoint 符号外推整段。

两个完整 body 报告的 SHA256 依次为

    1edd27337e9c3819c770501683e160395956a68cc35c2cb09e98190ba4477e15
    5e2cbd5396746bf8c41acf834b52b5ff37bc86b9d0500de6b2f1ff032ca6f6f4

它们与55个根领口 cell、64个自然权 graft cell 合计1423个正域 cell。
另一个逐 cell manifest 保存每个原始 cell 的准确区间、完整内容的
canonical-JSON SHA 和所属报告 SHA，供独立平覆盖与加总复核。

## 2. 一个整体的实际正域

取 \(x=r-t(\delta)\)，\(0\le x\le L(\delta)=25/8-t(\delta)\)。
R64/R66 的同一 \(Y_z\) ground state 给真实材料密度

\[
 B=\begin{pmatrix}\alpha&\alpha b\\
 \alpha b&\alpha b^2+\eta K_0\end{pmatrix},\quad
 \alpha,\eta>0,\quad b=-\mathcal M/\mathcal D .
 \tag{69.3}
\]

对根领口使用已付 \(K_0/(r-t)\)；其余 cell \([a_j,b_j]\) 使用
\[
 \frac{\underline K_j}{b_j-\underline t}
 \le \frac{K_0(r,\delta)}{r-t(\delta)}
 \le \frac{\overline K_j}{a_j-\overline t}.
 \tag{69.4}
\]
后者的所有分母都严格正。

令 \(I_r=\sum_j(b_j-a_j)\sup_j|b_\theta|\)，复角相应为 \(I_c\)。
最初位于根外包络下端的极短多计区间只会增加费用，故这些和控制从
每个真实根出发的同一角流。保持物理 \(r\) 不变，解
\(\Theta_r=b(r,\Theta)\)，根处 \(\Theta=\phi\)。得到
\[
 e^{-I_r}\le J,J^{-1}\le e^{I_r},\qquad
 \widetilde B=\operatorname{diag}(J\alpha,\eta K_0/J).
 \tag{69.5}
\]
因此相对于 \(A_0=\operatorname{diag}(1,x)\)，逐 cell 的
\(\alpha\) 和 \(\eta K_0/x\) 给全域 \(mI<C<MI\)。
乘子 \(\eta\) 与 \(K_0/x\) 在同一 cell 内相乘；没有把不同位置
最坏值组合成虚假的更紧界。

该角流只以真实径向坐标为时间。原 spline 的 knots 仍是固定径向
位置；不要求跨 knot 的径向解析性。角向每个所需有限导数和小正
解析宽均由同一复角管支付。

令 \(\ell_-=L_-/4,\ell_+=L_+/4\)。R36 的完整两个端口
\(\mathcal T=H^{1/3}\oplus H^{1/2}\) 可取平方常数
\[
\begin{aligned}
 C_{\rm tr}&=\max\{2\ell_++4/\ell_-+16/\ell_-^2,\,
                  2\ell_++4/\ell_-+32/(3L_-\ell_-)\},\\
 C_E&=\max\{\ell_-^{-1}+\ell_+/3+\ell_+^2/12,\,
            \ell_-^{-1}+\ell_+/3+L_+\ell_+/3\}.
\end{aligned}
 \tag{69.6}
\]

取 \(g=(1+L_+^2/\pi^2)/m\)，则完整 Poisson 和 \(V^*\) source
contact norm 不超过 \(\sqrt{C_E}(1+Mg)\)，DN 不超过 \(MC_E\)。
内部 \(L^2H^{2/3}\) 增益常数是
\(\sqrt{1+\max(3,4/L_-^2)}\)，因而同一完整 contact 对
\(L^2H^{-2/3}\) 源成立。均值、两端 cross 和 charge 恒等式均保留。

在所有输入已付物理角带的最小值 \(\sigma_c=1/512\) 上，
\[
 \rho_*=\sigma_c/(2e^{I_c}),\qquad
 M_c=e^{I_c}\max_j\{\alpha_{c,j},\eta_{c,j}(K_0/x)_{+,j}\}.
 \tag{69.7}
\]
真实复流首次出管论证及 \(J_r=b_\theta J\) 给这个实际管和系数 norm。
再令
\[
 N_C=\frac{2M_ce^{-\rho_*/2}}{(1-e^{-\rho_*/2})^2},\qquad
 C_\Lambda=C_E[1+2g(M+1)]^2 ,
\]
\[
 s_*=\min\{\rho_*/2,1/N_C,(2gN_C)^{-1},
                         (2C_\Lambda N_C)^{-1}\}>0.
 \tag{69.8}
\]
所有常数用 Arb 有向计算，分母用 expm1，不容许非有限值。
在明确的 ground-state flux frame，正负权 \(|s|\le s_*\) 的完整
归一 Robin 逆 norm 不超过2，Cayley norm 不超过5。
原物理密度源是 \(-JY_z f\circ\Theta\)，动量为
\(Y_zp_w-wp_{Y_z}\) 后的对偶角换元；这些量没有改名成另一 Airy frame。

同一256-bit合并报告实际得到下列严格安全界：

| 完整正域量 | 安全界 |
|---|---:|
| 实角流 \(J,J^{-1}\) | \(<4.137\) |
| 归一矩阵 | \(0.005804I<C<146.966I\) |
| trace 平方常数 | \(<37.710\) |
| 延拓平方常数 | \(<2.321\) |
| 零 Dirichlet 逆 | \(<317.728\) |
| 完整 Poisson / \(V^*\) contact | \(<71135\) |
| 完整 DN | \(<341.054\) |
| \(L^2H^{-2/3}\) 源到完整 contact | \(<142270\) |
| 物理 \(L^2\) 源到新密度 \(L^2\) 源 | \(<2.034\) |
| 实际复系数角宽 | \(>7.6059\,10^{-7}\) |
| 允许 signed Robin 角权 | 可取 \(2^{-95}\) |

未四舍五入值给 \(s_*>4.5313\,10^{-29}>2^{-95}\)。
这个正宽是本次充分门的实际费用，未称其已支付最终全局迭代的小量。

本节只涉及完整有限正域 \([t(\delta),25/8]\)。下面真正尾部的零势
平台、负曲率部分及无限层，不能继续使用这个简单正能量模型。

## 3. 从当前入口出发的准确长径向段

R66 已给实际
\[
 a_*=\exp(l_0+l_1/8),\quad
 Z_*=Z(3)+\int_0^{1/8}a_e^2c_e\,ds,\quad
 \omega_*=-l_1/(4c_0)\in(1.46115285,1.46115287).
 \tag{69.9}
\]
近接缝以 \(u=4c_0(r-25/8)\) 作坐标。对
\(0\le u\le T=2^{24}\)，准确定义
\[
 a(u)=a_*e^{-\omega_*u},\qquad
 z(u)=Z_*+\frac{a_*^2}{8\omega_*}
                 (1-e^{-2\omega_*u}).
 \tag{69.10}
\]
于是 \(z_u=a^2/4\)，\(h=1/a\) 满足 \(h_u/h=\omega_*\)，
\(q=\omega_u/\omega^2=0\)。所有入口四阶数据由 R66 匹配。
新段完全径向，其目标度量就是其准确诱导度量。

两主曲率绝对值不超过 \(0.171098\)，全段高度费用
\[
 0<\Delta z_{\rm rad}<a_*^2/(8\omega_*).
 \tag{69.11}
\]
在 \(u=T\) 置 \(h_T=1/a_T\)。由 (69.9)，
\[
 a_T<7\cdot10^{-6}e^{-(7/5)T},\qquad
 h_T>2^{17}e^{(7/5)T}.
 \tag{69.12}
\]
这里极长的坐标区间并不产生大的物理高度或半径。

## 4. 真 R11 connector；没有任意代换尾斜率

使用 R11 已证明的真实 R72 第四模强尾方向。令其 cut128 物理高度
斜率为 \(d_*\in(14,15)\)，则
\[
 R_*=\frac{1-d_*}{16-d_*}\in(-14,-13/2).
 \tag{69.13}
\]
这一定义使用完整无限尾的线性方向；不是从某个非零非线性尾的比值
猜一个 Robin 数。

令 \(v=\log(h/h_T)\)，取控制方程
\[
 (\log\omega)_v=q,\qquad
 R_v=q(1-R)+1-16R^2,\qquad
 (\log y)_v=16R.
 \tag{69.14}
\]
入口是当前实际 \(\omega=\omega_*,q=0,R=-1/4\)。
\(R=-1/4\) 对应 (69.10) 上的真实稳定第四模方向；此处没有宣称
非径向核心的未知解已自动落在该方向。

准确采用 R11 §§4–5 的构造：长度 \(\eta=2^{-24}\) 的
\(S(s)=10s^3-15s^4+6s^5\) 过渡到 \(q=-1\)；沿这个主段走到
唯一使下一个短过渡落在 \(q=2,R=-1/2\) 的停止值；在 \(q=2\)
上放大到 \(\omega=\Omega=2^{360}\)；再经短过渡、\(q=-1\) 主段
和末端短过渡准确落在 \(q=-8,R=R_*\)。

为核对这里确实适用于当前入口，R11 所用全部假设仅为
\[
 1\le\omega_0\le2,\quad |q_0|\le1,\quad
 -3/10\le R_0\le-1/5 ,
 \tag{69.15}
\]
且本次更有 \(\omega_0>5/4\)。短过渡上的
\(|q(1-R)+1-16R^2|\le4233\)、\(4233\eta<1/3000\)，及
\[
 \partial R_{\rm out}/\partial R_{\rm in}
 =\exp\!\int(-q-32R)\,dv>0
 \tag{69.16}
\]
都不含旧 Pöschl–Teller 主干。它们分别保证两次所需横截根唯一；
主段显式 \(P_v=P+16P^2\) 保证停止时有限。
因此这是本对象的一个明确 ODE/唯一根构造，不是尚待寻找的过渡。

准备段长小于 \(\log(11/8)+2\eta\)。其每个前缀
\(\omega>(5/4)e^{-\log(11/8)-2\eta}>9/10\)；放大段只增加
\(\omega\)。末端每个前缀 \(\omega>(4/5)\Omega\)。
在最终点 \(H_e=h_e\)、\(\omega_e\) 有
\[
 h_a\sqrt{\Omega/\omega_a}\le H_e
 <\frac65h_a\sqrt{\Omega/\omega_a},\quad
 \frac45\Omega<\omega_e<\frac54\Omega,\quad
 h_T\le h_a<\frac32h_T,\quad \frac23<\omega_a<3.
 \tag{69.17}
\]

物理高度归一始终是 \(z_u=a^2/4\)，故
\[
 z_v=\frac{a^2}{4\omega},\qquad
 \kappa_\theta=\frac1{\sqrt{a^2+16\omega^2}},\quad
 \kappa_s=\frac{16(1+q)\omega^2}{(a^2+16\omega^2)^{3/2}}.
 \tag{69.18}
\]
由全部前缀界，整个有限 connector 的两主曲率绝对值小于 \(5/6\)，
且
\[
 \Delta z_{\rm con}<\frac1{4(9/10)}
          \int_0^\infty a_T^2e^{-2v}\,dv
          =\frac5{36}a_T^2.
 \tag{69.19}
\]
任意大的 \(\Omega\) 不增加这个高度费用。

## 5. 真 R72 全无限层及准确物理匹配

参考 profile 是 R72 的 \(\epsilon=1\) 真无限尾。记
\[
 \delta_*=(2/25)2^{-128},\quad b\in(1,2),\quad
 \bar W_b=\delta_*^6/b^7 .
 \tag{69.20}
\]
按当前 \(z_u=a^2/4\) 定义
\[
 \rho=\frac1{H_eb},\qquad
 \lambda=\frac1{4H_e^2b\omega_e\bar W_b},\qquad
 \epsilon_{\rm tail}=\frac\lambda\rho
                     =\frac1{4H_e\omega_e\bar W_b}.
 \tag{69.21}
\]
参考半径为 \(\bar a=a/\rho\)，尾图为
\(z(a)=z_{\rm shift}+\lambda\bar z(a/\rho)\)，其中
\(\bar z_{\bar a}=-\bar W\)。高度平移准确匹配末端高度。
接缝上
\[
 W_e=(\lambda/\rho)\bar W_b=\frac{a_e}{4\omega_e},\qquad
 a_eW_a/W=-7=q_e+1.
 \tag{69.22}
\]
因此物理背景的完整二阶 jet 匹配，不能只说切平面匹配。

这也给真实非线性模块合法的尺度：先用 \(\epsilon_{\rm tail}\)
重新调用 R72 的参考构造，再整体等比缩放 \(\rho\)。
不对一个既有非线性等距族作各向异性空间伸缩。
由 (69.17)，\(H_e\omega_e>\frac14h_T\Omega^{3/2}\)；
\(\bar W_b>2^{-799}\)，所以
\[
 0<\epsilon_{\rm tail}<2^{259}a_T<1.
 \tag{69.23}
\]
本篇闭背景对应该模块的零内部标签。所有非零标签、非线性高模和
mean 仍是后续匹配方程的输出，不在这里任意指定或删除。

为覆盖无限尾的每个过渡，R14 §11 已从实际 log-quintic 层逐项证明
\[
 M_{\rm tail}:=\sup\max\{\bar W/\bar a,|\bar W_{\bar a}|\}
 \le 2^{14}(1+|\log\delta_*|)\delta_*^{7/2}.
 \tag{69.24}
\]
其证明对所有胞元使用
\(\bar W=\delta_j^6p_*/\bar a^7\)、
\(\eta_j=\delta_j^{3/2}/(4\sqrt2)\)、
\(|(\log p_*)_{\bar a}|\le15\sqrt6\delta_j^{-3/2}
(\log65+2|\log\delta_j|)\)；随 \(j\to\infty\) 的界趋于0。
所以它含所有平台、过渡、接缝和实际平坦极限。

正确二阶缩放是
\[
 \lambda/\rho^2=\frac b{4\omega_e\bar W_b},
 \qquad
 \max\{W/a,|W_a|\}<\frac{5\,2^{10}b^8
       (1+|\log\delta_*|)\delta_*^{-5/2}}{\Omega}.
 \tag{69.25}
\]
使用 \(b^8<2^8\)、\(1+|\log\delta_*|<96\)、
\(\delta_*^{-5/2}<625\,2^{320}\)，右边严格小于
\[
 5\,2^{10}2^8\,96\,625\,2^{320-360}
 =0.07152557373046875<1/8.
 \tag{69.26}
\]
因此真无限尾的两物理主曲率绝对值均小于 \(1/8\)，不是只用切口
\(aW_a/W=-7\) 代表整条尾。
若平坦极限半径为 \(a_{\rm flat}>0\)，则
\[
 0<\Delta z_{\rm tail}
 =\int_{a_{\rm flat}}^{a_e}W\,da
 <a_T^2/16.
 \tag{69.27}
\]
此后向盘心接固定水平盘。因为 \(W,W_a\to0\)，这是真 \(C^2\)
接合；不要求退化的 Sturm 坐标延伸到盘心。

## 6. 闭嵌入与两个平子盘的实际尺寸

主体是柱面，两个末端按前述构造接闭盘，参数流形为 \(S^2\)。
负侧使用 R66/R57 的准确径向反射，正负高度相反；所有接缝至少
\(C^2\)。主体和 graft 的实际支持分子已经连续认证为正。
新径向段与 connector 有
\[
 X\cdot n=\frac{a^2+4z\omega}{\sqrt{a^2+16\omega^2}}>0,
 \tag{69.28}
\]
真平尾为 \((z+aW)/\sqrt{1+W^2}>0\)，平盘为 \(z>0\)。
故整个闭面都有正支持、无零位置且为浸入。

径向投影 \(\pi=X/|X|\) 的局部定向面积因子为
\[
 \pi\cdot(\pi_\theta\times\pi_r)
 =\frac{X\cdot(X_\theta\times X_r)}{|X|^3}>0.
 \tag{69.29}
\]
它是紧连通 \(S^2\) 到 \(S^2\) 的局部微分同胚，因此是覆盖；
目标球面单连通，覆盖只有一层。于是 \(\pi\) 全局一一，\(X\) 也
全局一一，得到闭 \(C^2\) 星形嵌入。这个步骤支付了全局双点不交，
不是从局部浸入性直接推出嵌入。

整体直径从原始 cell 的 \(|F|^2\) 上界和新增尾的准确费用得到。
在 graft 上亦可用一个无需角截断的粗界：任一零均值闭角原函数若
\(|F_\theta|=a\)，则
\[
 |F-Ze_z|
 \le\frac1{2\pi}\int_0^{2\pi}
       a\,d_{S^1}(\theta,\phi)\,d\phi=\frac{\pi a}{2}.
 \tag{69.30}
\]
graft 的 \(a\) 递减、\(Z\) 递增，故以真实入口 \(a(3)\) 和真实
末端 \(Z_*\) 控制它。完整尾的高度满足
\[
 Z_{\rm flat}\le Z_*+\frac{a_*^2}{8\omega_*}
                   +\frac5{36}a_T^2+\frac1{16}a_T^2 .
 \tag{69.31}
\]

在上下两个真正平盘各取半径 \(a_{\rm flat}/2\) 的闭子盘，其并为
\(H\)。它闭且内部非空，包含上下两个轴心，故
\[
 \operatorname{diam}X(H)\ge2Z_{\rm flat}\ge2Z_* .
 \tag{69.32}
\]
这是两个平区的并集；不是将半径约 \(10^{-6}\) 的单帽误认为大握持区。
最终合并报告使用全部有向界计算 \(D\le2\sup|F|\) 及
\(\operatorname{diam}X(H)/D\)，并严格检查它大于 \(1/5\)。

实际安全数值是
\[
 Z_{\rm flat}<0.966198670557,\quad
 D<2.557687166,\quad
 \operatorname{diam}X(H)>1.9323973400,\quad
 \frac{\operatorname{diam}X(H)}D>0.75552529>\frac15 .
 \tag{69.32a}
\]
所有值来自同一输入的有向端点。尤其未用旧 PT 主干的直径或支撑界。
新增指数段的高度费用小于 \(3.686\,10^{-12}\)；
connector 和真尾的高度费用分别小于
\(8\,10^{-21292669}\)、\(3.581\,10^{-21292669}\)，虽在普通
binary64 中下溢，仍由 Arb 的准确指数端点保存。

本节证明的是当前闭近似背景的几何尺寸。若在后续线性重建中只知道
每个帽上的场是局部 Killing，仍不能据此断言两帽都固定；
必须保留 R37 的相对刚体/两帽迹条件。一个整体 rotation 只能消去一套
共同刚体数据。本文也没有用主体尚未认证的曲率来宣称全域 reach。

## 7. 保留的完整 PDE 和非线性接口

§2 是同一真实有限正域的全角源/DN；§§3–6 是同一真实对象的完整
外尾与闭背景。它们消除了“有限 \(r=3\) Robin 行等于封口”的旧缺口。
但 R72 外尾的完整非线性两迹及 mean 仍必须与 connector、body 和
核心联立。

在真尾的非零 \(4\mathbb Z\) 模，R15 提供完整内部标签及普通源：
\[
 X=\mathcal Ha+\mathcal Gf,\qquad
 \|X\|_{\mathcal X}\le4\|a\|_{\ell^1}
                       +2^{77}\|N\|_{\mathcal S_1}.
 \tag{69.33}
\]
切口条件是源依赖的仿射两迹条件
\(v_n-g_n(N)\in\Lambda_{|n|}\)，附带实际标签权，不是任意高度的
同宽 DN 图。对物理高度源，按本次 \(\rho\) 准确有
\[
 C^{\rm ref}(\bar a)=C^{\rm phys}(\rho\bar a)/\rho,\quad
 V^{\rm ref}=\rho^3V^{\rm phys},\quad
 F^{\rm ref}=\rho F^{\rm phys},\quad
 N^{\rm ref}=\rho^3N^{\rm phys}.
 \tag{69.34}
\]
这些是两次物理半径微分的结果。R15 的 \(\mathcal S_2\) 点态源门
另付二阶平坦性，不能由径向 \(L^1\) 源范数替代。

非线性修正不会自动只取第四模：必须使用整个内部标签空间，保留
high-mode 输出、mean 与 holonomy 条件。必要的增长/衰减方向分离也
不能由很长的径向段本身推出；若尾输入恰在增长线上，单纯增加长度
不改变该方向。R11 附录 A 的真实双 bump 匹配机制可用于后续支付这项
门，但本篇没有把尚未选择的 bump 计入当前 background 的定义。
若加入它，须同步更新该区域的 metric、完整源与高度费用。

最终公共度量、可见幅度、固定 \(H\) 的完整族和 reach 仍由全局
非线性问题决定。本文没有把 closed approximate background 升级为
主课题已经完成。

## 8. 计算入口与可重放范围

合并源为
[closed exterior source](../scripts/fourfold_phase_closed_approximate_exterior.py)；
它只接受完整的 true finite-cell 报告，重新检查覆盖、参数包含、
源/依赖哈希及全域正角宽。无限尾常数由上面的准确解析构造计算，
不会在某个大 cutoff 截断后忽略余下层。
实际最终报告为
[closed exterior report](../notes/2026-11-12-actual-closed-approximate-exterior.json)。

~~~bash
PYTHONDONTWRITEBYTECODE=1 python scripts/fourfold_phase_closed_approximate_exterior.py \
  --core data/phase_ring_continuation/type_fixed_step02_d5_affine_core_interval.json \
  --collar notes/2026-11-12-positive-family-root-collar.json \
  --body notes/2026-11-12-positive-family-outer-quarter-to-one.json.gz \
         notes/2026-11-12-positive-family-outer-one-to-three.json.gz \
  --graft notes/2026-11-12-positive-family-natural-graft.json \
  --barrier-length 16777216 --bits 256 \
  --out /workspace/scratch/f6a2c7886477/closed-exterior-replay.json
~~~

源码、完整原始 cell 报告、合并报告、数学依赖与本文由 ready manifest
统一登记。展示用 float 可在极小尾尺度下变成0；所有严格判断均使用
Arb 有向端点，绝不使用这种下溢的展示值。
