# R648：真实自由均值的完整内尾 G、归一位置 S 与度量界

2026-11-28，Astra-new-mechanism-8cdb3418-20261128。

本稿补 [R643](R643-fixed-metric-unsolved-mean-height-and-periodic-position-system.md)
实际新系统仍未支付的一个具体量：从真平帽一直到原数值口，保留真实 mean
未知量时的完整连续连接残差 G 和位置缺陷 S。这里不移动口、不截断任何真尾，
也不要求 trial 满足原 lambda 盒或对 trial 除以均值系数。

所用固定 seed 仍是 run46117718197 的真实 accepted1473 响应，
其逐字响应 SHA256 为
`19519575f7b4a8100cf9813851c258188ad4a0063edad05eb1b5b332b83f2cc7`。
它的已经支付的同一连续均值分支及所有原源误差继承原记录；本稿只在该固定
seed 的导数界中使用它自己的非零分母。新 trial 的 mean 保持自由。

## 1. 对象与仅在固定 seed 上使用的已付输入

沿原真实内尾取

\[
r_c=11/50,\quad\ell=1/5,\quad A_W=4/5,\quad
u=\ell/(r-r_c),\quad
W=A_W e^{-u(2-\sin u)},\quad r_c<r\le r_m,\quad
U=\ell/(r_m-r_c)\ge108.
\tag{1}
\]

为避免与几何速度混淆，本稿只在 (1)–(3) 中用 u 表示尾坐标；后面几何速度写 v。
实际 R643 的口仍为原 `r_m=.22184543511708774`，不是新指定的有利边界。
以下所有界都覆盖整个 (1) 及全部角，而非只覆盖有限采样点。

直接微分得

\[
|W'|\le W L(u),\qquad L(u)=\frac{u^3+3u^2}{\ell}.
\tag{2}
\]

各单项 \(u^ke^{-2u}\) 在 \(u\ge108\)、\(k\le3\) 上递减，因而

\[
W_+=A_We^{-U},\qquad
\mathfrak w_2=A_W^2e^{-2U},\qquad
\mathfrak w_1=\frac{A_W^2}{\ell}(U^3+3U^2)e^{-2U}
\tag{3}
\]

分别上界 W、W²、W|W'|。没有对无界的 W'/W 单独取有限全尾上界。

固定 E=E*(r) 是同一原参考高度 f* 在 p*=-W+f*_r 上的连续 turning 根。
使用原已付源合同的 \(0<E_-\le E\le E_+\)，原范围为 [.99,1.01]。
固定 seed 的真实 mean 斜率记 s*，已付原分支给

\[
|s_*|\le\lambda_*W,\qquad
|\langle\omega_*C_*\rangle|\ge\kappa_*W,\qquad
\lambda_*\ge0,\quad\kappa_*>0.
\tag{4}
\]

这里 \(\lambda_*\) 消费原输出的 `lambda_radius_upper`，\(\kappa_*\)
消费同一原输出的 `kappa`。原数值上界约为 6.5631e−198、下界约为 .78159；
实际区间消费者保留完整向外区间，不以本行近似值代替。

固定 seed 的 (4) 是已经存在的唯一对象的性质。它不对新 trial 的 mean
施加盒，也不被借作 trial Jacobian 的逆。对固定 seed 求导的使用范围将在
第 4 节准确限定。

对任一场 f 记五个非负全尾常数

\[
J=(J_r,J_q,J_t,J_{rr},J_{r\theta}),\quad
\frac{(|f_r|,|f_\theta|,|f_{\theta\theta}|,
|f_{rr}|,|f_{r\theta}|)}{W}\le J.
\tag{5}
\]

参考、固定 seed 的角向高度、新 trial 的角向高度分别记 \(J^0,J^s,J^n\)。
这里 seed/trial 的角向高度都包括同一个参考 f* 及它们的全部实际响应。
新 trial 为

\[
p=-W+s_*+m'+f_r,\qquad
p_r=-W'+s_*'+m''+f_{rr},
\qquad |m'|/W\le M_1,\quad |m''|/W\le M_2.
\tag{6}
\]

