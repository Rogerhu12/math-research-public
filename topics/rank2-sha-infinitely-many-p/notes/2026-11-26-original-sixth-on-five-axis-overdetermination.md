# 第六原中央在旧五轴必要系统上的真实过定余式

日期：2026-11-26。**以下有限恒等式和读者的精度证明已证明；公开运行尚待执行，余式尚未被赋为零或非零。** 本注不扩成六个未知量，也不把一个有限余式的非零升级为无穷素数定理。

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


## 本次原来源执行

状态：源码和完整证明已提交；实际运行结果待返回，不预置零或非零。

同一 `check-original-e65-full-cm-sixth-axis.py` v3 入口先完整重生 E65 的 degree390 CM7/19 来源和原 E89 的 degree178 来源，各一次；两新消费者共享同次来源。固定参数为 `workers=4`、`python-flint=0.9.0`、过定系统 `p=227`、精度5；所有旧局部/六jet/角帽/六sigma门保持。原 h 的零投影作为准确结果保留，不将它误报为整个伴随张量为零。只存脚本、参数、run和摘要；不保存可重算输出。

- 入口 SHA-256：`8cfe88309ec81ac50a363ede36350696c4818cff1c5d23cebe4868a87ad9f96b`。
- workflow SHA-256：`86567ee9a9c092d19c4144701933cd5118b6543573859663f6dc29e98f57c702`。
- request SHA-256：`e93377bdb70fef640febc7ae836bd4b66e8cc6f3373686812c9cc73ddf9838c7`。
- 五轴过定及全部 C24 helper：`204b014a969916e34b3404e4372d47010ad15013b1b54e26798431ec1f196abd`。
- 含原 h 投影的六sigma helper：`027b26c944a37d94e4e12f2d2c13dbd98c9188a6de4ee5cea40332e013dc85bc`。

2026-11-26 12:51:37 UTC 挂入触发路径；实际 source commit/run/job 由下一条回执补齐。
