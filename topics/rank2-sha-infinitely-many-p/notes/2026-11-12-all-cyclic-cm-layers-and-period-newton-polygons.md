# 全部循环 CM 同源层、周期 Newton 多边形与真实迹格

日期：2026-11-12。状态：本文给全层几何、估值和格的完整证明；
根端撰写，已由第二位研究者独立全文核验。
主目标的无穷素数非零性仍未由这些结论推出。

## 1. 实际对象和层的含义

沿用[一级真实邻点](2026-11-12-critical-gauss-period-map-and-canonical-neighbors.md)
的实际 Legendre 变形与晶体标记：
$$
t=\lambda-\tfrac12,\quad s=1-4t^2,\quad
Y=\begin{pmatrix}K&L\\K'&L'\end{pmatrix},\quad
KL'-K'L=1/s,\quad J=L/t,
$$
$$
K(0)=J(0)=1,\quad L'(0)=1,\qquad
F_0=\begin{pmatrix}0&pa\\b&0\end{pmatrix},\quad ab=-1.
$$
固定惰性 $p\ge7$。
$B/\mathbb Q_p$ 是含 $\mathbb Q_{p^2}$、原 prime-to-$p$ 级结构及规范常数
的有限非分歧域。原 CM 纤维的形式群是高度二的典范
$\mathcal O_{\mathbb Q_{p^2}}$ 模；与 $E_{17}$ 的既定同构只含好位单位。

对每个 $r\ge1$，只取循环子群
$H\subset E_0[p^r]$、$|H|=p^r$，置
$$
e_r=p^{r-1}(p+1),\qquad w_r=1/e_r,\qquad
\delta_r=\frac{p^r-1}{p^{r-1}(p^2-1)}.
\tag{1}
$$
子群数恰为 $e_r$：原始向量数 $p^{2r}-p^{2r-2}$ 除以
$\varphi(p^r)=p^{r-1}(p-1)$。
按原标记取 Serre 商 $q_H:E_0\to E_H$，
目标参数记为 $t_H$，$q_H^*\omega_H=c_H\omega_0$。
级结构和坐标符号与一级相同，商映射约化为第 $r$ 次 Frobenius。

循环限定不可删除。非循环子群会重复较低层，
例如阶 $p^2$ 的 $E[p]$ 给回典范点 $t=0$。

## 2. 挠点给出目标的准确 Newton 多边形

源的 exact $p^j$ 挠点均满足
$$
v_pZ(Q)=\frac1{p^{2j-2}(p^2-1)}.
\tag{2}
$$
源 $[p](Z)$ 首项为 $pZ$，约化为单位倍 $Z^{p^2}$，
故第一层 Newton 线段连接 $(1,1)$ 与 $(p^2,0)$。
在更小估值处 $Z^{p^2}$ 项严格主导，逐层原像把估值除以 $p^2$，得 (2)。

目标 $E_H[p]=[p]^{-1}H/H$ 中，若 $[p]R$ 是 $H$ 的生成元，
则 $R$ 为 exact $p^{r+1}$ 点，估值严格小于所有非零 $Q\in H$。
Serre 商 $q_H(Z)=\prod_{Q\in H}F(Z,Z(Q))$ 给
$$
v_pZ(q_HR)=p^rv_pZ(R)
=\frac1{p^r(p^2-1)}=:b_r.
\tag{3}
$$
这类点有 $\varphi(p^r)p^2/p^r=p^2-p$ 个。
余下 $p-1$ 个非零点组成 $[p]^{-1}(pH)/H$ 的一维
$\mathbb F_p$ 子群，单位整数乘法互传它们，故估值相同，记为 $a_r$。

目标 $[p](Z)/Z$ 的 Weierstrass 多项式次数 $p^2-1$，常数估值一，
所以根的估值总和为一。这给
$$
(p-1)a_r+(p^2-p)b_r=1,\qquad
a_r=\frac1{p-1}-\frac{p^{1-r}}{p^2-1}>b_r.
\tag{4}
$$
目标 Newton 多边形因此恰有顶点
$$
\boxed{(1,1),\quad(p,w_r),\quad(p^2,0).}
\tag{5}
$$
实际 Legendre $[p]$ 的 $Z^p$ 系数在原点为
$t\,v(t)+p\,h(t)$，$v(0)$ 是单位，
即标准 Hasse 多项式在 $t=0$ 的简单零点。
由 $w_r<1$，得到对实际参数的结论
$$
\boxed{v_p(t_H)=1/e_r.}
\tag{6}
$$

## 3. 完整轨道、局部 CM 阶和微分

$t_H$ 的 $B$-共轭仍来自这 $e_r$ 个子群。
(6) 的分母则迫使 $[B(t_H):B]\ge e_r$。
故所有参数互异，构成完整轨道，且该扩张完全分歧、次数恰为 $e_r$。

