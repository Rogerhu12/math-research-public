# 原四个单位盘的完整词域与 A34 移动门阈值

日期：2026-11-15。**状态：已证明。**

本注只使用已经支付的原物理轴、完整核心和原整数格。
它给出两个可直接用于实际外部比较的事实：

1. Y/Z/W/V 四轴的来源矩阵虽然只有有限轨道，但在原四-unit平面上，
   不同约化物理词的像两两不交；
2. 把 A34 轴经越来越深的 Y 正交伙伴缩放，确实会得到趋向伙伴轴的行，
   但同一真实像格的精度也准确增加。这个精度不能冻结。

所有原权、单位观察、径向倍率和无限词的剩余集合均保留。
本注不从这些域事实增加一个中央零，也不假定边界上的原测度为零。

## 1. 原两个平面框架

固定已有普通素数、原局部嵌入 $K_{\mathfrak p}=\mathbf Q_p$，并记
$$
\lambda=-\bar\pi_0^{-1},\qquad
\kappa=\pi_0/\bar\pi_0=p\lambda^2,\qquad v_p(\kappa)=1.
\tag{1}
$$
保持原六输入中的
$$
Y=A+c+2d,\qquad W=A+3\delta c+4d,\qquad
\delta=1+2\omega,\quad\omega^2+\omega+1=0.
$$
设
$$
\alpha=17-3\omega,\quad
b_Y=\frac{20+3\omega}{17},\quad d_Y=\frac{263}{17},\quad
Z=W-b_YY,\quad V=36Y-\alpha W .
$$
于是完整换元为
$$
\binom WV=M\binom YZ,\qquad
M=\begin{pmatrix}b_Y&1\\d_Y&-\alpha\end{pmatrix},\qquad
M^{-1}=\frac1{36}
 \begin{pmatrix}\alpha&1\\d_Y&-b_Y\end{pmatrix}.
\tag{2}
$$
这里
$$
\alpha b_Y=\frac{349}{17},\qquad
\alpha b_Y+d_Y=36,\qquad \det M=-36.
$$
固定坏素数 $2,3,17,263,349$ 已被原射线或原有限坏集排除。
特别 $\alpha,b_Y,d_Y$ 都是单位；只检查 $\det M$ 不够。
所以 $M\in\operatorname{GL}_2(\mathbf Z_p)$。

原 E 输出及三个 A 伙伴逐个正交于这整个平面。
以下平面矩阵在完整六维上均固定这四个伙伴。

## 2. 四个实际物理字母及反向字母的比例

使用 R692 的原完整物理映射，令
$$
A_Y=R_YP_{Y,\kappa},\quad A_Z=R_YP_{Z,\kappa},
\quad A_W=P_{W,\kappa},\quad A_V=P_{V,\kappa}.
\tag{3}
$$
在 $(Y,Z)^t$ 上准确为
$$
A_Y=\begin{pmatrix}-\kappa&0\\0&1\end{pmatrix},\qquad
A_Z=\begin{pmatrix}-1&0\\0&\kappa\end{pmatrix},
\tag{4}
$$
$$
A_W=\frac1{36}
 \begin{pmatrix}
 \alpha b_Y\kappa+d_Y&\alpha(\kappa-1)\\
 d_Yb_Y(\kappa-1)&d_Y\kappa+\alpha b_Y
 \end{pmatrix},
$$
$$
A_V=M^{-1}\begin{pmatrix}1&0\\0&\kappa\end{pmatrix}M .
\tag{5}
$$
设 $a=[A_Y]$、$b=[A_W]$ 为射影变换，则
$$
[A_Z]=a^{-1},\qquad[A_V]=b^{-1}.
\tag{6}
$$
完整比例是
$$
A_Z=\kappa A_Y^{-1},\qquad A_V=\kappa A_W^{-1}
\quad\text{仅在这个二维平面上}.
\tag{7}
$$
在六维上，(7) 的 $\kappa I$ 应写成
$$
C_\kappa=P_{Y,\kappa}P_{Z,\kappa};
\qquad A_YA_Z=A_WA_V=C_\kappa .
\tag{8}
$$
$C_\kappa$ 固定 E 和另外三个伙伴。因此 (8) 不是六个输入共同缩放，
不能在原 E 门、斜门或 Mellin 观察中删去。

