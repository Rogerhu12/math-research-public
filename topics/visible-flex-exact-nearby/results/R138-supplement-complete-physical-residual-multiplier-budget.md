# R138 补篇：完整物理残差的可消费乘子预算

2026-11-20，visible-exact-astra-ac637-20261120 / global_route。

本篇给 [V 篇](R138-supplement-Volterra-Grushin-energy-and-root-defect-trace.md)
实际体能量预算的封闭算法。只消费同一个原候选已经完成的正区闭行、完整
moving 角缺陷闭行及真根 germ；Qrepair 的完整差和准确 mean 留在公式里。
算法同时给同物理径向 frame 的 $Z,Z_\theta,P,P_\theta$，所以根端高频费用
可以消费同一结果。没有重新求解原 residual、曲率、候选 Fourier 包络或模型
ODE，也没有把 WVC hybrid 的主部认作真正 $DF(Q_c)$。

这里证明预算公式；新消费者的实际保存数及门的真假应由其独立执行记录给出。
特别，完整上界存在和最终吸收比较为真是两件不同的事。

## 1. 负 Sobolev 保守输运只需点态 Jacobian

设 $H_r+\partial_\theta(\epsilon H)=0$，在一个径向段上令
$$
 A=\exp\int\|\epsilon_\theta\|_\infty\,dr.
$$
其 flow 的 Jacobian 及逆 Jacobian 都不超过 $A$。保守传播是密度拉回
$Uf=\chi'(f\circ\chi)$，故 $\|U\|_{L^2\to L^2}\le\sqrt A$。
其 $L^2$ 伴随是普通 composition $g\mapsto g\circ\chi^{-1}$。
由 V.15 的直接 Jacobian 证明，该 composition 的 $H^1$ 范数也至多
$\sqrt A$。对偶和 Hilbert 插值于是给
$$
 \boxed{\quad \|U\|_{H^{-\tau}\to H^{-\tau}}\le\sqrt A,
              \qquad 0\le\tau\le1.\quad}
 \tag{X.1}
$$
所以 V.5、V.8、V.21--V.22 中同一个输运因子可以取
$$
 E_\epsilon=\exp\left(\frac12\int\|\epsilon_\theta\|_\infty\,dr\right).
 \tag{X.2}
$$
这是比物理角 $A^0$ 费用更直接的已证替代式，不需要把几何 supremum
误称作 Fourier 绝对和。所有圆周空间仍在真实 $2\pi$ 圆上。

同一论证也直接支付 V 根迹到 U 真根型的密度变换：
$$
 \mathsf H=\vartheta(H\circ\Theta),\qquad
 \|\mathsf H\|_{H^{-\tau}_\phi}
    \le\sqrt{A_\Theta}\,\|H\|_{H^{-\tau}_\theta},
       \quad 0\le\tau\le1.
 \tag{X.2a}
$$
这里 $A_\Theta=\sup\max(\vartheta,\vartheta^{-1})$。
准确 Jacobian 与真实角图作为同一个密度拉回处理，mean 保留；无需另付
$\vartheta$ 的 $C^1$ 乘子。若根型先给 moving 常数 $C_{\rm mov}$，
V 的物理缺陷常数可取 $C_*=A_\Theta C_{\rm mov}$。

对任意矩阵或向量乘子 $A(\theta)$，若
$\|A\|_\infty\le A_0$、$\|A_\theta\|_\infty\le A_1$，定义
$$
 N_\tau(A_0,A_1)=A_0^{1-\tau}(A_0+A_1)^\tau,
              \qquad0\le\tau\le1.
 \tag{X.3}
$$
它控制乘法在 $H^{\pm\tau}$ 上的范数。证明分别使用 $L^2$ 上界 $A_0$
和乘积求导所得 $H^1$ 上界 $A_0+A_1$，再插值、对偶。
向量叉乘及矩阵转置具有相同的这两个上界。$A_0=0$ 时实际乘子为零，
按零解释；$\tau=0$ 直接取 $A_0$。

## 2. 完整 Hessian 中先准确消去 $1/a$

本节 $\mathcal F=(B,C)=(u/v,1/v)\circ\Theta^{-1}$ 是物理曲率对，
而 $(X,Y,n)$ 仍是实际 frame。所有右侧 moving 状态均先按真实逆角拉回。
设
$$
 P_c=\begin{pmatrix}C&-BC\\0&-C^2\end{pmatrix},\qquad
 t=P_c R,\qquad \epsilon=I_\theta(CR_v),
 \quad R=(R_u,R_v),\quad R_m=\langle R_v\rangle_\phi.
 \tag{X.4}
