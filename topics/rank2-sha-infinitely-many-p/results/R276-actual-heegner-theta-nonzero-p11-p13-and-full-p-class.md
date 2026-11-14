# R276：原 Heegner theta 的两个实际非零素数与完整 $11$ 类群二阶矩

日期：2026-11-13。**状态：完整有限证明。固定 E389 的两个素数
$11,13$ 已由原 Heegner 两矩给出非零证书；未证明无穷素数。**

本篇直接计算 R234/R271 的实际 definite theta 元素，不以
任意非零 quaternion 本征函数代替原 CM 全和。全部 CM 标签、
模 Hecke 本征线、局部 torus 标号和类群 Artin 作用均明确给出。
计算只用有理数和有限域，不用 Heegner 点浮点近似或猜测有理重构。

## 1. 结论和固定曲线

固定
$$
 E:y^2+y=x^3+x^2-2x,\qquad N_E=\Delta_E=389.
\tag{1}
$$
R2/R136 已证明该曲线非 CM、根数为 $+1$、代数秩至少二。
本文证明以下三个实际来源。

| $p$ | 观察 $q$、符号 $\epsilon$ | $D_F$ | 原 $\ell$ | $h_F$ | 全部 CM 标签数 | 实际低矩 |
|---|---|---|---|---|---|---|
| $11$ | $13,-1$ | $-7$ | $131$ | $1$ | $132$ | $(m_0,m_1,m_2)=(0,0,4)$ |
| $13$ | $7,+1$ | $-11$ | $233$ | $1$ | $234$ | $(m_0,m_1,m_2)=(0,4,8)$ |
| $11$ | $13,-1$ | $-1307$ | $43$ | $11$ | $484$ | 全 $C_{11}^2$ 一次项为零，二次矩阵为 $\left(\begin{smallmatrix}8&8\\8&0\end{smallmatrix}\right)$ |

矩在 $\mathbb F_p$ 中，使用下文唯一确定的本征函数规范。
若改变原参数化到局部线的基，它们只同时乘一个非零标量。
第一行证明原完整迹的第二矩非零，故原指数 $a\le1$；
第二行的第一矩非零，甚至给 $a=0$。
第一行不单凭一个负号观察宣称 $a=1$。

第三行保留全部 $11$ 类群标签。规范化真实分歧商由
$b\in\mathbb F_{11}$ 标记，其第二矩准确为
$$
                         m_2(b)=4+8b.
\tag{2}
$$
因此十个商非零、只有 $b=5$ 这个商的二阶项为零。
这给 R271 联合忠实性一个实际算术实例，也说明固定一个商
和保留所有真实商并非同一个测试。

结合 R271 的整个通常 Selmer 两步判据，得到
$$
 \boxed{\quad
 \operatorname{rank}E(\mathbb Q)=2,\qquad
 \Sha(E/\mathbb Q)[11^\infty]=
 \Sha(E/\mathbb Q)[13^\infty]=0.
 \quad}
\tag{3}
$$
这里不是依据数据库的 analytic Sha 数值。所用非零输入是
本篇逐标签构造的实际 theta 系数。

可重现的完整算术证书见
[脚本](../scripts/check-actual-heegner-theta-p11-p13-and-p-class.py)、
[输出](../scripts/check-actual-heegner-theta-p11-p13-and-p-class.json)。
61 项精确检验全部通过；输出保存稀疏 Hecke 算子、完整本征函数、
非零秩子式、全部 CM 标签和完整群环系数，没有提交大稠密矩阵。

## 2. 两个最大整环及真实有限 Shimura set

### 2.1 判别式 $13$

取
$$
 B_{13}=\left(\frac{-2,-13}{\mathbb Q}\right),\qquad
 i^2=-2,\quad j^2=-13,\quad k=ij=-ji,
$$
以及基
$$
 e_1=1,\quad e_2=i,\quad
 e_3=\frac{1+i+j}{2},\quad e_4=\frac{2+i+k}{4}.
\tag{4}
$$
该基的整数格记为 $\mathcal O_{13}$。写
$v=a e_1+b e_2+c e_3+d e_4$，则
$$
 \begin{aligned}
 \operatorname{nrd}(v)
   &=a^2+2b^2+4c^2+2d^2+ac+ad+2bc+bd+cd,\\
 \operatorname{trd}(v)&=2a+c+d.
 \end{aligned}