对任一有限正字，把 Y/Z/W/V 分别替换为
$a,a^{-1},b,b^{-1}$ 后作自由约化。
每删掉一对相邻反向字母，完整六维物理矩阵留下一个 $C_\kappa$。
它与四个字母交换。因此完整物理字仍为
$C_\kappa^h$ 乘其约化字的指定代表，而不仅是那个射影字。
所有真实测试都按完整矩阵运输。

## 3. 原四个残数盘及准确映射

在 $X=\mathbf P^1(\mathbf Q_p)$ 上定义
$$
\begin{aligned}
D_Y&=\{[Y:Z]:|Y|_p<|Z|_p\},&
D_Z&=\{[Y:Z]:|Z|_p<|Y|_p\},\\
D_W&=\{[Y:Z]:|W|_p<|V|_p\},&
D_V&=\{[Y:Z]:|V|_p<|W|_p\}.
\end{aligned}
\tag{9}
$$
取任一 primitive 代表，即
$\max(|Y|_p,|Z|_p)=1$。由 (2)，$(W,V)$ 也 primitive。

四盘两两不交。具体地：

- 在 $D_Y$，$Z$ 为单位且 $Y\in p$，所以
  $W\equiv Z$、$V\equiv-\alpha Z\pmod p$ 都是单位。
- 在 $D_Z$，$Y$ 为单位，所以
  $W\equiv b_YY$、$V\equiv d_YY\pmod p$ 都是单位。
- 在 $D_W$，$V$ 为单位；由 (2) 的逆式，
  $Y\equiv V/36$、$Z\equiv-b_YV/36\pmod p$ 都是单位。
- 在 $D_V$，$W$ 为单位；同理
  $Y\equiv\alpha W/36$、$Z\equiv d_YW/36\pmod p$ 都是单位。

故其补集
$$
F=X\setminus(D_Y\sqcup D_Z\sqcup D_W\sqcup D_V)
\tag{10}
$$
在 primitive 格中的逆像正是原
$$
\mathcal G_4=\{Y,Z,W,V\in\mathbf Z_p^\times\}.
$$
四盘分别是四个不同的 $\mathbf P^1(\mathbf F_p)$ 残数类，
所以 $F$ 是其余 $p-3$ 个残数盘之并，特别非空。

以下不仅是包含，而是准确等式：
$$
\boxed{
\begin{array}{ll}
a(X\setminus D_Z)=D_Y,&a^{-1}(X\setminus D_Y)=D_Z,\\
b(X\setminus D_V)=D_W,&b^{-1}(X\setminus D_W)=D_V .
\end{array}}
\tag{11}
$$
证明第一式：在 $X\setminus D_Z$ 可取 $Z=1$、$Y\in\mathbf Z_p$，
(4) 将斜率 $Y/Z$ 乘 $-\kappa$。由于
$\kappa\mathbf Z_p=p\mathbf Z_p$，其像恰为 $D_Y$。
第二式在 $Y=1$ 的坐标同样成立；最后两式由 (2) 共轭得到。
这也明确支付了逆字母的原 $p$ 比例。

## 4. 不同约化词的四-unit像严格不交

取字母集
$$
\mathcal A=\{a,a^{-1},b,b^{-1}\},
\quad D(a)=D_Y,\ D(a^{-1})=D_Z,\ D(b)=D_W,\ D(b^{-1})=D_V .
$$
若 $w=s_1\cdots s_m$ 非空且约化，(11) 逐字给
$$
wF\subset D(s_1).
\tag{12}
$$
理由是 $F$ 不在任何排斥盘中；相邻两个字母不互逆，
所以后一字母的吸引盘不在前一字母的排斥盘中。

