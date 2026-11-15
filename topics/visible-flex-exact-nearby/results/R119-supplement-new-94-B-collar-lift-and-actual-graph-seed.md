# R119 续篇：新94成员的真实 B 端 collar 修补与窄源 graph 初入口

2026-11-15，visible-exact / tail_connector。

**解析结论，已完成全文及单侧 jets、物理单位、三径源的独立核对。** 本篇只消费已经重实例化于同一 fixed-stop
对象的新94步链，不消费旧重停对象的第94标签。对其真正的非mean斜率
差，在准确指定的正型 collar 内作单侧五 jet Hermite 修补。所得
非mean高度属于原参考 graph，具有真实 holonomy mean，且在 B
具有 cap--long 的完整高度/斜率数据。所有新增 ordinary 源及前三
径向导数均由原同单位图范数计入。

这给一个可核的 body Nash 种子。未知帽内匹配、真实外行更新的
onto Schur、独立 frame/height/flux/ν 行仍是 augmented 问题；
没有把一个初始斜率已经对齐的图自动称为完整 BVP 的解。

## 1. 固定输入及当前几何身份

使用：

- [新94步](R119-supplement-new-fixed-stop-small-width-cap-and-full-94-step-chain.md)，记为 P；
- [固定参考 graph](R119-supplement-reference-graph-scale-exact-residual-and-angular-smoothing.md)，记为 E；
- [finite Nash](R119-supplement-finite-Nash-iteration-in-reference-graph-with-port-conditions.md)，记为 B；
- [真实 long](R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md)，记为 D；
- [新候选对象](../notes/2026-11-14-R119-simple-root-fixed-stop-new-object-and-transfer-gates.md)，记为 S。

B 使用已经发布的3500/400归纳版本，正文 SHA256 为
7ad04c3b8c1573ae9c5ddd0853efc421779a56aff99d676e879306746a775736。
其 source 损失1734、背景窗口1796不变。

几何 Nash 入口固定实偶的实际帽输入 $\gamma$；以下在其已付复化
中作完整估计，唯一性保证最终标签为实。取 P 的真实标签，令
$$
 a^\dagger=a_{94},\quad
 R_a=2^{-55000000},\quad
 \|a^\dagger\|_{66624}<R_a/4,\quad
 \sigma=s_{66624}=66624-\frac{88823}{400}.
 \tag{G.1}
$$
真实 tail/connector 在 B 的归一非mean迹记为 $f,k$。
同一个实际帽给 $f_*=\Phi_\gamma(f)$，同一个 long 给
$K_{\rm L}=K_{B,\perp}(f,f_*)$。于是
$$
 g=k-K_{\rm L},\qquad
 r_{94}:=\|g\|_{\dot A^1_\sigma}<2^{-5280041760}.
 \tag{G.2}
$$
$f,k,K_{\rm L},g$ 全部为共同反射复偶数据，所有正负模均保留。
它们的实际 physical 角相同；不把 moving 角 Fourier 系数直接
放入此式。

冻结 $\gamma_2^\flat=\gamma_2^*(a^\dagger)$。
以这个第二参数的真实径向基点建立 E 的固定参考 $w_0$；
第一参数继续采用 E/L 的同一个 principal 值图。
P 末节与 L 唯一性将原 $\gamma_1^*(a^\dagger)$ 识别为该值图在
当前成员上的值。没有用另一个 $\Gamma^0$ 的 profile 替换它。

记该真尾加有限 connector 的非mean正高度为 $u^\dagger$。
它在每片满足完整 Darboux 方程，原内部线性 traces 已真实匹配，
唯一尚未在本步对齐的行是 B 的 (G.2)。E 的已证成员估计给
$$
 \mathcal X\le16\|a^\dagger\|_{224}\le4R_a,\qquad
 \|u^\dagger\|_{E_{8192}}
          \le2^{133001}\mathcal X
          <2^{-54866997}.
 \tag{G.3}
