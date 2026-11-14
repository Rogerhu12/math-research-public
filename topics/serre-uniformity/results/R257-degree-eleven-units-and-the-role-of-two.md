# R257：11 次域的真实单位基、零自局部斜率与素数 2 的作用

**状态：已证明，且所列有限符号、整式恒等式与无条件类数认证均已实际执行。**
本条处理 R243 新出现的阶 11 特征 $\chi^{\pm8}$，给出该小域的明确
普通单位、类群与射线输入，并区分是否把素数 $2$ 放入 $S$。
忠实特征 $\chi^{\pm1}$ 的实际 Norm 原像和 $\mathcal L$ 仍未取得；
本条不占用 R202。

仍取 R171/R191 的同一个 $p=43,q$、正算术 Artin
$\sigma=\mathrm{Frob}_{(-1+2i)}$、Weil 根 $\zeta=e(P,iP)$，
以及 $\omega=8+25i\in k=\mathbf F_{43^2}$。
记
$$
 M=F^{\langle\sigma^{11}\rangle},\qquad
 H_{11}=M^{\langle\tau\rangle},\qquad
 L_{11}=ML_q,\qquad
 \psi=\chi^8,\quad \psi(\sigma)=\eta=11+3i.
 \tag{257.1}
$$
$[M:K]=[H_{11}:\mathbf Q]=11$，
$\mathrm{Gal}(M/\mathbf Q)=D_{22}$，
$\tau\sigma\tau=\sigma^{-1}$。
$H_{11}$ 的签名为 $(1,5)$；这里只把“实”用于指定的 $\tau$ 固定域，
没有声称它全实。

本文的结构结论为
$$
 \boxed{
 \begin{gathered}
 h(H_{11})=1,\qquad \operatorname{Cl}(M)_{43}=0,\\
 e_{W_8}\operatorname{Cl}_{\{43,q,\infty\}}(L_{11})_{43}
       \ne0,\\
 e_{W_8}\operatorname{Cl}_{\{2,43,q,\infty\}}(L_{11})_{43}
       =0.
 \end{gathered}}
 \tag{257.2}
$$
其中 $W_8$ 为 $\psi,\psi^{-1}$ 合成的二维 $\mathbf F_{43}$ 型；
带下标 $S$ 的类群约去 $S$ 上的素理想类。
第二行的非零商明确为加法群 $k$。
这些结论也适用于全域 $L$ 的同一个 $W_8$ 分量，因为
$[L:L_{11}]=4$ 与 $43$ 互素，且 $\langle\sigma^{11}\rangle$
在该分量上平凡。

## 1. 同一小域的精确模型和无条件类数

R219 已证明
$$
 s=\left(\frac{z-1}{z+1}\right)^4,\qquad H_{11}=\mathbf Q(s).
$$
本条把它精确改写为 $\mathbf Q(y)$，其中
$$
 \begin{split}
 f_{11}(y)={}&y^{11}-4y^{10}+19y^9-52y^8-13y^7+532y^6\\
             &-1159y^5+100y^4+2812y^3-1696y^2-4652y+6704.
 \end{split}
 \tag{257.3}
$$
证书保存 $s$ 关于 $y$ 和 $y$ 关于 $s$ 的全部有理系数。
标准库核验器在两个有理数商环中验证原多项式、新多项式及两个
复合映射都是恒等式，因此没有用浮点根匹配来识别域。
所有共同分母均由逐系数分母的最小公倍数构成，并逐项回读比较。

PARI 2.17.2 的实际计算给出
$$
 d(H_{11})=-86^{10}=-22130157888803070976,\qquad
 (r_1,r_2)=(1,5).
 \tag{257.4}
$$
不能把这里的判别式误写成 $-43^{10}$：
$M/K$ 在 $43$ 的相对导子判别式是 $(43)^{10}$，
绝对判别式还含基域 $\mathbf Q(i)$ 的 $2$ 部分。