R643 的完整 94 条 mean 中，90 条在这个真实尾上因原支持准确为零；
另四条 Gaussian 的所有实际系数给 M1、M2，不许丢弃任何非零小尾。
mean 的核心迹 lift 也在这里准确为零。m 的值和真帽积分继续使用原消费者。

## 2. 一个可复用的正域盒

给定 J 和 \(|p|/W\le P\)，定义

\[
\begin{split}
\beta^2&=1-(W_+J_q/r_c)^2,\\
v_-^2&=E_--W_+^2P^2/\beta^2,\\
n_-&=1-W_+^2PJ_t/(r_c\beta^3),\\
n_+&=\beta^{-1}+W_+^2PJ_t/(r_c\beta^3),\\
c_+&=E_+J_t+r_mP,\qquad
d_+=J_{r\theta}+J_q/r_c,\\
m_+&=r_m+W_+^2(PJ_t+J_q^2/r_c),\\
m_-&=r_c-W_+^2(PJ_t+J_q^2/r_c),\\
\Omega_+&=(v_-^3r_c\beta^3)^{-1},\qquad
\Omega_-=(r_mE_+^{3/2})^{-1}.
\end{split}
\tag{7}
\]

本节的必要正条件为 \(\beta^2,v_-^2,n_->0\)；第 3 节参考盒另要求
\(m_->0\)。保持 R643 的准确定义

