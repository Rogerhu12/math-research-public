# R753　固定帽姿时两条材料轴的局部精确闭合与真实曲率门

设 $a=.075,\ b=.22,\ \sin\vartheta=.27,\ \cos\vartheta>0$。使用同一材料 $g=E(r)dr^2+r^2d\varphi^2$、完整材料角、已给两帽以及中心 $(C_x,0,C_z)$。下文的两条轴分别是 $\varphi=0,\pi$。给定高度为实反射偶周期函数，$s^2=1-|\nabla_g u|^2>0$。在固定帽有 $E(a)=E(b)=1$，内帽高度三径迹为 $(C_z-a\sin\vartheta\cos\varphi,-\sin\vartheta\cos\varphi,0)$，外帽三径迹全零。所有位置、方向和长度沿用真正材料标记。[R748](R748-single-height-periodic-development-and-complete-two-cap-geometry.md)；[R749](R749-two-cap-Volterra-defects-and-reflection-axis-anchors.md)。

## 全反射偶角空间内的两个独立轴

令 $x=\cos\varphi,\ z_+(r)=u(r,0),\ z_-(r)=u(r,\pi)$。对每个 $K\ge2$，次数不超过 $K$ 的实偶 Fourier 空间恰好由下式一一参数化：

$$
 u=\frac{1+x}{2}z_++\frac{1-x}{2}z_-+(1-x^2)Q(r,x),
 \qquad \deg_x Q\le K-2 .
$$

确实 $\cos(k\varphi)=T_k(x)$，从原多项式减去两端线性插值即被 $1-x^2$ 整除。逆映射取两个端值并作同一除法。此为常数线性坐标变换，保留每个系数的原径向函数空间及共同结迹；未假设半周反号。若原来允许独立正弦模而不强制反射偶性，则不在本文机制内。

记 $p_j=z_j'$, $A_j=\sqrt{E-p_j^2}$ 和 $L_j=\int_a^b A_j\,dr$。R749 的两个目标为

$$
 L_+^*=b-a\cos\vartheta-C_x,\qquad L_-^*=b-a\cos\vartheta+C_x .
$$

在已经具有该 $C_z$ 真迹的某一 $u$ 上取

$$
 u_t=u+\tfrac12(1+x)t_+h_+(r)+\tfrac12(1-x)t_-h_-(r).
$$

两轴新长度分别只含 $t_+$、$t_-$。$Q$ 原样自由。若 $h_j,h_j',h_j''$ 在两端均为零，则两端原高度、径向和全部混合二阶迹不变。首次给定 $C_z$ 或改变 $C_z$ 时要先施加具有相应内端三迹的真实 lift，并为得到的 $u$ 重付下文的正图、两轴和残差；这两个方向自身保持 $C_z$ 不动。

在连续径向空间总可构造横截方向。令 $g_j=p_j/A_j$，$w>0$ 于开区间，$w=w'=0$ 于两端，$\bar g_j=\int wg_j/\int w$。取 $h_j(a)=0,\ h_j'=-w(g_j-\bar g_j)$。则 $h_j(b)=0$，两端的 $h_j',h_j''$ 为零，且

$$
 L_j'(0)=-\int_a^b g_j h_j'\,dr
         =\int_a^b w(g_j-\bar g_j)^2\,dr>0.
$$

严格性来自 $g_\pm(a)=\mp\tan\vartheta,\ g_\pm(b)=0$ 与连续性。此处 $'$ 对 $L_j$ 表示本轴幅度导数。此构造所给 $h_j$ 若超出指定径向离散空间，则用下述原结构造或如实另报扩空间。

## 原五次样条上可付费的半径

在原真结中选 $a<r_I\le r_O<b$，带宽 $\ell_I=r_I-a,\ \ell_O=b-r_O$。令 $S(y)=10y^3-15y^4+6y^5$ 于 $[0,1]$，两侧以 0、1 常值延伸。取