$$
在本题反射类中 $R_v,C$ 为 even，$\epsilon$ 为 odd，因此这正是 T.6 的
准确速度。特别 $\epsilon_\theta=CR_v-R_m/m$，没有删掉 mean。

令 $W=\omega_\theta-H$、
$x'=(W\cdot Y,-W\cdot X)=a(b,c)$。把 J.26 的完整逆微分写为
$$
 L=\begin{pmatrix}v&-uv\\0&-v^2\end{pmatrix},\qquad
 \widehat h=\mathfrak M_Qx'
 =L\left[x'-v\mathcal F_\theta I_\theta
                  \{x'_C-mC\langle x'_C\rangle_\theta\}\right].
 \tag{X.5}
$$
由于 $a$ 只依赖 $r$，原 moving 方向在物理角中的表示准确为
$h=\widehat h/a$。T.8 乘以 $a$ 后成为
$$
 \boxed{\begin{split}
 a f_0=\mathcal L_R\widehat h
  :={}&DP_c[t]\widehat h-t_\theta I_\theta(C\widehat h_2)\\
   &+\mathcal F_\theta\left\{(CR_v)I_\theta(C\widehat h_2)
                       +\epsilon\langle C\widehat h_2\rangle_\theta\right\},
 \qquad
 DP_c[t]=\begin{pmatrix}
 t_C&-Ct_B-Bt_C\\0&-2Ct_C
 \end{pmatrix}.
 \end{split}}
 \tag{X.6}
$$
完整一般坐标 Hessian 中的另一项
$-\mathcal F_\theta\langle C\epsilon\widehat h_2\rangle$ 在本题为 odd
的平均，准确等于零；若扩大函数类，必须重新加入它。
式 (X.5)--(X.6) 把 $1/a$ 在估计前消去，并完整保留 mean 投影和 primitive。

所有 primitive 的输入是四重标量，故在 $H^s$ 中范数至多 $1/4$。
环境向量本身仍用全圈范数，不能对它擅用这个 $1/4$。用 (X.3) 对每个
已指定乘子取上界，记
$$
 \begin{split}
 M_\tau&=N_\tau(L)\left[1+rac14N_\tau(v\mathcal F_\theta)
                                      \{1+N_\tau(mC)\}\right],\\
 J_\tau&=N_\tau(DP_c[t])+rac14N_\tau(t_\theta)N_\tau(C)\\
 &\qquad+N_\tau(\mathcal F_\theta)N_\tau(C)
                    \left\{\frac14N_\tau(CR_v)+N_\tau(\epsilon)\right\}.
 \end{split}
 \tag{X.7}
$$
则 $\|\mathfrak M_Q\|_{H^{-\tau}\to H^{-\tau}}\le M_\tau$，
$\|\mathcal L_R\|\le J_\tau$。常数平均是正交投影，范数为 $1$；
没有将 mean 当成一个免费消失的系数。

T.14 的其余三项可直接写成矩阵乘法：
$$
 \begin{split}
 Z_*&=\gamma\{-Z_X\otimes Y
                  +Z_Y\otimes[2uY+(u^2+Kv^2)X]\},\\
 E_*&=-\epsilon\{X_\theta\otimes X+Y_\theta\otimes Y\},\\
 \mathcal T_R W
   &=[-Y,X],\mathcal L_R\mathfrak M_Q
                     \binom{W\cdot Y}{-W\cdot X}
       +Z_*W+E_*W-\epsilon_\theta W.
 \end{split}
 \tag{X.8}
$$
设 $o_1\ge\|O_\theta\|_\infty$，提取与插入矩阵的 $C^0$ 范数为 $1$，
一阶导数范数至多 $\sqrt2o_1$。因此一个可消费的完整乘子界为
$$
 \boxed{\quad
 k_{-\tau}=N_\tau(1,\sqrt2o_1)^2 J_\tau M_\tau
       +N_\tau(Z_*)+N_\tau(E_*)+N_\tau(\epsilon_\theta),
       \qquad\tau\in\{0,1/3,1/2\}.\quad}
 \tag{X.9}