$$
E 的同一公式仅在 tail/connector 的实际定义域使用；
它不把 B 的剩余外迹偷偷设为0。后面将显式修补这条外迹。

## 2. 一个准确存在的正 collar

在 B 令 $t=\log(a/a_B)$，所以 long 在 $t\ge0$；
向有限 connector 内走用
$$
                        v=-t=\log(a_B/a)\ge0.
 \tag{G.4}
$$
原 R69 (69.14)--(69.16) 的真实首段、以及 S 明确保留的准备段，
准确为
$$
 q_{\rm con}(v)=-S(v/\eta),\quad
 S(x)=10x^3-15x^4+6x^5,\quad \eta=2^{-24}.
 \tag{G.5}
$$
它由 $q_{\rm con}=0$ 过渡到 $-1$，不与 S 新增的末端
$2\to-8$ 过渡混同。D.2 的 $w=a/(4\omega)$ 在此继续成立，
$A=(\log w)_t=q_{\rm con}+1$，故负型量
$$
 Q=-A=S(v/\eta)-1.
 \tag{G.6}
$$
选定
$$
                     d=\ell_o=2^{-1024},\qquad 0\le v\le d .
 \tag{G.7}
$$
因为 $d/\eta=2^{-1000}<1/4$ 且 $S(1/4)<1/4$，该整个 collar
满足 $Q<-3/4$。它严格处于真实正型区，离所有 negative 分量、
根、第一和第二 Γ bump 及第129胞外行的支集均有正距离。
这不是以一个任意新短段代替原几何。

在这个 collar，所有 profile/固定 stop/物理安装都保持原值。
principal 返回的实际输入只使用相应负分量及其根邻域；
本篇的修补在那里逐点为0。更准确地，L.10 的两个真实流在每个
候选第一参数值上只读取同一负分量的状态与 metric；这整个参数族
都在本 collar 保持原 profile，且在所有 L.10 输入点上两场逐点相同。
故完整 fixed-point 映射在修补前后相同，再由 L.14--15 的值图唯一性，
第一参数值准确相同。这不只是一条在中心的 $D\Gamma$ 导数消失结论。
第二参数按 (G.1) 已固定；不在修补后重新选择另一度量。

## 3. 物理高度单位和需要匹配的 Cauchy 数据

D.2--D.6 与 P.27 给
$$
 u^\dagger(0,\theta)=a_Bw_B f,\qquad
 u^\dagger_t(0,\theta)=a_Bw_B k .
 \tag{G.8}
$$
这里 $u$ 是 Darboux 的正高度非mean部分。北帽实际空间高度为
$Z_0-u$，故其物理 derivative 差带负号；
这个几何符号不改变以下正高度方程。

目标 Cauchy pair 是
$$
 u^*(0,\theta)=a_Bw_B f,\qquad
 u^*_t(0,\theta)=a_Bw_BK_{\rm L}.
 \tag{G.9}
$$
因此
$$
 \Delta J_0=0,\qquad
 \Delta J_1=-a_Bw_Bg .
 \tag{G.10}
$$
不能将 $g$ 直接当作裸高度 derivative，亦不能把 $a_Bw_B$
的极小量先除掉再在别处不明收费。

所有高于一阶的目标 jets 按同一 connector 一侧 PDE生成。
具体记
$$
 Y=(P,K_\perp,U,V),\quad
 P=\frac{u_\theta}{aw},\quad K_\perp=\frac{u_t}{aw},\quad
 U=P_\theta,\quad V=(K_\perp)_\theta .
$$
$K=K_\perp+\kappa(q_{\rm phys};P,K_\perp,U)$ 含原 holonomy 小根；
这里显式列出其真实 $U=P_\theta$ 输入，不把它当成无角导的代用根，
$q_{\rm phys}=w^2$。原完整方程准确给
$$
 P_t=V+(Q-1)P,\quad
 (K_\perp)_t=P_\perp F_Q(P,K,U,V),
