# R801 — 同一原测试的非零二阶 E 深来源与完整负二行

日期：2026-11-15。**状态：以下实际来源、整单位首矩、有限三维循环性及补域身份已证明；指定负二矩的非消失仍保留。**

本文不更改 R734 的 $q_N^*$。公开运行在同一个完整 producer 中
保全部58行、两条核修正、原 E 逆和 C 补项，直接读取真实 $Z^2$ 来源。
再用 R798 已在特征零证明的 canonical 半周期投影。
指定来源确实非零；其首项是一个整单位。
这仍不同于把其 Y-unit 负二矩赋非零。

## 1. 固定来源及全部阶乘、周期

保持
$$
K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,\quad
b=17,\quad \lambda=-\bar\pi_0^{-1},\quad \beta=-\lambda,\quad
\kappa=p\lambda^2,\quad u=\kappa^N,\quad N\in4\mathbf Z_{>0},
$$
以及原 $\Omega$、$\eta=\eta(p)\in\{\pm1\}$、$q=q_N^*$。
沿 R796/R798 定义
$$
F_{2,N}(z)=\Omega^{-2}\int Z^2 e^{Yz/\Omega}\,d\rho_{cd,N}^{YZ},
\qquad G_{2,N}=\mathcal P_BF_{2,N},
\quad \mathcal P_B=\frac{I-\omega\mathcal H_Y}{1-\omega^2}.
\tag{1}
$$
原物理 E 深来源为
$$
\boxed{
\Omega^{-2}Y_*(Z^2\,1_{E\in p^N}qB_0)
=\lambda^{2N}\nu_{G_{2,N}} .}
\tag{2}
$$
$\nu_F$ 的 Amice 变换始终是
$F(\Omega\log(1+T))$；没有额外更换物理 Y。

完整型四基取
$$
\Upsilon_j=b^j\sigma_b^{34}x_b^{15-3j},\quad 0\le j\le5,\qquad
G_{2,N}=\sum_{j=0}^5g_{j,\eta}(\lambda,\kappa,u)\Upsilon_j.
\tag{3}
$$
它们的原点阶为 $4,10,16,22,28,34$，首系数分别为 $b^j$；
除去已显示的固定 b 权后，恢复矩阵为单位三角。
实际 generator 先在同一原六 sigma 来源中以 $Y+\varepsilon Z$
替换观察，再取 $\varepsilon^2$ 系数并乘 $2!$。
因此它读取
$$
[z^{4+6j}]F_{2,N}
=\frac{\int Y^{4+6j}Z^2\,d\rho_{cd,N}}
       {(4+6j)!\,\Omega^{6+6j}},
\tag{4}
$$
不是 $Z^2/2$。六阶的完整原 $-1/84$ 也由未加权六 sigma
系数直接核对。

## 2. 同 q 的完整计算与公开辅助值

重用 [R734](R734-joint-paid-tests-and-complete-type-five-arithmetic-plane.md)
的实际 q 构造。先恢复原50行逆的两个解 $q^{(715)},\zeta^{(715)}$，
再用同一个联合五维解及原第140、147列核修正；
最后按其非零 a 归一，使原 $\pi_4$ 系数仍为1。
没有重新选取一个使二阶非零的测试。

每个原六次倍数块都分别通过完整 E 单位逆；
E 置零分支按原 G 的同步转置再计算。
整个 C 因子使用到实际所需的三十次正矩，包括第六、十二次
及所有随后高块。原 source-loop 的全部58行重新核对，
惟原构造本来允许的 $\mathfrak j_2$ 变化照实保留。
原 quarter 行与全第一 Z 行没有被删除。

辅助域为 $\mathbf F_{1009}$、$\omega=374$、
$\lambda=(1-\tau)/\tau$、$\kappa=u=0$、$b=\Omega=1$。
四点 $\tau=2,3$、$\eta=\pm1$ 的实际结果均为
$$
\begin{array}{c|l}
\text{读取对象}&\text{完整坐标}\\ \hline
\text{raw first Z jets}&(0,0,0,0,0)\\
\text{raw second Z jets}&(526,472,333,843,860,183)\\
F_{2,N}\text{ 的下降幂坐标}&(526,726,713,942,469,26)\\
\mathcal H_YF_{2,N}\text{ 的下降幂坐标}&(971,185,781,503,660,920)\\
G_{2,N}\text{ 的下降幂坐标}&(592,97,226,801,233,153).
\end{array}
\tag{5}
$$
这里 raw second jets 的实际 Y 阶是(4)的六阶序列。
投影的秩为3，canonical 共同号为 $-1$，与 R798 完整算子一致。