$$
每个量只依赖中心和已构造 frame 的完整已知系数，不含待求 BVP 逆。
这里首先在本题原四重加反射等变子空间上取范数。若使用 V 的全空间
写法，则定义扩展为 $\mathcal T_R\Pi_{\rm sym}$，其中原有限对称群的
正交平均 $\Pi_{\rm sym}$ 在每个 $H^s$ 上范数为 $1$；真实 $W$ 不变。
这样 $1/4$ 只用于提取后的四重标量，(X.9) 仍给严格的全空间扩展范数。

## 3. 旧闭行给真正修补 residual

旧[完整 moving 角缺陷定理](R133-supplement-complete-angular-model-geometry-from-moving-residual.md)
的每个闭行保存 $\mathcal R,\mathcal R_\phi,\mathcal T,\mathcal T_\phi$
的全角上界 $R_0,R_1,T_0,T_1$，不是角采样。
为避免与原 even mean $R_m$ 混淆，下式的 $R_j$ 仅是矩阵范数上界。
写原状态的 $|m|\in[m_-,m_+]$、$a\ge a_->0$，原 moving
$|u|\le U$、$|v|\le V$、$|u_\phi|\le U_1$、$|v_\phi|\le V_1$。
由原 A.8--A.9 的第三分量与后二分量准确得到
$$
 \begin{split}
 r_m&=m_+^2R_0/a_-,\\
 r_u&=m_+\sqrt{1+U^2}R_0/a_-,&
 r_v&=m_+(T_0+VR_0)/a_-,\\
 r_{u1}&=m_+(R_1+U_1R_0)/a_-,&
 r_{v1}&=m_+(T_1+V_1R_0)/a_- .
 \end{split}
 \tag{X.10}
$$
这些分别控制原 $|R_m|,\|R_u\|_\infty,\|R_v\|_\infty$ 和两项 moving
角导数。已保存几何范数没有被倒称为 Wiener 范数。
具体是先用准确恒等式
$R_m=-m^2r_3/a$、$R_u=(m/a)(r_2-ur_3)$、
$R_v=(m/a)(t-vr_3)$，再取范数；没有在取范数后丢掉两次 mean 的抵消。
$r_3=-aR_m/m^2$ 只依赖径向变量，所以 $r_{3,\phi}=0$；
这正是上述两个角导数界没有另一个 $r_{3,\phi}$ 项的理由。

在每个原开片，Qrepair offset $e$ 的径向导数准确为零，故
$R_c=R-\{F(Q+e)-F(Q)\}$。用原完整修补的 $A^0$ 界 $e_0$、角导数界
$e_1$ 和 mean 界 $e_m$，置 $Q_0=U+V$、$Q_1=U_1+V_1$、
$K_+=\max(1,|K|)$、$S=K_+Q_0^2$、
$\Delta S=K_+(2Q_0e_0+e_0^2)$。由原完整 moving field 逐项给
$$
 \begin{split}
 f_c={}&\frac{|\beta|}{4}
             \{\Delta S\,Q_1+(S+\Delta S)e_1\}\\
 &+\gamma K_+\{e_mQ_1+(m_++e_m)e_1\}\\
 &+|\beta|\{e_0+\Delta S\,Q_0+(S+\Delta S)e_0\}.
 \end{split}
 \tag{X.11}
$$
本式的 $U,V,U_1,V_1$ 取原 positive/germ 的完整 Wiener $A^0$ 界，
它们也可用于 (X.10) 的点态界。这里的 $1/4$ 用于背景修补差的 Wiener
primitive；(X.10) 恢复的 residual 只有 $C^0$ 资格，没有带入该 $1/4$。
于是 $\|R_c-R\|_{A^0,\rm pair}\le f_c$。差仍是 index 至多 $96$、
物理频率至多 $384$ 的三角多项式，故其一次角导数不超过 $384f_c$。
将 (X.10) 的前三级各加 $f_c$，后两级各加 $384f_c$，便是修补中心
真正完整的 residual 包络。二次 moving 角导数可用 Bernstein
$\|R_{c,\phi\phi}\|_\infty\le384\|R_{c,\phi}\|_\infty$；
对背景则使用真实频率 $128$。

