# R282：完整对称 Gaussian 二层系数与一个不由六能量推出的平方 history 门

日期：2026-11-15。**完整纸面推导与有限参数非蕴含证明；没有执行求积、符号程序、profile 扫描、人工检查或研究计算。**

[R280](R280-ordered-three-moment-areas-and-five-block-Gaussian-cancellation.md) 在同一个真实圆上支付了全部六个 Gaussian 面积及六能量。这不等于支付二层 history 的对称部分。本稿从原第四式保全全部外槽，给出十个 $E_rE_s$ 的准确系数；其中 $E_{-3}^2$ 在已构造微包类上等价于三个新的 $C^3$ 能量条件。再用同一个有限数据纤维，证明第一个新条件确实不由此前全部面积、六能量、三矩及完整第三条件推出。

这个非蕴含结论不是对 R280 某个未作数值选择的根宣告失败；它证明存在同样满足那些既有条件、却不满足新平方门的真实圆。所有未付项仍须在同一个圆上继续支付。

来源：[R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R243](R243-finite-jet-criterion-for-the-complete-even-exceptional-ruling.md)、[R245](R245-complete-block-additivity-and-four-Gaussian-history-reduction.md)、[R249](R249-Gaussian-word-independence-and-complete-resonant-fourth-harmonic-obstruction.md)、[R250](R250-complete-circle-Gaussian-area-and-nonuniform-profile-cancellation.md)、[R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R277](R277-low-jet-observation-fibers-and-high-jet-energy-control-for-equal-background-circles.md)、[R279](R279-finite-frequency-fiber-control-pays-both-even-profile-energies.md)与 R280。

## 1. 原共同锚、完整相位与真实独立基

沿用原正右积分

$$
Jv(x)=\int_x^r v(t)\,dt,\qquad (Jv)'=-v,
$$

及共振例外端芽

$$
H=e^{\varepsilon\sigma^2},\quad
h=h_eH,\quad
k=\kappa(1-2\varepsilon\sigma^2),\quad
\omega=\kappa/h,\quad
\varepsilon=\kappa^2/4,\quad \kappa\ne0,\ h_e>0.
$$

记 $j=2\varepsilon\kappa\sigma^2$。圆与内槽为

$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta.
\tag{1}
$$

$\odot$ 是对称双线性算子槽，不把它当作一个先点乘后任意求导的函数。三外矩保持

$$
I_0(u,v)=\int u''v'',\quad
I_1(u,v)=\int xu''v'',\quad
I_2(u,v)=\int(x^2u''v''+2u'v'),
$$

$$
\mathcal E_\sigma(u,v)
=\frac{1+j^2}{4h}I_0(u,v)+\frac j2I_1(u,v)+\frac h4I_2(u,v).
\tag{2}
$$

令 $\mathcal S=\{1,-1,-2,-3\}$，
$E_r(\sigma)=\int_0^\sigma H(t)^r\,dt$。
R249 已证明

$$
1,\quad E_r,\quad E_rE_s\ (r\le s),\quad A_{r,s}\ (r<s)
\tag{3}
$$

是 $\mathbb F=\mathbb R(\sigma,H)$ 上真实独立的21元基。故面积系数不能与十个乘积系数抵消；乘积也不能被零层、一层或偶部三矩空间 $\mathcal W_e\subset\mathbb F$ 消去。

按 R224/R243 的真实中心比较，允许的原路径历史和独立 homogeneous 选择不改变本稿中心化偶部在 $\mathcal W_e$ 商中的必要条件。下面提取的是完整原式的二层系数，不把实际段首值重新设为零。

## 2. 从原第四式直接取得十个乘积系数

R73/R250 的同锚恢复为

$$
Z(D)=K_D-Y_{\Phi_{\mathsf m}D},\qquad
C(a;D)=K_C(a;D)-Y_{W_C(a;D)},
$$

$$
\Phi_{\mathsf m}=Q_\sigma+\sum_{r\in\mathcal S}E_rB_r,
\tag{4}
$$

其中 $Q_\sigma$ 为原奇 Laurent 部分，$B_r$ 为固定几何确定的真实二次算子。完整第四 ruling 为

