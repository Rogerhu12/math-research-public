
# 原 Q11 的 Manin 值与完整超奇异接触：公开 consumer

日期：2026-11-27。会话：Astra-rank2-Sha-0b097461-20261127。

**状态：原公式及完整消费算法已证明；新数学执行结果待。**
本输入只消费 R1036 已付的唯一原截面，计算 R1043§19 的新
$\mu(Q_{11})$；不重跑任何极除子枚举、两覆盖平方根或 Norm。

## 1. 唯一实际来源

实时只读的原公开回执固定为：

- run 45968889219、job 140404155125；
- source 3d702b7bc21923e82270953022b09b0950bb4adf；
- request 2026-11-27-0850-original-q11-all-minimal-poles；
- script check-original-q11-all-minimal-poles.py；
- script SHA256
  ecc383aa7ae9603e5b48e6490d4273bb778994c6e5851447393f6c8a5dbc5a03；
- stdout 3843 bytes、SHA256
  fda5154eea5725d118bc78383d6f9bac059c9384c2e0f0ee94c4abce99230ecd；
- enumeration SHA256
  af5567090bed1c212eda796cf0d8cf984b4c9085cfa19cbd03c2af152df3f357。

沿既有 lift-original-q11-section-to-two-cover.py 的严格 reader
核 run/job/source、唯一 timestamped 原 stdout/receipt、成功状态、
请求/源码/输出哈希及完整原数学状态。
该 helper 的固定 SHA256 为
812fd5e5a8899e2b47095c2eee50e22ba5b7063397121a0e44ec8801d1fe3b43；
只加载其定义，**不调用 main**。
新脚本为 consume-original-q11-manin-contacts.py。
没有把旧 stdout 或生成系数缓存进源码。

## 2. 真实函数域公式

使用完整域
$\mathbf F_{11}(X)[V]/(V^2-4X^3-1)$，
$Y=(V-1)/2$、$t=-Y/27$。
原点的 $x,W$ 从上述实际回执读取。
对 $f=a(X)+Vb(X)$，
$$
 D_Bf=(4X^3+1)b'(X)+6X^2b(X)+Va'(X),\qquad
 D=\frac X9D_B .
$$
这是原不变微分对偶的真实推导，不以有限点拟合。
按 R1043(101)计算
$\mu(Q_{11})/\delta$，$W$ 的符号和 $\delta^2=-3$ 均固定。

R1043§19已证明该函数在原有限仿射 $B$ 上正则；
所以约分后必须严格落在
$\mathbf F_{11}[X]\oplus V\mathbf F_{11}[X]$。
脚本返回这个必要的新函数及原短模型的 Hasse 函数；
先完整核短模型身份，没有另外再枚举点。

## 3. 全 Hasse 除子的厚接触，不作点采样

令 $R=\mathbf F_{11}[X,V]/(V^2-D_0)$，
$D_0=4X^3+1$。
若 $f=a+bV$、$g=c+dV$，则理想 $(f,g)$ 作为
$\mathbf F_{11}[X]$ 子模由完整四行
$$
 (a,b),\quad(D_0b,a),\quad(c,d),\quad(D_0d,c)
$$
生成。其全六个 $2\times2$ minor 的首一 gcd 是
$\operatorname{Fitt}_0(R/(f,g))$。
因此 gcd 的次数准确等于这个有限商的
$\mathbf F_{11}$ 维数。

把 $f=A_{11}^n$、$g=\mu(Q_{11})/\delta$ 代入，
$1\le n\le10$，得到
$$
 \ell_n=
 \sum_{\substack{b\ {\rm finite}\\A_{11}(b)=0}}
   \deg(b)\min\{n,\operatorname{ord}_b\mu(Q_{11})\}.
$$
Hasse 简单零由原完整
$(A_{11},D_BA_{11})$ 商长度为0返回，
其全有限次数是9。
所用 $R$ 是原光滑曲线的完整仿射环；
上式包括 $V=0$ 的分歧点、非有理闭点及所有重数。
没有把 resultant 的一个重因子误当作一个 reduced 点。

差 $\ell_n-\ell_{n-1}$ 给 $\mu$ 阶至少 $n$ 的几何点数。
R1043(105)使其准确给原 $Q_{11}$ 与 prime-to-11 torsion
叶的接触阶；此处没有目标 $p$ 的猜测。

## 4. 无穷点与两坏纤维也完整保留

若 $\mu/\delta=a(X)+Vb(X)$，
无穷点 $O$ 的极阶是
$$
 d_\mu=\max\{2\deg a,\ 2\deg b+3\}.
$$
两项奇偶不同，不能发生首项相消。
原 $\nu$ 在 $O$ 的阶正是 $11-d_\mu$；
这里使用 canonical 极小模型，不直接把 raw 微分代入。

在两乘法纤维 $X=0,V=\pm1$，$X$ 是真正参数。
脚本由 $V^2=1+4X^3$ 的唯一两个形式分支求
$\mu$ 的完整阶；$\nu$ 的阶各减去 KS 的一阶极。
总零度固定为9。
剩余非超奇异、非 cusp 零的次数由完整全局度数准确求得，
不是把未显示点忽略。

## 5. 本次实际作用范围

本次新计算能明确回答：已经构造的原 $Q_{11}$ 在完整
超奇异纤维上是横截还是具有何种真实高接触。
它还给一般 $q$ 的 Manin 公式一个可消费的真实具体来源。

它不把 $q=11$ 的有限数据外推到一般 $q$，
不把 characteristic-$q$ descent 改名为目标-$p$ 非零，
也不从 $p$ 除点存在推出接触阶增加。
原三个完整带权 $J_j$ 的非零、通常全 $\Sha$ forcing
及无穷不同 $p$ 仍需原链真正完成。


## 6. 启动前的根审与唯一请求

根已逐项手核实际KS导数、短模型身份、δ^q=−δ的符号、Broumas规范和全Tate边界；检查完整四行的六minor确给Fitting长度、Hasse所有闭点和分歧点均保留、canonical O与两cusp计入总零度。helper全文定义审过，其main不被调用。当前源码10074 bytes / SHA256 119c2f8d55e993732f346b042dd5ac95578b866930b4a3eba67705039213e0fd。沿既有rank2-sha-small-public-check.yml，python-flint 0.9.0；request 2026-11-27-1444-original-q11-manin-contacts。执行前不记PASS；新输出/日志不入库。
