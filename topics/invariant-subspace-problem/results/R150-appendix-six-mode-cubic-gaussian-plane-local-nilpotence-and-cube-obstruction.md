# R150 附录：六模式立方二阶矩平面的局部五次归属与三次障碍

日期：2026-11-13（UTC）。作者：normal_rebuild / Astra-ISP-1cf8c51d。

状态：**已证明。** 对下述明确的完整临界点，任意匹配 $B_r$ 的第五个自然幂属于完整局部梯度理想；原三组已付实际逆的 first，其第三个自然幂均不属于该局部理想。因此，这三组选取不可能具有全局自然三次 Jacobian 证书。第四次是否属于本局部理想，仍未由本稿决定。

本稿所有分母只在指定有限标量点附近为单位，没有付它们的实际算子逆；原 $F^3$ 的零参数循环性仍开放。

## 1. 原目标、二阶矩平面与明确点

保持[完整第三矩 Schur 消元](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md)的原 $K,J_3,R_3(y,H),B_r$，不改合并键或自然幂的类型。一次变量为六个 $y_i$，二阶 Hankel 矩阵为 $H=(H_{i+j})_{0\le i,j\le5}$。

令三参数 $T=(t_0,t_1,t_2)$ 确定十一项序列
$$
h_0=t_0,\quad h_1=t_1,\quad h_2=t_2,\qquad
h_{n+3}=5h_{n+2}-\frac{32}{5}h_{n+1}+\frac85h_n.
\tag{1.1}
$$
置 $\mathsf H(T)=(h_{i+j})$。由[指定全等向平面](R150-appendix-isotropic-three-plane-moment-critical-sections-and-matched-bell-values.md)的 $E_+$，每个 $\mathsf H(T)$ 都可写成 $E_+C(T)E_+^{\mathsf T}$，且 $E_+^{\mathsf T}KE_+=0$。故
$$
\mathsf H(T)K\mathsf H(T)=0.
\tag{1.2}
$$

于是
$$
\mathcal G:\qquad y=0,\quad H=\mathsf H(T)
\tag{1.3}
$$
是完整 $R_3$ 的零临界图，而且每个 $B_r$ 在其上为零。确实，此处 $\ell=0$，$R_3=-8\operatorname{tr}((KH)^3)=0$；一次导数由 $y$ 的偶性为零，二阶矩导数由 (1.2) 为零。完整第三矩消元还给 $V=0$。这里只是形式二阶累积量截面，不要求正测度。

取
$$
p_+:\quad T=(1,0,0),\quad y=0,
$$
即
$$
(H_0,\ldots,H_{10})=
\left(1,0,0,\frac85,8,\frac{744}{25},\frac{2504}{25},
\frac{40392}{125},\frac{127784}{125},
\frac{2002216}{625},\frac{6245128}{625}\right).
\tag{1.4}
$$
令 $\mathcal O_+=\mathbb C[y,H]_{\mathfrak m_{p_+}}$，并令
$$
I_+=(\nabla R_3)\mathcal O_+.
$$

**定理。**

1. 对每个 $r\in\mathbb C^6$，有 $B_r^5\in I_+$。
2. 对[原平方精确证明](R150-appendix-six-mode-exact-jacobian-jets-and-all-square-fibers.md)选出的三个 $r=(A,B,0,0,0,1)$，均有 $B_r^3\notin I_+$。

因此这三个候选在本局部的最小自然幂只可能是四或五；没有由此排除使用较高自然幂的全局证明。

## 2. 十二个真实梯度的消元

保留两个一次横向坐标
$$
u=y_4,\qquad v=y_5.
$$
将其余四个一次坐标 $y_0,\ldots,y_3$，以及八个二阶偏差 $H_3-h_3(T),\ldots,H_{10}-h_{10}(T)$，合记为 $q\in\mathbb C^{12}$。所以 (1.3) 的理想为
$$
J=(u,v,q).
$$
这是原局部环的可逆线性坐标换元。

取原完整 Hessian 在
$$
(y_0,y_1,y_2,y_3,H_3,H_4,\ldots,H_{10})
$$
上的十二阶主块 $M$。原 $J_3$ 行列式模 $103$ 为 $75$；准确有理计算给
$$
\boxed{\det M\equiv81\pmod{103}\ne0.}
\tag{2.1}
$$
故 $M$ 在 $\mathcal O_+$ 中可逆。