具体认证顺序为
$$
 \texttt{nfinit}(f_{11}),\quad
 \texttt{bnfinit}(\mathrm{nf},1),\quad
 \texttt{bnfcertify}(\mathrm{bnf},1)=1.
 \tag{257.5}
$$
前一步返回候选类数 $1$；最后一步实际遍历认证所需的素数，
日志所示上界为 $186080$，并返回 $1$。
PARI 官方文档明确说明：最后参数 $1$ 认证真实类群是候选类群的商。
候选群为平凡群，所以此处已经无条件推出 $h(H_{11})=1$。
**这个调用没有认证整组基本单位；本文也不用它作这种声称。**
早先不带 flag 的完整认证被停止，未报告其返回值；
这里使用的是已完成的 flag $1$ 认证。

下面直接从 $h(H_{11})=1$ 推出所需的 $\operatorname{Cl}(M)_{43}=0$。
令 $A=\operatorname{Cl}(M)_{43}$。
二次扩张 $M/H_{11}$ 的理想扩张、范数复合为 $2$，所以
$A^\tau=0$。由于 $2$ 可逆，$\tau$ 在 $A$ 上作用为 $-1$。
二面体关系随即给 $\sigma=\sigma^{-1}$；又 $\sigma^{11}=1$，
所以 $\sigma=1$。于是 $A=A^{C_{11}}$。
扩张 $M/K$ 的范数和扩张复合为 $11$，而 $h(K)=1$，
故 $11A=0$。$11$ 在 $43$ 群上可逆，得到 $A=0$。
此论证没有把一个反射的固定部分消失直接等同于全部类群消失，
而是明确使用了二面体关系。

## 2. 无平移 Robert 值给出真实的普通单位

令 $P_j=(-1+2i)^jP$，
$\phi_j:A\to E_j=A/\langle P_j\rangle$ 为规范 Vélu 同源。
沿用 R198 的准确函数
$$
 \mathcal F_A(Q)=\frac{64^{10}}{\psi_{11,A}(Q)}.
$$
定义
$$
 R_j=\prod_{a=1}^{42}\mathcal F_A(aP_j)
     =\left(\frac{\Delta_{E_j}}{64}\right)^{10}.
 \tag{257.6}
$$
这里第二个等式是一个全局精确恒等式。证明是在 R198 的精确
isogeny Norm 关系中令商曲线点趋近原点：
$\mathcal F_A$ 的首项为 $64^{10}t^{120}/11$，
规范 Vélu 同源满足 $t'=t+O(t^2)$，
所以原点附近的那一个因子消去后，剩余常数正好为
$(\Delta_{E_j}/64)^{10}$。没有未指定的 $43$ 次根或单位因子。

Robert 函数 $\Theta_{A,(11)}$ 等于 $\mathcal F_A^{12}$。
Rubin 的 Theorem 7.4(iii) 给出：在原始 $(43)$ 挠点上的值在
$43$ 外为单位。因此 $R_j$ 本身也在 $43$ 外为单位；
从 $12v(R_j)=0$ 得 $v(R_j)=0$，不需要选择 $12$ 次根。
这是普通全局代数数的单位支撑断言。

乘 $i$ 对应原 $\sigma^{22}$；$\mathcal F_A(iQ)=\mathcal F_A(Q)$，
故 $R_{j+22}=R_j$。令
$$
 T_j=R_jR_{j+11},\qquad
 v_j=T_j/T_{j+1}\quad(j\bmod11).
 \tag{257.7}
$$
则 $T_j\in M$，$T_j=\sigma^jT_0$，
$\tau T_j=T_{-j}$。
$M$ 在 $43$ 只有一个素点，因而所有 $T_j$ 在该点的赋值相同。
所以
$$
 v_j\in E_M,\qquad \prod_{j=0}^{10}v_j=1.
 \tag{257.8}
$$
这些是可由 $43$ 次 Vélu 运算精确求值的普通单位，不是形式上的
非整数特征幂。它们在本文只被用作底域单位，尚未给出上域 Norm 原像。

## 3. 十个单位的 43 饱和证书