若 $v,w$ 是两个不同的约化词而 $vF\cap wF\ne\varnothing$，
则 $F\cap(v^{-1}w)F\ne\varnothing$。约化后的 $v^{-1}w$ 非空，
与 (10)、(12) 矛盾。因此
$$
\boxed{vF\cap wF=\varnothing\qquad(v\ne w).}
\tag{13}
$$
同一论证表明没有非空约化词代表射影恒等：
四个实际矩阵在射影平面中生成一个自由二生成群。

(13) 应用于原六维来源时，可附任意 E/旧伙伴条件。
不同约化射影字的完整 $\mathcal G_4$ 像仍不可能相交，
因为其射影平面像已不相交。
但本结论**没有**说两个完整词像格 $M_v\mathbf Z_p^6$、
$M_w\mathbf Z_p^6$ 不相交；这些像格通常有深层交集。
同一个约化字而不同 $C_\kappa^h$ 的情形也必须另保实际径向深度。

R692 的三态矩阵满足
$R^2=K^2=(KR)^4=I$。这与 (13) 不冲突：
该关系只在来源表示中成立，不是物理像格或真实测试的关系。
特别不能据此把两条不同字的四-unit部分认成同一个域后相减。

## 5. 全部有限分区和无限字剩余集合

对于长度 m 的约化字
$w=s_1\cdots s_m$，定义实际残数圆盘
$$
C_w=s_1\cdots s_{m-1}D(s_m).
\tag{14}
$$
由 (11)，对每个 $m\ge1$ 有完整的有限不交分区
$$
\boxed{
X=\coprod_{|w|<m}wF\ \sqcup\
  \coprod_{\substack{|w|=m\\w\ {\rm reduced}}}C_w .
}
\tag{15}
$$
空字对应 F。确实
$$
D(s)=sF\ \sqcup\
\coprod_{t\ne s^{-1}}sD(t),
$$
逐层迭代即得 (15)。

定义
$$
\Sigma_\infty=
\bigcap_{m\ge1}\ \coprod_{|w|=m}C_w
=X\setminus\coprod_{w\ {\rm reduced}}wF .
\tag{16}
$$
它恰由所有无限约化字 $s_1s_2\cdots$ 的唯一极限点组成。
为付唯一性，取标准 chordal 距离。$M\in\mathrm{GL}_2(\mathbf Z_p)$
是该距离的等距变换；在 (11) 的每个定义域上，
对应字母将距离准确乘 $|\kappa|_p=p^{-1}$。
故一个长度 m 圆盘 $C_w$ 的直径至多 $p^{-m}$。
沿无限约化字所得圆盘嵌套且非空，紧性与此直径界给唯一交点。
不同无限字在首个分叉处进入两个不交圆盘。

$\Sigma_\infty$ 不为空；例如 a 的两个固定点以及 b 的两个固定点
都在其中。它是本注的无限词剩余集合，不是可以凭核心标量删掉的域。
(15) 可在原实际来源上逐层积分，每层只使用有限相加。
这里既未证明 $\Sigma_\infty$ 的原测度为零，也未把有界 p-adic 测度
当作实 Haar 测度，或未经收敛证明作可数相加。

从射影平面回到整格时，还须保
$\min(v_p(Y),v_p(Z))$ 的共同深度。
在任何全来源等式中，$Y=Z=0$ 的原子纤维也须另保；
它不属于射影坐标。本注的四-unit应用本来不含这个纤维。

## 6. A34 的原伙伴坐标与已付共同缩放

现在加入 R698 的原
$$
Q=c+2d,\qquad L=2c-d,\qquad J=5A-29Q.
$$
准确有
$$
A=\frac{29Y+J}{34},\qquad Q=\frac{5Y-J}{34},
\quad \operatorname{Gram}(Y,J,L)=\operatorname{diag}(34,4930,5).
\tag{17}
$$
本节的 L、J 都是实际物理行，不是中央函数。