记 $g=\partial_qR_3$、$I_q=(g)$，并在商环
$$
\mathcal A=\mathcal O_+/I_q
$$
中工作。有限差商分解 $g=M_0q+u c+v d$ 中 $M_0(p_+)=M$，故模 $I_q$ 有 $q\in(u,v)$。因此 $J$ 的像恰为
$$
\mathfrak a=(u,v)\mathcal A.
\tag{2.2}
$$
尤其每个 $\overline{B_r}\in\mathfrak a$。

对任意固定有限次数，可以逐次用同一可逆的十二阶线性块解出 $q$ 关于 $u,v$ 的系数；每一步的系数都是 $T$ 附近的正规有理函数。代回与截断次数相同的商环得到相互逆的有限代数映射。这为下文的有限 Taylor 系数提供准确含义，不要求把局部环换成其完成。

## 3. 沿整个三参数图的二次项都消失

这一点必须沿 (1.3) 证明，不能只在 $T=(1,0,0)$ 检查。

在 $y=0,H=\mathsf H(T)$ 处，$R_3$ 的 $y$-二次部分只有
$$
-18\,e(y,T)^{\mathsf T}J_3^{-1}e(y,T),
$$
其中
$$
e_m(y,T)=[z^m]\big(v(z)^{\mathsf T}K\mathsf H(T)Kv(z)\big)
\big(v(z)^{\mathsf T}Ky\big).
$$
因为 $\operatorname{tr}((KH)^2)=0$ 且 $HKH=0$，$G_6$ 的全部 $y$-二次项均为零。因此若 $e=E(T)y$，则准确 Hessian 为
$$
Y(T)=-36E(T)^{\mathsf T}J_3^{-1}E(T).
\tag{3.1}
$$
它是 $T$ 的二次矩阵多项式。

令 $A(T)=Y(T)[\{0,1,2,3\}]$。下列三个五阶子式恒为零：
$$
\det Y[\{0,1,2,3,i\},\{0,1,2,3,j\}]=0,
\qquad (i,j)=(4,4),(4,5),(5,5).
\tag{3.2}
$$
这里有一个完整的有限恒等式证书：三式均是 $T$ 的齐次十次多项式。清去共同有理分母后，在
$$
t_0=1,\qquad (t_1,t_2)=(a,b),\quad
a,b\in\{0,1,\ldots,10\},\quad a+b\le10
$$
的全部 $66$ 个节点，$198$ 个整数 Bareiss 行列式严格为零。

这些节点对总次数不超过十的二变量多项式是唯一决定的：按 $t_2=0,1,\ldots,10$ 逐层作一变量插值，或使用
$\prod_{i<a}(t_1-i)\prod_{j<b}(t_2-j)$、$a+b\le10$ 的三角基，即得每个系数为零。再用齐次性便得 (3.2) 的原三变量恒等式。这里只使用特征零整数恒等式，不以有限域零值冒充恒等式。

在 $p_+$，十二块 $M$ 按 $y/H$ 分块，对角块分别为这个四阶 $A$ 和八阶 $H$ 块，交叉块为零。由 (2.1)，$A$ 在附近为单位。于是 (3.2) 准确给出两个保留一次坐标的 Schur 补为零。

原 $R_3$ 对 $y\mapsto-y$ 为偶。十二梯度的有限逐次解也保持四个被消去的 $y$ 坐标为奇、八个 $H$ 偏差为偶的对称性。结合二次 Schur 补恒零，商环中的
$$
\bar f=\overline{R_3}
$$
满足
$$
\boxed{\bar f\in\mathfrak a^4.}
\tag{3.3}
$$
其四次首项是二元齐次式 $F_4(T;u,v)$；系数为 $T$ 的正规有理函数。

特别，沿三个图参数的完整导数也从 $\mathfrak a^4$ 起。这一步保留了原全部梯度，而非只研究两个横向导数。

## 4. 二元四次首项的准确证书

