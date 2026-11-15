# R119 续篇：固定实际帽输入的外预算及真实 body Nash 初入口

2026-11-15，visible-exact / tail_connector。

**状态：已证明的解析结论，声明域内。** 本篇对同一个已经存在的实际
两输入帽，固定其内端非mean物理曲率输入 $\gamma$，将外图的高范数
依赖从变化的 tail 状态中准确分开。因此新94/collar种子的
body Nash 归纳有了确定的外常数，不再条件于一个未计量的 $B_*$。

结论仍限于 body residual。迭代中采用真实 linearized 外行，
不意味着 nonlinear 端口误差自动保持为0；真实内帽匹配、mean、
height/frame和设计参数行仍必须联立。本文不新增数值计算或新对象。

使用：

* [P：新同对象94链](R119-supplement-new-fixed-stop-small-width-cap-and-full-94-step-chain.md)；
* [G：真实 B collar种子](R119-supplement-new-94-B-collar-lift-and-actual-graph-seed.md)；
* [E：固定参考图范数](R119-supplement-reference-graph-scale-exact-residual-and-angular-smoothing.md)；
* [A：graph近似右逆](R119-supplement-reference-graph-approximate-right-inverse-and-exact-port-defects.md)；
* [B：3500/400 finite Nash归纳](R119-supplement-finite-Nash-iteration-in-reference-graph-with-port-conditions.md)；
* [O：actual两输入 long行](R133-supplement-actual-two-input-cap-long-tame-forms-and-physical-Poisson.md)；
* [HT：actual外行的完整 high/source账](R119-supplement-actual-cap-outer-update-in-full-network-tame-and-source-windows.md)。

所有 $E_s,Z_s^{[3]}$、source单位、层权、scaled径向导数、
真实分片和有限connector保持原定义。

## 1. 固定的是哪一份输入

固定同一实际修补 M32 帽及其 $\eta_0,\delta=0$ intrinsic数据。
令 $\sigma_0=1/8192,\ r_\gamma=10^{-9},\ r_B=2^{-60}$。
帽内输入 $\gamma$ 是物理 $C_{\ne0}(L)$ 的原指定增量；
不是尾第一参数 $\Gamma_1$，也不是一个 independent mean。

先给一般的固定 finite-Sob 输入门：
$$
 \gamma\text{ real-even},\qquad
 \|\gamma/r_\gamma\|_{A_0}\le1/128,\qquad
 \|\gamma/r_\gamma\|_{H^{8176}}\le2^{1048576},\qquad
 G_\gamma:=1+\|\gamma/r_\gamma\|_{H^{8176}}
                                      <2^{1048577}.
 \tag{F.1}
$$
$\gamma$ 在每一次 smoothing、proxy和 nonlinear帽图调用中保持同一函数，
不能事后按每个 $v_n$ 重选。这不是对未知 inner匹配问题的解。

为了取得本篇后段的**已存在初值**，使用原P/G已经覆盖的子域
$$
 \gamma\text{ real-even},\qquad
 \|\gamma\|_{A_{\sigma_0}}\le r_\gamma/128 .
 \tag{F.2}
$$
尤其 $\gamma=0$ 在其中。这里
$A_\sigma(f)=\sum_{m\in4\mathbb Z}e^{\sigma|m|}|f_m|$，
$\sigma$ 是物理角宽，不是Sobolev阶数。
(F.2)仅用于选择固定输入及原解析预处理；后续未知 $f_B(v_n)$
不要求有复角值。

(F.2)直接推出(F.1)。对 $0\le k\le8176$，
完整 Fourier 矩给
$$
 \|f\|_{H^k}
 \le\sup_m\{\langle m\rangle^ke^{-\sigma_0|m|}\}\|f\|_{A_{\sigma_0}}
 \le2^{26k+8}\|f\|_{A_{\sigma_0}} .
 \tag{F.3}
$$
用 $\langle m\rangle\le1+|m|$、$|m|^ke^{-\sigma_0|m|}
 \le k!\sigma_0^{-k}$，
以及 $k!\le((k+1)/2)^k<2^{12k}$（$1\le k\le8176$）即可；
$k=0$直接读原norm。这里包括全部正负模式，没有截尾。
因 $26\cdot8176+8=212584<262144$，
实际上 $G_\gamma<2^{262145}$，比(F.1)更强。

## 2. B端四态到真实高度的全阶读取

取 E 的同一 holonomy-one图成员 $u\in E_{8192}$，低球为
$$
 \|u\|_{E_{1856}}\le\rho_E/2,\qquad \rho_E=2^{-8192016}.
 \tag{F.4}
