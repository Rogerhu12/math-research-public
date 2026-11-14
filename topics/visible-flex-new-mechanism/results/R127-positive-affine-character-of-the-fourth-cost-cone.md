# R127：若真实第四成本闭锥仍为真子锥，则有单一整权的平移不变正泛函

日期：2026-11-14。**已证明。** 本稿是有限维实表示与闭凸锥的纸面论证，不运行新的研究计算。

使用 [R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md) 的有限真实算子空间和完整仿射表示，以及 [R120](R120-G-lineality-of-the-closed-fourth-cost-cone.md) 的真实成本闭锥仿射不变性。结论缩小剩余正性障碍的范围；不证明闭锥已经等于全空间，也不把闭锥变成实际成本半群。

## 1. 空间、闭锥与真实仿射作用

固定同一 canonical 目标、同右锚和零传入历史。对任一固定 scalar 常值 germ、frame $I\to I$，令

$$
\mathcal S
=\{V_B:B\text{ 为实际有限同端口路径， }M_B=T_B=0\},
$$

$$
U=\mathcal U_4=\operatorname{span}_{\mathbb R}\mathcal S,
\qquad
C=\overline{\operatorname{cone}(\mathcal S)}\subseteq U.
\tag{1}
$$

闭包在有限维真实函数空间 U 的普通向量空间拓扑中取。成本是 universal 原式延拓；与 R120 相同，此处不预先规定统一总长、scalar 盒或必须容纳全部仿射变换的某个窄物理区间。

R105、R120 证明 U 有限维，C 不依赖 scalar germ，并且

$$
\mathsf P_{H,d}U=U,\qquad
\mathsf P_{H,d}C=C
\quad(H>0,\ d\in\mathbb R).
\tag{2}
$$

真实缩放与平移分别记作

$$
D_H=\mathsf P_{H,0},\qquad
T_d=\mathsf P_{1,d}=\exp(dN).
$$

存在有限个整数权使

$$
U=\bigoplus_{w\in\mathbb Z}U_w,\qquad
D_H|_{U_w}=H^w\operatorname{id},
\qquad
N(U_w)\subseteq U_{w-1}.
\tag{3}
$$

N 幂零。这里只用 R105 对完整真实算子已证明的有限 Laurent/坐标多项式表示，不假设实际几何路径的时间参数解析。

定义对偶闭锥

$$
C^*=\{\lambda\in U^*:\lambda(V)\ge0\quad\forall V\in C\}.
\tag{4}
$$

由 (1)，

$$
\operatorname{span}C=U.
$$

所以 $C^*$ 是 pointed 的，即

$$
C^*\cap(-C^*)=\{0\}.
\tag{5}
$$

证明很直接：若 $\lambda,-\lambda$ 同在 $C^*$，则 $\lambda$ 在 C 上恒零，因而在其线性 span U 上恒零。此处不能省掉 $\operatorname{span}C=U$；一个位于较小线性子空间中的锥，其对偶一般含非零直线。

## 2. 定理

若 $C\ne U$，则存在非零 $\nu\in U^*$ 和某个整数 $a$，使

$$
\boxed{
\nu(C)\ge0,\qquad
N^*\nu=0,\qquad
\nu\circ D_H=H^a\nu.
}
\tag{6}
$$

这里 $N^*\nu=\nu\circ N$。因此

$$
\boxed{\nu\circ\mathsf P_{H,d}=H^a\nu}
\quad(H>0,\ d\in\mathbb R).
\tag{7}
$$

也就是说，若仍有任何非平凡的完整正性障碍，就有一个**平移不变、单一整数缩放权的正泛函**。它可能与最初取得的分离泛函具有不同的权。

反之，如果不存在满足 (6) 的非零正泛函，则 $C=U$。这个逆向表述仍只关于闭凸锥，不关于实际成本集合 $\mathcal S$。

## 3. 第一步：从任意正泛函提取一个非零整权部分

若 $C\ne U$，有限维闭凸锥分离给出一个非零

$$
\lambda\in C^*.
$$

按 (3) 分解

$$
\lambda=\sum_w\lambda_w,
\qquad
\lambda_w|_{U_v}=0\quad(v\ne w).
$$

于是

$$
\lambda\circ D_H=\sum_wH^w\lambda_w.
\tag{8}
$$

令 m 是其中 $\lambda_m\ne0$ 的最大权。由 (2)，每个 $\lambda\circ D_H$ 仍在 $C^*$；乘正数 $H^{-m}$ 不离开这个锥。有限维极限给

$$
H^{-m}\lambda\circ D_H
\longrightarrow\lambda_m\in C^*
\quad(H\to+\infty).
\tag{9}
$$