重新形成修补后的 moving curvature/torsion 时，可以只给原完整范数加
严格的中心差，避免先恢复 raw residual 再重复放大。令
$m_c^-=m_--e_m$、
$i_1=e_m/(m_-m_c^-)$、
$i_2=e_m(2m_++e_m)/(m_-^2(m_c^-)^2)$。
对 $z=u,v$ 分别取背景上界 $Z,Z_1$ 和原 residual 上界 $r_z,r_{z1}$，置
$$
 \begin{split}
 q_z&=\frac{f_c}{m_c^-}+r_z i_1
       +\frac{e_0(r_m+f_c)+Zf_c}{(m_c^-)^2}+Zr_m i_2,\\
 q_{z1}&=\frac{384f_c}{m_c^-}+r_{z1}i_1
       +\frac{e_1(r_m+f_c)+Z_1f_c}{(m_c^-)^2}+Z_1r_m i_2,\\
 q_m&=\frac{f_c}{(m_c^-)^2}+r_m i_2.
 \end{split}
$$
它们分别控制
$\Delta\{R_z/m-zR_m/m^2\}$、其 moving 角导数和
$\Delta(R_m/m^2)$。因此可直接使用
$$
 \begin{split}
 R_{0,c}&=R_0+\sqrt{b_0^2q_v^2+a^2q_u^2+a^2q_m^2},\\
 R_{1,c}&=R_1+\sqrt{b_0^2q_{v1}^2+a^2q_{u1}^2},\\
 T_{0,c}&=T_0+aq_v,\qquad T_{1,c}=T_1+aq_{v1}.
 \end{split}
 \tag{X.11a}
$$
这里 $|a|,|b_0|$ 取所在闭片的完整上界。角导式的 $\Delta R_m$ 仍按
$f_c$ 支付，没有误乘 $384$，也没有将它设零。

所有 $\partial_\theta$ 均按 $\lambda\partial_\phi$ 转换，
$\lambda=m/v>0$。例如
$f_{\theta\theta}=\lambda^2 f_{\phi\phi}
 +\lambda\lambda_\phi f_\phi$。
真实 $v,m$ 间隙和每个闭片的有向商界仍保留；不能用有限 moving
support 冒认物理 Fourier support。

## 4. 物理 frame 缺陷：首分量抵消和无指数传播

写 $\vartheta=v/m$，并把修补后的完整 moving 曲率、torsion 写为
$$
 \mathcal R=\Omega(r_1,r_2,r_3),\qquad
 \mathcal T=(0,t,0),\qquad \mathcal F=(B,C).
$$
真实角图有 $\Theta_r=\tau+\epsilon$，而连接关系是
$\Omega_r^M=\Omega_r^P+\tau\Omega_\theta^P$。
所以按照 J.5 的符号，准确有
$$
 \mathfrak D=-\mathcal R/\vartheta
                   +\partial_\theta(\epsilon\Omega_\theta^P).
 \tag{X.12}
$$
这里 $a\epsilon=I_\phi t$、$a\epsilon_\theta=t/\vartheta$。
$r_1=(b_0/a)t$ 使第一分量准确抵消，而非只被小量上界吸收。因此
$$
 \mathfrak D=\Omega\left(0,
       -\frac{(r_2,r_3)}{\vartheta}
       +\frac t\vartheta\mathcal F+a\epsilon\mathcal F_\theta\right).
 \tag{X.13}
$$
若 $\vartheta\ge s_->0$、$\|\vartheta_\phi\|\le s_1$，
$\|\mathcal F\|\le F_0$、$\|\mathcal F_\theta\|\le F_1$、
$\|\mathcal F_{\theta\theta}\|\le F_2$，$p=\pi/8$，则
$$
 \begin{split}
 d_0&=\frac{R_0+F_0T_0}{s_-}+pT_0F_1,\\
 d_1&=\frac{R_1+F_0T_1}{s_-^2}
       +\frac{(R_0+F_0T_0)s_1}{s_-^3}
       +\frac{2T_0F_1}{s_-}+pT_0F_2
 \end{split}
 \tag{X.14}
$$
分别控制 $\|\mathfrak D\|,\|\mathfrak D_\theta\|$。
这里的 $R_j,T_j$ 必须是第 3 节已经加完修补费后按原准确 A.8--A.9
重新形成的新上界，不能将原中心直接换名。

