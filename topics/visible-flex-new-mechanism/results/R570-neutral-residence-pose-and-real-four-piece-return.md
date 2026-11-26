# R570 保八矩的有限姿态词与四段实际 pose 返回

日期：2026-11-26。**已证明。** 接 R567 的同母八矩零与 R568 的双偶 germ；正文经完整端图、实际入口冻结成本、慢图修正及原姿态方程核对。

目标是把当前同一 $\chi$ 的第二/第三返回块推进到真实 scalar、frame、
位置、第二、第三全部返回。第四 characteristic 成本始终保留，最终仍为
$4V_P$，本稿不宣称完整 period 或课题完成。

## 1. 两个较便宜的 pose 条件

取初 frame 为 $I$、初位置为 $0$，$N_0=e_2$，
$D=\operatorname{diag}(-1,1,-1)$。设一个 R568 型半词 $P$ 的末 pose 为
$(G,v)$，$n=GN_0$。其真实反射双词 $Q=PP^R$ 的 pose 是
$$
Q_{\rm pose}=(D_nD,\,(I-D_n)v),\qquad D_n=GDG^{-1}=2nn^t-I.
\tag{1}
$$
第二个刚体半周转 $(D_n,(I-D_n)v)$ 的轴是 $v+\mathbb Rn$，
第一个的轴是 $\mathbb RN_0$。

如果只付两个准确标量条件
$$
\boxed{n\cdot N_0=0,\qquad v\cdot(N_0\times n)=0,}
\tag{2}
$$
这两轴相交且正交。也可不引用几何图像，直接写
$v=aN_0+bn$，则
$$
D_nD=D_{N_0\times n},\quad (I-D_n)v=2aN_0,
\quad D_{N_0\times n}N_0=-N_0.
$$
故
$$
\boxed{Q_{\rm pose}^2=(I,0).}
\tag{3}
$$
$Q$ 已由 R568 真正使 scalar、$A,T$ 返回，因此可以在同一 $\chi$
下正向重复一次。这里的词是 $(PP^R)^2$，不是 R526 中需要额外第三盲核
的 $P^2(P^R)^2$。以下实际支付(2)，不把(3)本身当作存在证明。

## 2. 当前末端水平支并不退化成常 k

继续 R567 的参数盒、$M=(1+\log R)^6$ 和两个
$L_\pm=\ell_\pm\sqrt R$ 回路。取第三高尾末端的真状态。
R563(18)(19)给
$$
j_{\rm high}
=C_W\frac{\ell_1+r_2\ell_2+r_3\ell_3}{\sqrt\xi}
\frac{\sqrt M}{R^2}\{1+o^1(1)\}>0,
\quad H_f\asymp\sqrt M R.
\tag{4}
$$
此时 $\Gamma_0,\Gamma_2=O(M/R^2)$、$\Gamma_1=2c+O(R^{-1})$。
原准确冻结水平系数（只用于比较，真实路径不冻结）为
$$
W_\infty=j-\frac{2q_\Gamma(h)}{h^2}
-2\Gamma_0\int_h^\infty
\frac{dr}{r^4\sqrt{\Gamma_1^2-\Gamma_0\Gamma_2-\Gamma_0^2/r^2}}.
\tag{5}
$$
在 $H_f$，(5)与 $j$ 的差是 $O(\sqrt M/R^3)$，因此
$W_\infty\asymp\sqrt M/R^2>0$。

R564 的各有限下降和两侧桥，在固定 $R$ 后只给最后 $o_\delta^1$。
两个实际长快回路的原 R559(27)(29)给
$$
\Delta j=O(R^{-2}+M/R^{5/2}),\qquad
\Delta\Gamma=O(M/R^3+R^{-5/2})+o_\delta^1(1).
\tag{6}
$$
跨零小带的 $j$、$\Gamma$ 误差更小；由原
$j_\tau=-2dh_\tau/h^3$ 和 R564 的完整带内界，亦可保守界为
$O(R^{-15/4})+o_\delta^1(1)$。
(5)对 $(j,\Gamma,h)$ 的导数在固定低高度紧域有有限统一界。
有限水平过渡在冻结极限准确保(5)，所以全部后继以后仍有
$$
\boxed{W_{\infty,\rm end}\ge c_W\sqrt M/R^2>0}
\tag{7}
$$
于足够大 $R$、随后足够小 $\delta$。
例如 $R^{-2}$ 与(7)的比值为 $O(M^{-1/2})$；
不能仅用原较粗的 $O(g_R)$ 盒证明这个号。