$\lambda_m$ 非零且为单一整权。所有低权项在真实对偶空间中趋零，不需要对一个不完备的形式系数商取极限。

## 4. 第二步：两向平移迫最后一个非零导数为偶阶

从现在起把 $\lambda_m$ 记为 $\lambda_0$。由于 N 幂零，存在最大非负整数 j 使

$$
\nu_0=(N^*)^j\lambda_0\ne0,
\qquad
(N^*)^{j+1}\lambda_0=0.
\tag{10}
$$

由 (2)，对每个实数 d，

$$
\lambda_0\circ T_d
=\exp(dN^*)\lambda_0
=\sum_{i=0}^j\frac{d^i}{i!}(N^*)^i\lambda_0
\in C^*.
\tag{11}
$$

以正数 $|d|^{-j}$ 归一，并分别让 $d\to+\infty$、$d\to-\infty$，得到

$$
\frac{\nu_0}{j!}\in C^*,\qquad
\frac{(-1)^j\nu_0}{j!}\in C^*.
\tag{12}
$$

如果 j 是奇数，(12) 与 pointed 性 (5) 迫 $\nu_0=0$，矛盾。因此 j 必为偶数。令 $\nu=\nu_0$，便有

$$
\nu\ne0,\qquad \nu\in C^*,\qquad N^*\nu=0.
\tag{13}
$$

这里没有假设存在连续的“最高项方向选择”，也没有对实际路径使用负时间。负 d 是 R120 已支付的真实反向平移参数；归一系数始终为正。

## 5. 最后的权会改变，但仍是单一整数权

由 (3)，$N^*$ 将对偶权 m 送到权 $m+1$：

若 $V\in U_v$，则 $NV\in U_{v-1}$；所以 $\lambda_m(NV)$ 仅在 $v-1=m$ 时可能非零。

于是 (10) 的最后非零项满足

$$
\nu|_{U_v}=0\quad(v\ne m+j),
\qquad
\nu\circ D_H=H^{m+j}\nu.
\tag{14}
$$

取 $a=m+j$，就得到 (6)。**最终权是 $m+j$，不能写成仍等于最初 m。** j 为偶数只限制两者差为非负偶数，不给出其具体值。

由 $N^*\nu=0$，

$$
\nu\circ T_d=\nu
$$

对所有 d 成立。正仿射群由正缩放与平移生成，结合 (14) 即得 (7)。无论采用哪一等价的缩放—平移乘法顺序，平移部分都被 $\nu$ 消去，剩余因子恰为 $H^a$。

## 6. 已知可付方向必须全部被这个泛函杀掉

R120 给

$$
A=
\mathcal R_8+
\operatorname{span}\{\mathsf P_{H,d}G:H>0,\ d\in\mathbb R\}
\subseteq C\cap(-C).
\tag{15}
$$

每个非负泛函都在 lineality 上恒零，所以定理所得 $\nu$ 满足

$$
\boxed{
\nu(\mathcal R_8)=0,\qquad
\nu(\mathsf P_{H,d}G)=0
\quad\forall H>0,\ d\in\mathbb R.
}
\tag{16}
$$

结合 [R126](R126-first-G-translation-separation-and-52-query-control.md)，(15) 至少包含 52 个独立真实方向；不过其完整维数仍未知。

因此后续寻找 universal 正性障碍，可先限定于有限个空间

$$
\left\{
\nu\in U_a^*:
N^*\nu=0,\ 
\nu(A)=0
\right\}.
\tag{17}
$$

然后才检验它是否对全部实际成本非负。R119 的静态乘子不等式给这些候选的必要门，但只在常态表上非负不足以通过完整路径、导数权二/四、连接桥及全部历史成本。

式 (17) 只减少候选空间，没有计算其维数，也没有找到一个实际非零正泛函。特别，任何模素数证书的非零值只证非零，不能用作这里的实数正性判断。

## 7. 范围

本稿严格区分三件事：

1. U 是实际成本的真实线性 span，允许在证明 span 时取差；
2. C 是非负实组合再取闭包，已经比实际有限路径成本集合更宽；
3. $\mathcal S$ 的拼接只提供实际加法，未提供任意成本逆元。

即使将来证明 $C=U$，还须单独支付实际有限路径层的局部可达性、基准成本与精确有限组合，不能仅靠凸锥分离把它们省去。

本稿没有对任意预给的窄物理区间、统一控制盒、总长或 reach 上限断言仿射不变性。若在这些受限类中 (2) 不成立，本定理不能直接搬用。

它也未证明完整第四 ruling、所有高阶校正或有限连续等距族。下一任务仍是确定剩余完整商的实际成本及其可支付性。
