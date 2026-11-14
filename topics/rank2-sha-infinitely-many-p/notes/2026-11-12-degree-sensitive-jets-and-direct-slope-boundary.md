# 次数敏感的全部 jet 预算与直接乘积公式门槛

日期：2026-11-12。**已证明。** 本篇直接处理 R158 的
$k\log D$ 项，不将 $D\asymp k^{1/3}$ 代入后冒称完整
arithmeticity。得到的是原三维图像的严格预算门槛；惰性位的
所需改善尚未证明，因此主目标未完成。

## 1. 一个只用真实饱和旗标的命题

设
$$
 \gamma(w)=(f_1(w),\ldots,f_r(w)),\qquad f_i\in w\mathbb Q[[w]]
 \tag{1}
$$
是整函数组成的曲线，且 $f_1,\ldots,f_r$ 在 $\mathbb C$ 上
代数独立。假定存在 $C_0>0,\rho>0$，使对每个 $R\ge1$，
$$
 \sup_{|w|\le R}\log\max(1,|f_1(w)|,\ldots,|f_r(w)|)
                  \le C_0(1+R^\rho).
 \tag{2}
$$
这是显示的有限型增长界，不只是一个未付型常数的阶数记号。

令
$$
 E_D=\bigoplus_{|\alpha|\le D}\mathbb Z X^\alpha,\qquad
 N_D=\binom{D+r}{r},
 \quad r_k(P)=[w^k]P(\gamma(w)).
 \tag{3}
$$
在每个有限位使用单项式系数的最大范数，在实位使用同一
单项式基的 Euclidean 范数。始终保留饱和前缀
$$
 K_{D,k}=\ker_{\mathbb Q}(r_0,\ldots,r_{k-1})\cap E_D,
 \qquad
 \varphi_D^k=r_k|_{K_{D,k}\otimes\mathbb Q}.
 \tag{4}
$$
如果 $r_k$ 不增加秩，则该层为零，不计入下文的非零层。
目标是系数 $[w^k]$ 的原平凡化，未换成第 $k$ 阶导数格。

**命题。** 假设对全部 $D,k\ge1$ 的非零层，有统一的有限位界
$$
 \sum_p\log\|\varphi_D^k\|_p
     \le a k\log D+b k\log k+C_1(k+D),
 \qquad a,b\ge0,\quad b<\rho^{-1}.
 \tag{5}
$$
则必有
$$
 \boxed{\qquad
 r\le\frac{a+\rho^{-1}}{\rho^{-1}-b}.
 \qquad}
 \tag{6}
$$
可以在 (5) 中删去固定有限个素数，只要另外付清它们的
$O(k+D)$ 贡献。不能删去一整个尚未估计的惰性素数集合。

## 2. 适配的整数基与准确的范数恒等式

代数独立性使 $E_D\otimes\mathbb Q\to\mathbb Q[[w]]$ 单射。
因此 (4) 恰有 $N_D$ 个非零的一维跳跃。按顺序记其阶数为
$$
          0\le k_1<k_2<\cdots<k_{N_D},
          \qquad k_i\ge i-1.
 \tag{7}
$$
在本篇的整个多项式格中 $k_1=0$。这层为常数层，所有位的
范数都是一。每个 $K_{D,k}$ 都是饱和子格，故各个非零
商 $K_{D,k_i}/K_{D,k_i+1}$ 是秩一自由 $\mathbb Z$ 模。
清除有限矩阵的有理分母后使用 Smith 正规形，也可见这个
饱和格的 $p$ 完备化就是原 $\mathbb Q_p$ 核与
$\mathbb Z_p^{N_D}$ 的交，没有改变 R158 的局部源格。

逐层选其原始生成元的提升 $u_i$。可以选成 $E_D$ 的一个
适配整数基；它相对单项式基的行列式是 $\pm1$。令 $d_i$
是 $u_i$ 在实商空间
$$
 (K_{D,k_i}\otimes\mathbb R)/
 (K_{D,k_i+1}\otimes\mathbb R)
$$
中的 quotient 范数。逆序 Gram–Schmidt 或 Gram 行列式公式给
$$
                         \prod_i d_i=1.
 \tag{8}
