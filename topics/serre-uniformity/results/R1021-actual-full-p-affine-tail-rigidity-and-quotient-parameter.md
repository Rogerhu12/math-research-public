# R1021：真实 full-\(p\) 仿射尾的模 \(p\) 常数化与商同源参数

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；global_route / root。

**已证明：在实际 full-\(p\) 变形环中可取 tame eigenparameters，
使 Drinfeld 仿射尾在模 \(p\) 的整个非约化基底上为常数模型；
真实普通 \(p\)-商的 target 参数为
\(\varepsilon(c_Q\psi+pR_Q)\)，其中 \(c_Q\) 是保留的常数单位。**
这比只确定特殊纤维或首个形式层强，但只控制仿射尾及所指函数。
节点处全部极部、跨尾 Frobenius 校正和实际对数仍需另算。

## 1. 同一个局部来源及精确环

令 \(p>3\)，\(k=\overline{\mathbf F}_p\)，\(W=W(k)\)。
固定原辅助 prime-to-\(p\) 标记下的一个超奇异椭圆曲线。
Serre–Tate 等价将其 full-\(p\) 局部问题识别为同一个 height-two
一维形式群的 Drinfeld level-one 变形问题；不先固定 Weil pairing。

记其完整局部环为 \(R_{\mathrm{full}}\)。
Strauch §2.1、Theorem 2.2 给：

- \(R_{\mathrm{full}}\) 是维二正则完整局部 \(W\)-代数；
- 两个原 level 坐标 \(x_0=T(P),y_0=T(Q)\) 构成正则参数；
- level 换基 \(\mathrm{GL}_2(\mathbf F_p)\) 与 framing 自同构群交换。

取 framing 群中的 \(\mu_e\)，其中 \(e=p^2-1\)。
使用 Strauch 的右作用约定
\((X,\iota,\phi)\cdot(g,b)=(X,\iota\circ b,\phi\circ g)\)，
并把 \(b=\zeta^{-1}\) 对应的作用记为 \(g_\zeta\)。
它在两 level 坐标的 cotangent 上同乘 \(\zeta\)。
这是 framing 在特殊形式群参数上的线性项；
也与 Strauch Theorem 4.4 证明中 CM specialization 对挠点的
\(b^{-1}\) 作用一致。此作用固定系数环 \(W\)。

有限平均给真正的参数
\[
x=\frac1e\sum_{\zeta\in\mu_e}\zeta^{-1}g_\zeta(x_0),\qquad
y=\frac1e\sum_{\zeta\in\mu_e}\zeta^{-1}g_\zeta(y_0).
\tag{1021.1}
\]
它们与 \(x_0,y_0\) 有同一线性项，仍构成正则参数，并满足
\(g_\zeta(x)=\zeta x,\ g_\zeta(y)=\zeta y\)。
同一个平均也可先在通用形式群的参数 \(T\) 上作，再在 \(P,Q\)
处评价，所以两参数可同时保持 \(x=T(P),y=T(Q)\) 的实际来源。
这是对真实变形环的坐标选择，不将特殊纤维的抽象
Deligne–Lusztig 曲线假装成实际高阶模型。

## 2. Cohen 方程的完整次数约束

参数给一个满射
\[
W[[X,Y]]\longrightarrow R_{\mathrm{full}},\qquad X\mapsto x,\quad Y\mapsto y.
\]
其核是高度一主理想：源正则，目标为维二整环。
可取生成元 \(f\) 使 \(f(0,0)=p\)。
具体地，\(p\in(x,y)R_{\mathrm{full}}\)，故核中有
\(p-F(X,Y)\)，\(F\) 无常数项；任一主生成元的常数项必须是
\(p\) 乘一个 \(W\)-单位，遂可归一为 \(p\)。

在源上令 \(g_\zeta(X,Y)=(\zeta X,\zeta Y)\)。
核稳定，故 \(g_\zeta(f)=u_\zeta f\)；
代入原点得 \(u_\zeta(0,0)=1\)。
所以平均 \(e^{-1}\sum_\zeta g_\zeta(f)\) 仍是同一理想的生成元，
且现在精确 invariant。于是
\[
\boxed{\quad
f=p+F_e(X,Y)+F_{2e}(X,Y)+F_{3e}(X,Y)+\cdots,
\quad F_{je}\text{ 齐次、总次数 }je.
\quad}
\tag{1021.2}
\]
不存在其它正总次数。

Drinfeld level 定义给乘 \(p\) 级数的根乘积。
取 \(T\) 的一次系数，
\[
p=\text{单位}\cdot
 \prod_{(a,b)\in\mathbf F_p^2\setminus\{0\}}
 T(aP+bQ).
\]
每个因子的初始形式为 \(a x+b y\)。
正则环的 associated graded 是 \(k[x,y]\)，故乘积初始形式非零；
它是非零常数乘
\((X^pY-XY^p)^{p-1}\)。因此
\[
\overline{F_e}(X,Y)
 =c_0(X^pY-XY^p)^{p-1},\qquad c_0\in k^\times.
\tag{1021.3}
\]
这里保留常数，不为后续微分比较把它任意设为一。

