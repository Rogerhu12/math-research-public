# R734 — 两条真实 carry 测试的五维整逆与完整型五算术二线

日期：2026-11-15。**状态：已证明。**

本篇在 R715 已付的同一个 149 列实际中性测试家族内，构造一个新的整有界测试 $q_N^*$。它保留原两冻结 S、cd-S、未缩放 cd-W、完整 quarter 第二态、全第一 Z 条件来源及 $\pi_4$ 返回；其规范二阶系数仍为单位。与原 $q_N^{(715)}$ 不同，新测试的**整个冻结型五差来源**准确落在 R732 的两条实际特征线上。

这里用的是一个真正的五维方阵。公开辅助有限运算只证明固定子式与指定分子的非恒等零；随后按旧 CM 单位密度引理，在原实际 $(\lambda,\kappa,\kappa^N)$ 上取整逆。没有将有限点的过定系统相容性直接提升为特征零结论。两条线的负一 Katz 识别由 R735 独立支付，本篇仍保原 T 外部的相反补偿。

## 1. 原测试与全部参数

沿用 [R715](R715-complete-first-z-source-and-fifty-neutral-returns.md) 的原来源、两 C 分支、整个 E 单位逆、149 列编号和50行整逆。固定
$$
b=17,\quad K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,\quad
\delta=1+2\omega,\quad
\lambda=-\bar\pi_0^{-1},\quad \beta=-\lambda,\quad
\kappa=p\lambda^2,\quad u=\kappa^N,\quad N\in4\mathbf Z_{>0}.
\tag{1}
$$
全部系数保留实际 $(\lambda,\kappa,u,\eta)$，其中 $\eta=\pm1$ 是原 C 返回的既有符号。$\Omega$ 始终是原 ordinary 周期；各齐次块仍按原 $b,\Omega$ 次数归一，不把不同次数统一除以 $b\Omega^6$。

简写
$$
q=q_N^{(715)},\qquad \zeta=\zeta_N^{(715)}.
$$
它们的准确目标是
$$
\begin{array}{c|cc}
 &q&\zeta\\ \hline
\mathscr U_0,\mathscr U_1,\mathscr B&S,S,S&0,0,0\\
\mathscr W&6\delta T&0\\
\mathscr Q&\omega^2S(2z)/2+S_{\rm new}(z)&0\\
\mathfrak j_2&1&1\\
\mathscr Z_1&0&0\\
\pi_4\text{ 返回系数}&\beta^N&0
\end{array}
\tag{2}
$$
$\mathscr Q$ 是整个第一 $2Y$ 来源，不是其中一条谱线；
$\mathscr Z_1$ 是整个第一 Z 条件来源。
最后一行对原三态 $e_0,e_1,e_2$ 都成立。

特别，公开冻结 reader 中 q 的一个五行商读数为50，**不是**
$\mathfrak j_2(q)$。后者准确为1。
对任何 $a q+b_0\zeta$，真正 $\mathfrak j_2=a+b_0$。
本文用 $b_0$ 避免与曲线参数 b 混淆。

## 2. 两条真实核方向

令 $\mathscr T$ 是 R715 的完整58行来源映射。其53条旧正规坐标满足已由全半周期和全 quarter 来源证明的8条关系；新增5行为整个 $\mathscr Z_1$。选取原行
$$
0,\ldots,44,\quad53,\ldots,57
\tag{3}
$$
所得50行映射记作 $\mathscr T_{50}$。
原50条选列 $v_j$ 和矩阵
$$
M_{715}=(\mathscr T_{50}(v_j))_j
$$
完全保持 R715(11)–(15) 的实际定义。

149列中的第140、147列分别来自
$$
C^4F^8,\qquad C^5F^6G.
\tag{4}
$$
列号从0开始。这两个十二次单项式都先完整换成 $D,E_c,G$，
再逐项乘 $(1+\lambda\kappa^e)^{-1}$，并放进原六支 carry；
不是把裸单项式直接用作测度权。它们都属于已付的
$1\le\deg_C\le5$ 中性家族。