$$
$$
 U_t=V_\theta+(Q-1)U,\quad
 V_t=\partial_\theta P_\perp F_Q(P,K,U,V).
 \tag{G.11}
$$
$F_Q$ 是 E.15 的完整商式，不删 $K_0$、mean反馈或任何
primitive产生的规范项。对 (G.9) 用 (G.11) 求得
$J_j^*=(\partial_t^ju^*)_{0^-}$，$0\le j\le5$；
对 (G.8) 用同式得到原真正的 $J_j^\dagger$，置
$$
                    \Delta J_j=J_j^*-J_j^\dagger .
 \tag{G.12}
$$
这只是有限、准确的单侧 jet递推，不要求在正区求一个粗 Sobolev
Cauchy解。原标签/long给的角解析域足够完成这五步。

## 4. 单侧 jet 差的明确有限费用

为给 (G.12) 一个可审核的宽界，使用第一片的准确 polynomial germ。
它在 $|t|<2^{-128}$ 上满足
$$
 |Q|<2,\quad |q_{\rm phys}|<1/2,\quad
 \left|\frac{a(t)w(t)}{a_Bw_B}\right|,
 \left|\frac{a_Bw_B}{a(t)w(t)}\right|<2.
 \tag{G.13}
$$
例如 $|t|/\eta<2^{-104}$，将 (G.5) 的五个准确幂项直接代入；
$\log(aw/(a_Bw_B))$ 的 derivative 是 $A+1$，
其绝对值在这个盘小于4。此复盘只是同一第一片 germ的有限
jet工具；没有把 actual piecewise profile 跨 B 宣称为解析。

Cauchy给所列 profile 普通 jets到五阶的统一宽界 $2^{650}$。
原 holonomy分支在四态总和 $<2^{-10}$ 的全复 Banach代数球上，
$D,J$ 均有严格逆级数。完整小根和商式在该球上的值可宽取
$2^{10}$；在起始四态周围半径 $2^{-11}$ 的状态圆盘上，
Cauchy加复极化给至五阶状态偏导
$q^q2^{11q+10}<2^{80}$（$1\le q\le5$）。
这是对整个小根/商式的导数界，不用只有有限项的展开替换分母。

由 P.3，(G.8)--(G.9) 的起始四态远小于 $2^{-100}$。
从 (G.11) 进行至多四次微分，再用 $u_t=awK_\perp$，
每个 resulting monomial 至多含五个 profile/小根偏导因子；
一次角导在连续留出的单位角宽上以 $A^0$ Cauchy 收费。
每步至多五阶 Leibniz分拆和六个 state/profile选择，
其 branch数小于 $2^{10}$；至多五步连同最后读出，可将全部
普通 Leibniz/Faà组合数宽取 $2^{64}$。
各阶原四态 jets 仍小于 $2^{-10}$，因为
$2^{4096}(2^{-443}\|a^\dagger\|_{66624}+r_{94})<2^{-100}$；
因此同一个正分支与导数盘逐次有效。
对两组数据之差保留恰好一个 difference因子。完整预算可取
$5(650+80+10)+64<4096$，从而
$$
 \max_{1\le j\le5}
 \left\|\frac{\Delta J_j}{a_Bw_B}\right\|_{A^0_{\sigma-16}}
                  <2^{4096}r_{94}.
 \tag{G.14}
$$
这里留出的16角宽包括四次 (G.11)、起始 $V$ 行及最后
两个角 derivative 的缓冲。只用有限阶真实导数，不用未知高频截断。

(G.14) 也解释为何只调整一阶 slope 后立刻宣称所有径向源门成立
是不充分的：二至五阶必须由同一个包含 mean 的方程求出。

## 5. 精确五 jet Hermite lift

令 $s=v/d$，对 $1\le j\le5$ 定义
$$
 H_j(s)=s^j(1-s)^6
             \sum_{\ell=0}^{5-j}\binom{5+\ell}{\ell}s^\ell .
 \tag{G.15}