## 3. 实际仿射尾及所有 level 作用模 \(p\)

令
\[
\mathcal O=W[\varpi]/(\varpi^e-p),\qquad
x=\varpi\alpha,\quad y=\varpi\beta .
\]
在对应 radial chart 中，将 (1021.2) 除以 \(p=\varpi^e\)：
\[
1+F_e(\alpha,\beta)+pF_{2e}(\alpha,\beta)
 +p^2F_{3e}(\alpha,\beta)+\cdots=0.
\tag{1021.4}
\]
这里使用 \(\varpi\)-进完成的仿射 chart；所示齐次项带递增的 \(p\)
幂，故构成该环中的收敛表达式。它是 R1018 所用 full-\(p\)
尾仿射开在 normalization/blowup 中的真实坐标。
模 \(\varpi\) 时 (1021.4) 光滑，故该开已正规，没有另一个
未计入的 normalization 修改。

置
\[
C=\alpha^p\beta-\alpha\beta^p.
\]
模 \(p\) 的方程准确为 \(1+c_0C^{p-1}=0\)。
各因子因 \(p-1\) 为单位而互素；在一个选定 Weil 分支上，
对某个 \(c\in k^\times\)，得到
\[
\boxed{\quad
\mathscr R/(p)\simeq
(\mathcal O/(p))\otimes_k k[\alpha,\beta]/(C-c).
\quad}
\tag{1021.5}
\]
\(\mathscr R\) 表示所选仿射支的实际完成坐标环。
右侧的 \(\mathcal O/(p)=k[\varpi]/(\varpi^e)\) 非约化；
因此 (1021.5) 不仅仅是特殊纤维 \(\varpi=0\) 的描述。

再取任一实际 level 换基 \(g\)。
它与 framing 作用交换，所以 \(g(x),g(y)\) 在
\(W[[X,Y]]\) 中可用总次数 \(1\bmod e\) 的 eigen series 表示：
\[
g(x,y)=L_g(x,y)+
 \sum_{j\ge1}(G_{g,1+je}(x,y),H_{g,1+je}(x,y)).
\]
线性项模 \(p\) 是原 \(\mathbf F_p\) 换基矩阵。
除以 \(\varpi\) 后，其余项全含 \(p^j\)。
故在 (1021.5) 上，所有 level 作用准确为原线性作用，
会按 determinant 运输 Weil 分支。
固定分支时仅使用其真实稳定子；不把移动分支的元素误称为该支自同构。

对实际阶数 prime-to-\(p\) 的商，取不变量与模 \(p\) 交换，
因为有限平均给精确的 Reynolds 投影。
因此原非分裂正规化子及辅助 tame 稳定子所给仿射尾的相应结论
由真实商继承。这里没有对整个紧化曲线或节点作常数化断言。

## 4. 真正普通 \(p\)-商的 target eigenparameter

