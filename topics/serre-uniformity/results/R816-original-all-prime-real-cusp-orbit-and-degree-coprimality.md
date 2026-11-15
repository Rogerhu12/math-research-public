# R816：原一般素数曲线的实 cyclotomic 尖点域与互素单轨道

日期：2026-11-15。状态：**下述原尖点剩余域、一般 p 单轨道及三次覆盖的总分歧已证明。** 本篇不将 p=41 的 Hom 域/秩一计算或某个实际微分首系数外推到一般 p；原同标签 Cartier/Legendre 非零与高度排除仍开放。

## 1. 允许素数、原曲线和系数字段

先令
$$
 p\ge41,\qquad p\equiv5\pmod6,\qquad
 K=\mathbf Q(\zeta),\quad s=1+2\zeta,\quad s^2=-3.
 \tag{816.1}
$$
群与尖点计算适用于全部 (816.1)。
联用原 R725 的正 CM 分裂域时，仍采用该篇主任务允许条件
$p\equiv2,5\pmod9$；不扩大其别的算术结论。

R575(575.4) 已对一般 p 固定原曲线
$$
 X_p=\operatorname{Norm}
 \left(X_{\rm ns}^+(p)\times_j\mathbf P^1_a\right),
 \qquad j=6912a^3(1-a^3).
 \tag{816.2}
$$
保持原 $a$，置
$$
 t=a^3,\qquad
 Y_p=\operatorname{Norm}
 \left(X_{\rm ns}^+(p)\times_j\mathbf P^1_t\right),
 \qquad j=6912t(1-t).
 \tag{816.3}
$$
于是 $X_p\to Y_p$ 是原 $\mu_3$ 商；在 K 上选定的原生成元为
$a\mapsto\zeta a$。
本篇以下会由尖点估值再次核其函数域次数确为三。

令 L 为 R725(725.11) 的原域：
$$
 H_0=K(E_{27}[p])^{\mathbf F_p^\times},\qquad
 L=H_0^{G_6},\qquad
 [L:K]=m=\frac{p+1}{6},
 \tag{816.4}