$$
准确有 $H_j(s)=s^j+O(s^6)$，且在 $s=1$ 有六阶零。
在 collar 上定义
$$
 \ell_B(t,\theta)
       =\sum_{j=1}^5\frac{(-d)^j}{j!}\Delta J_j(\theta)H_j(-t/d),
 \qquad
 \ell_B=0\quad(t\le-d).
 \tag{G.16}
$$
因此
$$
 \partial_t^k\ell_B(0^-)=\Delta J_k\ (0\le k\le5),\qquad
 \partial_t^k\ell_B(-d^+)=0\ (0\le k\le5).
 \tag{G.17}
$$
原内部端 $t=-d$ 没有新增状态跳或分布 source原子。
$\ell_B$ 的普通角 mean准确为0，复偶性保持。
这里的字母 $\ell_B$ 表示 height lift，区别原径向尺度 $\ell_o=d$。

置
$$
                         \widetilde u=u^\dagger+\ell_B .
 \tag{G.18}
$$
它在 B 与 (G.9) 的完整 connector单侧 jets到五阶准确相符。
$Q$ 在 B 与 long 的常 $Q=-1$ 的0、1、2阶 jets相同；
第三 jet一般有真跳。因此正高度两侧的 jets到四阶相同，
第五阶使用真实的一侧 PDE，不抹掉该已知 coefficient跳。
这足以保实际所需 $C^2$ matching；更高阶始终按原 broken口径。

由于 (G.12) 正是 PDE递推，其普通非mean residual及前三单侧
$t$ derivatives在 B准确为0。完整 holonomy恒等式 (G.25) 再给
$\widetilde u$ 的全 residual及这三个 derivatives亦准确为0；不是
只检非mean行。此处不以一个点的 residual
上界代替 collar中的完整源预算。

## 6. 同一 graph 单位中的实际 lift 界

在 $0\le s\le1$，
$$
 R(s):=\frac{a_Bw_B}{a(-ds)w(-ds)}
 =\exp\!\left(2ds-\eta\int_0^{ds/\eta}S(x)\,dx\right).
 \tag{G.19}
$$
对于 $|s|\le2$，其绝对值小于2，故
$|\partial_s^aR|<2a!<2^8$，$0\le a\le5$。
同理 $Q(-ds)$ 的 scaled jets有相同宽界。
而 (G.15) 的 coefficient绝对和小于 $2^{15}$，
五阶 derivative再乘的整数小于 $2^{16}$。
连同五项和、全部 Leibniz配对及两个 state分量，统一用 $2^{64}$。

E 的 scaled ordinary derivatives恰为
$d^a\partial_t^a=(-1)^a\partial_s^a$。
在 $P,U$ 行保一个额外的 $d$，在 $K,V$ 行不丢任何 $d^{-1}$：
$$
 P(\ell_B)=R\sum_{j=1}^5\frac{(-d)^j}{j!}
                 \partial_\theta\!\left(\frac{\Delta J_j}{a_Bw_B}\right)H_j,
$$
$$
 K_\perp(\ell_B)=-R\sum_{j=1}^5\frac{(-d)^j}{d\,j!}
                 \frac{\Delta J_j}{a_Bw_B}H_j'.
 \tag{G.20}
$$
$U,V$ 再取准确一角导。由于 $d^{j-1}\le1$，
四径 state费用至多 $2^{4096+64}r_{94}$。
参考 ordinary residual
$e_0=(K_\perp)_t-Q(2K_\perp+U)$ 的前三径 scaled导数再至多收
$d^{-1}=2^{1024}$。

最后恢复 E.3/E.5 的原 finite权 $2^{440}$，得
$$
 \boxed{\quad
 \|\ell_B\|_{E_s}<2^{8192}r_{94},
 \qquad 0\le s\le8192 .
 \quad}                                                   \tag{G.21}
$$
实际总指数只需 $4096+64+1024+440<8192$。
(G.14) 的剩余角宽大于 $8198$；
对同一物理 Fourier 频率 $m\in4\mathbb Z\setminus\{0\}$，$\Lambda_m\le e^{|m|}$，因此上述有限高
$H^s$ norm及额外两角导从完整 $A_{\sigma-16}$ 直接控制。
此处没有把有限 Fourier支持当完整输入。

