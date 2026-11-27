# R1037 — 原 B12 商的完整 degree378 输入、有限三分类与全谱验收

日期：2026-11-27 UTC。**已证明：原两条秩至少二的 degree390 来源除以实际 B12，得到两条质量一的完整 degree378 来源；其中42维最高三进层的角色真正含九次值，不能当作另一条有理 CM 椭圆曲线。可能的有理椭圆曲线部分严格位于整个22维 δ-old 来源，另外两个旧层的维数为8、3。** 本篇同时给原三处好算子的完整生成关系、全部64列验收和原二处算子。新公开计算的实际全谱、质量和算术标签在取得完整回执后续接；本版不预填任何新曲线、秩或中央非零。

本篇使用 R981 的两条完整来源
$$
 f_A=\Psi_{35},\qquad f_B=\Psi_{53},\qquad
 f_\nu=\sigma^{390}P_\nu(X),\quad X=x^3,\quad y^2=X+1,
 \tag{1}
$$
及 R1021 §15 已证明的原 B12 和全部 Weyl 相位。两条来源的原完整
66维共同核、绝对 Hecke 角色及秩下界仍由 R981 给出。本篇不改变它们，
也不把除法、投影或质量零当作传播中央零的算子。

## 1. 两个实际完整商

原规范是
$$
 \sigma(z)=z+O(z^7),\qquad x=z^{-2}+O(z^4),\qquad
 y=-z^{-3}+O(z^3),\qquad \delta^2=-3,\quad
 \omega=(-1+\delta)/2.
$$
R1021 §15 给
$$
 B_{12}=\sigma^{12}y^2=\frac{\sigma^4\sigma(2z)^2}{4},
 \qquad \operatorname{div}(B_{12})=6(O)+2\mathcal D_2,
 \tag{2}
$$
其中 $\mathcal D_2$ 是三个非零二挠点的和。原两源在 O 准确六阶，
在三个二挠点至少二阶；因此不是仅在 Taylor 展开中作商，而是全局整截面
$$
 F_\nu=\frac{f_\nu}{B_{12}}
     =\sigma^{378}Q_\nu(X),\qquad
 Q_\nu=P_\nu/(X+1),\quad
 \deg Q_\nu=63,\quad [X^{63}]Q_\nu=1.
 \tag{3}
$$
相应全空间是
$$
 V_{378}=\sigma^{378}K[X]_{\le63},\qquad \dim_KV_{378}=64.
 \tag{4}
$$
最后一列是质量列，完整保留。两商各质量一，差 $F_A-F_B$ 质量零。
这不说明差在每一个算术块的质量都零。

原来源的固定完整向量摘要为
$$
\begin{array}{c|l}
 f_A&
 \texttt{4485e52f18d5349f8158e0d2177d38b6ae5c5b5862089ea66ab6e4cf4546bcb0}\\
 f_B&
 \texttt{dd354f3138dff257035c02561acef381470829b66fdb712801cb08455442fbe1}.
\end{array}
 \tag{5}
$$
新生产器必须先由同次原390的两张完整矩阵重新取得这两个向量，核定
(5)、原完整 δ-trace 零，再对全部多项式作 (3) 的除法和反乘。
本篇不把归档的生成坐标填入新源码。

## 2. 原二处算子及全部质量

取实际二挠点 $T=(e,0)$、$e^3=-1$。R1021 §15 的同一 lift 给
$$
 q_T^2=\frac{e^2}{\sqrt3}(x-e),\qquad
 x(P+T)=e\frac{x+2e}{x-e},\qquad
 y(P+T)=-\frac{3e^2y}{(x-e)^2},
 \tag{6}
$$
$$
 q_T^{-4}T_T^{390}f=B_{12}\,T_T^{378}(f/B_{12}).
 \tag{7}
$$
常数恰为一，因为 $9e^4(e^2/\sqrt3)^4=e^{12}=1$。
原390与新378的 Pauli 符号相反；式 (7) 已保全部 fourth Miller 费用，
不能将原二处本征值直接沿除法搬下。