$$
\mathscr K_\theta
=-\mathfrak b_\sigma(Z(D_\theta),Z(D_\theta))
+4\mathfrak b_\sigma(Y_{\phi_\theta},C(\phi_\theta;D_\theta)).
\tag{5}
$$

其二层来源正好是

$$
(W_C)_{\mathrm{two}}
=-\sum_{r,s}K_{r,s}B_r(\phi_\theta,B_sD_\theta),\qquad
K_{r,s}=\frac{E_rE_s+A_{r,s}}2.
\tag{6}
$$

这里保留整个外槽 $\phi_\theta$ 与内槽 $D_\theta$。原局部第三恢复至多一层；$Q_\sigma$ 交叉按原同锚分部积分也只产生零层、一层及其真实常数，不会再产生一个 $E_rE_s$ 项。

将(4)、(6)代回(5)，得四个平方系数

$$
\boxed{
\mathscr Q_{rr,\theta}
=-\mathcal E_\sigma(B_rD_\theta,B_rD_\theta)
+2\mathcal E_\sigma\{\phi_\theta,
 B_r(\phi_\theta,B_rD_\theta)\}.
}
\tag{7}
$$

六个 $r\ne s$ 的对称乘积系数为

$$
\boxed{
\begin{aligned}
\mathscr Q_{rs,\theta}
={}&-2\mathcal E_\sigma(B_rD_\theta,B_sD_\theta)\\
&+2\mathcal E_\sigma\{\phi_\theta,
 B_r(\phi_\theta,B_sD_\theta)
 +B_s(\phi_\theta,B_rD_\theta)\}.
\end{aligned}
}
\tag{8}
$$

同一计算的反对称部分仍是
$2\mathcal E_\sigma\{\phi_\theta,[B_r,B_s](\phi_\theta;D_\theta)\}$，与 R259 的方向和因子完全一致。

这些式子是从原 $Z^2$ 与第三 history 同时取得，不能只保其中一个项。分解中的第三 profile 可以带左尾；只有原完整 lower fields 已付的支持条件可使用，不把每个嵌套分解项擅自当成紧 profile。

对固定 $\theta$，(7)、(8)分别写成(2)的三个外矩组合。H 对 $\mathbb R(\sigma)$ 超越、j 为非常数多项式，故每个乘积系数恒零等价于其三个外矩分别为零。具体乘以 $4h$ 后是

$$
(1+j^2)q_0+2hj q_1+h^2q_2=0,
$$

其中 $q_\ell$ 对 $\sigma$ 为常数；按 H 次数比较即迫 $q_0=q_1=q_2=0$。原五相位始终保留，$D_0=0$ 给出的角关系可用，但不能由一个 pure 对角替代整个 $\theta$ 条件。

本节没有宣称这些全部外矩相互独立，也没有把条目数量当成函数秩。

## 3. $B_{-3}=c\mathcal P$ 的平方不可由面积身份删去

原 R249/R259 给

$$
\mathcal P(u,v)=J(u''v''),\qquad
B_{-3}=c\mathcal P,\qquad
c=-\frac{\kappa(41\kappa^4+27)}{216h_e^3}\ne0.
\tag{9}
$$

固定 $\theta$，简写

$$
r=\phi_\theta'',\quad v=\phi_\theta',\quad
F=(f'')^2,\quad d=F-r^2,\quad A=Jd,\quad
B=\mathcal P(\phi_\theta,A).
\tag{10}
$$

d 是 $D_\theta^{[2,2]}$，不是 $D_\theta$ 的四次导数。真实三矩特别给 $\int d=0$，故 A 在两侧 collar 真正为零。B 可以有常左尾，本稿不会删掉它。

由原右积分直接得到

$$
A'=-d,\quad A''=-d',\qquad
B'=rd',\quad B''=r'd'+rd''.
\tag{11}
$$

令

$$
q_\ell=-I_\ell(A,A)+2I_\ell(\phi_\theta,B).
$$

将(11)代入原 $I_\ell$，只作端项可核的分部积分，得到

