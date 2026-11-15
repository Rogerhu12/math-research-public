# R797 — 原零常数 charge 窗口的移动因子、六十四格与完整三次几何门

日期：2026-11-15。**状态：本文的来源分类、全部角帽、几何下界与显示非齐次矩阵已证明。** 本文不预报尚未执行的 producer 输出，不据有限分类本身宣称全部三次候选无解。

R792 已处理 $q(t,0)\ne0$。这里处理其剩余 $r=2$、$q(t,0)=0$ 分支。原最低 charge 是1，因而允许 $F(t,0)$ 含一个次数至多二的移动多项式 $H$；$H(0)$ 可以为零。保留这个实际常数系数后，原 $\mathbf F_p$ 上的来源准确被 $50+13+1$ 个固定角格覆盖。对 $b=b_0=3$，再保全部十九角可得
$$
\kappa\ge 9+6\deg H,
$$
以及完整有限几何类和原非齐次接触矩阵。本篇没有把移动根除掉，也没有改变已固定的首次修正 $P_2=P^{\rm fact}+pR$。

## 1. 原窗口及最低非零 charge

保持 R792 的原来源
$$
P^{\rm fact}=qt^2F^3\in\overline{\mathcal W}_D,\qquad
q=d^{-C_D}Q,\quad Q\in\mathbf F_p[t,Y],\qquad
d=1+8t,
\tag{1}
$$
其中 $F$ 为 primitive 不可约多项式，
$$
F(0,1)=0,\quad F_Y(0,1)q(0,1)\ne0,\quad
b=\deg_YF,\quad b_0=\deg_YF(0,Y)>4k_{\rm carry}+2.
$$
原零角条件给
$$
k_{\rm carry}=0,\qquad b_0=m_F=3,\qquad m_q\le1.
$$
本篇新增假设仅为 $q(t,0)=0$。R792(19)、(22) 遂精确给
$$
\boxed{
q=Y\widetilde q,\qquad
\widetilde q(0,Y)=c_q\in\mathbf F_p^\times,\qquad
-v_0(\widetilde q)=0.}
\tag{2}
$$
不是把 $Y$ 免费除掉后再使用常数 charge 的四次帽。

以下先分类所有 $b\ge3$。第5节以后才取 $b=3$，并在强接触应用中保
$$
\ell=1,\quad s=2h+2,\quad p=12h+11>101,\quad f_D<p,
\qquad h\ge\kappa+14,\quad \kappa=C^2.
\tag{3}
$$
特别 $h<s$，原低轴 $\rho$ 与真正 regularized 轴的 $t^{<h}$ 系数相同。

令 $F_0=F(t,0)\ne0$，按其准确 $d$ 阶写
$$
F_0=\lambda d^cH,\qquad
c\ge0,\quad \lambda\in\mathbf F_p^\times,\quad
H\text{ monic},\quad (H,d)=1,\quad z=\deg H.
$$
原 charge1 系数为次数至多八的多项式：
$$
t^2\widetilde q(t,0)F_0^3\in\mathbf F_p[t]_{\le8}.
$$
唯一可能的分母在 $d$；$H$ 与 $d$ 互素。因此
$$
\boxed{
0\le z\le2,\quad
G=\frac{F}{\lambda d^c},\quad G(t,0)=H,\quad
A_1=\lambda^3d^{3c}\widetilde q(t,0)\in\mathbf F_p[t],}
\tag{4}
$$
$$
\boxed{
A_1(0)\ne0,\qquad \deg A_1\le6-3z,\qquad
t^2YA_1G^3\in\overline{\mathcal W}_{3b+1}.}
\tag{5}
$$
最后一个结论是 R792(23) 的真正来源返回：在 $\widetilde q$ 中仅取常数 charge 提高各 Gauss 赋值，再按 R491 的双向识别返回全部原系数帽。原 $D\ge3b+1$，且 $f_{3b+1}\le f_D<p$。

## 2. 原五种 Gauss 赋值和移动根