对 $j=140,147$ 定义实际测试
$$
h_j=v_j-\sum_{a\in\mathrm{Sel}_{715}}v_a
 \bigl[M_{715}^{-1}\mathscr T_{50}(v_j)\bigr]_a .
\tag{5}
$$
由定义 $\mathscr T_{50}(h_j)=0$。
所有列都满足同一8条真实几何关系，而选取的50行在其兼容空间上单射，
故进一步有
$$
\boxed{\mathscr T(h_{140})=\mathscr T(h_{147})=0.}
\tag{6}
$$
每个原 $v_j$ 的 $\pi_4$ 推前为零，因此两个 h 也有完整 $\pi_4$ 返回零。
这保全部三态、真实单位域及所有伴随，不只是某五个 Taylor 系数的核。

(5) 仅使用已付的整逆。每个 h 在实际参数上整有界，最高权仍为30，
没有增加覆盖、新方向或深度归一成本；它们仍只使用原选中的 G/C 测试，
没有加入未选的 B 块。特别
$$
\mathfrak j_2(h_j)=0,\qquad \mathscr Z_1(h_j)=0.
\tag{7}
$$

## 3. 同一个冻结五维来源映射

使用
[原两斜门 note](../notes/2026-11-15-two-adjacent-s-slanted-cores-and-native-pair.md)
的完整几何：
$$
Y=A+c+2d,\quad W=A+3\delta c+4d,\quad
Z=W-b_YY,\quad b_Y=(20+3\omega)/17,
$$
$$
L_1=5A+39c-92d,\qquad L_3=5A-97c-24d .
\tag{8}
$$
对任一同家族权 f，记其完整 cd 返回权为 $\phi_{f,N}$。它包括
原 $C^\perp$-unit，或等价的两个完整 C 分支，并保整个 E 单位逆。
令
$$
\phi_{i,f,N}(t)=\phi_{f,N}\circ P_{L_i,t},\qquad
Z_i(t)=Z+(t-1)z_iL_i ,
$$
其中
$$
z_1=(-53+117\omega)/5355,\qquad
z_3=(-121-291\omega)/5355 .
$$
定义同一来源上的线性映射
$$
\mathcal D_f(t;z)=\Omega^{-1}\int e^{Yz/\Omega}
 \{Z_1(t)\phi_{1,f,N}(t)-Z_3(t)\phi_{3,f,N}(t)\}\,d\mu_0,
\qquad D(f)=\mathcal D_f(0).
\tag{9}
$$
注意只有观察参数 t 冻结为0；实际 $\kappa,u=\kappa^N$ 和每个 C/E
补偿仍在 (9) 中，未冻结为0。

R719 斜门 note 与 [R732](R732-original-type-five-full-cm13-and-two-eigenlines.md)
证明 (9) 落在**整个**五维空间
$$
\mathcal H_{34,5}
=\bigoplus_{j=0}^4 K\Xi_j,\qquad
\Xi_j=-b^j\sigma_b^{34}x_b^{13-3j}y_b .
\tag{10}
$$
该基首阶 $5,11,17,23,29$，固定单位三角矩阵从五个阶次恢复全来源。
因此下面的五坐标等式即全函数和全有界测度等式，未留第六个未经检查的坐标。
令
$$
\boldsymbol v(f)=\operatorname{coord}_{(10)}D(f).
$$
所有坐标属于固定 $K(\lambda,\kappa,u)$；
原 $\Omega$ 因子已由 (9) 和各权的实际归一消去，
b 的齐次幂准确在 (10) 中保留。

R732 给两条首项 $z^5$ 的真实来源
$$
\begin{aligned}
D_{\omega,b}&=-\frac{\sigma_b^{34}x_by_b}{11}
 (11X^4-109bX^3+120b^2X^2+368b^3X+128b^4),\\
