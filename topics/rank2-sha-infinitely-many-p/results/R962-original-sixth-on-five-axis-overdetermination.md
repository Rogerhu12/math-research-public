# R962. 第六原中央在旧五轴必要系统上的真实过定余式

日期：2026-11-26。**已证明。公开 run45823614454 已成功返回 p=227 的实际单位余式与全部 C24 行；这里只登记有限结论和其完整证明，不宣称无穷素数非零。** 本注不扩成六个未知量，也不把一个有限余式的非零升级为无穷素数定理。

使用 R943 的五个原来源和 R959 的完整第六来源。它们都在共同
$E_1$ 上归一为 $w+O(w^2)$，$w=z^6$。第六源先除以固定单位175；
R959 已证明该操作、原17/65周期和通常 Selmer 比较的准确范围。
依次记六源为 $\nu=S,T,U,V,W,Z$，相对 charge 为
$$
q_\nu=(1,36/17,4,33/17,89/17,195/17).
$$
共同 Gaussian 取 $\kappa=34c$、$c=[w^s]\log(\sigma/z)$、$a=p\kappa$，
$p=6s-1>211$。R943 §8 / R342 的整 Gaussian 重标说明，这个 $\Delta=0$
规范与任意已经支付的实际整 $\Delta$ 具有相同的中央零；这里固定这一
规范作精确有限计算，不给它自由高位。

## 1. 第六行用同一五轴，而非第六自由参数

沿 R943，令
$$
A_r^*=\ell_{s-r}+(-1)^{s-r+1}\frac{8^{s-r}}{s-r},
\qquad r=1,\ldots,5,
$$
$$
\ell_n=\frac{17}{3n}\frac{(1/3)_n}{(5/6)_n}.
$$
从原 $g$ 删除这五项，得到同一个参考 $g_\circ$。
所有六源都用同一个
$$
g_A=g_\circ\exp\!\left(\sum_{r=1}^5 A_rt^{s-r}\right).
$$
不存在独立的第六来源高轴。实际 $t(w)=-w\mathcal W(w)^{-3}$ 的全部
高尾保留，不能以五个纯 $w$ 单项式替代它。

为计算方便置 $x=A-A^*$，按 $r=5,4,3,2,1$ 排序。由同一个
原 regularized 来源
$$
\widehat\nu=\nu e^{-q_\nu\kappa w^s}
$$
直接定义
$$
C_{\nu,h}(x)=
[w^{hs}]\widehat\nu
\sum_{j=0}^{h}\frac{q_\nu^j}{j!}
 \left(\sum_{r=1}^5x_rt^{s-r}\right)^j,
\qquad1\le h\le6.
\tag{1}
$$
$1+(h+1)(s-5)>hs$ 对 $s>35,h\le6$ 成立，因此 (1) 没有丢项。
这里 $x=0$ 恰是原算术来源。

第六源在 R959 原记号下满足
$$
\frac{\widehat Z}{w}
=f^{-195}\mathcal W^{192}
 \sum_{j=0}^{64}c_j\left(w/\mathcal W^3\right)^{64-j},
\quad
f=(\sigma/z)^{-2}e^{2cw^s}.
\tag{2}
$$
每一项的 $\mathcal W$ 幂非负，最低为零；所有源分母在 $p>211$
为单位。R614 的真 addition 整窗包含式(1)需要的全部次数，
至 $6s-1=p$ 的扰动指数只使用 $0!,\ldots,6!$。因此所有
$C_{\nu,h}$ 是整多项式。

R602 / R943 的 Hurwitz 尾对 (2) 同样适用。取 $H=6$ 得剩余尾
属于 $p^6\mathcal O$；第六项本身由刚付的整性也属于 $p^6$。
故六条**同五变量**必要行是
$$
F_\nu(x)=\sum_{h=1}^5
\frac{(-1)^{h-1}(h-1)!p^{h-1}}
 {q_\nu^h a^{h-1}}C_{\nu,h}(x)
