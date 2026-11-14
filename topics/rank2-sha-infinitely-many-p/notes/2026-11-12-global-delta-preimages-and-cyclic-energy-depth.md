# 真实全局 delta 原像与两个循环能量的整深度

日期：2026-11-12。**已证明。** 本篇继续 R161 的全局有理
参数版本，只对原 Heegner 点的真实整数原像计算。
得到精确平方迹式和 $a/(p-1)$ 型整除预算；这个预算在当前
已经证明的指数范围内仍只有一层 p，不证明原测试非零。

## 1. 原点、整数原像和全部完成

保留 R130/R139/R146 的实际输入、原范数一簇
$$
 A=\ker(\operatorname{Res}_{L/F}E\longrightarrow E),\qquad
 \Gamma=\langle\tau\rangle=C_p,\qquad
 \delta=\tau^{(p-1)/2}(\tau-1).
 \tag{1}
$$
取 $p\ge7$，保留原 p-unit formalizer $D_p$。记
$\mathcal P=\mathcal O_L\otimes\mathbb Z_p$、
$\mathcal B=\mathcal O_F\otimes\mathbb Z_p$、
$N=N_\Gamma$。不删去完全分裂情形的任何完成。
原不分歧局部结构给
$$
              \mathcal P\simeq\mathcal B[\Gamma],\qquad
              I=\ker N=\delta\mathcal P .
 \tag{2}
$$
内积记为
$\langle x,y\rangle=\operatorname{Tr}_\Gamma(xy)$，值属于
$\mathcal B$；下文赋值指所有相应完成的最小 p 赋值。

若原全局指数为 a，则本篇使用
$$
                    Q=\delta^aS,\qquad S\in A(F)
 \tag{3}
$$
的**整数群**等式。它来自 R128 的实际有限 p 商论证，
而非把半局部加法原像当成椭圆曲线点：
$A(F)/\delta^aA(F)$ 有限且为 p 群，故到 p 完成的映射
是同构。$\delta$ 在素于 p 的挠点群上可逆，原输入已排掉
相关 p 挠点，因此已知完成中的除性准确给 (3)。
这个论证同样适用于原 E389 范数一簇。

同一个整数群环算子 $D_p$ 对任意实际 $S\in E(L)$ 都在全部 p 处
formalize，故
$$
 z_S=\log_E(D_pS)/p\in I,\qquad
 z_Q=\log_E(D_pQ)/p=\delta^a z_S .
 \tag{4}
$$
它们是真实全局点的对数。以下在 (2) 中选用加法正规基
只用于证明整格估计，不改变这个全局来源。

## 2. 同一循环核的对数能量

对 $z\in\mathcal P$ 定义
$$
 \mathcal E_1(z)=\frac12\sum_{j,k=0}^{p-1}
                     d(j,k)(p-d(j,k))\,\tau^jz\,\tau^kz,
 \tag{5}
$$
$$
 \mathcal E_2(z)=\frac1{24}\sum_{j,k=0}^{p-1}
                     d(j,k)^2(p-d(j,k))^2\,\tau^jz\,\tau^kz,
 \tag{6}
$$
其中 $d(j,k)$ 是 j-k 的最小非负模 p 代表。
本篇的 $\mathcal E_i(z_Q)$ 对应 R161 §7 中同一个
$R=D_pQ$ 的对数列；它不是把 R161 §2 的 canonical
Frobenius 行数值无说明地换成此列。

令
$$
 K_r=\sum_{d=0}^{p-1}\{d(p-d)\}^r\tau^d
 \quad(r=1,2).
$$
则
$\mathcal E_1(z)=\langle z,K_1z\rangle/2$、
$\mathcal E_2(z)=\langle z,K_2z\rangle/24$。
在群环 involution $\tau^*=\tau^{-1}$ 下，
$$
       \delta^*=-\delta,\qquad
       \delta^2=\tau+\tau^{-1}-2 .
 \tag{7}
$$
R161 已直接计算的循环 Laplacian 因而准确给
$$
 \delta^2K_1=2p-2N,\qquad
 \delta^2K_2=-12K_1+2(p^2+1)N-4p .
 \tag{8}
$$
对 $z_S\in I$，所有 N 项消失。利用 (7) 把
$\delta^a$ 从一个因子移到另一个因子，得到：
$$
 \boxed{\quad
  \mathcal E_1(z_Q)
      =-p\,\operatorname{Tr}_\Gamma
                         ((\delta^{a-1}z_S)^2),
                  \qquad a\ge1 ,
 \quad}
 \tag{9}
$$
$$
 \boxed{\quad
  \mathcal E_2(z_Q)
      =-p\,\operatorname{Tr}_\Gamma
                         ((\delta^{a-2}z_S)^2)
        +\frac p6\operatorname{Tr}_\Gamma
                         ((\delta^{a-1}z_S)^2),
                  \qquad a\ge2 .
 \quad}
 \tag{10}
$$
所有原像仍是 (3) 的同一个真实 S。
这里没有除去一个可能不是全局点的局部 $\delta$ 因子。

## 3. 准确的自动 p 整层

写 $\Delta=\tau-1$。整数群环中
$$
 \delta^{p-1}=N-pV,\qquad \varepsilon(V)=1,\qquad
                        \delta N=0 ,
 \tag{11}
$$
其中可以准确取
$$
 V=\tau^{(p+1)/2}
       \sum_{i=1}^{p-1}\frac{\binom pi}{p}\Delta^{i-1}.
 \tag{12}
$$
$V\in\mathbb Z_p[\Gamma]^\times$；在最大理想
$(p,\Delta)$ 下它约化为 1。
注意 (11) 在完整置换格上保留 N，不能先把它省掉。

