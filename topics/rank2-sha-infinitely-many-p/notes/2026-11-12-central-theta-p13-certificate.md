# 中央 Kronecker 对角 d₁₂ 的精确 13-进证书

**状态：本笔记的有限环计算与轨道校准已证明并复算通过。**
日期：2026-11-12。

沿用 [中央 theta 对角笔记](2026-11-12-anticyclotomic-theta-diagonal.md)
的 $E:y^2=x^3-17x$、$f=34(1+i)$、$P_f=\Omega_E/f$、
固定 $256$ 点 Galois 轨道及其 $d_m$。
选定 $13$-进嵌入使
$$
i\equiv8\pmod{13},\qquad \pi=-3+2i,\qquad v_{13}(\pi)=1.
\tag{1}
$$

**结论。**
$$
\boxed{
d_{12}\equiv13351
=13^2+6\cdot13^3\pmod{13^4};
\qquad v_{13}(d_{12})=2.
}
\tag{2}
$$
而在完全不借旧 CLS 数值校准的原始轨道上，直接得到
$$
\boxed{
d_{12}^{\rm raw}\equiv20618
=5\cdot13^2+9\cdot13^3\pmod{13^4}.
}
\tag{3}
$$
四个可能轨道只相差 $\mu_4$ 单位，因此 (3) **自身已证明**
$v_{13}(d_{12})=2$。旧数值只确定 (2) 的准确单位方向。

这是新中央值
$L_{\mathfrak f}(\bar\psi^{25},13)$ 所对应的 Kronecker 系数，
不是旧的非中央值 $L(\bar\psi^{13},13)$。
中央值的计算没有使用预期非零、Sha 有限性或中央高度调节子。
该单个素数的证书不证明所需素数集合无穷。

脚本：
[check-central-theta-p13.py](../scripts/check-central-theta-p13.py)。
依赖 python-flint，本次环境版本为 0.9.0；全部运算精确，
没有浮点近似。两条提取算法对轨道中每个点都给出同一个值。

## 1. 准确的 Galois 轨道

记 $\lambda=1+i$。已有导子计算给出
$$
\mathfrak f=(\lambda^3)(17),\qquad
F=K(E[\mathfrak f]),\quad [F:K]=256,
$$
而 primitive $\mathfrak f$-division 点共有
$4\cdot16^2=1024$ 个。
Galois 作用在 $(\mathbb Z[i]/\mathfrak f)^\times$ 的像为
$$
\boxed{H=\langle-3,-2+i\rangle\cong C_{16}\times C_{16}.}
\tag{4}
$$

**证明。** 在惰性素数 $3$ 处，有限域 Frobenius 的平方为 $[-3]$，
故 $-3$ 属于 Galois 像。
直接点数给 $\#E(\mathbb F_5)=10$，所以 $a_5=-4$，
两个 CM Frobenius 为 $-2+i$、$-2-i$，故第二个生成元也在像中。
在 $17$ 的两个因子处分别取 $i=4,-4$。
以 $3$ 为 $\mathbb F_{17}^\times$ 的生成元，
两个元素的离散对数分别是
$$
-3:(9,9),\qquad -2+i:(14,7).
$$
行列式 $9\cdot7-9\cdot14=-63\equiv1\pmod{16}$。
所以它们的 $17$-部分已经生成大小 $256$ 的群。
已知整个 Galois 像的大小也是 $256$，故两者相等。
两个生成元在 $\mathfrak f$ 模下的阶确为 $16$，
亦由脚本在每行及全部行结束时的点和 $U$ 值闭合逐项核对。证毕。

因此任取 primitive 点 $S$，
$$
\mathcal S_S=
\{[(-3)^a(-2+i)^b]S:0\le a,b<16\}
\tag{5}
$$
就是一个完整的 Galois 轨道。
四个轨道由 $\mu_4$ 互相转换。为直接核对 $H\cap\mu_4=\{1\}$，
若一个 $H$ 元素在模 $17$ 下为 $-1$，
上面的可逆对数矩阵迫使 $(a,b)=(8,0)\pmod{16}$。
但 $(-3)^8\equiv1\pmod{\lambda^3}$，而
$-1\not\equiv1\pmod{\lambda^3}$，故 $-1\notin H$。
$\mu_4$ 的任一非平凡子群均含 $-1$，从而交确实平凡；
再用 $|H|\cdot|\mu_4|=1024$。
脚本实际生成 $256$ 个不同点，绝不对全部 $1024$ 点求迹。

## 2. 只用旧矩确定四次单位的方向

