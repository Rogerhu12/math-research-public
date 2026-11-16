# R480：以有限完整 C² 观测支付全第三空间的三个外矩，并消去所有零矩 prototype 的重复漂移

日期：2026-11-16。**新的纸面构造；没有执行符号程序、原根恢复、profile 求积、数学秩、开发检查或科学任务。**

[R476](R476-full-third-diagonal-kernel-is-invisible-to-disjoint-rank-one-circles.md) 已证明，原完整十八维第三对角核 $Z$ 在严格不交 rank-one profile 平面的三个槽上逐函数为零。本稿支付剩余完整第三空间 $W/Z$ 的外矩门。采用的是从构造起点明确增强的有限观测；不声称旧冻结 $\mathcal F^\star$ 原已含这些量。

新增结论如下：可以在原 R455 的同一四自然矩图册、共同外 cap、有限复制和二十目标构造中，选择一个新的真实母库，使
$$
\boxed{
I_j\{\phi_\theta,T(\phi_\theta;D_\theta)\}=0
\quad(T\in W,\ j=0,1,2,\ \text{全部 }\theta).
}
\tag{1}
$$
于是 R472 的任意真实 $A_B=0$ prototype，即使完整 $T_B\notin Z$，也没有任何内部 $s$ 的重复 ruling 漂移。此时第三传入 profile 本身可以变化；消掉的是其在第四 ruling 中的三个真实配对，不能把它改称完整第三场不变。

证明全程保留有序左右尾、原 $I_2$ 的一阶导项和全部第四基准。一个 prototype 自身的内部 ruling、$A\ne0$ 子桥及同一个十三行规范的其余全路径条件，仍不是(1)的推论。

## 1. 只需处理全部二十八个原交换子

采用 [R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md) 的八个完整二次算子
$$
\mathcal E=\{P,R,S,L,U,V,T,Y\}
=\{\Phi_{r_0},\Phi_{r_1},\Phi_{s_0},\Phi_{p_0},
\Phi_{s_1},\Phi_{p_1},\Phi_{t_1},\Phi_{p_2}\}.
\tag{2}
$$
字母 $T$ 在(2)中是一个二次基方向；下文一般完整第三方向用 $\tau$ 表示，避免混淆。原交换子为
$$
[X,Y](a;B)=X(a,YB)-Y(a,XB).
\tag{3}
$$

[R254](R254-eight-exact-third-diagonal-lifts-and-eighteen-dimensional-image.md) 与 [R261](R261-eight-local-self-adjoint-hook-operators-and-full-third-kernel.md) 给出整个 $W$ 的实际生成表：二十八个(3)及八个原额外模板 $\tau_j$。每个额外模板都有已付的完整差
$$
\tau_j-\gamma_j=\chi_j\in Z,
\tag{4}
$$
其中 $\gamma_j$ 是这二十八个完整交换子的明确线性组合。这里使用完整同锚身份，未重求其矩阵或秩。

对当前不交 rank-one 平面，R476 给 $\chi_j(\phi_\theta;D_\theta)=0$。所以，只要对(2)的全部二十八个无序 pair 支付(1)，便已支付整个 $W$。不需要把原六个 Gaussian pair 假称为全部二十八个，也不需要新的第三核观察。

三矩保持
$$
\mathbf I(u,v)=
\left(
\int u''v'',\
\int xu''v'',\
\int\{x^2u''v''+2u'v'\}
\right).
\tag{5}
$$
所有积分仍使用原共同物理区间及同一右锚 $J=\int_x^{r_*}$。

## 2. 每个完整 self 是四次 C² 观测：先保两条真尾

