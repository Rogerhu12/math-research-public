# R872 补充 — 原 charge 四十的 cubic 原函数格与三尾零像

日期：2026-11-16。**状态：下列同一原来源子格、唯一值门、两整条 carry 带的零响应及因子交已证明。没有证明该子格之外的原首核尾像，也没有构造一个新的非 $F^2$ 首核。**

本注接 [R872](../results/R872-actual-quartic-third-carry-and-central-first-digit.md) 和[原 cubic／square 因子层](2026-11-16-r872-tail-adjustments-in-cubic-and-square-factor-lattices.md)。这里使用原总 charge 的对角逆，不使用裸 $E$ 原函数，不扩大 $\mathcal W_D$，不改变同一 $P,R,S$。

## 1. 原格与窗口

在 R872 的共同 $b=1$、Hasse 对齐规范内工作。置
$$
p=6s-1>211,\qquad
\Gamma=\mathcal O[w,\epsilon]/
(w^s-p\epsilon,\epsilon^4,w^{\ell+13}\epsilon^3).
$$
所有 $P_{134}$、$c_*U_0$、十九角及原三条十三行带均保留。

本注采用原低松弛情形
$$
r=3,\qquad
\tau=3+2h-s\in\{1,2,3\},\qquad
\tau<\ell\le h-1,\qquad h<s-4 .
\tag{1}
$$
记 $T=s-13$。假设原不可约因子 $F$ 满足
$$
\deg_YF(0,Y)=3,\qquad
F(0,1)=0,\qquad
(EF)(0,1)\ne0,\qquad E=Y\partial_Y,
\tag{2}
$$
以及在原实际轴上接触为 $h$。
R872 的参考轴 $g_{\Theta,\circ}$ 与实际轴之差始于 $w^{s-4}$，所以
$$
F(t(w),\bar g_{\Theta,\circ}(w))=w^h u(w),\qquad u(0)\ne0 .
\tag{3}
$$
以下 $W_i$ 始终是 R872 同一参考上的完整读取；不独立重选 $g$。

另显式要求原 charge 单位门
$$
\boxed{p>D+40.}
\tag{4}
$$
这是使全部 $40,41,\ldots,40+D$ 为单位的来源门；不由 (1) 偷推。

设 $k$ 为剩余域。原格按 $Y$ 的次数直和，故
$$
L=E+40:\mathcal W_D\longrightarrow\mathcal W_D
\tag{5}
$$
是同一格的对角自同构：
$$
L^{-1}\!\left(\sum_{n=0}^D c_n(t)Y^n\right)
 =\sum_{n=0}^D\frac{c_n(t)}{n+40}Y^n .
\tag{6}
$$
每项只乘 $k$ 的单位，原 $q_n(t)$、次数帽与十九角均逐项保持。
这与 $E^{-1}$ 的零 charge 缺陷不同。

令 $U(w)$ 表示 R872 读取中已经固定的完整公共单位。准确有
$$
W_i(W)=U(w)(L^iW)(t(w),\bar g_{\Theta,\circ}(w)).
\tag{7}
$$
式 (7) 保留公共 charge 四十；没有把物理 $w^{13}$ 从原目标中反除。

## 2. Gauss 低角迫原 cubic 值含 $t^2$

定义真正的因子子格
$$
\mathscr V_j=\mathcal W_D\cap F^j k(t)[Y].
\tag{8}
$$
在 $t=0$ 附近取 $F$ 的原整本原框。因 $F(0,Y)\ne0$，若
$F^jA\in\mathcal W_D$，则 $A$ 在 $t=0$ 无极点。

原零角 Gauss 帽逐个给
$$
\boxed{
[t^\nu]W\ne0\quad\Longrightarrow\quad
\deg_Y[t^\nu]W\le4\nu+2 .
}
\tag{9}
$$
也可直接从原 $n$ 列至少含 $t^{\lfloor(n+1)/4\rfloor}$ 读出。
$d(t)$ 在 $0$ 为单位，不影响这个首系数论证。

若 $F^3A\ne0$，令 $\nu=\operatorname{ord}_t A$。
其首系数为 $F(0,Y)^3A_\nu(Y)$，次数至少为 $9$。
$\nu=0,1$ 的原帽分别为 $2,6$，均不可能，故
$$
\boxed{F^3A\in\mathcal W_D\ \Longrightarrow\ A\in t^2k[[t]][Y].}
\tag{10}
$$
相同论证给
$$
\boxed{F^4A\in\mathcal W_D\ \Longrightarrow\ A\in t^3k[[t]][Y].}
\tag{11}
$$
这里不把 $A/t^2$ 或 $A/t^3$ 认成原来源列；只读取原整乘积迫出的局部阶。

## 3. 一个不要求 $F^2$ 因子的实际尾零子格

定义
$$
\boxed{\mathscr J_3=L^{-1}(\mathscr V_3)\subset\mathcal W_D.}
\tag{12}
$$
取 $W\in\mathscr J_3$，写 $LW=F^3A$。
由 (10)，$A\in t^2$。原 $L$ 的两次乘积式为
$$
\begin{aligned}
L(F^3A)&=3F^2eA+F^3LA,\\
L^2(F^3A)&=
6Fe^2A+3F^2f_2A+6F^2eLA+F^3L^2A,
\end{aligned}
\tag{13}
$$
其中 $e=EF,\ f_2=E^2F$。$L$ 不改变 $t$ 阶。
代入同一轴 (3)，连同真实 $t/w$ 和 $U$ 单位，得到
$$
\boxed{
\operatorname{ord}_wW_1(W)\ge3h+2,\qquad
\operatorname{ord}_wW_2(W)\ge2h+2,\qquad
\operatorname{ord}_wW_3(W)\ge h+2 .
}
\tag{14}
$$
式 (1) 给 $s\le2h+2$、$\ell\le h-1$。因此这三条读取自动满足原首核中的全部相应长／短块。