记 $h_7=16t^2+4t+7$。对于只在 $d$ 有极的 $P=\sum P_n(t)Y^n$，原来源的准确条件是
$$
\begin{array}{c|c|c}
\text{位置}&v(P)&\text{下界}\\ \hline
0,\ h_7(\alpha)=0&\min_n(4\operatorname{ord}_\alpha P_n-n)&-2\\
1&\min_n(3\operatorname{ord}_1P_n-n)&-1\\
d=0&\min_n(2\operatorname{ord}_dP_n+n)&0\\
\infty&\min_n(9n-2\deg_tP_n)&-8 .
\end{array}
\tag{6}
$$
这些赋值对乘法准确相加。对归一 $G$ 定义
$$
m_\alpha=-v_\alpha(G),\quad m_1=-v_1(G),\quad
\delta_d=-v_d(G),\quad \delta_\infty=-v_\infty(G).
$$
由 $F$ primitive，任一有限角都有某个 $F_n$ 在该角为单位；故
$$
0\le m_\alpha,m_1\le b.
$$
这里即使 $H$ 在该角消失也成立：不能仅从常数系数读出整个 $F$ 的共同因子。又因 $H(d)\ne0$ 和 $\deg H=z$，
$$
\boxed{\delta_d\ge0,\qquad \delta_\infty\ge2z,\qquad v_0(G)=-3.}
\tag{7}
$$

将 (5) 逐角代入 (6)，得到
$$
\boxed{
\begin{aligned}
3m_\alpha&\le4\operatorname{ord}_\alpha A_1+1,\\
m_1&\le\operatorname{ord}_1A_1,\\
3\delta_d&\le1+2\operatorname{ord}_dA_1,\\
3\delta_\infty+2\deg A_1&\le13.
\end{aligned}}
\tag{8}
$$
零角正好为
$$
v_0(t^2YA_1G^3)=8-1-9=-2.
\tag{9}
$$
这里 (8) 的常数 $1,1,13$ 都包含真实额外 $Y$ 的角权；不能改用 R782 的五型常数。

若 $\alpha$ 是 $H$ 的移动根而不在固定角上，$G$ 的所有系数仍在 $\alpha$ 正则。原来源不要求各系数都被 $H$ 整除，所以这里没有一个可被丢弃的共同因子。若擅自改用 $G/H$，就在这些根处新增极点，并须把 $H^3$ 加回乘子。本文始终保 $G_0=H$，因此完整覆盖 $H$ 的两个不同根、重根以及 $H(0)=0$；没有为这些根预设分裂或单位条件。

## 3. 六十四个固定角 mask 与每一条准确次数帽

删去 $A_1$ 中不在 $(t-1)dh_7$ 上的因子不减弱有限固定角条件，而只改善无穷远帽。$A_1(0)\ne0$，所以没有需要删除的 $t$ 因子。

在原 $\mathbf F_p$ 上，$p\equiv5\pmod6$ 使 $h_7$ 不可约，其两几何角的亏损相同，记为 $m_h$。于是某个真实返回乘子可取
$$
\boxed{
A_*=(t-1)^i d^j h_7^k,\qquad
i,j,k\ge0,\qquad i+j+2k\le6-3z,}
\tag{10}
$$
且
$$
t^2YA_*G^3\in\overline{\mathcal W}_{3b+1}.
$$
这仍是保同一 $F$ 的因子存在性操作，不声称新 cube 与原 $P^{\rm fact}$ 有相同首 Bockstein。

令 $a=i+j+2k$。对应完整格的亏损上界是
$$
\boxed{
\begin{aligned}
M_h&=\min\!\left(b,\left\lfloor\frac{4k+1}{3}\right\rfloor\right),&
M_1&=\min(b,i),\\
D_d&=\left\lfloor\frac{2j+1}{3}\right\rfloor,&
D_\infty&=\left\lfloor\frac{13-2a}{3}\right\rfloor .
\end{aligned}}
\tag{11}
$$
实际亏损可小于上界，并且 $2z\le\delta_\infty\le D_\infty$。

| $z=\deg H$ | mask 的完整范围 | 原始 mask 数 | 移动常数系数 |
|---|---|---:|---|
| 0 | $i+j+2k\le6$ | 50 | $H=1$ |
| 1 | $i+j+2k\le3$ | 13 | $H=t+h_0$ |
| 2 | $i=j=k=0$ | 1 | $H=t^2+h_1t+h_0$ |

