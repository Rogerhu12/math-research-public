# R119 续篇：真实负型段的双端二维特征图、完整密度与源

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 对已经联立选定的实际无限参数
$\Gamma^*(a)$，每个内部负型分量都有一个真正的二维 $C^2$
微分同胚。它固定两端转向圆，把完整 raw Jacobi 方程的
principal 准确化为同一个预选径向参考型，保留真实正密度，
且没有引入额外零阶势。两端高度、conormal、完整 mean、
ordinary source 及弱散度源都有下面的准确变换公式。

这不是同宽解析相对小量结论。实际背景只有 $C^2$ 接缝；
把径向变量混入角变量后不能继续免费使用原解析角范数。
下文只主张真实 $C^2$ 图、分片光滑系数和明确的密度合同；
对完整尾的统一强范数与振幅相对逆不在本篇结论内。

## 1. 实际对象、固定参考和导数范围

使用
[全参数真实 return KAM](R119-supplement-joint-actual-negative-band-return-kam.md)
的整个标签域 $\|a\|_{\ell^1_{224}}<1/4$，以及其指标集
$$
 \mathcal I=\{(j,1):j\ge129\}\cup\{(j,2):j\ge130\}.
 \tag{G.1}
$$
本篇不把在 cut128 截断的最外分量补成虚构的两转向分量。
对一个 $i\in\mathcal I$，记真实固定端点为 $t_-<t_+$。
令
$$
 q(t)=\sqrt{-A_{\Gamma^*(a)}(t)},\qquad
 q_0(t)=\sqrt{-A_{\Gamma^0}(t)},\qquad
 S_0(t)=\int_{t_-}^tq_0(s)\,ds,\quad L_0=S_0(t_+).
 \tag{G.2}
$$
$\Gamma^0$ 是前篇 (K.27) 中一次选定的零标签参数，
$-2L_0=\omega_i/4$。它随后不随标签变化。
两个 $q$ 在端点邻域准确相同，因为所有度量参数都支撑在
严格负型的下降段内部。两端均为简单型别零点。

这里 $t$ 用原参考尾的 $\log r$ 加一个固定常数。
完整 connector 重调引起的整体物理尺度 $\rho(\Gamma)$
单独记在 $a_{\rm phys}(t)=\rho(\Gamma)e^t$ 中；不让固定
转向端点随一个记号选择移动。前篇已证明这个重调准确不改变
$\epsilon_{\rm tail}$ 和全部相对四态。

下面的图是在真实联立选择支 $\Gamma=\Gamma^*(a)$ 上构造的。
沿此支的标签导数包括所有 $\Gamma^*$ 的交叉导数。
不能把它解释为任意独立改变 $\Gamma$ 后仍保持同一个
Diophantine 目标。当在一个已选实际背景上使用 Jacobi 方程时，
则把图固定；Jacobi 高度及 source 可以是整个空间中的任意
元素，并不限于这个参数选择支的切向量。

## 2. 两个真实逆特征标签

仍用实际 hodograph 角 $\xi=\chi(t,\theta)$。其真实两支为
$$
 \frac{d\xi}{dt}=-b(t,\xi)\mp c(t)q(t),\qquad c(t)>0.
 \tag{G.3}
$$
记 $F_\pm(t)$ 为从 $t_-$ 出发的两支流，
$k(\eta)=h_i(4\eta)/4$ 为前篇求得的真实 KAM 圆周图。
它满足准确 lift 恒等式
$$
 F_-(t_+)^{-1}F_+(t_+)=k\circ T_{-2L_0}\circ k^{-1}.
 \tag{G.4}
$$
定义完整逆特征标签
$$
 \ell_\pm(t,\xi)=k^{-1}\!\left(F_\pm(t)^{-1}(\xi)\right),\qquad
 \Phi=\frac{\ell_++\ell_-}{2},\quad
 \Sigma=\frac{\ell_+-\ell_-}{2}.
 \tag{G.5}
$$
每个 $\ell_\pm$ 是 degree-one lift，且
$\ell_{\pm,\xi}>0$。因此 $\Phi$ 也是 degree-one lift，
$\Sigma$ 是真正的周期函数，不依赖 lift 的共同整数选择。