作为独立核对，由 J.31 的 $R_{\rm phys}=D\Psi R$，同样得到
$\|\mathfrak D\|\le a(\|t\|+|\epsilon|F_1)$、
$\|\mathfrak D_\theta\|\le a(\|t_\theta\|+|\epsilon_\theta|F_1+|\epsilon|F_2)$，
其中本句 $t=P_cR$ 用第 2 节的曲率对记号。两组上界可以取较小者，
但不能扣除独立的上界。

从真实外端向根传播 J.6--J.10。令
$o_0\ge\|\Omega_\theta^P\|$、$o_{r1}\ge\|\partial_\theta\Omega_r^P\|$
为一片上的常数上界，incoming majorant 是 $(z,z_1,p_0,p_1)$，宽为 $h$。
置
$$
 A=o_{r1}+d_0,\quad B=o_0d_0+d_1,\quad
 I_z=hz+\tfrac12h^2d_0,\quad
 I_{z_1}=hz_1+\tfrac12h^2(Az+B)+\tfrac16h^3Ad_0 .
$$
准确的单片输出上界为
$$
 \boxed{\quad
 z^+=z+hd_0,\quad z_1^+=z_1+A I_z+hB,\quad
 p_0^+=p_0+e I_z,\quad p_1^+=p_1+e I_{z_1}.
 \quad}
 \tag{X.15}
$$
这是三角多项式 majorant 的准确积分，没有数值 ODE 误差或指数增长。
在这一片上可用输出端的四个非负数界整片。
然后
$\|O_\theta\|\le o_0+z$，
$\|O_{\theta\theta}\|\le(o_0+z)o_0+\|\partial_\theta\Omega_\theta\|+z_1$。

Qrepair 的状态、全部角导数和 $\Theta$ 在每个原接口准确连续。
因此本物理径向构造的 $Z,P$ 也连续，没有残留接口原子。
这个结论使用完整修补定理的真实跳抵消；消费时仍核对原全部分片和接口，
不把原未修补模型的跳从它自己的证书里删除。

## 5. 同一全圈外锚的实际初值

使用 S.2 的同一物理外锚。准确有
$P_R=P_{\theta,R}=0$、$\|O_{\mathrm{anchor},\theta}\|_{\rm op}=1$。
原 moving anchor 缺陷满足 $E_R=\vartheta Z_{\rm orig}\circ\Theta$。
若旧已付 anchor 数为 $E_R^*,E_{R,\phi}^*$，则
$$
 z_R\le E_R^*/s_-+a_R\delta F_0,\qquad
 z_{1,R}\le E_{R,\phi}^*/s_-^2+E_R^*s_1/s_-^3
                                      +a_R(\delta F_0+\delta F_1).
 \tag{X.16}
$$
$\delta F_j$ 是同一固定物理角的原/修补曲率对 $C^j$ 差。
以下是只用外端整闭片背景的显式费用，因而无需重算候选端点。

设原 $|v|\ge v_-$，修补后 $v_c\ge v_--e_0$ 表示 $|v_c|$ 的下界，
$m_c\ge m_--e_m$ 同理。取
$$
 \Delta\vartheta=\frac{e_0}{m_c}+rac{V e_m}{m_-m_c},\qquad
 \Delta\Phi=\frac{\pi\Delta\vartheta}{8s_-},\qquad
 \Delta\lambda=\frac{e_m}{v_c}+rac{m_+e_0}{v_-v_c}
                           +\frac{m_+V_1}{v_-^2}\Delta\Phi.
 \tag{X.17}
$$
直接的 moving 商差为
$$
 \begin{split}
 D_B&=e_0/v_c+Ue_0/(v_-v_c),& D_C&=e_0/(v_-v_c),\\
 D_{C,\phi}&=e_1/v_c^2+rac{V_1e_0(2V+e_0)}{v_-^2v_c^2},\\
 D_{B,\phi}&=e_1/v_c+rac{U_1e_0}{v_-v_c}
       +\frac{e_0V_1+(U+e_0)e_1}{v_c^2}
       +\frac{UV_1e_0(2V+e_0)}{v_-^2v_c^2}.
 \end{split}
 \tag{X.18}
$$
若原 moving $\|\mathcal F_\phi\|\le F_{\phi,1}$、
$\|\mathcal F_{\phi\phi}\|\le F_{\phi,2}$，则可取
$$
 \begin{split}
 \delta F_0&=\sqrt{D_B^2+D_C^2}+F_{\phi,1}\Delta\Phi,\\
 \delta F_1&=\frac{m_++e_m}{v_c}
          \{\sqrt{D_{B,\phi}^2+D_{C,\phi}^2}
                                  +F_{\phi,2}\Delta\Phi\}
                                  +F_{\phi,1}\Delta\lambda.
 \end{split}
 \tag{X.19}
