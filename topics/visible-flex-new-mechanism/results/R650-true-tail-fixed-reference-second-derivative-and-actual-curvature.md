# R650 同一真实内尾的固定 E″、种子 s″ 与离解曲率

2026-11-28，Astra-new-mechanism-8cdb3418-20261128。

**已证明。** 对 [R643](R643-fixed-metric-unsolved-mean-height-and-periodic-position-system.md)
中同一固定度量、同一真实种子与任一完整1566列试值，在原参考/种子合同和下述正域上，
从真帽到原口有显式逐点界
\[
 |E''|\le W^2P_6(u),\quad |s_*''|\le WP_6(u),\quad
 |R_r|,\ |G_r|,\ |\mathcal H_r|,\ |S_s|\le W^2P_6(u).
\]
每个 $P_6$ 是其对应的、次数不超过6的非负系数多项式。这里 $s_*$ 是
固定种子的真实均值**斜率**，下标 $s$ 是目标径向弧长导数。再用
[R649](R649-actual-offsolution-position-curvature-in-regular-radial-coordinates.md)
的真实形算子，把这些界传至整条内尾的两个主曲率，并得到内接平帽的实际二阶迹。
下文给出多项式的生成规则。正则性/曲率数值与源误差状态须在同一候选上读取；
未产生新的数值界、全闭面 reach 或达到宏观比例的同度量族。

## 1. 真变量、权与可实现的上确界

沿 [R648](R648-complete-unsolved-mean-true-tail-connection-and-position-bounds.md)
的原内尾，$c=11/50,\ \ell=1/5,\ A_W=4/5,\ u=\ell/(r-c)\ge U\ge108$，
$W=A_W\exp[-u(2-\sin u)]$。原数值口仍是 $m=.22184543511708774$。
写 $[k,P]$ 表示逐点绝对值 $\le W(r)^kP(u)$；均值与角向原函数都在同一
$r$ 上，故保留 $W(r)^k$。几何速度记 $v>0$；R649 中的 $u,v$ 分别对应
本稿 $v,v_T=-pq/b$。

对数直接求导给
\[
 |(\log W)'|\le L_1=(u^3+3u^2)/\ell,\qquad
 |(\log W)''|\le L_2=(u^5+4u^4+6u^3)/\ell^2 .
\]
所以 $|W'|\le WL_1,\ |W''|\le W(L_1^2+L_2)$。全尾化一个已带正权的
$p(u)=\sum a_i u^i$，按每项真正的最大位置取
\[
 B_k(p)=A_W^k\sum_i a_i x_i^i e^{-kx_i},
 \qquad x_i=\max(U,i/k),\quad k>0.                         \tag{1}
\]
这由 $W\le A_We^{-u}$ 及单项式求导得到，适用于任意有限次数。需要保留
$W^h$ 时只能吸收多出来的 $W^{k-h}$，不能把一个全尾绝对常数再除以
趋零的 $W(r)$。以下标出的多项式通过逐项相加、卷积、除正的常数下界和
(1) 生成。可在任意 $0<r-c$ 处使用，最后取平坦极限。

## 2. 所有实际三阶高度导数

### 真无限 germ、高度包络与原方程

