# R456：真实同角色镜对上的两个最高有序不变量与完整响应评价商

日期：2026-11-16。**完整纸面证明与已发表原源的只读消费；没有执行 profile、积分、符号程序、数学秩、格点枚举、人工测试或科学任务。**

[R454](R454-complete-response-self-principal-trace-and-seven-ordered-current-invariants.md) 已证明，整个原响应空间中保持 whole $E=(\pi,\mathcal Q)$ 的响应，其三尾退化点 current 像准确是
$
\ker D\subset\mathscr C_{39},\qquad
D:\mathscr C_{39}\longrightarrow\operatorname{Pol}_{\le6}.
$
这里的七个形式系数尚不是七个实际独立障碍。本稿把它们放到 [R455](R455-four-natural-moments-with-one-common-degenerate-pair-and-twenty-targets.md) 已构造的唯一共同镜对及原真实复制位置上。

主要结论是：固定一个实际宽度，使用一个原 suffix 零阶矩非零的同角色族及至少八个已有不同中心，完整评价满足
$
\boxed{D(\ker\operatorname{Eval})=\operatorname{Pol}_{\le4}.}
$
因此相对于**全部** whole-$E$ 零响应，这个完整同宽镜点族的有序评价商恰剩两个形式坐标 $D_5,D_6$。原 R295 末 low/high 布局提供所需 $n_0\ne0$ 的具体角色；没有把三尾矩假设成三个独立物理参数。

这个结论可以同时包含该宽度下的全部角色、全部真实 suffix 和全部对应副本。它不是把每个角色分别选出的成本拼接。若整个库有多个实际宽度，必须保留最后一节的共同评价问题；不能把单宽右逆免费搬到全宽。

直接来源为 [R433](R433-actual-universal-ordered-flux-zero-and-explicit-local-cap-currents.md) 的完整局部 current 和 actual $J^+$ 接口、[R434](R434-complete-self-kernel-and-three-tail-current-image-on-144-original-responses.md) 的原三十二维像、R454、R455，以及 [R295](R295-final-grid-forces-zero-platform-matrix-and-exact-self-history-principal.md) §§2–2.2、R397 §§4–5 的真实 suffix 与完整 cell 定义。没有重算上述旧秩或原母根。

## 1. 原 current、实际余行与规范

全稿先在原同锚范围
$
E(V)=0,\qquad \mathcal O(V)=0
\tag{1}
$
工作。实际成本可取 R433 的同一 $J^+=(E,\mathcal A,\mathcal O)$ 零背景；$\mathcal A$ 仍仅是该最终库的有限自然查询，不是 universal self 自然全零。

对左包 $u$ 及右包三矩参数 $n$，R433 给完整原输出
$
\mathcal U_{V,n}=4Q_{V,n},\qquad
\int_{\ell_u}^{x}u'\mathcal U_{V,n}''
=\mathcal K_{V,n}(x;u).
\tag{2}
$
所有 $s$-history、原右常数与 $J_0,J_1,J_2$ 已在其系数中。式(2)不是只对 principal 或一个重置左锚的原函数成立。

置
$
p=u',\quad r=u'',\quad A_u=6pu'''-2r^2,
\qquad F_V(x,u,p,r;n)=\frac14\mathcal K_{V,n}\big|_{A_u=0}.
\tag{3}
$
$F_V$ 是三次 jet 多项式，对 $n$ 线性。外根满足 $p\ne0$，但 R433 的公式本身没有除 $p$。