原 E/Z 与 J/L 的关系为
$$
Z=-\frac{3(1+\omega)}{85}J+\frac{2+12\omega}{5}L,
\qquad
E=\frac{5+6\omega}{5}J+\frac{87\omega}{5}L.
\tag{18}
$$
其行列式是 $263/85$，是当前 p 处单位。
所以已付的共同正交映射
$$
\mathcal H_s=P_{Z,s}P_{E,s},\qquad s=\kappa^n,
$$
在 $(Y,J,L)$ 上恰为 $\operatorname{diag}(1,s,s)$，
另外三个 A 伙伴逐个固定。这里不需要假定一个新的单 J 核。

设 $t=\kappa^{34}$。原 A 缩放在这些坐标上为
$$
P_{A,t}:
\begin{cases}
Y\longmapsto Y+(t-1)A,\\
J\longmapsto J+5(t-1)A,\\
L\longmapsto L.
\end{cases}
\tag{19}
$$
这是原 A 的正交投影，使用
$\langle Y,A\rangle/N(A)=1$、
$\langle J,A\rangle/N(A)=5$。
它没有把 A 换成一个同范数轴。

R737 的共同 E/Z 核支付 $\mathcal H_{\kappa^n}$，
其中奇 n 时有原 $R_Y^n$，必须保留。
为直接同 R698 的同一来源 A34 核组合，可取正偶 n
（特别仍可取原 $n\in4\mathbf Z$）。
在 R698 的未作角平均来源 $\Psi_\chi$ 上，
E 核与第一 Y 的完整 CM 作用交换，故
$$
\Psi_\chi|_{\mathcal H_s\mathbf Z_p^6}
=\lambda^{2n}(\mathcal H_s)_*\Psi_\chi
\qquad(n\ {\rm even}).
$$
随后使用该篇的 A34 核，得到真正的组合词
$$
\boxed{
\Psi_\chi|_{\mathcal M_n\mathbf Z_p^6}
=\epsilon_\chi\lambda^{2n+34}
  (\mathcal M_n)_*\Psi_\chi,\qquad
\mathcal M_n=\mathcal H_{\kappa^n}P_{A,\kappa^{34}} .
}
\tag{20}
$$
$\epsilon_\chi$ 仍为 R698 原符号。所有外部标量为单位。
(20) 的 n 偶条件是为了保同一来源；以下纯格公式则对任意 n 成立。

## 7. 趋近伙伴轴的真实精度恰为 n+34

由 (17)–(19) 的整像和整像逆，准确有
$$
\boxed{
\mathcal M_n\mathbf Z_p^6
=\{J,L\in p^n\mathbf Z_p,\quad
       J+29\kappa^nY\in p^{n+34}\mathbf Z_p\},
}
\tag{21}
$$
另外三个伙伴自由。证明如下。

先取 $\mathcal H_s^{-1}$，要求 $J,L\in p^n$。
在所得坐标里，$P_{A,t}^{-1}$ 整的充要条件是
$$
A_s:=\frac{29Y+s^{-1}J}{34}\in p^{34}\mathbf Z_p.
$$
乘以 $34s$，正是 (21) 的第三个条件。
所有变基的固定行列式在当前 p 处为单位，所以这是充要条件，
不是仅一侧包含。

若再附原 $Y\in\mathbf Z_p^\times$，则 (21) 还迫
$$
\boxed{v_p(J)=n,\qquad
      J/\kappa^n\equiv-29Y\pmod{p^{34}}.}
\tag{22}
$$
因此虽有行
$J+29\kappa^nY\to J$，其真实门深度同时是 $n+34$。
把这个门偷换成固定深度34、或仅 $J\in p^n$，
都会删除 (22) 中相对 Y 的完整近相消条件。
这说明为何“轴趋向纯伙伴”本身不把 (20) 变成一个纯伙伴条件中央零。

## 8. 同一原权及观察的完整转置

(21) 上的完整逆返回为
$$
\boxed{
Y_{\rm ret}=Y+(t^{-1}-1)A_s,\quad
J_{\rm ret}=s^{-1}J+5(t^{-1}-1)A_s,\quad
L_{\rm ret}=s^{-1}L .
}
\tag{23}
$$
它一般不保原 Y-unit。原算术测试要求的是
$1_{Y_{\rm ret}\ {\rm unit}}\langle Y_{\rm ret}\rangle^{d_pw}$，
不能替换成 $1_{Y\ {\rm unit}}\langle Y\rangle^{d_pw}$。