$$
 h_+=S((r-a)/\ell_I)-S((r-r_O)/\ell_O),\qquad h_-=-h_+ .
$$

这两个径向方向在同一分片五次 $C^2$ 样条空间，原结只须持有相应的 $(h_j,h_j',h_j'')$。原 cosine 模 $0,1$ 的增量分别为 $(t_+h_++t_-h_-)/2,(t_+h_+-t_-h_-)/2$，高模保持自由。稀疏径向子空间若缺这两个方向，须验证方向属于该空间或声明插结、增加方向。$\int_0^1 S'=1,\ \|S'\|_\infty=15/8,\ \int_0^1(S')^2=10/7$。令 $\langle g\rangle_I,\langle g\rangle_O$ 是各带按缩放的 $S'$ 概率权取均，则

$$
 L_+'(0)=\langle g_+\rangle_O-\langle g_+\rangle_I,\qquad
 L_-'(0)=\langle g_-\rangle_I-\langle g_-\rangle_O .
$$

各端带 $g_j$ 偏离各自端值至多 $\tan\vartheta/4$ 即给两导数下界 $\tan\vartheta/2$。较宽的原带可以直接验证两个真实加权均值之差。仅由端值连续性得充分窄的带存在，未保证指定原结已足够窄。

选双参数盒 $|t_j|\le T_j$，$\sigma\in(0,1)$。在每个真径向胞 $I$ 用覆盖全角的 $m_I\ge\sup|\nabla_g u|$，并取

$$
 B_r=\max_j T_j\sup_I|h_j'|/\sqrt{\inf_I E},\qquad
 B_\varphi=\frac{\sum_jT_j\sup_I|h_j|}{2\inf_I r}.
$$

若每胞 $m_I+\sqrt{B_r^2+B_\varphi^2}\le\sqrt{1-\sigma^2}$，则整盒整圈保持 $s\ge\sigma$。径向系数是非负和为一的二个角权，角向导数额外带 $\sin\varphi/2$。只核两条轴不足以推出此条件。

真实二阶导数及其一个原样条全盒界为

$$
 L_j''(t)=-\int_a^b\frac{E(h_j')^2}{[E-(p_j+t h_j')^2]^{3/2}}\,dr,
 \qquad
 H_j=\frac{10}{7}\sum_{\nu=I,O}
 \frac{\sup_\nu(E/A_{j,\mathrm{box}}^3)}{\ell_\nu},
$$