设
$$
\lambda_{13}(S)
=4\sum_{R\in\mathcal S_S}y(R)B_5(x(R)),
\tag{6}
$$
其中 $B_5$ 按 R6 的整数递推产生。
R19 的准确关系给
$\lambda_{13}(P_f)=\delta^{13}\log\Phi(O)$。
CLS II 的已勘误 Table I 给
$c_{13}^+(E)/13^2\equiv6\pmod{13}$。
由
$$
\lambda_{13}(P_f)
=-2 f^{13}12!\,c_{13}^+(E),\qquad
f\equiv7,\quad12!\equiv-1\pmod{13},
$$
可得
$$
\boxed{\lambda_{13}(P_f)/13^2\equiv6\pmod{13}.}
\tag{7}
$$
这个独立数值及规范在 R36 已核准；本次又直接查看了 CLS II
印刷页 19 的勘误段及页 20 的 $p=13$、case $17$ 表项。

对 $\epsilon\in\mu_4$，有
$$
U_{\epsilon S}=\epsilon^{-1}U_S,\quad
x(\epsilon S)=\epsilon^{-2}x(S),\quad
y(\epsilon S)=\epsilon^{-3}y(S).
\tag{8}
$$
赋 $U,X,Y$ 权 $1,2,3$，常数 $17$ 权 $4$；
中央公式中每项的总权为 $25-j$，而 $4\mid j$。
因此
$$
d_{12}(\epsilon S)=\epsilon^{-25}d_{12}(S)
=\epsilon^{-1}d_{12}(S).
\tag{9}
$$
旧矩的权为 $13$，也满足
$\lambda_{13}(\epsilon S)=\epsilon^{-1}\lambda_{13}(S)$。
故由 (7) 可唯一选择正确的 $\mu_4$ 轨道：
四个单位模 $13$ 彼此不同，且旧矩的已知首位非零。

本次未校准轨道给
$$
\lambda_{13}(S)\equiv29237\pmod{13^5},\qquad
\lambda_{13}(S)/13^2\equiv4\pmod{13}.
\tag{10}
$$
因为 $i\equiv8$ 且 $8\cdot4\equiv6$，应对 trace 乘 $i$；
等价地，将点轨道改为 $-i\mathcal S_S$。
同一个单位用于中央值，不能为中央值另挑方向。
在模 $13^5$ 环中
$$
i=228249,\qquad i^2+1\equiv0\pmod{13^5},
$$
校准后的旧矩为 $66924\pmod{13^5}$。
新中央值 (2) 从这一已确定的轨道独立算出。
若只需要赋值，跳过本节所有 CLS 输入，(3) 已足够。

## 3. 一个很小的无分歧模环足够

使用
$$
\begin{aligned}
g(A)={}&A^{16}+3A^8+12A^7+8A^6+2A^5\\
&+12A^4+9A^3+12A^2+6A+2.
\end{aligned}
\tag{11}
$$
脚本首先核验 $\bar g$ 在 $\mathbb F_{13}$ 上不可约，随后使用
$$
k=\mathbb F_{13}[A]/(\bar g),\qquad
\mathcal O_5=(\mathbb Z/13^5)[A]/(g).
\tag{12}
$$
$g$ 的判别式为 $13$-单位，所以第二个环是次数 $16$ 的无分歧
$13$-进整数环的模 $13^5$ 商。

令 $a_n=\pi^n+\bar\pi^n$，则
$a_0=2,a_1=-6,a_n=-6a_{n-1}-13a_{n-2}$。
所以
$$
\#E(k)=13^{16}+1-a_{16}
=665416610814412800,
\tag{13}
$$
其 $17$-赋值恰为 $2$。
先取横坐标 $A+s$，从 $s=1$ 递增，找到平方纵坐标后乘
$\#E(k)/17^2$。
脚本在 $s=2$ 得到一个 $R_{17}$，并直接检验
$$
[17]R_{17}=O,\qquad [4+i]R_{17}\ne O,\qquad[4-i]R_{17}\ne O.
\tag{14}
$$
它因此是 primitive $\mathbb Z[i]/(17)$-模生成元。

再取 $a^4=17$ 于 $k$，令
$$
Q=(ia^2,(1-i)a^3).
\tag{15}
$$
直接群法给 $[2]Q=(0,0)$，所以 $Q$ 的准确 CM 零化理想为
$\lambda^3$。于是 $S=Q+R_{17}$ 为 primitive $\mathfrak f$-点。
还分别核对两个点上的实际 Frobenius 方向：
$$
(x^{13},y^{13})=[-3+2i](x,y).
\tag{16}
$$