$$
所有 $\Gamma_1,\Gamma_2$ bump支集与新增finite connector不交，
所以 E.17 准确给 $\psi=0$；特别 B处的 $a_Bw_B=s_B$ 不随
当前 $\Gamma_1^*(u)$ 变化。

定义真实 normalized非mean高度
$$
 f_B(u)=u(B,\cdot)/s_B .
$$
其完整四态满足
$$
 P_T=\partial_\theta f_B,\quad
 U_T=\partial_\theta^2 f_B,\quad
 K_T=K_{T,\perp}+\kappa_T,\quad V_T=\partial_\theta K_{T,\perp}.
 \tag{F.5}
$$
$\kappa_T$ 是同一个真实holonomy小根，普通mean不设零。
$u$本身普通角mean为0；$\lambda$和总mean高度在原独立坐标中保留。

E.22 在每个 $20\le a\le8192$ 给
$X_a^{\rm true}\le16\|u\|_{E_a}$。
其finite部分准确带 $2^{440}$，故四态每一分量的 B迹都小于
$2^{-436}\|u\|_{E_a}$。
对非mean物理频率 $|m|\ge4$，
$$
 \frac{\langle m\rangle^2}{m^2}\le17/16 .
 \tag{F.6}
$$
因此 O.13 的两个真实输入数，在 $64\le q\le8144$ 有
$$
 \boxed{\quad
 n_q(u)+f_q(u)
 \le(4+17/16)\,16\,2^{-440}\|u\|_{E_{q+32}}
 <2^{-430}\|u\|_{E_{q+32}} .
 \quad}
 \tag{F.7}
$$
这里 $n_q$ 是四态的 $H^{q+32}$ block sum，
$f_q=\|f_B\|_{H^{q+34}}$。
常数81小于 $2^7$，显示的 $2^{-430}$另留三bits。
没有索取 $u$ 的 $q+34$ 阶四态，因为高度的两额外导数已经是 $U_T$。
没有把物理 $1/s_B$ 当成有界常数：它正是 E.2--E.3 已定义的state单位。

(F.7)同时保 $\kappa_T$ 的mean，因 E.22 的 $X^{\rm true}$从定义就含它。
只用 $K_\perp$ 的界不能单独推出这个结论。

## 3. 每个实际调用都留在同一外域

E.22与(F.4)给 N.1 的真实低背景
$\mathscr R_{1856}<2^{-8192000}$。
在1824阶直接从同一完整 $X_{1856}^{\rm true}$ 的finite项读取，
再用(F.6)，给 O.21 所需的
$n_{1824}+f_{1824}\le2^{1024}\mathscr R_{1856}$；
其宽数远大于上述实际state迹界。这一步不把 $E_s$ 与
$X_s^{\rm true}$ 的单向上界反用。

帽 normalized product低门也直接成立。
由 $A_0\le2H^2$、(F.7)和(F.4)，
$$
 \|\gamma/r_\gamma\|_{A_0}
 +\||D|^2f_B/r_B\|_{A_0}
 +64\|\mathbf V_T\|_{A_0,\rm sum}
       <1/128+2^{-100}<1/64 .
 \tag{F.8}
$$
这里 $r_B^{-1}=2^{60}$明确保留。
所以始终进入 O.4 的 $1/16$球及真实帽值图的严格内域。
(F.1)还直接给 O.21 的 $g_{1824}\le2^{1048576}$。

因此 O.23b 和 D/HT 的两个独立 N2门对每一次实际 $v_n$成立。
高阶 $\|v_n\|_{E_{8192}}$ 可以增长；这一步没有用它做small gate，
也没有从 $\mathcal A_{64}$小推 $\mathcal A_{1824}$小。
原第二相位间隙仍由 N.1a/b 的低196阶输入保证。

## 4. 用固定系数抽出变化的高状态

令 $\epsilon=e^{-7L/4}<2^{-57000000}$。
对任何(F.4)成员和 $64\le q\le8144$，
O.13给
$$
 \begin{split}
 \mathcal A_q(u)+\epsilon\mathcal D_q(u)
  ={}&n_q+f_q+
      (n_{64}+f_{64}+\epsilon)(1+g_q)\\
     &+\epsilon(1+g_q+r_B^{-1}f_q+64n_q).
 \end{split}
 \tag{F.9}