\tag{5}
$$
十六个基乘积均在该整数格中；完整乘法表存于证书。
其 trace Gram 矩阵为
$$
 \begin{pmatrix}
 2&0&1&1\\
 0&-4&-2&-1\\
 1&-2&-7&0\\
 1&-1&0&-3
 \end{pmatrix},
 \qquad |\det|=13^2.
\tag{6}
$$
$B_{13}$ 在 $13,\infty$ 分歧：在 $13$ 的 Hilbert 符号是
$(-2/13)=-1$；在 $2$ 的符号指数为
$7+21=28$，故为 $+1$；其他有限位均为 $+1$。
所以 (6) 表明 $\mathcal O_{13}$ 为最大整环。

全部范数一单位为 $\{\pm1\}$。范数 $2,3$ 元素模左单位的
完整代表分别为
$$
 \begin{array}{c|l}
 2&(0,0,0,1),\ (0,1,0,0),\ (1,0,0,-1)\\
 3&(0,1,0,-1),\ (1,-1,0,0),\
                (1,1,0,-1),\ (1,1,0,0).
 \end{array}
\tag{7}
$$
坐标始终相对于 (4)，不是相对于 $1,i,j,k$。

### 2.2 判别式 $7$

取
$$
 B_7=\left(\frac{-1,-7}{\mathbb Q}\right),\qquad
 e_1=1,\ e_2=i,\ e_3=\frac{1+j}{2},\
 e_4=\frac{i+ij}{2}.
\tag{8}
$$
相应最大整环 $\mathcal O_7$ 上
$$
 \operatorname{nrd}(a,b,c,d)=a^2+b^2+2c^2+2d^2+ac+bd,\qquad
 \operatorname{trd}(a,b,c,d)=2a+c.
\tag{9}
$$
全部基乘积整，trace Gram 矩阵为
$$
 \begin{pmatrix}
 2&0&1&0\\
 0&-2&0&-1\\
 1&0&-3&0\\
 0&-1&0&-4
 \end{pmatrix},
 \qquad |\det|=7^2.
\tag{10}
$$
Hilbert 符号给分歧集 $\{7,\infty\}$，故此环最大。
单位群为 $\{\pm1,\pm i\}$。模左单位的范数 $2,3$ 代表为
$$
 \begin{array}{c|l}
 2&(-1,-1,0,0),\ (-1,0,1,0),\ (0,0,-1,0)\\
 3&(-1,-1,0,1),\ (-1,-1,1,0),\
               (-1,0,0,-1),\ (-1,0,0,1).
 \end{array}
\tag{11}
$$

### 2.3 类数一的直接证明

在约化范数定义的四维 Euclidean 空间中，两环的 covolume
均为 $q/4$，其中 $q=7,13$。对任意局部主右理想 $I$，
covolume 为 $q\,\operatorname{nrd}(I)^2/4$。四维球和
Minkowski 定理给非零 $a\in I$，满足
$$
 \frac{\operatorname{nrd}(a)}{\operatorname{nrd}(I)}
       <\frac{\sqrt{8q}}{\pi}+\eta
\tag{12}
$$
对任意预先选定的 $\eta>0$ 可取到这样的界。
因为 $\bar aI\subset\bar I I=\operatorname{nrd}(I)\mathcal O_q$，
$$
       J=\frac{\bar a}{\operatorname{nrd}(I)}I
$$
是同一理想类中的整右理想，其范数为 (12) 左端。

只用 $\pi>3$ 就有 $q=13$ 时该整数范数至多 $3$，
$q=7$ 时至多 $2$。最大整环在不分歧素数 $r$ 的范数 $r$
整右理想恰有 $r+1$ 个，由 $\mathbb P^1(\mathbb F_r)$ 分类。
(7)、(11) 的代表 $a$ 是模左单位的，因此直接列出的是互异
左主理想 $\mathcal O_q a$。将它们共轭，便得到同样数目的互异
右主理想 $\bar a\mathcal O_q$；此时生成元模右单位。
这些共轭恰好给全数的范数 $r$ 整右理想，故所需小范数理想全部主，
两环的右理想类数都等于一。

这里没有把 type number 一误当成 ideal class number 一。
枚举完整性也不用浮点界。例如 (4) 的正交坐标为
$$
 \left(a+\frac c2+\frac d2,\
       b+\frac c2+\frac d4,\ \frac c2,\ \frac d4\right).