固定一个大有限 $R$，取其小 $\delta$ 极限末 Gram 与水平入值，记为
$(\Gamma^R,j^R)$。在 $H_-$ 周围选一个固定开区间 $J_R$，
使 $h>0,y+\eta>0,hy+d>0,C_k>0$ 且 $B<0$ 有严格余量。
冻结稳定支 $d=q_{\Gamma^R}(h)$ 和原水平式定义唯一的
$k_R(h),\eta_R(h)$。

这条支上的 $k_R$ 不可能在任一开区间恒定。
若 $k_R=K$ 恒定，则水平式迫 $\eta_R=\eta_0$，
$q(h)=h\eta_0-K$。代入原 $\Psi_\Gamma(h,q)=0$ 后，$1/h$ 系数为
$\Gamma_0(1+K^2)/2$，所以 $\Gamma_0=0$；常数项再给
$-\Gamma_1K=0$，故 $K=0$。这时(5)为零，与(7)矛盾。
因此可在同一个负耦合合法区间取两个固定高度 $h_1,h_2$，使
$$
k_1=k_R(h_1)\ne k_R(h_2)=k_2.
\tag{8}
$$
它们的差可以很小，但对已固定的有限 $R$ 严格非零。
后面所有有限词长度和常数允许依赖这一已付差值；不假装对 $R$ 一致。

## 3. 同高度总驻留时长恒定的冻结姿态族

原 frame 方程为
$$
F_s=F\Omega(k),\qquad
\Omega(k)=\begin{pmatrix}0&-k&0\\k&0&1\\0&-1&0\end{pmatrix}.
\tag{9}
$$
其旋转轴向量为 $a(k)=(-1,0,k)$。
(8)使 $\Omega(k_1),\Omega(k_2)$ 及其括号张成 $\mathfrak{so}(3)$。
每个常高度流有周期 $2\pi/\sqrt{1+k_j^2}$，所以负时间可加整周期
改成正时间。由三个非共面共轭轴的三参数端图可得单位元的开邻域；
连通性和有限次邻域相乘遂使这两个真实常高度旋转生成整个 $SO(3)$。
以下还需要一个比普通可控性更精确的构造。

取四个单位向量 $n_1,n_2,n_3,n_4$，使
$n_1-n_4,n_2-n_4,n_3-n_4$ 线性独立，例如正四面体的四个方向。
在先考虑零时长高度跳变的旋转词中，依次访问四个 frame，使同一
$a(k_1)$ 的空间方向分别为 $n_i$，最后回到单位 frame。
由上述两轴生成性，每一段都可取有限正时长词。
每次访问插入 $h_1$ 的一个整旋转周期 $T_1$。

只变这四个驻留时长为
$$
T_1+s_1,\quad T_1+s_2,\quad T_1+s_3,
\quad T_1-s_1-s_2-s_3.
\tag{10}
$$
在小正参数盒内都严格为正。总 $h_1$ 驻留时长准确固定，
$h_2$ 的所有时长也固定。末 frame 的三导数是非零公因子乘
$n_i-n_4$，所以该三维端图在单位元满秩。

现在将全部高度跳变替换为固定的短、光滑、两端平坦的真实高度参考路径，
包括 $H_-\to h_1$ 与末端回到 $H_-$；全部路径留在 $J_R$。
在冻结水平系统里，缩短其固定物理时长使旋转增量接近单位元。
上述三维旋转端图及导数随之接近原简单零。
先用有限维 IFT 校正(10)的中心值，得到一个真正有限时长光滑高度词
$B_s$，其冻结 frame 映射在参数中心准确等于 $I$，且局部微分同胚。
所有切换路径已经固定，不随驻留参数改变。

设其像包含 $SO(3)$ 中一个固定单位元邻域 $U$。
取较小闭邻域 $U_0\Subset U$。由轴角表示，可固定有限 $N_R$，
使每个 $G\in SO(3)$ 都可写成 $N_R$ 个 $U_0$ 元素之积：
把角度至多 $\pi$ 的旋转均分即可。
于是由 $N_R$ 个 $B_s$ 组成的一份固定有限词 $B_\sigma$ 的冻结 frame
映射 $\mathcal G_R(\sigma)$ 覆盖 $SO(3)$。
每个目标都有参数盒内部的正规原像；固定前 $N_R-1$ 个块，
最后一块的三个参数给可逆读出。
紧性给有限个这样的局部截面和统一有限逆界。