令
$$
 S_{378}=\sum_{0\ne T\in E[2]}T_T^{378},\qquad
 D_2=S_{378}/\sqrt3 .
$$
在 (4) 的整个64列上有显式有理矩阵
$$
 \boxed{(D_2)_{ij}
   =3^{-94}(-1)^j[x^{3i}]
       (x+1)^{189-3j}(x-2)^{3j},
       \quad 0\le i,j\le63.}
 \tag{8}
$$
证明是在 (6) 中代入 $\sigma^{378}X^j$。单个 $e=-1$ 项的共同常数为
$3^{-94}/\sqrt3$，另两个 e 项在所有非三倍指数上相消，
在三倍指数上是同一项的三倍。再除 $\sqrt3$ 正好给 (8)。
原 Pauli 恒等式给
$$
 D_2^2=I,\qquad \Pi_{2,\pm}=(I\pm D_2)/2.
 \tag{9}
$$
这是完整二处投影，不是只读质量的一条公式。对 (3)，(8) 的最后一行准确给
$$
 m_0(D_2F_\nu)=3^{-94}Q_\nu(-1)
              =3^{-94}P_\nu'(-1),
 \qquad
 m_0(\Pi_{2,\pm}F_\nu)=
 \frac{1\pm3^{-94}P_\nu'(-1)}2 .
 \tag{10}
$$
新原 good CM 算子与 (8) 交换：其完整 Heisenberg 交织在三个非零二挠点
上只是置换，实际 sum 不变。消费者将对整个矩阵回乘 (9)、该交换关系及 (10)。

## 3. 完整三处模型与最高42维的严格排除

原378的有限模型是
$$
 W_2\otimes W_{27}\otimes W_7,\qquad \dim=2\cdot27\cdot7.
 \tag{11}
$$
这里 $W_{27}$ 是原加性角色下的27维 Schrödinger 模型，
不是27份任意一维来源。将 ramified torus 写成
$$
 T_{27}=\{u\in(\mathcal O_K/27)^\times:u\bar u=1\}
       =\langle-1\rangle\times\langle\omega\rangle\times\langle h\rangle,
 \qquad h=1+3\delta,\quad h^k=1+3k\delta\bmod27.
 \tag{12}
$$
所以三个因子的阶为2、3、9。每个 norm-one 单位的实部模3为 $\pm1$，
对每个 δ 系数均有两个实部提升，故 $|T_{27}|=54$；
(12) 的54个元素两两不同，已经给全体。

关键不是把其全部角色预先压成三次。取 $(1,\delta)$ 为三处的整基
（与标准基的行列式是二的单位）。在这一基中
$$
 h^3=1+9\delta
  \longmapsto
  \begin{pmatrix}1&-27\\9&1\end{pmatrix}
  \equiv\begin{pmatrix}1&0\\9&1\end{pmatrix}\pmod{27}.
 \tag{13}
$$
若采用标准辛基，下方9只乘一个三进单位。原 finite Weil 的 unipotent
公式因而为
$$
 W_{27}(h^3)e_r=\zeta_3^{\,c r^2}e_r,
 \qquad r\bmod27,\quad c\in\mathbf F_3^\times.
 \tag{14}
$$
c 由原加性角色及辛基决定；本篇不自由改其符号。对下面的断言，
只需要且已经证明 $c\ne0$。
因此
$$
 \ker(W_{27}(h^3)-I)=
 \operatorname{span}\{e_{3r}:r\bmod9\},\quad\dim=9,
 \tag{15}
$$
其18维补空间上 $h^3$ 的值为同一个非平凡三次根。每个出现在该补空间
的 h 角色都具有准确九阶，而非三阶或六阶。

原 $[\delta]$ 的 kernel 是 theta group 中的三阶各向同性子群。
在同一 Schrödinger 极化中，其不变向量正是 (15)；
拉回 $[\delta]^*:H^0(\mathcal O(126O))\to H^0(\mathcal O(378O))$
的像也是该不变空间。维数126与 $2\cdot9\cdot7$ 相等，故是整个像，
没有漏掉一个陪集。对几何 $\mu_6$ 平均后，
$$
 V_{378}^{\delta\text{-old}}
     =[\delta]^*V_{126},\qquad \dim=22,
 \qquad \dim V_{378}^{\delta\text{-new}}=42.
 \tag{16}
$$

对固定 CM torus 的 Hecke 角色，Hilbert90 只把该局部有限角色换成逆角色
并保留原 splitting；在这一奇数阶主单位子群上，quadratic splitting
没有新的九次角色。原 theta-group 的共同绝对标量也不能把一个准确九次
角色变成六次。因此 (14) 的42维主型补空间具有真实非六次的三处单位值。

另一方面，每条 $\mathbf Q$ 上 $j=0$ 椭圆曲线的 CM 角色相对于固定
最大整环角色是六次扭曲，在所有坏单位上其扭曲值属于 $\mu_6$。
遂得严格分类：
$$
 \boxed{\text{最高三进层的全部42维都不是 }\mathbf Q
 \text{ 上另一条 }j=0\text{ 椭圆曲线来源。}}
 \tag{17}
$$
它们仍是真正 CM Hecke/theta 来源；本篇没有给其相应较高维动机套用
椭圆曲线的通常全 Selmer 桥。可能的有理 CM 椭圆曲线只在 (16) 的22维内。
这个结论不由两个好位的数值外观推得。

## 4. 全三层旧空间及显式 pull/trace

对 $N=3M$ 且 M 偶，令
$$
 o\equiv M/2\pmod3,\quad0\le o\le2,\qquad
 J=(M-2o)/6.
$$
原下层主型为 $\sigma^Mx^oK[X]_{\le J}$。
由
$\sigma(\delta z)=\delta\sigma(z)^3x(z)$、
$x(\delta z)=-(X+4)/(3x^2)$，完整拉回第 j 列为
$$
 E_{M,j}(X)=
 (-3)^{M/2}(-1/3)^{o+3j}
     X^{2(J-j)}(X+4)^{o+3j}.
 \tag{18}
$$
没有省去最后质量列，其最高列质量仍为一。

完整未平均 trace 可以逐列无根式写出。令 a 是下层 x 坐标，
$S_k(a)=\sum_{x^3+3ax^2+4=0}x^k$，按重数取整条三纤维。准确递推为
$$
\begin{aligned}
 S_0&=3,& S_1&=-3a,& S_2&=9a^2,&
 S_k&=-3aS_{k-1}-4S_{k-3}\quad(k\ge3),\\
 S_{-1}&=0,&S_{-2}&=-3a/2,&
 S_{-k}&=-3aS_{-(k-2)}/4-S_{-(k-3)}/4\quad(k\ge3).
\end{aligned}
 \tag{19}
$$
故原上层第 j 列的 trace 为
$$
 (-3)^{-M/2}S_{3j-M}(a)=a^o\sum_i(T_M)_{ij}a^{3i},
 \qquad T_ME_M=3I.
 \tag{20}
$$
(20) 同时证明相应平均投影是 $E_MT_M/3$，并保完整来源相位。

依次取 $M=126,42,14$。全部主型维数为
$$
\begin{array}{c|c|c|c}
 \text{下层 degree}&o&J&\dim\\ \hline
126&0&21&22\\
42&0&7&8\\
14&1&2&3.
\end{array}
 \tag{21}
$$
三次完整复合投影嵌套。因此从高到低，四个互不交的三进层维数严格为
$$
 \boxed{42,\quad14,\quad5,\quad3.}
 \tag{22}
$$
所有 good norm 算子与 (18)–(20) 交织，因为它们的实际 pull/trace
是互素 CM 同源的完整纤维重排。公开验收将逐矩阵回乘全部恒等式；
不得只保最高层或只保两个来源所在的列。

## 5. 七处全部旧向量与三处好算子的完整生成

七在 K 中分裂。令 $\gamma_7=(5+\delta)/2$，
$R_7=X-(2-6\delta)/7$，并写
$x(\gamma_7z)=x A_7(X)/(\gamma_7^2R_7(X)^2)$。
两条真正退化映射是
$$
 [\gamma_7]^*,[\bar\gamma_7]^*:
   V_{54}=\sigma^{54}K[X]_{\le9}\longrightarrow V_{378}.
 \tag{23}
$$
第一条第 j 列的完整多项式为
$$
 \gamma_7^{54-6j}R_7^{54-6j}X^jA_7^{3j},
 \qquad0\le j\le9;
 \tag{24}
$$
另一条全共轭。两像各维10，且交为零：共同向量将同时被两个互补七阶
kernel 的 theta lifts 固定，但其 commutator 是原 nondegenerate 七阶
Weil pairing，因 $378/7=54$ 与7互素而非一。故七处整个旧像维20。
它对应 split finite Weil 中的那条重数二角色，不能把两旧向量当成两条曲线。
消费者保持两套完整10列和每个联合块与该20维像的真实交。

为分开其余有限类型，使用
$$
 \gamma_{13}=(7+\delta)/2,\quad
 \gamma_{19}=4+\delta,\quad
 \gamma_{31}=(11+\delta)/2,\qquad
 N_\gamma=[\gamma]_*[\bar\gamma]^*/\gamma.
 \tag{25}
$$
先显示 $\bar\gamma/\gamma$ 的准确 compact 比值；原 $N_\gamma$
在 Heisenberg 群上实施其逆 $\gamma/\bar\gamma$，方向不可混用。
七处取 $\delta\mapsto2$、$\zeta_6=-\omega\mapsto3$。
$$
\begin{array}{c|c|c|c}
 \gamma&2&27&7\\ \hline
 \gamma_{13}&\omega&\omega^2h^4&\zeta_6^3\\
 \gamma_{19}&1&\omega^2h^8&\zeta_6^5\\
 \gamma_{31}&\omega&\omega h^8&\zeta_6^5.
\end{array}
 \tag{26}
$$
例如三处的三个值分别是 $4+7\delta,22+\delta,4+2\delta\bmod27$；
用 $h^k=1+3k\delta$ 可逐项核 (26)。

除去共同全局 $\mu_6$ 后，完整 compact 参数为
$$
 (C_3\times(C_2\times C_3\times C_9)\times C_6)/\mu_6
       \simeq C_3\times C_9\times C_6.
 \tag{27}
$$
先用共同 $-1$ 令三处符号为正，再用共同
$\omega=(1,1,0,4)$ 消二处坐标，(26) 的三行变成
$$
 v_{13}=(1,4,5),\quad v_{19}=(2,8,5),\quad v_{31}=(0,8,1).
 \tag{28}
$$
$v_{19}-2v_{13}=(0,0,1)$。仅前两行所生成的子群有54个元素，
在完整162个参数中 index 为三，因为其前两坐标满足
第二坐标模3等于第一坐标。加入 $v_{31}$ 后，
$(0,0,1)-v_{31}=(0,1,0)$，再从 $v_{13}$ 减去
这两生成元的四倍、五倍得到 $(1,0,0)$。所以三行确实生成整个群。

实际矩阵中保所有绝对标量，定义
$$
 C=N_{19}N_{13}^{-2},\qquad
 H=CN_{31}^{-1},\qquad
 A=N_{13}H^{-4}C^{-5}.
 \tag{29}
$$
原 ratio 方向使其几何参数分别是 (28) 对应三个标准生成元的逆。
不将这种方向误写成独立重相位。
这里的绝对标量不用未付的「属于根单位」断言。使用 R302 的实际
degree2 参考 $\Theta=\sigma^2x$：其完整 Hecke/Schwartz 来源已给
$$
 \psi_1((a))/a=\varepsilon_1(a)^{-1},\qquad
 \varepsilon_1(a)=
 \operatorname{Teich}_{\mu_3}(a\bmod2)\,(a\bmod\delta).
 \tag{30a}
$$
三个原生成元准确是
$\gamma_{13}=4+\omega,\gamma_{19}=5+2\omega,\gamma_{31}=6+\omega$。
在二处的值依次是 $\omega,1,\omega$，在 δ 处依次是 $-1,1,1$。
沿原 $N_\gamma=M_\gamma/\gamma$（不是其逆）的规范，得到
$$
 (N_{13},N_{19},N_{31})\Theta=(-\omega^2,1,\omega^2)\Theta.
 \tag{30b}
$$
这是 R302 的真正 Hecke/Schwartz 公式逐项计算；并非由三个好位
trace 猜测，也没有从 $\Theta^2$ 的 degree4 特征取平方根。
消费者在 degree2 唯一 principal 列上用全部13、19、31点 fiber
独立核 (30b)，两个目标都保原 sigma 除子相位。

再取真正的
$\Theta_{378}(z)=\Theta(\delta^3\gamma_7z)$。
它在 (4) 中，质量一。norm189 与13、19、31均互素，因此原完整
CM pull/trace 的纤维换元给
$N_\gamma D_{\delta^3\gamma_7}=D_{\delta^3\gamma_7}N_\gamma$；
全半特征由同一偶 sigma 线束的 Gram 身份保持。
$\Theta(\gamma_7z)=\sigma^{14}xA_7(X)$，其中 $A_7$
正是 (23) 的完整 numerator；随后三次 (18) 的 δ-pull 给
$\Theta_{378}$ 的全部64坐标，消费者不另选规范。

令 $\zeta_6=-\omega$。将 (30b) 代入 (29) 得
$$
 A\Theta_{378}=\zeta_6\Theta_{378},\quad
 C\Theta_{378}=\omega^2\Theta_{378},\quad
 H\Theta_{378}=\Theta_{378}.
 \tag{30c}
$$
由原 theta-group 交织，(28) 中几何参数成为单位的算子词只差一个
标量与对应的全局 $\mu_6$ 作用；后者在 principal 空间为一。
(30c) 这个完整非零锚遂逐一固定标量，给准确的全64维身份
$$
 \boxed{C^6=I,\quad A^6=I,\quad H^{18}=I,\qquad
 A^3=-I,\quad H^9=I.}
 \tag{30}
$$
全部64列另作直接回乘，不把锚的单列身份冒成整个矩阵验收。
原三个算子也有十八次幂一，并可由
$$
 N_{13}=AH^4C^5,\qquad
 N_{19}=CN_{13}^2,\qquad N_{31}=CH^{-1}
 \tag{31}
$$
完整回乘。这不是只在候选来源上的必要条件。

H 的六个线性 $\mu_6$ 因子与四个可能的三次因子
$$
 U-\zeta_6^j\ (0\le j<6),\qquad
 U^3-\zeta_6^j\ (j=1,2,4,5)
 \tag{32}
$$
给完整 $U^{18}-1$ 分解。每个三次因子在 K 上不可约。
(14)–(16) 给线性部分准确等于整个22维 δ-old，三次部分准确等于42维
补空间。A、C 的全部六次投影与 (32) 共同使用，故不遗漏相同三次
特征多项式内不同的 Galois 方向；两个额外独立参数已由 (27)–(29) 给出。

## 6. 整条新 CM fiber，而非生成坐标输入

对 $\ell=13,19,31$，原完整 sigma quotient
$$
 q_\gamma(x)=\frac{\sigma(\gamma z)}{\gamma\sigma(z)^\ell}
$$
是首一多项式，次数 $(\ell-1)/2$，只含三倍指数。
这由整个 division divisor 与 CM 型确定；其
$x^d,x^{d-3},\ldots,1$ 有限基由相同个数 Laurent 系数唯一决定。
生产器从
$x''=6x^2$、$(\log\sigma)''=-x$ 原递推生成这些系数，
不是用低 jet 近似整条来源。
所需系数数量对13、19、31分别为3、4、6。旧 norm7、norm13、
norm19 的完整 quotient 同时逐系数反核。

原 x-map 全分子为
$$
 n_\gamma=\ell xq_\gamma^2
       -4(x^3+1)(q_\gamma''q_\gamma-q_\gamma'^2)
       -6x^2q_\gamma'q_\gamma ,
 \tag{33}
$$
所以对每个实际目标 a，完整 fiber 是首一 degree $\ell$ 方程
$$
 F_{\gamma,a}=n_\gamma-a\gamma^2q_\gamma^2.
 \tag{34}
$$
在该整代数中做原 trace，保
$\gamma^{-379}q_\gamma^{-378}$ 和全部 $\bar\gamma$ carrier，
得到 (4) 的全部64列。使用64个不同 $a^3$ 插值，再对另外两个整 fiber
验证全部64列，因全像仍在 (4)，这是完整算子的证书。

### 6.1 忠实 doubled rational 后端

为了使 norm31 的完整 fiber 保持可执行，写
$F=F_0+\delta F_1$，置
$$
 D=F_0^2+3F_1^2,\qquad
 d=-F_0F_1^{-1}\pmod D.
 \tag{35}
$$
只在 $\gcd(F_1,D)=1$ 时使用 (35)。D 首一、次数 $2\ell$，且
$d^2=-3,F_0+dF_1=0$。这给忠实的等维同构
$$
 K[x]/(F)\simeq\mathbf Q[x]/(D),\qquad \delta\mapsto d.
 \tag{36}
$$
右端仍是整条 doubled fiber，未选择一根、未删任何分支。
对任意 a，准确恢复原 K-trace 的公式为
$$
 \operatorname{Tr}_{K[x]/F\,/K}(a)
   =\left(\tfrac12\operatorname{Tr}_{\mathbf Q[x]/D\,/\mathbf Q}(a),
       -\tfrac16\operatorname{Tr}_{\mathbf Q[x]/D\,/\mathbf Q}(da)\right)
 \tag{37}
$$
（坐标依次为实部和 δ 部）。
因为 trace 的传递性给
$\operatorname{Tr}_{K/\mathbf Q}(u+v\delta)=2u$、
$\operatorname{Tr}_{K/\mathbf Q}(\delta(u+v\delta))=-6v$。
若 (35) 不可逆，程序严格回到原 K 上的完整 fiber 后端，
不跳过该目标。每个新算子还将一个整个64列 fiber 与原后端交叉回乘。

## 7. 新公开验收所保留的内容

独立脚本为 scripts/check-original-degree378-complete-spectrum.py。
它只在本公开仓库 Actions 中执行，且只读 source/request；不读生成系数文件，
不写生成坐标到仓库。新请求 pin 实际全部依赖及消费者本身。

已经实时只读核过 R976 的公开 job140130269899 和 R982 的
job140158402506（run45892525657、source
c3fc3c60605f4455fc57177367c89e56a9763f6a）及其生产器：
两条原66向量只输出完整 hash、分母、归一列和标量，没有保存完整坐标。
所以旧回执不能直接提供这次商的输入。新入口只生产为此必需的
390-degree N7/N19：各全部66列、68个 full fibers、两 extra、
共轭逆与交换，整个两矩阵合并 hash 必须准确返回
e80e5777735077da004012b5abe8dfd2ba246b9404fd53899502c453242d1fff。
它采用同一个 (35)–(37) 后端，并交叉原 K-fiber；不调用旧
construct_complete_source，不复做无关的旧 E65 kernel、六来源或全谱结论。
原输入 hash (5) 与 δ-new trace 仍逐式回乘。

标准输出仅一个紧凑 JSON，低于公开请求的60000字节界限。
两原66向量、新64商向量、所有质量零秩一块的完整坐标以及完整精确报告
均作为带 hash 的独立 JSON 行写入同一公开 job 的 stderr 日志；
它们不是输入缓存。主回执保全每块的秩、层、dyadic/7-old、
真实零/非零、完整 hash 与通常大小的实际标量；若标量串超过输出界限，
仍以完整日志摘要严格关联，不删数学验收。

必须同时通过：原390完整来源、(5) 的两个完整摘要与整除反乘；
三张新的64列矩阵、每张66个 full fibers、两 extra 全列返回；
R302 的三个 degree2 绝对锚及其实际 degree378 拉回；
原 norm13 的 S34 锚、norm19 的 degree4 锚；
所有共轭逆、交换与十八次幂；(8)–(10)；
(18)–(22) 的全部 pull/trace；(23)–(24) 两个完整7-old 像；
(29)–(32) 的所有联合幂等块及其总和 $I_{64}$；
两个输入及其差的每个投影在全部64坐标上的总和返回。

每块读取完整质量行；若秩一，读取真实质量/原点阶、整规范、全向量摘要、
两来源及其差的真实标量；若质量零，还返回全部规范多项式。
higher-dimensional 和 old 重数不改名成多条椭圆曲线。

为核对潜在有理六次扭曲，程序可在固定13、19、31三个好位计算
$d=2^a3^b7^c,\ 0\le a,b,c<6$ 的准确 trace，并同 (31) 比较。
负 d 可用有理三同源 $d\mapsto-27d$ 回到这个正六次代表范围。
这些是固定有限角色辨认资料；三好位符合本身不是秩下界，也不是全部
Schwartz/Yang 因子的证明。最终曲线标签仍须按 (11)–(32) 的全部有限型、
实际 conductor 和 old/primitive 范围认回；实际秩至少二须另外由有理点
与下降或已证明的等价算术输入给出。

当前没有声称这次全谱已经执行。第一批实际回执取得后在本篇继续记录；
不以更换来源空间代替主问题所需的中央导数非零。

## 8. 本次完整公开入口与身份

本次使用独立 workflow .github/workflows/rank2-sha-degree378-complete-spectrum.yml；60分钟外帽、数学子进程3300秒帽、
4个固定 fork workers、python-flint0.9.0。
它只监听该 workflow 与本次固定 request，不监听其它课题文件。
原几何 v10 的 workflow、请求、参数及正在运行的作业均保持原样。

宿主仅校验源、精确请求/当前 detached commit 和工作流，
同时流式读取 stdout/stderr；完整坐标及谱报告保在公开 job 日志。
所有日志内容以 JSON 数据安全输出，原子进程两条原始字节流分别记 hash，
完整报告的 payload hash 必须与最后摘要相符才给宿主完成回执。
数学出错或达到时间帽时只记 INCOMPLETE，不从中途列数推断完整谱。

本次全部源身份：

| 源 | 字节 | SHA256 |
|---|---:|---|
| check-original-degree378-complete-spectrum.py | 36578 | e5dc7114c455695349bc263061e3b8e6247a258c5c82469402b0934c64f0f2f2 |
| launch-original-degree378-complete-spectrum.py | 9794 | 1a6b2f908affe6989ae302622ac11ef4741487d66bc308791a63c17f03793898 |
| workflow | 1745 | 70e970500ad9bff262b874e1fc664d08b192f70d8ce310314b6f36ac2feb4867 |
| ci/original-degree378-complete-spectrum-request.json | 1488 | be7284acf6e2e66b718e5ee2b2ae249292687693576460235eb23392c2be9c9b |
| check-r480-actual-input-cm19.py | 7811 | 3d4d9a05872cdde0f24ff756ec79407417afa943eabf6f71f4e48d32f91f9c45 |
| check-r466-fixed-two-division-source.py | 13402 | effd6f1526421cfcb9da3bd7769eed258374fa0addf337313d0315cb3ef08245 |
| check-r464-degree102-cm7-exact.py | 13396 | b3e11a9da1b28a7623d86acf944262ab23c2d1969b1f0183030a4d1c96b5f1ff |

根已逐个从原提交读取三依赖并核同这些字节与 hash。
新证明/消费者/宿主只经手工静态审读；本节不声称新数学已执行。
公开作业的完整终态及实际谱须随后消费。