$$
\boxed{
\begin{aligned}
q_0&=-\int F'd',\\
q_1&=-\int (xF'+2r^2)d',\\
q_2&=-\int x^2F'd'
      -4\int xr^2d'+4\int vr d'-2\int d^2.
\end{aligned}}
\tag{12}
$$

例如

$$
I_0(\phi_\theta,B)
=\int r(r'd'+rd'')=-\int rr'd',
$$

所以 $d'+2rr'=F'$ 给第一式。第二式也可利用
$\int dd'=0$，写成 $-\int(xF'+2F)d'$。第三式保了原 $I_2$ 的 $2u'v'$，尤其最后的 $-2\int d^2$ 不能丢去。

所有这些 IBP 的边项含紧 $\phi_\theta$、d 或 A 的零 jets；并没有用 B 的左尾为零。于是完整 $E_{-3}^2$ 系数准确为

$$
\boxed{
\mathscr Q_{-3,-3,\theta}
=c^2\left\{\frac{1+j^2}{4h}q_0
+\frac j2q_1+\frac h4q_2\right\}.
}
\tag{13}
$$

(12)既不是交换子，也没有因 $[\mathcal P,\mathcal P]=0$ 消失。后者只说明同字母没有反对称面积。

## 4. 真正不交微包上的完整局部式

取目前使用的真实 rank-one 微包表示

$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,
$$

各 $u_i$ 的开放支持两两不交。定义

$$
c_i(\theta)=a_i\cos\theta+b_i\sin\theta,\quad
d_i(\theta)=a_i^2-c_i(\theta)^2,\quad
\rho_i=(u_i'')^2,
$$

$$
K_{\ell,i}=\int x^\ell(\rho_i')^2\quad(\ell=0,1,2),
\qquad C_i=\int(u_i'')^4.
\tag{14}
$$

此处索引 i 可以直接覆盖全部实际八/十二副本与最后 block；其共同幅度应纳入 $a_i,b_i$，不能省去四次权。

(12)的所有 integrand 都已是实际局部表达式，故在这一步可按不交支持相加，得到

$$
\boxed{
\begin{aligned}
q_0&=-\sum_i a_i^2d_iK_{0,i},\\
q_1&=-\sum_i a_i^2d_iK_{1,i},\\
q_2&=-\sum_i a_i^2d_iK_{2,i}
-\frac23\sum_i c_i^2d_iC_i
-2\sum_i d_i^2C_i.
\end{aligned}}
\tag{15}
$$

准确的两个局部 IBP 是

$$
\int x\rho_i\rho_i'=-C_i/2,\qquad
\int u_i'u_i''\rho_i'=-2C_i/3.
$$

所以第三式中
$-4\int xr^2d'$ 贡献 $+2c_i^2d_iC_i$，
$4\int vr d'$ 贡献 $-8c_i^2d_iC_i/3$；
合并后恰为 $-2c_i^2d_iC_i/3$。这不是只保 $u'''$ 的 principal 近似。

## 5. R277/R280 类上恰为三个新的 even 能量

先在一个等平方背景基本布局中记

$$
b_i^2=B_0>0,\quad
R_i=a_i^2-B_0\in\{-B_0/2,8B_0\},\quad
T_i=a_ib_i.
$$

原格点十矩包括 $\sum_iR_i=\sum_iT_i=0$，并有逐项恒等式

$$
R_i^2-4T_i^2=\frac{7B_0}{2}R_i.
\tag{16}
$$

同一 $\mathcal F$-纤维保留每个母包的 $C_i=C_0$，其来源是已经列入 R277 的原 Gaussian self，而非额外增强 $\mathcal F$。具体取 $B_{-1}=d_-\Phi_{p_0}+e_-\Phi_{s_1}$。R267 保真实单包 Green 尾的表给

$$
S_{\mathcal P,\Phi_{p_0},0}(u)=C(u)/6,\qquad
S_{\mathcal P,\Phi_{s_1},0}(u)=7C(u)/6,
$$

故按 R277 的 $S=2I$ 规范，

$$
S_{B_{-1},B_{-3},0}(u)
=-\frac{c(d_-+7e_-)}6 C(u),\qquad
d_-+7e_-=-\frac{\kappa(81\kappa^2+7)}{4h_e}\ne0.
$$

式(9)也给 $c\ne0$，所以保持这个原 self 的平移常数项即准确保持 $C(u)$。这里使用 R267 的非合法单包表，不将 R252 仅对零三矩方向的变分论证直接套到实母包。

所有完整副本按实际正四次幅权相加；十二副本准确消除 odd 角项。所需平移次数均不超过旧十次界，不能只凭一个单微包的奇性就越过该包装。

令 $s_\theta=\sin\theta$。由
$d_i=s_\theta^2R_i-2\sin\theta\cos\theta\,T_i$、
(16)及原零矩，得到包装后的准确恒等式

$$
\sum_i c_i^2d_iC_i=0,\qquad
\sum_i d_i^2C_i=s_\theta^2\sum_iR_i^2C_i.
\tag{17}
$$

这两式对 R280 的两个布局、所有最终位置、保全同一 $\mathcal F$ 的不同实际母包以及其最终正幅混合成立。每个完整副本内用其自己的背景值；不要求所有最终副本有同一个全局 $B_0$。

定义全部实际副本的三个量

$$
\boxed{
\begin{aligned}
H_0&=\sum_i a_i^2R_iK_{0,i},\\
H_1&=\sum_i a_i^2R_iK_{1,i},\\
H_2&=\sum_i a_i^2R_iK_{2,i}
       +2\sum_i R_i^2C_i.
\end{aligned}}
\tag{18}
$$

(15)—(17)准确化为

$$
(q_0,q_1,q_2)=-\sin^2\theta\,(H_0,H_1,H_2).
\tag{19}
$$

因此在这个已付完整包装的实际类内，

$$
\boxed{
E_{-3}^2\text{ 的完整圆系数为零}
\quad\Longleftrightarrow\quad H_0=H_1=H_2=0.
}
\tag{20}
$$

这时消掉的不只是 pure 谐波，而是整个(19)。$H_2$ 中的低阶正项是准确的基线，不能在未来高频 principal 模型中删掉。R279 的两个能量则是

$$
L_c=\sum_i\lambda_iS(u_i),\quad
M_c=\sum_i\lambda_iT(u_i),\qquad
\lambda_i=-a_i^2R_i,
\tag{21}
$$

$$
S(u)=\frac1{64}\int x^6(x^2u''-2xu'+2u)^2(u''')^2,
$$