\equiv\frac ap J_\nu'(0)\pmod {p^5}.
\tag{3}
$$
这只在 $x=0$ 读取原算术中央。其余 $x$ 是准确的有限参数 family。

## 2. 完整五位 Hensel 和定义明确的第六余式

写 $\lambda_{\nu,j}=[w^j]\nu$，
$$
B_5=(\lambda_{\nu,5},\ldots,\lambda_{\nu,1})_{\nu=S,T,U,V,W},
\quad
b_Z=(\lambda_{Z,5},\ldots,\lambda_{Z,1}).
$$
所有这些低项都来自同一次完整 CM 重生与原 ODE，未读旧输出表。
令 $T$ 是
$$
T_{i,r}=[w^{s-5+i}]t^{s-r},
\qquad i=0,\ldots,4,\quad r=5,4,3,2,1.
$$
$T$ 是整下三角，所有对角为 $\pm1$。式(3)的 Jacobian 模 $p$
恒为 $B_5T$，因为 $h\ge2$ 的项含显式 $p$，
而第一权只读五个真实低系数。

当实际 $\det B_5$ 为 $p$ 单位时，前五行有唯一
$$
x^\dagger\in(\mathcal O/p^5)^5,\qquad
F_S(x^\dagger)=\cdots=F_W(x^\dagger)=0 .
$$
定义
$$
\boxed{\mathfrak r_{Z|5,p}=F_Z(x^\dagger)\in\mathcal O/p^5.}
\tag{4}
$$
若六个完整原中央同时零，则前五原行使 $x^\dagger=0$，
所以必有 $\mathfrak r_{Z|5,p}=0$。
这一步并不假定一个原 Fourier 深核存在，也不向乘积传播中央零。

读者逐位计算 $x^\dagger$。已得模 $p^j$ 的解 $x_j$ 后，先验证
每个前五行的真实值被 $p^j$ 整除，再作实际整商；用同一个
$(B_5T)^{-1}\bmod p$ 解下一位。每一位更新后，再验证完整五条
式(3)至模 $p^{j+1}$。完成第五位后才读取式(4)。
没有以一阶线性 Schur 式替代高位非线性 Hensel。

## 3. 首位是一个固定六来源系数，不能删除其完整基准

在特征零准确求固定有理行
$$
\mathbf c=b_ZB_5^{-1}.
\tag{5}
$$
它与 $p$、原高轴和 Gaussian 无关。置
$$
\mathscr T=\frac Z{q_Z}
-\sum_{\nu=S,T,U,V,W}c_\nu\frac\nu{q_\nu},
\qquad
\Delta=Z-\sum_\nu c_\nu\nu .
\tag{6}
$$
于是
$$
\boxed{\mathfrak r_{Z|5,p}\equiv[w^s]\mathscr T\pmod p.}
\tag{7}
$$
证明：模 $p$ 的式(3)是仿射系统。用(5)消去共同 $T$ 后，
余式恰为 $F_Z(0)-\sum c_\nu F_\nu(0)$。
所有源质量为零，删 Gaussian 不改变它们的第一 $w^s$ 系数，
所以这个量就是(7)。

令 $\mathcal E=\Theta\partial_\Theta/17$，则
$$
\mathcal E\mathscr T=\Delta,\qquad
[w]\Delta=\cdots=[w^5]\Delta=0,
$$
$$
\boxed{[w^6]\Delta=-\frac{\det B_6}{\det B_5}\ne0.}
\tag{8}
$$
其中 $B_6$ 的列按 $w^6,\ldots,w$ 排序。
式(8)的负号来自将第六行减去(5)的前五行组合后，按第一列展开。
它说明这个固定差来源不是零函数；**不说明**其(7)在一般素数非零。
特别不能将 $w^6$ 的非零首项冒认为可变 $w^s$ 的单位。

读者以三条独立记账核(7)：最终五位 Hensel 余式的首位、
实际 $x=0$ 的六行首 Schur 组合、以及同一完整(6)的 $w^s$ 系数。
它不为后三者另选高轴。