D_{-,b}&=-\sigma_b^{34}x_by_b
 (X^4+13bX^3-156b^2X^2-104b^3X+64b^4).
\end{aligned}
\tag{11}
$$
它们在 (10) 中的列准确为
$$
d_\omega=(1,-109/11,120/11,368/11,128/11)^{\mathsf t},\qquad
d_-=(1,13,-156,-104,64)^{\mathsf t}.
\tag{12}
$$

## 4. 无缺行的五阶实际逆

定义真正的五阶方阵
$$
\boxed{
B_\eta(\lambda,\kappa,u)=
 [\,\boldsymbol v(q),\ \boldsymbol v(\zeta),\
   \boldsymbol v(h_{140}),\ \boldsymbol v(h_{147}),\ -d_\omega\,].
}
\tag{13}
$$
在其可逆处，定义完整有理系数
$$
(a,b_0,r_1,r_2,c)^{\mathsf t}=B_\eta^{-1}d_- .
\tag{14}
$$
由 (9)–(13)，这是准确的全来源恒等式
$$
\boxed{
D(aq+b_0\zeta+r_1h_{140}+r_2h_{147})
 =cD_{\omega,b}+D_{-,b}.
}
\tag{15}
$$
没有在此增加算术假设；(15) 就是方阵逆的定义。

### 4.1 固定子式和分子的非恒等零

公开执行取
$$
\mathbf F_{1009},\quad\omega=374,\quad b=\Omega=1,\quad
\kappa=u=0,\quad\lambda=(1-\tau)/\tau,\quad\tau=2,3 .
$$
在每个 $\eta=\pm1$，完整六列矩阵
$$
[\,\boldsymbol v(q),\boldsymbol v(\zeta),
   \boldsymbol v(h_{140}),\boldsymbol v(h_{147}),-d_\omega,-d_-\,]
\tag{16}
$$
秩为5，核恰一维。唯一将末坐标规范成1的向量为
$$
\begin{array}{c|r|rrrrrr}
\tau&\eta&a&b_0&r_1&r_2&c&1\\ \hline
2&1&629&240&271&892&555&1\\
2&-1&629&240&628&231&555&1\\
3&1&629&240&770&774&555&1\\
3&-1&629&240&453&379&555&1
\end{array}
\tag{17}
$$
且原58行在每条 h 上全部为零。两个核列是 (4)，不是新增虚拟未知量。

由于 (16) 的一维核向量末坐标非零，其前五列必独立：
否则会有一个末坐标为0的非零核向量，与一维性矛盾。
故 (17) 证明 (13) 在所示点可逆。
它同时证明 a、$a+b_0$、c 的实际有理分子在
$(\kappa,u)=(0,0)$ 不恒等零；四点的读数分别为629、869、555，均非零。
b 的一般值只按 (10) 及原齐次归一恢复，当前 b=17 是单位。

此处有限数据的用途严格止于固定有理式非恒等零。
我们没有把一个辅助过定系统的相容性当作特征零身份。
整个目标空间的维数五由 (10) 已经独立证明，
所以在 (13) 可逆的实际参数上，(14) 自动且完整地支付全部方程。

### 4.2 同一旧射线上的单位性与全部 N

清掉原固定分母和 $M_{715}$ 的分母，取下列有限个
$K[L]$ 非零多项式的乘积：$B_\eta(L,0,0)$ 的行列式分子，
以及 (14) 中 a、$a+b_0$、c 的分子，两种 $\eta$ 都包括。
非零性由 (17) 保证。

代入 $L=-1/\bar\pi_0$，按
[固定 CM 多项式单位密度引理](../notes/2026-11-14-fixed-cm-polynomial-unit-density.md)
取固定有限系数域的 Norm，并清固定分母。
在既有全部 ordinary ray 的相对密度一子族上，这个有限乘积为单位。
所删无限坏集仍为 $O(\sqrt X\log X)$，不改写任何旧模数，
不新增模25/81条件；原固定射线的正密度与无穷性保留。