$$
注意 $d_i$ 一般不是一；它们的乘积才是一。

在每个 $p$ 处，原始 quotient 生成元的商范数准确是一。
证明这一点也排除了隐含的格替换：若可以加一个
$K_{D,k_i+1}\otimes\mathbb Q_p$ 中的向量，使范数严格小于一，
则所得向量属于 $p\mathbb Z_p^{N_D}$。前缀格的饱和性使它
属于 $p(K_{D,k_i}\otimes\mathbb Z_p)$；再用下一前缀格的
饱和性，原 quotient 生成元就被 $p$ 除，矛盾。

写
$$
                  c_i=r_{k_i}(u_i)\in\mathbb Q^\times.
$$
由于评价的核恰是下一层，实际算子范数是
$$
       \|\varphi_D^{k_i}\|_p=|c_i|_p,\qquad
       \|\varphi_D^{k_i}\|_\infty=|c_i|_\infty/d_i.
 \tag{9}
$$
对有理数 $c_i$ 用乘积公式，再对 $i$ 求和，得到准确恒等式
$$
 \boxed{\quad
 \sum_{i=1}^{N_D}
       \left(\log\|\varphi_D^{k_i}\|_\infty
                      +\sum_p\log\|\varphi_D^{k_i}\|_p\right)=0.
 \quad}
 \tag{10}
$$
这里没有用单个 Taylor 系数代替饱和 jet 范数，也没有从一个
包络的指数中擅自扣除一个线性条件的长度。只有真实旗标的
一维商进入 (10)。

## 3. 全次数的复侧估计

若单项式系数向量的 Euclidean 范数为一，Cauchy–Schwarz 与
(2) 给
$$
 \sup_{|w|=R}|P(\gamma(w))|
       \le \sqrt{N_D}\exp(C_0D(1+R^\rho)).
 \tag{11}
$$
Cauchy 估计于是给
$$
 \log\|\varphi_D^k\|_\infty
       \le -k\log R+C_0D R^\rho+C_0D+\tfrac12\log N_D.
 \tag{12}
$$
先在整个系数空间估计，再限制到实际前缀子空间，范数不会
增大。当 $k$ 大于固定倍 $D$ 时，取
$R^\rho=k/(C_0\rho D)$；其余情形取 $R=1$。统一得到
$$
 \boxed{\quad
 \log\|\varphi_D^k\|_\infty
       \le-\rho^{-1}k\log k
            +\rho^{-1}k\log D+C_2(k+D).
 \quad}
 \tag{13}
$$
所有常数只依赖固定曲线和 $r,\rho$，不依赖 $D,k$。
这里的 $k!$ 并未遗失：目标从头到尾是系数 $[w^k]$，
Cauchy 估计与 (9) 使用完全相同的规范。

## 4. 不假设接触阶上界的累计

置
$$
 B=\rho^{-1}-b>0,\qquad
 A=a+\rho^{-1},\qquad s=A/B.
$$
由 $a,b\ge0$ 有 $s\ge1$。把 (5)、(13) 代入 (10)，并合并
常数，可得
$$
 0\le\sum_{i=1}^{N_D}
       \{-B k_i\log k_i+A k_i\log D+C_3 k_i+C_3D\},
 \tag{14}
$$
约定 $0\log0=0$。这一步保留了全部实际跳跃 $k_i$；
并没有假设每一个跳跃都位于 $D^r$ 附近。

设反之 $r>s$。函数
$$
            G_D(t)=-Bt\log t+A t\log D+C_3t
$$
在 $t\ge0$ 的最大值是 $O(D^s)$，由直接求导可见。故前半
跳跃的总上界至多 $O(N_DD^s)$。

对后半跳跃，(7) 给 $k_i\ge N_D/2-1\gg D^r$。于是
$$
 B\log k_i-A\log D-C_3
       \ge\tfrac12(Br-A)\log D>0
$$
对充分大 $D$ 成立。后半各项因此至多
$-c k_i\log D$，总计至多 $-c' N_D^2\log D$。
剩余的 $C_3D$ 项总共 $O(DN_D)$。因为
$$
 N_DD^s=o(N_D^2),\qquad DN_D=O(N_D^2),