## 4. 一个准确 whole-heat 入口

若继续使用 R855/R856 与固定 horizontal-frame 笔记，令
$m_\nu=2n_\nu$、$N=(p+1)/2$。在先于 $p$ 固定的共同水平覆盖上，
原纤维截面的质量为 $f_\nu^{\rm flat}$，且
$$
\mathfrak B_{m_\nu,p}
=(2m_\nu)^N\frac{(T_N f_\nu^{\rm flat})(\widetilde P)}p\pmod p.
$$
原 Hurwitz规范给
$[w^s]\nu\equiv-\mathfrak B_{m_\nu,p}$：
确实 $(p+1)!/p\equiv-1\bmod p$。
因每个分子在该实际点被 $p$ 整除，系数可在除 $p$ 后约化；
$$
\frac{(2m_\nu)^N}{q_\nu}
\equiv68\left(\frac{2m_\nu}{p}\right)\pmod p.
$$
故(7)准确化为
$$
\boxed{
\mathfrak r_{Z|5,p}
=-68\,\frac{(T_N f_p^{\rm ex})(\widetilde P)}p\pmod p,
\quad
f_p^{\rm ex}=
\chi_Z f_Z^{\rm flat}-\sum_\nu c_\nu\chi_\nu f_\nu^{\rm flat},
\quad \chi_\nu=\left(\frac{2m_\nu}{p}\right).}
\tag{9}
$$
覆盖、各 $f_\nu^{\rm flat}$ 和 $\mathbf c$ 全先于 $p$ 固定，
只有所示有限二次角色选择随 $p$ 变化。
需要排除的固定坏素数仍包括各水平覆盖及源分母的原坏集。

这里的分子除 $p$ 只在原 CM 点有定义；没有宣称它在整个参数曲线整。
六个质量各自恰三阶零，但其组合可能有更高阶抵消。
式(9)保全部 $T_N$、Riccati 半密度、双参数原提升及除 $p$ forcing，
不把它换成裸 $D^N$，也没有从(8)推出(9)非零。

## 5. 同次完整源读者及输入精度

新 helper 只导入已有 r941-original-six-digit-central-reader.py 的原递推函数，
其 SHA-256 固定为
b64be67a71cc0870acde67d27cf679db0a557030ce57ed13994e80c6f68dfd6d。
R941 从 $p^8$ 起算，完整两次真实除 $p$ 给
$\mathcal W_{\le p},f_{\le p}\bmod p^6$。这比(3)的五位需求多一位。
每个(2)的有限逆、幂和多项式组成均在该整窗内，
所有显示源分母、阶乘和 $q_\nu a$ 都是单位。

调用接口为
~~~python
check_sixth_overdetermination(coefficients, old.SOURCE_ASC, all_jets)
~~~
放在本次 E65 producer 的 sixth_actual_jet 中。
三个参数分别是本 job 的完整原66维 CM7/19源向量去质量顶项、
本 job 完整 E89 CM7/CM13唯一源、及本 job 六条原低 jet。
helper 不读取生成的输出表，不启动另一 CM producer，不写数据文件。

实际素数固定为227，不进行扫描。此输入使 $s=38$，
整个(3)只需要 $5s-1=189$ 的 inner 系数。
读者仍完整使用 R941 已付的六位输入，并核同一曲线身份；
六来源前六项再与同 job 的特征零 jets 逐项比较，
以防系数翻转、175缩放或新源号次被替换。

应登记的实际结论限于本次(4)的值及其准确赋值。
若非零，它排除**这个素数**的六中央同时零，并证明此实际第六有限行
没有在该纤维自动消失；若为零，它只表示五位内未排除。
两种结果都不证明原完整中央为零或非零的无穷素数命题。


## 6. 同一个完整 C24 三列上的实际消费