$$
T(u)=-\frac1{64}\int x^5(x^2u''-2xu'+2u)
(3x^2u''-5xu'+4u)(u''')^2.
$$

(18)与(21)是不同的完整 bulk；不能只因都含三阶导数便把它们认作同一组门。

## 6. 新 $H_0$ 确实不由此前全部条件推出

下面给有限参数证明，而不是以“未检查”代替独立性。选 R280 的一个最后完整 block；其余四个保持不动。使用 R279 的同一个 $\mathcal F$-正则基点、有限纠正方向和三个真实 high–low–high 基本位置

$$
t_1<t_2<t_3,\qquad
\lambda_1<0,\quad\lambda_2>0,\quad\lambda_3<0.
$$

每个位置的扰动仍复制到这个 block 的全部原八/十二副本；不改变相位包装、方向系数或最终中心。取原 even cutoff $\chi$，令

$$
K_\chi=\int(u_0'')^2\chi^2>0,\qquad
\mathcal W=\sum_\nu\gamma_\nu^4>0,\qquad
s_0=\frac{\mathcal W K_\chi}{128}>0.
\tag{22}
$$

设基本位置为 $X+t_i$，真实副本偏移为固定 $d_\nu$。在
$z_iN^{-3}\chi\cos Ny$ 及原有限 $\mathcal F$-纠正下，三个量

$$
(-H_0,L_c,M_c)
$$

的准确函数，在固定有限正幅盒内以 $C^1$ 收敛到一个基线加三条平方向量：

$$
b+\sum_{i=1}^3z_i^2\lambda_i
\begin{pmatrix}k_0\\ \mathcal S(X+t_i)\\ \mathcal T(X+t_i)\end{pmatrix},
\qquad k_0=2\mathcal W K_\chi=256s_0>0.
\tag{23}
$$

这里 $\mathcal S,\mathcal T$ 是保全部实际副本权与偏移的 principal 多项式。原 R279 的 bulk 给

$$
\mathcal S(X)=s_0X^{10}+O(X^9),\qquad
\mathcal T(X)=-3s_0X^9+O(X^8).
\tag{24}
$$

$O$ 项是固定的真实多项式；其系数可以依赖母包和全部副本，未把它们设为零。$k_0$ 没有位置权，因为 $K_{0,i}$ 不含 x。

### 6.1 三条 principal 行真正独立

对三个固定不同的 $t_i$，将(24)在共同大正 X 展开。行列式的首项是

$$
\begin{aligned}
&\det
\begin{pmatrix}
1&1&1\\
\mathcal S(X+t_1)&\mathcal S(X+t_2)&\mathcal S(X+t_3)\\
\mathcal T(X+t_1)&\mathcal T(X+t_2)&\mathcal T(X+t_3)
\end{pmatrix}\\
&\qquad
=135s_0^2X^{16}
 (t_2-t_1)(t_3-t_1)(t_3-t_2)+O(X^{15}).
\end{aligned}
\tag{25}
$$

系数由
$10(-108)-45(-27)=135$ 给出；相同次数以上的未知低项不存在，真实副本偏移只改 $O(X^{15})$。所以一次选足够大的有限 X 后，(23)的三行确实独立。非零 $\lambda_i$ 与严格正 $z_i$ 只分别乘非零列因子，不改变秩。

### 6.2 在准确双能量零曲线内改变 $H_0$

R279 的严格正 principal balance 先给一个严格正幅点 $z^*$，使(23)的后两行准确为零；固定中幅时两外幅的二维 Jacobian 可逆。

其同纤维纠正对 z 的导数在 $C^3$ 中为 $O(N^{-1})$，且(18)的 $H_0$ 与(21)一样是 $C^2$ 系数乘 $(u''')^2$ 的积分。因此原 R279 的 $C^1$ 收敛证明同时适用于这第三个观测，不需要把 N 取成无穷的实际 profile。

由(25)，在一个充分大的**有限** N 上：

- $L_c=M_c=0$ 具有经过所选正幅根的一条真实局部 $C^1$ 曲线；
- 沿这条曲线，$H_0$ 的导数非零。否则三行微分不可能满秩；
- 于是可取曲线上一个仍严格正幅的真实点，使 $H_0\ne0$。

每个 z 都经过同一个固定有限 $\mathcal F$-IFT，故全部原二次矩、全部 Gaussian self/ordered 数据、72面积条件与其五块正权准确不变。该完整 block 的 $L_c,M_c$ 始终为零；原十二包装给 $L_s,M_s=0$，共振身份给 $N_c=N_s=0$。完整第三的八复制仍按原参数族成立，最后 $I_0$ 归一值也由 $\mathcal F$ 保持。

其他最后 block 不动时，全局 $H_0$ 等于该非恒定函数乘一个固定正四次幅权再加常数，故同样可避开零。完整圆依然合法、非退化、支持不交。其新的 seed 与目标按原构造共同定义，不冒作某个旧固定 seed 的任意自由变换。

得到准确结论：

$$
\boxed{
\text{三矩、完整第三、全部72面积和六能量}
\quad\not\Longrightarrow\quad H_0=0.
}
\tag{26}
$$

这没有评估 R280 任一具体选择的根，也没有说其全部根都失败；它明确排除了把旧条件直接当成新平方门证明的做法。

## 7. 后继的可归因问题与边界

下一项确实需要在同一个圆上支付(18)，并继续检验(7)、(8)其余九个乘积。一个可审的后继接口是同时处理

$$
(H_0,H_1,H_2,L_c,M_c).
$$

其高频 principal 的前三个位置权来自
$4(u'')^2\chi^2(1,x,x^2)$，后两项由原 S、T 给出；在共同大正位置上引出五个不同幂次
$\{1,x,x^2,x^9,x^{10}\}$。这提示用六个真实交替 high/low 位置建立五维正 balance，再作有限频率 IFT；但本稿**没有**为此声明完整 Chebyshev 符号、正锥、五变量根或全部其余乘积已支付。

实际后继必须保 $H_2$ 的低阶基线、所有副本权和偏移，以及每个有限 N 的原 $\mathcal F$ 数据。不得把 principal 可达性当作完整根，也不得靠改变最后位置破坏已付面积。

零层、一层、其余对称二层、canonical period 与其端点条件、全路径 homogeneous 联立以及更高阶非线性问题仍在。R280 的72面积和六能量正面结论保持不变；本稿新增的是完整原第四式中此前没有支付的、确实独立的一项必要门。