$$
证明是先比较两个真实 lift 及其逆，再对
$\lambda\mathcal F_\phi$ 作商差和真实 composition 差。
原与修补后的角未被当成同一个角；$a_R$ 和外锚也没有另行改动。

## 6. 形成 V 的全部体费用

以每片输出的 $z,z_1,p_0,p_1$ 以及第 2 节的 $k_{0},k_{-1/3},k_{-1/2}$
直接形成 T.21 的矩阵 $\mathcal L$，并用 (X.3) 形成
$$
 \begin{split}
 a_1&=N_{1/2}(eX+2\epsilon F_\theta),\qquad
 p_1^*=N_{1/2}(M_P\mathcal L),\\
 r_1&=2N_{1/2}(G)k_{-1/2},\qquad
 e_1^*=N_{1/2}(\epsilon F_\theta).
 \end{split}
 \tag{X.20}
$$
其中 $F_\theta=aY+P$，导数 $F_{\theta\theta}=aY_\theta+P_\theta$，
$|G|<222/125$ 已付，$G_\theta=F_\theta$。
取 $E_0=\sup(p_1^*+r_1+e_1^*)$、
$E_1=\sup(a_1+p_1^*+r_1)$，正是 T.22 证明中尚未代入 $H$ 的完整双线性费用。

背景的一组直接闭片上界为
$$
 \begin{split}
 M&=1+U^2+|K|V^2,\quad
 C_W=\frac{M}{\gamma_-\sigma_-v_-^2},\quad
 A_\Theta=\max\{V/m_-,m_+/v_-\},\\
 C_E&=\frac{M}{\sigma_-v_-}
                    \left(\gamma_+m_++\frac1{\gamma_-m_-}\right),\qquad
 C_H=\gamma_+^2U^2m_+/v_-+|K|V/m_- ,
 \end{split}
 \tag{X.21}
$$
其中全部字母此处均为**修补后**的上、下界，$\sigma_-=2/5$。
原 closed-row 的 $d_\phi$ 上界只需另加
$2|\beta|K_+(2Q_0e_0+e_0^2)$。
以原真实闭片宽度做上 Darboux 和，得到
$$
 \begin{split}
 D_0&=\int\|d_\phi\|_\infty,
 &\Gamma&=e^{D_0},\qquad
 \Lambda_\epsilon=rac12\int|\epsilon_\theta|,\\
 J_0&\le120\int C_W k_0^2,
 &K_-^2&=\int k_{-1/3}^2 .
 \end{split}
 \tag{X.22}
$$
对真根不确定区间使用整个 $[r_-^*,r_+^*]$ 与原 germ 的覆盖；
所有非负积分可以扩到 $[r_-^*,R]$ 作上界。V.4 的 $x/K\le120$
仍只用于真实正区，不把下端区间端点冒称为真正根。

将实际保存的 (X.20)--(X.22) 代入 V.8、V.18、V.22--V.25，便给
$h_E,h_B,w_E,w_B,z_E,z_B,r_E,r_B$ 与
$a_{EE},a_{EB},a_{BB}$。
根端完整型的独立常数 $C_*$ 仍应由实际根二次型给出；一旦已付，
最终三门就是 V.25 的三个有理比较。没有通过的比较应保存为 false，
不能由某个新的小 residual 或已有几何正 support 代替。

## 7. 只消费旧目标的最小新科学范围

原输入是原完整 positive 的 4650 闭行、原完整 moving angular 的 7722
公共闭行及原真根 complex germ。输入的 hash、参数、全角域、mean、
原 3594 个正区接口与完整 6143 个旧 angular 接口都保留。
真根 collar 不外推正区闭行，而直接使用已证明覆盖它的完整 germ。

新的科学输出只有以上组合的标量上界、积分、实际根缺陷四标量及吸收比较。
背景 Fourier 数组、旧 residual 行、frame 轨迹和旧系数包均不重新发表。
每个新部分和以原有精确闭片宽度消费其完整行，并作可恢复的累计标量
checkpoint。旧 primitive、曲率、候选 coefficient norm、模型几何目标
和原成功消费者的生产入口调用数必须为零。