回到 R1018 的同一个
\[
\phi:E\longrightarrow E'=E/\langle Q\rangle .
\]
保原 \(Q\)-线、原六标记的运输和实际 target 辅助坐标。
令 \(u'\) 为 \(E'\) 的通用 height-two 变形参数。
在特殊纤维 \(\phi\) 是 Frobenius，故 source framing 的线性权
\(\zeta\) 在 target 成为 \(\zeta^p\)。
target 参数的权因此为
\[
(\zeta^p)^{1-p}=\zeta^{p-1}.
\]
可在 target 变形环先作 tame 平均，取精确的这个 eigenparameter；
其 linear term 仍是 Hasse 的非零单位倍。
因而 \(u'\) 在 \(R_{\mathrm{full}}\) 中有只含总次数
\(p-1\bmod e\) 的代表。

其最低齐次部分准确为
\[
u'\equiv \overline c_Q\,y^{p-1}\pmod{\mathfrak m^p},
\qquad \overline c_Q\in k^\times.
\tag{1021.6}
\]
这正是 R1018 的实际 norm derivative / Hasse 简单零计算：
\(\phi\) 的微分首项由
\(\prod_{a\in\mathbf F_p^\times}(-ay)=-y^{p-1}\) 给出，
而 target Hasse 是它的常数单位倍。
同一结论适用于 (1021.1)，因为该坐标更换在线性项为恒等。
没有用任意抽象 height-two 群替换原商同源。

取任一单位提升 \(c_Q\in W^\times\)，并令
\[
\varepsilon=\varpi^{p-1},\qquad
\varepsilon^{p+1}=p,\qquad \psi=\beta^{p-1}.
\]
低次部分中可能的 \(p\) 倍差以及更高次数
\(p-1+je\) 的各项，在 radial chart 上均多一个 \(p\)。
因此得到比单独模 \(p\) 同余更明确的式子
\[
\boxed{\quad
u'=\varepsilon\bigl(c_Q\psi+pR_Q\bigr),
\qquad R_Q\in\mathscr R.
\quad}
\tag{1021.7}
\]
在原 \(e_1\) 细辅助点，可写实际
\(b_{\mathrm{lift}}=B_s(u')\)，其中
\(B_s\in W[[u']]\)、\(B_s(0)\bmod p=b_s\)、\(B_s'(0)\in W^\times\)。
\(B_s(0)\) 是该 eigenparameter 零点给出的未分歧提升，不预称它为
\(b_s\) 的 Teichmüller 提升。
它是同一六标记 moduli 的真实坐标更换，不能将其二、三阶项删掉。

同理，source eigenparameter 的权为 \(\zeta^{1-p}\)，
最小可能总次数是 \(p(p-1)\)，故 source 参数属于
\(\varepsilon^p\mathscr R\)。
这说明 target 的 \(\varepsilon\) 层与 source 的
\(\varepsilon^p\) 层来自实际 deformation map 的不同权。

**精度范围。** \(R_Q\) 只在所指仿射尾上正则。
本篇不声称它在紧化后的节点无极点；
也不从一个 \(m\) 次方模 \(p\) 等式直接取得同精度的 \(m\) 次根。
节点过渡和除 \(p\) 后的对数计算必须另外保留这些误差。

## 5. 同一首 gap 的显式 Frobenius nullhomotopy

在 (1021.5) 上定义 Dickson 多项式
\[
\mathcal D=
 \frac{\alpha^{p^2}\beta-\alpha\beta^{p^2}}
      {\alpha^p\beta-\alpha\beta^p}.
\]
分子可被分母整除，所以这是多项式。
它是根多项式
\[
\prod_{a,b\in\mathbf F_p}(T-a\alpha-b\beta)
 =T^{p^2}-\mathcal D\,T^p+C^{p-1}T
\tag{1021.8}
\]
的实际系数，因而对 level 的 \(\mathrm{GL}_2(\mathbf F_p)\)
换基 invariant。

取 \(\psi=\beta^{p-1}\)，直接分组 (1021.8)，或直接乘以 \(C\)，给
\[
\boxed{\quad
\mathcal D=\psi^p+\frac{C^{p-1}}{\psi}.
\quad}
\tag{1021.9}
\]
这是原 full-\(p\) 坐标中的等式，不只是
“某个 Frobenius 作用为零”的存在断言。

在 R1018 的 \(p\equiv11\bmod12\)、\(e_1\) 尾上，令
\(m=(p-1)/2=2h-1\)。
选普通节点的同一个局部分支，原比较给
\[
\psi=z^{-m}(1+Az^{p+1})^{-1/2}
\]
至读取其全部负次主部的精度；唯一负次项是 \(z^{-m}\)。
\(\mathcal D\) 对实际商群 invariant，故下降为尾仿射开上的
正则函数；而 \(1/\psi\) 在这个节点正则且消失。
于是 (1021.9) 精确给出
\[
[\psi^p]=0\in H^1(C_s,O_{C_s})
\]
所需的同一 Čech 消去函数 \(\mathcal D\)。
这里的 \(\psi\) 是所选节点的局部来源，
没有把它误称为整个非分裂商尾的全局正则函数。

在平滑后的全图上，余项 \(C^{p-1}/\psi\) 会通过真实节点过渡
返回 Igusa 中心，再可能返回其它尾；
(1021.9) 不使这些全局返回项自动为零。
因为 \(\varepsilon^{p+1}=p\)，实际对数的 degree-\(p\) 项
除以 \(p\) 后，二次的跨尾变形可能恰好与原
\(\varepsilon\) 层同阶。该项仍须计算。

## 6. 来源、核准及继续范围

- Strauch, *Geometrically connected components of Lubin–Tate deformation
  spaces with level structures*, [arXiv:math/0611121](https://arxiv.org/pdf/math/0611121),
  §2.1、Theorem 2.2 与 Theorem 4.4 的证明：
  本篇实际使用正则参数、两个交换作用及 framing 的准确方向。
- [R1018](R1018-original-CM-divisor-exact-first-formal-layer.md)：
  同一个普通 quotient-isogeny、六标记、norm derivative、
  原 \(\psi\) 的 node 主部及完整形式点最早层。
- [R1019](R1019-original-CM-killing-correspondences-preserve-first-formal-layer.md)：
  实际 CM-killing Norm 函数及仍需计算的对数。
- Edixhoven–Parent,
  [stable model](https://websites.math.leidenuniv.nl/edixhoven/publications/2021/xpnonsplit_model_documenta.pdf)
  §§2–3：本篇的 radial chart 与原 full-\(p\) 尾及 tame 商的既定识别。

global_route 与 root 纸面核准 Cohen 生成元的常数项、
平均仍为生成元、全部齐次次数、非约化模 \(p\) 基底、
真实 level 换基、target framing 的 Frobenius 权、
\(pR_Q\) 的准确仿射范围及 (1021.8)–(1021.9) 的全部项。
未执行数学程序，未重算已成窗口。
真正的全局 log 首项、非 CM 简单商的整投影与 O0 覆盖仍 OPEN，
不以本局部精度结论代 Serre 完成。