因为 $NV=N$、$N^j=p^{j-1}N$，对 $b\ge1$ 有
$$
 \delta^{b(p-1)}
     =(-1)^{b+1}p^{b-1}N+(-p)^bV^b .
 \tag{13}
$$
若另乘正次幂 $\delta^r$，第一项消失。
写 $2j=b(p-1)+r$、$0\le r<p-1$，从 (13) 和
$\delta^*=-\delta$ 得任意 $y\in\mathcal P$ 满足
$$
 v_p\operatorname{Tr}_\Gamma((\delta^jy)^2)
      \ge \left\lceil\frac{2j}{p-1}\right\rceil-1,
                         \qquad j\ge1 .
 \tag{14}
$$
当 r=0 时，右侧的减一正是完整置换格的 N 项所需；
不允许以 norm-zero 格上的关系免费丢掉它。

在 (2) 中写已知的 $z_S=\delta y$，只作加法整格运算。
由 (9)–(10)、(14) 得实际对数能量的下界
$$
 \boxed{\begin{aligned}
 v_p\mathcal E_1(z_Q)
        &\ge\left\lceil\frac{2a}{p-1}\right\rceil,
                                           &&a\ge1,\\
 v_p\mathcal E_2(z_Q)
        &\ge\left\lceil\frac{2a-2}{p-1}\right\rceil,
                                           &&a\ge2 .
 \end{aligned}}
 \tag{15}
$$
这不是声称实际能量达到等号。
它给出只从真实全局除性和整循环格自动取得的 p 整层。

## 4. 返回 R161 的全局有理数

用 R161 的奇参数
$$
 u_{17}=-x/y,\qquad u_{389}=-2x/(2y+1)
 \tag{16}
$$
和 $R=D_pQ$，令
$b_Q=u_E(R)/p$。在这个整奇参数中，形式对数也是奇级数，
且第 m 项的系数分母整除 m 的 p 部分。因此 p≥7 时
$$
                  z_Q-b_Q\in p^2\mathcal P .
 \tag{17}
$$
E17 还有 $u(iP)=iu(P)$，故只有 $m\equiv1\bmod4$ 的项，
此时 (17) 加强为 $p^4\mathcal P$。这些断言直接来自整
不变微分积分，不需普通 sigma 或 regulator 非退化。

由于 (5)–(6) 为整二次式，
$$
       I_i^{\rm rat}-\mathcal E_i(z_Q)\in p^2\mathcal B
                   \quad(i=1,2),
 \tag{18}
$$
E17 可将 p² 换为 p⁴。特别，若 a≥2，则原全局有理数
的除 p 首项准确为
$$
 \begin{aligned}
 \frac{I_1^{\rm rat}}p
    &\equiv-\operatorname{Tr}_\Gamma
                         ((\delta^{a-1}z_S)^2)\pmod p,\\
 \frac{I_2^{\rm rat}}p
    &\equiv-\operatorname{Tr}_\Gamma
                         ((\delta^{a-2}z_S)^2)
          +\frac16\operatorname{Tr}_\Gamma
                         ((\delta^{a-1}z_S)^2)\pmod p .
 \end{aligned}
 \tag{19}
$$
这两条 trace 是实际全局 S 的不变量，尚没有证明它们
必为单位或必再被 p 除。这里只识别了它们，不把它们的
定义式当作新的非零输入。

对应的有理能量自动界为 (15) 与精度 2 的较小者；
E17 则与精度 4 比较。在当前已付范围
$$
                        2\le a\le(p-3)/2
 \tag{20}
$$
内，(15) 的两个右端都恰为 1。
E17 的长度上界 $2a$ 与 E389 的准确长度 $2(a+1)$
分别保留原范围；它们本身不把 (19) 的两个具体平方迹
进一步约束为零模 p。

## 5. 小高度不能无代价传给原像

这个问题可在原全局点的 Néron–Tate 空间内直接量化。
Galois $\tau$ 保持 canonical-height 内积；在 norm-zero
空间上其复特征值为非平凡 p 次单位根。因而 $\delta$
的各特征值绝对值为
$2|\sin(\pi j/p)|$，$1\le j<p$。由 (3) 得
$$
 (2\sin(\pi/p))^{2a}\widehat h(S)
       \le\widehat h(Q)\le4^a\widehat h(S).
 \tag{21}
$$
特别
$$
             \widehat h(S)\le(p/4)^{2a}\widehat h(Q),
 \tag{22}
$$
用的是 $\sin(\pi/p)\ge2/p$。
因此 a=2 时，原 $Q$ 的小高度没有给 S 相同常数的高度
上界。R161 的有理能量高度及 (19) 不能在这里无代价
替换成一个固定小高度 S 的估计。

本篇未证明原 $I_1,I_2$ 在无穷多个 p 非零，也未构造
实际 CM 失败的反例。接下来的正向输入必须约束 (19) 中
这些**实际全局**平方迹，或支付一个新的原像高度/全局
饱和性结论。

## 6. 依赖

- [R128 整数有限 p 商及固定 Artin 生成元](../results/R128-fixed-artin-generator-and-integral-augmentation.md)
  的整数商论证。
- [R161 原整循环核与全局有理参数](2026-11-12-integral-cyclic-invariants-and-actual-second-moment.md)：
  本篇 (8) 的核恒等式、原全部完成及有理数定义。
- R130/R139/R146 的原 formalizer、范数一格和两步 Sha
  证书；R125 的 E17 长度上界 $2a$ 与 R144/R156 的
  E389 准确长度 $2(a+1)$ 在各自原假设范围内使用。

本文所有新增群环、平方迹、精度及高度等式均在正文直接证明。