提升到 $\mathcal O_5$ 时，$a$ 用 $a^4-17$ 的 Newton 迭代提升，
$R_{17}$ 的横坐标用标准 $\psi_{17}$ 的单根 Hensel 提升，
纵坐标由曲线方程及原剩余符号唯一提升。
因 $17$-torsion 在 $13$ 处 étale，$\psi_{17}'$ 为单位；
脚本每次求逆都直接核验这一点。
提升后重新核验曲线方程、$[17]R_{17}=O$、
$[34]S=(0,0)$、$[68]S=O$。

整个环内逆元由剩余域逆元开始，以
$b\leftarrow b(2-ab)$ 三次迭代，得到模 $13^5$ 的准确逆元；
每个逆元又经 $ab=1$ 检验。
程序没有除以非单位，也没有靠浮点寻找 torsion 根。

## 4. 不展开 Ψ₆₉ 的准确 U 初值

记 $U_S=E_1^*(S)$。Weierstrass 加法公式直接给
$$
U_{P+Q}=U_P+U_Q+
\frac{y(Q)-y(P)}{x(Q)-x(P)}.
\tag{17}
$$
当 $P=Q$ 时最后一项改为
$(3x(P)^2-17)/(2y(P))$，正是通常的切线斜率。

从形式初值 $r_1=0$ 出发，用 (17) 的加法链递推
$$
U_{[n]S}=nU_S+r_n(S).
$$
因 $[34]S=(0,0)$，而这个非零二挠点的 $U$ 值为零，
$$
\boxed{U_S=-r_{34}(S)/34.}
\tag{18}
$$
它等于中央笔记中的
$-(\delta\log\Psi_{34})(S)/34^2$，
也等于 $\Psi_{69}$ 公式给出的初值。
这里不需要展开次数很高的 division polynomial。

计算只用单位斜率分母。
有关点均为 prime-to-$13$ torsion，约化单射；
出现分母为零仅可能是相加点互为正负或一个倍点为二挠，
而所选 $34$ 的加法链只在最后到达 $(0,0)$。
脚本的实际求逆检查同时提供逐步证书。

在 $H$ 的两个生成元之间继续用 (17)、(8) 传播 $U$，
并在三个不同轨道位置重新独立计算 (18)。
每条 $16$ 周期及整个双循环均检查 $(x,y,U)$ 完全闭合。
最终还得到
$$
\operatorname{Tr}_{F/K}U_S\equiv0\pmod{13^5},
\tag{19}
$$
与已证 $d_0=0$ 相符。

## 5. 两条不同的对角提取算法

第一条算法直接使用中央笔记式 (33)。
在
$\mathbb Z[U,X,Y]/(Y^2-X^3+17X)$ 中取
$$
\mathcal D U=-X,\quad
\mathcal D X=2Y,\quad
\mathcal D Y=3X^2-17,\qquad
C_{n+1}=\mathcal D C_n+UC_n,\ C_0=1.
$$
只需
$$
q_0=1,\quad q_4=\frac{17}{60},\quad
q_8=\frac{5491}{50400},\quad
q_{12}=\frac{50019253}{1297296000}.
\tag{20}
$$
每点的 $13d_{12}$ 贡献为
$$
W(S)=\frac1{12!}
\sum_{j=0,4,8,12}\frac{13q_j}{(13-j)!}
\left(\mathcal D^{12}C_{13-j}\right)(U_S,x(S),y(S)).
\tag{21}
$$
规范约化 $Y^2=X^3-17X$ 后，$W$ 有 $66$ 个非零单项式。
程序使用精确有理数生成其系数，再检验每个系数的分母与 $13$ 互素。

第二条算法不计算 $\mathcal D^{12}C_k$。
它在每个点直接递推微分系统的原始导数：
$$
\begin{aligned}
X_{n+1}&=2Y_n,\\
Y_{n+1}&=3\sum_{j=0}^n\binom nj X_jX_{n-j}
-17\,\mathbf1_{n=0},\\
U_{n+1}&=-X_n,\qquad
F_{n+1}=\sum_{j=0}^n\binom nj U_jF_{n-j},\quad F_0=1.
\end{aligned}
\tag{22}
$$
这里 $F_n=F_S^{(n)}(0)$。只计算到 $n=25$。
再令 $b_\ell=[z^\ell]F_S(z)^{-1}$，只需 $\ell\le12$，
由普通级数乘法得到 $b_\ell$。
直接从
$\Theta_S(z,w)=F_S(z+w)/(F_S(z)\sigma(w))$ 提取，给
$$
\boxed{
W_{\rm jet}(S)=
\sum_{j=0,4,8,12}\frac{13q_j}{(13-j)!}
\sum_{\ell=0}^{12}
\frac{F_{13-j+\ell}}{\ell!}\,b_{12-\ell}.
}
\tag{23}
$$
这条公式没有 (21) 的外层 $12!$，因为此处已直接提取普通
$z^{12}$ 系数；把它再除 $12!$ 会改变答案。