直接微分真实流，置 $\mathscr D=\partial_t-b\partial_\xi$，
得到
$$
 \mathscr D\ell_\pm=\pm cq\,\ell_{\pm,\xi},\qquad
 \mathscr D\Sigma=cq\,\Phi_\xi,\qquad
 \mathscr D\Phi=cq\,\Sigma_\xi.
 \tag{G.6}
$$
在左端 $\Sigma=0$。在右端，由 (G.4) 反演，
$k^{-1}F_+^{-1}=T_{2L_0}k^{-1}F_-^{-1}$，故
$$
 \Sigma(t_+,\xi)=L_0.                                    \tag{G.7}
$$
这是实际非径向两射线给出的准确常数，不是只匹配旋转数后
忽略一个非恒定边界函数。

沿共同漂移 $\dot\xi=-b$，(G.6) 给
$d\Sigma/dt=cq\Phi_\xi>0$。因此
$$
 0<\Sigma(t,\xi)<L_0\quad(t_-<t<t_+).                     \tag{G.8}
$$
所有实际无限尾依赖均在 $b,c,k$ 中保留。

## 3. 真正的二维图及全域一一性

在开负型段定义
$$
 T=S_0^{-1}(\Sigma),\qquad
 \Psi(t,\xi)=(T,\Phi).                                   \tag{G.9}
$$
因为 $q_0>0$，这不是形式的径向替换，而是一个已经有值域
保证的实际函数。令
$u=\Phi_\xi$、$v_1=\Sigma_\xi$。准确有
$$
 u^2-v_1^2=\ell_{+,\xi}\ell_{-,\xi}>0,
$$
$$
 J_\Psi=T_t\Phi_\xi-T_\xi\Phi_t
       =\frac{cq}{q_0(T)}
                    \ell_{+,\xi}\ell_{-,\xi}>0.
 \tag{G.10}
$$

全域一一性可以直接证明。先沿共同漂移以其左端角作坐标。
由 (G.8)，每个 $0<\sigma<L_0$ 的水平集 $\Sigma=\sigma$
恰与每条共同漂移线相交一次。这个水平集上的 $\Phi$ 导数，
按定向参数计算，因 (G.10) 严格为正。它又是 degree-one
圆周 map，所以是圆周微分同胚。因而每个
$(S_0(T),\Phi)$ 有唯一原像，且局部逆由正 Jacobian 给出。
这同时证明到整个开圆柱的满射性；没有从两个单独的偏导
正性误推二维一一性。

## 4. 两个转向端的 $3/2$ 因子与 $C^2$ 延伸

此节给出 (G.9) 在两个转向圆的真正延伸，尤其不直接把
$1/q_0(T)$ 当作有界量。

在左端写 $s=t-t_-$。由于端点位于未修改的 quintic 内部，
$$
 q(t)=q_0(t)=\sqrt{s}\,Q_-(s),\qquad Q_-(0)>0,
 \tag{G.11}
$$
其中 $Q_-$ 在一个真实邻域光滑。原四态方程的分母是
$J=1+K+EU$，不是 $A$；它在已付的小球中离0。因此在这个
光滑背景邻域，可以反复用原方程和角 Cauchy 估计取得任意
有限径向导数，每次只缩小一个正的角余宽。这对整个标签域的
局部全纯依赖同时成立。它不是对所有层宣称同一个未付的高阶
径向常数。

用 $\zeta=\sqrt{s}$，两支流的准确方程为
$$
 \frac{d\xi}{d\zeta}
   =-2\zeta\,b(t_-+\zeta^2,\xi)
      \mp2\zeta^2c(t_-+\zeta^2)Q_-(\zeta^2).
 \tag{G.12}
$$
这是 $\zeta=0$ 附近的光滑方程。把 $\zeta$ 换成 $-\zeta$
恰好交换两支。其逆流有相同奇偶性；再复合同一个 $k^{-1}$，
得到 $\Phi$ 为偶函数，$\Sigma$ 为奇函数。
两支在 $\zeta$ 的一次 jet 均为0，所以 $\Sigma$ 的第一个
可能非零奇次项是三次。光滑除法给
$$
 \Sigma=s^{3/2}B_-(s,\xi),\qquad
 S_0(t_-+s)=s^{3/2}B_{0,-}(s),
 \tag{G.13}
$$
且 $B_-,B_{0,-}$ 光滑、正。由 (G.6)，若
$H_-=k^{-1}$，则
$$
 B_-(0,\xi)=\frac23c_-Q_-(0)H_-'(\xi),\qquad
 B_{0,-}(0)=\frac23Q_-(0).                               \tag{G.14}