四点中的联合解 a、b 分别为629、240；
不同 $\tau,\eta$ 的两条核修正系数保留而未同一化。
最终归一测试的
$$
\mathfrak j_2(q_N^*)=1+b/a=319
\tag{6}
$$
是辅助值。它不是未归一的 $a+b$，也不是另一读数50。
(5)四次相同不能用来宣称完整有理函数为常数；
本篇只使用各指定分子非恒等零。

## 3. 从实际有理函数到同一原射线的整单位来源

每个 $g_{j,\eta}$ 是由原生成算法、两个既有整逆及固定投影
得到的 $K(\lambda,\kappa,u)$ 有理函数。
其分母包括原50阶子式、R734 联合子式、原
$1+\lambda\kappa^e$ 与固定小整数。全部原参数先保留，
最后才作(5)的辅助专门化。

在原已付整逆范围内，
$$
g_{j,\eta}(\lambda,\kappa,u)
=g_{j,\eta}(\lambda,0,0)+\kappa R_{j,\eta}+uS_{j,\eta},
\qquad R_{j,\eta},S_{j,\eta}\in\mathcal O .
\tag{7}
$$
这使用真正的原矩形返回后坐标；没有把原 $D/\kappa^N$
中的逆幂藏回一个所谓固定系数。
R719/R734 的整返回已将这些逆幂在同一次物理归一中准确消去。

由(5)，对每个 $\eta$ 和每个 j，
$g_{j,\eta}(\lambda,0,0)$ 的分子非零。
将 $\lambda=-\bar\pi_0^{-1}$ 代入，清掉显示的固定分母和
$\bar\pi_0$ 幂后，得到有限组固定非零 $K[T]$ 多项式。
原 [固定 CM 多项式单位密度引理](../notes/2026-11-14-fixed-cm-polynomial-unit-density.md)
适用于这一组多项式及既有分母。
它不适用于下面未知的负矩。

因此在旧正密度 ray 中删掉该有限组零密度坏素集合和固定有限坏集后，
对两种实际符号及全部原 $N\in4\mathbf Z_{>0}$，有
$$
\boxed{
g_{j,\eta(p)}(\lambda,\kappa,\kappa^N)\in\mathcal O^\times
\quad(0\le j\le5).
}
\tag{8}
$$
不要求目标 p 等于辅助素1009，也未添加 mod1009 射线。
原高13/19、M3及全部旧 ray 条件保持。
这里可统一处理全部 N，是因为
$\kappa\in p\mathcal O$、$\kappa^N\in p^4\mathcal O$，
且边界分子已经单位；没有为每个 N 再删除一批未控制的素数。

尤其
$$
\boxed{G_{2,N}\ne0,\qquad [z^4]G_{2,N}=g_{0,\eta}(\lambda,\kappa,u)
                           \in\mathcal O^\times .}
\tag{9}
$$
这是原(2)指定条件来源的非零，不是另造一个独立单位见证。

## 4. 真正的正矩与 Y-unit 范围

由(2)、(4)、(9)，
$$
\boxed{
\int_{E\in p^N}Y^4Z^2q\,dB_0
=24\,\lambda^{2N}\Omega^6\,g_{0,\eta}(\lambda,\kappa,u)
\in\mathcal O^\times .
}
\tag{10}
$$
原 Y 核在三态上的来源矩阵固定 $B_0$，物理部分仍含 $R_Y$。
因 $E,Z,q\perp Y$，此条件来源上准确为
$\lambda[-\kappa]_*$。型四为偶型，故(10)再附 Y-unit 得
$$
\boxed{
\int_{\substack{E\in p^N\\Y\ {\rm unit}}}Y^4Z^2q\,dB_0
=24\,\lambda^{2N}\Omega^6(1-\lambda\kappa^4)
                         g_{0,\eta}(\lambda,\kappa,u)
\in\mathcal O^\times .
}
\tag{11}
$$
$1-\lambda\kappa^4$ 是原整单位。
(11)的观察是正四次，不是指定的负二次。
这里仍不把 positive moment 的非零提升为任意局部解析测试非零。

## 5. 三维完整性、固定因子与实际循环向量