本次只在 finite connector使用 ordinary $e_0$。
内部 $c_0e_0$ 及其所有新增 source均为0，故不能在 (G.21) 另造一个
$\rho^{-3}$ 或 $\mu_j^{-1}$ 的单位。新对象的
$\rho,\epsilon$ 已在 (G.8)、(G.19) 的同一实际 $a_B,w_B$ 中，
正好以 ratio消去；它们没有被改成旧对象的数。
若要输出物理 Darboux density source，仍应乘原真正 density，
而不是把本式的 ordinary $e_0$ 直接改名。

## 7. Holonomy、两 mean 和唯一高度规范

对 $\widetilde u$ 重新应用 E.12 的同一个实际 holonomy小根。
除 collar外，非mean四态和 metric都与 $u^\dagger$ 相同，
所以小根也逐点相同。在 B，由 (G.9)--(G.10)，
$P,U,K_\perp,V$ 和 $q_{\rm phys}$ 全部与同一个 long 相同；
小根唯一性给
$$
                         \widetilde\kappa(0)=\kappa_{\rm L}(0).
 \tag{G.22}
$$
所以 $w_B\kappa$ 的真实 mean slope也已匹配，未设置 $\kappa=0$。

选择唯一整体 $\lambda$，使 E.13 的平均高度在 B等于同一个
cap--long的真实平均高度。其余高度由一次连续积分决定，特别保留
$$
 \Delta H_0(t)=
 \Delta\lambda+\int_{t_f}^t
        a(s)w(s)[\widetilde\kappa(s)-\kappa^\dagger(s)]\,ds .
 \tag{G.23}
$$
它在 collar外可能是非zero常数，不得每胞重新置0。
同一低阶 holonomy导数界和 (G.14)、(G.20)给宽界
$$
 |\Delta H_0(t)-\Delta H_0(0)|
                      <a_Bw_B\,2^{8192}r_{94}.
 \tag{G.24}
$$
这是实际物理高度费用，不带 $\varepsilon_L$。

重建后全场准确满足 holonomy-one。
由 E.14，完整 source为
$$
       \mathfrak F(\widetilde u)
        =\Pi_{A_{\widetilde u}}
                    P_\perp\mathfrak F(\widetilde u),\qquad
       A_{\widetilde u}=JD^{-3/2}.
 \tag{G.25}
$$
普通 source mean一般非zero；本式不把它删除。
本篇没有引入独立非zero flux荷。若外问题另外给这样的荷，
它不属于 (G.25) 的恒等式，仍按 M 的独立荷图保留。

## 8. 真正完整 source 的三径门

原真成员 $\mathfrak F(u^\dagger)=0$。
第一参数在本次局部改动前后相同，故 E.17 在 collar准确是
$P_\perp e=e_0-P_\perp{\cal Q}_F$；
在其余区域，全部 nonlinear source仍为0。

由 (G.3)、(G.21)，
$$
                   \|\widetilde u\|_{E_{8192}}
                         <2^{-54866996}<\rho_E/8,
 \qquad \rho_E=2^{-8192016}.
 \tag{G.26}
$$
用 E.20--E.25 的完整三径 tame差及 $K_E=2^{2097152}$，
对 $0\le s\le6396$，最高所需 state阶为 $s+4\le6400$：
$$
 \begin{split}
 Z_s^{[3]}(P_\perp\mathfrak F(\widetilde u))
 \le &\, Z_s^{[3]}(\mathcal L_0\ell_B)\\
 &+K_E\{(2\|u^\dagger\|_{E_{20}}+\|\ell_B\|_{E_{20}})
                   \|\ell_B\|_{E_{s+4}}
       +\|\ell_B\|_{E_{20}}\|u^\dagger\|_{E_{s+4}}\}.
 \end{split}
 \tag{G.27}
