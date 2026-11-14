# R454 — 原残余斜轴的 degree 33 绝对核心与完整深管运输

日期：2026-11-14。**状态：已证明。**

在 R451 的同一个实际 $D$ 正来源上，残余斜轴
$T=Z-33H$ 与 $Z$ 真正正交，两个 theta degree 是 $33,18480$。
只将原固定 ray 再细分 $\pi_0\equiv2\pmod{11}$ 后，整个奇
degree 33 核心是实际标量 $\chi_p$。本篇以两个原 sigma 的
完整联合锚证明 $\chi_p^2=1$，不猜它的符号。

由原两输出全深身份，$T$ 核心严格返回同一个
$\mathcal L_+$，系数为 $-\eta\chi_p\lambda$。
它保原 $Z,c$，因此保 $Y=Z+c$；目标
$\mathscr H=U-280X=9T$ 的深条件终于可以在保原独立 sigma 的
完整来源上直接运输。对应的另一个正交输出
$\mathscr J=U+17X$ 也有已定绝对符号的真实核心。
所有测试的剪切和补域仍保留。

## 1. 同一个固定无限普通族的 mod 11 细分

保持 R439 的原实际规范
$$
\lambda=-\bar\pi_0^{-1},\qquad
\lambda_\sigma=-\lambda,\qquad
\kappa=p/\bar\pi_0^2,\qquad
\pi_{17}=-\pi_0,\qquad \eta=\eta_{5,p}\in\{\pm1\}.
\tag{1}
$$
原 ray 是
$$
\pi_0\equiv158774527+130245570\omega\pmod{253955520}.
$$
只追加固定条件 $\pi_0\equiv2\pmod{11}$。
完整 CRT 给
$$
\boxed{
\pi_0\equiv1428552127+2161889730\omega
                  \pmod{2793510720}.}
\tag{2}
$$
模原模数的两个坐标不变，模 $11$ 的坐标分别为 $2,0$。
新模数是原模数乘 $11$，新类的范数与模数互素；
其范数余数是 $1646199559$。因此同一个 CM ray-class
Chebotarev 输入给一个固定正密度普通子族。
所有旧条件、原 $E_{17}$、周期和 $\pi_{17}=-\pi_0$ 均保留。

记 $g=\pi_0/\bar\pi_0$。直接约化得到
$$
\boxed{g\equiv1\pmod{33},\qquad g\equiv1\pmod{66}.}
\tag{3}
$$
还保 $p\equiv7\pmod{64}$。
以后仍只用原 $p>19$；特别 $2,3,7,11,17$ 都已排除。
新 ray 没有更换目标曲线或另取一个未经控制的无限集合。

## 2. 真正的奇偶两轴 theta 格

沿用 R451 的残余物理输出 $(Z,H)$，其 Gram 矩阵为
$$
\begin{pmatrix}33&1\\1&17\end{pmatrix}.
$$
这是从原 $\mathcal K_+$ 的两个 degree $34,18$ 中，
准确去掉外部 $\sigma(y-v)$ 的 Gram
$\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$ 得到的。

定义
$$
\boxed{T=Z-33H.}
\tag{4}
$$
真实整坐标矩阵及 Gram 为
$$
\begin{pmatrix}1&0\\1&-33\end{pmatrix},
\qquad \det=-33,
$$
$$
\boxed{
\begin{pmatrix}1&0\\1&-33\end{pmatrix}
\begin{pmatrix}33&1\\1&17\end{pmatrix}
\begin{pmatrix}1&1\\0&-33\end{pmatrix}
=\operatorname{diag}(33,18480).}
\tag{5}
$$
当前每个普通处的行列式都是单位。

R446、R451 给
$\mathcal L_+(y,v)=\sigma(y+v)A_+(y,v)$，
其中 $A_+\in\mathcal S_{32}\otimes\mathcal S_{16}$。
在新生成变量 $(z,t)$ 中，完整来源是
$$
\boxed{
\widetilde{\mathcal L}_+(z,t)
=\sigma(z-32t)A_+(z+t,-33t)
\in\mathcal S_{33}\otimes\mathcal S_{18480}.}
\tag{6}
$$
两个 degree 和交叉项分别为
$$
1+32=33,\qquad
32^2+32+16\cdot33^2=18480,\qquad -32+32=0.
$$
$z$ 轴的唯一 odd 半特征来自 $\sigma(z-32t)$，
正是原 $\sigma^{33}$ 的半特征；
$t$ 轴的该系数 $-32$ 为偶数，故半特征平凡。
没有平坦 twist 或交叉 Gaussian 留下。