$$
右侧 (14) 最终严格为负，矛盾。这证明 (6)。

证明既不需要一个关于最大接触阶的零数定理，也不需要
把 $D\asymp k^{1/r}$ 当成所有评价层的前提。即使某些
$k_i$ 特别大，(13) 的负项只会使同一个反证更强。

## 5. 原来的三维 theta 图像

现取 R155、R158 的固定原对象
$$
       \gamma(w)=(w,A_2(w),B(w)),\qquad
       w=z^4,\quad A_2=A(2z)/16,\quad B=R(x^2)A_2.
 \tag{15}
$$
其 Taylor 系数在 $\mathbb Q$，基点为 $(0,0,0)$。
R158 §6 用真实准周期轨道证明三坐标代数独立，因此
$r=3$、$N_D=\binom{D+3}{3}$。

这里也有 (2) 所需的有限型界。固定正 theta 截面在 $z$
平面的准周期公式，把任意点化到一个固定基本平行四边形；
有限符号和线性指数只贡献 $O(1+|z|^2)$。两个原截面均在
整个 $z$ 平面全纯，故
$$
      \log\max(1,|z|^4,|A_2(z)|,|B(z)|)
                           \le C(1+|z|^2).
 \tag{16}
$$
四重不变性使其成为 $w$ 整函数，并给 (2) 中准确的
$\rho=1/2$。这不是只由“阶至多二”免费认定有限型。

R158 的普通位估计，对所有 $D,k$ 给
$$
   \sum_{\substack{p\equiv1\ (4)\\p\notin S}}
       \log\|\varphi_D^k\|_p
                         \le 2k\log D+O(k+D).
 \tag{17}
$$
其中 $D>k$ 的情形用该文的 $\min(D,k)$ 版本，$\log4$ 已收入
$O(k)$。所用 Amice 尺度是
$A_2(\Omega_p\log(1+T))$，所以矩含正幂 $\Omega_p^m$；
它为单位，不改变 (17) 的真实范数。

固定坏集也只有 $O(k+D)$ 的成本。确实，每一个固定坏位，
原形式群、sigma/theta 和固定代数乘子的 Taylor 展开均有
正收敛半径。在一个足够小的固定闭盘上，三坐标有有限
Gauss 范数。因此每个多项式列、进而整个系数最大范数为一
的源元素，都满足 $|r_k(P)|_p\le C_p^D R_p^{-k}$。
有限多个这样的位合并即得所述界。它不提供无穷惰性位的
统一成本。

## 6. 准确剩余预算

假定能对同一真实三维源格的全部非零评价层证明
$$
 \sum_{\substack{p\equiv3\ (4)\\p\notin S}}
       \log\|\varphi_D^k\|_p
       \le a_I k\log D+b_I k\log k+C_I(k+D),
 \qquad a_I,b_I\ge0.
 \tag{18}
$$
则 (6)、(17) 给
$$
       3\le\frac{4+a_I}{2-b_I}\quad(b_I<2).
$$
等价地，任何这样的真实预算必须满足
$$
                  \boxed{\ a_I+3b_I\ge2.\ }
 \tag{19}
$$
因此，若在原中央全失败的假设下能严格得到
$$
                              a_I+3b_I<2,
 \tag{20}
$$
同一个真实三维图像就产生矛盾。(20) 是充分的严格门槛，
不是本文已经证明的惰性估计。

例如单纯的 $a_I=2,b_I=0$ 正在边界，不能据此宣称代数化；
$a_I=0,b_I=2/3$ 也正在边界。两个普通中央行的零性并未
出现在 (17) 的证明中，不能再次从其右侧自动扣掉两份成本。
R155 的混合列单位、R152 的局部规范限制和惰性的非中央
项，仍须在任何试图证明 (18)–(20) 的方案中保留。

如果 (20) 的证明需要有限条固定 rank 至少二曲线的中央
共同失败，则反证只能先推出这些曲线的好素数集合之并
无穷，再用有限鸽巢选出一条固定曲线。若只用 E17 的原
失败条件，则直接得到 E17。两种量词都合法，但都还缺
(20) 的真正输入，不能用这个预算命题替代主目标。