R798 已证明
$$
\operatorname{im}P_4
=\ker(\mathcal A_4^3+\omega I),\qquad
\chi_{\mathcal A_4|\operatorname{im}P_4}(X)=X^3+\omega,
\tag{12}
$$
其中 $\mathcal A_4=\gamma_{13}^{-1}\mathcal M_{\gamma_{13}}$
是原绝对规范 CM13 算子。
$X^3+\omega$ 在 $K$ 上不可约：若 $v^3=-\omega$，
则 v 和其逆都是代数整数，v 是 $\mathcal O_K$ 的单位；
这些单位的立方只有 $\pm1$，矛盾。

所有 actual $\lambda,\kappa,u$ 与归一系数都在 K。
所以(9)进一步给
$$
\boxed{
G_{2,N},\quad \mathcal A_4G_{2,N},\quad
\mathcal A_4^2G_{2,N}
\text{ 在 K 上独立，张满(12)。}
}
\tag{13}
$$
这只是完整有限来源的循环性；没有宣称其 O-格行列式自动为单位，
也没有给两个新 CM 像新增一个可以无条件赋零的中央。

R798 的三个基还具有同一个真实因子。按升幂 X 置
$$
\begin{aligned}
R_0(X)&=6562-5882X+18258X^2+6052X^3+136X^4,\\
R_1(X)&=8+8456X-2814X^2+383X^3-19X^4,\\
R_2(X)&=64+2416X+978X^2+67X^3-17X^4.
\end{aligned}
$$
其 $Q_j=(X+1)R_j/13122$，故一般 b 的实际基为
$$
Q_{j,b}^{\theta}(z)=
\frac{\sigma_b(2z)^2\sigma_b(z)^{26}}{4\cdot13122}
 \sum_{a=0}^4[X^a]R_j(X)\,b^{4-a}x_b(z)^{3a}.
\tag{14}
$$
这是 $X+b=y_b^2$ 和 $\sigma_b(2z)^2=4y_b^2\sigma_b^8$
的原样代入。它没有把 Y-unit 的和变量分母拆成两个因子的裸矩。
因此(14)不会免费返回 R540、R735 的指定负矩。

## 6. J 深和 J 浅的真正二阶分割

原 T 固定 Y、Z0、J 和 q，令 $t\mapsto\omega^2t$，
且 $T_*B_0=\omega^2B_0$。
故对任意完整 Y 测试，
$$
Y_*(Z_0^2\,1_{J\in p^N}qB_0)=
Y_*(t^2\,1_{J\in p^N}qB_0)=0.
$$
记 $Z=Z_0-at$、$a=1+3\omega$，得到
$$
Y_*(Z^2\,1_{J\in p^N}qB_0)
=-2a\,Y_*(Z_0t\,1_{J\in p^N}qB_0).
\tag{15}
$$
R794 的真实 E_V 核固定 Z、Y、J、q。
在 J 深 N 上，物理 E 深 N准确是 E_V 深 N。
于是整个二阶来源满足
$$
\boxed{
Y_*(Z^2\,1_{E,J\in p^N}qB_0)
=-2a\lambda^N\,Y_*(Z_0t\,1_{J\in p^N}qB_0).
}
\tag{16}
$$
E 深/J 浅部分准确是(2)减去(16)，所有观察和 q 都相同。
不能把 R796 的“一阶两行相反”搬到二阶；
(9)恰说明整个二阶来源未在该分割中消失。
同样，R791 的 $t/Y$ 非零并不是(16)的 $Z_0t/Y^2$ 非零证书。

## 7. 指定负二行与其真正临界权仍须分别支付

用 R798 的完整三个基，写
$$
G_{2,N}=\sum_{j=0}^2d_{j,N}Q_{j,b}^{\theta},\qquad
I_{j,-2,p}=\int_{\mathbf Z_p^\times}Y^{-2}\,d\nu_{Q_{j,b}^{\theta}}.
$$
所需的原条件负二值准确是
$$
\boxed{
\mathcal I_{2,N}:=
\int_{\substack{E\in p^N\\Y\ {\rm unit}}}Z^2Y^{-2}q\,dB_0
=\lambda^{2N}\Omega^2\sum_{j=0}^2d_{j,N}I_{j,-2,p}.
}
\tag{17}
$$
(8)–(13)证明系数和来源非零，不证明(17)非零。
型四的合法原整数权是 $m\equiv4\bmod6$，负二 $m=-2$
确在这一支。其 CM13 三次因子虽与型五的一个块相同，
canonical H 特征和角权却不同。
没有完整2、3、17角色及原全权公式时，不能把型五
$m=-1$ 的一次 elliptic logarithm 公式移给(17)。