在 $\mathbf F_{859^2}$ 取
$$
 P=(209,591),\quad z_0=548,\quad
 \zeta_{859}=e(P,iP)=510+324i.
 \tag{257.9}
$$
程序检查点方程、$[43]P=0$、Weil 根的阶、全部正 Artin 分支，
并在 $859$ 和原 $q$ 两处分别对全部 $44$ 个分支直接比较
(257.6) 的两边，共 $88$ 个精确恒等式。

以 $\ell_\ell(a)=\log_{\zeta_\ell}(a^{(\ell^2-1)/43})$ 记幂剩余符号。
在 $859$，$v_0,\ldots,v_{10}$ 的符号为
$$
 (23,16,30,35,35,23,35,35,30,16,23).
 \tag{257.10}
$$
其 $11$ 条共轭剩余映射组成循环矩阵
$C_{a,j}=\ell_{859}(v_{a+j})$。
实际计算
$$
 \operatorname{rank}_{\mathbf F_{43}}C=10,\qquad
 \det C_{\{0,\ldots,9\},\{0,\ldots,9\}}=39\ne0.
 \tag{257.11}
$$
$M$ 为次数 $22$ 的全虚域，单位秩为 $10$，且无 $43$ 阶单位根。
因此 $v_0,\ldots,v_9$ 在 $E_M/E_M^{43}$ 中是一组基。
本条由实际有限符号证明全部 $43$ 饱和性，
没有使用条件性的 PARI 单位完备性。

在原 $q$ 的同一 Weil 规范下，循环矩阵秩为 $8$；
相应五对非平凡特征的 Fourier 和如下。
表中数值都是 $\sum_{j=0}^{10}\omega^{nj}\ell(v_j)$，
尚未乘 $1/11$。

| $n$ | $859$ 的值 | 原 $q$ 的值 |
|---|---:|---:|
| $4$ | $38+32i$ | $27+25i$ |
| $8$ | $4+42i$ | $0$ |
| $12$ | $4+30i$ | $34+40i$ |
| $16$ | $2+19i$ | $16+23i$ |
| $20$ | $14+11i$ | $21+38i$ |

结合 (257.11)，原 $q$ 的普通单位剩余映射在 $\psi,\psi^{-1}$
两条特征线上恰好为零，在其余四对线上非零。
这独立重现 R243 的阶 $11$ 方向，并给出了该小域自己的明确单位基。

## 4. 同一自局部斜率确为零

记 R171 的普通主化元为 $\alpha=89460y_{171}+1$，
其中 $(\alpha)=\lambda_0$。
为免与 (257.3) 的生成元混淆，这里给旧变量加下标。
置
$$
 \alpha_{11}=N_{F/M}\alpha
     =\prod_{r=0}^3\sigma^{11r}\alpha.
 \tag{257.12}
$$
它被 $\tau$ 固定，在 $M$ 中生成所选 $q$ 素理想。
在该素点 $\alpha_{11}/q$ 是 $\tau$ 固定的单位，其剩余在
$\mathbf F_q^\times$，所以其 $43$ 次幂剩余符号为零。
其余分支的符号由四项相加得到；把选定分支的上述单位部分记为第 $0$ 项，
完整列表为
$$
 (0,5,25,22,3,31,12,40,21,18,38).
 \tag{257.13}
$$
核验器从 R171 的全部 $44$ 个标记根重新计算这些符号。
用
$$
 e_\psi=\frac1{11}\sum_{j=0}^{10}\widehat\eta^{-j}\sigma^j
$$
得到
$$
 \boxed{
 \frac1{11}\sum_{j=0}^{10}\eta^{-j}
       \ell_j(\alpha_{11}/\text{所选一致化元})=0.}
 \tag{257.14}
$$
在 $44$ 分支原标记下同样有
$\sum_{j=1}^{43}\omega^{8j}\ell(\sigma^j\alpha)=0$。
与之比较，忠实特征的原值为 $32i=2i\lambda_q$，$\lambda_q=16$。
本条没有把这两种特征的斜率混为一谈。