在 $T=(1,0,0)$，令
$$
F_4=c\,Q_4,\qquad
Q_4=q_0u^4+q_1u^3v+q_2u^2v^2+q_3uv^3+q_4v^4,
\tag{4.1}
$$
其中 $q_i$ 是互素整数，$c$ 为非零有理数。全部五个整数及 $c$ 保存在[精确有限证书](../notes/2026-11-13-six-mode-cubic-gaussian-plane-local-certificate.json)，由[自含验证器](../notes/2026-11-13-six-mode-cubic-gaussian-plane-local-verify.py)直接从原 $R_3$ 生成。

其很小的非零性见证是
$$
(q_0,q_1,q_2,q_3,q_4)\equiv(90,27,54,83,62)\pmod{103},
$$
$$
\boxed{\operatorname{Res}_{u,v}(\partial_uQ_4,\partial_vQ_4)
\equiv71\pmod{103}\ne0.}
\tag{4.2}
$$
这里的 resultant 是两个二元三次式的六阶 Sylvester 行列式，亦即两个三次式乘二次单项式后，映到六维五次齐次空间的行列式。故它的非零性严格给
$$
(u,v)^5\subset
(\partial_uF_4,\partial_vF_4)
\quad\text{在齐次五次层成立。}
\tag{4.3}
$$
其矩阵在 $T=(1,0,0)$ 非零，因此在图参数的局部环中为单位。

验证器还真正解完十二个 $q$ 梯度到总次数三，并逐项核验原十七个梯度的全部三阶系数：十二个被消去的梯度及三个图参数梯度到三次都为零；仅保留的两项准确为 $\partial_uF_4,\partial_vF_4$。它没有省掉这些十五个原条件。具体复算使用 $(u,v)=(1,0),(0,1),(1,1),(1,-1),(1,2)$ 五条射线：逐阶解的第 $j$ 次系数依赖 $(u,v)$ 为齐次 $j$ 次多项式，所以每个三次梯度由其中任意四个不同射影方向唯一确定，四次目标由全部五个方向唯一确定。因而此有限检验决定所有系数，并非只在五个采样点成立。

## 5. 特征零局部环中的五次归属

在 $\mathcal A$ 上使用保持十二个 $g$ 的导子
$$
D_u=\partial_u-
(\partial_qg)^{-1}(\partial_ug)\cdot\partial_q,
\qquad
D_v=\partial_v-
(\partial_qg)^{-1}(\partial_vg)\cdot\partial_q.
\tag{5.1}
$$
它们严格保持 $I_q$，并满足 $D_uu=D_vv=1$、$D_uv=D_vu=0$，也保持 $T$ 不变。与[局部立方引理](R150-appendix-six-mode-cubic-local-jacobian-cube.md)相同，这些都是普通局部化中的有理导子。

由 (3.3)，
$$
D_u\bar f=\partial_uF_4\pmod{\mathfrak a^4},
\qquad
D_v\bar f=\partial_vF_4\pmod{\mathfrak a^4}.
$$
两项均属于完整梯度理想在 $\mathcal A$ 中的像 $\bar I_+$。把 (4.3) 的准确二次乘子用于这两项，得到
$$
\mathfrak a^5\subseteq \bar I_++\mathfrak a^6.
\tag{5.2}
$$

为明确说明这里确实结束了误差，而不是无限形式迭代，令 $L$ 是 $\mathfrak a^5$ 在 $\mathcal A/\bar I_+$ 中的像。它由六个五次单项式生成，且 (5.2) 给 $L=\mathfrak a L$。对这六个生成元写成矩阵式 $\ell=C\ell$，其中 $C$ 的条目都在局部极大理想内。则 $\det(I-C)$ 为单位，乘伴随矩阵即得 $\ell=0$。所以
$$
\boxed{\mathfrak a^5\subseteq\bar I_+.}
\tag{5.3}
$$
再由 $\overline{B_r}\in\mathfrak a$，得到对每个 $r$
$$
\boxed{B_r^5\in I_+.}
\tag{5.4}
$$
没有使用全局 Nullstellensatz、未验证的分支分类或任何实际算子分母。

## 6. 两个三次梯度的张成空间没有纯立方

令
$$
G=(4q_0,3q_1,2q_2,q_3)^{\mathsf T},\qquad
H=(q_1,2q_2,3q_3,4q_4)^{\mathsf T}
$$
为两个三次导数的系数列。它们前两行的 $2\times2$ 子式模 $103$ 等于 $25$，故可准确构造两个有理左核：分别令第三、第四坐标为一，另一自由坐标为零，再解前两坐标。