本节保持已有“同一 degree24 奇因子与三维真实差矩阵”笔记的全部
绝对规范。仍取 $b=1$、$X=x^3$、
$$
Q_2(X)=7X^2-4X+16,\qquad
C_{24}=-\sigma^{24}x^2yQ_2/7,
$$
$$
E_0=-\sigma^{24}x^8y,\quad
E_1=-\sigma^{24}x^5y,\quad
E_2=-\sigma^{24}x^2y,\qquad
c_*=(1,-4/7,16/7)^t .
\tag{10}
$$
所以 $C_{24}=\sum_jc_{*,j}E_j$，而
$E_j/C_{24}=7(-t)^j/h_7(t)$。
这里负号和原 $(-t)^j$ 列都不改变。

### 6.1 两个新 whole 奇伙伴

R943/R960 的同次完整源给
$$
W=\sigma^{178}x^2P_{28}(X),\qquad
Z=\sigma^{390}P_{64}(X).
$$
由真实 $f_W=\mathfrak a G_W$、$\deg G_W=25$，
以及 $f_Z=\mathfrak a G_Z$、$\deg G_Z=60$、$\deg f_Z=64$，有
$$
P_{28}=(X+1)Q_2R_{25},\qquad
P_{64}=X(X+1)Q_2R_{60}.
\tag{11}
$$
$R_{25},R_{60}$ 的最高系数均为 $1/7$。
helper 对同次完整系数向量作准确多项式除法，核(11)及两个最高系数；
不从几个低 jet 猜测全来源可除。

由 $y^2=X+1$，两个完整伙伴因此准确为
$$
\boxed{
J_W=-7\sigma^{154}yR_{25}(X),\qquad
J_Z=-7\sigma^{366}xyR_{60}(X),\qquad
W=C_{24}J_W,\quad Z=C_{24}J_Z.}
\tag{12}
$$
它们没有有限极。函数因子的最大极阶分别为
$3+6\cdot25=153$ 和 $2+3+6\cdot60=365$，
分别比 degree154/366 小一，故 whole 全纯，首项都恰为 $z$。
最低 $x$ 幂分别为零、一。所有固定分母及175缩放仍按原范围保留。
它们是同一个原 $C_{24}$ 的伙伴，没有将新伙伴视为新的算术中央。

### 6.2 原点与五轴 Hensel 点都保完整五乘三矩阵

对同一参数 $x=A-A^*$，令
$$
\nu_x=\nu\exp\!\left(q_\nu\sum_rx_rt^{s-r}\right).
$$
这些来源仍可在有限形式窗中写成 $C_{24,x}J_{\nu,x}$：
共同 $\sigma$ 因子改为
$\sigma_x=\sigma\exp(\sum_rx_rt^{s-r}/34)$，
所以各 degree 的指数准确相加。
这只定义原必要系统的有限形式 family，
不对 $x\ne0$ 声称原 CM 谱、Hecke 角色或通常 Selmer 运输。

令六源的 inner 级数为
$$
B_{\nu,x}=w^{-1}\nu_x e^{-q_\nu\kappa w^s}.
$$
全部系数都由第1–5节同一输入给出。在模 $p$ 定义
$$
\boxed{
M(x)_{\nu j}
=-[w^{s-1}]
 \frac{7(-t)^j}{h_7(t)}
 (B_{\nu,x}-B_{S,x}),
\quad
\nu=T,U,V,W,Z,\quad j=0,1,2.}
\tag{13}
$$
每一行、每一列都保留；没有只选择一个预期非零 minor。
因来源从 $w$ 起，Gaussian 的第一次改动从 $w^{s+1}$ 起，
所以(13)正是已有奇因子笔记的全部首差矩阵，既可由原
Hurwitz除 $p$ 式读取，也可由同一个完整低卷积读取。

原指定向量准确满足
$$
\boxed{M(x)c_*=
-\big([w^s](\nu_x-S_x)\big)_{\nu=T,U,V,W,Z}.}
\tag{14}
$$
证明只用
$$
\frac7{h_7(t)}
\left(1-\frac47(-t)+\frac{16}7(-t)^2\right)=1.
$$
因此这是原固定向量，不能分别将三列赋零。