(6) 还是整张量格中的元素：它由原整联合测度作 (5) 的整
可逆变换得到。奇 degree 33 的基
$\sigma^{33}x^j$、$\sigma^{33}yx^j$ 的首阶互异，
与 R413 的正式群首阶消元同样给整系数。
特别
$$
\widetilde{\mathcal L}_+(z,0)
=-\frac{2S(z)}{3\sigma(z)}
=-\frac23z^5+\cdots\ne0.
\tag{7}
$$
这是一条实际非零 primitive 来源，不使用未知中央值。

## 3. 奇 degree 33 的完整 trace 与唯一中心规范

对 $\mathcal S_{33}=\sigma^{33}L(33O)$，
使用 R368、R370 的同一个奇 degree division trace，只将幂改为
$33$：
$$
\mathscr M_a(\sigma^{33}f)
=\sigma^{33}\operatorname{Tr}_{[a]}
 \left[\left(\frac{r_{\bar a}}{r_a}\right)^{33}
                          f\circ[\bar a]\right],
$$
$$
\boxed{K_{33}=\frac{\bar\pi_{17}}p\mathscr M_{\pi_{17}},\qquad
\nu_F|_{p\mathbf Z_p}
=\lambda[\kappa]_*\nu_{K_{33}F}.}
\tag{8}
$$
原 division 函数、未归一 trace 和普通周期都不改换。
因 $\pi_{17}$ 在二挠上为恒等，奇半特征在该 trace 中保持；
原正式群根单位平均给 (8)，其整性也由右侧的规范化限制直接得到。
这适用于整个奇 degree 空间，不只是一个角型或边际。

为支付 order $33$ 的中心，记 $\mathsf JF(z)=F(-z)$。
对任一 $P\in E[33]$ 的 lift $A_P$，写
$$
A_P^{33}=a,\qquad
\mathsf JA_P\mathsf J=bA_P^{-1},\qquad b^{33}=a^2.
$$
则
$$
\boxed{U_P=(b^{16}/a)A_P}
\tag{9}
$$
准确满足 $U_P^{33}=I$ 和
$\mathsf JU_P\mathsf J=U_P^{-1}$。
两个满足这些条件的 lift 之比同时是三十三次根和平方根，
所以必须为一。这给同一个唯一完整规范，不能另添一个中心符号。

原几何 trace 将 Heisenberg 参数送至 $gP$ 并与 $\mathsf J$ 交换。
如在 lift 比较中出现标量，它同时有三十三次幂一和平方一，
因此为一。这与 R370 的奇 degree 五证明完全同构，
但这里已逐项给出 degree 33 的规范。
由 (3)，$K_{33}$ 与所有 $U_P$ 交换。

在标准三十三维 Heisenberg 基上，一对生成元分别为互异
$\zeta_{33}$ 特征的对角矩阵和循环移位矩阵；
同时与两者交换的算子只能是标量。
于是存在由原实际 trace 唯一确定的 $\chi_p$，使
$$
\boxed{K_{33}=\chi_p I
          \quad\text{于整个 }\mathcal S_{33}.}
\tag{10}
$$
此时尚未猜定它的值；下一节同时排除零并付绝对平方。

## 4. 两个原 sigma 付清绝对平方

令
$$
\delta=1+2\omega,\qquad \gamma_7=3+\omega,\qquad
\alpha=2\delta,\qquad\beta=\delta\gamma_7.
$$
准确有
$$
N\alpha=12,\qquad N\beta=21,\qquad N\alpha+N\beta=33.
$$
取两个同一原 sigma 的真实联合
$$
\boxed{
F(z,t)=\sigma(\alpha z-\bar\beta t)
       \sigma(\beta z+\bar\alpha t).}
\tag{11}
$$
它的两个 degree 均为 $33$，交叉 Hermitian 项是
$-\alpha\beta+\beta\alpha=0$。
其两个半特征也必须保留：$\alpha$ 是偶 CM 整数，
而 $\beta\equiv\omega^2\pmod2$，
$-\bar\beta\equiv\omega\pmod2$；
原 sigma 半特征对 $\omega$ 作用不变。
因此
$$
\boxed{F\in\mathcal S_{33}\otimes\mathcal S_{33}}
\tag{12}
$$
具有两条原 odd 半特征，没有改变 theta characteristic。

对应真实两个输出的矩阵是
$$
\begin{pmatrix}\alpha&\beta\\-\bar\beta&\bar\alpha\end{pmatrix},
\qquad \det=N\alpha+N\beta=33.
$$
它在当前处整可逆，所以两个新输出同时深一层，恰好等价于
两个原 sigma 输入同时深一层。
原 sigma 核心给系数
$\lambda_\sigma^2=\lambda^2$；另一方面，
(8)、(10) 给系数 $\lambda^2\chi_p^2$。
$F\ne0$，例如 $F(z,0)=\alpha\beta z^2+\cdots$，
且 $\alpha\beta=-6\gamma_7$ 在当前处为单位。
消去同一非零缩放后，严格得到
$$
\boxed{\chi_p^2=1,\qquad \chi_p\in\{1,-1\}.}
\tag{13}
$$
这不是一个 norm 33 的单变量 sigma 锚，也没有选择需要的平方根。
$\chi_p$ 是 (8) 给出的实际符号。
例如可用 $S/\sigma=z^5+\cdots$ 将它准确记成
$[z^5]K_{33}(S/\sigma)$。