把纯立方
$$
(\alpha u+\beta v)^3
$$
的系数列 $(\alpha^3,3\alpha^2\beta,3\alpha\beta^2,\beta^3)$ 代入这两个左核，得到两个二元三次式。它们按同一顺序的系数模 $103$ 为
$$
(93,95,3,0),\qquad (0,16,0,1).
$$
准确的六阶 Sylvester 行列式满足
$$
\boxed{\operatorname{Res}\equiv101\pmod{103}\ne0.}
\tag{6.1}
$$
全部左核分母与 $103$ 互素。所以这两个二元三次式在特征零没有非零共同点，得到
$$
\boxed{
0\ne L\text{ 为一次式}
\quad\Longrightarrow\quad
L^3\notin\operatorname{span}_{\mathbb C}
\{\partial_uF_4,\partial_vF_4\}.
}
\tag{6.2}
$$

## 7. 完整 Artin 商与原三个候选的三次障碍

把十二个梯度逐次解到三阶，再令三个图参数等于基点值，给出原局部环到有限代数
$$
\mathscr B=
\frac{\mathbb C[u,v]}
{(u,v)^4+(\partial_uF_4,\partial_vF_4)}
\tag{7.1}
$$
的明确同态。它的原点是 $p_+$，故局部环中原有的单位都映成单位。

第4节已核验：原全部十七个梯度在 (7.1) 中为零。十二个消去梯度到三阶为零，三个图参数梯度从四阶起，剩余两个三次式在 (7.1) 中按定义为零。因此 $I_+$ 被送到零，不能只核两个横向条件后声称这是原理想的商。

设 $B_r$ 的一阶像为 $L_r(u,v)$。因为 $B_r(p_+)=0$，其第三次自然幂在 (7.1) 中的像恰为 $L_r^3$。由 (6.2)，
$$
L_r\ne0\quad\Longrightarrow\quad B_r^3\notin I_+.
\tag{7.2}
$$

现在对原三个方向核验 $L_r\ne0$。仍令
$$
f(d)=3725d^3-43931504d^2+6080833024d+52565262336,
$$
$$
A=-\frac{521d^2-46784d+271360}{160(5d-704)},\qquad
B=A+d,\qquad r=(A,B,0,0,0,1),
\tag{7.3}
$$
其中 $d$ 为其任一实根。取 $L_r$ 的 $u$ 系数 $a_r$。

在准确三次代数 $\mathbb Q[d]/(f)$ 中计算这个系数；所有常数分母在 $103$ 处为单位。相应模 $103$ 数据为
$$
\bar f=d^3+76d^2+5d+35,
$$
$$
A=35+4d+59d^2,\qquad
B=35+5d+59d^2,\qquad
a_r=40+94d+2d^2.
$$
原 $A$ 的分母的乘法行列式模 $103$ 为 $37$，而
$$
\boxed{
\det\big[m_{a_r}:\mathbb F_{103}[d]/(\bar f)
\longrightarrow\mathbb F_{103}[d]/(\bar f)\big]=57\ne0.
}
\tag{7.4}
$$
这严格证明相应特征零的乘法行列式非零，所以 $a_r$ 在 $f$ 的每个根上都非零。并未把一个有限域非零值当成某一个实根的近似。

因此三个原 $r$ 都满足 $L_r\ne0$，(7.2) 给
$$
\boxed{B_r^3\notin I_+\quad\text{对原三个候选分别成立。}}
\tag{7.5}
$$
结合 (5.4)，其局部最小自然幂只能为四或五。

## 8. 对原全局问题的准确含义

如果 $B_r^3$ 属于原未局部化的全局梯度理想，它必属于 $I_+$，与 (7.5) 矛盾。因此原这三组选取的全局自然三次证书已经排除。经已付完整 Schur 理想等价，相同结论适用于原完整匹配 Bell 立方的自然三次分母。

相反，(5.4) 只是在 $p_+$ 的局部五次归属，不能自动变成全局第五次证书。尚须处理其他临界点和局部分母；这些分母未被证明有原实际有界交换逆。第四次在此点是否仍失败，本稿没有决定。原 $F^3$ 零参数循环性、全部更高目标与普通 ISP 保持开放。