$$
固定范数后，每个坐标有明确平方界；脚本在这些完整整数区间
内用整数判别式平方检验穷尽全部元素。

### 2.4 层 $389$ 的点与 Hecke 算子

由 Deuring 对应，上述类数一给一个 supersingular 基础椭圆曲线，
其 $389$ 阶循环子群由
$$
                  X_q=\mathcal O_q^\times\backslash
                         \mathbb P^1(\mathbb F_{389})
\tag{13}
$$
描述。它就是判别式 $q$、Eichler 层 $389$ 的真实 definite
Shimura set。

为把所有矩阵定死，令 $m=2$ 或 $1$，分别对应 $q=13$ 或 $7$。
在奇素数 $r\ne q$ 的 split realization 中取
$$
 i_r=\begin{pmatrix}0&-m\\1&0\end{pmatrix},\qquad
 j_r=\begin{pmatrix}A&mC\\C&-A\end{pmatrix},\qquad
                     A^2+mC^2=-q.
\tag{14}
$$
按 $0\le A,C<r$ 的字典序选择第一个解，再代入 (4)、(8)。
在 $r=389$，两个解参数分别为
$$
         (A,C)_{13}=(1,185),\qquad (A,C)_7=(0,185).
\tag{15}
$$
对 $q=13$，单位模标量平凡，$|X_{13}|=390$。
对 $q=7$，$i$ 作用为 $x\mapsto-1/x$；它在
$\mathbb P^1(\mathbb F_{389})$ 有两个固定点，故 $|X_7|=196$。
每个轨道取最小的整数代表，$\infty$ 用 $389$ 编号。

对 $r\nmid389q$，令 $\mathcal A_r$ 为范数 $r$ 元素模左单位的
完整代表。标准 Hecke 的实际值为
$$
                  (T_r f)(x)=\sum_{a\in\mathcal A_r}f(a_{389}x).
\tag{16}
$$
因为范数 $r$ 的 endomorphism 的核正好跑过全部 $r+1$ 个
循环子群，(16) 保留全部 isogeny 的重数。$q=7$ 时不能把
额外单位作用删掉，也不能对有不同 stabilizer 的节点另行平均。
公式在商 (13) 上良定义；更换范数代表仅改变目标的单位代表。

## 3. 实际剩余 Hecke 本征函数与升层规范

直接数 (1) 的有限域点，得到
$$
 \begin{array}{c|rrrrrrrrr}
 r&2&3&5&7&11&13&43&131&233\\ \hline
 a_r&-2&-2&-3&-5&-4&-3&12&2&-6.
 \end{array}
\tag{17}
$$
构造 (16) 的稀疏矩阵后，两个系统都满足
$$
                  \dim_{\mathbb F_p}
                    \ker\binom{T_2+2}{T_3+2}=1,
\tag{18}
$$
其中 $(q,p)=(13,11),(7,13)$。令 $\varphi_q$ 在按顺序排列
的节点上第一个非零值为 $1$。

证书不仅保存了 kernel 维数：它保存 (18) 的完整非零核向量、
一个 $(|X_q|-1)$ 阶子式的行列索引和行列式。其值为
$$
              3\pmod{11}\quad(q=13),\qquad
              1\pmod{13}\quad(q=7).
\tag{19}
$$
核向量直接满足 $T_2\varphi=-2\varphi$、
$T_3\varphi=-2\varphi$，并另有
$T_5\varphi=-3\varphi$。所有矩阵来自 (7)、(11)、(14)--(16)，
故 (19) 是完全有限的可重现秩证明。

必须核实这个唯一的核确实含原升层函数。首先，
$E$ 在 $389$ 为 $I_1$，剩余惯性含一个非平凡 transvection。
在 $p=11$，Frobenius $2$ 的判别式为 $-4$，是非平方；
在 $p=13$，Frobenius $3$ 的判别式为 $-8$，也是非平方。
所以两剩余表示都不可约。

一个不可约子群若含非平凡 transvection，取另一个把其固定线
移走的群元，得到两条不同固定线的 transvection。在以这两条
线为基的坐标中，二者为非平凡上、下幺幺三角矩阵；因为底域
为素域，其整数幂给全体上、下幺幺矩阵，故生成
$\mathrm{SL}_2(\mathbb F_p)$。行列式的 cyclotomic 满射遂给
$\mathrm{GL}_2(\mathbb F_p)$。$p\ge5$ 的标准整提升
（R237 的满像短证）和 cyclotomic 行列式给全
$\mathrm{GL}_2(\mathbb Z_p)$。