数量分别是
$28+15+6+1=50$、$10+3=13$、$1$。
相同上界可能重复，producer 可以去重；不把去重误作删除实际格。

对每个 $1\le n\le b$，定义
$$
a_n=\left\lfloor\frac n4\right\rfloor,\quad
b_n=\max\left(0,\left\lceil\frac{n-M_h}{4}\right\rceil\right),\quad
c_n=\max\left(0,\left\lceil\frac{n-M_1}{3}\right\rceil\right),
$$
$$
z_n=\left\lfloor\frac{n+D_d}{2}\right\rfloor,\quad
K_n=\left\lfloor\frac{9n+D_\infty}{2}\right\rfloor,\quad
r_n=t^{a_n}h_7^{b_n}(t-1)^{c_n}d^{-z_n}.
$$
整个允许线性包络精确为
$$
\boxed{
G=H+\sum_{n=1}^bY^nr_n p_n(t),\qquad
\deg p_n\le K_n-\deg_t r_n.}
\tag{12}
$$
有理函数次数包括 $d$ 分母，负帽表示该组为空。
式 (12) 是 (6) 各有限角整除条件与无穷远帽逐系数求交，不仅是一组试验来源。归一 $H$ 的精确次数和 $(H,d)=1$ 另外保留。

反过来，若 (12) 的元素满足准确零角 $v_0(G)=-3$，则 (11)、(8)、(9) 证明其 (10) cube 确实属于原 $\overline{\mathcal W}_{3b+1}$。但 primitive、不可约、原点光滑、准确 $b_0$ 以及强接触都不是表格自动赋予的性质。

在较大剩余域上，必须把 $h_7$ 按真实因子分开记录；本篇不把六十四这个数推广到分裂域。

## 4. 原接触是一个保移动常数的非齐次问题

沿原低轴
$$
\rho(t)=d(t)\Theta(t)^{17},\qquad
\log\Theta(t)=-\sum_{n\ge1}\frac{q_n^\Theta}{3n}t^n,
$$
$$
q_1^\Theta=-\frac25,\qquad
q_n^\Theta=q_{n-1}^\Theta\frac{6n-4}{6n-1}.
\tag{13}
$$
这仍是 R788 的同一原级数；其 $\rho'(0)=154/15$。

把 $H=t^z+\sum_{j<z}h_jt^j$ 的低系数与 (12) 的全部 $p_n$ 系数合并为未知数，真正接触 $G(t,\rho)\equiv0\bmod t^h$ 为
$$
\boxed{
\sum_{j<z}h_j\mathbf1_{\ell=j}
+\sum_{n=1}^b\sum_{j=0}^{K_n-\deg r_n}
x_{n,j}[t^{\ell-j}](r_n\rho^n)
=-\mathbf1_{\ell=z},\qquad0\le\ell<h.}
\tag{14}
$$
这里 RHS 为 $-t^z$；不能改成常数 $-1$ 后把 $H$ 当单位除掉。
在 (3) 中 $h<s$，(13) 的所有被读分母均为 $p$ 单位，且与目标特征的原低轴相同。没有另造独立的各幂系数。

式 (14) 保整个必要包络。无解即可排除对应原因子；有解仍须保 $(H,d)=1$、$F_Y(0,1)\ne0$、$b_0=3$ 和实际十九角几何，不能把线性解认作已经找到强接触曲线。

## 5. b=3 的全部十九角及更强自交数下界

现在取 $b=b_0=3$。原零角四步链的重数全为零，因为 $F_3(0)\ne0$。记原紧化的最小整数 $u$ 满足
$$
\deg_tF_n\le u+4n,
$$
并置 $v=u-c$。由 $F_0=\lambda d^cH$ 得 $v\ge z$。