### 3.1 整个原八矩成本为何对这些参数准确不变

冻结支上的全部 scalar 和速度为
$$
S_R(h)=(h,k_R(h),\Omega+\eta_R(h)),\quad
(h_s,k_s)=(h_s,k_R'(h)h_s).
$$
原 $M_{\rm raw}=M_0+M_2$ 只读这些 scalar/速度，不读世界 frame。
每个固定平滑过渡的完整 $M_0+M_2$ 积分已固定。
各驻留只有同一 $M_0(h_j)$，而每个高度的总驻留时长由(10)准确固定。
因此整冻结有限词的八矩成本为一个固定向量
$$
\boxed{\int_{B_\sigma}M_{\rm raw}^{\rm frozen}\,ds=C_R^{M},
\qquad D_\sigma C_R^{M}=0.}
\tag{11}
$$
(11)不是把速度平方删掉；短过渡的速度成本可能很大，但有限且与
$\sigma$ 无关。其完整第三费用后面仍按原方程演化。

## 4. 真实有限词：小 A 入口、完整第三与 C1 矩费用

记原 R568 半词的八个真实控制参数为 $u$，包括原 $P_2$ 小停止值。
其八矩共同根为 $u_0(\delta)$。
固定 $R$ 后，原已证明的可逆端图给
$$
J_{R,\delta}:=\delta D_u\mathsf m_P(u_0(\delta))
$$
一致有界且一致可逆；原各 $R,M$ 归一因子都已吸收入这个固定有限矩阵。
在新增有限词前使用实际缩小参数盒
$$
u=u_0(\delta)+\delta\eta,\qquad |\eta|\le C_R.
\tag{12}
$$
于是进入有限词的原未缩放 $A_{\rm in}=\Phi_{\mathsf m_P}$ 有有限统一界。
这里不是在任意 $O(a_R/\delta)$ 原入口直接引用固定有限时长估计。
第三 $T$ 可以保持原 $O(\delta^{-2})$ 大值；其实际缩放 Gram 仍在
原 $\Gamma_1>c$ 的固定合法盒内。

这里先区分实际入口和其 $\delta\to0$ 极限。置
$$
p_{\rm in}(\eta,\delta):=(j_{\rm in},\Gamma_{\rm in}),\qquad
p^R:=(j^R,\Gamma^R).
$$
原全词的缩放 history 和水平累计在固定 $R$ 的原参数盒上满足
$$
\|D_u p_{\rm in}\|\le C_R,\qquad
p_{\rm in}(\eta,\delta)\longrightarrow p^R,
\qquad \|D_\eta p_{\rm in}\|\le C_R\delta.
\tag{12a}
$$
第二式在(12)的有界 $\eta$ 盒上一致，但这里不主张其值有
$O(\delta)$ 收敛率。第一式所需的是原状态估计，而不只是八矩端图：
R567(11)(14)(15)的完整 $BV,C^1$ history 界给
$D_u(\delta A,\delta^2\widetilde T)=O(C_R)$，代入 R544(11)的准确
Gram 多项式即给 $D_u\Gamma=O(C_R)$；水平量则用
$j_s=-2dh_s/h^3$ 在原有限慢时钟、有限快时钟和固定物理桥上逐段积分。
R559 第3–4节、R564 的两侧桥及跨带估计均保这些一阶参数导数，
其末四控的正规逆界和 R568 的末平坦切换也保此界。
有限次复合后得到第一式；链式法则给第三式。
原同一状态的 $C^1$ 极限和 $u_0(\delta)\to u_0^R$ 给第二式。

按 §3 已经固定的高度函数 $h_\sigma(s)$ 解原完整剩余 ODE。
初开区间恒 $H_-$，与 R568 末开 germ 逐函数匹配。
控制为真正预给 $h_{ss}$，不把冻结 scalar 当作真解。

### 4.1 中心化的 R537 修改能量

用 R537 的无 $k_{ss}$ 变量
$$
\widetilde T=T-P_{\rm acc}+\mathcal A h_s k_s,
\qquad \bar T=\delta^2\widetilde T.
$$
在最大存在的固定几何盒内，原方程先给
$$
A_s=\Phi_{M_0+M_2},\qquad
\bar T_s=-\delta^2\Phi_M\circ A+\delta^2\mathcal C_{\rm slow},
\tag{13}
$$
$\mathcal C_{\rm slow}$ 不含 $k_{ss}$。
若速度在固定盒内，则 $A$ 在固定物理时长内有有限界，
$\bar T_s=O(C_R\delta^2)$。
因 $\bar A=\delta A$，有效 $\Gamma_s$ 同样为 $O(C_R\delta^2)$。

中心化为 $e=d-q_\Gamma(h)$。
把真实 $\Gamma_s$ 一并代入后，隐式速度和质量系数为 $1+O(C_R\delta^2)$；
原正频率为 $\Psi_{\Gamma,d}/(2C_k)>0$。
原 $A$ 的速度线性系数现在只有固定有限界。
因此恰按 R537(23)–(30)，以实际慢变量
$(j,A,\bar T)$ 构造
$$
\mathscr E=\tfrac12 e_s^2+\delta^{-2}V(s,e)
-f(s,j,A,\bar T)e+C_R\delta^2,
\quad V\asymp e^2.
\tag{14}
$$
$f$ 使用 $e=e_s=0$ 的原剩余项，沿慢状态的导数不含未控制加速度。
初端 $e=0$、$d_s=0$，而 $q_{\Gamma,s}=O(C_R\delta^2)$，
所以 $\mathscr E(0)=O(C_R\delta^2)$。
完整速度线性/二次项用同一 Young 估计得到
$\mathscr E_s\le C_R\mathscr E$。
固定物理时长以后
$$
\boxed{|e|\le C_R\delta^2,\qquad |e_s|\le C_R\delta.}
\tag{15}
$$
这改进最大盒并给真实全段延拓；随后原式给 $k_{ss}=O(C_R)$。
原势、$-M\circ A$、面积和全部三次速度没有重置或删除。

参数一阶变分的正能量允许较弱而足够的界
$$
|D_\sigma e|\le C_R\delta,
\qquad |D_\sigma e_s|\le C_R.
\tag{16}
$$
理由是变分方程中 $\delta^{-2}\alpha_\sigma e=O(C_R)$，
其余变分与有限时长慢状态一起作普通 Gronwall；正能量仍不给
$e^{C_R/\delta}$。不把(15)未经证明地逐参数微分成相同阶数。

### 4.2 全八矩的 C1 精度

对于每个实际 $(\eta,\delta)$，以它自己的 $p_{\rm in}$ 冻结比较轨道：
$$
d^{\rm fr}(h)=q_{\Gamma_{\rm in}}(h),\qquad
j^{\rm fr}(h)=j_{\rm in}-2\int_{H_-}^{h}
 q_{\Gamma_{\rm in}}(r)r^{-3}\,dr,
\qquad k^{\rm fr}=h^2j^{\rm fr}-2d^{\rm fr}.
\tag{16a}
$$
同一高度的总驻留时长仍准确固定，全部平滑高度过渡也仍是同一份，
所以(11)对每个这样的冻结入口分别成立。把其成本记作
$$
C_{R,\delta}^{M}(\eta)
 :=\mathcal C_R^{M}(p_{\rm in}(\eta,\delta)),\qquad
\partial_\sigma C_{R,\delta}^{M}=0.
\tag{16b}
$$
有限词上的光滑常规积分与(12a)给
$$
C_{R,\delta}^{M}(\eta)\to C_R^{M},\qquad
\|D_\eta C_{R,\delta}^{M}\|\le C_R\delta.
\tag{16c}
$$
这一步只要收敛和 $\eta$ 导数小，不需要实际入口到 $p^R$ 的
$O(\delta)$ 值误差。

实际 $\Gamma$ 相对入值变 $O(C_R\delta^2)$，
原水平式 $j_s=-2dh_s/h^3$ 与(15)使真实 scalar 相对冻结水平轨道
相差 $O(C_R\delta^2)$；其参数导数差为 $O(C_R\delta)$。
这里的冻结轨道是(16a)，参数导数包括 $\sigma,\eta$；
对 $\eta$ 变分使用(12a)，且未缩放入口 $A$ 的 $\eta$ 导数有界，
故同一有限时长正能量估计适用。

原 $M_0$ 的积分因此在值为 $O(C_R\delta^2)$、一导为 $O(C_R\delta)$。
对完整 $M_2$，把速度写成冻结速度加 $e_s$ 与已控余项。
线性交叉具有 $L(s)e_s$ 的形式。$L$ 的主系数和固定高度路径导数有界，
一次真实分部积分给
$$
\int L e_s=[Le]-\int L_s e.
\tag{17}
$$
末初高度开区间平坦，主要边项亦为零；即使保全部实际边项，
(15)(16)也给值 $O(C_R\delta^2)$、一导 $O(C_R\delta)$。
二次余项 $\int e_s^2$ 由(15)(16)给同样的值/一导阶。
因此
$$
\boxed{\int_{B_\sigma}M_{\rm raw}\,ds
=C_{R,\delta}^{M}(\eta)+O_{C^1_{\sigma,\eta}}(C_R\delta).}
\tag{18}
$$
这里正是需要的完整 $C^1$ 积分估计，不能只用真实速度的逐点小量。

末端仍留固定快窗，以原四加速度内控支付
$h=H_-,h_\tau=0,d=q_{\Gamma_{\rm out}}(H_-),d_\tau=0$，
最后开区间真正 $h_{\tau\tau}=0$。
由(15)，端残差在快状态是 $O(\delta^2)$，一导是 $O(\delta)$。
真实四控 Jacobian 在 $\beta_-\ne0$ 下保持可逆。
短控矩速度费用的值为 $O(\delta^3)$、一导 $O(\delta^2)$，
其它静态及第三费用也在(18)的余项内。
故 §3 的全有限词在实际系统里存在，并保真正末偶 germ 接口。

## 5. 同一个实际八矩纤维中的 frame 覆盖

把原半词和整个有限后继（含末四控）共同读入八矩图。
在(12)中，该图为
$$
\mathsf m_{\rm total}
=J_{R,\delta}\eta+C_{R,\delta}^{M}(\eta)+o_{C^1_\eta}(1)
+O_{C^1_{\sigma,\eta}}(C_R\delta).
\tag{19}
$$
固定 $R$ 后，原八矩端图的 $C^1$ 收敛和统一可逆性支付
$(u-u_0)/\delta$ 有界的 Taylor 重写。
矩阵费用 $C_{R,\delta}^{M}(0)$ 虽可能很大，但有固定有限界；
取一个包含全部 $-J_{R,\delta}^{-1}C_{R,\delta}^{M}(0)$
且留余量的固定有限 $\eta$ 盒即可。(16c)保证其 $\eta$ 导数趋零，
所以它不破坏原统一可逆的 $\eta$ Jacobian。
最后小 $\delta$ 使对应 $u$ 仍处原正参数盒内部。

真实八维 IFT 因此给
$$
u=u(\sigma,\delta),\quad \mathsf m_{\rm total}=0,
\qquad
\boxed{D_\sigma u=O(C_R\delta^2).}
\tag{20}
$$
最后一式来自准确微分(19)：$\partial_\sigma C_{R,\delta}^M=0$，
余项一导 $O(C_R\delta)$，再乘(12)外面的 $\delta$。
不需要把原七/八矩根的下一项凭空设为零。

原 frame 方程是正交流。在整个原长半词上，参数变分满足
$$
\|D_uG_P\|\le C_R/\delta,
\qquad \|D_uv_P\|\le C_R/\delta^2.
\tag{21}
$$
第一式由 $\int|D_uk|ds$，第二式由原
$\alpha_s=h^2Fe_1$ 及第一式积分得到。
所有实际段用其原慢/快时钟参数化，停止时间的导数也在其中。
不存在 frame 的指数增长，因为其齐次流正交。

由(20)(21)，八矩重解对随姿态参数变化的 frame 只给 $O(C_R\delta)$，
对位置给固定 $O(C_R)$；这两个阶不能混写。
取参数族内一个固定参考点 $\sigma_*$，令
$p_\delta^*=p_{\rm in}(\eta(\sigma_*,\delta),\delta)$。
由(12a)(20)，整个有限参数族上的实际入口与 $p_\delta^*$
相差 $O_{C^1_\sigma}(C_R\delta^2)$。
记 $\mathcal G_{R,\delta}(\sigma)$ 为以这个共同实际入口
$p_\delta^*$ 冻结的 §3 有限词 frame 图。
与 §4 实际有限词的估计合并，完整末 frame 在八矩纤维内为
$$
G(\sigma,\delta)=G_{R,\delta}^{\rm base}\,
\mathcal G_{R,\delta}(\sigma)+O_{C^1}(C_R\delta),
\qquad \mathcal G_{R,\delta}\longrightarrow\mathcal G_R
\quad\hbox{in }C^1.
\tag{22}
$$
$G_{R,\delta}^{\rm base}$ 可以快速依赖 $\delta$，但它属于紧群 $SO(3)$。
最后一个收敛只主张 $o(1)$，不强行给 $O(\delta)$ 率。
§3 给每个目标的正规原像及统一有限局部逆界，且这些性质对
$C^1$ 小扰动稳定，故充分小 $\delta$ 后，
实际(22)也覆盖整个 $SO(3)$，并在每个目标附近有真正的局部光滑截面。
这时全部八矩仍准确为零，末端仍用实际 $\Gamma$ 和原四控。

在任意一个这样的局部截面上，完整位置满足
$$
\boxed{|D_\sigma v|\le C_R.}
\tag{23}
$$
这是(20)(21)和末有限段的原位置 ODE 一起给出的界，
不把巨大原位移误叫成有限小量。

## 6. 原首高尾的巨大横向位移

为了用(23)真正支付第二个条件，需要位移有一个不会随末姿态截面消失的
大横向分量。这个量来自原共同首高尾，不需新增自由平移原子。

### 6.1 初次有限上升可使空间轴避开初 N 轴

原 R544 快准备只耗 $O(\delta)$ 物理时间，frame 增量趋零。
接下来的真实高度上升 $H\to R$ 可在固定 $R$ 后选一个很短但有限的
平滑物理时长；冻结水平曲线上 $k$ 有有限上界。
取该时长使 $\int\sqrt{1+k^2}\,ds<\varepsilon_F$。
R544 的原补偿反馈仍实现它；其可能很大的高度导数和矩费用都是
固定 $R$ 后有限 $C_R$，最后 $\delta$ 一起支付。
水平末 $k$、$j$ 的冻结值只依赖高度路径的端点，不依赖这个时长。
因此原 $K_*<-4$ 和后面全部矩端图保持。

由原(9)，进入首高尾的 frame $F_a$ 满足
$\|F_a-I\|\le C\varepsilon_F+o_\delta(1)$。
该处旋转轴
$$
n_a=F_a\frac{(-1,0,k_a)}{\sqrt{1+k_a^2}}
$$
在 $\varepsilon_F$ 足够小时满足
$$
\|\Pi_{N_0^\perp}n_a\|\ge 3/4.
\tag{24}
$$
这里改的是原有限高度控制，不是初 frame 的坐标重命名。

### 6.2 对原慢首尾的逐段导数精度

首高尾参考高度恒为 $R$，其历史时钟为
$\tau=\delta R^{3/2}s$，总 $\tau$ 长度为 $O(1+\log R)$ 且包含
R550 的固定 $L\log R$ 饱和等待。
对下面仅在固定有限 $R$ 后取 $\delta\to0$ 的几何估计，可将原实际
$k$ 写成
$$
k(s)=K_{R,\delta}(\delta R^{3/2}s)+r_\delta(s),
\quad \|K_{R,\delta}\|_{C^2}\le C_R,
\quad \int|r_\delta|ds\le C_R\delta,
\tag{25}
$$
且 $h=R+O(C_R\delta)$。
这里需要说明(25)比只有 $k_s=O(\delta)$ 强，不能直接后者乘长时间。

(25)由 R544(35)–(40)的真实耗散系统作一次慢图修正取得。
具体令 $x=(h-R)/\delta$、$z_n=(R_n,w_n)/\delta$；
已付能量给它们有界。为避免把高度松弛层误算成慢 $j$ 的初值跳跃，
先使用原水平分部积分坐标
$$
\jmath=j+2\int_R^h q_\Gamma(r)r^{-3}\,dr.
$$
其准确导数是
$$
\jmath_s=-2(d-q_\Gamma(h))h_s/h^3
+2\left(\int_R^h q_{\Gamma,\Gamma}(r)r^{-3}\,dr\right)\Gamma_s.
$$
因此这里 $\jmath_s=O(C_R\delta^2)$。
以 $V=(\jmath,\bar A,\bar T)$ 为慢状态。
恒参考区间没有外加时间振荡；由原完整方程和非零质量，Taylor 展开为
$$
\begin{aligned}
\delta(z_n)_s&=A_n(V)z_n+f_0(V)
+\delta f_1(V,x,z_n)+O(C_R\delta^2),\\
x_s&=-\kappa_hx+\kappa(z_n)_1,\\
V_s&=\delta F_0(V)+\delta^2F_1(V,x,z_n)+O(C_R\delta^3).
\end{aligned}
\tag{25a}
$$
所有系数及所需有限导数在固定 $R$ 的盒内有界；$A_n$ 是原稳定法向块。
$F_0$ 不依赖 $x,z_n$：原零速 $M_0$ 在 $h=R,d=q_\Gamma(R)$ 评价，
速度平方从 $\delta^2$ 起；$\jmath$ 的首导数为零。
这给(25a)的次序，不是另假一个任意慢系统。

先取 $z_0=-A_n^{-1}f_0$、$x_0=\kappa(z_0)_1/\kappa_h$；
再取 $z_1=-A_n^{-1}f_1(V,x_0,z_0)$ 和
$x_1=\{\kappa(z_1)_1-Dx_0F_0\}/\kappa_h$。
代回(25a)，法向和高度图的残余均为 $O(C_R\delta^2)$。
用原耗散卷积及高度 $e^{-\kappa_h(s-t)}$ 卷积，
$x-(x_0+\delta x_1)$、$z_n-(z_0+\delta z_1)$ 为
$O(C_R\delta^2)$ 加固定物理/快时钟上的指数衰减层。
慢比较状态解
$$
(V_c)_s=\delta F_0(V_c)
+\delta^2F_1(V_c,x_0(V_c),z_0(V_c)).
$$
慢方程的剩余项是 $O(C_R\delta^3)$；初始层乘 $\delta^2$ 后的
总积分为 $O(C_R\delta^2)$。在有限 $\tau$ 区间用慢 Gronwall，
$V-V_c=O(C_R\delta^2)$。
所以从该比较图恢复 $k$ 时，真正几何余量为
$O(C_R\delta^2)+O(C_R\delta e^{-c_Rs})$ 加更短快层，
在 $O(C_R/\delta)$ 物理时长上的 $L^1$ 范数正是 $O(C_R\delta)$。
在比较图上定义 $K_{R,\delta}$，其前两阶慢导数由上述光滑有限慢 ODE
有界，得到(25)。这一步没有将原耗散盒的 $O(\delta)$ 余项未经修正升级。

原早期恒高长段可同样归入这一恒 $R$ 区间；若保分段记号，有限个接点
的衰减层仍给同一个 $L^1$ 界。

### 6.3 原位置 ODE 的直接积分

先用(25)的慢比较曲率恢复 frame。正交流的 Duhamel 估计使真实 frame
与比较 frame 相差 $O(C_R\delta)$；对整个首高尾位置的影响为 $O(C_R)$。
所以只需计算比较曲率 $K=K_{R,\delta}(\tau)$。

写 $n(s)=F(s)(-1,0,K)/\sqrt{1+K^2}$。
由原 $N_s=-KT-B$ 准确有
$$
n_s=-\frac{K_s}{(1+K^2)^{3/2}}N_s.
$$
一次分部积分，利用 $K_s=O(C_R\delta)$、
$\int |(K_s/(1+K^2)^{3/2})_s|ds=O(C_R\delta)$，得到
$$
n(s)=n_a+O(C_R\delta).
\tag{26}
$$
另一个准确身份是
$$
T=-\frac{n}{\sqrt{1+K^2}}-\frac{K}{1+K^2}N_s.
\tag{27}
$$
代入原 $\alpha_s=h^2T$，以真实 $h=R+O(C_R\delta)$ 及一次分部积分，
得到整个共同首高尾的实际位移
$$
\boxed{v_{\rm first}=-\Lambda_{R,\delta}n_a+O(C_R),}
\tag{28}
$$
$$
\Lambda_{R,\delta}
=\frac{\sqrt R}{\delta}
\int\frac{d\tau}{\sqrt{1+K_{R,\delta}(\tau)^2}}
\ge c\frac{\sqrt R\log R}{\delta}>0.
\tag{29}
$$
分部积分的边项至多 $C_R$，$h^2-R^2=O(C_R\delta)$ 的实际时间费用
也至多 $C_R$。$K$ 的有界盒来自 R550；未用一个可能改变号的
形式“平均位移”代替(27)。

### 6.4 其余全词不能盖掉这个横向分量

不必对后三高尾作额外旋转平均。原位置速度就是 $h^2$，故用真实时长
直接给
$$
\left|v_{\rm later,high}\right|
\le C\frac{\sqrt R}{\delta M},\qquad
\left|v_{\rm low}\right|
\le C\frac{M^2}{\delta R^{3/2}}.
\tag{30}
$$
其余有限桥和 §3 有限姿态词的位移为固定 $C_R$；
原快准备、跨带和两个长快回路按实际 $O(\delta)$、$O(\delta\sqrt R)$
时间计入，均不改变(29)的主尺度。
上述共同首高尾不依赖后面八个控制参数，(30)则在整个原参数盒统一。

先取 $R$ 大，使(30)与(29)之比足够小，再最后取 $\delta$ 小。
由(24)(28)，在新增有限姿态族和八矩重解以后仍有
$$
\boxed{\|\Pi_{N_0^\perp}v\|\ge c_R/\delta>0.}
\tag{31}
$$
对不同姿态参数，位置变化的一阶界却只有(23)的 $C_R$。
二者相容：原位置本身巨大，其沿这个精确八矩纤维的变化有限。

## 7. 实际支付两条 pose 方程

取一个固定参考姿态参数点，记其完整位置为 $v_b$。
由(31)，$v_b$ 的横向分量非零。
在初 $N_0^\perp$ 平面选正交基 $e_a,e_b$，令
$$
n(\alpha)=\cos\alpha\,e_a+\sin\alpha\,e_b.
$$
选 $\alpha_b$ 使 $n(\alpha_b)$ 平行于 $\Pi_{N_0^\perp}v_b$。
构造一个局部光滑目标 frame $G_*(\alpha)$，使
$G_*(\alpha)N_0=n(\alpha)$。

由 §5 的实际覆盖及统一正规截面，可在
$|\alpha-\alpha_b|\le\varepsilon_R$ 的固定小区间内，
在同一准确八矩纤维上实现
$$
G(\alpha)=G_*(\alpha).
\tag{32}
$$
所用截面可以随 $G_{R,\delta}^{\rm base}$ 选择有限个候选之一；
参数始终在预先固定的共同正盒内，$\chi$ 不变。
由(23)，相应完整位置满足
$$
v(\alpha)=v_b+O(C_R),\qquad |v'(\alpha)|\le C_R.
\tag{33}
$$
参考 $v_b$ 可来自另一固定截面；各参数点之间由紧盒上的有限路径相连，
同一个 $O(C_R)$ 界仍成立。

第一条(2)已经由(32)准确支付。
对第二条定义真实连续函数
$$
f(\alpha)=v(\alpha)\cdot(N_0\times n(\alpha)).
\tag{34}
$$
(31)(33)给
$$
f(\alpha)
=\|\Pi_{N_0^\perp}v_b\|\sin(\alpha_b-\alpha)+O(C_R).
$$
在 $\alpha_b\pm\varepsilon_R$ 两端，这两个值在最后小 $\delta$ 后异号。
故存在实际 $\alpha_*$ 使 $f(\alpha_*)=0$。
还可由(33)读出局部导数的主项大小为 $c_R/\delta$，
所以这确是稳定零，不是一个未付误差的形式方向。
在这一参数点，全部八矩、末四端控、完整 ruling 与(2)同时准确成立。

## 8. 四段真实返回及保留的第四成本

令 $P$ 是 §7 得到的同规范实际半词。
它从原零 history 起点开始、末端全八矩零、两端有 R568 的真实偶 germs。
因此 $Q=PP^R$ 是原真实正长度反射词，沿途同一 $\chi$、全相位 ruling
恒为零，并准确返回 scalar、$A,T$。
其 pose 由 §7 满足(3)，于是再重复同一个真实 $Q$，得到
$$
\boxed{\mathcal W=(PP^R)^2.}
$$
整个词的原 scalar 全 jets、frame、位置、全第二矩阵和完整第三算子
在终点全部返回初值。
第二次 $Q$ 的真实入口 $A=T=0$，因此不是偷换一次新的规范或记账锚。
外 collar、seed、原 profile 和所有内部合法窗口都按 R526 保持。

原完整第四 characteristic 仍满足
$$
\boxed{V_{\mathcal W}(x,\theta)=4V_P(x,\theta).}
\tag{35}
$$
这整个函数尚未证明为零，同十三规范也未由本稿自动支付。
闭 pose 并不自动给嵌入、所需 reach、持握幅度或有限等距族。
下一必须继续原完整第四 period；本稿不把(35)的未付函数移出任务范围。

### 直接来源

- R521、R537、R544：原全 history 控制、无加速度第三变量与能量；
- R550、R552、R563：首高尾与低/高尾真实尺度、水平输运及原时钟；
- R559、R564：末两个实际回路、跨带、$j/\Gamma$ 真实费用；
- R567：八矩联合零与共同有限参数盒；
- R568、R526：真正偶 germs、同规范 $PP^R$ 与完整 pose/第四公式。