其中被积表达式的上界在两条真带及全幅盒求，$A_{j,\mathrm{box}}=\sqrt{E-(p_j+t h_j')^2}\ge\sqrt E\,\sigma$。故 $|L_j''|\le H_j$。一旦 $d_j\le L_j'(0)$ 为严格正下界，选

$$
 0<T_j^*\le\min(T_j,d_j/(2H_j)),\qquad
 d_j^*=d_j-H_jT_j^*>0.
$$

若 $|L_j^*-L_j(0)|\le T_j^* d_j^*$，在 $[-T_j^*,T_j^*]$ 有唯一实根令 $L_j(t_j)=L_j^*$，并有 $|t_j|\le |L_j^*-L_j(0)|/d_j^*$。两轴同时满足才得到同一 $u_t$ 的两轴精确闭合。这是中值定理和区间两端异号的直接推论。收细根区间可仅在两个端带积分

$$
 L_j(t)-L_j(0)
 =-t\int_a^b
 \frac{h_j'(2p_j+t h_j')}{\sqrt{E-(p_j+t h_j')^2}+\sqrt{E-p_j^2}}\,dr .
$$

给定真实 $L_j(0)$ 的区间无需重付整轴积分。一个二进制中点仍应报告其实际轴残差；若证明需要精确实根，可用上式定义其唯一性并在后续整带证明中包住该根。其余参数 $\xi$ 的局部隐导数是 $(\partial_\xi L_j^*-\partial_\xi L_j)/\partial_{t_j} L_j$，分子中 $\partial_\xi L_j$ 在固定 $t$ 下取。由此可以消去两个局部轴残差而继续独立计入三项 Gram、真实三维闭合、全周和曲率。所得可达范围随 $u,C_z$ 及两条真带改变，未推出任意指定水平、竖向平移都可达。

[条件区间消费者](../scripts/r753_two_axis_quintic_radius.py) 的联合输入为同一连续高度的固定帽姿、真轴积分、全角梯度界、两真带斜率区间、原固定度量与证据身份。它对原结端带导数采用全带包围，可保守返回未决。它报告整盒正图、局部单调范围与实根包含区间。本文未给新高度的执行结果。

## 同一物理代表的双正图与曲率

以下只施用于选定的实际三维 $F=(U_\chi,u)$（或已付其实现导数误差的代表）。在 $g$ 正交标架中，R749 的两理想水平列组成 $Q_h$，奇异值为 $1,s$，取向为正。竖向行为 $du$，$\|du\|_g=\sqrt{1-s^2}$。混合的理想水平部分为复乘 $LQ_h$，其中 $L=1-\chi+\chi R$，$|L|^2=1-q$；两实际水平误差列的长度分别至多 $e_r,e_\varphi$，令 $e=(e_r^2+e_\varphi^2)^{1/2}$。

若 $\sqrt{1-q}\,\sigma>e$，线性插入两误差列时最小水平奇异值始终正，故实际水平投影 Jacobian 为正。理想混合的未归一法向在外轴 $e_z$ 的分量为 $(1-q)s$，水平法向大小为 $|L|\sqrt{1-s^2}$。每个三维理想列长至多一，加入实际水平误差后的叉积误差至多 $\varepsilon_\times=e_r+e_\varphi+e_r e_\varphi$。对与外轴夹锐角 $\vartheta$ 的实际内轴 $v_i$，以下全胞条件足以同时得到内外两投影 Jacobian 为正：

$$
 (1-q)\sigma\cos\vartheta-\sqrt{1-\sigma^2}\sin\vartheta
 >\varepsilon_\times .
$$

取 $q$ 的上界应用该式。实际两列面积至多 $(1+e)^2$，故在分子为正时 $N_F\cdot e_z\ge[(1-q)\sigma-\varepsilon_\times]/(1+e)^2$。双正图的全局使用还要满足给定延拓的 proper 性及帽/其余壳的相应条件。[R662](R662-tilted-two-plane-global-tube-and-offset-cap-clearance.md)。

令 $G=F^*\mathrm e$ 为该三维实际诱导度量。由真实六 jet 得单位法向 $N_F$ 与 $II$；在 $\eta=\|G-g\|_{g,\mathrm{op}}<1$ 时，$MG+II\succeq0,\ MG-II\succeq0$ 等价于真正两主曲率绝对值不超过 $M$。亦可以实际 $G$ 的一阶误差给验证上界。设 $N_F\cdot e_z\ge m>0$，$D_G=\|\nabla^g G\|_{g,\mathrm{tri}}$，均为全域或真胞界。Koszul 差公式给 $\|\nabla^G-\nabla^g\|_g\le3D_G/[2(1-\eta)]$；取两次方向均为任意 $g$ 单位切向，并用 $\mathrm{Hess}_G u=(N_F\cdot e_z) II$，得到

$$
 \|S_F\|_{G,\mathrm{op}}\le
 \frac{\|\mathrm{Hess}_g u\|_{g,\mathrm{op}}
 +3D_G\sqrt{1-\sigma^2}/[2(1-\eta)]}{m(1-\eta)} .
$$

这里 $S_F=G^{-1}II$，分母最后一因子来自 $G\ge(1-\eta)g$。单凭小 $\eta$ 或高度的材料 Hessian 不给所需的 $D_G$。每个真正校正后的场仍须支付整带闭合、Gram、曲率、物质边迹、宏观和法球余项；本条两实根只消去 R749 的两个指定锚点。