$$
其中 $G_6$ 为原唯一六阶子群。
本篇关于 L 的证明仅使用其包含 K 及显示的准确次数；
所以同一尖点结论也适用于任意 $L'/K$ 满足
$[L':K]\mid m$ 的域。

## 2. 原扭曲与标准 level-2p 算术模型的准确识别

保留原 period basis 中的非分裂环面
$$
 T(a,b)=
 \begin{pmatrix}a&-b\\ b&a+b\end{pmatrix},
 \qquad
 \mathcal Q(x,y)=x^2+xy+y^2 .
$$
为免与 (816.2) 的全局函数 a 混淆，本节环面参数 a,b
仅表示 $\mathbf F_p$ 元素。
令
$$
 J=\begin{pmatrix}-1&-1\\0&1\end{pmatrix},
 \qquad N_p=\mathsf T_\zeta\sqcup J\mathsf T_\zeta,
$$
$$
 G_{2p}=C_3\times N_p
 \subset\operatorname{GL}_2(\mathbf Z/2p\mathbf Z),
 \qquad H_{2p}=G_{2p}\cap\operatorname{SL}_2 .
 \tag{816.5}
$$
这里模二的 $C_3$ 是原 $A_3\subset\operatorname{GL}_2(\mathbf F_2)$；
行列式满射到 $\mathbf F_p^\times$。

标准模二 $C_3$ 覆盖由同一个模函数
$$
 u=E_6/\eta_{\rm Ded}^{12},\qquad u^2=j-1728
$$
给出。其与原 (816.3) 的字段识别为
$$
 \boxed{u=24s(2t-1).}
 \tag{816.6}
$$
因为
$$
 (24s)^2(2t-1)^2=6912t(1-t)-1728,
$$
此式保留原 $t=0,1$ 分支。
CRT 的标准模解释将 level-2 $C_3$ 覆盖与原 level-p 正规化子
曲线的正规化纤维积识别为 $G_{2p}$ 模曲线。
因此 (816.6) 给
$$
 (Y_p)_K\simeq (X_{G_{2p}})_K .
 \tag{816.7}
$$
这正是 R772(772.3) 的原字段识别；公式与 p 无关，
而一般 p 的原纤维积来自 R575，不是由 p=41 的亏格或 cusp 数猜出。
它是在 K 上的识别，因而也在原 L 上成立。

## 3. 几何尖点标签与宽度

$-3$ 在 $\mathbf F_p$ 中非平方，故 $\mathcal Q$ 各非零值的
纤维均由 norm-one 环面单传递。准确有
$$
 \mathcal Q(T(a,b)v)=\det(T(a,b))\mathcal Q(v),\quad
 \det T(a,b)=a^2+ab+b^2,
$$
$$
 \mathcal Q(Jv)=\mathcal Q(v),\qquad \det J=-1.
 \tag{816.8}
$$
所以 $N_p\cap\operatorname{SL}_2$ 由 norm-one 部分与
J 乘 norm-minus-one 部分组成；后者将范数 n 送到 $-n$。

全 level-2p 的 primitive 列向量具有非零模二与模 p 分量。
模二 $C_3$ 在三个非零列上传递；又 $-I\in H_{2p}$，
所以原几何尖点恰标为
$$
 \boxed{\{n,-n\}\in\mathbf F_p^\times/\{\pm1\}.}
 \tag{816.9}
$$
特别地共有
$$
 c=\frac{p-1}{2}
 \tag{816.10}
$$
个尖点。此处始终使用列向量；没有把对偶行向量的负号二次型混入。

每个尖点的宽度准确为 $2p$。
确实，任意共轭的平移 $T^\ell$ 在模 p 非平凡时是阶 p 的
unipotent，而 $p\nmid|N_p|=2(p^2-1)$，所以必须 $p\mid\ell$。
模二非平凡的同一平移为阶二元，不属于 $C_3$，所以还须
$2\mid\ell$。反之 $\ell=2p$ 已模 $2p$ 为恒等。
因此在 Y 的任一尖点
$$
 \operatorname{ord}(j)=-2p,\qquad
 \operatorname{ord}(t)=-p .
 \tag{816.11}
$$
第二式直接使用 (816.3) 在无穷处的二次主项。

## 4. 真正算术作用及准确剩余域

标准算术尖点公式（Zywina, §5.2, Lemma 5.2）给
$$
 C_G=G_{2p}\backslash\operatorname{GL}_2(\mathbf Z/2p\mathbf Z)/U_{2p},
$$
$$
 \sigma_d(G_{2p}AU_{2p})
 =G_{2p}A\begin{pmatrix}1&0\\0&d\end{pmatrix}U_{2p},
 \qquad \sigma_d(\xi_{2p})=\xi_{2p}^d .
 \tag{816.12}
$$
尖点都在 $\mathbf Q(\xi_{2p})=\mathbf Q(\xi_p)$ 中定义。

取 $A\in\operatorname{SL}_2$ 代表尖点，第一列为 v。
在原环面中选 determinant d 的 $g_d$，并令其模二分量为恒等。
范数满射保证这样的原 $g_d$ 存在。用
$$
 A'=g_d^{-1}A\operatorname{diag}(1,d)
$$
恢复 determinant one；其第一列为 $g_d^{-1}v$。
由 (816.8)，算术作用准确为
$$
 \boxed{\{n,-n\}\longmapsto\{d^{-1}n,-d^{-1}n\}.}
 \tag{816.13}
$$
这个逆元来自左乘 $g_d^{-1}$，不是任意几何 deck 作用。

故每个尖点在完整 cyclotomic Galois 群中的 stabilizer 恰为
$\{\pm1\}$，所有尖点单传递。标准 $\mathbf Q$ 模型中
每个尖点的准确剩余域为
$$
 \boxed{C_p^+=\mathbf Q(\xi_p)^+.}
 \tag{816.14}
$$
因为 K 是虚二次域、$C_p^+$ 为全实域，二者交为
$\mathbf Q$。经 (816.7)，原 $Y_K$ 的全部尖点形成一个
次数 c 的闭点，其剩余域为 $KC_p^+$。

这是一般 p 的原算术模型计算，不是仅从 p=41 有二十尖点推测
实 cyclotomic 域。R778 的 p=41 标签/相位正是它的原特例。

## 5. 与原 L 的互素次数，不需要完整 cyclotomic 不交

由 (816.4)、(816.10)，
$$
 \boxed{c=3m-1,\qquad \gcd(m,c)=1.}
 \tag{816.15}
$$
因此 L 与 $KC_p^+$ 在 K 上线性不交：
两个域的交次数同时整除 m 与 c，
且 $KC_p^+/K$ 是 Galois。
于是
$$
 \boxed{[LC_p^+:L]=c,\qquad
        \operatorname{Gal}(LC_p^+/L)
          \simeq\operatorname{Gal}(KC_p^+/K).}
 \tag{816.16}
$$
(816.13) 的整个尖点置换群因此在原 L 上仍存在，得到
$$
 \boxed{\text{原 }(Y_p)_L\text{ 的全部 }(p-1)/2
        \text{ 个尖点构成一个闭点，剩余域 }LC_p^+.}
 \tag{816.17}
$$

特别在 $p=11\pmod{12}$ 时，m 为偶数，
$\gcd(m,p-1)$ 可以为二；这不影响 (816.15)。
本篇没有声称 $L\cap K(\xi_p)=K$，
也没有声称原 $L(\xi_p)/L$ 中全部 $p-1$ 个 automorphism
都存在。实际只需、且已证明保留的是实子域的 c 个 cusp 作用。
代表 d 与 $-d$ 给同一个 (816.13)，恰好消除了该无关的二次问题。

## 6. 原 X 到 Y：尖点总分歧而剩余域不变

在 $Y_p$ 的每个尖点，(816.11) 给
$\operatorname{ord}(t)=-p$，与三互素。
因此 $a^3=t$ 在函数域中不可约；$X_p/Y_p$ 次数确为三。

在该尖点对应的离散赋值域扩张中，
$\operatorname{ord}(a)=-p/3$ 迫使分歧指数为三。
全部扩张次数已经用尽，故其上只有一个尖点，且剩余域次数为一。
这个论证也在原闭点及 base change 到 L 后成立。
所以
$$
 \boxed{
 X_p\longrightarrow Y_p
 \text{ 在每个原尖点总分歧三，且 }\kappa(c_X)=\kappa(c_Y).
 }
 \tag{816.18}
$$
结合 (816.17)，得到本篇的另一主结论：
$$
 \boxed{\text{原 }(X_p)_L\text{ 的全部 }(p-1)/2
        \text{ 个尖点同样构成一个闭点，剩余域 }LC_p^+.}
 \tag{816.19}
$$
几何 j 极点阶也因此准确为 $6p$。

这不将一个指定解析参数
$Q=\exp(2\pi i\tau/(6p))$ 或其全部 Fourier 系数强行降到
$LC_p^+$。tame 根的切向相位可需要更大的系数字段。
(816.18)--(816.19) 说的是粗点剩余域与消失阶，不是任意参数的
逐系数不变性。

## 7. 对原函数、微分及后续 Hom 核的准确用途

任一 L 定义有理函数、微分或 L 定义线丛的截面，
在全部原尖点的零/极点阶都相同：
这是 (816.17) 或 (816.19) 的 Galois 运输，
局部参数乘单位不改变消失阶。
因此对任一 L 定义线丛 $\mathcal V$，非零截面 s 若在一个尖点
消失至少 r 阶，则
$$
 \frac{p-1}{2}\,r\le\deg\mathcal V .
 \tag{816.20}
$$
这是 R778 短展开注入论证的一般 p 几何输入，
不预称任何所需截面或 Fourier 前缀已经计算。

也可给后续一个严格的条件性接口。
设 V 是原 K-Hom 微分空间，所有元素在 L 上定义，
并且一个原作用实际满足
$$
 T h=\rho\,\sigma(h),\qquad
 \rho\in L^\times,\quad \sigma\in\operatorname{Gal}(L/K).
 \tag{816.21}
$$
取固定原尖点 c。若 h 在 c 的微分评价为零，
单轨道先迫使 h 在全部尖点为零；
再作 $\sigma$ 共轭并乘非零常数 $\rho$，仍在全部尖点为零。
故该评价核是 $K[T]$ 子模。

**只有再证明**该原 $K[T]$ 是域、V 为其秩一模，
以及至少一个原 V 元素在尖点评价非零，
才能推出评价核为零。
本篇没有将 R791 的 p=41 矩阵、域次数或一条已算非零首项
作为这些一般 p 输入；也没有用一个任意 Hodge 线性组合
替代真实 K-Hom 空间。

R770 的同一 primitive h 上三因子共同单位与原真实高度问题，
均不由单轨道结论自动完成。

## 依据

- [R575](R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md)，
  (575.4)：一般 p 的原六层纤维积及原三次扭曲。
- [R725](R725-original-CM-elliptic-model-and-splitting-field.md)，
  (725.10)--(725.11)：原最小分裂域 L 与准确次数 $(p+1)/6$。
- [R772](R772-original-RR-descent-and-exact-function-recovery-certificates.md)，
  (772.2)--(772.3)：原 mod2 算术模型及 $u=24s(2t-1)$ 的分支规范。
- [R778](R778-original-cusp-orbit-and-short-exact-recovery.md)，
  §§2--3：已登记 p=41 的原列向量、norm 标签及算术逆元方向。
- D. Zywina, *Explicit open images for elliptic curves over Q*，
  §5.2, Lemma 5.2，作者原稿：
  https://pi.math.cornell.edu/~zywina/papers/ExplicitOpenImage.pdf 。
  本次回读原文，确认 (816.12) 的右乘位置与 cusp 定义域；
  本篇的范数标签、原 K 识别、实子域互素和三次总分歧在正文证明。

本篇不运行新的数学计算，不重跑旧周期、Hom、尖点枚举或有限素数扫描。