## 5. 素数 2 的主化元与准确射线坐标

证书给出一个完整 $g_2\in H_{11}$，按 (257.3) 的幂基为
$$
 \begin{split}
 43724736\,g_2={}&
 -3796019888+2764038172y+1928955988y^2-1495222240y^3\\
 &-472916468y^4+688291019y^5-130975259y^6\\
 &-44159524y^7+22390248y^8-3736907y^9+1661019y^{10}.
 \end{split}
 \tag{257.15}
$$
标准库核验器检查其首一整多项式恒等式
$$
 \begin{split}
 P_{g_2}(X)={}&X^{11}-42X^{10}+493X^9+11334X^8+61346X^7\\
 &+517292X^6+3516290X^5+8064636X^4+13010525X^3\\
 &+32958X^2+145X-2.
 \end{split}
 \tag{257.16}
$$
由于 $[H_{11}:\mathbf Q]=11$ 为素数且 $g_2$ 非有理，
这就是最小多项式，所以 $g_2$ 整且 $N_{H_{11}/\mathbf Q}g_2=2$。
其主理想是一个范数为 $2$ 的素理想。
程序还独立从乘法/迹计算
$$
 \operatorname{Tr}_{H_{11}/\mathbf Q}(2/g_2^2)=152857/2.
 \tag{257.17}
$$
若该素点在 $2$ 的分歧指数至少为 $2$，则 $2/g_2^2$ 在所有素点整，
其迹应为整数，与 (257.17) 矛盾。
故它恰是 $H_{11}$ 在 $2$ 的唯一 $e=1,f=1$ 素点。
$M/K$ 在 $2$ 完全分裂，而 $K/\mathbf Q$ 在 $2$ 二次分歧，
因此在 $M$ 中
$$
 (g_2)=\mathfrak p_2^2
 \tag{257.18}
$$
且 $\mathfrak p_2$ 被 $\tau$ 固定。
也可直接看 $M/K$ 的射线角色：$\pi=1+i$ 满足 $\pi^2=2i$，
在阶 $11$ 商中 $\pi$ 的 Artin 为一。

现在将 (257.15) 经已核验的两个有理映射代回原 $s,z$ 标记。
在同一个 $q$、同一个 $\zeta$，完整 $11$ 分支的实际符号为
$$
 \ell(\sigma^j g_2)_{j=0}^{10}
       =(0,9,24,8,18,17,26,25,35,19,34).
 \tag{257.19}
$$
这里所有分母都在 $q$ 可逆；程序在各分支同时核对两种幂基表示和
(257.16)，防止有理系数截断造成伪符号。
于是
$$
 \sum_{j=0}^{10}\eta^j\ell(\sigma^jg_2)=22i,\qquad
 \ell(e_\psi g_2)=\frac1{11}\sum_j\eta^{-j}\ell(\sigma^jg_2)
                  =-2i.
 \tag{257.20}
$$
在射线剩余线中用“选定素点的 $e_\psi$ 剩余坐标等于 $1$”
归一化基向量，记其正主理想映射下的像为 $b_0$。
由 (257.18) 和两边同一正 Artin 约定，
$$
 \boxed{e_\psi[\mathfrak p_2]=-i\,b_0\ne0.}
 \tag{257.21}
$$
若只关心分裂性，则 (257.20) 的非零性已经足够；
这里同时保留了除以 $11$ 和除以分歧指数 $2$ 的两个因子。

## 6. 哪个 $S$ 类群非零，哪个消失

令 $\mathfrak q=\prod_{\lambda\mid q}\lambda$，先在 $M$ 的射线类群工作。
由 $\operatorname{Cl}(M)_{43}=0$、$v_{43}(q^2-1)=1$ 以及 §3 的完整
单位像计算，射线正合列给
$$
 e_\psi\operatorname{Cl}_{\mathfrak q}(M)_{43}\simeq k.
 \tag{257.22}