在实际算术点 $x=0$，读者保存完整 $M(0)$ 的运行输出、秩和全部
右核基，且以(14)逐行比较原六源第一块。它不把(14)的五个值预设为零。

在五轴 Hensel 点 $x=x^\dagger$，前五行(3)模 $p$ 为零，
所以 $[w^s]\nu_{x^\dagger}=0$ 对旧五源全部成立。因此
$$
M(x^\dagger)_{\{T,U,V,W\}}c_*=0,\qquad
\operatorname{rank}M(x^\dagger)_{\{T,U,V,W\}}\le2,
$$
$$
\boxed{
M(x^\dagger)_{Z,\bullet}c_*=
-q_Z\mathfrak r_{Z|5,p}\pmod p.}
\tag{15}
$$
这给第六真实过定余式在同一三维有限像中的精确符号。
若实际旧四差行秩为二且(4)首位非零，则添加新行后的完整秩必为三；
若旧秩较低或余式首位零，读者按实际结果返回，不预设结论。
所有右核都对完整三列矩阵计算；其输出仅留在运行日志。

在(6)的固定来源组合中，共同奇高行的系数为
$$
\alpha_{\rm odd}=\frac1{q_Z}
-\sum_\nu\frac{c_\nu}{q_\nu}.
\tag{16}
$$
它也由同次准确有理 $\mathbf c$ 计算。
除非(16)实际为零，不能把这一公共高行从 whole-heat 表达删去。
(13)使用相对 $S$ 的差才完整消去该共同项，而(7)的一般线性组合
仍须保相应的 $S$ 行。这两种记账通过(14)–(16)相容。

本节与原 $W_{\rm low}$ 或 $K_1/K_2$ 的满像无关，
不把六低 jet 的独立性认作那个全局有限限制像的满射。


### 6.3 完整五位中央提升与同核的精确 Smith 消费

不仅可以读(13)模 $p$。定义十八个同源辅助截面
$$
A_{\nu,j}=E_jJ_\nu=\frac{7(-t)^j}{h_7(t)}\nu,\qquad
\nu=S,T,U,V,W,Z,\quad0\le j\le2 .
$$
由已有四伙伴和(12)，它们全部是各自 degree $m_\nu$ 中的 whole 截面，
在原点的阶至少六。每一行的三个 charge 相同，仍是 $q_\nu$。
$h_7(0)=7$ 为单位，且实际来源已含完整 $h_7$ 因子；
有限形式表达中的 $1/h_7$ 不产生真实几何极。
原严格圆盘上该逆的范数为一，Hurwitz 封闭性与第1节同一尾界
适用于全部十八个截面。

按(1)–(3)，对每个 $A_{\nu,j}$ 定义其完整五权必要值
$F_{\nu,j}(x)\bmod p^5$。只对这一步使用线性：
同一行内 charge 相同，故原整 Gaussian 和全 Newton 函数给
$$
\sum_{j=0}^2c_{*,j}F_{\nu,j}(x)=F_\nu(x)\pmod {p^5}.
\tag{17}
$$
不将任何一个单独的 $F_{\nu,j}$ 赋零。

置真正五位矩阵
$$
\boxed{\mathbb M(x)_{\nu j}
=-q_\nu F_{\nu,j}(x)+F_{S,j}(x)
\in\mathcal O/p^5,\qquad\nu=T,U,V,W,Z.}
\tag{18}
$$
它模 $p$ 恰为(13)，因第一权为裸系数除 $q_\nu$。
在所有 $x$ 都有完整恒等式
$$
\mathbb M(x)c_*=
(-q_\nu F_\nu(x)+F_S(x))_\nu\pmod {p^5}.
\tag{19}
$$
所以在同一个 $x^\dagger$，
$$
\mathbb M(x^\dagger)_{\{T,U,V,W\}}c_*=0,\qquad
\mathbb M(x^\dagger)_{Z,\bullet}c_*=-q_Z\mathfrak r_{Z|5,p}.
\tag{20}
$$
这保(4)后四位，没有把完整五位关系替成模 $p$ 的符号类比。

