# R993 — 原十三核的实际 Z 单位、两个共同 frame 权与全来源余式

日期：2026-11-26 UTC。**已证明：原指定特征 $p$ primitive $Z$ 在两条十三核的所有非零点均为单位；其全部值由一个固定一次多项式给出，完整 resultant 是 $6912\pi(4+\delta)$。同 degree130 的 canonical 平移在原 $P_2$ 有理模型中的整个 frame 缺陷可用同一个明确乘子表示。每个六点轨道的零阶缺陷因此是一个真实共同权乘以该轨道的完整质量行；没有把 $P_2(T)$ 设成一。**

公开原完整执行已给两个 rank≥2 来源在两十三二次商的准确比例为 $-11(1\pm\delta)/40$，两支可除重数均恰为一；完整首非零除商也已返回。原已知 old 差与 primitive 行在每个二次商的行列式为明确非零单位。以下同时把两个从 $z^{12}$ 起的实际来源接到 R711 的同一个第六 Cartier 行，保持全部低卷积及原点以外的极部。

## 1. 原对象、两个实际核与绝对相位

始终取 R887 的同一个模型与指定函数：
$$
 E_1:y^2=x^3+1,\quad dz=\frac{dx}{2y},\quad
 x=z^{-2}+\cdots,\ y=-z^{-3}+\cdots,
 \quad p=6s-1>211.
 \tag{1}
$$
记
$$
 \delta^2=-3,\quad \omega=(-1+\delta)/2,\quad
 \pi=(7+\delta)/2,\quad \bar\pi=(7-\delta)/2,
 \quad X=x^3,
$$
$$
 R(X)=X^2+(2+6\delta)X+(40+24\delta)/13,
 \qquad \sigma(\pi z)=\pi\sigma(z)^{13}R(X(z)).
 \tag{2}
$$
非零 $\pi$ 核分成 R987 的两个实际六点轨道，$X$ 值为
$$
 t_\pm=-1-3\delta\pm6\delta/r,\qquad r^2=\pi.
 \tag{3}
$$
共轭核使用 $\bar R$，与 R987 同取 $s_{13}=g/r$、$s_{13}^2=\bar\pi$；指定根 $-1+3\delta-6\delta/s_{13}$ 相对 Weyl-dual 正轨道的实际符号仍为 $-1$。本篇没有重新择根或改变这个相位。

原特征 $p$ 数据是
$$
 c_p=\binom{3s-1}{2s-1}\in\mathbf F_p^\times,\qquad
 Z=\frac{\mathscr R_p(x)}{y^p},\qquad DZ=1,
$$
$$
 G=\sum_{i=0}^{p-2}\frac{(-1)^iZ^{i+1}D^i(-x)}{(i+1)!},
 \qquad H=G+x^2/y,\qquad
 P=\mathcal P_2=-(D-2G)^{p-1}Z^{p+1}.
 \tag{4}
$$
这里的 $\mathscr R_p$、原常数坐标与完整 $p$ 基乘法都逐字沿 R887；没有添加一个水平项。特别 R887(46) 已付原 $\rho_p=c_p^{-1}$，而 $P$ 的所有极只在原三个非零二挠点。

对任一非零十三核点 $T$，令
$$
 \lambda_T=\zeta(T)-\eta(T),\qquad
 L_T=\lambda_T+x(T)^2/y(T).
 \tag{5}
$$
$\eta$ 是与原 sigma 相同的准周期反线性延拓。R887(51) 给 $\lambda_T$ 的固定代数有限和，(54) 准确给
$$
 \boxed{Z(T)=(-c_p^{-1}L_T)^p.}
 \tag{6}
$$
式 (6) 中保留 $p$ 次方；十三点及其常数不必定义于 $\mathbf F_p$。

## 2. 两个原核上的完整 L 值与固定坏集合

对 $T\in E[\pi]\setminus\{O\}$，在 $z=T+v$ 处取 (2) 的对数导数：
$$
 D\log R(X(z))=\pi\zeta(\pi z)-13\zeta(z).