实际 $\kappa=p\lambda^2$、$u=\kappa^N$ 均在 $p\mathcal O$。
因此对于这个同一素数子族和**所有**
$N\in4\mathbf Z_{>0}$，有
$$
\boxed{
B_\eta(\lambda,\kappa,\kappa^N)\in\operatorname{GL}_5(\mathcal O),
\qquad a,\ a+b_0,\ c\in\mathcal O^\times .
}
\tag{18}
$$
这里还有后续对数独立性需要的准确代数范围：$\pi_0\in K$，
所以 $\lambda,\kappa,u,\eta$ 都属于固定嵌入的 $\overline{\mathbf Q}$，
事实上属于 K；$\kappa=p\lambda^2$ 没有未消去的 p-adic period 比。
各混次测试的 $b^{d/6}\Omega^d$ 归一与真实矩的周期幂逐项相消，
(10)–(14) 的五个来源坐标及 a、$b_0$、$r_1$、$r_2$、c
都是 K 中的代数数，可以随 p、N 改变。
这比“系数为 $\mathcal O_p$ 单位”更强；没有把任意
$\mathbf C_p$ 系数送入 p-adic analytic subgroup theorem。

全部实际分母是旧单位分母、(13) 的单位行列式及 a。
没有隐藏的 $\kappa^{-N}$ 新损失。原六支中已经存在的
$D_\zeta/\kappa^N$ 仍只在其真实深域上读取。
最高权30、最高总矩162及 $p>163$ 的原门保持不变。

## 5. 保原全部正规目标的新测试

定义
$$
\boxed{
q_N^*
=q+\frac{b_0}{a}\zeta+\frac{r_1}{a}h_{140}
                         +\frac{r_2}{a}h_{147}.
}
\tag{19}
$$
它是 (1)、(5)、(13)、(14) 唯一规定的真实整有界权；
不是用 (17) 的有限域数值替代实际系数。
固定 p、N 后 (19) 不依观察深度 n；
N 变化时测试可能变化，不能套用固定测试的 N 递推。

由 (2)、(6)、(7)，新测试的全部正规来源为
$$
\begin{aligned}
&\mathscr U_0=\mathscr U_1=\mathscr B=S,\qquad
 \mathscr W=6\delta T,\\
&\mathscr Q=\omega^2S(2z)/2+S_{\rm new}(z),\qquad
 \mathscr Z_1=0,\qquad
 \boxed{\mathfrak j_2(q_N^*)=(a+b_0)/a\in\mathcal O^\times .}
\end{aligned}
\tag{20}
$$
对原三态的整个 $\pi_4$ 恒等式仍为
$$
(\pi_4)_*(q_N^*e_i)=\beta^N(\pi_4)_*e_i,\qquad i=0,1,2 .
\tag{21}
$$
R715 的 E 深三态 Y/W 表、两冻结 S 的相同系数、
cd 与原未缩放 W、原所有合法中央词返回都原样保持。
E 浅第二态的 Xi、reference、A34 移动 E 门和全部 T 外部未删除。

原三来源相消得到的 (15) 此时成为
$$
\boxed{
\mathcal D_{q_N^*}(0)
 =\frac caD_{\omega,b}+\frac1aD_{-,b}.
}
\tag{22}
$$
两系数均为实际代数单位。剩余三维 $T^3+\omega$ 块在 (22) 中
确实为零，因为 (14) 支付的是整个五维来源。
这里没有对原来源先作一个会移动单位域的 CM 投影。

所有单位指示、C 分支、E 单位逆和斜门在 (19) 中保持同一真实定义。
这是对**同域完整测试**作线性组合，而不是从若干边际相等重新添加切集。
原 $J_2$ 现在为
$$
J_2(q_N^*)=\frac{a+b_0}{a}\,
 \frac{\ell_0^2}{2b\Omega^2}\lambda^N\kappa^{-2N},