若实际旧四差行模 $p$ 的秩为二，则在
$\mathcal O/p^5$ 中，其整个右核恰为自由直线 $(\mathcal O/p^5)c_*$。
证明：取列基 $(e_1,e_2,c_*)$，其中
$e_1=(0,1,0)^t,e_2=(0,0,1)^t$。因 $c_{*,0}=1$，
该换基行列式为一。旧矩阵第三列严格为零，前两列模 $p$ 独立，
故有单位二阶 minor；单位消元给两个单位 Smith 因子和一条自由核。

将第六行加入后，清掉其前两列不改变第三列，准确得到唯一余项
$-q_Z\mathfrak r_{Z|5,p}$。因此完整新矩阵的截断 Smith 赋值为
$$
\boxed{
(0,0,\min\{v_p(\mathfrak r_{Z|5,p}),5\}),}
\tag{21}
$$
并且整个右核为
$$
\boxed{
\ker\mathbb M(x^\dagger)
=\{u\,c_*:\ u\,\mathfrak r_{Z|5,p}=0\text{ in }\mathcal O/p^5\}.}
\tag{22}
$$
若余式截断赋值为 $v<5$，该有限核由 $p^{5-v}c_*$ 生成、长度为 $v$；
$v=0$ 时为零，余式为零模 $p^5$ 时为完整自由直线。
“赋值五”在这里始终表示至少五，不能据此说实际余式严格为零。

helper 在 $x=0,x^\dagger$ 都计算完整五位矩阵及截断 Smith 赋值，
并逐行核(19)。Smith 步骤只在当前完整有限环中选择赋值最小的
主元，提取其 $p$ 幂后作单位消元；每次实际除法都检查整除。
当上述单位秩条件满足，另核(21)和(22)；若不满足，保实际矩阵、
全部模 $p$ 右核与完整截断 Smith，不增添该条件。

这是一份同 $C_{24}$、同 $c_*$、同六源、同五位 Hensel 的有限消费。
它没有把任何原 $W_{\rm low}$ 的环境维数认作实际 $K_1/K_2$，
也没有删除真实辅助截面的 Gaussian、共同奇行或最高 carry。



### 6.4 与原六源整数格的准确交：同一 $c_*$ 与两个完整角点

本节把上述三维测试空间接到 R960 的原来源格，而不把十八个
辅助截面各自作为免费来源列。
取包含 R960 全部固定单位的原系数环 $\mathcal O$；
所有结论也在 $\mathcal O/p^n$ 上逐字成立，$n\ge1$。
令
$
h_7=7+4t+16t^2,\quad a=t(t-1)h_7,\quad d=1+8t,
\quad
P_c(-t)=c_0-c_1t+c_2t^2 .
$
第6.3节的同一个测试向量 $c\in\mathcal O^3$ 给
$
A_{\nu,c}:=\sum_{j=0}^2c_jA_{\nu,j}
=\frac{7P_c(-t)}{h_7}\,F_\nu .
\tag{23}
$
这是一个共同的三维测试向量；不为每个来源另挑 $c$。

先看原 $S=\Theta^{17}ad/7$：
$
A_{S,c}=\Theta^{17}t(t-1)d\,P_c(-t),\qquad
B^{(6)}_{17}=\Theta^{17}a\,\mathcal O[t]_{\le1}.
\tag{24}
$
后一个帽准确来自 $\lfloor64\cdot17/195\rfloor=5$。
在 $\mathcal O[t]/(h_7)$ 内，$t(t-1)d$ 是单位：
$h_7(0)=7$、$h_7(1)=27$、$h_7(-1/8)=27/4$，
而 $2,3,7$ 都已在原好位范围中为单位。
这同时保留零角、$t=1$ 与 $d=0$ 的互素条件。
故 (24) 属于原 $B^{(6)}_{17}$ 当且仅当
$h_7\mid P_c(-t)$。
因为 $\deg P_c\le2$、$16$ 为单位，这又等价于
$
\boxed{c\in\mathcal O c_*,
\qquad c_*=(1,-4/7,16/7)^t .}
\tag{25}
$
若 $c=uc_*$，则 $7P_c(-t)=u h_7$，
所以全部六行同时准确为
$
A_{\nu,c}=uF_\nu .
\tag{26}
$
因此 (25) 不仅必要，还保证每个来源的所有其它有限角点、
无穷远帽及原 charge 完整返回。
并且它已经回到原六源环本身：这些就是六个已认证的原 $F_\nu$，
无需再乘 $S^2$ 或 $c_6$。反之，若六行都属于各自原来源格，
仅 $S$ 行就已迫 (25)。

