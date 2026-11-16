# R424：完整局部 C2 负四自然函数的共同查询归约与从起点增加一个母矩

日期：2026-11-16。**独立纸面证明；没有执行新的 profile、求积、符号程序、秩、原根、开发检查或科学任务。**

本稿证明一个可供尚未知低层原式使用的条件性结论。假定某个原成本权 $-4$ 的**完整自然函数**已经准确化为关于 $x,u,u',u''$ 的有限局部多项式积分，所有原 primitive、pure 及真实 Green 尾均已收齐。那么，在同一次母构造中从起点增加
$$
M_{25}(u)=\int x^2(u'')^5
$$
这一观察后，它在全部实际母包的共同正仿射查询及不交有序 $3+2$ 查询上，都与一个已知 Q4 平移像列成固定比例。因此它不能承载经这些共同查询及 whole $E$ 下降的非零负四平移头。

这不声称 R422 的两个未知自然函数已经满足上述假定。仅消去最高三导平方、仅证明 $C^2$ 连续，或只在某个母上得到局部表达，都不够应用本稿。对仍含原 primitive、矩乘积或真实尾的函数，必须继续完整归约。

来源：[R393](R393-nine-dimensional-natural-Q4-affine-image-and-two-character-heads.md)、[R411](R411-positive-analytic-mothers-blind-to-the-weight-zero-natural-affine-orbit.md)、[R412](R412-complete-weight-zero-natural-null-mothers-and-nineteen-common-targets.md)、[R413](R413-common-mother-Q4-chain-and-exact-low-layer-character-reduction.md)、[R414](R414-common-high-natural-quotient-and-actual-finite-C1-sections.md)及[R323](R323-full-pure-self-cone-and-complete-negative-weight-response-control.md)。

## 1. 原自然读出、完整局部假设与权的区别

保持原真实成本空间 $U$、响应空间 $\mathcal R$，以及
$$
E(V)=(\pi V,\mathcal Q(V)),\qquad
\mathcal Q(V)(u)=\frac14[x^2]_{\rm left}V(u^2,0).
$$
$\mathcal Q$ 是整个 universal self 左二次系数，不是整个输出函数。