保 R495 的实际非增重数序列
$$
\boldsymbol\mu_h\ (4\text{项，两共轭角相同}),\quad
\boldsymbol\mu_1\ (3\text{项}),\quad
\boldsymbol\mu_d\ (2\text{项}),\quad
\boldsymbol\mu_\infty\ (2\text{项}).
$$
其准确总和是
$$
\boxed{
\begin{aligned}
|\boldsymbol\mu_h|&=3-m_h,&
|\boldsymbol\mu_1|&=3-m_1,\\
|\boldsymbol\mu_d|&=2c-\delta_d,&
|\boldsymbol\mu_\infty|&=2v-\delta_\infty .
\end{aligned}}
\tag{15}
$$
每条总和介于0与3之间。还保来自真实常数系数的逐步条件
$$
\mu_{d,1}\le c,\qquad
\mu_{\infty,1}\le v-z.
\tag{16}
$$
非增性使这些条件也给每个累计值不超过 $jc$、$j(v-z)$。注意 $z>0$ 时不能只用旧的 $jv$ 帽。

故全部参数有有限范围
$$
\boxed{
0\le c\le\left\lfloor\frac{3+\delta_d}{2}\right\rfloor,\qquad
z\le v\le\left\lfloor\frac{3+\delta_\infty}{2}\right\rfloor,\qquad u=c+v.}
\tag{17}
$$
由于本篇可能有 $\delta_d,\delta_\infty>1$，不能套 R788 的特殊两项等式
$(c,c-\delta_d)$ 和 $(v,v-\delta_\infty)$；必须枚举满足 (15)、(16) 的全部实际二步序列。

自交数和反规范交数准确为
$$
\kappa=36+6(c+v)
-2\sum\mu_h^2-\sum\mu_1^2-\sum\mu_d^2-\sum\mu_\infty^2,
$$
$$
\chi=-K_XC=9+2m_h+m_1+\delta_d+\delta_\infty.
\tag{18}
$$
另保原必要门 $\kappa\ge\chi-2$ 和 $\kappa-\chi$ 为偶数。

**定理。** 所有本篇实际三次曲线都满足
$$
\boxed{
\kappa\ge9+6m_h+3m_1+3\delta_d+3\delta_\infty
=3\chi-18\ge9+6z.}
\tag{19}
$$

**证明。** (15) 的每个重数介于0与3之间，故 $\mu^2\le3\mu$。将此逐项代入 (18)，再用 (15)，得到
$$
\begin{aligned}
\kappa
&\ge36+6c+6v
-6(3-m_h)-3(3-m_1)
-3(2c-\delta_d)-3(2v-\delta_\infty)\\
&=9+6m_h+3m_1+3\delta_d+3\delta_\infty.
\end{aligned}
$$
最后由 $\delta_\infty\ge2z$ 得结论。该证明只使用真正十九角重数，不用一般位置或任何特征零消失定理。$\square$

于是 (3) 的强窗必要地满足
$$
\boxed{h\ge23+6z,\qquad p\ge287+72z.}
\tag{20}
$$
若某个更短有理前缀给出全大素数门，(20) 可以精确缩小余下有限特征；不能只据参数个数省掉小素数几何。

## 6. 每个实际几何类的整段原来源

令 $V_j^h,V_j^1,V_j^d,V_j^\infty$ 为 (15) 对应累计值。
对 $1\le n\le3$ 定义
$$
\begin{aligned}
\widehat b_n&=\max\left(0,\max_{1\le j\le4}
 \left\lceil\frac{V_j^h-3+n}{j}\right\rceil\right),\\
\widehat c_n&=\max\left(0,\max_{1\le j\le3}
 \left\lceil\frac{V_j^1-3+n}{j}\right\rceil\right),\\
\widehat z_n&=\max\left(0,\max_{1\le j\le2}
 \left\lceil\frac{V_j^d-n}{j}\right\rceil\right),\\
\widehat K_n&=\min\left(u+4n,\
 \min_{1\le j\le2}
 \left\lfloor\frac{ju+(4j+1)n-V_j^\infty}{j}\right\rfloor\right).
\end{aligned}
\tag{21}
$$
则全部原多项式系数包络是
$$
\boxed{
F=d^cH+\sum_{n=1}^3
Y^nh_7^{\widehat b_n}(t-1)^{\widehat c_n}
d^{\widehat z_n}p_n,\qquad
\deg p_n\le\widehat K_n-2\widehat b_n-\widehat c_n-\widehat z_n.}
\tag{22}
$$
标量 $\lambda$ 已用整体非零倍归一。式 (21) 沿 R495 每一步角帽逐项求交；某个包络元素可能有更大的真实重数，使用这个较大格作无解证明仍合法。