这是一条 primitive 整直线，任意 $p^n$ 都没有额外模 $p^n$ 的
非法方向。具体地，准确满射为
$
\psi:\mathcal O^3\longrightarrow \mathcal O[t]/(h_7),
\qquad c\longmapsto P_c(-t)\bmod h_7,
$
$
\boxed{
0\longrightarrow\mathcal O c_*
\longrightarrow\mathcal O^3
\xrightarrow{\ \psi\ }\mathcal O[t]/(h_7)
\longrightarrow0.}
\tag{27}
$
取第6.3节同一 $e_1=(0,1,0)^t,e_2=(0,0,1)^t$。
它们的像为 $-t,t^2$；在基 $1,t$ 下，
$t^2=-7/16-t/4$，故二阶行列式是 $-7/16$，为单位。
这证明 (27) 是分裂自由整列，并证明所有 $p^n$ 的基变换相容。
不用选择 $h_7$ 的两个根，也不把几何分裂型作为假设；
它保的是同一个完整秩二有限代数。
由于判别式 $-432$ 为单位，其好位纤维也保原两个几何角点。

原六源环的正权部分在每个权都含 $h_7$，
且不同 $\Theta$ 权在原函数域中线性独立。
因此允许加入任意更高权的真实来源，也不能在全角多项式中
抵消 (24) 的权17非法余类。
事实上原六源环权17只有原 $S$ 直线，
所以同一个交还准确为
$
\operatorname{span}_{\mathcal O}\{A_{S,0},A_{S,1},A_{S,2}\}
\cap A^{(6)}_{\le N}
=\mathcal O S \qquad(N\ge17).
\tag{28}
$
这个陈述是在来源整环中的交，不是关于有限 Taylor 评价像的交。

现在回到同一个 $x^\dagger$ 和真正五位矩阵。
由 (20)，旧四差行杀掉 (25)，故它们**作为线性映射**
准确下降到 (27) 的整个秩二商。
若第6.3节的实际单位秩条件成立，这个商映到四行目标中是
primitive 单射。新增 $Z$ 行对唯一合法方向的值准确为
$-q_Z\mathfrak r_{Z|5,p}$。
于是 (21)–(22) 确实分别消费了两个非法除 $h_7$ 的余方向
及这个唯一合法的原六来源方向，没有把三列逐列当成原格。

必须区分两种映射：$\psi$ 是真实角点限制，
$\mathbb M$ 是完整 Gaussian/Newton 中央行；
它们不是同一个矩阵。
(27) 只给后者在实际杀掉 $c_*$ 后的准确商来源，
不把其值替成有限点的函数值。
同样，(28) 不排除高权来源在某个截断物理 jet 像中发生抵消；
该问题仍须使用 R960 的完整 $\mathcal J_6$ 和全部有序前缀。

六条原中央同时零时，原指定 primitive 向量 $c_*$
在这份共同测试空间中的像就是六个原 $F_\nu$，并被同一模 $p^5$ 整矩阵杀掉。
这是一个有实际原来源返回的受迫向量，不是任选核向量。
但它属于此处的中央测试矩阵；不能据此把它冒作
原 $\mathcal J_6$ 的 $p^6$ 右核，或赋给任何单个辅助截面新的中央零。

## 7. 同一原来源的实际运行及准确有限结论