本文三个虚二次域均不在 $\mathbb Q(\mu_{p^\infty})$ 中：
它们的判别式不被相应 $p$ 分歧支持。满群的二次商来自行列式，
所以限制到每个 $G_F$ 仍满像。

其次，
$$
 \begin{aligned}
  a_{13}&=-3\equiv-(13+1)\pmod{11},&
                    13^2&\not\equiv1\pmod{11},\\
  a_7&=-5\equiv7+1\pmod{13},&
                    7^2&\not\equiv1\pmod{13}.
 \end{aligned}
\tag{20}
$$
故它们准确为 R234 的负、正一般 admissible 观察。
$389$ 的剩余分歧由 $I_1$ 保留；全部导子平方自由。
R234 所核的已发表升层和 Zhang (2014), §4.2 因而在这两个
具体 $p$ 适用，给一个非零的原剩余 Hecke 本征函数。
其 $T_2,T_3$ 值必须为 (17)，所以由 (18) 它就是本篇
$\varphi_q$ 的一个单位倍。

模参数化也没有隐藏的 $p$ 因子：最优参数化的 Manin 常数在
这两个半稳定好素数为单位；从最优曲线到 (1) 的同源可取次数
与 $p$ 互素，因为其 $p$ 剩余表示不可约。R234 的同一
度零 Hecke 处理对全部 CM 标签仍只引入一个共同单位。
因此下面非零系数是原点的非零系数，不是另一个本征系统的数值。

## 4. 从实际 CM isogeny 核得到全部环类标签

本文使用 Cornut--Jetchev (2013), Theorem 3.1 与 §4.10 的
已发表、保 conductor 且 Galois 等变的 CM reduction 对应。
它把原模曲线 CM 轨道送到相应 definite 最优嵌入轨道；
在观察 $q$ 惰性、原 conductor 与 $q389$ 互素的本情形，
conductor 和每一个类群标签保持。下列公式也直接说明其
isogeny 和理想作用，避免只引用一个无标号的 supersingular 集合。

设
$$
               \eta^2-\eta+c=0,\qquad
                 c=(1-D_F)/4,
\tag{21}
$$
并在 $\mathcal O_q$ 中选具有 trace $1$、norm $c$ 的
$r=\iota(\eta)$。令 $v\in\mathbb P^1(\mathbb F_{389})$
为 $r_{389}$ 的一个本征线；这固定原 Heegner 的 $389$ 定向。
若 $\ell$ 在 $F$ 惰性，$r_\ell$ 生成的非分裂 torus 在
$\mathbb P^1(\mathbb F_\ell)$ 上单传递。

对每个 $a\in\mathcal A_\ell$，其 mod $\ell$ 矩阵秩一。
在 supersingular 椭圆曲线上，$a$ 的核为这条
$\mathbb P^1(\mathbb F_\ell)$ 线；商曲线重新以
$\mathcal O_q$ 的类数一规范识别后，$389$ 子群和原
$\mathcal O_{F,\ell}$ 嵌入分别为
$$
                  x_a=[a_{389}v],\qquad
                  s_a=a\,r\,\bar a.
\tag{22}
$$
第二式来自 $a(\ell r)a^{-1}$ 和 $a^{-1}=\bar a/\ell$。
其 trace 为 $\ell$、norm 为 $\ell^2c$。惰性保证没有
保持最大 CM 整环的 $\ell$-核，故这些正是 conductor $\ell$
的全部 $\,\ell+1$ 个局部 CM 来源。

选字典序最小的整数 $A\ge0$，使
$A I+r_\ell$ 在 $\mathbb P^1(\mathbb F_\ell)$ 上阶为
$\ell+1$。从 $\infty$ 开始，将其轨道标为 $j=0,\ldots,\ell$。
按 (22) 的核来赋标签。这是实际局部 ring-class torus 的
生成元标号，允许整体 Artin 正逆约定不同：反向和起点平移
只改变已知的非零单位或低项间的三角变换，不改变本文非零性。