(22) 的实际接触矩阵右端是 $-d^ct^z$，另将全部 $d^ct^j$、$0\le j<z$ 保为未知列。正 charge 列是
$$
t^j h_7^{\widehat b_n}(t-1)^{\widehat c_n}
d^{\widehat z_n+n}\Theta^{17n}.
\tag{23}
$$
因此同一个 $\rho$、全部原多项式乘子和移动常数系数都显式保留。

在任何仿射解空间中，三项必要开条件分别为
$$
F_3(0)\ne0,\qquad F_Y(0,1)\ne0,\qquad H(-1/8)\ne0.
\tag{24}
$$
它们各是一个仿射线性函数不为零。若每个函数在该解空间上不恒零，则因 $p>101>3$，三个真仿射超平面不能覆盖整个解空间；故这些开条件可同时满足。反之任一函数恒零即可删去该必要类。即使 (24) 可同时满足，也未证明不可约、primitive 或准确强接触。

## 7. 可复现的全素数判定程序与当前证据边界

producer：
[check-r797-original-r2-y-factor-b3.py](../scripts/check-r797-original-r2-y-factor-b3.py)。

它只复用已发布 R788 脚本的精确整数、Fraction、Bareiss 和有限域运算，不复用 R788 五型的排除结论。预定参数为
`--max-order 64 --remaining-examples 20`；所有数学执行交本库公开 Actions，本文不以未执行输出作证据。

第一段对 (10)—(12) 的去重完整格计算最大有理子式。常数列 $1,t,\ldots,t^z$ 在行 $0,\ldots,z$ 是单位块；其余所用行保全部正 charge 列。逐行清除原有理分母后，在整数中求多个非零最大子式的 gcd，并要求完整试除后的剩余因子恰为1，才报告全共同坏素数已确定。高于这些共同坏素数且 $h$ 超过全部所读行时，原非齐次矩阵必无解。

第二段按 (11)、(15)—(18) 枚举全部必要十九角类，并对所有未被第一段排除的目标素数使用 (22)、(23) 的全行非齐次消元。它另外核 (24)，保同一个真实 RHS。每个可能的原候选都在所枚举包络中。

程序只向公开日志输出最多59000字节，保完整 profile 摘要、gcd 因式、证书行范围和哈希、全部几何输入及有限消元结果的哈希、计数和至多二十个余例。不向仓库或 Release 写矩阵、输出或可复算数据。只有执行完成并取得 run、脚本与输出 SHA256 后，才能据具体结果追加全素数排除或准确的剩余类。

## 8. 同一个首次修正仍保留

从 (1) 投影到 (5)、再删冗余 mask，仅为原因子存在性提供必要来源门。若原 $P^{\rm fact}+pR$ 已经固定，不能用 $t^2YA_*G^3$ 替换后仍保旧 forcing。

尤其本篇 $q(0,Y)=c_qY$，其非常数 charge 在零点不被 $t$ 整除；所以 R782 的特定 scalar 投影第三块不变式不能照搬。原第三 $w^{13}$ 单位行、完整 first-normal、两条十三行 carry、$P_{134}/U_0$ 及下一精度的同一个 $R$ 继续原样保留。

本篇的新结论是零常数支的完整六十四格、移动根不被丢弃的实际接触矩阵、全部三次十九角类和 (19) 的几何加强。尚未由这些结论本身得到一般 $b\ge4$ 无解、指定完整 Bockstein 非零，或主目标的无穷素数结论。

依赖：
[R491](R491-valuated-source-factor-lifts-and-homogeneous-joint-obstruction.md)；
[R495](R495-fixed-angular-surface-and-full-triple-source-joint-image.md)；
[R788](R788-original-cubic-factor-all-prime-exclusion.md)；
[R790](R790-original-cube-full-forcing-and-factor-contact-bockstein-pairing.md)；
[R792](R792-original-nonzero-constant-charge-classification-and-cubic-extension.md)；
[R795](R795-original-factor-contact-one-dimensional-kernel-and-unit-next-row.md)。