于是原完整首核 $K_1=\ker\bar M$ 在此子格上只有一个实际条件：
$$
\boxed{
\mathscr J_3\cap K_1
=\{W\in\mathscr J_3:\ W_0(W)\in w^Tk[[w]]\}.
}
\tag{15}
$$
这个条件仍在同一原格中，不能把 $W_0$ 的高前缀自由赋值。
在参数 $F^3A=\sum c_n(t)Y^n$ 下，(15) 正是
$$
\left[
U(w)\sum_{n=0}^D\frac{c_n(t(w))}{n+40}
  \bar g_{\Theta,\circ}(w)^n
\right]_{<T}=0 .
\tag{16}
$$
所以 $L:\mathscr J_3\simeq\mathscr V_3$ 虽是整单位同构，
(16) 的有限评价核仍须实际求解。

定义同 R872 的三尾映射
$$
\Pi(W)=
\bigl([w^{s-3}]W_2(W),[w^{s-2}]W_2(W),[w^{s-1}]W_2(W)\bigr).
$$
由 (14) 得
$$
\boxed{\Pi(\mathscr J_3)=0.}
\tag{17}
$$
这不要求 $W$ 本身被 $F^2$ 整除。
若改回实际轴，同一代换的首差含
$w^{s-4}W_3(W)$，其阶至少 $s+h-2\ge s$；
因此本子格的三个零尾也不因该完整参考运输改变。

## 4. 两整条原 carry 带也为零

R828 的原第一 carry 为
$$
\mathcal K_{j,1}(W)_r
=\frac{a^{j-1}}{(j-1)!}
\left([w^{s-13+r}]W_{j-1}(W)
 +H_p[w^{r-9}]B W_j(W)\right),
\quad0\le r\le12 .
\tag{18}
$$
这里只约化第一 Bockstein 行；$B$ 仍是实际完整级数。

由 (14)，对任意 $W\in\mathscr J_3$，
$$
\boxed{
\mathcal K_{2,1}(W)=\mathcal K_{3,1}(W)=0,\qquad
\mathcal K_{1,1}(W)_r=[w^{T+r}]W_0(W).
}
\tag{19}
$$
所以对 (15) 中的实际首核，通过这三条带的下一步必要门，恰是同一个值条件从 $T$ 加深到 $s$：
$$
\boxed{
\mathcal K_{j,1}(W)=0\ (j=1,2,3)
\iff W_0(W)\in w^sk[[w]] .
}
\tag{20}
$$
这只是显示的三条带，不是整个第一 Bockstein 为零的充要条件。
其余目标行、native 整商及所有 normal/carry 仍保留。

## 5. 与平方因子格的准确交

由 (2) 和 $F$ 不可约，有 $\gcd(F,e)=1$。
若 $W=F^2C\in\mathscr J_3$，则
$$
LW=2FeC+F^2LC\in F^3k(t)[Y].
$$
先除一个 $F$ 再模 $F$，得 $F\mid C$。
写 $C=FC_1$ 后，
$$
LW=3F^2eC_1+F^3LC_1,
$$
又得 $F\mid C_1$。反过来 $L(F^4C_2)$ 必被 $F^3$ 整除。
因为 $2,3$ 为单位，准确得到
$$
\boxed{\mathscr J_3\cap\mathscr V_2=\mathscr V_4.}
\tag{21}
$$
公共常数 $40$ 只进入较高 $F$ 次项，不能改变这两个首项。

由 (11)，$\mathscr V_4$ 的四个原读取首阶分别至少为
$4h+3,3h+3,2h+3,h+3$，故在 (1) 内
$$
\boxed{\mathscr V_4\subset K_1.}
\tag{22}
$$
于是
$$
(\mathscr J_3\cap K_1)\cap(\mathscr V_2\cap K_1)=\mathscr V_4 .
$$
这条交是原格中的实际交，不是环境理想商的维数类比。

本注没有证明 $\mathscr J_3\cap K_1$ 严格大于 $\mathscr V_4$。
特别不能由 (21) 宣称已经构造一个非 $F^2$ 的首核。
若前述因子层注的两个严格反门成立，则
$\mathscr V_2\cap K_1=\mathscr V_4$；
此时已支付的整个平方块已包含在 $\mathscr J_3\cap K_1$ 中，
两个块的秩不能再相加。

## 6. 对同一修正的准确用途和剩余门

式 (17) 给原映射的真实因子化
$$
\boxed{
\Pi:K_1/(\mathscr J_3\cap K_1)\longrightarrow k^3 .
}
\tag{23}
$$
该商的像仍未判定。

在 R872 第二页固定 $P$ 改 $R\mapsto R+W$，或第三页固定 $P,R$ 改
$S\mapsto S+W$，若 $\bar W\in\mathscr J_3\cap K_1$，
则该文 $\tau=1,2,3$ 的指定 scalar 不变，因为其响应恰是
$a^2\pi_\tau(W)/2$。
这不意味着全部页类不变：同一个 $W$ 的其余
$\beta_1(W)$ 及更高整商仍可能贡献。
式 (19) 只另外支付了两条完整十三行带的零响应。

因此下一问题确切是 (23) 剩余商的实际像，以及该像与同一
$R,S$ 的其它行是否兼容。新的 source 对角逆没有添加一条中央零，
没有增加原 target 的长度，也没有由一个局部单位推全局余类非零。

本注仅作原格的符号证明，无新增数值运行。