使用同一个真实右锚与原完整自然函数
$$
\Lambda_u(V)=
\int u'''V(u^2,0)
-\frac{16}{5}\int u'''\pi V(u)
-\frac{32}{15}\int u'''\mathscr G_{V,u}(\mu(u)),
\tag{1}
$$
其中
$$
\mu(u)=
\left(
\int(u'')^2,\ \int x(u'')^2,\
\int\{x^2(u'')^2+2(u')^2\}
\right).
$$
$\mathscr G$ 是原 pure 有序 $2+2$ 三矩尾；它不能独立选取。已付
$$
\Lambda_\cdot(\mathcal R)=0.
\tag{2}
$$

固定 $V\in U_{-4}$。本稿的局部假设是：对全部合法实紧 $u$，存在一个固定有限多项式 $g$，使
$$
\boxed{\quad
\Lambda_u(V)=\mathcal L(u)=\int g(x,u,u',u''),
\quad}
\tag{3}
$$
且(3)是(1)的**完整恒等式**。右边不另加 primitive、矩乘积、左边界值或其它待定余项。系数是固定实数，$x$ 只取非负整数幂；若原式有参数，须先固定对应完整成本系数。

式(1)对 profile 幅度五次齐次。原协变为
$$
\Lambda_u(\mathsf P_{H,c}V)
=H^2\Lambda_{C_{H,c}u}(V),\qquad
C_{H,c}u(x)=u((x-c)/H).
\tag{4}
$$
因此 $V$ 的成本真权为 $-4$ 时，
$$
\mathcal L(C_{H,0}u)=H^{-6}\mathcal L(u).
\tag{5}
$$
后文的 $-6$ 是积分的输入伸缩幂，不是另一个成本权。

若(3)的某个多项式呈示没有逐项分级，先按 profile 幅度与(5)的有限幂分组。有限不同幂在一个合法开区间上独立，故其它组给零泛函，可以丢去；保留的组同时五次齐次、输入权 $-6$。这一步不需要对原中间场假设紧支撑。所有使用的局部积分都只含紧 $u$ 的 jets。

## 2. 六个显示密度的穷尽

记 $p=u',r=u''$。一个保留的单项为
$$
x^k u^a p^b r^c,\qquad
a,b,c,k\in\mathbb Z_{\ge0}.
$$
幅度五次及(5)分别给
$$
a+b+c=5,\qquad
k-b-2c+1=-6,
$$
即
$$
k=b+2c-7\ge0.
\tag{6}
$$
逐 $c$ 穷尽：

| $c$ | $(a,b,k)$ | 密度 |
|---|---|---|
| $2$ | $(0,3,0)$ | $p^3r^2$ |
| $3$ | $(1,1,0)$ | $upr^3$ |
| $3$ | $(0,2,1)$ | $xp^2r^3$ |
| $4$ | $(1,0,1)$ | $xur^4$ |
| $4$ | $(0,1,2)$ | $x^2pr^4$ |
| $5$ | $(0,0,3)$ | $x^3r^5$ |

$c\le1$ 时由 $b\le5-c$ 得 $b+2c<7$，没有单项；其它情形也被(6)排除。因此
$$
\boxed{
\mathcal L(u)=
\int\{\beta_1p^3r^2+\beta_2upr^3
+\beta_3xp^2r^3+\beta_4xur^4
+\beta_5x^2pr^4+\beta_6x^3r^5\}.
}
\tag{7}
$$
这是六项**呈示的穷尽**，不声称六个积分线性独立，也不把六个标签称为新秩。全部项都连续于固定紧支撑上的 $C^2$ 拓扑。

## 3. 偶母的真实平移，只留下四个完整积分

现在 $u$ 为中心在零的实偶紧母，写 $u_c(x)=u(x-c)$。换元 $x=y+c$，$p(y)$ 为奇、$r(y)$ 为偶。定义
$$
\begin{aligned}
U_4&=\int ur^4,& P_4&=\int p^2r^3,\\
X_4&=\int xpr^4,& M_{25}&=\int x^2r^5,
\end{aligned}
\qquad M_5=\int r^5.
\tag{8}
$$
下标仅作本稿记号，均为五次泛函。

(7)第一、二项的积分因奇偶恒零，并不随平移改变。其余四项准确为
$$
\begin{aligned}
\int x p_c^2r_c^3&=cP_4,\\
\int x u_c r_c^4&=cU_4,\\
\int x^2p_c r_c^4&=2cX_4,\\
\int x^3r_c^5&=3cM_{25}+c^3M_5 .
\end{aligned}
\tag{9}
$$
例如最后一式保留了真实三次中心项，没有先以一个共同中心代替实际副本。

R411/R412 的四个完整 $q$ 约束包含 $q_0=-3M_5/80=0$。因此在该约束流形上，
$$
\boxed{
\mathcal L(u_c)=c\,b_{\mathcal L}(u),\qquad
b_{\mathcal L}
=\beta_3P_4+\beta_4U_4+2\beta_5X_4+3\beta_6M_{25}.
}
\tag{10}
$$
式(10)在每个有限真实平移上准确，不是窄包或大中心的渐近式。

## 4. 一个新增母矩足够固定全部四个积分

沿 R413，使用
$$
D=-\frac12P_4+\frac12X_4-\frac3{20}M_{25},
\qquad
E_5=-\frac12X_4+\frac7{20}M_{25},
\tag{11}
$$
以及完整平移系数
$$
q_1=-\frac14U_4-P_4+\frac{15}{8}X_4-\frac{63}{80}M_{25}.
\tag{12}
$$
$E_5$ 与联合映射 $E$ 不同。

从 $(U_4,P_4,X_4,M_{25})$ 到 $(q_1,D,E_5,M_{25})$ 的真实矩阵为
$$
\begin{pmatrix}
q_1\\D\\E_5\\M_{25}
\end{pmatrix}
=
\begin{pmatrix}
-\frac14&-1&\frac{15}{8}&-\frac{63}{80}\\
0&-\frac12&\frac12&-\frac3{20}\\
0&0&-\frac12&\frac7{20}\\
0&0&0&1
\end{pmatrix}
\begin{pmatrix}
U_4\\P_4\\X_4\\M_{25}
\end{pmatrix}.
\tag{13}
$$
其行列式为 $-1/16$。逐行回代，在 $q_1=0$ 上得到
$$
\boxed{
\begin{aligned}
X_4&=\frac7{10}M_{25}-2E_5,\\
P_4&=\frac25M_{25}-2E_5-2D,\\
U_4&=\frac12M_{25}-7E_5+8D .
\end{aligned}}
\tag{14}
$$
若不设 $q_1=0$，最后一行另有 $-4q_1$；本稿没有略去它后用于更大的类。

因此，如果全部最终母 $U_i$ 从同一起点满足
$$
q(U_i)=0,\qquad
D(U_i)=D_0,\quad E_5(U_i)=E_0,\quad
M_{25}(U_i)=M_0,
\tag{15}
$$
则四个(8)在所有 $U_i$ 上相同。对每一个固定完整函数(7)，
$b_{\mathcal L}(U_i)$ 也有同一个值 $b_{\mathcal L}$。

这里不把 $D_0,E_0,M_0$ 当成可任意独立指定的数。它们是同一个实际受限 regular 母点的值。第8节给从起点同时保留(15)和十九个原目标的选择。

## 5. 实际幅度、宽度和中心的完整比例式

保持 R414 的实际规范
$$
u_i(x)=\rho_iU_i((x-\xi_i)/w_i),\qquad w_i>0.
\tag{16}
$$
$\rho_i$ 可以带符号；若幅度已并入圆的原系数，则统一取 $\rho_i=1$，不可在两种规范间重复计幅。不同母、真实宽度、八/十二复制和其它完整块的全部中心均保留。

对同一个合法仿射参数 $(H,c)$，
$$
C_{H,c}u_i(x)
=\rho_iU_i\!\left(
\frac{x-(H\xi_i+c)}{Hw_i}
\right).
$$
先用(5)，再用(10)，得到
$$
\boxed{
\mathcal L(C_{H,c}u_i)
=\rho_i^5(Hw_i)^{-7}(H\xi_i+c)b_{\mathcal L}.
}
\tag{17}
$$
可以直接检查：缩放给 $(Hw_i)^{-6}$，母的无量纲中心为
$(H\xi_i+c)/(Hw_i)$，二者乘积正是(17)。第五幅权、七次宽度因子和实际中心均不能删去。

接着选一个已付的原 Q4 列。R393 用 $F,G,H_4$ 表示完整自然函数，其中 $H_4$ 是其表中
$$
H_4(u)=\frac14\int r(p-xr)^4 .
$$
这里下标只为避开仿射尺度 $H$，它不是后来已更正为零的正规 H 层。原真实平移作用满足
$$
NF=-4D,\qquad NG=\frac43D-2E_5,\qquad
NH_4=\frac12F-3G.
\tag{18}
$$
对中心偶、$M_5=0$ 的母，完整平移式给
$$
F(u_c)=-4D_0c,\qquad
G(u_c)=\left(\frac43D_0-2E_0\right)c.
$$
所以
$$
(NH_4)(u_c)=6(E_0-D_0)c.
\tag{19}
$$

R393 的系数取值与有限真权投影在真实 $U$ 内给一个权 $-3$ 代表 $V_H$，其完整自然函数是 $H_4$。令
$$
Z=NV_H\in U_{-4}.
\tag{20}
$$
它是一个真实 signed 成本类，未被称为一条实际路径。由(4)、(18)—(19)，
$$
\boxed{
\Lambda_{C_{H,c}u_i}(Z)
=6(E_0-D_0)\rho_i^5(Hw_i)^{-7}(H\xi_i+c).
}
\tag{21}
$$
R413/R414 从起点保留的严格条件是 $D_0-E_0>0$。于是
$$
\eta_{\mathcal L}=\frac{b_{\mathcal L}}{6(E_0-D_0)}
\tag{22}
$$
有定义，且对所有实际 $i$、所有共同合法 $(H,c)$，都有
$$
\Lambda_{C_{H,c}u_i}(V)
=\eta_{\mathcal L}\Lambda_{C_{H,c}u_i}(Z).
\tag{23}
$$
$\eta_{\mathcal L}$ 不依赖实际宽度、幅度、中心或母标签。个别中心使两边同时为零时，(23)仍是无须除以该查询值的完整身份。

## 6. 有序 3+2 查询与任意右方辅助矩基

R414 的共同映射只增加
$$
\mathcal O_{u,v}(V)
=[s^3t^2]\Lambda_{su+tv}(V),
\qquad \operatorname{supp}u<\operatorname{supp}v,
\tag{24}
$$
及其共同正仿射闭包；不会把辅助包的 self 函数自动加作目标。

对(3)的完整局部五次密度，不交支持给逐点准确分解
$$
\mathcal L(su+tv)=s^5\mathcal L(u)+t^5\mathcal L(v).
\tag{25}
$$
所以 $\mathcal O_{u,v}(V)=0$。$Z$ 的完整 Q4 自然函数也有 R393 的局部二阶五次呈示，同样有
$\mathcal O_{u,v}(Z)=0$。

这对任意真实右方辅助包成立；辅助包不必偶，不必满足 $q=0$，也不必与实际母具有相同 $D,E_5,M_{25}$。共同仿射作用保持其原不交次序。

因此，如果 $\mathcal A$ 为全部实际母 self 查询与所需有序查询的共同映射，则(23)加强为
$$
\boxed{\mathcal A(V)=\eta_{\mathcal L}\mathcal A(Z).}
\tag{26}
$$
(26)是**这个从起点选择的共同有限母库及其仿射查询像**中的比例，不是两个 universal 自然泛函在所有 profile 上成比例。它也不把未知完整 $F_0,Q_2$ 的有序函数宣为零；只有已经满足(3)的完整函数可用(25)。

## 7. 为什么它准确杀下降的负四平移头

设
$$
J=(E,\mathcal A)
$$
使用同一个母库。令 $\lambda$ 是 $U$ 上的真权 $-4$ 线性泛函，满足：

- $\lambda$ 经 $J$ 下降，即杀 $\ker J$；
- $\lambda$ 杀整个 $\mathcal R$；
- $\lambda N=0$，即原平移不变条件。

实际正字符的相应必要头属于这个范围；本节不需要先假设其正性。

由(26)，$V-\eta_{\mathcal L}Z$ 的新增共同自然查询为零。原 R323 已准确支付
$$
E(U_{-4})=E(\mathcal R_{-4}).
\tag{27}
$$
因此存在同权 $R\in\mathcal R_{-4}$，使
$$
E(R)=E(V-\eta_{\mathcal L}Z).
$$
同时(2)给 $\mathcal A(R)=0$，故
$$
J(V-\eta_{\mathcal L}Z-R)=0.
$$
于是
$$
\lambda(V)=\eta_{\mathcal L}\lambda(Z)+\lambda(R)=0,
\tag{28}
$$
因为 $Z=NV_H$。

这个次序保留了 whole $E$ 的真实费用：先证明新增自然像的同一比例，再用原同权响应补足全部旧 $E$ 坐标。不能只引用(27)便删除未知自然像，也没有把 signed 响应校正改称一个零基准的实际控制词。

由此得到条件性定理：
$$
\boxed{
\text{每个满足(3)的完整负四自然函数，
在(15)的共同查询上不产生新的负四平移头。}
}
\tag{29}
$$

## 8. 从起点加 M25，同点保 q、整个原纤维和十九个真实根

本节构造(15)所需的新母库，明确不修改任何已经冻结的旧纤维。

从 R413 的 R411 初选版本开始，使同一正解析偶母满足
$$
q=(q_0,q_1,q_2,q_3)=0,\qquad D-E_5>0,
$$
并保原十六个四列正常 minor。R412 的内支撑四正常方向、有限 Morse 扰动和端 collar 固定在这个开邻域中完成。

**从此起点**规定有限观察
$$
\boxed{
F^\star=(F_{\rm rat},D,E_5,M_{25}).
}
\tag{30}
$$
新增三行都是连续 $C^2$ polynomial 泛函；其中 $D,E_5$ 已在 R414 使用，本稿再加一行 $M_{25}$。没有预设这些行独立，也不预设它们的任意数值可以达到。

在 R412 同一个 $q=0$ 解析图册 $\chi(v)$ 中，取
$$
r=\max\operatorname{rank}D(F^\star\circ\chi).
\tag{31}
$$
采用真实受限最大秩，选择 $r$ 个光滑切向与原四个正常向。原十九个 free-jet minor 仍可在避开这些正常支持的固定内区选择；新增积分没有限制那些点态 jets 为某个独立指定常数。

把最大 $F^\star$ minor 与全部十九 minor 的有限光滑见证合入同一个有限维参数空间。它们在同一个 $q=0$ 图册上各不恒零，其有限实解析乘积不恒零，所以可以在原邻域选同一个母 $U_0$ 同时实现。冻结的是该母的实际值
$$
F^\star(U_0),\qquad
D_0=D(U_0),\ E_0=E_5(U_0),\ M_0=M_{25}(U_0),
$$
并保 $D_0-E_0>0$。

原四个正常向加 $r$ 个切向的 Jacobian 仍为
$$
\begin{pmatrix}
Dq[e_1,\ldots,e_4]&0\\
*&DF^\star_I[f_1,\ldots,f_r]
\end{pmatrix},
\tag{32}
$$
两对角块可逆。对每个原真实基本位置，使用 R412 的集中脉冲和这些固定光滑方向作有限 IFT 纠正。脉冲及全部参数导的 $C^2$ 量为 $O(N^{-1/2})$；纠正系数和其参数导同阶。所选 minor 保持非零，受限最大秩保证常秩，故保持的不是仅所选几行，而是整个
$$
q(U_i)=0,\qquad F^\star(U_i)=F^\star(U_0).
\tag{33}
$$
$r=0$ 时切向块为空，常秩论证仍成立。

原十九量对最高三导至多二次。新增的固定光滑纠正与参数导为 $O(N^{-1/2})$，不改变原完整 $C^1$ 极限。全部真实 self、Green、有序 cross 和复制尾仍由原 $F_{\rm rat}$ 精保持。以这个新有限母基线重新选择原严格正幅盒，原交替位置的正 kernel 与十九阶 minor给非退化根，再取一个充分大的**有限** $N$，得到
$$
\boxed{
q(U_i)=0,\quad F_{\rm rat}(U_i)=F_{\rm rat}(U_0),\quad
(D,E_5,M_{25})(U_i)=(D_0,E_0,M_0),\quad
\mathcal V_{19}=0 .
}
\tag{34}
$$

端 collar、正性以及有限个简单 $p/A_f$ 零沿 R412 原分区证明保持：脉冲只在已有 $p<0,A_f<0$ 的固定内区，原零点邻域只有固定光滑小纠正。新增一行没有要求改变任何端恢复规范，也不把所有内部零点压成某个已控点数。

全部有限形状、实际宽度、复制和合法窗口必须按 R412/R414 的原选择次序共同冻结；若后继重新选择几何，仍须支付其实施前提。这里没有在旧最终库上追加一个未经证明可满足的等式，也没有把不同母的独立构造拼成同一个对象。

## 9. 对未付 Q2 的准确使用范围

R422 的原完整两项身份是
$$
\Lambda(V(k))=(1+k^2)^2
\{\Lambda(V_0)+k^2\Lambda(W)\},
\tag{35}
$$
其中 $V_0,W\in U_{-4}$ 是两个明确的原 hh 正规系数。

如果后续分别证明**这两个完整自然函数**满足(3)，则在(30)—(34)同一次新母库上，(28)逐项给
$$
\lambda(V_0)=\lambda(W)=0,\qquad \lambda(V(k))=0
\quad\text{对全部实际 }k.
\tag{36}
$$
这时原正性矩阵的 hh 对角为零，才可按其 PSD 必要条件消去同一矩阵的交叉项。其它尚未付的 kk 全曲率函数仍须处理；本稿不从单锚、连续性或局部主项外推它。

如果新的原式读出保留非局部字、矩乘积或左尾，(3)尚未成立，(36)也尚未获得。若得到有限局部密度但含三阶或更高 jet，仍须在保真实边界的完整 IBP 后确认(3)，不能以 Euler 的某个最高项消失代替这一证明。

本稿独立完成的是：六项穷尽、真实四积分矩阵、所有实际复制的共同比例、完整有序查询消失，以及从起点加入一个母矩仍同点保十九根的构造。它不宣布新的实际联合截面、完整 period 或整个低权正字符问题已经解决。
