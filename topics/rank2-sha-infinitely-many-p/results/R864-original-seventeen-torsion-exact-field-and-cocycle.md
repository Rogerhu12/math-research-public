# R864 — 原十七挠点的九次方程、三次坐标与实际 Frobenius 因子

日期：2026-11-16。

**状态：已证明（符号 CM 识别加公开 Actions 中的精确有理数和数域运算）。** 本篇把 [R862](R862-original-seventeen-torsion-product-and-complete-cubic-hom-matrix.md) 的固定乘积 $h$ 和原 $\Lambda(\mathfrak l)$ 写成完整有限代数输入。运行不涉及研究素数扫描；这些有限域扩张也不随研究素数改变。尚未算出 R859 的一个非零原 shadow，主目标未完成。

## 1. 固定来源与计算环

沿 R862 固定
$$
K=\mathbf Q(\omega),\quad\omega^2+\omega+1=0,\quad
E_0:Y^2=X^3+1,\quad\delta=1+2\omega,\quad
\alpha=-1+2\omega.
$$
$\rho_{17}$ 的满像、Artin 方向和完整 $\eta_j$ 已由该篇(4)–(7)固定。
令 $\Psi_{17}\in\mathbf Z[X]$ 为这条曲线的标准17分点多项式：
$$
\deg\Psi_{17}=144,\qquad\operatorname{lc}\Psi_{17}=17,\qquad
\Psi_{17}(0)=-2^{96}.
\tag{1}
$$
R862 的满像使 $\Psi_{17}$ 在 $K$ 上不可约，故在 $\mathbf Q$ 上亦不可约。
计算用的
$$
\mathcal A=\mathbf Q[X]/(\Psi_{17}/17)
$$
是一个真正的域；记 $x$ 为 $X$ 的像。置
$$
R(X)=-\frac{X^3+4}{3X^2},\qquad
h=\prod_{i=0}^{15}R^{\circ i}(x),\qquad t=h^3.
\tag{2}
$$
R862 已证明所有分母非零、$R^{\circ16}(x)=x$，且(2)就是原
$G_{32}/\{\pm1\}$ 的乘积。计算不以另一个九次类域生成元代替它。

## 2. 完整最小多项式

在 $\mathcal A$ 中准确有
$$
\boxed{
h^9+1577949509713920h^6
+2711671378835304087552h^3
+\frac{79228162514264337593543950336}{17}=0.
}
\tag{3}
$$
常数分子等于 $2^{96}$。
因此 $t$ 的完整三次式为
$$
\boxed{
t^3+1577949509713920t^2
+2711671378835304087552t+\frac{2^{96}}{17}=0.
}
\tag{4}
$$

这里的“最小”有两个准确依据。第一，R862 已给
$[K(h):K]=9$、$[K(t):K]=3$。
第二，producer 把 $1,h,\ldots,h^9$ 在 $\mathcal A$ 的144维标准基中
写成一个 $144\times10$ 有理矩阵，其右核维数恰1，且核向量最后坐标非零。
把最后坐标归一为1，所得全部坐标正是(3)。
若存在次数至多8的关系，其与该核向量线性独立，矛盾。
程序再把(3)完整代回 $\mathcal A$ 核为零。
这不是根据少量数值近似或有限多个素数猜出的多项式。

更小的坐标是
$$
v=\frac{t}{2^{32}}.
$$
直接把(4)除以 $2^{96}$ 得
$$
\boxed{v^3+367395v^2+147v+\frac1{17}=0.}
\tag{5}
$$
它仍是同一个原三次子域 $L$，并有 $\operatorname{Norm}_{L/K}v=-1/17$。
缩放只用于表达坐标，不改变 R862 中固定的 $h$ 或 $\phi_h$ 的尺度。

## 3. 同一三次域的纯三次坐标