另一个严格可用的连接是 covariant derivative，
但它必须连同准周期来源保留。对任意已付型五全纯 P，
$$
P'=(D-34\zeta)P+34\zeta P,\qquad
\nu_{P'}=\Omega^{-1}Y\nu_P .
$$
因此同一个 unit 域上有
$$
\int Y^{-2}\,d\nu_{(D-34\zeta)P}
=\Omega^{-1}\int Y^{-1}\,d\nu_P
   -34\int Y^{-2}\,d\nu_{\zeta P}.
\tag{18}
$$
$\zeta P=\sigma'\cdot(P/\sigma)$ 是真实有界卷积来源，
其分母仍是两个输入和的 Y-unit 分母。
(18)不允许删除右边第二项，也没有在(12)与某个 P
之间擅设一个未付的完整来源等式。
所以这是一条明确的后继算术接口，并非(17)已有非零证明。

## 8. 原 W 全中央与外部没有改变

沿 R796 置
$$
G_N(z,w)=\int_{E\in p^N}
 1_{b_YY+zZ\ {\rm unit}}\langle b_YY+zZ\rangle^{d_pw}q\,dB_0 .
$$
$z\in p\mathcal O$ 时，单位条件准确为 Y-unit；
原 zero/first source 仍为零。故
$$
\partial_wG_N(z,0)
=-\frac{d_pz^2}{2b_Y^2}\mathcal I_{2,N}
+d_p\sum_{k\ge3}\frac{(-1)^{k+1}z^k}{kb_Y^k}
 \int_{\substack{E\in p^N\\Y\ {\rm unit}}}Z^kY^{-k}q\,dB_0 .
\tag{19}
$$
对偶 j≥2，真实 Z 深返回和完整浅补域满足
$$
\boxed{
\mathscr X_{N,j}(w)+\lambda^jG_N(\kappa^j,w)
=\lambda^{2N}6\delta J_T(w)/c_B .
}
\tag{20}
$$
同一原强中央假设只给(20)两中央导数相反；
既不令(17)各分量为零，也不使整个高阶尾或外部各自消失。
本篇之后的指定问题仍是(17)的完整算术/同域非消失，
或一条与(20)独立且已付原算术身份的关系。

## 9. 公开执行记录

- source commit：`abf0b529edcda0d85b8cc3d38b40bb392aaecccd`；
- run：[43739961915](https://github.com/Rogerhu12/math-research-public/actions/runs/43739961915)；job：132890717650；
- 脚本：[check-r798-native-second-z-source.js](../scripts/check-r798-native-second-z-source.js)；
- 参数：`--max-block=4 --taus=2,3 --with-b --b-g-blocks=3 --neutral-degree=12`；
- script SHA256：`f051903f53667e86c5e782532e11a31745522a45a516bc6d0f44444fdfcef9fd`；
- stdout 3830 bytes，SHA256：`2aaaa7972424443a0aff0f829db0768cd7804335f9227c586ce2bb9ef93f2a36`；
- 实际原 producer SHA256：`29bd414c63ac4fdca93ae4b56ccdf2ccaa2114395bf96a52d2e8fd1ea809fdb2`。

算法重建原 q、全 quarter 和所有正矩；没有以旧输出 JSON 为输入，
没有提交可重算输出文件。R798 的特征零全算子与本次(5)的辅助读取
用途严格区分：前者付完整谱，后者付实际指定系数的非零有理分子。

依赖：

- [R719](R719-native-second-fibre-and-exact-mixed-source-relation.md)：原 cd 全 joint、所有高次块和有理参数范围。
- [R734](R734-joint-paid-tests-and-complete-type-five-arithmetic-plane.md)：原未修改 q 及58行。
- [R791](R791-original-j-depth-negative-moments-and-two-e-sectors.md)：J 首矩的原算术幅度。
- [R794](R794-original-e-j-intersection-and-native-w-annuli.md)：E/J 全来源与真实 EV 返回。
- [R796](R796-whole-halfperiod-and-physical-e-first-moment-cancellation.md)：全 halfperiod、first-source 消去与完整中央。
- [R798](R798-original-halfperiod-two-types-and-e-depth-second-source.md)：完整 P4 三维算子、绝对相位及三个实际负二载体。