将源 Tate 模识别为 $\mathcal O=\mathbb Z_{p^2}$。
循环商的格经乘一个 $\mathcal O^\times$ 单位后为
$\mathcal O+p^{-r}\mathbb Z_p$；再乘 $p^r$ 得
$\mathcal O_r=\mathbb Z_p+p^r\mathcal O$。
其乘法自同态环正是 $\mathcal O_r$。
Yu §4 Theorem1 的局部环类域描述给
$$
B_r:=B(t_H)=B\cdot K_r,\qquad
\operatorname{Gal}(B_r/B)
\simeq\mathcal O^\times/
\bigl(\mathbb Z_p^\times(1+p^r\mathcal O)\bigr)
\simeq C_{p+1}\times C_{p^{r-1}}.
\tag{7}
$$
$K_r/\mathbb Q_{p^2}$ 的范数群为 $p^\mathbb Z\mathcal O_r^\times$。
最后的群结构来自 Teichmüller 部分与 $p\mathcal O$ 上的对数。
$r\ge2$ 时有野分歧，不能沿用一级的纯根表达 $B(\varpi)$。

由 Serre 商在原点的导数为全部非零核点参数的乘积，
$$
\boxed{v_p(c_H)=
\sum_{j=1}^r\frac{p^{j-1}(p-1)}{p^{2j-2}(p^2-1)}
=\delta_r.}
\tag{8}
$$
变到既定 Legendre 微分只乘整模型单位，不引入额外估值。

## 4. 所有周期零点都在这些层

水平晶体函子性给每个 $q_H$ 的实际水平矩阵准确为 $F_0^r$。
保持 Hodge 线即给
$$
\begin{array}{c|c|c}
r&\text{目标条件}&c_H\\ \hline
2k+1&K(t_H)=0&(-p)^kbL(t_H)\\
2k&L(t_H)=0&(-p)^kK(t_H).
\end{array}
\tag{9}
$$

穷尽性还需 period-map 纤维分类。
本题相同水平平凡化中的 period map 为 $[K:L]$；
原 CM 在 $t=0$ 两个基向量上的特征不同，
所以两坐标轴就是两个 CM 特征线。
与 Gross–Hopkins 的标准特征基比较只改两个非零常数尺度，
不改变这两个纤维。
Yu §11 印刷 p.312 明确指出，标准坐标纤维恰由相应奇偶类的
quasi-canonical 格点组成。
高度二时，每个格同似类都有唯一初等因子形状 $(0,r)$，
即本文的循环 $p^r$ 商。
故
$$
\boxed{
\begin{aligned}
\{K=0,\ |t|<1\}
&=\coprod_{r\ge1,\ r\ {\rm odd}}\{t_H:H\text{ 循环},\ |H|=p^r\},\\
\{J=0,\ |t|<1\}
&=\coprod_{r\ge2,\ r\ {\rm even}}\{t_H:H\text{ 循环},\ |H|=p^r\}.
\end{aligned}}
\tag{10}
$$
典范层 $r=0$ 是已从 $J=L/t$ 除去的原点。
Wronskian 保证全部根简单；不同层的估值不同，不含重复计数。

## 5. 全 Newton 多边形及原函数的非零极部

每个对应层有 $e_r$ 个估值 $1/e_r$ 的简单根，
所以每个 Newton 线段的垂直落差为一。
所有负斜率段的顶点准确是
$$
\boxed{
\begin{aligned}
K:\ &\left(\frac{p^{2k}-1}{p-1},-k\right),\\
J:\ &\left(\frac{p(p^{2k}-1)}{p-1},-k\right),
\qquad k=0,1,2,\ldots.
\end{aligned}}
\tag{11}
$$
第一顶点分别为 $(p+1,-1)$、$(p^2+p,-1)$。
$K$ 的第二负顶点是 $1+p+p^2+p^3$，不是 $p^3+1$；
此前可能负层的计数下界不能当作精确顶点。

奇层 $r=2k+1$ 与偶层 $r=2k$ 的另一周期满足
$$
v_pL(t_H)=\delta_r-k,\qquad
v_pK(t_H)=\delta_r-k,
\tag{12}
$$
与实际微分 (9) 一致。
原 $M_e=t^4m(t)$，$m(0)=1$、$m\in\mathcal O_B[[t]]$，
故所有层都有 $v_pM_e(t_H)=4/e_r$，从不为零。