\[
\begin{gathered}
q=f_\theta,\quad t=f_{\theta\theta},\quad b^2=r^2-q^2,
\quad v^2=E-r^2p^2/b^2,\\
N=r/b+r^2pt/b^3,\quad a=N/v,\quad
C=Et+rp,\quad B=f_{r\theta}-q/r,\\
M=r+pt-q^2/r,\quad\omega=r^2/(v^3b^3),\quad
R=\omega(Cp_r-EB^2-E'M/2).
\end{gathered}
\tag{8}
\]

逐项得到

\[
\begin{gathered}
r\beta\le b\le r,\quad v_-\le v\le\sqrt{E_+},\quad
n_-\le N\le n_+,\quad
\Omega_-\le\omega\le\Omega_+,\\
|C|\le Wc_+,\quad |B|\le Wd_+,\quad
|M|\le m_+,\quad M\ge m_-.
\end{gathered}
\tag{9}
\]

三个盒分别使用
\(P_0=1+J^0_r\)、\(P_s=1+\lambda_*+J^s_r\)、
\(P_n=1+\lambda_*+M_1+J^n_r\)。所有记号的上标对应其自己的盒，
不能将原小 seed 的速度下界直接贴到新 trial。

## 3. 同一冻结 E 的真实导数界

参考场准确满足 \(\langle a^0\rangle=1\)。由 R643 的完整身份
\(a_r=K_\theta+R\)，微分该同一个参考根得

\[
0=\langle R^0\rangle
=\left\langle\omega^0\{C^0(-W'+f^*_{rr})-E(B^0)^2-E'M^0/2\}\right\rangle.
\tag{10}
\]

周期项的平均为零；这里没有重新选择 E。参考盒的 m0−>0 给
\(\langle\omega^0M^0\rangle\ge\Omega^0_-m^0_->0\)。所以

\[
|E'|\le d_1W|W'|+d_0W^2,
\tag{11}
\]

其中

\[
D_0=\frac{2\Omega^0_+}{\Omega^0_-m^0_-},\qquad
d_1=D_0c^0_+,\qquad
d_0=D_0(c^0_+J^0_{rr}+E_+(d^0_+)^2).
\tag{12}
\]

本界故意保留 W 与 W' 的组合。若先把 E' 换成一个绝对常数再去除
W(r)，会在 r↓rc 处失去有限界；(11) 避免了这个错误。
M 与 N 还准确满足 \(r^2M/b^3=N\)，所以 (10) 中的分母就是参考
turning 对 E 的严格正权，不是一个额外未知分支条件。

## 4. 只对真实固定 seed 支付 s*'，不消去新 mean

固定 seed 的连续 turning 也准确为一。对它求导后

\[
\langle\omega^sC^s\rangle s_*'
=-\left\langle\omega^s\{C^s(-W'+f^s_{rr})
                         -E(B^s)^2-E'M^s/2\}\right\rangle.
\tag{13}
\]

仅在 (13) 使用已付 (4)。将 (11) 保持在其点态组合形式，才可约去共同
W 并得到

\[
|s_*'|\le s_1|W'|+s_0W,
\tag{14}
\]

\[
\begin{split}
s_1&=\frac{\Omega^s_+}{\kappa_*}
          (c^s_++m^s_+d_1/2),\\
s_0&=\frac{\Omega^s_+}{\kappa_*}
          (c^s_+J^s_{rr}+E_+(d^s_+)^2+m^s_+d_0/2).
\end{split}
\tag{15}
\]

这可以比真实 seed 导数宽得多，但保持全尾有限并足以服务后面的量。
它没有改变 s* 的定义，也没有对新 trial 的 s*+m' 解任何根。
即使新 trial 的均值系数为零，后面的式子也照常适用。

## 5. 新 trial 的全部 R 与 G

由 (6)、(14) 得

\[
|p_r|\le(1+s_1)|W'|+WJ_2,
\qquad J_2=s_0+M_2+J^n_{rr}.
\tag{16}
\]

将其与 (11) 代入 (8)，完整的离解项均保留，得到

\[
\boxed{|R(r,\theta)|\le R_1W(r)|W'(r)|+R_0W(r)^2,}
\tag{17}
\]

\[
\begin{split}
R_1&=\Omega^n_+\{c^n_+(1+s_1)+m^n_+d_1/2\},\\
R_0&=\Omega^n_+\{c^n_+J_2+E_+(d^n_+)^2+m^n_+d_0/2\}.
\end{split}
\tag{18}
\]

故整个真实尾上可以直接取

\[
\boxed{R_+=R_1\mathfrak w_1+R_0\mathfrak w_2,
\qquad \|G\|_\infty=\|\langle R\rangle\|_\infty\le R_+.}
\tag{19}
\]

这不是用某个有限口上的 G 推断尾内值，也没有把 R 的任一常量或
非零角模删除。当前旧源误差若未包围，(17)–(19) 仍明确是对相应准确源
合同的条件结论，不能把这个条件静默删掉。

## 6. 完整归一周期位置 S，包括 F、G 两类项

令 \(\Pi_L\) 为 L 周期函数的零均值周期 primitive：
\((\Pi_L f)'=f-\langle f\rangle\)。其锯齿卷积核在 (0,L) 上为
\(1/2-x/L\)，故

\[
\|\Pi_L f\|_\infty\le (L/4)\|f\|_\infty.
\tag{20}
\]

对向量值也成立，因为卷积后欧氏范数可用核绝对值积分估计。
R643 的 a、R 都准确 π 周期；其使用的 2π 规范零均值 primitive
与 π 周期 primitive 相同。因此这两项可用 \(c_s=\pi/4\)。
下面的向量 H 为反 π 周期，完整周期为 2π，使用 \(c_v=\pi/2\)。
本证明不用 finite FFT 的离散算子范数替代这两个连续范数。

保持 R643 的符号

\[
\mathcal A=\langle a\rangle,\quad F=\mathcal A-1,\quad
Q=\Pi R-(\Pi a)G/\mathcal A,
\]
\[
\mathcal H=\frac F{\mathcal A}(NT+v_\theta JT)
                  +\frac b{\mathcal A}QJT,
\qquad S=\Pi\mathcal H/\sqrt E.
\tag{21}
\]

设原 R643 同一 tail 消费者已经给全尾 \(|F|\le F_+\)。其界来自
同一固定 seed 的零 F、实际全部角响应差及四条实际 mean Gaussian 的
完整 Lipschitz 线积分；本稿直接消费这个已付量，不重跑旧 mean 门。
由正域盒总有

\[
\mathcal A\ge A_-:=n^n_-/\sqrt{E_+}>0,
\qquad \|a\|_\infty\le a_+:=n^n_+/v^n_-.
\tag{22}
\]

直接微分 (8) 中的 v²，保留角向 mean 为常数的事实，得

\[
v_\theta=-\frac{r^2p f_{r\theta}}{vb^2}
          -\frac{r^2p^2qt}{vb^4}.
\]

因此

\[
V_\theta:=\frac{W_+^2P_nJ^n_{r\theta}}{v^n_-\beta_n^2}
 +\frac{W_+^4P_n^2J^n_qJ^n_t}{v^n_-r_c^2\beta_n^4}
\tag{23}
\]

上界其全部角和径向点的绝对值。由 (19)–(23)，

\[
\begin{split}
Q_+&=c_sR_+(1+a_+/A_-),\\
H_+&=\frac{F_+}{A_-}(n^n_++V_\theta)
                        +\frac{r_m}{A_-}Q_+,\\
\boxed{S_+}&\boxed{=\frac{c_vH_+}{\sqrt{E_-}}.}
\end{split}
\tag{24}
\]

这里 F 的两项与 G 的相位项全部进入；没有把 R643 的离解场错误简化成
只含两次 primitive 的旧 A=1 场。所有新 trial 分母只有正几何量和
准确正 turning 归一量。

## 7. 同一连续位置的度量与平面 Jacobian 消费

R643 已证的连续身份为
\(Y_\theta=bT\)、\(Y_r=V T-vJT+\sqrt E S\)，其中
\(V=-pq/b\)。未添 S 时的向量满足 \(V^2+v^2=E-p^2\le E\)。
因此真实诱导度量相对固定 \(g=Edr^2+r^2d\theta^2\)，在其正交单位标架中
有误差矩阵

\[
\begin{pmatrix}
2S\cdot(VT-vJT)/\sqrt E+|S|^2 & (b/r)S\cdot T\\
(b/r)S\cdot T&0
\end{pmatrix}.
\tag{25}
\]

所以最大相对二次型误差可用安全上界

\[
\boxed{\eta_{\rm tail}\le3S_++S_+^2.}
\tag{26}
\]

同一真实连续位置还有

\[
\det(Y_r,Y_\theta)
=b\{v+(\sqrt E S)\cdot(-JT)\}
\ge b(v^n_--\sqrt{E_+}S_+).
\tag{27}
\]

若末括号严格为正，就支付 R645 所需的这个真实尾上的局部平面正 Jacobian。
这并不支付身体、核心接缝或全连续主曲率；也没有把有限差分或有限 FFT
的某个 identity 数组赋予 (25)–(27) 的准确导数资格。

## 8. 实际旧 reference 的 rr、rθ 预算，没有遗漏 pre-tanh 与 forced

旧完整尾证明已经对每条真无限 germ 付出
\(\max_{0\le i\le2}|S_j^{(i)}|/W\le C_j\)，\(2\le j\le32\)。
所以原十条响应的 rr 与 rθ 贡献直接为
\(|a_j|C_j\)、\(j|a_j|C_j\)。每条 Gaussian 的已付三 radial jet
\((K_0,K_1,K_2)\) 则给 rr 为 \(|a|K_2\)、rθ 为 \(j|a|K_1\)。

原 reference 的正包络为

\[
\mathcal B=\frac{\sum_{j=2,4,6,8}(S_j/m_j)^2+
 e^{-\gamma/(r-r_c)^4}(R-r)^p}{C_*},
\quad\gamma=10^{-4},\quad p=2+2\alpha.
\tag{28}
\]

原已付 B0、B1 分别上界 \(|\mathcal B|/W,|\mathcal B'|/W\)。
记 \(d_-=R-r_m\)、
\(G_0=A_W^{-1}e^{-\gamma U^4/\ell^4+3U}\)，则

\[
G_2=\left[
 (4\gamma U^5/\ell^5+p/d_-)^2
 +20\gamma U^6/\ell^6+p/d_-^2\right]G_0,
\]
\[
B_2=\frac{4W_+\sum(C_j/m_j)^2+G_2}{C_*}
\tag{29}
\]

上界 \(|\mathcal B''|/W\)，条件为
\(10/U-4\gamma U^3/\ell^4+3<0\)。这个条件保证 (29) 所有至多十次幂
与 quartic 指数的乘积在全无限 u 范围递减；不用把 G0 的数值 underflow 当零。

对原五次 B 样条 \(\psi_i\)，P_i=1，Q_i 为原一阶界，二阶界使用

\[
\begin{split}
Q_{i,2}={}&\frac5{t_{i+5}-t_i}
 \left(\frac4{t_{i+4}-t_i}+\frac4{t_{i+5}-t_{i+1}}\right)\\
&+\frac5{t_{i+6}-t_{i+1}}
 \left(\frac4{t_{i+5}-t_{i+1}}+\frac4{t_{i+6}-t_{i+2}}\right).
\end{split}
\tag{30}
\]

重复 knots 的零分母项按真实 B 样条递推省略；当某个外系数分母为零时，
该整个外项为零。原四条 local-extra 在尾内因其支持恰为零，仍计入完整列表。
对 \(v_j=a_jS_j+\mathcal B\sum_i b_{ji}\psi_i\)，取

\[
\begin{split}
V_{j,0}&=|a_j|C_j+B_0\sum_i|b_{ji}|P_i,\\
V_{j,1}&=|a_j|C_j+\sum_i|b_{ji}|(B_1P_i+B_0Q_i),\\
V_{j,2}&=|a_j|C_j+\sum_i|b_{ji}|
                         (B_2P_i+2B_1Q_i+B_0Q_{i,2}).
\end{split}
\tag{31}
\]

记 Vr=ΣVj,1、Vrr=ΣVj,2、Vq=ΣjVj,0、Vrθ=ΣjVj,1。
对原 \(\sigma\tanh(V/\sigma)\)，\(|F'|\le1,|F''|\le2/\sigma\)，故

\[
J^{\rm pre}_{rr}=2\{V_{rr}+2W_+V_r^2/\sigma\},\qquad
J^{\rm pre}_{r\theta}=V_{r\theta}+2W_+V_rV_q/\sigma.
\tag{32}
\]

第一式前因子 2 正是原 canonical512 均值同步扣除的完整代价；第二式的
角微分消去该均值。没有把 canonical512 改成另一种平均。
再加原 reference 的全部 post 系数与原固定 forced-j4 的完整
`amplitude² × coefficient × tail_multiplier / scale`，后者用 raw germ 的
同一 C4 界而不误除核心归一，便得到 (5) 所需的完整 J0rr、J0rθ。

## 9. 实现与实际消费范围

后继纯源码 `scripts/r648_complete_mean_true_tail_connection_20261128.py`
从同一已经存在的 R643 tail 对象与该实际响应已付的 tail receipt 读入
全部原归一、原 literal q/knots、真实种子及其合同。它只新增 (29)–(32)
尚未付的第二 jet 求和与 (7)–(27) 的向外区间算式；不求 DtN、ODE、
mean 根、完整 J、FFT 或新位置样点。

它严格保留原七类源误差。如果这些误差仍未被包围，输出只标为同一准确
源合同下的连续尾条件界。该实现不改变已冻结并正在运行的 R643 科学源；
后续同态读取可直接在已有 model/tail/receipt 仍在内存时消费，不为此重建
已付科学对象。没有为它另开一个重复核验范围。

本稿实际闭合的是新 mean 系统整个内尾的 G、完整离解 S 和相应同 g 度量
误差的数学上界，以及全尾平面 Jacobian 的可计算充分条件。
身体求根、真实连续原源误差、核心接缝、主曲率和宏观门继续按原对象支付。