$$
取与 $W_8$ 对应的实际射线类域 $T/M$；
其 Galois 群为加法群 $k$，阶为 $43^2$。
这是整个位于一对共轭特征中的扩张，不是把单条
$k$ 特征线误当成次数 $43$ 的全局扩张。

在所选 $q$ 素点，局部惯性像是一维 $\mathbf F_{43}$ 直线。
(257.14) 说明一致化元的未分歧坐标为零，
故该局部分解群等于惯性群，阶恰为 $43$。
更具体地，$\alpha_{11}/q$ 的局部符号为零，所有其他
$q$ 分支的加权符号和为零；对主元 $\alpha_{11}$ 用互反即得
$q$ 的局部 Artin 为零。

$L_{11}/M$ 在这里也是循环、全 tame 分歧的 $43$ 次扩张，
且 $q$ 是其局部 Norm：
$\tau$ 固定 $q$ 而在 $\Gamma$ 上反演，所以局部 Artin$(q)$
等于其负数，因 $43$ 为奇数而为零。
在 $\mathbf Q_{q^2}$ 上，一个杀一致化元且在剩余单位上非零的
次数 $43$ 角色，其核唯一；因此 $T$ 的上述局部扩张正好等于
$L_{11}$ 的局部扩张。

由于 $C_{11}$ 在 $\operatorname{Gal}(L_{11}/M)$ 上平凡、
在 $\operatorname{Gal}(T/M)$ 上为非平凡 $W_8$ 型，两域在 $M$ 上不交。
所以
$$
 TL_{11}/L_{11}
$$
是次数 $43^2$、处处不分歧且在所有 $q$ 素点完全分裂的扩张。
它也在 $43$ 完全分裂：$M$ 上唯一的 $43$ 素点被 $C_{11}$ 固定，
其在 $T/M$ 中的 Frobenius 必须是 $W_8$ 中的 $C_{11}$ 不变量，故为零；
$L_q/K$ 本来就在 $43$ 分裂。
这证明 (257.2) 第二行及所述明确非零商。

但是它在 $2$ **不**分裂。(257.21) 给出的 Frobenius 非零，
且其 $C_{11}$ 共轭生成整个 $W_8$。
这已经排除了把它冒称为原 $S=\{2,43,q,\infty\}$ 类群商的做法。

现证明原 $S$ 类群的整个 $W_8$ 部分确实消失，而不只是上述商消失。
若该部分非零，取其模 $43$ 对偶，再取 $\Gamma$ 不变量，仍非零。
$C_{11}$ 与 $\Gamma$ 交换；$C_{11}$ 阶与 $43$ 互素，
且 $W_8^{C_{11}}=0$，故
$$
 H^r(C_{11}\times\Gamma,W_8)=0\qquad(r\ge0).
$$
Hochschild--Serre 因而把这个类唯一且非零地下降为 $K$ 上的
$W_8$ 值类。限制到 $M$ 后，它只可能在 $q$ tame 分歧：
$L_{11}/M$ 在其余处不分歧，原类处处不分歧，
而在 $43,2$，$L_q/K$ 分裂且原类还要求完全分裂。
在 $q$，其限制在 $L_{11}$ 为零，故至多有次数 $43$ 的 tame 分歧。
因此该类属于 (257.22) 的射线角色空间。
该空间是单条 $k$ 线，(257.21) 说明每个非零角色在 $2$ 的某个
素点非零；这与原 $S$ 的完全分裂条件矛盾。
所以得到 (257.2) 第三行。

这一步没有计算普通 $\operatorname{Cl}(L_{11})_{43}$ 的全部长度、
$\Gamma$ 作用或上域单位剩余值，也不把它们设为平凡。

## 7. 一个可直接求值的小域 Norm 目标及忠实边界

令
$$
 (c_0,\ldots,c_{10})=(-42,11,-17,2,18,7,7,18,2,-17,11),\qquad
 V_8=\prod_{j=0}^{10}T_j^{c_j}.
 \tag{257.23}
$$
这些整数满足
$$
 \sum c_j=0,\qquad c_{-j}=c_j,\qquad
 c_j=\operatorname{Re}(\eta^j)\pmod{43}.