$$
$g_q\le G_\gamma-1$ 是固定输入的数，$n_q,f_q$则随 $u$变化。
用(F.7)、$\|u\|_{E_{96}}\le\|u\|_{E_{q+32}}$ 和
$2^{60}\epsilon<1$，逐项得
$$
 \boxed{\quad
 \mathcal A_q(u)+\epsilon\mathcal D_q(u)
 \le4G_\gamma\{\|u\|_{E_{q+32}}+\epsilon\}.
 \quad}
 \tag{F.10}
$$
这一步既不令 $\epsilon=0$，也不让 fixed $\gamma$ 的高norm变成小量。

定义一个**固定**的外系数
$$
 \overline B_\gamma:=2^{1024}G_\gamma
                         <2^{2097152}.
 \tag{F.11}
$$
1024含上述finite B归一的充分余量；
$1024+1048577=1049601<2097152$。
它是单个选定 $\gamma$ 的数据，不是
$\sup_n\mathcal A_q(v_n)$，也不是将 B.8的旧固定外行假设改名。

特别对 $64\le s\le6396$，实际调用 $q=s+1748$ 给
$q+32=s+1780<s+1796$，故
$$
 1+\|v\|_{E_{s+1796}}+
        \mathcal A_{s+1748}(v)+\epsilon\mathcal D_{s+1748}(v)
 \le\overline B_\gamma(1+\|v\|_{E_{s+1796}}).
 \tag{F.12}
$$
最高仍是 $s+1796\le8192$。未增加原1734 source损失，
也不将未知 $f_B$ 放回一个解析输入空间。

## 5. 真实 nonlinear外图下重实例化 body近似逆

在每个 $v$ 处使用同一 $\Phi_\gamma(f_B(v))$ 的真实线性化外行，
包含 $D_f\Phi_\gamma$ 的反馈及全部mean；不是固定远端 $f_*$。
HT支付新外高常数后，A.13/A.15与(F.12)给
$$
 \|\mathcal R_v(g,0)\|_{E_{20}}+X_{20}(H)
                   \le2^{10485768}|g|_{1794},
$$
$$
 \|\mathcal R_v(g,0)\|_{E_s}+X_s(H)
 \le2^{10485768}|g|_{s+1734}
   +2^{41943040}\overline B_\gamma
       (1+\|v\|_{E_{s+1796}})|g|_{1794}.
 \tag{F.13}
$$
这里只用 compatible body channel，未给独立外荷。
$H$仍是同一次完整proxy解，$P_\perp H=\mathcal R_v(g,0)$。
原准确 body缺陷继续是
$$
 Df(v)\mathcal R_v(g,0)=g-P_\perp\mathcal E_v[H].
 \tag{F.14}
$$
A/J 的 $\mathcal E$、$D\Pi_A$、三径source与第一参数metric列全保留。
(F.14)是body恒等，不把 nonlinear boundary derivative缺陷删掉。

实际外图只进入(F.13)的operator；body nonlinear残差
$f(u)=\mathcal L_0u+\mathcal Q(u)$、E/A的Taylor余项及 smoothing恒等
均未改变。因而原 B.4--B.7在这个实际外图下全部有了明确输入。

## 6. 固定迭代常数和真实初值

重新固定 B.9 的统一常数为
$$
 C_\gamma=2^{134217728}(1+\overline B_\gamma)^8 .
 \tag{F.15}
$$
原单步证明至多两份校正、一次完整Taylor/graph读出；
所有 $\overline B_\gamma$因子和 (F.13)中的high状态按原once-high分组。
这次重实例化不要求把变化的 $\mathcal A_q(v)$本身变成固定上界。

选原 P/G 在同一个(F.2)输入下已经构造的
$\widetilde u=u_{94}+\ell_B$ 为 $u_0$。
G.26/G.28的实际同单位结论为
$$
 \|u_0\|_{E_{8192}}<2^{-54866996},\qquad
 |f(u_0)|_s<2^{-5275847456},\quad0\le s\le6396 .
 \tag{F.16}
$$
它是新对象的第94链与真实Hermite source，不用旧对象的数据。
G的全部mean、ordinary源前三径导、五阶broken口径、
唯一 $\lambda$和原内部matching一并保留。

明确取
$$
 T_0=2^{1500000}.
 \tag{F.17}
$$
(F.11)给
$$
 \log_2(16C_\gamma)
  <134217728+8(2097153)+4=150994956<189000000
                         =\log_2T_0^{126},
$$
$$
 \log_2(16C_\gamma/\rho_E)
       <159186972<1899000000=\log_2T_0^{1266}.
 \tag{F.18}