令 $e_A=5+6\omega$。由 (18)，
$$
\boxed{
E_{\rm ret}=s^{-1}E+e_A(t^{-1}-1)A_s,\qquad
Z_{\rm ret}
=-\frac{3(1+\omega)}{85}J_{\rm ret}
 +\frac{2+12\omega}{5}L_{\rm ret}.
}
\tag{24}
$$
于是
$$
W_{\rm ret}=b_YY_{\rm ret}+Z_{\rm ret},\qquad
V_{\rm ret}=d_YY_{\rm ret}-\alpha Z_{\rm ret}
$$
也全有显示公式。
原 $\Delta_\ell$ 要用
$b_iZ_{\rm ret}+e_iE_{\rm ret}$，所有单位门随各自观察运输。

对 R737 的同一完整 cd 权
$$
\Phi_N=\sum_{a=0}^{30}E^a\phi_{a,N}
$$
而言，三个 $\phi_{a,N}$ 所依的共同伙伴逐点固定，所以
$$
\boxed{\Phi_N\circ\mathcal M_n^{-1}
=\sum_{a=0}^{30}E_{\rm ret}^{\,a}\phi_{a,N}.}
\tag{25}
$$
两个 C 支、混次归一和全部系数均在 (25) 中。
$s^{-1}$、$t^{-1}$ 的负赋值不能从式中省去；
整性由实际像格 (21) 支付。

为避免转置方向混淆，若从像格上的**native**权开始积分，
(20) 使用的是正向拉回：
$$
\int_{\mathcal M_n\mathbf Z_p^6}f\,\Phi_N\,d\Psi_\chi
=\epsilon_\chi\lambda^{2n+34}
 \int(f\circ\mathcal M_n)(\Phi_N\circ\mathcal M_n)\,d\Psi_\chi ,
\tag{26}
$$
而正向 E 是
$$
E\circ\mathcal M_n=s\{E+e_A(t-1)A\}.
$$
若希望返回后恰为原 $\Phi_N$，则像格上必须放 (25)。
这两种测试不能相认。
同样，原 $H=D_*-E/29$ 的 $D_*$ 固定时，
逆门准确为 $D_*-E_{\rm ret}/29$。

## 9. 对原中央问题的准确范围

(13) 排除的是：仅凭有限来源关系，在两个不同约化词的
$\mathcal G_4$ 像上直接认同域、同权后相消。
它不排除完整词像格的真实深交域，也不排除再加入 A34 后的新关系。

(21)–(26) 给后者的一个完全可用实例：
原 same-source 返回存在，但保 Y 的伙伴极限同时带增长精度、
新的 Y-unit 观察和完整三十次 E 权。
是否能用这些准确域与原 $J'_S,J'_T,J'_{\rm new}$ 得到附加约束，
仍需对实际积分另作证明。

本注不对 $\Sigma_\infty$、任一外部、任一参考来源或完整
$\log(1+\kappa\,\text{线性行}/\text{单位行})$ 赋零。
也未用点因子投影穿过未支付的无限和。

### 原来源引用

- [R692](../results/R692-original-four-axis-three-state-and-arithmetic-unit-cuts.md)，
  第1–4节：完整四轴三态、物理反射、原词像格与全部伙伴。
- [R698](../results/R698-adjusted-cm-and-thirty-four-layer-arithmetic-words.md)，
  第2–6节：原 J/L 框架、未改17²射线、A34完整核心与未平均 CM 来源。
- [R737](../results/R737-common-depth-elimination-and-native-primitive-strips.md)，
  第1–3节：同一 $\Phi_N$、全部三十次 E 权、共同 E/Z 深度和原反射。
- [R747](../results/R747-original-source-restoration-and-p-primary-gate-model.md)：
  两返回条带的完整单位观察和原来源恢复。

全部新增结论为显示矩阵与原完整来源身份的精确推导；
本注没有新增数值运行或可重算输出。