## 5. 同一个 D 正来源的完整斜轴核心

原 $W,Q$ 同时深和新 $Z,T$ 同时深是同一个整域。
R451 的原两个残余核心为 $-\lambda,\eta\lambda$，乘积为
$-\eta\lambda^2$。
用 (8) 和完整偶 degree $18480$ trace 比较，得
$$
K_{33}K_{18480}\widetilde{\mathcal L}_+
=-\eta\widetilde{\mathcal L}_+.
$$
代入整个 $K_{33}=\chi_pI$ 和 $\chi_p^2=1$：
$$
\boxed{
K_{18480}\widetilde{\mathcal L}_+
=-\eta\chi_p\widetilde{\mathcal L}_+.}
\tag{14}
$$
这支付的是同一实际来源的绝对核心，不仅是一个无中心的交织形状。

所以对任意 $r,s\ge0$，完整测度满足
$$
\boxed{
\nu_{\widetilde{\mathcal L}_+}|_{\{Z\in p^r,T\in p^s\}}
=(\chi_p\lambda)^r(-\eta\chi_p\lambda)^s
[\kappa^r,\kappa^s]_*\nu_{\widetilde{\mathcal L}_+}.}
\tag{15}
$$
原独立 sigma 输入 $c$ 可原样附在两边；
$T$ 限制保持整个 $Z,c$，特别保持 $Y=Z+c$ 和任意 $c$ 单位条件。
两个符号由同一个真实 trace 决定，未分别按需要选择。

由 (13)，新系数仍只是 $\lambda$ 的正负号。
故 R410 已付的 $1\pm\lambda$ 单位结论也统一适用于
$1\pm\chi_p\lambda$ 和 $1\pm\eta\chi_p\lambda$。
这项单位结论是在绝对平方付清之后才使用的。

## 6. 目标斜管的完整物理运输

仍保
$$
Y=Z+c,\qquad X=H-c,\qquad U=9Z-17H-280c.
$$
定义
$$
\boxed{
\mathscr H=U-280X=9T,\qquad
\mathscr J=U+17X=9(Z-33c).}
\tag{16}
$$
两者与 $(X,U)$ 的变换行列式为 $-297$，在当前处为单位；
反解为
$$
X=(\mathscr J-\mathscr H)/297,\qquad
U=(280\mathscr J+17\mathscr H)/297.
\tag{17}
$$

$T$ 的一层核心保持 $Z,c$，即保持 $Y,\mathscr J$，
并将 $\mathscr H$ 乘 $\kappa$。
在原物理坐标中，这个真实缩放是
$$
\boxed{
P_{\mathscr H}:
\begin{cases}
Y\mapsto Y,\\
X\mapsto X+(1-\kappa)\mathscr H/297,\\
U\mapsto U+17(\kappa-1)\mathscr H/297 .
\end{cases}}
\tag{18}
$$
它是深域上的规范化返回，逆映射只在相应像域使用。

因此同一个完整三输入测度有
$$
\boxed{
\nu_{\Phi_+}|_{\{\mathscr H\in p\}}
=-\eta\chi_p\lambda(P_{\mathscr H})_*\nu_{\Phi_+}.}
\tag{19}
$$
这保所有独立输出和原 sigma 条件，尤其保 $Y$ 本身；
不需要先将 $c$ 卷掉或忘掉第三输出。

## 7. 另一个正交轴及完整 principal 两轴返回

在 $(Z,T,c)$ 中，再取 $(Y,\mathscr J,\mathscr H)$。
完整 Gram 是
$$
\operatorname{diag}(34,90882,1496880),
$$
因为
$$
90882=81(33+33^2),\qquad1496880=81\cdot18480,
\qquad33\cdot9-297=0.
$$
两个 odd 半特征在 $Y$、$\mathscr J$ 轴各自成对抵消；
$\mathscr H$ 轴原本为偶。故这是完整无 twist 的整外积格。

原 $Z,c$ 同时深系数为 $-\chi_p\lambda^2$；
同一个域是 $Y,\mathscr J$ 同时深，且 $\mathscr H$ 保持。
整个 degree 34 核心是 R443 的 $R_Y$，所以
$$
\boxed{K_{\mathscr J}\Phi_+=-\chi_pR_Y\Phi_+.}
\tag{20}
$$
这是实际来源式，没有以 projective 相位代替绝对标量。
此处的 $R_Y$ 固定 $\mathscr J,\mathscr H$，
也即固定原 $X,U$，与 R448 的反射相同。