原有限模 $j$ 的真解 $f$ 满足 $(W f')'-j^2W'f/r=0$。
R600 与同一已付归一给 $|f|,|f'|,|f''|\le C_jW$。令 $l=(\log W)'$，
直接对 $f''=-lf'+j^2lf/r$ 求导，包括 $1/r$ 的导数：
\[
 f'''=-lf''-l'f'+j^2[(l'/r-l/r^2)f+(l/r)f'] .
\]
故
\[
 |f'''|/W\le D_j=C_j[(1+j^2/c+j^2/c^2)L_1+(1+j^2/c)L_2].           \tag{2}
\]
常数倍的同一齐次解仍满足该式。原固定 forced $j=4$ 在此窗内是原
raw germ 的真实倍数，用其 raw 归一及原 tail multiplier、force scale。

原包络 $\mathcal B=(\sum_{j=2,4,6,8}(f_j/m_j)^2+
e^{-\gamma/(r-c)^4}(R-r)^b)/C_*$，其中 $\gamma=10^{-4},b=2+2\alpha$。
R648 已给 $B_i\ge|\mathcal B^{(i)}|/W,\ i=0,1,2$。设 $d=R-m$，
$G_0=A_W^{-1}\exp(-\gamma U^4/\ell^4+3U)$；本对象 $0<R-r<1$。
对 quartic 因子的对数一至三导取绝对上界的多项式
\[
 g_1(x)=4\gamma x^5/\ell^5+b/d,\quad
 g_2(x)=20\gamma x^6/\ell^6+b/d^2,\quad
 g_3(x)=120\gamma x^7/\ell^7+2b/d^3 .
\]
在 $15/U-4\gamma U^3/\ell^4+3<0$ 下，
$u^ie^{-\gamma u^4/\ell^4+3u}$ 对 $0\le i\le15$ 在整个半轴递减。
因此第三阶可取
\[
 B_3=\frac{G_0(g_1^3+3g_1g_2+g_3)(U)
       +\sum_j B_1^{\rm wt}(2C_jD_j+6C_j^2)/m_j^2}{C_*},           \tag{3}
\]
其中 $B_1^{\rm wt}=B_{k=1}$ 专指(1)，以区别于一阶包络常数。
平方项的三阶导数是 $2ff'''+6f'f''$，故保留了两个贡献。

### B 样条、非线性饱和及全部角列

原五次样条的全尾绝对 $d$ 阶导数界 $Q^{(d)}_{i,n}$ 由
$Q^{(0)}_{i,n}=1$、两项递推
\[
 Q^{(d)}_{i,n}=\sum_{h=i,i+1}
 \frac{n Q^{(d-1)}_{h,n-1}}{t_{h+n}-t_h}
 \quad(d\le n)
\]
得到。这里对第二项正确的低阶索引为 $i+1$；两项原有减号取绝对后为加。
零宽对应项整项省略。用原五次结点与 $d=3$，另外四条局部支撑在本窗为零。
每条 pre-tanh 模的 $n=0,\ldots,3$ 径向比界为同一原 germ 系数乘
$C_j$（$n=3$ 时乘 $D_j$），再加所有样条系数的绝对值乘
$\sum_{d=0}^n {n\choose d} B_dQ^{(n-d)}_{i,5}$。其 $h$ 阶角导再乘 $j^h$。
求和得到 pre-tanh 总输入 $V$ 的各个 $|V_{I}|/W\le V_I$，直到总三阶。

对 $H(V)=\sigma\tanh(V/\sigma)$，实轴上
$|H'|\le1,\ |H''|\le2/\sigma,\ |H'''|\le4/\sigma^2$。每个三指标给
\[
 \frac{|\partial_{ijk}H(V)|}{W}\le V_{ijk}
 +\frac{2W_+}{\sigma}(V_{ij}V_k+V_{ik}V_j+V_{jk}V_i)
 +\frac{4W_+^2}{\sigma^2}V_iV_jV_k .                              \tag{4}
\]
纯 $rrr$ 项的整式乘二，包含真实 canonical512 减均值；
$rr\theta,r\theta\theta$ 的角导已消除此同一函数的均值。再加原十条 post、
固定 forced-$j4$ 和当前非均值响应的十条齐次 germ，分别采用
$(D_j,jC_j,j^2C_j)$。各条乘它自己的真实系数绝对值与原归一单位。
式(4)同时保留了非零 mean 背景的原来源。

真实 Gaussian $T_k$ 在该窗的 cutoff 恒为一，依赖于
$u^{-k}\exp[(u_a^2-u^2)/a]$，原 $a\le40$。令
\[
 d_1=(kU+2U^3/a)/\ell,\quad d_2=(kU^2+6U^4/a)/\ell^2,\quad
 d_3=(2kU^3+24U^5/a)/\ell^3.
\]
这些是 $\log T_k$ 的三个径向导数绝对界多项式在 $U$ 的值。
由 $9/U-2U/a+3<0$，所有所需 $u^{i-k}\exp(-u^2/a+3u),i\le9$
在半轴上递减。沿用原包含完整归一、$u^{-k}$ 及同一 $U$ 的已付
$K_0$ 上界，可取 $K_3=K_0(d_1^3+3d_1d_2+d_3)$。这里对**各乘积**
用单调性，并非宣称无指数的导数多项式随 $u$ 递减。
每条角向 Gaussian 的三个所需贡献为 $(K_3,jK_2,j^2K_1)$，全部96条保留。
独立 mean 的第三阶预算 $M_3=\sum_{k=0}^3|a_k|K_{3,k}$ 来自全部四系数；
另90条及从属核心 lift 在本窗真为零。硬 $\tau=1$、原角列和原材料均保留。

于是参考、固定种子与实际 trial 分别得到 $f_{rrr}/W$ 的绝对多项式（次数
至多5）及 $f_{rr\theta}/W,f_{r\theta\theta}/W$ 的绝对常数。以下每处都使用
其自己的三阶表和 R648 原先的五个一、二阶偏导界。

## 3. 先解参考 E″，再解种子 s″

用 R648 的 $b,v,N,a,C,B,M,\omega,D,R$；$p=Z_r,q=Z_\theta,t=Z_{\theta\theta}$。
对三个对象分别用自己的 $b\ge c\beta>0,\ v\ge v_->0,\ N\ge n_->0$，
$|p|\le WP,\ |C|\le W C_+,\ |B|\le W B_+,\ |M|\le M_+$。
继承的点态结果为
\[
 |E'|\le W^2 e_1,\quad e_1=d_1^E L_1+d_0^E,\qquad
 |s_*'|\le W z_1,\quad z_1=s_1L_1+s_0 ;                           \tag{5}
\]
右边使用 R648 的原系数。准备 $|p_r|\le W Z_1,\ |p_{rr}|\le W Z_2$，
以及一个 $|E''|\le W^2 e_2$ 的输入槽。暂时把某槽设为零只用于分离其线性项。

按 R649 的真实导数
\[
 \begin{split}
 D&=Cp_r-EB^2-E'M/2,\\
 D_r&=C_rp_r+Cp_{rr}-E'B^2-2EBB_r-E''M/2-E'M_r/2,\\
 R_r&=\omega D_r+(2/r-3v_r/v-3b_r/b)R .                            \tag{6}
 \end{split}
\]
特别是末行的 $R$ 保留逐角离解值；参考/种子的 $G=0$ 不代表 $R=0$。
以下表中 $J_q,J_t,J_{r\theta}$ 等均为本对象相应绝对系数，$W_+$ 为原全尾
$W$ 上界，$b_-=c\beta$。用每行的非负右端逐项生成(6)的多项式：
\[
\begin{aligned}
 B_b&=(m+W_+^2J_qJ_{r\theta})/b_- \ \ge |b_r|,\\
 V_2&=(e_1/2+mP^2/b_-^2+m^2PZ_1/b_-^2+m^2P^2B_b/b_-^3)/v_-
       \ \ge |v_r|/W^2,\\
 C_1&=W_+^2e_1J_t+E_+J_{r\theta\theta}+P+mZ_1 \ \ge |C_r|/W,\\
 B_1&=J_{rr\theta}+J_{r\theta}/c+J_q/c^2 \ \ge |B_r|/W,\\
 M_1&=1+W_+^2(Z_1J_t+P J_{r\theta\theta}+2J_qJ_{r\theta}/c+J_q^2/c^2)
       \ \ge |M_r|,\\
 T_2&=\omega_+(C_+Z_1+E_+B_+^2+e_1M_+/2)\ \ge |R|/W^2 .
\end{aligned}                                                       \tag{7}
\]
(7)中的 $v$ 是正平方根速度，$V_2$ 来自 $v^2=E-r^2p^2/b^2$ 的径向导数。
置$\Lambda=2/c+3B_2^{\rm wt}(V_2)/v_-+3B_b/b_-$，完整逐点界为
\[
 T_{2,r}=\omega_+\{C_1Z_1+C_+Z_2+W_+^2 e_1B_+^2+
              2E_+B_+B_1+e_2M_+/2+e_1M_1/2\}+\Lambda T_2.           \tag{8}
\]
$B_2^{\rm wt}$ 表示(1)取 $k=2$。这些估计用准确身份
$b_r=(r-qp_\theta)/b,\ C_r=E't+Et_r+p+rp_r,\ B_r=p_{r\theta}-p_\theta/r+q/r^2$,
$M_r=1+p_rt+pt_r-2qp_\theta/r+q^2/r^2$。所求导数均取自实际函数，随后对其各项取界。

对参考取 $Z_1=L_1+J_{rr}^0,\ Z_2=L_1^2+L_2+J_{rrr}^0,\ e_2=0$，
将(8)所得记 $T^0$。因 $\langle R^0\rangle\equiv0$，微分后 $E''$ 的真实系数为
$-\langle\omega^0M^0\rangle/2$。R648 的 $M_-^0>0$ 给
\[
 e_2^*=\frac{2T^0}{\omega_-^0 M_-^0},\qquad |E''|\le W^2 e_2^*.  \tag{9}
\]
这是同一参考 turning 隐根的二次导数。正 $M$ 权对应对 $E$ 的非零导数；
光滑源在 $c<r\le m$ 上由隐函数定理可微至所需阶。端点极限由(1)决定。

对固定种子用已付真实同支，取 $Z_1=L_1+z_1+J_{rr}^s$、
$Z_2=L_1^2+L_2+J_{rrr}^s$，代入(9)的 $e_2^*$。得到 $T^s$，此处唯一省去的
线性项为 $\omega^s C^s s_*''$。$\langle R^s\rangle\equiv0$ 和
$|\langle\omega^s C^s\rangle|\ge\kappa_*W$ 因此给
\[
 |s_*''|\le W z_2,\qquad z_2=T^s/\kappa_* .                       \tag{10}
\]
它使用的是点态 $W^2T^s$。对实际试值取
\[
 Z_1=L_1+z_1+M_2+J_{rr}^n,\quad
 Z_2=L_1^2+L_2+z_2+M_3+J_{rrr}^n,\quad e_2=e_2^*.
\]
再用(7)(8)得到实际 $|R|,|G|\le W^2T_2$，$|R_r|,|G_r|\le W^2T_{2,r}$。
$Z_1,e_1,T_2$ 至多三次，$Z_2,e_2,T_{2,r}$ 至多六次。试值不用自己的
均值根，不对其均值系数除法。

## 4. 点态 F 与真正归一的完整向量原函数

参考与试值使用同一个 $E(r)$。对各自的盒有
\[
 |a-1/\sqrt E|\le W^2 A_2,\qquad
 A_2=\frac{J_q^2/[c^2\beta(1+\beta)]+P J_t/(c\beta^3)}{v_-}
       +\frac{P^2}{\beta^2v_-\sqrt{E_-}(\sqrt{E_-}+v_-)}.          \tag{11}
\]
事实上 $r/b-1=(q/r)^2/[(b/r)(1+b/r)]$，且
$1/v-1/\sqrt E=(r^2p^2/b^2)/(v\sqrt E(\sqrt E+v))$。再用
$N=r/b+r^2pt/b^3$ 即得(11)。参考 $\langle a^0\rangle=1$；
因此实际 $F=\langle a^n-a^0\rangle$ 满足 $|F|\le W^2 F_2$，
$F_2=A_2^0+A_2^n$。这里无须对已付的全窗 $F$ 除以 $W(r)^2$，
也不把一次浮点响应相减当作准确系数差。

以下均为试值。记 $\mathcal A=\langle a\rangle\ge A_-=n_-/\sqrt{E_+}$，
$a_+=n_+/v_-$，$c_s=\pi/4,\ c_v=\pi/2$ 为 R648 的两个连续原函数范数；
$\Pi a,\Pi R,\Pi R_r$ 是 $\pi$ 周期标量，原平面向量 $\mathcal H,\mathcal H_r$
是 $\pi$ 反周期。可用 $p_a=c_sa_+$ 上界 $|\Pi a|$。记
\[
 K=\frac{r^2pB}{vb^3},\quad Q=\Pi R-(\Pi a)G/\mathcal A,\quad
 h_r=(K+\Pi R)/\mathcal A-(\Pi a)G/\mathcal A^2 .
\]
对 $K$ 可取 $K_2=m^2P B_+/(v_- b_-^3)$ 上界 $|K|/W^2$。
对 $Q,h_r,Q_r$ 的逐点系数依次取
\[
\begin{split}
 Q_2 &=c_sT_2+p_a T_2/A_-,\\
 h_2 &=(K_2+c_sT_2)/A_-+p_a T_2/A_-^2,\\
 Q_{r,2}&=c_sT_{2,r}+(K_2+c_sT_2)\bar G/A_-
        +p_a T_{2,r}/A_-+p_a\bar G T_2/A_-^2 ,
\end{split}                                                        \tag{12}
\]
其中 $\bar G=B_2^{\rm wt}(T_2)$。由 $K$ 奇、零均值及 $a_r=K_\theta+R$，
$(\Pi a)_r=K+\Pi R$，故(12)保留 $\mathcal A_r=G$ 导致的所有项。

为写明 $v_{\theta r}$ 的代价，定义以下非负界，仍按(1)吸收多出来的 $W$：
\[
\begin{split}
 V_{T,2}&=P J_q/b_-,\quad
 V_{T,r,2}=(Z_1J_q+P J_{r\theta})/b_-+P J_q B_b/b_-^2,\\
 V_{\theta,2}
 &= [m^2P J_{r\theta}/b_-^2+
              W_+^2m^2P^2 J_qJ_t/b_-^4]/v_-,\\
 K_{r,2}
 &= [2mP B_++m^2(Z_1 B_++P B_1)]/(v_-b_-^3)
       +K_2\{3B_b/b_-+B_2^{\rm wt}(V_2)/v_-\},\\
 K_{\theta,2}
 &=m^2[J_{r\theta}B_++P(J_{r\theta\theta}+J_t/c)]/(v_-b_-^3)
       +K_2[3W_+^2J_qJ_t/b_-^2+B_2^{\rm wt}(V_{\theta,2})/v_-].
\end{split}                                                        \tag{13}
\]
它们分别上界 $|v_T|,|(v_T)_r|,|v_\theta|,|K_r|,|K_\theta|$ 除以 $W^2$。
由 $v_\theta=av_T-bK$ 与 $a_r=K_\theta+R$ 得
\[
 V_{\theta r,2}=
 B_2^{\rm wt}(K_{\theta,2}+T_2)V_{T,2}+a_+ V_{T,r,2}
 +B_b K_2+m K_{r,2}\ \ge |v_{\theta r}|/W^2 .
\]
$N_r$ 的绝对界为
\[
 N_1=b_-^{-1}+m B_b/b_-^2+
 W_+^2[2mP J_t+m^2(Z_1J_t+P J_{r\theta\theta})]/b_-^3
       +3W_+^2m^2P J_t B_b/b_-^4 .                               \tag{14}
\]
这些式子均直接来自 R649 的实际速度、$K$、$N$ 的导数，在 $p=0$ 或
$B=0$ 也适用。

设 $\bar v_\theta=B_2^{\rm wt}(V_{\theta,2})$、
$\bar v_{\theta r}=B_2^{\rm wt}(V_{\theta r,2})$、
$\bar h=B_2^{\rm wt}(h_2)$、$d_{b,r}=B_b/A_-+m\bar G/A_-^2$。
将完整平面向量写为
$\mathcal H=H_T T+H_J JT$，其中
$H_T=(F/\mathcal A)N,\ H_J=(F/\mathcal A)v_\theta+(b/\mathcal A)Q$。
用 $T_r=h_rJT,(JT)_r=-h_rT$ 微分，得到
\[
\begin{split}
 H_{T,2}&=F_2 n_+/A_-,\qquad H_{J,2}=F_2\bar v_\theta/A_-+mQ_2/A_-,
 \qquad H_2=H_{T,2}+H_{J,2},\\
 H_{r,T,2}&=T_2 n_+/A_-^2+F_2N_1/A_-+\bar h H_{J,2},\\
 H_{r,J,2}&=T_2\bar v_\theta/A_-^2+F_2\bar v_{\theta r}/A_-+
          d_{b,r}Q_2+mQ_{r,2}/A_-+\bar h H_{T,2},\\
 H_{r,2}&=H_{r,T,2}+H_{r,J,2}.
\end{split}                                                        \tag{15}
\]
$\|\mathcal H\|\le W^2H_2$、$\|\mathcal H_r\|\le W^2H_{r,2}$ 是对同一
**原平面向量**的欧氏范数界。连续向量原函数作用于这整个向量。最后，
\[
 \boxed{\ |S|\le W^2 c_v H_2/\sqrt {E_-},\qquad
 |S_s|\le W^2c_v[H_{r,2}/E_-+
           B_2^{\rm wt}(e_1)H_2/(2E_-^2)]\ }.                      \tag{16}
\]
这里准确使用 $S_s=\Pi\mathcal H_r/E-E'\Pi\mathcal H/(2E^2)$。$(13)$至
$(16)$ 中最高六次来自 $G_r,\Pi R_r$，没有只因 $S$ 小就假设 $S_s$ 小。

## 5. 实际主曲率与真平帽接缝

取 $ds=\sqrt E\,dr$、$\chi=1/\sqrt E$。R649 的 $P_s$ 在此节表示真实高度
$Z_s=\chi p$ 的弧长导数；此前大写 $P$ 仅是 $|p|/W$ 的预算。实际弧长输入为
\[
 |(Z_s)_s|\le W\{Z_1/E_-+P B_2^{\rm wt}(e_1)/(2E_-^2)\},\qquad
 |(\chi v)_s|\le W^2\{V_2/E_-+e_1\sqrt{E_+}/(2E_-^2)\}.           \tag{17}
\]
$|Z_s|\le WP/\sqrt{E_-},\ |q_s|\le WJ_{r\theta}/\sqrt{E_-}$，
$|h|=|\chi h_r|\le W^2 h_2/\sqrt{E_-}$，$k=a/\mathcal A$ 用正盒
$[A_-/a_+,a_+/A_-]$。$S\cdot T,S\cdot n$ 以及 $S_s\cdot T,S_s\cdot n$
分别用(16)同一向量的范数包围。$\chi v$ 用正区间
$[v_-/\sqrt{E_+},\sqrt{E_+}/\sqrt{E_-}]$。

把这些真实区间、$q,t$ 及 $r\in[c,m]$ 代入 R649(9)–(19)，得到
真实 $\mathcal Q^2=U^2r^2+(Vq-Z_sb)^2$，其中
$U=\chi v+S\cdot n,\ V=-Z_s q/b+S\cdot T$。
若区间能将所需几何分母与零分开，即可用完整实际第二基本形式得到
两主曲率区间、$K_{\rm abs}$ 上界及 $bU$ 的平面 Jacobian 区间。
主导加速度 $(Z_s)_s=O(WP_3)$；水平径向加速度中的各项
$(\chi v_T)_s,(\chi v)_s,h,S_s$ 均为 $O(W^2P_6)$。曲率计算保留实际
缺陷和真实诱导度量。$\tau$ 若给定，$1-\tau K_{\rm abs}$ 只支付本尾曲率门；
R648 的同 $g$ 度量界另原样保留。

在 $r\downarrow c$，任一 $W^kP_d(u)$（$k>0$）趋零。参考
$\langle a^0\rangle=1$ 与(11)给 $E\to1$；同式和 $b\to c,v\to1,N\to1$
给 $\mathcal A\to1,k\to1,\Pi a\to0$。以 $n=(\cos\theta,\sin\theta)$、
$T=(-\sin\theta,\cos\theta)$ 表示端点旋转框架，式(16)(17)及
$Y=\Pi(bT)$ 给 $Y\to c n,\ X_s\to(n,0),\ X_\theta\to(cT,0)$。
由 R649 真二阶式 $X_{ss}\to0,\ X_{s\theta}\to(T,0),\
X_{\theta\theta}\to(-c n,0)$。这些极限全角一致，正是同一真实平帽
以其半径作弧长坐标时的二阶迹。原均值积分从 $c$ 起，角场与独立 mean 在
$c$ 全平，故高度值也匹配。于是对原源合同中的真实场，内侧接帽达到
$C^2$ 且两主曲率趋零。这里的平帽接缝是 $r=c$；外缘 $r=R$ 的竖直接柱
及主体几何仍需单独支付。

## 6. 实际接续范围

脚本 scripts/r650_complete_mean_true_tail_curvature_20261128.py 的入口
CompleteTrueTailCurvature(existing_R648).evaluate(response, paid_R643_receipt,
paid_R648_receipt) 只读真实现存对象和同一响应的原收据。它追加(2)–(17)
的代数，保留逐点多项式、来源、全部七类旧误差和累计开销，调用冻结 R649
的弧长形算子。若整窗盒的几何分母未分开，保留已证多项式和未闭原因。
整个接续没有新增 ODE、DtN、均值根、J、FFT、径向/角向样点或独立重复读出。

本证明不将原条件源转成无条件认证，也没有执行新的科学计算。实际 R643 沿原范围
继续。将来有同响应现存对象时才消费本条；主体误差、外核、全时嵌入、宏观变化和
同一固定 $g$ 的求解精化仍依赖各自的真实证据。