$$
(G.3) 的实际低量远比 $K_E^{-1}$ 小；
再用 A.4--A.5 对 (G.25) 的完整三径 mean投影收费，
可统一保留以下更宽的明定预算：
$$
 \boxed{\quad
 Z_s^{[3]}(\mathfrak F(\widetilde u))
 <2^{4194304}r_{94}
 <2^{-5275847456},\qquad 0\le s\le6396 .
 \quad}                                                   \tag{G.28}
$$
这里 $5280041760-4194304=5275847456$。
未将原 far norm直接宣称为 $Z_s^{[3]}$；(G.10)--(G.27)正是中间
全部物理/jet/cutoff/source转换。每项都是同一实际成员上的界。

collar内初始场仍有一般非zero Darboux residual；
只有当后续迭代将它解为0时，才得到该处真正的等距曲面。
源具有上述完整 ordinary门，不能用初始 Cauchy数据已匹配
来宣称 PDE也已匹配。

## 9. 对已发布 finite Nash 初始门的准确比较

对 B 的 $a=1856,b=6396$，(G.26)和(G.28)已经支付真实 body初值：
$$
 \|\widetilde u\|_{E_a}<\rho_E/8,\qquad
 \|\widetilde u\|_{E_b}+|\mathfrak f(\widetilde u)|_b<1,\qquad
 |\mathfrak f(\widetilde u)|_a<2^{-5275847456}.
 \tag{G.29}
$$
这里 $|\mathfrak f|_s=Z_s^{[3]}(P_\perp\mathfrak F)$。
(G.29)并不包含一个尚未更新完的外部 $B_*$ 上界。

例如，若后续对同一 actual外行另外核得
$$
                         B_*\le2^{6000000},
 \tag{G.30}
$$
则可准确选择 $T_0=2^{1500000}$。
B.9 给
$\log_2(16C_*)\le134217728+8(6000001)+4=182217740$，
而
$$
 \log_2 T_0^{126}=189000000,\qquad
 \log_2 T_0^{1266}=1899000000 .
$$
两常数门以及 $T_0\ge1+\|\widetilde u\|_b+|\mathfrak f(\widetilde u)|_b$
均成立，且
$$
 |\mathfrak f(\widetilde u)|_a
       <2^{-5275847456}<2^{-4500000000}=T_0^{-3000}.
 \tag{G.31}
$$
这仅将 (G.30) 保作清晰的独立实际外门。
它不以帽或 long 某一个低阶 norm替代完整 $B_*$，
也不从 body source极小推出所有真实外荷已小。

## 10. 已对齐的行与仍须联立的行

当前初始 B 接口的非mean高度、非mean slope、holonomy mean slope、
一个选定的 mean高度和所需真实单侧 jets已由 (G.9)--(G.25)对齐。
内部原胞元/根/两接缝完全未改；没有新增 impulse。
共同反射、所有真实 modes、$C^4$及更高 broken径向口径保持。

这些是初始 scalar图的准确事实，不意味着随后的 body Newton修正
会自动保持 nonlinear far返回。A.22--A.24 的真实端口缺陷仍必须在
同一个 augmented近似右逆中处理。特别：

- actual cap--long 的 nonlinear外行必须更新到这个同一背景，
  并支付其真实低 form、伴随、所有 Poisson与 mean列；
- cap内输入 $\gamma$ 的选择以及 $B(L),C_0(L)$、frame/phase、
  真实内端高度和 $\nu$ 仍须与原 body 一起匹配；
- 只有一个全局高度常数 $\lambda$；其余 height/span和任何独立
  flux荷均留在同一个 Schur，不能为每片另置规范；
- (G.30)和 augmented初始数据门若尚未核验，本篇不登记它们通过。

本篇完成的是新94成员到原窄源 graph的同对象、同物理单位入口。
完整有限 Nash迭代可以消费其 body种子；全几何结论仍取决于以上
实际 augmented行和相容域的闭合。