对紧 profile $u$ 及 $j=0,1,2$，定义
$$
F_{X,j}(u)=I_j(u,X(u,u))=\int f_{X,j}(x,u,u',u'').
\tag{6}
$$
R259 §§2–4 给全部八个算子的二十四个 local cubic 密度；并给
$$
Q_{X,j}=\operatorname{EL}f_{X,j}-L_jX(u,u),
\tag{7}
$$
$$
L_0=D^4,\quad L_1=xD^4+2D^3,\quad
L_2=x^2D^4+4xD^3,
$$
以及对任意允许带左尾的 $w$ 的完整身份
$$
2I_j\{u,X(u,w)\}=\int Q_{X,j}(u)\,w.
\tag{8}
$$

令
$$
S_{XY,j}(u)=2I_j\{u,[X,Y](u;u\odot u)\}.
\tag{9}
$$
单包 $Xu^2,Yu^2$ 可以有二次左尾，不能把二者冒称为紧函数以删除 Green 边项。

写两条真实左尾
$$
p_X=A_Xx^2+B_Xx+C_X,\qquad
p_Y=A_Yx^2+B_Yx+C_Y.
$$
原 [R294](R294-corrected-self-fibers-pay-all-angular-symmetric-Gaussian-histories.md)(8)–(10) 给
$$
I_j(v,w)=\int vL_jw+\beta_j(p_v,p_w).
\tag{10}
$$
定义仅为密度多项式运算的
$$
D_{\rm loc}F_{X,j}(u)[w]
=\int(f_u w+f_{u'}w'+f_{u''}w'').
\tag{11}
$$
这没有把非紧 $u+tw$ 当作合法 profile 族。

由(7)(8)，先保留两项 $L_j$，再用(10)及原 $I_j$ 对称性，准确得到
$$
\boxed{
\begin{aligned}
S_{XY,j}(u)
={}&D_{\rm loc}F_{X,j}(u)[Yu^2]
-D_{\rm loc}F_{Y,j}(u)[Xu^2]\\
&+\beta_j(p_Y,p_X)-\beta_j(p_X,p_Y).
\end{aligned}}
\tag{12}
$$
例如最后差的三个分量依次为
$$
\boxed{
2(A_YB_X-A_XB_Y),\
2(A_XC_Y-A_YC_X),\
2(C_XB_Y-C_YB_X).
}
\tag{13}
$$
它们由原 Green 表直接相减；任选左零 collar 位置全部抵消。式(13)一般不为零，本文没有删除它。

原八个二次表的二导均为
$$
(Xu^2)''=\alpha_X(x,u,u',u'')u'''
+\beta_X(x,u,u',u'',J_0,J_1,J_2),
\tag{14}
$$
其中 $\alpha_X$ 局部一次，$\beta_X$ 只需 $C^2$ 数据，
$$
J_0=J(u''{}^2),\quad J_1=J(xu''{}^2),\quad
J_2=J(x^2u''{}^2+2u'{}^2).
$$
因此(12)唯一超过二阶的项形如
$A(x,u,u',u'')u'''$，且只线性出现；其系数 $A$ 局部。以最后变量取多项式原函数
$$
\mathscr A(x,u,p,r)=\int_0^rA(x,u,p,\rho)\,d\rho
$$
便有
$$
A(x,u,u',u'')u'''
=D_x\mathscr A-\mathscr A_x-u'\mathscr A_u-u''\mathscr A_p.
\tag{15}
$$
真紧平端使 $\mathscr A$ 的两端值为零。其它项以及(13)都是原二次矩与有限 $C^2$ primitive 的多项式。

故每个 $S_{XY,j}$ 都是固定支持空间上的**完整、连续、光滑、四次 polynomial/C² 泛函**。这里不是说它只有 C² principal，也没有用高频极限删掉任何三阶平方余项：不存在那种余项，(12)–(15)是准确降阶。

## 3. 全部 self 平移次数至多十

对合法共同小平移 $u_t(x)=u(x-t)$，R259 全八方向表给
$$
\boxed{S_{XY,j}(u_t)=\sum_{k=0}^{10}t^k s_{XY,j,k}(u).}
\tag{16}
$$
完整度数界如下。原二次输出在搬回母坐标后，包括三个真实 primitive 的展开，总位置次数至多四；原 $f_{X,j}$ 的次数至多五，(7)的 $Q_{X,j}$ 至多六。因此从(8)(9)的 $Q_{X,j}Yu^2-Q_{Y,j}Xu^2$ 得到至多 $6+4=10$。

此计数包含 $V,T,Y$ 三个高位置方向，不仅是旧 Gaussian 的六个基本方向。右锚始终位于输入的同一零 collar；同步搬回坐标后，原积分上限在零区的移动不产生新常数。(13)的矩二次式次数更低，也已包括在原同一个(16)内。

每个系数 $s_{XY,j,k}$ 可由十一种固定合法小平移的 $S_{XY,j}(u_t)$ 以固定 Vandermonde 逆线性组合定义。故这些系数仍是四次 C² 泛函，不要求 profile 具有十阶连续导数，也不执行新的插值求值。

## 4. 新有限观测必须从构造起点加入

明确定义
$$
\boxed{
\mathcal F_{\rm all3}
=\left(
\mathcal F^\star,\
s_{XY,j,k}:
X<Y\text{ 于(2)},\
j=0,1,2,\
0\le k\le10
\right).
}
\tag{17}
$$
此处 $\mathcal F^\star$ 是原 R455/R467 已声明的完整有限输入，含 $\mathcal F_{\rm rat},D,E_5$、三真实矩和原所需保持量。新列最多为
$28\cdot3\cdot11=924$ 个生成标量；可以冗余，本文不声称其独立，不把924称为控制秩。

(17)在共同几何窗口、完整复制布局、允许宽度与母形选择开始时就固定。然后才选限制最大秩母、正常方向及二十目标根。没有要求一个已经冻结的旧母在其旧纤维内无偿满足新目标；最终 profiles 与 seed 是按(17)重新从起点选出的对象。

需要保持的是所有最终形状在(17)上具有共同母的准确值，而不是令每个 self 单独为零。这一点使下一节真正的正负幅编码可以工作。

## 5. 全二十八方向的有序展开只需要同三个真实矩

对任意两个实际不交微包，左 outer 为 $u$、右 inner 为 $v$。原八方向的左尾皆由
$$
\mathbf m(u)=\left(\int u''{}^2,\int xu''{}^2,
\int(x^2u''{}^2+2u'{}^2)\right)
\tag{18}
$$
线性决定。R259 §5 的全八方向表还给
$$
X(u,Ax^2+Bx+C)
=\alpha_-(X;A,B,C)D_-u
+\alpha_0(X;A,B,C)D_0u
+\alpha_+(X;A,B,C)D_+u,
\tag{19}
$$
其中 $D_-u=u'$、$D_0u=xu'-u$、$D_+u=x^2u'-2xu$，三个系数线性。原三矩对(19)的值也线性依赖(18)。

所以对全部二十八 pair，都有原有序双线性核
$$
\Gamma_{XY,j}(\mathbf m,\mathbf n)
=2I_j\{u,X(u,p_Y(\mathbf n))-Y(u,p_X(\mathbf n))\}.
\tag{20}
$$
它是一个固定真实 $3\times3$ 双线性矩阵的配对。本文无需它只落在旧六 Gaussian pair 的三种特殊核中；保留任意这样的矩阵恰好足够。

设从左到右的包为 $u_i$，令
$$
c_i=a_i\cos\theta+b_i\sin\theta,\qquad d_i=a_i^2-c_i^2.
$$
R259(26)的原 local outer 与右尾推导逐字给
$$
\boxed{
2I_j\{\phi,[X,Y](\phi;D)\}
=\sum_i c_i^2d_i S_{XY,j}(u_i)
+\sum_{i<k}c_i^2d_k
\Gamma_{XY,j}(\mathbf m_i,\mathbf m_k).
}
\tag{21}
$$
没有来自 $k<i$ 的项，因为该 inner 场在那里已是其准确右零 collar。来自 $k>i$ 的真实二次左尾完整保留为(20)。这不是把有序核改成对称核，也不是将单包三矩设零。

## 6. 等背景十矩支付全部 even self 与对称 cross

采用原 [R280](R280-ordered-three-moment-areas-and-five-block-Gaussian-cancellation.md) 的两个有限格点布局。每个基本布局满足
$$
b_i^2=B>0,\qquad
R_i=a_i^2-B\in\{-B/2,8B\},\qquad T_i=a_ib_i,
\tag{22}
$$
$$
\sum_iR_it_i^k=\sum_iT_it_i^k=0\quad(0\le k\le10),
\qquad
R_i^2-4T_i^2=\frac{7B}{2}R_i.
\tag{23}
$$
各中心 $t_i$ 是同一等距有限格点。初始形状来自同一个偶母 $u_0$；后续各形状严格保持(17)，故
$$
\mathbf m_i=m(1,t_i,t_i^2+\nu),\qquad
S_{XY,j}(u_i)=P_{XY,j}(t_i),\quad\deg P_{XY,j}\le10
\tag{24}
$$
是准确值。真实 $\nu$ 含(18)中的 $2\int u'{}^2$，不是点质量替代。

固定 pair、外矩，记 $S_i$ 和 $\Gamma$ 为(21)中的值。两个 even 系数满足原代数
$$
E_{04}
=B\sum_kR_k\left\{S_k+\sum_{i<k}\Gamma(\mathbf m_i,\mathbf m_k)\right\},
\tag{25}
$$
$$
E_{22}-E_{04}
=\sum_i(R_i^2-4T_i^2)S_i
+\sum_{i<k}(R_iR_k-4T_iT_k)\Gamma(\mathbf m_i,\mathbf m_k).
\tag{26}
$$
它们分别来自 $\sin^4\theta$ 和 $\cos^2\theta\sin^2\theta$，没有删掉配套背景项。

在(24)的等距格点上，$\sum_{i<k}\mathbf m_i$ 的分量是 $k$ 的次数至多三的准确有限和多项式，$\mathbf m_k$ 的次数至多二。因此(25)的整个前缀项次数至多五。结合 self 的十次界与(23)，得到
$$
E_{04}=0.
\tag{27}
$$
这一步适用于任意(20)的双线性核，不使用旧三种特殊核的系数。

由(23)(24)，(26)的 self 和也为零。写
$\Gamma=\Gamma_{\rm sym}+\Gamma_{\rm alt}$。真实三矩给
$\sum R_i\mathbf m_i=\sum T_i\mathbf m_i=0$，因此
$$
\begin{aligned}
&\sum_{i<k}(R_iR_k-4T_iT_k)\Gamma_{\rm sym}(\mathbf m_i,\mathbf m_k)\\
&\quad=-\frac12\sum_i(R_i^2-4T_i^2)\Gamma(\mathbf m_i,\mathbf m_i)=0.
\end{aligned}
\tag{28}
$$
最后的对角核是中心的次数至多四的多项式，仍由(23)准确消去。

于是全部二十八 pair 的 even 余项，都只剩相同三条真实有序面积
$$
\boxed{
\mathcal A_{rs}
=\sum_{i<k}(R_iR_k-4T_iT_k)
(m_{r,i}m_{s,k}-m_{s,i}m_{r,k}),
\quad0\le r<s\le2.
}
\tag{29}
$$
若 $\Gamma(\mathbf m,\mathbf n)=\mathbf m^{\mathsf T}G\mathbf n$，其系数是
$(G_{rs}-G_{sr})/2$。这保原规范的 $1/2$，不是增加三个可随意选择的形状常数。

## 7. 十二完整 copy 与五个正权 block 同时适用于全部二十八 pair

先保原 R183/R259 的完整八 copy 前提：每个 base 的三矩和全部第三 forcing 在合法共同平移后仍准确成立。不能只知道某一个位置上的第三 ruling 为零就套复制。

对这个完整 base，原十二 copy 取
$$
d_\ell=d_0+\ell\Delta,\quad
\epsilon_\ell=(-1)^\ell,\quad
\gamma_\ell=\binom{11}{\ell}^{1/4},
\quad0\le\ell\le11,
\tag{30}
$$
第 $\ell$ 份为 $(\gamma_\ell f_\ell,\epsilon_\ell\gamma_\ell g_\ell)$。

(21)的两个 odd 角系数在 $g\mapsto-g$ 时变号，并按共同幅度四次缩放。它们的共同平移次数至多十，由第3节和(20)保证。所以第十一有限差分
$$
\sum_{\ell=0}^{11}(-1)^\ell\binom{11}{\ell}d_\ell^k=0
\quad(0\le k\le10)
\tag{31}
$$
一次消掉全部二十八 pair、三个外矩的全部 odd 系数。没有新增复制层或把 cubic 幅权当 quartic 幅权。

不同完整 base 之间的(21) cross 精确为零：每个右方 base 的
$\sum d_i(\theta)\mathbf m_i=0$，而(20)对 inner 矩线性。这一步使用完整 base 的合法性，不删除它内部每个微包的真实左尾。

R280 已构造两个实际有限布局，使 $\mathcal A_{01}$ 分别严格正、负。其证明只用(22)(24)的真实三矩，不依赖选取哪一个 Gaussian pair。然后在一次固定的最后位置上，以三个正布局和两个负布局、五个严格正四次幅权准确配平
$$
\mathcal A_{01}=\mathcal A_{02}=\mathcal A_{12}=0.
\tag{32}
$$
原(25)–(28)对每个完整布局及其任何共同平移都成立；故这些最后平移和幅权不会恢复已消掉的 even 项。原十二包装的 odd 零也保持。

(17)保存各实际微包的三个矩和全部 self 平移数据，因此后续同纤维形状改变不改变(27)–(32)。由(21)，最终得到
$$
I_j\{\phi_\theta,[X,Y](\phi_\theta;D_\theta)\}=0
\quad(X,Y\in\mathcal E,\ j=0,1,2,\ \text{全部 }\theta).
\tag{33}
$$
再用(4)和 R476 的完整核零，即得开头(1)。

## 8. 与原四自然矩、共同 cap 和二十完整目标在同一点实现

必须核实(17)不会把原 R455 的高阶目标支付偷换为新未知假设。这里直接用其原证明机制，精确扩展有限观察的输入。

先按 [R455](R455-four-natural-moments-with-one-common-degenerate-pair-and-twenty-targets.md) §§2–6 选择真实有限周期母 $u_*$、固定共同外 cap、两个简单 $A_u$ 镜点、四个内支撑正常方向以及
$$
q_0=q_1=q_2=q_3=0,\qquad D-E_5>0.
\tag{34}
$$
在其原内区建立同一个四约束实解析 $C^2$ 图册 $\chi(v)$。新增加的(17)全是有限 polynomial/C² 观察；原 $\mathcal F^\star$ 仍是其分量。

现在以 $\mathcal F_{\rm all3}\circ\chi$ 取**真实限制最大秩** $r$，并选有限光滑内支撑见证。没有使用一个预填的924阶矩阵，也不假定 $r$ 等于新增列数。

原二十 principal 的非零见证只需在固定单调小窗内自由指定有限二阶 jets，随后沿四个避开该窗的正常方向纠正 $q$。这一见证在选择(17)的最大 minor 之前仍成立，并不要求新 $F$ 已为常值。把两个有限见证族放入同一个有限参数空间，真实解析的非零 minor 乘积不恒零；故可在原母的允许邻域同时选择：

- 四自然矩图册的正常 minor；
- $\mathcal F_{\rm all3}$ 的限制最大 minor；
- 原二十目标的 principal minor。

这正是 R455 §7 的同点选择论证，有限 $F$ 的列数改变不改变其逻辑。原有限布局、宽度、复制、额外原开条件和共同物理窗口均已在此之前纳入，不在求根以后移动。

随后使用原 R455/R447 的同一有号三阶集中。由于全部新增观察只需 $C^2$，其真实值和参数导增量仍是原 $O(K^{-1/2})$；固定的有限正常右逆给同阶光滑纠正。沿块三角 Jacobian，准确保持的是
$$
q=0,\qquad
\mathcal F_{\rm all3}(U_i)=\mathcal F_{\rm all3}(u_0).
\tag{35}
$$
限制最大秩使其余观察局部因子化，不能只保持挑出的若干分量后声称保持全映射。

低阶纠正在原二十完整目标的 $C^1$ 主系统中趋零；原有限正锥、严格正 kernel 与非退化正幅根不变。因此一个充分大而有限的 $K$ 上，同一真实母库同时满足
$$
\boxed{
q(U_i)=0,\quad
\mathcal F_{\rm all3}(U_i)=\mathcal F_{\rm all3}(u_0),\quad
(\mathcal V_{19},d_P)=(0,\eta).
}
\tag{36}
$$
原完整基线与所有 C² 余项一直进入有限 IFT，未以主项近似替代准确根。

最高脉冲仍只在原单调窗，符号仍保持 $A<0$；其余内区只有固定光滑低阶小纠正。两外 cap 及镜点全部 jets 不变，正性、有限简单 $p$ 零点、$D-E_5>0$ 依原同一开条件保持。新观察包含原三矩，所以原已付 cap 连续族身份亦保其明确范围。

这是新的从起点母库，不是对一套旧已冻结实际 profiles 的无偿改动。原 R467/R468 的增强成本条件若随后使用，必须指向这个同一新库、同一 $J_{\rm aff}$ 和同一规范；本文不因(36)自动判定其两个 self 商类成比例或其 actual 截面已完成。

## 9. 真实任意第三分配现在不再产生 A=0 重复漂移

固定由(36)得到的同一个圆。取原 [R80](R80-complete-third-affine-class-and-P1-endpoint-obstruction.md) 允许的任意真实 $A_B=0$、同常数 scalar/frame 返回的完整第三 prototype。其 $T_B\in W$，故(1)成立。

一槽 $\phi_\theta$ 真紧，原物理配对保完整
$$
\mathcal E_s(\phi_\theta,T_B(\phi_\theta;D_\theta))
=\frac{1+(h\omega-k)^2}{4h}I_0
+\frac{h\omega-k}{2}I_1+\frac h4I_2=0.
\tag{37}
$$
原 $I_2$ 第二项及另一槽的左尾均没有删除；三个数各自零使本结论与实际 $h,k,\omega$ 无关，因而对 prototype 的全部内部 $s$ 成立。

R472(34)遂给
$$
\boxed{\mathscr C_1=\mathscr C_2=0,\qquad
\mathscr K_j(s,\theta)=\mathscr K_0(s,\theta).}
\tag{38}
$$
一般 $T_B(\phi_\theta;D_\theta)$ 本身并不为零。其真实入口演化仍是
$$
a_j=a_0,\qquad b_j=b_0-2jT_B(\phi_\theta;D_\theta).
\tag{39}
$$
(38)是(39)的全部配对漂移被(1)消掉，不能把它写成 R476 特殊 $Z$ 分支的 $b_j=b_0$。

对串联的不同 $A_{B_i}=0$ 块，(39)改为先前各 $T_{B_i}$ 的和；由 $W$ 线性和(37)，这种累积第三传入对每个后继块的第四 ruling 项 $2\mathcal E_s(\phi,b)$ 也没有影响。因此原实际第三目标可以在 $W$ 内分配，而不必逐块限制在 $Z$。

例如预先固定有限个 $T_1,\ldots,T_m\in W$，令
$$
T_{m+1}=\tau\mathfrak H-\sum_{i=1}^mT_i.
\tag{40}
$$
R80 的真实第三截面分别实现这些零矩闭块，整词第三仍为固定 $\tau\mathfrak H$；不能用负时间替代负目标。所有具体路径、参数盒、桥与共同窗口须先固定，再在本稿同一 profile 构造中消费。原完整第三 period 因总 $\tau\mathfrak H$ 和 R476 保持其真实范围。

## 10. 同一个十三行规范与全部第四基准仍在问题中

(38)使一个已有真实 prototype 的任意有限重复不再增加第三漂移方程，但没有求解共同的 $\mathscr K_0$。

原 R472(29)仍是
$$
\mathscr K_B^{(a,b)}
=\mathscr K_B^0+\mathcal B_B(a)-\mathcal E_s(a,a)
+2\mathcal E_s(\phi,b).
\tag{41}
$$
本稿只消掉 $b$ 中由先前完整 $T_i$ 产生的那一部分；$\mathscr K_B^0$、二阶历史 $a$、其平方与原全局第三 Gram 规范均保留。$A\ne0$ 子桥的 $\mathscr C_2$ 和其余 $\mathscr C_1$ 项不在(38)内。

第四传递亦仍含
$$
V_B+2T_B(a;D_\theta)-4T_B(\phi_\theta;\phi_\theta,a).
\tag{42}
$$
(1)是三个外矩的身份，不是这些完整函数的零身份。全部 prototypes 乘真实整数的基准、R70 桥、真实倒行及 Klein 组装必须统一进入原最终成本；不因新外矩零而删除任意一个 $V_B$。

原 R469 的允许再调仍受同一个
$L_f\eta_\theta=0$ 与原十三行 $C_\theta\beta_\theta=0$ 约束；已有 protected germ 锁定第三 Gram 的规则不变。不能给每个实际块另选 $w_\theta$ 或 $\chi_\theta$。后续若接 R468/R467，只能使用同一新库的实际联合截面及同一相位 seed，不能把本稿的 profile 构造当成那个 actual 条件已成立。

本稿的新增完成项是明确有限观测(17)、完整 C²/尾证明、原复制与真实有序面积的全二十八方向推广、与原二十目标的同点实现，以及实际任意零矩第三分配下的全内部 $s$ 重复漂移消失。下一真正全路径条件已缩为这些真实块自身的(41)、$A\ne0$ 子桥及唯一规范的共同解；这些没有被有限条款数或全 $W$ 外矩零冒作已经完成。