令 $a^3=17$。在抽象域 $\mathbf Q(a)$ 中，(4)恰有一个根，重数1：
$$
\boxed{
t=-525983169904640
  -204560702373888a
  -\frac{1352450841772032}{17}a^2.
}
\tag{6}
$$
等价地，
$$
\boxed{
v=-122465-47628a-\frac{314892}{17}a^2.
}
\tag{7}
$$
producer 在精确数域 $\mathbf Q[T]/(T^3-17)$ 中求根并代回；
(7)亦可直接用 $a^3=17$ 代入(5)验证。
它不是有理数，故生成整个三次域；于是(6)给
$\mathbf Q(t)\simeq\mathbf Q(a)$ 的明确坐标。

若把 $a$ 取为实立方根，(6)相当于选择 $t$ 的唯一实嵌入。
对 R862 起初任意选定的非零17挠点，这只是对该三次域的一个坐标同构；
其延伸到原 $H_9$ 时，$h$、Frobenius、Hom 和全部 Artin 系数同时运输。
下面保留 $t$ 基，故没有暗中另选 Galois 分支或改变原循环。

## 4. 定向的七次 CM 映射

置
$$
c_7=\frac{-2+6\delta}{7},\qquad
r_7(X)=
\frac{X^7+(12-28c_7)X^4+(7c_7^2-24c_7)X}
     {\alpha^2(X^3+c_7)^2}.