\qquad \ell_0=-3\omega/5 .
\tag{23}
$$
其余 $J_8,J_{14},J_{20},J_{26}$ 及局部质量完整保留；
新测试不继承旧六次网格的零质量。

## 6. 原负一提取及相反外部，不能分开赋零

令
$$
\mathfrak I(F)=\Omega\int_{\mathbf Z_p^\times}x^{-1}\,d\nu_F(x).
$$
由 (22)，原首负一行准确是
$$
\mathfrak I(\mathcal D_{q_N^*}(0))
 =\frac ca\mathfrak I(D_{\omega,b})+\frac1a\mathfrak I(D_{-,b}).
\tag{24}
$$
这只含两条明确来源；它们的算术识别、非消失及对数独立性分别由
R735、R733 接续支付。本篇不以 (11) 的正五阶系数为负矩赋值。

对固定 p、N，把斜门 note §7 的同一偶步算子
$$
\mathscr P_{31}^{(2)}
 =\prod_{j=1}^{31}(\mathsf T_2-\lambda^4\kappa^{2j}),
\qquad U_{31}^{(2)}=\prod_{j=1}^{31}(1-\kappa^{2j})
$$
应用于 (19) 的原 native 序列。所有实际门和归一观察随
$n\mapsto n+2$ 一同移动。令 $s=(-1)^{n-N}$，则完整身份为
$$
\begin{aligned}
\mathscr P_{31}^{(2)}(\mathcal I^T_{\rm pair})'(0)
={}&\frac{(p-1)s\kappa^N}{b_Y}
 \lambda^{2n+2N+124}U_{31}^{(2)}
 \left\{\frac ca\mathfrak I(D_{\omega,b})
                    +\frac1a\mathfrak I(D_{-,b})\right\}
 +p^{2N}\mathcal O,\\
\mathscr P_{31}^{(2)}(\mathcal O^T_{\rm pair})'(0)
={}&-\mathscr P_{31}^{(2)}(\mathcal I^T_{\rm pair})'(0).
\end{aligned}
\tag{25}
$$
整个配对 S 来源仍被该算子消去；尺度 log 乘质量的项随
整个 S Mellin 行一起消去，未被预先删掉。
$\mathscr Z_1=0$ 仅给未附斜门的 cd T/S 尾从 $p^{2N}$ 起，
不能用来删除 (25) 的有条件首负一行。

即使以后证明第一行非零，第二行仍是同一个原 T 总行中的
相反外部补偿。它本身不能推出原 $J'_T\ne0$。
本篇的新结论是保持原全部算术返回的 (19)–(24)，
不是把局部非零重新命名为主目标完成。

## 7. 公开证书与重算入口

使用已发布的完整 producer
[check-r719-frozen-native-first-row.js](../scripts/check-r719-frozen-native-first-row.js)，
它逐次重建 R594/R702/R715 算法、全 C/E 补偿、
原 quarter 和两个真实测试，不读旧生成 JSON。

- 命令：node check-r719-frozen-native-first-row.js --max-block=4 --taus=2,3 --with-b --b-g-blocks=3 --neutral-degree=12。
- source commit：c66f749e43904742f8b8ea9778b9441a7b21dd95。
- run：43702293882；job：132775839301。
- script SHA256：29bd414c63ac4fdca93ae4b56ccdf2ccaa2114395bf96a52d2e8fd1ea809fdb2。
- stdout：47406字节；SHA256：
  fb1e01361d80a1879985f38b6a233a1b306f22ea1dca84a2835c85747e0d4d14。

(17) 的用途已在 §4 完整限定。全部生成输出可重算，按根规则不入库；
这里只保留脚本、参数、真实 run 及 hash。