记 R451 的第一 principal 条件测度为 $\mathcal G_+(u)$。
由 (19)、(20)，在 $(\mathscr J,\mathscr H)$ 坐标中，
$$
\boxed{
\begin{aligned}
\mathcal G_+(u)|_{\mathscr H\in p}
 &=-\eta\chi_p\lambda[1,\kappa]_*\mathcal G_+(u),\\
\mathcal G_+(u)|_{\mathscr J\in p}
 &=-\chi_p\lambda[\kappa,1]_*\mathcal G_+(u).
\end{aligned}}
\tag{21}
$$
两个算子作用不同正交轴，故所有独立深度和完整环带都可依此返回。
其乘积为 $\eta\lambda^2$，与 R451 的原 $X,U$ 全深乘积吻合。

对常数测试，原总质量仍是 $-\frac23J_S(u)$。
因此
$$
\boxed{
\int_{\substack{Y\ {\rm unit}\\
\mathscr J\in p^r,\ \mathscr H\in p^s}}
\langle Y\rangle^{du}\,d\nu_{\Phi_+}
=-\frac23(-\chi_p\lambda)^r
          (-\eta\chi_p\lambda)^sJ_S(u).}
\tag{22}
$$
对应环带取相邻差，比例也是已付单位。
这是原算术零向目标斜轴深条件的真实传播；这里的测试没有额外
未运输的 $X^6$。

## 8. 原第二输出测试的准确剪切，保全部补域

对任意完整 $h(X)$，在 $\mathscr H\in p^n$ 上定义整规范输出
$$
X_n^\natural=\frac{\mathscr J-\mathscr H/\kappa^n}{297}.
\tag{23}
$$
其整数性来自显示的深域，不能把 $\kappa^{-n}$ 当作整个空间的
整自同构。由 (19)，准确有
$$
\boxed{
\int_{\substack{Y\ {\rm unit}\\\mathscr H\in p^n}}
 \langle Y\rangle^{du}h(X_n^\natural)\,d\nu_{\Phi_+}
=-\frac23(-\eta\chi_p\lambda)^nJ_S(u)
                                  \int h\,d\nu_{G_{18}}.}
\tag{24}
$$
所以原 $J'_S(0)=0$ 确实控制这条完整归一行。

若坚持原未归一 $X^6$，则必须保留完整转置：
$$
\boxed{
\int_{\substack{Y\ {\rm unit}\\\mathscr H\in p^n}}
 d\log\langle Y\rangle X^6\,d\nu_{\Phi_+}
=(-\eta\chi_p\lambda)^n
 \int_{Y\ {\rm unit}}d\log\langle Y\rangle
 \left(X+\frac{1-\kappa^n}{297}\mathscr H\right)^6d\nu_{\Phi_+}.}
\tag{25}
$$
右侧是同一个完整混合六次测试，不能只保其中的 $X^6$ 项。

原 R451 非零域为
$$
\mathscr D_n=\{Z,T\in p^n,\ c\ {\rm unit}\}
=\{X\ {\rm unit},W\in p^n,\mathscr H\in p^n\}.
$$
本篇的斜轴核心保 $Z,c$，所以其内部条件可以原样运输；
但 (24) 的规范测试与 R451 的原 $X^6$ 非零测试有 (23) 的真实差别。
无权测试的该管首项则含 R332 尚未证明非零的固定
$I_{\sigma,-5}$。因此不能把 (22) 的无权零与 R451 的加权非零
直接相认。

本篇付清了目标斜轴的完整真实核心和精确测试转置。
后续仍须用 (21)、(24)、(25) 在同一来源中处理 $W/V$ 深条件及
全部斜管内部补域；没有把新 scalar core 当作主目标完成。

## 依赖

- [R370：奇 degree 中心规范及两 sigma 全深定标方法](R370-original-degree-five-core-and-common-infinite-six-phase-primes.md)。
- [R413：原完整偶 degree trace 与整张量方法](R413-original-three-output-core-and-eight-source-central-return.md)。
- [R443：整个 degree 34 的真实反射核心](R443-original-residual-quarter-source-and-complete-central-return.md)。
- [R448：保独立伴随的真实反射](R448-original-retained-companion-reflection-and-joint-principal-carry.md)。
- [R451：同一 D 正来源及真实非零管](R451-original-dplus-source-and-complete-u-shell-zero-propagation.md)。
- [R332：固定负五次 sigma 矩的准确未付边界](R332-fixed-negative-original-moments-actual-soule-classes-and-reflected-root-signs.md)。