\tag{8}
$$
它满足
$$
7c_7^2+4c_7+16=0,\qquad
\boxed{
\frac{(X^3+1)r_7'(X)^2}{\alpha^2}=r_7(X)^3+1.
}
\tag{9}
$$
第二式是 $K(X)$ 中的精确有理函数恒等式；清分母后逐项用
$\delta^2=-3$、$\alpha=\delta-2$ 即可验证，producer 也完整核了该恒等式。

所以
$$
(X,Y)\longmapsto
\left(r_7(X),\frac{r_7'(X)Y}{\alpha}\right)
\tag{10}
$$
给 $E_0$ 到自身的非恒定有理映射，延拓为射影光滑曲线间的态射。
由于 $r_7(X)\sim X/\alpha^2$，它把 $O$ 送到 $O$，因而是椭圆曲线同态；
且
$$
(10)^*\frac{dX}{2Y}=\alpha\frac{dX}{2Y}.
$$
在特征零 $\operatorname{End}_K(E_0)=\mathcal O_K$ 的微分表示单射，
故(10)恰是原 $[\alpha]$，而非其共轭或另一个七次同源。

由于 $\alpha$ 的范数为7，核不含非零17挠点，故(8)在全部计算点上分母非零。
令 $\sigma=\operatorname{Art}_{H_9/K}((\alpha))$，则
$$
h^\sigma=h(r_7(x)),\qquad
\ell=\Lambda((\alpha))=\frac{\alpha h}{h^\sigma},\qquad
\tau=\sigma|_L.
\tag{11}
$$
这里 $h(r_7(x))$ 指(2)所得有理函数在同一分点域内代入。
R862 固定的 CM Frobenius 方向保证(11)正是原因子，不能换成任意范数解。

## 5. $\tau$ 与 $\ell$ 的全部坐标

用基 $(1,t,t^2)$，写
$$
\tau(t)=A_0+A_1t+A_2t^2,\qquad
\ell=B_0+B_1t+B_2t^2.
\tag{12}
$$
以下每一项均在 $K=\mathbf Q\oplus\mathbf Q\omega$ 中：

| 系数 | $1$ 的坐标 | $\omega$ 的坐标 |
|---|---:|---:|
| $A_0$ | $-107830658604204032/205$ | $107818332282945536/205$ |
| $A_1$ | $4015398270471/13120$ | $4015398277031/6560$ |
| $A_2$ | $21858753/112699941847040$ | $21858753/56349970923520$ |
| $B_0$ | $21905009/25505280$ | $-11561011/12752640$ |
| $B_1$ | $56176995091/54772171737661440$ | $13643765191/27386085868830720$ |
| $B_2$ | $305813/470489372688302752640532480$ | $74273/235244686344151376320266240$ |

producer 在 $\mathcal A_K=K\otimes\mathcal A$ 内准确计算(11)，再用
$1,t,t^2$ 的144维坐标解两个 $144\times3$ 线性系统。
求解后完整乘回矩阵；不是只检查三条选出的行。
随后又逐次代入(12)，核得
$$
\boxed{
\tau(t)\ne t,\quad\tau^3(t)=t,\quad
\ell\,\tau(\ell)\,\tau^2(\ell)=-1-19\omega.
}
\tag{13}
$$
这与 R862 的 $c=\alpha^3\omega^2=-1-19\omega$ 一致。
最关键的识别是(11)本身；(13)单独不足以指定原 $\Lambda$。

例如用较小坐标 $v=t/2^{32}$，同一 $\ell$ 可直接约成
$$
\boxed{
\ell=
\frac{
21905009-23122022\omega
+(112353990182+54575060764\omega)v
+(305813+148546\omega)v^2
}{25505280}.
}
\tag{14}
$$
(14)只是表中 $B_i$ 的精确换基，不添第二次实验或新的范数根。
从(11)还直接恢复
$$
h^\sigma=\alpha h/\ell .
\tag{15}
$$
因此不需要存一个144维的 $h^\sigma$ 大向量，便已得到 R862 所需的
全部实际 Galois 数据。

## 6. 回到原 Hom 矩阵

令 $b^3=c=-1-19\omega$、$b_j=\omega^jb$，
$(F_0,F_1,F_2)=(g_{10},g_{16},g_4)$。由(12)计算 $\tau^2\ell$ 后，
R862 的全部矩阵由
$$
u_0=1,\quad u_1=\tau^2\ell,\quad u_2=c/\ell,\qquad
G_j=1+\frac{u_1}{b_j}+\frac{u_2}{b_j^2},\qquad
M_{ij}=\frac h3b_j^iG_j
\tag{16}
$$
明确给出。
表中的所有分母、$\phi_h^*\omega_0=h\omega_C$ 的尺度、
完整二处 $\Lambda((2))=-2$、原准同态的整数清分母 $n$
及 R859 的整数 $D$ 都继续保留。
不能从特征零表格或 $\det M\ne0$ 宣称任意约化素数处为单位。

本篇解决的是原实际代数输入，而非原 Jacobian 态射的全局函数坐标。
下一步是在同一 $X_0(2601)$ 上恢复这些真实映射，随后代入 R859 的
完整交点/迹公式。所有原 $q_0,q_2$、Artin 组合、闭点重数仍在。

## 7. 完整 producer、运行与可重算标识

- 脚本：[produce-original-seventeen-torsion-input.py](../scripts/produce-original-seventeen-torsion-input.py)。
- 参数：[seventeen-torsion-input-request.json](../ci/seventeen-torsion-input-request.json)：
  $E_0=[0,0,0,0,1]$，$\ell_{\rm tors}=17$，轨道长16，
  $\delta=1+2\omega$、$\alpha=-1+2\omega$。
- workflow：仓库根下 $.github/workflows/rank2-sha-seventeen-torsion-input.yml$。
- 固定源码提交：$062a0c64d11a5d07a33d775235f5f0a7efcb0876$。
- 公开 [Actions run 43822409558](https://github.com/Rogerhu12/math-research-public/actions/runs/43822409558)，
  job $133148299804$，attempt1；2026-11-16 07:15:33 UTC 完成，
  精确数学部分约5.440秒，Sage10.6。
- image：$sagemath/sagemath@sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb$。
- producer SHA-256：$69a6001b2a1864a6faee7000640d195eefbd8564f9d15675f4dbbd179c6c3c46$。
- 完整规范输出 SHA-256：$6ba8a52b271276b1491076837bc1570df78922a0486eb9b246e529995eb1f53f$。
- $\Psi_{17}$ 升幂系数列表 SHA-256：$87d348b4f96b4b503a5aba042dea8aacbdfed01a6ffbc3771339c77834545d30$。
- $h$ 的144维标准代表 SHA-256：$09e8b78c9068d6ea8c55d5167c685d604924aa504d2c23cc0387e7163462964c$。

哈希编码由脚本的 $canonical$ 函数确定。
只保存脚本、参数、run/hash 和上述数学结论；不入库或上传可重算输出、
144维中间向量、分块或 Release 数据。脚本有公开 Actions 环境门，
数学执行均在本公开仓库完成。