实际圆的原符号仍为
$
f=\sum_i a_i u_i,\quad g=\sum_i b_i u_i,\quad
R_i=a_i^2-b_i^2,\quad T_i=a_ib_i.
$
令
$
n_{R,i}=\sum_{j>i}R_j\mu_j,\quad
n_{T,i}=\sum_{j>i}T_j\mu_j,\quad
n_i=T_i n_{R,i}-R_i n_{T,i}.
\tag{4}
$
这里
$
\mu_j=\left(\int(u_j'')^2,\ \int x(u_j'')^2,\
\int\{x^2(u_j'')^2+2(u_j')^2\}\right).
$
R397/R433 的准确消-self 组合为
$
\boxed{\mathcal C_{i,\pm}
=R_iH_{e,i,\pm}+T_iH_{d,i,\pm}
=4a_i^3F_V(x_{i,\pm},u_i,p_i,r_i;n_i).}
\tag{5}
$
其真实原累计量 $H_d,H_e$ 和原平台项使用同一成本。whole $E$ 消的是二次尾，未把仿射尾置零。

所有允许的同一二阶 gauge 给 $2\tau L_f(k)$；原
$p(L_fk)''=\{A_f(pk''-f''k')\}'$
使它在各真 $A_f$ 点的累计量为零。因此(5)也是原 period 的必要不变量，不是可由换 gauge 重置的读出。

## 2. 十三列完整形式空间及 D

为缩短式子，将 R433 的 $\ell_0,\ell_1,\ell_2$ 写成
$
\begin{aligned}
a(x,n)&=A_0(n)+A_1(n)x+A_2(n)x^2,\\
b(x,n)&=B_0(n)+B_1(n)x-3A_1(n)x^2-2A_2(n)x^3,\\
c(x,n)&=C_0(n)-2B_0(n)x-B_1(n)x^2
+2A_1(n)x^3+A_2(n)x^4 .
\end{aligned}
\tag{6}
$
每个 $A_j,B_j,C_0$ 是 $n$ 的线性函数。不是将它们称为实际成本可自由指定的 normal 系数。

六个规范代表取 R433(18b) 的
$
d=-\left(\frac32A_0+\frac54B_1\right)x^2+2A_1x^3+A_2x^4,
\quad
e=-C_0x+B_0x^2+2(A_0+B_1)x^3-\frac52A_1x^4-A_2x^5 .
$
其完整根值为
$
\begin{aligned}
F_{\rm can}={}&
\frac{2A_2}{3}u^3
+(A_0+B_1/2-2A_1x-2A_2x^2)up^2\\
&-(B_0+B_1x-3A_1x^2-2A_2x^3)upr-\frac c6ur^2\\
&+\left(\frac{2B_0}3-2A_0x-B_1x+2A_1x^2+\frac{4A_2}3x^3\right)p^3\\
&+\left((3A_0+5B_1/2)x^2-4A_1x^3-2A_2x^4\right)p^2r\\
&+\left(\frac{2C_0}3x-\frac{2B_0}3x^2
-\frac{4(A_0+B_1)}3x^3+\frac{5A_1}3x^4+\frac{2A_2}3x^5\right)pr^2 .
\end{aligned}
\tag{7}
$
余下七个 $p,r$ 列是
$
p^3,\quad p^2r,\quad xp^2r,\quad pr^2,\quad
xpr^2,\quad x^2pr^2,\quad
S_7=2xp^3-5x^2p^2r+3x^3pr^2.
\tag{8}
$
各乘 $n_0,n_1,n_2$，给既有 $\mathscr C_{39}$。这是原完整 ODE 规范，不新增一个独立 rank 计算。

定义
$
D_F(x)=c(x;(1,x,x^2))
=\sum_{\nu=0}^6D_\nu(F)x^\nu.
\tag{9}
$
(8)不改变 $c$ 或 $D$。显然 $D$ 满到 $\operatorname{Pol}_{\le6}$，例如 $C_0(n)$、$B_0(n)$、$B_1(n)$、$A_1(n)$、$A_2(n)$ 的原多项式次数给各单项。

记 $A_j(n)=\sum_{\nu=0}^2A_j^{[\nu]}n_\nu$，其余同理。最高两项准确为
$
\boxed{D_6=A_2^{[2]},\qquad D_5=A_2^{[1]}+2A_1^{[2]}.}
\tag{10}
$

R454 的完整响应定理现在可以直接写成
$
\boxed{\operatorname{im}(\mathcal R\cap\ker E\longrightarrow\mathscr C_{39})
=\ker D.}
\tag{11}
$
不把 $\mathcal R$ 限成144列；反向满像则已有 R434 的原144来源证书。每个这样的响应同时杀全部自然函数，因此保持原 $J^+$。

## 3. 真实镜点与同角色 suffix 输运

固定一个物理宽度及实际共同 cap。以该包中心为零，R455 给唯一镜对
$
x_-=-b_*,\quad x_+=b_*,\quad
u_-=u_+=h_*r_*,\quad
p_-=s_*r_*,\quad p_+=-s_*r_*,
\tag{12}
$
其中
$
b_*>0,\quad r_*>0,\quad h_*>0,\quad s_*>0.
$
下文简写 $b,h,s,r$。这些都是最终 profile 的真实值；没有改母、改变 cap 或为每个点另选参数。

对一个共同平移量 $t$，用 $\varepsilon=+1$ 表示左根、$\varepsilon=-1$ 表示右根：
$
x_\varepsilon=t-\varepsilon b,\qquad
u=hr,\quad p=\varepsilon sr .
$
若参考角色的有效 suffix 为 $n=(n_0,n_1,n_2)$，其真实平移为
$
\boxed{n(t)=(n_0,\ n_1+tn_0,\ n_2+2tn_1+t^2n_0).}
\tag{13}
$
式(13)包含原第三矩中的 $2\int p^2$；没有丢掉一个独立常数。

定义归一化 pair 多项式
$
E_\varepsilon(F)(t)
=r^{-3}F(t-\varepsilon b,hr,\varepsilon sr,r;n(t)).
\tag{14}
$
由(7)—(8)，固定外部 $n$ 时次数至多五；(13)最多再加二次，故
$
E_\varepsilon(F)\in\operatorname{Pol}_{\le7}.
\tag{15}
$

因此在八个真实不同 $t_j$ 上，两个方向都为零，等价于(14)两个完整多项式恒零。这仅用次数与根数的精确事实，不求新的数值 Vandermonde 秩。多于八个原副本并不需要重作一个研究计算。

## 4. 两个最高系数确由真实 n0 检出

先保 $n_0\ne0$。由(7)，最高 degree7 只来自
$A_2^{[2]}n_2(t)$ 的 $2x^5pr^2/3$，所以
$
[t^7]E_\varepsilon(F)
=\varepsilon\,\frac23s n_0D_6.
\tag{16}
$
两条多项式恒零首先迫 $D_6=0$。

在这以后，置
$
B=A_2^{[1]},\qquad C=A_1^{[2]}.
$
需要保留(7)的完整偶、奇部分。两个可能贡献最高 degree6 的原列是
$
\begin{array}{c|l|l}
&\text{不含 }\varepsilon\text{ 的部分}
&\varepsilon s\text{ 乘的部分}\\ \hline
A_1&
-2hs^2x-(h/3+4s^2)x^3&
(3h+2s^2)x^2+5x^4/3\\
A_2&
2h^3/3-2hs^2x^2-(h/6+2s^2)x^4&
(2h+4s^2/3)x^3+2x^5/3 .
\end{array}
\tag{17}
$
把(13)与 $x=t-\varepsilon b$ 代入，准确得到
$
[t^6]E_\varepsilon(F)
=\varepsilon\,\frac{s n_0}{3}(5C+2B),
\tag{18}
$
以及两方向 degree5 的共同部分
$
\boxed{
\frac12[t^5](E_+(F)+E_-(F))
=-n_0\left(\frac h6+2s^2+\frac{10bs}{3}\right)(2C+B).
}
\tag{19}
$
(19)的 $10bs/3$ 是真实左右位置偏移，不能把两根都当在中心 $t$。

其余原列在这一步的最高 degree5 都是两方向反号，故不贡献(19)：
$A_0,B_1$ 与(8)的最高项至多是三次 odd，乘 $n_2(t)$ 后如此；
$A_1^{[1]},A_2^{[0]}$ 的 degree5 同样反号；
$C_0,B_0$ 更低。
$n_1,n_2$ 的低次部分也只进相应反号项或低阶。
因此(18)—(19)没有漏掉旧七列或真实 suffix 的 lower coefficients。

由于
$
\frac h6+2s^2+\frac{10bs}{3}>0,
$
(19)为零迫 $D_5=2C+B=0$。若还用(18)，则 $B=C=0$；
后一个更强参数结论不是定义本稿商所必需的。

遂有
$
\boxed{
D(\ker E_+\cap\ker E_-)\subset\operatorname{Pol}_{\le4}.
}
\tag{20}
$
这个推导只使用一个真实 $n_0\ne0$ 的角色，不把 $n_0,n_1,n_2$ 独立变化。

### 4.1 从有限实际值直接读取 D5、D6

(15)允许用任何八个已有中心的 Lagrange 插值，准确恢复 $E_\pm$ 的系数。先取
$
D_6=\frac{3}{4sn_0}[t^7](E_+-E_-).
\tag{21}
$
令 $F_6$ 为(7)中唯一参数 $A_2(n)=n_2$ 的完整形式代表；
它满足 $D_{F_6}=x^6$。
从评价向量减 $D_6 E_\pm(F_6)$，得到 $\widetilde E_\pm$，再取
$
\boxed{
D_5=
-\frac{[t^5](\widetilde E_++\widetilde E_-)}
{2n_0(h/6+2s^2+10bs/3)}.
}
\tag{22}
$
这里只用形式代表定义一个确定的读出减项，不要求 $F_6$ 本身是可控成本。

## 5. 显式 mirrorblind 形式提升给出反向包含

本节不能只以(20)当成等式。要保留五个低系数，须给出同一完整形式 current，其**两个镜点在所有 x 都为零**。

固定任意
$
c(x)=c_0+c_1x+c_2x^2.
$
在(6)—(7)取
$
A_1=A_2=0,\quad
B_0=-c_1/2,\quad B_1=-c_2,\quad C_0=c_0,
\quad
A_0=\frac{c_2(5s^2+3h)}{14s^2}.
\tag{23}
$
其 $c(x)$ 正是所给二次式。

将规范代表除 $r^3$，写成
$
F_{\rm can}/r^3=E(x)+\varepsilon s\,O(x).
$
这里 $E$ 至多二次，$O$ 至多三次。最高两项为
$
E_2=(3A_0+5B_1/2)s^2+B_1h/6,\qquad
O_3=-4(A_0+B_1)/3.
$
(23)准确给
$
E_2+\frac{5s^2}{3}O_3
=\frac{7s^2}{9}A_0-\frac{c_2(5s^2+3h)}{18}=0.
\tag{24}
$
原第七列满足
$
S_7/r^3=-5s^2x^2+\varepsilon s(2s^2x+3x^3).
$
加上 $4(A_0+B_1)S_7/9$，同时消 $E_2,O_3$。
剩余 even 至多一次、odd 至多二次，分别由
$
p^2r,\ xp^2r;\qquad pr^2,\ xpr^2,\ x^2pr^2
$
逐项消去；$s>0$ 保全部所需除数非零。

由此得到一个确定的线性形式提升
$
c\longmapsto B_{h,s}(c)\in\mathscr C_{13},
\qquad
B_{h,s}(c)(x,hr,\pm sr,r)=0\quad\text{对全部 }x,
\tag{25}
$
其 $c$ 系数不变。(25)是形式空间中的构造，未将每一列宣布为实际成本；后面只用它与真实 $\ker D$ 比较。

给定任意 $d(x)=\sum_{\nu=0}^4d_\nu x^\nu$，例如取
$
c^{(0)}=d_0+d_1x+d_2x^2,\qquad
c^{(1)}=d_3x^2,\qquad
c^{(2)}=d_4x^2
$
并置
$
B_d(x,u,p,r;n)=\sum_{j=0}^2n_j B_{h,s}(c^{(j)})(x,u,p,r).
\tag{26}
$
则
$
D(B_d)=c^{(0)}+xc^{(1)}+x^2c^{(2)}=d,
$
而 $B_d$ 在固定镜对的所有实际位置和**任意** suffix $n$ 上均为零。

结合(20)，得到精确结论
$
\boxed{
D(\ker\operatorname{Eval}_{\rm role})
=\operatorname{Pol}_{\le4}.
}
\tag{27}
$
其中 Eval_role 可以取一条完整同角色 polynomial，也可以取其至少八个真实不同中心的两根评价。

更强地，在同一固定 $h,s,r,b$ 的库中追加任意多个角色、任意真实 suffix 及全部对应位置，(26)仍在评价核内。只要其中包含第4节的一条 $n_0\ne0$ 角色族，仍有
$
\boxed{
D(\ker\operatorname{Eval}_{\rm all\ roles,\ one\ width})
=\operatorname{Pol}_{\le4}.
}
\tag{28}
$
这里是同一个 $B_d$，不是逐角色重新选取后相加。

## 6. 原有限布局确有 n0 非零的角色

现回原实际布局，而不把(13)当作可自由设计的矩族。

R295 §§2–2.2 逐原 R280 正布局给
$
i=kL+j,\quad L=17^{11},\quad K=2^{11},
\quad \epsilon_k=(-1)^{\operatorname{popcount}(k)},
$
$
R_H=8B,\ T_H=\epsilon_k3B,\qquad
R_L=-B/2,\ T_L=\epsilon_k B/\sqrt2,\quad B>0.
\tag{29}
$
所以
$
T_LR_H-R_LT_H
=\epsilon_k B^2(4\sqrt2+3/2)\ne0.
\tag{30}
$

在最右正布局的一份完整基本圆内，取最后 $k=K-1$ 子块。
其最后 high 是 $j_H=L-7$，紧前的 $j_L=L-8$ 是 low；
R295 的原17进制末位推导还给前面至少三个 low。
当前只需最邻近的这一个。

在该 low 右方，后续 low 与它的 $(R,T)$ 成比例，
故每一项 $T_LR_j-R_LT_j$ 都为零。
high 只有 $j_H$ 一项，且没有更右的 $k$ 子块。
于是这份基本圆内部的准确有效 suffix 是
$
\boxed{
n_{\rm role}
=\epsilon_{K-1}B^2(4\sqrt2+3/2)\,\mu_{j_H}.
}
\tag{31}
$
真实非零 high 包有 $(\mu_{j_H})_0=\int(u_{j_H}'')^2>0$，故
$
(n_{\rm role})_0\ne0.
\tag{32}
$
所有原 $a_i\ne0$ 亦在 R295 的当前模板中明确保留。

### 6.1 更右完整块不产生遗漏的 suffix

R397 §5 的 cell 是十二包装中的一个**完整八副本块，含全部最细编码和完整圆**，不是八个孤立同轴包。其原三矩闭合为
$
\sum_{i\in{\rm cell}}R_i\mu_i=0,\qquad
\sum_{i\in{\rm cell}}T_i\mu_i=0.
\tag{33}
$
原来源是 R280 的完整三矩编码、R324 的实际副本库与逐包 $\mathcal F_{\rm rat}$ 保三矩；R431/R455 的最终形状也准确保持这些三矩。

应在每个选中完整 cell 的**最右内部副本**中选(31)的同一个角色。
该 cell 内此后没有另一内部副本；它右边的所有完整 cells、其它完整最终块及预先加入的完整宏块都满足(33)。
所以它们对(4)的贡献准确为零，(31)没有漏掉外部后缀。

八副本的 $\alpha^3$ 交替权负责原第三差分，**不能**单独证明(33)；
这里使用的是含全部原 $R/T$ 编码的完整圆三矩身份。
这个区别也正是 R435 的 cell 术语修正。

### 6.2 十二个真实位置与原幅度归一

固定一个最终正布局 block、一个实际宽度和其它外层角色。
其十二个已有完整 cells 给上述角色十二个不同的物理中心 $t_j$。
同角色外 cap 相同；R455 的最终二十目标纠正严格不动这个 cap 和原 $\mu$。
因此不需要移动原根或增加新的 profile 查询位置。

把 cell 的共同幅度写成 $\gamma_j\ne0$，整块 g 翻号写成 $\delta_j=\pm1$；
其余固定内层幅度吸收在参考角色 $a_i,b_i$ 中。
原实际系数变换为
$
a_{ij}=\gamma_j a_i,\quad
b_{ij}=\delta_j\gamma_jb_i,\quad
R_{ij}=\gamma_j^2R_i,\quad
T_{ij}=\delta_j\gamma_j^2T_i .
$
把 profile 幅度归入这些系数以后，参考矩仅作真实平移。由(4)、(33)
$
n_{ij}=\delta_j\gamma_j^4 n_i(t_j).
\tag{34}
$
于是由(5)
$
\boxed{
\frac{\mathcal C_{ij,\varepsilon}(V)}
{4\delta_j\gamma_j^7a_i^3r^3}
=E_\varepsilon(F_V)(t_j).
}
\tag{35}
$
所有分母非零；$\gamma^7$ 来自外 $a^3$ 和 suffix 的四次幅，不能误写成四次或五次。

(35)把第3–5节的 polynomial 评价直接识别成原 raw period 组合的有限真实值。任选其中八个原不同中心即可；其余四个并非由新的数值拟合补出。

## 7. 完整响应评价商与真正的同一成本补偿

由(11)、(28)及线性代数的第一同构定理，
$
\boxed{
\frac{\operatorname{Eval}(\mathscr C_{39})}
{\operatorname{Eval}(\mathcal R\cap\ker E)}
=
\frac{\operatorname{Eval}(\mathscr C_{39})}
{\operatorname{Eval}(\ker D)}
\ \simeq\
\frac{\operatorname{Pol}_{\le6}}{\operatorname{Pol}_{\le4}}
\simeq\mathbb R^2.
}
\tag{36}
$
这里 Eval 是第6节真实族，并可包括该固定宽度下的全部其它角色和镜点。
这不是宣称整个 actual $U$ 必须映满右边两维。

对一个已经满足(1)的具体目标成本 $V$，其全部这些 $\mathcal C$ 值可被一个 signed whole-$E$ 零响应同时清除，当且仅当
$
\boxed{D_5(V)=D_6(V)=0.}
\tag{37}
$
必要性由(21)—(22)和R454响应 $D=0$ 得到。
充分性也有明确原式构造：令 $F=F_V$，按(26)取 $B_{D_F}$；
则
$
F-B_{D_F}\in\ker D.
$
由原 R434 的既有三十二维像证书，选择同一个
$R\in\mathcal B(E_8,Z)\cap\ker\mathcal Q\subset\mathcal R\cap\ker E$
使其 current 为 $-(F-B_{D_F})$。
净评价只剩 $B_{D_F}$，在所有这些真实根上同时为零。
该响应同时保持原 $J^+$，没有把它对 self 通道的代价删除。

(37)是完整有序 $\mathcal C$ 的 signed 评价结论。
实际路径的同点增强还必须把这一个响应的原 prototype 成本、
后置 quotient 校正、完整 self partial 和其余规范基准一起入账。
本文不把 signed 加法自动称为已构造的实际 $C^1$ 截面，
也不因为两个 quotient 系数消失就宣全部 period 已解。

## 8. 多个真实宽度的准确边界与一个共同低次提升

R455 的原母 cap 经正伸缩 $w$ 后，
$
h_w=w^2h_0,\qquad s_w=ws_0,\qquad b_w=wb_0.
\tag{38}
$
原公共幅度可并入 $a_i,b_i$；即使放在 profile 内，
比值
$
\kappa_{\rm cap}=\frac{u r}{p^2}=\frac{h_w}{s_w^2}>0
\tag{39}
$
仍不变。它不是几何曲率参数。

(23)—(26)在单宽下给全部 $\operatorname{Pol}_{\le4}$。
其低列的最终扣除一般依赖实际 $h_w,s_w$；
因此对不同宽度分别得到的响应，不能未经共同求解就相加。
本稿不以此证明整个多宽库也只有两个余量。

不过，两个低次 mirrorblind 提升可以直接在所有宽度共用。
由(7)的 $c=1$ 或 $c=x$ 代表加(8)，准确得到
$
\boxed{
B^{(0)}=\frac{\kappa_{\rm cap}p^2r-ur^2}{6},
\quad c(B^{(0)})=1,
}
$
$
\boxed{
B^{(1)}=(ur-\kappa_{\rm cap}p^2)
\left(\frac p2-\frac{xr}{6}\right),
\quad c(B^{(1)})=x.
}
\tag{40}
$
例如 $c=x$ 的规范代表是
$upr/2-xur^2/6-p^3/3+x^2pr^2/3$；
补 $(1/3-\kappa_{\rm cap}/2)p^3+
\kappa_{\rm cap}xp^2r/6-x^2pr^2/3$ 即为(40)。
所以没有把 $up^2$ 或别的额外自由单项塞入七列。

两式在实际每个 mirror 的 $ur=\kappa_{\rm cap}p^2$ 上恒零，
与 $x$、宽度、幅度和 suffix 无关。
乘 $n_0,n_1,n_2$ 后，D 值包含全部 $\operatorname{Pol}_{\le3}$。

令 $\operatorname{Eval}_{\rm full}$ 包含该原同 cap 母库的所有实际宽度、角色和根，
且至少包含第6节的一条 witness 族。则已严格证明
$
\boxed{
\operatorname{Pol}_{\le3}
\subset
D(\ker\operatorname{Eval}_{\rm full})
\subset
\operatorname{Pol}_{\le4}.
}
\tag{41}
$
故整个多宽库的 formal 有序评价商维数为二或三；
潜在多出的一项只能是 $D_4$ 的共同评价类。
这里没有预先决定该类非零，也没有忽略真实 suffix 的宽度协变。
若整个所问库只有一个实际宽度，(28)已给左端提升到 $\operatorname{Pol}_{\le4}$。

对任意多宽库，(40)已有一个立即可用的充分条件：
若具体成本的 $D_4=D_5=D_6=0$，同一个形式 blind 提升和(11)
给一个 signed 响应，清掉该库全部角色的 ordered $\mathcal C$。
若只有 $D_5=D_6=0$，是否可清所有宽度的 $D_4$ 余值，
须用同一个真实联合评价映射继续判断。

## 9. 已闭与仍欠的真正问题

本稿完成的是实际有限镜点评价，不再只有39列或七项形式目录：

- 原同角色的真实 suffix 确有 $n_0\ne0$，并有十二个原不同位置；八个足以忠实恢复两个 degree7 多项式。
- 固定同宽的全部角色同时只保两个响应不变量 $D_5,D_6$，有显式真实值读出和 signed 补偿构造。
- 多宽库仍保实际共同映射；已确定其额外形式余量至多一个 $D_4$，不是任意多条新的未知函数。

一般 canonical 成本的 $D$ 值由原路径决定。R453 的完整几何 action 与 R454 的响应 trace 身份必须在各自定义域内使用；
本稿没有从 whole $E$、有限自然或 ordered 零值推出 $D_5,D_6=0$。
若原路径给其中非零值，(21)—(22)、(35)就是这一个真实副本族上的明确障碍，
并且所有保持 whole $E$ 的响应及所有允许 gauge 都不能消掉它。

即使所需 $D$ 系数已经准确归零，完整 self cap、原所有 $p$ 简单零点的 inverse germ、
平台仿射连接、$k$ 值闭合、两条真正 period 及同一十三行规范仍分别存在。
本稿没有修改冻结母、另造逐点成本，或重做旧四矩/二十根研究。
