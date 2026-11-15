# R360：完整 P–Y 第二 self、有序尾与六维中层正锥

日期：2026-11-15。**有限纸面建设性证明；未执行求积、符号程序、参数扫描、人工检查或研究计算。**

[R357](R357-genuine-mother-fibers-and-a-three-dimensional-ordered-profile-cone.md) 已给真实母纤维
$\mathcal F_\kappa=0,\mathcal J/h=\eta,\mathcal K/h=\zeta$
和含真实有序历史的 $(Q,S,V)$ 三维正锥。
本稿只增加一个新的完整外矩：$\mathcal P_2=0$。
它与旧 $\mathcal D_1,\mathcal C_0$ 同权，不能只在旧锥旁添两个未经证明独立的行。

关键原恒等是
$S_{P,Y,2}=-2S_{R,Y,1}-2S_{S,Y,1}-\mu_1\mu_2$。
真实跨核把最后一项补成完整有序 $\mu_1/\mu_2$ 尾，而不是使它消失。
由此得到六个实际同权目标的严格正锥，再与 [R359](R359-exact-same-weight-quotient-and-four-dimensional-cone-pay-the-Gaussian-PY-zero-moment.md) 的
$(\mathcal B_1,\mathcal P_0)$ 四行真实正锥和旧 $\mathcal C_2$ 两行接合。
所有同权代价和最终负 $\Psi$ 储备均保留。