当 $h_F=1$ 时，这已经是全部环类群。对
$\ell+1=pu$，真正完整的次数 $p$ theta 元素为
$$
 \theta_a=\sum_{\substack{0\le j\le\ell\\j\equiv a\ (p)}}
                 \varphi_q(x_j),\qquad
       \Theta=\sum_{a=0}^{p-1}\theta_a\tau^a.
\tag{23}
$$
其中的每个 $u$ 项都保留。其矩为
$$
              m_k=\sum_{a=0}^{p-1}\binom ak\theta_a,
                  \qquad k=0,1,2.
\tag{24}
$$

对非平凡 Hilbert 类群也没有将一个 maximal-order CM 点
充当全体。当一个分裂辅助素数 $r_0$ 的理想为
$(r_0,\eta-\lambda)$，在 conductor $\ell$ 的嵌入 $s$ 上，
其 isogeny 核是 $s_{r_0}$ 的 $\ell\lambda$ 本征线。选对应
的范数 $r_0$ 元素 $a$，准确更新
$$
          (s,x)\longmapsto
          \left(\frac{a s\bar a}{r_0},\,a_{389}x\right).
\tag{25}
$$
每一步仍在同一 conductor，(25) 是该真实理想类的 Artin
作用。下一节的 $p$ 类群计算完整使用这个作用。

## 5. 两个类数一的原低阶非零值

### 5.1 $p=11$ 的第二负矩

取 $q=13,F=\mathbb Q(\sqrt{-7}),\ell=131$。
有 $389$ 分裂、$13,131$ 惰性，$h_F=1$。
在 (4) 中取
$$
                   r=(0,0,0,1),\qquad v=0.
\tag{26}
$$
它的 trace/norm 为 $1,2$，其 $389$ 本征线为 $0,19$。
在 $\ell=131$ 的 (14) 规范中，$(A,C)=(0,37)$；
局部 torus 生成元为 $4I+r_{131}$。
全部 132 个范数 131 核由 (22) 标号，得到
$$
 \begin{aligned}
 (\theta_0,\ldots,\theta_{10})
       &=(2,4,10,2,2,10,4,2,3,2,3),\\
 (m_0,m_1,m_2)&=(0,0,4)\pmod{11}.
 \end{aligned}
\tag{27}
$$
源满足完整反射恒等式 $\theta_j=\theta_{7-j}$。
由于 $m_0=m_1=0$，平衡这个反射不改变第二矩。
另一 $389$ 定向给第二矩 $7=-4\pmod{11}$，也非零。

条件没有漏付：$\ell+1=11\cdot12$、
$a_{131}=2$ 为 $11$ 单位，$a_{11}=-4$ 好普通、非异常，
满像在 §3 已证。R234 的真实完整完成与 (27) 相差一个单位。
若原 $Q$ 属于 $\delta^2A(F)^\wedge_p$，其完成必在 $T^3$，
与 (27) 矛盾。因此原 $a\le1$，R146/R271 给 (3) 的 $p=11$ 部分。

### 5.2 $p=13$ 的第一正矩

取 $q=7,F=\mathbb Q(\sqrt{-11}),\ell=233$。
有 $389$ 分裂、$7,233$ 惰性，$h_F=1$。
在 (8) 的坐标中取
$$
                   r=(0,-1,1,0),\qquad v=189.
\tag{28}
$$
其 trace/norm 为 $1,3$，另一个 $389$ 本征线为 $200$。
$\ell=233$ 的 (14) 参数为 $(A,C)=(0,61)$，
$r_{233}$ 本身就是局部 torus 生成元。
完整 234 标签给
$$
 \begin{aligned}
 (\theta_0,\ldots,\theta_{12})
    &=(0,9,10,3,4,0,0,3,6,0,7,10,0),\\
 (m_0,m_1,m_2)&=(0,4,8)\pmod{13}.
 \end{aligned}
\tag{29}
$$
完整反射为 $\theta_j=-\theta_{5-j}$。
第一矩不受平衡平移影响；这里并未把未平衡的第二矩 $8$
当作独立的中央条件。另一 $389$ 定向给第一矩 $9=-4$。

有 $\ell+1=13\cdot18$、$a_{233}=-6$ 为单位，
$a_{13}=-3$ 好普通、非异常。若 $a\ge1$，真实完成的
增广为零给 $\Phi_q(Q)\in T^2$，与第一矩非零矛盾，
故准确为 $a=0$。R271 给 (3) 的 $p=13$ 部分。
这里 $p=13$ 在 $F$ 惰性并不造成遗漏：
R139/R271 的通常局部条件比较已包括 $p$ 的分裂、惰性情形，
没有额外假定必须在 $F$ 分裂。