公开 [run 45823614454](https://github.com/Rogerhu12/math-research-public/actions/runs/45823614454)，job `139921952585`，source commit `a39e5a6f88c9695ae43abcc6358679a422c4d5e8`，于 **2026-11-26 12:57:50 UTC** 成功。原入口 `scripts/check-original-e65-full-cm-sixth-axis.py`、参数 `--workers=4`、`python-flint=0.9.0`、请求 `ci/e65-full-cm-source-request.json` v3；共14个源码/参数文件、12个 Python AST。数学入口用时356.926008728秒。

E65完整390来源与旧E89完整178来源在同job各重生一次；全部64局部Schwartz门、全66列CM、旧六jet和原两来源哈希均保持。没有读取旧系数表、另重建一套CM或保存生成输出。固定 `p=227,s=38,precision=5`；原W/f两次真除p保六位，完整曲线关系、六个真实低jet、五次整Hensel与首位三路线全部返回。

准确得到
$$
\boxed{\mathfrak r_{Z|5,227}=233762530371\pmod{227^5},
\qquad \mathfrak r_{Z|5,227}\equiv157\pmod{227}.}
\tag{29}
$$
因此它是单位。在同一个五行Hensel必要值处，五条旧行严格为零模 $227^5$；完整原 $C_{24}$ 四个旧差行模227秩为二，加入第六源差行后秩为三，且
$$
M(x^\dagger)c_*=(0,0,0,0,162)^t\pmod{227}.
\tag{30}
$$
旧模227右核确为一条线，完整五行右核为零。由已证明的(17)–(22)，进一步严格推出**同一完整五位矩阵**的截断 Smith 为 $(0,0,0)$、整个右核为零。这里的五位结论来自已付代数定理与实际单位余式，不冒称运行了另一份完整五位输出。

在原算术值 $x=0$，旧四差行本身已为秩三；两个参数点在回执中分开保留。$x^\dagger$ 只属于本篇指定有限五轴 family，不附加CM本征或算术中央身份。由(4)，六条原中央不可能在这个素数同时为零；R941已证明这个素数的旧四中央非零，本次新增的是原五轴必要系统的真实第六排除和完整C24消费，不把同一个素数重新当跨素数成果。

### 7.1 复现摘要

- 入口 SHA-256：`8cfe88309ec81ac50a363ede36350696c4818cff1c5d23cebe4868a87ad9f96b`。
- workflow：`86567ee9a9c092d19c4144701933cd5118b6543573859663f6dc29e98f57c702`；request：`e93377bdb70fef640febc7ae836bd4b66e8cc6f3373686812c9cc73ddf9838c7`。
- 实际过定/C24 helper：`204b014a969916e34b3404e4372d47010ad15013b1b54e26798431ec1f196abd`。
- R941原读者：`b64be67a71cc0870acde67d27cf679db0a557030ce57ed13994e80c6f68dfd6d`。
- 同次六低jet摘要：`284d27873a50de529d722371656982e81fb960438fcdecec498cdab77a32d091`。
- 原manifest完整3263字节：`e5cf014aad41a38298c943c8fe1229bed6a2fcedec3c2fb9567f378a1d347b30`。
- 数学stdout完整25210字节：`08b4e721680bd5980e475547d5ec554d63596ef69d4f52b0b6dc4617932aa52a`。
- 完整job日志69656字节：`502f82e4cdfd2643ee2a3204dfdfc175eb4de308050ad3ea5a721a8902f72a3f`。

原结果无穷性字段、全深核字段均为 false。完整五位扩展 `scripts/held-original-sixth-on-five-axis-overdetermination-p5.py` 的 SHA-256 为 `abb46796a3d11f7e369ffef9e756079a0c2820a568efda221441258c9f3736d3`，仍未触发；不为可由上述单位条件直接推出的结论重复CM。

后续实际门是(9)的完整跨$p$非零或同来源全长像的联立排除。第六低jet独立、此一素数的单位和C24测试空间满秩，均不替代这一门。