本稿依赖的其他原来源为
[R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、
[R263](R263-ordered-Gaussian-area-81-scalar-recursion.md)、
[R267](R267-amplitude-width-shapes-pay-the-complete-minus-one-minus-three-area.md)、
[R270](R270-odd-mother-perturbation-pays-a-further-Gaussian-zero-moment.md)、
[R271](R271-six-complete-blocks-pay-the-first-two-positive-negative-Gaussian-moments.md)、
[R278](R278-third-slope-gap-masses-break-the-first-moment-halfplane.md)、
[R291](R291-exact-positive-Gaussian-square-moment-is-the-leading-energy.md)、
[R346](R346-positive-six-target-cone-pays-a-further-complete-Gaussian-zero-moment.md)、
[R349](R349-complete-second-self-and-positive-cone-pay-the-fourth-Gaussian-area.md)、
[R353](R353-ordered-tails-and-three-positive-centers-pay-the-positive-minus-two-first-moment.md)及
[R354](R354-complete-reflection-and-positive-omega-bridges-pay-three-remaining-Gaussian-moments.md)。

## 1. 原规范与新目标

保持原 $P,R,S,L,U,Y$、$W_*=aR+bS$、$Z_*=dL+eU$，
同一右锚 $J$，以及 R357(1) 的共振参数。特别
$$
b\ne0,\quad a-b\ne0,\quad
\Gamma_\kappa=\frac{d^2-e^2}{d+7e}\ne0,\qquad
c_\kappa=\frac{5d+7e}{5(d+7e)}.
\tag{1}
$$
对 $\phi=f\cos\theta+g\sin\theta$、$D=f\odot f-\phi\odot\phi$，
仍用六个 pair 的完整外矩
$\mathcal M_j,\mathcal A_j,\mathcal B_j,\mathcal C_j,\mathcal D_j,\mathcal P_j$。
$I_2(u,w)=\int(x^2u''w''+2u'w')$；第二项始终保留。

下文 $E_{22},E_{04}$ 均为 $2I_j$ 的原 even 系数，
$E_p=E_{22}-E_{04}$。
新目标 $\mathcal P_2=0$ 是两个实际 even 系数全零；
其 odd 部分由原十二完整副本清掉。
非零原 Gaussian 常数只同乘该 pair，不改变这个准确门。

先在正半轴构造强完整原型，再按 R354 与其完整反射配对。
本稿只在有必要时对这个配对的正半块求 $Q,S,V$；
$\mathcal P_1$ 在配对后为零，不能再把它当一个自由实际目标。

## 2. P–Y 的完整 nonlegal 第二 self

令 $u$ 为任意实紧输入，$v=u',r=u''$，
$$
C=J(x^2r^2+2v^2),\qquad \mu_j=I_j(u,u).
$$
单包的三矩通常非零，$P(u,u),Y(u,u)$ 通常有真实左尾。
原 local cubic 为
$$
F_{P,2}=\int\left(\frac43xr^3-2vr^2\right),\qquad
F_{Y,2}=0.
\tag{2}
$$
第一式直接来自 $P'= -r^2,P''=-2rr'$；
第二式是 R291 已付的完整原恒等，不从合法复 profile 的特例推出。

R259 原 local 变分／Green 式给
$$
S_{P,Y,2}
=D_{\rm loc}F_{P,2}[Y(u,u)]+G_2(P,Y).
$$
左尾为 $P=\mu_0$、$Y=-\mu_2x^2/4$。
完整 $I_2$ 的 Green concomitant
$$
x^2(U'''V-U''V'+U'V''-UV''')
+2x(U''V-UV'')-2(U'V-UV')
$$
在这两个尾上为零，右端亦为零。因此 $G_2(P,Y)=0$；
不是把单包 $P,Y$ 当成紧方向。

原输出及其导数为
$$
Y=-xu^2+x^2uv-\frac{x^3v^2}{2}-\frac{x^2C}{4},
$$
$$
Y'=-u^2+x^2ur-x^3vr+\frac{x^4r^2}{4}-\frac{xC}{2},
$$
$$
Y''=-2uv+2xur-2x^2vr+x^2ur'-x^3vr'
+\frac{x^4rr'}2-\frac C2+\frac{x^3r^2}2+xv^2.
\tag{3}
$$
于是
$$
D_{\rm loc}F_{P,2}[Y]=
\int\{4r(xr-v)Y''-2r^2Y'\}.
$$
其中原 $C$ 系数是
$2vr-xr^2=(v^2)'-xr^2$，准确给
$$
\int v^2(x^2r^2+2v^2)-\int xCr^2.
$$
含 $r'$ 的全部项为
$$
4x^3ur^2r'-6x^4vr^2r'-4x^2uvrr'
+4x^3v^2rr'+2x^5r^3r'.
$$
分别按 $(r^2)'/2,(r^3)'/3,(r^4)'/4$ 做紧 outer 的 IBP，得到
$$
\boxed{
\begin{aligned}
S_{P,Y,2}={}&
\int\left[
2u^2r^2-12xuvr^2+9x^2v^2r^2+4x^2ur^3
-\frac{16}{3}x^3vr^3+x^4r^4+\frac{v^4}{3}
\right]\\
&-\int xCr^2.
\end{aligned}}
\tag{4}
$$
真实 primitive 没有消掉。

与 R353(4)、(5) 的两个完整 self 逐项比较，恰为
$$
\boxed{S_{P,Y,2}=-2S_{R,Y,1}-2S_{S,Y,1}-\mu_1\mu_2.}
\tag{5}
$$
最后一项来自 R353 的 $-\mu_1\mu_2/2$ 真 Green 余项。
只在母包上比较 local 密度而忘记它会得到错误的 whole 结论。

## 3. 补回原 Γ 后的有序尾

对严格不交的 rank-one 微包，记原幅为 $a_i,b_i$，
$c_i=a_i\cos\theta+b_i\sin\theta$、
$d_i=a_i^2-c_i^2$，母矩为 $\mu_{\ell i}$。
R259 给
$$
\Gamma_{P,Y,2}(\mu,\nu)=-\mu_1\nu_2,\qquad
\Gamma_{S,Y,1}(\mu,\nu)=-\mu_2\nu_1/2,\qquad
\Gamma_{R,Y,1}=0.
\tag{6}
$$
所以完整 $2I$ 角函数满足
$$
\boxed{
\mathcal P_2^{\rm raw}
=-2\mathcal RY_1^{\rm raw}
-2\mathcal SY_1^{\rm raw}-T_{12},
}
$$
$$
T_{12}=
\sum_i c_i^2d_i\mu_{1i}\mu_{2i}
+\sum_{i<j}c_i^2d_j
(\mu_{1i}\mu_{2j}+\mu_{2i}\mu_{1j}).
\tag{7}
$$
$\mathcal RY_1,\mathcal SY_1$ 在此分别指原 $[R,Y]$、$[S,Y]$ 外矩。

只有现在才使用整个 $D$ 的三矩为零。
两个相关矩给
$$
T_{12}
=\frac12\sum_{i<j}
(a_i^2d_j-a_j^2d_i)
(\mu_{1i}\mu_{2j}+\mu_{2i}\mu_{1j}).
\tag{8}
$$
式(8)只含 $\sin^2\theta,\cos\theta\sin\theta$；
它的 even 系数相同，不含独立的 pure 差。
因此
$$
\boxed{
\mathcal R:=
E_p^{P,2}+\frac2bE_p^{D,1}
=\frac{2(a-b)}b E_p^{RY,1}.
}
\tag{9}
$$
这是真实 whole 恒等，不要求单个微包三矩为零。

在普通／伴随两版中，$\theta=\pi/2$ 的 squared densities 相同。
以辅助中心零的实际配置作共同平移，写
$$
\mu_{1i}=m(\xi+\delta t_i),\quad
\mu_{2i}=m\{(\xi+\delta t_i)^2+\nu\delta^2w_i^2\}.
$$
原 R278 gap 匹配也保真实二次项 $\nu w_i^2$。
real weights 与平方密度关于辅助中心成镜像，故(8)的 $\xi^3$、$\xi\delta^2$ 两项准确为零。
与 R271 原 $P_1$ 的同一个 prefix 比较，得到
$$
\boxed{(T_{12})_{04}=3\xi^2V+\delta^3\Theta_{12},}
\tag{10}
$$
$V=-E_{04}^{P,1}/\xi$ 为 R357 的正半块真实坐标。
$\Theta_{12}$ 保留全部有限 self、宽度矩和内部次序。
八／十二完整副本的四次加权中心为零；其真实方差只增加
$\Theta_{12}$，不改变 $3\xi^2V$。
这里没有把所有副本的物理中心偷换成同一个中心。

## 4. 新局部商与实际母形

R353 完整 self 还给
$$
S_{R,Y,1}=-S_{L,Y,0}-\frac1{12}\int(v-xr)^4.
$$
对偶母 $u$ 的真实 $\eta_{w,\xi}$，
$$
S_{R,Y,1}(\eta_{w,\xi})
=-\frac7{24}\frac{C\xi^4}{w}
+w\xi^2B_R+w^3D_R,
$$
$$
B_R=-U_3+5N-\frac72V_2-\frac74X_2.
\tag{11}
$$
$D_R$ 是同一个实际母的完整中心零值；不当成独立输入。
由 R357(3)—(5)，
$$
\boxed{
B_R+\frac74C\nu
=-\frac{\mathcal K}{2}-c_\kappa\mathcal J.
}
\tag{12}
$$
原 $Z$–$Y$ 第零 self 则满足 R346 的准确身份
$$
B_Z-6a_{4,Z}C\nu=\Gamma_\kappa\mathcal J.
\tag{13}
$$

先取普通两斜率 $(\alpha,\beta)$。对每个最后正中心，全部 finite-copy 数据已固定后，两个 local pair 的 $E_{04}$ 准确有
$$
E_{04}^{RY,1}
=K_\alpha\delta\xi^2(1-q^2)
\left(-\frac{\mathcal K}{2}-c_\kappa\mathcal J\right)
+\delta^3\Theta_R,
$$
$$
E_{04}^{C,0}
=K_\alpha\delta\xi^2(1-q^2)
\Gamma_\kappa\mathcal J+\delta^3\Theta_Z,\qquad
K_\alpha=64na_c\mathcal W>0.
\tag{14}
$$
并且整个有限式均有 $E_{22}=\alpha\beta E_{04}$。
这是 R270 原四阶中心多项式与真实方差的直接代入，最后两项含全部第四中心矩，未删掉。

对 R357 的三斜率 mid 版本，必须把 $\alpha\beta$ 改为其(23)的真实系数。
相同宽度的零至四次矩匹配使(14)的 local 消项仍成立。
因此在 R357 的共同基点 $\mathcal J=\mathcal K=0$，
$$
E_p^{RY,1},\ E_{04}^{RY,1},\
E_{22}^{C,0},\ E_{04}^{C,0}=O(\delta^3)
\tag{15}
$$
对每个已固定有限布局成立。
这里没有从 leading 零宣称有限 $\delta$ 的这些量本来为零。

## 5. 同一个 Q,S,V 正锥进入新三行

需要核完整平移，不能只平移外面的 $x^2$。
R353 的 self 及原 Γ 给
$$
\partial_\xi\mathcal RY_1=\mathcal RY_0,\qquad
\partial_\xi\mathcal SY_1=\mathcal SY_0+\mathcal P_1.
\tag{16}
$$
它同时给
$$
\partial_\xi S_{R,Y,0}
=\int(-2ur^3+10xvr^3-7v^2r^2-\tfrac72x^2r^4),
$$
$$
\partial_\xi S_{S,Y,0}
=S_{P,Y,0}
+\int(\tfrac{10}{3}xvr^3-v^2r^2-\tfrac23ur^3-\tfrac32x^2r^4).
\tag{17}
$$
跨核满足
$\partial_\xi K_{3,0}=K_{1,0}$，所以第二式确能补成 whole 公式。

以 R357 的原母恒等 $X_2-C\nu=8N/5-16e\mathcal J/[5(d+7e)]$ 支付该项后，(17)的两个 local 余量分别是
$$
-\mathcal K-2c_\kappa\mathcal J,\qquad
\mathcal K+\left(-\frac23+\frac{24e}{5(d+7e)}\right)\mathcal J
\tag{18}
$$
乘原真实 quartic 宽度权和。
第一式也直接由(11)对中心求两次导数得到。
原三斜率版本的 local 值由 R278 相同宽度匹配而相同；不是重新沿用旧 $\alpha\beta$ 比例。

在 $\mathcal J=\mathcal K=0$ 上，local 两项全零。
pure 槽的 $\mathcal P_1$ 为零，common 槽有
$E_{04}^{P,1}=-\xi V$。
积分(16)—(17)，保辅助中心零的完整真实常数，再用(10)，得到
$$
\boxed{
\begin{aligned}
E_p^{D,1}&=\frac{b\xi^2}{2}Q+O(\delta^2),\\
E_{04}^{D,1}&=\frac{b\xi^2}{2}(S-V)+O(\delta^2),\\
E_{04}^{P,2}&=-\xi^2(S+2V)+O(\delta^2).
\end{aligned}}
\tag{19}
$$
$Q,S,V$ 本身准确为 $O(\delta)$。
这些余项来自实际辅助中心值和有限副本偏移；其系数在已经固定的有限 $n,N,A$、母与中心上连续有界。
具有原完整内部反射时余项还可写为 $O(\delta^3)$，本稿不需要这个加强。
从头至尾只需固定一个有限正 $\delta$ 的严格正核稳定性。

(19)的 leading 线性变换是
$$
(Q,S,V)\longmapsto
\left(\frac b2Q,\frac b2(S-V),-S-2V\right),
\qquad \det=-\frac{3b^2}{4}\ne0.
\tag{20}
$$
每列另乘 $\xi^2>0$，不改变正锥。
故 R357 的六个真实 top 原型在前三行上给三维严格正锥；
其剩下三行
$(E_{22}^{C,0},E_{04}^{C,0},\mathcal R)$
除以 $\delta$ 后趋零，依据是(9)、(15)。

## 6. 两个实际母坐标给三个缺失的 local 方向

这一节只调用 R357 已证明的实际小族(14)，不重新研究母根。
选两个不同 $\alpha_1,\alpha_2$，在 $19/40$ 的小邻域中，
令 $\beta_i=(5-\alpha_i)/(1-\alpha_i)$。
$\alpha\beta$ 严格递增，且此邻域 $\alpha\beta\ne1$。

先分别在两个斜率上取
$$
\mathcal J=\pm h\eta_0,\qquad
\mathcal K=-2c_\kappa\mathcal J,
\tag{21}
$$
其中 $\eta_0>0$ 固定足够小。
(12)使 $\mathcal R/\delta$ 的 leading 为零，
而 $(E_{22}^{C,0},E_{04}^{C,0})/\delta$ 沿
$$
\pm(\alpha_i\beta_i,1)
$$
取得严格非零真实极限。

另在一个斜率上取
$$
\mathcal J=0,\qquad \mathcal K=\pm h\zeta_0,
\tag{22}
$$
$\zeta_0>0$ 小且固定。
两个 C0 行的 leading 为零；
由(9)、(12)，$\mathcal R/\delta$ 取得两个严格相反非零值：
系数含
$(a-b)(\alpha\beta-1)/b\ne0$。

因此这六个实际母选项在底部三行形成满秩3且含严格正 kernel 的极限矩阵。
所有原型仍保 $\mathcal F_\kappa=0$、原三矩和整个
$\mathcal M_j,\mathcal A_j$。
没有假定它们保持原 $\mathcal H$ 或旧六能量根。
其前三个有序目标均保为完整真实有限值。

把这六列和§5六列共同除以各自正 $\delta$，
在三维 top／三维 local 坐标上得到
$$
M_\delta\longrightarrow
\begin{pmatrix}T_3&D\\0&L_3\end{pmatrix}.
\tag{23}
$$
$T_3,L_3$ 各满秩3并含严格正 kernel。
先取 $L_3$ 的正 kernel，再用 $T_3$ 的全正锥消掉 $D$ 的真值并加入正 kernel，就得(23)的严格正 kernel。
它满秩6。固定一个非零六列 minor，保持其余坐标，
便可在足够小的**实际有限正** $\delta$ 上纠正残差，正性保留。

六个坐标
$$
(E_p^{D,1},E_{04}^{D,1},E_{04}^{P,2},
E_{22}^{C,0},E_{04}^{C,0},
E_p^{P,2}+2E_p^{D,1}/b)
$$
与原 $(\mathcal D_1,\mathcal C_0,\mathcal P_2)$ 六行之间是固定可逆变换。
因此
$$
\boxed{
\operatorname{cone}_+
\{(\mathcal D_1,\mathcal C_0,\mathcal P_2)
\text{ 的十二个实际列}\}=\mathbb R^6,
}
\tag{24}
$$
且实际矩阵有严格正 kernel。
每个最后中心从一开始固定；所有最后支撑不交后才评价真实列。
有限项没有被设成零；它们通过同一个真实 minor 的连续稳定性支付。

现在将每个完整正半原型与其完整空间反射配对。
六个目标均为 reflection-even，实际列共同乘2；
原 rank 和正 kernel 保持。
被反射清掉的旧 odd 外矩及全部 angular odd 位置不重新出现。


## 7. 同权低层四行必须一起保留

本节使用 R359 已给的实际低层库：
$$
L_4:\quad(\mathcal B_1,\mathcal P_0)\in\mathbb R^4,
\qquad \operatorname{rank}L_4=4,\quad
\ker L_4\text{ 含严格正向量}.
\tag{25}
$$
它从 R357 的三个有序坐标和一个真实 local 商构造，
不是将这四行分别可控直接拼接。
其余旧门按 R359 的实际反射范围保留，$\Psi$ 为有限正成本。

$\mathcal B_1$ 和 $\mathcal P_0$ 的完整伸缩权都为 $-5$。
所以在本稿任何伸缩中，它们都必须作为同一低层处理；
不能把新增 $\mathcal P_0$ 代价估为较低阶而删去。
(25)每列的 $\mathcal D_1,\mathcal C_0,\mathcal P_2,\mathcal C_2$ 真值全部保留。

把§6的十二个 middle 原型共同作大有限正伸缩 $H$，
并令第四幅度乘 $H^3$。完整权为
$$
\boxed{
(\mathcal B_1,\mathcal P_0):-5,\quad
(\mathcal D_1,\mathcal C_0,\mathcal P_2):-3,\quad
\mathcal C_2:-1,\qquad \Psi:-7 .
}
\tag{26}
$$
这些来自原 E8 算子及两个原 $I_2$ 项的准确齐次性。
例如 $P$ 权 $-3$、$Y$ 权 $+1$，
$[P,Y]$ 三次场权 $-2$，$I_2$ 的两项同给总 $-3$；
本稿没有只计 $x^2u''w''$。

因此 middle 的低层四行是 $O(H^{-2})$，中层六行固定。
其实际十行矩阵趋于
$$
\begin{pmatrix}
L_4&0\\
D_6&M_6
\end{pmatrix},
\tag{27}
$$
其中 $D_6$ 是旧低层库的六个真实代价，$M_6$ 为(24)。
两个对角块都有全正锥。先取 $L_4$ 的正 kernel，
再用 $M_6$ 付 $D_6$ 并加正 kernel，得到(27)的全分量严格正 kernel。
它行秩10。固定非零十列 minor，便可在一个足够大的**有限** $H$
上保 rank10 和严格正 kernel。
没有将 $D_6$ 设零，也没有假设旧四行与新六行无关。

最后加入 R349 的四个真实 $\mathcal C_2$ 原型及其完整反射。
取另一个大有限伸缩 $H_2$，第四幅度乘 $H_2$。
低层四行为 $O(H_2^{-4})$，中层六行为 $O(H_2^{-2})$，
新 $\mathcal C_2$ 两行保持其严格二维正锥。
旧库的 $\mathcal C_2$ 真值保为左下块。
同一论证给一个完全真实有限矩阵
$$
\boxed{
M_{12}:\quad
(\mathcal B_1,\mathcal P_0;\
 \mathcal D_1,\mathcal C_0,\mathcal P_2;\
 \mathcal C_2),\qquad
\operatorname{rank}M_{12}=12,\quad
\ker M_{12}\cap(0,\infty)^{24}\ne\varnothing .
}
\tag{28}
$$
这里共有 $8+12+4=24$ 个实际完整镜像列；12是已证明的这份具体矩阵行秩；不把整个72接口的位置数当成独立秩。
所有列都是实际正幅可并置的完整 blocks。
新组的正支撑可通过上述同一次有限伸缩放在旧组右方，负支撑则为其完整镜像；
原始有限 profiles 的中心没有在评价以后被另行移动。

## 8. 同一个最终弱圆支付最后一个面积外矩

从 R359 最后强控制器以前的实际偶弱基线接入。
其所有已付17矩为零，$\Psi=-\Delta\sin^2\theta$、$\Delta>0$，
当前 $\mathcal P_2$ 的完整 residual 为 $r\in\mathbb R^2$。
此基线包括原弱幂段、局部常量、远宽 cutoff、三矩回补及后继全部真实中心；不以一个未补矩 core 替代。

固定(28)的严格正 kernel $k$ 和实右逆 $R_{12}$。
把整组真实新原型共同伸缩 $S$，第四幅度写成 $S^5c_i(S)$。
按(26)，低层四行缩放1，中层六行缩放 $S^2$，高层两行缩放 $S^4$。
令
$$
c(S)=k+
R_{12}\big(0_{\mathbb R^4};
\,0_{\mathbb R^2},0_{\mathbb R^2},-r/S^2;
\,0_{\mathbb R^2}\big).
\tag{29}
$$
充分大的有限 $S$ 使 $c(S)>0$ 且有界。原矩阵身份准确给
$$
\Delta\mathcal B_1=\Delta\mathcal P_0
=\Delta\mathcal D_1=\Delta\mathcal C_0=\Delta\mathcal C_2=0,\qquad
\Delta\mathcal P_2=-r .
\tag{30}
$$
全部其他已付面积在每列自身为零；
反射清掉的 odd 外矩也继续为零。
所有完整 blocks 的 $D$ 三矩各自为零，
故 R259/R263/R325 的完整加法消去跨完整 blocks 的尾；
微包内部的真实 tail 已在§2—6与每列原值中全部保留。

若固定原型的真实正 $\Psi$ 系数为 $\psi_i$，
新增成本准确为
$$
S^{-2}\sum_i c_i(S)\psi_i\,\sin^2\theta.
\tag{31}
$$
有限 $S$ 可使它小于 $\Delta/2$，并使所有正、负新包络分别位于旧偶基线支撑两端之外。
原基线中心不动，不在归零以后再整体平移。

现在全部18个面积外矩准确为零，$\Psi$ 仍有严格负余量。
最后使用 R354 已接好的**成对反射**强控制器，
在从起点选定的有限 $F^\star$ 纤维中取一个有限频率，
支付三个 directed 行并令 $\Psi=0$。
该控制器自身的全部72 Gaussian面积为零，
有限纤维变化保留这些实际原值；因此不会重开(30)。
高频只发生在新强 blocks 中，原弱单 hook/rank-two 核心及其真实 histories 固定。

(29)特意同时含 $\mathcal P_0$ 与 $\mathcal B_1$。
若没有(25)的真实四行联合库，只保 $\mathcal B_1$ 的两行并不能推出(30)；
本稿不使用那个错误的同权三角替代。

## 9. 有限选择、物理区间与完整 scope

选择顺序为：

1. 先取 R357 的实际母根、小族、共同紧支撑和有限三排序数据。所有宽常量、原子及母宽都是有限真实量。
2. 对§5 top 六列，固定 R357 的 finite $n,A,N$ 及实际复制；对§6 local 六列，固定两种斜率及两形状符号。先固定不同的最后正中心，再取共同有限正 $\delta$ 得(24)。
3. 读取 R359 的真实低层四行库；它的全部中、高层成本保留。依次固定有限 $H,H_2$，取得(28)和所有实际 disjoint 支撑。
4. 取有限 $S$ 和(29)的实际正四次幅，同时支付最后 residual、保旧17矩并留负 $\Psi$。
5. 最后固定成对强控制器及一个有限频率，完成 directed 三行和 $\Psi$。整圆公共正归一化只同乘零等式，不改变结论。
6. 所有有限 supports，包括负半轴反射模块，确定以后，再按 R354 的原归一规则选足够大的 $\omega$ 下界和足够小的初始 $h_e$，实际安装同一闭 hook 几何、共振保护芽和共同合法区间。归一计算中的所有 Gaussian行只受原非零尺度因子影响，零等式保留。

最后一步不许偷换成任意已经冻结旧几何或窄区间的免费扩域。
本稿也不把其他几何上已付的 universal pure、whole self 或全部 period 自动移植到这里。
所用实际几何保证的层级仍是 R354 的
$M=0,T=\kappa_H\mathfrak H$、非零 hook 与指定共振芽。

最终同一个真实偶弱圆保非零 derivative rank-two 开段，
并且
$$
\boxed{
\mathcal M_j=\mathcal A_j=\mathcal B_j
=\mathcal C_j=\mathcal D_j=\mathcal P_j=0
\quad(j=0,1,2)
}
\tag{32}
$$
对全部 $\theta$ 成立。
原三矩、完整第二／第三 range、
$\Psi=F_0=F_1=F_2=0$ 及原指定一层均保留。
在 R259 的规范中，六个 pair 的18个外矩及其全部72形式角位置已经在这个同一最终圆上支付。

这只完成全部 Gaussian **反对称二history面积**。
它不自动授全部对称乘积、整个零／一history函数、canonical第四 period、
同一补偿 gauge 的 joint ruling或整个第四阶解。
任何这些后继门都必须继续使用当前同一最终 profile 的原式，而不能以本稿的面积正锥代替。