$$
因 $\pi T\in\Lambda$，右边在 $v=0$ 的常数项恰为 $-13\lambda_T$。左边的常数项为 $D^2R(T)/(2DR(T))$，所以
$$
 \boxed{\lambda_T=-\frac{D^2R(T)}{26DR(T)}.}
 \tag{7}
$$
这同时支付实际准周期项；没有把 $\zeta(T)$ 单独当成代数数。

原微分给
$$
 DX=6x^2y,\qquad D^2X=6x(7X+4).
$$
代入 (7)，再用 $R(X)=0$ 完整约化，得到
$$
 \boxed{
 L_T=-\frac{(34+42\delta)X+88+72\delta}
                  {26xyR'(X)}\bigg|_T.}
 \tag{8}
$$
完整约化过程是
$$
 (19X-4)R'(X)-12X(X+1)
 \equiv-(34+42\delta)X-(88+72\delta)\pmod R.
 \tag{9}
$$
令 $A=34+42\delta$、$B=88+72\delta$。对首一二次多项式的准确 resultant 为
$$
 \begin{aligned}
 \operatorname{Res}_X(R,AX+B)
 &=B^2-AB(2+6\delta)+A^2(40+24\delta)/13\\
 &=\frac{3456(325+143\delta)}{13}
 =\boxed{6912\pi(4+\delta)}.
 \end{aligned}
 \tag{10}
$$
最后一步使用 $325+143\delta=26\pi(4+\delta)$。所以 (8) 在两个完整轨道均非零，不是只在选定的一根上非零。

全部分母与单位门也明确如下：

- $6912=2^8 3^3$，$N\pi=13$、$N(4+\delta)=19$；故 (10) 只涉及 $2,3,13,19$。
- $R(0)=(40+24\delta)/13$ 的范数为 $256/13$，因此 $x(T)$ 在 $2,13$ 外为单位。
- $R(-1)=27(1-2\delta)/13$ 的范数为 $729/13$，因此 $y(T)^2=X(T)+1$ 在 $3,13$ 外为单位。
- $R'(t_\pm)^2=-432/\pi$，故 $R'(T)$ 只涉及 $2,3,13$；式 (8) 的另外一个分母是 $26$。

因此，在固定十三点域中、对每个 $p>211$ 的好惰性位，所有 $L_T$ 及 (6) 的 $Z(T)$ 均为单位。共轭支逐项取共轭，有同样的完整结论。特别
$$
 \boxed{(E[\pi]\cup E[\bar\pi])\setminus\{O\}
       \quad\text{与原 }Z=0\text{ 的其余点严格不交}.}
 \tag{11}
$$
原其它 $Z$ 零点没有因 (11) 被删除。

若需要 principal 轨道的固定权，可直接使用二次代数中的完整式
$$
 L_T^6=\frac{(AX+B)^6}
 {26^6X^2(X+1)^3R'(X)^6}\bigg|_T,
 \qquad
 \boxed{Z(T)^6=c_p^{-6}(L_T^6)^p.}
 \tag{12}
$$
本篇消费者在 $K[X]/R$ 与 $K[X]/\bar R$ 中保留 (12) 的全部两个坐标，核分母逆及整个乘回。这里 $c_p$ 在 $\mathbf F_p$ 中，只有它可先用 $c_p^p=c_p$；其余数据仍按原 Frobenius 运输。

实际完整除法返回
$$
 \boxed{L_T^6\equiv
 \frac{-203383240-191156384\delta
            +(-32450065+6966808\delta)X}{39^6}\pmod R.}
 \tag{12a}
$$
其中 $39^6=3518743761$。另一核的两个系数全部取共轭；回执核了整个逆与乘回，不只核范数或一个根。

## 3. 三个真实来源、两个 z12 差与完整质量边界

记 R972/R973 的实际两个 degree130 rank≥2 来源为
$$
 \Phi_* =\sigma^{130}x^2P_*(X),\qquad
 \Phi_{260}=\sigma^{130}x^2P_{260}(X),
 \qquad [z^6]\Phi_*=[z^6]\Phi_{260}=1.
 \tag{13}
$$
两个完整原 polynomial 的最高次数均为20，最高系数为一。R971 的 raw 六 sigma 来源是
$$
 F_{10}=\sigma^{130}x^2P_S(X)\mathcal J_5(X),
 \qquad [z^6]F_{10}=1,
 \tag{14}
$$
其中 $P_S,\mathcal J_5$ 完全按该篇原群律生成，消费者另从此式重建，不从投影结论反造 raw 输入。

R978 的两个实际 raw pull 满足
$$
 \Delta_{125}=D_\pi\Psi_{125}-D_{\bar\pi}\Psi_{125},
 \quad [z^6]\Delta_{125}=-21840\delta,
 \quad F_{10}=-\frac{11}{2}\Phi_*+\frac{\delta}{10080}\Delta_{125}.
 \tag{15}
$$
所以以下是两个同 degree、同完整 sigma frame 的真差：
$$
 \boxed{G_{65}=\Phi_{260}-\Phi_*,\qquad
 G_{\rm old}=\Delta_{125}+21840\delta\Phi_*
       =3360\delta(\Phi_*-F_{10}).}
 \tag{16}
$$
二者的实际首阶均恰为 $z^{12}$，由完整多项式最高非零项返回；没有把一个首阶仍为六的 old 差直接放进同首抵消公式。

对任一 $f=\sigma^{130}x^2P_f(X)$，R987 的同一个 canonical lift 在非零 $\pi$ 核的质量是
$$
 m_{T,f}=(T_Tf)(0)
 =\frac{P_f(X(T))}
 {6^{10}X(T)^6(X(T)+1)^5R'(X(T))^{10}}.
 \tag{17}
$$
定义其完整二次余式
$$
 m_f(X)=a_f+\beta_fX\in K[X]/R,
 \qquad \operatorname{tr}_R(m_f)=2a_f-(2+6\delta)\beta_f.
 \tag{18}
$$
两个 primitive 来源在 $Q_\pi,Q_{\bar\pi}$ 下都为零。对 $\Phi_*$，这就是 R987 的十三 quadratic 向量；对 $\Phi_{260}$，R973 的 $b=4$ 角色不同于两个核不变向量的 $b=6$ 角色，完整有限投影同样给零。因此
$$
 \operatorname{tr}_R(m_*)=
 \operatorname{tr}_R(m_{260})=0,
 \qquad
 \boxed{m_{260}=\varrho_\pi m_*,\quad
 \varrho_\pi=\beta_{260}/\beta_*\in K.}
 \tag{19}
$$
R987 实际返回 $\beta_*=-(1+2\delta)/997920\ne0$。共轭源的全部系数有理，故另一支的比例准确为 $\varrho_{\bar\pi}=\overline{\varrho_\pi}$；不能先假设它们相同。

本次实际完整22投影与二次除法进一步给
$$
 m_{260}(X)=-\frac{8+3\delta}{907200}
                    +\frac{-5+3\delta}{3628800}X,
$$
$$
 \boxed{\varrho_\pi=-\frac{11(1+\delta)}{40},\qquad
 \varrho_{\bar\pi}=-\frac{11(1-\delta)}{40},\qquad
 \varrho_\pi-\varrho_{\bar\pi}=-\frac{11\delta}{20}.}
 \tag{19a}
$$
因此两比例真正不同，其差在所有 $p>211$ 为单位。

旧差有不同的完整 trace。由 R987 的绝对 good-13 相位
$\theta=\omega^2\pi=-1-2\delta$，
$$
 Q_\pi\Delta_{125}=(1-\theta/13)D_\pi\Psi_{125}.
$$
两个非零轨道各有六点，而原点质量为零，故
$$
 \boxed{\operatorname{tr}_R(m_{G_{\rm old}})
       =\frac{13-\theta}{6}=\frac{2\pi}{3},\qquad
 \operatorname{tr}_{\bar R}(m_{G_{\rm old}})
       =-\frac{2\bar\pi}{3}.}
 \tag{20}
$$
第二式也由 $\overline{G_{\rm old}}=-G_{\rm old}$ 得到，不能误写为两个 trace 相互共轭。

为明确整条边界而不仅是 trace，本次实际返回还给
$$
 \boxed{m_{G_{\rm old}}(X)
       =\frac{444+160\delta}{297}
          +\frac{13(6-\delta)}{594}X,}
 \qquad
 m_{F_{10}}(X)=\frac{13(-1+\delta)}{90720}
                  +\frac{1+2\delta}{181440}X.
 \tag{20a}
$$
两共轭核中的 $F_{10}$ 余式为共轭，$G_{\rm old}$ 余式为负共轭。两者的完整源关系 (16) 在两个二次商中也逐项保持。

因此，在基 $(1,X)$ 中，$m_*$ 与 $m_{G_{\rm old}}$ 的完整边界行列式是
$$
 \boxed{
 \det\begin{pmatrix}a_*&a_{G_{\rm old}}\\
                         \beta_*&\beta_{G_{\rm old}}
       \end{pmatrix}
 =-\frac{\beta_*\pi}{3}
 =\frac{\pi(1+2\delta)}{2993760}\ne0.}
 \tag{21}
$$
其中 $2993760=3\cdot997920$，$N(1+2\delta)=13$，故 (21) 在 $p>211$ 为单位；共轭支的行列式是其负共轭。两条 primitive 行在每一支的零阶边界只占同一个一维方向，而 old 行补足该完整二次边界的第二维。这是实际来源的矩阵事实，并未给 old 中央赋零。

## 4. 完整可除重数与同一 frame 的逐阶取消

式 (17) 的分母在整个二次代数中可逆，所以 (19) 等价于整个多项式的准确整除：
$$
 \boxed{P_{260}-\varrho_\pi P_*=R^{e_\pi}Q_\pi,
 \qquad e_\pi\ge1,\quad Q_\pi\not\equiv0\pmod R.}
 \tag{22}
$$
本篇消费者读取的是最高可除重数 $e_\pi$、首个非零商的全部二次余式、以及整条 $R^{e_\pi}Q_\pi$ 回乘；共轭支全部同做。实际返回
$$
 \boxed{e_\pi=e_{\bar\pi}=1,\qquad \deg Q_\pi=18.}
 \tag{22a}
$$
准确的首商写成 $Q_\pi\equiv q_0+q_1X\pmod R$，其完整两个 $K$ 坐标为
$$
 \begin{aligned}
 q_0={}&-\frac{12889490753114453419200545292288}{28550575235}
       +\frac{223536810748803314020800264142848}{142752876175}\delta,\\
 q_1={}&-\frac{7324003038729297635495091634176}{1568712925}
       +\frac{30162353838072419756145270325248}{10980990475}\delta.
 \end{aligned}
 \tag{22b}
$$
这些是所用首 jet 的两个准确系数，不是存下一个生成矩阵。全部分母整除 $25\cdot7\cdot13^8$。原 $R$ 在 $K$ 上不可约，因其判别式 $-432/\pi$ 的十三赋值为奇数；因此 (22b) 在两个实际根上均非零。若须约化后仍保持这个准确首阶，另删固定非零整数
$$
 D_Q=\operatorname{num}\!\left(
 N_{K/\mathbf Q}\!\left(q_0^2-(2+6\delta)q_0q_1
              +\frac{40+24\delta}{13}q_1^2\right)\right)
 \tag{22c}
$$
的素因子；其分母已由上列固定集合支付。这里没有预认 $D_Q$ 的分子素因子都小于211。另一核的整个首商为共轭。

对于任意共同正则权 $W(P)$，完全不除以 $W(T)$ 就有
$$
 W\,x^2(P_{260}-\varrho_\pi P_*)
 =W\,x^2R^{e_\pi}Q_\pi.
 \tag{23}
$$
因此在每个 $T\in E[\pi]\setminus\{O\}$，所有小于 $e_\pi$ 的切向 Taylor 系数准确为零；第 $e_\pi$ 个系数是
$$
 \boxed{W(T)x(T)^2\bigl(DR(T)\bigr)^{e_\pi}Q_\pi(X(T)).}
 \tag{24}
$$
若 $W(T)=0$，则实际阶更高；没有把它改成一个单位。

特别可取原全部第六 Cartier 权
$$
 W=Z^{-7}P^{65},
 \tag{25}
$$
因为第2节已付 $Z(T)$ 为单位，且 $P$ 在这些十三点正则。式 (23)–(25) 对原 $P$ 的全部系数成立，未以 canonical sigma 值替换它。

这里也区分两个真实组合：$G_{65}$ 的首六阶系数为零，但在 $R$ 商中的余式是 $(\varrho_\pi-1)P_*$；$\Phi_{260}-\varrho_\pi\Phi_*$ 可除 $R$，其首六阶系数却是 $1-\varrho_\pi$。两种便利不能免费合并到同一个来源。

## 5. 原 canonical 平移的整个共同 frame 缺陷

本节的 $f$ 取上述质量零来源及其线性组合，故 $\deg P_f\le20$、$R_f$ 在 $O$ 的极阶至多124。对固定 $T\in E[\pi]\setminus\{O\}$，直接在原曲线上定义
$$
 a_T(P)=\frac{R(X(P))}{R(X(P+T))}.
 \tag{26}
$$
因平移置换整个十三核，完整除子准确为
$$
 \operatorname{div}(a_T)=13(-T)-13(O).
 \tag{27}
$$
所以 (26) 已是这个 lift 所需的原 Miller 函数，不须另择一个有限 cover 或相位。R987 的绝对 deck 式逐项消 sigma 后给
$$
 \boxed{T_Tf(P)=\sigma(P)^{130}a_T(P)^{10}R_f(P+T),
       \qquad R_f=x^2P_f(X).}
 \tag{28}
$$
在 $P=O$，$a_T(z)=z^{-13}/DR(T)+\cdots$，从而
$$
 C_T:=(DR(T))^{-10},\qquad m_{T,f}=C_TR_f(T).
 \tag{29}
$$
式 (29) 与 (17) 完全一致，保全部十次方与 $x,y$ 的符号。

把同一线性有理模型 $\widehat f=P^{65}R_f$ 代入，得到整个函数域身份
$$
 \boxed{\widehat{T_Tf}-t_T^*\widehat f
       =\mathcal W_{T,p}\,R_f(P+T),}
 \tag{30}
$$
$$
 \boxed{\mathcal W_{T,p}
       =P(P)^{65}a_T(P)^{10}-P(P+T)^{65}.}
 \tag{31}
$$
这里的两个 $P(\cdot)$ 都是原 $\mathcal P_2$。式 (30) 没有删除 R887 的 $G/P_2$ 水平初值：它将该完整缺陷保留为一个对所有同 degree 来源共同的实际函数。

由 (27)，式 (30) 在 $O,-T$ 的 apparent 极均完整抵消：在 $O$，$P^{65}$ 的130阶零与 $a_T^{10}$ 的130阶极抵消；在 $-T$，两个 frame 项均至少130阶，而 $R_f(P+T)$ 的极至多124阶。实际极仅在原二挠集合及其 $-T$ 平移，不能删掉其中任何一支。

原点的共同零阶权因此准确为
$$
 \boxed{d_{T,p}=1-P(T)^{65}(DR(T))^{10},\qquad
 (\widehat{T_Tf}-t_T^*\widehat f)(O)=d_{T,p}\,m_{T,f}.}
 \tag{32}
$$
这是真正的 $P_2(T)$ 权；它可为零，也可为非零，未被归一掉。

该权在每个实际六点轨道内保持。对 $\zeta\in\mu_6$，原 $P$ 的型为二，而 $R(X)$ 的型为零，所以
$$
 P(\zeta T)^{65}=\zeta^{130}P(T)^{65},\qquad
 (DR(\zeta T))^{10}=\zeta^{-10}(DR(T))^{10};
$$
乘积的型为 $\zeta^{120}=1$。故两轨道的实际零阶边界块准确是
$$
 \boxed{\operatorname{diag}(d_{+,p},d_{-,p})
        \begin{pmatrix}
          m_{+,*}&m_{+,260}&m_{+,G_{\rm old}}\\
          m_{-,*}&m_{-,260}&m_{-,G_{\rm old}}
        \end{pmatrix}.}
 \tag{33}
$$
这支付了共同 frame 权及全部相位。若其中一个 $d_{\pm,p}=0$，实际秩必须据此下降，不能仍借 (21) 宣称该带权块满秩。

此外，(19a) 使两条 canonical 行可以准确分离两个核。对任意相同的实际权，令 $B_\pi(f),B_{\bar\pi}(f)$ 为两核的完整零阶加权和，并写 $B(f)=B_\pi(f)+B_{\bar\pi}(f)$。则
$$
 \boxed{\begin{aligned}
 B_\pi(\Phi_*)&=
 \frac{B(\Phi_{260})-\varrho_{\bar\pi}B(\Phi_*)}
      {\varrho_\pi-\varrho_{\bar\pi}},\\
 B_{\bar\pi}(\Phi_*)&=
 \frac{\varrho_\pi B(\Phi_*)-B(\Phi_{260})}
      {\varrho_\pi-\varrho_{\bar\pi}}.
 \end{aligned}}
 \tag{33a}
$$
这使用原固定单位 $-11\delta/20$，没有选择一个依赖 $p$ 的子式。若所用全局行另含其它边界，必须先把它们保留在 $B(f)$ 的补项里；(33a) 不把 canonical 中央零自动改成这两个局部和为零。

式 (22) 还能逐阶作用于整个 (30)：其同源组合为
$\mathcal W_{T,p}\,x(P+T)^2R(X(P+T))^{e_\pi}Q_\pi(X(P+T))$。
在 $O$，小于 $e_\pi$ 的 Taylor 系数全消，首项为
$$
 (C_T-P(T)^{65})x(T)^2(DR(T))^{e_\pi}Q_\pi(X(T)).
 \tag{34}
$$
完整首商正是这里需要的原数据；一次整除不支付所有高 jet。

最后，若施第六 Cartier 的真正权，完整运输必须写成
$$
 \boxed{
 Z^{-7}\widehat{T_Tf}\,\omega_E
 -t_T^*(Z^{-7}\widehat f\,\omega_E)
 =\bigl[Z^{-7}P^{65}a_T^{10}
       -(Z\circ t_T)^{-7}(P\circ t_T)^{65}\bigr]
       (R_f\circ t_T)\,\omega_E.}
 \tag{35}
$$
不能把 $(Z\circ t_T)^{-7}$ 改成 $Z^{-7}$。式 (6)、(11) 使右边第二项在 $O$ 正则，但其整个 Taylor 级数仍须保留。原全部 $Z$ 零点、平移后的零点和二挠极部都在 (35) 中。

## 6. 两条真 z12 来源的同一第六 Cartier 行

令 $c=[z^{p+1}]\log(\sigma/z)$ 为原特征零 Gaussian 系数，$\sigma^\circ=\sigma e^{-cz^{p+1}}$。对任一质量零的同 degree130 来源 $f$，记
$$
 f^\circ=e^{-130cz^{p+1}}f,\quad
 g_6(f)=[z^{6(p+1)}]f^\circ,\quad
 a^+(f)=[z^{p+7}]f^\circ,
 \quad c_6(f)=[z^6]f.
 \tag{36}
$$
R711 的原 $\eta_p=[z^{6p+2}](P-(\sigma^\circ)^2)$ 与
$\kappa_5=(3/5)^p/c_p$ 保持。对 (13)、(16)、(22) 这些实际完整来源，同一个整窗口给
$$
 \boxed{\mathcal T_6(f)=\overline{g_6(f)}
       +65c_6(f)\eta_p+7\kappa_5\overline{a^+(f)}.}
 \tag{37}
$$
这里
$$
 \mathcal T_6(f)=
 \left(\frac{D^5}{5!}
  \left[\frac{\mathcal C(Z^{-7}\widehat f\,\omega_E)}{\omega_E}
       -\frac{c_6(f)^{1/p}}Z\right](O)\right)^p.
 \tag{38}
$$
对 $K$ 系数，(38) 保留 Cartier 的 $p$ 次根；最后的 $p$ 次方使 (37) 对原来源线性。没有把 $\varrho_\pi^{1/p}$ 错写成 $\varrho_\pi$。

对 $G_{65},G_{\rm old}$，$c_6=0$，所以输入 $Z^{-7}\widehat f\omega_E$ 在 $O$ 本来正则，且
$$
 \boxed{\mathcal T_6(G)=\overline{g_6(G)}
                   +7\kappa_5\overline{a^+(G)},
        \qquad G=G_{65},G_{\rm old}.}
 \tag{39}
$$
两者的第5坐标常数 carry 也同时为零。第6项的 $a^+$ 并未因同首消去：它是同原全部 $<s$ sigma 系数与完整分子的低卷积。对可除 $R$ 的另一组合 $\Phi_{260}-\varrho_\pi\Phi_*$，则必须继续保留
$65(1-\varrho_\pi)\eta_p$ 及第5项的 $6\kappa_5(1-\varrho_\pi)$。

R978、R987 已付 $G_{\rm old}$ 的完整惰性函数：
$$
 \boxed{j_{G_{\rm old}}
       =(p+1)\log_p(\pi/\bar\pi)+21840\delta j_{\Phi_*}.}
 \tag{40}
$$
故在 canonical 坏中央 $j_{\Phi_*}=j_{\Phi_{260}}=0$ 下，$j_{G_{65}}=0$，而 $j_{G_{\rm old}}\ne0$。这两条身份都在同一完整 degree130/同一 Gaussian 读者中；普通版本保 R978 的 $1-\upsilon_p$ 与 $p-1$。式 (40) 没有给其非零对数一个未经证明的统一赋值上界。

本篇新增的实际比较数据是 (8)–(12)、两完整二次边界 (19)–(22)、整个共同 frame (30)–(35) 和同一第六行 (39)。要让已付的非零 (40) 与 canonical 零矛盾，仍必须在这个同一全权身份中消费两条实际 $P_2$ 权、所有其它 $Z$ 零点和二挠补项；单个固定十三边界的零或非零都不代替整个 Cartier 读数。

## 7. 独立原完整执行入口

新消费者是 `scripts/check-original-thirteen-boundary-weights.py`，函数
`check_original_thirteen_boundary_weights(degree130_context)`。
它只接受 R987 的 genuine direct22 context：两原 CM 算子仍由各24条完整纤维、全部22列/质量列/额外两纤维重建，并必须与 R972/R976 原66限制的 canonical hash 相同。

消费者同次完成以下整式，而非读取生成坐标表：

- 在该完整 context 重新投影 $(4,3),(4,5)$ 两原算术线，核全部 source hash 和原 $z^6=1$ 归一。
- 用 R971 原 $P_S\mathcal J_5$ 重建完整 raw $F_{10}$，用原 $R,A$ 两个 norm13 maps 重建两条 level10 pull，并完整回乘 (15)–(16)。
- 在 $R,\bar R$ 两个完整二次代数中读取所有质量坐标、trace、$\varrho_\pi$ 与共轭、最高可除重数、首个非零商与完整乘回。
- 核 (10) 的整个 resultant、(12) 的完整有理权及其逆，并核 (21) 的实际非零边界行列式。

公开原完整执行是
[run45903334519](https://github.com/Rogerhu12/math-research-public/actions/runs/45903334519)，job140194103108，源提交
`4d1a123b11a4161bdd4e4592eb145ff163d65a38`，2026-11-26 22:13:07–22:13:20 UTC，全部 PASS。
整个原 direct22 数学入口8.852288255000001秒，本消费者0.0653333019999991秒；R987 原消费者0.108700620999997秒，其全部旧门同次保持。

| 实际固定对象 | 字节数 | SHA256 |
|---|---:|---|
| 原 direct22 入口（同次接 R987/R993） | 6139 | `e91528215bc3421c5891649beb2a027764c1398cc596647bff6321d40de351ea` |
| `check-original-thirteen-boundary-weights.py` | 13687 | `72b72c384ab352e1cdd405f1b985517bb2d2ebbef64dd0a7f31fb07473074717` |
| 原 R987 十三核消费者 | 11563 | `550d182490d957b31898fda76c18999e2eaffc59f796eefd6b1dd75c26092104` |
| 精确 stdout | 7803 | `25daf35b3e71badd796807c004f886b064aefae4008932d9de78feece31fd7dc` |
| 完整 job 日志 | 30210 | `76fe1033d08835850e685a625ed358ffcc48e0fc96cae464651dbbc8eb010500` |

同次原完整22矩阵 hash 为
`aed9d071b6bf9b8b2751b253883fc2664e2dd19724edec8383c5a7f3e4017113`，与原66限制相同；两组各24条完整纤维、所有22列和质量列、额外两纤维、整个交换/共轭逆/十二次幂均通过。
两个实际来源与 raw 来源 hash 分别为

- $\Phi_*$：`510b32718ce9ff51aee4a4de86cc5c362f7f0242a94b7d72df4effc0f95a4497`。
- $\Phi_{260}$：`d27425cf5e8895ad6f054ef73d126608ab7dc5a38c22eb9acaa8cadea7e678b3`。
- $F_{10}$：`33cde970bc30d9c7fd7e991db9156275df0862297e983d42a42f63bec9090b2e`。

两条完整18次首商的 hash 为
`1f11230995b3f6f4d6f7af8af3b25256683906ff239f71bdb24f029698c9d922`
及其共轭支
`ae86db13819212c3064a8cbdf37feb810658c54e97274ab3e65d5cbf575007c0`；最高可除幂均恰为一且整条回乘通过，首次非零余式就是 (22b)。实际边界行列式分别为
$$
 \frac{1+15\delta}{5987520},\qquad
 \frac{-1+15\delta}{5987520},
$$
与 (21) 完全一致。$G_{65},G_{\rm old}$ 的准确首阶均为12，全部共轭及负共轭返回通过。

数学入口的六源码 manifest hash 为
`cf73d598bb8f541c716aa4dbaee3c2109e756ab4b671d0ff5cc6d3bffb597c91`；workflow 的八项来源 manifest hash 为
`829c3857e528c68d9f51d3f67a8de76a25376a8721b7bb688788c6ee04b09d90`。
数学只在公开 Actions 执行；没有运行一个素数扫描，没有保存可重算的矩阵或日志，也没有改变 R887 的指定 primitive、$G$ 或 $P_2$。

## 依赖

- R887 §§8–14：同原 $Z$、全部 CM/挠点常数、完整 $G/P_2$ 缺陷与 $p$ 基；本篇仅消费，未将这些通式重报为新结果。
- R971–973、R978：三个实际 degree130 来源、原绝对13相位、两个 rank≥2 primitive 与完整 old 差。
- R987：canonical lift、两真实轨道、完整质量余式与绝对根/相位。
- R711、R989：原完整第六 Cartier 行、全部低卷积、整窗口和真实除 $p$ 范围。

主目标的固定曲线与无穷素数量词仍由原真实中央联合非零承担；这里没有把一个边界接口或有限执行写成该量词已完成。