$$

于是令 $T=t_-+s\,g_-(s,\xi)$，(G.9) 等价于
$$
 g_-^{3/2}B_{0,-}(s g_-)=B_-(s,\xi).
 \tag{G.15}
$$
在 $s=0$，左侧对 $g_-$ 的导数严格为正；隐函数定理给
唯一正光滑 $g_-$。它与内侧已定义的逆相同。
这是对退化逆的实际消因子证明。

右端用 $s=t_+-t$，以准确公共右端标签
$$
 H_+(\xi)=\ell_+(t_+,\xi)-L_0
         =\ell_-(t_+,\xi)+L_0
$$
重复同一反向流论证，得到
$L_0-\Sigma=s^{3/2}B_+(s,\xi)$ 和
$T=t_+-s\,g_+(s,\xi)$。
两个端点均有准确 jet
$$
 \begin{aligned}
 T_t&=(c_\pm H_\pm')^{2/3}=:\gamma_\pm>0,&T_\xi&=0,\\
 \Phi_\xi&=H_\pm',&\Phi_t&=b_\pm H_\pm',\\
 J_\Psi&=c_\pm^{2/3}(H_\pm')^{5/3}>0.
 \end{aligned}                                         \tag{G.16}
$$
实际两端角图通常不同，均没有被置成恒等。

在其余径向接缝，$w_\Gamma$ 为 $C^2$，所以 $A_\Gamma$
为 $C^1$，$q$ 在严格负区为 $C^1$。真实流、$\Sigma,\Phi$
以及 $S_0$ 在这些位置为 $C^2$，而 $q_0$ 严格非零。
普通逆函数定理给同样的 $C^2$ 接合。因此 $\Psi$ 及其逆
是整个闭负型圆柱上的 $C^2$ 微分同胚。

## 5. 参数与标签导数经过退化逆时的完整项

在内部，任意两个沿联立选择支的方向 $u_1,u_2$ 满足
$$
 D T[u_1]=\frac{D\Sigma[u_1]}{q_0(T)},
$$
$$
 D^2T[u_1,u_2]
 =\frac{D^2\Sigma[u_1,u_2]
       -q_0'(T)DT[u_1]DT[u_2]}{q_0(T)}.
 \tag{G.17}
$$
所有 $\Sigma$ 导数都包括 $k,F_\pm,b,c,\Gamma^*$ 的真实
依赖；不能只微分一条标量参考相位。

在任一端点，(G.13)–(G.15) 表明
$D^r\Sigma=O(s^{3/2})$，$D^rT=O(s)$，对于每个固定有限
参数阶数 $r$ 成立。在二阶公式中，
$q_0'(T)DT[u_1]DT[u_2]=O(s^{3/2})$，所以整个分子按
相同阶消失。(G.15) 还直接给任意有限阶的参数导数，而无需
逐次把发散的 $q_0^{(r)}$ 分开估计。
例如边界径向 jet 的完整一阶参数导数是
$$
 D\gamma_\pm
 =\frac23\gamma_\pm
   \left(\frac{Dc_\pm}{c_\pm}
                 +\frac{D H_\pm'}{H_\pm'}\right).         \tag{G.18}
$$
实际 $H_+$ 的导数包括整个分量的两个真实流。

这里必须区别全域正则性。端点邻域和各光滑径向子段上有上述
任意有限阶参数公式；跨过仅 $C^2$ 的原参考接缝时，
$S_0^{-1}$ 只保证 $C^2$。因此全域可以直接主张：图依赖参数
连续取值于 $C^2$，一阶参数导数取值于 $C^1$，二阶参数导数
取值于 $C^0$，并具有 (G.17) 的真实值。
本篇不把这种分级正则性升级成全域解析角图或任意阶
$C^2$-值参数可微性。

## 6. 完整 raw 方程的实际 hodograph 密度

对一个固定的已选真实背景，使用
[实际正型两端 DN 篇](R119-supplement-actual-positive-band-two-end-dn-and-ordinary-source.md)
(P.1)–(P.7) 的完整 raw Jacobi 方程。虽然此处型别为负，
那些代数恒等式并不需要 $A>0$。写
$$
 E=1+w^2,\quad J=1+K+EU,\quad
 D=1-w^2(2K+K^2+EP^2),\quad
 d=\frac{E(V-P)}J,\quad v=\frac{\sqrt D}J,
$$
$$
 \operatorname{div}_{t,\theta}\left[
 \mu\begin{pmatrix}1&-d\\-d&d^2-v^2q^2\end{pmatrix}
                    \nabla h\right]=s_h,\qquad
 \mu=\frac{w}{a_{\rm phys}}JD^{-3/2},\quad
 s_h=w^2JD^{-3/2}e.
 \tag{G.19}
$$
这里 $h$ 是正参考高度扰动的 Jacobi 变化，北侧实际垂直
高度变化为 $-h$；这个共同号数沿用原合同。

实际 $\chi_\theta=c/v$、$b=d\chi_\theta-\chi_t$ 给
$$
 \widehat\mu=\frac{\mu}{\chi_\theta}
       =\frac{w/a_{\rm phys}}{cD},\qquad
 \widehat s=\frac{s_h}{\chi_\theta}
       =\frac{w^2}{cD}\,e
 \quad\text{均在 }\theta=\chi^{-1}(t,\xi)\text{ 求值}.
 \tag{G.20}
$$
在 $(t,\xi)$ 中，完整弱矩阵是
$$
 \widehat{\mathsf M}
 =\widehat\mu
     \begin{pmatrix}1&-b\\-b&b^2-c^2q^2\end{pmatrix}.
 \tag{G.21}
$$
特别有准确消去 $\widehat\mu c=(w/a_{\rm phys})D^{-1}$。
这不是只比较 principal 根而忽略真实密度。

## 7. 二维推送后的准确矩阵与普通源

令 $H=h\circ\chi^{-1}\circ\Psi^{-1}$。
一般正定向坐标变换的弱矩阵按
$D\Psi\,\widehat{\mathsf M}\,D\Psi^{T}/J_\Psi$ 推送。
由 (G.6)，
$$
 T_t-bT_\xi=\frac{cq}{q_0(T)}\Phi_\xi,\qquad
 \Phi_t-b\Phi_\xi=cq\Sigma_\xi.
$$
代入后交叉项准确为0；两条对角项分别是
$\widehat\mu cq/q_0(T)$ 与其乘 $-q_0(T)^2$。
所以完整方程为
$$
 \boxed{\quad
 \operatorname{div}_{T,\Phi}\left[
 \mu_{\rm eff}
       \begin{pmatrix}1&0\\0&A_0(T)\end{pmatrix}\nabla H
                         \right]=s_{\rm new},
 \qquad A_0=-q_0^2,
 \quad}                                                    \tag{G.22}
$$
$$
 \boxed{\quad
 \mu_{\rm eff}
 =\left[\frac{w/a_{\rm phys}}{D}
                    \frac{q}{q_0(T)}\right]\circ\Psi^{-1},
 \qquad
 s_{\rm new}
       =\left[\frac{\widehat s}{J_\Psi}\right]\circ\Psi^{-1}.
 \quad}                                                    \tag{G.23}
$$
没有额外高度权，故没有因改写未知量而产生的零阶势。
常高度 $H=1$ 仍是准确齐次解。

若需要归一到第二径向导数的 source，其准确值为
$$
 \frac{s_{\rm new}}{\mu_{\rm eff}}
 =\left[
  a_{\rm phys}w e\,
  \frac{q_0(T)^2}
       {c^2q^2\ell_{+,\xi}\ell_{-,\xi}}
                  \right]\circ\Psi^{-1}.                   \tag{G.24}
$$
因此 ordinary source 不是只把 $e$ 复合角图。
在任一转向端，该因子有有限严格正极限：
$$
 \left.\frac{s_{\rm new}}{\mu_{\rm eff}}\right|_\pm
  =\left.\frac{a_{\rm phys}w\,e}
                     {(c_\pm H_\pm')^{4/3}}\right|_\pm.
 \tag{G.25}
$$
(G.13) 给 $q/q_0(T)\to(c_\pm H_\pm')^{-1/3}$，
所以 $\mu_{\rm eff}$ 本身也有限、正，并具有完整端点 jet。

记从原物理角到 $(T,\Phi)$ 的总图为 $\Xi$，
$J_\Xi=\chi_\theta J_\Psi$。准确有
$$
 \int s_{\rm new}\,dT\,d\Phi=\int s_h\,dt\,d\theta,\qquad
 \int (J_\Xi\circ\Xi^{-1})|s_{\rm new}|^2\,dT\,d\Phi
       =\int |s_h|^2\,dt\,d\theta.                          \tag{G.26}
$$
后一式给明确的全部频率加权 $L^2$ source 合同。
对每个有限真实分量，$J_\Xi$ 正且连续，所以它也给通常
$L^2$ 的有限常数等价；本篇未把这些有限常数直接取全层上确界。

## 8. 两端完整迹、通量密度和 normal/shear 恢复

在任一端，令
$$
 \theta=K_\pm(\Phi)
       :=\chi_\pm^{-1}\!\left(H_\pm^{-1}(\Phi)\right).
 \tag{G.27}
$$
这里 $H_\pm$ 是 (G.14)、(G.16) 的真实端角图。
原 raw 通量
$p_h=\mu(h_t-dh_\theta)$ 沿正 $t$ 定向，
新通量 $p_{\rm new}=\mu_{\rm eff}H_T$ 沿正 $T$ 定向。
由 (G.16) 和 (G.20)，准确得到
$$
 f_{\rm new}=f_h\circ K_\pm,\qquad
 p_{\rm new}=K_\pm'\,(p_h\circ K_\pm).
 \tag{G.28}
$$
左右端的外法向号分别为负、正；(G.28) 对两个号一致成立。
因此完整双端 Green pairing 和 flux mean 都被保存：
$$
 \int f_{\rm new}p_{\rm new}\,d\Phi
    =\int f_hp_h\,d\theta,\qquad
 \langle p_{\rm new}\rangle=\langle p_h\rangle=\dot M.
 \tag{G.29}
$$
高度 mean 则是
$\langle f_h\rangle=\langle K_\pm'f_{\rm new}\rangle$；
两个高度平均不能同时被任意清零。

两端的全部原 raw 一阶 jet 可以直接恢复。若
$\mathfrak j_\pm=\chi_\theta H_\pm'$，则
$$
 h_\theta=\mathfrak j_\pm H_\Phi,\qquad
 h_t=\gamma_\pm H_T+d\,\mathfrak j_\pm H_\Phi,
$$
$$
 \dot P=\frac{\mathfrak j_\pm H_\Phi}{a_{\rm phys}w},
 \qquad
 \dot K=\frac{\gamma_\pm H_T+
                  d\,\mathfrak j_\pm H_\Phi}{a_{\rm phys}w}.
 \tag{G.30}
$$
它们保留两个分量以及原 mean root。原 grounded 高度、
normal/shear、水平重建应从这些真实 jet 按原几何公式恢复；
本篇不把 $p_h$ 改名为 grounded 通量。因为原 jet 完整可逆，
这个变换没有删掉 normal/shear 所需的任何分量。

在两端合起来写 $T_Kf=(f_-\circ K_-,f_+\circ K_+)$、
$C_Kp=(K_-'p_-\circ K_-,K_+'p_+\circ K_+)$。
若一个已证双端 DN 算子为 $\Lambda$，准确传输是
$$
 \Lambda_{\rm new}=C_K\Lambda T_K^{-1}.                    \tag{G.31}
$$
尤其相邻正型段的完整 $2\times2$ 端口矩阵必须整体传输，
不能删除其非对角项，也不能把传输后的算子换回旧对角 Fourier
乘子而不再付费用。

## 9. 弱散度源及移动坐标的完整参数列

更一般地，若原 source 是 $f+\operatorname{div}Z$，
总坐标变换给准确 Piola 公式
$$
 f_{\rm new}=(f/J_\Xi)\circ\Xi^{-1},\qquad
 Z_{\rm new}=(D\Xi\,Z/J_\Xi)\circ\Xi^{-1},
$$
$$
 \operatorname{div}Z_{\rm new}
          =(\operatorname{div}Z/J_\Xi)\circ\Xi^{-1}.
 \tag{G.32}
$$
它可由对任意紧支撑试验函数换元直接证明，故对真实弱源也
成立。参数改变弱矩阵时产生的
$-\operatorname{div}((\delta\mathsf M)\nabla h)$
因此仍有一个准确源列，并没有因主型被共轭而消失。

若还微分图本身，定义真实变形场
$$
 V_u=(D\Xi)^{-1}D\Xi[u].
$$
对高度和 scalar 密度有
$$
 D(h\circ\Xi^{-1})[u]
   =(Dh[u]-V_u\cdot\nabla h)\circ\Xi^{-1},
$$
$$
 D\bigl[(f/J_\Xi)\circ\Xi^{-1}\bigr][u]
   =\left[\frac{Df[u]-\operatorname{div}(fV_u)}
                         {J_\Xi}\right]\circ\Xi^{-1}.
 \tag{G.33}
$$
证明使用
$D\log J_\Xi[u]=\operatorname{div}V_u+
V_u\cdot\nabla\log J_\Xi$。这些式子给出完整参数源，
不能只对 (G.23) 的显式 $w$ 微分。
二阶导数由对 (G.33) 再应用同一个规则取得，
包括 $DV_u$ 和全部交叉输运项。
在两个固定转向圆，$V_u$ 的径向分量为0，所以 (G.33)
没有隐藏的径向移动边界源；角边界的周期项积分为0。

完整目标族的物理缩放改变另有已经证明的
$$
 \delta w^{\rm phys}
 =w_\Gamma\left(\sum_i\psi_i\delta\gamma_i
                                  +A_\Gamma\delta\ell\right).
 \tag{G.34}
$$
在固定物理 $a$ 使用源列时必须保留第二项和 mean 高度的
移动切口项。它们是度量变化列，不能自动称为固定度量的
齐次 Jacobi 列，也不能由 (G.32) 自动断言已满足某个强
source 空间的统一估计。

## 10. 精确剩余密度算子与未支付的统一费用

为说明接下来真正还缺什么，取同一当前物理尺度上的径向比较
密度
$$
 \mu_0(T)=\frac{w_{\Gamma^0}(T)}{\rho(\Gamma)e^T},\qquad
 \mathcal R(T,\Phi)=\frac{\mu_{\rm eff}(T,\Phi)}{\mu_0(T)}.
 \tag{G.35}
$$
这只是参考算子的一次常数尺度选择，不改变最终实际目标。
因 $(\log\mu_0)_T=A_0-1$，若
$z=H_\Phi$、$v_2=H_T$，(G.22) 准确为
$$
 \begin{pmatrix}z\\v_2\end{pmatrix}_T
 =
 \begin{pmatrix}0&1\\-A_0&0\end{pmatrix}
 \begin{pmatrix}z\\v_2\end{pmatrix}_\Phi
 +\begin{pmatrix}
 0&0\\
 -A_0(\log\mathcal R)_\Phi&
       -(A_0-1)-(\log\mathcal R)_T
 \end{pmatrix}\begin{pmatrix}z\\v_2\end{pmatrix}
 +\begin{pmatrix}0\\s_{\rm new}/\mu_{\rm eff}\end{pmatrix}.
 \tag{G.36}
$$
下左项仍有准确 $A_0$ 因子。全部两端振幅问题因此可以被
准确定位为这个密度算子、完整 source 和边界变换的共同
估计，而不只是一个圆周旋转问题。

但本篇不声称
$\int\|(\log\mathcal R)_T\|$ 或对应 Airy 权费用很小。
两个具体原因不能略过：

1. 原 log-quintic 和新 bump 只有指定的有限接缝正则性。
   真实 $T(t,\xi)$ 混合径向与角变量；一个仅 $C^2$ 的径向
   接缝可能变成角向曲线。于是原来每个固定 $t$ 上的解析
   角带，不能从 (G.9) 免费传给 (G.35)。
2. 在下降段 $q_0^2=7+\Lambda S'(x)$、$\Lambda\to\infty$。
   坡肩 $x\asymp\Lambda^{-1/2}$ 的径向宽为
   $\eta/\sqrt\Lambda$。仅有一个绝对小的 $T-t$ 或
   $k'-1$，不足以证明跨越这些坡肩的
   $q(t)/q_0(T)$ 是统一相对小量。不能用未付的径向
   Lipschitz 常数把它补出来。

因此后续的完整振幅/高输入相对逆，应继续保原径向 $t$，
在两支真实特征角图中支付幅度与坡肩费用，或另证足够强的
实际加权密度定理。前篇的全频 KAM 和本篇的准确双端图，
都不替代这个剩余算子结论。

[代数与端点核验程序](../scripts/fourfold_two_ended_characteristic_chart_20261113.py)
及其
[实际依赖报告](../notes/2026-11-13-R119-two-ended-characteristic-chart-budget.json)
保存可重跑的完整恒等式。程序不把符号核验当作一个未证明的
全层强范数估计。