## 6. 全部 $11$ 类群的实际二阶矩阵

现在固定同一个 $p=11,q=13$，取
$$
          F=\mathbb Q(\sqrt{-1307}),\quad
          \eta^2-\eta+327=0,\quad\ell=43.
\tag{30}
$$
基本判别式 $-1307$ 的全部 reduced forms 为
$$
 \begin{gathered}
 (1,1,327),\quad(3,\pm1,109),\quad(7,\pm3,47),\\
 (9,\pm5,37),\quad(17,\pm11,21),\quad(19,\pm17,21).
 \end{gathered}
\tag{31}
$$
这是 $a\le\sqrt{1307/3}$ 的完整整数枚举，故 $h_F=11$。
素数 $3$ 分裂；理想 $\mathfrak a=(3,\eta)$ 非主，因为
$x^2+xy+327y^2=3$ 无整数解。于是它生成整个类群，且
$$
       N(420+\eta)=420^2+420+327=3^{11},\qquad
                   \mathfrak a^{11}=(420+\eta).
\tag{32}
$$
后一个等式由两个 $3$ 上素理想的约化分别为
$420=0$、$421\ne0\pmod3$ 确定，不只从范数相等推断。

$389$ 分裂、$13,43$ 惰性，且 $a_{43}=12$ 是 $11$ 单位。
在 $\mathbb F_{43^2}=\mathbb F_{43}[\eta]$ 中精确有
$$
                      (420+\eta)^{(43^2-1)/11}
                         =(420+\eta)^{168}=1.
\tag{33}
$$
因此 R271 的真实扩张判据给
$$
 \operatorname{Gal}(F[43]/F)_{(11)}
                 \simeq C_{11}\times C_{11};
\tag{34}
$$
不是把一个可能的循环 $C_{121}$ 擅自写成直积。

在 $\mathcal O_{13}$ 中取
$$
                  r=(1,13,0,-1),\qquad v=135.
\tag{35}
$$
其 trace/norm 为 $1,327$，$v$ 是对应的 $389$ 本征线。
先按 (22) 用全部 44 个范数 43 核得到一个局部 block。
局部 torus 的生成元为 $r_{43}$。然后对每个嵌入 $s$，
使用 $s_3$ 的零本征线，在四个范数 3 代表中选出其核对应
的唯一 $a$，按 (25) 作一次真正的 $\mathfrak a$ 作用。
这恰是 $(3,\ell\eta)$ 的作用，因为 $\ell$ 与 $3$ 互素。

连续 11 次后，完整 44 个标签统一平移 $11\pmod{44}$。
这给 (33) 的另一个实际域交核验：在局部 $C_{11}$ 商中
该平移为零。此前十一层的 $11\cdot44=484$ 个
$(s,x)$ 嵌入数据彼此不同，正好为
$h_F(\ell+1)$，故全部 Hilbert 类群 coset 都已用到。
源中没有除以 $11$。

记 $i=0,\ldots,10$ 为 $\mathfrak a$ 的 coset 标签，$j=0,\ldots,43$
为原局部标签。先仅对局部阶四部分作完整求和：
$$
 A_{i,a}=\sum_{j\equiv a\ (11)}\varphi_{13}(x_{i,j}),\qquad
 \Theta_{\rm raw}=\sum_{i,a=0}^{10}A_{i,a}g^it^a
                   \in\mathbb F_{11}[C_{11}^2].
\tag{36}
$$
全部 $121$ 个 $A_{i,a}$ 以及原 $484$ 个值存于证书。
按 R271 的局部、类群两个 log 坐标，准确得到
$$
 \begin{aligned}
 &\sum_{i,a}A_{i,a}=0,\qquad
   \sum_{i,a}aA_{i,a}=\sum_{i,a}iA_{i,a}=0,\\
 &\left(
 \begin{array}{cc}
 \sum a^2A_{i,a}&\sum aiA_{i,a}\\
 \sum aiA_{i,a}&\sum i^2A_{i,a}
 \end{array}\right)
       =\begin{pmatrix}8&8\\8&0\end{pmatrix},\qquad \det=2\ne0.
 \end{aligned}