## 7. 原二坐标平面：普通预算为零的更宽门槛

还可使用另一个实际源格
$$
 \gamma_{\rm pl}(w)=(A_2(w),B(w)),\qquad
 E_{D,\rm pl}=\bigoplus_{b+c\le D}\mathbb Z X^bY^c.
 \tag{21}
$$
它不含自由的 $w^a$ 列。R158 的三坐标代数独立性立即给
$A_2,B$ 代数独立；基点仍为有理点，$A_2'(0)=1$ 使原
参数给一个非奇异形式曲线，(16) 仍给有限型 $\rho=1/2$。

在每个好普通位，(21) 的每个输出都是同一个整 Amice
测度。R158 的下降阶乘证明此时取 $K=0$，准确有
$$
 E_p(4k,0)=v_p((4k)!),\qquad
                 \log\|\varphi_{D,\rm pl}^k\|_p\le0.
 \tag{22}
$$
这是原平面的所有次数和所有饱和前缀上的结论，不是
对两个单独坐标的估计。原三维格有自然参数幂，其分布
导数成本不能一并删去；(22) 只适用于显示的二坐标源。

另一个局部核法有助于后续惰性计算。沿原形式曲线，
$$
 V=B/A_2-1=-22w+O(w^2)
$$
是参数。在 $p\ne2,11$ 时，对一个消失至少 $k$ 阶的
输出，$w$-jet 与 $V$-jet 只差单位 $(-22)^k$。
前缀核本身相同；高阶换元系数不需要另外假设整。
此处 $V$ 是源曲线的形式参数，未被加作环境空间的新坐标，
也未被假称为环境原点处的一个正则有理函数。

对原系数格作整幺三角变换 $Y\mapsto Y-X$，其全部列准确为
$$
                     F(V)^j V^c,\qquad 0\le c\le j\le D.
 \tag{23}
$$
这里没有任意的自由 $V^a$ 列。这个区别在指数 gauge 和
混合列消元中必须保留。复侧仍使用原整参数 $w$ 的 (16)，
没有把具有无穷极点的 $V$ 当成一个全局整一致化参数。

若对 (21) 的真实惰性 jet 范数能证明
$$
 \sum_{\substack{p\equiv3\ (4)\\p\notin S}}
       \log\|\varphi_{D,\rm pl}^k\|_p
       \le a_{I,\rm pl}k\log D+b_{I,\rm pl}k\log k+O(k+D),
 \tag{24}
$$
由 (6)、(22) 及 $r=2,\rho=1/2$，必须有
$$
 \boxed{\qquad a_{I,\rm pl}+2b_{I,\rm pl}\ge2.\qquad}
 \tag{25}
$$
所以在真正的中央全失败假设下获得严格的
$a_{I,\rm pl}+2b_{I,\rm pl}<2$ 也足以反证。
相较 (20)，这是当前更合适的实际源格；两式中的惰性
范数属于不同源格，不能在未作限制比较时混写。
等号 $(a_{I,\rm pl},b_{I,\rm pl})=(2,0)$ 或 $(0,1)$
仍然不够。本文没有证明 (24) 的严格改善。

## 依赖和独立核查

- [R158 的实际全部列](2026-11-12-ordinary-falling-factorial-saturated-jets.md)
  提供 (15)、(17) 和真实三维性；这里独立累计全部跳跃，
  不直接套用只含 $k\log k$ 的 arithmeticity 定理。
- [R155](../results/R155-two-theta-rows-common-amice-lattice.md)
  保同一个原 Amice 规范和完整单位核。
- [R152](../results/R152-all-degree-euler-stokes-gauge-isometry.md)
  给原 theta 准周期与局部规范的准确范围。
- (8)–(14) 是本文显示的整数饱和旗标、Gram 行列式、
  有理数乘积公式及 Cauchy 估计的完整证明。另一代理已
  独立核算实 quotient 长度乘积、全部跳跃累计和严格门槛。