$$
因此 $V_8$ 是 $H_{11}$ 中的普通单位，其模 $43$ 类仅有
$\psi,\psi^{-1}$ 两个特征。
原 $q$ 的全部 $11$ 个剩余符号为零；在辅助 $859$ 则为
$$
 (0,39,41,3,25,31,12,18,40,2,4),
 \tag{257.24}
$$
所以它不是 $43$ 次幂。
按循环 Hasse Norm 定理，$V_8$ 是 $L_{11}/M$ 的普通元素 Norm。
再用 §6 的原 $S$ 类群消失，逐字按 R201 的除子清支撑及
$43$ 次幂修正论证，可把原像选为普通 $S$ 单位。
最后用 $(x\tau x)^{22}/V_8$，还可选取被 $\tau$ 固定的原像。
这给出了一个明确、非平凡、可在 $11$ 次底域处理的 Norm 目标。
**其上域原像仍未计算；没有把这个存在性写成已经执行的 Norm 求解。**

忠实目标 $U$、$V_{42}$ 属于 $\chi^{\pm1}$。
$L_{11}$ 是 $L$ 的真 $K$ 子域，故来自本条的上域元素，即使未来
实际求出，也不能仅靠乘积和 $43$ 次幂产生忠实 Norm 见证；
R219 后的 faithful-field 边界仍然适用。
本条增加的是小域中的准确单位和支撑/Artin 输入，
不是 $\rho$ 或 $\mathcal L$ 的数值。
忠实目标使用非单位原像时，R200 的外支撑正 Artin 修正仍必须保留。

## 8. 源、证书及实际检查

- §1 两向有理映射、§5 首一整式/非整迹、全部标记有限运算：
  [verify_r257_small_field_ray.py](../scripts/verify_r257_small_field_ray.py)。
- 无条件 $h(H_{11})=1$ 的独立重算：
  [certify_r257_h11_class_number.py](../scripts/certify_r257_h11_class_number.py)，
  需要 CyPari2/PARI；调用的是 §1 明确说明的 flag $1$。
- 完整有理系数、两个有限点、两张 $11\times11$ 矩阵、所有分支符号：
  [r257_small_field_ray_certificate.json](../notes/r257_small_field_ray_certificate.json)。

~~~sh
python scripts/verify_r257_small_field_ray.py \
  notes/r257_small_field_ray_certificate.json \
  notes/small_robert_norm_target_certificate.json \
  notes/r171_principal_norm_selflocal_certificate.json \
  notes/o6_single_real_norm_target_certificate.json
python scripts/certify_r257_h11_class_number.py \
  notes/r257_small_field_ray_certificate.json
~~~

标准库程序明确报告它没有重复 PARI 类数认证；
第二条命令才是该认证的重算入口。
两类检查均保留
`actual_norm_preimage_computed:false`、`actual_L_computed:false`。

引用：

1. PARI/GP 2.17.2, *General number fields*, §§ “Class group, units, and the GRH”、
   “bnfcertify”。flag $1$ 的准确保证见官方手册：
   <https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html#bnfcertify>。
2. K. Rubin, *Elliptic Curves with Complex Multiplication and the Conjecture of
   Birch and Swinnerton-Dyer*, LNM 1716 (1999), §7, Theorem 7.4(iii)；
   这里仅使用原始 $(43)$ 挠点值在 $43$ 外为单位的结论：
   <https://swc-math.github.io/notes/files/99RubinCM.pdf>。
3. R198 §1.1 所列 A. J. Scholl, *An introduction to Kato's Euler systems*,
   Theorem 1.2.1(iii)、Remark(iv) 的准确 isogeny Norm 及奇数度正号：
   <https://www.dpmms.cam.ac.uk/~ajs1005/preprints/euler.pdf>。
4. 循环 Hasse Norm 定理同 R201/R243：J. S. Milne, *Class Field Theory*,
   Chapter VIII, Theorem 3.1；其余类群下降、局部分裂与支撑论证已在上文给出。