\tag{37}
$$
完整反射关系是 $A_{i,a}=A_{5-i,1-a}$，与原负号观察相符。

规范化的所有真分歧商为
$t\mapsto\tau,\ g\mapsto\tau^b$。对 (36) **pushforward**
而不是先 norm 再 pushforward，得到
$$
 \begin{aligned}
 \Theta_b&=\sum_{i,a}A_{i,a}\tau^{a+bi},\\
 [T^2]\Theta_b
    &=\frac12\sum_{i,a}(a+bi)^2A_{i,a}
      =4+8b\pmod{11}.
 \end{aligned}
\tag{38}
$$
第一式保留每个 coset，第二式中一次矩为零已经由 (37) 核实。
所以 (2) 不是仅对抽象二次形式的评价，而是十一个真实子域的
原完整 Heegner theta 的实际值。

对 $b=0$ 就有第二矩 $4$，R271 的有限 $p$ 类群下降给
原 $a\le1$ 和同一固定曲线的 $11$ 初级 Sha 为零。
$b=5$ 的二阶项为零并不表示其全 theta 为零，也不否定其他
十个商的原非零性。

三个辅助域的基层扭点亦可直接排除，故可取 $t_F=1$：
在 $F=-7$ 的 $3,7$ 处约化群阶为 $12,13$；
在 $F=-11$ 的 $3,13$ 处为 $6,187$；
在 $F=-1307$ 的 $3,7$ 处为 $6,13$。
结合好约化在不同剩余特征的 prime-to-characteristic 挠点单射，
各自均给 $E(F)_{\rm tors}=0$。因而本文使用的确实是整数
范数零点 R271 (5)，没有事后乘一个可能丢掉原低项的非单位。

## 7. 对跨素数任务的确切意义

本篇付清了两个标量和一个完整 $p$ 类群来源的实际非零输入，
使 O4 的接口不再只有环境函数或抽象模块例子。
每个证书只含固定的有限算术；没有证明这些输入属于 R149 的
整个联合无穷子族，也没有把两个素数说成无穷多个。

这里还有一个必须保持的量词约束。固定观察 $q$ 时，
admissibility 要求
$$
                         p\mid a_q-\epsilon(q+1).
\tag{39}
$$
Hasse 界使右边整数不为零，因此一个固定 $q$ 只能覆盖有限
多个 $p$。本篇 $q=13,\epsilon=-1$ 的整数就是 $11$，
$q=7,\epsilon=+1$ 的整数为 $-13$。故这两个 class-number-one
quaternion 模型不能单独产生跨 $p$ 的无穷性；后续证明必须
让真实观察 $q$ 变化，或另找一个能控制原两矩的跨 $p$ 输入。

同理，固定的 $F=-1307$ 只在 $p=11$ 有这里的额外 $p$ 类群
方向。R271 的多个分歧商恢复的是确实已经存在的 (37)，
不自动制造它。在新的 $p$ 上，必须重新证明实际原全 theta
的二阶项非零，不能从本篇的有限矩阵秩、观察素数的自由选择、
或类数含 $p$ 推出。

## 来源

- R2、R136、R139、R146：固定曲线和原整数范数一 Heegner
  来源；R234：同一 conductor、完整类群、同一单位的
  Zhang definite 比较；R271：保全部 $p$ 类群的有限下降、
  总二阶项到真实分歧商与整个 Selmer 的充分条件。
- C. Cornut--D. Jetchev, *Liftings of reduction maps for quaternion
  algebras*, Bulletin of the London Mathematical Society **45** (2013),
  370--386，Theorem 3.1、§4.10；
  [DOI](https://doi.org/10.1112/blms/bds098)，
  [作者全文](https://webusers.imj-prg.fr/~christophe.cornut/papers/liftings.pdf)。
  本篇使用其保 conductor、Galois 等变的最优嵌入 reduction
  对应；全部具体 isogeny 和类群标签由 (22)、(25) 实算。
- W. Zhang, *Selmer groups and the indivisibility of Heegner points*,
  Cambridge Journal of Mathematics **2** (2014), 191--253，
  Theorem 2.1、§4.2，具体适用条件见 R234 和本文 §3。

最大整环、ideal class number 一、剩余满像、小类数、
有限本征线和全部实际矩的证明都已在本篇及精确证书中给出；
未使用数据库 rank/Sha 数字作为证明输入。