两算法在全部 $256$ 个点逐点核对
$$
W_{\rm jet}(S)=W(S)\quad\text{于 }\mathcal O_5.
\tag{24}
$$
这同时检查了微分规范、两个方向的系数提取及阶乘的位置。

## 6. 模 13⁵ 为什么给出 d₁₂ 模 13⁴

在 (21) 或 (23) 中，潜在的 $13$ 分母只有
$13!$ 和 $q_{12}$ 各自的一层。
预先乘的 $13$ 消去每项的这一个分母。
其余阶乘至多为 $12!$，都是单位；
第二算法中的 $F^{-1}$ 也只计算至第 $12$ 项。
因此两算法均在 $\mathcal O_5$ 内完成，没有中间精度损失。

轨道求和后，所有 $A,\ldots,A^{15}$ 的系数均严格为零，
所以该和下降到基环 $\mathbb Z/13^5$。
校准单位后得到
$$
\boxed{
\sum_{S\in\mathcal S}W(S)
\equiv173563=13\cdot13351\pmod{371293}.
}
\tag{25}
$$
此时才进行一次普通整数除以 $13$，
得到 $d_{12}$ 模 $13^4$，即 (2)。
这一步的除法不是在 $\mathcal O_5$ 中求 $13$ 的逆元。
若不校准，完全相同的计算输出 (3)，已独立给出准确赋值。

脚本主要输出为：

| 项目 | 精确输出 |
|---|---:|
| 模数 $13^5$ | $371293$ |
| 轨道点数 | $256$ |
| $\operatorname{Tr}U$ 模 $13^5$ | $0$ |
| 未校准中央值模 $13^4$ | $20618$，赋值 $2$ |
| 未校准旧矩模 $13^5$ | $29237$ |
| 未校准旧矩除 $13^2$ 模 $13$ | $4$ |
| 校准单位 | $i\equiv228249\pmod{13^5}$ |
| 校准后旧矩除 $13^2$ 模 $13$ | $6$ |
| 两条算法逐点一致 | 全部 $256$ 点 |
| $d_{12}$ 模 $13^4$ | $13351$ |
| 四位 $13$-进数字，从低到高 | $(0,0,1,6)$ |

## 7. 这个证书落实了什么

它验证了新中央对角确实能用固定代数微分系统、准确角色轨道及有限模环
算出，并给出首个非零主层 $d_{12}/13^2\equiv1\pmod{13}$。
因此中央笔记的插值比较一经采用，$p=13$ 满足其第一权门槛。
旧矩的数值只确定单位轨道，没有给中央值输入任何期望余数。
所需无穷性仍须控制 $d_{p-1}$ 随 $p$ 的行为；
本证书不将一个有限例子扩展为该结论。

## 来源与可复算依赖

- 本仓库 [中央 theta 对角笔记](2026-11-12-anticyclotomic-theta-diagonal.md)，
  式 (12)、(14)、(15)、(29)–(33)，给所计算对象的完整定义。
- [R6](../results/R6-cm-trace-recurrence.md)、[R19](../results/R19-fixed-rational-logarithmic-moments.md)，
  给旧整数矩的准确规范。
- [R36](../results/R36-two-bockstein-functionals-and-a-nonzero-value.md)，
  $p=13$ 的旧矩、周期和原始 CLS 数值核对。
- Coates–Liang–Sujatha，
  *The Tate–Shafarevich group for elliptic curves with complex multiplication II*，
  Milan J. Math. **78** (2010)，395–416，§4 式 (77) 后的勘误及 Table I，
  [作者全文](https://arxiv.org/pdf/1005.4206)。
  用于 (7) 的只有已更正 $p=13$、case $17$ 的旧非中央表项 $6$。
- [精确计算脚本](../scripts/check-central-theta-p13.py)；
  剩余域定义多项式、点的完整剩余坐标、Hensel 提升和两套对角递推均在其中，
  可独立运行，不需要 Sage、Magma、完整复周期或外部数据库。