在奇层，$E'=M_e/(sK)$ 的留数为
$$
\operatorname{res}_{t_H}E'\,dt=-L(t_H)M_e(t_H)\ne0,
\quad v_p\operatorname{res}=\delta_r-k+4/e_r.
\tag{13}
$$
在偶层，$I'=M_eK/(sL^2)$ 的二阶极部与留数分别是
$$
A_H=sM_eK^3(t_H),\qquad
R_H=sK^2(M_e'K+M_eK')(t_H).
\tag{14}
$$
两者也都非零。事实上偶层圆周上 $K$ 恰有唯一主导顶点
$a_k=(p^{2k}-1)/(p-1)\equiv1\pmod p$，
因此
$$
\frac{t_HK'(t_H)}{K(t_H)}\equiv1,\qquad
\frac{t_HM_e'(t_H)}{M_e(t_H)}\equiv4
\pmod{\mathfrak m_{B_r}}.
$$
和为单位 $5$，故
$$
v_pA_H=3(\delta_r-k)+4/e_r,\qquad
v_pR_H=3(\delta_r-k)+3/e_r.
\tag{15}
$$
特别，$r=2$ 的 $p(p+1)$ 个实际邻点是最近的全部 $J$ 根，
$I$ 在每点均有非零简单极部与对数项。
这里高层的 $I$ 指所写亚纯微分 $I'\,dt$ 的局部原函数，
不声称原点的 Taylor 级数能越过最近的 $J$ 根收敛。
完整迹可能配对消去这些项，单支非零不等于中央行非零。

## 6. 不同理想、野分歧迹与高 jet 格

记 $\Delta_r$ 为 $B_r/B$ 的不同指数，整数赋值规范为
$v_{B_r}(p)=e_r$。
非平凡角色中，第一层有 $e_1-1=p$ 个导子一角色；
第 $s\ge2$ 层新增 $e_s-e_{s-1}$ 个导子 $s$ 角色。
导子–判别式公式给
$$
\boxed{\Delta_r
=p+\sum_{s=2}^r s(e_s-e_{s-1})
=r e_r-1-\sum_{s=1}^{r-1}e_s.}
\tag{16}
$$
若 $\mathscr P_r$ 是 $t_H$ 的 Eisenstein 最小多项式，
则 $\mathcal O_{B_r}=\mathcal O_B[t_H]$，从而
$$
\boxed{v_p(\mathscr P_r'(t_H))
=\frac{\Delta_r}{e_r}
=r-\frac1{p-1}+\frac2{p^{r-1}(p^2-1)}.}
\tag{17}
$$

由逆不同理想的迹对偶定义，
$\operatorname{Tr}(\mathfrak m_{B_r}^j)\subset p^h\mathcal O_B$
等价于
$\mathfrak m_{B_r}^j\subset
p^h\mathfrak D^{-1}=\mathfrak m_{B_r}^{he_r-\Delta_r}$。
这里使用 $\mathfrak m_{B_r}^j$ 是 $\mathcal O_{B_r}$ 理想，
所以单个迹包含即同时控制乘所有整元后的迹。
对任意整数 $j$，准确得到
$$
\boxed{\operatorname{Tr}_{B_r/B}(\mathfrak m_{B_r}^j)
=p^{\lfloor(j+\Delta_r)/e_r\rfloor}\mathcal O_B.}
\tag{18}
$$
一级恢复 $\lceil j/(p+1)\rceil$；
一般 $\operatorname{Tr}\mathcal O_{B_r}=p^{r-1}\mathcal O_B$。
实际微分的整数估值为
$v_{B_r}(c_H)=(p^r-1)/(p-1)$；
带 $c_H^{-w}$ 的迹理想只须在 (18) 中把 $j$ 平移
$-w(p^r-1)/(p-1)$。

同理，$k$ 阶增厚的 Hasse-jet 映射
$\mathcal O_B[t]/\mathscr P_r^k\to\mathcal O_{B_r}^k$
的余核长度为 $\binom k2\Delta_r$：
采用 $\mathscr P_r^j t^i$ 基，对角块为乘 $\mathscr P_r'(t_H)^j$。
更深同源并不免费给一个同精度的迹格。

## 7. 来源及尚未支付的中央条件

- Jiu-Kang Yu, *On the moduli of quasi-canonical liftings*,
  Compositio Math.96(1995),293–321，
  [原文](https://www.numdam.org/article/CM_1995__96_3_293_0.pdf)：
  §3 Serre 商及标记；§4 Theorem1 的局部环类域；
  §11 印刷 p.312 的 period-map 同源判据和标准坐标纤维分类。
- 水平晶体与本题 $[K:L]$ 的识别沿用 R85 已核定的
  André, *Period mappings and differential equations*，
  [原文](https://arxiv.org/pdf/math/0203194)，
  II Lemmas6.1.3、6.2.5，不使用未经基变换核对的显式连接式。
- 导子–判别式的局部恒等式见 Milne,
  [*Class Field Theory*, v4.03](https://www.jmilne.org/math/CourseNotes/CFT.pdf)，
  V Theorem3.27，印刷 p.165；该定理明确指出乘积式归结为局部域的等式。
  单生成整格的迹对偶及不同生成元另见 Conrad,
  [*The Different Ideal*](https://kconrad.math.uconn.edu/blurbs/gradnumthy/different.pdf)，
  Theorems3.7、4.3 和 relative 版本 Remark4.26。
  本文 (18) 则直接从迹对偶定义证明，未另假设迹理想的大小。
- (2)–(6)、(8)、(11)–(15) 直接计算真实群、参数和原截面；
  (16)–(18) 保留局部类域的不同理想与迹对偶成本。

这些结论把全部同源层接回真实周期零点。
尚须将原 theta/Hecke 的准确关系放入这些格，
对中央 Hermite 行或 R77 的完整深度证书证明跨素数非零。
无权迹、单支真留数和 period map 非退化均不替代这个条件。