$$
另有 $\|u_0\|_{E_{1856}}<\rho_E/8$、
$1+\|u_0\|_{E_{6396}}+|f(u_0)|_{6396}<T_0$，且
$$
 |f(u_0)|_{1856}<2^{-5275847456}
                       <2^{-4500000000}=T_0^{-3000}.
 \tag{F.19}
$$
所以原B全部body初始门现已实际支付；没有只比较两个不相同对象的bits。

## 7. 全归纳使用同一个变化的实际帽图

仍取
$$
 T_n=T_0^{(5/4)^n},\quad v_n=S_{T_n}u_n,\quad
 w_n=-\mathcal R_{v_n}(S_{T_n}f(u_n),0),\quad
 u_{n+1}=u_n+w_n .
 \tag{F.20}
$$
$\gamma$固定，$\Phi_\gamma$的输入则始终是当前真实 $f_B(v_n)$。
$w_n$外面没有第二次Fourier截断。
$u_n$只需 $E_{6396}$，$v_n$有 $E_{8192}$，每次都由真实
$\Gamma_1^*(v_n)$、holonomy小根和单一高度规范重建。
所有候选保持同轴反射，由完整方程唯一性和相同实 Fourier投影保证。

为排除把 $B_*$取sup隐藏进迭代的问题，逐条重读原幂：
在低 $a=1856$，(F.12)新增的状态因子仍是
$\|v_n\|_{E_{a+1796}}\le T_n^{1120}$，
所以纯source项 $T_n^{-1266}$主导。
在高 $b=6396$，
$\|v_n\|_{E_{b+1796}}\le T_n^{1796+2800}$，
乘低source $T_n^{-3000}$得到1596；
纯source仍是3274。所有其余外系数是一次性 $C_\gamma$。

因此B.19--B.25的表逐项保留：
低尾 $-4220$、二次 $-4266$、两背景差 $-4740,-4842$、
残差缺陷 $-4739,-4266$；高表仍准确为
$1\cdot T_n^{320}+C_\gamma T_n^{274}$。
状态的 $C_\gamma T_n^{3274}$用226幂吸收到3500；
高source的新项用126幂吸收到400。
(F.18)恰好足够，不先粗成 $C_\gamma T_n^{320}$。

故完整归纳为
$$
 |f(u_n)|_{1856}\le T_n^{-3000},\quad
 \|u_n\|_{E_{6396}}\le T_{n-1}^{3500},\quad
 |f(u_n)|_{6396}\le T_{n-1}^{400},\quad
 \|u_n\|_{E_{1856}}\le\rho_E/4 .
 \tag{F.21}
$$
(F.8)和O/HT低门在每一步成立，无需另取与high norm有关的cutoff。
由原可和界，$u_n$在 $E_{1856}$收敛到 $u_\infty$，
真实holonomy mean和同一个第一参数值图传到极限，完整body residual为0：
$$
 \mathfrak F(u_\infty)=\Pi_{A_{u_\infty}}f(u_\infty)=0 .
 \tag{F.22}
$$
原两mean、深层weighted径向读出及原须连续的内部traces保持。
本文不以角1856阶单独代替物理径向 $C^2$ 的原E/J层衰减证明。

## 8. 已支付的门与剩余实际匹配

本篇已支付固定(F.2)实际帽输入下的固定外乘子、实际body初值及
变化的actual外图中的全部body归纳。
(F.11)满足原G.30要求的 $2^{6000000}$充分幅度，但其准确含义是
(F.12)的固定系数；变化的高state仍显式留在原tame项内。

每个proxy解只满足其当时真实 linearized外行。
Taylor之后 nonlinear far残差一般有二次余项，不能因初始G.22的
Cauchy matching就宣称所有 $u_n$或 $u_\infty$仍匹配该行。
A.19--A.24的端口缺陷、跨端 $H_p$、独立flux和meanheight继续保留。
同样，帽内 $\gamma$仍是这里固定的输入，尚未与M32主体/waist求解；
内B/Cmean、frame/phase、两端height及设计参数仍是真正未知行。

因此(F.22)不是单个全闭精确 $G$ 的存在定理。
它将原实际种子上的 $B_*$和body初始化两项从待付改为已付，
使下一步可集中处理具体 nonlinear端口和内端增广Schur。
在取得单个全闭 $G$ 后，intrinsic参数全部冻结，
挠曲族按已证明的材料圆作用与固定marker构造；
不再要求一个变动$\nu$的固定metric族IFT。
